"""
Fix generators for Nextflow-specific gaps.

CONTAINER-001: process has no container directive.
Strategy: prompt the LLM with the process name and script block,
ask it to suggest a pinned public Docker/Biocontainer image,
then insert the directive at the correct position in the source.

CONTAINER-002: container image uses :latest or has no tag.
Strategy: prompt the LLM with the current image name and ask it
to suggest a pinned replacement, then replace the existing line.
"""

from __future__ import annotations

import difflib
import re

from workflow_clinic.core.llm_client import LLMClient
from workflow_clinic.doctor.fix_generators.base import BaseFixGenerator, FixProposal
from workflow_clinic.parsers.nextflow import NextflowParser
from workflow_clinic.schema.gap_report import Gap

# ── Prompt templates ──────────────────────────────────────────────────────────

_CONTAINER_PROMPT = """\
You are a bioinformatics workflow expert. A Nextflow process is missing a container directive.

Process name: {process_name}

Script block:
{script}

Your task: suggest ONE specific, pinned, publicly available Docker image that
provides all the tools used in this script. Prefer Biocontainers or official
tool images. The image must have a specific version tag — never use :latest.

Reply with ONLY the image name and tag on a single line, nothing else.
Example reply: quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8

Image:"""

_PIN_TAG_PROMPT = """\
You are a bioinformatics workflow expert. A Nextflow process uses a container
image with an unpinned or :latest tag which is not reproducible.

Process name: {process_name}
Current image: {current_image}

Your task: suggest the correct pinned version tag for this image.
Reply with ONLY the full image name with a specific version tag, nothing else.
Example reply: quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8

Image:"""

# ── Regexes ───────────────────────────────────────────────────────────────────

_RE_PROCESS_OPEN   = re.compile(r"^\s*process\s+(\w+)\s*\{")
_RE_CONTAINER_LINE = re.compile(r"""^(\s*container\s+)['"](.+?)['"](.*)$""")

# ── TODO (full project): image existence validation ───────────────────────────
# The _validate method below only checks syntactic correctness via the parser.
# It cannot confirm the suggested image actually exists on a registry.
# The full project should add a registry check here, e.g.:
#
#   GET https://biocontainers.pro/api/v1/containers/{tool}/
#   GET https://hub.docker.com/v2/repositories/{image}/tags/{tag}/
#
# A 404 from either API means the image was hallucinated and confidence
# should drop to 0.0 with human_review_required=True.
# ─────────────────────────────────────────────────────────────────────────────


class ContainerMissingFixer(BaseFixGenerator):

    def __init__(self) -> None:
        self._llm    = LLMClient()
        self._parser = NextflowParser()

    def can_fix(self, gap: Gap) -> bool:
        return gap.gap_id == "CONTAINER-001"

    def fix(self, gap: Gap, source_lines: list[str]) -> FixProposal | None:

        # ── Step 1: extract the script block from the gap evidence ────────────
        script_text = self._extract_script(gap, source_lines)

        # ── Step 2: ask the LLM for a container image ─────────────────────────
        prompt = _CONTAINER_PROMPT.format(
            process_name=gap.process_name,
            script=script_text or "(script block not available)",
        )
        try:
            raw   = self._llm.complete(prompt).strip().strip("'\"")
            image = self._clean_image_response(raw)
        except Exception as exc:
            return FixProposal(
                gap_id=gap.gap_id,
                process_name=gap.process_name,
                description="LLM call failed — cannot suggest container image.",
                unified_diff="",
                validation_passed=False,
                validation_output=str(exc),
                confidence=0.0,
                human_review_required=True,
            )

        # ── Step 3: insert the container directive ────────────────────────────
        patched_lines = self._insert_container(
            source_lines, gap.process_name, image
        )
        if patched_lines is None:
            return FixProposal(
                gap_id=gap.gap_id,
                process_name=gap.process_name,
                description="Could not locate process block in source to apply fix.",
                unified_diff="",
                validation_passed=False,
                validation_output="Process block not found.",
                confidence=0.0,
                human_review_required=True,
            )

        # ── Step 4: build unified diff ────────────────────────────────────────
        diff = "".join(difflib.unified_diff(
            source_lines,
            patched_lines,
            fromfile=f"{gap.process_name} (original)",
            tofile=f"{gap.process_name} (fixed)",
            lineterm="\n",
        ))

        # ── Step 5: validate — re-parse patched source and check ──────────────
        patched_source = "".join(patched_lines)
        validation_passed, validation_output = self._validate(
            patched_source, gap.process_name, image
        )

        return FixProposal(
            gap_id=gap.gap_id,
            process_name=gap.process_name,
            description=f"Add container directive: '{image}'",
            unified_diff=diff,
            validation_passed=validation_passed,
            validation_output=validation_output,
            confidence=0.85 if validation_passed else 0.4,
            human_review_required=not validation_passed,
            patched_content=patched_source,   # ← Day 9: stored for --create-pr
        )

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _clean_image_response(self, raw: str) -> str:
        """
        Extract the first plausible image:tag token from an LLM response.
        Smaller models often add prose around the answer — this strips it.

        Strategy: take the first non-empty line, then find the first
        whitespace-delimited token that looks like image:tag (contains both
        a colon and a slash). Falls back to the cleaned first line if nothing
        matches.
        """
        first_line = next(
            (line.strip() for line in raw.splitlines() if line.strip()),
            raw.strip(),
        )

        for token in first_line.split():
            token = token.strip("',\"")
            if ":" in token and "/" in token:
                return token

        return first_line.strip("',\"")

    def _extract_script(self, gap: Gap, source_lines: list[str]) -> str:
        """Pull the script block lines for the relevant process."""
        start = gap.location.line_start - 1
        end   = gap.location.line_end
        block = source_lines[start:end]
        in_script   = False
        script_lines: list[str] = []
        for line in block:
            if re.match(r"^\s*(script|shell|exec)\s*:\s*$", line):
                in_script = True
                continue
            if in_script:
                script_lines.append(line)
        return "".join(script_lines).strip()

    def _insert_container(
        self,
        source_lines: list[str],
        process_name: str,
        image: str,
    ) -> list[str] | None:
        """
        Find the opening brace of the named process and insert
        a container directive on the very next line.
        """
        patched = list(source_lines)
        for i, line in enumerate(patched):
            m = _RE_PROCESS_OPEN.match(line)
            if m and m.group(1) == process_name:
                indent = "    "
                for j in range(i + 1, min(i + 5, len(patched))):
                    stripped = patched[j].lstrip()
                    if stripped:
                        indent = patched[j][: len(patched[j]) - len(stripped)]
                        break
                directive = f"{indent}container '{image}'\n"
                patched.insert(i + 1, directive)
                return patched
        return None

    def _validate(
        self,
        patched_source: str,
        process_name: str,
        image: str,
    ) -> tuple[bool, str]:
        """
        Re-parse the patched source and verify the container directive
        is now present with the expected image.
        """
        try:
            workflow = self._parser.parse(patched_source)
            proc = next(
                (p for p in workflow.processes if p.name == process_name),
                None,
            )
            if proc is None:
                return False, "Process not found after patching."
            if proc.container != image:
                return False, (
                    f"Container directive present but value mismatch: "
                    f"expected '{image}', got '{proc.container}'."
                )
            return True, "Parser confirmed container directive is present."
        except Exception as exc:
            return False, f"Validation error: {exc}"


class ContainerLatestTagFixer(BaseFixGenerator):

    def __init__(self) -> None:
        self._llm    = LLMClient()
        self._parser = NextflowParser()

    def can_fix(self, gap: Gap) -> bool:
        return gap.gap_id == "CONTAINER-002"

    def fix(self, gap: Gap, source_lines: list[str]) -> FixProposal | None:

        # ── Step 1: ask LLM for a pinned replacement ──────────────────────────
        current_image = gap.evidence.replace("container '", "").strip("'")
        prompt = _PIN_TAG_PROMPT.format(
            process_name=gap.process_name,
            current_image=current_image,
        )
        try:
            raw   = self._llm.complete(prompt).strip().strip("'\"")
            image = ContainerMissingFixer().__class__._clean_image_response(
                ContainerMissingFixer(), raw
            )
        except Exception as exc:
            return FixProposal(
                gap_id=gap.gap_id,
                process_name=gap.process_name,
                description="LLM call failed — cannot suggest pinned image.",
                unified_diff="",
                validation_passed=False,
                validation_output=str(exc),
                confidence=0.0,
                human_review_required=True,
                patched_content="",  # ← Day 9: stored for --create-pr
            )

        # ── Step 2: replace the container line in source ──────────────────────
        patched            = list(source_lines)
        replaced           = False
        in_target_process  = False
        depth              = 0

        for i, line in enumerate(patched):
            m_proc = _RE_PROCESS_OPEN.match(line)
            if m_proc:
                in_target_process = (m_proc.group(1) == gap.process_name)
                depth = 0

            if in_target_process:
                depth += line.count("{") - line.count("}")
                if depth <= 0 and i > 0:
                    in_target_process = False
                    continue
                m_cont = _RE_CONTAINER_LINE.match(line)
                if m_cont:
                    patched[i] = f"{m_cont.group(1)}'{image}'{m_cont.group(3)}\n"
                    replaced   = True
                    break

        if not replaced:
            return FixProposal(
                gap_id=gap.gap_id,
                process_name=gap.process_name,
                description="Could not locate container line to replace.",
                unified_diff="",
                validation_passed=False,
                validation_output="Container line not found.",
                confidence=0.0,
                human_review_required=True,
            )

        # ── Step 3: diff ──────────────────────────────────────────────────────
        diff = "".join(difflib.unified_diff(
            source_lines,
            patched,
            fromfile=f"{gap.process_name} (original)",
            tofile=f"{gap.process_name} (fixed)",
            lineterm="\n",
        ))

        # ── Step 4: validate ──────────────────────────────────────────────────
        try:
            workflow = self._parser.parse("".join(patched))
            proc = next(
                (p for p in workflow.processes if p.name == gap.process_name),
                None,
            )
            if proc and proc.container == image:
                validation_passed = True
                validation_output = "Parser confirmed updated container tag."
            else:
                validation_passed = False
                validation_output = (
                    f"Value mismatch after patch: "
                    f"got '{proc.container if proc else None}'."
                )
        except Exception as exc:
            validation_passed = False
            validation_output = f"Validation error: {exc}"

        return FixProposal(
            gap_id=gap.gap_id,
            process_name=gap.process_name,
            description=f"Pin container tag: '{current_image}' → '{image}'",
            unified_diff=diff,
            validation_passed=validation_passed,
            validation_output=validation_output,
            confidence=0.85 if validation_passed else 0.4,
            human_review_required=not validation_passed,
        )
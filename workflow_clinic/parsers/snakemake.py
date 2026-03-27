"""
Snakemake parser — extracts rule blocks and their directives.

Maps Snakemake-specific directives to the shared NextflowProcess dataclass
so every existing Critic rule runs unchanged against Snakemake workflows:

  singularity: / container:  →  process.container
  conda:                      →  process.conda
  threads:                    →  process.cpus
  resources: mem_mb / mem_gb  →  process.memory
  input:                      →  process.input   (DirectiveBlock)
  output:                     →  process.output  (DirectiveBlock)
  shell: / run: / script:     →  process.script  (DirectiveBlock)

Design: indentation-based rather than brace-based (unlike Nextflow).
A rule block starts at column 0 with `rule NAME:` and ends when the next
non-empty, non-comment line returns to column 0.  Section keywords sit at
indent-level-1 (usually 4 spaces); section content at indent-level-2+.

Limitations (acceptable for the POC):
  - `use rule ... as ... with:` (rule reuse) is not parsed.
  - `module` blocks (DSL v6+) are not parsed.
  - `checkpoint` blocks are parsed identically to `rule` blocks.
  - threads / resource values must be integer literals, not expressions.
"""

from __future__ import annotations

import re
from pathlib import Path

from workflow_clinic.parsers.nextflow import (
    DirectiveBlock,
    NextflowProcess,
    ParsedWorkflow,
)

# ── Regexes ───────────────────────────────────────────────────────────────────

# Rule / checkpoint start (must be at column 0)
_RE_RULE_START       = re.compile(r"^rule\s+(\w+)\s*:\s*(?:#.*)?$")
_RE_CHECKPOINT_START = re.compile(r"^checkpoint\s+(\w+)\s*:\s*(?:#.*)?$")

# singularity / container — both Snakemake keyword spellings
_RE_SINGULARITY_INLINE = re.compile(
    r"""^\s+(?:singularity|container):\s+['"](.+?)['"]\s*(?:#.*)?$"""
)
_RE_SINGULARITY_SECTION = re.compile(
    r"^\s+(?:singularity|container):\s*(?:#.*)?$"
)

# conda
_RE_CONDA_INLINE   = re.compile(r"""^\s+conda:\s+['"](.+?)['"]\s*(?:#.*)?$""")
_RE_CONDA_SECTION  = re.compile(r"^\s+conda:\s*(?:#.*)?$")

# threads: N  (integer literal only)
_RE_THREADS = re.compile(r"^\s+threads:\s+(\d+)\s*(?:#.*)?$")

# resources section content
_RE_MEM_MB   = re.compile(r"^\s+mem_mb\s*[=:]\s*(\d+)")
_RE_MEM_GB   = re.compile(r"^\s+mem_gb\s*[=:]\s*(\d+)")
_RE_RES_CPUS = re.compile(r"^\s+cpus\s*[=:]\s*(\d+)")

# Any section keyword at indentation level ≥ 1 with nothing after the colon
# (except optional trailing whitespace / comment).
# Note: singularity, conda, and threads are listed here as a safety net —
# the more specific patterns above are always checked first.
_RE_SECTION_HEADER = re.compile(
    r"^\s+"
    r"(input|output|shell|run|script|params|log|benchmark|resources|"
    r"singularity|container|conda|threads|wildcard_constraints|envmodules|"
    r"wrapper|notebook|cache|priority|group|message|shadow|cwl|version)"
    r"\s*:\s*(?:#.*)?$"
)

# A quoted string value at indent level ≥ 2 — used for multi-line
# singularity: / conda: where the value sits on the line below the keyword.
_RE_QUOTED_VALUE = re.compile(r"""^\s+['"](.+?)['"]\s*(?:#.*)?$""")


# ── Parser ────────────────────────────────────────────────────────────────────

class SnakemakeParser:
    """
    Line-by-line state machine parser for Snakemake `.smk` files.

    Iterates through the file, detects `rule` (or `checkpoint`) blocks,
    and extracts each into a `NextflowProcess` object so the CriticEngine
    and all registered rules can operate without modification.
    """

    def parse(
        self, source: str, path: Path = Path("unknown.smk")
    ) -> ParsedWorkflow:
        lines  = source.splitlines()
        workflow = ParsedWorkflow(path=path)

        i = 0
        while i < len(lines):
            line = lines[i]
            m = _RE_RULE_START.match(line) or _RE_CHECKPOINT_START.match(line)
            if m:
                rule, i = self._parse_rule(m.group(1), lines, i)
                workflow.processes.append(rule)
            else:
                i += 1

        return workflow

    def parse_file(self, path: Path) -> ParsedWorkflow:
        return self.parse(path.read_text(encoding="utf-8"), path=path)

    # ── Internal ──────────────────────────────────────────────────────────────

    def _parse_rule(
        self, name: str, lines: list[str], start: int
    ) -> tuple[NextflowProcess, int]:
        proc = NextflowProcess(
            name=name, line_start=start + 1, line_end=start + 1
        )
        current_section:    str | None = None
        awaiting_string_for: str | None = None  # "singularity" | "conda"
        i = start + 1

        while i < len(lines):
            line    = lines[i]
            stripped = line.strip()

            # ── Blank lines ───────────────────────────────────────────────────
            if not stripped:
                # Preserve blank lines inside script blocks (shell / run)
                if current_section == "script":
                    proc.script.lines.append(line)
                i += 1
                continue

            # ── Comment-only lines ────────────────────────────────────────────
            if stripped.startswith("#"):
                i += 1
                continue

            # ── End of rule: non-indented, non-empty line ─────────────────────
            if line[0] not in (" ", "\t"):
                proc.line_end = i
                return proc, i

            # ── Pending multi-line singularity / conda value ──────────────────
            if awaiting_string_for is not None:
                m = _RE_QUOTED_VALUE.match(line)
                if m:
                    if awaiting_string_for == "singularity":
                        proc.container = m.group(1)
                    elif awaiting_string_for == "conda":
                        proc.conda = m.group(1)
                    awaiting_string_for = None
                    i += 1
                    continue
                else:
                    # Not a quoted value — reset and fall through so this
                    # line is processed normally (e.g. it's a new section).
                    awaiting_string_for = None

            # ── singularity / container — inline ─────────────────────────────
            m = _RE_SINGULARITY_INLINE.match(line)
            if m:
                proc.container  = m.group(1)
                current_section = None
                i += 1
                continue

            # ── singularity / container — section style ───────────────────────
            if _RE_SINGULARITY_SECTION.match(line):
                awaiting_string_for = "singularity"
                current_section     = None
                i += 1
                continue

            # ── conda — inline ────────────────────────────────────────────────
            m = _RE_CONDA_INLINE.match(line)
            if m:
                proc.conda      = m.group(1)
                current_section = None
                i += 1
                continue

            # ── conda — section style ─────────────────────────────────────────
            if _RE_CONDA_SECTION.match(line):
                awaiting_string_for = "conda"
                current_section     = None
                i += 1
                continue

            # ── threads: N ────────────────────────────────────────────────────
            m = _RE_THREADS.match(line)
            if m:
                proc.cpus       = m.group(1)
                current_section = None
                i += 1
                continue

            # ── Generic section header ────────────────────────────────────────
            m = _RE_SECTION_HEADER.match(line)
            if m:
                sname = m.group(1)
                if sname in ("input", "output"):
                    current_section = sname
                elif sname in ("shell", "run", "script"):
                    current_section = "script"
                elif sname == "resources":
                    current_section = "resources"
                else:
                    current_section = None
                i += 1
                continue

            # ── Section body content ──────────────────────────────────────────
            if current_section == "resources":
                mm = _RE_MEM_MB.match(line)
                if mm:
                    proc.memory = f"{mm.group(1)} MB"
                mg = _RE_MEM_GB.match(line)
                if mg:
                    proc.memory = f"{int(mg.group(1)) * 1024} MB"
                mc = _RE_RES_CPUS.match(line)
                if mc and proc.cpus is None:   # threads: takes priority
                    proc.cpus = mc.group(1)

            elif current_section in ("input", "output"):
                block: DirectiveBlock = getattr(proc, current_section)
                block.lines.append(line)

            elif current_section == "script":
                proc.script.lines.append(line)

            i += 1

        # EOF reached inside a rule block — return what we have
        proc.line_end = i
        return proc, i
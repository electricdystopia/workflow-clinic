"""
Nextflow DSL2 parser — extracts process blocks and their directives.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


# ── Data models ──────────────────────────────────────────────────────────────

@dataclass
class DirectiveBlock:
    """Raw content of a multi-line directive (input, output, script)."""
    lines: list[str] = field(default_factory=list)

    @property
    def raw(self) -> str:
        return "\n".join(self.lines).strip()


@dataclass
class NextflowProcess:
    name: str
    line_start: int
    line_end: int
    container: str | None = None
    cpus: str | None = None
    memory: str | None = None
    # Added in Day 8: populated by SnakemakeParser for `conda:` directives.
    # Always None for Nextflow processes — existing rules are unaffected.
    conda: str | None = None
    input: DirectiveBlock = field(default_factory=DirectiveBlock)
    output: DirectiveBlock = field(default_factory=DirectiveBlock)
    script: DirectiveBlock = field(default_factory=DirectiveBlock)

    def directives_found(self) -> list[str]:
        found = []
        if self.container:
            found.append("container")
        if self.cpus:
            found.append("cpus")
        if self.memory:
            found.append("memory")
        if self.conda:                  # Day 8: conda is a first-class directive
            found.append("conda")
        if self.input.raw:
            found.append("input")
        if self.output.raw:
            found.append("output")
        if self.script.raw:
            found.append("script")
        return found


@dataclass
class ParsedWorkflow:
    path: Path
    processes: list[NextflowProcess] = field(default_factory=list)


# ── Regexes ───────────────────────────────────────────────────────────────────

_RE_PROCESS_START = re.compile(r"^\s*process\s+(\w+)\s*\{")
_RE_CONTAINER     = re.compile(r"""^\s*container\s+['"](.+?)['"]\s*(?://.*)?$""")
_RE_CPUS          = re.compile(r"^\s*cpus\s+(.+?)\s*(?://.*)?$")
_RE_MEMORY        = re.compile(r"^\s*memory\s+(.+?)\s*(?://.*)?$")
_RE_INPUT_START   = re.compile(r"^\s*input\s*:\s*$")
_RE_OUTPUT_START  = re.compile(r"^\s*output\s*:\s*$")
_RE_SCRIPT_START  = re.compile(r"^\s*(script|shell|exec)\s*:\s*$")
_RE_SECTION_START = re.compile(
    r"^\s*(input|output|script|shell|exec|when|stub)\s*:\s*$"
)


# ── Parser ────────────────────────────────────────────────────────────────────

class NextflowParser:
    """
    Line-by-line state machine parser for Nextflow DSL2 `.nf` files.
    Extracts all process blocks and their key directives.
    """

    def parse(self, source: str, path: Path = Path("unknown.nf")) -> ParsedWorkflow:
        lines = source.splitlines()
        workflow = ParsedWorkflow(path=path)

        i = 0
        while i < len(lines):
            m = _RE_PROCESS_START.match(lines[i])
            if m:
                process, i = self._parse_process(m.group(1), lines, i)
                workflow.processes.append(process)
            else:
                i += 1

        return workflow

    def parse_file(self, path: Path) -> ParsedWorkflow:
        return self.parse(path.read_text(encoding="utf-8"), path=path)

    # ── Internal ──────────────────────────────────────────────────────────────

    def _parse_process(
        self, name: str, lines: list[str], start: int
    ) -> tuple[NextflowProcess, int]:
        proc = NextflowProcess(name=name, line_start=start + 1, line_end=start + 1)
        depth = 0
        current_section: str | None = None
        i = start

        while i < len(lines):
            line = lines[i]
            depth += line.count("{") - line.count("}")

            if depth <= 0 and i > start:
                proc.line_end = i + 1
                return proc, i + 1

            if m := _RE_CONTAINER.match(line):
                proc.container = m.group(1)
                current_section = None
            elif m := _RE_CPUS.match(line):
                proc.cpus = m.group(1)
                current_section = None
            elif m := _RE_MEMORY.match(line):
                proc.memory = m.group(1)
                current_section = None
            elif _RE_INPUT_START.match(line):
                current_section = "input"
            elif _RE_OUTPUT_START.match(line):
                current_section = "output"
            elif _RE_SCRIPT_START.match(line):
                current_section = "script"
            elif _RE_SECTION_START.match(line) and i > start:
                current_section = None
            elif current_section and line.strip():
                block = getattr(proc, current_section)
                block.lines.append(line)

            i += 1

        proc.line_end = i
        return proc, i
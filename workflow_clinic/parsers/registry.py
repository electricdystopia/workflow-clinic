"""
ParserRegistry — maps workflow file extensions to the correct parser instance.

This is a factory that mirrors the rule-registry pattern in the Critic: a
single lookup table where adding a new language requires only one new entry
and a corresponding parser implementation — nothing else changes.

Supported languages (Day 8):
  .nf                    → NextflowParser
  .smk / .snakefile      → SnakemakeParser
  Snakefile (bare name)  → SnakemakeParser

Unrecognised extensions fall back to NextflowParser to preserve the Day 1–7
behaviour for files passed directly to the CLI without an extension.
"""

from __future__ import annotations

from pathlib import Path

from workflow_clinic.parsers.nextflow import NextflowParser
from workflow_clinic.parsers.snakemake import SnakemakeParser

# Type alias for all supported parsers — extend as new languages are added
WorkflowParser = NextflowParser | SnakemakeParser

# ── Extension → parser class ──────────────────────────────────────────────────

_EXT_PARSERS: dict[str, type[WorkflowParser]] = {
    ".nf":        NextflowParser,
    ".smk":       SnakemakeParser,
    ".snakefile": SnakemakeParser,
}

# Bare filenames that have no extension (case-insensitive)
_NAME_PARSERS: dict[str, type[WorkflowParser]] = {
    "snakefile":    SnakemakeParser,
    "snakefile.py": SnakemakeParser,  # unusual but valid
}


class ParserRegistry:
    """
    Factory that resolves a workflow file path to the correct parser.

    Usage::

        parser   = ParserRegistry().get_parser(Path("align.smk"))
        workflow = parser.parse_file(Path("align.smk"))
    """

    def get_parser(self, path: Path) -> WorkflowParser:
        """
        Return the appropriate parser instance for *path*.

        Resolution order:
        1. Bare filename match (e.g. ``Snakefile``, ``Snakefile.py``)
        2. File extension match (``.nf``, ``.smk``, ``.snakefile``)
        3. Default: NextflowParser (preserves pre-Day-8 behaviour)
        """
        # 1. Bare filename (covers files named exactly "Snakefile")
        if path.name.lower() in _NAME_PARSERS:
            return _NAME_PARSERS[path.name.lower()]()

        # 2. Extension-based routing
        ext = path.suffix.lower()
        parser_cls = _EXT_PARSERS.get(ext, NextflowParser)
        return parser_cls()
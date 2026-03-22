"""
Pydantic models for the Workflow Clinic gap report.
These are the core data structures that cross module boundaries —
the parser produces NextflowProcess objects, the rule engine
consumes them and produces these.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel


class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    MAJOR    = "MAJOR"
    MINOR    = "MINOR"
    INFO     = "INFO"


class GapCategory(str, Enum):
    CONTAINERIZATION = "containerization"
    STORAGE          = "storage"
    IO_DECLARATION   = "io_declaration"
    RESOURCE_HINTS   = "resource_hints"
    REPRODUCIBILITY  = "reproducibility"
    METADATA         = "metadata"


class CodeLocation(BaseModel):
    file: str
    line_start: int
    line_end: int


class Gap(BaseModel):
    gap_id: str                 # e.g. "CONTAINER-001"
    process_name: str           # which process triggered this
    category: GapCategory
    severity: Severity
    location: CodeLocation
    description: str            # human-readable explanation
    evidence: str               # the offending line(s) or empty string
    recommendation: str         # what to do about it
    auto_fixable: bool = False  # Day 3+ — whether the Doctor can attempt a fix


class GapSummary(BaseModel):
    total_gaps: int
    critical: int
    major: int
    minor: int
    info: int
    auto_fixable_count: int
    cloud_readiness_score: float   # 0.0 – 1.0, computed from gaps


class GapReport(BaseModel):
    schema_version: str = "0.1.0"
    generated_at: datetime
    workflow_path: str
    gaps: list[Gap]
    summary: GapSummary
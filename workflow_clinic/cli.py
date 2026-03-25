"""
Workflow Clinic CLI — entry point for all commands.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich import box

from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.parsers.nextflow import NextflowParser
from workflow_clinic.schema.gap_report import GapReport, Severity

from workflow_clinic.doctor.engine import DoctorEngine
from workflow_clinic.doctor.fix_generators.base import FixProposal
from datetime import datetime, timezone

import dataclasses

app = typer.Typer(
    help="Workflow Clinic — cloud-readiness tools for bioinformatics workflows.",
    no_args_is_help=True,
)
console = Console()
err_console = Console(stderr=True)


# ── Output format enum ────────────────────────────────────────────────────────

class OutputFormat(str, Enum):
    terminal = "terminal"
    json     = "json"
    markdown = "markdown"


# ── Severity colours for rich ─────────────────────────────────────────────────

_SEVERITY_COLOUR = {
    Severity.CRITICAL: "bold red",
    Severity.MAJOR:    "yellow",
    Severity.MINOR:    "cyan",
    Severity.INFO:     "dim",
}


# ── parse command (from Day 1) ────────────────────────────────────────────────

@app.command("parse")
def parse(
    path: Path = typer.Argument(..., help="Path to a .nf workflow file"),
) -> None:
    """Parse a Nextflow workflow and list all processes with their detected directives."""
    if not path.exists():
        err_console.print(f"[red]File not found:[/red] {path}")
        raise typer.Exit(1)

    parser = NextflowParser()
    workflow = parser.parse_file(path)

    if not workflow.processes:
        console.print("[yellow]No processes found in workflow.[/yellow]")
        raise typer.Exit(0)

    console.print(f"\n[bold cyan]Workflow:[/bold cyan] {path}")
    console.print(f"[bold]Processes found:[/bold] {len(workflow.processes)}\n")

    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("Process", style="cyan")
    table.add_column("Lines")
    table.add_column("container")
    table.add_column("cpus")
    table.add_column("memory")
    table.add_column("input")
    table.add_column("output")
    table.add_column("script")

    def tick(val: object) -> str:
        return "[green]✓[/green]" if val else "[red]✗[/red]"

    for p in workflow.processes:
        table.add_row(
            p.name,
            f"{p.line_start}–{p.line_end}",
            tick(p.container),
            tick(p.cpus),
            tick(p.memory),
            tick(p.input.raw),
            tick(p.output.raw),
            tick(p.script.raw),
        )

    console.print(table)


# ── critic command ────────────────────────────────────────────────────────────

@app.command("critic")
def critic(
    source: str = typer.Argument(
        ...,
        help=(
            "Path to a .nf file, or a remote source:\n\n"
            "  dockstore:github.com/owner/repo\n\n"
            "  https://github.com/owner/repo"
        ),
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.terminal,
        "--format", "-f",
        help="Output format: terminal (default), json, or markdown.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output", "-o",
        help="Save the report to this file instead of printing to stdout.",
    ),
    score: bool = typer.Option(
        False,
        "--score",
        help="Print only the cloud readiness score (0.0–1.0) and exit.",
    ),
) -> None:
    """Analyse a Nextflow workflow and report cloud-readiness gaps."""

    # ── Resolve source → ParsedWorkflow ──────────────────────────────────────
    # Local file path
    if not any(source.startswith(p) for p in ("dockstore:", "github:", "https://")):
        path = Path(source)
        if not path.exists():
            err_console.print(f"[red]File not found:[/red] {path}")
            raise typer.Exit(1)
        workflow = NextflowParser().parse_file(path)
        display_path = path

    # Remote source — fetch then parse from string
    else:
        from workflow_clinic.core.fetcher import fetch
        try:
            # full_repo=True fetches all .nf files — needed for nf-core DSL2
            fetched = fetch(source, full_repo=True)
        except Exception as exc:
            err_console.print(f"[red]Fetch failed:[/red] {exc}")
            raise typer.Exit(1)
        workflow     = NextflowParser().parse(fetched.content, Path(fetched.filename))
        display_path = Path(fetched.filename)
        console.print(
            f"[dim]Fetched {len(fetched.files)} .nf file(s) "
            f"from {fetched.source}[/dim]\n"
        )

    # ── Run engine ────────────────────────────────────────────────────────────
    report = CriticEngine().run(workflow)

    # ── --score shortcut ──────────────────────────────────────────────────────
    if score:
        console.print(report.summary.cloud_readiness_score)
        raise typer.Exit(0)

    # ── Render ────────────────────────────────────────────────────────────────
    if format == OutputFormat.json:
        rendered = _render_json(report)
    elif format == OutputFormat.markdown:
        rendered = _render_markdown(report)
    else:
        _render_terminal(report, display_path)
        if output:
            output.write_text(_render_markdown(report), encoding="utf-8")
            console.print(f"\n[dim]Report saved to {output}[/dim]")
        return

    # ── Write or print ────────────────────────────────────────────────────────
    if output:
        output.write_text(rendered, encoding="utf-8")
        console.print(f"[dim]Report saved to {output}[/dim]")
    else:
        if format == OutputFormat.markdown:
            console.print(Markdown(rendered))
        else:
            typer.echo(rendered)

# ── Renderers ─────────────────────────────────────────────────────────────────

def _render_terminal(report: GapReport, path: Path) -> None:
    """Rich-formatted terminal output with colour-coded severity."""
    s = report.summary

    # ── Header ────────────────────────────────────────────────────────────────
    console.rule("[bold cyan]Workflow Clinic — Gap Report[/bold cyan]")
    console.print(f"[bold]Workflow:[/bold]  {path}")
    console.print(f"[bold]Processes:[/bold] {len(set(g.process_name for g in report.gaps or []))}")
    console.print()

    # ── Score ─────────────────────────────────────────────────────────────────
    score = s.cloud_readiness_score
    score_colour = "green" if score >= 0.8 else "yellow" if score >= 0.5 else "red"
    console.print(
        f"[bold]Cloud Readiness Score:[/bold] "
        f"[{score_colour}]{score:.2f} / 1.00[/{score_colour}]"
    )
    console.print()

    # ── Summary counts ────────────────────────────────────────────────────────
    summary_table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    summary_table.add_column("label", style="bold")
    summary_table.add_column("value")
    summary_table.add_row("Total gaps",    str(s.total_gaps))
    summary_table.add_row("[bold red]Critical[/bold red]", str(s.critical))
    summary_table.add_row("[yellow]Major[/yellow]",        str(s.major))
    summary_table.add_row("[cyan]Minor[/cyan]",            str(s.minor))
    summary_table.add_row("[dim]Info[/dim]",               str(s.info))
    summary_table.add_row("Auto-fixable",  str(s.auto_fixable_count))
    console.print(summary_table)

    if not report.gaps:
        console.print("[bold green]✓ No gaps found — workflow is cloud-ready![/bold green]")
        return

    # ── Gap table ─────────────────────────────────────────────────────────────
    console.rule("[bold]Gaps[/bold]")
    gap_table = Table(
        show_header=True,
        header_style="bold magenta",
        box=box.ROUNDED,
        expand=True,
    )
    gap_table.add_column("ID",       style="bold", no_wrap=True)
    gap_table.add_column("Severity", no_wrap=True)
    gap_table.add_column("Process",  style="cyan")
    gap_table.add_column("Category")
    gap_table.add_column("Lines",    no_wrap=True)
    gap_table.add_column("Auto-fix", no_wrap=True)

    for g in report.gaps:
        colour = _SEVERITY_COLOUR[g.severity]
        gap_table.add_row(
            g.gap_id,
            f"[{colour}]{g.severity.value}[/{colour}]",
            g.process_name,
            g.category.value,
            f"{g.location.line_start}–{g.location.line_end}",
            "[green]✓[/green]" if g.auto_fixable else "[red]✗[/red]",
        )

    console.print(gap_table)

    # ── Per-gap detail ────────────────────────────────────────────────────────
    console.rule("[bold]Detail[/bold]")
    for g in report.gaps:
        colour = _SEVERITY_COLOUR[g.severity]
        console.print(
            f"\n[bold]{g.gap_id}[/bold] "
            f"[{colour}]{g.severity.value}[/{colour}] "
            f"— [cyan]{g.process_name}[/cyan] "
            f"(line {g.location.line_start}–{g.location.line_end})"
        )
        console.print(f"  [bold]Description:[/bold] {g.description}")
        if g.evidence:
            console.print(f"  [bold]Evidence:[/bold]    [italic]{g.evidence}[/italic]")
        console.print(f"  [bold]Fix:[/bold]         {g.recommendation}")


def _render_json(report: GapReport) -> str:
    return json.dumps(report.model_dump(mode="json"), indent=2)


def _render_markdown(report: GapReport) -> str:
    s = report.summary
    lines: list[str] = []

    lines.append("# Workflow Clinic — Gap Report\n")
    lines.append(f"**Workflow:** `{report.workflow_path}`  ")
    lines.append(f"**Generated:** {report.generated_at.strftime('%Y-%m-%d %H:%M UTC')}  ")
    lines.append(f"**Schema version:** {report.schema_version}\n")

    lines.append("## Summary\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Cloud Readiness Score | **{s.cloud_readiness_score:.2f} / 1.00** |")
    lines.append(f"| Total Gaps | {s.total_gaps} |")
    lines.append(f"| Critical | {s.critical} |")
    lines.append(f"| Major | {s.major} |")
    lines.append(f"| Minor | {s.minor} |")
    lines.append(f"| Info | {s.info} |")
    lines.append(f"| Auto-fixable | {s.auto_fixable_count} |\n")

    if not report.gaps:
        lines.append("✅ **No gaps found — workflow is cloud-ready!**\n")
        return "\n".join(lines)

    lines.append("## Gaps\n")
    lines.append("| ID | Severity | Process | Category | Lines | Auto-fix |")
    lines.append("|---|---|---|---|---|---|")
    for g in report.gaps:
        fix = "✓" if g.auto_fixable else "✗"
        lines.append(
            f"| {g.gap_id} | {g.severity.value} | `{g.process_name}` "
            f"| {g.category.value} | {g.location.line_start}–{g.location.line_end} | {fix} |"
        )

    lines.append("\n## Detail\n")
    for g in report.gaps:
        lines.append(f"### {g.gap_id} — {g.process_name}\n")
        lines.append(f"**Severity:** {g.severity.value}  ")
        lines.append(f"**Category:** {g.category.value}  ")
        lines.append(f"**Lines:** {g.location.line_start}–{g.location.line_end}\n")
        lines.append(f"**Description:** {g.description}\n")
        if g.evidence:
            lines.append(f"**Evidence:**\n```\n{g.evidence}\n```\n")
        lines.append(f"**Recommendation:** {g.recommendation}\n")
        lines.append("---\n")

    return "\n".join(lines)

@app.command("doctor")
def doctor(
    path: Path = typer.Argument(..., help="Path to a .nf workflow file"),
    gap: str | None = typer.Option(
        None,
        "--gap", "-g",
        help="Only fix gaps with this ID, e.g. CONTAINER-001.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output", "-o",
        help="Save fix proposals as JSON to this file.",
    ),
) -> None:
    """Generate fixes for auto-fixable gaps in a Nextflow workflow."""
    if not path.exists():
        err_console.print(f"[red]File not found:[/red] {path}")
        raise typer.Exit(1)
 
    source       = path.read_text(encoding="utf-8")
    source_lines = source.splitlines(keepends=True)
    workflow     = NextflowParser().parse_file(path)
    report       = CriticEngine().run(workflow)
 
    # filter to requested gap_id if provided
    if gap:
        filtered_gaps = [g for g in report.gaps if g.gap_id == gap]
        if not filtered_gaps:
            console.print(f"[yellow]No gaps with ID '{gap}' found in report.[/yellow]")
            raise typer.Exit(0)
        report = report.model_copy(update={"gaps": filtered_gaps})
 
    auto_fixable = [g for g in report.gaps if g.auto_fixable]
    if not auto_fixable:
        console.print("[yellow]No auto-fixable gaps found.[/yellow]")
        raise typer.Exit(0)
 
    console.print(f"\n[bold cyan]Workflow Doctor[/bold cyan] — {path}")
    console.print(f"[dim]Auto-fixable gaps: {len(auto_fixable)}[/dim]\n")
 
    proposals = DoctorEngine().run(report, source_lines)
 
    if not proposals:
        console.print("[yellow]No fixes could be generated.[/yellow]")
        raise typer.Exit(0)
 
    # ── Save to file if --output given ────────────────────────────────────────
    if output:
        rendered = _render_doctor_json(proposals, path)
        output.write_text(rendered, encoding="utf-8")
        console.print(f"[dim]Fix proposals saved to {output}[/dim]\n")
 
    # ── Always print to terminal ──────────────────────────────────────────────
    for proposal in proposals:
        colour = "green" if proposal.validation_passed else "yellow"
        console.rule(
            f"[bold]{proposal.gap_id}[/bold] — [cyan]{proposal.process_name}[/cyan]"
        )
        console.print(f"[bold]Fix:[/bold]        {proposal.description}")
        console.print(
            f"[bold]Confidence:[/bold] [{colour}]{proposal.confidence:.0%}[/{colour}]"
        )
        console.print(
            f"[bold]Validated:[/bold]  "
            f"{'[green]✓[/green]' if proposal.validation_passed else '[red]✗[/red]'} "
            f"{proposal.validation_output}"
        )
        if proposal.human_review_required:
            console.print("[yellow]⚠ Human review required before applying.[/yellow]")
        if proposal.unified_diff:
            console.print("\n[bold]Diff:[/bold]")
            for line in proposal.unified_diff.splitlines():
                if line.startswith("+") and not line.startswith("+++"):
                    console.print(f"[green]{line}[/green]")
                elif line.startswith("-") and not line.startswith("---"):
                    console.print(f"[red]{line}[/red]")
                else:
                    console.print(line)
        console.print()
 
 
def _serialize_proposals(proposals: list[FixProposal]) -> list[dict[str, object]]:
    """Convert a list of FixProposal dataclasses to JSON-safe dicts."""
    return [dataclasses.asdict(p) for p in proposals]
 
 
def _render_doctor_json(proposals: list[FixProposal], workflow_path: Path) -> str:
    """Serialise fix proposals to a JSON string matching the gap report style."""
    doc = {
        "schema_version": "0.1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workflow_path": str(workflow_path),
        "proposals": _serialize_proposals(proposals),
        "summary": {
            "total_proposals": len(proposals),
            "validated": sum(1 for p in proposals if p.validation_passed),
            "human_review_required": sum(1 for p in proposals if p.human_review_required),
            "avg_confidence": round(
                sum(p.confidence for p in proposals) / len(proposals), 2
            ) if proposals else 0.0,
        },
    }
    return json.dumps(doc, indent=2)
 
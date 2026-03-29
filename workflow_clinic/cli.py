"""
Workflow Clinic CLI — entry point for all commands.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
import os

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich import box

from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.parsers.nextflow import NextflowParser
from workflow_clinic.parsers.registry import ParserRegistry
from workflow_clinic.schema.gap_report import GapReport, Severity
from workflow_clinic.core.github_client import GitHubClient, GitHubIssuesDisabledError

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

# ── Severity → suggested GitHub label ────────────────────────────────────────

_SEVERITY_LABEL = {
    Severity.CRITICAL: "critical",
    Severity.MAJOR:    "major",
    Severity.MINOR:    "minor",
    Severity.INFO:     "info",
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

    workflow = ParserRegistry().get_parser(path).parse_file(path)

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
            "Path to a .nf or .smk file, or a remote source:\n\n"
            "  dockstore:github.com/owner/repo\n\n"
            "  https://github.com/owner/repo"
        ),
    ),
    format: OutputFormat = typer.Option(
        OutputFormat.terminal, "--format", "-f",
        help="Output format: terminal (default), json, or markdown.",
    ),
    output: Path | None = typer.Option(
        None, "--output", "-o",
        help="Save the report to this file instead of printing to stdout.",
    ),
    score: bool = typer.Option(
        False, "--score",
        help="Print only the cloud readiness score (0.0–1.0) and exit.",
    ),
    create_issue: bool = typer.Option(
        False, "--create-issue",
        help=(
            "Draft a GitHub issue body from the gap report. "
            "Does not submit anything to GitHub unless --submit is also passed."
        ),
    ),
    issue_output: Path | None = typer.Option(
        None, "--issue-output",
        help="Save the drafted GitHub issue body to this file (implies --create-issue).",
    ),
    submit: bool = typer.Option(
        False, "--submit",
        help=(
            "POST the issue to GitHub (implies --create-issue). "
            "Requires GITHUB_TOKEN in the environment and --repo."
        ),
    ),
    repo: str | None = typer.Option(
        None, "--repo",
        help=(
            "Target GitHub repository as owner/repo (e.g. nf-core/rnaseq). "
            "Inferred from the source URL when the source is a GitHub or "
            "Dockstore identifier; required for local files."
        ),
    ),
) -> None:
    """Analyse a Nextflow or Snakemake workflow and report cloud-readiness gaps."""

    # --issue-output implies --create-issue
    if issue_output is not None:
        create_issue = True

    # --submit implies --create-issue
    if submit:
        create_issue = True

    # ── Resolve source → ParsedWorkflow ──────────────────────────────────────
    if not any(source.startswith(p) for p in ("dockstore:", "github:", "https://")):
        path = Path(source)
        if not path.exists():
            err_console.print(f"[red]File not found:[/red] {path}")
            raise typer.Exit(1)
        workflow = ParserRegistry().get_parser(path).parse_file(path)
        display_path = path

    else:
        from workflow_clinic.core.fetcher import fetch
        try:
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

    # ── Render gap report ─────────────────────────────────────────────────────
    if format == OutputFormat.json:
        rendered = _render_json(report)
    elif format == OutputFormat.markdown:
        rendered = _render_markdown(report)
    else:
        _render_terminal(report, display_path)
        if output:
            output.write_text(_render_markdown(report), encoding="utf-8")
            console.print(f"\n[dim]Report saved to {output}[/dim]")

        if create_issue:
            _handle_issue_draft(report, issue_output)
        if submit:
            _submit_issue_to_github(report, source, repo)
        return

    # ── Write or print gap report ─────────────────────────────────────────────
    if output:
        output.write_text(rendered, encoding="utf-8")
        console.print(f"[dim]Report saved to {output}[/dim]")
    else:
        if format == OutputFormat.markdown:
            console.print(Markdown(rendered))
        else:
            typer.echo(rendered)

    # ── Issue draft (runs after main report in all non-terminal modes) ────────
    if create_issue:
        _handle_issue_draft(report, issue_output)
    if submit:
        _submit_issue_to_github(report, source, repo)


def _handle_issue_draft(report: GapReport, issue_output: Path | None) -> None:
    """Generate a GitHub issue draft and either save it or print it."""
    title, body = _render_github_issue(report)

    if issue_output:
        # Write a self-contained markdown file with title at top
        full = f"<!-- WORKFLOW CLINIC ISSUE DRAFT -->\n<!-- Title: {title} -->\n\n{body}"
        issue_output.write_text(full, encoding="utf-8")
        console.print(f"[dim]GitHub issue draft saved to {issue_output}[/dim]")
        console.print(f"[bold]Suggested title:[/bold] {title}")
    else:
        # Print to terminal so the user can copy-paste
        console.print()
        console.rule("[bold cyan]GitHub Issue Draft[/bold cyan]")
        console.print(f"[bold]Suggested title:[/bold]  {title}")
        console.print(
            "[bold]Suggested labels:[/bold]  "
            + ", ".join(_issue_labels(report))
        )
        console.print()
        console.print(Markdown(body))
        console.rule()
        console.print(
            "[dim]ℹ️  This draft has NOT been submitted to GitHub. "
            "Use --issue-output to save it, then create the issue manually "
            "or add --submit (coming in Day 9) to post it automatically.[/dim]"
        )


# ── GitHub submission helpers (Day 9) ─────────────────────────────────────────

def _resolve_repo(repo_flag: str | None, source: str) -> str | None:
    """
    Return 'owner/repo' from the explicit --repo flag or inferred from source.

    --repo accepts three forms:
        owner/repo                          (canonical)
        https://github.com/owner/repo      (full URL — normalised here)
        github.com/owner/repo              (URL without scheme — normalised here)

    Source inference handles:
        dockstore:github.com/owner/repo
        https://github.com/owner/repo
        github:owner/repo
        github.com/owner/repo

    Returns None for local file paths — the caller must require --repo.
    """
    _URL_PREFIXES = (
        "https://github.com/",
        "http://github.com/",
        "github.com/",
        "github:",
        "dockstore:github.com/",
    )

    def _strip_to_owner_repo(s: str) -> str | None:
        """Return 'owner/repo' from any of the supported string forms."""
        for prefix in _URL_PREFIXES:
            if s.startswith(prefix) or prefix in s:
                tail  = s.split(prefix, 1)[1]
                parts = [p for p in tail.split("/") if p]
                if len(parts) >= 2:
                    return f"{parts[0]}/{parts[1]}"
        # Already in owner/repo form — no prefix matched
        if s.count("/") == 1 and not s.startswith("http"):
            return s
        return None

    if repo_flag:
        normalised = _strip_to_owner_repo(repo_flag)
        # If normalisation failed (unrecognised format) return as-is and let
        # the caller's format check catch it with a clear error message.
        return normalised if normalised else repo_flag

    return _strip_to_owner_repo(source)

def _render_pr_body(proposal: "FixProposal") -> str:
    """
    Build a GitHub PR body for a single FixProposal.

    Mirrors the _render_github_issue structure so issues and PRs are visually
    consistent in the GitHub UI: attribution blockquote, fix summary, diff
    in a code fence, and a human-review warning when validation was partial.
    """
    from workflow_clinic.doctor.fix_generators.base import FixProposal as FP
    lines: list[str] = [
        "## 🏥 Workflow Clinic — Automated Fix",
        "",
        "> **This PR was opened automatically by "
        "[Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), "
        "a GA4GH Cloud Work Stream tool for cloud-readiness gap remediation.**",
        "",
        f"**Gap:** `{proposal.gap_id}`  ",
        f"**Process:** `{proposal.process_name}`  ",
        f"**Fix:** {proposal.description}  ",
        f"**Confidence:** {proposal.confidence:.0%}  ",
        (
            "**Validated:** ✓ Parser confirmed the fix is syntactically correct."
            if proposal.validation_passed
            else "**Validated:** ✗ Syntactic validation failed — review carefully."
        ),
        "",
        "### Diff",
        "",
        "```diff",
        proposal.unified_diff.rstrip(),
        "```",
        "",
    ]
    if proposal.human_review_required:
        lines += [
            "> ⚠️ **Human review required before merging.** The fix was not "
            "fully validated — confirm the suggested image exists on its "
            "registry before approving.",
            "",
        ]
    lines += [
        "---",
        "_Generated by "
        "[Workflow Clinic](https://github.com/electricdystopia/workflow-clinic)_",
    ]
    return "\n".join(lines)


def _submit_issue_to_github(
    report: GapReport,
    source: str,
    repo_flag: str | None,
) -> None:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        err_console.print(
            "[red]--submit requires GITHUB_TOKEN to be set in the environment.[/red]\n"
            "  export GITHUB_TOKEN=ghp_..."
        )
        raise typer.Exit(1)

    repo_str = _resolve_repo(repo_flag, source)
    if (
        not repo_str
        or "/" not in repo_str
        or repo_str.count("/") != 1
        or repo_str.startswith("http")
        or repo_str.startswith("github")
    ):
        err_console.print(
            f"[red]Invalid repository '[bold]{repo_str}[/bold]'.[/red]\n"
            "  --repo must be in [bold]owner/repo[/bold] format, "
            "e.g. [bold]electricdystopia/proteinannotator[/bold]."
        )
        raise typer.Exit(1)

    owner, repo_name = repo_str.split("/", 1)
    title, body      = _render_github_issue(report)
    labels           = _issue_labels(report)

    client = GitHubClient(token)

    try:
        existing = client.find_existing_issue(owner, repo_name, "[Workflow Clinic]")
    except GitHubIssuesDisabledError as exc:
        err_console.print(f"[red]Cannot submit issue:[/red] {exc}")
        err_console.print(
            "[dim]Tip: use [bold]--issue-output report.md[/bold] to save the "
            "draft locally instead.[/dim]"
        )
        raise typer.Exit(1)

    try:
        if existing is not None:
            console.print(
                f"[yellow]Open issue #{existing} already exists for this repo. "
                f"Appending the updated report as a comment.[/yellow]"
            )
            comment_body = (
                "## 📋 Updated Workflow Clinic Report\n\n"
                f"_(Re-run on {report.generated_at.strftime('%Y-%m-%d %H:%M UTC')})_\n\n"
                + body
            )
            url = client.add_comment(owner, repo_name, existing, comment_body)
            console.print(f"[green]✓ Comment added:[/green] {url}")
        else:
            url = client.create_issue(owner, repo_name, title, body, labels)
            console.print(f"[green]✓ Issue created:[/green] {url}")
    except GitHubIssuesDisabledError as exc:
        err_console.print(f"[red]Cannot submit issue:[/red] {exc}")
        err_console.print(
            "[dim]Tip: use [bold]--issue-output report.md[/bold] to save the "
            "draft locally instead.[/dim]"
        )
        raise typer.Exit(1)
    except Exception as exc:
        err_console.print(f"[red]GitHub API error:[/red] {exc}")
        raise typer.Exit(1)

def _submit_pr_to_github(
    proposal:      "FixProposal",
    source_path:   Path,
    repo_flag:     str | None,
    branch_prefix: str,
) -> None:
    """
    Apply a FixProposal by committing the patched file to a new branch and
    opening a pull request.

    Branch name: {prefix}/{gap_id_lower}/{process_name_lower}
    e.g. wf-clinic/container-001/align

    The file committed to the repo is named after the source file's basename.
    For a workflow at /home/user/project/main.nf, the file committed is main.nf
    at the root of the repo.  Pass --repo explicitly since there is no source
    URL to infer from for local files.
    """
    from workflow_clinic.core.github_client import GitHubClient

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        err_console.print(
            "[red]--create-pr requires GITHUB_TOKEN to be set in the environment.[/red]\n"
            "  export GITHUB_TOKEN=ghp_..."
        )
        raise typer.Exit(1)

    if (
            not repo_flag
            or "/" not in repo_flag
            or repo_flag.count("/") != 1
            or repo_flag.startswith("http")
            or repo_flag.startswith("github")
        ):
            err_console.print(
                f"[red]--create-pr requires --repo in [bold]owner/repo[/bold] format.[/red]\n"
                "  e.g. [bold]--repo electricdystopia/proteinannotator[/bold]\n"
                "  Do not pass a full URL."
            )
            raise typer.Exit(1)

    owner, repo_name = repo_flag.split("/", 1)
    client           = GitHubClient(token)

    # ── Resolve base branch ───────────────────────────────────────────────────
    try:
        base_branch = client.get_default_branch(owner, repo_name)
    except Exception as exc:
        err_console.print(f"[red]Could not resolve default branch: {exc}[/red]")
        raise typer.Exit(1)

    # ── Build branch name ─────────────────────────────────────────────────────
    slug = (
        f"{proposal.gap_id}/{proposal.process_name}"
        .lower()
        .replace("_", "-")
        .replace(" ", "-")
    )
    branch_name = f"{branch_prefix}/{slug}"

    console.print(f"[dim]Creating branch '{branch_name}' off '{base_branch}'...[/dim]")
    try:
        client.create_branch(owner, repo_name, base_branch, branch_name)
    except Exception as exc:
        err_console.print(
            f"[red]Failed to create branch '{branch_name}': {exc}[/red]\n"
            "  The branch may already exist. Delete it or run with a different "
            "--branch-prefix."
        )
        raise typer.Exit(1)

    # ── Commit the patched file ───────────────────────────────────────────────
    file_path_in_repo = source_path.name   # e.g. "main.nf" or "workflow.smk"
    commit_message = (
        f"fix({proposal.gap_id.lower()}): {proposal.description}\n\n"
        f"Process:    {proposal.process_name}\n"
        f"Confidence: {proposal.confidence:.0%}\n"
        f"Validated:  {'yes' if proposal.validation_passed else 'no'}\n\n"
        "Applied automatically by Workflow Clinic.\n"
        "https://github.com/electricdystopia/workflow-clinic"
    )
    console.print(f"[dim]Committing '{file_path_in_repo}' to '{branch_name}'...[/dim]")
    try:
        client.commit_file(
            owner, repo_name, branch_name,
            file_path_in_repo, proposal.patched_content, commit_message,
        )
    except Exception as exc:
        err_console.print(f"[red]Failed to commit patched file: {exc}[/red]")
        raise typer.Exit(1)

    # ── Open the PR ───────────────────────────────────────────────────────────
    pr_title = (
        f"[Workflow Clinic] Fix {proposal.gap_id} in `{proposal.process_name}`"
    )
    pr_body = _render_pr_body(proposal)
    console.print(f"[dim]Opening PR '{pr_title}'...[/dim]")
    try:
        pr_url = client.create_pull_request(
            owner, repo_name, branch_name, base_branch, pr_title, pr_body,
        )
        console.print(f"[green]✓ PR created:[/green] {pr_url}")
    except Exception as exc:
        err_console.print(f"[red]Failed to create PR: {exc}[/red]")
        raise typer.Exit(1)


def _issue_labels(report: GapReport) -> list[str]:
    """Return a de-duplicated, severity-ordered list of suggested GitHub labels."""
    labels = ["workflow-clinic", "cloud-readiness"]
    if report.summary.critical > 0:
        labels.append("severity:critical")
    if report.summary.major > 0:
        labels.append("severity:major")
    if report.summary.minor > 0:
        labels.append("severity:minor")
    # One label per gap category present in the report
    seen_cats: set[str] = set()
    for gap in report.gaps:
        cat = gap.category.value.replace("_", "-")
        if cat not in seen_cats:
            labels.append(f"gap:{cat}")
            seen_cats.add(cat)
    return labels


def _render_github_issue(report: GapReport) -> tuple[str, str]:
    """
    Build a GitHub issue title and body from a GapReport.

    Returns:
        (title, body) — title is a single-line string; body is markdown.

    The body is designed to be copy-pasted directly into a GitHub issue.
    It contains everything a reviewer needs to understand the gaps without
    running the tool themselves: summary counts, a gap table, and per-gap
    detail with recommendations.

    Nothing is submitted to GitHub — the caller decides what to do with the
    strings. Actual submission is planned for Day 9 (GitHub client).
    """
    s = report.summary

    # ── Title ─────────────────────────────────────────────────────────────────
    unique_processes = list(dict.fromkeys(g.process_name for g in report.gaps))
    n = len(unique_processes)
    score_pct = int(report.summary.cloud_readiness_score * 100)

    if s.total_gaps == 0:
        title = f"[Workflow Clinic] No cloud-readiness gaps found (score: {score_pct}%)"
    elif n == 1:
        title = (
            f"[Workflow Clinic] {s.total_gaps} cloud-readiness gap"
            f"{'s' if s.total_gaps > 1 else ''} in process "
            f"`{unique_processes[0]}` (score: {score_pct}%)"
        )
    else:
        title = (
            f"[Workflow Clinic] {s.total_gaps} cloud-readiness gaps across "
            f"{n} processes (score: {score_pct}%)"
        )

    # ── Body ──────────────────────────────────────────────────────────────────
    lines: list[str] = []

    lines.append("## 🏥 Workflow Clinic — Automated Cloud-Readiness Report")
    lines.append("")
    lines.append(
        "> **This issue was drafted automatically by "
        "[Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), "
        "a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness "
        "gaps in bioinformatics workflows.**"
    )
    lines.append(">")
    lines.append(f"> Workflow: `{report.workflow_path}`  ")
    lines.append(
        f"> Generated: {report.generated_at.strftime('%Y-%m-%d %H:%M UTC')}  "
    )
    lines.append(f"> Schema: `{report.schema_version}`")
    lines.append("")

    # Score badge (text-based for plain GitHub markdown)
    score_emoji = "🟢" if s.cloud_readiness_score >= 0.8 else (
        "🟡" if s.cloud_readiness_score >= 0.5 else "🔴"
    )
    lines.append(
        f"### {score_emoji} Cloud Readiness Score: "
        f"**{s.cloud_readiness_score:.2f} / 1.00**"
    )
    lines.append("")

    if s.total_gaps == 0:
        lines.append(
            "✅ **No gaps found.** This workflow meets all currently checked "
            "cloud-readiness criteria. No action is required."
        )
        return title, "\n".join(lines)

    # Summary table
    lines.append("### Summary")
    lines.append("")
    lines.append("| Severity | Count | Description |")
    lines.append("|---|---|---|")
    if s.critical:
        lines.append(
            f"| 🔴 **Critical** | {s.critical} | "
            "Portability blockers — workflow cannot run on cloud WES |"
        )
    if s.major:
        lines.append(
            f"| 🟠 **Major** | {s.major} | "
            "Significant gaps affecting reproducibility or correctness |"
        )
    if s.minor:
        lines.append(
            f"| 🟡 **Minor** | {s.minor} | "
            "Resource hints missing — affects cost and scheduling efficiency |"
        )
    if s.info:
        lines.append(
            f"| ⚪ **Info** | {s.info} | "
            "Informational — best practice suggestions |"
        )
    lines.append(f"| **Total** | **{s.total_gaps}** | |")
    lines.append(f"| Auto-fixable | {s.auto_fixable_count} | "
                 "Can be fixed automatically with `workflow-clinic doctor` |")
    lines.append("")

    if s.auto_fixable_count > 0:
        lines.append(
            f"> 💡 **{s.auto_fixable_count} gap(s) can be fixed automatically.** "
            "Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate "
            "a patch and open a PR."
        )
        lines.append("")

    # Gap overview table
    lines.append("### Gaps")
    lines.append("")
    lines.append("| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, g in enumerate(report.gaps, 1):
        sev_icon = {"CRITICAL": "🔴", "MAJOR": "🟠", "MINOR": "🟡", "INFO": "⚪"}.get(
            g.severity.value, ""
        )
        fix_mark = "✅" if g.auto_fixable else "—"
        lines.append(
            f"| {i} | `{g.gap_id}` | {sev_icon} {g.severity.value} "
            f"| `{g.process_name}` | {g.category.value} "
            f"| L{g.location.line_start}–{g.location.line_end} | {fix_mark} |"
        )
    lines.append("")

    # Per-gap detail
    lines.append("### Detail")
    lines.append("")
    for i, g in enumerate(report.gaps, 1):
        sev_icon = {"CRITICAL": "🔴", "MAJOR": "🟠", "MINOR": "🟡", "INFO": "⚪"}.get(
            g.severity.value, ""
        )
        lines.append(
            f"<details><summary>"
            f"{sev_icon} <strong>{i}. {g.gap_id} — {g.process_name}</strong>"
            f" ({g.severity.value})</summary>"
        )
        lines.append("")
        lines.append(f"**Category:** `{g.category.value}`  ")
        lines.append(
            f"**Location:** `{g.location.file}` "
            f"L{g.location.line_start}–{g.location.line_end}  "
        )
        lines.append(f"**Auto-fixable:** {'Yes' if g.auto_fixable else 'No'}")
        lines.append("")
        lines.append("**Description:**  ")
        lines.append(g.description)
        lines.append("")
        if g.evidence:
            lines.append("**Evidence:**")
            lines.append("```")
            lines.append(g.evidence)
            lines.append("```")
            lines.append("")
        lines.append("**Recommendation:**")
        lines.append("```")
        lines.append(g.recommendation)
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append(
        "_Generated by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic) "
        f"· schema `{report.schema_version}` · "
        "[Report a false positive](https://github.com/electricdystopia/workflow-clinic/issues)_"
    )

    return title, "\n".join(lines)


# ── Renderers ─────────────────────────────────────────────────────────────────

def _render_terminal(report: GapReport, path: Path) -> None:
    """Rich-formatted terminal output with colour-coded severity."""
    s = report.summary

    console.rule("[bold cyan]Workflow Clinic — Gap Report[/bold cyan]")
    console.print(f"[bold]Workflow:[/bold]  {path}")
    console.print(f"[bold]Processes:[/bold] {len(set(g.process_name for g in report.gaps or []))}")
    console.print()

    score = s.cloud_readiness_score
    score_colour = "green" if score >= 0.8 else "yellow" if score >= 0.5 else "red"
    console.print(
        f"[bold]Cloud Readiness Score:[/bold] "
        f"[{score_colour}]{score:.2f} / 1.00[/{score_colour}]"
    )
    console.print()

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
    path: Path | None = typer.Argument(
        None,
        help=(
            "Path to a local .nf or .smk workflow file. "
            "Omit when using --source for remote workflows."
        ),
    ),
    source: str | None = typer.Option(
        None, "--source", "-s",
        help=(
            "Remote workflow source (same formats as `critic`):\n\n"
            "  https://github.com/owner/repo\n\n"
            "  dockstore:github.com/owner/repo\n\n"
            "When given, --repo is inferred automatically."
        ),
    ),
    gap: str | None = typer.Option(
        None, "--gap", "-g",
        help="Only fix gaps with this ID, e.g. CONTAINER-001.",
    ),
    output: Path | None = typer.Option(
        None, "--output", "-o",
        help="Save fix proposals as JSON to this file.",
    ),
    create_pr: bool = typer.Option(
        False, "--create-pr",
        help=(
            "Apply each validated fix and open a pull request on GitHub. "
            "Requires GITHUB_TOKEN in the environment and --repo."
        ),
    ),
    branch_prefix: str = typer.Option(
        "wf-clinic", "--branch-prefix",
        help="Branch name prefix for fix branches (default: wf-clinic).",
    ),
    repo: str | None = typer.Option(
        None, "--repo",
        help=(
            "Target GitHub repository as owner/repo. "
            "Inferred automatically from --source when source is a GitHub URL."
        ),
    ),
) -> None:
    """Generate and optionally submit fixes for auto-fixable gaps."""

    # ── Resolve source → local file content + display path ───────────────────
    if source is not None and path is not None:
        err_console.print(
            "[red]Pass either a local path or --source, not both.[/red]"
        )
        raise typer.Exit(1)

    if source is not None:
        # Remote path — fetch all .nf files exactly as `critic` does
        from workflow_clinic.core.fetcher import fetch
        try:
            fetched = fetch(source, full_repo=True)
        except Exception as exc:
            err_console.print(f"[red]Fetch failed:[/red] {exc}")
            raise typer.Exit(1)

        source_text   = fetched.content
        display_path  = Path(fetched.filename)
        workflow      = NextflowParser().parse(fetched.content, display_path)
        # For --create-pr we need a path object to derive the filename;
        # use the fetched filename as a stand-in.
        effective_path = display_path
        # Infer --repo from source URL if not given explicitly
        if repo is None:
            repo = _resolve_repo(None, source)

    elif path is not None:
        if not path.exists():
            err_console.print(f"[red]File not found:[/red] {path}")
            raise typer.Exit(1)
        source_text    = path.read_text(encoding="utf-8")
        display_path   = path
        effective_path = path
        workflow       = ParserRegistry().get_parser(path).parse_file(path)

    else:
        err_console.print(
            "[red]Provide a local file path or --source for a remote workflow.[/red]\n"
            "  workflow-clinic doctor main.nf --gap CONTAINER-001\n"
            "  workflow-clinic doctor --source https://github.com/owner/repo "
            "--gap CONTAINER-001 --create-pr"
        )
        raise typer.Exit(1)

    # ── Run critic ────────────────────────────────────────────────────────────
    source_lines = source_text.splitlines(keepends=True)
    report       = CriticEngine().run(workflow)

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

    console.print(f"\n[bold cyan]Workflow Doctor[/bold cyan] — {display_path}")
    console.print(f"[dim]Auto-fixable gaps: {len(auto_fixable)}[/dim]\n")

    proposals = DoctorEngine().run(report, source_lines)

    if not proposals:
        console.print("[yellow]No fixes could be generated.[/yellow]")
        raise typer.Exit(0)

    if output:
        rendered = _render_doctor_json(proposals, display_path)
        output.write_text(rendered, encoding="utf-8")
        console.print(f"[dim]Fix proposals saved to {output}[/dim]\n")

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

    # ── --create-pr ───────────────────────────────────────────────────────────
    if create_pr:
        submitted = 0
        for proposal in proposals:
            if not proposal.validation_passed:
                console.print(
                    f"[yellow]Skipping {proposal.gap_id}/{proposal.process_name} "
                    f"— validation failed (confidence {proposal.confidence:.0%}). "
                    f"Review the diff manually before applying.[/yellow]"
                )
                continue
            if not proposal.patched_content:
                console.print(
                    f"[yellow]Skipping {proposal.gap_id}/{proposal.process_name} "
                    f"— no patched content available.[/yellow]"
                )
                continue
            _submit_pr_to_github(proposal, effective_path, repo, branch_prefix)
            submitted += 1

        if submitted == 0:
            console.print(
                "[yellow]No proposals were suitable for PR creation. "
                "Run without --create-pr to review diffs manually.[/yellow]"
            )

def _serialize_proposals(proposals: list[FixProposal]) -> list[dict[str, object]]:
    return [dataclasses.asdict(p) for p in proposals]


def _render_doctor_json(proposals: list[FixProposal], workflow_path: Path) -> str:
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
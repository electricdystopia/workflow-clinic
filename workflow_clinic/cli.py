import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from workflow_clinic.parsers.nextflow import NextflowParser

app = typer.Typer(
    help="Workflow Clinic — cloud-readiness tools for bioinformatics workflows.",
    invoke_without_command=True,
    no_args_is_help=True,
)
console = Console()


@app.command("parse")
def parse(
    path: Path = typer.Argument(..., help="Path to a .nf workflow file"),
) -> None:
    """Parse a Nextflow workflow and list all processes with their detected directives."""
    if not path.exists():
        console.print(f"[red]File not found:[/red] {path}")
        raise typer.Exit(1)

    parser = NextflowParser()
    workflow = parser.parse_file(path)

    if not workflow.processes:
        console.print("[yellow]No processes found in workflow.[/yellow]")
        raise typer.Exit(0)

    console.print(f"\n[bold cyan]Workflow:[/bold cyan] {path}")
    console.print(f"[bold]Processes found:[/bold] {len(workflow.processes)}\n")

    table = Table(show_header=True, header_style="bold magenta")
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
# Day 3 — CLI + Report Output

## What we built and why

Day 2 left us with a working `CriticEngine` that produces a `GapReport` object.
Day 3 answers the next question: how does a user actually interact with this?

The goal was to turn the internal pipeline into a real, usable CLI tool. By the
end of Day 3 the full flow looks like this:
```
.nf file → NextflowParser → ParsedWorkflow → CriticEngine → GapReport → CLI output
```

The CLI lives in `workflow_clinic/cli.py`. The tests live in `tests/test_cli.py`.

---

## New files introduced today
```
workflow_clinic/
└── cli.py          ← extended with the critic command and three output renderers
tests/
└── test_cli.py     ← 17 new CLI integration tests
```

---

## Why Typer for the CLI?

The two mainstream options for Python CLIs are `argparse` (standard library)
and `Typer`. We use Typer for three reasons:

- **Type-driven argument parsing.** Typer reads Python type annotations directly
  — `path: Path`, `format: OutputFormat`, `score: bool` — and generates the
  correct CLI argument types, validation, and `--help` text automatically. No
  separate schema to maintain.
- **Subcommands for free.** As soon as you register two `@app.command()` 
  functions, Typer switches to subcommand mode automatically. This is how
  `workflow-clinic parse` and `workflow-clinic critic` coexist, and how
  `workflow-clinic doctor` will slot in on Day 5 without touching anything else.
- **Typer's `CliRunner`** (inherited from Click) lets us test the CLI in-process
  without spawning subprocesses — fast, clean, and captureable in tests.

Note that adding the `critic` command also fixed the `parse` subcommand issue
from Day 1 — with two commands registered, Typer correctly treats both as named
subcommands rather than collapsing to a single root command.

**Resources:**
- [Typer documentation](https://typer.tiangolo.com/)
- [Typer — subcommands](https://typer.tiangolo.com/tutorial/commands/)
  — explains how multiple `@app.command()` functions create a subcommand tree.
- [Click's CliRunner](https://click.palletsprojects.com/en/8.x/testing/)
  — the test runner Typer inherits; used in `tests/test_cli.py`.

---

## The three output modes

The `--format` flag accepts three values, defined as an enum in `cli.py`:
```python
class OutputFormat(str, Enum):
    terminal = "terminal"
    json     = "json"
    markdown = "markdown"
```

Using an enum rather than a plain string means Typer validates the value
automatically and shows the allowed options in `--help`. Passing `--format xml`
fails immediately with a clear error rather than blowing up inside the renderer.

### Terminal (default)

Handled by `_render_terminal()` in `workflow_clinic/cli.py`. Uses `rich`
directly — coloured severity labels, a summary table, a gap table, and a
per-gap detail section. The score gets a colour too: green above 0.8, yellow
above 0.5, red below.

This output is for humans. It is never parsed programmatically — that's what
JSON is for.

**Resources:**
- [Rich documentation](https://rich.readthedocs.io/en/stable/)
- [Rich — Tables](https://rich.readthedocs.io/en/stable/tables.html)
- [Rich — Markup](https://rich.readthedocs.io/en/stable/markup.html)
  — the `[bold red]text[/bold red]` syntax used throughout `_render_terminal`.

### JSON

Handled by `_render_json()` in `workflow_clinic/cli.py`:
```python
def _render_json(report: GapReport) -> str:
    return json.dumps(report.model_dump(mode="json"), indent=2)
```

`model_dump(mode="json")` is a Pydantic v2 method that serializes the entire
`GapReport` to a plain dict with all types converted to JSON-safe equivalents
— `datetime` becomes an ISO string, enums become their string values, etc.

One important implementation detail: JSON output is written via `typer.echo()`
rather than `console.print()`. Rich applies line-wrapping to everything it
prints, which breaks long strings like absolute file paths mid-line and
produces invalid JSON. `typer.echo()` writes directly to stdout with no
processing. We discovered this when three JSON tests failed with
`JSONDecodeError: Invalid control character` — the newline Rich inserted inside
the `workflow_path` string was the culprit.

**Resources:**
- [Pydantic `model_dump`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump)
  — specifically the `mode="json"` argument which handles datetime and enum
  serialization automatically.
- [Python `json` module](https://docs.python.org/3/library/json.html)

### Markdown

Handled by `_render_markdown()` in `workflow_clinic/cli.py`. Builds a markdown
string manually — a summary table, a gap overview table, and a detail section
with one `###` heading per gap. This format is designed to be pasted directly
into a GitHub issue body, which is exactly what Day 4's issue creation will do.

When printing to the terminal, the markdown string is passed through
`rich.Markdown` for rendering. When saved to a file via `--output`, the raw
markdown string is written so the file is valid `.md`.

---

## The `--score` flag
```bash
workflow-clinic critic broken.nf --score
# 0.2
```

Prints only the `cloud_readiness_score` float and exits. This is designed for
use in CI scripts:
```bash
score=$(workflow-clinic critic main.nf --score)
if (( $(echo "$score < 0.8" | bc -l) )); then
  echo "Workflow is not cloud-ready enough to deploy"
  exit 1
fi
```

The flag is implemented as an early-return shortcut at the top of the `critic`
command in `workflow_clinic/cli.py`, before any rendering logic runs.

---

## The `--output` flag

Saves the report to a file instead of printing to stdout. For `--format json`
and `--format markdown`, the raw string is written directly. For the default
terminal format, saving to a file falls back to markdown automatically — rich
terminal markup isn't useful in a `.md` file.

---

## Two consoles — `console` and `err_console`
```python
console     = Console()           # stdout — report content
err_console = Console(stderr=True) # stderr — errors and warnings
```

Error messages (file not found, etc.) go to stderr so they don't pollute stdout
when the output is being piped or redirected. This matters for the JSON mode
especially — if an error message appeared in stdout alongside the JSON, any
downstream tool trying to parse it would fail.

**Resources:**
- [Rich — Console](https://rich.readthedocs.io/en/stable/console.html)
  — explains the `stderr` argument and why separating output streams matters.

---

## Test strategy

Tests live in `tests/test_cli.py` and use Typer's `CliRunner` to invoke
commands in-process:
```python
runner = CliRunner()
result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf")])
assert result.exit_code == 0
assert "CONTAINER-001" in result.output
```

`result.output` captures everything written to stdout during the invocation.
This lets us assert on content without parsing terminal markup.

The most important tests are the JSON ones — they actually parse `result.output`
with `json.loads()`, so they catch any output pollution (rich markup, extra
lines, wrapping) that would break machine consumption. This is exactly how we
caught the rich line-wrapping bug during development.

One design decision: the CLI exits with code `0` even when gaps are found.
Gaps are not a CLI error — they are the expected, informative output of the
tool. Exit code `1` is reserved for genuine errors like a missing file. This
matches the convention of tools like `pylint` and `eslint` — though those tools
do optionally support non-zero exits on findings, which is something we could
add later via a `--fail-on CRITICAL` flag.

**Resources:**
- [Typer testing guide](https://typer.tiangolo.com/tutorial/testing/)
- [Click CliRunner reference](https://click.palletsprojects.com/en/8.x/api/#click.testing.CliRunner)
- [POSIX exit code conventions](https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html)
  — why 0 means success and non-zero means error.

---

## What Day 4 builds on top of this

Day 4 adds live workflow fetching — pointing the CLI at a Dockstore TRS URL or
a GitHub repo URL instead of a local file, and running the Critic against real
public workflows. The `critic` command will grow a `--source` flag to
distinguish between local paths and remote URLs. The `GapReport` output is
identical either way — the fetcher's job is just to get the `.nf` file content
into the parser.
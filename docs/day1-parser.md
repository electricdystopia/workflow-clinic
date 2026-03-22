# Day 1 — Project Scaffold & Nextflow Parser

## What we built and why

The goal of Day 1 was to answer one question: given a raw `.nf` file, can we
reliably extract *what's inside each process block*? Everything else in Workflow
Clinic — detecting gaps, scoring cloud readiness, generating fixes — depends on
this. If the parser is wrong, every downstream result is wrong. So we built it
first, in isolation, and tested it thoroughly before touching anything else.

The parser lives in `workflow_clinic/parsers/nextflow.py`.
The tests live in `tests/test_nextflow_parser.py`.
The fixture workflows used for testing live in `tests/fixtures/nextflow/`.

---

## Why Nextflow first?

The project supports multiple workflow languages (Snakemake, CWL, WDL, Airflow).
We picked Nextflow DSL2 as the starting point for three reasons:

1. It has the largest number of publicly registered workflows on Dockstore and
   WorkflowHub, so fixes here have the highest immediate impact.
2. Its syntax is structured enough to parse reliably with a state machine — each
   process is a named block with clearly delimited sections.
3. The nf-core community has well-documented best practices, which gives us a
   clear target for what "cloud-ready" looks like.

**Resources:**
- [Nextflow DSL2 process syntax reference](https://www.nextflow.io/docs/latest/process.html)
  — the official docs; this is what we used to understand which directives exist
  and how they are structured inside a process block.
- [nf-core pipeline structure guide](https://nf-co.re/docs/contributing/nf-core-guidelines)
  — the community best practices that define what a "cloud-ready" Nextflow
  workflow actually looks like in practice.

---

## What is a state machine and why use one here?

A state machine is a program that moves between defined states based on what it
reads. In our parser, the states are:
```
OUTSIDE_PROCESS → (see "process FOO {") → INSIDE_PROCESS
INSIDE_PROCESS  → (see "input:")         → READING_INPUT
INSIDE_PROCESS  → (see "output:")        → READING_OUTPUT
INSIDE_PROCESS  → (see "script:")        → READING_SCRIPT
READING_*       → (see "}")              → OUTSIDE_PROCESS
```

The alternative would be to use a proper grammar-based parser (like ANTLR or
tree-sitter). We chose the state machine for two reasons:

- **No external dependency.** A grammar-based approach would require a Nextflow
  grammar file and a parser generator. The state machine is pure Python and runs
  anywhere.
- **Good enough for our needs.** We don't need a full syntax tree — we just need
  the directives. The state machine gets us exactly that without the overhead.

The tradeoff is that it can break on unusual but valid Nextflow syntax (e.g.
deeply nested closures). That's acceptable for a POC and something to harden in
the full project.

**Resources:**
- [Crafting Interpreters — Scanning chapter](https://craftinginterpreters.com/scanning.html)
  — the best approachable explanation of how to write a line-by-line state
  machine scanner/lexer, which is exactly the pattern our parser follows.
- [Python `re` module documentation](https://docs.python.org/3/library/re.html)
  — reference for every regex construct used below.
- [regex101.com](https://regex101.com) — use this to test and understand any
  regex in this file interactively; paste the pattern and a sample line and it
  will explain each part.

---

## Data models — why dataclasses?

We use Python `dataclass` objects (`NextflowProcess`, `ParsedWorkflow`,
`DirectiveBlock`) rather than plain dicts. This matters because:

- A dict like `{"name": "ALIGN", "container": None}` gives you no guarantees.
  You can typo a key and Python won't complain until runtime.
- A `dataclass` gives you a named, typed structure. Your editor autocompletes
  fields, mypy catches wrong types, and the code reads like documentation.

We use `dataclasses` here (not Pydantic) because these are *internal* parsing
structures — they never leave the parser module. Pydantic is reserved for the
`GapReport` and `FixProposal` models that cross module boundaries and need
runtime validation.

These models are defined at the top of `workflow_clinic/parsers/nextflow.py`.

### The key models:

**`DirectiveBlock`** — holds the raw lines of a multi-line section (input,
output, script). The `.raw` property joins them into a single string for easy
inspection. We store lines rather than a joined string so we can later do
line-level analysis (e.g. "which specific line has the hardcoded path?").

**`NextflowProcess`** — one process block. Holds all the directives we care
about plus `line_start` and `line_end` so we can point a user to exactly where
in their file a problem is. `directives_found()` returns a list of which
directives are actually present — used by the rule engine in Day 2.

**`ParsedWorkflow`** — the top-level result of parsing a file. Just a path plus
a list of `NextflowProcess` objects.

**Resources:**
- [Python dataclasses documentation](https://docs.python.org/3/library/dataclasses.html)
- [Real Python — dataclasses guide](https://realpython.com/python-data-classes/)
  — a more readable walkthrough of when and why to use dataclasses over dicts
  or namedtuples.

---

## The regex patterns — what each one does

All regex patterns are defined as module-level constants at the top of
`workflow_clinic/parsers/nextflow.py` (lines prefixed with `_RE_`). Keeping
them at the top means they are compiled once when the module loads, not on
every function call.
```python
_RE_PROCESS_START = re.compile(r"^\s*process\s+(\w+)\s*\{")
```
Matches the opening line of a process block. `(\w+)` captures the process name.
The `\s*` at the start handles any indentation.
```python
_RE_CONTAINER = re.compile(r"""^\s*container\s+['"](.+?)['"]\s*(?://.*)?$""")
```
Matches a container directive. The `['"]` matches either single or double quotes.
`(.+?)` is a non-greedy capture of the image name. The `(?://.*)?` at the end
optionally ignores inline `// comments` — we discovered this was necessary when
a test fixture had an annotated container line and the test failed.
```python
_RE_SECTION_START = re.compile(
    r"^\s*(input|output|script|shell|exec|when|stub)\s*:\s*$"
)
```
Matches the start of any named section inside a process. We track `input`,
`output`, and `script` explicitly; the others just reset the current section so
we don't accidentally collect their lines into the wrong block.

**Resources:**
- [regex101.com](https://regex101.com) — paste any of the above patterns here
  with a sample line from a `.nf` file and it will highlight exactly what each
  group matches and why.
- [Python docs — re.compile](https://docs.python.org/3/library/re.html#re.compile)
  — explains why compiling at module level (rather than inline) is faster.
- [Regular Expressions: The Complete Tutorial (Jan Goyvaerts)](https://www.regular-expressions.info/tutorial.html)
  — specifically the sections on non-greedy quantifiers (`+?`) and
  non-capturing groups (`(?:...)`) which appear in our patterns.

---

## Brace depth tracking

This logic lives in the `_parse_process` method of `NextflowParser` in
`workflow_clinic/parsers/nextflow.py`.

The parser tracks how deep it is in curly braces with a simple counter:
```python
depth += line.count("{") - line.count("}")
```

When `depth` drops to 0 after the opening line, we've reached the closing `}`
of the process block. This is simpler than scanning for a lone `}` on its own
line, and handles cases where the script block contains `{` and `}` characters
(e.g. Groovy closures, shell `${}` substitutions).

The edge case here is strings containing literal `{` or `}` — e.g.
`echo "done {sample}"` in a script block. This could throw off the depth count
in theory. In practice it rarely causes issues because script blocks are usually
the last section in a process, so the parser exits cleanly after them anyway.

**Resources:**
- [Crafting Interpreters — Parsing Expressions](https://craftinginterpreters.com/parsing-expressions.html)
  — the concept of tracking brace/bracket depth to find matching delimiters is
  a standard technique explained well here.

---

## Why we strip inline comments from directives

When we fixed the failing test `test_partial_latest_tag_captured`, the root
cause was that the container line in `tests/fixtures/nextflow/partial.nf`
looked like this:
```nextflow
container 'quay.io/biocontainers/trimmomatic:latest'  // latest tag — bad
```

Our original regex required the line to end right after the closing quote. The
comment broke it. The fix was adding `(?://.*)?` to all single-line directive
regexes (`_RE_CONTAINER`, `_RE_CPUS`, `_RE_MEMORY`) in
`workflow_clinic/parsers/nextflow.py`. This is important beyond just fixing the
test — real-world workflows are heavily annotated, and a parser that can't
handle comments is useless on real data.

---

## pyproject.toml vs requirements.txt

See `docs/design-decisions.md` for a full breakdown. Short version: `pyproject.toml`
makes `workflow-clinic` an installable package with a real CLI entry point.
`requirements.txt` can't do that.

**Resources:**
- [PEP 621 — Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
  — the actual standard that defines the `[project]` table we use.
- [setuptools pyproject.toml guide](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
  — explains the `[build-system]` table and `build-backend` field specifically.

---

## Test strategy

The tests live in `tests/test_nextflow_parser.py`. Each fixture in
`tests/fixtures/nextflow/` tests a specific failure mode:

| Fixture | What it represents |
|---|---|
| `clean.nf` | A well-written workflow — parser should find everything |
| `broken.nf` | Missing containers, no outputs, hardcoded paths — worst case |
| `partial.nf` | Mixed quality — some good, some bad, inline comments |

Tests are written to be *specific* — rather than `assert wf is not None` we
assert exact values (`assert align.container == "quay.io/..."`) so a regression
in the regex immediately points to the exact field that broke. Coverage sits at
97% on the parser module, with the 3% miss being an EOF edge case (file ends
without a closing brace) that we handle defensively but haven't written an
explicit fixture for yet.

**Resources:**
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/)
  — how to read the coverage report and what the Miss column means.
- [Real Python — pytest guide](https://realpython.com/pytest-python-testing/)
  — a good walkthrough of fixture design and test specificity, which informed
  how we structured the three fixture files.

---

## What Day 2 builds on top of this

The rule engine in Day 2 receives a `ParsedWorkflow` object (defined in
`workflow_clinic/parsers/nextflow.py`) and runs checks against it. For example:

- `ContainerMissingRule` just checks `process.container is None`
- `ContainerLatestTagRule` checks `"latest" in process.container`
- `HardcodedPathRule` scans `process.script.raw` for strings matching `r"['\"]?/\w"`

The parser's job was to make those checks trivially simple. If the parser is
right, the rules are just a few lines each.
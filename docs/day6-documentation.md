# Day 6 — Polish, Tests, CI, README

## What we built and why

The four goals for Day 6 were:

1. Push test coverage from 75% to ≥80% (ended at 90.62%)
2. Write a README that explains the tool in under a minute
3. Add GitHub Actions CI so every push is automatically linted, type-checked,
   and tested
4. Commit real gap reports from Dockstore workflows as evidence

---

## Why coverage was at 75% and how we fixed it

After Day 5, `pytest --cov` showed:

| Module | Coverage | Reason it was low |
|---|---|---|
| `cli.py` | 70% | `doctor` command had no tests; remote fetch path untested |
| `fetcher.py` | 59% | `_fetch_github_full` (new tree API path) had zero tests |
| `llm_client.py` | 44% | Provider methods never ran — LLM always mocked at class level |
| `nextflow_fixes.py` | 63% | `ContainerLatestTagFixer` had no tests at all |

The fix in each case was targeted tests that exercise the uncovered paths
without making real network calls or requiring API keys:

- `tests/test_fetcher.py` — added `_mock_github_full_client()` and five new
  tests for `_fetch_github_full`. The mock returns a plausible tree API
  response with two `.nf` files and one non-`.nf` file, verifying that only
  the correct files are fetched and concatenated.

- `tests/test_llm_client.py` — new file. Tests each provider routing branch
  using `monkeypatch` to set/unset environment variables and `patch` to mock
  `httpx.post`. Each test asserts both that the correct provider was called
  (by checking the URL in `mock_post.call_args`) and that the response is
  correctly parsed.

- `tests/test_doctor.py` — added `ContainerLatestTagFixer` tests and
  `_clean_image_response` unit tests. Added `test_doctor_*` tests to
  `test_cli.py` to cover the `doctor` CLI command paths.

**Resources:**
- [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
  — used in `test_llm_client.py` to set and unset environment variables
  cleanly within a single test without affecting other tests.
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/)
  — the `--cov-fail-under=80` flag makes the test run exit with a non-zero
  code if coverage drops below the threshold, which causes CI to fail.

---

## GitHub Actions CI

The CI config lives in `.github/workflows/ci.yml`. It runs on every push and
pull request to `main`/`master`.

Three jobs run in sequence:
```yaml
- name: Lint with ruff
  run: ruff check workflow_clinic/

- name: Type-check with mypy
  run: mypy workflow_clinic/ --ignore-missing-imports

- name: Run tests with coverage
  run: pytest tests/ -v --cov=workflow_clinic --cov-fail-under=80
```

The matrix runs against Python 3.11 and 3.12 to catch version-specific
behaviour early.

**Why these three checks specifically:**

- `ruff` catches style issues and common bugs (unused imports, undefined names)
  faster than any other Python linter. One command replaces flake8, isort,
  and pyupgrade.
- `mypy --ignore-missing-imports` catches type errors without requiring stubs
  for every third-party library. `--strict` would be ideal but requires
  annotating everything including test files — too noisy for a POC.
- `pytest --cov-fail-under=80` enforces the coverage floor. If a new feature
  is added without tests, CI fails. This is the mechanism that makes
  "maintain coverage" a real constraint rather than a suggestion.

**Resources:**
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [actions/setup-python](https://github.com/actions/setup-python)
  — the official action for setting up a Python version in CI.
- [Ruff documentation](https://docs.astral.sh/ruff/)

---

## The README

`README.md` is structured around a single question: *can someone who has never
seen this project before understand what it does and run it in under 5 minutes?*

The sections are ordered by that principle:

1. **Two-sentence description** — what it does, no jargon
2. **Install** — three commands, copy-paste ready
3. **Quick start** — three real CLI examples with real output
4. **Architecture diagram** — ASCII, no external tools needed to render
5. **LLM setup table** — the three free options, what each requires
6. **Real-world results table** — links to `results/` for credibility
7. **Gap report schema** — links to the Pydantic model for technical readers

The architecture diagram is plain ASCII rather than Mermaid because it renders
correctly in any context — GitHub, a terminal `cat`, a PDF export — without
requiring JavaScript.

---

## Real-world results in `results/`

The `results/` folder contains JSON gap reports from real Dockstore workflows
produced by `python scripts/collect_real_results.py`. These are committed to
the repo as static evidence — a mentor can open any file and see exactly what
the tool found on a real workflow without running anything.

The most interesting result is `nf-core_atacseq.json` — 88 gaps, cloud
readiness score 0.00, 51 CRITICAL containerization gaps across all its local
modules. This is the kind of workflow the full Workflow Clinic project is built
to fix at scale.

The `nf-core_rnaseq.json` result (score 1.00, 0 gaps) is equally important —
it shows the tool produces clean results on well-maintained workflows and is
not generating false positives on the nf-core gold standard.

---

## Coverage after Day 6
```
workflow_clinic/cli.py                   90%
workflow_clinic/core/fetcher.py          78%
workflow_clinic/core/llm_client.py       87%
workflow_clinic/doctor/...               90%
workflow_clinic/parsers/nextflow.py      97%
workflow_clinic/schema/gap_report.py    100%
workflow_clinic/critic/...              100%
─────────────────────────────────────────────
TOTAL                                    91%
```

The 3 missed lines in `parsers/nextflow.py` are the EOF-without-closing-brace
defensive path. The 22% miss in `fetcher.py` is the Dockstore full-repo path
(`_fetch_dockstore` with `full_repo=True`) and some 404-handling branches in
`_fetch_github_full`.

---

## What the full project builds on top of this

The POC is complete. The full GSoC project extends in four directions:

- **More workflow languages** — Snakemake, CWL, WDL parsers with their own
  rule sets and fix generators, following the exact same `BaseRule` /
  `BaseFixGenerator` pattern established here.
- **GitHub issue and PR creation** — the `GapReport` and `FixProposal` models
  are already designed for this. A `GitHubClient` wrapping PyGitHub posts
  issues from gap reports and PRs from fix proposals.
- **Image existence validation** — the TODO in `nextflow_fixes.py` becomes a
  real registry check against Biocontainers and Docker Hub APIs.
- **Agentic orchestration** — the CriticEngine and DoctorEngine are today
  called directly. In the full project they become agents in a LangGraph
  workflow, enabling multi-step reasoning, tool use, and human-in-the-loop
  review flows.
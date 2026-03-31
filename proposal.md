# GSoC 2026 Proposal: Workflow Clinic

**Applicant:** Aansh (B22AI058) \
**Project Track:** GA4GH Cloud Work Stream \
**Scope:** 350h — Workflow Critic + Workflow Doctor \
**Mentors:** Alexander Kanitz, Javed Habib, Anurag Gupta

---

## 1. Personal Statement & Motivation

I am a final-year AI student (Roll No. B22AI058) with hands-on experience in Python, LLM-based multi-agent pipelines, and scientific software engineering. My most relevant prior project is StudySphere `https://github.com/QuantTitan/StudySphere` — a LangChain-based multi-agent RAG teaching assistant with a FAISS vector store, an LLM-as-Judge evaluation layer, and a Google Cloud Run deployment — which gave me direct experience with the exact technology stack this project requires: LangGraph-style orchestration, tool-wrapped deterministic logic, and production CI.

I am drawn to Workflow Clinic because it is a problem I can reason about empirically. Before writing a line of proposal text, I built a working proof-of-concept: a Nextflow and Snakemake parser, a deterministic rule engine, an LLM-backed fix generator, and a GitHub issue and PR creation client. I ran this against eight real public Dockstore workflows and collected structured gap reports. The results — including a score of 0.00 / 1.00 and 88 gaps on nf-core/atacseq, and a confirmed successful issue and PR creation on a real repository — are committed to the public proof-of-concept repository at `github.com/electricdystopia/workflow-clinic`. This proposal is grounded in that evidence.

---

## 2. Problem Statement

The GA4GH Cloud Work Stream defines four interoperability standards: TRS (share tools and workflows), WES (execute full workflows on cloud platforms), TES (run individual jobs), and DRS (address data objects across clouds). These standards describe what a cloud-ready workflow must expose: a container image per task, explicit and typed input/output declarations, parameterized paths rather than hardcoded ones, and resource hints the scheduler can act on.

In practice, the majority of publicly registered workflows on Dockstore and WorkflowHub do not meet these requirements. The evidence is not merely anecdotal: the Yevis/DDBJ registry paper (PMC9944229, 2023) documents that workflow registry submissions lack systematic quality control, resulting in workflows that are "not reusable, such as those that lack dependencies, documentation, or the appropriate open-source license." The WorkflowHub Scientific Data paper (2025) observes that "workflows are scattered and difficult to find" and that "workflow sharing is not yet part of research practice," partly because no automated tooling enforces cloud-readiness at registration time.

Running my proof-of-concept Critic against eight real Dockstore workflows produced the following directly observed gap distribution:

| Workflow | Score | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|
| nf-core/rnaseq | 1.00 | 0 | 0 | 0 |
| nf-core/atacseq | 0.00 | 51 | 37 | 0 |
| nf-core/methylseq | 0.00 | 6 | 5 | 0 |
| erinyoung/roundabout | 0.00 | 1 | 10 | 0 |

A score of 1.00 for nf-core/rnaseq is evidence of specificity, not false negatives — it is one of the most mature community pipelines and fully conforms to nf-core module standards. A score of 0.00 for atacseq reflects 51 processes with no container directive, confirmed by manual inspection.

**Important caveat on scores:** A score of 1.00 means "passes all currently implemented checks," not "is fully cloud-ready." The implemented rules do not yet cover cloud executor profiles in `nextflow.config`, WES input schema validation, or FAIR metadata completeness. This distinction is explicit in the gap report schema via a `rules_applied` field and will be documented prominently in the tool.

Retroactively fixing thousands of workflows manually is not feasible. Workflow Clinic automates this: the Critic identifies gaps and files structured issues; the Doctor generates and submits validated code patches as PRs. The tool is designed to be run by registry operators, workflow authors, and CI systems, reducing the ongoing cost of cloudification to near zero for new workflows.

---

## 3. Deep Research: Portability Blockers

The gap categories defined in this project represent an original operational taxonomy synthesized from multiple authoritative sources, including the [GA4GH Workflow Execution Service (WES)](https://www.ga4gh.org/product/workflow-execution-service-wes/), and key publications ([Nature Biotech 2020](https://doi.org/10.1038/s41587-020-0439-x), [PMC9944229](https://pmc.ncbi.nlm.nih.gov/articles/PMC9944229/), [Scientific Data 2025](https://doi.org/10.1038/s41597-025-04786-3)).

No single source explicitly enumerates these categories. Instead, this taxonomy is a principled synthesis of the constraints these works collectively imply for workflows to be portable and executable within WES-compliant environments.

---

### 3.1 Missing or Incomplete Containerization

Containerization is a foundational requirement for reproducible and portable workflows. As noted in *Nature Biotechnology (2020)*, traditional pipelines are tightly coupled to local environments and sensitive to software and data version drift, whereas containerized workflows eliminate such dependencies.

WES-compatible execution engines (e.g., Cromwell on Terra, Toil) assume or enforce container-based execution.

**Common failure modes include:**

* Nextflow processes lacking a `container` directive
* Snakemake rules with `conda:` but no `singularity:` fallback
* WDL tasks missing `runtime { docker: ... }`
* CWL `CommandLineTool` definitions without `DockerRequirement`

Empirical results from the project’s proof-of-concept (POC) indicate that this is the most prevalent **critical** portability blocker.

---

### 3.2 Hardcoded Local Paths and Non-Cloud Storage

Many workflows rely on absolute filesystem paths (e.g., `/data/ref/hg38.fa`, `/scratch/tmp/`) for inputs, references, or intermediate data. These assumptions break in WES environments, where each execution occurs on a freshly provisioned virtual machine.

As highlighted in prior work, hardcoded paths prevent proper decoupling between workflow logic and execution environment.

**Required remediation:**

* Replace local paths with parameterized inputs
* Use URI-based storage compatible with distributed systems:

  * `drs://` (GA4GH DRS)
  * `s3://`, `gs://` (object storage)

The `STORAGE-001` rule detects such patterns using regex heuristics. Due to known false positives (e.g., shell substitutions like `s/foo//g`), a selective LLM-based adjudication step is planned.

---

### 3.3 Implicit, Undeclared, or Untyped I/O

WES promotes interoperability by abstracting execution across workflow languages and engines. However, this abstraction depends on explicitly declared and typed inputs/outputs.

Best practices (e.g., CWL guidelines) emphasize strict I/O specification.

**Common issues:**

* Implicit typing in Nextflow DSL1 channels
* Dynamic expansion patterns in Snakemake (`expand()`)
* Missing `secondaryFiles` in CWL, causing silent runtime failures

The `IO-001` rule detects missing output declarations. While useful, this remains a **syntactic check**; full semantic I/O validation is an open challenge.

---

### 3.4 Missing Resource Declarations

Cloud schedulers (AWS Batch, Google Life Sciences, Azure Batch) allocate compute resources based on declared requirements such as CPU and memory.

Absent or incomplete specifications lead to:

* Over-provisioning → unnecessary cost
* Under-provisioning → runtime failures (e.g., OOM in alignment/variant calling)

**Detection coverage:**

* `RESOURCE-001`, `RESOURCE-002` → Nextflow directives
* Equivalent checks for WDL (`runtime`) and CWL (`ResourceRequirement`)

Explicit resource specification is critical for both performance and cost optimization.

---

### 3.5 Non-Reproducible Software Pinning

Using mutable tags (e.g., `:latest`) in container images undermines reproducibility. Such tags may resolve to different images over time, violating the determinism expected in WES executions.

**Correct practices:**

* Use immutable digests: `image@sha256:<hash>`
* Use versioned, stable tags

Analogous issues arise in Snakemake when `conda:` environments reference mutable YAML files without content hashing.

**Rules:**

* `CONTAINER-002` → detects `:latest` usage
* `CONTAINER-003` → detects reliance on Conda without container isolation

---

### 3.6 Absent or Incomplete Workflow Metadata

TRS-compliant registries require rich metadata, including:

* Descriptions
* Licensing (SPDX identifiers)
* Test inputs
* Author information

Empirical studies show that many workflows lack sufficient metadata, limiting discoverability, validation, and reuse.

**Coverage:**

* `META-001` → license validation
* `META-002` → test parameter files
* `META-003` → README completeness

---

### 3.7 Missing Cloud Executor Profiles

Workflows often lack configuration for cloud execution backends.

**Example:**

```groovy
process.executor = 'awsbatch'
```

Without such profiles, workflows default to local or HPC schedulers, requiring manual refactoring for cloud deployment.

This significantly increases friction when migrating to elastic, cloud-native execution environments.

---

### 3.8 Insufficient WES Parameter Schema Validation

WES supports structured parameter validation via JSON schemas. However, many legacy workflows omit these schemas entirely.

**Implications:**

* No pre-execution validation of user inputs
* Increased risk of runtime failures
* Wasted compute resources on invalid jobs

Schema validation is a key mechanism for enforcing contract correctness between client and execution service.

---

### 3.9 Incomplete FAIR Metadata and Provenance Packaging

Beyond minimal metadata, workflows often fail to meet FAIR principles (Findable, Accessible, Interoperable, Reusable).

Standards such as RO-Crate aim to capture:

* Inputs and outputs
* Execution context
* Software dependencies
* Provenance metadata

Lack of FAIR packaging limits interoperability across platforms like WorkflowHub and reduces downstream reuse.

---

## Acknowledged Gaps in the Current Rule Set

While the current POC effectively identifies primary execution blockers, several complex cases remain unresolved:

* **Semantic I/O completeness** beyond syntactic declarations
* **Implicit binary dependencies** embedded in shell scripts
* **Dynamic constructs**, such as inline JavaScript evaluation in CWL

These limitations stem from the reliance on regex-based static analysis. Addressing them will require deeper program analysis and selective use of LLM-based reasoning.

---

## 4. Systems Architecture

### 4.1 Current POC State

The proof-of-concept at `github.com/electricdystopia/workflow-clinic` has the following components implemented and tested:

- **Parsers:** Nextflow DSL2 (line-by-line state machine) and Snakemake (indentation-based state machine), with a `ParserRegistry` factory for auto-detection by file extension
- **Critic engine:** 7 deterministic rules (CONTAINER-001/002/003, STORAGE-001, IO-001, RESOURCE-001/002) with a `GapReport` Pydantic schema
- **Doctor engine:** Model-agnostic `LLMClient` (Ollama, OpenAI, Anthropic, Gemini); `ContainerMissingFixer` and `ContainerLatestTagFixer` with unified diff output and parser re-validation
- **GitHub integration:** Issue creation with label management and deduplication, branch creation, file commit, and PR creation
- **Live fetching:** Dockstore TRS v2 API (including the `/files` endpoint for full-repo fetching) and GitHub Git Tree API
- **CI:** GitHub Actions with ruff, mypy, and pytest; 193 tests; 91% line coverage

This is not a prototype in the exploratory sense — it is a functioning tool with production-quality tests and real-world validation. The GSoC project extends this foundation in two directions: (1) agentic orchestration wrapping the existing pipeline, and (2) coverage of additional workflow languages (CWL, WDL) and gap categories.

### 4.2 Code Structure

```
workflow_clinic/
├── cli.py                        # Typer CLI: parse, critic, doctor commands
├── core/
│   ├── fetcher.py                # TRS API + GitHub Tree API fetcher
│   ├── github_client.py          # Issue, branch, commit, PR via httpx
│   └── llm_client.py             # Model-agnostic LLM wrapper
├── parsers/
│   ├── nextflow.py               # Nextflow DSL2 state machine parser
│   ├── snakemake.py              # Snakemake state machine parser
│   ├── registry.py               # ParserRegistry factory
│   ├── cwl.py                    # CWL parser (GSoC Phase 2)
│   └── wdl.py                    # WDL parser (GSoC Phase 2)
├── schema/
│   └── gap_report.py             # Pydantic GapReport, Gap, GapSummary
├── critic/
│   ├── engine.py                 # CriticEngine: runs all rules
│   └── rules/
│       ├── base.py               # Abstract BaseRule
│       ├── containerization.py   # CONTAINER-001/002/003
│       ├── storage.py            # STORAGE-001
│       ├── io_declaration.py     # IO-001
│       ├── resource_hints.py     # RESOURCE-001/002
│       └── reproducibility.py   # REPRO-001 (GSoC)
├── doctor/
│   ├── engine.py                 # DoctorEngine: runs fix generators
│   └── fix_generators/
│       ├── base.py               # BaseFixGenerator, FixProposal dataclass
│       └── nextflow_fixes.py     # ContainerMissingFixer, LatestTagFixer
└── agents/                       # GSoC addition: LangGraph orchestration
    ├── graph.py                  # LangGraph StateGraph definition
    ├── critic_agent.py           # CriticAgent: wraps CriticEngine as tool
    ├── doctor_agent.py           # DoctorAgent: wraps DoctorEngine as tool
    └── submission_agent.py       # SubmissionAgent: wraps GitHubClient as tool
```

### 4.3 Agentic Architecture: Option A → Option C

The agentic architecture follows a deliberate two-phase approach, chosen because the underlying tool implementations are already complete and the agentic layer is additive rather than a replacement.

**Phase A (primary deliverable): LangGraph multi-agent orchestration**

The existing `CriticEngine`, `DoctorEngine`, and `GitHubClient` are wrapped as LangGraph nodes in a `StateGraph`. An `OrchestratorAgent` manages state transitions and coordinates three specialized agents:

```
OrchestratorAgent (LangGraph StateGraph)
├── CriticAgent   → wraps CriticEngine deterministically
│                   (no LLM invocation for rule-based checks)
├── DoctorAgent   → wraps DoctorEngine with LLM tool calls
│                   (LLM invoked only for fix generation)
└── SubmissionAgent → wraps GitHubClient
                    (deterministic HTTP operations)
```

Each agent node has a defined input/output schema, explicit state transitions, and can fail and retry independently. The LangGraph `StateGraph` provides persistence, checkpointing, and the ability to resume a partial run — important for the mass-run milestone where processing hundreds of Dockstore workflows may span hours.

This architecture requires approximately 2-3 days of refactoring from the current POC state: the core logic is unchanged, the agents are wrappers. No existing tests break.

**Phase C (stretch goal, contingent on compute credits): ReAct reasoning agent**

If compute credits are secured through the GSoC stipend or GA4GH infrastructure access, the tool will be extended to a single ReAct agent with tool use:

```python
tools = [
    Tool("fetch_workflow",    fetch),
    Tool("run_critic",        CriticEngine().run),
    Tool("run_doctor",        DoctorEngine().run),
    Tool("create_issue",      GitHubClient.create_issue),
    Tool("create_pr",         GitHubClient.create_pull_request),
]
agent = create_react_agent(llm, tools)
```

The agent drives the entire pipeline through reasoning rather than hardcoded graph edges. The underlying tool implementations are identical to Phase A — the migration is purely at the orchestration layer. Phase C adds value for novel workflow patterns not covered by static rules, where the agent can reason about context rather than following a fixed decision tree. Without sufficient credits for LLM API calls across hundreds of workflows, this phase degrades gracefully to Phase A.

**Why this path rather than alternatives:** A single per-workflow-language agent (processing all workflows of a given type in parallel) was considered but deprioritized for the 350h scope — the parallelism benefit is real for the mass-run milestone but requires async refactoring of the HTTP layer, adding risk without changing the core analysis quality.

### 4.4 LLM Strategy

The tool is model-agnostic. No LLM is invoked for deterministic checks — `CONTAINER-001` (missing directive) is a boolean parse result; `RESOURCE-001` (missing cpus) is a field-presence check. The LLM is reserved for three tasks where deterministic rules are insufficient:

1. **Fix generation:** Suggesting a pinned container image for a given script block (`ContainerMissingFixer`, `ContainerLatestTagFixer`)
2. **Selective gap validation:** For ambiguous rules like `STORAGE-001`, an LLM judge distinguishes genuine hardcoded paths from false positives like sed expressions. Critically, the judge uses a separate prompt role ("you are a reviewer, not a fixer") and can use a different model than the fixer. The concern with LLM-as-judge is not circularity per se — production systems use it effectively — but rather cost-proportionality: applying LLM judgment only where deterministic rules have known ambiguity.
3. **PR and issue description generation:** Natural language summaries for human reviewers.

**Image existence validation (gap between current state and full reliability):** The Doctor currently validates fixes syntactically via parser re-parsing but cannot confirm a suggested container image actually exists on its registry. The planned addition is a registry check against the Biocontainers TRS v2 API (`https://api.biocontainers.pro/ga4gh/trs/v2/tools`) before awarding full confidence. A 404 response drops the proposal's `confidence` to 0.0 and sets `human_review_required=True`. This is the single most important gap between the current Doctor and a production-reliable one, and it is a Week 3-4 deliverable in the GSoC timeline.

**Biocontainers candidate injection for image suggestion:** Rather than asking the LLM to generate a container image name from scratch, `ContainerMissingFixer` first queries the Biocontainers TRS v2 API — `GET https://api.biocontainers.pro/ga4gh/trs/v2/tools?name={tool_name}&limit=10` — using the primary tool name extracted from the script block (the first non-shell-builtin command token, e.g. `bwa` from `bwa mem -t ${task.cpus} ...`). The verified image IDs from the response are injected into the prompt as a candidate list, shifting the LLM's task from open-ended generation to selecting among known-real options — a task small local models handle reliably. If the API returns no results the prompt falls back to open-ended generation, preserving current behaviour. This is a single `httpx.get` call with a 5-second timeout added before the LLM prompt is constructed.

---

## 5. Gap Report Data Model

The gap report is the core artifact of the Workflow Critic. It is a structured, versioned JSON document conforming to a Pydantic v2 schema. The current schema (`workflow_clinic/schema/gap_report.py`) is already implemented and producing real output. The GSoC project extends it with `workflow_type`, `registry_url`, `rules_applied`, and `by_category` summary fields.

```python
class GapReport(BaseModel):
    schema_version: str = "1.0.0"
    generated_at: datetime
    workflow_path: str
    workflow_type: WorkflowType        # NEXTFLOW | SNAKEMAKE | CWL | WDL
    registry_url: HttpUrl | None       # TRS identifier if fetched from registry
    rules_applied: list[str]           # Which rule IDs were checked
                                       # (makes score interpretation honest)
    overall_cloud_readiness_score: float   # 0.0–1.0
    gaps: list[Gap]
    summary: GapSummary

class Gap(BaseModel):
    gap_id: str                        # e.g. "CONTAINER-001"
    category: GapCategory
    severity: Severity
    location: CodeLocation
    description: str
    evidence: str
    recommendation: str
    references: list[HttpUrl]          # GA4GH specs, nf-core docs
    auto_fixable: bool
    rule_confidence: float             # 0.0–1.0: how reliable is this rule's
                                       # detection (CONTAINER-001 ≈ 1.0,
                                       # STORAGE-001 ≈ 0.7 due to regex FPs)
```

The `rules_applied` field is a deliberate design choice: a score of 1.00 means "passes all checks in `rules_applied`," not "is fully cloud-ready." This distinction is critical for honest reporting and will be prominently documented.

The `rule_confidence` field on `Gap` encodes known false-positive rates per rule. `CONTAINER-001` has near-zero FP rate (it's a boolean field presence check). `STORAGE-001` has a known FP rate from regex matching shell expressions. This metadata enables downstream tools and human reviewers to triage gaps appropriately.

The cloud readiness score uses severity-based penalties (CRITICAL: −0.25, MAJOR: −0.10, MINOR: −0.03), floored at 0.0. A more sophisticated category-weighted score is a documented stretch goal.

---

## 6. Workflow Critic: Detection Rules

The current implemented rules and the GSoC additions:

| Rule ID | Category | Languages | Detection | Status |
|---|---|---|---|---|
| CONTAINER-001 | Containerization | Nextflow | AST: missing `container` directive | ✅ Implemented |
| CONTAINER-002 | Reproducibility | All | Regex: `:latest` tag or no tag | ✅ Implemented |
| CONTAINER-003 | Reproducibility | Snakemake | AST: `conda:` without `singularity:` | ✅ Implemented |
| CONTAINER-004 | Containerization | CWL | Schema: missing `DockerRequirement` | GSoC Phase 2 |
| CONTAINER-005 | Containerization | WDL | AST: `task` missing `runtime { docker }` | GSoC Phase 2 |
| STORAGE-001 | Storage | All | Regex: absolute paths in script blocks | ✅ Implemented |
| IO-001 | I/O | Nextflow/Snakemake | AST: missing output declaration | ✅ Implemented |
| IO-002 | I/O | CWL | Schema: missing `secondaryFiles` | GSoC Phase 2 |
| IO-003 | I/O | WDL | AST: `File` input with no default | GSoC Phase 2 |
| RESOURCE-001 | Resources | Nextflow | AST: missing `cpus` directive | ✅ Implemented |
| RESOURCE-002 | Resources | Nextflow | AST: missing `memory` directive | ✅ Implemented |
| RESOURCE-003 | Resources | WDL | AST: `runtime` missing `memory`/`disks` | GSoC Phase 2 |
| REPRO-001 | Reproducibility | Nextflow | Regex: unpinned conda without lock | GSoC Phase 1 |
| META-001 | Metadata | All | File: missing LICENSE/SPDX | GSoC Phase 3 |
| META-002 | Metadata | All | File: no test parameter file | GSoC Phase 3 |

Parsers use established libraries where available: `miniwdl` for WDL (exposes a Python AST), `cwltool`'s schema loader for CWL. For Nextflow and Snakemake, custom state machine parsers are already implemented (see POC) — grammar-based parsers were considered and rejected for the POC due to the dependency overhead; the tradeoff is documented.

**Issue deduplication strategy:** Before creating a GitHub issue for a gap, the tool checks whether an equivalent issue already exists. Two scenarios require different handling.

**Scenario A — previous Workflow Clinic run.** Each issue body carries a deterministic HTML comment fingerprint derived from `gap_id + process_name + file_path` (e.g. `<!-- wc:fp:a3f9b2c1d4e5f678 -->`). Before creating an issue, `GitHubClient.find_existing_issue()` fetches open issues labelled `workflow-clinic` and scans their bodies for this fingerprint. A match appends an updated report as a comment; no match creates a new issue. An atomic all-or-nothing approach is deliberately rejected here: if a run fails mid-way through 11 gaps, atomicity would either require rolling back already-created issues (GitHub has no transaction API) or re-creating all 11 on retry, duplicating the successful ones. Per-gap fingerprinting means retries are safe and re-runs after partial fixes create issues only for the gaps that remain open.

**Scenario B — human-opened issues (stretch goal).** Fingerprinting cannot detect a human-written issue covering the same gap in different wording. If time and compute budget allow, semantic deduplication can be layered on top: fetch all open issues from the repo via the GitHub issues API (paginated at 100 per page), embed each issue's title and first ~500 characters of body using the same LLM provider already configured for the Doctor (an `embed()` method added to `LLMClient` following the same provider-routing pattern as `complete()`), embed the current gap's description, and compute cosine similarity in memory. Similarity above a configurable threshold (default 0.85) suppresses creation. The comparison is always against one repo's open issues at runtime — a small, transient set — so no persistent index is needed and the full comparison runs in milliseconds. This feature is gated behind a `--semantic-dedup` flag to avoid consuming embedding quota on every run; the fingerprint check runs unconditionally and costs nothing.

---

## 7. Workflow Doctor: Fix Generation

The fix pipeline per auto-fixable gap:

1. **Context assembly:** The relevant process/rule block (±20 lines) is extracted from the source. For `CONTAINER-001`, the script block is passed to the LLM as context so it can identify the actual tool being invoked rather than guessing from the process name alone.

2. **Fix generation:** The `DoctorAgent` receives the gap, evidence, and recommendation. For container fixes, a RAG step first queries the Biocontainers TRS v2 API to fetch candidate images for the detected tool, which are included in the prompt. The LLM selects from verified-real candidates rather than generating image names from memory.

3. **Response sanitization:** Small local models frequently append explanatory prose after the image name. `_clean_image_response()` extracts the first `registry/image:tag`-shaped token. This is already implemented and tested.

4. **Syntactic validation:** The patched source is re-parsed. If the parser finds the new directive with the expected value, `validation_passed=True`. This is a syntactic check, not a semantic one.

5. **Registry existence check (GSoC addition):** A HEAD request to the image registry confirms the suggested image actually exists. A 404 drops `confidence` to 0.0 and sets `human_review_required=True`. This closes the most significant gap between the current Doctor and a reliable one.

6. **Language-specific linting (stretch goal):** For workflows where linting is feasible without execution — `nextflow -syntax-check`, `snakemake --lint`, `cwltool --validate`, `miniwdl check` — the patched file is run through the linter and failures feed back as retry context.

The `FixProposal` schema includes `patched_content` (full patched file as a string) for the `--create-pr` path, where the content is committed directly to a fix branch without re-running the fixer.

**On WES semantic correctness:** Container directive additions are additive — they do not change the workflow's logic, channel topology, or parameter handling. A workflow that ran before our changes will almost certainly still run after them. The edge case where a suggested image lacks the required tool version is caught by registry validation combined with human review for sub-0.7 confidence proposals. Full WES execution testing (running the patched workflow on an actual WES platform) is outside the scope of a GSoC project but is documented as the correct long-term validation approach.

---

## 8. GitHub/GitLab Integration

The `GitHubClient` in `workflow_clinic/core/github_client.py` is fully implemented using raw `httpx` (which is already a project dependency) rather than PyGitHub, keeping the install footprint minimal and the test pattern consistent with the fetcher and LLM client.

**Issue creation (Critic):** One consolidated issue per workflow, with collapsible `<details>` blocks per gap (critical for workflows like atacseq with 88 gaps). Labels are created automatically if absent. Deduplication via fingerprint before POST.

**PR creation (Doctor):** One PR per validated fix proposal, from a branch named `{prefix}/{gap-id}/{process-name}` (e.g. `wf-clinic/container-001/align`). The PR body includes the before/after cloud readiness score, the unified diff in a code fence, a confidence indicator, and a human review disclaimer for proposals below 0.7 confidence.

**On PR conventions for non-nf-core repos:** The tool uses a fixed, well-structured PR template that is self-documenting for maintainers who have never seen Workflow Clinic. Parsing each target repo's `CONTRIBUTING.md` to infer PR conventions is documented as a stretch goal for non-nf-core workflows.

---

## 9. Coding Best Practices

**Testing:** Test-driven development throughout. The POC already has 193 tests at 91% line coverage. Unit tests cover every detection rule against clean/broken/partial fixtures per language. Integration tests run the full pipeline against real Dockstore workflows. Target: ≥90% coverage maintained throughout. CI on every push via GitHub Actions (ruff, mypy, pytest).

**Type safety:** All data models use Pydantic v2. Function signatures are fully annotated; mypy validation runs in CI.

**Documentation:** All public functions carry docstrings with file path references and external references for non-obvious patterns. A MkDocs site with `mkdocstrings` is a Week 21 deliverable.

**LLM safety:** All LLM-generated content passes through a sanitization step before being written to issues or PRs, preventing prompt injection via malicious workflow comments.

**Reproducibility:** Distributed as a `pyproject.toml`-based package with pinned dependencies and a published CLI entry point (`workflow-clinic`).

---

## 10. Workflow Language Coverage Plan

| Phase | Languages | Deliverable |
|---|---|---|
| Phase 1 (Weeks 1–4) | Nextflow (DSL2) — extend POC | Registry validation, RAG image lookup, REPRO-001 rule, LangGraph agent wrapping |
| Phase 2 (Weeks 5–9) | + Snakemake (extend POC) + CWL | Snakemake Doctor; CWL parser + CONTAINER-004, IO-002 rules; issue creation for all three |
| Phase 3 (Weeks 10–14) | + WDL | WDL parser + CONTAINER-005, IO-003, RESOURCE-003; Doctor for Snakemake and CWL |
| Phase 4 (Weeks 15–18) | All | Doctor ported to WDL; metadata rules META-001/002; Option C stretch (if credits available) |
| Phase 5 (Weeks 19–22) | All | Mass-run on Dockstore/WorkflowHub; docs; community feedback |

Nextflow and Snakemake are already substantially implemented. The GSoC project's parser work is primarily CWL and WDL.

---

## 11. Detailed Timeline (350h over 22 weeks)

| Weeks | Focus | Deliverables | Hours |
|---|---|---|---|
| 1–2 | Community bonding; deep-dive into TRS/WES specs; registry validation implementation | Biocontainers registry check in Doctor; RAG image lookup; finalized gap schema v1.0 | 20h |
| 3–4 | LangGraph agent wrapping; REPRO-001 rule; extend POC test suite | OrchestratorAgent + CriticAgent + DoctorAgent in LangGraph; ≥90% coverage maintained | 30h |
| 5–6 | Snakemake Doctor (fix generators for Snakemake-specific gaps) | ContainerMissingFixer for Snakemake; end-to-end Critic→Doctor→PR for Snakemake | 25h |
| 7–9 | CWL parser + Critic rules; CWL issue creation | CWL CONTAINER-004, IO-002 rules; CWL fixtures; CWL issue creation | 40h |
| 10–11 | WDL parser + Critic rules | WDL CONTAINER-005, IO-003, RESOURCE-003 rules; miniwdl integration | 30h |
| 12–13 | Doctor for Snakemake and CWL; PR creation for both | End-to-end Critic→Doctor→PR for Snakemake and CWL | 30h |
| 14 | Buffer/contingency — integration testing, bug fixes | All Phase 1–3 tests passing at ≥90% coverage | 15h |
| 15–16 | WDL Doctor; metadata rules META-001/002 | WDL fix generators; metadata rule implementation across all languages | 30h |
| 17–18 | Option C stretch (if credits available); otherwise: deduplication embedding layer | ReAct agent OR semantic issue deduplication via embeddings | 25h |
| 19–20 | Mass-run on Dockstore/WorkflowHub; triage and submit issues/PRs | 50+ real issues filed; 10+ PRs raised; empirical gap distribution data | 30h |
| 21 | Documentation: MkDocs site, user guide, API docs | Published docs site | 15h |
| 22 | Final review, mentor feedback, code freeze, GSoC submission | Final report, tagged release v1.0.0 | 10h |
| **Total** | | | **350h** |

The Week 14 buffer is deliberate — LLM-based fix generation for CWL and WDL is less proven than for Nextflow, and the validation loop (syntax check + registry check + optional linting) may require iteration.

---

## 12. Expected Impact

By the end of this project, Workflow Clinic will have:

Filed structured, actionable gap report issues across hundreds of Nextflow, Snakemake, CWL, and WDL workflows on Dockstore and WorkflowHub, with empirical data on the most common portability blockers — data that can directly inform TRS feedback endpoint improvements and WES structured I/O schema extensions.

Raised PRs with validated, registry-confirmed code-level fixes for all auto-fixable gaps, covering at minimum containerization gaps (CONTAINER-001 through CONTAINER-005) across all four supported languages.

Produced a reusable, extensible Python tool — installable from PyPI, documented, and CI-tested at ≥90% coverage — that any registry operator, workflow author, or CI system can run to make "cloud-ready by default" the standard for new workflow submissions.

Demonstrated a concrete agentic architecture (LangGraph orchestrator + specialized agent nodes) that is en route to a fully reasoning ReAct agent given additional compute credits, with the underlying tool implementations unchanged between the two modes.

---

*The proof-of-concept implementation supporting this proposal is available at `github.com/electricdystopia/workflow-clinic`. Real gap reports from eight Dockstore workflows, 193 passing tests, and a successful live issue and PR creation on a real repository are available for review.*
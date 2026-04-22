# Agent Team Orchestrator

[![Release](https://img.shields.io/github/v/release/DeclanJeon/agent-team-orchestrator?sort=semver)](https://github.com/DeclanJeon/agent-team-orchestrator/releases)
[![CI](https://github.com/DeclanJeon/agent-team-orchestrator/actions/workflows/ci.yml/badge.svg)](https://github.com/DeclanJeon/agent-team-orchestrator/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/DeclanJeon/agent-team-orchestrator)](./LICENSE)
[![Stars](https://img.shields.io/github/stars/DeclanJeon/agent-team-orchestrator?style=social)](https://github.com/DeclanJeon/agent-team-orchestrator/stargazers)

Document-first multi-agent organization pack for Hermes.

This project helps you run AI agents like a real product team without role collision.
Instead of throwing multiple agents at the same codebase and hoping for the best, it fixes:
- role boundaries
- source-of-truth documents
- handoff contracts
- change-request flow
- review and integration gates

It ships as a local Hermes skill plus a one-click bootstrap flow.

## What this gives you

- Hermes skill: `agent-team-orchestrator`
- one-click installer: `./install.sh`
- one-click project bootstrapper: `agent-team-bootstrap`
- uninstall script: `./uninstall.sh`
- release packaging helper: `./package-release.sh`
- quick installer for hosted tarballs: `./quick-install.sh`
- operating model for a full AI org, not just dev lanes
- prompt catalog for each role
- templates for PRD, task board, task instruction, change request, UI spec, and API spec
- operator playbook for recommended execution order: `docs/OPERATOR_PLAYBOOK.md`
- a seeded example workspace: `examples/minimal-product/`
- versioned social preview asset: `assets/social-preview.svg`

## Supported team structure

Decision / coordination lanes
- Orchestrator
- Product Owner
- PM / Service Planner
- Prompt / Workflow Designer
- System Architect
- Reviewer / Senior Engineer

Execution lanes
- UX Research / UXUI
- Frontend Engineer
- Backend Engineer
- Data Engineer
- AI Engineer
- QA Engineer
- DevOps / Platform
- Security Engineer
- Operations / CS
- Growth / Marketing
- Integrator

## Repository structure

```text
agent_team/
├─ docs/
│  ├─ AGENT_TEAM_OPERATING_TEMPLATE.md
│  └─ HERMES_APPLY_GUIDE.md
├─ pack/
│  └─ skill/
│     ├─ SKILL.md
│     ├─ references/
│     ├─ scripts/
│     └─ templates/
└─ install.sh
```

## Quick start

### 1. Install the skill into Hermes

```bash
cd /path/to/agent_team
./install.sh
```

### 2. Verify installation

```bash
hermes skills list | grep agent-team-orchestrator
```

### 3. Bootstrap a new project

```bash
~/.local/bin/agent-team-bootstrap /path/to/project --project-name "My Project"
```

### 4. Start Hermes with the skill loaded

```bash
hermes -s agent-team-orchestrator
```

### 5. Package a release tarball

```bash
./package-release.sh v1.0.0
```

### 6. Uninstall locally

```bash
./uninstall.sh
```

## What bootstrap creates

The bootstrap script generates a document-first workspace including:
- product docs with structured sections for vision, priorities, and success metrics
- planning docs with backlog, release scope, milestones, and a seeded multi-lane task board
- architecture docs with system overview, module boundaries, tech decisions, and integration contract
- design docs with IA, user flow, wireframes, design system, and per-screen UI spec scaffold
- backend/db docs with API spec, domain model, error policy, and ERD
- data/AI docs with data flow, event schema table, ETL plan, model IO contract, and evaluation plan
- review/security/ops/growth docs with practical tables/checklists instead of empty placeholders
- lane-specific task instruction samples under `docs/task_instructions/`
- role prompt files for each lane
- QA, infra, and final integration/runbook files

## Core operating rules

- Do not start parallel implementation before the baseline docs exist.
- Do not let one lane directly rewrite another lane's contract.
- Use change requests for cross-lane contract changes.
- Keep integration gated by review, QA, and approval state.
- Treat Product + PRD + UI/API/ERD + module boundaries as the minimum source-of-truth set.

## What you get from this skill

### 1. Clear role boundaries
When multiple AI agents work at once, the most common failure mode is role collision.
This skill reduces that by fixing:
- what each lane is responsible for
- what each lane must not change
- what documents each lane reads
- what outputs each lane is expected to produce

### 2. Safer parallel execution
Instead of opening frontend, backend, data, and AI work all at once with no contract, this skill forces a document-first sequence.
That means parallel work happens after key source-of-truth documents exist, such as:
- product vision / priorities
- PRD
- UI spec
- API spec
- ERD
- module boundaries

### 3. Better output quality
The skill does not stop at lane assignment.
It also builds in quality gates such as:
- reviewer gate
- security gate
- QA gate
- integrator final pass

This makes it much harder to merge plausible-but-wrong output directly into the final result.

### 4. Faster project kickoff
The included bootstrap flow creates a ready-to-use project workspace with:
- product documents
- design and architecture documents
- backend / data / AI contracts
- QA / security / ops / growth docs
- role prompts
- seeded task board
- lane task instruction samples

So a new project starts from an organized operating structure instead of an empty directory.

### 5. Reusable team operating model
Instead of re-explaining the same collaboration rules every session, this skill packages them into a repeatable operating system:
- lane boundaries
- handoff rules
- review gates
- change request flow
- bootstrap conventions

That makes the approach reusable across projects, not just within a single conversation.

### 6. Human decision points stay explicit
This skill is designed so AI lanes can move fast without taking over irreversible product decisions.
Important checkpoints still stay visible for human approval, especially around:
- scope
- release readiness
- risk acceptance
- final integration

### Where it helps most
This skill is especially useful when you want to:
- run several AI agents like a real team
- split product, design, engineering, QA, security, ops, and growth work
- reduce cross-lane interference
- bootstrap a new project quickly
- keep parallel implementation grounded in shared contracts

### Where it is probably overkill
For very small tasks, this structure can be heavier than necessary, for example:
- one-off scripts
- tiny bug fixes
- single-file edits
- very small prototypes with no parallel work

In those cases, a single agent or a much lighter workflow is usually faster.

## Key files

- `pack/skill/SKILL.md`
- `pack/skill/references/operating-model.md`
- `pack/skill/references/prompt-catalog.md`
- `pack/skill/references/starter-prompts.md`
- `pack/skill/evals.json`
- `pack/skill/scripts/bootstrap_project.py`
- `pack/skill/templates/product-vision.md`
- `pack/skill/templates/review-report.md`
- `pack/skill/templates/event-schema.md`
- `docs/AGENT_TEAM_OPERATING_TEMPLATE.md`
- `docs/HERMES_APPLY_GUIDE.md`
- `docs/OPERATOR_PLAYBOOK.md`
- `docs/SOCIAL_PREVIEW_SETUP.md`
- `examples/minimal-product/README.md`
- `assets/social-preview.svg`

## Example workflow

```bash
./install.sh
~/.local/bin/agent-team-bootstrap ~/work/my-product --project-name "My Product"
cd ~/work/my-product
hermes -s agent-team-orchestrator
```

Then fill these first:
- `docs/product/vision.md`
- `docs/product/priorities.md`
- `docs/PRD.md`
- `docs/design/ui_spec.md`
- `docs/backend/api_spec.yaml`
- `docs/db/erd.md`
- `docs/task_board.md`

Only after that should you open parallel implementation lanes.

If you want ready-to-paste prompts, start from:
- `pack/skill/references/starter-prompts.md`

If you want the recommended order of operation for a real project, read:
- `docs/OPERATOR_PLAYBOOK.md`

If you want a concrete seeded example workspace, open:
- `examples/minimal-product/`

If you want to set the GitHub social preview image, use:
- `assets/social-preview.svg`
- `docs/SOCIAL_PREVIEW_SETUP.md`

## Verification

Verified locally:
- installer dry-run
- installer real run
- Hermes skill visibility
- bootstrap script execution
- Python syntax check for bootstrap script

## Rollback

```bash
rm -rf ~/.hermes/skills/agent-team-orchestrator
rm -f ~/.local/bin/agent-team-bootstrap
```

Or simply run:

```bash
./uninstall.sh
```

## Release packaging

```bash
./package-release.sh v1.0.0
SKILL_REPO_URL="https://github.com/DeclanJeon/agent-team-orchestrator/releases/download/v1.0.0/agent-team-orchestrator-v1.0.0.tar.gz" ./quick-install.sh
```

## License

MIT

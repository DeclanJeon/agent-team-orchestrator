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
- operating model for a full AI org, not just dev lanes
- prompt catalog for each role
- templates for PRD, task board, task instruction, change request, UI spec, and API spec

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

## What bootstrap creates

The bootstrap script generates a document-first workspace including:
- product docs: vision, priorities, success metrics
- planning docs: PRD, backlog, release scope, milestones, task board
- architecture docs: system overview, module boundaries, integration contract
- design docs: IA, user flow, wireframes, design system, UI spec
- backend/db docs: API spec, domain model, error policy, ERD
- data/AI docs: data flow, event schema, ETL plan, model IO contract, evaluation plan
- review/security/ops/growth docs
- role prompt files for each lane
- QA, infra, and final integration/runbook files

## Core operating rules

- Do not start parallel implementation before the baseline docs exist.
- Do not let one lane directly rewrite another lane's contract.
- Use change requests for cross-lane contract changes.
- Keep integration gated by review, QA, and approval state.
- Treat Product + PRD + UI/API/ERD + module boundaries as the minimum source-of-truth set.

## Key files

- `pack/skill/SKILL.md`
- `pack/skill/references/operating-model.md`
- `pack/skill/references/prompt-catalog.md`
- `pack/skill/scripts/bootstrap_project.py`
- `docs/AGENT_TEAM_OPERATING_TEMPLATE.md`
- `docs/HERMES_APPLY_GUIDE.md`

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

## License

MIT

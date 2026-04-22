# Operator Playbook

This playbook explains how to run the repository assets in the intended order.

## 1. Install and bootstrap
```bash
./install.sh
~/.local/bin/agent-team-bootstrap /path/to/project --project-name "My Project"
```

## 2. Fill source-of-truth docs first
Minimum baseline before parallel work:
- docs/product/vision.md
- docs/product/priorities.md
- docs/PRD.md
- docs/design/ui_spec.md
- docs/backend/api_spec.yaml
- docs/db/erd.md
- docs/task_board.md
- docs/architecture/module_boundaries.md

## 3. Choose a launch mode
### Mode A: start from ready-made prompts
Use:
- `pack/skill/references/starter-prompts.md`

Best when you want Hermes-ready prompts immediately.

### Mode B: start from lane task instructions
Use generated project files under:
- `docs/task_instructions/*.md`

Best when you want to hand specific work packets to each lane.

## 4. Recommended execution order
1. Product Owner
2. PM
3. UXUI + Architect + Prompt/Workflow
4. Backend + Data + AI contracts
5. Reviewer gate
6. Frontend / Backend / Data / AI / DevOps implementation
7. Security + QA gate
8. Ops + Growth prep
9. Integrator final pass

## 5. Asset map
### Repository assets
- `pack/skill/references/operating-model.md`
- `pack/skill/references/prompt-catalog.md`
- `pack/skill/references/starter-prompts.md`
- `pack/skill/evals.json`

### Generated project assets
- `docs/task_instructions/*.md`
- `prompts/*.md`
- `docs/*`

## 6. How to use the example workspace
See:
- `examples/minimal-product/`

Use it when you want to understand what a lightly-seeded real project looks like after kickoff.

## 7. Recommended human checkpoints
- after Product + PM docs
- after contract docs
- after Reviewer gate
- before release after Security + QA

## 8. Anti-mixing rules
- do not let FE edit API spec directly
- do not let BE rewrite UI spec directly
- do not skip Reviewer/QA just because docs exist
- do not treat starter prompts as substitutes for approvals

---
name: agent-team-orchestrator
description: Run a document-first multi-agent product organization on Hermes. Use this whenever the user wants a full AI team split into PO, PM, UX/UI, frontend, backend, data, AI, QA, DevOps, security, operations, growth, reviewer, architect, prompt-workflow, and integrator lanes with strict role boundaries, handoff contracts, approval flow, and project bootstrap before any parallel implementation starts.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [team-orchestration, multi-agent, document-first, prompts, task-board, integration, qa, product, security, growth]
    related_skills: [ai-team-orchestration, hermes-agent, planning-with-files, subagent-driven-development]
---

# Agent Team Orchestrator

이 스킬은 단순히 개발 lane만 나누는 스킬이 아니다.
제품 방향 결정부터 운영/성장까지 포함한 전체 AI 조직을 Hermes 위에서 문서 중심으로 굴리기 위한 운영 스킬이다.

핵심 원칙
- 문서가 기준이고, 사람 승인자가 최종 방향을 확정한다.
- 각 역할은 자기 산출물만 만든다.
- 다른 역할 산출물은 직접 수정하지 않고 change request를 올린다.
- 병렬 실행 전에 기준 문서와 인터페이스 계약을 먼저 만든다.
- 리뷰와 QA 근거 없이 통합하지 않는다.
- 작은 팀에서는 여러 역할을 묶어도 되지만, 산출물 경계는 유지한다.

## When to use
- 사용자가 여러 에이전트를 팀처럼 운영하고 싶을 때
- PO/PM/UXUI/FE/BE/Data/AI/QA/DevOps/Security/Ops/Growth까지 분리하고 싶을 때
- 에이전트끼리 일이 섞이지 않게 역할 경계와 승인 절차가 필요할 때
- Hermes에서 프로젝트를 문서-first로 부트스트랩하고 싶은 때
- 구현 이전에 PRD, UI, API, ERD, 보안, 운영, 성장, QA 기준을 먼저 깔아야 할 때

## Read in this order
1. `references/operating-model.md` — 전체 조직 구조, 문서 체계, 승인 규칙
2. `references/prompt-catalog.md` — 역할별 프롬프트
3. `references/starter-prompts.md` — Hermes에 바로 붙여넣는 스타터 프롬프트 세트
4. `templates/*` — task board, task instruction, change request, PRD, UI, API 템플릿
5. `scripts/bootstrap_project.py` — 프로젝트 초기 문서/프롬프트 골격 생성기

## Full role map
### Decision / Coordination lanes
- Orchestrator: 전체 작업 분해, 승인 흐름, 충돌 조정
- Product Owner (PO): 왜 만드는지, 무엇을 포기하는지, 제품 방향과 우선순위 확정
- PM / Service Planner: PRD, backlog, scope, milestone 관리
- System Architect: 시스템 구조, 모듈 경계, 인터페이스 결정
- Reviewer / Senior Engineer: 산출물 리뷰, 구조/품질/보안/현실성 점검
- Prompt / Workflow Designer: 에이전트 프롬프트, 자동화 규칙, workflow 설계

### Execution lanes
- UX Research / UX/UI: 사용자 흐름, IA, wireframe, UI spec, design system
- Frontend: 화면 구현, 상태 관리, API 연동, component map
- Backend: API, 인증, 도메인 로직, persistence, error policy
- Data Engineer: 데이터 모델, ETL, 추적 스키마, 이벤트 설계
- AI Engineer: AI feature spec, prompt contract, evaluation plan, inference/runtime integration
- QA: test cases, regression, release readiness
- DevOps / Platform: 배포, env, CI/CD, monitoring, rollback
- Security: threat model, access control, privacy, security checklist
- Operations / CS: FAQ, support flow, 운영 정책
- Growth / Marketing: growth hypotheses, funnel events, experiment log, launch content outline
- Integrator: 승인된 산출물만 최종 병합

## Recommended team bundles by scale
### MVP 1~3인
- PO/PM 묶음
- UX/UI + Prompt Designer 묶음
- Fullstack (FE+BE)
- QA + DevOps 최소 묶음

### 4~8인 스타트업형
- PO
- PM
- UX/UI
- Frontend
- Backend
- QA
- DevOps
- Data/AI는 제품 성격에 따라 추가

### 10인 이상 서비스형
- PO / PM / UX Research / UI Design
- Frontend team
- Backend team
- Data Engineer / AI Engineer
- QA
- DevOps / Platform / Security
- Operations / Growth
- Reviewer / Architect

## Required baseline documents before parallel implementation
아래 문서가 없으면 구현 lane를 병렬 실행하지 않는다.
- `docs/product/vision.md`
- `docs/product/priorities.md`
- `docs/PRD.md`
- `docs/design/ui_spec.md`
- `docs/backend/api_spec.yaml`
- `docs/db/erd.md`
- `docs/task_board.md`
- `docs/architecture/module_boundaries.md`

## Handoff contracts
- PO → PM: vision, priorities, success metrics
- PM → UX/UI / Architect / Backend: PRD, scope, acceptance criteria
- UX/UI → Frontend: UI spec, design system, user flow
- Architect → FE/BE/Data/AI/DevOps: module boundaries, integration rules
- Backend → Frontend / QA: API spec, auth rules, error policy
- Data Engineer → AI/Growth: event schema, data flow, source contracts
- AI Engineer → Backend/QA: prompt contract, evaluation plan, model IO contract
- QA → Integrator / Release approver: bug report, release readiness
- Security → DevOps / Integrator: threat model, access control, release blockers
- Ops/Growth → Product: FAQ, feedback themes, experiment priorities

## Non-negotiable boundaries
- Frontend는 `api_spec.yaml`을 직접 수정하지 않는다.
- Backend는 `ui_spec.md`를 직접 수정하지 않는다.
- QA는 요구사항을 새로 만들지 않는다.
- Growth는 제품 기능 범위를 임의 확장하지 않는다.
- Security는 위험을 보고하지만 제품 우선순위를 대신 결정하지 않는다.
- Reviewer는 직접 구현보다 판단과 피드백을 우선한다.
- Integrator는 Approved 상태 산출물만 포함한다.

## Minimal orchestration flow
1. Orchestrator + PO + PM이 vision / priorities / PRD / task board를 만든다.
2. UX/UI + Architect + Prompt/Workflow Designer를 병렬 실행한다.
3. Backend + Data Engineer + AI Engineer가 계약 문서를 만든다.
4. Reviewer가 1차 구조 리뷰를 한다.
5. Frontend / Backend / Data / AI / DevOps를 병렬 구현한다.
6. Security + QA + Reviewer가 검증한다.
7. Ops/Growth가 운영/출시 준비 문서를 만든다.
8. Integrator가 최종 병합한다.
9. 사람 승인자가 릴리즈 여부를 결정한다.

## delegate_task pattern
각 lane에는 반드시 아래가 있어야 한다.
- 입력 문서 경로
- 출력 경로
- 금지 범위
- 완료 기준
- 후속 handoff 대상

예:
```python
delegate_task(tasks=[
  {
    "goal": "PO lane — define vision, priorities, success metrics",
    "context": "Output only under docs/product/. Read user request first.",
    "toolsets": ["file"]
  },
  {
    "goal": "PM lane — write PRD, backlog, release scope, task board",
    "context": "Read docs/product/vision.md and docs/product/priorities.md first.",
    "toolsets": ["file"]
  }
])
```

## Use these templates
Core
- `templates/task-board.md`
- `templates/task-instruction.md`
- `templates/change-request.md`
- `templates/PRD.md`
- `templates/ui-spec.md`
- `templates/api-spec.yaml`

Expanded planning / governance
- `templates/product-vision.md`
- `templates/product-priorities.md`
- `templates/success-metrics.md`
- `templates/approval-log.md`
- `templates/review-report.md`
- `templates/event-schema.md`

## Bootstrap
```bash
python3 scripts/bootstrap_project.py /path/to/project --project-name "Example App"
```

이 스크립트는 제품/설계/개발/데이터/보안/운영/성장 문서 골격과 역할별 프롬프트를 생성한다.
기본 placeholder만 만드는 수준이 아니라, task board / review / growth / security / QA 문서에 바로 채워 넣을 수 있는 표와 체크리스트를 함께 만든다.

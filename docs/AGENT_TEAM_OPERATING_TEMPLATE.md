# AI 에이전트 개발 조직 운영 템플릿

## 1. 목적
여러 AI 에이전트를 활용해 하나의 제품/서비스를 만들 때 역할이 섞이지 않도록 분리하고, 각 산출물을 통합해 최종 결과물을 만들기 위한 운영 기준 문서다.

핵심 목표
- 역할과 책임을 명확히 구분한다.
- 권한 밖 작업을 금지해 충돌을 줄인다.
- 산출물 형식을 표준화한다.
- 검수와 승인 절차로 품질을 유지한다.
- 실행 가능한 하나의 결과물로 병합한다.

## 2. 운영 원칙
| 원칙 | 설명 |
|---|---|
| 단일 책임 원칙 | 각 에이전트는 하나의 핵심 역할만 맡는다. |
| 문서 우선 원칙 | 의견 충돌 시 승인된 문서를 우선한다. |
| 직접 수정 금지 원칙 | 다른 팀 산출물을 임의로 수정하지 않는다. |
| 산출물 계약 원칙 | 모든 작업은 정해진 입력과 출력 포맷을 가진다. |
| 중앙 승인 원칙 | 방향 변경은 총괄 에이전트 또는 사람 책임자가 승인한다. |
| 검수 후 통합 원칙 | 검토되지 않은 산출물은 최종 결과물에 포함하지 않는다. |

## 3. 전체 조직 구조
### 3.1 의사결정/조정 계층
| 역할 | 목적 | 주요 산출물 |
|---|---|---|
| Orchestrator | 전체 목표 분해, lane 배정, 승인 흐름 관리 | task board, task instruction, approval log |
| Product Owner | 제품 방향, 우선순위, 범위 결정 | `docs/product/vision.md`, `docs/product/priorities.md` |
| PM / Service Planner | 요구사항과 릴리즈 범위 정리 | `docs/PRD.md`, `docs/backlog.md`, `docs/release_scope.md` |
| System Architect | 시스템 구조와 경계 정의 | `docs/architecture/*` |
| Reviewer / Senior Engineer | 산출물 품질/현실성 점검 | `docs/review/*` |
| Prompt / Workflow Designer | 프롬프트와 워크플로 설계 | `docs/agent-workflow/*` |

### 3.2 실행 계층
| 역할 | 목적 | 주요 산출물 |
|---|---|---|
| UX Research / UX/UI | 사용자 흐름과 화면 구조 설계 | `docs/design/*` |
| Frontend Engineer | 화면 구현과 사용자 인터랙션 | `frontend/*`, `docs/frontend/*` |
| Backend Engineer | API, 인증, 비즈니스 로직, 저장소 | `backend/*`, `docs/backend/*`, `docs/db/erd.md` |
| Data Engineer | 이벤트/데이터 흐름/적재 구조 설계 | `docs/data/*`, `data/*` |
| AI Engineer | AI 기능/평가/모델 입력출력 설계 | `docs/ai/*` |
| QA Engineer | 테스트/회귀/릴리즈 판정 근거 | `qa/*` |
| DevOps / Platform | 배포/운영/CI/CD/모니터링 | `infra/*` |
| Security Engineer | 위협 모델/권한/개인정보/보안 정책 | `docs/security/*` |
| Operations / CS | 운영 정책/FAQ/고객 대응 규칙 | `docs/ops/*` |
| Growth / Marketing | 성장 가설/측정/출시 메시지 | `docs/growth/*` |
| Integrator | 승인 산출물 최종 병합 | `release/*`, `docs/final/*` |

## 4. 프로젝트 규모별 추천 조합
### 4.1 MVP 1~3인
- PO + PM
- UX/UI + Prompt/Workflow
- Fullstack (FE+BE)
- QA + DevOps 최소 조합

### 4.2 4~8인 스타트업형
- PO
- PM
- UX/UI
- Frontend
- Backend
- QA
- DevOps
- Data/AI 선택 추가

### 4.3 10인 이상 서비스형
- PO, PM, UX Research, UI Design
- Frontend team
- Backend team
- Data Engineer, AI Engineer
- QA
- DevOps / Platform
- Security
- Operations / Growth
- Reviewer / Architect

## 5. 역할별 입력/출력/금지 범위
### 5.1 Orchestrator
- 입력: 사용자 요구사항, 기존 문서, 사업 제약
- 출력: `docs/task_board.md`, `docs/approval_log.md`, 역할별 task instruction
- 금지: 세부 구현 직접 개입

### 5.2 Product Owner
- 입력: 사업 목표, 사용자 문제, 시장/전략 맥락
- 출력: `docs/product/vision.md`, `docs/product/priorities.md`, `docs/product/success_metrics.md`
- 금지: 세부 구현 지시, UI/API 직접 설계

### 5.3 PM / Service Planner
- 입력: vision, priorities
- 출력: `docs/PRD.md`, `docs/backlog.md`, `docs/release_scope.md`, `docs/milestones.md`
- 금지: 코드 작성, DB 구조 결정

### 5.4 UX Research / UXUI
- 입력: PRD, 사용자 시나리오, 브랜드 방향
- 출력: `docs/design/information_architecture.md`, `docs/design/user_flow.md`, `docs/design/wireframes.md`, `docs/design/design_system.md`, `docs/design/ui_spec.md`
- 금지: API 구조 변경, 제품 범위 확장

### 5.5 Prompt / Workflow Designer
- 입력: task board, team structure, product constraints
- 출력: `docs/agent-workflow/system_map.md`, `docs/agent-workflow/prompt_contract.md`, `docs/agent-workflow/automation_rules.md`
- 금지: 제품 요구사항 변경

### 5.6 System Architect
- 입력: PRD, UI 방향, 기술 제약
- 출력: `docs/architecture/system_overview.md`, `docs/architecture/module_boundaries.md`, `docs/architecture/tech_decisions.md`, `docs/architecture/integration_contract.md`
- 금지: 세부 카피 작성

### 5.7 Frontend Engineer
- 입력: UI spec, design system, API spec
- 출력: `frontend/*`, `docs/frontend/component_map.md`, `docs/frontend/integration_notes.md`
- 금지: API 명세 임의 수정

### 5.8 Backend Engineer
- 입력: PRD, architecture, domain rules
- 출력: `backend/*`, `docs/backend/api_spec.yaml`, `docs/backend/domain_model.md`, `docs/backend/error_policy.md`, `docs/db/erd.md`
- 금지: UX 흐름 재정의

### 5.9 Data Engineer
- 입력: PRD, architecture, analytics/growth needs
- 출력: `docs/data/data_flow.md`, `docs/data/event_schema.md`, `docs/data/etl_plan.md`
- 금지: 제품 목표 재정의

### 5.10 AI Engineer
- 입력: PRD, data contracts, backend structure
- 출력: `docs/ai/ai_feature_spec.md`, `docs/ai/model_io_contract.md`, `docs/ai/prompt_contract.md`, `docs/ai/evaluation_plan.md`
- 금지: 서비스 범위 임의 확장

### 5.11 QA Engineer
- 입력: PRD, UI spec, API spec, 구현 결과
- 출력: `qa/test_cases.md`, `qa/bug_report.md`, `qa/regression_checklist.md`, `qa/release_readiness.md`
- 금지: 요구사항 재정의

### 5.12 DevOps / Platform
- 입력: architecture, FE/BE/AI runtime needs
- 출력: `infra/deployment.md`, `infra/env.example`, `infra/monitoring.md`, `infra/ci_cd.md`, `infra/rollback.md`
- 금지: 제품 요구 변경

### 5.13 Security Engineer
- 입력: architecture, API/auth model, data flow
- 출력: `docs/security/threat_model.md`, `docs/security/access_control.md`, `docs/security/privacy_notes.md`, `docs/security/security_checklist.md`
- 금지: 제품 범위 재정의

### 5.14 Operations / CS
- 입력: release scope, product behavior, failure modes
- 출력: `docs/ops/faq.md`, `docs/ops/response_policy.md`, `docs/ops/escalation_flow.md`
- 금지: 핵심 기능 요구사항 직접 수정

### 5.15 Growth / Marketing
- 입력: product vision, event schema, launch scope
- 출력: `docs/growth/growth_hypotheses.md`, `docs/growth/funnel_events.md`, `docs/growth/launch_outline.md`
- 금지: 검증 없이 기능 범위 확장

### 5.16 Reviewer / Senior Engineer
- 입력: 각 lane 산출물
- 출력: `docs/review/architecture_review.md`, `docs/review/implementation_review.md`, `docs/review/risk_register.md`
- 금지: 소유권 무시한 직접 수정

### 5.17 Integrator
- 입력: Approved 상태 산출물 전체
- 출력: `release/*`, `docs/final/integration_report.md`, `docs/final/runbook.md`
- 금지: 미승인 산출물 포함, 요구사항 임의 변경

## 6. 표준 작업 흐름
1. PO가 vision / priorities / success metrics를 만든다.
2. PM이 PRD / backlog / release scope를 만든다.
3. UX/UI, Prompt/Workflow, Architect를 병렬 실행한다.
4. Backend, Data Engineer, AI Engineer가 계약 문서를 만든다.
5. Reviewer가 1차 구조 검토를 한다.
6. Frontend / Backend / Data / AI / DevOps를 병렬 구현한다.
7. Security / QA / Reviewer가 검증한다.
8. Operations / Growth가 출시 준비 문서를 만든다.
9. Integrator가 승인 산출물만 병합한다.
10. 사람 승인자가 최종 릴리즈 여부를 결정한다.

## 7. 단일 진실 공급원
- `docs/product/vision.md`
- `docs/product/priorities.md`
- `docs/PRD.md`
- `docs/design/ui_spec.md`
- `docs/backend/api_spec.yaml`
- `docs/db/erd.md`
- `docs/architecture/module_boundaries.md`
- `docs/task_board.md`

## 8. 변경 요청 프로세스
1. 요청자가 `docs/change_requests/` 아래 요청서를 작성한다.
2. Orchestrator 또는 Architect가 승인/반려한다.
3. 원 소유 lane이 수정한다.
4. Reviewer가 영향 범위를 다시 본다.
5. 관련 하위 문서와 task board 상태를 업데이트한다.

## 9. 완료 기준
- 필수 입력 문서가 명시돼 있어야 한다.
- 출력 경로가 고정돼 있어야 한다.
- 금지 범위가 적혀 있어야 한다.
- 다음 lane이 바로 쓸 수 있을 정도로 명확해야 한다.
- Approved / In Review / Blocked / Rejected / Integrated 상태 중 하나로 관리돼야 한다.

## 10. 추천 폴더 구조
```text
project-root/
├─ docs/
│  ├─ product/
│  ├─ architecture/
│  ├─ agent-workflow/
│  ├─ design/
│  ├─ backend/
│  ├─ db/
│  ├─ data/
│  ├─ ai/
│  ├─ security/
│  ├─ ops/
│  ├─ growth/
│  ├─ review/
│  ├─ final/
│  ├─ change_requests/
│  ├─ PRD.md
│  ├─ backlog.md
│  ├─ release_scope.md
│  ├─ milestones.md
│  ├─ task_board.md
│  └─ approval_log.md
├─ frontend/
├─ backend/
├─ data/
├─ infra/
├─ qa/
├─ prompts/
└─ release/
```

## 11. 실전 운영 규칙
- vision/priorities 없이 PRD를 만들지 않는다.
- PRD 없이 UI/API/ERD를 병렬로 만들지 않는다.
- module boundaries 없이 대규모 구현 lane를 열지 않는다.
- Frontend와 Backend는 계약 문서 없이 병렬 구현하지 않는다.
- Security와 QA를 릴리즈 직전에만 붙이지 않는다.
- Growth는 출시 뒤가 아니라 event schema 설계 단계부터 관여한다.
- Reviewer는 마지막 형식 체크가 아니라 중간 의사결정 검증까지 맡는다.

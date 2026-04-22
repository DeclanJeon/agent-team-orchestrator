# Starter Prompt Set

이 파일은 처음 쓰는 사람이 Hermes에 바로 붙여넣어 실행할 수 있는 스타터 프롬프트 모음이다.
각 프롬프트는 self-contained로 유지하고, 출력 경로와 금지 범위를 포함한다.

## 1. Product kickoff
사용 예시:
```text
agent-team-orchestrator를 기준으로 이 프로젝트의 Product Owner + PM kickoff를 시작해라.
먼저 docs/product/vision.md, docs/product/priorities.md, docs/product/success_metrics.md,
docs/PRD.md, docs/backlog.md, docs/release_scope.md, docs/milestones.md, docs/task_board.md를 작성해라.
조건:
- 아직 구현은 시작하지 마라
- 모르는 내용은 가정으로 명시하라
- PRD와 backlog는 MVP 범위 기준으로 잘라라
- 각 문서 끝에 open questions를 남겨라
```

## 2. UX/UI + Architect parallel start
```text
agent-team-orchestrator를 기준으로 UX/UI lane과 System Architect lane을 병렬 시작해라.
입력 문서:
- docs/product/vision.md
- docs/product/priorities.md
- docs/PRD.md
출력 문서:
- docs/design/information_architecture.md
- docs/design/user_flow.md
- docs/design/wireframes.md
- docs/design/design_system.md
- docs/design/ui_spec.md
- docs/architecture/system_overview.md
- docs/architecture/module_boundaries.md
- docs/architecture/tech_decisions.md
- docs/architecture/integration_contract.md
규칙:
- UX/UI는 API 구조를 확정하지 마라
- Architect는 UI 카피를 확정하지 마라
- 충돌 사항은 docs/change_requests/ 아래 요청서로 남겨라
```

## 3. Backend + Data + AI contract phase
```text
agent-team-orchestrator를 기준으로 Backend, Data Engineer, AI Engineer 계약 문서 단계를 진행해라.
입력:
- docs/PRD.md
- docs/architecture/module_boundaries.md
- docs/design/ui_spec.md
출력:
- docs/backend/api_spec.yaml
- docs/backend/domain_model.md
- docs/backend/error_policy.md
- docs/db/erd.md
- docs/data/data_flow.md
- docs/data/event_schema.md
- docs/data/etl_plan.md
- docs/ai/ai_feature_spec.md
- docs/ai/model_io_contract.md
- docs/ai/prompt_contract.md
- docs/ai/evaluation_plan.md
규칙:
- 구현 코드는 아직 만들지 마라
- FE/BE/AI handoff에 필요한 계약 위주로 작성하라
- 인증, 실패 응답, 이벤트 schema를 빠뜨리지 마라
```

## 4. Reviewer gate before implementation
```text
agent-team-orchestrator를 기준으로 Reviewer / Senior Engineer gate review를 실행해라.
검토 대상:
- docs/PRD.md
- docs/design/ui_spec.md
- docs/backend/api_spec.yaml
- docs/db/erd.md
- docs/architecture/module_boundaries.md
- docs/data/event_schema.md
- docs/ai/model_io_contract.md
출력:
- docs/review/architecture_review.md
- docs/review/implementation_review.md
- docs/review/risk_register.md
판단 기준:
- 역할 경계가 섞이지 않았는가
- 병렬 구현 전에 계약 문서가 충분한가
- Security / QA / Ops / Growth가 나중에 막히지 않는가
```

## 5. Frontend + Backend implementation launch
```text
agent-team-orchestrator를 기준으로 Frontend Engineer와 Backend Engineer 구현 lane를 병렬 실행해라.
입력:
- docs/design/ui_spec.md
- docs/design/design_system.md
- docs/backend/api_spec.yaml
- docs/backend/domain_model.md
- docs/backend/error_policy.md
- docs/architecture/module_boundaries.md
출력:
- frontend/*
- backend/*
- docs/frontend/component_map.md
- docs/frontend/integration_notes.md
규칙:
- frontend는 api_spec을 직접 수정하지 마라
- backend는 ui_spec을 직접 수정하지 마라
- 계약 변경이 필요하면 change request를 남겨라
- 각 lane 종료 시 테스트/미완료 항목을 명시하라
```

## 6. Security + QA release gate
```text
agent-team-orchestrator를 기준으로 Security Engineer와 QA Engineer release gate를 실행해라.
입력:
- docs/PRD.md
- docs/backend/api_spec.yaml
- docs/db/erd.md
- 구현 결과 전체
출력:
- docs/security/threat_model.md
- docs/security/access_control.md
- docs/security/privacy_notes.md
- docs/security/security_checklist.md
- qa/test_cases.md
- qa/bug_report.md
- qa/regression_checklist.md
- qa/release_readiness.md
규칙:
- blocker와 non-blocker를 분리하라
- 개인정보/권한/에러 노출 위험을 분리해서 적어라
- 릴리즈 가능 여부를 명확히 결론내라
```

## 7. Ops + Growth launch prep
```text
agent-team-orchestrator를 기준으로 Operations / CS와 Growth / Marketing launch prep을 실행해라.
입력:
- docs/product/vision.md
- docs/product/priorities.md
- docs/PRD.md
- docs/data/event_schema.md
- qa/release_readiness.md
출력:
- docs/ops/faq.md
- docs/ops/response_policy.md
- docs/ops/escalation_flow.md
- docs/growth/growth_hypotheses.md
- docs/growth/funnel_events.md
- docs/growth/launch_outline.md
규칙:
- 운영 FAQ와 마케팅 메시지를 섞지 마라
- growth는 이벤트 schema에 없는 지표를 임의로 만들지 마라
```

## 8. Final integration prompt
```text
agent-team-orchestrator를 기준으로 Integrator final pass를 실행해라.
입력:
- Approved 상태 문서와 구현 결과 전체
출력:
- docs/final/integration_report.md
- docs/final/runbook.md
- release/*
규칙:
- 미승인 산출물은 포함하지 마라
- 환경 변수, 실행 순서, known issues, rollback path를 반드시 적어라
- 최종 보고서에 open risks를 남겨라
```

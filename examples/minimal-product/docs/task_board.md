# Task Board

| Task ID | 작업명 | 담당 | 입력 | 출력 | 상태 | 선행 조건 |
|---|---|---|---|---|---|---|
| T-001 | 제품 비전 정의 | Product Owner | 사용자 요구사항 | docs/product/vision.md | Approved | 없음 |
| T-002 | 우선순위 및 성공지표 정리 | Product Owner | docs/product/vision.md | docs/product/priorities.md, docs/product/success_metrics.md | Approved | T-001 |
| T-003 | PRD 작성 | PM | docs/product/* | docs/PRD.md | Approved | T-002 |
| T-004 | UI Spec 작성 | UXUI | docs/PRD.md | docs/design/ui_spec.md | In Review | T-003 |
| T-005 | API / ERD 작성 | Backend | docs/PRD.md | docs/backend/api_spec.yaml, docs/db/erd.md | In Review | T-003 |
| T-006 | Review gate | Reviewer | docs/design/ui_spec.md, docs/backend/api_spec.yaml | docs/review/architecture_review.md | Pending | T-004,T-005 |

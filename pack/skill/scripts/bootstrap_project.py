#!/usr/bin/env python3
import argparse
from pathlib import Path

DOCS = {
    'docs/product/vision.md': """# Product Vision

## Problem
- What user pain is this project solving?

## Target User
- Primary user:
- Secondary user:

## Why Now
- Why should this exist now instead of later?

## Product Promise
- In one sentence, what value should users reliably get?

## Non-goals
- What this release explicitly will not solve:
""",
    'docs/product/priorities.md': """# Product Priorities

## Must Win
- 

## Important but Later
- 

## Explicitly Deferred
- 

## Trade-off Notes
- What are we optimizing for in this phase?
""",
    'docs/product/success_metrics.md': """# Success Metrics

| Metric | Target | Why it matters | Owner |
|---|---|---|---|
| Activation | | | |
| Time-to-value | | | |
| Quality / error rate | | | |
""",
    'docs/PRD.md': """# PRD

## Goal

## Users

## Core Features

## Non-functional Requirements

## Acceptance Criteria

## Risks

## Open Questions
""",
    'docs/backlog.md': """# Backlog

## Now
- [ ]

## Next
- [ ]

## Later
- [ ]
""",
    'docs/release_scope.md': """# Release Scope

## In Scope
- 

## Out of Scope
- 

## Release Blocking Conditions
- 
""",
    'docs/milestones.md': """# Milestones

| Milestone | Outcome | Owner | Target Date | Exit Criteria |
|---|---|---|---|---|
| Discovery | | | | |
| Contracts | | | | |
| Implementation | | | | |
| Release Gate | | | | |
""",
    'docs/task_board.md': """# Task Board

| Task ID | 작업명 | 담당 | 입력 | 출력 | 상태 | 선행 조건 |
|---|---|---|---|---|---|---|
| T-001 | 제품 비전 정의 | Product Owner | 사용자 요구사항 | docs/product/vision.md | Draft | 없음 |
| T-002 | 우선순위 및 성공지표 정리 | Product Owner | docs/product/vision.md | docs/product/priorities.md, docs/product/success_metrics.md | Pending | T-001 |
| T-003 | PRD / Backlog / Release Scope 작성 | PM | docs/product/* | docs/PRD.md, docs/backlog.md, docs/release_scope.md | Pending | T-002 |
| T-004 | UX/UI 초안 | UXUI | docs/PRD.md | docs/design/* | Pending | T-003 |
| T-005 | Architecture 계약 초안 | Architect | docs/PRD.md | docs/architecture/* | Pending | T-003 |
| T-006 | API / ERD / Data / AI 계약 | Backend, Data, AI | docs/PRD.md, docs/architecture/* | docs/backend/*, docs/db/erd.md, docs/data/*, docs/ai/* | Pending | T-005 |
| T-007 | Reviewer 게이트 | Reviewer | contracts set | docs/review/* | Pending | T-006 |
| T-008 | 구현 | Frontend, Backend, Data, AI, DevOps | approved contracts | code + integration notes | Pending | T-007 |
| T-009 | Security / QA 게이트 | Security, QA | implementation | docs/security/*, qa/* | Pending | T-008 |
| T-010 | Ops / Growth launch prep | Ops, Growth | release-ready scope | docs/ops/*, docs/growth/* | Pending | T-009 |
| T-011 | Final integration | Integrator | approved outputs | docs/final/*, release/* | Pending | T-010 |
""",
    'docs/approval_log.md': """# Approval Log

| Date | Artifact | Decision | Approver | Notes |
|---|---|---|---|---|
| | docs/PRD.md | Approved / Rejected / Needs changes | | |
""",
    'docs/architecture/system_overview.md': """# System Overview

## Product Context

## System Components
- Client
- API / Backend
- Data / Analytics
- AI Runtime
- Infra / Ops

## Primary Flows
- User request flow
- Data capture flow
- AI inference flow
""",
    'docs/architecture/module_boundaries.md': """# Module Boundaries

## Frontend Owns
- 

## Backend Owns
- 

## Data Owns
- 

## AI Owns
- 

## Shared Contracts
- API spec
- Event schema
- Model IO contract
""",
    'docs/architecture/tech_decisions.md': """# Tech Decisions

| Topic | Decision | Why | Rejected Alternatives |
|---|---|---|---|
| Frontend stack | | | |
| Backend stack | | | |
| Data layer | | | |
| AI runtime | | | |
""",
    'docs/architecture/integration_contract.md': """# Integration Contract

## Required Interfaces
- Frontend ↔ Backend
- Backend ↔ Data
- Backend ↔ AI
- Ops ↔ Runtime

## Versioning / Change Rules
- Cross-lane contract changes require change request + approval
""",
    'docs/agent-workflow/system_map.md': """# Agent System Map

## Lanes
- Orchestrator
- Product Owner
- PM
- UXUI
- Prompt / Workflow
- Architect
- Reviewer
- Frontend
- Backend
- Data
- AI
- QA
- DevOps
- Security
- Ops
- Growth
- Integrator
""",
    'docs/agent-workflow/prompt_contract.md': """# Prompt Contract

## Required fields per lane prompt
- role
- goal
- input docs
- output path
- forbidden scope
- completion criteria
""",
    'docs/agent-workflow/automation_rules.md': """# Automation Rules

- Do not start implementation lanes before baseline docs exist.
- Do not directly edit another lane's contract file.
- Use change requests for cross-lane changes.
- Reviewer / QA / Security gate required before integration.
""",
    'docs/design/information_architecture.md': """# Information Architecture

## Top-level sections
- 

## Core navigation
- 
""",
    'docs/design/user_flow.md': """# User Flow

## Primary flow
1. 
2. 
3. 

## Failure paths
- 
""",
    'docs/design/wireframes.md': """# Wireframes

## Screen list
- 

## Notes
- Keep wireframes text-first and implementation-oriented
""",
    'docs/design/design_system.md': """# Design System

## Colors

## Typography

## Spacing

## Component rules
""",
    'docs/design/ui_spec.md': """# UI Spec

## Screen List

## Per-screen contract
### Screen
- Goal:
- Main components:
- Default state:
- Loading state:
- Empty state:
- Error state:
- Required API dependency:
""",
    'docs/backend/api_spec.yaml': "openapi: 3.0.3\ninfo:\n  title: Example API\n  version: 0.1.0\npaths: {}\n",
    'docs/backend/domain_model.md': """# Domain Model

## Entities
- 

## Invariants
- 
""",
    'docs/backend/error_policy.md': """# Error Policy

## Error classes
- Validation
- Auth
- Permission
- Domain conflict
- Internal

## Client response rules
- 
""",
    'docs/db/erd.md': """# ERD

## Core entities
- 

## Relationships
- 
""",
    'docs/data/data_flow.md': """# Data Flow

## Sources
- 

## Transformations
- 

## Sinks / Consumers
- 
""",
    'docs/data/event_schema.md': """# Event Schema

| Event | Trigger | Properties | Consumer |
|---|---|---|---|
| | | | |
""",
    'docs/data/etl_plan.md': """# ETL Plan

## Raw inputs

## Processing steps

## Validation checks
""",
    'docs/ai/ai_feature_spec.md': """# AI Feature Spec

## Use case

## Model responsibility

## Human fallback / override
""",
    'docs/ai/model_io_contract.md': """# Model IO Contract

## Input schema

## Output schema

## Failure / timeout handling
""",
    'docs/ai/prompt_contract.md': """# AI Prompt Contract

## System prompt inputs

## Runtime variables

## Safety / refusal boundaries
""",
    'docs/ai/evaluation_plan.md': """# Evaluation Plan

## Success criteria

## Test cases

## Regression checks
""",
    'docs/frontend/component_map.md': """# Component Map

| Component | Route / Surface | Depends on | Notes |
|---|---|---|---|
| | | | |
""",
    'docs/frontend/integration_notes.md': """# Integration Notes

## API dependencies

## Known gaps

## Mock / fallback behavior
""",
    'docs/security/threat_model.md': """# Threat Model

## Assets
- 

## Threats
- 

## Mitigations
- 
""",
    'docs/security/access_control.md': """# Access Control

## Roles

## Permissions

## Sensitive operations
""",
    'docs/security/privacy_notes.md': """# Privacy Notes

## Sensitive data touched

## Retention / deletion

## Logging constraints
""",
    'docs/security/security_checklist.md': """# Security Checklist

- [ ] Authn/authz reviewed
- [ ] Sensitive data exposure checked
- [ ] Error leakage checked
- [ ] Secrets handling reviewed
""",
    'docs/ops/faq.md': """# FAQ

## Common user questions
- 
""",
    'docs/ops/response_policy.md': """# Response Policy

## Severity levels

## Response owner

## SLA / handling notes
""",
    'docs/ops/escalation_flow.md': """# Escalation Flow

1. Detect issue
2. Triage severity
3. Route to owner
4. Escalate blocker
""",
    'docs/growth/growth_hypotheses.md': """# Growth Hypotheses

| Hypothesis | Metric | Expected lift | Risk |
|---|---|---|---|
| | | | |
""",
    'docs/growth/funnel_events.md': """# Funnel Events

## Activation funnel
- 

## Retention / conversion events
- 
""",
    'docs/growth/launch_outline.md': """# Launch Outline

## Audience

## Core message

## Channels

## Launch risks
""",
    'docs/review/architecture_review.md': """# Architecture Review

## Scope

## Findings by Severity
### Critical
- 

### High
- 

### Medium
- 

### Low
- 

## Release Recommendation
- Approve / Block / Re-review
""",
    'docs/review/implementation_review.md': """# Implementation Review

## Reviewed areas

## Quality findings

## Follow-up actions
""",
    'docs/review/risk_register.md': """# Risk Register

| Risk | Impact | Likelihood | Owner | Mitigation |
|---|---|---|---|---|
| | | | | |
""",
    'docs/final/integration_report.md': """# Integration Report

## Included artifacts

## Remaining gaps

## Sign-off notes
""",
    'docs/final/runbook.md': """# Runbook

## Startup steps

## Rollback steps

## Known issues
""",
    'qa/test_cases.md': """# Test Cases

| ID | Scenario | Expected Result | Status |
|---|---|---|---|
| | | | |
""",
    'qa/bug_report.md': """# Bug Report

| ID | Severity | Summary | Status | Owner |
|---|---|---|---|---|
| | | | | |
""",
    'qa/regression_checklist.md': """# Regression Checklist

- [ ] Core flow
- [ ] Error flow
- [ ] Permission flow
- [ ] Data integrity flow
""",
    'qa/release_readiness.md': """# Release Readiness

## Blockers
- 

## Non-blockers
- 

## Final recommendation
- Release / Hold
""",
    'infra/deployment.md': """# Deployment

## Environments

## Deploy order

## Required approvals
""",
    'infra/env.example': "# ENV\n# KEY=value\n",
    'infra/monitoring.md': """# Monitoring

## Critical signals
- 

## Dashboards / alerts
- 
""",
    'infra/ci_cd.md': """# CI/CD

## Required checks
- 

## Deploy gate
- 
""",
    'infra/rollback.md': """# Rollback

## Trigger conditions

## Rollback steps

## Validation after rollback
""",
}

PROMPTS = {
    'prompts/orchestrator.md': '역할: Orchestrator\n목표: 작업 분해, 승인 흐름 관리, lane 충돌 조정\n금지: 세부 구현 직접 개입\n',
    'prompts/product-owner.md': '역할: Product Owner\n출력: docs/product/*\n금지: 세부 구현 지시\n',
    'prompts/pm.md': '역할: PM / Service Planner\n출력: docs/PRD.md, docs/backlog.md, docs/release_scope.md, docs/milestones.md\n금지: 코드 작성\n',
    'prompts/ux-ui.md': '역할: UX Research / UXUI\n출력: docs/design/*\n금지: API 구조 변경\n',
    'prompts/prompt-workflow.md': '역할: Prompt / Workflow Designer\n출력: docs/agent-workflow/*\n금지: 제품 요구사항 직접 변경\n',
    'prompts/architect.md': '역할: System Architect\n출력: docs/architecture/*\n금지: 세부 UI 확정\n',
    'prompts/reviewer.md': '역할: Reviewer / Senior Engineer\n출력: docs/review/*\n금지: 소유권 무시한 직접 수정\n',
    'prompts/backend.md': '역할: Backend Engineer\n출력: docs/backend/*, docs/db/erd.md, backend/*\n금지: UX 흐름 재정의\n',
    'prompts/frontend.md': '역할: Frontend Engineer\n출력: frontend/*, docs/frontend/*\n금지: API 구조 임의 수정\n',
    'prompts/data-engineer.md': '역할: Data Engineer\n출력: docs/data/*, data/*\n금지: 제품 목표 재정의\n',
    'prompts/ai-engineer.md': '역할: AI Engineer\n출력: docs/ai/*\n금지: 서비스 범위 임의 확장\n',
    'prompts/qa.md': '역할: QA Engineer\n출력: qa/*\n금지: 요구사항 재정의\n',
    'prompts/devops.md': '역할: DevOps / Platform\n출력: infra/*\n금지: 제품 요구 변경\n',
    'prompts/security.md': '역할: Security Engineer\n출력: docs/security/*\n금지: 제품 목표 재정의\n',
    'prompts/operations.md': '역할: Operations / CS\n출력: docs/ops/*\n금지: 핵심 기능 요구사항 직접 수정\n',
    'prompts/growth.md': '역할: Growth / Marketing\n출력: docs/growth/*\n금지: 검증 없이 기능 범위 확장\n',
    'prompts/integrator.md': '역할: Integrator\n출력: release/*, docs/final/*\n금지: 미승인 산출물 포함\n',
}


def write_if_needed(path: Path, content: str, force: bool):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return False
    path.write_text(content, encoding='utf-8')
    return True


def main():
    parser = argparse.ArgumentParser(description='Bootstrap a project for Hermes agent-team orchestration.')
    parser.add_argument('project_root')
    parser.add_argument('--project-name', default='New Project')
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0

    for rel, content in DOCS.items():
        if rel == 'docs/backend/api_spec.yaml':
            content = f'openapi: 3.0.3\ninfo:\n  title: {args.project_name} API\n  version: 0.1.0\npaths: {{}}\n'
        ok = write_if_needed(root / rel, content, args.force)
        created += int(ok)
        skipped += int(not ok)

    readme = (
        f'# {args.project_name}\n\n'
        'This project was bootstrapped with agent-team-orchestrator.\n\n'
        'Core docs:\n'
        '- docs/product/vision.md\n'
        '- docs/product/priorities.md\n'
        '- docs/PRD.md\n'
        '- docs/design/ui_spec.md\n'
        '- docs/backend/api_spec.yaml\n'
        '- docs/db/erd.md\n'
        '- docs/task_board.md\n'
    )
    ok = write_if_needed(root / 'README.md', readme, args.force)
    created += int(ok)
    skipped += int(not ok)

    for rel, content in PROMPTS.items():
        ok = write_if_needed(root / rel, content, args.force)
        created += int(ok)
        skipped += int(not ok)

    for d in ['docs/change_requests', 'frontend', 'backend', 'data', 'release']:
        (root / d).mkdir(parents=True, exist_ok=True)

    print('BOOTSTRAP_COMPLETE')
    print(f'project_root={root}')
    print(f'created={created}')
    print(f'skipped={skipped}')

if __name__ == '__main__':
    main()

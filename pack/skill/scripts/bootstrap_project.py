#!/usr/bin/env python3
import argparse
from pathlib import Path

DOCS = {
    'docs/product/vision.md': '# Product Vision\n',
    'docs/product/priorities.md': '# Product Priorities\n',
    'docs/product/success_metrics.md': '# Success Metrics\n',
    'docs/PRD.md': '# PRD\n\n## Goal\n\n## Users\n\n## Core Features\n\n## Success Metrics\n',
    'docs/backlog.md': '# Backlog\n\n- [ ]\n',
    'docs/release_scope.md': '# Release Scope\n\n## In Scope\n\n## Out of Scope\n',
    'docs/milestones.md': '# Milestones\n',
    'docs/task_board.md': '# Task Board\n\n| Task ID | 작업명 | 담당 | 입력 | 출력 | 상태 | 선행 조건 |\n|---|---|---|---|---|---|---|\n| T-001 | 제품 비전 정의 | Product Owner | 사용자 요구사항 | docs/product/vision.md | Draft | 없음 |\n',
    'docs/approval_log.md': '# Approval Log\n',
    'docs/architecture/system_overview.md': '# System Overview\n',
    'docs/architecture/module_boundaries.md': '# Module Boundaries\n',
    'docs/architecture/tech_decisions.md': '# Tech Decisions\n',
    'docs/architecture/integration_contract.md': '# Integration Contract\n',
    'docs/agent-workflow/system_map.md': '# Agent System Map\n',
    'docs/agent-workflow/prompt_contract.md': '# Prompt Contract\n',
    'docs/agent-workflow/automation_rules.md': '# Automation Rules\n',
    'docs/design/information_architecture.md': '# Information Architecture\n',
    'docs/design/user_flow.md': '# User Flow\n',
    'docs/design/wireframes.md': '# Wireframes\n',
    'docs/design/design_system.md': '# Design System\n',
    'docs/design/ui_spec.md': '# UI Spec\n',
    'docs/backend/api_spec.yaml': 'openapi: 3.0.3\ninfo:\n  title: Example API\n  version: 0.1.0\npaths: {}\n',
    'docs/backend/domain_model.md': '# Domain Model\n',
    'docs/backend/error_policy.md': '# Error Policy\n',
    'docs/db/erd.md': '# ERD\n',
    'docs/data/data_flow.md': '# Data Flow\n',
    'docs/data/event_schema.md': '# Event Schema\n',
    'docs/data/etl_plan.md': '# ETL Plan\n',
    'docs/ai/ai_feature_spec.md': '# AI Feature Spec\n',
    'docs/ai/model_io_contract.md': '# Model IO Contract\n',
    'docs/ai/prompt_contract.md': '# AI Prompt Contract\n',
    'docs/ai/evaluation_plan.md': '# Evaluation Plan\n',
    'docs/frontend/component_map.md': '# Component Map\n',
    'docs/frontend/integration_notes.md': '# Integration Notes\n',
    'docs/security/threat_model.md': '# Threat Model\n',
    'docs/security/access_control.md': '# Access Control\n',
    'docs/security/privacy_notes.md': '# Privacy Notes\n',
    'docs/security/security_checklist.md': '# Security Checklist\n',
    'docs/ops/faq.md': '# FAQ\n',
    'docs/ops/response_policy.md': '# Response Policy\n',
    'docs/ops/escalation_flow.md': '# Escalation Flow\n',
    'docs/growth/growth_hypotheses.md': '# Growth Hypotheses\n',
    'docs/growth/funnel_events.md': '# Funnel Events\n',
    'docs/growth/launch_outline.md': '# Launch Outline\n',
    'docs/review/architecture_review.md': '# Architecture Review\n',
    'docs/review/implementation_review.md': '# Implementation Review\n',
    'docs/review/risk_register.md': '# Risk Register\n',
    'docs/final/integration_report.md': '# Integration Report\n',
    'docs/final/runbook.md': '# Runbook\n',
    'qa/test_cases.md': '# Test Cases\n',
    'qa/bug_report.md': '# Bug Report\n',
    'qa/regression_checklist.md': '# Regression Checklist\n',
    'qa/release_readiness.md': '# Release Readiness\n',
    'infra/deployment.md': '# Deployment\n',
    'infra/env.example': '# ENV\n',
    'infra/monitoring.md': '# Monitoring\n',
    'infra/ci_cd.md': '# CI/CD\n',
    'infra/rollback.md': '# Rollback\n',
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

# Hermes 적용 가이드

## 설치
```bash
cd /home/declan/Documents/00_Develop/agent_team
./install.sh
```

## 설치 결과
- Hermes skill: `~/.hermes/skills/agent-team-orchestrator`
- wrapper: `~/.local/bin/agent-team-bootstrap`

## 사용
```bash
hermes -s agent-team-orchestrator
~/.local/bin/agent-team-bootstrap /path/to/project --project-name "Example App"
```

## 이번 버전의 역할 세분화
- Orchestrator
- Product Owner
- PM / Service Planner
- UX Research / UXUI
- Prompt / Workflow Designer
- System Architect
- Reviewer / Senior Engineer
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

## 롤백
```bash
rm -rf ~/.hermes/skills/agent-team-orchestrator
rm -f ~/.local/bin/agent-team-bootstrap
```

#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="agent-team-orchestrator"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
SKILL_DEST="$HERMES_HOME/skills/$SKILL_NAME"
BIN_DIR="${BIN_DIR:-$HOME/.local/bin}"
WRAPPER_PATH="$BIN_DIR/agent-team-bootstrap"

if [[ -d "$SKILL_DEST" ]]; then
  rm -rf "$SKILL_DEST"
  echo "Removed skill: $SKILL_DEST"
else
  echo "Skill not installed: $SKILL_DEST"
fi

if [[ -f "$WRAPPER_PATH" ]]; then
  rm -f "$WRAPPER_PATH"
  echo "Removed wrapper: $WRAPPER_PATH"
else
  echo "Wrapper not installed: $WRAPPER_PATH"
fi

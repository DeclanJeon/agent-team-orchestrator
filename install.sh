#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="$SCRIPT_DIR/pack/skill"
SKILL_NAME="agent-team-orchestrator"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
SKILL_DEST="$HERMES_HOME/skills/$SKILL_NAME"
BIN_DIR="${BIN_DIR:-$HOME/.local/bin}"
WRAPPER_PATH="$BIN_DIR/agent-team-bootstrap"
DRY_RUN=0

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    *) echo "Unknown argument: $arg" >&2; exit 1 ;;
  esac
done

show_plan() {
  echo "Install plan"
  echo "- source: $SKILL_SRC"
  echo "- HERMES_HOME: $HERMES_HOME"
  echo "- skill dest: $SKILL_DEST"
  echo "- wrapper: $WRAPPER_PATH"
}

copy_tree() {
  local src="$1"
  local dst="$2"
  mkdir -p "$dst"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$src"/ "$dst"/
  else
    rm -rf "$dst"
    mkdir -p "$dst"
    cp -R "$src"/. "$dst"/
  fi
}

command -v python3 >/dev/null 2>&1 || { echo 'Missing command: python3' >&2; exit 1; }
show_plan
[[ -f "$SKILL_SRC/SKILL.md" ]] || { echo "Missing skill source: $SKILL_SRC/SKILL.md" >&2; exit 1; }

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo 'DRY_RUN=1; no files changed'
  exit 0
fi

mkdir -p "$HERMES_HOME/skills"
copy_tree "$SKILL_SRC" "$SKILL_DEST"
find "$SKILL_DEST/scripts" -type f -name '*.py' -exec chmod +x {} + 2>/dev/null || true
mkdir -p "$BIN_DIR"
cat > "$WRAPPER_PATH" <<EOF
#!/usr/bin/env bash
set -euo pipefail
python3 "$SKILL_DEST/scripts/bootstrap_project.py" "\$@"
EOF
chmod +x "$WRAPPER_PATH"

if command -v hermes >/dev/null 2>&1; then
  if hermes skills list | grep -q "$SKILL_NAME"; then
    echo "Hermes skill visible: $SKILL_NAME"
  else
    echo 'Installed, but Hermes may need relaunch to show the skill.'
  fi
fi

echo 'DONE'
echo "- skill: $SKILL_DEST"
echo "- wrapper: $WRAPPER_PATH"

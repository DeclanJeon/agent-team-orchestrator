#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_NAME="agent-team-orchestrator"
VERSION="${1:-v1.0.0}"
OUT_DIR="$SCRIPT_DIR/dist"
TMP_PARENT="$(mktemp -d)"
PKG_DIR="$TMP_PARENT/$PROJECT_NAME"
ARCHIVE_PATH="$OUT_DIR/${PROJECT_NAME}-${VERSION}.tar.gz"

cleanup() {
  rm -rf "$TMP_PARENT"
}
trap cleanup EXIT

mkdir -p "$OUT_DIR"
mkdir -p "$PKG_DIR"

cp -R "$SCRIPT_DIR"/. "$PKG_DIR"/
rm -rf "$PKG_DIR/.git" "$PKG_DIR/dist" "$PKG_DIR/.github"
find "$PKG_DIR" -type d -name __pycache__ -prune -exec rm -rf {} +
find "$PKG_DIR" -type f -name '*.pyc' -delete

(
  cd "$TMP_PARENT"
  tar -czf "$ARCHIVE_PATH" "$PROJECT_NAME"
)

echo "$ARCHIVE_PATH"

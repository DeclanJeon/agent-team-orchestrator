#!/usr/bin/env bash
set -euo pipefail

SKILL_REPO_URL="${SKILL_REPO_URL:-}"
if [[ -z "$SKILL_REPO_URL" ]]; then
  echo "Set SKILL_REPO_URL to a hosted .tar.gz release asset URL" >&2
  exit 1
fi

TMP_DIR="$(mktemp -d)"
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

ARCHIVE_PATH="$TMP_DIR/skill.tar.gz"
EXTRACT_DIR="$TMP_DIR/extracted"
mkdir -p "$EXTRACT_DIR"

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$SKILL_REPO_URL" -o "$ARCHIVE_PATH"
elif command -v wget >/dev/null 2>&1; then
  wget -qO "$ARCHIVE_PATH" "$SKILL_REPO_URL"
else
  echo "Need curl or wget to download the release asset" >&2
  exit 1
fi

tar -xzf "$ARCHIVE_PATH" -C "$EXTRACT_DIR"
INSTALL_SCRIPT="$(find "$EXTRACT_DIR" -maxdepth 2 -type f -name install.sh | head -1)"
if [[ -z "$INSTALL_SCRIPT" ]]; then
  echo "install.sh not found in downloaded package" >&2
  exit 1
fi

bash "$INSTALL_SCRIPT"

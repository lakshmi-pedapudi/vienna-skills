#!/usr/bin/env bash
# install.sh: wrapper around bin/vienna-skills for people who cloned the repo instead of using npm.
#   bash install.sh [--target claude|codex|agents|all] [--copy] [--uninstall]
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
if [ "${1:-}" = "--uninstall" ]; then shift; exec bash "$HERE/bin/vienna-skills" uninstall "$@"; fi
exec bash "$HERE/bin/vienna-skills" install "$@"

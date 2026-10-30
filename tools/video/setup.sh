#!/usr/bin/env bash
# setup.sh — install two open-source video tools as Claude Code skills, pinned to known commits.
#
#   video-use    (browser-use/video-use, MIT)        edit raw footage by conversation
#   HyperFrames  (heygen-com/hyperframes, Apache-2.0) HTML scenes rendered to MP4 in headless Chrome
#
#   setup.sh            clone what is missing, check out the pins, link the skills
#   setup.sh --latest   change nothing; print the upstream HEADs, to bump the pins below
#
# Safe to re-run, and fast when nothing changed. Prints one line: "✓ video  ..." or "✗ video  ...".
# Clones go to ~/.local/share/claude-vendor (outside any repo); the skills are links in ~/.claude/skills.
# Secrets never go in git: the ElevenLabs key lives in <video-use>/.env on each laptop.
set -uo pipefail

VENDOR="${CLAUDE_VENDOR_DIR:-$HOME/.local/share/claude-vendor}"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
BACKUPS="$HOME/.claude/skill-backups"

VIDEO_USE_URL=https://github.com/browser-use/video-use.git
VIDEO_USE_PIN=43cfc566833548093455c9d4a46bd69913b7e552
HYPERFRAMES_URL=https://github.com/heygen-com/hyperframes.git
HYPERFRAMES_PIN=a6dec0701f550c6bbf06c6e8506360f2b1373a52
HYPERFRAMES_SKILLS="hyperframes hyperframes-cli hyperframes-registry media-use"

# Windows (Git Bash): make ln -s a real symlink. Needs Developer Mode.
case "$(uname -s)" in MINGW*|MSYS*|CYGWIN*) export MSYS=winsymlinks:nativestrict ;; esac
export GIT_LFS_SKIP_SMUDGE=1   # HyperFrames keeps ~240 MB of test media in LFS; the skills need none of it

if [ "${1:-}" = "--latest" ]; then
  echo "video-use    pinned $VIDEO_USE_PIN   upstream $(git ls-remote "$VIDEO_USE_URL" HEAD | cut -f1)"
  echo "hyperframes  pinned $HYPERFRAMES_PIN   upstream $(git ls-remote "$HYPERFRAMES_URL" HEAD | cut -f1)"
  exit 0
fi

notes=(); bad=()

# fetch_pinned DIR URL PIN [SPARSE_PATH]: clone if missing, then check out PIN.
fetch_pinned() {
  local dir=$1 url=$2 pin=$3 sparse=${4:-}
  if [ ! -d "$dir/.git" ]; then
    mkdir -p "$(dirname "$dir")"
    if [ -n "$sparse" ]; then
      git clone -q --filter=blob:none --sparse "$url" "$dir" 2>/dev/null \
        && git -C "$dir" sparse-checkout set "$sparse" 2>/dev/null || return 1
    else
      git clone -q "$url" "$dir" 2>/dev/null || return 1
    fi
    notes+=("cloned $(basename "$dir")")
  fi
  [ "$(git -C "$dir" rev-parse HEAD 2>/dev/null)" = "$pin" ] && return 0
  git -C "$dir" cat-file -e "$pin^{commit}" 2>/dev/null || git -C "$dir" fetch -q origin 2>/dev/null
  git -C "$dir" -c advice.detachedHead=false checkout -q "$pin" 2>/dev/null || return 1
  notes+=("$(basename "$dir") at ${pin:0:7}")
}

# link_skill NAME SRC: ~/.claude/skills/NAME -> SRC; a real folder in the way is moved aside.
link_skill() {
  local name=$1 src=$2 link="$DEST/$1"
  [ -f "$src/SKILL.md" ] || { bad+=("no SKILL.md in $src"); return; }
  if [ -L "$link" ] && [ "$(readlink "$link")" = "$src" ]; then return; fi
  if [ -e "$link" ] && [ ! -L "$link" ]; then
    mkdir -p "$BACKUPS"; mv "$link" "$BACKUPS/$name.$(date +%Y%m%d-%H%M%S)"
  fi
  mkdir -p "$DEST"
  ln -sfn "$src" "$link" && notes+=("linked $name") || bad+=("could not link $name")
}

# 1. video-use: the whole repo is the skill (SKILL.md sits next to helpers/).
VU="$VENDOR/video-use"
if fetch_pinned "$VU" "$VIDEO_USE_URL" "$VIDEO_USE_PIN"; then
  link_skill video-use "$VU"
  if [ ! -x "$VU/.venv/bin/python" ] && [ ! -x "$VU/.venv/Scripts/python.exe" ]; then
    if command -v uv >/dev/null 2>&1 && (cd "$VU" && uv sync -q >/dev/null 2>&1); then
      notes+=("video-use Python deps installed")
    else
      bad+=("video-use Python deps not installed (needs uv: then cd $VU && uv sync)")
    fi
  fi
  [ -f "$VU/.env" ] || { [ -f "$VU/.env.example" ] && cp "$VU/.env.example" "$VU/.env"; }
  if [ -z "${ELEVENLABS_API_KEY:-}" ] && ! grep -qE '^ELEVENLABS_API_KEY=.+' "$VU/.env" 2>/dev/null; then
    notes+=("no ElevenLabs key yet ($VU/.env)")
  fi
else
  bad+=("could not fetch video-use")
fi

# 2. HyperFrames: only skills/ is checked out; four core skills are linked.
HF="$VENDOR/hyperframes"
if fetch_pinned "$HF" "$HYPERFRAMES_URL" "$HYPERFRAMES_PIN" skills; then
  for s in $HYPERFRAMES_SKILLS; do link_skill "$s" "$HF/skills/$s"; done
else
  bad+=("could not fetch hyperframes")
fi

# 3. Tools the skills call at run time. Reported, never installed from here.
command -v ffmpeg >/dev/null 2>&1 && command -v ffprobe >/dev/null 2>&1 || notes+=("needs ffmpeg")
node_major=$(node -p 'process.versions.node.split(".")[0]' 2>/dev/null || echo 0)
[ "$node_major" -ge 22 ] 2>/dev/null || notes+=("HyperFrames needs Node 22+")

join() { local IFS=';'; sed 's/;/; /g' <<< "$*"; }
if [ ${#bad[@]} -gt 0 ]; then echo "✗ video  $(join "${bad[@]}" ${notes[@]+"${notes[@]}"})"; exit 1; fi
if [ ${#notes[@]} -gt 0 ]; then echo "✓ video  $(join "${notes[@]}")"; else echo "✓ video  in step"; fi

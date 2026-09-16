#!/usr/bin/env bash
# Style gate for paper sources: em-dashes, banned filler words, AI-tell phrases.
# .tex files also flag the LaTeX em-dash '---'; markdown/HTML skip it (tables, frontmatter).
# Usage: check_style.sh <file or glob> [...]
# Exit 1 when any hit is found. Allowed hits (file names, cited titles) must be
# confined to Appendix A and references.bib; filter those by eye.
set -uo pipefail

if [ "$#" -eq 0 ]; then
  echo "usage: $(basename "$0") <files...>" >&2
  exit 2
fi

DASH_MD='—|&mdash;|&#8212;'
DASH_TEX='—|---'
BANNED='\b[Aa]rms?\b|\b[Ii]nstrument\w*|\b[Ll]icens\w*|\b[Cc]ontract\w*|\b[Gg]round\w*|\b[Ll]everag\w*|\b[Rr]obust\w*|\b[Ss]eamless\w*|\b[Dd]elv\w*|\b[Uu]nlock\w*'
TELLS='\b[Gg]enuinely\b|\b[Pp]aramount\b|\bunderscor\w* the need\b|\bsweet spot\b|\bit is worth noting\b|\bin today.s\b|\bdive into\b|\bdelve\b|\bcomprehensive\b'
# Allowed literals that contain a banned stem: file names, the proper noun 'Grounding DINO', cite keys.
ALLOW='arm_scores\w*|rebuild_arm_results\w*|grounding/|Grounding DINO|references\.bib|\\cite[tp]?\{[^}]*\}|\\bibitem\{[^}]*\}'

hits=0
for f in "$@"; do
  [ -f "$f" ] || continue
  case "$f" in
    *.tex) DASH="$DASH_TEX" ;;
    *)     DASH="$DASH_MD" ;;
  esac
  # Strip allowed literals (file names, proper nouns, cite keys) from each line, then re-test. perl: BSD sed lacks \w.
  out=$(perl -ne 'BEGIN { $allow = shift; $pat = shift; } my $l = $_; $l =~ s/$allow//g; my @m = ($l =~ /$pat/g); print "$.:" . join(" ", @m) . "\n" if @m;' "$ALLOW" "$DASH|$BANNED|$TELLS" "$f" || true)
  if [ -n "$out" ]; then
    echo "== $f"
    echo "$out"
    hits=$((hits + $(echo "$out" | wc -l | tr -d ' ')))
  fi
done

if [ "$hits" -gt 0 ]; then
  echo "style gate: $hits hit(s)" >&2
  exit 1
fi
echo "style gate: clean"

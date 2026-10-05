#!/usr/bin/env bash
# Style gate for paper sources: em-dashes, banned words, AI-tell phrases (all hard failures),
# plus non-failing warnings for AI-tell sentence shapes ("not A, but B" pivots and similar).
# .tex files also flag the LaTeX em-dash '---'; HTML and markdown skip it (tables, frontmatter).
#
# Usage: check_style.sh [--allow REGEX ...] <file or directory> [...]
#   A directory expands to the .tex and .html sources inside it (backups/ and .git/ skipped).
#
# Word lists (edit these, not this script):
#   banned_words.txt    house banned words, one regex per line, next to this script
#   allow.txt           generic allow patterns (cite keys, the bib file name), next to this script
#   .paper-style-allow  optional per-paper allow patterns, read from the current directory and from
#                       the paper folder (each directory argument, and the folder and parent folder
#                       of each file argument) when present
#   --allow REGEX       extra allow pattern for this run (repeatable)
# Text matching an allow pattern is removed from a line before the checks run, so a literal file
# name or proper noun containing a banned stem does not fail the gate.
#
# Exit codes: 0 clean (warnings may be printed), 1 at least one hit, 2 usage error or nothing to check.
set -uo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
BANNED_FILE="$here/banned_words.txt"
ALLOW_FILE="$here/allow.txt"

usage() { echo "usage: $(basename "$0") [--allow REGEX ...] <files or directories...>" >&2; exit 2; }

# Read a pattern file: drop comments and blank lines, wrap each pattern, join with '|'.
read_patterns() {
  [ -f "$1" ] || return 0
  perl -ne 'chomp; s/\r$//; next if /^\s*(#|$)/; push @p, "(?:$_)"; END { print join("|", @p) if @p }' "$1"
}

join_alt() {
  # join non-empty arguments with '|'
  local out="" p
  for p in "$@"; do
    [ -n "$p" ] || continue
    if [ -n "$out" ]; then out="$out|$p"; else out="$p"; fi
  done
  printf '%s' "$out"
}

extra_allow=""
args=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --allow)
      [ "$#" -ge 2 ] || usage
      extra_allow="$(join_alt "$extra_allow" "(?:$2)")"; shift 2 ;;
    --allow=*)
      extra_allow="$(join_alt "$extra_allow" "(?:${1#--allow=})")"; shift ;;
    -h|--help) usage ;;
    *) args+=("$1"); shift ;;
  esac
done

[ "${#args[@]}" -gt 0 ] || usage

if [ ! -f "$BANNED_FILE" ]; then
  echo "style gate: missing word list $BANNED_FILE" >&2
  exit 2
fi
BANNED="$(read_patterns "$BANNED_FILE")"

DASH_MD='—|&mdash;|&#8212;'
DASH_TEX='—|---'
# AI-tell phrases: hard failures, built in.
TELLS='\b[Gg]enuinely\b|\b[Pp]aramount\b|\bunderscor\w* the need\b|\bsweet spot\b|\bit is worth noting\b|\bin today.s\b|\bdive into\b|(?i:\bgame.?changer\w*|\bcutting.edge\b|\brevolutionary\b|\btransformati(?:ve|onal)\b|\bsupercharg\w*|\bneedless to say\b|\bit(?:.s| is) no secret\b|\bat the end of the day\b|\bthat being said\b|\blet.s look at\b|\b(?:it is|it.s) crucial to\b|\barguably one of the most\b)'
# Warnings only (printed, exit status unchanged): "not A, but B" pivots, recap phrases, narrated
# structure, and "comprehensive" (filler only when used as praise; judge by eye). Scope statements
# ("does not replace expert review") can trip these; judge each by eye. The Introduction's "rest of
# this paper is organized as follows" paragraph is exempt and not matched.
WARN_PAT='(?i:\bnot only\b[^.]{0,120}?\bbut\b|\b(?:is|are|was|were)(?: not|n.t) (?:just |only |merely |simply )?about\b|\b(?:is|are)(?: not|n.t) (?:just|only|merely|simply)\b|\b(?:it|this)(?:.s| is) not\b[^.]{0,80}?[,;] (?:it|this)(?:.s| is)\b|\bwe (?:do not|don.t)\b[^.]{0,80}?[,;.] we\b|\bin summary\b|\bto summari[sz]e\b|\bin this section,? we\b|\b(?:now we|we now) turn to\b|\bcomprehensive\b)'

# Expand directory arguments to the paper sources inside them, so the gate never reports clean
# having checked nothing. Collect candidate folders for a per-paper allow file on the way.
files=()
allow_dirs=("$PWD")
for a in "${args[@]}"; do
  if [ -d "$a" ]; then
    allow_dirs+=("$a")
    while IFS= read -r line; do files+=("$line"); done < <(find "$a" -type f \( -name '*.tex' -o -name '*.html' \) ! -path '*/backups/*' ! -path '*/.git/*' | sort)
  elif [ -f "$a" ]; then
    d="$(dirname "$a")"
    allow_dirs+=("$d" "$d/..")
    files+=("$a")
  else
    echo "style gate: no such file or directory: $a" >&2
    exit 2
  fi
done

if [ "${#files[@]}" -eq 0 ]; then
  echo "style gate: no .tex or .html sources matched ${args[*]}" >&2
  exit 2
fi

# Allow patterns: generic file, each distinct per-paper file found, then --allow.
ALLOW="$(read_patterns "$ALLOW_FILE")"
seen=""
for d in "${allow_dirs[@]}"; do
  f="$d/.paper-style-allow"
  [ -f "$f" ] || continue
  real="$(cd "$(dirname "$f")" && pwd)/.paper-style-allow"
  case "|$seen|" in *"|$real|"*) continue ;; esac
  seen="$seen|$real"
  echo "style gate: using per-paper allow file $real" >&2
  ALLOW="$(join_alt "$ALLOW" "$(read_patterns "$f")")"
done
ALLOW="$(join_alt "$ALLOW" "$extra_allow")"
# A pattern that can never match keeps the perl substitution valid when nothing is allowed.
[ -n "$ALLOW" ] || ALLOW='(?!)'

hits=0
warns=0
for f in "${files[@]}"; do
  case "$f" in
    *.tex) DASH="$DASH_TEX" ;;
    *)     DASH="$DASH_MD" ;;
  esac
  # Strip allowed literals from each line, then test. perl: BSD sed lacks \w.
  out=$(perl -ne 'BEGIN { $allow = shift; $pat = shift; } my $l = $_; $l =~ s/$allow//g; my @m = ($l =~ /$pat/g); print "$.:" . join(" ", @m) . "\n" if @m;' "$ALLOW" "$DASH|$BANNED|$TELLS" "$f" || true)
  if [ -n "$out" ]; then
    echo "== $f"
    echo "$out"
    hits=$((hits + $(echo "$out" | wc -l | tr -d ' ')))
  fi
  wout=$(perl -ne 'BEGIN { $allow = shift; $pat = shift; } my $l = $_; $l =~ s/$allow//g; my @m = ($l =~ /$pat/g); print "$.:" . join(" | ", @m) . "\n" if @m;' "$ALLOW" "$WARN_PAT" "$f" || true)
  if [ -n "$wout" ]; then
    echo "== $f (warnings: sentence shapes, see style.md Sentence Shapes)"
    echo "$wout"
    warns=$((warns + $(echo "$wout" | wc -l | tr -d ' ')))
  fi
done

if [ "$warns" -gt 0 ]; then
  echo "style gate: $warns warning(s), review each by eye" >&2
fi
if [ "$hits" -gt 0 ]; then
  echo "style gate: $hits hit(s) in ${#files[@]} file(s)" >&2
  exit 1
fi
echo "style gate: clean (${#files[@]} file(s) checked)"

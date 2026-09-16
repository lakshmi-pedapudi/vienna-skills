---
name: <paper-slug>-status
description: "Status of the <topic> paper (<project> project): artifact + LaTeX draft locations, which numbers are authoritative, what is provisional, style rules. Read before any paper edit or review."
metadata:
  type: project
---

Paper "<Title>" (<organisation> / <product>). One-paragraph thesis. Sibling papers: [[<other-paper>-status]].

**Why:** <first draft date; what phase the paper is in>.
**How to apply:** read before touching either document. Records which numbers are authoritative and which are superseded so no stale table is reintroduced.

## Two Deliverables

1. **Reviewer-facing artifact (working doc):** <URL>
   Source: `<project>/paper/<name>.html` (N sections + appendices). Publish by passing the URL as `url`. Backup: `<name>.html.bak_<date>`. Superseded artifacts: <URL or id>, do not edit.
2. **arXiv LaTeX draft:** `<project>/arxiv_paper/` (`main.tex`, `sections/*.tex`, `figures/`, `references.bib`, `build.sh`, `README.md`). Build `./build.sh`. Section map to the artifact is in the README.

## Submission Plan

Venue, target format and length, author list and order (provisional or confirmed, with the date), deadline for order confirmation, companion papers.

## Which Numbers Are Authoritative

- **Source of truth:** <path to audit doc or unified CSV>, dated. Older drafts and their tables that are superseded: list the numbers explicitly and write "never reuse".
- **Headline table:** basis rows, treatment of declines or abstentions, file name, values.
- **Provisional:** what carries an asterisk or `\pilot`, why, what unblocks it.
- **Confounds:** label leakage, oracle hints, reference-is-baseline rows, warm starts.
- **Pending re-runs:** who is running what, on which split.

## Style Rules

No em-dashes. Banned: arm, instrument, license, contract, ground (filler), leverage, robust, seamless, delve, unlock. Title Case noun headings, Arabic numbering. Bullets and tables over prose. Never fabricate a number; gaps go to Appendix B. Charts: rust accent plus neutrals, hatch, direct labels. Check: `bash ~/.claude/skills/paper/scripts/check_style.sh sections/*.tex main.tex paper/*.html`.

## Decisions Applied

Folds, merges, drops, renames (with the reason and the date). Label conventions currently in force (Route A = ..., Route B = ...).

## Open Items

- `[TO BE FILLED]` slots and `\todo{}` notes with their blockers.
- Author list and order status.
- Vendor naming decisions.
- Data gaps: files not located, filters not reproducible, missing reports.
- Git status of the project folder (repo or not; the author's default is commit-and-push).

## Immediate Next Step

One line. What the next session does first.

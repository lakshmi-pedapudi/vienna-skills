---
name: <deck-slug>-status
description: "Status of the <name> deck (<project>): current and archived files, audience, rules added per review round, open items. Read before any edit or review of this deck."
metadata:
  type: project
---

Deck "<Title>" for <audience>, <occasion and date>. Family: <methodology / board / ...>, palette <field / DG>. Rules file: `<path>/CLAUDE.md` (or `DECK_PLAN.md`). Session record: `<path>/SESSION.md`.

**Why:** <first build date; which round the deck is in>.
**How to apply:** read before touching the script or the deck. Records which version is current, what each review round added, and what is still open.

## Files

- Current: `<deck>.pptx` (N slides, N images). Archived: `<deck>_v-1.pptx` (<date>, reason).
- Build: `build_deck.py`; charts `charts/gen_*.py`; registry `analysis/figures.csv`.
- Review carrier: `<deck>_review.pptx` (`Reviewer:` boxes) or Google Slides link.
- Frozen external copies (do not edit): <file or URL, date sent, recipient>.

## Rules Added per Round

- Round 1 (<date>): rules 1.1 to 1.N.
- Round 2 (<date>): ...

## Which Numbers Are Authoritative

- Registry `analysis/figures.csv`, <N> rows, last reconciled <date> against <source>.
- Superseded: <numbers never to reuse>.
- Pending or blocked: <key, owner>.

## Open Items

- <review comments not yet applied>.
- <numbers awaiting a person>.
- Git status of the folder.

## Immediate Next Step

One line.

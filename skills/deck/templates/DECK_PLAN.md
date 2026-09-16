# <Deck Name>: Rules and Build Plan

Read this file first in any session that touches `build_deck.py` or `<deck>.pptx`. Rules are numbered; add new rules with the next number, never re-derive style from scratch.

## 0. Orientation

| Item | Value |
|---|---|
| Audience | <who reads it; internal or external> |
| Occasion and date | <meeting, deadline> |
| Presenter | <name, on behalf of> |
| Slide budget | <N main + dividers + appendix> |
| Narrative spine | <one line> |
| Deck family and palette | <field / corporate example; primitives module> |
| Current file | `<deck>.pptx`; archived `_v-1`, `_v-2` |
| Rebuild | `python3 build_deck.py && python3 ~/.claude/skills/deck/scripts/check_layout.py <deck>.pptx && ...` |
| Expected baseline | <N slides, N images, ~N MB> |

## 1. Hard Rules

House rules from `~/.claude/skills/deck/references/style.md` apply. Project-specific rules below.

1.1 <rule, with the review comment that produced it>
1.2 ...

## 2. Structure

```
1   Cover
2   Overview                (table: Topic | Description)
3   SECTION 1 divider
...
N   Appendix divider
N+  Appendix slides
```

Ordering reasons: <why each section precedes the next>.

## 3. Sources of Substance

| Slide subject | Where the numbers and text come from |
|---|---|
| | `analysis/figures.csv` keys ..., `materials/...` |

## 4. Review Integration Log

| Round | Slide reviewed | Comment summary | Where it landed |
|---|---|---|---|
| 1 | | | Rule 1.x / slide rebuilt / slide dropped |

## 5. Default Behaviour for a New Claim

1. Strip any personal name or role attribution.
2. Expand any section code to the topic name.
3. Add the number to `figures.csv` with row set, source and status; reference it by key.
4. Promote a buried good number to the hero layout in the body; keep unflattering numbers inline.
5. Shorten a sentence title to its subject.
6. Put the source in speaker notes, not on the face.

## 6. Next Session

1. Read this file end to end, then `SESSION.md`.
2. If a new `<deck>_review.pptx` exists, extract `Reviewer:` comments, add rules, update script and deck together, log the mapping.
3. Rebuild, run the three checkers, open the file, check the PDF.

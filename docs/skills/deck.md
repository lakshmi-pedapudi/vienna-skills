# /deck

Use when building, revising, reviewing, or converting a slide deck or presentation for a research or product team: board or leadership decks, funder or workshop decks, partner pre-reads, CEO talks, methodology decks, tech updates, Google Slides or PDF exports. Also use when review comments come back on a deck, when a deck must be rebuilt from raw data, or when an artifact must be split into slides. Triggers: "/deck", "slide deck", "presentation", "pptx", "slides", "build the deck", "review comments on the deck", "tech update", "board", "workshop deck", "pre-read", "speaker notes", "google slides".

## Files

```
skills/deck/
  SKILL.md
  references/build.md
  references/figures.md
  references/lessons.md
  references/review.md
  references/style.md
  references/workflow.md
  scripts/check_figures.py
  scripts/check_layout.py
  scripts/check_words.py
  scripts/deck_primitives.py
  scripts/extract_review_comments.py
  scripts/preview_slides.py
  templates/DECK_PLAN.md
  templates/REVIEW_LOG.md
  templates/REVIEW_NOTES.md
  templates/SESSION.md
  templates/build_deck_example.py
  templates/deck_status_memory.md
  templates/figures.csv
  templates/topic.md
```


# Deck Building and Review

House workflow for slide decks, distilled from nine decks (a board deck, a production latency report, methodology decks, a CEO conference talk, funder workshop decks and their pre-read, research slides) and roughly 200 instructions and corrections given while building them. Every deck is python-pptx from a deterministic script, never hand-edited.

**Core principle:** the script is the source of truth and the `.pptx` is disposable. Charts and tables carry the content, text is short numbered points with bold lead-ins, every number resolves to one registry row, and nothing internal appears on a slide that leaves the building.

**Scope:** this skill carries rules, not any one deck's content. Past decks appear only as provenance and as the shape of an example. No number, model name, vendor, denominator or slide title in this skill or in its templates belongs to the deck in front of you: every figure comes from that deck's own registry, and every claim from its own source data. Where an example names a subject (a crop, a language, a modality, a vendor), the rule transfers and the subject does not.

## When to Use

- A new deck for any audience: board, CEO, funder, partner workshop, internal team.
- Review comments arrived (a `_review.pptx` with `Reviewer:` boxes, Google Slides comments, or a numbered list).
- A deck has degraded through patching and must be rebuilt from raw data.
- An artifact or long document must be cut into slides, or a deck exported to Google Slides or PDF.
- Not for: the HTML page itself (use `/artifact`), the research paper (use `/paper`), a stakeholder email (CLAUDE.md stakeholder rules).

## Session Start

1. Read the project's deck rules file (`CLAUDE.md` or `DECK_PLAN.md` in the deck folder) and its status memory. If neither exists, create both from `templates/`. Rules there carry numbers; add new rules with the next number, never re-derive style from scratch.
2. Confirm audience, occasion, slide budget, and whether the deck leaves the organisation. External decks trigger the standalone rules in `references/style.md`.
3. Read `references/style.md`. The title rule, the word bans, and the no-names rule apply to every slide including the appendix and the speaker notes.

## Phase Flow

| Phase | Output | Detail |
|---|---|---|
| 0 Recall | Rules file, status memory, prior decks in the family | `references/workflow.md` §0 |
| 1 Collect | `materials/` drop zone, `topics/<slug>.md` per topic, saturation declared per topic | `references/workflow.md` §1 |
| 2 Skeleton | Section list with ordering reasons, slide budget, sub-task allocation; confirmed at a checkpoint question before any build | `references/workflow.md` §2, `references/review.md` §Checkpoint Questions |
| 3 Draft | `DECK_DRAFT.md` slide by slide, self-consistency pass | `references/workflow.md` §3 |
| 4 Build | `build_deck.py` on `scripts/deck_primitives.py`, `figures.csv` registry, charts as SVG and PNG | `references/build.md` |
| 5 Check | `check_layout.py`, `check_figures.py`, `check_words.py`, `preview_slides.py` PNGs read, open the file, check the PDF | `references/build.md` §Checks |
| 6 Review | Comments extracted, generalised into numbered rules, rules + script + deck updated together; convergent loop (2 to 3 passes, stop on agreement), `REVIEW_LOG.md` | `references/review.md` |
| 7 Ship | Version archive, external scrub, Google Slides or PDF, pre-read sibling | `references/workflow.md` §7 |
| 8 Close | `SESSION.md` record, status memory, hand-off note | `references/workflow.md` §8 |

Phases repeat. A review round re-enters at 2 or 3, never at 4 alone.

## Non-Negotiables

- Titles are plain nouns, 1 to 4 words ("Current Pipeline", "Image Analysis", "Inference Cost"). No sentence titles, no questions, no "X not Y", no narration of what the slide will show. The takeaway goes in the body.
- Chart or table first. Text only as short numbered or bulleted points, each opening with a bold lead-in. Never a paragraph on a slide. "Don't be overly descriptive where tables/charts can do the trick."
- One deck per session's working set. Decks in a family share primitives, slide titles and registry key names; confirm which deck and which registry before every edit, and never carry a figure from one deck into another.
- Every number is fetched from `figures.csv` by key with its row set and source. Unknown key fails the build. Pending or blocked numbers render as a visible pending block naming the owner. No number is typed into the script or baked into an image.
- No personal names, role attributions, internal section codes, task ids, or references to other documents anywhere on a slide face or in speaker notes of a deck that leaves the organisation. Sources go in speaker notes for internal decks.
- Plain English. Banned: em-dashes, AI tells (leverage, robust, seamless, delve, unlock), consultant jargon (blast radius, mitigation in flight, force multiplier, fan-out, cohort, surface area, operationalise, headline), invented vocabulary (arm, axes, verdict, "under the rule"), "Theme N", "Why it matters" (write "Impact").
- Native text boxes and native tables. Images only for structural visuals (flowcharts, architecture, charts with axes). Diagrams carry structure, not measurements, and no title of their own.
- One hero number per slide, and only for good news. Unflattering numbers go inline with their qualifier.
- Skeleton approved before build. Proposed rewrites shown in chat before the live file changes. Change exactly what was asked.
- Checkpoint questions at topic segregation, skeleton and budget, narrative spine, and before any restructure, even in bypass mode: one or two simple questions with a recommended option, via AskUserQuestion. Nowhere else.
- Review runs as a convergent loop: at least two passes, at most three, each re-verifying every earlier fix by id; stop only when two successive passes agree. Log in `REVIEW_LOG.md`.
- Snapshot before any restructure (`deck_v-1.pptx`, `DECK_DRAFT.md.bak_<date>`). A deck or URL already sent outside is frozen.
- Charts via matplotlib and diagrams via Graphviz DOT, always saved as SVG and PNG. Never Mermaid. Never a raster whose text Claude cannot read back.

## Quick Reference

| Need | Go to |
|---|---|
| Titles, bullets, tables, word bans, names, external scrub, hero numbers, speaker notes | `references/style.md` |
| Collection loop, skeleton, draft, ship, close, folder layout | `references/workflow.md` |
| python-pptx conventions, palettes, primitives, registry, charts, checkers, pitfalls | `references/build.md` |
| Chart forms, palettes per modality, distribution views, diagram polish | `references/figures.md` |
| Review intake, rule generalisation, integration log, three-bucket notes, slide-level diffs, checkpoint questions, convergent review loop | `references/review.md` |
| Dated corrections and pushbacks, rationalization table | `references/lessons.md` |
| Scripts: primitives, layout and figure checkers, word gate, slide preview renderer, review extractor | `scripts/` |
| Templates: DECK_PLAN, figures.csv, topic file, SESSION record, status memory, REVIEW_NOTES, example build | `templates/` |

## Red Flags

Stop and re-read the relevant reference when any of these appear in your own output or plan:

- A title longer than four words, or one that could be read aloud as a sentence.
- A paragraph of prose in a text box, or a tile that describes instead of listing.
- A number in the script that is not `fig("key")`, or a chart drawn from a number that exists only on a slide.
- A person's name, a code like B1 or T2.1, a Linear id, or "as discussed" on any slide or note of an external deck.
- "Theme", "Why it matters", "arm", "blast radius", or an em-dash anywhere in the deck text.
- A hero tile carrying a rejection rate or a failure share.
- Editing the `.pptx` by hand, or building a new deck when told to augment the existing one.
- A rebuild without running the three checkers and opening the file.
- Reporting a list of defects as fixed without re-checking each one.
- A table, chart and takeaway on the same slide that disagree.
- "the paid outside service", "a fine-tuned open model", or any other euphemism where the vendor or model name is cleared for use.
- A caveat footnote on most slides, or a slide with no speaker notes on an internal deck.

## Session Close

Write or update `SESSION.md` in the deck folder (sources consulted, produced, reproduce commands, claim set with sources, caveats, still open) and the status memory (current version, archived versions, rules added this round, open review items, next step). If the user asks to clear context, the status memory must let a cold session rebuild the deck with no memory of the conversation.

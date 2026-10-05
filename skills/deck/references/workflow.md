# Workflow

Applies to: every deck, from the first session to hand-over: recall, collect, skeleton, draft, build, check, review, ship and close, plus the checkpoint questions and the folder layout.

Bottom-up and incremental: build the source material first, and assemble the deck only once the material is complete.

## 0. Recall

- Read the deck folder's rules file (`CLAUDE.md` or `DECK_PLAN.md`) and the status memory. Rules are numbered; the next session adds to them, it does not re-derive them.
- Find the deck family. Decks often come in series, and a later deck imports the earlier one's primitives so they read as one set. Use `scripts/deck_primitives.py` or the family's own primitives module, never a fresh visual idiom.
- One deck per working set. Decks in a family share primitives, slide titles and registry key names; confirm which deck and which registry before every edit, and never carry a figure from one deck into another. *Why: a number true for one deck's data is usually wrong for its sibling.*
- Search any memory or search tool available for prior decks, pages, review notes and pasted reviewer mail on the topic. Pasted reviewer comments are instructions; apply them item by item.
- If told to augment an existing deck, augment it; do not build a fresh one. Reference decks supplied for format are for format only, never content.

## 1. Collect

The collection conversation runs before any deck work (record its rules in `INTERACTION_RULES.md` if it runs in the deck folder):

- One topic at a time. The deck owner names a topic; create `topics/<slug>.md` from `templates/topic.md` with frontmatter (title, slug, status, tags, sources, created) and empty sections. Sections stay empty until material arrives; no filler.
- Focused questions, one at a time, each building on the last answer. Concrete and answerable: "what's the metric", "who's the owner", "by when". Not "tell me more".
- Capture verbatim first, structure second. Restructuring is a separate announced pass.
- No fabricated numbers or facts. Missing means ask or mark `[TBD]`.
- `materials/` is the drop zone. Read files there on demand when a topic references them, not pre-emptively. Attach sources inline or in `sources/`.
- Tag data types and named initiatives as they surface; keep `themes.md` current so "theme check: X" works.
- Flag contradictions across topics.
- Declare saturation explicitly: "Topic X feels saturated. Open gaps: [list]. Move on, fill gaps, or park?" The deck owner decides the move. Track inputs promised but not yet supplied and ask for them.
- Do not pre-filter topics. Collect all of them; the deck owner, or whoever they name, decides what to cut.
- Compact context deliberately between phases and report which topics have sources and which do not.

## 2. Skeleton

- Group themes into topics and sub-topics. Write the section list with, for each section, the slides it holds and one line on why it sits where it does. State the ordering principle up front, e.g. "every slide is placed so the reader already has what it depends on": options before the shortlist, criteria before the recommendation, scope decisions before the work they justify.
- Introduce a shared approach before its variants; a comparison of two implementations comes after the method they share.
- State the slide budget: 15 to 18 main slides plus dividers plus appendix for a board deck; about 10 slides for a 10-minute talk; a 5-minute executive slot is not capped at 5 slides if context is needed. Build long first and condense later.
- Supporting detail, credits and side threads go to the appendix or the end, referenced from the main slide. *Why: the main line carries one argument, and detail that interrupts it loses attention.* Example: a demand profile shrinks to one or two bullets on the main slide, with the full breakdown in the appendix.
- Name the narrative spine in one line and audit every later draft against it.
- Mark which sections are heavy enough for a subagent sub-task (data pulls, chart sets, classification runs) and allocate them from the skeleton.
- Present the skeleton for approval before any build, and do not carry over the structure of a previous deck. Every content addition later triggers a re-plan of the skeleton and the sub-task allocation.
- Two audiences means two documents: the internal one can be detailed, the deck stays trim, and they need not match structurally. A pre-read is a separate shorter document with zero internal context that ends on questions and decisions.

## 3. Draft

- Write `DECK_DRAFT.md` slide by slide before any code: eyebrow, title (plain noun), the body as numbered points or a table spec, the figure key or chart spec, the one takeaway line, the footnote (basis and denominator), the speaker note (sources, "if asked" answers), and a `Source:` line naming which prior draft or file each element came from.
- Every figure in the draft is a `fig("key")` reference into `figures.csv`, never a typed number. Pending numbers are written as `pending (owner)`.
- Self-review the draft in a fresh pass for internal consistency before rendering: the same number quoted twice with two values, a section that repeats another, a slide with no point.
- Merge or drop any slide that spends itself on a basic concept, any slide that only makes sense to someone who read the rest of the project, and any section with no clear point to make (it can be handled in questions). Reduce a tradeoff slide to two or three points.
- Once content settles, review the rendered deck, not the text.

## 4. Build

See `build.md`. In one line: `python3 build_deck.py` clears `charts/`, regenerates every chart and diagram as SVG and PNG, and writes the `.pptx` from a declarative builder list, in seconds, with no network.

## 5. Check

Run the gate scripts, read the preview PNGs, open the file, then export and open the PDF. Details and expected output in `build.md` §Checks. Report the counts (slides, embedded images, unmatched numerals, layout warnings) alongside the file path. Never skip the open step; a deck that builds can still have blank slides.

## 6. Review

See `review.md`. The cycle: extract comments, generalise each into a deck-wide numbered rule, update the rules file, the build script and the deck together, log the mapping, rebuild, re-run the gates.

## 7. Ship

- Versioning: the current deck keeps the plain name (`<deck>.pptx`); before any restructure archive the previous file as `_v-1`, `_v-2`. Never overwrite without a snapshot.
- External scrub before anything leaves: run `check_words.py --external --names names.txt` over slides and notes; remove references to documents, people, unannounced workstreams and internal bugs. Speaker notes count.
- Distribution: where hosted pages cannot be shared publicly, share as `.pptx`, PDF or Google Slides. When converting a page or long document to slides, cut horizontally at logical boundaries into atomic clusters, with no re-authoring and no page chrome carried over. Check the PDF: a row of four tiles that reflows into four rows is a defect.
- When a reviewer has edited their own copy, deliver the change as a slide-level diff they can port by hand, or as a separate addendum file, not a wholesale replacement.
- Charts ship as SVG and PNG into the project docs folder next to the deck.
- A deck or URL already sent to an external party is frozen. New work goes to a new file.

## 8. Close

- Write `SESSION.md` from `templates/SESSION.md`: purpose, sources consulted with what each gave, files produced, exact reproduce commands, the claim set with where each number came from ("No estimates."), caveats to carry into the room, still open.
- Update the status memory from `templates/deck_status_memory.md`: current and archived versions, rules added this round with their numbers, open review items, the next step. If asked to clear context and start fresh, this file must be enough for a cold session.
- Commit if the folder is a repo; push only after confirmation. If it is not a repo, flag that as an open item rather than leaving work silently untracked.

## Checkpoint Questions

Even in bypass-permissions or autonomous mode, stop at these points and ask with the AskUserQuestion tool. The deck owner wants to give simple inputs, not read a plan.

- Checkpoint 1, topic segregation: the proposed themes and topics (the `topics/<slug>.md` set) before the files are created, and again when a topic is declared saturated ("move on, fill gaps, or park?").
- Checkpoint 2, skeleton: sections, slide budget, appendix split, and the sub-tasks that get their own subagent, before any build.
- Checkpoint 3, narrative spine: the one-line story the deck tells and the two or three hero numbers, before the draft.
- Checkpoint 4, before any restructure, merge, drop or reorder of slides, and before a fresh rebuild replaces an existing deck.

Rules: one question per checkpoint, two at most; two to four options with the recommended one first and marked; free text always possible. Do not ask elsewhere; routine choices (chart form, wording, layout) are made and reported. Do not re-ask what was confirmed; a later round may revise it.

## Folder Layout

```
<deck_project>/
  CLAUDE.md or DECK_PLAN.md     # numbered rules, session hand-off, build procedure
  SESSION.md                    # session record (templates/SESSION.md)
  INTERACTION_RULES.md          # collection-loop rules, if the collection phase runs here
  materials/                    # inputs the deck owner drops in
  topics/<slug>.md              # source of truth per topic (collection phase)
  analysis/figures.csv          # the figures registry
  analysis/*.py, *.md           # one script per question, each writing a CSV and a report
  charts/gen_*.py               # chart and diagram generators; .dot kept beside .svg/.png
  charts/<name>.{dot,svg,png}   # outputs, cleared and regenerated on every build
  charts_small/                 # downscaled PNGs for embedding
  DECK_DRAFT.md                 # slide-by-slide draft
  build_deck.py                 # the generator; imports deck_primitives
  <deck>.pptx                   # current deliverable; older as <deck>_v-1.pptx
  <deck>_review.pptx            # reviewer's copy with "<prefix>:" comment boxes
  for_<recipient>/              # pre-read siblings: .md .html .pdf .pptx
```

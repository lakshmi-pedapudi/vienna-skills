# Workflow: Collect, Skeleton, Draft, Build, Ship, Close

Bottom-up and incremental, the same shape as the paper skill. The author's framing at the start of the board deck: "we slowly build the sources and underlying material first. and then only when we have all the material we need in detail, let's go for the final presentation."

## 0. Recall

- Read the deck folder's rules file (`CLAUDE.md` or `DECK_PLAN.md`) and the status memory. Rules are numbered; the next session adds to them, it does not re-derive them.
- Find the deck family. Decks come in series and a later deck imports the earlier one's primitives so they read as one set (methodology to audio to the funder to VLM). Use `scripts/deck_primitives.py` or the family's own primitives module, never a fresh visual idiom.
- Run Eagle Mem search and `/brain` for prior decks, artifacts, review notes and pasted reviewer mail on the topic. Pasted reviewer comments are instructions; apply them item by item.
- If told to augment an existing deck, augment it. "But I thought I told you not to create a fresh deck, it needs to be an augmented version." Reference decks supplied for format are for format only, never content.

## 1. Collect

The collection conversation runs before any deck work (the board `INTERACTION_RULES.md`):

- One topic at a time. The author names a topic; create `topics/<slug>.md` from `templates/topic.md` with frontmatter (title, slug, status, tags, sources, created) and empty sections. Sections stay empty until material arrives; no filler.
- Focused questions, one at a time, each building on the last answer. Concrete and answerable: "what's the metric", "who's the owner", "by when". Not "tell me more".
- Capture verbatim first, structure second. Restructuring is a separate announced pass.
- No fabricated numbers or facts. Missing means ask or mark `[TBD]`.
- `materials/` is the drop zone. Read files there on demand when a topic references them, not pre-emptively. Attach sources inline or in `sources/`.
- Tag data modes (text, voice, image, language) and named initiatives as they surface; keep `themes.md` current so "theme check: X" works.
- Flag contradictions across topics.
- Declare saturation explicitly: "Topic X feels saturated. Open gaps: [list]. Move on, fill gaps, or park?" The author decides the move. Track inputs promised but not yet supplied and ask for them.
- Do not pre-filter topics. "we're not picking anything. let's make a presentation with all topics and let vineet figure out what to keep and what to lose."
- Compact context deliberately between phases and report which topics have sources and which do not.

## 2. Skeleton

- Group themes to topics to sub-topics. Write the section list with, for each section, the slides it holds and one line on why it sits where it does. The the funder skeleton stated its ordering principle up front: "Every slide is placed so the reader already has what that slide depends on" (routes before the candidate list, all four decision criteria before the lean, scope decisions before the work they justify).
- State the slide budget: 15 to 18 main slides plus dividers plus appendix for a board deck; about 10 slides for a 10-minute talk; a CEO 5-minute slot is not capped at 5 slides if context is needed. Build long first, condense later: "keep it as detailed as necessary, we'll condense it later."
- Name the narrative spine in one line and audit every later draft against it.
- Mark which sections are heavy enough for a subagent sub-task (data pulls, chart sets, classification runs) and allocate them from the skeleton.
- Present the skeleton for approval. "first give me the skeleton structure ... Only after I approve the planned skeleton structure, go ahead and build the full deck. don't carry forward any existing bias regarding the slides." Every content addition later triggers a re-plan of the skeleton and the sub-task allocation.
- Two audiences means two artefacts: the internal doc can be detailed, the deck stays trim, and they need not match structurally. A pre-read is a separate shorter document with zero internal context that ends on questions and decisions.

## 3. Draft

- Write `DECK_DRAFT.md` slide by slide before any code: eyebrow, title (plain noun), the body as numbered points or a table spec, the figure key or chart spec, the one takeaway line, the footnote (basis and denominator), the speaker note (sources, "if asked" answers), and a `Source:` line naming which prior draft or file each element came from.
- Every figure in the draft is a `fig("key")` reference into `figures.csv`, never a typed number. Pending numbers are written as `pending (owner)`.
- Self-review the draft in a fresh pass for internal consistency before rendering: same number quoted twice with two values, a section that repeats another, a slide with no point. "Review ... one more time for internal consistency (review your own work in a fresh iteration)."
- Merge or drop any slide that spends itself on a basic concept, and any slide that only makes sense to someone who read the rest of the project. "Section 6.6 - completely skip. we don't have a good point to make here."
- Once content settles, review the rendered deck, not the text: "It's time we take a look at what the final product looks like and conduct a review at that level instead of at text level."

## 4. Build

See `references/build.md`. In one line: `python3 build_deck.py` clears `artefacts/` or `charts/`, regenerates every chart and diagram as SVG and PNG, and writes the `.pptx` from a declarative builder list, in seconds, with no network.

## 5. Check

Run all three checkers, then open the file, then export and open the PDF. Details and expected output in `references/build.md` §Checks. Report the counts (slides, embedded images, unmatched numerals, layout warnings) alongside the file path. A deck handed over with blank slides was reported twice in one evening; never skip the open step.

## 6. Review

See `references/review.md`. The cycle: extract comments, generalise each into a deck-wide numbered rule, update the rules file and the build script and the deck together, log the mapping, rebuild, re-run checks.

## 7. Ship

- Versioning: the current deck keeps the plain name (`deck.pptx`); before any restructure archive the previous file as `_v-1`, `_v-2`. Never overwrite without a snapshot.
- External scrub before anything leaves: run `check_words.py --names names.txt` over slides and notes; remove references to documents, people, unannounced workstreams and internal bugs. Speaker notes count.
- Distribution: org policy blocks public artifact links, so anything shared outside goes as `.pptx`, PDF, or Google Slides. When converting an artifact to slides, cut horizontally at logical boundaries into atomic clusters, no re-authoring, no chrome carried over. Check the PDF: a row of four tiles that reflows into four rows is a defect.
- When a reviewer has edited their own copy, deliver the change as a slide-level diff they can port by hand ("can I just take slide 7 from _6 and replace it in _5?"), or as a separate addendum file, not a wholesale replacement.
- Charts ship as SVG and PNG into the project docs folder next to the deck.
- A deck or URL already sent to an external party is frozen. New work goes to a new file.

## 8. Close

- Write `SESSION.md` from `templates/SESSION.md`: purpose, sources consulted with what each gave, files produced, exact reproduce commands, the claim set with where each number came from ("No estimates."), caveats to carry into the room, still open.
- Update the status memory from `templates/deck_status_memory.md`: current and archived versions, rules added this round with their numbers, open review items, the next step. If asked to "clear context and start fresh", this file must be enough for a cold session.
- Commit and push if the folder is a repo. Most deck folders were not; flag it as an open item rather than silently leaving work untracked.

## Folder Layout

```
<deck_project>/
  CLAUDE.md or DECK_PLAN.md     # numbered rules, session hand-off, build procedure
  SESSION.md                    # session record (templates/SESSION.md)
  INTERACTION_RULES.md          # collection-loop rules, if the collection phase runs here
  materials/                    # inputs the author drops in
  topics/<slug>.md              # source of truth per topic (collection phase)
  analysis/figures.csv          # the figures registry
  analysis/*.py, *.md           # one script per question, each writing a CSV and a report
  charts/gen_*.py               # chart and diagram generators; .dot kept beside .svg/.png
  charts/<name>.{dot,svg,png}   # outputs, cleared and regenerated on every build
  charts_small/                 # downscaled PNGs for embedding
  DECK_DRAFT.md                 # slide-by-slide draft
  build_deck.py                 # the generator; imports deck_primitives
  <deck>.pptx                   # current deliverable; older as <deck>_v-1.pptx
  <deck>_review.pptx            # reviewer's copy with "Reviewer:" boxes
  for_<recipient>/              # pre-read siblings: .md .html .pdf .pptx
```

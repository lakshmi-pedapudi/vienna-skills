# Workflow

Applies to: every phase of a paper from first materials to hand-off. Section numbers match the phase table in `SKILL.md`.

The build is bottom-up and incremental: gather materials by theme, write a basic structure, publish a bare skeleton artifact with mapped sources, then fill it one element at a time (section, subsection, table, chart) before any LaTeX exists. *Why: every element is reviewed against its evidence while it is still small.*

## Checkpoint Questions

Even in bypass-permissions or autonomous mode, stop at these points and ask with the AskUserQuestion tool. The author wants to give simple inputs, not read a plan.

- Checkpoint 1, materials segregation: the proposed thematic folders (`01_background`, `02_pipeline`, ...) before any folder is created or filled.
- Checkpoint 2, skeleton: the section list with mapped sources, plus the length target and any budget ("50% data, 50% methodology"), before drafting.
- Checkpoint 3, rough themes: the two or three claims the paper will make and the figures that carry them.
- Checkpoint 4, before any restructure, trim plan, merge or cut of a whole section, or a change of skeleton.

Rules: one question per checkpoint, two at most; two to four options with the recommended one first and marked; free text always possible. Do not ask elsewhere; routine choices are made and reported. Do not re-ask what was confirmed; a later round may revise it.

## 0. Recall

- Read the paper's status memory file first. It names the active artifact URL, the LaTeX folder, authoritative versus superseded numbers, style rules, decisions applied, open items. It is the only source for this paper's numbers and structure; nothing about a sibling paper enters the working set.
- Search any memory or search tool available for prior artifacts, workshop drafts, analysis documents, shared-drive documents, and chat or call notes the author pastes in. Pasted chats and call summaries are source material; extract facts and decisions from them.
- For a new paper, read the team's reference papers (listed in the status memory, if any) for structure and voice. Once the author supplies a skeleton, that skeleton overrides prior-paper conventions.
- Do not take early aggregate metrics seriously. Build the raw row-level data and the matching predictions first. *Why: aggregates computed before the rows exist are usually wrong in ways no one can trace.*

## 1. Gather Materials

Create `paper/materials/` in the project folder (durable, never the session scratchpad):

```
paper/materials/
  README.md                       # table: Folder | Contents | Paper section; bolded corrections inline
  01_background_motivation/
  02_pipeline_architecture/
  03_<module>_M0/
  ...
  NN_<gap_name>/GAP_NOTE.md       # one per suspected gap
```

- Organise by paper section or theme, not by source repository. Zero-padded numbered folders; gaps in numbering are fine.
- Copy evidence files (CSVs, result JSONs, plots, extraction scripts). Exclude huge binaries (caches, raw image folders, parquet feature stores) and say so in the README.
- Every folder README row maps to a paper section. Corrections go inline in bold: "**Its headline table (a / b / c / d) is superseded by the <date> audit**".
- `GAP_NOTE.md` for each gap the author suspects: status in the heading ("# Status: <Component> Is Not Missing"), what the folder holds, a "Headline numbers (measured, not projected)" table. Gaps resolved as not-gaps stay documented.
- Sub-evidence stays reproducible: keep the extraction script next to its output.
- Raw row-level datasets are listed separately from derived aggregates so any aggregate can be re-derived. This list becomes Appendix A.

## 2. Skeleton

- Draft the section list with mapped sources per section, `[TO BE FILLED]` for results not yet run. Use `structure.md`.
- Present the skeleton for approval (Checkpoint 2) before drafting anything. Do not carry forward structure from an older deck or draft; rebuild from the requirement.
- Order sections by dependency: nothing appears before what it depends on (pipeline options before the evaluation candidates they determine). Section weight follows importance, not availability of material: a side topic gets a short late section, not a pillar.
- If the author asks for a budget ("50% data, remaining methodology"), record it in the status memory and hold to it.
- Plan subagent hand-offs off the skeleton: which sections are heavy enough for a parallel micro-task.

## 3. Reviewer-Facing Artifact

The HTML artifact is the working draft that the author, teammates and a second model review. It precedes any PDF.

Build rules:
- One element at a time: a section, a subsection, a table, a chart. Fill a section only when its source exists or the author supplies the content. Sections without data (Results, Discussion, Impact) stay visibly empty with a pending note. Do not over-commit or run ahead unprompted.
- Per-section pattern: card with section number and status pill (sourced / outlined / pending), source chips naming the file or document behind the section, then content (tables, module cards, inline SVG figure with caption), then a dashed pending box for anything provisional.
- Status card at the top: draft date, headline scale facts, submission plan when agreed.
- Abstract as labelled blocks (Problem, Key Challenges, Proposed Approach, Evaluation, Main Results) until prose is warranted.
- Appendix A (Materials and Sources) and a reconciliation section from the first publish. In the artifact the reconciliation section is visible to reviewers; it never reaches the external PDF (`structure.md`, Reconciliation Register).
- Load the `artifact-design` and `artifact-diagramming` skills, and an artifact skill if one is installed, before writing HTML. Inline hand-authored SVG for flowcharts; theme through CSS tokens for light and dark; no external chart libraries needed.
- No em-dashes in HTML either, neither the entity form nor the U+2014 character. Run `scripts/check_style.sh` on the file before publishing.

File and publish rules:
- The HTML source lives in the project folder (`paper/<name>.html`), not the session scratchpad. *Why: session scratch space is not durable.*
- Republish by passing the existing URL as `url`. Omitting it forks a new artifact and loses the review trail. Superseded artifacts are recorded in the status memory as "do not edit".
- Back up before any restructure: `<name>.html.bak_YYYY-MM-DD`.
- Teammates may edit the artifact collaboratively. Before editing, `read` the live version and diff against the local copy; merge rather than overwrite.
- When restructuring, say what is reorganised versus what is new content. Reorganisation must not smuggle in additions.

## 4. LaTeX Folder

```
arxiv_paper/
  main.tex                 # preamble, macros, \input of sections in order
  sections/00_abstract.tex ... NN_conclusion.tex, appendix.tex
  figures/fig_*.dot        # Graphviz diagrams
  figures/make_charts.py   # data charts from materials CSVs; emits PDF + SVG (+ CSS-vars SVG for the artifact)
  tables/                  # optional
  references.bib
  build.sh                 # dot -> pdf/svg, make_charts.py, tectonic -X compile main.tex
  README.md                # section map to the artifact, style rules, pre-commit grep, open items
```

- The LaTeX draft is usually a tightened fold of the artifact (fewer sections). The README carries a Section Map table listing folds, merges and drops with reasons. Apply the same folds to the artifact only if asked (it renumbers every reference).
- Macros: `\todo{...}` (accent colour, bracketed, states what will appear, where it comes from, what blocks it), `\pilot` (superscript p on pilot-scale numbers), `\flag{...}` (accent tint on a proposed or problematic value). No bare `TBD`.
- Build with tectonic, Graphviz `dot` and `rsvg-convert`. `./build.sh` must compile clean before any commit.
- Author block, affiliation, ownership and corresponding author: see `submission.md`, Author Block.
- One master per format. If two formats must coexist (single-column and IEEEtran), they share `sections/`, and every edit names the files it touched. When two candidate master files exist (`main.tex` and `main_<variant>.tex`), name the target back to the author before editing. *Why: edits split across two masters are the hardest drift to undo.*

### Update Guide

When results are still landing, write `PAPER_UPDATE_GUIDE.md` in the paper folder: placeholder inventory (file, table label, field, data needed), two update paths (drop CSV with exact expected headers, or inline values), figure swap instructions, compile commands, and a submission checklist. Later the author points at the guide plus the new results file and asks for the update. The guide is the agreed input format for that.

## 5. Review

Run the passes and the convergent loop in `review.md`. Output: `CRITICAL_REVIEW.md`, `REVIEW_LOG.md`, `citation_verification.csv`.

## 6. Submit

Follow `submission.md`: format and length decisions, author block, arXiv package compiled from a clean extract, pre-submission checklist, data and code releases.

## 7. Close and Hand-off

- Update the status memory: locations, authoritative versus superseded numbers, decisions applied, open items, next step. This file is the only thing that survives a context reset.
- Before a long build phase, offer to compact.
- "Write it up" or "write this up and let's close" means: persist findings and decisions to the plan and status files, not just the chat.
- When asked to retain what is needed to restart a fresh session, write the hand-off in the shape of `templates/paper_status_memory.md`: project thesis, active artifact file and URL, superseded artifacts, structure with anchors, style rules, key content already present, source materials, standing instructions, open items, immediate next step.
- Paper project folders are often not git repos. Ask once whether to `git init` and whether to commit after substantive changes; record the answer in the status memory. Push only after confirmation.

## Incremental Edits

- Patch, never regenerate. Change only what the author asked for and touch nothing else. *Why: a regenerated file hides every unrequested change inside the requested one.*
- Prefer scripted patches for repeated edits across many section files (`patch_*.py`) so the change is reviewable and re-runnable.
- After every edit batch, report which files changed. Offer the diff when the author asks what moved.
- Roll back a specific change on request without touching the rest.
- Strip rather than delete when a reviewer has not weighed in yet.
- Before deleting a block for redundancy, grep for everything that points at it, and re-check numbering of the subsections after it. *Why: claims elsewhere can be left standing on support that was just cut.*
- Before dropping a model or variant from a results table, list every figure measured only on its data (behaviour rates, confusion pairs, per-class readings) and decide per item: recompute on a surviving model's shared rows, or cut. *Why: otherwise one checkpoint's measurements are silently credited to another.*
- Sweep the whole document after any rename or number change. Half-updated documents are the most common complaint. A changed result is propagated in one pass to every carrier listed in `style.md`, Where Numbers Live (including derived differences and ranges), plus the artifact's matching sections and the status memory's authoritative-numbers list. Run `scripts/check_number_placement.py arxiv_paper/` afterwards.
- When the author pastes an independent review from another model or person: judge each comment on merit, adopt what holds, say what does not and why, and do not deviate far on the strength of one review.
- When the author supplies a subsection verbatim, insert it faithfully (bold lead-in bullets are fine), add its citations to the references section, and do not rewrite it.
- Keep reporting while working. After a couple of failed attempts at a simple edit, stop, say what is blocking, and ask; long silent tool loops are a failure.

## Collaborative Reconciliation

When a co-author or reviewer edits their own copy (their own artifact, their own branch), converge on one master (usually the arXiv `main.pdf` source) and let every other surface follow it.

- Build a differences sheet before changing anything: one row per difference, a one-line statement of the section's purpose, their version, our version, and an empty Comments column for the author to fill. One CSV plus one README in a dedicated folder.
- Reconcile only after the sheet comes back filled, row by row, content differences before style ones.
- Take the hard content wins from their draft and keep this skill's rules for everything else.
- A section their version explains better is merged at the same length, not appended.

## Page Reduction

Cutting to a page target is a plan the author approves before execution (Checkpoint 4), with per-item savings. The levers, in order of least damage:

- **A. Layout.** Margins, table and caption font size, float separation (`\intextsep`, `\textfloatsep`), list spacing.
- **B. Figure geometry.** Size each figure to its content; drop the default full text width.
- **C. Table surgery.** Merge related tables, restructure wide ones as two side by side, demote an explanatory table to bullets, move a redundant one to the appendix.
- **D. Content reframing and cuts.** Collapse prose into numbered points, cut edge-case disclaimers, drop a model or variant the author has already deprioritised.

Do not change the layout format (for example single-column to two-column) to meet a page target unless the author asks. *Why: it changes the paper's reading experience and venue fit, not just its length.* Levers A to D alone can remove a large share of pages with no result, table column, figure or worked example lost.

Converting prose to points (including a caption-cap round) takes more vertical space than the prose did. Budget a layout pass afterwards.

# Workflow: Materials to Artifact to LaTeX

The build is bottom-up and incremental. The author's words: "construct the materials first in a thematic fashion. write up a basic structure. publish a claude artifact with bare minimum skeleton and mapped references. let's build the artifact one element at a time, like a research paper section/subsection filling afterwards. including tables and charts and descriptions and bullet etc."

## 0. Recall

- Read the paper's status memory file first. It names the active artifact URL, the LaTeX folder, authoritative versus superseded numbers, style rules, decisions applied, open items. It is the only source for this paper's numbers and structure; nothing about a sibling paper enters the working set.
- Run `/brain` and Eagle Mem search for prior artifacts, workshop drafts, analysis docs, Google Drive documents, and chat or call notes the author pastes in. Pasted chats and call summaries are source material; extract facts and decisions from them.
- For a new paper, download the two published PDFs (arXiv:2602.03868, arXiv:2603.03294) and read them for structure and voice. Once the author supplies a skeleton, that skeleton overrides the prior-paper conventions.
- Do not take early aggregate metrics seriously. "aggregate metrics are meaningless at this stage. we'll need to build the raw data and corresponding predicted data first."

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

- Organize by paper section or theme, not by source repository. Zero-padded numbered folders; gaps in numbering are fine.
- Copy evidence files (CSVs, result JSONs, plots, extraction scripts). Exclude huge binaries (caches, raw image folders, parquet feature stores) and say so in the README.
- Every folder README row maps to a paper section. Corrections go inline in bold: "**Its headline table (a / b / c / d) is superseded by the <date> audit**".
- `GAP_NOTE.md` for each gap the author suspects: status in the heading ("# Status: Quality Filter (M0) Is NOT Missing"), what the folder holds, a "Headline numbers (measured, not projected)" table. Gaps resolved as not-gaps stay documented.
- Sub-evidence stays reproducible: keep the extraction script next to its output.
- Raw row-level datasets are listed separately from derived aggregates so any aggregate can be re-derived. This list becomes Appendix A.

## 2. Skeleton

- Draft the section list with mapped sources per section, `[TO BE FILLED]` for results not yet run. Use `structure.md`.
- Present the skeleton for approval before drafting. "Only after I approve the planned skeleton structure, go ahead and build." Do not carry forward structure from an older deck or draft; rebuild from the requirement.
- Order sections by dependency: nothing appears before what it depends on (pipeline options before the evaluation candidates they determine). Section weight follows importance, not availability of material (PII awareness is a short late section, not a pillar).
- If the author asks for a budget ("50% data focused, remaining methodology"), record it in the status memory and hold to it.
- Plan subagent hand-offs off the skeleton: which sections are heavy enough for a parallel micro-task.

## 3. Reviewer-Facing Artifact

The HTML artifact is the working draft that the author, teammates, and Codex review. It precedes any PDF.

Build rules:
- One element at a time: a section, a subsection, a table, a chart. Fill a section only when its source exists or the author supplies the content. Sections without data (Results, Discussion, Impact) stay visibly empty with a pending note. "Don't over-commit / don't go too far unprompted."
- Per-section pattern used in both 2026 papers: card with section number and status pill (sourced / outlined / pending), source chips naming the file or document behind the section, then content (tables, module cards, inline SVG figure with caption), then a dashed pending box for anything provisional.
- Status card at the top: draft date, headline scale facts, submission plan when agreed.
- Abstract as labelled blocks (Problem, Key Challenges, Proposed Approach, Evaluation, Main Results) until prose is warranted.
- Appendix A (Materials and Sources) and Appendix B (Raw Datasets / Reconciliation Flags) from the first publish. The author asked for this appendix in both 2026 papers within the first hour.
- Load the `artifact-design` and `artifact-diagramming` skills before writing HTML. Inline hand-authored SVG for flowcharts; theme through CSS tokens for light and dark; no external chart libraries needed.
- No em-dashes in HTML either, neither the entity form nor the U+2014 character. Run `scripts/check_style.sh` on the file before publishing.

File and publish rules:
- The HTML source lives in the project folder (`paper/<name>.html`), not the session scratchpad. One paper's source sat in a scratchpad and needed rescuing.
- Republish by passing the existing URL as `url`. Omitting it forks a new artifact. Superseded artifacts are recorded in the status memory as "do not edit".
- Back up before any restructure: `<name>.html.bak_YYYY-MM-DD`.
- Teammates may edit the artifact collaboratively. Before editing, `read` the live version and diff against the local copy; merge rather than overwrite.
- When restructuring, say what is reorganized versus what is new content. "any of this changes the actual content or does it just reorganize it?" Reorganization must not smuggle in additions.

## 4. arXiv LaTeX Folder

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

- The LaTeX draft is a tightened fold of the artifact (16 sections from 21, 12 from 15). The README carries a Section Map table listing folds, merges, and drops with reasons. Apply the same folds to the artifact only if asked (it renumbers every reference).
- Macros: `\todo{...}` (rust, bracketed, states what will appear, where it comes from, what blocks it), `\pilot` (superscript p on pilot-scale numbers), `\flag{...}` (rust tint on a proposed or problematic value). The SFT paper used `\placeholder{...}` in red. No bare `TBD`.
- Build with tectonic (`brew install tectonic`), Graphviz `dot`, `rsvg-convert`. `./build.sh` must compile clean before any commit.
- Author block: the organisation affiliation, corresponding author email, equal-contribution asterisks, provisional order noted as a dated open item until confirmed.
- One master per format. The SFT paper drifted between `main.tex` and `main_updated.tex`, then `main.tex` and `main_ieee.tex`; the author had to ask "which file did you update?" four times. If two formats must coexist they share `sections/`, and every edit names the files it touched.

## 5. Update Guide Pattern

When results are still landing, write `PAPER_UPDATE_GUIDE.md` in the paper folder: placeholder inventory (file, table label, field, data needed), two update paths (drop CSV with exact expected headers, or inline values), figure swap instructions, compile commands, and a submission checklist. Later the author points at the guide plus the new results file and says "update the paper". The guide is the agreed input format for that.

## 6. Incremental Edits

- Patch, never regenerate. "I need an updated version of the deck that I already had, not a new one." "only change what I'm telling you to, pls don't touch anything else."
- Prefer scripted patches for repeated edits across many section files (`patch_*.py`) so the change is reviewable and re-runnable.
- After every edit batch, report which files changed. Offer the diff when the author asks what moved.
- Roll back a specific change on request without touching the rest (trimming was rolled back alone).
- Strip rather than delete when a reviewer has not weighed in yet.
- Sweep the whole document after any rename or number change. Half-updated documents ("the results section still shows the old numbers for two of the models") are the most common complaint. A changed result is propagated in one pass to every carrier: `00_abstract` Main Results, `01_intro` Contributions, the Results table and its reading paragraph, `NN_conclusion`, `figures/make_charts.py` inputs and the regenerated chart, any `.dot` label or caption that carried the value, the artifact's matching sections, and the status memory's authoritative-numbers list. Run `scripts/check_number_placement.py arxiv_paper/` afterwards; a chart older than its CSV or a value still quoted outside the four homes fails the sweep.
- When the author pastes an independent review from another model or person: judge each comment on merit, adopt what holds, say what does not and why. "Don't deviate too far based on just this review."
- When the author supplies a subsection verbatim, insert it faithfully (bold lead-in bullets are fine), add its citations to the references section, and do not rewrite it.

## 7. Session Close and Hand-off

- Update the status memory: locations, authoritative versus superseded numbers, decisions applied, open items, next step. This file is the only thing that survives a `/clear`.
- Before a long build phase, offer to compact.
- "write it up" or "write this up and let's close" means: persist findings and decisions to the plan and status files, not just the chat.
- When asked to "retain exactly what is needed to restart a fresh session", write the hand-off in the shape of `templates/paper_status_memory.md`: project thesis, active artifact file and URL, superseded artifacts, structure with anchors, style rules, key content already present, source materials, standing instructions, open items, immediate next step.
- Paper project folders are often not git repos. The author's default is commit-and-push after substantive changes; ask once whether to `git init`, record the answer in the status memory.

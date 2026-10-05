# /paper

Use when writing, reviewing, or revising a research paper, arXiv preprint, whitepaper, or the reviewer-facing HTML artifact that precedes one. Also use when new experiment results must be folded into an existing draft, when numbers or citations need verification, or when a paper is being prepared for arXiv. Triggers: "/paper", "write a paper", "paper skeleton", "paper artifact", "review the paper", "critical review", "proof read", "arxiv draft", "update the paper with new results", "reconcile numbers", "verify citations", "submit to arxiv".

## Files

```
skills/paper/
  SKILL.md
  references/figures.md
  references/pitfalls.md
  references/review.md
  references/structure.md
  references/style.md
  references/submission.md
  references/workflow.md
  scripts/allow.txt
  scripts/banned_words.txt
  scripts/check_number_placement.py
  scripts/check_style.sh
  templates/CRITICAL_REVIEW.md
  templates/REVIEW_LOG.md
  templates/materials_README.md
  templates/paper_status_memory.md
```


# Paper Writing and Review

## Overview

A workflow for writing and reviewing empirical applied-ML papers, from scattered evidence to an arXiv submission. Distilled from several papers and their review cycles.

**Core principle:** build from evidence upward in small pieces. Materials first, skeleton second, one section or table at a time, LaTeX last. Every number names its source and denominator. Nothing is invented to look complete.

**Scope:** this skill carries rules, not any one paper's content. No number, model name, denominator, section count, appendix set or route mapping in this skill or its templates belongs to the paper in front of you. Take every one of those from the active paper's own status memory and its own materials. If an example names a subject (a crop, a language, a vendor, a modality), the rule is the part that transfers and the subject is not.

"Author" means the paper's owner who directs the work; "reviewer" means anyone commenting on a draft.

## When to Use

- Starting a paper from scattered material (artifacts, documents, chats, CSVs).
- Adding a section, table, figure or new results to a draft or artifact.
- Any review, proofread, citation check or number reconciliation.
- Preparing or fixing an arXiv or conference submission.

**When not to use:** slide decks, briefs or stakeholder emails (use a deck or artifact skill, if installed; `references/submission.md`, External Standalone Artifacts, covers consistency with the paper). Dataset publishing on its own (only the link section of `references/submission.md` applies).

## Inputs

- Source material: prior artifacts, analysis documents, pasted chats and call notes, CSVs, result JSONs, plots, extraction scripts.
- The paper's status memory (`<paper>-status.md` in the project memory directory), or nothing for a new paper.
- An author-supplied skeleton, venue, format and length target, when they exist.
- An existing draft: the HTML artifact URL and source, and the LaTeX folder.
- Review input: a second model's review file, stakeholder comments, a co-author's edited copy.
- New results to fold in, usually via `PAPER_UPDATE_GUIDE.md`; predictions or data files from collaborators.

## Outputs

- `paper/materials/` organised by theme, with `README.md` and one `GAP_NOTE.md` per suspected gap (`templates/materials_README.md`).
- An approved skeleton with mapped sources.
- The reviewer-facing HTML artifact, published and republished to one URL.
- `arxiv_paper/`: `main.tex`, `sections/`, `figures/` (DOT sources, `make_charts.py`), `references.bib`, `build.sh`, README with a section map; `PAPER_UPDATE_GUIDE.md` while results are landing.
- Review files: `CRITICAL_REVIEW.md` (including the reconciliation register), `REVIEW_LOG.md`, `citation_verification.csv` (`templates/`).
- A differences sheet when reconciling with a co-author's copy.
- The arXiv package and a completed pre-submission checklist.
- An updated status memory and, on request, a hand-off note (`templates/paper_status_memory.md`).

## Workflow

### Session Start

1. Read the paper's status memory. It records which numbers are authoritative, which are superseded, and the open items. If none exists, create one from `templates/paper_status_memory.md`.
2. Confirm the active artifact URL and LaTeX folder from that file. Never publish an artifact without its `url`; that forks a new one.
3. Read `references/style.md`. The banned-word list and no-em-dash rule apply to every line written, including HTML and LaTeX source.

### Phases

| Phase | Output | Detail |
|---|---|---|
| 0 Recall | Status memory, prior artifacts, results from any memory or search tool available | `references/workflow.md` §0 |
| 1 Gather | `paper/materials/NN_topic/` folders + README + GAP_NOTE.md | `references/workflow.md` §1 |
| 2 Skeleton | Section list with mapped sources, `[TO BE FILLED]` slots; confirmed at a checkpoint question | `references/workflow.md` §2, `references/structure.md` |
| 3 Artifact | Reviewer-facing HTML, built one element at a time | `references/workflow.md` §3 |
| 4 LaTeX | `arxiv_paper/` folder, `build.sh`, README with section map | `references/workflow.md` §4 |
| 5 Review | `CRITICAL_REVIEW.md`, convergent loop (2 to 3 passes), `REVIEW_LOG.md`, second-model review | `references/workflow.md` §5, `references/review.md` |
| 6 Submit | arXiv package, checklist, dataset and code links | `references/workflow.md` §6, `references/submission.md` |
| 7 Close | Updated status memory, hand-off note for a fresh session | `references/workflow.md` §7 |

Phases repeat. New results land over weeks; each landing goes through 1, 3, 4 and 5. Checkpoint questions (`references/workflow.md`, Checkpoint Questions) gate phases 1 and 2 and any restructure.

### Session Close

Update the status memory: locations, authoritative versus superseded numbers, decisions applied, open items, next step. If the author asks to clear context and start fresh, write a hand-off note in the shape of `templates/paper_status_memory.md` so the next session restarts without loss.

## Quality Standards

### Non-Negotiables

**Wording**
- No em-dashes anywhere: prose, LaTeX (`---`), HTML (`&mdash;`). `references/style.md`, Punctuation.
- No banned words (house list in `scripts/banned_words.txt`). `references/style.md`, Banned Words.
- No AI-tell sentence shapes in body text; scope statements and the paper-organisation paragraph are exempt. `references/style.md`, Sentence Shapes.
- Bullets, tables, charts and flowcharts over prose; formal Title Case noun-phrase headings; Arabic numbering. `references/style.md`, Headings and Numbering.
- Plain language a ten-year-old can follow, numbers kept; every metric defined before use; short ids spelled out; captions at most 15 to 20 words. `references/style.md`, Prose and Captions.
- The published version reads as finished: no pending wording, draft markers or personal-information review. `references/structure.md`, Reader-Facing Rule.
- No internal names, task ids, or internal table or file names in anything external. `references/style.md`, Naming Consistency.

**Numbers**
- Never fabricate a number, citation, model name, or an example presented as real; every tabulated result has a supporting file or is flagged. `references/review.md`, pass 3.
- Pilot, provisional and LLM-judged numbers are marked as such; Results, Discussion and Impact stay empty until real data exists. `references/structure.md`, Markers.
- Superseded numbers are listed in the status memory and the reconciliation register as "must not be reused". `references/structure.md`, Reconciliation Register.
- Result values live in four homes (Abstract, Introduction, Results, Conclusion) and every carrier is swept together when one changes. `references/style.md`, Where Numbers Live.

**Figures**
- Diagrams are Graphviz DOT or hand-authored inline SVG, never Mermaid (house default). `references/figures.md`, Toolchain.
- Placement is checked in the compiled PDF, not the source. `references/figures.md`, Figure and Table Placement.

**Process**
- Patch, do not regenerate; report which files changed; one master file per format. `references/workflow.md`, Incremental Edits.
- One paper per working set: confirm the project folder before every edit (sibling papers often share section file names) and never carry a finding, label or number across papers.
- Checkpoint questions at materials, skeleton, rough themes and before any restructure, and nowhere else. `references/workflow.md`, Checkpoint Questions.
- Review is a convergent loop: two to three passes, stop on agreement. `references/review.md`, Convergent Review Loop.
- No long silent tool loops: after a couple of failed attempts at a simple edit, report what is blocking and ask.

### Gate Scripts

Run both before every publish or commit. Script paths are relative to the skill directory (`<skill-dir>/scripts/`).

| Command | Exit codes | Options | Does not catch |
|---|---|---|---|
| `bash scripts/check_style.sh <files or dirs>` | 0 clean (warnings may print); 1 any em-dash, banned word or AI-tell phrase; 2 usage error, missing path, or no `.tex`/`.html` matched | `--allow REGEX` (repeatable); per-paper `.paper-style-allow` in the current directory or paper folder; word lists in `scripts/banned_words.txt` and `scripts/allow.txt` | Sentence shapes beyond the warning patterns; banned words used legitimately (needs an allow pattern); `.md` files inside a directory argument |
| `python3 scripts/check_number_placement.py <paper_dir>` | 0 pass; 1 any result value in prose outside the four homes (or any warning with `--strict`) | `--allow REGEX` (extra home sections), `--exempt REGEX` / `--exempt-file FILE` (model names and ids with digits), `--data-dir DIR`, `--strict` | The HTML artifact; derived differences and ranges; values written as words; tables legitimately outside Results (warns, mark `% table-ok:`) |

### Red Flags

Stop and re-read the relevant reference when any of these appear in your own output or plan:

- A banned word or an em-dash pasted in from a source document.
- A number with no file path behind it, or a percentage with no denominator.
- Filling Results with pilot numbers "for now".
- Regenerating a whole `.tex` or `.html` file for a one-paragraph change.
- Publishing an artifact without `url`, or editing a file in a session scratchpad instead of the project folder.
- A citation you cannot open, or a `% TODO: verify` left in the bib.
- A figure or table that lands pages after the section that references it.
- Two master files (for example `main.tex` and `main_updated.tex`) diverging.
- A result value in a Method, Module, Data, Design, Discussion or Limitations section, a caption, or a `.dot` label.
- A caption running past one line, a metric used before it is defined, or a bare `B0` in prose.
- Pending wording, a `\todo`, or a personal-information review in a version about to be published.
- A second copy of the paper being edited elsewhere with no differences sheet, or a page cut that reaches for a layout-format change.
- A result changed in the Results table but not in the Abstract, Introduction, Conclusion, the chart, or a difference or range computed from it.
- A row dropped from a results table while figures measured on that model's own data stay in the paper.

## Reference Guides

| Need | Go to |
|---|---|
| Word bans, sentence shapes, headings, naming, numbers, where numbers live, captions | `references/style.md` |
| Checkpoints, phases, folder layouts, artifact build, LaTeX folder, incremental edits, reconciliation, page reduction, hand-off | `references/workflow.md` |
| Canonical skeleton, Appendix A, reconciliation register, reader-facing rule, markers, id naming | `references/structure.md` |
| Critical-review prompt, review passes, suspicion rules, CRITICAL_REVIEW.md, convergent loop | `references/review.md` |
| Toolchain, palette, figure content, placement, table formatting | `references/figures.md` |
| Format and length decisions, author block, arXiv package, checklist, releases | `references/submission.md` |
| Tempting rationalisations and common failure modes | `references/pitfalls.md` |
| Templates: status memory, materials README, critical review, review log | `templates/` |

## Limitations

- Tuned for empirical applied-ML papers in LaTeX for arXiv (`article` or `IEEEtran`). Theory papers, humanities formats, Word-based submissions and journal-specific templates need adaptation.
- The default skeleton assumes a production-system paper; a benchmark or method paper drops sections.
- Depends on Claude Code tooling: the Artifact tool, AskUserQuestion, subagents, and the `artifact-design`, `artifact-diagramming` and `dataviz` skills. The build needs tectonic, Graphviz `dot`, `rsvg-convert`, perl, python3 and matplotlib.
- Both gates are regex heuristics. `check_style.sh` can flag legitimate uses ("groundwater", "instrumental variable", a literal licence cell) and needs an allow pattern for them. `check_number_placement.py` reads LaTeX only, detects home sections by file name, and treats any chart older than the newest CSV in its data directories as stale.
- Citation checks need web access.
- arXiv facts (the pdflatex engine, the abstract character limit, moderation time) can change; check current guidance.
- House style choices (no em-dashes, the banned list, the rust accent, IBM Plex, Graphviz over Mermaid, arXiv first) are opinionated defaults; record any per-paper override in the status memory.

## Troubleshooting

| Symptom | Fix |
|---|---|
| The style gate prints "clean" but you expected hits | Check the "N file(s) checked" count; a directory expands only to `.tex` and `.html`. |
| The style gate fails on a legitimate file name or proper noun | Add an allow pattern: `--allow REGEX` or a line in the paper's `.paper-style-allow`. |
| The number gate says `homes NONE MATCHED` | Name section files with abstract, intro, results, conclusion, or pass `--allow`. |
| The number gate flags a model name with digits | `--exempt REGEX` or `--exempt-file FILE`. |
| "chart older than its data" | Regenerate with `figures/make_charts.py` or `build.sh`. |
| A sentence vanished from the PDF after adding `% number-ok:` | The marker was mid-line; move it to the end of the line and re-check the rendered sentence. |
| Every citation renders `[?]` and References is missing in the uploaded build | Ship `.bib` with `.bbl` and compile from a clean extract (`references/submission.md`). |
| `Lonely \item` from the `.bbl` | Inline the references as a `thebibliography` block. |
| pdflatex fails on non-Latin characters | Romanise or configure fonts and test the arXiv build (`references/submission.md`). |
| IEEEtran prints Roman section numbers | Override `\@seccntformat` for Arabic numbering. |
| Figures float pages away from their section | `[t]` / `[!t]` with `figure*`, or `\FloatBarrier`; verify in the PDF. |
| The page count grew after converting prose to points | Tighten `\intextsep`, `\textfloatsep` and list spacing. |
| Local and arXiv builds differ | Strip engine-specific directives such as `\special{pdf:...}`. |
| A collaborator's predictions score 100% | The field mapping is scoring gold against gold; reproduce their reported figures first. |
| Your row count is lower than a collaborator's document | Check the download completed before reporting a discrepancy. |

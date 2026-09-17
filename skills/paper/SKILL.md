---
name: paper
description: Use when writing, reviewing, or revising a research paper, arXiv preprint, whitepaper, or the reviewer-facing HTML artifact that precedes one, for a research or product team. Also use when new experiment results must be folded into an existing draft, when numbers or citations need verification, or when a paper is being prepared for arXiv. Triggers: "/paper", "write a paper", "paper skeleton", "paper artifact", "review the paper", "critical review", "proof read", "arxiv draft", "update the paper with new results", "reconcile numbers", "verify citations", "submit to arxiv".
---

# Paper Writing and Review

House workflow for research papers, distilled from four papers (two published on arXiv, 2602.03868 and 2603.03294, and two in draft) and roughly 300 instructions given while writing them. The two published PDFs are the style reference; download and read them when a fresh paper starts.

**Scope:** this skill carries rules, not any one paper's content. Past papers appear only as provenance and as the shape of an example. No number, model name, denominator, section count, appendix set or route mapping in this skill or in its templates belongs to the paper in front of you. Take every one of those from the active paper's own status memory and its own materials. If an example here names a subject (a crop, a language, a vendor, a modality), the rule is the part that transfers and the subject is not.

**Core principle:** build from evidence upward in small pieces. Materials first, skeleton second, one section or table at a time, LaTeX last. Every number names its source and denominator. Nothing is invented to look complete.

## When to Use

- Starting a paper from scattered material (artifacts, docs, chats, CSVs).
- Adding a section, table, figure, or new results to a draft or artifact.
- Any review, proofread, citation check, or number reconciliation.
- Preparing or fixing an arXiv or conference submission.
- Not for: slide decks or stakeholder emails (use CLAUDE.md stakeholder rules), dataset publishing alone (see `references/submission.md` only for the link section).

## Session Start

1. Read the paper's status memory file (`<paper>-status.md` in the project memory dir). It records which numbers are authoritative, which are superseded, and the open items. If none exists, create one from `templates/paper_status_memory.md`.
2. Confirm the active artifact URL and LaTeX folder from that file. Never publish an artifact without its `url`; that forks a new one.
3. Read `references/style.md`. The banned-word list and no-em-dash rule apply to every line written, including HTML and LaTeX source.

## Phase Flow

| Phase | Output | Detail |
|---|---|---|
| 0 Recall | Status memory, prior artifacts, `/brain` hits | `references/workflow.md` §0 |
| 1 Gather | `paper/materials/NN_topic/` folders + README + GAP_NOTE.md | `references/workflow.md` §1 |
| 2 Skeleton | Section list with mapped sources, `[TO BE FILLED]` slots; confirmed at a checkpoint question | `references/structure.md`, `references/review.md` §Checkpoint Questions |
| 3 Artifact | Reviewer-facing HTML, built one element at a time | `references/workflow.md` §3 |
| 4 LaTeX | `arxiv_paper/` folder, `build.sh`, README with section map | `references/workflow.md` §4 |
| 5 Review | `CRITICAL_REVIEW.md`, convergent loop (2 to 3 passes, stop on agreement), `REVIEW_LOG.md`, second-model review | `references/review.md` |
| 6 Submit | arXiv package, checklist, dataset and code links | `references/submission.md` |
| 7 Close | Update status memory, hand-off note for a fresh session | `references/workflow.md` §7 |

Phases repeat. New results land over weeks; each landing goes through 1, 3, 4, 5.

## Non-Negotiables

- No em-dashes anywhere. Not in prose, LaTeX (`---`), or HTML (`&mdash;`).
- Banned words: arm, instrument, license, contract, ground (as filler), leverage, robust, seamless, delve, unlock. Source documents use "arm" constantly; re-check after every paste. Run `scripts/check_style.sh` before every publish or commit.
- Bullets, numbered points, tables, charts, and flowcharts over prose. "Crisp language." Formal noun-phrase headings in Title Case, Arabic numbering (1, 1.1, 1.1.1).
- Language a ten-year-old can follow, with the numbers kept. Every metric defined in one line before first use; short ids spelled out in prose ("Baseline 0", not "B0"); no caption over 15 to 20 words, with the overflow as a note line under the table.
- The version being published reads as finished: no pending language, no draft markers, and no mention of a personal-information review. Whether it carries a Limitations section or only Future Work is a per-paper decision recorded in the status memory.
- Never fabricate a number, a citation, a model name, or an example presented as real. Every tabulated result has a supporting file in `materials/` or `results/`; otherwise it is flagged for manual review.
- Pilot, provisional, and LLM-judged numbers are marked as such (`\pilot`, `\flag`, `.pend`, asterisk) and never presented as final. Results, Discussion, and Impact stay empty until real experiment data exists.
- Superseded numbers are listed in the status memory and Appendix B with "must not be reused".
- Result numbers have four homes: Abstract, Introduction, Results, Conclusion. Every other section describes and points at a table or figure by number without quoting the value. Figures, flowcharts and captions carry structure, not result values, unless the figure is the result (a chart drawn from the data); detail beside a figure goes in a table. When a number changes, the four homes, the tables, the chart sources, the `.dot` labels and the captions are swept together. Gate: `scripts/check_number_placement.py`.
- Patch, do not regenerate. Report which files changed. Keep one master file per format.
- One paper per session's working set. Sibling papers share section filenames (`03_failure.tex` exists in more than one); confirm the project folder before every edit, and never carry a finding, table label or number across papers.
- Checkpoint questions at materials segregation, skeleton, rough themes, and before any restructure, even in bypass mode: one or two simple questions with a recommended option, via AskUserQuestion. Nowhere else.
- Review runs as a convergent loop: at least two passes, at most three, each re-verifying every earlier fix by id; stop only when two successive passes agree. Log in `REVIEW_LOG.md`.
- Diagrams are Graphviz DOT rendered to SVG/PDF, or hand-authored inline SVG in the artifact. Never Mermaid.
- Standalone external artifacts carry no internal names, task ids, or internal table or file names.

## Quick Reference

| Need | Go to |
|---|---|
| Word bans, tone, headings, numbering, naming consistency, where numbers live | `references/style.md` |
| Folder layouts, artifact patterns, LaTeX folder, incremental edits, hand-off | `references/workflow.md` |
| Canonical skeleton, appendices A and B, markers, module naming | `references/structure.md` |
| The critical-review prompt, review passes, CRITICAL_REVIEW.md format, citation audit, checkpoint questions, convergent review loop | `references/review.md` |
| Palette, DOT/SVG, charts, table fitting, figure placement | `references/figures.md` |
| arXiv package, format choice, author block, known compile errors, HF links | `references/submission.md` |
| Collaborative reconciliation, page-reduction levers | `references/workflow.md` §6a, §6b |
| Dated corrections and pushbacks, rationalization table | `references/lessons.md` |

## Red Flags

Stop and re-read the relevant reference when any of these appear in your own output or plan:

- "Arm", "instrument", or an em-dash slipped in from a source document.
- A number with no file path behind it, or a percentage with no denominator.
- Filling Results with pilot numbers "for now".
- Regenerating a whole `.tex` or `.html` file for a one-paragraph change.
- Publishing an artifact without `url`, or editing a file in a session scratchpad instead of the project folder.
- A citation you cannot open, or a `% TODO: verify` left in the bib.
- A figure or table that cannot be located by number, or that lands pages after the section that references it.
- Two master files (for example `main.tex` and `main_updated.tex`) diverging.
- An accuracy, error rate, cost or latency value quoted in a Method, Module, Data, Design, Discussion or Limitations section, in a caption, or in a `.dot` label.
- A caption running past one line, a metric used before it is defined, or a bare `B0` in prose.
- "Not yet measured", "pending", a `\todo`, or a personal-information review named in a version about to be published.
- A second copy of the paper being edited elsewhere with no differences sheet, or a page cut that reaches for two columns.
- A result changed in the Results table but not in the Abstract, Introduction, Conclusion, or the chart that draws it.
- A difference, ratio, range or system count quoted in prose that was computed from a value the latest sweep changed.
- A row dropped from a results table while figures measured on that model's own split stay in the paper.

## Session Close

Update the status memory: locations, authoritative versus superseded numbers, decisions applied, open items, next step. If the user asks to "clear context and start fresh", write a hand-off note in the shape of `templates/paper_status_memory.md` so the next session restarts without loss.

# Submission

## Decisions to Make Early

- Format: single-column `article` for long-form arXiv, `IEEEtran` two-column when a conference target exists. The SFT paper kept both as twins sharing `sections/`. Ask which; do not assume a page limit.
- Length target: 8 pages for conferences, or long and detailed for arXiv. The author changed this both ways. Record the current target in the status memory.
- Venue: arXiv first, always. A first-time arXiv submission can take about a week to clear moderation, so the base draft goes up as soon as it compiles, and revisions follow as new versions. Predatory journals are ruled out (IJAR was checked and rejected).
- Categories: read the paper and propose arXiv categories with reasons (cs.CL, cs.CV, cs.LG, cs.SD, eess.AS as applicable).

## Author Block

- Authors with affiliation the organisation, equal-contribution asterisks where agreed, and emails only where each address will still work after publication. A corresponding author is marked when the author asks for one; a paper may ship without one, and an address being deactivated is never used. The email line wraps; break it after a name when it spills past the margin.
- Author order is provisional until the author confirms; carry it as a dated open item in the title-page comment and in Appendix B. Adding authors after publication is a new arXiv version.
- Prior arXiv ids of the group's published papers are listed in the status memory; cite them where the new paper builds on them.

## arXiv Package

- Files: `main.tex`, `sections/*.tex`, `references.bib` or an inline bibliography, `figures/*.pdf` (and PNG where used), any class or style files not on arXiv. List them explicitly when asked "what do I upload".
- Prefer an inline `thebibliography` block or a clean `main.bbl`. A `.bbl` with `Lonely \item` errors could not be fixed; the working fix was inlining all references into `main.tex`.
- pdflatex on arXiv does not accept Devanagari, Telugu, or Odia characters. Romanize examples or configure fonts and test the exact arXiv build.
- Compile locally with the same engine before uploading; keep only the files the build needs in the upload.
- After upload, sanity-check the arXiv-compiled PDF against the local one: fonts, figures, tables, author block, references, no red placeholders.

## Pre-Submission Checklist

From `PAPER_UPDATE_GUIDE.md` and the review files:

- [ ] No `\placeholder{}`, `\todo{}`, `[TO BE FILLED]`, or `% TODO: verify` left in source or bib.
- [ ] `scripts/check_style.sh` clean on `sections/*.tex` and `main.tex`.
- [ ] All figures present, referenced in order, placed near first reference in the PDF.
- [ ] All cross-references resolve; no BibTeX warnings; no unused bib entries.
- [ ] Every table cell traceable to a file in `materials/` or `results/`.
- [ ] Contributions list links released datasets and code as done, not planned. Hugging Face dataset and toolkit pages carry the arXiv id so they surface under "Code, Data and Media" on the arXiv abstract page.
- [ ] Abstract within both limits: the in-PDF target (about 250 words) and arXiv's metadata field, about 1,920 characters. A plain-language rewrite usually grows the character count even when the word count holds, so measure characters too and keep a shorter metadata version if the two cannot be reconciled.
- [ ] No caption over 15 to 20 words; overflow moved to a note line under the table.
- [ ] No pending language ("not yet measured", "pending", "prepared for release") and no draft markers anywhere in the body.
- [ ] No mention of a personal-information review, anonymisation pass or PII screening.
- [ ] Every short id spelled out in prose ("Baseline 0", not "B0"); best values bold and green, never red.
- [ ] Page count within the target, reached through the lever order in `workflow.md` §6b and never by switching to two columns.
- [ ] Author block and order confirmed; Disclosure paragraph present when commercial systems are benchmarked.
- [ ] No internal names, task ids, internal file paths, or internal table names anywhere, including captions and appendix.
- [ ] Status memory updated with the submitted version and date.

## Releasing Data and Code Alongside

- Dataset releases: strip PII (names in greetings and honorific patterns included), dedupe exact rows and near-duplicate queries, one README with no "v1" or internal table names, per-language breakdowns. Run an independent PII review and act on it before publishing.
- Code releases (a metric toolkit, a scorer, a gate model): package the logic, publish, and cite the URL in the paper so no contribution remains "planned" in a published paper.
- Hugging Face: datasets as dataset repos, toolkits as model or space repos with card tags linking the arXiv id.

## External Standalone Artifacts

Decks or briefs derived from the paper for a CEO or a partner stand alone: no internal names, no references to work outside the artifact's scope, more technical context rather than less, numbers that agree with the paper (10 systems in the paper means 10 on the slide), qualified sentences for deployment readiness, and a closure ledger for the reviewer's comments.

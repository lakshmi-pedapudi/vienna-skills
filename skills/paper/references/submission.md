# Submission

Applies to: format and length decisions, the author block, the arXiv package, the pre-submission checklist, data and code releases, and standalone material derived from the paper.

## Decisions to Make Early

- Format: single-column `article` for long-form arXiv, `IEEEtran` two-column when a conference target exists. Both can coexist as twins sharing `sections/`. Ask which; do not assume a page limit.
- Length target: a conference page limit, or long and detailed for arXiv. Targets can change in either direction during a paper; record the current one in the status memory and ask before trimming or expanding.
- Venue: arXiv first (house default). A first-time arXiv submission can take some days to clear moderation (check current guidance), so the base draft goes up as soon as it compiles, and revisions follow as new versions. Check the legitimacy of any journal; predatory journals are ruled out.
- Categories: read the paper and propose arXiv categories with reasons (cs.CL, cs.CV, cs.LG, cs.SD, eess.AS as applicable).

## Author Block

- Authors with their affiliation, equal-contribution asterisks where agreed, and emails only where each address will still work after publication. A corresponding author is marked when the author asks for one; a paper may ship without one, and an address being deactivated is never used. The email line wraps; break it after a name when it spills past the margin.
- Experiment ownership and draft ownership are separate. Confirm who ran which experiments before the author block or any contributions line ships. *Why: a wrong attribution is easy to make and awkward to correct after publication.*
- Author order is provisional until the author confirms; carry it as a dated open item in the title-page comment and in the reconciliation register. Adding authors after publication is a new arXiv version.
- Verify the team's prior arXiv ids against the PDFs, not memory, before citing them. *Why: two ids are easily swapped in a bib.*

## arXiv Package

- Files: `main.tex`, `sections/*.tex`, `references.bib` and the generated `.bbl` (or an inline bibliography), `figures/*.pdf` (and PNG where used), any class or style files not on arXiv. Derive the list from the source and state it explicitly when asked what to upload.
- Compile the package from a clean extract of the tarball, never from the project folder. Ship the `.bib` alongside the `.bbl`. *Why: the project folder hides missing files; a package missing its bibliography can still report a successful build while rendering every citation as `[?]` and dropping the References section.*
- A `.bbl` that raises `Lonely \item` errors: inline all references into `main.tex` as a `thebibliography` block.
- Strip engine-specific directives (for example `\special{pdf:minorversion ...}`, which pdflatex ignores) before submission. *Why: deleting them leaves nothing that behaves differently between local and arXiv builds.*
- Non-Latin script: pdflatex on arXiv does not accept characters such as Devanagari or other Indic scripts. Romanise examples, or configure fonts in the build and test the exact arXiv compile before relying on it. This also applies to treemaps and other rendered examples.
- Compile locally with the same engine arXiv uses before uploading; keep only the files the build needs in the upload.
- After upload, sanity-check the arXiv-compiled PDF against the local one: fonts, figures, tables, author block, references, no red placeholders.

## Pre-Submission Checklist

From `PAPER_UPDATE_GUIDE.md` and the review files:

- [ ] No `\placeholder{}`, `\todo{}`, `\flag{}`, `[TO BE FILLED]`, or `% TODO: verify` left in source or bib.
- [ ] `scripts/check_style.sh sections/ main.tex` clean; `scripts/check_number_placement.py arxiv_paper/` passes.
- [ ] All figures present, referenced in order, placed near first reference in the PDF.
- [ ] All cross-references resolve; no BibTeX warnings; no unused bib entries.
- [ ] Every table cell traceable to a file in `materials/` or `results/`.
- [ ] Contributions list links released datasets and code as done, not planned. Hugging Face dataset and toolkit pages carry the arXiv id so they surface under "Code, Data and Media" on the arXiv abstract page.
- [ ] Abstract within both limits: the in-PDF target (about 250 words) and arXiv's metadata field (about 1,920 characters at the time of writing; check current limits). A plain-language rewrite usually grows the character count even when the word count holds, so measure characters too and keep a shorter metadata version if the two cannot be reconciled.
- [ ] No caption over 15 to 20 words; overflow moved to a note line under the table.
- [ ] Nothing from the Reader-Facing Rule in `structure.md`: no pending language, no draft markers, no mention of a personal-information review.
- [ ] Every short id spelled out in prose ("Baseline 0", not "B0"); best values bold and green, never red.
- [ ] Page count within the target, reached through the lever order in `workflow.md`, Page Reduction.
- [ ] Author block, ownership and order confirmed; Disclosure paragraph present when commercial systems are benchmarked.
- [ ] No internal names, task ids, internal file paths or internal table names anywhere, including captions and appendix.
- [ ] Package compiled from a clean extract.
- [ ] Status memory updated with the submitted version and date.

## Releasing Data and Code Alongside

- Dataset releases: strip PII (names in greetings and honorific patterns included), dedupe exact rows and near-duplicate queries, one README with no "v1" or internal table names, per-language breakdowns. Run an independent PII review and act on it before publishing. The paper itself does not mention this review.
- Code releases (a metric toolkit, a scorer, a gate model): package the logic, publish, and cite the URL in the paper so no contribution remains "planned" in a published paper.
- Hugging Face: datasets as dataset repos, toolkits as model or space repos with card tags linking the arXiv id.

## External Standalone Artifacts

Decks or briefs derived from the paper for leadership, a partner or customers stand alone: no internal names, no references to work outside the artifact's scope, more technical context rather than less, numbers that agree with the paper (the same count of systems in both), qualified sentences for deployment readiness, and a closure ledger for the reviewer's comments. Build them with a deck or artifact skill, if installed.

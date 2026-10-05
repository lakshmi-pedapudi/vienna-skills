# Pitfalls

Applies to: self-checks while drafting, editing or reviewing. Each row is a tempting thought and the reason it fails; the rules themselves live in the files named under Common Failure Modes.

## Rationalisation Table

| Thought | Reality |
|---|---|
| "The source document uses this term, so it is the domain term." | Banned words stay banned. Write route, model or configuration. |
| "One em-dash reads better here." | Zero em-dashes. Rewrite the sentence. |
| "Pilot numbers make Results look complete for now." | Results stay empty or carry `\pilot` and a pending box. An unsourced number will be questioned. |
| "The number is in the summary document." | Summary documents get superseded. Trace to the row-level file or flag it. |
| "Regenerating the file is faster than patching." | Patch and report which files changed. |
| "The citation is well known; no need to open it." | Citations recalled from memory are sometimes fabricated. Open it. |
| "Publishing without `url` is quicker." | It forks a new artifact and loses the review trail. |
| "The scratchpad is fine for the source file." | Scratch space is not durable. Project folder only. |
| "I can restructure while I am in there." | Say what is reorganised versus new; get the structure approved first. |
| "The accuracy belongs where the model is described." | Describe the module and cite the Results table by number. |
| "The exact count is more rigorous than the rounded one." | In prose it is noise. Round it; the source table carries the digits. |
| "The measured total is the honest latency number." | Next to a vendor's name a total becomes a claim about that vendor. Split it by stage first. |
| "The caption needs one more clause to be precise." | Twenty words, then a note line under the table. |
| "Stating what is not yet measured is honest." | In the published version it reads as unfinished. Make it a Future Work line. |
| "The baseline just scores badly on this column." | Check its label vocabulary against the reference first; a duplicated class can outweigh any model difference. |
| "Normalising more makes the comparison fairer." | Merging duplicate names is a fix. Crediting a coarser answer is leniency, and it picks a winner. |
| "The predictions file's label field is the prediction." | It may be the gold label. Reproduce the sender's own numbers before scoring. |
| "Their row count disagrees with my file, so their document is wrong." | Check your download finished. |
| "Showing open conflicts in the paper is the honest thing." | Conflicts go to the reconciliation register; the paper states each gap once in reader-facing words. |
| "Every gate passed, so the PDF is right." | Gates miss derived numbers and sentences dropped by a mid-line `%`. Read the rendered page. |

## Common Failure Modes

- Half-updated documents after a number change, including derived differences and ranges: `style.md`, Where Numbers Live; `workflow.md`, Incremental Edits.
- A fix applied to one copy of a claim and not its twin: `review.md`, Review Passes (pass 4).
- Scoring and label-vocabulary errors in comparisons, and data from collaborators: `review.md`, Suspicion Rules.
- Internal bookkeeping or pending wording reaching the published PDF: `structure.md`, Reader-Facing Rule.
- Packages that build locally but not on arXiv: `submission.md`, arXiv Package.
- Floats landing pages away from their section: `figures.md`, Figure and Table Placement.
- Two master files drifting apart: `workflow.md`, LaTeX Folder.

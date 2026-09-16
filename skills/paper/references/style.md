# Style Rules

Applies to prose, LaTeX source, HTML artifacts, captions, table notes, READMEs inside the paper folder, and review documents. The two published papers (arXiv:2602.03868, arXiv:2603.03294) are the writing-voice reference. Every example below illustrates a shape; none supplies a number or a subject for the current paper.

## Prose

- Crisp. Bulleted or numbered points over paragraphs. One idea per sentence. The author's words: "I'm sick of looking at ai generated verbose text for no reason."
- Formal academic register, third person, grounded tone. No hyperbole, no marketing language carried over from internal decks or articles.
- Plain words over coined labels. Do not invent terms like "specificity collapse" or "hallucination space"; describe the thing.
- No hedging clauses stacked after a claim ("claim-then-hedge" is a flagged AI pattern). State the claim with its evidence and its scope, once.
- No filler: genuinely, actually, just, basically, comprehensive (when used as praise), paramount, "underscoring the need for", "sweet spot", "it's worth noting".
- No sensational numbers in the abstract or conclusion. Highlight contributions; let tables carry the magnitudes.
- Explain a concept in one plain sentence before its technical name if the name is not standard in the field.
- Define every metric in one or two lines before its first use, standard ones included. A derived variant is defined next to the metric it derives from (the word error rate before the agriculture-weighted version, F1 before the first F1 table). "before jumping into [the derived metric], just add 1-2 lines establishing the definition of WER."
- Readability target: "Make it sound like you are explaining to a 10 year old, but with numbers and points." Short sentences, one idea each, every term of art glossed on first use, every number and denominator kept.
- Cut sentences written to pre-empt an objection a naive reader will not raise ("systems with partial language coverage are omitted"). State the scope once, where the basis is named.

## Punctuation and Characters

- No em-dashes. Use commas, colons, parentheses, or a new sentence. In LaTeX also ban `---`; in HTML also ban `&mdash;` and the U+2014 character. Spaced hyphens are acceptable in chat, not in the paper.
- Native-script examples (Devanagari, Telugu, Odia) break pdflatex on arXiv. Romanize, or set up a font in the build and test the arXiv compile before relying on it.

## Banned Words

| Banned | Why | Use instead |
|---|---|---|
| arm(s) | Source docs use it for experiment branches; reads as jargon | route, branch, configuration, variant, model |
| instrument | filler for "tool" or "measure" | tool, metric, measure, script |
| license (as metaphor) | filler | permission, allowance; literal software-license cells are fine |
| contract | filler for "interface" or "agreement" | interface, schema, agreement |
| ground (as filler) | "ground truth" reads as loose | reference label, verified reference, panel label, reference transcript |
| leverage (verb) | AI tell | use |
| robust, seamless, delve, unlock | AI tells | specific claim, or cut |

Allowed exceptions: literal file or folder names (`arm_scores_crop.csv`, `grounding/`), and words inside a cited paper title in `references.bib`. Confine those to Appendix A and the bib.

Check command (run on `sections/`, `main.tex`, and the artifact HTML):

```bash
bash ~/.claude/skills/paper/scripts/check_style.sh sections/*.tex main.tex paper/*.html
```

## Headings and Numbering

- Headings are formal noun phrases in Title Case. Good: "Production Failure Analysis", "Limitations and Future Work". Bad: "Why it breaks", "What we found".
- Subsection titles reuse the exact names the paper's own category or taxonomy table already defines. Do not invent or rephrase a parallel vocabulary for the same set: "titles of all sub-sections to be simplified to recognizable names from Table 13. Don't invent or rephrase new names."
- Arabic numbering at every level: 1, 1.1, 1.1.1. Never Roman numerals for sections, never A/B for subsections. In IEEEtran this needs a manual `\@seccntformat` override.
- Distinct typography per heading level (bold subsection, italic subsubsection). Identical fonts across levels was flagged twice.
- Section order and content follow `structure.md`. When a skeleton is supplied by the author, its numbering is the sole authority; do not revert to prior-paper conventions.

## Naming Consistency

- One nomenclature per concept, used everywhere: a qualifier keeps its exact form and punctuation on every mention, a model keeps its official name ("GPT-4o", never "ChatGPT-4o"), a vendor keeps one spelling once naming is cleared, a component keeps one label. Record the set in the status memory and sweep the whole document after any rename.
- Short ids are defined in a table and then spelled out in prose and in table stubs: "Baseline 0", not "B0". Keep the id form only where a column is too narrow for the words, and only for ids the reader meets often (M0..M4, S1..S4, Route A/B).
- Route, module, stage, and experiment labels (Route A/B, M0..M4, S1..S4, E1..E4, B0..B3, P1..P6, RQ1..RQn) are defined once in a table and never re-defined with a different meaning. A flipped convention (Route A meant CV in one draft and VLM in the next) must be applied consistently and recorded in the status memory.
- Combine confusing paired columns into one intuitive label (for example "Stage" + "Training Samples" became a single named stage) and use that label in the body.
- No internal artifacts in the text: no `results/*substitutions*.csv`, no internal table names (`chat_messagemetric`), no "prior evaluations" that refer to internal metrics, no Linear ids, no "v1" of a dataset that readers never saw.
- Do not use internal misnomers that mean something else outside (the team's "rlhf pipeline" is written as human data curation and expert review).

## Numbers

- Every number names its denominator and its source file. Shape: "<value> on the <N> rows every model was shown (`<file>.csv`)". The value, the basis and the file come from the paper's own status memory; an example number in this skill is never carried into a draft.
- Percentages over raw counts where both are possible; drop Median and N columns unless they carry the argument.
- Same sample set across models in any comparison table; say so in the caption.
- A cross-pipeline delta is never written as a same-model improvement. Name both baselines exactly.
- Distinguish measured results from field observations: "we see this in production" versus "on the benchmark".
- LLM-judged values are labelled LLM-judged until human annotation confirms them.
- Cost figures carry a date and must postdate the models they price.
- Rounding is consistent across tables (a value shown as 0.2125 in one table and 0.21 in another is a flag).
- Error rates and accuracies are written as percentages with one decimal (31.2%), not ratios (0.312), and every comparison between them is made in percentage space. Asked for on the first paper that reported word-level error rates, and it holds for every paper since, whatever the metric family.
- Approximate values observed on a sample carry a tilde (~27%) rather than false precision.
- The version being published reads as finished: "Don't mention anything as pending. this paper is the final publish-worthy version." A measurement still to come is a Future Work line in the future tense, not a gap annotated in the body. Draft-stage markers (`\todo`, `\pilot`, `\flag`, `[TO BE FILLED]`, `.pend`) live in the artifact and the internal build only.
- Never mention a personal-information review, anonymisation pass or PII screening in the paper. It is handled in the released repository, and naming it invites a question the paper does not answer: "DONT EVEN MENTION PII IN THE PAPER."

## Where Numbers Live

Author ruling, 2026-09-14: "ensure experiment results details and numbers are quoted explicitly in Abstract, Introduction, Experiment Results, Conclusion. Don't quote specific numbers and results in other random places."

- Experiment results (accuracy, error rates, F1, cost, latency, deltas, comparisons between models or routes) are quoted in four homes only: Abstract (Main Results block), Introduction (Contributions), Results, Conclusion. The same value, same rounding, same basis in all four.
- Every other section describes without quoting: Existing System, Failure Analysis, Design, Modules, Routes, Data Curation, Methodology, Discussion, Impact, Limitations. They point at the carrier: "Table 3 reports per-stage accuracy", "the coverage curve in Figure 2 sets the scope". Discussion interprets the Results tables by number and does not restate the values.
- Dataset and production descriptive numbers (corpus size, splits, class counts, funnel volumes) are stated once, as a table in the Data or Methodology section, and referenced by table number elsewhere. Prose in those sections names the table, not the count.
- Method parameters (a threshold, a sample size for a study design) are stated once where the method is defined and never repeated as findings. Mark that one source line `% number-ok: <reason>` so the gate skips it; the reason stays visible in the `.tex`.
- Figures, flowcharts and diagrams carry structure, not result values. A pipeline figure shows stages and decisions; it does not print accuracies on its boxes. A chart drawn from the result data is itself a result and carries its own values with direct labels; nothing else does. If a figure needs numbers beside it, they go in a table next to it, not in the figure or its caption.
- Captions name what the figure shows and its basis (one denominator), not the finding's value. Shape: "Coverage of submitted items by the top-N classes, on the items sent for diagnosis", not "89.2% of items are covered by the top 20 classes". The subject is whatever the current paper measures.
- When a result changes: update the four homes, the Results table, the chart source data and regenerate the chart, the `.dot` labels if any carry the value, and the captions. One sweep, one commit, and the status memory records the new authoritative value. `scripts/check_number_placement.py` flags result-type numerals outside the four homes, in captions and in `.dot` sources, and charts older than the CSV they draw from.

## Captions

- Fifteen to twenty words, and fewer is better: "none of the tables or figures should have a description of more than 15-20 words. lesser the better."
- A caption names what the object shows and its one denominator. Everything else (a second denominator, a scoring definition, a circularity warning, an exclusion) goes in a short note line under the table or in the section prose, not into a longer caption.
- A caption that has grown past one line is a sign the table needs a note line, not that the rule needs an exception.

## Tables

- Bold the best value per column and state the convention in a table note. Bold that is not the column maximum was flagged as an error.
- Colour the best value green where the document uses colour, and keep it bold. Never red for a good value: "instead of representing the best number in each row with red font, make it green and bold."
- A Yes/No column becomes a green tick and a red cross, with the words kept in the header (`pifont` or `amssymb` in the preamble). Ticks read faster than repeated words down a column.
- When the table's subject is the metric set, Metric is the first column and holds nothing else; the rest is one plain description column. Drop grouping and score-range columns: "Make Metric the primary column. Don't mention anything else in that column... Remove 'Group' and 'scores' columns."
- A two-column id-to-name table sits immediately before the results table it explains, so the reader is not paging back for what S2 or M1 means.
- Confidence intervals come out unless the argument is about uncertainty. Two narrower side-by-side tables beat one wide one.
- Fit within the column; tighten spacing or span two columns before shrinking fonts below legibility.
- A confusing figure loses to a simple table. When a chart has "weird orientations and markers", replace it with the table.
- Multi-denominator tables show each denominator as its own column with a header that names it.

## Length

Future Work items are one line each, at most 20 words, and only the points that still matter. One paper kept three plus a language-expansion point and cut the rest.

Length targets flipped both ways across papers (8-page conference cut, then "I don't mind if the paper is long and detailed"). Ask which target applies before trimming or expanding. Trimming is a plan with per-item page savings, approved before execution, and rolled back item by item if the author changes course.

## Code and Prompts

- No code in the main body; link the repository.
- Prompts: in a short paper, link GitHub and show one input and output example. In a long-form arXiv version, prompts may sit in the appendix in boxes with an explanation and positive and negative examples. Examples marked as illustrative when they are constructed.

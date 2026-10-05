# Style

Applies to: prose, LaTeX source, HTML artifacts, captions, table notes, READMEs inside the paper folder, and review documents.

Every example below illustrates a shape; none supplies a number or a subject for the current paper. The no-em-dash rule and the banned-word list are house defaults; a paper may override them in its status memory. If the team keeps reference papers for voice, they are listed in the status memory.

## Prose

- Crisp. Bulleted or numbered points over paragraphs. One idea per sentence. *Why: verbose, machine-sounding text is the first thing a reader notices and holds against the paper.*
- Formal academic register, third person, grounded tone. No hyperbole, no marketing language carried over from internal decks or articles.
- Plain words over coined labels. Do not invent a term such as "<adjective> collapse" for an effect; describe the thing.
- No hedging clauses stacked after a claim ("claim-then-hedge" is a flagged AI pattern). State the claim with its evidence and its scope, once.
- No filler: genuinely, actually, just, basically, comprehensive (when used as praise), paramount, "underscoring the need for", "sweet spot", "it's worth noting".
- No sensational numbers in the Abstract or Conclusion. Highlight contributions; let tables carry the magnitudes.
- Frequency and strength words match the data. *Why: "often" claims a majority.* Example: "the model often misreads units" → "the model sometimes misreads units" when it is a minority of cases.
- Describe baselines and vendors fairly: their errors are the normal behaviour of that class of system, not a defeat. *Why: an unfair baseline undermines the comparison and invites a rebuttal.*
- Explain a concept in one plain sentence before its technical name if the name is not standard in the field.
- Define every metric in one or two lines before its first use, standard ones included. A derived variant is defined next to the metric it derives from (the base error rate before any domain-weighted variant, F1 before the first F1 table).
- Readability target: a ten-year-old could follow it, with every number kept. Short sentences, one idea each, every term of art glossed on first use, every number, denominator and caveat kept. A term that is also a column name stays, and the caption defines it.
- A basis or scope paragraph gets two sentences and at most one cross-reference; the detail goes in each table's own note line. *Why: many section pointers in one place lose the reader.*
- Cut sentences written to pre-empt an objection a naive reader will not raise ("systems with partial coverage are omitted"). State the scope once, where the basis is named.

## Sentence Shapes

Rhetorical shapes that read as AI-generated, whatever the wording. The rule targets the shape: rewording a pivot so it sounds less templated does not pass it; restructure the sentence.

- No "not A, but B" pivots: "this is not about X, it is about Y", "we do not X, we Y", "not only X but also Y". State the affirmative claim first. If the contrast carries information, frame it as a finding ("the bottleneck turned out to be Y"), not a rebuttal. A scope statement (what the method does not replace or cover) states a limit rather than setting up a pivot, and stays. `check_style.sh` warns on pivot shapes; it does not fail on them.
- List length matches the content. Two items are a complete list; a third added for rhythm is padding. Keep lists concise.
- One concrete detail over stacked adjectives: "scales to 10,000 concurrent requests", not "a powerful, flexible, scalable pipeline". Applies most in the Abstract and contribution bullets.
- No importance preambles or intensifiers: "it is crucial to understand", "truly", "arguably one of the most important". State the claim with its evidence.
- No tagline sentences. Read the Abstract's last line and the Conclusion's last line aloud; a line that performs ("The receipts do not lie.") rather than explains is rewritten as a claim with its context or cut.
- Body sections (Results subsections, Discussion, Method) end on their most specific implication, not on an "In summary" restatement. The Abstract and Conclusion summarise by design and are exempt.
- No generic hinge phrases ("that being said", "at the end of the day") and no narrated structure ("now we turn to", "in this section, we"). Headings already signpost. Exception: the Introduction's one "rest of this paper is organized as follows" paragraph, which some venues expect.
- Tables, figures and sections show, list, give or describe; they never know, believe, understand or think. Example: "what is known about each stage" → "Table N describes each stage".

## Punctuation and Characters

- No em-dashes (house default). Use commas, colons, parentheses, or a new sentence. In LaTeX also ban `---`; in HTML also ban `&mdash;` and the U+2014 character. Spaced hyphens are acceptable in chat, not in the paper.
- Non-Latin script in examples: see `submission.md`, arXiv Package.

## Banned Words

House default list. The gate reads it from `<skill-dir>/scripts/banned_words.txt` (one regex per line); edit that file to change the list.

| Banned | Why | Use instead |
|---|---|---|
| arm(s) | Source docs use it for experiment branches; reads as jargon | route, branch, configuration, variant, model |
| instrument | filler for "tool" or "measure" | tool, metric, measure, script |
| license (as metaphor) | filler | permission, allowance; literal software-licence cells are fine |
| contract | filler for "interface" or "agreement" | interface, schema, agreement |
| ground (as filler) | "ground truth" reads as loose | reference label, verified reference, panel label, reference transcript |
| leverage (verb) | AI tell | use |
| robust, seamless, delve, unlock | AI tells | specific claim, or cut |

Allowed exceptions: literal file or folder names (`<banned-stem>_scores.csv`, `<banned-stem>/`), proper nouns, a literal licence cell, and words inside a cited paper title in `references.bib`. Confine file names to Appendix A and the bib. Clear each one with an allow pattern rather than by editing the banned list: `--allow REGEX` on the command line, or one regex per line in a `.paper-style-allow` file in the paper folder.

Check command (run on `sections/`, `main.tex`, and the artifact HTML; a directory expands to the `.tex` and `.html` files inside it):

```bash
bash <skill-dir>/scripts/check_style.sh sections/ main.tex paper/*.html
```

Banned words, em-dashes and AI-tell phrases fail the gate (exit 1). Sentence shapes and "comprehensive" print warnings to judge by eye.

## Headings and Numbering

- Headings are formal noun phrases in Title Case. Good: "Production Failure Analysis", "Limitations and Future Work", "Current Pipeline". Bad: "Why it breaks", "What we found", "What happens to an input today".
- A heading may carry the finding as a noun phrase ("Model Comparison: Different Models, Different Strengths"), never as a sentence, a slogan, or an "X not Y" pair ("Evidence Not Verdict"). *Why: sentence and slogan headings read as marketing.*
- Subsection titles reuse the exact names the paper's own category or taxonomy table already defines. Do not invent or rephrase a parallel vocabulary for the same set. *Why: two names for one category make the reader map them.*
- Arabic numbering at every level: 1, 1.1, 1.1.1. Never Roman numerals for sections, never A/B for subsections. In IEEEtran this needs a manual `\@seccntformat` override.
- Distinct typography per heading level (bold subsection, italic subsubsection). Identical fonts across levels hide the hierarchy.
- Section order and content follow `structure.md`. When the author supplies a skeleton, its numbering is the sole authority; do not revert to prior-paper conventions.

## Naming Consistency

- One nomenclature per concept, used everywhere: a qualifier keeps its exact form and punctuation on every mention, a model keeps its official name ("GPT-4o", never "ChatGPT-4o"), a vendor keeps one spelling once naming is cleared, a component keeps one label. Record the set in the status memory and sweep the whole document after any rename.
- Short ids are defined in a table and then spelled out in prose and in table stubs: "Baseline 0", not "B0". Keep the id form only where a column is too narrow for the words, and only for ids the reader meets often (M0..M4, S1..S4, Route A/B). *Why: two extra words save the reader a lookup.*
- Route, module, stage and experiment labels (Route A/B, M0..Mn, S1..Sn, E1..En, B0..Bn, P1..Pn, RQ1..RQn) are defined once in a table and never re-defined with a different meaning. When a label's meaning flips between drafts, apply the new convention everywhere and record it in the status memory.
- Use the label in the author's latest skeleton; never rename a label on your own initiative.
- Combine confusing paired columns into one intuitive label (for example "Stage" + "Training Samples" become a single named stage) and use that label in the body.
- No internal artefacts in the text: no `results/<internal>.csv`, no internal database table names, no "prior evaluations" that refer to internal metrics, no tracker ticket ids, no "v1" of a dataset that readers never saw.
- Do not use an internal nickname that names a different, established technique outside the team; describe what the process actually does.

## Numbers

- Every number names its denominator and its source file. Shape: "<value> on the <N> rows every model was shown (`<file>.csv`)". The value, the basis and the file come from the paper's own status memory; an example number in this skill is never carried into a draft.
- Percentages over raw counts where both are possible; drop Median and N columns unless they carry the argument.
- Same sample set across models in any comparison table; say so in the caption.
- For a system expected to always answer, a refusal counts as an error. State whether accuracy is on answered cases or on all cases, and report the declined share. *Why: answered-only accuracy rewards declining.*
- A cross-pipeline delta is never written as a same-model improvement. Name both baselines exactly ("best non-diarised baseline versus best diarised result").
- Distinguish measured results from field observations: "we see this in production" versus "on the benchmark".
- Before comparing a measured end-to-end total with a named system, split it by stage from the traces. *Why: next to a vendor's name a total reads as a claim about that vendor, and the slow stage may be your own.*
- LLM-judged values are labelled LLM-judged until human annotation confirms them.
- Cost figures carry a date and must postdate the models they price.
- Rounding is consistent across tables (a value shown as 0.2125 in one table and 0.21 in another is a flag).
- Error rates and accuracies are written as percentages with one decimal (31.2%), not ratios (0.312), and every comparison between them is made in percentage space.
- Approximate values observed on a sample carry a tilde (~27%) rather than false precision.
- Round a corpus total in prose and in any header chip ("~1.2 M items"); the exact figure lives in the one table that sources it. Drop an absolute count whose denominator invites the wrong reading. *Why: exact digits in prose are noise.*
- Wording a published version must not carry (pending language, a personal-information review): see `structure.md`, Reader-Facing Rule.

## Where Numbers Live

This is the single home of the four-homes rule; other files point here.

- Experiment results (accuracy, error rates, F1, cost, latency, deltas, comparisons between models or routes) are quoted in four homes only: Abstract (Main Results block), Introduction (Contributions), Results, Conclusion. The same value, same rounding, same basis in all four. *Why: values quoted in many places drift apart after the next data refresh.*
- Every other section describes without quoting: Existing System, Failure Analysis, Design, Modules, Routes, Data Curation, Methodology, Discussion, Impact, Limitations. They point at the carrier: "Table 3 reports per-stage accuracy", "the coverage curve in Figure 2 sets the scope". Discussion interprets the Results tables by number and does not restate the values.
- A results table belongs in the Results section, not only its values. A Module, Route, Method or Data section holding a results table has misplaced it even when its own prose is clean: the reader meets scores before the experiment is defined, and the module section stops being about the pipeline. Move the table, its chart and its reading bullets together, and leave behind the design description plus a pointer to the Results subsection. Tables that are not results (production measurements of the system being replaced, label vocabulary, dataset splits, configurations, metric definitions) stay where they belong; mark each `% table-ok: <reason>` so the gate stops asking.
- Dataset and production descriptive numbers (corpus size, splits, class counts, funnel volumes) are stated once, as a table in the Data or Methodology section, and referenced by table number elsewhere. Prose in those sections names the table, not the count.
- Descriptive attributes of a component (model size, parameter count, per-call price) are stated once, where the module is built; elsewhere name the model plainly. *Why: repeating them reads as selling.*
- Method parameters (a threshold, a sample size for a study design) are stated once where the method is defined and never repeated as findings. Mark that one source line `% number-ok: <reason>` so the gate skips it. The marker goes at the very end of the line: LaTeX drops everything after `%`, so a mid-line marker deletes the rest of the sentence from the PDF. After adding any LaTeX comment, check the rendered sentence.
- Figures, flowcharts and diagrams carry structure, not result values. A pipeline figure shows stages and decisions; it does not print accuracies on its boxes. A chart drawn from the result data is itself a result and carries its own values with direct labels; nothing else does. If a figure needs numbers beside it, they go in a table next to it, not in the figure or its caption.
- Captions name what the figure shows and its basis (one denominator), not the finding's value. Shape: "Coverage of submitted items by the top-N classes, on the items sent for diagnosis", not "X% of items are covered by the top N classes".
- When a result changes: update the four homes, the Results table, the chart source data and regenerate the chart, the `.dot` labels if any carry the value, and the captions. One sweep, one commit, and the status memory records the new authoritative value.
- Sweep derived quantities too: differences ("8 points better"), ratios, ranges ("15% to 56%"), counts of systems and "N of M" statements. Recompute each from the new table rather than reading it forward. *Why: a stale difference appears nowhere else in the paper, so no gate catches it.*
- Gate: `scripts/check_number_placement.py` flags result-type numerals outside the four homes, whole tables carrying values outside them, values in captions and in `.dot` sources, and charts older than the CSV they draw from.

## Captions

- Fifteen to twenty words, and fewer is better. *Why: a caption is read out of context, so unreadable language is noticed there first.*
- A caption names what the object shows and its one denominator. Everything else (a second denominator, a scoring definition, a circularity warning, an exclusion) goes in a short note line under the table or in the section prose, not into a longer caption. A note line is not a caption, so moving text there also clears the gate's caption warnings while keeping the denominator visible.
- A caption that has grown past one line is a sign the table needs a note line, not that the rule needs an exception.
- Table formatting rules (bold and colour for best values, ticks, column shapes): see `figures.md`, Tables.

## Length

- Future Work items are one line each, at most 20 words, and only the points that still matter.
- The length target is a per-paper decision (`submission.md`, Decisions to Make Early). Trimming follows the plan in `workflow.md`, Page Reduction.

## Code and Prompts

- No code in the main body; link the repository.
- Prompts: in a short paper, link the repository and show one input and output example. In a long-form arXiv version, prompts may sit in the appendix in boxes with an explanation and positive and negative examples. Examples are marked as illustrative when they are constructed.

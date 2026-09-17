# Lessons: Corrections and Pushbacks

Dated, verbatim where possible. These are the moments the author stopped the work. Read them as tests the next draft must pass. Each quote belongs to the paper it was said about: the correction generalises, the subject, the model name and the number do not.

## Prose and Headings

- 2026-02-03, 2026-01-30 and eight more times: "Proof read the entire paper. Be a very critical reviewer... Patterns like em-dashes or weird vocabulary that a normal person might not use, should all be identified and fixed... Be ruthless."
- 2026-09-08: "DO NOT USE terms like 'instrument', 'arm', 'license', 'ground' etc to describe basic technical concepts. I'm sick of looking at ai generated verbose text for no reason."
- 2026-08-15: "don't use weird hyper jargon language like 'arms' for 'models'. keep the language as colloquial as possible."
- 2026-08-15: "words like 'axes' or 'verdict', and don't use that style where you use 'not' in the heading phrases like 'verified not committed', or 'evidence not verdict'."
- 2026-08-11: "'What happens to a photograph today' -> I don't like this kind of phrasing. I'd rather prefer simpler dry titles like 'Current Pipeline'."
- 2026-08-17: "Model Comparison: Crop and Disease Accuracy -> Say instead - Model Comparison: Different Models, Different Strengths." A heading may carry the finding as a noun phrase, never as a sentence.
- 2026-08-16: "the descriptive text in the artifact is too long... make it a bulleted/numbered list of quick overview points." "cut this short... skip unnecessary points that might seem obvious."
- 2026-08-17: "change 'often' to 'sometimes'." Frequency words match the data.
- 2026-02-05: "Rephrase any claims or content that is hyperbolic. Keep the overall tone professional. Try to avoid mentioning sensational numbers in the abstract and conclusions."
- 2026-01-30: "Section 4.4.3 refers to results/*substitutions*.csv this is unprofessional in a technical paper to be published. look for similar issues and fix all of them."
- 2026-01-30: "Best Speaker is mentioned inconsistently across the paper... standardize using parentheses wherever you mention Best Speaker or BS."
- 2026-02-05: "This is popularly called rlhf pipeline in the company, but since it means something else outside, don't use the term rlhf."
- 2026-08-16: "don't make it sound like a huge failure on plantix. it is just how predictive systems work." Baselines and vendors are described fairly.

- 2026-09-16: "Modify all language as if a 10 year old can understand it. Simplify sections." Applies to the whole
  paper, not one section: split long sentences, replace or gloss every term of art on first use, and keep every number,
  denominator and caveat. A term that is also a column name stays, and the caption defines it.
- 2026-09-16: "Simplify all the contributions - max 15 words." Also no section numbers inside a contribution bullet;
  the reader finds the section from the heading, and the bullet is a claim, not a map.
- 2026-09-16: "Table 2 describes each stage. It does not 'know'." A table, a figure or a section does not know,
  believe, understand or think. It lists, gives, shows or describes. ("what is known about each stage" became
  "Table 2 describes each stage".)
- 2026-09-16: "stop confusing people by mentioning so many sections in one place. simplify the language -
  significantly." A basis or scope paragraph gets two sentences and at most one cross-reference. Push the rest into
  each table's own caption, which has to name its rows anyway.
- 2026-09-16: "THIS IS INTERNAL INFORMATION IRRELEVANT TO A NAIVE READER." Rows and shares that exist only because a
  feature shipped part-way through the corpus are internal history. Merge them into one row that states what is true of
  the reader's world (rows predating the gate plus rows judged with nothing recorded became one "No quality decision
  recorded" row), and keep the funnel summing to the total.

- 2026-09-16: "Improve the readability of the entire paper. I do not want to see this language anywhere in the paper.
  Make it professional, simple language that a 10 year old can understand. sentence construction needs to be simpler.
  Look at the description of Table 13. It is insane - no normal person will be able to understand it in the first
  parse. I am not reading the paper any further. I am tired of this language." A caption is where unreadable language
  is noticed first, because it is read out of context.
- 2026-09-16: "none of the tables or figures should have a description of more than 15-20 words. lesser the better."
  What will not fit becomes a note line under the table.
- 2026-09-16: "skip writing unnecessary edge cases like 'systems with partial language coverage are ommitted...'"
  A disclaimer written for a reviewer who is not reading yet costs a naive reader a sentence.
- 2026-09-16: "titles of all sub-sections to be simplified to recognizable names from Table 13. Don't invent or
  rephrase new names." Headings reuse the vocabulary the paper already defined.
- 2026-09-16: "Instead of saying B0, B1 and B2 -> just call them Baseline 0, Basline 1, Basline 2." Spell out short
  ids in prose; keep the id only where a column is too narrow.
- 2026-09-16: "before jumping into [the derived metric], just add 1-2 lines establishing the definition of WER." Define the parent
  metric before the derived one, even when the parent is standard in the field.
- 2026-09-16: "for all items in Future work, reduce the point level prose significantly. rephrase to max 1 line and
  20 words."
- 2026-09-16: "Don't mention anything as pending. this paper is the final publish-worthy version." Pending markers
  belong to the draft and the artifact, not the version being posted.
- 2026-09-16: "DONT EVEN MENTION PII IN THE PAPER." The review is handled in the released repository. Naming the
  process in the paper raises a question the paper does not answer.
- 2026-09-16: "Do not highlight this. just mention it as a footnote somewhere." A dependency that is not part of the
  argument gets a footnote, not a subsection.

## Numbers and Evidence

- 2026-02-04: "ensure all the tabulated results are accurate. You must find at least one supporting document or record... for all the results discussed. If you don't, flag it and let me review manually."
- 2026-02-04: "Do any of the claims seem too good to believe... Check if we are making any claims without sufficient evidence that would be raised in a review."
- 2026-02-04: "The docx file sensationalizes the results a bit. Ignore 93% statistic. The story here is - 4 human agronomy experts... 203 cases out of 308 and vanilla responses in 105 cases out of 308."
- 2026-01-30: "For odia, Google, SpringLabs and AI4Bharat, all show identical WER, CER and MER. This doesn't seem like a coincidence. Could you inspect if there is something fishy?"
- 2026-01-30: "Section 3.1 -> the number of transcriptions seem to be inflated a bit. Could you verify our results and update these numbers?"
- 2026-01-29: "Ensure all the models are reporting metrics for the exact same set of samples for fairness and consistency of benchmarking."
- 2026-08-16: "davit disease results seem unusually impressive. i feel like it'll be difficult to explain. seem suspicious? should i be double checking?"
- 2026-08-16: "since davit is a deep learning model... rejections should be treated as misses and accounted for in the error."
- 2026-08-15: "we need to explain whether the model accuracy values are being reported on the samples where a response was provided or all cases?... mention declined percentage."
- 2026-08-16: "instead of mentioning exact figures, mention ~ before the number to highlight that it is approximate number observed on a sample."
- 2026-08-16: "don't mention 11,000 or 0.3% (668 of 224,939) or any absolute number here." Absolute counts that invite the wrong reading are dropped.
- 2026-08-10: "we're providing ground truth during the inference which pollutes the results correct?" Contaminated comparisons are retracted, not caveated.
- 2026-06-28: "Drop the correlation and RMSE numbers. the paper is weak and the numbers expose it."
- 2026-09-05: "don't take any metrics results seriously yet... aggregate metrics are meaningless at this stage."
- 2026-06-20: "edit the details in the paper that are tentative and unverified right now because we blindly trusted the llm as a judge."
- 2026-06-09 (CEO comment adopted): "That compares Google STT without diarization to Azure diarized best speaker, not same model pipeline. Say 'best non-diarized baseline vs best diarized result' unless same-model."
- 2026-06-09 (CEO comment adopted): "If not quantified in paper, say 'we see this in production' not as benchmark finding."
- 2026-09-14: "Table 1 and Table 8 talk about 'Answered in' and 'Responded to'. These are unnecessary. In fact remove all instances where internal conflicts are being openly written in the paper. these are relevant for internal reviewers. not for external readers who are just trying to get a perspective of our approach." Status columns, Appendix B, superseded-number history and `\todo`/`\flag` markers moved to the tracker.
- 2026-09-14, on a two-denominator coverage caption: "no need to mention the exact number of images and no need to mention the conflicts here. just mention percentages and the representative curve which is the black curve mentioning 89.2%." One denominator per figure.

- 2026-09-14: "ensure experiment results details and numbers are quoted explicitly in Abstract, Introduction, Experiment Results, Conclusion. Don't quote specific numbers and results in other random places. Figures, Plots, flowcharts, other minor items in the papers should also be edited when a number or a result changes. But don't explicitly mention detailed numbers in these locations unless the figure explicitly warrants it. it is explainable in a table if needed only." Four homes for result values; figures carry structure; a changed number is swept through every carrier at once.

- 2026-09-16: "Just mention ~1.16 M photos from four countries." Round a corpus total in prose and in any header
  chip; the exact figure belongs in the one table that sources it, where the derived shares need it.
- 2026-09-16: "No need to mention 2.4 MB every time it is referenced. Only explain in the specific implementation
  section." A size, a parameter count or a per-call price is repeated only where the module is built. Elsewhere name
  the model plainly and let the results table carry the figure. Same rule as result values having four homes, applied
  to descriptive attributes.
- 2026-09-16: "inaccurate. Plantix has 2-4 seconds latency." A measured end-to-end total quoted next to a vendor's
  name reads as a claim about that vendor. Split the total by stage from the traces before comparing anything: the
  slow stage here was the quality gate at 6.2 to 8.2 s, not the diagnosis call at 2.8 to 4.4 s.
- 2026-09-16: "Inaccurate. Plantix gives category confidence values -> likely, very likely, unlikely." Check any
  "exposes no confidence" or "returns no breakdown" claim against a real captured response before writing it. A coarse
  word-level confidence is easy to miss in a large payload and makes the flat claim false.
- 2026-09-16: "this comes out of nowhere. doesn't belong in this section. not yet." A sentence that forward-references
  a design decision from inside a description of the existing system is cut, not moved earlier. The section that owns
  the decision already introduces it.
- 2026-09-17: A number sweep that updates every table cell still misses the differences between cells. After a scoring
  change moved two systems' values, the Conclusion still said "8.3 points better" and "0.8 points behind", both computed
  from the retired figures, and both gates passed because the values quoted were nowhere else in the paper. Sweep derived
  quantities too: differences, ratios, ranges ("15% to 56%"), counts of systems, and "N of M" statements. Recompute each
  one from the new table rather than reading it forward.
- 2026-09-17: `check_style.sh <directory>` used to print "clean" having checked nothing, because its loop skipped
  anything failing a `-f` test. Every "gate clean" run made against a folder was meaningless. Fixed to expand a
  directory to the `.tex` and `.html` sources inside it and to exit 2 when nothing matched. Lesson for any gate:
  make it report how many files it checked, and fail loudly on zero rather than passing silently.
- 2026-09-17: A `% number-ok:` exemption belongs at the END of its line and nowhere else. Placed mid-line to clear a
  gate, it made LaTeX discard the rest of the sentence, and the PDF lost a pointer to the scoring tables with no
  warning from any gate. Both gates and the build were clean; only reading the rendered page caught it. After adding
  any LaTeX comment, check the built PDF for the sentence it sits in.
- 2026-09-17: When a block is deleted for redundancy, grep for what pointed AT it before deleting. Three claims in
  other sections were left standing on support that had just been cut: a headroom clause, a "best in the comparison"
  cell, and an exclusion reason that then contradicted Limitations. A dropped row also renumbers subsections; check
  the ones after it.
- 2026-09-17: When a model is dropped from the results table, every figure measured on its own split dies with it. Before
  removing the row, list what only that model sourced (behaviour rates, confusion pairs, per-class readings) and decide
  per item: recompute on the surviving model's shared rows, or cut. Leaving them attributed to "the fine-tune" silently
  reattributes one checkpoint's measurements to another.

## Citations

- 2026-01-30: "this publication doesn't exist. The collaborators of Vaani never wrote a paper... how did you come up with this citation to begin with?"
- 2026-01-30: "This research paper doesn't exist. better to point to their website as well."
- 2026-02-03: "Can you verify every single reference citation. Whether it exists, whether it is necessary in the context in which it is being referred? Make a list of references for which you have different levels of confidence."
- 2026-02-03: "So, you can confirm that there is absolutely no citation that is fabricated in this paper?"
- 2026-02-05: "are there any orphan references that haven't been cited? do a thorough check."
- 2026-01-30: "there are 46 references. Are all of these really needed? Keep only those that are critical to the paper or have some real impact."
- 2026-08-16: "The gemma model isn't gemma-3-27B, it is gemma-4-e4B needs correction." Model identities are looked up, not recalled.

## Workflow

- 2026-02-03, twice more: "which file did you update? main.tex or main_updated.tex?" One master file.
- 2026-02-04: "@main.tex might be a couple of changes behind. @main_ieee.tex is my latest file. This was a mistake from my end. apologies, pls fix this file instead." Name the target file back to the author before editing when two exist.
- 2026-02-04: "Ok, the trimming part was probably unnecessary. Would you be able to roll back only the trimming changes?"
- 2026-08-10: "But I thought I told you not to create a fresh deck, it needs to be an augmented version."
- 2026-08-17: "only change what I'm telling you to, pls don't touch anything else."
- 2026-08-16: "review the artifact again. don't make any edits before I agree... just tell me the deviations."
- 2026-08-16: "any of this changes the actual content or does it just reorganize it?"
- 2026-08-11: "first give me the skeleton structure... Only after I approve the planned skeleton structure, go ahead and build."
- 2026-09-09: "which sections in the artifact did you update? because I'm looking at the results section and it feels like they are still the old results." Sweep every section after a data refresh.
- 2026-09-09: "i'd now like to do a fresh review session by clearing all the context from here. can you retain exactly what is needed to restart a fresh session?"
- 2026-01-28: "Can you create a guidance document that you can read yourself, so that later, when I have the updated results, I can just point you to the guidance document?"
- 2026-01-30, 2026-01-31: "what are you doing? why are you struggling for so long?" Long silent tool loops on a simple edit are a failure; report and ask.
- 2026-06-28: "Separate independent review done. Check if these comments make sense meaningfully. Don't deviate too far based on just this review."
- 2026-09-16: "We're sitting together, we'd like to reconcile the differences manually. So Curate a sheet with the
  list of differences - content and style wise... Leave a section open for comments which I'll fill. And then we can
  make changes. Only after that, carefully reconcile the differences into our paper - do this step by step." The sheet
  comes first, filled by the author, and reconciliation follows row by row.
- 2026-09-16: "Let's maintain one paper that we can collaboratively edit on - which will be the arxiv - main.pdf."
  One master; every other surface follows it.
- 2026-09-16: "Implement A+B+C+D. DO NOT implement E." Page cuts came from layout, figure geometry, table surgery and
  content reframing. Two-column layout was refused and is not a lever.
- 2026-09-16: "experiments owner is aakash. not lakshmi. lakshmi just owns the draft." Experiment ownership and draft
  ownership are separate; confirm both before the author block ships.

## Figures and Tables

- 2026-02-03: "The top and bottom parts of the pipeline are overlapping leading to superimposed boxes."
- 2026-02-03: "The legend is too far right it is spilling out of the page... The width of Q, A1 and A2 must be more."
- 2026-02-03: "Ensure all the text within Q, A1 and A2 have the same font size. The font is irregular right now. It is not aesthetic."
- 2026-02-04: "The figure showing cost performance tradeoff is very confusing. Let us remove this figure. Just include a simple table."
- 2026-02-04: "Fig 2 and Table 2 should both go up, closer to Section 3.3. They are all clubbed together and in different pages than the relevant sections."
- 2026-02-04: "That might be the case in the .tex file, however, the final latex render in the pdf shows Fig. 2 coming after Section 3.3.3." Check the PDF.
- 2026-01-30: "Table II seems to be spilling out of the page... Is that aesthetic? pls make a call."
- 2026-08-16: "'Route' is confusing. Call it Path A and Path B." (In the September skeleton the author chose Route A/B again; use the label in the latest skeleton and do not rename on your own.)
- 2026-08-16: "don't highlight the numbers at the top left boxes... The numbers are not flattering."

- 2026-09-16: "reduce the size of the overall figure. take care of text overlap with box boundaries." Size to content,
  then read the rendered page for text crossing a boundary.
- 2026-09-16: "Figure 3 ... make it tighter as 3-4 rows of connected boxes." A long chain wastes width.
- 2026-09-16: "table is very confusing with the numbers" (a multi-stage funnel). It became a funnel figure with a
  worked example per stage. The converse lesson also stands; choose the form the reader parses faster.
- 2026-09-16: "Table 12 (pair labels): add examples in a new column." An example column earns its width.
- 2026-09-16: "instead of representing the best number in each row with red font, make it green and bold." Red reads
  as an error, whatever it marks.
- 2026-09-16: "In the table, can we add green ticks for yes and red crosses." Ticks read faster than a column of
  repeated words.
- 2026-09-16: "Make Metric the primary column. Don't mention anything else in that column... Remove 'Group' and
  'scores' columns." A metric table is one row per metric plus one plain description.
- 2026-09-16: "Table 15 -> skip confidence interval. Make it two side by side tables with 4 columns." Intervals come
  out unless the argument is about uncertainty.
- 2026-09-16: "along with the configuration (S1 to S4), also mention the Module names again (M0 to M4) in a simple
  table with two columns. Makes it easier to associate Table 17." The mapping sits immediately before the results
  table, not pages earlier.
- 2026-09-16: "Move Table 17 and associated content to appendix. it is adding confusion. Same with Table 20. Wherever
  the point is F1 vs WER comparison, move it to appendix. these are redundant." With no appendix, cut or demote to
  bullets.

- 2026-09-17: applying the caption cap to a finished draft turns prose into points, and points take more vertical
  space than prose: the paper grew a page. Tighter `\intextsep` and `\textfloatsep` paid it back. Budget a layout
  pass after any prose-to-points round.
- 2026-09-17: moving caption text into note lines under the table also clears the number-placement gate's caption
  warnings (15 to 5 on one paper), because a note line is not a caption. The denominators stay visible either way.

- 2026-09-17: a label list that holds two classes for one crop (beet and sugar beet, pepper and chili pepper, bean
  and common bean) silently scores one system's vocabulary as error. It cost the production baseline 12 points in a
  headline table, more than any model difference in the same column. Before publishing a comparison, list each
  system's predicted labels that never match any reference label, and check the row-level correspondence: a
  prediction that meets one reference value on 472 of 484 rows is a spelling, not a mistake.
- 2026-09-17: merging duplicate label classes is a correction to the label list, so it applies to every system and
  gets re-run for all of them. Crediting an answer one level coarser than the reference (cucurbit for cucumber) is
  something else, leniency, and it favours the models that hedge over the baseline that commits. Keep the two apart
  and say which was chosen.
- 2026-09-17: a predictions file from a collaborator carried the gold label in top-level `crop` and `disease` and the
  model's answer in a nested `parsed` object. Auto-detecting field names by convention scores gold against gold and
  returns 100%. Reproduce the sender's own reported figures first; if they do not match, the field mapping is wrong.
- 2026-09-17: verify a collaborator's split-integrity claim rather than quoting it, and verify your own download
  before contradicting their document. A truncated local copy of a training split read 84,198 of 88,227 rows with no
  parse error, which looked like a discrepancy in their data and was not.

## Rationalization Table

| Thought | Reality |
|---|---|
| "The source doc says 'arm', so it is the domain term" | It is banned. Write route, model, or configuration. |
| "One em-dash reads better here" | Zero em-dashes. Rewrite the sentence. |
| "Pilot numbers make Results look complete for now" | Results stay empty or carry `\pilot` and a pending box. The author will ask where the number came from. |
| "The number is in the summary doc" | Summary docs were superseded twice. Trace to the row-level file or flag it. |
| "Regenerating the file is faster than patching" | The author asked which file changed four times. Patch and report. |
| "A prose paragraph explains it more fully" | Bullets, table, or figure. Prose is the exception. |
| "The citation is well known, no need to open it" | Two citations that "everyone knows" did not exist. Open it. |
| "Publishing without `url` is quicker" | It forks a new artifact and loses the review trail. |
| "The scratchpad is fine for the HTML source" | It vanished once. Project folder only. |
| "Restructuring while I am in there" | Say what is reorganized versus new; get approval for structure first. |
| "This figure will float near enough" | Check the compiled PDF page by page. |
| "A witty heading adds life" | Dry noun phrase. "Current Pipeline." |
| "The accuracy belongs in the module section, that is where the model is described" | Describe the module, cite the Results table by number. Values live in Abstract, Introduction, Results, Conclusion. |
| "Printing the accuracy on the pipeline box makes the figure self-contained" | Figures carry structure. The value goes in a table beside it, and the figure is regenerated when the value changes. |
| "The exact count is more rigorous than the rounded one" | In prose it is noise. Round it and let the source table carry the digits. |
| "Repeating the model size reminds the reader how small it is" | It reads as selling. State it once, where the module is built. |
| "The measured total is the honest latency number" | Next to a vendor name a total becomes a claim about that vendor. Split it by stage first. |
| "The source system documents no confidence value" | Open a captured response. A word-level likelihood counts, and the flat claim is then wrong. |
| "The caption needs one more clause to be precise" | Twenty words, then a note line under the table. An unreadable caption is noticed before an unreadable paragraph. |
| "B0 and B1 are defined in a table, so the reader knows them" | Spell them out. "Baseline 0" costs two words and saves a lookup. |
| "Red makes the best value stand out" | Red reads as an error. Green and bold. |
| "WER is standard, no need to define it" | Define the parent metric in one line before the derived one. |
| "Stating what is not yet measured is honest" | In the published version it reads as unfinished. It is a Future Work line in the future tense. |
| "Mentioning the PII review shows diligence" | It raises a question the paper does not answer. The repository handles it. |
| "Two columns would solve the page count" | Refused outright. Layout, figure geometry, table surgery, then cuts. |
| "Their draft says it better, so append their paragraph" | Merge at the same length into one master, after the differences sheet comes back filled. |
| "The baseline just scores badly on this column" | Check its label vocabulary against the reference's first. One duplicated class cost 12 points. |
| "Normalising more makes the comparison fairer" | Merging duplicate names is a fix. Crediting a coarser answer is leniency, and it picks a winner. |
| "The predictions file's crop field is the prediction" | It was the gold label. Reproduce the sender's own numbers before scoring. |
| "Their document's row count disagrees with the file, so their document is wrong" | Check your download finished. |
| "Showing the open conflicts in the paper is the honest thing" | Internal reviewers read CRITICAL_REVIEW.md. The PDF states each gap once in reader-facing words; no status columns, superseded numbers, or reconciliation appendix. |

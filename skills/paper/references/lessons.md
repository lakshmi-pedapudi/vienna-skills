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
| "Showing the open conflicts in the paper is the honest thing" | Internal reviewers read CRITICAL_REVIEW.md. The PDF states each gap once in reader-facing words; no status columns, superseded numbers, or reconciliation appendix. |

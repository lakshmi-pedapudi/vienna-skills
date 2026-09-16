# Lessons: Corrections and Pushbacks

Dated, verbatim where possible. These are the moments the author stopped the work. Read them as tests the next page must pass. Sources: funder pre-read (Aug 2026), Resolution Signal (Aug 2026), methodology article (Jul 2026), The Gate and the Gap (Sep 2026), Follow-Up Query Analytics (Sep 2026), paper artifacts (Sep 2026), the survey vendor pages (Apr 2026).

Each quote belongs to the page it was said about. The correction generalises; the subject, the vendor, the model name and the number do not. Nothing here is a figure for the page in front of you.

## Length and Prose

- 2026-08-19: "Keep it absolutely crisp and to the point. Don't be too verbose. If you're writing more than 3 sentences or 100 words, make it bulleted or convert into a chart or a table with simple captions."
- 2026-09-07: "too verbose and too many sections and graphs. can you narrow it down to simple visualizations, examples and basic explanation text - concise, numbered/bulleted with only the main numbers."
- 2026-09-08: "I'm sick of looking at ai generated verbose text for no reason."
- 2026-08-16: "across all the four tiles, make the content visual or bulleted rather than overly descriptive." "Again, make all this either visually descriptive or add bullet points and keep them concise."
- 2026-08-16: "the descriptive text in the artifact is too long. Can be cut short - remove risky parts to present in public forum and make it a bulleted/numbered list of quick overview points."
- 2026-08-16: "cut this short. make it concise and skip unnecessary points that might seem obvious. give me the reframe first before updating directly."
- 2026-07-25: "keep it minimal. don't reference any external resources here. treat it like a fresh clean documentation anyone can understand. don't keep too many sections."

## Words and Headings

- 2026-08-15: "please do not add information that is self referential or something that can't be understood, no unnecessary footnotes. main content, as simple as possible, clean, with necessary charts/images/tables as concise and visual as possible. don't use weird hyper jargon language like 'arms' for 'models'. keep the language as colloquial as possible. words like 'axes' or 'verdict', and don't use that style where you use 'not' in the heading phrases like 'verified not committed', or 'evidence not verdict' etc. No em-dashes. try to minimize ai - generated markers."
- 2026-09-08: "DO NOT USE terms like 'instrument', 'arm', 'license', 'ground' etc to describe basic technical concepts."
- 2026-08-11: "'What happens to a photograph today' -> I don't like this kind of phrasing. I'd rather prefer simpler dry titles like 'Current Pipeline'."
- 2026-08-17: "Model Comparison: Crop and Disease Accuracy -> Say instead - Model Comparison: Different Models, Different Strengths."
- 2026-08-17: "change 'often' to 'sometimes'."
- 2026-08-16: "Quality gate - say gpt based LLM check instead of Paid service." 2026-08-13: "change 'paid service' references to the vendor pls." 2026-09-09: "You can use 'the vendor' instead of 'Paid Baseline' everywhere."
- 2026-08-16: "Also probably need to mention somewhere that DaViT means Dual Attention Vision Transformer."

## Standalone and Self-Reference

- 2026-08-19: "this artifact should not contain any self references or the process we followed or references to a person or gates foundation or anything like that. it is a self contained entity that any random person reading can understand."
- 2026-08-16: "Remove references to sentences like these - 'Also flagged from the data, outside the CEO's five'. also time to do a review of the entire doc - remove all self references or references to people or internal documents. also do a style check based on the rules set earlier."
- 2026-08-16: "Remove the 'Changes in this version' section ... No reference to internal artifacts or names or documents. Make it sound like a first version, fresh upload."
- 2026-08-15: "you can skip this disclaimer altogether - 'Bucket 9 is new ... That screen still needs to happen before this bucket can ship.'"
- 2026-08-15: "None of this is built yet. It's the direction everything above is pointing us toward. -> Change this to 'Our internal pipeline for continuous improvement'."
- 2026-08-16: "include it in the decomposition plan and session findings but in the pre-read section, don't make it sound like a huge failure on plantix."
- 2026-08-15: "'The question effect' this section isn't adding value and it is increasing confusion ... this is probably something of a bug for us to fix internally than to show externally."

## Caveats and Footnotes

- 2026-08-16: "Remove all of it. none of it is useful. We can write latency/cost related specifications in a separate column that says 'Comments'. But even there, don't write anything. just add a column."
- 2026-08-15: "Voice is measured as a floor here ... -> remove this sentence."
- 2026-08-16: "metric calculation for accuracy not clearly explained in the pre-read artifact. - provisional pending a check for training/test overlap. No need to add this phrasing for Davit."
- 2026-08-17: "Confirmed real livestock photos only (false positives and unreadable species dropped). -> remove the part in the parentheses. keep it simple."

## Numbers

- 2026-08-16: "Mention this mechanism of accuracy calculation in the pre-read ... also mention declines." "I still don't see decline number as a separate column in the model comparison table. Gemma-FT is not present in the table."
- 2026-08-16: "what would the numbers look like if the denominator was the entire 10,335 samples and why aren't you doing that?"
- 2026-08-16: "instead of mentioning exact figures, mention ~ before the number to highlight that it is approximate number observed on a sample."
- 2026-08-16: "don't highlight the numbers at the top left boxes. Make it a simple normal sized heading ... start with 28.2% rejected on quality gate before diagnosis runs ... The numbers are not flattering in the current scenario."
- 2026-08-17: "Better to say 8.9% of photos arrive with typed or spoken words; voice is currently 0.2% of all photos ... Should be photo (not query) volume."
- 2026-09-06: "Candidate rows = 3.29M is a bit misleading. we're focusing on Original Queries number only ... also remove 6.87M candidate rows number from here. this is again misleading."
- 2026-08-17: "What are you talking about. Image is not 639. We had close to 1.2 M image queries earlier. we're literally working on the claude artifact for vlm workshop." A query result that contradicts the page's own headline is caught before it is shown.
- 2026-08-18: "this chart is confusing because I would've expected all greens (country level) to add up to 100%."
- 2026-07-25: "Don't include the actual cost estimates yet. it depends on where we host it and our workloads etc. so that is TBD."
- 2026-09-05: "don't take any metrics results seriously yet ... aggregate metrics are meaningless at this stage." Skeletons carry status markers, not provisional numbers.

## Visuals

- 2026-08-16: "I don't need the entire explanation, but a simple visual flowchart with 4 boxes -> Farmer sends an image + query, Quality gate detects quality, Prediction model gives prediction, LLM synthesis gives the final answer."
- 2026-08-16: "could you show a translucent bar against each row's accuracy number to also show a visual representation of accuracy?"
- 2026-09-06: "the section with Geography & language does not indicate any bar showing the percentages. the bars are static, only the numbers are written on side." "the flow chart has some overlapping text."
- 2026-08-17: "no this table is confusing or overwhelming. need a better visualization to show top 4 crops by country."
- 2026-08-17: "the Image vs Text column - too much detail in a single table. overwhelming. let's reverse this, and make it a new table ... In the current table, remove the explanations."
- 2026-08-17: "Model comparison table -> Davit and Qwen-FT are our planned deployment models, Gemini and the vendor are existing baselines. Can you highlight those rows in separate colors?"
- 2026-08-17: "brown bars have to say held out somewhere near the barplot, otherwise it is not clear. and '8 Models One Question' is getting obstructed by some legend."
- 2026-08-17: "8 independent opinions - can you make it a small bar chart with different color bars for the 5 models and 3 held out models? That way, you don't need another sub-section."
- 2026-08-17: "I want to show that the validation and test datasets will go for human review, not just write it. how could that be visually shown?" "Human review part needs to be a little more prominent both in style and font and maybe just a little flashy."
- 2026-08-17: "this heading can be bold and same font as other headings and can be moved outside of the visualization box."
- 2026-08-17: "both charts side by side would be better. one below the other is not needed." "is it possible to make the chart slightly less wide and slightly taller? width 75% of current, and 10% taller."
- 2026-08-17: "the arrow that says 'vote' doesn't have to be curved and it is too long. adjust the gap between 2nd and 3rd boxes and the size of the arrow."
- 2026-08-16: "Can you extend the X-axis to show almost 100% and show the long tail to indicate Top 20, Top 30 and Top 40 numbers as well in the graph."
- 2026-08-19: "keep the response inside a box that is fixed height and i can scroll within the box." "can you make a grid and reduce the overall scroll pls."
- 2026-08-18: "keep the green for photo, but for text, make the color gray and for voice make it dark, blackish gray."
- 2026-09-07: "I think you're trying to show example photos but they're not showing up in the UI right now."
- 2026-07-25: "Currently, that one flowchart has become too small to read ... I'd like it to be prominent." Then: "the flowcharts are now too big. Just separating them was enough."

## Process

- 2026-08-08: "maintain this as an artefact so we keep editing live before we can respond to rikin."
- 2026-09-05: "publish a claude artifact with bare minimum skeleton and mapped references. let's build the artifact one element at a time."
- 2026-08-11: "first give me the skeleton structure ... Only after I approve the planned skeleton structure, go ahead and build. don't carry forward any existing bias."
- 2026-08-16: "review the artifact again. don't make any edits before I agree. this is the expected theme, just tell me the deviations."
- 2026-08-16: "cool. try not to add any new content that is not relevant. and make the changes to the live artifact."
- 2026-08-16: "Cool, looks good but it is too wide ... re-render pls." then "cool. wire it up in the live artifact."
- 2026-08-17: "only change what I'm telling you to, pls don't touch anything else."
- 2026-08-17: "Do 1 and 2. Don't do 3. don't do the slide split yet. let's first see how the changes look."
- 2026-08-16: "reconcile the entire document, check for logical inconsistencies, and make sure the whole document from earlier iterations lines up with latest findings. so go from latest to first."
- 2026-09-09: "which sections in the artifact did you update? because I'm looking at the results section and it feels like they are still the old results."
- 2026-08-17: "keep a copy of this artifact in case we want to roll back changes."
- 2026-08-17: "dude do not touch the railway_preread under any circumstances. that is already published ... this url is already sent to gates. I repeat - DO NOT TOUCH IT. I presume all edits from here on out will be done on this artifact only -> [url]."
- 2026-08-19: "which artifact did you do this update on? worth reconciling stage with the main and just maintaining one artifact."
- 2026-08-17: "something wrong with the artefact. Slides 5-9 aren't rendering." then "Cant see slides 5 to 9 still."
- 2026-08-17: "the pdf version converts the flowchart of 4 tiles in one row into four separate rows. How do I avoid that?"
- 2026-08-17: "my org doesn't let me share the claude artifact publicly ... migrate this artifact to my personal claude account?" Declined; exported and mirrored to Railway instead. "I have the authorization from the ceo ... publish this on railway."
- 2026-08-19: "Can you start dumping them in a sub-folder next time so that they don't get lost and I might do some further analytics myself?"
- 2026-09-12: "i asked aakash to edit it collaboratively. can you see any latest changes compared to what we already had earlier?"
- 2026-09-09: "i want to clear the context here and start a fresh session. can you write up everything you have so far including the artifact details so that i can start fresh?"

## Rationalization Table

| Thought | Reality |
|---|---|
| "A fresh publish is simpler than finding the URL" | It forks the page and loses the review trail. Find the URL in the status memory. |
| "The scratchpad is fine for now" | Two sources were lost that way. Project folder, then publish. |
| "This paragraph is only four sentences" | Bullets, a table, or a chart. The limit is three. |
| "A confidence note helps the reader" | The author deletes caveat blocks outright. One plain sentence at most. |
| "'The paid service' is safer than the vendor name" | Naming was cleared. Ask once if unsure; do not euphemise by default. |
| "This rejection rate is the key finding, make it a tile" | Unflattering numbers go inline with their qualifier. |
| "A 'What This Page Covers' section orients the reader" | Self-reference. The structure orients the reader. |
| "I will reorganize and tidy the wording while I am in there" | Reorganize only. Say what moved versus what is new. |
| "Two sections changed, no need to sweep the rest" | Reconcile latest to earliest; stale results were caught by the reader. |
| "The build published, it must render" | Open it. Blank sections shipped twice. |
| "A chart library would be faster" | Blocked by CSP and by house rule. Inline SVG or a data URI. |
| "Move it to a personal account to share" | Production data. Export or Railway with authorization. |

## Baseline Trial, 2026-09-14

A fresh agent with no skill wrote a funder pre-read from a small materials folder. Observed: eleven sections where four to seven were needed; a "Summary" pull quote with editorial framing the sources did not support; sections titled "Evidence and Confidence", "Solid", "Not Yet Solid", "Claims We Are Not Repeating" (self-referential, colloquial headings); a confidence chip on every number plus a "Confidence Warning" callout and a five-trace caveat box; four paragraphs over 60 words; "verdict" in the body; light-only theme with no `data-theme` override. Done well without the skill: em-dash free, names and ids stripped, proportional CSS waterfall, inline SVG chart, derived numbers labelled, the unverifiable vendor claim flagged rather than used.

## With-Skill Trial, 2026-09-14

Same task, same materials, skill loaded. Five sections with status pills, one paragraph on the whole page, nineteen list items, three inline SVGs (flowchart with structure only, monthly bars, latency waterfall with widths tied to seconds), two tables with in-cell bars and row tints, a pending box for the disease column, the vendor and model names used, both rejection denominators named, tildes on the five-trace latency figures, three-state theme, gate 0 failures 0 warnings. The trial exposed a defect in the skeleton template (the numbered-list grid split the bold lead-in from its text, one word per line), fixed in the template. The agent found it by rendering the page in a headless browser and reading it, which is the step the rule "open the live page and look" exists for.

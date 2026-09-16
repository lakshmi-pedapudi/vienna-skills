# Lessons: Corrections and Pushbacks

Dated, verbatim where possible. These are the moments the author stopped the work. Read them as tests the next deck must pass. Sources: board deck (Apr 2026), latency report (Apr 2026), the benchmark CEO deck (Jun 2026), image methodology (Jul 2026), funder workshop deck and pre-read (Aug 2026), gender slides (Aug 2026).

Each quote belongs to the deck it was said about. The correction generalises; the subject, the vendor, the model name and the number do not. Nothing here is a figure for the deck in front of you.

## Titles and Words

- 2026-08-11: "'What happens to a photograph today' -> I don't like this kind of phrasing. I'd rather prefer simpler dry titles like 'Current Pipeline' or something similar. this is true for entire deck."
- 2026-08-13: "'Two ways to build it' is a ridiculous title, change it." Fix: state the methodology at top level first, then expand into the two implementations.
- 2026-08-15: "don't use weird hyper jargon language like 'arms' for 'models'. keep the language as colloquial as possible. words like 'axes' or 'verdict', and don't use that style where you use 'not' in the heading phrases like 'verified not committed', or 'evidence not verdict' etc. No em-dashes. try to minimize ai - generated markers."
- 2026-08-13: "'Under the rule' is very confusing. Just mention disease identification accuracy." "'Declined' as a metric is also confusing." "Reliability is very confusing. Drop it."
- 2026-04-26 (review round 3): "Title -> 'Overview'. Stop using 'Theme' everywhere. Use simple words like 'Topic' / 'Description'." "Don't write commentary subtitles. 'Why it matters' -> 'Impact'." "Don't say 'V2 product pivot', call it 'Enhancements'."
- 2026-04-26 (review round 2): "Simplify terms ('Blast radius', 'Mitigation in flight'); reframe as opportunity." Became the jargon table and "Optimisation opportunities".
- 2026-08-16: "'Route' is confusing. Call it Path A and Path B." (The September paper skeleton chose Route A/B again; use the author's latest label.)
- 2026-08-17: "change 'often' to 'sometimes'." Frequency words match the data.
- 2026-08-17: "Confirmed real livestock photos only (false positives and unreadable species dropped). -> remove the part in the parentheses. keep it simple."

## Content and Numbers

- 2026-04-25: "How did you decide cost reduction over 50% target? you need to be a bit more descriptive." "When you make a claim, show the work and references. this is mandatory for all the slides."
- 2026-04-25: "you might have oversimplified the slides based on my earlier commands but it is not necessary to do to this extent. the CXOs are patient and smart enough to understand these technical details."
- 2026-04-25: "for all other regions/languages, the work is in progress, so the cost reduction is 'expected' not actual."
- 2026-04-14: "telugu trans out p95 seems to be 3.5 s in the table, but doesn't reflect in the chart or in the key observations, what's going on there?"
- 2026-06-09 (CEO deck): two error-pair examples in a colleague's deck were "NOT in our data"; replaced with verified rows cited to the CSV with n. "'~1 in 3 errors lands on a high-value ag term' ... Couldn't verify the denominator ... Confirm the source or soften it."
- 2026-08-16: "instead of mentioning exact figures, mention ~ before the number to highlight that it is approximate number observed on a sample." "For Davit FT, Gemma FT, Qwen FT, mention in cost/query -> Training & Hosting."
- 2026-08-16: "don't highlight the numbers at the top left boxes. Make it a simple normal sized heading ... start with 28.2% rejected on quality gate before diagnosis runs ... The numbers are not flattering in the current scenario."
- 2026-08-16: "are we giving accuracy numbers excluding the 'Declined' queries or including?" Both bases named.
- 2026-08-18: "huggingface published data for gates foundation says this - Top crops: Rice (346,697) ... Rice comes up to 7% but the chart says Rice is 15% what's wrong?" Reconcile with everything published.
- 2026-08-18: "this chart is confusing because I would've expected all greens (country level) to add up to 100% ... can we reconcile the numbers on the bar chart?"
- 2026-07-25: "Don't include the actual cost estimates yet. it depends on where we host it and our workloads etc. so that is TBD."
- 2026-08-10: "livestock content - it is what it is. don't mention any reasons ... so let the data reflect as it is right now."
- 2026-08-15: "'The question effect' ... this is probably something of a bug for us to fix internally than to show externally."
- 2026-08-16: "don't make it sound like a huge failure on plantix."

## Names, Codes and Standalone

- 2026-04-13: "don't mention engineering response or ramaskanda or any of the follow up details. higher management doesnt care about intermediate discussions."
- 2026-04-26 (round 1 and 2): "No names" on four slides; "Image contains names ('a teammate', 'a co-author'); make boxes native pptx." "Don't say 'CTO review framing'." "no section codes."
- 2026-06-09: "can you ensure none of the contents or notes within the ppt contain names like 'rikin', 'vineet' etc. or any reference to 'hausa'. Don't refer to details discussed outside of the scope of the pptx. the pptx is a standalone artefact to be used for external presentation."
- 2026-08-10: "It should be a standalone artefact, no reference to any other docs or internal proesses or earlier discussions."
- 2026-04-27: "don't show P02, P16 etc as prompt labels. keep it simple ... refer to Query Orchestration in next flows as a single box."
- 2026-04-26 (round 1): "Can you make this a table of text instead of an image of a table? I'd like to be able to edit the text." Became the native-text rule.

## Structure

- 2026-08-11: "first give me the skeleton structure. Prepare the underlying artefacts and details on the side. Only after I approve the planned skeleton structure, go ahead and build the full deck. don't carry forward any existing bias regarding the slides."
- 2026-08-10: "But I thought I told you not to create a fresh deck, it needs to be an augmented version of ... is this taken care ?"
- 2026-08-13: "One major rule throughout - Don't be overly discreptive where tables/charts can do the trick. And if you're using text, keep it to short numbered/bullet points ... something to follow religiously in presentations."
- 2026-08-13: "Wherever possible, skip redundant slides or merge with larger scope. Conciseness helps hold attention without making it seem useless to scroll through a basic concept in an entire slide."
- 2026-08-13: "Route Comparison - Slide 5.4 - too self referential, too confusing. boil down the tradeoffs into 2-3 points. I don't even know where this fits."
- 2026-08-13: "Section 6.6 - completely skip. we don't have a good point to make here. not worth venturing. we can talk about it if brought up."
- 2026-08-13: "Demand profile - the entire slide can be just 1-2 bullet points ... this probably goes into appendix and gets referred to in the detailed hosting scenarios."
- 2026-04-26 (§2.2): "The 27-main-slide version was too long for board attention budget." Budget 15 to 18 main slides.
- 2026-04-26 (round 1): "Purpose unclear - merge or skip." "abstract slide doesn't belong standalone." Content distributed inline.
- 2026-04-26 (round 1): credits "Move to end; separate the two providers; inline notes in main slides." Funding is a sub-thread, not the headline.
- 2026-08-17: "max 10 slides, with approx 10 mins presentation worthy content. don't make any content changes. just logical splits and organization. but before that, keep a copy."
- 2026-08-16: "review the artifact again. don't make any edits before I agree. this is the expected theme, just tell me the deviations - Narrative spine ... The rationale is differentiation - other presenters will lead with generic confidence and accuracy percentages."

## Visuals and Charts

- 2026-04-25: "The bar chart is completely misleading, so I'd get rid of that first."
- 2026-04-26 (round 2): "Bar graph meaningless; merge with Partnerships slide." "Replace error-rate chart with a Hard / Soft variables table." A confusing chart loses to a table.
- 2026-08-13: "Slide 2.6 -> ... the flowchart image is doing majority of the heavy lifting so the image needs to be the prominent piece in the slide where the attention goes first. Text is secondary."
- 2026-08-13: "build separate charts for - volume by month, volume by country, and volume by country + month ... Better to keep this as separate charts rather than tables."
- 2026-04-14: "show histograms of times taken ... highlight 4 quartiles + 90th and 95th percentile so that it is clear if there are any bimodal distributions or significant number of outliers."
- 2026-08-16: "Can you extend the X-axis to show almost 100% and show the long tail to indicate Top 20, Top 30 and Top 40 numbers."
- 2026-08-17: "no this table is confusing or overwhelming. need a better visualization to show top 4 crops by country."
- 2026-08-17: "the Image vs Text column - too much detail in a single table. overwhelming ... make it a new table."
- 2026-08-17: "brown bars have to say held out somewhere near the barplot, otherwise it is not clear. and '8 Models One Question' is getting obstructed by some legend."
- 2026-08-17: "the arrow that says 'vote' doesn't have to be curved and it is too long. adjust the gap between 2nd and 3rd boxes."
- 2026-08-17: "both charts side by side would be better. one below the other is not needed." "make sure that the heading sits outside the viz box similar to other headings."
- 2026-08-17: "Model comparison table -> Davit and Qwen-FT are our planned deployment models, Gemini and the vendor are existing baselines. Can you highlight those rows in separate colors?"
- 2026-08-18: "keep the green for photo, but for text, make the color gray and for voice make it dark, blackish gray."
- 2026-07-25: "Currently, that one flowchart has become too small to read, while that is a major part of our overall strategy. I'd like it to be prominent." Then: "the flowcharts are now too big. Just separating them was enough. zoom them out to normal size."
- 2026-04-27: "all the artefacts need to fit within a ppt slide. and all the text needs to neatly fit into a box without spillover."
- 2026-04-26 (round 1): "overlapping text makes this plot unreadable."
- 2026-09-06: "the bars are static, only the numbers are written on side." Bars must be proportional.

## Process

- 2026-04-26: "I've added my review comments as 'the author: ' in the pptx ... before you do that though, can you retain the earlier version as v-1 so that i can refer back to it if i want to? the latest version will always remain deck.pptx. Be careful."
- 2026-04-26: "ensure that these instructions are followed for all future sessions of this ppt deck generation." Rules go in the rules file, numbered.
- 2026-04-26: "so ensure all the necessary details are present in the md file for you to understand in the next session when you don't remember any of these."
- 2026-04-14: "It looks like trying to build addendums is making the reports worse. can you use the existing reports and generate fresh reports from scratch."
- 2026-04-15: "could you create this as an addendum pptx and word docx maybe so that i can make the changes in the main documents by myself easily?"
- 2026-06-09: "so if i had to make explicit edits to _5 version instead of using _6 directly, which slides would i replace/add independently?"
- 2026-08-16: "cut this short ... give me the reframe first before updating directly."
- 2026-08-17: "only change what I'm telling you to, pls don't touch anything else."
- 2026-08-17: "Do 1 and 2. Don't do 3. don't do the slide split yet. let's first see how the changes look."
- 2026-08-17: "dude do not touch the railway_preread under any circumstances. that is already published ... I repeat - DO NOT TOUCH IT."
- 2026-08-17: "something wrong with the artefact. Slides 5-9 aren't rendering." Then again: "Cant see slides 5 to 9 still."
- 2026-08-17: "the pdf version converts the flowchart of 4 tiles in one row into four separate rows. How do I avoid that?"
- 2026-08-15: "fix all issues identified earlier. - #1 ... not fixed. - #2 ... not fixed. - #3 ... not fixed."
- 2026-08-13: "review one more time for internal consistency (review your own work in a fresh iteration). then ... create a fresh slide deck pls. It's time we take a look at what the final product looks like."
- 2026-07-25: "looks like my org doesn't allow sharing the claude artifact to anyone with the link publicly. Can you convert this into a slide deck directly on my google slides perhaps?"
- 2026-04-28: "please review the formatting and the title slides in this ppt. don't change any of the order of the slides. check if the overview slide (2) correctly describes the rest of the ppt. ensure page numbers are accurate."

## Baseline Trial, 2026-09-14

A fresh agent with no skill built a 6 to 8 slide funder deck from a small materials folder. What it got wrong, in order of how often the author has corrected the same thing:

- Titles read as phrases or sentences: "Three Steps Behind Every Photo", "Conditions for a Switch", "Service and Scale". Plain nouns were available: "Current Pipeline", "Next Steps", "Scale".
- Text boxes carried 40-word paragraphs labelled "Interpretation" instead of a table or numbered points.
- 20 numerals on slides resolved to no registry row: derived percentages (136%, 61%), roundings (94.6%, $3,000), and a computed monthly cost. Derived numbers need their own registry rows with the formula in `claim`.
- The vendor became "the paid outside service" and the models became "fine-tuned open model", although the notes named both and clearance was given.
- Pilot, LLM-judged numbers were rendered as hero stat cards.
- A caveat footnote on five of eight slides (currency, funnel gap, sample size, July spike, excluded claim). One footnote per slide at most, only when load-bearing; the rest go to speaker notes.
- No speaker notes on any slide.
- The file was never opened; layout was "verified programmatically". Fifteen layout warnings, one real overflow.

What it got right without the skill, so the skill need not belabour it: names and task ids stripped, jargon rewritten, em-dash free, charts regenerated from CSV, the unverifiable ~93% claim flagged rather than plotted, both accuracy bases named.

## With-Skill Trial, 2026-09-14

Same task, same materials, skill loaded. Eight slides: Farmer Demand, Current Pipeline, Crop Recognition, Disease Diagnosis, Serving Cost, Response Time, Next Steps. Every slide carried an eyebrow, a plain-noun title, numbered points with bold lead-ins or a native table, one takeaway, a footnote with the basis, and speaker notes with "if asked" answers. the vendor and the model names used. Disease accuracy rendered as a pending block naming the owner; hosting cost left as an estimate in a "Basis" column. Word gate 0, layout 0, figures gate clean once page footers and point labels were exempted (the trial exposed that false positive). The agent wrote a markdown draft first and an approximate renderer to look at the slides, since no PowerPoint renderer exists on the machine.

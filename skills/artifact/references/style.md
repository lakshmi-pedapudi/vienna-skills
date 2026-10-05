# Style Rules

Applies to: every visible string on the page, including headings, body, tiles, table cells, captions, chart labels and alt text. Any user or project writing rules apply on top.

## Standalone

- A stranger with no context understands the page end to end. *Why: pages are forwarded, and the forwarded reader has none of the conversation.*
- Strip internal scaffolding: no named colleagues, no funder names in the body, no internal document or file references, no tracker or task ids, no internal table names, no "as discussed", no references to a colleague's list or request.
- No process narration and no self-reference: nothing about what is or is not finished, how the page was built, or which version this is. No changelog; every publish reads as a fresh first version.
- No disclaimers about unfinished internal work. Label future work neutrally for what it is. *Why: a disclaimer makes the reader doubt the finished parts too.* Example: "None of this is built yet" becomes a section titled "Planned Improvement Pipeline".
- Internal working documents and the published page carry the same facts in a different tone. Risky, unflattering or internal-bug material goes in the working document only. *Why: an internal bug shown externally reads as a product failure and adds confusion.*
- Name vendors and models once naming is cleared, and never show them in a bad light. *Why: a euphemism for a named competitor hides the comparison the reader came for.* Ask once if clearance is unknown.
- Do not over-commit to one approach. Show the competing options and the criteria that will decide (for example accuracy, cost of serving, latency, reliability).
- For senior audiences, drop internal identifiers and collapse an explained subsystem to one box.
- Screen every embedded sample for personal data before it ships: faces, documents, location overlays, minors, watermarks.

## Prose Limits

- More than three sentences or about 100 words in one place becomes bullets, a numbered list, a table, or a chart with a one-line caption. *Why: readers skim, and dense prose is where filler hides.*
- Every tile is visual or bulleted. Never a descriptive paragraph.
- Bullets open with a bold lead-in. Numbered points for sequences and arguments.
- Skip points a reader would find obvious.
- First drafts over-produce; cut to simple visuals, a few examples and the main numbers.

## Sentence Shapes

Rhetorical shapes that read as AI-generated, whatever the wording. The rule targets the shape: rewording a pivot so it sounds less templated does not pass it; restructure the sentence. Applies to body text, bullets, tiles and captions, not only headings.

- No "not A, but B" pivots: "this is not about X, it is about Y", "we do not X, we Y", "not only X but also Y". State the affirmative claim first. If the contrast carries information, frame it as a finding ("the bottleneck turned out to be Y"), not a rebuttal. The gate warns on pivot shapes.
- List length matches the content. Two items are a complete list; a third added for rhythm is padding.
- One concrete detail over stacked adjectives: "scales to 10,000 concurrent requests", not "a powerful, flexible, scalable pipeline". Tiles especially.
- No importance preambles or intensifiers: "it is crucial to understand", "truly", "arguably one of the most important". State the claim.
- No tagline sentences or pull quotes that perform rather than explain ("Full stop.", "The receipts do not lie."). Read-aloud test: if a line sounds like it is addressing an audience, rewrite it as a claim with its context or cut it.
- Sections end on their most specific implication, not on a recap of what the section just said ("In summary", "To summarise").
- No generic hinge phrases ("that being said", "at the end of the day") and no narrated structure ("now let's look at", "below we explore"). Headings already signpost.

## Headings

- Formal noun phrases in Title Case: "Current Pipeline", "Model Comparison", "Serving Cost", "Next Steps".
- Not narrative ("What happens to a request today"), not a question, not "X not Y" ("evidence not verdict"), not clever ("Two ways to build it"). *Why: dry headings let a reader scan the page as an outline.*
- A heading may carry the finding as a noun phrase: "Model Comparison: Different Models, Different Strengths".
- Headings live in the page's type system, outside any visualisation box, consistent across sections.
- Section count for a pre-read or report: four to seven.

## Words

Banned everywhere: em-dashes in any form, and the house word list in `scripts/house_words.json` (arm for a model or variant, instrument, licence as metaphor, verdict, axes, "under the rule", and jargon such as blast radius, force multiplier, fan-out, operationalise). Also banned and checked by the gate: leverage, robust, seamless, delve, unlock, dive into, genuinely, paramount, "it is worth noting". Not gated but equally banned: "ground" as filler. Use plain colloquial words for ordinary technical things. *Why: metaphor-jargon makes simple ideas look harder and reads as machine-written.* Example: "two model arms" becomes "two models".

Expand every acronym on first use. Define every metric plainly. Quantifiers match the data (a single-digit share is "sometimes", not "often"). Rename anything a reader might misread, everywhere at once, and keep the author's latest label.

## Numbers

- Every metric carries its calculation basis: denominator, declines or abstentions, the unit (per item or per request), the population it is a percentage of. Where two bases exist, name both.
- Prefix approximate values observed on a sample with a tilde.
- Never quote an inflated derived count when a smaller true count is the honest unit. Example: report the <N> original requests, not the <M> candidate rows derived from them.
- Never fabricate a number or an example. A number with no file behind it is flagged, not shown.
- Do not hero-size an unflattering number. Fold it into a normal heading with its qualifier: "<x>% filtered at the first step, before the main model runs".
- Withhold numbers that depend on undecided infrastructure. An empty labelled column beats an estimate.
- Pilot or LLM-judged values are marked as such and never rendered as results.
- Check every query result against the page's own headline figures before showing it. *Why: a result orders of magnitude away from the headline signals a wrong filter or table.* Example: a count reported in the hundreds when the headline says over a million.
- Numbers reconcile with everything already published elsewhere (partner charts, dataset cards, the paper). A conflict is resolved, not captioned.

## Caveats and Footnotes

- No footnotes, no caveat blocks, no methodology parentheticals in captions. *Why: readers skip them, and they make every number look provisional.*
- Cut methodology hedges that soften a number ("<metric> is measured as a floor here"). The number stands on its named basis or it does not belong on the page.
- An essential caveat is one plain sentence at the point of use, or a labelled column left empty.

## Tables

- Complete: every model and every column the reader expects. Name every category in the header, including the residual one ("Unresolved").
- In-cell translucent bars beside each value, proportional to it.
- Row colour encodes the reader's decision categories (planned deployment versus existing baseline).
- An overloaded table is split into two, not given more columns. A confusing table becomes a visual. Explanations under tables are dropped.

# Style Rules

Applies to every visible string on the page: headings, body, tiles, table cells, captions, chart labels, alt text. Global CLAUDE.md prose rules apply on top.

## Standalone

- A stranger with no context understands the page end to end. "it is a self contained entity that any random person reading can understand."
- Strip internal scaffolding: no named colleagues, no funder names in the body, no internal document or file references, no Linear or task ids, no internal table names, no "as discussed", no "outside the CEO's five".
- No process narration and no self-reference: nothing about what is or is not finished, how the page was built, or which version this is. No changelog. "Make it sound like a first version, fresh upload."
- Internal working docs and the published page carry the same facts in different tone. Risky, unflattering, or internal-bug material goes in the working doc only. "this is probably something of a bug for us to fix internally than to show externally."
- Name vendors and models once naming is cleared, never in a bad light. A euphemism for a named competitor hides the comparison the reader came for: "we've confirmed that it is ok to name them, just don't show them in bad light." Ask once if clearance is unknown.
- Do not over-commit to one approach. Show the competing options and the criteria that will decide (accuracy, cost of serving, latency, reliability).
- For senior audiences, drop internal identifiers and collapse an explained subsystem to one box.
- Screen every embedded sample for PII before it ships. Faces, documents, GPS overlays, minors, watermarks.

## Prose Limits

- More than three sentences or about 100 words in one place becomes bullets, a numbered list, a table, or a chart with a one-line caption. "If you're writing more than 3 sentences or 100 words, make it bulleted or convert into a chart or a table with simple captions."
- Every tile is visual or bulleted. Never a descriptive paragraph.
- Bullets open with a bold lead-in. Numbered points for sequences and arguments.
- Skip points that are obvious. "skip unnecessary points that might seem obvious."
- First drafts over-produce; cut to simple visuals, examples, and the main numbers.

## Headings

- Formal noun phrases in Title Case. "Current Pipeline", "Model Comparison", "Serving Cost", "Next Steps".
- Not narrative ("What happens to a photograph today"), not a question, not "X not Y" ("evidence not verdict"), not clever ("Two ways to build it").
- A heading may carry the finding as a noun phrase: "Model Comparison: Different Models, Different Strengths".
- Headings live in the page's type system, outside any visualisation box, consistent across sections.
- Section count for a pre-read or report: four to seven.

## Words

Banned everywhere: em-dashes in any form; arm (for a model or variant), instrument, license (as metaphor), ground (as filler), axes, verdict, "under the rule"; leverage, robust, seamless, delve, unlock, dive into, genuinely, paramount, "it is worth noting"; blast radius, mitigation in flight, force multiplier, fan-out, operationalise. Plain colloquial words for ordinary technical things. "I'm sick of looking at ai generated verbose text for no reason."

Expand every acronym on first use. Define every metric plainly. Quantifiers match the data (8.9% is "sometimes", not "often"). Rename anything a reader might misread, everywhere at once, and keep the author's latest label.

## Numbers

- Every metric carries its calculation basis: denominator, declines or abstentions, the population it is a percentage of. Where two bases exist, name both.
- Prefix approximate values observed on a sample with a tilde.
- Never quote an inflated derived count when a smaller true count is the honest unit ("Candidate rows = 3.29M is a bit misleading").
- Never fabricate a number or an example. A number with no file behind it is flagged, not shown.
- Do not hero-size an unflattering number. Fold it into a normal heading with its qualifier: "28.2% rejected on quality gate before diagnosis runs".
- Withhold numbers that depend on undecided infrastructure. An empty labelled column beats an estimate.
- Pilot or LLM-judged values are marked as such and never rendered as results.
- Numbers reconcile with everything already published elsewhere (partner charts, dataset cards, the paper). A conflict is resolved, not captioned.

## Caveats and Footnotes

- No footnotes, no caveat blocks, no methodology parentheticals in captions. "Remove all of it. none of it is useful." "remove the part in the parentheses. keep it simple."
- Cut methodology hedges that soften a number. One page had "<metric> is measured as a floor here" struck out with "remove this sentence"; the number stands on its named basis or it does not belong on the page.
- An essential caveat is one plain sentence at the point of use, or a labelled column left empty.
- No process disclaimers about unfinished internal work.

## Tables

- Complete: every model, every column the reader expects. Category labels explicit in the header ("'Unresolved' needs to be mentioned else the 3rd category is confusing").
- In-cell translucent bars beside each value, proportional to it.
- Row colour encodes the reader's decision categories (planned deployment versus existing baseline).
- An overloaded table is split into two, not given more columns. A confusing table becomes a visual. Explanations under tables are dropped.

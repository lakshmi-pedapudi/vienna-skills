# Style Rules

Applies to slide text, table cells, chart labels, diagram labels, footnotes, speaker notes, and the markdown draft. Global CLAUDE.md prose rules apply on top: no em-dashes, no AI-tell phrases, plain words over coined labels, formal noun-phrase headings.

## Titles and Subtitles

- Title is the subject of the slide, 1 to 4 plain words: "Current Pipeline", "Image Analysis", "Inference Cost", "Partnerships". The conclusion goes in the body, not the title. This reverses the McKinsey action-title convention on purpose.
- Rejected: "What happens to a photograph today", "Two ways to build it", "Inference cost cut 85% on Region A; remaining language buckets in flight". "'Two ways to build it' is a ridiculous title, change it."
- No questions, no "X not Y" ("evidence not verdict"), no narration of the slide's structure ("One slide for the supervised track, the DPO track, and ..."). The presenter narrates live.
- Subtitles describe substance in one short line, or are removed. If a subtitle can be deleted without losing meaning, delete it.
- Section dividers name the section subject and carry its thesis in one line. Never "Theme 1", never "Themes". Column headers on an overview slide are "Topic" and "Description".
- An eyebrow (small uppercase label above the title) may carry the section or the slide's role ("The job", "Today", "In one slide").
- Headings sit outside the visualisation box, in the deck's type system, consistent across slides.

## Body Text

- Chart or table first. When content is N items of the same shape, it is a table. Bullets only for free-form points or fewer than three parallel items.
- Every bullet opens with a bold lead-in that names the point, then the detail. "**Region A (shipped):** migrated to gpt-4o-mini FT, measurable gains in production."
- Numbered points for a sequence or an argument; a big numeral, a bold lead-in, one line of body.
- Three to five points per slide, each about one line. No paragraph anywhere. "if you're using text, keep it to short numbered/bullet points ... something to follow religiously in presentations."
- Every tile is visual or bulleted, never descriptive. "across all the four tiles, make the content visual or bulleted rather than overly descriptive."
- Do not oversimplify for executives. "the CXOs are patient and smart enough to understand these technical details." Show the mechanism behind a number, not only the number.
- Separate shipped from expected in the wording. Approximate figures carry a tilde. A cost figure says what it covers (API call, hosting, training).
- Quantifier words match the data: 8.9% is "sometimes", not "often".
- Cut methodological parentheticals from captions. Drop explanatory paragraphs under tables. An empty labelled column beats a caveat block.
- Each shipped fact gets one canonical mention. Other slides refer back, they do not restate.

## Words

| Banned | Write instead |
|---|---|
| em-dash (any form) | comma, colon, parentheses, new sentence |
| blast radius | current issues, impact |
| mitigation in flight | proposed enhancements, what we are doing |
| force multiplier | compounding effect, unlocks more work (plain) |
| fan-out | branches into, scales to |
| cohort | group of users |
| surface area | scope, what is exposed |
| operationalise | put into production, ship |
| headline (as noun) | top number, main result |
| Why it matters, Why this matters, What this means | Impact |
| Theme, Theme N | Section, Topic, or the subject itself |
| Risk surface | Optimisation opportunities |
| V2 product pivot | Enhancements |
| arm (for a model or variant) | model, route, path, configuration |
| axes, verdict, "under the rule", instrument, license, ground (filler) | plain description of the thing |
| leverage, robust, seamless, delve, unlock, dive into | specific claim or cut |
| paid service, third-party vendor (once naming is cleared) | the vendor's name, without putting them in a bad light |

Test: would a non-engineer, non-consultant understand this without thinking? If not, rewrite. Define every metric plainly and name its denominator on first use. Expand every architecture or metric acronym on first use, looked up rather than recalled.

Rename anything a reader might misread and rename it everywhere, including inside `.dot` sources ("'Route' is confusing. Call it Path A and Path B."). Whatever label the author chose last stands; do not rename on your own.

## Names, Codes and Sources

- No team member by name on any slide, appendix, chart label, legend, owner column or footer. Only the presenter on the cover. No role attribution either ("the CTO said"). Passive or institutional voice: "the team decided", "the pipeline is built".
- No internal section or topic codes (A1, B1, C5, T2.1, D.3.X), no prompt ids (P02), no Linear or task ids, no internal table or file names on a slide face.
- Source citations live in speaker notes (internal decks) or the appendix, never on the slide face. The presenter cites verbally if asked. No "Cross-link:" footers.
- Once a subsystem has been drawn in detail once, later diagrams collapse it to a single box.
- Name vendors and models concretely once naming is cleared. A euphemism ("the paid outside service", "a fine-tuned open model") hides the comparison the reader came for, and the author has twice asked for the real name in its place and for our own models highlighted against the rest. Ask once if clearance is unknown; do not euphemise by default.

## External Decks

A deck that leaves the organisation is standalone. A reader with zero context gets through it with no other document.

- No names, no role references, no internal process, no past discussions, no references to other documents or unreleased workstreams. Speaker notes are scrubbed too; "can you ensure none of the contents or notes within the ppt contain names like 'rikin', 'vineet' etc."
- A finding that is really an internal bug stays internal. Where data is weak, state the data and stop; do not volunteer the internal reasoning behind a gap.
- Never frame a vendor's shortfall as failure. "don't make it sound like a huge failure on plantix. it is just how predictive systems work."
- Where a comparison is not apples to apples, the slide says so in the wording. One deck had to say "best non-diarized baseline vs best diarized result" because the two numbers came from different pipelines; write the equivalent sentence for whatever the mismatch is.
- Numbers reconcile with everything already published elsewhere, including partner decks and public dataset cards. A conflict is resolved, not captioned.
- Differentiate from what the rest of the room will present; do not lead with generic accuracy percentages if everyone else will.

## Numbers on the Slide

- One hero number per slide, rendered large, only for good news. An unflattering number goes inline at normal size with its qualifier: "28.2% rejected on quality gate before diagnosis runs", not a bare "28.2%" tile.
- Every rate names its base: "of the 384,271 rejected", "on 12,246 test images". Where two bases exist, both are named; never pick one silently.
- Lead with the credited number, put the caveat in a footnote.
- Show our own wins where they exist, and show them fairly.
- Pending and blocked numbers are visible as "pending" with an owner. A slide that silently omits a number reads as finished.
- Numbers that depend on undecided infrastructure (hosting cost before the host is chosen) are TBD, not estimated.

## Speaker Notes

- Sources, denominators, "answer if asked X" prep, and expert detail pushed off the slide face.
- Same word bans and, for external decks, the same no-names rule.
- Do not pre-empt the live narration in a subtitle; the slide carries substance, the presenter carries the story.

## Model and Vendor Naming

- Look model identities up, do not recall them ("The gemma model isn't gemma-3-27B, it is gemma-4-e4B"). Check the current Anthropic model versions before writing them; a deck rules file may pin a version for consistency across slides.
- Fine-tunability, pricing and availability claims carry a date and are verified against the provider page.

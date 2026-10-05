# Style

Applies to: slide text, table cells, chart and diagram labels, footnotes, speaker notes and the markdown draft, on every deck. Any project or user writing rules apply on top.

## Titles and Subtitles

- Title is the subject of the slide, 1 to 4 plain words: "Current Pipeline", "Image Analysis", "Inference Cost", "Partnerships". The conclusion goes in the body, not the title. *Why: the presenter narrates live; a sentence title competes with them.* This deliberately reverses the action-title convention common in consulting decks.
- Rejected shapes: "What happens to a photograph today", "Two ways to build it", "Cost fell 85% in one region; others in progress".
- No questions, no "X not Y" ("evidence not verdict"), no narration of the slide's structure ("One slide each for the three options").
- Subtitles describe substance in one short line, or are removed. If a subtitle can be deleted without losing meaning, delete it.
- Section dividers name the section subject and carry its thesis in one line. Never "Theme 1", never "Themes". Column headers on an overview slide are "Topic" and "Description".
- An eyebrow (small uppercase label above the title) may carry the section or the slide's role ("The job", "Today", "In one slide").
- Headings sit outside the visualisation box, in the deck's type system, consistent across slides.

## Body Text

- Chart or table first. When content is N items of the same shape, it is a table. Bullets only for free-form points or fewer than three parallel items. *Why: a table or chart is read faster than the same content as prose.*
- Every bullet opens with a bold lead-in that names the point, then the detail: "**Region A (shipped):** moved to a smaller fine-tuned model, gains measured in production."
- Numbered points for a sequence or an argument; a big numeral, a bold lead-in, one line of body.
- Up to five points per slide, as many as the content has, each about one line. No paragraph anywhere, and every tile is visual or bulleted, never descriptive.
- Do not oversimplify for senior audiences. *Why: executives are patient and capable with technical detail; show the mechanism behind a number, not only the number.*
- Separate shipped from expected in the wording. Approximate figures carry a tilde. A cost figure says what it covers (API call, hosting, training).
- Quantifier words match the data: 8.9% is "sometimes", not "often".
- Cut methodological parentheticals from captions. Drop explanatory paragraphs under tables. An empty labelled column beats a caveat block.
- Each shipped fact gets one canonical mention. Other slides refer back, they do not restate.

## Sentence Shapes

Rhetorical shapes that read as AI-generated, whatever the wording. The rule targets the shape: rewording a pivot so it sounds less templated does not pass it; restructure the line. Applies to bullets, table cells, captions and speaker notes, not only titles. `check_words.py` does not catch these; they are a self-review item.

- No "not A, but B" pivots: "this is not about X, it is about Y", "we do not X, we Y", "not only X but also Y". State the affirmative point first. If the contrast carries information, frame it as a finding ("the bottleneck turned out to be Y"), not a rebuttal.
- List length matches the content. Two bullets are a complete slide; a third added for rhythm is padding.
- One concrete detail over stacked adjectives: "scales to 10,000 concurrent requests", not "powerful, flexible, scalable".
- No importance preambles or intensifiers: "it is crucial to", "truly", "arguably one of the most important".
- No tagline lines on a slide ("Full stop.", "The receipts do not lie."). Read-aloud test: a line that performs rather than informs is the presenter's to say live, not the slide's to carry.

## Words

The machine-checked lists live in `scripts/house_words.json`; this table is the human-readable version with replacements.

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
| arm (for a model or variant) | model, route, path, configuration |
| axes, verdict, "under the rule", instrument, licence, ground (filler) | plain description of the thing |
| leverage, robust, seamless, delve, unlock, dive into | specific claim or cut |
| paid service, third-party vendor (once naming is cleared) | the vendor's name, without putting them in a bad light |

Test: would a non-engineer, non-consultant understand this without thinking? If not, rewrite. Define every metric plainly and name its denominator on first use; if a metric label still confuses, drop it rather than explain it. Expand every architecture or metric acronym on first use, looked up rather than recalled. Frame a list of risks as optimisation opportunities where that is accurate.

Rename anything a reader might misread, and rename it everywhere, including inside `.dot` sources (a label changed from "Route" to "Path" changes in every diagram too). The label the deck owner chose last stands; do not rename on your own.

## Names, Codes, Sources and Vendors

- No team member by name on any slide, appendix, chart label, legend, owner column or footer. Only the presenter on the cover. No role attribution either ("the CTO said"). Passive or institutional voice: "the team decided", "the pipeline is built".
- No internal section or topic codes (A1, T2.1), no prompt ids (P02), no ticket or task ids, no internal table or file names on a slide face.
- Source citations live in speaker notes (internal decks) or the appendix, never on the slide face. The presenter cites verbally if asked. No "Cross-link:" footers.
- Once a subsystem has been drawn in detail once, later diagrams collapse it to a single box.
- Name vendors and models concretely once naming is cleared, and highlight your own models against the rest. *Why: a euphemism ("the paid outside service", "a fine-tuned open model") hides the comparison the reader came for.* Ask once if clearance is unknown; do not euphemise by default.
- Look model identities up, do not recall them; a version or size recalled from memory is often wrong. Check current model versions before writing them; a deck rules file may pin a version for consistency across slides.
- Fine-tunability, pricing and availability claims carry a date and are verified against the provider page.

## External Decks

A deck that leaves the organisation is standalone. A reader with zero context gets through it with no other document.

- No names, no role references, no internal process, no past discussions, no references to other documents or unreleased workstreams. Speaker notes are scrubbed too. *Why: notes travel with the file.*
- A finding that is really an internal bug stays internal. Where data is weak, state the data and stop; do not volunteer the internal reasoning behind a gap.
- Never frame a vendor's or partner's shortfall as failure; describe it as how such systems behave.
- Where a comparison is not like for like, the slide says so in the wording (e.g. "best baseline vs best result from a different pipeline").
- Numbers reconcile with everything already published elsewhere, including partner decks and public dataset cards. A conflict is resolved, not captioned.
- Differentiate from what the rest of the room will present; do not lead with generic accuracy percentages if everyone else will.

## Numbers on the Slide

- Every target, threshold or claim shows how it was set and where it came from. *Why: senior audiences ask "how did you decide" before anything else.* Bad: "Target: 50% cost reduction". Good: "Target: 50% cost reduction (matches <basis>)", with the derivation in the notes.
- One hero number per slide, rendered large, only for measured, settled good news. Pilot, model-judged or unflattering numbers go inline at normal size with their qualifier. *Why: a large tile reads as a settled result.* Bad: a bare "28%" tile. Good: "28% rejected at intake, before analysis runs".
- Every rate names its base: "of the <N> rejected", "on <N> test images". Where two bases exist, both are named; never pick one silently.
- Lead with the credited number; put its basis in the footnote.
- Show your own wins where they exist, and show them fairly.
- Pending and blocked numbers are visible as "pending" with an owner. A slide that silently omits a number reads as finished.
- Numbers that depend on undecided infrastructure (hosting cost before the host is chosen) are TBD, not estimated.

## Footnotes

- A **basis footnote** (denominator, period, data source in one line) is expected on a content slide that shows numbers. It is part of the slide frame.
- A **caveat footnote** (a limitation, an exclusion, a known gap) appears on at most one slide in a few, and only when the number would mislead without it. *Why: caveats on most slides read as a deck that does not trust itself.* Other caveats go to speaker notes.

## Speaker Notes

- Every content slide has speaker notes. *Why: the slide carries substance, the presenter carries the story, and the notes carry what the presenter needs to defend it.*
- Notes hold sources, denominators, "if asked X, answer Y" prep, caveats moved off the face, and expert detail.
- Same word bans and, for external decks, the same no-names rule.
- Do not pre-empt the live narration in a subtitle.

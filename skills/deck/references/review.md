# Review

Applies to: every round of comments on a deck, self-review before hand-over, review of decks you did not build, and the convergent review loop.

A comment on one slide is usually a style rule for the whole deck, and it lands in three places at once: the rules file, the build script and the deck.

## How Comments Arrive

1. A copy of the deck saved as `<deck>_review.pptx` with a text box per comment, each starting with the agreed reviewer prefix (default `REVIEW:`). Extract with `scripts/extract_review_comments.py <deck>_review.pptx [--prefix "<prefix>:"]`. Notes-pane paragraphs with the prefix are included.
2. Google Slides comments on a shared copy.
3. A numbered list in chat or at the top of the draft markdown. Apply item by item.
4. Reviewer mail relayed by the deck owner, often as Remove and Add lists. Apply literally, item by item, and keep a closure ledger.

## The Cycle

1. Extract every comment with its slide number. Say how many there are.
2. Generalise. Ask of each comment whether it is a rule for every slide (title style, word choice, names, layout) or a fix for one slide. Most are rules. Add each rule to the rules file with the next number; never edit an existing rule's number.
3. Update the build script and rebuild. Run the gate scripts. Open the file.
4. Log the mapping in the rules file: a table per round, `Slide reviewed | Comment summary | Where it landed` (rule number, slide rebuilt, slide dropped with content moved).
5. Report back by slide number with what changed, and list anything not done and why.
6. Archive the previous deck as `_v-N` before overwriting.

Keep a cold-session note at the top of the rules file: do not re-derive style preferences; they are codified as numbered rules.

## Working Agreements During Review

1. **Show the proposed rewrite before editing the live file.** *Why: the deck owner wants to approve the reframe, not discover it.*
2. **In review-only mode, report deviations and make no edits until the deck owner agrees.** *Why: a review pass that edits cannot be compared against the brief.*
3. **Change exactly what was asked.** *Why: unrequested changes elsewhere have to be found and reverted.*
4. **Offer options numbered and stage the risky step separately.** *Why: the deck owner can approve some options and hold others back.*
5. **Do not reorder or merge slides on a review pass.** *Why: reordering is the deck owner's call, made slide by slide, by name.*
6. **Strip rather than delete while a senior reviewer has not yet weighed in.** *Why: a stripped slide can be restored; a deleted one has to be rebuilt.*
7. **Measure a sizing instruction against the result.** *Why: "very compact" means the section occupies visibly less of the page, not one sentence fewer.*
8. **When a list of defects was raised, re-verify each one by id before saying it is fixed.** *Why: reporting a fix without re-checking is the most common review failure.* This is the single home of the re-check rule; other files point here.
9. **Check an independent second review for sense before adopting it.** *Why: one outside review should not pull the deck far from its agreed spine.*

## Self-Review Before Hand-Over

Run these on your own output before the deck owner sees it:

- Every title 1 to 4 plain words. Every bullet has a bold lead-in. No paragraph.
- Table, chart and takeaway on the same slide agree.
- Every number is a registry key with a row set; approximate values carry a tilde; pending values are visible.
- No names, codes, ids, document references, em-dashes or banned words. Notes included for external decks.
- No "not A, but B" pivots, lists padded to three, stacked adjectives, importance preambles or tagline lines in bullets, cells or notes (`style.md` §Sentence Shapes). The word gate does not catch these; read each slide aloud.
- Every content slide has speaker notes; caveat footnotes are rare (`style.md` §Footnotes).
- Overview slide matches the actual contents. Page numbers correct.
- Diagrams: labels fit, nothing overlaps, encodings labelled, no title inside the image.
- The deck opens, every slide renders, the PDF export keeps its layout.
- Audit against the narrative spine: does every slide advance it, and does anything appear before what it depends on?

## Decks You Do Not Own

When a reviewer (a senior leader, a partner or a customer) has edited their own copy, write `REVIEW_NOTES.md` from `templates/REVIEW_NOTES.md` with three buckets: what changed in the new version (numbered, with reasons and file citations for any replaced figure), flags to confirm before it goes external (unverifiable denominators, scope of a chart, coverage claims), and comments already handled with no action. Deliver changes as a slide-level diff they can port by hand, or as a separate addendum file. Examples in a colleague's deck that are not in the data are called out and replaced with verified rows, each cited with its n.

## Rationalisations to Refuse

| Thought | Reality |
|---|---|
| "The title is only five words, close enough" | Cut it to the subject. The body carries the claim. |
| "This paragraph explains it better than bullets" | Three bullets with bold lead-ins, or a table. |
| "I will type this one number, it is in the notes" | Add the registry row. Unknown key must fail the build. |
| "A quick edit in PowerPoint is faster" | Lost on the next rebuild. Edit the script. |
| "The name is only in the speaker notes" | Notes leave with the file. Scrub them. |
| "This tile number is the finding, make it big" | Unflattering or pilot numbers go inline with their qualifier. |
| "I fixed the list, no need to re-check each item" | Working Agreement 8: re-check each item by id. |
| "The build ran, the deck is fine" | Open it. A deck that builds can still have blank slides. |
| "A fresh deck is cleaner than augmenting" | If told to augment, augment. |
| "Reviewer said compact, I trimmed a sentence" | Measure the space. Compact means the section shrinks. |

## Checkpoint Questions

The checkpoint rules (where to stop and ask, and how) live in `workflow.md` §Checkpoint Questions.

## Convergent Review Loop

Fixes break other fixes. Review is a loop, not a pass, and it stops on agreement between passes, not on a feeling of done.

Each pass, in order:

1. Mechanical gates: the gate scripts (word gate, figures check, layout check). Zero failures before reading.
2. Full read, latest to earliest, for logical consistency: the same quantity quoted with two values, a section contradicted by a later one, a stale result after a data refresh.
3. Reference and number check: every citation opens and is necessary; every number resolves to its source file and row set; every derived number has its formula recorded.
4. Regression check: every issue closed in an earlier pass is re-verified, by id, as still closed.
5. New issues introduced by the fixes themselves (a renamed label missed in one place, a table that no longer fits, a figure that moved).

Record each pass in `REVIEW_LOG.md` (`templates/REVIEW_LOG.md`): pass number, findings with id, severity and location, fixes applied, regressions (a prior id reopened), new issues caused by fixes.

Stop rule: run at least two passes. Stop when two successive passes agree: no high-severity finding, no regression, and at most one minor new finding between them. Cap at three passes. If pass 3 still diverges from pass 2, stop patching and report the unstable areas to the deck owner with the log; the document needs a decision, not a fourth pass.

Fresh eyes: run pass 2 and pass 3 in a fresh context (a subagent given only the document, the gates and the log) so the reviewer is not anchored on its own fixes. Where another model is available, use it for one pass. Report closure per item id, never "addressed".

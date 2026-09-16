# Review: Intake, Generalisation, Integration

Review is a loop, not an edit. A comment on one slide is a style rule for the whole deck, and it lands in three places at once: the rules file, the build script, and the deck.

## How Comments Arrive

1. A copy of the deck saved as `<deck>_review.pptx` with a text box per comment, each starting with `Reviewer:`. Extract with `scripts/extract_review_comments.py <deck>_review.pptx`. Notes-pane comments are included.
2. Google Slides comments on a shared copy.
3. A numbered list in chat or at the top of the draft markdown (the VLM `FINAL_DRAFT_reviewed.md` opened with 19 numbered comments). Apply item by item.
4. Reviewer mail relayed by the author, often as Remove and Add lists. Apply literally, item by item, and keep a closure ledger.

## The Cycle

1. Extract every comment with its slide number. Say how many there are.
2. Generalise. Ask of each comment whether it is a rule for every slide (title style, word choice, names, layout) or a fix for one slide. Most are rules. Add each rule to the rules file with the next number; never edit an existing rule's number.
3. Update the build script and rebuild. Run the three checkers. Open the file.
4. Log the mapping in the rules file: a table per round, `Slide reviewed | Comment summary | Where it landed` (rule number, slide rebuilt, slide dropped with content moved).
5. Report back by slide number with what changed, and list anything not done and why.
6. Archive the previous deck as `_v-N` before overwriting.

Three board rounds produced 25 numbered rules this way. The cold-session protocol at the top of that rules file says: do not re-derive style preferences; they are codified with rule numbers.

## Working Agreements During Review

- Show the proposed rewrite before editing. "cut this short. make it concise and skip unnecessary points that might seem obvious. give me the reframe first before updating directly."
- Review mode means report deviations only, no edits, until agreement. "review the artifact again. don't make any edits before I agree ... just tell me the deviations."
- Change exactly what was asked. "only change what I'm telling you to, pls don't touch anything else."
- Offer options numbered; the author picks ("Do 1 and 2. Don't do 3."). Stage the risky step separately.
- Reordering and merging is done slide by slide, by name, by the author. Do not reorder on a review-only pass.
- Strip rather than delete when a senior reviewer has not weighed in yet: "I would keep a stripped version for now. to be cut out completely only if rikin reviews and asks for it to be cut out."
- Measure a sizing instruction against the result. When a reviewer said "very compact", the section must occupy less of the page.
- When a list of defects was raised, confirm each is fixed before saying so. "#1 ... not fixed. #2 ... not fixed." is the failure to avoid.
- Independent second reviews are checked for sense before adoption: "Check if these comments make sense meaningfully. Don't deviate too far based on just this review."

## Self-Review Before Hand-Over

Run these on your own output before the author sees it:

- Every title 1 to 4 plain words. Every bullet has a bold lead-in. No paragraph.
- Table, chart and takeaway on the same slide agree.
- Every number is a registry key with a row set; approximate values carry a tilde; pending values are visible.
- No names, codes, ids, document references, em-dashes, banned words. Notes included for external decks.
- Overview slide matches the actual contents. Page numbers correct.
- Diagrams: labels fit, nothing overlaps, encodings labelled, no title inside the image.
- The deck opens, every slide renders, the PDF export keeps its layout.
- Audit against the narrative spine: does every slide advance it, and does anything appear before what it depends on?

## Decks You Do Not Own

When a reviewer (the CEO, a partner) has edited their own copy, write `REVIEW_NOTES.md` from `templates/REVIEW_NOTES.md` with three buckets: what changed in the new version (numbered, with reasons and file citations for any replaced figure), flags to confirm before it goes external (unverifiable denominators, scope of a chart, coverage claims), and comments already handled with no action. Deliver changes as a slide-level diff they can port by hand, or as a separate addendum file. Fabricated examples in a colleague's deck are called out and replaced with verified rows, each cited with its n.

## Rationalizations to Refuse

| Thought | Reality |
|---|---|
| "The title is only five words, close enough" | Cut it to the subject. The body carries the claim. |
| "This paragraph explains it better than bullets" | Three bullets with bold lead-ins, or a table. |
| "I will type this one number, it is in the notes" | Add the registry row. Unknown key must fail the build. |
| "A quick edit in PowerPoint is faster" | Lost on the next rebuild. Edit the script. |
| "The name is only in the speaker notes" | Notes leave with the file. Scrub them. |
| "This tile number is the finding, make it big" | Unflattering numbers go inline with their qualifier. |
| "I fixed the list, no need to re-check each item" | Re-check each item. It was reported unfixed five times in one message. |
| "The build ran, the deck is fine" | Open it. Blank slides shipped twice. |
| "A fresh deck is cleaner than augmenting" | If told to augment, augment. |
| "Reviewer said compact, I trimmed a sentence" | Measure the space. Compact means the section shrinks. |

## Checkpoint Questions

Even in bypass-permissions or autonomous mode, stop at these points and ask with the AskUserQuestion tool. The author wants to give simple inputs, not read a plan.

- Checkpoint 1, topic segregation: the proposed themes and topics (the `topics/<slug>.md` set) before the files are created, and again when a topic is declared saturated ("move on, fill gaps, or park?").
- Checkpoint 2, skeleton: sections, slide budget, appendix split, and the sub-tasks that get their own subagent, before any build.
- Checkpoint 3, narrative spine: the one-line story the deck tells and the two or three hero numbers, before the draft.
- Checkpoint 4, before any restructure, merge, drop, or reorder of slides, and before a fresh rebuild replaces an existing deck.

Rules: one question per checkpoint, two at most; two to four options with the recommended one first and marked; free text always possible. Do not ask elsewhere; routine choices (chart form, wording, layout) are made and reported. Do not re-ask what was confirmed; a later round may revise it.

## Convergent Review Loop

Fixes break other fixes. Review is a loop, not a pass, and it stops on agreement between passes, not on a feeling of done.

Each pass, in order:

1. Mechanical gates: the skill's scripts (style or word gate, figure or citation check, layout check). Zero failures before reading.
2. Full read, latest to earliest, for logical consistency: the same quantity quoted with two values, a section contradicted by a later one, a stale result after a data refresh.
3. Reference and number check: every citation opens and is necessary; every number resolves to its source file and row set; every derived number has its formula recorded.
4. Regression check: every issue closed in an earlier pass is re-verified, by id, as still closed.
5. New issues introduced by the fixes themselves (a renamed label missed in one place, a table that no longer fits, a figure that moved).

Record each pass in `REVIEW_LOG.md` (`templates/REVIEW_LOG.md`): pass number, findings with id, severity and location, fixes applied, regressions (a prior id reopened), new issues caused by fixes.

Stop rule: run at least two passes. Stop when two successive passes agree: no high-severity finding, no regression, and at most one minor new finding between them. Cap at three passes. If pass 3 still diverges from pass 2, stop patching, and report the unstable areas to the author with the log; the document needs a decision, not a fourth pass.

Fresh eyes: run pass 2 and pass 3 in a fresh context (a subagent given only the document, the gates, and the log) so the reviewer is not anchored on its own fixes. Where a second model is available (Codex), use it for one pass. Report closure per item id, never "addressed".

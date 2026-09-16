# Review: Loop, Checkpoints, Working Agreements

Review intake and working agreements live in `workflow.md` §3. This file holds the checkpoint questions and the convergent review loop.

## Checkpoint Questions

Even in bypass-permissions or autonomous mode, stop at these points and ask with the AskUserQuestion tool. The author wants to give simple inputs, not read a plan.

- Checkpoint 1, section segregation: the proposed section list (four to seven for a pre-read or report) with the source behind each, before the empty canvas is published.
- Checkpoint 2, atomic elements: which sections become their own build step or subagent task, and the visual form for any load-bearing element (offer two or three chart or diagram options, numbered).
- Checkpoint 3, rough themes: the takeaway line per section and the modality or category palette, before filling.
- Checkpoint 4, before any restructure, staging trial, slide split, or fresh artifact at a new URL.

Rules: one question per checkpoint, two at most; two to four options with the recommended one first and marked; free text always possible. Do not ask elsewhere; routine choices are made and reported. Do not re-ask what was confirmed; a later round may revise it.

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

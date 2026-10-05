# Review Loop and Checkpoints

Applies to: the questions asked at fixed checkpoints during a build, and the convergent review loop run before publishing. Review intake rules (deviations only, itemised approval, change only what was asked) live in `references/workflow.md` §3.

## Checkpoint Questions

Even in bypass-permissions or autonomous mode, stop at these points and ask with the AskUserQuestion tool. *Why: the author can answer a short choice quickly and well, but a long plan gets skimmed.*

- Checkpoint 1, section segregation: the proposed section list (four to seven for a pre-read or report) with the source behind each, before the empty canvas is published.
- Checkpoint 2, atomic elements: which sections become their own build step or subagent task, and the visual form for any load-bearing element (offer two or three numbered chart or diagram options).
- Checkpoint 3, rough themes: the takeaway line per section and the category palette, before filling.
- Checkpoint 4: before any restructure, staging trial, slide split, or fresh artifact at a new URL.

Rules: one question per checkpoint, two at most; two to four options with the recommended one first and marked; free text always possible. Do not ask elsewhere; make routine choices and report them. Do not re-ask what was confirmed; a later round may revise it.

## Convergent Review Loop

Fixes break other fixes. Review is a loop, and it stops when passes agree, not when it feels done.

Each pass, in order:

1. Mechanical gate: `scripts/check_html.py` with zero failures before reading. Resolve or justify every warning, including each pivot warning. Then a read-aloud pass for the sentence shapes in `references/style.md` §Sentence Shapes (pivots, padded lists of three, stacked adjectives, taglines and pull quotes, recap endings).
2. Full read, latest section to earliest, for logical consistency: the same quantity quoted with two values, a section contradicted by a later one, a stale result after a data refresh.
3. Reference and number check: every link opens and is necessary; every number resolves to its source file and row set; every derived number has its formula recorded.
4. Render check: open the live page; every section renders, every image shows, no diagram labels overlap, the PDF keeps tile rows intact.
5. Regression check: every issue closed in an earlier pass is re-verified, by id, as still closed.
6. New issues introduced by the fixes themselves (a renamed label missed in one place, a table that no longer fits, a figure that moved).

Record each pass in `REVIEW_LOG.md` (`templates/REVIEW_LOG.md`): pass number, findings with id, severity and location, fixes applied, regressions (a prior id reopened), new issues caused by fixes.

Stop rule: run at least two passes. Stop when two successive passes agree: no high-severity finding, no regression, and at most one minor new finding between them. Cap at three passes. If pass 3 still diverges from pass 2, stop patching and report the unstable areas to the author with the log; the document needs a decision, not a fourth pass.

Fresh eyes: run passes 2 and 3 in a fresh context (a subagent given only the document, the gate and the log) so the reviewer is not anchored on its own fixes. Where a second model is available, use it for one pass. Report closure per item id, never "addressed".

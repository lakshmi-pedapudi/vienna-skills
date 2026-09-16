# Review Protocol

Reviews are separate passes, each with one objective, each producing a written file the author can re-run against the current source. Findings are diagnosed first; edits follow approval or an explicit "fix what you can".

## The Critical Review Prompt

Used verbatim more than ten times across the published papers. Run it as written when the author says "proof read", "critical review", or "be ruthless":

> Proof read the entire paper. Be a very critical reviewer. Identify, investigate any indications that this paper might have been written using an AI tool or coding agent. Patterns like em-dashes or weird vocabulary that a normal person might not use, should all be identified and fixed. Look for structural inconsistencies, or factual inaccuracies. Be ruthless. Give a critical review as to what fixes need to be in place for this paper before it is published. Be especially careful with the references section. ensure there are no fabricated references or citations. flag everything that looks suspicious. Also review if there are any hyperbolic claims that are unsupported.

Variants the author appended: name the paper's core components and flag content that strays from them, check whether the structure would benefit from realignment around that core, remove unnecessary citations, and identify trimming to reach a page target ("don't be too strict, this is a good to have").

## Review Passes

Run the pass the author asks for. When asked for a full review, run them in this order and write one file.

1. **AI-tell and prose pass.** Em-dashes, banned words, coined labels, "X not Y" headings, claim-then-hedge, repeated vocabulary density ("expert-curated appears 10+ times"), named-problem headings, footnote padding, self-reference. Output: Location | Phrase | Issue | Suggested Fix table.
2. **Claims versus evidence.** Every claim in abstract, discussion, and conclusion traced to a table or a citation. Numbers that exist only in prose are flagged as unverifiable. Hyperbole rewritten to the qualified sentence. Check the scope statement: what the method does not replace.
3. **Tabulated results versus source records.** For every table cell, find at least one supporting file in `materials/` or `results/`. Missing support is flagged for manual review, never guessed. Check: same sample set across models, abstentions shown, denominators stated, rounding consistent across tables, bold convention obeyed, cost dates postdate the models, model names exist.
4. **Internal consistency.** Text against table against support matrix; counts that appear in several places (number of models, clips, rows) agree; naming consistent; figure and table numbers referenced in order and placed near their sections; superseded numbers absent; route or module labels match their definition table.
5. **Citation audit.** For each reference: exists (open it, Crossref or arXiv), is cited, is needed, is used in the right context, is the right paper for the model named (Llama 3 is not the Llama 2 paper). Orphan references removed. Redundant references pruned. Output: `citation_verification.csv` with Citation Key, Title, First Author, Year, Venue, Verification Status, Source URL, Discrepancies, Notes; plus a confidence-tiered list of what the author must check manually. No `% TODO: verify` survives in the bib.
6. **Objectives check.** Read the planning brief (`whitepaper_prompt.md`, `PAPER_UPDATE_GUIDE.md`, the skeleton) and confirm each stated objective, required visualization, and critical constraint is met in the source.
7. **Structure and flow.** Dependency order, related concepts before the methodology that uses them, figures adjacent to first reference, section weight versus importance, duplicates to merge.
8. **Trimming plan** (only when a page target exists). Each item with location, what goes, page saving, and impact rank. Executed only after approval, reversible item by item.
9. **Similarity and self-citation.** Web search for suspiciously close papers; check that the group's prior papers are cited; verify author identities where a reader would.
10. **De-internalize.** No internal names, task ids, internal file paths, internal table names, "v1" labels, or references to discussions outside the document. Also no reviewer bookkeeping in the body: status columns, "Answered in" / "Responds to" columns, superseded-number history, dated audit names in captions, two-denominator conflict framings, "not located" / "not reproducible" wording, `\todo` / `\flag` markers, or a reconciliation appendix. Move each to `CRITICAL_REVIEW.md` and state the gap once in reader-facing words (`references/structure.md`, Reader-Facing Rule).

## CRITICAL_REVIEW.md Format

Template in `templates/CRITICAL_REVIEW.md`. Shape used since the first published paper:

- Header: date, reviewed version, previous review date.
- Status Summary table: Fixed | Remaining High | Medium | Low | New.
- Section I: items fixed since the last review, each with location and a check.
- Section II: remaining items grouped HIGH / MEDIUM / LOW, each tagged `[STILL OPEN]` or `[STILL OPEN, NEW]`, with Location (file, line, table), description, and a Fix line.
- Section III: priority table restating everything.

The markdown file is the tracker. On re-review, replace it with the current state rather than appending. The author asks "verify all items marked high are addressed" and then "how about medium"; the file must answer both.

## Fix Loop

- "Fix what you can, and give me the list of fixes I need to implement manually." Apply mechanical fixes (punctuation, banned words, orphan refs, numbering, placement) directly. Leave judgement calls (drop a model, reframe a claim, change author order) as a numbered list of questions.
- "Ask me detailed questions about the items you skipped." Skipped items get one concrete question each, with a recommended answer.
- After fixes, re-run the relevant pass and report closure per item, not a general "addressed".

## Second-Model and External Reviews

- Codex or another agent reviews the artifact and the LaTeX. Write to survive it. When a Codex review file exists (`codex_critical_review.md`), address it item by item with file and line references and say which items were rejected and why.
- A stakeholder's comments (for example the CEO's numbered comments on a deck or paper) become a closure ledger: each comment, its status, where it was applied. Diff their edited version against ours before redoing anything they already fixed.
- An independent review the author pastes in is advisory: adopt what holds, argue what does not, do not swing the draft around one review.
- Reviewing a neighbouring paper (a colleague's draft) means deconstructing it, locating the novelty, listing omissions, and giving a verdict (separate paper versus merge), then re-testing its hypotheses on our own data where possible.

## Reconciliation Passes

When findings have accumulated across sessions: reconcile the whole document, plan, and findings files from latest to oldest so late findings win. Check for logical inconsistencies across all three, not just the draft. Report deviations before editing.

## Suspicion Rules

- A too-good number is a defect until explained. Look for label leakage, oracle hints in prompts, warm-start contamination, test rows in training data, reference labels that are the baseline's own output.
- Identical metrics across two supposedly independent models means a data-processing error, not a coincidence.
- A model present in the data but absent from the paper needs a stated reason.
- Numbers the author "knows" (about 100k samples, 16 languages) beat pipeline totals; when they disagree, find the duplication.
- Distinguish suspicion from proof in writing: "cannot be proven without the full training run" is a legitimate sentence in a flag.

## Checkpoint Questions

Even in bypass-permissions or autonomous mode, stop at these points and ask with the AskUserQuestion tool. The author wants to give simple inputs, not read a plan.

- Checkpoint 1, materials segregation: the proposed thematic folders (`01_background`, `02_pipeline`, ...) before any folder is created or filled.
- Checkpoint 2, skeleton: the section list with mapped sources, plus the length target and any budget ("50% data, 50% methodology"), before drafting.
- Checkpoint 3, rough themes: the two or three claims the paper will make and the figures that carry them.
- Checkpoint 4, before any restructure, trim plan, merge or cut of a whole section, or a change of skeleton.

Rules: one question per checkpoint, two at most; two to four options with the recommended one first and marked; free text always possible. Do not ask elsewhere; routine choices are made and reported. Do not re-ask what was confirmed; a later round may revise it.

## Convergent Review Loop

Fixes break other fixes. Review is a loop, not a pass, and it stops on agreement between passes, not on a feeling of done.

Each pass, in order:

1. Mechanical gates: the skill's scripts (style or word gate, figure or citation check, layout check). Zero failures before reading.
2. Full read, latest to earliest, for logical consistency: the same quantity quoted with two values, a section contradicted by a later one, a stale result after a data refresh.
3. Reference and number check: every citation opens and is necessary; every number resolves to its source file and row set; every derived number has its formula recorded. Number placement: result values appear in the four homes (Abstract, Introduction, Results, Conclusion) with one rounding and one basis, nowhere else in prose; captions and `.dot` labels carry no result values; every chart is newer than the CSV it draws from. `scripts/check_number_placement.py` is the gate for this step.
4. Regression check: every issue closed in an earlier pass is re-verified, by id, as still closed.
5. New issues introduced by the fixes themselves (a renamed label missed in one place, a table that no longer fits, a figure that moved).

Record each pass in `REVIEW_LOG.md` (`templates/REVIEW_LOG.md`): pass number, findings with id, severity and location, fixes applied, regressions (a prior id reopened), new issues caused by fixes.

Stop rule: run at least two passes. Stop when two successive passes agree: no high-severity finding, no regression, and at most one minor new finding between them. Cap at three passes. If pass 3 still diverges from pass 2, stop patching, and report the unstable areas to the author with the log; the document needs a decision, not a fourth pass.

Fresh eyes: run pass 2 and pass 3 in a fresh context (a subagent given only the document, the gates, and the log) so the reviewer is not anchored on its own fixes. Where a second model is available (Codex), use it for one pass. Report closure per item id, never "addressed".

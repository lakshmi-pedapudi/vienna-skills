# Review

Applies to: every review of a paper draft or artifact, from a single proofread to the full convergent loop, including reviews by a second model or by reviewers outside the team.

Reviews are separate passes, each with one objective, each producing a written file the author can re-run against the current source. Findings are diagnosed first; edits follow approval or an explicit "fix what you can".

## The Critical Review Prompt

A reusable prompt. Run it as written when the author asks for a proofread, a critical review, or a ruthless review:

> Proofread the entire paper. Be a very critical reviewer. Identify and investigate any indication that this paper was written with an AI tool or coding agent: patterns such as em-dashes, or vocabulary a normal person would not use, should all be identified and fixed. Look for structural inconsistencies and factual inaccuracies. Be ruthless. Give a critical review of the fixes this paper needs before it is published. Be especially careful with the references section: ensure there are no fabricated references or citations, and flag everything that looks suspicious. Also check for hyperbolic claims that are unsupported.

Optional additions: name the paper's core components and flag content that strays from them; check whether the structure would benefit from realignment around that core; remove unnecessary citations; identify trimming toward a page target (a soft target unless the author says otherwise).

## Review Passes

Run the pass the author asks for. When asked for a full review, run them in this order and write one file. Inside the convergent loop below, passes 1 to 10 are the content of loop steps 2 and 3; the loop adds the gates, the regression check and the stop rule around them.

1. **AI-tell and prose pass.** Em-dashes, banned words, coined labels, "X not Y" headings, claim-then-hedge, repeated vocabulary density (one term repeated ten or more times), named-problem headings, footnote padding, self-reference. Then the sentence shapes no script fully catches (`style.md`, Sentence Shapes): "not A, but B" pivots in body text (review every `check_style.sh` warning), lists padded to three, stacked adjectives, importance preambles, a tagline closing the Abstract or Conclusion (read aloud), recap endings on body sections, narrated structure. Output: Location | Phrase | Issue | Suggested Fix table.
2. **Claims versus evidence.** Every claim in the Abstract, Discussion and Conclusion traced to a table or a citation. Numbers that exist only in prose are flagged as unverifiable. Hyperbole rewritten to the qualified sentence. Check the scope statement: what the method does not replace. Check every "system X provides no Y" claim (no confidence value, no breakdown) against a real captured response before it stands. *Why: a coarse signal (a word-level likelihood, a category label) is easy to miss in a large payload, and it makes the flat claim false.*
3. **Tabulated results versus source records.** For every table cell, find at least one supporting file in `materials/` or `results/`. Missing support is flagged for manual review, never guessed. Check: same sample set across models, abstentions shown, denominators stated, rounding consistent across tables, bold convention obeyed, cost dates postdate the models, model names exist and the exact version string matches the run configuration rather than memory.
4. **Internal consistency.** Text against table against support matrix; counts that appear in several places (number of models, items, rows) agree; naming consistent; figure and table numbers referenced in order and placed near their sections; superseded numbers absent; route or module labels match their definition table. Aim part of this pass at twins: list every claim, label and exclusion reason stated more than once and check each group agrees; then close the class by measurement with a number-level diff between the paper and the artifact over every results cell and row count. *Why: a fix applied to one copy and not its twin is the most common defect across passes, and the diff finds reverse twins (content cut from the paper but still on the page) that no reader raises.*
5. **Citation audit.** For each reference: exists (open it via Crossref, arXiv or the publisher), is cited, is needed, is used in the right context, is the right paper for the model named (Llama 3 is not the Llama 2 paper). When a project has no paper, cite its website rather than inventing a publication. Orphan references removed. Redundant references pruned. Output: `citation_verification.csv` with Citation Key, Title, First Author, Year, Venue, Verification Status, Source URL, Discrepancies, Notes; plus a confidence-tiered list of what the author must check manually. No `% TODO: verify` survives in the bib.
6. **Objectives check.** Read the planning brief (the author's brief, `PAPER_UPDATE_GUIDE.md`, the skeleton) and confirm each stated objective, required visualisation and critical constraint is met in the source.
7. **Structure and flow.** Dependency order, related concepts before the methodology that uses them, figures adjacent to first reference, section weight versus importance, duplicates to merge. A sentence that forward-references a design decision from inside a description of the existing system is cut, not moved earlier; the section that owns the decision already introduces it.
8. **Trimming plan** (only when a page target exists). Each item with location, what goes, page saving and impact rank. Executed only after approval, reversible item by item (`workflow.md`, Page Reduction).
9. **Similarity and self-citation.** Web search for suspiciously close papers; check that the organisation's own relevant prior papers are cited; verify author identities where a reader would.
10. **De-internalise.** No internal names, task ids, internal file paths, internal table names, "v1" labels, or references to discussions outside the document. Also no reviewer bookkeeping in the body: status columns, "Answered in" / "Responds to" columns, superseded-number history, dated audit names in captions, two-denominator conflict framings, "not located" / "not reproducible" wording, `\todo` / `\flag` markers. Move each to the reconciliation register in `CRITICAL_REVIEW.md` and state the gap once in reader-facing words (`structure.md`, Reader-Facing Rule).

## CRITICAL_REVIEW.md Format

Template in `templates/CRITICAL_REVIEW.md`:

- Header: date, reviewed version, previous review date.
- Status Summary table: Fixed | Remaining High | Medium | Low | New.
- Section I: items fixed since the last review, each with location and a check.
- Section II: remaining items grouped HIGH / MEDIUM / LOW, each tagged `[STILL OPEN]` or `[STILL OPEN, NEW]`, with Location (file, line, table), description, and a Fix line.
- Section III onwards: AI-writing signals, reference audit, priority table, reconciliation register, questions for the author.

The markdown file is the tracker. On re-review, replace it with the current state rather than appending. It must answer both "are all high items addressed?" and "what about medium?" at a glance.

## Fix Loop

- When the author asks to fix what can be fixed: apply mechanical fixes (punctuation, banned words, orphan references, numbering, placement) directly. Leave judgement calls (drop a model, reframe a claim, change author order) as a numbered list of questions.
- Every skipped item gets one concrete question with a recommended answer.
- After fixes, re-run the relevant pass and report closure per item, not a general "addressed".

## Second-Model and External Reviews

- A second model or agent reviews the artifact and the LaTeX. Write to survive it. When its review file exists (`<reviewer>_critical_review.md`), address it item by item with file and line references and say which items were rejected and why.
- A stakeholder's numbered comments on a deck or paper become a closure ledger: each comment, its status, where it was applied. Diff their edited version against ours before redoing anything they already fixed.
- An independent review the author pastes in is advisory: adopt what holds, argue what does not, and do not swing the draft around one review. *Why: a single reviewer's priorities are not the paper's.*
- Reviewing a neighbouring paper (a colleague's draft) means deconstructing it, locating the novelty, listing omissions, and giving a recommendation (separate paper versus merge), then re-testing its hypotheses on our own data where possible.

## Reconciliation Passes

When findings have accumulated across sessions: reconcile the whole document, plan and findings files from latest to oldest so late findings win. Check for logical inconsistencies across all three, not just the draft. Report deviations before editing.

## Suspicion Rules

- A too-good number is a defect until explained. Look for label leakage, oracle hints in prompts, warm-start contamination, test rows in training data, reference labels that are the baseline's own output.
- A comparison contaminated by leaked reference data (the reference supplied at inference, test rows in training) is retracted, not caveated. *Why: a caveat leaves a number in the paper that measures nothing.*
- Identical metrics across two supposedly independent models mean a data-processing error, not a coincidence.
- A model present in the data but absent from the paper needs a stated reason.
- Numbers the author knows (approximate corpus size, number of languages) beat pipeline totals; when they disagree, find the duplication.
- Before publishing a comparison, list each system's predicted labels that never match any reference label, and check the row-level correspondence. A prediction that meets one reference value on nearly every row is a spelling difference, not a mistake. *Why: a duplicated class name in the label list can outweigh any real model difference.*
- Merging duplicate label classes is a correction to the label list: apply it to every system and re-run all of them. Crediting an answer one level coarser than the reference is leniency; keep the two apart and state which was chosen. *Why: leniency favours models that hedge over a baseline that commits.*
- Before scoring a predictions file from a collaborator, reproduce the collaborator's own reported figures. A perfect score usually means the field mapping is wrong (gold labels scored against gold labels).
- Verify a collaborator's data claim (split integrity, row counts) rather than quoting it, and verify your own download is complete before contradicting their document. *Why: a truncated local copy can parse without error and look like their mistake.*
- Distinguish suspicion from proof in writing: "cannot be proven without the full training run" is a legitimate sentence in a flag.

## Checkpoint Questions

Defined in `workflow.md`, Checkpoint Questions. A review that proposes a restructure, trim plan, merge or whole-section cut hits Checkpoint 4 before any edit.

## Convergent Review Loop

Fixes break other fixes. Review is a loop, not a pass, and it stops on agreement between passes, not on a feeling of done.

Each pass, in order:

1. Mechanical gates: `scripts/check_style.sh` and `scripts/check_number_placement.py`, plus any figure, citation or layout checks the paper has. Zero failures before reading.
2. Full read, latest to earliest, for logical consistency: the same quantity quoted with two values, a section contradicted by a later one, a stale result after a data refresh.
3. Reference and number check: every citation opens and is necessary; every number resolves to its source file and row set; every derived number has its formula recorded; number placement follows `style.md`, Where Numbers Live.
4. Regression check: every issue closed in an earlier pass is re-verified, by id, as still closed.
5. New issues introduced by the fixes themselves (a renamed label missed in one place, a table that no longer fits, a figure that moved).

Record each pass in `REVIEW_LOG.md` (`templates/REVIEW_LOG.md`): pass number, findings with id, severity and location, fixes applied, regressions (a prior id reopened), new issues caused by fixes.

Stop rule: run at least two passes. Stop when two successive passes agree: no high-severity finding, no regression, and at most one minor new finding between them. Cap at three passes. If pass 3 still diverges from pass 2, stop patching and report the unstable areas to the author with the log; the document needs a decision, not a fourth pass.

Fresh eyes: run pass 2 and pass 3 in a fresh context (a subagent given only the document, the gates and the log) so the reviewer is not anchored on its own fixes. Where a second model is available, use it for one pass. Report closure per item id, never "addressed".

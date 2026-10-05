# Structure

Applies to: the section skeleton, appendices, the reconciliation register, reader-facing wording, draft markers and id naming for any paper built with this skill.

## Canonical Skeleton

A starting skeleton for an applied-ML system paper (a production pipeline, its failures, a proposed redesign, and its evaluation). When the author supplies a skeleton, use it verbatim, numbering included. Otherwise start here and trim; a benchmark or method paper drops the sections it does not need.

```
Abstract              Problem / Key Challenges / Proposed Approach / Evaluation / Main Results [TO BE FILLED]
1 Introduction        1.1 Motivation  1.2 Problem Statement  1.3 Research Questions (RQ1..RQn)  1.4 Contributions
2 Existing System and Baselines
                      2.1 Production pipeline today  2.2 Existing-System Limitations
                      2.3 Baselines (B0 production, B1 general-purpose model, B2/B3 proposed routes or ablated pipeline)
                      2.4 Related Work (folded here, not a standalone section)
3 Production Failure Analysis
                      per failure class, each quantified from production data; funnel by segment; human-review yield
4 Design Principles and Architecture
                      P1..Pn as short imperative statements; architecture figure; configuration table
5..k Modules          one section per stage (M0 input gate, M1 ..., M2 ...), each: role, candidates, metrics, chosen design
k+1 Alternative Design Strategies / Routes
                      Route A versus Route B, or fine-tune versus wrap; what each adds or removes
k+2 Data Curation     human curation, synthetic curation, panel labelling; each with a figure
k+3 Experimental Methodology
                      dataset splits, scoring rule, pipeline configurations table, metrics by stage, ablation plan, run plan
k+4 Results           headline table; component-level (E1..En); end-to-end; error analysis; cost, latency, quality; ablations
k+5 Discussion        key findings; generalisability; what the fix does not replace
k+6 Impact            production rollout metrics [TO BE FILLED until measured]
k+7 Limitations and Future Work
                      includes release plan for data and code
k+8 Conclusion
References
Appendix A  Source Index
Appendix B onwards  Prompt templates with worked examples, detailed per-slice tables (per segment, per class, per language)
```

Conventions inside the skeleton:
- Result values live in four homes; see `style.md`, Where Numbers Live.
- Research questions are numbered and each is answered explicitly in Results or Discussion.
- Contributions are a numbered list; datasets and code releases appear there with links once live, written as done rather than planned.
- Each contribution bullet is at most 15 words and carries no section numbers. *Why: a contribution is a claim, not a map; the reader finds the section from the headings.*
- Baselines, principles, modules, routes, configurations and experiments carry short ids (B0, P1, M0, S1, E1) defined once in a table (`style.md`, Naming Consistency).
- Every table is followed by a short paragraph that reads the numbers and names the takeaway.
- Subsection titles reuse the paper's own category names (`style.md`, Headings and Numbering).
- An Error Analysis subsection exists in every Results section. Its load-bearing figure is the error distribution across the categories the domain cares about, whatever the modality.
- Cost, latency and deployability sit beside accuracy in the results, not in an afterthought.
- Human review or expert evaluation gets its own subsection, with the study design stated plainly (blind test, n questions, k experts, preference counts) and no sensationalised percentage.
- Concepts a method depends on (evaluation platform, curated data) appear before the Methodology section that uses them.
- Limitations is a per-paper decision recorded in the status memory: either a Limitations section, or Future Work only. Under Future Work only, each load-bearing caveat moves next to the result it qualifies, in one sentence, rather than being collected into a section that reads as a list of weaknesses. Nothing load-bearing is dropped in the move.
- A table whose only job is to explain a metric, or to repeat a comparison the paper already made, moves to an appendix. If the paper has no appendix, cut it or demote it to bullets. *Why: it adds confusion in the body and nothing the reader needs.*
- A dependency that is not part of the argument (a third-party service, a preprocessing tool) gets a footnote, not a subsection. *Why: a subsection signals importance the dependency does not have.*
- Open-source contributions are a release-plan paragraph inside Limitations and Future Work (or Contributions once live), not a standalone section.
- A Disclosure paragraph closes a paper that benchmarks commercial systems: the authors' employer, and no financial relationship with the evaluated vendors.

## Appendix A: Source Index

"Every raw dataset behind a number in this paper, so an aggregate can be re-derived rather than re-quoted."

Two tables:
1. Internal documents, chats, call notes: Source | Type | Owner | Updated | Feeds (sections).
2. Row-level data: Dataset | Location | Rows | Backs (sections and table numbers). In the external PDF, Location is a description plus basename; repository paths and bucket names stay in the tracker.

Caption: "Reconcile against these, not against summary documents." File names containing banned stems are allowed only here.

## Reconciliation Register (internal; never in the external PDF)

Lives in its own section of `CRITICAL_REVIEW.md` and in the status memory, never in the `.tex`. *Why: internal conflicts matter to internal reviewers, not to external readers trying to understand the approach.* A bullet list, one bold lead-in per flag, of every unresolved item:
- Superseded row sets with the superseded numbers spelled out and "must not be reused".
- Files referenced but not located; filters that could not be reproduced.
- Confounds with a pending re-run (label leakage, warm-start checkpoint, oracle hints in prompts).
- Source-paper internal inconsistencies and which value this draft quotes.
- Denominator mismatches between sources.
- Pilot sample sizes for every `\pilot` number.
- Provisional author order with its deadline.

Nothing is silently filled. A gap in the paper is stated once, in reader-facing words, and points at nothing outside the document.

## Reader-Facing Rule

The version being published reads as finished. The external PDF carries none of the following; each is fine in the skeleton, the artifact draft stage and the tracker:
- Pending language: "not yet measured", "pending", "prepared for release". A measurement still to come is a Future Work line in the future tense. *Why: in a published version, pending wording reads as unfinished work.*
- Any mention of a personal-information review, anonymisation pass or PII screening. The release repository handles it. *Why: naming the process raises a question the paper does not answer.*
- Status columns: "Measured", "Not run", "Not started", "In progress", "In this draft: Yes / No / Partly".
- Cross-reference columns: "Answered in", "Responds to", "Where reported".
- Superseded numbers or their history ("the <date> figures ... must not be reused"), and alternative-basis tables kept only to explain a discrepancy.
- Dated audit or rebuild names in captions ("<date> audit", "rebuilt <date>").
- Two-denominator framings presented as a conflict ("X% of the labelled subset but Y% of everything sent, because N came back empty"). One representative denominator per figure; the other is a finding stated once in prose if it matters.
- Rows or shares that exist only because of internal history (a feature that shipped part-way through the data). Merge them into one row that states what is true of the reader's world (for example "No decision recorded"), and keep the totals summing.
- "Not located", "not reproducible from any file", "referenced in an earlier internal report", "project notes", "should not be quoted without".
- `\todo{}` and `\flag{}` markers, and "Revised draft" in the date line ("Preprint" instead).
- Repository paths, storage buckets, internal document names in the source index.

## Markers

Draft-stage markers live in the skeleton, the artifact and internal builds only; all are stripped before the external PDF.

| Marker | Where | Meaning |
|---|---|---|
| `[TO BE FILLED]` | skeleton and artifact only | slot for a result not yet run |
| `\todo{...}` | LaTeX body, internal builds only | accent-coloured bracketed note: what will appear, source, blocker |
| `\pilot` | LaTeX numbers | pilot-scale value; listed in the reconciliation register with n |
| `\flag{...}` | LaTeX tables, internal builds only | proposed or problematic value, accent tint |
| `\placeholder{...}` | legacy LaTeX macro | red placeholder text; grep before submission |
| `.pend` box | HTML artifact | dashed pending note under provisional content |
| status pill | HTML artifact | sourced / outlined / pending per section |
| asterisk + note | tables | provisional model or checkpoint |

## Naming

- Modules M0..Mn in pipeline order. Stages or cumulative configurations S1..Sn. Experiments E1..En. Baselines B0..Bn. Principles P1..Pn. Routes A/B for architectural alternatives.
- Route letters can flip meaning between drafts of the same paper. Record the current mapping in the status memory and apply it everywhere, including figure colours.
- Module and route colours are fixed tokens (house default: rust accent for flags, blue and green when the paper compares two routes, one accent per module when it does not) and reused across artifact, charts and LaTeX. The paper's own mapping lives in its status memory.
- Take the current paper's format, section count and appendix set from its own status memory and its own `main.tex`, never from another paper.

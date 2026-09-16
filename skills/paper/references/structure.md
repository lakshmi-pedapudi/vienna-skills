# Structure: Skeleton, Appendices, Markers

## Canonical Skeleton

Merged from the two 2026 skeletons the author wrote (one of 21 sections, one of 15) and the two published papers. Those counts are provenance, not a target. When the author supplies a skeleton, use it verbatim, numbering included. Otherwise start here and trim.

```
Abstract              Problem / Key Challenges / Proposed Approach / Evaluation / Main Results [TO BE FILLED]
1 Introduction        1.1 Motivation  1.2 Problem Statement  1.3 Research Questions (RQ1..RQn)  1.4 Contributions
2 Existing System and Baselines
                      2.1 Production pipeline today  2.2 Existing-System Limitations
                      2.3 Baselines (B0 production, B1 general-purpose model, B2/B3 proposed routes or ablated pipeline)
                      2.4 Related Work (folded here, not a standalone section)
3 Production Failure Analysis
                      per failure class, each quantified from production data; funnel by country; human-review yield
4 Design Principles and Architecture
                      P1..Pn as short imperative statements; architecture figure; configuration table
5..k Modules          one section per stage (M0 quality gate, M1 ..., M2 ...), each: role, candidates, metrics, chosen design
k+1 Alternative Design Strategies / Routes
                      Route A versus Route B, or fine-tune versus wrap; what each adds or removes
k+2 Data Curation     human curation, synthetic curation, panel labelling, PII screening; each with a figure
k+3 Experimental Methodology
                      dataset splits, scoring rule, pipeline configurations table, metrics by stage, ablation plan, run plan
k+4 Results           headline table; component-level (E1..En); end-to-end; error analysis; cost, latency, quality; ablations
k+5 Discussion        key findings; generalizability; what the fix does not replace
k+6 Impact            production rollout metrics [TO BE FILLED until measured]
k+7 Limitations and Future Work
                      includes release plan for data and code
k+8 Conclusion
References
Appendix A  Source Index
Appendix B  Reconciliation Flags
Appendix C+ Prompt templates with worked examples, detailed per-slice tables (per country, per class, per language)
```

Conventions inside the skeleton:
- Numbers live in four homes: Abstract (Main Results), 1.4 Contributions, Results, Conclusion. Sections 2 through k+3 and Discussion, Impact and Limitations describe and cite a table or figure by number; they do not quote result values. Dataset counts sit in one table in Data or Methodology. See `style.md` §Where Numbers Live.
- Research questions are numbered and each is answered explicitly in Results or Discussion.
- Contributions are a numbered list; datasets and code releases appear there with links once live, written as done rather than planned.
- Baselines, principles, modules, routes, configurations, and experiments carry short ids (B0, P1, M0, S1, E1) defined once in a table.
- Every table is followed by a short paragraph that reads the numbers and names the takeaway.
- An Error Analysis subsection exists in every Results section. Its load-bearing figure is the error distribution across the categories the domain cares about, whatever the modality.
- Cost, latency, and deployability sit beside accuracy in the results, not in an afterthought.
- Human review or expert evaluation gets its own subsection, with the study design stated plainly (blind test, n questions, k experts, preference counts) and no sensationalized percentage.
- Concepts a method depends on (evaluation platform, curated data) appear before the Methodology section that uses them.
- Limitations own a section in the 2026 papers; earlier papers kept it as a Discussion subsection. Either is fine; it must exist.
- "Open-Source Contributions" as a standalone section became a release-plan paragraph inside Limitations in the LaTeX fold.

## Appendix A: Source Index

"Every raw dataset behind a number in this paper, so an aggregate can be re-derived rather than re-quoted."

Two tables:
1. Internal documents, chats, call notes: Source | Type | Owner | Updated | Feeds (sections).
2. Row-level data: Dataset | Location | Rows | Backs (sections and table numbers). In the external PDF, Location is a description plus basename; repository paths and bucket names stay in the tracker (author ruling 2026-09-14).

Caption: "Reconcile against these, not against summary documents." File names containing banned stems (`arm_scores_*.csv`) are allowed only here.

## Reconciliation Register (internal; never in the external PDF)

Formerly "Appendix B: Reconciliation Flags" inside the paper. Since 2026-09-14 it lives in `CRITICAL_REVIEW.md` (its own section) and the status memory, not in the tex. Author ruling: "remove all instances where internal conflicts are being openly written in the paper. these are relevant for internal reviewers. not for external readers." A bullet list, one bold lead-in per flag, of every unresolved item:
- Superseded row sets with the superseded numbers spelled out and "must not be reused".
- Files referenced but not located; filters that could not be reproduced.
- Confounds with a pending re-run (label leakage, warm-start checkpoint, oracle hints in prompts).
- Source-paper internal inconsistencies and which value this draft quotes.
- Denominator mismatches between sources.
- Pilot sample sizes for every `\pilot` number.
- Provisional author order with its deadline.

Nothing is silently filled. A gap in the paper is stated once, in reader-facing words ("not yet measured", "listed in \S Limitations"), and points at nothing outside the document.

## Reader-Facing Rule

The external PDF carries none of the following; each is fine in the skeleton, the artifact draft stage and the tracker:
- Status columns: "Measured", "Not run", "Not started", "In progress", "In this draft: Yes / No / Partly".
- Cross-reference columns: "Answered in", "Responds to", "Where reported".
- Superseded numbers or their history ("the 13 August figures ... must not be reused"), and alternative-basis tables kept only to explain a discrepancy.
- Dated audit or rebuild names in captions ("16 August 2026 audit", "rebuilt 16 August").
- Two-denominator framings presented as a conflict ("X% of the labelled subset but Y% of everything sent, because N came back empty"). One representative denominator per figure; the other is a finding stated once in prose if it matters.
- "Not located", "not reproducible from any file", "referenced in an earlier internal report", "project notes", "a mechanical re-score supplies it", "should not be quoted without".
- Rust `\todo{}` and `\flag{}` markers, and "Revised draft" in the date line ("Preprint" instead).
- Repository paths, S3 buckets, internal document names in the source index.

## Markers

| Marker | Where | Meaning |
|---|---|---|
| `[TO BE FILLED]` | skeleton and artifact only | slot for a result not yet run |
| `\todo{...}` | LaTeX body, internal builds only | rust bracketed note: what will appear, source, blocker; stripped before the external PDF |
| `\pilot` | LaTeX numbers | pilot-scale value; listed in Appendix B with n |
| `\flag{...}` | LaTeX tables, internal builds only | proposed or problematic value, rust tint; stripped before the external PDF |
| `\placeholder{...}` | SFT-era LaTeX | red placeholder text; grep before submission |
| `.pend` box | HTML artifact | dashed pending note under provisional content |
| status pill | HTML artifact | sourced / outlined / pending per section |
| asterisk + note | tables | provisional model or checkpoint |

## Naming

- Modules M0..Mn in pipeline order. Stages or cumulative configurations S1..Sn. Experiments E1..En. Baselines B0..Bn. Principles P1..Pn. Routes A/B for architectural alternatives.
- Route letters have flipped meaning between drafts of the same paper. Record the current mapping in the status memory and apply it everywhere, including figure colours.
- Module and route colours are fixed tokens (rust for flags, blue and green when the paper compares two routes, one accent per module when it does not) and reused across artifact, charts, and LaTeX. The paper's own mapping lives in its status memory.

## Prior Papers as Reference

| Paper | Format | Sections | Appendix pattern |
|---|---|---|---|
| ASR benchmark (2602.03868) | IEEEtran, Arabic numbering forced | Intro, Related Work (4 subsections), Methodology (data, audio quality, metrics, models), Results (by language, by model, diarization impact, domain error analysis, the benchmark, LLM utility), Discussion (findings, implications, limitations), Future Work, Conclusion, Disclosure | none; 8 tables, 6 figures |
| SFT + DG-Eval (2603.03294) | article (arXiv) and IEEEtran twins | Intro with Contributions, Background and Related Work, Methodology (data curation, hybrid engine, DG-Eval), Experiments (setup, benchmarks, human evaluation, ablation, crop-topic), Discussion (findings, limitations), Conclusion | prompt templates with examples, specificity illustration, detailed tables, example output |
| Vision pipeline (2026) | article, tectonic | 16 sections per canonical skeleton | none; A and B removed 2026-09-14, see Reader-Facing Rule |
| Voice pipeline (2026) | article, tectonic | 12 sections per canonical skeleton, `\pilot` macro | A Source Index, B Reconciliation Flags as last seen |

The rows are provenance and they drift. Take the current paper's format, section count and appendix set from its own status memory and its own `main.tex`, never from this table.

A Disclosure paragraph (authors are employees of the organisation; no financial relationship with evaluated vendors) closes a paper that benchmarks commercial systems.

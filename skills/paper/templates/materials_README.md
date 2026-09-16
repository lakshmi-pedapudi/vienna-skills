# Paper Materials: <Paper Title>

Evidence gathered for the paper, organized by paper section or theme, not by source repository. Every aggregate in the paper should be re-derivable from a file listed here.

## Folder Map

| Folder | Contents | Paper section |
|---|---|---|
| `01_background_motivation/` | production funnel CSV, corpus stats, extraction script | 1, 3 |
| `02_pipeline_architecture/` | architecture notes, prior artifact HTML, DOT sources | 2, 4 |
| `03_<module>_M0/` | candidate comparison CSV, experiment report | 5 |
| `NN_<gap>/` | `GAP_NOTE.md` with status in the heading | as noted |

Corrections and supersessions go inline in bold in this table, for example: **the 13 Aug headline table (a / b / c / d) is superseded by the 16 Aug audit; never reuse.**

## Excluded

Large binaries not copied (caches, raw image folders, parquet feature stores), with their original location so they can be fetched.

## Gaps

One line per gap the author flagged, with its `GAP_NOTE.md` and its status (resolved as not missing, confirmed missing with quantified evidence, parked pending re-run).

## Style Reference

The two published papers: arXiv:2602.03868 (ASR benchmark), arXiv:2603.03294 (SFT and DG-Eval). House rules in `~/.claude/skills/paper/references/style.md`.

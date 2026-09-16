---
name: artifact
description: Use when building, revising, reviewing, publishing, or exporting a Claude artifact (a published HTML page) for a research or product team: pre-reads for funders or partners, analysis reports and dashboards, methodology articles, reviewer-facing paper drafts, design documents, findings pages with charts and example tables. Also use when an artifact must be republished after a data change, mirrored to Railway, exported to PDF or Google Slides, or when teammates have edited it. Triggers: "/artifact", "claude artifact", "publish", "republish", "pre-read", "html page", "dashboard", "findings page", "share via railway", "convert the artifact".
---

# Artifact Building and Review

House workflow for Claude artifacts, distilled from fifteen published pages (funder pre-reads and their slide versions, analysis findings pages, a methodology article, two reviewer-facing paper drafts, survey result pages) and roughly 110 instructions and corrections given while building them.

**Core principle:** an artifact is an empty canvas filled one element at a time, each element approved before it is wired in. Charts, tables and short numbered points carry the content. A stranger with no context must understand the page end to end, and the page must survive being read a month later, exported to PDF, or cut into slides.

**Scope:** this skill carries rules, not any one page's content. Past pages appear only as provenance and as the shape of an example. No number, model name, vendor, denominator or section title in this skill or in its templates belongs to the page in front of you: every figure comes from that page's own source data and its own status memory. Where an example names a subject (a crop, a language, a modality, a vendor), the rule transfers and the subject does not.

## When to Use

- Any page published with the Artifact tool, or an HTML page that will be.
- A data change that must reach a published page.
- Converting a page to PDF, Google Slides, a Railway mirror, or a slide deck.
- Teammates editing a shared artifact.
- Not for: the research paper itself (use `/paper`, which owns the paper artifact's structure), a `.pptx` (use `/deck`), a stakeholder email.

## Session Start

1. Read the artifact's status memory (`<name>-status.md` in the project memory dir). It records the URL, the source file path, superseded URLs marked "do not edit", frozen copies, and open items. If none exists, create one from `templates/artifact_status_memory.md`.
2. Confirm the source file lives in the project folder, not a session scratchpad. If it is only in the scratchpad, copy it into the project folder now.
3. If teammates may have edited the live page, `read` it with its `url` and diff against the local file before touching anything.
4. Load the `artifact-design` skill (and `artifact-diagramming` for any flowchart) before writing HTML. Read `references/style.md`.

## Phase Flow

| Phase | Output | Detail |
|---|---|---|
| 0 Recall | Status memory, URL, live diff, prior artifacts to reuse components from | `references/workflow.md` §0 |
| 1 Skeleton | Empty canvas: title, status card, section cards with status pills and source chips, appendix stubs; confirmed at a checkpoint question | `references/workflow.md` §1, `references/review.md` §Checkpoint Questions |
| 2 Build | One element at a time: render standalone, approve, wire in, republish to the same URL | `references/workflow.md` §2 |
| 3 Review | Deviations reported before edits; reframe shown in chat; itemized approval; convergent loop (2 to 3 passes, stop on agreement), `REVIEW_LOG.md` | `references/workflow.md` §3, `references/review.md` |
| 4 Publish | Same URL, dated backup, `check_html.py` clean, render verified, PDF checked | `references/publish.md` |
| 5 Distribute | Railway mirror, PDF, Google Slides, frozen copy recorded | `references/publish.md` |
| 6 Close | Status memory updated, which sections changed stated | `references/workflow.md` §6 |

## Non-Negotiables

- One URL per artifact for its whole life. Republish by passing `url`; omitting it forks a new page. Superseded ids are recorded as "do not edit". A URL already sent to an external party is frozen: "DO NOT TOUCH IT."
- The HTML source lives in the project folder and is backed up before any restructure as `<name>.html.bak_YYYY-MM-DD` or `_backup_<date>_<state>`. Two sources were lost to scratchpads.
- One page per session's working set. Sibling pages share section titles and component names, and two paper artifacts can look alike; confirm the URL and the local source file before every edit, and never carry a number from one page into another.
- Standalone. No named colleagues, funders, internal documents, task ids, file names, process narration, self-reference, or "as discussed". No changelog; every publish reads as a fresh first version.
- More than three sentences or about 100 words in one place becomes bullets, a numbered list, a table, or a chart with a one-line caption. Every tile is visual or bulleted, never a paragraph.
- No em-dashes (neither `&mdash;` nor U+2014). Banned: arm, instrument, license, ground (filler), axes, verdict, "under the rule", leverage, robust, seamless, delve, unlock. Headings are formal noun phrases in Title Case; no sentences, no "X not Y".
- Every number names its denominator and row set. Approximate values carry a tilde. Never an inflated derived count. Never a fabricated number or example. Unflattering numbers are not hero-sized.
- No footnotes, caveat blocks, or methodology parentheticals. An essential caveat is one plain sentence or an empty labelled column.
- Charts are hand-authored inline SVG or matplotlib PNGs embedded as data URIs. No chart library. Never Mermaid. Bars are proportional. Labels sit next to the marks they encode. No number lives only inside a raster.
- Three-state theme through CSS tokens on `:root`, redefined under `prefers-color-scheme: dark` guarded by `:root:not([data-theme="light"])` and again under `:root[data-theme="dark"]`. Body has an explicit token background. Holds at 400 px. Rows of tiles survive PDF export.
- Show the proposed rewrite before editing the live page. Review mode reports deviations only. Change exactly what was asked. Republish after every data change and say which sections changed.
- Checkpoint questions at section segregation, atomic elements and their visual form, rough themes, and before any restructure, even in bypass mode: one or two simple questions with a recommended option, via AskUserQuestion. Nowhere else.
- Review runs as a convergent loop: at least two passes, at most three, each re-verifying every earlier fix by id; stop only when two successive passes agree. Log in `REVIEW_LOG.md`.
- Respect org sharing limits: export or mirror to Railway with authorization; never move an artifact to a personal account.

## Quick Reference

| Need | Go to |
|---|---|
| Standalone rules, word bans, prose limits, numbers, headings, tiles | `references/style.md` |
| Skeleton, element-at-a-time build, review loop, reconciliation, close | `references/workflow.md` |
| Page anatomy, palette, typography, theme CSS, charts, tables, layout, scroll control | `references/design.md` |
| URL reuse, backups, staging, freezing, Railway, PDF, Google Slides, visibility | `references/publish.md` |
| Checkpoint questions, convergent review loop | `references/review.md` |
| Dated corrections and pushbacks, rationalization table, baseline trial | `references/lessons.md` |
| `scripts/check_html.py` gate; `templates/page_skeleton.html`; `templates/artifact_status_memory.md` | `scripts/`, `templates/` |

## Red Flags

Stop and re-read the relevant reference when any of these appear in your own output or plan:

- An Artifact call without `url` for a page that already exists.
- The HTML being edited under `/private/tmp` or a scratchpad path.
- A paragraph you had to scroll to read, or a tile that describes instead of listing.
- A section named "Caveats", "Not Yet Solid", "Claims We Are Not Repeating", "Changes in This Version", or any heading that talks about the document itself.
- A person's name, a Linear id, a `.csv` or `.py` name, or "the paid service" where the vendor name is cleared.
- A stat tile carrying a rejection rate or an LLM-judged pilot number.
- `<script src>` for a chart library, a Mermaid block, or a bar whose width is not computed from the value.
- A page with more than seven or eight sections for a pre-read or report.
- Publishing without running `scripts/check_html.py` and opening the live page.
- Two live copies (main and staging) after the trial is over.

## Session Close

Update the status memory: URL, source path, backups, frozen copies, superseded ids, which sections changed this session, open items, next step. If the user asks to clear context, the memory must let a cold session republish correctly without forking.

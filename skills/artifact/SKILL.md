---
name: artifact
description: Use when building, revising, reviewing, publishing, or exporting a Claude artifact (a published HTML page): pre-reads for external stakeholders, analysis reports and dashboards, methodology articles, reviewer-facing paper drafts, design documents, findings pages with charts and example tables. Also use when an artifact must be republished after a data change, mirrored to an approved host, exported to PDF or Google Slides, or when teammates have edited it. Triggers: "/artifact", "claude artifact", "publish", "republish", "pre-read", "html page", "dashboard", "findings page", "convert the artifact".
---

# Artifact Building and Review

## Overview

A house workflow for building, reviewing and publishing Claude artifacts: standalone HTML pages that carry analysis, findings or proposals to readers who were not in the room.

**Core principle:** an artifact is an empty canvas filled one element at a time, each element approved before it is wired in. Charts, tables and short numbered points carry the content. A stranger with no context must understand the page end to end, and the page must survive being read a month later, exported to PDF, or cut into slides.

**Scope:** this skill carries rules, not any one page's content. No number, model name, vendor, denominator or section title in this skill or its templates belongs to the page in front of you: every figure comes from that page's own source data and its own status memory. Where an example names a subject, the rule transfers and the subject does not.

**Provenance:** distilled from about fifteen published pages and over a hundred review corrections made while building them.

## When to Use

- Any page published with the Artifact tool, or an HTML page that will be.
- A data change that must reach a published page.
- Converting a page to PDF, Google Slides, a mirror on an approved host, or a slide deck.
- Teammates editing a shared artifact.

**When not to use:** the research paper itself (use the paper skill, if installed, which owns the paper artifact's structure); an editable `.pptx` (use a deck skill, if installed); an email or chat message to a stakeholder.

## Inputs

- Source data: the files, extracts or documents behind every number and example.
- Audience, and whether the page leaves the organisation (external pages trigger the standalone rules in `references/style.md`).
- Format constraints from the stakeholder who asked for the page (length, proportion of a section, slide count).
- Naming clearance: whether vendors, partners and models may be named.
- For an existing page: its status memory, live URL and local source file.
- For the gate: a `names.txt` of people's names to block, and optionally a word config other than the default.
- Optional: brand tokens to replace the house default palette.

## Outputs

- One live artifact URL, kept for the page's whole life.
- The HTML source in the project folder, with dated backups before each restructure.
- `charts/` (standalone SVG and PNG renders and their generators) and `data/` (backing extracts), so the analysis can be re-run.
- A status memory for the page (`templates/artifact_status_memory.md`) and a `REVIEW_LOG.md` (`templates/REVIEW_LOG.md`).
- When asked: a PDF or HTML export, a mirror on an approved host, or Google Slides.

## Workflow

### Session Start

1. Read the page's status memory (`<name>-status.md` in the project memory folder). It records the URL, source path, superseded URLs marked "do not edit", frozen copies, and open items. If none exists, create one from `templates/artifact_status_memory.md`.
2. Confirm the source file lives in the project folder, not a session scratchpad. If it is only in the scratchpad, copy it into the project folder now.
3. If teammates may have edited the live page, `read` it with its `url` and diff against the local file before touching anything.
4. Load the `artifact-design` skill (and `artifact-diagramming` for any flowchart) before writing HTML. Read `references/style.md`.

### Phases

| Phase | Output | Detail |
|---|---|---|
| 0 Recall | Status memory, URL, live diff, prior artifacts to reuse components from | `references/workflow.md` §0 |
| 1 Skeleton | Empty canvas: title, status card, section cards with status pills and source chips, appendix stubs; confirmed at a checkpoint | `references/workflow.md` §1 |
| 2 Build | One element at a time: render standalone, approve, wire in, republish to the same URL | `references/workflow.md` §2 |
| 3 Review | Deviations reported before edits; rewrite shown in chat; itemised approval; convergent loop logged in `REVIEW_LOG.md` | `references/workflow.md` §3, `references/review.md` |
| 4 Publish | Same URL, dated backup, gate clean, render verified, PDF checked | `references/publish.md` |
| 5 Distribute | Export, mirror or slides; frozen copy recorded | `references/publish.md` |
| 6 Close | Status memory updated; sections changed stated | `references/workflow.md` §6 |

### Checkpoints

Ask at four points, even in bypass or autonomous mode, using AskUserQuestion: section segregation, atomic elements and their visual form, rough themes, and before any restructure. One or two simple questions with a recommended option; nowhere else. Detail in `references/review.md` §Checkpoint Questions.

### Session Close

Update the status memory: URL, source path, backups, frozen copies, superseded ids, sections changed this session, open items, next step. If the author is about to clear context, the memory must let a cold session republish correctly without forking.

## Quality Standards

### Non-Negotiables

**Page**
- One URL per artifact for its whole life; republish with `url`, record superseded ids, never edit a URL already sent outside. `references/publish.md`
- The source lives in the project folder and is backed up before any restructure. `references/publish.md`
- Confirm the URL and local source before every edit; never carry a number from one page into another. `references/workflow.md` §0
- Respect organisation sharing limits; never move an artifact to a personal account. `references/publish.md` §Distribution Routes

**Content**
- Standalone: no named people, funders, internal documents, task ids, file names, process narration or self-reference; no changelog. `references/style.md` §Standalone
- More than three sentences or about 100 words in one place becomes a list, table or chart; tiles are never paragraphs. `references/style.md` §Prose Limits
- No em-dashes, no house banned words, no AI-tell sentence shapes; headings are Title Case noun phrases. `references/style.md`
- Every number names its basis; approximations carry a tilde; nothing fabricated or inflated; unflattering numbers are not hero-sized. `references/style.md` §Numbers
- No footnotes, caveat blocks or methodology parentheticals. `references/style.md` §Caveats and Footnotes

**Visual**
- Inline SVG or embedded PNG charts only; no chart library, no Mermaid; bars proportional; labels beside marks. `references/design.md` §Charts
- Three-state theme through tokens on `:root`; explicit body background; holds at 400 px; tile rows survive PDF. `references/design.md`

**Process**
- Show the proposed rewrite before editing; review reports deviations only; change exactly what was asked; republish after every data change and say which sections changed. `references/workflow.md` §3
- Review is a convergent loop of two to three passes, logged. `references/review.md`

### Gate Script

| Item | Detail |
|---|---|
| Command | `python3 <skill-dir>/scripts/check_html.py <name>.html --names names.txt` |
| Exit codes | `0` no failures (warnings may exist); `1` one or more failures, or any warning under `--strict` |
| Fails on | em-dashes; AI tells and hype phrases; house banned words and jargon (`scripts/house_words.json`); names from `--names`; chart libraries; Mermaid; missing `<title>`; `<script src>` outside cdnjs.cloudflare.com and cdn.jsdelivr.net/npm/ |
| Warns on | paragraphs over 3 sentences or 100 words; more than 7 `<h2>` sections; sentence-like or "X not Y" headings; pivots, recap endings, narrated structure; self-reference and caveat blocks; internal ids and file names; theme not three-state; no body background; missing images |
| `--names FILE` | One personal name per line; any hit fails |
| `--words FILE` | Another word config in the `house_words.json` format; `--words none` skips the house lists |
| `--id-pattern REGEX` | Extra internal-id pattern to warn on (repeatable); tracker keys like `ABC-123` and file names are always checked |
| `--allow REGEX` | Suppress hits whose surrounding text matches (repeatable) |
| `--strict` | Treat warnings as failures |
| Does not catch | meaning: wrong numbers, missing denominators, unflattering framing, a confusing chart, a blank render, a section that contradicts another. Read every warning, then open the live page. |

### Red Flags

Stop and re-read the relevant reference when any of these appear in your own output or plan:

- An Artifact call without `url` for a page that already exists.
- The HTML being edited under `/private/tmp` or a scratchpad path.
- A paragraph you had to scroll to read, or a tile that describes instead of listing.
- A section named "Caveats", "Not Yet Solid", "Changes in This Version", or any heading that talks about the document itself.
- A person's name, a tracker id, a file name, or a euphemism for a vendor whose naming is cleared.
- A stat tile carrying an unflattering number, or a pilot or LLM-judged value.
- `<script src>` for a chart library, a Mermaid block, or a bar whose width is not computed from its value.
- More than seven sections for a pre-read or report.
- Publishing without running the gate and opening the live page.
- Two live copies (main and staging) after a trial is over.

## Reference Guides

| Need | Go to |
|---|---|
| Standalone rules, word bans, prose limits, sentence shapes, numbers, headings, tables | `references/style.md` |
| Recall, skeleton, element-at-a-time build, review intake, reconciliation, close, folder layout | `references/workflow.md` |
| Page anatomy, palette, typography, theme CSS, charts, layout, file shape | `references/design.md` |
| URL reuse, backups, staging, freezing, distribution routes, collaboration | `references/publish.md` |
| Checkpoint questions, convergent review loop | `references/review.md` |
| Rationalisations to resist and common failure modes | `references/pitfalls.md` |
| Gate script and its word config | `scripts/check_html.py`, `scripts/house_words.json` |
| Page skeleton, status memory, review log | `templates/` |

## Limitations

- The Artifact tool cannot make a page public; visibility is set by the author through the page's Share menu, within organisation policy.
- A published page never updates itself; every data change needs a republish.
- Pages cannot be moved between accounts.
- Content Security Policy blocks chart libraries and most external hosts; scripts load only from cdnjs.cloudflare.com and cdn.jsdelivr.net/npm/.
- The gate is a set of regular expressions. It produces false positives (a model name like `GPT-4` matches the tracker-key pattern; "axes" fails even in a legitimate sense) and misses anything semantic. Use `--allow` or edit `house_words.json` rather than rewording correct text.
- The workflow assumes AskUserQuestion, subagents and a project memory folder are available; without them, ask in chat and keep the status memory as a file beside the source.

## Troubleshooting

| Symptom | Fix |
|---|---|
| A publish created a new URL | Find the original URL in the status memory or with the Artifact `list` action; republish to it with `url`; record the stray id as superseded. |
| Sections render blank or images are missing | Embed images as `data:` URIs or publish them through `files`; open the live page and check every section. |
| Tile rows break into a column in the PDF | Use `display:flex; flex-wrap:nowrap` with `print-color-adjust: exact` in print CSS; re-export and check. `references/design.md` §Layout |
| The live page has edits you do not have locally | `read` the live page, diff, merge into the local source, then republish. `references/publish.md` §Collaboration |
| A scripted edit silently changed nothing | Anchor on inner content, assert the match count, print misses. `references/workflow.md` §2 |
| The gate warns "theme not three-state" | Define tokens on `:root`, redefine under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])` and again under `:root[data-theme="dark"]`. |
| The gate flags a correct word | Pass `--allow` for that context, or edit `scripts/house_words.json`. |
| A reviewer says a section still shows old results | Reconcile the whole page from latest to earliest section, then list the sections changed. `references/workflow.md` §3 |

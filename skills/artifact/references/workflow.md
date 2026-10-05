# Workflow

Applies to: every artifact, from the first empty canvas to the session that closes it.

Asked for a whole page in one go, a model invents its own structure and fills it with whatever the data suggests. So build an empty canvas first, then add one approved component at a time and assemble them on the page.

## 0. Recall

- Read the status memory. Note the URL, source path, superseded ids and frozen copies. Confirm the URL and the local source file before every edit: sibling pages share section titles and component names, and never carry a number from one page into another.
- When teammates may have edited the live artifact, `read` it with its `url`, diff against the local file, and merge rather than overwrite. *Why: overwriting silently discards a colleague's work.*
- Search for earlier artifacts on the topic with any memory or search tool available. Reuse components by reference ("a miniature version of <section> from <earlier artifact>"). A teammate's artifact can serve as the template when the audience is shared. Reuse the component, never the earlier page's numbers.
- Confirm the audience and whether the page leaves the organisation. External pages trigger the standalone rules in `references/style.md`.
- Ask what the stakeholder requested in format and proportion, and hold to it literally. *Why: a section asked for as "compact" that grows to half the page is a review failure even when every line is correct.*

## 1. Skeleton

- Publish an empty canvas first: title, status card (draft date, scale facts), the section list with one-line scope each, a status pill per section (`sourced` / `outlined` / `pending`), source chips naming the file or document behind each section, and "content pending" markers. No numbers yet. *Why: provisional numbers on a skeleton get read as results.*
- Sections are logically atomic, slide-sized clusters in logical order, so the page can later be cut into slides or a PDF without restructuring.
- Budget the sections. Pre-reads and reports run four to seven sections. *Why: first drafts always over-produce sections and charts.*
- Present the skeleton for approval. Do not carry forward structure from a prior version unless told to. *Why: inherited structure carries inherited bias.*
- Paper-style artifacts add Appendix A (materials and sources) and Appendix B (raw datasets and reconciliation flags) from the first publish; see the paper skill, if installed.

## 2. Build One Element at a Time

- One element per iteration: a section, a table, a chart, a diagram, a tile row. Fill a section only when its source exists or the author supplies the content. Sections without data stay visibly pending.
- Propose the visual form before building it, as numbered options (for example: 1. a bar chart of totals per group; 2. small multiples per group). The author picks one.
- Render a chart or diagram standalone first (SVG and PNG in the project folder), iterate on width, labels, arrows, gaps and title, and only then wire it into the live artifact. Diagram specs may arrive as JSON node and edge lists; follow them exactly.
- Republish to the same URL after each element. Say which sections changed.
- Long content goes in a fixed-height scrollable box; large example sets get collapsible rows with filter chips and a per-row flag toggle. Prefer grids and side-by-side layouts to stacking, to control scroll length.
- Back aggregates with inspectable row-level examples carrying full metadata, spanning distinct cases and segments, from the real published dataset. Attach evidence (an image, a transcript) to the exact row it belongs to.
- Delegate heavy sub-tasks (data pulls, per-component SVGs, classification runs) to subagents so the page keeps moving.
- Keep the backing extracts in a project subfolder so the author can re-run the analysis by hand.

### Editing the Source

- Make structural moves with exact per-element anchors, never one regex across the whole page; afterwards walk each affected element and count its open and close tags. *Why: a page-wide pattern matches across element boundaries and silently breaks nesting.* Example: moving a note out of every `<figcaption>` with one regex left some notes inside and stray closing tags after tables.
- Anchor edits on inner content, not on indentation; assert the expected match count and print the misses. *Why: a wrong guess about indentation makes edits match nothing without any error.* Example: assuming eight-space indentation on a six-space file skipped a fifth of the edits.

## 3. Review

- Review mode reports deviations only, with no edits, until the author agrees. *Why: the author is judging the page against an expected theme and needs the list, not a moving target.*
- Show the proposed rewrite in chat before touching the page. *Why: a rewrite is cheap to reject in chat and expensive to undo on a live page.*
- Approval is itemised ("do 1 and 2, not 3"). Do the approved items only; stage any risky step separately.
- Change exactly what was asked and nothing else. *Why: unrequested edits force the author to re-review the whole page.*
- Fix a complaint with the smallest change that resolves it. *Why: overcorrection creates the opposite complaint.* Example: a flowchart called too small was both separated and enlarged, then called too big; separating it was enough.
- When review feedback arrives as a list (for example remove and add items), apply it literally, item by item, and keep a closure ledger.
- A reorganisation pass reorganises. It introduces no new content. Say what moved versus what is new.
- After any data update, reconcile the whole page from latest section to earliest so earlier sections line up with the latest findings without contradictions, then state which sections changed. *Why: stale results in an untouched section are the most common miss a reader catches.*
- Before shipping, sweep for named people, internal documents, self-reference and style violations as a dedicated pass, then run the gate (`scripts/check_html.py`).
- Two or three rounds is normal for a short internal report; a long external page can take many more.

## 4. Publish

See `references/publish.md`. In one line: same URL, dated backup first, gate clean, open the live page and look, check the PDF.

## 5. Distribute

See `references/publish.md`. Where organisation policy blocks public artifact links, the routes are PDF or HTML export, a mirror on an approved host with the data owner's authorisation, or Google Slides. The shipped copy is then frozen and new work branches to a new artifact.

## 6. Close

- Update the status memory from `templates/artifact_status_memory.md`: URL, source path, backups, frozen copies and their recipients, superseded ids, sections changed this session, open items, next step.
- Before a context clear, write everything a cold session needs into the status memory, including the artifact details. *Why: without it, the next session forks the page.*
- Commit if the folder is a repo; push only after confirmation. Otherwise flag version control as an open item.

## Folder Layout

```
<project>/
  <topic>/<name>.html                   # the source; never in a scratchpad
  <topic>/<name>.html.bak_YYYY-MM-DD    # before each restructure
  <topic>/charts/<chart>.{svg,png}      # standalone renders, SVG and PNG
  <topic>/charts/gen_*.py               # generators reading the extracts
  <topic>/data/*.csv                    # backing extracts, re-runnable
  <topic>/mirror_<name>/index.html      # mirror for an approved host, plus package.json
  <topic>/exports/                      # exported siblings: .pdf .pptx .md
<project memory folder>/<name>-status.md
```

# Workflow: Skeleton, Element by Element, Review, Close

The author's description of the method, from an interview: "you can't just say create a chart out of my data or my work. It's going to do whatever it wants to do. So what we did was we built an empty canvas, the artifact, make an empty artifact and start building one component at a time, and then put them together."

## 0. Recall

- Read the status memory. Note the URL, source path, superseded ids, frozen copies.
- `read` the live artifact with its `url` when teammates may have edited it; diff against the local file; merge, do not overwrite. "can you see any latest changes compared to what we already had earlier?"
- Search Eagle Mem and `/brain` for earlier artifacts on the topic. Reuse components by reference: "add a miniature version of '<section name>' from [earlier artifact]". A teammate's artifact can serve as the template when the audience is shared. Reuse the component, never the earlier page's numbers.
- Confirm audience and whether the page leaves the organisation. External pages trigger the standalone rules in `references/style.md`.
- Ask what the stakeholder requested in format and proportion, and hold to it literally. "rikin's message said a very compact model comparison, but we seem to have taken up a larger portion of the page."

## 1. Skeleton

- Publish an empty canvas first: title, status card (draft date, scale facts), the section list with one-line scope each, a status pill per section (`sourced` / `outlined` / `pending`), source chips naming the file or document behind each section, and "content pending" markers. No numbers yet. "publish a claude artifact with bare minimum skeleton and mapped references."
- Sections are logically atomic, slide-sized clusters in logical order, so the page can later be cut into slides or a PDF without restructuring.
- Budget the sections. Pre-reads and reports run four to seven sections; first drafts always over-produce ("too verbose and too many sections and graphs").
- Present the skeleton for approval. Do not carry forward structure from a prior version unless told to.
- Paper-style artifacts add Appendix A (materials and sources) and Appendix B (raw datasets and reconciliation flags) from the first publish; see `/paper`.

## 2. Build One Element at a Time

- One element per iteration: a section, a table, a chart, a diagram, a tile row. Fill a section only when its source exists or the author supplies the content. Sections without data stay visibly pending.
- Propose the visual form before building it, as numbered options: "what's the most creative way to add this? A bar chart of the totals for countries and a donut chart for the species distribution?" The author picks one.
- Render a chart or diagram standalone first (SVG and PNG in the project folder), iterate on width, labels, arrows, gaps and title, then "wire it up in the live artifact." Diagram specs may arrive as JSON node and edge lists; follow them exactly.
- Republish to the same URL after each element. Say which sections changed.
- Long content goes in a fixed-height scrollable box; large example sets get collapsible rows with filter chips and a per-row flag toggle. Grids and side-by-side layouts over stacking, to control scroll length.
- Back aggregates with inspectable row-level examples carrying full metadata, spanning distinct cases and geographies, from the real published dataset. Attach evidence (a photo) to the exact row it belongs to.
- Delegate heavy sub-tasks (data pulls, per-component SVGs, classification runs) to subagents so the page keeps moving.
- Keep the backing CSVs in a project subfolder so the analysis can be re-run by hand.

## 3. Review

- Review mode: report deviations only, no edits, until agreement. "review the artifact again. don't make any edits before I agree. this is the expected theme, just tell me the deviations."
- Show the reframe in chat before touching the page. "cut this short ... give me the reframe first before updating directly."
- Approval is itemized: "Do 1 and 2. Don't do 3." Do the approved items only; stage the risky step separately.
- Change exactly what was asked. "only change what I'm telling you to, pls don't touch anything else."
- Reviewer mail arrives as Remove and Add lists; apply literally, item by item, and keep a closure ledger.
- A reorganisation pass reorganises. It introduces no new content. Say what moved versus what is new.
- After any data update, reconcile the whole page latest to earliest: "make sure the whole document from earlier iterations lines up with latest findings ... without contradictions." Then state which sections changed. "which sections in the artifact did you update? because I'm looking at the results section and it feels like they are still the old results."
- Before shipping, sweep for named people, internal documents, self-reference, and style violations as a dedicated pass, then run `scripts/check_html.py`.
- Two or three rounds is normal for a short internal report; an external pre-read took twenty.

## 4. Publish

See `references/publish.md`. In one line: same URL, dated backup first, checker clean, open the live page and look, check the PDF.

## 5. Distribute

See `references/publish.md`. Org policy blocks public artifact links; the routes are PDF or HTML export, a Railway mirror under a named subdomain with authorization, or Google Slides. The shipped copy is then frozen and new work branches to a new artifact.

## 6. Close

- Update the status memory from `templates/artifact_status_memory.md`: URL, source path, backups, frozen copies and their recipients, superseded ids, sections changed this session, open items, next step.
- Before a context clear: "write up everything you have so far including the artifact details so that i can start fresh." The memory must be enough for a cold session to republish without forking.
- Commit and push if the folder is a repo; otherwise flag it as an open item.

## Folder Layout

```
<project>/
  <topic>/<name>.html                   # the source; never in a scratchpad
  <topic>/<name>.html.bak_YYYY-MM-DD    # before each restructure
  <topic>/charts/<chart>.{svg,png}      # standalone renders, SVG and PNG
  <topic>/charts/gen_*.py               # generators reading the CSVs
  <topic>/data/*.csv                    # backing extracts, re-runnable
  <topic>/railway_<name>/index.html     # mirror, plus package.json
  <topic>/for_<recipient>/              # exported siblings: .pdf .pptx .md
~/.claude/projects/<proj>/memory/<name>-status.md
```

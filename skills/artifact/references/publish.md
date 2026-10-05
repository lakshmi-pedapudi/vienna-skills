# Publish and Distribute

Applies to: every publish and republish of an artifact, and every copy of it that leaves the Artifact tool (export, mirror, slides).

## Publishing

- First publish: pass `icon` (one plain generic word, then never changed) and a one-sentence `description`, with the source file in the project folder. Load `artifact-design` first.
- Every later publish passes the existing `url`. *Why: omitting it forks a new artifact and loses the review trail.* Superseded ids go in the status memory as "do not edit".
- Before any restructure, back up the source: `cp <name>.html <name>.html.bak_$(date +%F)`, or `<name>_backup_<date>_<state>.html` naming the structural state preserved (for example `_pre-split`). *Why: scratchpads are cleared, and a restructure is the edit most likely to need rolling back.*
- Run `python3 <skill-dir>/scripts/check_html.py <name>.html --names names.txt` and fix every failure. `names.txt` lists the people whose names must never appear on the page, one per line. Read warnings one by one.
- After publishing, open the live page and look at every section, ideally after rendering it in a headless browser and reading the result. Blank sections, missing images and overlapping diagram labels are blocking bugs. *Why: a successful publish says nothing about whether the page renders.*
- Republish after every data change and state which sections changed. *Why: a published page does not update itself, and stale numbers stay live until someone notices.*
- Visibility belongs to the author, through the Share menu on the page. The tool cannot make a page public; pages are private until the author shares them.

## Staging

- Trial a risky addition (a photo gallery, a big restructure) in a separate staging artifact copied from the main one. Promote it, then collapse back to one live artifact. *Why: two live copies drift, and edits land on the wrong one.*
- When the format or audience changes (a long draft becomes a three-page pre-read), publish a fresh artifact at a new URL and leave the old one untouched as source material for later deliverables.

## Freezing

- A URL sent to an external party is frozen and never edited again. Record it in the status memory with the date and recipient. New work branches to a new artifact, and the memory names which one is editable. *Why: the recipient may already have read or forwarded it.*

## Distribution Routes

If your organisation blocks public "anyone with the link" sharing of artifacts, never move an artifact to a personal account to get around it. *Why: pages can carry production or customer data.*

1. **PDF or HTML export.** Convert the artifact HTML to PDF (browser print or a headless renderer). Check that tile rows and side-by-side charts keep their layout. Send the file.
2. **Mirror on an approved host.** With authorisation from the data owner, copy the HTML to `mirror_<name>/index.html` with whatever the host needs to serve a static file (for example a `package.json` that runs `serve -s . -l ${PORT:-3000}`), deploy, and give it a readable subdomain (`<project>-<page>.<host-domain>`). Same bytes as the artifact. The mirror is then frozen too.
3. **Google Slides.** Cut the page horizontally at logical boundaries into slide-sized clusters (about ten slides for ten minutes), with no re-authoring and no headings or footers carried over. Keep the artifact's own rendering rather than rebuilding in native elements, unless the author asks for editable slides; then use a deck skill, if installed.

## Collaboration

- Teammates edit the same live artifact. Before any edit, `read` the live version with its `url`, diff against the local file, merge the teammate's changes into the local source, then republish. Never overwrite a teammate's edits.
- When the published copy belongs to a teammate, ship a patch note ("What to update in the published artifact") rather than republishing over their page.
- Comments on the page: read them with the Artifact comments tool when asked; reply to and resolve only threads sent to Claude.

## Status Memory

Use `templates/artifact_status_memory.md` and update it at every session close. Its fields are listed in `references/workflow.md` §6.

# Publish and Distribute

## Publishing

- First publish: pass `favicon` (one emoji, then never changed), a one-sentence `description`, and put the file in the project folder. Load `artifact-design` first.
- Every later publish passes the existing `url`. Omitting it forks a new artifact and loses the review trail. Superseded ids go in the status memory as "do not edit".
- Before any restructure: `cp <name>.html <name>.html.bak_$(date +%F)` or `_backup_<date>_<state>.html` naming the structural state preserved (`_preslides`, `_10slide`, `_9slide_prewrap`).
- Run `python3 ~/.claude/skills/artifact/scripts/check_html.py <name>.html --names names.txt` and fix every failure. Warnings are read one by one.
- After publishing, open the live page and look at every section. Blank sections and missing images are blocking bugs: "Slides 5-9 aren't rendering." was reported twice in one evening.
- Republish after every data change and state which sections changed. A published page does not update itself; the Resolution Signal page shipped stale numbers for a day.
- Visibility is the user's, through the Share menu on the page. The tool cannot make a page public. Pages are private until the user shares them.

## Staging

- Trial a risky addition (a photo gallery, a big restructure) in a separate staging artifact copied from the main one. Promote it, then collapse back to one live artifact. "worth reconciling stage with the main and just maintaining one artifact."
- When the format or audience changes (long draft to three-page pre-read), publish a fresh artifact at a new URL and leave the old one untouched as source material for later deliverables.

## Freezing

- A URL sent to an external party is frozen. Record it in the status memory with the date and recipient. New work branches to a new artifact and the memory names which one is editable. "this url is already sent to gates. I repeat - DO NOT TOUCH IT."

## Distribution Routes

Org policy blocks public "anyone with the link" sharing of artifacts. Never move an artifact to a personal account to bypass that; the pages carry production data.

1. **PDF or HTML export.** Convert the artifact HTML to PDF (browser print, or a headless renderer). Check that tile rows and side-by-side charts keep their layout. Send the file.
2. **Railway mirror.** With authorization from the CEO or owner, copy the HTML to `railway_<name>/index.html` with a `package.json` that runs `serve -s . -l ${PORT:-3000}`, deploy, and rename the subdomain to something readable (`your-org-preread.up.railway.app`). Same bytes as the artifact. The mirror is then frozen too.
3. **Google Slides.** Cut the page horizontally at logical boundaries into slide-sized clusters (about 10 slides for 10 minutes), no re-authoring, no headings or footers carried over. Keep the artifact's own rendering rather than rebuilding in native elements unless the author asks for editable slides, in which case use `/deck`.

## Collaboration

- Teammates edit the same live artifact. Before any edit, `read` the live version with its `url`, diff against the local file, merge the teammate's changes into the local source, then republish. Never overwrite a teammate's edits.
- When the published copy belongs to a teammate, ship a patch note ("What to update in the published artifact") rather than republishing over their page.
- Comments on the page: read with the Artifact tool's comments action when asked; reply and resolve only threads sent to Claude.

## Status Memory

`templates/artifact_status_memory.md`. Update at every session close. It carries: URL, source path, backups, frozen copies with recipients and dates, superseded ids, palette and structural decisions, which numbers are authoritative, open items, next step.

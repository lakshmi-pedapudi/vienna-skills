---
name: <artifact-slug>-status
description: "Status of the <title> artifact (<project>): URL, source file, backups, frozen copies, superseded ids, authoritative numbers, open items. Read before any edit or republish."
metadata:
  type: project
---

Artifact "<Title>" for <audience>, <purpose>. Source `<project>/<topic>/<name>.html`. Publish by passing the URL below as `url`; publishing without it forks a new artifact.

**Why:** <first publish date; what round it is in>.
**How to apply:** read before touching the file. Names the one editable artifact, the frozen copies, and which numbers are current.

## Artifacts

- **Live (editable):** <URL>. Favicon <emoji>. Last published <date>; sections changed: <list>.
- **Frozen (sent externally, do not edit):** <URL or mirror>, sent <date> to <recipient>.
- **Superseded (do not edit):** <URL or id>, reason.
- **Backups:** `<name>.html.bak_<date>` (<state>).
- **Mirror:** `railway_<name>/index.html` at <subdomain>, deployed <date>.
- **Exports:** `for_<recipient>/<name>.pdf`, `.pptx`, `.md`.

## Structure and Design Decisions

Sections in order with status. Palette and modality colours. Components reused from other artifacts. Stakeholder format constraints ("very compact model comparison").

## Which Numbers Are Authoritative

- Source files or registry, dated. Row sets named.
- Superseded numbers, never to reuse.
- Pending: <what, owner>.

## Open Items

- Review comments not yet applied (Remove / Add lists with closure status).
- Broken or unverified renders.
- Git status of the folder; backing CSVs location.

## Immediate Next Step

One line.

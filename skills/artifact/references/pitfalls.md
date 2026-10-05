# Pitfalls

Applies to: the moments a shortcut looks reasonable. Each line points to the file where the full rule lives.

## Rationalisations

| Thought | Reality |
|---|---|
| "A fresh publish is simpler than finding the URL" | It forks the page and loses the review trail. Find the URL in the status memory. (`publish.md` §Publishing) |
| "The scratchpad is fine for now" | Scratchpads are cleared. Project folder first, then publish. (`workflow.md` Folder Layout) |
| "This paragraph is only four sentences" | The limit is three. Bullets, a table or a chart. (`style.md` §Prose Limits) |
| "A confidence note helps the reader" | Readers skip caveat blocks. One plain sentence at most. (`style.md` §Caveats and Footnotes) |
| "A vague label is safer than the vendor name" | If naming is cleared, the euphemism hides the comparison. Ask once if unsure. (`style.md` §Standalone) |
| "This unflattering number is the key finding, make it a tile" | It goes inline with its qualifier. (`style.md` §Numbers) |
| "A 'What This Page Covers' section orients the reader" | That is self-reference. The structure orients the reader. (`style.md` §Standalone) |
| "I will tidy the wording while I am in there" | Change only what was asked. Say what moved versus what is new. (`workflow.md` §3) |
| "Only two sections changed, no need to sweep the rest" | Reconcile latest to earliest; stale sections are the most common miss. (`workflow.md` §3) |
| "The publish succeeded, so it renders" | Open it. Blank sections have shipped. (`publish.md` §Publishing) |
| "A chart library would be faster" | Blocked by the page's security policy and by house rule. Inline SVG or a data URI. (`design.md` §Charts) |
| "Move it to a personal account to share it" | Pages can carry production data. Export or mirror with authorisation. (`publish.md` §Distribution Routes) |

## Common Failure Modes

- Too many sections and too much prose in a first draft. (`workflow.md` §1, `style.md` §Prose Limits)
- Headings that narrate, ask, or take the "X not Y" shape. (`style.md` §Headings)
- A percentage with no named denominator, or an inflated derived count. (`style.md` §Numbers)
- A query result shown without checking it against the page's own headline. (`style.md` §Numbers)
- An overcorrection that trades one complaint for its opposite. (`workflow.md` §3)
- A single regex edit across the page, or an anchor that silently matched nothing. (`workflow.md` §2 Editing the Source)
- Tile rows that wrap into a column in the PDF. (`design.md` §Layout)
- An edit made on the frozen or staging copy instead of the live one. (`publish.md` §Freezing, §Staging)

# vienna-skills

Three [Claude Code](https://claude.com/claude-code) skills for producing research communication with evidence discipline: an arXiv paper, a slide deck, and a published HTML page (Claude artifact). Extracted from skills in daily use on an applied ML team since 2026, with every person, organisation, vendor and funder replaced by a role. What remains is the method: how the work is sequenced, what the author is asked and when, which words are banned, where numbers may appear, and the scripts that check all of it before anything ships.

## Skills

| Skill | Command | What it does |
|-------|---------|--------------|
| [paper](docs/skills/paper.md) | `/paper` | Use when writing, reviewing, or revising a research paper, arXiv preprint, whitepaper, or the reviewer-facing HTML artifact that precedes one, for a research or product team. |
| [deck](docs/skills/deck.md) | `/deck` | Use when building, revising, reviewing, or converting a slide deck or presentation for a research or product team: board or leadership decks, funder or workshop decks, partner pre-reads, CEO talks, methodology decks, tech updates, Google Slides or PDF exports. |
| [artifact](docs/skills/artifact.md) | `/artifact` | Use when building, revising, reviewing, publishing, or exporting a Claude artifact (a published HTML page) for a research or product team: pre-reads for funders or partners, analysis reports and dashboards, methodology articles, reviewer-facing paper drafts, design documents, findings pages with charts and example tables. |

Each skill is a folder with `SKILL.md` (trigger, phase table, non-negotiables, red flags), `references/` (workflow, style, review, dated lessons), `templates/` and `scripts/` (gates that exit non-zero). Claude Code loads the skill when the task matches the description or when you type the slash command.

## Three Rules Shared by All Three

1. **Evidence upward, one element at a time.** Materials first, an approved skeleton second, then one section, table or chart per iteration. Nothing is invented to look complete; a missing number renders as a visible pending marker with an owner.
2. **Checkpoint questions, even when running unattended.** At topic segregation, skeleton, rough themes and before any restructure, the skill stops and asks one or two short questions with a recommended option. Nowhere else.
3. **Convergent review.** Review runs as a loop of two to three passes. Each pass re-verifies every earlier fix by id, and the loop stops only when two successive passes agree. Logged in `REVIEW_LOG.md`.

## Install

```bash
npm install -g vienna-skills
vienna-skills install                    # symlinks into ~/.claude/skills
vienna-skills install --target all       # Claude Code, Codex (~/.codex/skills) and ~/.agents/skills
vienna-skills list                       # what is installed where
vienna-skills doctor                     # links resolve, python-pptx, matplotlib, dot, perl present
vienna-skills update                     # npm update, then relink
vienna-skills uninstall --target all
```

Or without installing globally:

```bash
npx vienna-skills install --target all
```

Or from a clone (the same CLI, run in place):

```bash
git clone https://github.com/lakshmi-pedapudi/vienna-skills.git && cd vienna-skills
bash install.sh --target all      # wraps bin/vienna-skills install
```

Or as a Claude Code plugin:

```
/plugin marketplace add lakshmi-pedapudi/vienna-skills
/plugin install vienna-skills@vienna-skills
```

Skills are symlinked, so `npm update -g vienna-skills` or `git pull` refreshes them in place. Prerequisites for the scripts: `python3` with `python-pptx`, `matplotlib`, `pillow` (deck), Graphviz `dot` (deck and paper figures), `perl` (paper style gate). Paths inside the references assume `~/.claude/skills/<name>`; adjust for other runtimes.

## Adaptation

- Palettes and typography are constants at the top of `skills/deck/scripts/deck_primitives.py` and in `skills/artifact/templates/page_skeleton.html`. Replace the corporate example with your brand once; everything downstream reads it.
- Banned-word lists live in `skills/paper/scripts/check_style.sh`, `skills/deck/scripts/check_words.py` and `skills/artifact/scripts/check_html.py`. Edit them to your house style.
- The review-comment prefix (`Reviewer:`) and the figures-registry columns are documented in each skill's `references/review.md` and `references/build.md`.
- `references/lessons.md` in each skill is a dated record of the corrections that produced the rules. Keep appending your own; the rules stay honest when the reasons stay attached.

## Related

- [claude-code-workflows](https://github.com/lakshmi-pedapudi/claude-code-workflows): twelve slash commands for reproducible ML engineering.
- [journal-system](https://github.com/lakshmi-pedapudi/journal-system) and [ideation-system](https://github.com/lakshmi-pedapudi/ideation-system): the personal-workflow templates these skills grew up beside.

## License

MIT.

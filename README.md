# vienna-skills

Three [Claude Code](https://claude.com/claude-code) skills for producing research communication with evidence discipline: an arXiv paper, a slide deck, and a published HTML page (Claude artifact). Extracted from skills in daily use on an applied ML team since 2026, with every person, organisation, vendor and funder replaced by a role. What remains is the method: how the work is sequenced, what the author is asked and when, which words are banned, where numbers may appear, and the scripts that check all of it before anything ships.

## Skills

| Skill | Command | What it does |
|-------|---------|--------------|
| [paper](docs/skills/paper.md) | `/paper` | Use when writing, reviewing, or revising a research paper, arXiv preprint, whitepaper, or the reviewer-facing HTML artifact that precedes one. |
| [deck](docs/skills/deck.md) | `/deck` | Use when building, revising, reviewing, or converting a slide deck or presentation: board or leadership decks, funder, partner or customer decks, workshop decks, pre-reads, executive talks, methodology decks, tech updates, Google Slides or PDF exports. |
| [artifact](docs/skills/artifact.md) | `/artifact` | Use when building, revising, reviewing, publishing, or exporting a Claude artifact (a published HTML page): pre-reads for external stakeholders, analysis reports and dashboards, methodology articles, reviewer-facing paper drafts, design documents, findings pages with charts and example tables. |

Each skill is a folder with `SKILL.md` (overview, inputs, outputs, workflow, quality standards, limitations, troubleshooting), `references/` (workflow, style, review, pitfalls and topic guides), `templates/` and `scripts/` (gates that exit non-zero, with house word lists in editable config files). Claude Code loads the skill when the task matches the description or when you type the slash command.

## Three Rules Shared by All Three

1. **Evidence upward, one element at a time.** Materials first, an approved skeleton second, then one section, table or chart per iteration. Nothing is invented to look complete; a missing number renders as a visible pending marker with an owner.
2. **Checkpoint questions, even when running unattended.** At topic segregation, skeleton, rough themes and before any restructure, the skill stops and asks one or two short questions with a recommended option. Nowhere else.
3. **Convergent review.** Review runs as a loop of two to three passes. Each pass re-verifies every earlier fix by id, and the loop stops only when two successive passes agree. Logged in `REVIEW_LOG.md`.

## Install

From a clone (the CLI runs in place):

```bash
git clone https://github.com/lakshmi-pedapudi/vienna-skills.git && cd vienna-skills
bash install.sh --target all                 # wraps bin/vienna-skills install
bin/vienna-skills install                    # symlinks into ~/.claude/skills
bin/vienna-skills install --target all       # Claude Code, Codex (~/.codex/skills) and ~/.agents/skills
bin/vienna-skills list                       # what is installed where
bin/vienna-skills doctor                     # links resolve, python-pptx, matplotlib, dot, perl present
bin/vienna-skills update                     # git pull, then relink
bin/vienna-skills uninstall --target all
```

Or as a Claude Code plugin:

```
/plugin marketplace add lakshmi-pedapudi/vienna-skills
/plugin install vienna-skills@vienna-skills
```

Skills are symlinked, so `git pull` (or `bin/vienna-skills update`) refreshes them in place. Prerequisites for the scripts: `python3` with `python-pptx`, `matplotlib`, `pillow` (deck), Graphviz `dot` (deck and paper figures), `perl` (paper style gate). References write script paths as `<skill-dir>`, wherever the skill is installed. Deck build scripts read it from `DECK_SKILL_DIR` (default `~/.claude/skills/deck`).

## Adaptation

- Palettes and typography are constants at the top of `skills/deck/scripts/deck_primitives.py` and in `skills/artifact/templates/page_skeleton.html`. Replace the corporate example with your brand once; everything downstream reads it.
- House word lists are config files, not code: `skills/paper/scripts/banned_words.txt` and `allow.txt`, `skills/deck/scripts/house_words.json`, `skills/artifact/scripts/house_words.json`. Edit them to your house style, or point a gate at another file with `--words`. Built-in checks (em-dashes, AI-tell and hype phrases, sentence-shape warnings) stay in the scripts.
- The review-comment prefix defaults to `REVIEW:` (the 1.0 default `Reviewer:` still matches); pass `--prefix` (repeatable) to `extract_review_comments.py` for your own. The figures-registry columns are documented in `skills/deck/references/build.md`.
- `references/pitfalls.md` in each skill lists the rationalisations and failure modes that the rules exist to stop, each pointing to the file that holds its rule. Add your own as rules in the relevant reference file, with a one-line reason.

## Changes in 1.1.0

- Every `SKILL.md` follows one layout: Overview, When to Use, Inputs, Outputs, Workflow, Quality Standards (with a gate-script table), Reference Guides, Limitations, Troubleshooting.
- `references/lessons.md` is replaced by `references/pitfalls.md`. The dated corrections are condensed into rules with reasons inside the reference files.
- New "Sentence Shapes" rules in all three style guides ("not A, but B" pivots, padded lists, stacked adjectives, taglines, recap endings, narrated structure). Paper and artifact gates warn on them; all gates fail on hype phrases.
- House word lists moved to config files. New options: `--allow` and a per-paper `.paper-style-allow` (paper), `--words`, `--codes`, `--external` (deck words), `--exempt-file` (deck figures, paper numbers), `--words` and `--id-pattern` (artifact).
- Deck: the review-comment prefix default is `REVIEW:`, and the 1.0 default `Reviewer:` still matches; build scripts locate the skill through `DECK_SKILL_DIR`.
- Paper: the number-placement gate reports correct line numbers after tables and maths.
- Artifact: paragraph and section thresholds match the style rules; the script CDN allowlist is cdnjs and jsdelivr/npm only.

## Related

- [claude-code-workflows](https://github.com/lakshmi-pedapudi/claude-code-workflows): twelve slash commands for reproducible ML engineering.
- [journal-system](https://github.com/lakshmi-pedapudi/journal-system) and [ideation-system](https://github.com/lakshmi-pedapudi/ideation-system): the personal-workflow templates these skills grew up beside.

## License

MIT.

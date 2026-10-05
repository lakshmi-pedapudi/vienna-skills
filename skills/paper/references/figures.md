# Figures and Tables

Applies to: diagrams, data charts, illustration figures and tables in the artifact and the LaTeX paper, including their placement, palette and formatting.

Use visualisations, tables, charts and flowcharts wherever they carry the point faster than prose. A figure earns its place when a cold reader sees a mechanism they would otherwise assemble from prose. If a sentence says it faster, write the sentence. If a chart confuses, use a table.

## Toolchain

- Diagrams: Graphviz DOT in `figures/fig_*.dot`, rendered by `build.sh` to PDF (LaTeX) and SVG (artifact). Never Mermaid (house default).
- Data charts: `figures/make_charts.py` (matplotlib), reading CSVs from `paper/materials/` where possible so the chart regenerates when data changes. Emits print PDF and SVG, plus a CSS-variables SVG for the artifact so it themes light and dark.
- Artifact flowcharts: hand-authored inline `<svg>` per the `artifact-diagramming` skill (viewBox sizing, `currentColor` strokes, marker arrowheads, labelled arrows, `<figure>` with `<figcaption>`, no `<style>` or `<script>` inside the SVG).
- Illustration figures inside LaTeX (example boxes, pyramids, legends): TikZ, kept simple.
- No metrics baked into raster images. Results change; images cannot be edited. Charts are separate source files in a folder, regenerated from data.
- Load the `dataviz` skill before authoring any chart.

## Palette

House defaults; a paper may override them in its status memory.

- One accent (rust `#A6472B`) for flags, proposed items and emphasis; neutrals for everything else; hatch texture and direct labels so the chart reads in greyscale.
- Blue and green are reserved for the two routes (Route A, Route B) and used identically in the artifact tokens, the charts and the LaTeX figures.
- A multi-hue categorical set can fail colour-vision-deficiency checks. Never rely on green versus rust alone; add hatch, labels or position.
- Typography in artifacts: IBM Plex Sans, IBM Plex Mono, a serif for headings (Newsreader or Source Serif 4), loaded from Google Fonts with a fallback stack.

## What a Figure Must Show

- The mechanism and the decision, not a linear chain of boxes. When two routes exist, draw the orchestration between them rather than a single pipeline.
- Decision nodes name their criteria (case, coverage, reliability, cost, latency).
- Comparing options: draw the difference, side by side, with the edge each option adds or removes.
- Labels are plain words. If a label confuses a reader, rename it in the figure and the text together (with the author's agreement; see `style.md`, Naming Consistency).
- Pipeline figures: main flow as boxes, intermediate operations in parentheses on the arrows, no overlapping boxes, aligned baselines, uniform font size, legend inside the page. Three or four rows of connected boxes beat one long chain. *Why: a long chain wastes width and shrinks the text.*
- Size the figure to its content, not to the text width by default. Shrink the figure and its font together, then check the rendered page for text touching or crossing a box boundary.
- Pick whichever form the reader parses faster. A multi-stage funnel carrying many numbers often reads better as a funnel figure with one worked example per stage than as a table; a confusing chart (odd orientations, too many markers) loses to a simple table. Say which was chosen and why.
- Add a worked example beside any definition, label set or pair taxonomy. An example column earns its width.
- Coverage charts show the full tail (to near 100%) with the named thresholds (Top 20, Top 30, Top 40) marked.
- Error distribution by category is the load-bearing figure for any recognition-error paper, with a concrete row-level example beside the aggregate. The category set comes from the domain's own term types.
- Unflattering numbers stay, in context, never as a hero stat: "X% rejected at <stage> before <next stage> runs", not a bare "X%".
- Ablation: a detailed line chart in addition to the table when the point is a curve (data scale versus quality); saturation visible.
- Cost versus performance: a simple table (model, cost, F1) usually beats a scatter. Use the paper's own cost figures where they exist; otherwise web-search and cite the pricing date.

## Process

Specify, render, review, integrate. The author supplies or approves a node-and-edge spec, sees the render, then it goes into the document. Geometry is checked on the rendered page (too wide, too large on the page, overlapping parts).

## Figure and Table Placement (LaTeX)

- A figure or table appears at or before the first section that references it, in numeric order (Fig. 1 before Fig. 2). Two-column figures in IEEEtran float unpredictably; use `[t]` or `[!t]` with `figure*`, or `\FloatBarrier`, and check the compiled PDF, not the source order.
- Fix placement until the PDF, not the `.tex`, is right; report placement by page and section. *Why: source order says nothing about where a float lands.*
- Captions follow `style.md`, Captions: name what the object shows and its one denominator, at most 15 to 20 words, no result values. Consistent styling across all figures.
- A screenshot of an internal tool carries a caption note that specific user inputs are illustrative.

## Tables

This is the single home for table formatting rules.

- LaTeX tables use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), no vertical rules, `tabularx` when a text column must wrap. The house preamble loads both.
- Fit the column. Tighten spacing, abbreviate headers, or span two columns (`table*`) before shrinking fonts below legibility. Splitting a table is a last resort and an aesthetic call to make explicitly.
- Bold the best value per column and state the convention in a table note. Bold that is not the column maximum is an error. Bold the best row per block when the table is grouped.
- Colour the best value green where the document uses colour, and keep it bold. Never red for a good value. *Why: red reads as an error, whatever it marks.*
- A Yes/No column becomes a green tick and a red cross, with the words kept in the header (`pifont` or `amssymb` in the preamble). *Why: ticks read faster than repeated words down a column.*
- When the table's subject is the metric set, Metric is the first column and holds nothing else; the rest is one plain description column. Drop grouping and score-range columns.
- A two-column id-to-name table sits immediately before the results table it explains, so the reader is not paging back for what S2 or M1 means.
- Confidence intervals come out unless the argument is about uncertainty. Two narrower side-by-side tables beat one wide one.
- One row per model; where a model has several variants, show the best one and say which.
- Percentages over counts; drop Median and N columns unless they carry the argument; show the declined or abstained share as its own column; state the row basis in the caption.
- Multi-denominator tables show each denominator as its own column with a header that names it.
- Merge paired columns into one intuitive label and use the same label in the body.
- Long prompts do not go in tables; link the repository or put them in appendix boxes.
- In-cell translucent bars against each accuracy value help a table read visually in the artifact.
- When the author asks for an empty column (for example Comments to fill later), leave it empty rather than fill it with caveats.

## Illustration Figures

Pattern for illustration figures: a question and two answers in boxes, phrases highlighted with background colours keyed to a single-column legend table with row borders; uniform font size throughout; legend inside a bounding box; black text on coloured backgrounds; the concept defined in the section text, not in the figure.

## Treemaps and Dense Charts

Treemaps: fixed cell count per category (1 to 5), dynamic thresholds so the smallest cell stays readable, wrapped text with one newline between fields, bold category name plus count, no duplicate word across categories, short glosses ("units", not "a unit of measurement"), a "not equal" sign rather than an arrow, critical-severity pairs only. Non-Latin examples follow `submission.md`, arXiv Package.

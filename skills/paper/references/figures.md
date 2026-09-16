# Figures, Charts, and Tables

"Focus on visualizations, tables, charts, plots, flowcharts as much as possible." A figure earns its place when a cold reader sees a mechanism they would otherwise assemble from prose. If a sentence says it faster, write the sentence. If a chart confuses, use a table.

## Toolchain

- Diagrams: Graphviz DOT in `figures/fig_*.dot`, rendered by `build.sh` to PDF (LaTeX) and SVG (artifact). Never Mermaid.
- Data charts: `figures/make_charts.py` (matplotlib), reading CSVs from `paper/materials/` where possible so the chart regenerates when data changes. Emits print PDF and SVG, plus a CSS-variables SVG for the artifact so it themes light and dark.
- Artifact flowcharts: hand-authored inline `<svg>` per the `artifact-diagramming` skill (viewBox sizing, `currentColor` strokes, marker arrowheads, labelled arrows, `<figure>` with `<figcaption>`, no `<style>` or `<script>` inside the SVG).
- Illustration figures inside LaTeX (example boxes, pyramids, legends): TikZ, kept simple.
- No metrics baked into raster images. Results change; images cannot be edited. Charts are separate source files in a folder, regenerated from data.
- Load the `dataviz` skill before authoring any chart.

## Palette

- One accent (rust `#A6472B`) for flags, proposed items, and emphasis; neutrals for everything else; hatch texture and direct labels so the chart reads in greyscale.
- Blue and green are reserved for the two routes (Route A, Route B) and used identically in the artifact tokens, the charts, and the LaTeX figures.
- The artifact palette failed colour-vision-deficiency checks as a multi-hue categorical set. Never rely on green-versus-rust alone; add hatch, labels, or position.
- Typography in artifacts: IBM Plex Sans, IBM Plex Mono, a serif for headings (Newsreader or Source Serif 4), loaded from Google Fonts with a fallback stack.

## What a Figure Must Show

- The mechanism and the decision, not a linear chain of boxes. "The diagram right now is just a pipeline. If I were to demonstrate that as an orchestration of Route A and Route B, how would I do it?"
- Decision nodes name their criteria (case, coverage, reliability, cost, latency).
- Comparing options: draw the difference, side by side, with the edge each option adds or removes.
- Labels are plain words. If a label confuses a reader ("Route"), rename it in the figure and the text together.
- Pipeline figures: main flow as boxes, intermediate operations in parentheses on the arrows, no overlapping boxes, aligned baselines. Three or four rows of connected boxes beat one long chain.
- Size the figure to its content, not to the text width by default. Shrink the figure and its font together, then check the rendered page for text touching or crossing a box boundary: "reduce the size of the overall figure. take care of text overlap with box boundaries."
- A multi-stage funnel carrying many numbers reads better as a funnel figure with one worked example per stage than as a table: "table is very confusing with the numbers." This sits beside the opposite lesson ("a confusing figure loses to a simple table"); pick the form the reader parses faster and say which was chosen and why.
- Add a worked example beside any definition, label set or pair taxonomy. An example column earns its width.
- Coverage charts show the full tail (to near 100%) with the named thresholds (Top 20, Top 30, Top 40) marked.
- Error distribution by category is the load-bearing figure for any recognition-error paper, with a concrete row-level example beside the aggregate. The category set comes from the domain; an agronomy pipeline used crop, pest or disease, chemical or fertilizer, unit or dose, practice, general.
- Unflattering numbers stay, in context, never as a hero stat: "X% rejected at the quality gate before diagnosis runs", not a bare "X%".
- Ablation: a detailed line chart in addition to the table when the point is a curve (data scale versus quality); saturation visible.
- Cost versus performance: a simple table (model, cost, F1) beat a confusing scatter. Wherever the paper has a cost figure use it; otherwise web-search and cite the pricing date.

## Process

Specify, render, review, integrate. The author supplies or approves a node-and-edge spec, sees the render, then it goes into the document. Geometry is checked on the rendered page ("it is too wide", "images on page 1 are too large", "top and bottom parts overlap").

## Figure and Table Placement (LaTeX)

- A figure or table appears at or before the first section that references it, in numeric order (Fig. 1 before Fig. 2). Two-column figures in IEEEtran float unpredictably; use `[t]` or `[!t]` with `figure*`, or `\FloatBarrier`, and check the compiled PDF, not the source order.
- The author checks placement in the PDF and reports it by page and section ("Section 3.3 is on page 3, Fig 2 on page 4, Table 2 on page 5"). Fix until the PDF, not the `.tex`, is right.
- Descriptive captions that state the claim. Consistent styling across all figures.
- A screenshot of an internal tool carries a caption note that specific user inputs are illustrative.

## Tables

- LaTeX tables use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), no vertical rules, `tabularx` when a text column must wrap. The house preamble loads both.
- Fit the column. Tighten spacing, abbreviate headers, or span two columns (`table*`) before shrinking below legibility. Splitting a table is a last resort and an aesthetic call to make explicitly.
- Bold the best value per column and state the rule in a table note. Bold the best row per language block when the table is grouped. Green and bold where the document uses colour; never red for a good value.
- Yes/No columns become green ticks and red crosses. Captions stay inside the 15-to-20-word cap in `style.md`; overflow becomes a note line under the table.
- One row per model; where a best-speaker variant exists, show only that variant.
- Percentages over counts; drop Median and N columns unless they carry the argument; show declined or abstained share as its own column; state the row basis in the caption.
- Merge paired columns into one intuitive label and use the same label in the body.
- Long prompts do not go in tables; link the repository or put them in appendix boxes.
- In-cell translucent bars against each accuracy value help a table read visually in the artifact.
- Leave a column empty rather than fill it with caveats when the author asks for a "Comments" column with nothing in it yet.

## Illustration Figures

The specificity illustration in the SFT paper set the pattern: question and two answers in boxes, phrases highlighted with background colours keyed to a single-column legend table with row borders; uniform font size throughout; legend inside a bounding box; black text on coloured backgrounds; a definition of the concept in the section text, not in the figure.

## Treemaps and Dense Charts

Lessons from one paper's error-category treemaps: fixed cell count per category (1 to 5), dynamic thresholds so the smallest cell stays readable, wrapped text with one newline between fields, bold category name plus count, no duplicate word across categories, short glosses ("units" not "a unit of measurement"), "not equal" sign rather than an arrow, critical-severity pairs only. Romanize non-Latin examples when the renderer cannot handle the script.

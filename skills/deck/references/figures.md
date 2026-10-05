# Figures

Applies to: choosing a chart, table or diagram for a slide, drawing it, colouring it, and the sample images or records shown in a deck.

Put visuals first: tables, charts, plots and flowcharts wherever they carry the content. A figure earns its place when a cold reader sees a mechanism or a distribution they would otherwise assemble from text. If a table says it faster, draw the table. If a chart misleads or confuses, delete it first and decide on a replacement second.

## Choosing the Form

- N items of the same shape: a native table, not bullets and not an image.
- Volume over time or across geography: separate charts by month, by region, and by both. *Why: monthly series show seasonality that a six-month aggregate hides.*
- Latency or any timing: distributions, not averages. Histogram with quartiles, P90 and P95 marked so bimodality and outliers show. Waterfalls use proportional block widths tied to measured values. One slide per finding: the distribution, two or three real example rows per mode, a short explanation, the fix.
- Coverage: cumulative curve extended to near 100% with the tail visible and reference lines at the decision points (Top 20, Top 30, Top 40).
- Comparing options: side by side on one slide with matching flowcharts and minimal text, so they read as one line of thinking with different implementations. Frame accuracy, cost and latency as a tradeoff, not a leaderboard; a radar chart is acceptable for multi-metric comparison.
- Pipelines: establish the pipeline visually up front with four or five plain boxes so later slides can name its stages. Main flow as boxes, operations on the arrows, no overlaps, aligned baselines.
- A good chart removes a section. Example: a small bar chart with one colour for the evaluated models and another for the held-out ones replaces a whole sub-section of text.
- If a table overwhelms, replace it with a visual or split it. Do not shrink the font or add columns.
- Show, do not state: if the message is "this goes to human review", draw it and give it deliberate visual prominence.

## Drawing Rules

- When a figure carries the argument, it is the dominant element on the slide and the text is secondary. *Why: attention goes to the largest element first; if that is the text, the figure is skipped.* Example: a flowchart that explains the whole strategy takes most of the slide, with two short points beside it.
- Every colour encoding is labelled next to the mark it encodes. Remove legends that obstruct or add nothing.
- Percentages on a chart add up to something the reader can verify. Stacked or grouped bars normalise the way a reader expects, or the chart changes.
- Bars are proportional. A static bar with the number beside it is a defect.
- Colour-code table rows by their role (your planned models versus existing baselines) so the grouping reads without reading.
- In-cell translucent bars against each value help a comparison table read visually.
- Colour carries consequence: high-consequence categories in the accent, the rest muted.
- Full range on the axis; no truncation that flatters.
- Sizing instructions are literal: "width 75% of current, 10% taller" means exactly that.
- Diagram polish goes down to arrow curvature, arrow length and box gaps. Straight short arrows, even spacing, overall width trimmed to fit.
- Split a diagram that has shrunk to illegibility into several; the strategically important one gets the most space. Then do not over-correct: separated diagrams return to normal size, not oversized.
- Strip internal identifiers from diagrams (prompt ids, codes). After a subsystem is shown in detail once, collapse it to one box.
- Diagrams carry no title of their own and no measurements.

## Colour

- Palette values live in `build.md` §Palettes, single-sourced in the script.
- Fixed colour per category across every chart in the set (`build.md` §Palettes).
- Charts must read in greyscale: hatch or direct labels, never hue alone.

## Process

Propose the chart form before building it, offer options numbered, render standalone, iterate on width, labels, arrows and title, then wire into the deck. Chart specs may arrive as stacks, groups and palette, or as JSON node and edge lists for diagrams; follow them exactly, global aggregate first.

## Sample Images and Records

Examples shown on a slide (photos, messages, records) come from the real source data, span distinct cases, and are screened for personal data (faces, documents, GPS overlays, minors, watermarks, names, phone numbers) before they ship. Captions are plain, with no methodological parentheticals.

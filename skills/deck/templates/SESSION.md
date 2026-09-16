# Session Record: <Deck Name>

Built <date> for <occasion, date>. Records what was consulted, what was produced, and what is still open, so the folder is self-explanatory in a month.

## Purpose

<Two or three sentences: who asked, for whom, what the deck must do.>

## Sources Consulted

| Source | What it gave |
|---|---|
| | |

## Produced

| File | Purpose |
|---|---|
| `<deck>.pptx` | |
| `build_deck.py` | Deck build script |
| `charts/gen_*.py` | Charts and diagrams |
| `analysis/figures.csv` | Figures registry |

## Reproduce

```bash
cd <deck folder>
python3 charts/gen_charts.py
for f in <diagram names>; do dot -Tsvg $f.dot -o charts/$f.svg; dot -Tpng -Gdpi=170 $f.dot -o charts/$f.png; done
python3 build_deck.py
S=~/.claude/skills/deck/scripts
python3 $S/check_layout.py <deck>.pptx && python3 $S/check_figures.py --deck <deck>.pptx --registry analysis/figures.csv && python3 $S/check_words.py <deck>.pptx --names names.txt
python3 $S/preview_slides.py <deck>.pptx      # read preview/slide_N.png
```

Requires matplotlib, python-pptx, Pillow, graphviz on PATH.

## The Claim Set, and Where Each Number Came From

Everything quoted in the deck traces to one of these. No estimates.

- <number, row set>: <file or report>.

## Caveats to Carry into the Room

- <what the data cannot support, said plainly>.

## Still Open

1. <item, owner>.
2. Git status of this folder.

"""Gate for where result numbers live in a LaTeX paper.

Author ruling: experiment results are quoted in four homes only, Abstract, Introduction,
Results, Conclusion. Other sections describe and cite a table or figure by number.
Figures, flowcharts and captions carry structure, not result values, unless the figure
is itself a chart drawn from the data.

    python3 check_number_placement.py <arxiv_paper dir> [--allow REGEX ...] [--data-dir DIR ...] [--strict]

What it does
  FAIL  result-type numerals (percentages, decimals, counts of four or more digits,
        currency, ms/s/MB values) in the prose of any sections/*.tex whose name is not
        an allowed home. Text inside table environments, math, comments, \\cite, \\ref,
        \\label, \\includegraphics and macros' arguments is skipped: tables are allowed
        carriers anywhere.
  warn  result-type numerals inside \\caption{...} in any section, and inside label text
        of figures/*.dot (a hand-authored diagram printing a value).
  warn  a chart output (figures/chart_*.{pdf,svg}) older than any CSV in the data dirs
        (default: figures/, ../paper/materials, ../materials), which means the chart was
        not regenerated after its data changed.

Allowed homes are matched on the section file name: abstract, intro, introduction,
results, conclusion (case-insensitive). Add --allow to extend (for example --allow impact
when a production-rollout section carries its own metrics table).

Exemptions inside prose: years (19xx, 20xx), section/figure/table references, ids
(M0, E1, RQ1, B0, P1, S1, Route A), model names with digits, ordinals, percentile
labels, small bare integers (three digits or fewer, no unit, no decimal).

A source line ending in "% number-ok: <reason>" is exempt from the prose scan. Use it
for a method parameter or a dataset count defined in that sentence, never for a result.

Exit 1 on any FAIL; --strict also fails on warnings.
"""
import argparse
import re
import sys
from pathlib import Path

HOMES = re.compile(r"(abstract|intro|introduction|results|conclusion)", re.I)

# a numeral that reads as a result value
RESULT_NUM = re.compile(
    r"(?<![A-Za-z0-9.\-])"
    r"(?:"
    r"\$?\s?\d{1,3}(?:,\d{3})+(?:\.\d+)?"            # 1,163,658  $3,014
    r"|\$\s?\d+(?:\.\d+)?"                           # $0.012
    r"|\d+\.\d+"                                     # 0.81  90.29
    r"|\d{4,}"                                       # 12246 (years handled below)
    r"|\d+(?:\.\d+)?[\s~]*(?:\\%|%|ms\b|s\b|MB\b|GB\b|EUR\b|USD\b|dB\b|min\b|minutes\b|seconds\b|hours\b)"
    r")"
)
EXEMPT = [
    re.compile(p, re.I) for p in (
        r"\b(?:19|20)\d{2}\b",                                        # years
        r"\\(?:ref|eqref|autoref|cref|Cref|label|cite[tp]?|citeauthor|pageref)\*?\{[^}]*\}",
        r"\\includegraphics(?:\[[^\]]*\])?\{[^}]*\}",
        r"\\(?:input|include|bibliography|url|href)\{[^}]*\}",
        r"\b(?:Section|Sec\.|Table|Tab\.|Figure|Fig\.|Appendix|Eq\.|Equation)~?\s*\d+(?:\.\d+)*",
        r"\b(?:M|E|B|P|S|RQ|C|R)\d{1,2}\b",                           # ids
        r"\bRoute\s+[AB]\b",
        r"\b(?:GPT|Qwen|Gemini|Gemma|Llama|Claude|Sonnet|Opus|Haiku|Whisper|IndicWhisper|Sarvam|Conformer|Canary|Parakeet|wav2vec|MMS|Deepgram|DaViT|YOLO|MobileNet|EfficientNet|ConvNeXt|ViT|Kimi|Pixtral|Mistral|Mixtral|Chirp|DFN|DeepFilterNet|Phi|Grok|Nova|Titan|L40S|A100|H100)(?:[\w\-.]*|[\s~])\d[\w\-.]*",
        r"\b\d+(?:st|nd|rd|th)\b",
        r"\bp\d{1,3}\b|\bF1\b|\bF\d\b",
        r"\bv\d+(?:\.\d+)*\b",                                        # versions
        r"\\(?:pilot|todo|flag)\b",
    )
]
TABLE_ENVS = ("table", "table*", "tabular", "tabular*", "tabularx", "longtable", "booktabs", "threeparttable")
MATH_ENVS = ("equation", "equation*", "align", "align*", "gather", "math", "displaymath")


def strip_env(text, envs):
    for env in envs:
        e = re.escape(env)
        text = re.sub(r"\\begin\{" + e + r"\}.*?\\end\{" + e + r"\}", " ", text, flags=re.S)
    return text


OPT_OUT = re.compile(r"%\s*number-ok\b", re.I)


def strip_comments(text):
    """Drop LaTeX comments. A line ending in '% number-ok: <reason>' is blanked entirely:
    the author has said this value belongs here (a method parameter, a dataset size that
    the sentence defines). The reason stays visible in the source."""
    kept = []
    for line in text.split("\n"):
        if OPT_OUT.search(line):
            kept.append("")
        else:
            kept.append(re.sub(r"(?<!\\)%.*", "", line))
    return "\n".join(kept)


def strip_math(text):
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$[^$]*\$", " ", text)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", " ", text, flags=re.S)
    return strip_env(text, MATH_ENVS)


def balanced_arg(text, start):
    """Return the contents of the {...} group starting at text[start] == '{'."""
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i]
    return text[start + 1:]


def captions(text):
    out = []
    for m in re.finditer(r"\\caption\*?(?:\[[^\]]*\])?\{", text):
        out.append(balanced_arg(text, m.end() - 1))
    return out


def dot_labels(txt):
    """Text of every label="..." and every HTML-like label=<...> in a DOT source. Only
    labels are scanned: nodesep, penwidth and margins are layout, not values."""
    out = re.findall(r'label\s*=\s*"([^"]*)"', txt)
    for m in re.finditer(r"label\s*=\s*<", txt):
        depth, i = 0, m.end() - 1
        start = i
        while i < len(txt):
            if txt[i] == "<":
                depth += 1
            elif txt[i] == ">":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        out.append(re.sub(r"<[^>]*>", " ", txt[start + 1:i]))
    return " ".join(out)


def mask(text):
    out = list(text)
    for pat in EXEMPT:
        for m in pat.finditer(text):
            for i in range(m.start(), m.end()):
                out[i] = " "
    return "".join(out)


def numerals(text):
    return [(m.group(0).strip(), m.start(), m.end()) for m in RESULT_NUM.finditer(mask(text))]


def context(text, s, e, width=90):
    pad = max(0, (width - (e - s)) // 2)
    a, b = max(0, s - pad), min(len(text), e + pad)
    return ("…" if a else "") + " ".join(text[a:b].split()) + ("…" if b < len(text) else "")


def line_no(text, pos):
    return text.count("\n", 0, pos) + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paper_dir", type=Path, help="folder holding sections/ and figures/")
    ap.add_argument("--allow", action="append", default=[], metavar="REGEX",
                    help="extra section-name pattern allowed to quote results (repeatable)")
    ap.add_argument("--data-dir", action="append", default=[], type=Path,
                    help="folder(s) holding the CSVs charts draw from (repeatable)")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    root = a.paper_dir.resolve()
    sections = sorted((root / "sections").glob("*.tex")) if (root / "sections").exists() else sorted(root.glob("*.tex"))
    if not sections:
        sys.exit(f"no .tex files under {root}")
    homes = [HOMES] + [re.compile(p, re.I) for p in a.allow]

    fails, warns = [], []

    for f in sections:
        raw = f.read_text(encoding="utf-8", errors="replace")
        is_home = any(h.search(f.stem) for h in homes)
        # captions in every file
        for cap in captions(raw):
            for tok, s, e in numerals(strip_comments(cap)):
                warns.append(("caption carries a value", f.name, None, tok, context(cap, s, e)))
        if is_home or f.stem.lower().startswith("appendix"):
            continue
        body = strip_comments(raw)
        body = strip_env(body, TABLE_ENVS)
        body = strip_math(body)
        # drop caption contents from the prose scan (already warned)
        body = re.sub(r"\\caption\*?(?:\[[^\]]*\])?\{", lambda m: "\\caption{" + " " * 0, body)
        for cap in captions(body):
            body = body.replace(cap, " " * len(cap), 1)
        for tok, s, e in numerals(body):
            fails.append(("result value outside the four homes", f.name, line_no(body, s), tok, context(body, s, e)))

    figdir = root / "figures"
    if figdir.exists():
        for dot in sorted(figdir.glob("*.dot")):
            txt = dot.read_text(encoding="utf-8", errors="replace").replace("\\n", " ").replace("\\l", " ")
            labels = dot_labels(txt)
            for tok, s, e in numerals(labels):
                warns.append(("diagram label carries a value", dot.name, None, tok, context(labels, s, e)))
        data_dirs = a.data_dir or [figdir, root.parent / "paper" / "materials", root.parent / "materials", root / "tables"]
        csvs = [c for d in data_dirs if d.exists() for c in d.rglob("*.csv")]
        newest_csv = max((c.stat().st_mtime for c in csvs), default=None)
        newest_name = max(csvs, key=lambda c: c.stat().st_mtime).name if csvs else None
        if newest_csv:
            for chart in sorted(list(figdir.glob("chart_*.pdf")) + list(figdir.glob("chart_*.svg"))):
                if chart.stat().st_mtime < newest_csv:
                    warns.append(("chart older than its data", chart.name, None, newest_name,
                                  "regenerate with figures/make_charts.py or build.sh"))

    homes_seen = [f.name for f in sections if any(h.search(f.stem) for h in homes)]
    print(f"paper     {root}")
    print(f"homes     {', '.join(homes_seen) or 'NONE MATCHED (check section names or pass --allow)'}")
    print(f"sections  {len(sections)}")
    print()
    if fails:
        print(f"FAIL ({len(fails)}) : result values quoted outside Abstract / Introduction / Results / Conclusion")
        for kind, fn, ln, tok, ctx in fails:
            print(f'  {fn}:{ln}: "{tok}"  in  "{ctx}"')
        print()
    if warns:
        print(f"warn ({len(warns)})")
        for kind, fn, ln, tok, ctx in warns:
            print(f'  [{kind}] {fn}: "{tok}"  {ctx}')
        print()
    print("PASS" if not fails and not (a.strict and warns) else "FAIL")
    sys.exit(1 if fails or (a.strict and warns) else 0)


if __name__ == "__main__":
    main()

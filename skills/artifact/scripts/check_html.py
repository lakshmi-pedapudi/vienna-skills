"""Gate for a Claude artifact HTML file before publishing.

Hard failures (exit 1): em-dashes, banned words, AI tells, jargon, personal names (from a
names file), external chart libraries, Mermaid, a missing <title>, a script src outside
the artifact CDN allowlist.

Warnings (exit 0): paragraphs over 100 words or 4 sentences, more than 8 top-level
sections, headings that read as sentences or "X not Y", self-referential or process
phrases, caveat or footnote blocks, changelog sections, internal ids and file paths, a
theme that is not three-state, images whose src is neither data: nor an existing file,
a body without an explicit background.

    python3 check_html.py page.html [--names names.txt] [--allow REGEX ...] [--strict]

--strict turns warnings into failures.
"""
import argparse
import html as htmlmod
import os
import re
import sys

HARD = [
    ("em-dash", r"—|&mdash;|&#8212;"),
    ("banned word", r"\b(?:arms?|instruments?|licen[cs]e[sd]?|verdicts?|axes|under the rule)\b(?![^<]*</code>)"),
    ("AI tell", r"\b(?:dive into|delve|leverag\w*|robust|seamless\w*|unlock\w*|genuinely|paramount|"
                r"it is worth noting|in today.s|underscor\w* the need|sweet spot)\b"),
    ("jargon", r"\b(?:blast radius|mitigation in flight|force multiplier|fan-?out|operationali[sz]e\w*)\b"),
    ("chart library", r"(?:chart\.js|chartjs|/d3(?:\.min)?\.js|d3js\.org|plotly|recharts|echarts|highcharts|apexcharts|vega)"),
    ("mermaid", r"mermaid"),
]
CDN_OK = r"^https://(?:cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net/npm/|cdn\.tailwindcss\.com|code\.jquery\.com)"

WARN = [
    ("self-reference", r"\b(?:this (?:document|artifact|page|pre-read|deck)|as discussed|earlier discussion|"
                       r"we (?:have )?not yet|not yet (?:solid|verified)|do not carry|out of the room|"
                       r"claims we are not repeating|changes in this version|changelog|what changed)\b"),
    ("caveat block", r"\b(?:caveats?|disclaimer|footnotes?|methodolog\w+ note)\b"),
    ("internal id", r"\b(?:AI-\d+|T\d[a-z]?\b|[A-E]\d(?:\.\w+)?\b|chat_message\w*|\w+\.(?:csv|py|json|md)\b)"),
    ("X not Y heading", r"<h[1-4][^>]*>[^<]*\b(?:not|vs\.?|versus)\b[^<]*</h[1-4]>"),
]
NARRATIVE_HEAD = re.compile(r"^(?:what|how|why|when|where|the |two ways|here|this|we |our )", re.I)


def text_of(fragment):
    return htmlmod.unescape(re.sub(r"<[^>]+>", " ", fragment)).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file")
    ap.add_argument("--names", help="file with one personal name per line")
    ap.add_argument("--allow", action="append", default=[], metavar="REGEX")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    src = open(a.file, encoding="utf-8").read()
    allow = [re.compile(p, re.I) for p in a.allow]
    fails, warns = [], []

    def ok(frag):
        return any(x.search(frag) for x in allow)

    # visible text only for word checks (drop style/script/svg internals)
    visible = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", src, flags=re.S | re.I)
    visible_txt = re.sub(r"<svg.*?</svg>", " ", visible, flags=re.S | re.I)

    rules = list(HARD)
    if a.names:
        names = [l.strip() for l in open(a.names) if l.strip()]
        if names:
            rules.append(("personal name", r"\b(?:" + "|".join(map(re.escape, names)) + r")\b"))
    for kind, pat in rules:
        target = src if kind in ("chart library", "mermaid", "em-dash") else visible_txt
        for m in re.finditer(pat, target, re.I):
            frag = target[max(0, m.start() - 50):m.end() + 50]
            if ok(frag):
                continue
            fails.append((kind, m.group(0), " ".join(text_of(frag).split())[:120]))

    if not re.search(r"<title>[^<]{2,}</title>", src, re.I):
        fails.append(("missing <title>", "", "put <title> in the first 8 KB"))
    for m in re.finditer(r"<script[^>]+src=[\"']([^\"']+)", src, re.I):
        if not re.match(CDN_OK, m.group(1)):
            fails.append(("script src outside CDN allowlist", m.group(1), ""))

    for kind, pat in WARN:
        for m in re.finditer(pat, visible_txt, re.I):
            frag = visible_txt[max(0, m.start() - 50):m.end() + 50]
            if ok(frag):
                continue
            warns.append((kind, m.group(0), " ".join(text_of(frag).split())[:120]))

    for m in re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", visible, re.S | re.I):
        h = text_of(m.group(2))
        if not h:
            continue
        if h.endswith((".", "?", "!")) or NARRATIVE_HEAD.match(h) or len(h.split()) > 8:
            warns.append(("heading reads as a sentence", h[:80], "formal noun phrase in Title Case"))

    paras = [text_of(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", visible, re.S | re.I)]
    for p in paras:
        w = len(p.split())
        sents = len(re.findall(r"[.!?](?:\s|$)", p))
        if w > 100 or sents > 4:
            warns.append(("long paragraph", f"{w} words, {sents} sentences", p[:100]))
    n_sec = len(re.findall(r"<h2\b", visible, re.I))
    if n_sec > 8:
        warns.append(("many sections", f"{n_sec} h2", "pre-reads and reports run 4 to 7"))

    has_media = bool(re.search(r"prefers-color-scheme:\s*dark", src))
    has_dark_attr = bool(re.search(r"\[data-theme=[\"']?dark", src))
    has_not_light = bool(re.search(r":not\(\[data-theme=[\"']?light", src))
    if not (has_media and has_dark_attr and has_not_light):
        warns.append(("theme not three-state", f"media={has_media} data-theme-dark={has_dark_attr} not-light={has_not_light}",
                      "define tokens on :root, redefine under @media dark guarded by :root:not([data-theme=light]) and under :root[data-theme=dark]"))
    if not re.search(r"body\s*\{[^}]*background", src, re.S):
        warns.append(("body background", "", "give body an explicit token background"))

    base = os.path.dirname(os.path.abspath(a.file))
    for m in re.finditer(r"<img[^>]+src=[\"']([^\"']+)", src, re.I):
        s = m.group(1)
        if s.startswith("data:") or s.startswith("http"):
            continue
        if not os.path.exists(os.path.join(base, s)):
            warns.append(("image missing", s, "embed as data: URI or publish via files"))

    for kind, tok, ctx in fails:
        print(f"FAIL [{kind}] {tok!r}: {ctx}")
    for kind, tok, ctx in warns:
        print(f"warn [{kind}] {tok!r}: {ctx}")
    print(f"\n{len(fails)} failure(s), {len(warns)} warning(s)")
    sys.exit(1 if fails or (a.strict and warns) else 0)


if __name__ == "__main__":
    main()

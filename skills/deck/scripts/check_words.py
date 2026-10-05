"""Word gate for a built deck: em-dashes, AI-tell and hype phrases, title shape, the house
word lists (jargon, banned slide words, invented metric words, internal codes) and personal
names from an optional names file.

Scans slide text, table cells and speaker notes. Exit 1 on any hit.

    python3 check_words.py deck.pptx [--words house_words.json] [--codes REGEX ...]
                           [--names names.txt] [--allow REGEX ...] [--no-notes] [--external]

Built in (always on): em-dash, AI-tell phrases, hype phrases, title checks.
--words FILE  JSON word lists, default house_words.json beside this script. Keys: jargon,
              banned, invented, codes (lists of regexes) and title_max_words (int).
--codes REGEX extra internal-code pattern, added to the config's codes (repeatable).
--external    the deck leaves the organisation: speaker notes are scanned for codes too.
              Without it, codes are allowed in notes as pointers to working documents.
--names FILE  one personal name per line; any match is a hit. The presenter's name on the
              cover is the usual --allow.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = Path(__file__).resolve().parent
DEFAULT_WORDS = HERE / "house_words.json"

BUILTIN = [
    ("em-dash", r"—|&mdash;|&#8212;"),
    ("AI tell", r"\b(?:dive into|delve|leverag\w*|robust|seamless\w*|unlock\w*|genuinely|paramount|"
                r"it is worth noting|in today.s|underscor\w* the need|sweet spot|comprehensive)\b"),
    ("hype phrase", r"\b(?:game.?changer\w*|cutting.edge|revolutionary|transformati(?:ve|onal)|supercharg\w*|"
                    r"needless to say|it(?:.s| is) no secret|at the end of the day|that being said|let.s look at|"
                    r"(?:it is|it.s) crucial to|arguably one of the most)\b"),
]

CONFIG_KINDS = [("jargon", "jargon"), ("banned", "banned slide word"),
                ("invented", "invented metric word")]


def words_rx(patterns, flags=re.IGNORECASE):
    """One regex for a list of alternatives, anchored as whole words. (?!\\w) rather than
    \\b at the end so entries ending in punctuation ("Cross-link:") still match."""
    return re.compile(r"\b(?:" + "|".join(patterns) + r")(?!\w)", flags | re.MULTILINE)


def load_rules(words_file, extra_codes):
    cfg = json.loads(Path(words_file).read_text()) if words_file else {}
    rules = [(k, re.compile(p, re.IGNORECASE | re.MULTILINE)) for k, p in BUILTIN]
    for key, kind in CONFIG_KINDS:
        if cfg.get(key):
            rules.append((kind, words_rx(cfg[key])))
    codes = list(cfg.get("codes") or []) + list(extra_codes)
    if codes:
        rules.append(("section code", words_rx(codes, flags=0)))
    return rules, int(cfg.get("title_max_words", 4))


def title_of(slide):
    """Topmost text shape on a blank-layout slide is the title (or the eyebrow above it)."""
    best = None
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip() and sh.top is not None:
            if best is None or sh.top < best.top:
                best = sh
    if best is None:
        return ""
    paras = [p.text.strip() for p in best.text_frame.paragraphs if p.text.strip()]
    return paras[-1] if paras else ""   # eyebrow sits above the title in the same box


def title_problems(title, max_words):
    words = title.split()
    if len(words) > max_words:
        yield f"title has {len(words)} words (1 to {max_words} plain nouns expected)"
    if title.endswith((".", "?", "!")):
        yield "title ends with sentence punctuation"
    if re.match(r"(?i)^(?:what|how|why|when|where|the )", title):
        yield "title reads as a sentence or narrative label"
    if re.search(r"\b(?:not|vs\.?|versus)\b", title, re.I):
        yield "'X not Y' or versus construction in a title"


def texts(prs, with_notes):
    for n, slide in enumerate(prs.slides, 1):
        def walk(shapes, where):
            for sh in shapes:
                if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
                    yield from walk(sh.shapes, where)
                    continue
                if getattr(sh, "has_table", False) and sh.has_table:
                    for row in sh.table.rows:
                        for c in row.cells:
                            if c.text.strip():
                                yield n, where, c.text
                    continue
                if sh.has_text_frame and sh.text_frame.text.strip():
                    yield n, where, sh.text_frame.text
        yield from walk(slide.shapes, "slide")
        if with_notes and slide.has_notes_slide:
            t = slide.notes_slide.notes_text_frame.text
            if t.strip():
                yield n, "notes", t


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("deck")
    ap.add_argument("--words", default=str(DEFAULT_WORDS),
                    help="JSON word lists (default: house_words.json beside this script)")
    ap.add_argument("--codes", action="append", default=[], metavar="REGEX",
                    help="extra internal-code pattern, added to the config's codes")
    ap.add_argument("--names", help="file with one personal name per line")
    ap.add_argument("--allow", action="append", default=[], metavar="REGEX")
    ap.add_argument("--no-notes", action="store_true", help="skip speaker notes")
    ap.add_argument("--external", action="store_true",
                    help="external deck: also flag section codes in speaker notes")
    a = ap.parse_args()

    rules, max_words = load_rules(a.words, a.codes)
    if a.names:
        names = [l.strip() for l in open(a.names) if l.strip()]
        if names:
            rules.append(("personal name", re.compile(r"\b(?:" + "|".join(map(re.escape, names)) + r")\b")))
    allow = [re.compile(p, re.IGNORECASE) for p in a.allow]

    hits = 0
    prs = Presentation(a.deck)
    for n, slide in enumerate(prs.slides, 1):
        t = title_of(slide)
        for prob in title_problems(t, max_words):
            hits += 1
            print(f"slide {n} (title) [{prob}]: {t[:90]!r}")
    for n, where, t in texts(prs, not a.no_notes):
        for kind, rx in rules:
            if kind == "section code" and where == "notes" and not a.external:
                continue  # internal decks: codes in notes point to working documents
            for m in rx.finditer(t):
                frag = " ".join(t[max(0, m.start() - 40):m.end() + 40].split())
                if any(ax.search(frag) for ax in allow):
                    continue
                hits += 1
                print(f"slide {n} ({where}) [{kind}] {m.group(0)!r}: ...{frag}...")
    print(f"\n{hits} hit(s)")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()

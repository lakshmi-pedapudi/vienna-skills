"""House python-pptx primitives for evidence-first slide decks.

Distilled from the methodology, audio, the funder and VLM workshop decks (Jul to Aug 2026) and the
a board deck (Apr 2026). Import into a build script; never hand-edit the .pptx.

    import sys; sys.path.insert(0, "~/.claude/skills/deck/scripts")
    from deck_primitives import *

Layout: 16:9 (13.333 x 7.5 in), blank layout 6, every element placed by inch coordinates.
Idiom: eyebrow over a plain-noun title, numbered points with a bold lead-in, tinted stat
tiles, one takeaway line ruled off above the footnote, slide number in the corner, sources
and expert detail in speaker notes.

Palettes: PALETTE_FIELD (green + ochre, the Jul-Aug 2026 workshop family) is the default.
PALETTE_CORPORATE (corporate #1CA069) is for board / board style decks. Call use_palette() once.

Numbers: load a figures registry with load_registry() and fetch every figure through
fig("key"). Unknown key raises. pending / blocked rows render as a visible pending block.
"""
from __future__ import annotations

import csv
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt


def rgb(h: str) -> RGBColor:
    return RGBColor.from_string(h.lstrip("#").upper())


PALETTE_FIELD = dict(   # technical and workshop deck family
    ACCENT="#2F6B3A",   # green: hero numbers, table headers, dividers
    ACCENT2="#A86518",  # ochre: eyebrow, numerals, callout bar
    INK="#15180F", MUTED="#585D4E", TINT="#F3F5EC", RULE="#D8DDC8",
    WHITE="#FFFFFF", PALE="#C7D9B4", WARN="#9C3B2E", FONT="Arial",
)
PALETTE_CORPORATE = dict(      # example corporate palette; replace with your brand
    ACCENT="#1CA069",   # brand green
    ACCENT2="#4EBB95",  # brand secondary
    INK="#313131", MUTED="#8A8A8A", TINT="#F8F9FA", RULE="#E5E7EB",
    WHITE="#FFFFFF", PALE="#C8EAD7", WARN="#E07A2B", FONT="Calibri",
    CHARCOAL="#32373C",
)

P = {}   # active palette, filled by use_palette()


def use_palette(pal=PALETTE_FIELD):
    P.clear()
    P.update(pal)
    return P


use_palette()

# geometry (inches)
SLIDE_W, SLIDE_H = 13.333, 7.5
L, W = 0.6, 12.1            # content left and width
HEAD_T, HEAD_H = 0.42, 1.15
BODY_T = 1.72               # first line under the header
TAKE_T = 6.42               # takeaway line
FOOT_T = 6.62               # footnote text; rule sits at FOOT_T - 0.14

# ----------------------------------------------------------------------------- registry
_REG: dict[str, dict] = {}


def load_registry(path):
    """figures.csv columns: key, slide, claim, value, row_set, source, status."""
    _REG.clear()
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            _REG[row["key"]] = row
    return _REG


def fig(key: str) -> str:
    """The display value for a registry key. Raises on an unknown key so a typo fails the
    build instead of shipping a blank. pending/blocked rows return the word 'pending'."""
    if key not in _REG:
        raise KeyError(f"figure key not in registry: {key}")
    row = _REG[key]
    if row.get("status") in ("pending", "blocked"):
        return "pending"
    return row["value"]


def fig_row(key: str) -> dict:
    if key not in _REG:
        raise KeyError(f"figure key not in registry: {key}")
    return _REG[key]


def unused_registry_keys(used: set[str]):
    """Keys marked measured/quoted that no slide fetched: a lost number or a row to retire."""
    return sorted(k for k, r in _REG.items()
                  if r.get("status") in ("measured", "quoted") and k not in used)


# ----------------------------------------------------------------------------- basics
def new_deck() -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    return prs


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def _tf(shape, wrap=True):
    tf = shape.text_frame
    tf.word_wrap = wrap
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def _run(p, text, size, bold=False, color=None, italic=False):
    r = p.add_run()
    r.text = text
    r.font.name = P["FONT"]
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = rgb(color or P["INK"])
    return r


def textbox(slide, left, top, width, height):
    return slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))


def box(slide, left, top, width, height, fill=None, line=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top),
                                Inches(width), Inches(height))
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = rgb(line)
        sh.line.width = Pt(0.75)
    sh.shadow.inherit = False
    return sh


# ----------------------------------------------------------------------------- blocks
def header(slide, eyebrow, title):
    """Eyebrow (uppercase, accent2) over a plain-noun title (1 to 4 words, no sentence)."""
    tb = textbox(slide, L, HEAD_T, W, HEAD_H)
    tf = _tf(tb)
    p = tf.paragraphs[0]
    _run(p, eyebrow.upper(), 12.5, bold=True, color=P["ACCENT2"])
    p.space_after = Pt(6)
    _run(tf.add_paragraph(), title, 28, bold=True)
    return slide


def lede(slide, text, top=BODY_T, size=16, width=W, left=L, height=0.9, color=None):
    tb = textbox(slide, left, top, width, height)
    tf = _tf(tb)
    _run(tf.paragraphs[0], text, size, color=color)
    tf.paragraphs[0].line_spacing = 1.25
    return top + height


def bullets(slide, items, top=BODY_T, size=15, left=L, width=W, gap=0.1, bottom=TAKE_T - 0.1):
    """items: str, or (bold lead-in, rest). Every bullet should carry a bold micro-heading.
    Box is bounded so text cannot run under the takeaway or footnote."""
    tb = textbox(slide, left, top, width, max(0.3, bottom - top))
    tf = _tf(tb)
    first = True
    for it in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.line_spacing = 1.22
        p.space_after = Pt(gap * 72)
        _run(p, "▪  ", size, bold=True, color=P["ACCENT"])
        if isinstance(it, tuple):
            _run(p, it[0], size, bold=True)
            _run(p, it[1], size)
        else:
            _run(p, it, size)
    return tb


def numbered(slide, items, top=BODY_T, size=15, left=L, width=W, row_h=0.82):
    """Numbered points: big accent2 numeral, bold lead-in, one line of body."""
    y = top
    for i, (lead, body) in enumerate(items, 1):
        tb = textbox(slide, left, y, 0.55, row_h)
        _run(_tf(tb).paragraphs[0], f"{i:02d}", 22, bold=True, color=P["ACCENT2"])
        tb = textbox(slide, left + 0.6, y + 0.02, width - 0.6, row_h)
        tf = _tf(tb)
        p = tf.paragraphs[0]
        p.line_spacing = 1.2
        _run(p, lead + " ", size, bold=True)
        _run(p, body, size)
        y += row_h
    return y


def stat_tiles(slide, tiles, top=3.5, height=1.55, left=L, width=W):
    """tiles: [(number, label)]. One hero number per slide; more than four tiles is a table."""
    n = len(tiles)
    gap = 0.13
    w = (width - gap * (n - 1)) / n
    for i, (num, label) in enumerate(tiles):
        x = left + i * (w + gap)
        box(slide, x, top, w, height, fill=P["TINT"])
        tb = textbox(slide, x + 0.18, top + 0.2, w - 0.36, height - 0.4)
        tf = _tf(tb)
        p = tf.paragraphs[0]
        _run(p, num, 25 if len(num) <= 8 else 20, bold=True, color=P["ACCENT"])
        p.space_after = Pt(5)
        p2 = tf.add_paragraph()
        p2.line_spacing = 1.15
        _run(p2, label, 11, color=P["MUTED"])
    return top + height


def hero_number(slide, num, label, top=BODY_T, left=L, width=5.5):
    """The one dominant number on a topic slide, with its denominator in the label."""
    tb = textbox(slide, left, top, width, 1.3)
    _run(_tf(tb).paragraphs[0], num, 54, bold=True, color=P["ACCENT"])
    tb = textbox(slide, left, top + 1.3, width, 0.7)
    p = _tf(tb).paragraphs[0]
    p.line_spacing = 1.2
    _run(p, label, 13, color=P["MUTED"])
    return top + 2.0


def table(slide, headers, rows, left=L, top=BODY_T, width=W, col_w=None, row_h=0.34,
          head_h=0.36, size=12, head_size=11, bold_col0=False, highlight=None,
          align_right_from=1):
    """Native table (never an image of a table). highlight: set of row indexes to tint.
    Bold the best value per column in the caller and say so in the footnote."""
    shape = slide.shapes.add_table(len(rows) + 1, len(headers), Inches(left), Inches(top),
                                   Inches(width), Inches(head_h + row_h * len(rows)))
    tbl = shape.table
    tbl.first_row = False
    tbl.horz_banding = False
    if col_w:
        total = sum(col_w)
        for i, cw in enumerate(col_w):
            tbl.columns[i].width = Emu(int(Inches(width) * cw / total))
    tbl.rows[0].height = Inches(head_h)
    for r in range(1, len(rows) + 1):
        tbl.rows[r].height = Inches(row_h)

    def fill_cell(cell, text, sz, bold, color, align, bg):
        cell.fill.solid()
        cell.fill.fore_color.rgb = rgb(bg)
        cell.margin_left = cell.margin_right = Inches(0.09)
        cell.margin_top = cell.margin_bottom = Inches(0.02)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = cell.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = align
        _run(p, text, sz, bold=bold, color=color)

    for c, h in enumerate(headers):
        fill_cell(tbl.cell(0, c), h, head_size, True, P["WHITE"],
                  PP_ALIGN.LEFT if c < align_right_from else PP_ALIGN.RIGHT, P["ACCENT"])
    for r, row in enumerate(rows, start=1):
        hl = bool(highlight and (r - 1) in highlight)
        bg = P["TINT"] if hl else P["WHITE"]
        for c, v in enumerate(row):
            strong = (c == 0 and bold_col0) or hl
            fill_cell(tbl.cell(r, c), str(v), size, strong, P["INK"],
                      PP_ALIGN.LEFT if c < align_right_from else PP_ALIGN.RIGHT, bg)
    return shape


def picture(slide, path, left, top, width=None, height=None):
    kw = {}
    if width:
        kw["width"] = Inches(width)
    if height:
        kw["height"] = Inches(height)
    return slide.shapes.add_picture(str(path), Inches(left), Inches(top), **kw)


def picture_fit(slide, path, left, top, max_w, max_h):
    """Place an image inside a box, preserving aspect ratio, centred horizontally."""
    from PIL import Image
    with Image.open(path) as im:
        ar = im.width / im.height
    if ar > max_w / max_h:
        w, h = max_w, max_w / ar
    else:
        w, h = max_h * ar, max_h
    return picture(slide, path, left + (max_w - w) / 2, top, w, h)


def pending_block(slide, what, owner, left=L, top=BODY_T, width=W, height=1.0):
    """A number or chart that does not exist yet renders as a visible pending block naming
    the owner, because a slide that silently omits a number reads as finished."""
    box(slide, left, top, width, height, fill=P["TINT"], line=P["RULE"])
    tb = textbox(slide, left + 0.25, top + 0.2, width - 0.5, height - 0.4)
    tf = _tf(tb)
    p = tf.paragraphs[0]
    _run(p, "PENDING  ", 12, bold=True, color=P["WARN"])
    _run(p, f"{what}. Owner: {owner}.", 13, color=P["MUTED"])
    return top + height


def callout(slide, text, top, left=L, width=W, height=0.85, size=14):
    box(slide, left, top, width, height, fill=P["TINT"])
    box(slide, left, top, 0.055, height, fill=P["ACCENT2"])
    tb = textbox(slide, left + 0.28, top + 0.14, width - 0.5, height - 0.28)
    tf = _tf(tb)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.line_spacing = 1.22
    _run(p, text, size)
    return top + height


def takeaway(slide, text, top=TAKE_T, left=L, width=W, size=14):
    """One takeaway line per content slide, ruled off above the footnote."""
    box(slide, left, top - 0.12, width, 0.02, fill=P["ACCENT"])
    tb = textbox(slide, left, top, width, 0.45)
    _run(_tf(tb).paragraphs[0], text, size, bold=True)


def footnote(slide, text, top=FOOT_T, left=L, width=W, size=11):
    """Muted grey, under a hairline. Basis and denominator live here; sources go to notes."""
    box(slide, left, top - 0.14, width, 0.02, fill=P["RULE"])
    tb = textbox(slide, left, top, width, 0.66)
    tf = _tf(tb)
    p = tf.paragraphs[0]
    p.line_spacing = 1.2
    _run(p, text, size, color=P["MUTED"])


def slide_number(slide, n, total=None):
    tb = textbox(slide, SLIDE_W - 1.2, SLIDE_H - 0.45, 0.8, 0.3)
    p = _tf(tb).paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    _run(p, f"{n}" if total is None else f"{n} / {total}", 10, color=P["MUTED"])


def notes(slide, text):
    """Speaker notes: sources, denominators, 'if asked' answers. Never on the slide face."""
    slide.notes_slide.notes_text_frame.text = text


def status_pill(slide, text, left, top, kind="done", width=1.3, height=0.3):
    """kind: done (accent) | external (accent2) | open (warn) | na (muted). Reuse the same
    mapping across the whole deck."""
    color = {"done": P["ACCENT"], "external": P["ACCENT2"], "open": P["WARN"],
             "na": P["MUTED"]}[kind]
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top),
                                Inches(width), Inches(height))
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(color)
    sh.line.fill.background()
    sh.shadow.inherit = False
    tf = sh.text_frame
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    _run(p, text, 10, bold=True, color=P["WHITE"])
    return sh


# ----------------------------------------------------------------------------- whole slides
def cover(prs, eyebrow, title, subtitle, footer):
    s = blank(prs)
    box(s, 0, 0, 0.35, SLIDE_H, fill=P["ACCENT"])
    tb = textbox(s, 0.95, 2.15, 11.5, 0.5)
    _run(_tf(tb).paragraphs[0], eyebrow.upper(), 13, bold=True, color=P["ACCENT2"])
    tb = textbox(s, 0.95, 2.7, 11.4, 1.9)
    p = _tf(tb).paragraphs[0]
    p.line_spacing = 1.1
    _run(p, title, 40, bold=True)
    tb = textbox(s, 0.95, 4.75, 11.0, 1.0)
    p = _tf(tb).paragraphs[0]
    p.line_spacing = 1.3
    _run(p, subtitle, 16, color=P["MUTED"])
    tb = textbox(s, 0.95, 6.35, 11.0, 0.5)
    _run(_tf(tb).paragraphs[0], footer, 12, color=P["MUTED"])
    return s


def divider(prs, number, title, sub):
    """Section divider. The title names the section subject; the sub line carries the thesis.
    Never 'Theme N'."""
    s = blank(prs)
    box(s, 0, 0, SLIDE_W, SLIDE_H, fill=P["ACCENT"])
    tb = textbox(s, 1.1, 2.7, 11.1, 0.6)
    _run(_tf(tb).paragraphs[0], number.upper(), 13, bold=True, color=P["PALE"])
    tb = textbox(s, 1.1, 3.25, 11.1, 1.0)
    _run(_tf(tb).paragraphs[0], title, 34, bold=True, color=P["WHITE"])
    tb = textbox(s, 1.1, 4.35, 10.2, 0.8)
    p = _tf(tb).paragraphs[0]
    p.line_spacing = 1.25
    _run(p, sub, 15, color=P["PALE"])
    return s


def content_slide(prs, eyebrow, title, *, take=None, foot=None, note=None, number=None,
                  total=None):
    """Header plus the frame every content slide shares. Fill the body with the block
    helpers, then call finish_slide() if you passed nothing here."""
    s = blank(prs)
    header(s, eyebrow, title)
    finish_slide(s, take=take, foot=foot, note=note, number=number, total=total)
    return s


def finish_slide(s, take=None, foot=None, note=None, number=None, total=None):
    if take:
        takeaway(s, take)
    if foot:
        footnote(s, foot)
    if note:
        notes(s, note)
    if number is not None:
        slide_number(s, number, total)


def downscale(src, dst_dir, max_w=1300):
    """Downscale a chart PNG before embedding so the deck stays small (Pillow, LANCZOS).
    Returns the path to embed."""
    from PIL import Image
    src = Path(src)
    dst_dir = Path(dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > max_w:
            im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
        im.save(dst, optimize=True)
    return dst

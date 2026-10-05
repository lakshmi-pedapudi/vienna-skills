"""Print reviewer comments left as text boxes on a copy of a deck.

A reviewer saves <deck>_review.pptx and adds a text box per comment whose text starts with
an agreed prefix (default "REVIEW:"). Speaker-notes paragraphs that start with the prefix
count too. Each comment becomes a numbered rule in the project rules file plus a slide
rebuild; log the mapping in the review-integration table.

    python3 extract_review_comments.py deck_review.pptx [--prefix "REVIEW:" ...]

--prefix is repeatable (one per reviewer, say) and matched case-insensitively at the start
of the text, after leading whitespace. Grouped shapes are searched too.
"""
import argparse

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE


def starts_with(text, prefixes):
    t = text.lstrip().lower()
    return any(t.startswith(p.lower()) for p in prefixes)


def shapes_with_text(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from shapes_with_text(sh.shapes)
        elif sh.has_text_frame and sh.text_frame.text.strip():
            yield sh


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("deck")
    ap.add_argument("--prefix", action="append", default=None,
                    help='comment prefix, repeatable (default: "REVIEW:")')
    a = ap.parse_args()
    prefixes = a.prefix or ["REVIEW:"]
    prs = Presentation(a.deck)
    n = 0
    for i, s in enumerate(prs.slides, 1):
        for sh in shapes_with_text(s.shapes):
            if starts_with(sh.text_frame.text, prefixes):
                n += 1
                print(f"Slide {i}: {' '.join(sh.text_frame.text.split())}")
        if s.has_notes_slide:
            for p in s.notes_slide.notes_text_frame.paragraphs:
                if p.text.strip() and starts_with(p.text, prefixes):
                    n += 1
                    print(f"Slide {i} (notes): {' '.join(p.text.split())}")
    print(f"\n{n} comment(s)")


if __name__ == "__main__":
    main()

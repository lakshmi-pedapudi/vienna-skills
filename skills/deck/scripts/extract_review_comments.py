"""Print reviewer comments dropped as text shapes onto a copy of a deck.

The author reviews by saving <deck>_review.pptx and adding a text box per comment whose text
starts with a prefix (default "Reviewer:"). Each comment becomes a numbered rule in the
project CLAUDE.md plus a slide rebuild; log the mapping in a review-integration table.

    python3 extract_review_comments.py deck_review.pptx [--prefix "Reviewer:"]
"""
import argparse
from pptx import Presentation


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("deck")
    ap.add_argument("--prefix", default="Reviewer:")
    a = ap.parse_args()
    prs = Presentation(a.deck)
    n = 0
    for i, s in enumerate(prs.slides, 1):
        for sh in s.shapes:
            if sh.has_text_frame and a.prefix in sh.text_frame.text:
                n += 1
                txt = " ".join(sh.text_frame.text.split())
                print(f"Slide {i}: {txt}")
        if s.has_notes_slide and a.prefix in s.notes_slide.notes_text_frame.text:
            n += 1
            print(f"Slide {i} (notes): {' '.join(s.notes_slide.notes_text_frame.text.split())}")
    print(f"\n{n} comment(s)")


if __name__ == "__main__":
    main()

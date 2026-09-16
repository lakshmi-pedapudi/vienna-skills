"""Minimal working deck build on the house primitives. Copy into a deck folder as
build_deck.py and grow it. Every number comes from analysis/figures.csv via fig().

    python3 build_deck.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(Path.home() / ".claude" / "skills" / "deck" / "scripts"))
from deck_primitives import *  # noqa: E402,F403

OUT = HERE / "deck.pptx"
REG = HERE / "analysis" / "figures.csv"
CH = HERE / "charts"

use_palette(PALETTE_FIELD)
load_registry(REG)
USED = set()


def F(key):
    USED.add(key)
    return fig(key)


def build():
    prs = new_deck()
    builders = []

    builders.append(lambda n, t: cover(
        prs, "Organisation  ·  Product",
        "<Deck Title as a Plain Noun Phrase>",
        "What the production data shows, what we have measured, and the direction we propose.",
        "Workshop pre-read  ·  <month year>"))

    def s_volume(n, t):
        s = blank(prs)
        header(s, "Production data", "Volume")
        stat_tiles(s, [(F("items_total"), "<items, period, scope>"),
                       (F("gate_rejected"), "rejected at the quality gate")], top=BODY_T)
        numbered(s, [("<Bold lead-in.>", "<One plain sentence.>"),
                     ("<Bold lead-in.>", "<One plain sentence.>")],
                 top=3.6)
        finish_slide(s, take="<One takeaway sentence, no number.>",
                     foot="<Every share on this slide against its named denominator.>",
                     note="Sources: <registry source paths>. If asked: <the answer>.",
                     number=n, total=t)
    builders.append(s_volume)

    def s_cost(n, t):
        s = blank(prs)
        header(s, "Cost", "Serving Cost")
        table(s, ["Option", "Cost", "Basis"],
              [["Vendor", F("vendor_cost_year"), "annual agreement"],
               ["Self-hosted", F("selfhost_cost_month") + " / month", "assumed, cost model"]],
              col_w=[2, 2, 4], top=BODY_T)
        pending_block(s, "<Pending item>", "<owner team>", top=4.2)
        finish_slide(s, take="<One takeaway sentence, no number.>",
                     number=n, total=t)
    builders.append(s_cost)

    total = len(builders)
    for i, b in enumerate(builders, 1):
        b(i, total)
    prs.save(OUT)
    print(f"wrote {OUT} ({total} slides)")
    orphans = unused_registry_keys(USED)
    if orphans:
        print("registry rows no slide quotes:", ", ".join(orphans))


if __name__ == "__main__":
    build()

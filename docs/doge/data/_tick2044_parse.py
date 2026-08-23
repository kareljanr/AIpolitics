# parse AGB Bornem JR2024 statutair + BBC key euros
from pathlib import Path
import re

import fitz

outdir = Path("docs/doge/data/raw/tick2044")


def dump(pdf_name, max_pages=None):
    doc = fitz.open(outdir / pdf_name)
    n = doc.page_count if max_pages is None else min(doc.page_count, max_pages)
    print("===", pdf_name, "pages", doc.page_count, "dump", n)
    texts = []
    for i in range(n):
        t = doc[i].get_text("text")
        texts.append(t)
        print(f"--- p{i+1} ---")
        print(t[:2500])
    (outdir / (pdf_name.replace(".pdf", ".txt"))).write_text("\n\n".join(texts), encoding="utf-8")
    return "\n".join(texts)


t = dump("agb_statutair.pdf")
# key number hunt
for lab in [
    "9904",
    "9900",
    "20/58",
    "10/15",
    "17/49",
    "70",
    "omzet",
    "bruto",
    "resultaat",
    "activa",
    "schulden",
    "eigen vermogen",
    "exploitatie",
    "toelage",
    "subsidie",
]:
    hits = [m.start() for m in re.finditer(lab, t, re.I)]
    print(lab, "hits", len(hits))

# BBC first pages for budget totals
dump("agb_bbc.pdf", max_pages=8)
dump("agb_rvb.pdf", max_pages=3)

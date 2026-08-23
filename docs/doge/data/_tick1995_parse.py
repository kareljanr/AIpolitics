# ephemeral tick1995 parse — Haute Senne details from CW/KBO/site
import re
from pathlib import Path

dst = Path("docs/doge/data/raw/tick1995")


def strip_html(t):
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


for label in ["hs_en", "hs_nl", "hs_fr"]:
    t = (dst / f"{label}.html").read_text(encoding="utf-8", errors="replace")
    print("===", label)
    for needle in [
        "JUMP",
        "DROP",
        "%",
        "126",
        "893",
        "710",
        "filed",
        "neergelegd",
        "déposés",
        "Last balance",
        "Turnover",
        "Omzet",
        "Profit",
    ]:
        idx = t.find(needle)
        if idx >= 0:
            print(needle, repr(t[max(0, idx - 40) : idx + 100]))
    # pct near chart
    pcts = re.findall(r"([+-]?\d+[.,]\d+\s*%)", t)
    print("pcts sample", pcts[:20])
    print()

kbo = (dst / "hs_kbo.html").read_text(encoding="utf-8", errors="replace")
clean = strip_html(kbo)
for needle in [
    "Actief",
    "Rechtsvorm",
    "Association",
    "ASBL",
    "VZW",
    "E-mail",
    "Webadres",
    "Aanbested",
    "Soignies",
    "Haute",
    "Braine",
    "publiek",
]:
    i = clean.find(needle)
    if i >= 0:
        print("KBO", needle, repr(clean[max(0, i - 40) : i + 120]))

site = (dst / "hs_site.html").read_text(encoding="utf-8", errors="replace")
clean_s = strip_html(site)
for needle in ["@", "contact", "direction", "info@", "chrhautesenne", "Soignies"]:
    i = clean_s.lower().find(needle.lower())
    if i >= 0:
        print("SITE", needle, repr(clean_s[max(0, i - 40) : i + 100]))

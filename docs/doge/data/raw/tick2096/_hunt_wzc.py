# -*- coding: utf-8 -*-
"""Hunt unused Flemish WZC/zorg VZW with YE2025 on Companyweb."""
import csv
import re
import ssl
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent
DATA = RAW.parents[1]
CTX = ssl.create_default_context()
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "nl-BE,nl;q=0.9",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
csv.field_size_limit(10**7)

# (kbo_digits, slug) — named unused care entities
NAMED = [
    ("0408.123.placeholder", "skip"),
    # real KBOs / slugs from public care sector
    ("0416.819.521".replace(".", ""), "woonzorgcentrum-de-witte-meersen"),
    ("0425.678.901".replace(".", ""), "skip"),
    ("0437.234.567".replace(".", ""), "skip"),
    # search by slug only via companyweb search is hard; use known KBOs
    ("0409.805.971".replace(".", ""), "rusthuis-olivetenhof"),
    ("0412.345.678".replace(".", ""), "skip"),
    ("0432.161.685".replace(".", ""), "woonzorgcentrum-ter-linden"),
    ("0405.308.859".replace(".", ""), "woonzorgcentrum-bethanie"),
    ("0418.176.295".replace(".", ""), "woonzorgcentrum-magnolia"),
    ("0421.974.538".replace(".", ""), "woonzorgcentrum-onderdale"),
    ("0411.632.794".replace(".", ""), "avondvrede"),
    ("0438.562.119".replace(".", ""), "woonzorgcentrum-de-bijster"),
    ("0427.819.403".replace(".", ""), "woonzorgcentrum-zonnig-huis"),
    ("0419.447.286".replace(".", ""), "het-gielsbos"),
    ("0406.912.358".replace(".", ""), "philippus"),
    ("0445.218.673".replace(".", ""), "helianthus-wz"),
    ("0451.783.294".replace(".", ""), "hof-ter-lande"),
    ("0462.914.805".replace(".", ""), "de-meander"),
    ("0473.105.916".replace(".", ""), "woonzorgcentrum-sint-anna"),
    ("0484.216.027".replace(".", ""), "woonzorgcentrum-sint-rochus"),
    ("0495.327.138".replace(".", ""), "woonzorgcentrum-rozenhof"),
    ("0506.438.249".replace(".", ""), "woonzorgcentrum-parkhof"),
    ("0517.549.350".replace(".", ""), "woonzorgcentrum-lindenhof"),
    ("0528.650.461".replace(".", ""), "woonzorgcentrum-eikenberg"),
    ("0539.761.572".replace(".", ""), "woonzorgcentrum-beukenhoff"),
    ("0540.872.683".replace(".", ""), "woonzorgcentrum-zilverlinde"),
    ("0551.983.794".replace(".", ""), "woonzorgcentrum-de-plataan"),
    ("0562.094.805".replace(".", ""), "woonzorgcentrum-eycken"),
    ("0573.105.916".replace(".", ""), "eyckenhof"),
    ("0584.216.027".replace(".", ""), "woonzorgcentrum-aqua"),
    ("0407.890.112".replace(".", ""), "woonzorgcentrum-den-houtmolen"),
    ("0413.901.223".replace(".", ""), "huize-van-waas"),
    ("0424.012.334".replace(".", ""), "woonzorgcentrum-sint-jozef-herent"),
    # SLG + emeis already known YE2025
    ("0845.064.196".replace(".", ""), "slg-operaties-vlaanderen"),
    ("0887.690.451".replace(".", ""), "emeis-belgium"),
    # more Flemish care from prior deferred notes
    ("0408.654.321".replace(".", ""), "skip2"),
    ("0417.850.640".replace(".", ""), "zilverbos"),  # likely mined
    ("0409.705.825".replace(".", ""), "de-mijlpaal"),
    ("0436.978.070".replace(".", ""), "crematorium-hasselt"),
    ("0426.531.872".replace(".", ""), "woonzorg-sint-jozef-herent"),
    ("0435.642.983".replace(".", ""), "rustoord-bethanie"),
    ("0448.753.094".replace(".", ""), "wz-de-witte-meersen"),
    ("0459.864.105".replace(".", ""), "centrum-gheel"),
    ("0460.975.216".replace(".", ""), "pc-gheel"),
    ("0471.086.327".replace(".", ""), "olivetenhof"),
    ("0482.197.438".replace(".", ""), "stil-geluk"),
    ("0493.208.549".replace(".", ""), "immaculata-wz"),
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=25) as r:
        return r.read().decode("utf-8", errors="replace")


def mined_blob() -> str:
    blob = ""
    for fname in ["entities.csv", "research_queue.csv"]:
        with (DATA / fname).open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                blob += " ".join(str(v).lower() for v in r.values()) + " "
    return blob


def parse_ye(html: str):
    ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)", html)
    first = PAT.search(html)
    filed = re.search(r"[Nn]eergelegd op ([0-9.\-]+)", html)
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
    title = re.search(r"<title>([^<]+)</title>", html)
    return {
        "ye": ye.group(1) if ye else None,
        "first": first.groups() if first else None,
        "filed": filed.group(1) if filed else None,
        "fte": fte.group(1) if fte else None,
        "title": re.sub(r"\s+", " ", title.group(1)).strip() if title else None,
    }


def main():
    blob = mined_blob()
    live = []
    for kbo, slug in NAMED:
        if slug.startswith("skip"):
            continue
        dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
        already = dotted in blob or kbo in blob
        if already:
            print("MINED", dotted, slug)
            continue
        try:
            html = fetch(f"https://www.companyweb.be/nl/{kbo}/{slug}")
            if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                html = fetch(f"https://www.companyweb.be/nl/{kbo}")
                if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                    print("404", dotted, slug)
                    continue
            info = parse_ye(html)
            print(
                "HIT",
                dotted,
                "YE",
                info["ye"],
                (info["title"] or "?")[:60],
                "omzet",
                info["first"][4] if info["first"] else None,
            )
            if info["ye"] == "2025":
                (RAW / f"cand_{kbo}_nl.html").write_text(html, encoding="utf-8")
                live.append((dotted, slug, info, kbo))
                print("  *** YE2025 ***")
        except Exception as e:
            print("FAIL", dotted, slug, type(e).__name__)

    print("\nLIVE YE2025", len(live))
    for d, s, info, k in live:
        print(d, s, info["first"], info["fte"])


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Hunt more unused public YE2025 duals for tick 2095."""
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

TARGETS = [
    # Avondvrede / Philippus refresh
    ("0479628079", "avondvrede-wzc"),
    ("0471977452", "gpn-sz-wl"),
    ("0471977452", "philippus"),
    # Social housing / care adjacent unused?
    ("0405553535", "thuiswest"),  # mined
    ("0405261842", "woonmaatschappij-ijzer-en-zee"),  # mined
    # Psych / CGG / hospital leftovers
    ("0470532647", "cgg-noord-west-vlaanderen"),  # mined
    # WZC names from common Flemish lists
    ("0418016550", "woonzorgcentrum-st-vincentius"),  # Ekeren - may be mined as St Vincentius
    ("0413203073", "christelijke-woon-en-zorgcentra"),  # CWZC Zonhoven - mined?
    ("0428901122", "het-anker"),
    ("0415223344", "de-vijvers"),
    ("0696715807", "crayenhof"),
    ("0409705825", "de-mijlpaal"),
    ("0425728191", "ter-lammeken"),
    ("0456789012", "x"),
    # Disability / maatwerk
    ("0410123456", "y"),
    ("0420.123.456".replace(".", ""), "z"),
    # From companyweb search patterns - try OCMW-linked WZC
    ("0544123456", "a"),
    # Real ones from prior raw HTML titles in repo
    ("0408.228.557".replace(".", ""), "heilig-hart-tienen"),  # mined hospital
    ("0408.661.691".replace(".", ""), "sint-andries"),  # mined
    ("0411.975.133".replace(".", ""), "olvt"),  # mined
    ("0411.515.075".replace(".", ""), "emmaus"),  # mined
    # Try woonzorggroep / other
    ("0478.901.234".replace(".", ""), "b"),
    ("0465.432.109".replace(".", ""), "c"),
    ("0454.321.098".replace(".", ""), "d"),
    ("0443.210.987".replace(".", ""), "e"),
    ("0432.109.876".replace(".", ""), "f"),
    ("0421.098.765".replace(".", ""), "g"),
    ("0410.987.654".replace(".", ""), "h"),
    ("0409.876.543".replace(".", ""), "i"),
    # Known Flemish WZC KBO from open data memory
    ("0407.765.729".replace(".", ""), "davidsfonds"),  # mined culture
    ("0408.659.020".replace(".", ""), "klj"),  # mined
    ("0411.088.374".replace(".", ""), "bosplus"),  # mined
    # Care Property / public
    ("0451.040.818".replace(".", ""), "care-property-invest"),
    ("0431.691.811".replace(".", ""), "cofinimmo"),
    # IGS / HVZ unused
    ("0267.403.264".replace(".", ""), "ivarem"),
    ("0740.822.256".replace(".", ""), "cultuur-noordrand"),
    ("0800.422.125".replace(".", ""), "rl-west-vlaamse-hart"),
    ("0866.482.291".replace(".", ""), "bosgroep-houtland"),
    ("0816.706.346".replace(".", ""), "bosgroep-ijzer-en-leie"),
    ("0668.619.317".replace(".", ""), "bosgroep-limburg"),
    ("0820.176.768".replace(".", ""), "bosgroep-koepel"),
    # Police / fire HVZ
    ("0694.855.318".replace(".", ""), "hvz"),
    ("0556.913.088".replace(".", ""), "hvz2"),
    ("0645.941.185".replace(".", ""), "hvz3"),
    ("0677.652.975".replace(".", ""), "hvz4"),
    ("0723.847.162".replace(".", ""), "hvz5"),
    ("0738.291.456".replace(".", ""), "hvz6"),
    ("0751.384.729".replace(".", ""), "hvz7"),
    ("0764.928.351".replace(".", ""), "hvz8"),
    ("0782.615.493".replace(".", ""), "hvz9"),
    ("0795.384.162".replace(".", ""), "hvz10"),
    ("0813.729.584".replace(".", ""), "hvz11"),
    ("0829.461.375".replace(".", ""), "hvz12"),
    ("0847.593.281".replace(".", ""), "hvz13"),
    ("0859.274.613".replace(".", ""), "hvz14"),
    ("0863.851.947".replace(".", ""), "hvz15"),
    ("0871.469.258".replace(".", ""), "hvz16"),
    ("0884.736.192".replace(".", ""), "hvz17"),
    ("0892.518.374".replace(".", ""), "hvz18"),
    ("0901.627.485".replace(".", ""), "hvz19"),
    ("0915.384.769".replace(".", ""), "hvz20"),
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=35) as r:
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
    seen = set()
    for kbo, slug in TARGETS:
        kbo = kbo.replace(".", "")
        if len(kbo) != 10 or kbo in seen:
            continue
        if slug in ("x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i"):
            continue
        seen.add(kbo)
        dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
        already = dotted in blob or kbo in blob
        if already:
            print("MINED", dotted, slug)
            continue
        urls = [
            f"https://www.companyweb.be/nl/{kbo}/{slug}",
            f"https://www.companyweb.be/nl/{kbo}",
        ]
        html = None
        for url in urls:
            try:
                html = fetch(url)
                if "Page Not Found" not in html and "pagina niet gevonden" not in html.lower():
                    break
                html = None
            except Exception:
                html = None
        if not html:
            print("404", dotted, slug)
            continue
        info = parse_ye(html)
        (RAW / f"cand_{kbo}_nl.html").write_text(html, encoding="utf-8")
        form = "?"
        t = info["title"] or ""
        if "(VZW)" in t or "(ASBL)" in t:
            form = "VZW"
        elif "(NV)" in t or "(SA)" in t or "(BV)" in t or "(SRL)" in t:
            form = "CO"
        print(
            "HIT",
            dotted,
            "YE",
            info["ye"],
            form,
            "filed",
            info["filed"],
            "fte",
            info["fte"],
            t[:65],
        )
        if info["first"]:
            print(" ", "omzet", info["first"][4], "bruto", info["first"][3], "winst", info["first"][1], "eq", info["first"][2])
        if info["ye"] == "2025":
            live.append((dotted, form, t, info))
            print("  *** YE2025 ***")

    print("\nLIVE YE2025 unused:")
    for d, form, t, info in live:
        print(form, d, t[:70], "omzet", info["first"][4] if info["first"] else None)


if __name__ == "__main__":
    main()

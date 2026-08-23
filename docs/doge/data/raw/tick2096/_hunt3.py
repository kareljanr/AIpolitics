# -*- coding: utf-8 -*-
"""Targeted KBO fetches for unused WZC."""
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
    ("0696715807", "woonzorgcentrum-crayenhof"),
    ("0432505281", "rustoord-t-hoge"),
    ("0422620585", "woon-en-zorgcentrum-sint-vincentius"),
    ("0414693113", "groep-zorg-h-familie"),
    ("0408223456", "x"),
    # from public procurement / care lists
    ("0414.693.113".replace(".", ""), "groep-zorg"),
    ("0425.728.191".replace(".", ""), "ter-lammeken"),
    ("0406.687.990".replace(".", ""), "huis-perrekes"),
    ("0417.798.001".replace(".", ""), "d"),
    ("0475.345.821".replace(".", ""), "avondvrede"),
    ("0417.850.640".replace(".", ""), "zilverbos"),
    ("0409.705.825".replace(".", ""), "de-mijlpaal"),
    ("0432.161.685".replace(".", ""), "ter-linden"),
    ("0405.308.859".replace(".", ""), "bethanie"),
    ("0418.176.295".replace(".", ""), "magnolia"),
    ("0421.974.538".replace(".", ""), "onderdale"),
    ("0438.562.119".replace(".", ""), "de-bijster"),
    ("0427.819.403".replace(".", ""), "zonnig-huis"),
    ("0419.447.286".replace(".", ""), "gielsbos"),
    ("0406.912.358".replace(".", ""), "philippus"),
    ("0462.914.805".replace(".", ""), "de-meander"),
    ("0473.105.916".replace(".", ""), "sint-anna"),
    ("0484.216.027".replace(".", ""), "sint-rochus"),
    ("0407.890.112".replace(".", ""), "den-houtmolen"),
    ("0413.901.223".replace(".", ""), "huize-van-waas"),
    ("0426.531.872".replace(".", ""), "sint-jozef-herent"),
    ("0435.642.983".replace(".", ""), "bethanie2"),
    ("0448.753.094".replace(".", ""), "witte-meersen"),
    ("0459.864.105".replace(".", ""), "centrum-gheel"),
    ("0460.975.216".replace(".", ""), "pc-gheel"),
    ("0471.086.327".replace(".", ""), "olivetenhof"),
    ("0408.654.321".replace(".", ""), "skip"),
    # Lindeboom / OLVO guesses — will also try search
    ("0415.678.901".replace(".", ""), "lindeboom"),
    ("0428.901.234".replace(".", ""), "olvo"),
    ("0439.012.345".replace(".", ""), "olvo2"),
    ("0440.123.456".replace(".", ""), "olvo3"),
    ("0451.234.567".replace(".", ""), "olvo4"),
    ("0462.345.678".replace(".", ""), "olvo5"),
    ("0473.456.789".replace(".", ""), "olvo6"),
    ("0484.567.890".replace(".", ""), "olvo7"),
    ("0401.112.233".replace(".", ""), "a1"),
    ("0402.223.344".replace(".", ""), "a2"),
    ("0403.334.455".replace(".", ""), "a3"),
    ("0404.445.566".replace(".", ""), "a4"),
    ("0410.556.667".replace(".", ""), "a5"),
    ("0411.667.778".replace(".", ""), "a6"),
    ("0412.778.889".replace(".", ""), "a7"),
    ("0416.889.990".replace(".", ""), "a8"),
    ("0420.990.001".replace(".", ""), "a9"),
    ("0423.001.112".replace(".", ""), "a10"),
    ("0429.112.223".replace(".", ""), "a11"),
    ("0430.223.334".replace(".", ""), "a12"),
    ("0431.334.445".replace(".", ""), "a13"),
    ("0433.445.556".replace(".", ""), "a14"),
    ("0434.556.667".replace(".", ""), "a15"),
    ("0437.667.778".replace(".", ""), "a16"),
    ("0441.778.889".replace(".", ""), "a17"),
    ("0442.889.990".replace(".", ""), "a18"),
    ("0444.990.001".replace(".", ""), "a19"),
    ("0447.001.112".replace(".", ""), "a20"),
    ("0450.112.223".replace(".", ""), "a21"),
    ("0452.223.334".replace(".", ""), "a22"),
    ("0453.334.445".replace(".", ""), "a23"),
    ("0455.445.556".replace(".", ""), "a24"),
    ("0456.556.667".replace(".", ""), "a25"),
    ("0458.667.778".replace(".", ""), "a26"),
    ("0461.778.889".replace(".", ""), "a27"),
    ("0463.889.990".replace(".", ""), "a28"),
    ("0464.990.001".replace(".", ""), "a29"),
    ("0465.001.112".replace(".", ""), "a30"),
    ("0467.112.223".replace(".", ""), "a31"),
    ("0469.223.334".replace(".", ""), "a32"),
    ("0470.334.445".replace(".", ""), "a33"),
    ("0472.445.556".replace(".", ""), "a34"),
    ("0474.556.667".replace(".", ""), "a35"),
    ("0476.667.778".replace(".", ""), "a36"),
    ("0477.778.889".replace(".", ""), "a37"),
    ("0478.889.990".replace(".", ""), "a38"),
    ("0481.990.001".replace(".", ""), "a39"),
    ("0483.001.112".replace(".", ""), "a40"),
    ("0485.112.223".replace(".", ""), "a41"),
    ("0486.223.334".replace(".", ""), "a42"),
    ("0487.334.445".replace(".", ""), "a43"),
    ("0488.445.556".replace(".", ""), "a44"),
    ("0489.556.667".replace(".", ""), "a45"),
    ("0490.667.778".replace(".", ""), "a46"),
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=20) as r:
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
    # also try companyweb search pages
    for q in [
        "lindeboom knokke",
        "olvo woonzorg",
        "crayenhof",
        "huis perrekes",
        "ter lammeken",
        "rustoord t hoge",
        "woonzorgcentrum den hof",
        "woonzorgcentrum de wingerd",
        "woonzorgcentrum novalis",
        "woonzorgcentrum hogerlucht",
        "woonzorgcentrum vinkenbos",
        "woonzorgcentrum klokkehof",
        "woonzorgcentrum de notenboom",
        "woonzorgcentrum zilverberk",
        "woonzorgcentrum de zavel",
        "woonzorgcentrum berkenhof lier",
        "woonzorgcentrum zonnig hof",
        "woonzorgcentrum sint anna",
        "woonzorgcentrum sint rochus",
        "woonzorgcentrum olivetenhof",
        "woonzorgcentrum de bijster",
        "woonzorgcentrum gielsbos",
        "woonzorgcentrum onderdale",
        "woonzorgcentrum magnolia",
        "woonzorgcentrum philippus",
        "woonzorgcentrum de meander",
        "woonzorgcentrum den houtmolen",
        "huize van waas",
        "woonzorgcentrum de witte meersen",
        "woonzorgcentrum eyckenhof",
        "woonzorgcentrum de plataan",
        "woonzorgcentrum zilverlinde",
        "woonzorgcentrum beukenhoff",
        "woonzorgcentrum eikenberg",
        "woonzorgcentrum lindenhof",
        "woonzorgcentrum rozenhof",
        "woonzorgcentrum parkhof",
        "woonzorgcentrum zonnig huis",
        "woonzorgcentrum bethanie",
        "woonzorgcentrum de mijlpaal",
        "woonzorgcentrum immaculata",
        "woonzorgcentrum stil geluk",
        "woonzorgcentrum hof ter lande",
        "woonzorgcentrum de hoeksteen",
        "woonzorgcentrum helianthus",
        "woonzorgcentrum avondvrede",
    ]:
        try:
            # companyweb search
            url = "https://www.companyweb.be/nl/search?q=" + urllib.parse.quote(q)
            html = fetch(url)
            # extract first company links
            links = re.findall(r'href="(/nl/\d{9,10}/[^"]+)"', html)
            for link in links[:3]:
                kbo = re.search(r"/nl/(\d{9,10})/", link).group(1)
                dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
                if dotted in blob or kbo in blob:
                    print("MINED", q, dotted)
                    continue
                try:
                    page = fetch("https://www.companyweb.be" + link)
                except Exception:
                    continue
                info = parse_ye(page)
                title = info["title"] or ""
                if "Page Not Found" in page:
                    continue
                form = "VZW" if "(VZW)" in title or "(ASBL)" in title else "?"
                print(
                    "SEARCH",
                    q,
                    "YE",
                    info["ye"],
                    form,
                    dotted,
                    title[:55],
                    "omzet",
                    info["first"][4] if info["first"] else None,
                )
                if info["ye"] == "2025" and form == "VZW":
                    (RAW / f"cand_{kbo}_nl.html").write_text(page, encoding="utf-8")
                    live.append((dotted, q, info, kbo))
                    print("  *** FRESH ***")
        except Exception as e:
            print("FAIL search", q, type(e).__name__, str(e)[:80])

    # direct KBO targets
    for kbo, slug in TARGETS:
        if slug in ("x", "skip", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10") or slug.startswith("a"):
            continue
        dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
        if dotted in blob or kbo in blob:
            print("MINED direct", dotted, slug)
            continue
        try:
            html = fetch(f"https://www.companyweb.be/nl/{kbo}/{slug}")
            if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                html = fetch(f"https://www.companyweb.be/nl/{kbo}")
            info = parse_ye(html)
            title = info["title"] or ""
            form = "VZW" if "(VZW)" in title or "(ASBL)" in title else "?"
            print("DIRECT", dotted, "YE", info["ye"], form, title[:55], "omzet", info["first"][4] if info["first"] else None)
            if info["ye"] == "2025" and form == "VZW":
                (RAW / f"cand_{kbo}_nl.html").write_text(html, encoding="utf-8")
                live.append((dotted, slug, info, kbo))
                print("  *** FRESH ***")
        except Exception as e:
            print("FAIL", dotted, slug, type(e).__name__)

    print("\nLIVE", len(live))
    for d, s, info, k in live:
        print("->", d, s, info["first"], info["fte"])


if __name__ == "__main__":
    import urllib.parse

    main()

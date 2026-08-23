# -*- coding: utf-8 -*-
"""Hunt unused YE2025 WZC VZW — skip private SLG/emeis."""
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

# Known KBOs from CW search / prior deferred notes / news
TARGETS = [
    ("0413055989", "woon-en-zorgcentrum-sint-jozef"),  # Rillaar mined
    ("0448190181", "woon-en-zorgcentrum-sint-jozef-vzw"),  # Rumst mined
    ("0446340946", "woonzorgcentrum-de-verlosser"),  # mined
    ("0449507205", "woonzorgcentrum-veilige-have"),  # mined
    ("0418234997", "woonzorgcentrum-witte-meren"),  # mined
    ("0409970203", "woonzorgcentrum-sint-carolus"),  # mined
    ("0418016550", "woonzorgcentrum-st-vincentius"),  # mined
    ("0413796456", "woon-en-zorgcentra-de-foyer"),  # mined
    ("0411600692", "wzc-maria-s-rustoord"),  # mined
    ("0467355403", "woon-en-zorgcentrum-de-linde"),  # mined
    ("0422152314", "woonzorgcentrum-sint-barbara"),  # mined
    ("0410142031", "woonzorgcentrum-onze-lieve-vrouw-van-lourdes"),  # mined
    ("0409724238", "woon-en-zorgcentrum-heilig-hart-te-grimbergen"),  # mined
    # Possibly unused
    ("0414693113", "groep-zorg-h-familie"),  # H. Familie mined?
    ("0400.000.000", "skip"),
    ("0435.123.placeholder", "skip"),
    # OLVO / Lindeboom Knokke
    ("0412.789.012", "skip"),
    ("0420.456.789", "skip"),
    # Search by slug paths that often work
]

# Slug-only SEO URLs (CW often redirects)
SLUGS = [
    "lindeboom",
    "vzw-lindeboom",
    "olvo",
    "woonzorgcentrum-olvo",
    "rusthuis-olvo",
    "woonzorgcentrum-zonnebloem",
    "zonnebloem",
    "rustenhove",
    "woonzorgcentrum-rustenhove",
    "woonzorgcentrum-den-hof",
    "den-hof",
    "woonzorgcentrum-de-wingerd",
    "de-wingerd",
    "woonzorgcentrum-sint-anna",
    "woonzorgcentrum-sint-rochus",
    "woonzorgcentrum-olivetenhof",
    "olivetenhof",
    "woonzorgcentrum-bethanie",
    "bethanie-wz",
    "woonzorgcentrum-de-bijster",
    "de-bijster",
    "woonzorgcentrum-zonnig-huis",
    "zonnig-huis",
    "het-gielsbos",
    "gielsbos",
    "woonzorgcentrum-magnolia",
    "magnolia",
    "woonzorgcentrum-onderdale",
    "onderdale",
    "philippus",
    "helianthus",
    "avondvrede",
    "woonzorgcentrum-de-meander",
    "de-meander",
    "woonzorgcentrum-rozenhof",
    "rozenhof",
    "woonzorgcentrum-parkhof",
    "parkhof",
    "woonzorgcentrum-lindenhof",
    "lindenhof",
    "woonzorgcentrum-eikenberg",
    "eikenberg",
    "woonzorgcentrum-beukenhoff",
    "beukenhoff",
    "woonzorgcentrum-zilverlinde",
    "zilverlinde",
    "woonzorgcentrum-de-plataan",
    "de-plataan",
    "eyckenhof",
    "woonzorgcentrum-eycken",
    "huize-van-waas",
    "de-witte-meersen",
    "woonzorgcentrum-den-houtmolen",
    "den-houtmolen",
    "ter-lammeken",
    "woonzorgcentrum-ter-lammeken",
    "aksent",
    "woonzorgcentrum-crayenhof",
    "crayenhof",
    "huize-ter-linde",
    "de-hoeksteen",
    "immaculata",
    "stil-geluk",
    "hof-ter-lande",
    "woonzorg-netwerk-edegem",
    "vulpia",  # mined
    "armonea",  # mined
    "solidum",
    "ipfbw",
    "woonzorgcentrum-sint-anna-antwerpen",
    "woonzorgcentrum-heilige-familie",
    "heilige-familie-wzc",
    "woonzorgcentrum-onze-lieve-vrouw",
    "woonzorgcentrum-sint-bernardus",
    "woonzorgcentrum-de-wijngaard",
    "de-wijngaard",
    "woonzorgcentrum-ten-bos",
    "ten-bos",
    "woonzorgcentrum-het-anker",
    "het-anker",
    "woonzorgcentrum-de-vijvers",
    "de-vijvers",
    "woonzorgcentrum-sainte-anne",
    "home-saint-anne",
    "maison-de-repos",
    "residence-du-parc",
    "woonzorgcentrum-ter-rade",
    "ter-rade",
    "woonzorgcentrum-de-wyngaerd",
    "de-wyngaerd",
    "woonzorgcentrum-huis-perrekes",
    "huis-perrekes",
    "perrekes",
    "woonzorgcentrum-sint-jozef-herent",
    "sint-jozef-herent",
    "woonzorgcentrum-de-witte-bergen",
    "de-witte-bergen",
    "woonzorgcentrum-avontuur",
    "woonzorgcentrum-lindenhof-leuven",
    "woonzorgcentrum-hogerlucht",
    "hogerlucht",
    "woonzorgcentrum-novalis",
    "novalis",
    "woonzorgcentrum-vinkenbos",
    "vinkenbos",
    "woonzorgcentrum-de-notenboom",
    "de-notenboom",
    "woonzorgcentrum-zilverberk",
    "zilverberk",
    "woonzorgcentrum-zonnig-hof",
    "zonnig-hof",
    "woonzorgcentrum-de-zavel",
    "de-zavel",
    "woonzorgcentrum-klokkehof",
    "klokkehof",
    "woonzorgcentrum-berkenhof",
    "berkenhof",
    "woonzorgcentrum-huize-zonnig",
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
    kbo = re.search(r"/nl/(0?\d{9,10})/", html) or re.search(r"BE0?(\d{9,10})", html)
    return {
        "ye": ye.group(1) if ye else None,
        "first": first.groups() if first else None,
        "filed": filed.group(1) if filed else None,
        "fte": fte.group(1) if fte else None,
        "title": re.sub(r"\s+", " ", title.group(1)).strip() if title else None,
        "kbo": kbo.group(1) if kbo else None,
    }


def main():
    blob = mined_blob()
    live = []
    seen = set()
    for slug in SLUGS:
        url = f"https://www.companyweb.be/nl/{slug}"
        try:
            html = fetch(url)
        except Exception:
            continue
        if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
            continue
        if "kernCijfers" not in html:
            continue
        info = parse_ye(html)
        kb = info["kbo"] or "?"
        if kb.isdigit() and len(kb) == 9:
            kb = "0" + kb
        if kb in seen:
            continue
        seen.add(kb)
        dotted = f"{kb[:4]}.{kb[4:7]}.{kb[7:]}" if kb.isdigit() and len(kb) == 10 else kb
        already = dotted in blob or kb in blob
        title = info["title"] or ""
        form = "VZW" if "(VZW)" in title or "(ASBL)" in title else ("NV" if "(NV)" in title or "(SA)" in title else "?")
        print(
            "HIT",
            slug,
            "YE",
            info["ye"],
            "mined" if already else "FRESH",
            form,
            dotted,
            title[:55],
            "omzet",
            info["first"][4] if info["first"] else None,
        )
        if info["ye"] == "2025" and not already and form == "VZW":
            (RAW / f"cand_{kb}_nl.html").write_text(html, encoding="utf-8")
            live.append((dotted, slug, info, kb))
            print("  *** FRESH VZW YE2025 ***")

    print("\nFRESH VZW YE2025 count", len(live))
    for d, s, info, k in live:
        print("->", d, s, info["first"], info["fte"], info["title"][:60])


if __name__ == "__main__":
    main()

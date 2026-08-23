# -*- coding: utf-8 -*-
"""Final hunt: named WZC/zorg VZW + decide unit."""
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

# Named candidates (slug, kbo) — Flemish WZC / zorg not obviously in do-not-redo
NAMED = [
    ("de-witte-meersen", None),
    ("huize-van-waas", None),
    ("woonzorgcentrum-den-houtmolen", None),
    ("woonzorgcentrum-ter-linden", None),
    ("woonzorgcentrum-sint-jozef-herent", None),
    ("woonzorgcentrum-bethanie", None),
    ("bethanie", None),
    ("woonzorgcentrum-de-bijster", None),
    ("de-bijster", None),
    ("woonzorgcentrum-zonnig-huis", None),
    ("zonnig-huis", None),
    ("woonzorgcentrum-het-gielsbos", None),
    ("gielsbos", None),
    ("pc-gheel", None),
    ("woonzorgcentrum-magnolia", None),
    ("magnolia-woonzorg", None),
    ("woonzorgcentrum-onderdale", None),
    ("onderdale", None),
    ("olivetenhof", None),
    ("woonzorgcentrum-olivetenhof", None),
    ("philippus", None),
    ("avondvrede", None),
    ("helianthus", "0466266429"),
    ("hof-ter-lande", "0480566704"),
    ("stil-geluk", "0443249616"),
    ("de-hoeksteen", "0598966387"),
    ("immaculata", "0685516024"),
    ("slg-operaties-vlaanderen", "0845064196"),
    ("emeis-belgium", "0887690451"),
    ("woonzorgcentrum-sint-anna", None),
    ("sint-anna-woonzorg", None),
    ("woonzorgcentrum-sint-rochus", None),
    ("woonzorgcentrum-onze-lieve-vrouw", None),
    ("woonzorgcentrum-de-meander", None),
    ("de-meander", None),
    ("woonzorgcentrum-aqua", None),
    ("woonzorgcentrum-eycken", None),
    ("eyckenhof", None),
    ("woonzorgcentrum-parkhof", None),
    ("parkhof", None),
    ("woonzorgcentrum-rozenhof", None),
    ("rozenhof", None),
    ("woonzorgcentrum-zilverlinde", None),
    ("zilverlinde", None),
    ("woonzorgcentrum-de-plataan", None),
    ("de-plataan", None),
    ("woonzorgcentrum-lindenhof", None),
    ("lindenhof", None),
    ("woonzorgcentrum-beukenhoff", None),
    ("beukenhoff", None),
    ("woonzorgcentrum-eikenberg", None),
    ("eikenberg", None),
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
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
    kbo = re.search(r"BE0?(\d{9,10})", html)
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
    for slug, kbo in NAMED:
        urls = []
        if kbo:
            urls.append(f"https://www.companyweb.be/nl/{kbo}/{slug}")
            urls.append(f"https://www.companyweb.be/nl/{kbo}")
        urls.append(f"https://www.companyweb.be/nl/search?q={slug}")
        # direct slug path often works as CW SEO
        urls.insert(0, f"https://www.companyweb.be/nl/{slug}")
        html = None
        used = None
        for url in urls[:3]:
            try:
                html = fetch(url)
                if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                    html = None
                    continue
                # search pages won't have kernCijfers
                if "kernCijfers" in html or "amountOfEmployees" in html:
                    used = url
                    break
                html = None
            except Exception:
                html = None
        if not html:
            continue
        info = parse_ye(html)
        t = info["title"] or ""
        kb = info["kbo"] or kbo or "?"
        dotted = None
        if kb and kb.isdigit():
            if len(kb) == 9:
                kb = "0" + kb
            if len(kb) == 10:
                dotted = f"{kb[:4]}.{kb[4:7]}.{kb[7:]}"
        already = False
        if dotted and (dotted in blob or kb in blob):
            already = True
        if any(x in t.lower() for x in ["armonea", "always home", "vulpia"]) and already:
            continue
        print(
            "HIT",
            slug,
            "YE",
            info["ye"],
            "mined" if already else "fresh",
            dotted,
            t[:70],
            "omzet",
            info["first"][4] if info["first"] else None,
        )
        if info["ye"] == "2025" and not already:
            live.append((dotted, t, info, used))
            path = RAW / f"cand_{kb}_nl.html"
            path.write_text(html, encoding="utf-8")
            print("  *** SAVED", path.name)

    print("\nFRESH YE2025 count", len(live))
    for d, t, info, u in live:
        print("->", d, t[:70], info["first"], info["fte"], u)


if __name__ == "__main__":
    main()

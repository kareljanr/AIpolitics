# -*- coding: utf-8 -*-
"""Probe prefer-path + unused YE2025 WZC cands for tick 2096."""
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
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
csv.field_size_limit(10**7)

PREFER = [
    ("faro_nl", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl", "https://www.companyweb.be/nl/0201712587/a-i-e-s-h"),
    ("rew_nl", "https://www.companyweb.be/nl/0644638937/rew"),
    ("bornem_jr", "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"),
]

# Leftover / deferred WZC from prior ticks + fresh named care VZWs
CANDS = [
    ("0466266429", "helianthus"),
    ("0480566704", "hof-ter-lande-woon-en-zorgcentrum"),
    ("0443249616", "rusthuis-stil-geluk"),
    ("0685516024", "immaculata"),
    ("0598966387", "de-witte-bergen"),
    ("0845064196", "huize-ter-linde"),
    ("0887690451", "woonzorg-netwerk"),
    ("0422620585", "aksent"),
    ("0441313178", "woonzorgcentrum-de-vijvers"),
    ("0471977452", "woon-zorgcentrum-het-anker"),
    ("0479628079", "woonzorgcentrum-sint-jozef"),
    ("0795384162", "woonzorgcentrum-bethanie"),
    ("0415223344", "woonzorgcentrum-de-vijvers"),
    ("0428901122", "woon-zorgcentrum-het-anker"),
    ("0405741862", "huis-van-de-toekomst"),
    ("0410853396", "de-lovie"),  # mined
    ("0428374764", "begralim"),  # mined
    ("0410151137", "sint-lucia"),  # mined
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as r:
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
    print("=== PREFER ===")
    for name, url in PREFER:
        try:
            html = fetch(url)
            (RAW / f"{name}.html").write_text(html, encoding="utf-8")
            if "bornem" in name:
                plain = re.sub(r"<[^>]+>", " ", html).lower()
                print(name, "OK", "jr2025?", ("2025" in plain and "jaarrekening" in plain), "len", len(html))
            else:
                info = parse_ye(html)
                print(name, "YE", info["ye"], "filed", info["filed"], "omzet", info["first"][4] if info["first"] else None)
        except Exception as e:
            print(name, "FAIL", type(e).__name__, str(e)[:120])

    blob = mined_blob()
    print("\n=== CANDS ===")
    live = []
    for kbo, slug in CANDS:
        dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
        already = dotted in blob or kbo in blob
        if already:
            print("MINED", dotted, slug)
            continue
        url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
        try:
            html = fetch(url)
            if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                html = fetch(f"https://www.companyweb.be/nl/{kbo}")
                if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                    print("404", dotted, slug)
                    continue
            info = parse_ye(html)
            (RAW / f"cand_{kbo}_nl.html").write_text(html, encoding="utf-8")
            print(
                "HIT",
                dotted,
                "YE",
                info["ye"],
                "filed",
                info["filed"],
                "fte",
                info["fte"],
                (info["title"] or "?")[:65],
            )
            if info["first"]:
                print(
                    " ",
                    info["first"][0],
                    "winst",
                    info["first"][1],
                    "eq",
                    info["first"][2],
                    "bruto",
                    info["first"][3],
                    "omzet",
                    info["first"][4],
                )
            if info["ye"] == "2025":
                live.append((dotted, slug, info, kbo))
                print("  *** YE2025 FRESH ***")
        except Exception as e:
            print("FAIL", dotted, slug, type(e).__name__, str(e)[:120])

    print("\nFRESH YE2025:", len(live))
    for d, s, info, k in live:
        print(" ->", d, s, "omzet", info["first"][4] if info["first"] else None, "fte", info["fte"])


if __name__ == "__main__":
    main()

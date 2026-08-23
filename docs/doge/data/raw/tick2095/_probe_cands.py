# -*- coding: utf-8 -*-
"""Probe prefer-path + unused YE2025 WZC cands for tick 2095."""
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

# Known leftover / deferred WZC from prior ticks (slugs matter for CW SEO URLs)
CANDS = [
    ("0466266429", "helianthus"),
    ("0696715807", "woonzorgcentrum-crayenhof"),
    ("0480566704", "hof-ter-lande-woon-en-zorgcentrum"),
    ("0443249616", "rusthuis-stil-geluk"),
    ("0685516024", "immaculata"),
    ("0415223344", "woonzorgcentrum-de-vijvers"),
    ("0428901122", "woon-zorgcentrum-het-anker"),
    ("0598966387", "de-witte-bergen"),
    ("0845064196", "huize-ter-linde"),
    ("0887690451", "woonzorg-netwerk"),
    ("0422620585", "aksent"),
    ("0417.850.640".replace(".", ""), "zilverbos"),
    ("0409.705.825".replace(".", ""), "de-mijlpaal"),
    ("0436.978.070".replace(".", ""), "crematorium-hasselt"),  # likely mined
    ("0471.475.527".replace(".", ""), "zilvervogel"),  # mined
    ("0407.601.720".replace(".", ""), "lidwina"),  # mined
    ("0410.151.137".replace(".", ""), "sint-lucia"),  # mined
    ("0413.653.827".replace(".", ""), "sint-elisabeth-s-dal"),  # mined
    # additional WZC often deferred in care scans
    ("0405.741.862".replace(".", ""), "huis-van-de-toekomst"),
    ("0415.234.567".replace(".", ""), "bad"),
    ("0424.123.789".replace(".", ""), "bad2"),
    ("0435.678.901".replace(".", ""), "bad3"),
    ("0446.789.012".replace(".", ""), "bad4"),
    ("0457.890.123".replace(".", ""), "bad5"),
    ("0468.901.234".replace(".", ""), "bad6"),
    ("0479.012.345".replace(".", ""), "bad7"),
    ("0480.566.704".replace(".", ""), "hof-ter-lande-alt"),
    ("0491.234.567".replace(".", ""), "bad8"),
    ("0502.345.678".replace(".", ""), "bad9"),
    ("0513.456.789".replace(".", ""), "bad10"),
    ("0524.567.890".replace(".", ""), "bad11"),
    ("0535.678.901".replace(".", ""), "bad12"),
    ("0546.789.012".replace(".", ""), "bad13"),
    ("0557.890.123".replace(".", ""), "bad14"),
    ("0568.901.234".replace(".", ""), "bad15"),
    ("0579.012.345".replace(".", ""), "bad16"),
    ("0580.123.456".replace(".", ""), "bad17"),
    ("0601.234.567".replace(".", ""), "bad18"),
    ("0612.345.678".replace(".", ""), "bad19"),
    ("0623.456.789".replace(".", ""), "bad20"),
    ("0634.567.890".replace(".", ""), "bad21"),
    ("0645.678.901".replace(".", ""), "bad22"),
    ("0656.789.012".replace(".", ""), "bad23"),
    ("0667.890.123".replace(".", ""), "bad24"),
    ("0678.901.234".replace(".", ""), "bad25"),
    ("0689.012.345".replace(".", ""), "bad26"),
    ("0701.234.567".replace(".", ""), "bad27"),
    ("0712.345.678".replace(".", ""), "bad28"),
    ("0723.456.789".replace(".", ""), "bad29"),
    ("0734.567.890".replace(".", ""), "bad30"),
    ("0745.678.901".replace(".", ""), "bad31"),
    ("0756.789.012".replace(".", ""), "bad32"),
    ("0767.890.123".replace(".", ""), "bad33"),
    ("0778.901.234".replace(".", ""), "bad34"),
    ("0789.012.345".replace(".", ""), "bad35"),
    ("0801.234.567".replace(".", ""), "bad36"),
    ("0812.345.678".replace(".", ""), "bad37"),
    ("0823.456.789".replace(".", ""), "bad38"),
    ("0834.567.890".replace(".", ""), "bad39"),
    ("0856.789.012".replace(".", ""), "bad40"),
    ("0867.890.123".replace(".", ""), "bad41"),
    ("0878.901.234".replace(".", ""), "bad42"),
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
                print(name, "OK", "2025?", ("2025" in plain and "jaarrekening" in plain), "len", len(html))
            else:
                info = parse_ye(html)
                print(name, "YE", info["ye"], "filed", info["filed"], "omzet", info["first"][4] if info["first"] else None)
        except Exception as e:
            print(name, "FAIL", e)

    blob = mined_blob()
    print("\n=== CANDS (real slugs only) ===")
    live = []
    for kbo, slug in CANDS:
        if slug.startswith("bad"):
            continue
        dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
        already = dotted in blob or kbo in blob or slug.replace("-", " ") in blob
        if already and kbo not in ("0893863017", "0201712587", "0644638937"):
            print("MINED", dotted, slug)
            continue
        url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
        try:
            html = fetch(url)
            if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                # try without slug
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
                "mined" if already else "fresh",
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
            if info["ye"] == "2025" and not already:
                live.append((dotted, slug, info))
                print("  *** YE2025 FRESH ***")
        except Exception as e:
            print("FAIL", dotted, slug, type(e).__name__, str(e)[:120])

    print("\nFRESH YE2025:", len(live))
    for d, s, info in live:
        print(" ->", d, s, "omzet", info["first"][4] if info["first"] else None, "fte", info["fte"])


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Probe prefer-path + unused WZC YE2025 candidates for tick 2095."""
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

# Unused WZC/zorg candidates deferred in prior ticks (from tick2091 probe list leftovers)
CANDS = [
    ("0466266429", "helianthus"),
    ("0696715807", "woonzorgcentrum-crayenhof"),
    ("0480566704", "hof-ter-lande-woon-en-zorgcentrum"),
    ("0443249616", "rusthuis-stil-geluk"),
    ("0685516024", "immaculata"),
    ("0415223344", "woonzorgcentrum-de-vijvers"),
    ("0428901122", "woon-zorgcentrum-het-anker"),
    ("0422620585", "aksent"),  # may be mined
    ("0598966387", "woonzorgcentrum-de-witte-bergen"),
    ("0845064196", "huize-ter-linde"),
    ("0887690451", "woonzorgnetwerk"),
    ("0478.123.456".replace(".", ""), "skip"),  # placeholder invalid
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
        return r.read().decode("utf-8", errors="replace")


def mined_blob() -> str:
    blob = ""
    for fname in ["entities.csv", "research_queue.csv", "commitments.csv"]:
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
                print(
                    name,
                    "OK",
                    len(html),
                    "2025_jr",
                    "jaarrekening 2025" in plain or "jr2025" in plain,
                    "2024_hits",
                    plain.count("2024"),
                )
                for m in re.finditer(r'href="([^"]+\.pdf[^"]*)"', html, re.I):
                    print("  pdf", m.group(1)[:120])
            else:
                info = parse_ye(html)
                print(name, "YE", info["ye"], "filed", info["filed"], "omzet", info["first"][4] if info["first"] else None)
        except Exception as e:
            print(name, "FAIL", e)

    blob = mined_blob()
    print("\n=== CANDS ===")
    # also scan tick2084 cand files and tick2091 leftovers for unused YE2025
    extra = [
        ("0466266429", "helianthus"),
        ("0696715807", "woonzorgcentrum-crayenhof"),
        ("0480566704", "hof-ter-lande-woon-en-zorgcentrum"),
        ("0443249616", "rusthuis-stil-geluk"),
        ("0685516024", "immaculata"),
        ("0415223344", "woonzorgcentrum-de-vijvers"),
        ("0428901122", "woon-zorgcentrum-het-anker"),
        ("0598966387", "de-witte-bergen"),
        ("0845064196", "huize-ter-linde"),
        ("0887690451", "woonzorg-netwerk-kempen"),
        ("0422620585", "aksent-vzw"),
        ("0478129123", "placeholder-skip"),
        ("0405.820.xxx".replace(".", "").replace("x", "0"), "skip2"),
        ("0435123456", "skip3"),
        ("0456789012", "skip4"),
        # from earlier deferred notes / common WZC
        ("0417.850.640".replace(".", ""), "zilverbos"),
        ("0429.123.456".replace(".", ""), "skip5"),
        ("0465.123.789".replace(".", ""), "skip6"),
        ("0409.705.825".replace(".", ""), "rusthuis-de-mijlpaal"),
        ("0475.901.234".replace(".", ""), "skip7"),
        ("0412.345.678".replace(".", ""), "skip8"),
        ("0438.654.321".replace(".", ""), "skip9"),
        ("0445.112.233".replace(".", ""), "skip10"),
        ("0451.998.877".replace(".", ""), "skip11"),
        ("0460.554.433".replace(".", ""), "skip12"),
        ("0472.110.099".replace(".", ""), "skip13"),
        ("0482.776.655".replace(".", ""), "skip14"),
        ("0490.332.211".replace(".", ""), "skip15"),
        ("0501.223.344".replace(".", ""), "skip16"),
        ("0520.998.877".replace(".", ""), "skip17"),
        ("0535.667.788".replace(".", ""), "skip18"),
        ("0544.112.233".replace(".", ""), "skip19"),
        ("0555.443.322".replace(".", ""), "skip20"),
        ("0566.778.899".replace(".", ""), "skip21"),
        ("0577.889.900".replace(".", ""), "skip22"),
        ("0588.001.122".replace(".", ""), "skip23"),
        ("0600.112.233".replace(".", ""), "skip24"),
        ("0611.223.344".replace(".", ""), "skip25"),
        ("0622.334.455".replace(".", ""), "skip26"),
        ("0633.445.566".replace(".", ""), "skip27"),
        ("0644.556.677".replace(".", ""), "skip28"),
        ("0655.667.788".replace(".", ""), "skip29"),
        ("0666.778.899".replace(".", ""), "skip30"),
        ("0677.889.900".replace(".", ""), "skip31"),
        ("0688.990.011".replace(".", ""), "skip32"),
        ("0699.001.122".replace(".", ""), "skip33"),
        ("0700.112.233".replace(".", ""), "skip34"),
        ("0711.223.344".replace(".", ""), "skip35"),
        ("0722.334.455".replace(".", ""), "skip36"),
        ("0733.445.566".replace(".", ""), "skip37"),
        ("0744.556.677".replace(".", ""), "skip38"),
        ("0755.667.788".replace(".", ""), "skip39"),
        ("0766.778.899".replace(".", ""), "skip40"),
        ("0777.889.900".replace(".", ""), "skip41"),
        ("0788.990.011".replace(".", ""), "skip42"),
        ("0799.001.122".replace(".", ""), "skip43"),
        ("0800.112.233".replace(".", ""), "skip44"),
        ("0811.223.344".replace(".", ""), "skip45"),
        ("0822.334.455".replace(".", ""), "skip46"),
        ("0833.445.566".replace(".", ""), "skip47"),
        ("0855.667.788".replace(".", ""), "skip48"),
        ("0866.778.899".replace(".", ""), "skip49"),
        ("0877.889.900".replace(".", ""), "skip50"),
    ]
    # Better: reuse known good cand list from tick2084/2091 files on disk
    from_disk = []
    for tick in ["tick2084", "tick2091"]:
        d = DATA / "raw" / tick
        if d.exists():
            for p in d.glob("cand_*_nl.html"):
                kbo = p.name.replace("cand_", "").replace("_nl.html", "")
                from_disk.append(kbo)
    print("from_disk cands", from_disk)

    seen = set()
    live_ye2025 = []
    for kbo in from_disk + [c[0] for c in CANDS if not c[1].startswith("skip")]:
        kbo = kbo.replace(".", "")
        if kbo in seen or len(kbo) != 10:
            continue
        seen.add(kbo)
        dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
        if dotted in blob or kbo in blob:
            # still allow prefer-path entities
            if kbo not in ("0893863017", "0201712587", "0644638937"):
                print("MINED", dotted)
                continue
        # slug unknown — try companyweb search by number path
        url = f"https://www.companyweb.be/nl/{kbo}"
        try:
            html = fetch(url)
            if "Page Not Found" in html or "pagina niet gevonden" in html.lower():
                print("404", dotted)
                continue
            info = parse_ye(html)
            title = info["title"] or "?"
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
                "title",
                (title[:70] if title else "?"),
            )
            if info["first"]:
                print(" ", info["first"][0], "winst", info["first"][1], "eq", info["first"][2], "bruto", info["first"][3], "omzet", info["first"][4])
            if info["ye"] == "2025":
                live_ye2025.append((dotted, title, info))
                print("  *** YE2025 ***")
        except Exception as e:
            print("FAIL", dotted, type(e).__name__, str(e)[:100])

    print("\nLIVE YE2025 unused:", len(live_ye2025))
    for d, t, info in live_ye2025:
        print(" ->", d, t[:60], "omzet", info["first"][4] if info["first"] else None)


if __name__ == "__main__":
    main()

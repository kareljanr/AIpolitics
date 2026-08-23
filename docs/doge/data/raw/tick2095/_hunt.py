# -*- coding: utf-8 -*-
"""Check Bornem JR2025 PDF + hunt unused public WZC VZW YE2025."""
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

# Public-ish WZC / zorg VZWs from prior deferrals and common Flemish care operators
CANDS = [
    ("0418.234.567".replace(".", ""), "x"),  # skip pattern
    # From tick2084 cand filenames that may still be unused
    ("0422620585", "aksent"),  # mined
    ("0443249616", "rusthuis-stil-geluk"),
    ("0466266429", "helianthus"),
    ("0480566704", "hof-ter-lande-woon-en-zorgcentrum"),
    ("0598966387", "de-hoeksteen"),
    ("0685516024", "woonzorgnetwerk-edegem"),
    # More plausible Flemish WZC VZWs
    ("0405.112.085".replace(".", ""), "familiezorg"),  # mined
    ("0416.493.254".replace(".", ""), "ben"),  # mined
    ("0428.659.430".replace(".", ""), "mater-dei"),  # mined
    ("0407.040.308".replace(".", ""), "sint-carolus-mayerhof"),  # mined
    ("0459.770.496".replace(".", ""), "sint-augustinus"),  # mined
    # Try Zilverbos sister / other
    ("0420.656.336".replace(".", ""), "rikolto"),
    ("0434.364.713".replace(".", ""), "natuurpunt"),
    # Care: look for YE2025 on known unused from progress notes
    ("0475.345.821".replace(".", ""), "avondvrede"),
    ("0408.516.488".replace(".", ""), "welvaart"),  # mined
    ("0411.600.692".replace(".", ""), "marias-rustoord"),  # mined
    ("0405.820.711".replace(".", ""), "ten-anker"),  # maybe mined as Ten Anker
    ("0419.876.543".replace(".", ""), "bad"),
    # Northdata-style known WZC
    ("0425.728.191".replace(".", ""), "woonzorgcentrum-ter-lammeken"),
    ("0432.111.222".replace(".", ""), "bad2"),
    ("0441.333.444".replace(".", ""), "bad3"),
    ("0450.555.666".replace(".", ""), "bad4"),
    ("0460.777.888".replace(".", ""), "bad5"),
    ("0470.999.000".replace(".", ""), "bad6"),
    ("0485.111.222".replace(".", ""), "bad7"),
    ("0495.333.444".replace(".", ""), "bad8"),
    ("0505.555.666".replace(".", ""), "bad9"),
    ("0515.777.888".replace(".", ""), "bad10"),
    ("0525.999.000".replace(".", ""), "bad11"),
    ("0535.111.222".replace(".", ""), "bad12"),
    ("0545.333.444".replace(".", ""), "bad13"),
    ("0555.555.666".replace(".", ""), "bad14"),
    ("0565.777.888".replace(".", ""), "bad15"),
    ("0575.999.000".replace(".", ""), "bad16"),
    ("0585.111.222".replace(".", ""), "bad17"),
    ("0605.333.444".replace(".", ""), "bad18"),
    ("0615.555.666".replace(".", ""), "bad19"),
    ("0625.777.888".replace(".", ""), "bad20"),
    ("0635.999.000".replace(".", ""), "bad21"),
    ("0645.111.222".replace(".", ""), "bad22"),
    ("0655.333.444".replace(".", ""), "bad23"),
    ("0665.555.666".replace(".", ""), "bad24"),
    ("0675.777.888".replace(".", ""), "bad25"),
    ("0695.999.000".replace(".", ""), "bad26"),
    ("0705.111.222".replace(".", ""), "bad27"),
    ("0715.333.444".replace(".", ""), "bad28"),
    ("0725.555.666".replace(".", ""), "bad29"),
    ("0735.777.888".replace(".", ""), "bad30"),
    ("0745.999.000".replace(".", ""), "bad31"),
    ("0755.111.222".replace(".", ""), "bad32"),
    ("0765.333.444".replace(".", ""), "bad33"),
    ("0775.555.666".replace(".", ""), "bad34"),
    ("0785.777.888".replace(".", ""), "bad35"),
    ("0795.999.000".replace(".", ""), "bad36"),
    ("0805.111.222".replace(".", ""), "bad37"),
    ("0815.333.444".replace(".", ""), "bad38"),
    ("0825.555.666".replace(".", ""), "bad39"),
    ("0835.777.888".replace(".", ""), "bad40"),
    ("0855.999.000".replace(".", ""), "bad41"),
    ("0865.111.222".replace(".", ""), "bad42"),
    ("0875.333.444".replace(".", ""), "bad43"),
    ("0885.555.666".replace(".", ""), "bad44"),
    ("0895.777.888".replace(".", ""), "bad45"),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as r:
        return r.read()


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


def check_bornem():
    html = (RAW / "bornem_jr.html").read_text(encoding="utf-8", errors="replace")
    print("=== BORNEM LINKS ===")
    for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{0,120})', html, re.I):
        href, txt = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
        blob = (href + " " + txt).lower()
        if any(k in blob for k in ["jaarrekening", "agb", "2025", "2024", "pdf", "bbc", "2023"]):
            print(" ", txt[:90], "->", href[:160])
    # absolute PDF URLs
    for m in re.finditer(r'(https?://[^"\s>]+\.pdf)', html, re.I):
        print(" ABS PDF", m.group(1)[:160])
    # relative pdf
    for m in re.finditer(r'href="([^"]+\.pdf[^"]*)"', html, re.I):
        href = m.group(1)
        if href.startswith("/"):
            href = "https://www.bornem.be" + href
        print(" TRY", href[:160])
        try:
            data = fetch(href)
            print("  OK", len(data), data[:20])
            (RAW / ("bornem_" + Path(href).name[:40])).write_bytes(data)
        except Exception as e:
            print("  FAIL", e)


def main():
    check_bornem()

    # Re-check SLG / emeis for public dual status — prefer skip private chains
    print("\n=== PRIVATE CHAIN CHECK ===")
    for name in ["cand_0845064196_nl.html", "cand_0887690451_nl.html"]:
        p = RAW / name
        if not p.exists():
            continue
        h = p.read_text(encoding="utf-8", errors="replace")
        info = parse_ye(h)
        print(name, info["title"], "YE", info["ye"])
        # NACE / form
        for pat in [r"NACE[^<]{0,40}", r"Rechtsvorm[^<]{0,40}", r"NV|VZW|ASBL"]:
            pass
        if "Slg" in (info["title"] or "") or "emeis" in (info["title"] or "").lower():
            print("  NOTE: private care chain — prefer public VZW over this unless dual explicitly wanted")

    # Hunt from tick2084 cand files on disk (already fetched earlier)
    print("\n=== DISK CANDS tick2084/2091 ===")
    blob = mined_blob()
    live = []
    for tick in ["tick2084", "tick2091", "tick2095"]:
        d = DATA / "raw" / tick
        if not d.exists():
            continue
        for p in sorted(d.glob("cand_*_nl.html")):
            kbo = p.name.replace("cand_", "").replace("_nl.html", "")
            dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
            h = p.read_text(encoding="utf-8", errors="replace")
            info = parse_ye(h)
            title = info["title"] or "?"
            already = dotted in blob or kbo in blob
            # skip prefer-path
            if kbo in ("0893863017", "0201712587", "0644638937", "0410151137", "0407601720", "0413653827", "0471475527"):
                continue
            if info["ye"] == "2025":
                form = "VZW" if "(VZW)" in title or "(ASBL)" in title else ("NV" if "(NV)" in title else "?")
                print(
                    "YE2025",
                    dotted,
                    "mined" if already else "FRESH",
                    form,
                    title[:70],
                    "omzet",
                    info["first"][4] if info["first"] else None,
                    "fte",
                    info["fte"],
                )
                if not already and form == "VZW":
                    live.append((dotted, title, info, p))

    print("\nFRESH VZW YE2025:", len(live))
    for d, t, info, p in live:
        print(" ->", d, t[:70], info["first"])

    # Additional targeted fetches: known unused WZC names from loop_log deferrals
    print("\n=== TARGETED FETCH ===")
    targets = [
        ("0475345821", "avondvrede"),
        ("0417850640", "zilverbos"),
        ("0425728191", "ter-lammeken"),
        ("0405741862", "huis"),
        ("0451122334", "x"),
        ("0462233445", "y"),
        ("0473344556", "z"),
        ("0484455667", "a"),
        ("0495566778", "b"),
        ("0406687990", "c"),
        ("0417798001", "d"),
        ("0428809112", "e"),
        ("0439910223", "f"),
        ("0441021334", "g"),
        ("0452132445", "h"),
        ("0463243556", "i"),
        ("0474354667", "j"),
        ("0485465778", "k"),
        ("0496576889", "l"),
        # From git status raw tick2052 names
        ("0400.000.000".replace(".", ""), "skip"),
    ]
    # Parse avondvrede / other from tick2052 if HTML exists
    for p in (DATA / "raw" / "tick2052").glob("*avondvrede*"):
        print("have", p.name)
    for p in (DATA / "raw" / "tick2052").glob("*.html"):
        name = p.name.lower()
        if any(k in name for k in ["avondvrede", "onderdale", "olivetenhof", "philippus", "woonsprong", "zorgkas"]):
            h = p.read_text(encoding="utf-8", errors="replace")
            info = parse_ye(h)
            if info["ye"] or info["title"]:
                print("RAW2052", p.name, "YE", info["ye"], (info["title"] or "")[:60], "omzet", info["first"][4] if info["first"] else None)


if __name__ == "__main__":
    main()

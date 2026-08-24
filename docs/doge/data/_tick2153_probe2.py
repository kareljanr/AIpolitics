# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2153")
ua = {"User-Agent": "Mozilla/5.0"}
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()

for n in [
    "0500.915.423",
    "0500915423",
    "brabant wallon",
    "zs_brabant_wallon",
    "zs_bw",
    "0500.916.314",
    "0500.927.103",
    "0500.916.017",
    "0500.915.720",
    "0500.916.116",
    "0500.927.202",
    "zone de secours de liege",
    "hestalie",
    "5 sur sambre",
]:
    print("mined", n, n in ents)

# Known/likely Walloon ZDS KBOs
urls = {
    "bw_en.html": "0500915423",
    "bw_nl.html": "0500915423",
    "bw_fr.html": "0500915423",
    "bw_kbo.html": "kbo:0500915423",
    # try nearby numbers for other zones
    "z1_en.html": "0500915314",
    "z2_en.html": "0500915414",
    "z3_en.html": "0500915522",
    "z4_en.html": "0500915720",
    "z5_en.html": "0500915819",
    "z6_en.html": "0500916116",
    "z7_en.html": "0500916314",
    "z8_en.html": "0500916413",
    "z9_en.html": "0500916611",
    "z10_en.html": "0500916819",
    "z11_en.html": "0500917008",
    "z12_en.html": "0500917107",
    "z13_en.html": "0500917206",
    "z14_en.html": "0500917305",
    "z15_en.html": "0500927103",
    "z16_en.html": "0500927202",
    "z17_en.html": "0500927400",
    "z18_en.html": "0500927509",
}

for name, digits in urls.items():
    if digits.startswith("kbo:"):
        d = digits.split(":")[1]
        url = (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={d}"
        )
    else:
        d = digits
        url = f"https://www.companyweb.be/en/{d}"
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25) as r:
            data = r.read()
        (base / name).write_bytes(data)
        t = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)", t)
        tit = title.group(1) if title else "?"
        if "Error 404" in tit or "Page not found" in tit:
            print(name, d, "404")
            continue
        if "Gegevens" in tit and "kbo" in name:
            # check if entity found
            if "niet gevonden" in t.lower() or "geen onderneming" in t.lower():
                print(name, d, "KBO miss")
                continue
        fte = re.search(r'Employees\s*=\s*"([^"]+)"', t)
        # only print zone de secours hits
        if "secours" in tit.lower() or "hulpverlening" in tit.lower() or "zone" in tit.lower():
            print(name, d, "HIT", tit[:90], "fte", fte.group(1) if fte else None)
            years = re.findall(r"\n(202[0-9])\s*:", t)
            if years:
                print("  years", years[:4])
            for y in ["2025", "2024"]:
                mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
                if mm:
                    print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:200])
        else:
            print(name, d, "other", tit[:70])
    except Exception as e:
        print("FAIL", name, d, e)

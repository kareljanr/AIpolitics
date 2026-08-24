# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path
from shutil import copy

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2153")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0"}
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()

# prefs from prior
for src_name in ["bornem_en.html", "faro_en.html", "aiesh_en.html", "rew_en.html"]:
    for prev in ["tick2152", "tick2150", "tick2149"]:
        src = Path(rf"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\{prev}") / src_name
        if src.exists():
            copy(src, base / src_name)
            t = (base / src_name).read_text(encoding="utf-8", errors="replace")
            years = re.findall(r"\n(202[0-9])\s*:", t)
            title = re.search(r"<title>([^<]+)", t)
            print(
                "pref",
                src_name,
                "years",
                years[:5],
                (title.group(1)[:70] if title else None),
            )
            for y in ["2025", "2024"]:
                mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
                if mm:
                    print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:180])
            break

# unused Walloon ZDS candidates (KBO patterns from civil security list)
candidates = {
    "luxembourg": "0500916511",  # guess
    "luxembourg2": "0500927302",
    "dinant": "0500927301",  # dinaphi already
    "liege": "0500918000",
    "liege2": "0500916510",
    "charleroi": "0500916210",
    "namur": "0500927000",
    "niraye": "0500916711",
    "amblève": "0500916909",
    "hestalie": "0500916513",
    "hesbaye": "0500916512",  # done
    "wapi": "0500915621",  # done
}

# better: search CW for known unused zone names
for n in [
    "zs_vesdre",
    "vesdre",
    "0500.916.908",
    "luxembourg",
    "zs_luxembourg",
    "0500.918",
    "zone de secours liege",
    "zs_liege",
    "hestalie",
    "ambleve",
    "niraye",
    "charleroi",
    "monceau",
    "incendie",
]:
    print("mined", n, n in ents)

# Probe a few known Walloon ZDS KBOs from prior deferred lists / common
for name, digits in {
    "zst_lux_en.html": "0500918704",  # speculative
    "zst_liege_en.html": "0500918512",
    "zst_charleroi_en.html": "0500916215",  # zhc was 0500916215? no that was hainaut centre 0500.916.215
}.items():
    pass

# From securitecivile / known: try Luxembourg and Liège II / Amblève / 5 sur Sambre already VDS
known = {
    "lux_en.html": "https://www.companyweb.be/en/0500918704",
    "ambleve_en.html": "https://www.companyweb.be/en/0500916909",
    "hestalie_en.html": "https://www.companyweb.be/en/0500916513",
    "niraye_en.html": "https://www.companyweb.be/en/0500916711",
    "liege_en.html": "https://www.companyweb.be/en/0500918512",
    "charleroi_en.html": "https://www.companyweb.be/en/0500918000",
}

for name, url in known.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25) as r:
            data = r.read()
        (base / name).write_bytes(data)
        t = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)", t)
        tit = title.group(1)[:100] if title else "?"
        if "Error 404" in tit or "404" in tit:
            print(name, "404")
            continue
        fte = re.search(r'Employees\s*=\s*"([^"]+)"', t)
        years = re.findall(r"\n(202[0-9])\s*:", t)
        print(name, "OK", tit, "fte", fte.group(1) if fte else None, "years", years[:3])
        for y in ["2025", "2024"]:
            mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
            if mm:
                print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:200])
    except Exception as e:
        print("FAIL", name, e)

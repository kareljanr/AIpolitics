# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2151")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0"}
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()

for n in [
    "0500.916.908",
    "0500916908",
    "vesdre",
    "zs_vesdre",
    "val de sambre",
    "zs_val_de_sambre",
    "hemeco",
]:
    print("mined", n, n in ents)

# copy prefs from prior tick if present
from shutil import copy

for src_name in ["bornem_en.html", "faro_en.html", "aiesh_en.html", "rew_en.html"]:
    src = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2150") / src_name
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
            (title.group(1)[:80] if title else None),
        )
        for y in ["2025", "2024"]:
            mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
            if mm:
                print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:200])

for name, url in {
    "vesdre_en.html": "https://www.companyweb.be/en/0500916908",
    "vesdre_nl.html": "https://www.companyweb.be/nl/0500916908",
    "vesdre_fr.html": "https://www.companyweb.be/fr/0500916908",
    "vesdre_kbo.html": (
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
        "?lang=nl&ondernemingsnummer=0500916908"
    ),
}.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        (base / name).write_bytes(data)
        t = data.decode("utf-8", "replace")
        title = re.search(r"<title>([^<]+)", t)
        years = re.findall(r"\n(202[0-9])\s*:", t)
        print(
            name,
            "OK",
            len(data),
            "years",
            years[:5],
            (title.group(1)[:90] if title else None),
        )
        for y in ["2025", "2024"]:
            mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
            if mm:
                print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:280])
        m = re.search(r'Employees\s*=\s*"([^"]+)"', t)
        if m:
            print("  fte", m.group(1))
    except Exception as e:
        print("FAIL", name, e)

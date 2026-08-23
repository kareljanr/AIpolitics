# -*- coding: utf-8 -*-
import json
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2087")
RAW.mkdir(parents=True, exist_ok=True)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
KBO = "0418352387"
KBO_DOT = "0418.352.387"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()


pages = [
    ("lindelo_nl.html", f"https://www.companyweb.be/nl/{KBO}/lindelo"),
    ("lindelo_en.html", f"https://www.companyweb.be/en/{KBO}/lindelo"),
    ("lindelo_fr.html", f"https://www.companyweb.be/fr/{KBO}/lindelo"),
    (
        "kbo_lindelo.html",
        f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    ),
]
for name, url in pages:
    try:
        data = fetch(url)
        (RAW / name).write_bytes(data)
        print("OK", name, len(data))
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)

t = (RAW / "lindelo_nl.html").read_text(encoding="utf-8", errors="replace")
# extract kernCijfers JS object
m = re.search(r"kernCijfers\s*=\s*(\{.*?\});", t, re.S)
if not m:
    raise SystemExit("no kernCijfers")
# crude: pull year blocks
blocks = re.findall(
    r"(20\d\d)\s*:\s*\{([^}]*)\}",
    m.group(1),
)
data = {}
for year, body in blocks:
    row = {}
    for key in [
        "winst",
        "verlies",
        "eigen_vermogen",
        "bruto_marge",
        "omzet",
        "aantal_personeelsleden",
        "currency",
    ]:
        km = re.search(rf'{key}:\s*"([^"]*)"', body)
        if km:
            row[key] = km.group(1)
    data[year] = row
print(json.dumps(data, indent=2, ensure_ascii=False))

# also try English labels
te = (RAW / "lindelo_en.html").read_text(encoding="utf-8", errors="replace")
me = re.search(r"kernCijfers\s*=\s*(\{.*?\});", te, re.S)
if me:
    blocks_e = re.findall(r"(20\d\d)\s*:\s*\{([^}]*)\}", me.group(1))
    data_e = {}
    for year, body in blocks_e:
        row = {}
        for key in [
            "profit",
            "loss",
            "equity",
            "gross_margin",
            "turnover",
            "number_of_employees",
            "winst",
            "eigen_vermogen",
            "bruto_marge",
            "omzet",
            "aantal_personeelsleden",
        ]:
            km = re.search(rf'{key}:\s*"([^"]*)"', body)
            if km:
                row[key] = km.group(1)
        data_e[year] = row
    print("EN", json.dumps(data_e, indent=2, ensure_ascii=False))

filed = re.search(r"neergelegd op ([0-9.\-]+)", t)
print("filed", filed.group(1) if filed else "?")
# emails / address hints
for pat in [
    r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}",
    r"Lille",
    r"VZW",
    r"aanbestedende",
]:
    hits = re.findall(pat, t)
    if hits:
        print(pat, hits[:5])

# KBO status
tk = (RAW / "kbo_lindelo.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Status[^<]{0,40}",
    r"Actief|Stopgezet|Active",
    r"Rechtsvorm[^<]{0,80}",
    r"Adres van de zetel[\s\S]{0,200}",
    r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}",
]:
    mm = re.search(pat, tk, re.I)
    if mm:
        print("KBO", re.sub(r"\s+", " ", mm.group(0))[:180])

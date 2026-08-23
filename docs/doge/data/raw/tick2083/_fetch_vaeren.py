# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2083")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

KBO_DIGITS = "0444313151"


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = resp.read()
        final = resp.geturl()
    (RAW / name).write_bytes(data)
    print("OK", name, len(data), final)
    return data.decode("utf-8", "replace")


# mined check
mined = False
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if "0444.313.151" in str(r) or "0444313151" in str(r) or "de vaeren" in str(r).lower():
            print("ENT HIT", r.get("entity_id"), r.get("name_nl"))
            mined = True
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if "0444313151" in str(r) or "0444.313.151" in str(r) or "de vaeren" in str(r).lower():
            print("RQ HIT", r["task_id"], r["status"], (r.get("title") or "")[:80])
            mined = True
if mined:
    raise SystemExit("already mined")

for name, url in [
    ("vaeren_nl.html", f"https://www.companyweb.be/nl/{KBO_DIGITS}/de-vaeren"),
    ("vaeren_en.html", f"https://www.companyweb.be/en/{KBO_DIGITS}/de-vaeren"),
    ("vaeren_fr.html", f"https://www.companyweb.be/fr/{KBO_DIGITS}/de-vaeren"),
    ("kbo_vaeren.html", f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}"),
]:
    try:
        t = fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)
        continue

t = (RAW / "vaeren_nl.html").read_text(encoding="utf-8", errors="replace")
print("TITLE", re.search(r"<title>([^<]+)</title>", t).group(1)[:140])
ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
print("YE", ye.group(1) if ye else "?")
for ym in list(
    re.finditer(
        r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
        t,
    )
)[:4]:
    print("Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
filed = re.search(r"neergelegd op ([0-9\-]+)|filed on ([0-9\-]+)", t, re.I)
print("FILED", filed.group(0) if filed else "?")
fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
print("FTE", fte.group(1) if fte else "?")
print("spans", re.findall(r"<span>(\d+[\.,]\d)</span>", t)[:5])

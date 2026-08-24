# -*- coding: utf-8 -*-
from pathlib import Path
import re
import csv
import ssl
import urllib.request

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0"}
out = Path(__file__).resolve().parent


def fetch(url, path):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    path.write_bytes(data)
    return data.decode("utf-8", "ignore")


def check(label, t):
    year = re.search(r"Last balance sheet year.{0,120}", t, re.S | re.I)
    plain = re.sub(r"<[^>]+>", " ", year.group(0)) if year else ""
    plain = re.sub(r"\s+", " ", plain)
    print(label, "YEAR_SNIP", plain[:120])
    for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t)[:3]:
        om = re.search(r'omzet:\s*"([^"]*)"', body)
        wi = re.search(r'winst:\s*"([^"]*)"', body)
        br = re.search(r'bruto_marge:\s*"([^"]*)"', body)
        eq = re.search(r'eigen_vermogen:\s*"([^"]*)"', body)
        print(f"  {y} omzet={om.group(1) if om else None} winst={wi.group(1) if wi else None} bruto={br.group(1) if br else None} eq={eq.group(1) if eq else None}")
    filed = re.search(r"filed on[^0-9]{0,20}(\d{2}-\d{2}-20\d\d)", t, re.I)
    print("  filed", filed.group(1) if filed else "-")


for label, url in [
    ("wznd", "https://www.companyweb.be/en/0500952540"),
    ("lork", "https://www.companyweb.be/en/0446022331"),
    ("delinde", "https://www.companyweb.be/en/0467355403"),
    ("aiesh", "https://www.companyweb.be/en/0201712587"),
]:
    t = fetch(url, out / f"{label}_en_full.html")
    check(label, t)

# mined check
with open(Path(r"docs/doge/data/entities.csv"), newline="", encoding="utf-8") as f:
    blob = "\n".join(" ".join(str(v) for v in r.values()) for r in csv.DictReader(f))
for n in ["0500952540", "0500.952.540", "woonzorgnet-dijleland", "woonzorgnet dijleland", "0446022331", "0446.022.331", "foyer de lork", "0467355403", "0467.355.403", "de linde", "lievegem"]:
    print("ENT", n, "YES" if n.lower().replace(".", "") in blob.lower().replace(".", "") else "NO")

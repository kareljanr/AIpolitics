# ephemeral probe tick2062
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2062")
outdir.mkdir(parents=True, exist_ok=True)

with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    ents = list(csv.DictReader(f))


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                return m.group(1)
    return None


def parse_blocks(html):
    return re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )


cands = [
    ("agb_bornem", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    ("faro", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh", "https://www.companyweb.be/en/0201712587/aiesh"),
    ("rew", "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre"),
    ("wezembeek", "https://www.companyweb.be/en/0433419259/woon-en-zorgcentrum-onze-lieve-vrouw-te-wezembeek-oppem"),
    ("sint_antonius", "https://www.companyweb.be/en/0424236725/woon-en-zorgcentrum-sint-antonius"),
]

for name, url in cands:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}_en.html").write_text(html, encoding="utf-8")
        emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
        title = re.search(r"<title>([^<]+)", html)
        print(
            "FETCH",
            name,
            "Y",
            year_of(html),
            "emp",
            emp.group(1) if emp else None,
            "filed",
            filed.group(1) if filed else None,
            (title.group(1)[:55] if title else ""),
            "blocks",
            parse_blocks(html)[:2],
        )
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])

for n, k in [
    ("wezembeek", "0433419259"),
    ("olv wezembeek", "0433419259"),
    ("sint_antonius", "0424236725"),
    ("sint-antonius", "0424236725"),
    ("ter_burg", "0479401318"),
]:
    hits = [
        e.get("entity_id")
        for e in ents
        if n.lower() in ((e.get("entity_id") or "") + (e.get("name") or "") + (e.get("notes") or "")).lower()
        or (k and k in ((e.get("notes") or "") + (e.get("entity_id") or "")))
    ]
    print("ENT", n, hits[:5])

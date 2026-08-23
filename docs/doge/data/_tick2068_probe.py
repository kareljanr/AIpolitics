# ephemeral probe tick2068 — claim + stalls + Compostela
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2068")
outdir.mkdir(parents=True, exist_ok=True)
UTC = "2026-08-24T22:05:00Z"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = [f.lstrip("\ufeff") for f in (list(rows[0].keys()) if rows else [])]
        for row in rows:
            for k in list(row):
                if k.startswith("\ufeff"):
                    row[k.lstrip("\ufeff")] = row.pop(k)
        return rows, fields


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2068")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))
if st == "open":
    r["status"] = "in_progress"
    r["updated_utc"] = UTC
    save("docs/doge/data/research_queue.csv", qrows, qfields)
    print("CLAIMED rq_2068")
else:
    print("ALREADY", st)


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
    ("compostela", "https://www.companyweb.be/en/0432401155/compostela"),
    ("always_home", "https://www.companyweb.be/en/0821289991/always-home"),
    ("vulpia", "https://www.companyweb.be/en/0521970559/vulpia-vlaanderen"),
]

for name, url in cands:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=35) as resp:
            html = resp.read().decode("utf-8", "replace")
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

with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    ents = list(csv.DictReader(f))
for n, k in [("compostela", "0432401155"), ("always_home", "0821289991"), ("vulpia", "0521970559"), ("leiehome", "0410556557")]:
    hits = [
        e.get("entity_id")
        for e in ents
        if n.lower() in ((e.get("entity_id") or "") + (e.get("name") or "") + (e.get("notes") or "")).lower()
        or k in ((e.get("notes") or "") + (e.get("entity_id") or ""))
    ]
    print("ENT", n, hits[:5])

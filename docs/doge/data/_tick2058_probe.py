# ephemeral probe tick2058 candidates
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()

with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if r.get("task_id") in ("rq_2058", "rq_2059"):
            print(r["task_id"], r["status"], (r.get("title") or "")[:100])
print("STATE", Path("docs/doge/data/loop_state.csv").read_text(encoding="utf-8").strip())

outdir = Path("docs/doge/data/raw/tick2058")
outdir.mkdir(parents=True, exist_ok=True)


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar"]:
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


# prefer: FARO/AIESH/REW; then unused WZC from folder + De Foyer / Werken Glorieux
cands = {
    "faro_en": "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_en": "https://www.companyweb.be/en/0201712587/aiesh",
    "rew_en": "https://www.companyweb.be/en/0207540958/rew",
    "de_foyer_en": "https://www.companyweb.be/en/0413796456/woon-en-zorgcentra-de-foyer",
    "werken_glorieux_en": "https://www.companyweb.be/en/0424380938/werken-glorieux",
}

# map existing local files
for p in sorted(outdir.glob("*.html")):
    html = p.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)", html)
    emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
    filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
    kbo = re.search(r"companyweb\.be/(?:en|nl|fr)/(\d+)/", html)
    print(
        "LOCAL",
        p.name,
        "Y",
        year_of(html),
        "kbo",
        kbo.group(1) if kbo else None,
        "title",
        (title.group(1)[:55] if title else None),
        "emp",
        emp.group(1) if emp else None,
        "filed",
        filed.group(1) if filed else None,
        "blocks",
        parse_blocks(html)[:2],
    )

for name, url in cands.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
        print(
            "FETCH",
            name,
            "Y",
            year_of(html),
            "emp",
            emp.group(1) if emp else None,
            "filed",
            filed.group(1) if filed else None,
            "blocks",
            parse_blocks(html)[:2],
        )
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])

# check if De Foyer already mined
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    ents = list(csv.DictReader(f))
for needle in ["de_foyer", "foyer", "werken_glorieux", "glorieux", "jacky_maes", "wijtshage", "bolster", "tpandje", "zonnestraal"]:
    hits = [
        e.get("entity_id")
        for e in ents
        if needle in ((e.get("entity_id") or "") + (e.get("name_nl") or "") + (e.get("notes") or "")).lower()
    ]
    print("ENT", needle, hits[:5])

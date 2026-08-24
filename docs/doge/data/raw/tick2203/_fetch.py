# tick2203 fetch — Ijsedal Maatwerkbedrijf YE2025 + claim rq_2203
from pathlib import Path
import csv
import re
import time
import urllib.request

RAW = Path("docs/doge/data/raw/tick2203")
csv.field_size_limit(10**7)

# Claim rq_2203
p = Path("docs/doge/data/research_queue.csv")
for attempt in range(5):
    try:
        with p.open(newline="", encoding="utf-8") as f:
            r = csv.DictReader(f)
            cols = r.fieldnames
            rows = list(r)
        for row in rows:
            if row["task_id"] == "rq_2203":
                print("rq_2203 before", row["status"], row["title"][:80])
                if row["status"] in ("open", "in_progress"):
                    row["status"] = "in_progress"
                    row["updated_utc"] = "2026-08-26T13:35:00Z"
                    row["entity_id"] = "vzw_ijsedal_maatwerk_overijse"
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print("claim ok")
        break
    except OSError as e:
        print("retry", e)
        time.sleep(1)

# Verify FREE
ent = Path("docs/doge/data/entities.csv").read_text(encoding="utf-8").lower()
for n in ["ijsedal", "0407.602.017", "0407602017", "vzw_ijsedal"]:
    print(n, "HIT" if n.lower() in ent else "FREE")

# kromme LB false-positive check
with Path("docs/doge/data/leaderboard.csv").open(encoding="utf-8") as f:
    for line in f:
        if "kromme" in line.lower() or "0454426489" in line or "0454.426" in line:
            print("LB kromme line:", line[:160])


def fetch(url, out):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0; research)",
            "Accept-Language": "en,nl;q=0.9,fr;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=45) as r:
        data = r.read()
    Path(out).write_bytes(data)
    print("OK", out, len(data))
    return data


urls = [
    ("ijsedal_en.html", "https://www.companyweb.be/en/0407602017/ijsedal-maatwerkbedrijf"),
    ("ijsedal_nl.html", "https://www.companyweb.be/nl/0407602017/ijsedal-maatwerkbedrijf"),
    ("ijsedal_fr.html", "https://www.companyweb.be/fr/0407602017/ijsedal-maatwerkbedrijf"),
    (
        "kbo.html",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=407602017",
    ),
    ("site.html", "https://www.ijsedal.be/"),
]

for name, url in urls:
    try:
        fetch(url, RAW / name)
    except Exception as e:
        print("FAIL", name, e)


def parse(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    print("====", path)
    m = re.search(r"filed on ([0-9-]+)|neergelegd op ([0-9-]+)|déposées le ([0-9-]+)", text, re.I)
    print("filed", m.groups() if m else None)
    parts = re.split(r'title="Section [^"]+"|title="Rubriek [^"]+"|title="Rubrique [^"]+"', text)
    for part in parts[1:14]:
        lab = re.search(r">\s*([A-Za-zÀ-ÿ /]+)<", part[:600])
        euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", part)
        plain = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", part)
        pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", part)
        if euros or (plain and lab):
            print(
                (lab.group(1).strip() if lab else "?")[:40],
                "e",
                euros[:4],
                "p",
                plain[:4],
                "pct",
                pct[:2],
            )


parse(RAW / "ijsedal_en.html")
parse(RAW / "ijsedal_nl.html")

# KBO extract
kbo = (RAW / "kbo.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Status van de entiteit.*?<[^>]+>([^<]+)",
    r"Rechtsvorm.*?<[^>]+>([^<]+)",
    r"Aantal vestigingseenheden.*?<[^>]+>([^<]+)",
    r"Maatschappelijke naam.*?<[^>]+>([^<]+)",
    r"Adres van de zetel.*?</div>(.*?)</td>",
    r"RSZ.*?</td>",
    r"Nace.*?</tr>",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        snip = re.sub(r"<[^>]+>", " ", m.group(0))
        snip = re.sub(r"\s+", " ", snip).strip()[:200]
        print("KBO", snip)

# site contact
if (RAW / "site.html").exists():
    site = (RAW / "site.html").read_text(encoding="utf-8", errors="replace")
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site)))
    print("emails", emails[:10])
    tels = re.findall(r"0\d[\d\s./-]{7,}", site)
    print("tels", tels[:5])

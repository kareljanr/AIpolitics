# ephemeral tick2000 — finish in_progress EVERY-10 + AZ Delta YE2025 probe
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
UTC = "2026-08-24T03:35:00Z"

p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
r = next(x for x in rows if x.get("task_id") == "rq_2000")
st = (r.get("status") or "").lower()
print("before", st, r.get("entity_id"), r.get("updated_utc"))
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + st)
r["status"] = "in_progress"
r["updated_utc"] = UTC
r["entity_id"] = "vzw_az_delta"
with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("claimed/kept rq_2000")

dst = Path("docs/doge/data/raw/tick2000")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) >= 2 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")
        elif len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    return float(s)


def summarize(name):
    path = dst / f"{name}.html"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:110] if title else None))
    print(" blocks", blocks[:3])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "déposés le"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 160]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2])
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print(" y0 winst,equity,bruto,omzet", y0)
        if len(blocks) > 1:
            y1 = tuple(parse_amount(x) for x in blocks[1])
            print(" y1", y1)
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                print(f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%" if pct is not None else f"  {n} {a} vs {b}")
    print()


urls = [
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("delta_en", "https://www.companyweb.be/en/0505931808/algemeen-ziekenhuis-delta"),
    ("delta_nl", "https://www.companyweb.be/nl/0505931808/algemeen-ziekenhuis-delta"),
    ("delta_fr", "https://www.companyweb.be/fr/0505931808/algemeen-ziekenhuis-delta"),
    ("delta_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0505931808"),
    ("delta_site", "https://www.azdelta.be/"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name in ["faro_en", "delta_en", "delta_nl", "delta_fr"]:
    summarize(name)

kbo = (dst / "delta_kbo.html").read_text(encoding="utf-8", errors="replace")
clean = re.sub(r"<[^>]+>", " ", kbo)
clean = re.sub(r"\s+", " ", clean)
for needle in ["Actief", "Rechtsvorm", "E-mail", "Webadres", "Aanbested", "Roeselare", "vestiging", "Delta"]:
    i = clean.lower().find(needle.lower())
    if i >= 0:
        print("KBO", needle, repr(clean[max(0, i - 40) : i + 120]))

site = (dst / "delta_site.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site)))
print("site emails", emails[:15])

# inventory counts for EVERY-10
def count_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def foi_counts():
    with open("docs/doge/data/foi_queue.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    ready = sum(1 for x in rows if (x.get("status") or "").lower() == "ready")
    answered = sum(1 for x in rows if (x.get("status") or "").lower() == "answered")
    partial = sum(1 for x in rows if (x.get("status") or "").lower() == "partial")
    return len(rows), ready, answered, partial


print(
    "counts",
    count_rows("docs/doge/data/budgets.csv"),
    count_rows("docs/doge/data/commitments.csv"),
    count_rows("docs/doge/data/leaderboard.csv"),
    count_rows("docs/doge/data/entities.csv"),
    count_rows("docs/doge/data/sources.csv"),
    foi_counts(),
)

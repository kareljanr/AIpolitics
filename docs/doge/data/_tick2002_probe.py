# ephemeral tick2002 — claim + AZ Klina / OLV Aalst / AZORG YE2025
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
UTC = "2026-08-24T04:20:00Z"

p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
r = next(x for x in rows if x.get("task_id") == "rq_2002")
st = (r.get("status") or "").lower()
print("before", st)
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + st)
r["status"] = "in_progress"
r["updated_utc"] = UTC
with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2002")

dst = Path("docs/doge/data/raw/tick2002")
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
    ("klina_en", "https://www.companyweb.be/en/0434302850/algemeen-ziekenhuis-klina"),
    ("klina_nl", "https://www.companyweb.be/nl/0434302850/algemeen-ziekenhuis-klina"),
    ("olv_en", "https://www.companyweb.be/en/0410424222/onze-lieve-vrouwziekenhuis"),
    ("olv_nl", "https://www.companyweb.be/nl/0410424222/onze-lieve-vrouwziekenhuis"),
    ("azorg_en", "https://www.companyweb.be/en/1005154085"),
    ("azorg_nl", "https://www.companyweb.be/nl/1005154085"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name in ["faro_en", "klina_en", "klina_nl", "olv_en", "olv_nl", "azorg_en", "azorg_nl"]:
    summarize(name)

with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    er = list(csv.DictReader(f))
for eid in ["vzw_az_klina", "vzw_olv_aalst", "vzw_azorg"]:
    print("exists", eid, any(x.get("entity_id") == eid for x in er))

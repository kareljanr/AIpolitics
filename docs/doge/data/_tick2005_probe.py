# ephemeral tick2005 — claim + FARO + Imelda/Monica recheck + new YE2025 hospitals
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
UTC = "2026-08-24T05:25:00Z"

p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
r = next(x for x in rows if x.get("task_id") == "rq_2005")
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
print("claimed rq_2005")

dst = Path("docs/doge/data/raw/tick2005")
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
    for lab in ["Last balance sheet year", "filed on", "neergelegd op"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 150]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2])
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0 winst,equity,bruto,omzet", y0)
            if len(blocks) > 1:
                y1 = tuple(parse_amount(x) for x in blocks[1])
                print(" y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%" if pct is not None else f"  {n} {a} vs {b}")
        except Exception as e:
            print(" parse err", e)
    print()


urls = [
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("imelda_en", "https://www.companyweb.be/en/0409835490/imelda"),
    ("monica_en", "https://www.companyweb.be/en/0459768815/monica"),
    ("herentals_en", "https://www.companyweb.be/en/0821734213/az-st-elisabeth-herentals-vzw"),
    ("mm_en", "https://www.companyweb.be/en/0405236067"),  # Maria Middelares guess
    ("alma_en", "https://www.companyweb.be/en/0476991178"),  # AZ Alma guess
    ("glorieux_en", "https://www.companyweb.be/en/0405218258"),
    ("damiaan_en", "https://www.companyweb.be/en/0411720245"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name in [
    "faro_en",
    "imelda_en",
    "monica_en",
    "herentals_en",
    "mm_en",
    "alma_en",
    "glorieux_en",
    "damiaan_en",
]:
    summarize(name)

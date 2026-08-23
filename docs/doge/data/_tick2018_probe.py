# ephemeral tick2018 — claim + prefer AGB/FARO/AIESH/REW else unused hospital
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
UTC = "2026-08-24T08:55:00Z"

p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
r = next(x for x in rows if x.get("task_id") == "rq_2018")
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
print("claimed rq_2018")

dst = Path("docs/doge/data/raw/tick2018")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, len(data), url)
    except Exception as e:
        print("FAIL", name, e, url)


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
    print("==", name, "==", (title.group(1)[:120] if title else None))
    for lab in [
        "Last balance sheet year",
        "filed on",
        "neergelegd op",
        "Laatste balansjaar",
        "Dernier exercice",
    ]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 160].replace("\n", " ")))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2], "n_blocks", len(blocks))
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0 winst/equity/bruto/omzet", y0)
            if len(blocks) > 1:
                y1 = tuple(parse_amount(x) for x in blocks[1])
                print(" y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(
                        f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%"
                        if pct is not None
                        else f"  {n} {a} vs {b}"
                    )
        except Exception as e:
            print(" parse err", e, blocks[0])


# KBOs filled after search; placeholders probed below
targets = [
    ("agb_bornem_en", "https://www.companyweb.be/en/0877556624"),
    ("faro_en", "https://www.companyweb.be/en/0893863017"),
    ("aiesh_en", "https://www.companyweb.be/en/0201712587"),
    ("rew_en", "https://www.companyweb.be/en/0644638937"),
    ("sfz_en", "https://www.companyweb.be/en/0469037857"),
    ("jessa_en", "https://www.companyweb.be/en/0821142117"),
    ("zol_en", "https://www.companyweb.be/en/0256543917"),
    ("noorderhart_en", "https://www.companyweb.be/en/0445662144"),
    ("noorderhart_nl", "https://www.companyweb.be/nl/0445662144"),
    # other unused FL hospitals
    ("az_st_jan_brugge_en", "https://www.companyweb.be/en/0405675785"),
    ("az_vesalius_en", "https://www.companyweb.be/en/0411797284"),
    ("az_groeninge_en", "https://www.companyweb.be/en/0465560280"),
    ("az_imelda_en", "https://www.companyweb.be/en/0411787091"),
    ("az_monica_en", "https://www.companyweb.be/en/0407044792"),
    ("az_maria_middelares_en", "https://www.companyweb.be/en/0407197779"),
]

for name, url in targets:
    fetch(name, url)
print("---SUMMARIES---")
for name, _ in targets:
    summarize(name)

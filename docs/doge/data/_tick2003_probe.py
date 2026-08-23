# ephemeral tick2003 — claim + prefer AGB/FARO/AIESH/REW + OLV Aalst vs Emmaüs
import csv
import re
import shutil
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
UTC = "2026-08-24T04:50:00Z"

p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
r = next(x for x in rows if x.get("task_id") == "rq_2003")
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
print("claimed rq_2003")

dst = Path("docs/doge/data/raw/tick2003")
dst.mkdir(parents=True, exist_ok=True)
# reuse emmaus raw if present from prior probe
for src_dir in [Path("docs/doge/data/raw/tick2002"), Path("docs/doge/data/raw/tick2002")]:
    if src_dir.exists():
        for name in [
            "emmaus_en.html",
            "emmaus_nl.html",
            "emmaus_fr.html",
            "emmaus_kbo.html",
            "faro_en.html",
            "aiesh_en.html",
            "rew_en.html",
            "agb_bornem_en.html",
            "sintmaarten_en.html",
        ]:
            s = src_dir / name
            if s.exists() and not (dst / name).exists():
                shutil.copy2(s, dst / name)
                print("copied", name)

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))
    return data.decode("utf-8", errors="replace")


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


def summarize(name, t=None):
    if t is None:
        path = dst / f"{name}.html"
        if not path.exists():
            print("missing", name)
            return
        t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:120] if title else None))
    print(" blocks", blocks[:2])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 140]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2])
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0", y0)
            if len(blocks) > 1:
                y1 = tuple(parse_amount(x) for x in blocks[1])
                print(" y1", y1)
                for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                    a, b = y0[i], y1[i]
                    pct = (a - b) / abs(b) * 100 if b else None
                    print(f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%" if pct is not None else f"  {n} {a} vs {b}")
        except Exception as e:
            print(" parse", e)
    print()


urls = [
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_en", "https://www.companyweb.be/en/0201712587"),
    ("rew_en", "https://www.companyweb.be/en/0644638937"),
    ("olv_en", "https://www.companyweb.be/en/0410424222"),
    ("olv_nl", "https://www.companyweb.be/nl/0410424222"),
    ("emmaus_en", "https://www.companyweb.be/en/0411515075"),
    ("emmaus_nl", "https://www.companyweb.be/nl/0411515075"),
    ("emmaus_fr", "https://www.companyweb.be/fr/0411515075"),
    ("emmaus_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411515075"),
    ("emmaus_site", "https://www.emmaus.be/"),
]

for name, url in urls:
    try:
        t = fetch(name, url)
        if name.endswith("_kbo"):
            clean = re.sub(r"<[^>]+>", " ", t)
            clean = re.sub(r"\s+", " ", clean)
            for needle in ["Actief", "Rechtsvorm", "E-mail", "Webadres", "Emma", "Aanbested", "vestiging"]:
                i = clean.lower().find(needle.lower())
                if i >= 0:
                    print("KBO", needle, repr(clean[max(0, i - 20) : i + 120]))
            print("emails", sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", clean)))[:8])
        elif name.endswith("_site"):
            print("site emails", sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)))[:12])
        else:
            summarize(name, t)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)

with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    er = list(csv.DictReader(f))
for eid in ["vzw_emmaus", "vzw_olv_aalst", "vzw_azorg"]:
    print("exists", eid, any(x.get("entity_id") == eid for x in er))

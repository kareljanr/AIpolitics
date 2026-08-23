# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2090")
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

path = Path("docs/doge/data/research_queue.csv")
with path.open(encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2090":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = "2026-08-25T03:35:00Z"
        row["notes"] = "CLAIM tick2090 EVERY-10 + probing AGB/FARO/AIESH/REW then unused WZC"
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2090")

blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(str(r).lower() for r in csv.DictReader(f))
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    blob += " ".join(
        ((r.get("entity_id") or "") + " " + (r.get("title") or "")).lower()
        for r in csv.DictReader(f)
    )


def mined(term: str) -> bool:
    return term.lower() in blob


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read(), resp.geturl()


# stall
for name, url in [
    ("faro_nl.html", "https://www.companyweb.be/nl/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_nl.html", "https://www.companyweb.be/nl/0201712587/aiesh"),
    ("rew_nl.html", "https://www.companyweb.be/nl/0644638937/rew"),
    ("bornem_jr.html", "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"),
]:
    try:
        data, final = fetch(url)
        (RAW / name).write_bytes(data)
        t = data.decode("utf-8", "replace")
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        years = re.findall(r"Jaarrekening\s+(20\d\d)", t)
        print(name, "YE", ye.group(1) if ye else years[:3])
    except Exception as e:
        print("FAIL", name, e)

# inventory for every-10
def count_rows(name):
    with open(f"docs/doge/data/{name}", encoding="utf-8-sig", newline="") as f:
        return sum(1 for _ in csv.reader(f)) - 1


print("budgets", count_rows("budgets.csv"))
print("commitments", count_rows("commitments.csv"))
print("leaderboard", count_rows("leaderboard.csv"))
print("entities", count_rows("entities.csv"))
print("sources", count_rows("sources.csv"))
foi_ready = foi_ans = foi_part = foi_tot = 0
with open("docs/doge/data/foi_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        foi_tot += 1
        st = (r.get("status") or "").lower()
        if st == "ready":
            foi_ready += 1
        elif st == "answered":
            foi_ans += 1
        elif st == "partial":
            foi_part += 1
print("foi", foi_ready, foi_ans, foi_part, foi_tot)

# candidates previously known unused / likely YE2025
CANDS = [
    ("0422620585", "woon-en-zorgcentrum-sint-vincentius", "vincentius erpe"),  # YE2024 before
    ("0441313178", "woon-en-zorgcentrum-avondvrede", "avondvrede"),  # YE2024
    ("0466266429", "helianthus", "helianthus"),
    ("0432505281", "rustoord-t-hoge", "t hoge"),
    # try disability / psych unused
    ("0473762450", "zusterhof", "zusterhof"),  # mined
    ("0410509443", "kanunnik", "kanunnik"),  # mined
]

for kbo, slug, term in CANDS:
    if mined(term) or mined(kbo):
        print("SKIP", term)
        continue
    try:
        data, final = fetch(f"https://www.companyweb.be/nl/{kbo}/{slug}")
        t = data.decode("utf-8", "replace")
        ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)\s*:", t)
        omzet = re.search(r"omzet:\s*\"([^\"]+)\"", t)
        title = re.search(r"<title>([^<]+)</title>", t)
        print(
            "PAGE",
            kbo,
            "YE",
            ye.group(1) if ye else "?",
            "omzet",
            omzet.group(1) if omzet else "?",
            (title.group(1)[:70] if title else "?"),
        )
        if ye and ye.group(1) == "2025":
            (RAW / f"cand_{kbo}_nl.html").write_bytes(data)
            print("  SAVED")
    except Exception as e:
        print("FAIL", kbo, type(e).__name__)

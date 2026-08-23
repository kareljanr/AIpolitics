# ephemeral probe tick2023
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10_000_000)

with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        eid = r.get("entity_id") or ""
        if "maria_rustoord" in eid or "0458458325" in str(r.values()):
            print("ENT", eid)
            for k, v in r.items():
                print(f"  {k}: {(v or '')[:220]}")

print("--- budgets ---")
with open("docs/doge/data/budgets.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        if "maria_rustoord" in (r.get("entity_id") or "") or "maria_rust" in (
            r.get("budget_id") or ""
        ):
            print(
                r.get("budget_id"),
                r.get("year"),
                r.get("amount_eur"),
                (r.get("notes") or "")[:100],
            )

print("--- leaderboard ---")
with open("docs/doge/data/leaderboard.csv", encoding="utf-8", newline="") as f:
    fields = None
    for r in csv.DictReader(f):
        if fields is None:
            fields = list(r.keys())
            print("lb fields", fields[:8])
        blob = " ".join(str(v) for v in r.values()).lower()
        if "maria" in blob and "rust" in blob:
            print({k: (r.get(k) or "")[:60] for k in fields[:6]})

print("--- foi ---")
with open("docs/doge/data/foi_queue.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        gid = (r.get("gap_id") or "").lower()
        if "maria" in gid or "ingelmunster" in gid:
            print(r.get("gap_id"), r.get("status"), (r.get("what_is_missing") or "")[:100])

# find AIESH / REW companyweb from prior notes
print("--- grep research notes ---")
with open("docs/doge/data/research_queue.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join(str(v) for v in r.values())
        if "AIESH" in blob or " REW" in blob or "aiesh" in blob.lower():
            if "YE2024" in blob or "YE2025" in blob or "KBO" in blob:
                print(
                    r.get("task_id"),
                    (r.get("notes") or r.get("instructions") or "")[:180],
                )

outdir = Path("docs/doge/data/raw/tick2023")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()

# refresh Maria site + dig email; try known AIESH/REW KBO from prior ticks
cands = [
    (
        "aiesh1",
        "https://www.companyweb.be/en/0200931609/association-intercommunale-de-lelectricite-du-sud-hainaut",
    ),
    ("aiesh2", "https://www.companyweb.be/en/0200931609/aiesh"),
    (
        "rew1",
        "https://www.companyweb.be/en/0200782469/intercommunale-pour-la-gestion-et-la-realisation-d-equipements-techniques-pour-l-energie-et-l-environnement",
    ),
    ("rew2", "https://www.companyweb.be/en/0222613656/rew-reseaux"),
    ("maria_site", "https://www.mariarustoord.be/"),
    (
        "maria_site2",
        "https://www.zorgnet-icuro.be/leden/maria-rustoord",
    ),
]


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                return m.group(1)
    return None


for name, url in cands:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        y = year_of(html)
        print(name, "ok", "year", y, "len", len(html), "url", url[-60:])
        emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html)))[:8]
        if emails:
            print("  emails", emails)
    except Exception as e:
        print(name, "ERR", type(e).__name__, e)

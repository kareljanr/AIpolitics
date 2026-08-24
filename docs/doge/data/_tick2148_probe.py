# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2148")
base.mkdir(parents=True, exist_ok=True)
ua = {"User-Agent": "Mozilla/5.0"}
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()

with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2148":
        print("2148", x.get("status"))

# preferred + candidate HVZ/WZC
cands = {
    "bornem_en.html": "https://www.companyweb.be/en/0877556624",
    "faro_en.html": "https://www.companyweb.be/en/0893863017",
    "aiesh_en.html": "https://www.companyweb.be/en/0201712587",
    "rew_en.html": "https://www.companyweb.be/en/0644638937",
    # Walloon HVZ candidates
    "hemeco_en.html": "https://www.companyweb.be/en/0500918000",  # guess - may fail
    # known WZC to try - Vallée / Hemeco / IILE
}
# Creditsafe-style known: try IILE Liege, Hemeco, Vesdre from prior knowledge
# Probe a few via KBO from Creditsafe patterns - fetch hemeco/iile via name search on kbo is hard
# Try direct known KBOs for unused walloon zones
for kbo, slug in [
    ("0500918512", "hemeco_try"),  # speculative
]:
    pass

for name, url in {
    "bornem_en.html": "https://www.companyweb.be/en/0877556624",
    "faro_en.html": "https://www.companyweb.be/en/0893863017",
    "aiesh_en.html": "https://www.companyweb.be/en/0201712587",
    "rew_en.html": "https://www.companyweb.be/en/0644638937",
}.items():
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read()
    (base / name).write_bytes(data)
    t = data.decode("utf-8", "replace")
    years = re.findall(r"\n(202[0-9])\s*:", t)
    title = re.search(r"<title>([^<]+)", t)
    print(name, "years", years[:5], (title.group(1)[:70] if title else None))
    for y in ["2025", "2024"]:
        mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
        if mm:
            print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:260])

# check mined walloon zones / try find unused MRS from leaderboard absence
for n in [
    "hemeco",
    "iile",
    "vesdre",
    "val de sambre",
    "luxembourg",
    "0500.918",
    "wzcsint",
    "huis vincent",
]:
    print("mined", n, n in ents)

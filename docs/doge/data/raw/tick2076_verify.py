from pathlib import Path
import re
t = Path(r"docs/doge/data/raw/tick2076/kuurne_fr.html").read_text(encoding="utf-8", errors="replace")
print("len", len(t))
print("omzet", re.findall(r'omzet:\s*"([^"]+)"', t)[:2])
print("winst", re.findall(r'winst:\s*"([^"]+)"', t)[:2])
m = re.search(r"window\.cw\.kernCijfers = \{(.{0,60})", t, re.S)
print("year head", m.group(1)[:40] if m else None)
# verify state
import csv
csv.field_size_limit(10**7)
with open(r"docs/doge/data/loop_state.csv", encoding="utf-8") as f:
    print(list(csv.DictReader(f))[0])
with open(r"docs/doge/data/research_queue.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["task_id"] in ("rq_2076","rq_2077") or r["status"]=="open":
            print(r["task_id"], r["status"], r["title"][:80])

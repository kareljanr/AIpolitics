import csv
from pathlib import Path

csv.field_size_limit(10**7)
p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rows = list(r)
print("cols", r.fieldnames)
print("total", len(rows))
ip = [x for x in rows if (x.get("status") or "").strip() == "in_progress"]
print("in_progress", len(ip))
for x in ip[:10]:
    t = (x.get("title") or x.get("topic") or "")[:80]
    print(x.get("id"), x.get("priority"), t)

open_rows = [x for x in rows if (x.get("status") or "").strip() == "open"]
print("open", len(open_rows))


def pri(x):
    try:
        return float(x.get("priority") or 0)
    except Exception:
        return 0


open_rows.sort(key=lambda x: (-pri(x), x.get("id") or ""))
print("--- top open ---")
for x in open_rows[:30]:
    t = (x.get("title") or x.get("topic") or x.get("notes") or "")[:100]
    print("%s|p=%s|%s" % (x.get("id"), x.get("priority"), t))

keys = ("AGB", "FARO", "AIESH", "REW", "WZC", "psych", "IGS", "dual", "hospita", "Bornem")
print("--- keyword open ---")
kw = []
for x in open_rows:
    blob = " ".join([(x.get(k) or "") for k in x.keys()]).upper()
    if any(k.upper() in blob for k in keys):
        kw.append(x)
kw.sort(key=lambda x: (-pri(x), x.get("id") or ""))
for x in kw[:50]:
    t = (x.get("title") or x.get("topic") or x.get("notes") or "")[:120]
    print("%s|p=%s|%s" % (x.get("id"), x.get("priority"), t))

print("--- rq_2030..2060 ---")
byid = {x.get("id"): x for x in rows}
for i in range(2030, 2061):
    rid = "rq_%d" % i
    x = byid.get(rid)
    if x:
        t = (x.get("title") or x.get("topic") or x.get("notes") or "")[:100]
        print("%s|%s|p=%s|%s" % (rid, x.get("status"), x.get("priority"), t))

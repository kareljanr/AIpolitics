import csv
csv.field_size_limit(10_000_000)
for fn in ["leaderboard.csv","foi_queue.csv","commitments.csv","budgets.csv","sources.csv","entities.csv"]:
    with open("docs/doge/data/"+fn, newline="", encoding="utf-8") as f:
        r=csv.reader(f)
        hdr=next(r)
        print("HDR", fn, len(hdr))
        print(hdr)
with open("docs/doge/data/leaderboard.csv", newline="", encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
print("LAST LB KEYS", list(rows[-1].keys()))
print("LAST LB", {k:(rows[-1].get(k) or "")[:120] for k in rows[-1]})
print("--- city_gent / elfen ---")
with open("docs/doge/data/entities.csv", newline="", encoding="utf-8") as f:
    r=csv.DictReader(f)
    for row in r:
        if row["entity_id"] in ("city_gent","vzw_elfenbankje","vzw_windekind") or "0431.806.386" in str(row):
            print(row["entity_id"], row["name_nl"][:80], "parent", row.get("parent_id"))
            print(" ", (row.get("notes") or "")[:200])
print("--- rq_2429 ---")
with open("docs/doge/data/research_queue.csv", newline="", encoding="utf-8") as f:
    r=csv.DictReader(f)
    for row in r:
        if row["task_id"]=="rq_2429":
            print({k:(row.get(k) or "")[:180] for k in row})
print("--- unused windekind ---")
needles=["0431.806.386","0431806386","Windekind","WINDEKIND"]
for fn in ["entities.csv","research_queue.csv","sources.csv"]:
    hits=0
    with open("docs/doge/data/"+fn, newline="", encoding="utf-8") as f:
        r=csv.DictReader(f)
        for row in r:
            blob=" ".join((row.get(c) or "") for c in r.fieldnames)
            if any(n.lower() in blob.lower() for n in needles):
                hits+=1
    print(fn, "hits", hits)

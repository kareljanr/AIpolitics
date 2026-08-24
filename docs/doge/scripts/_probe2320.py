import csv
csv.field_size_limit(10**7)
rows = list(csv.DictReader(open(r"docs/doge/data/research_queue.csv", newline="", encoding="utf-8")))
for r in rows:
    if r["task_id"] == "rq_2320":
        for k, v in r.items():
            print(f"{k}: {(v or '')[:220]}")
ents = list(csv.DictReader(open(r"docs/doge/data/entities.csv", newline="", encoding="utf-8")))
blob = "|".join(e.get("entity_id", "") + " " + (e.get("name_nl") or "") for e in ents).lower()
for name in ["bornem", "faro", "aiesh", "rew", "senes", "entre d", "citeco", "gandae", "homevil", "l_entre"]:
    print("in ents", name, name in blob)
print("ents n", len(ents), "last", ents[-1].get("entity_id"), ents[-1].get("name_nl"))

from pathlib import Path

src = Path("docs/doge/data/raw/tick2324/write_tick2324.py").read_text(encoding="utf-8")
t = src.replace("2324", "2325").replace("2026-08-28T00:05:00Z", "2026-08-28T00:15:00Z")
t = t.replace("after DominiekSavio@2323", "after Ritmica@2324")
t = t.replace("DominiekSavio@2323", "Ritmica@2324")
t = t.replace(
    'if not any(row["task_id"] == "rq_2325" for row in rows):',
    'if not any(row["task_id"] == "rq_2326" for row in rows):',
    1,
)
t = t.replace(
    '"task_id": "rq_2325",\n            "title": "leftover dual after Alma',
    '"task_id": "rq_2326",\n            "title": "leftover dual after Alma',
    1,
)
t = t.replace("next rq_2325; next EVERY-10 2330", "next rq_2326; next EVERY-10 2330")
t = t.replace(
    "Do NOT redo Alma/DominiekSavio/EntreDeux/Humival/Heder stack.",
    "Do NOT redo Alma/Ritmica/DominiekSavio/EntreDeux/Humival stack.",
)
Path("docs/doge/data/raw/tick2325").mkdir(parents=True, exist_ok=True)
Path("docs/doge/data/raw/tick2325/write_tick2325.py").write_text(t, encoding="utf-8")
print("ok")
for i, l in enumerate(t.splitlines(), 1):
    if "rq_232" in l and any(
        k in l for k in ("task_id", "last_unit", "already", "spawned", "next rq")
    ):
        print(f"{i}:{l[:110]}")

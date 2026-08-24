from pathlib import Path

p = Path("docs/doge/data/raw/tick2323/write_tick2323.py")
t = p.read_text(encoding="utf-8")
t = t.replace(
    'if row["task_id"] == "rq_2324" and row["status"] == "done":',
    'if row["task_id"] == "rq_2323" and row["status"] == "done":',
)
t = t.replace(
    'raise SystemExit("rq_2324 already done:',
    'raise SystemExit("rq_2323 already done:',
)
# only the update loop target, not spawn check
old = 'for row in rows:\n    if row["task_id"] == "rq_2324":\n        row.update('
new = 'for row in rows:\n    if row["task_id"] == "rq_2323":\n        row.update('
if old not in t:
    raise SystemExit("update loop pattern not found")
t = t.replace(old, new, 1)
t = t.replace('"last_unit_id": "rq_2324"', '"last_unit_id": "rq_2323"')
p.write_text(t, encoding="utf-8")
print("fixed")
for i, l in enumerate(t.splitlines(), 1):
    if "rq_2323" in l or "rq_2324" in l:
        if any(k in l for k in ("task_id", "last_unit", "already done", "spawned", "next rq")):
            print(f"{i}:{l[:110]}")

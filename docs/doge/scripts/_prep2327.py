import csv
from pathlib import Path

csv.field_size_limit(10**7)
p = Path("docs/doge/data/research_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields, rows = r.fieldnames, list(r)
for row in rows:
    if row["task_id"] == "rq_2327" and row["status"] == "open":
        row["status"] = "in_progress"
        row["entity_id"] = "vzw_mivalti_tielt"
        row["updated_utc"] = "2026-08-28T00:35:00Z"
        row["notes"] = (row.get("notes") or "") + "|CLAIM Mivalti Tielt YE2025"
        print("claimed", row["title"][:80])
        break
else:
    raise SystemExit("rq_2327 not open")
with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

src = Path("docs/doge/scripts/_tick2325_mivalti.py")
t = src.read_text(encoding="utf-8")
reps = [
    ("Tick 2325", "Tick 2327"),
    ('TICK = "2325"', 'TICK = "2327"'),
    ('RQ, NEXT_RQ = "rq_2325", "rq_2326"', 'RQ, NEXT_RQ = "rq_2327", "rq_2328"'),
    ('UTC = "2026-08-28T00:30:00Z"', 'UTC = "2026-08-28T00:40:00Z"'),
    ('"tick2325"', '"tick2327"'),
    ("src_mivalti_site_contact_2325", "src_mivalti_site_contact_2327"),
    ("if ticks >= 2325:", "if ticks >= 2327:"),
    ("after Ritmica@2324", "after Zonnebeke Sint-Jozef@2326"),
    ("Ritmica@2324", "Zonnebeke@2326"),
    (
        "Do not redo Ritmica/Dominiek Savio/Humival/Heder/Homevil stack.",
        "Do not redo Zonnebeke/Ithaka/Het Eepos/Ritmica/Dominiek Savio/Humival stack.",
    ),
    (
        "Do NOT redo Mivalti/Ritmica/Dominiek Savio/Humival/Heder/Homevil/Het Eepos stack.",
        "Do NOT redo Mivalti/Zonnebeke/Ithaka/Het Eepos/Ritmica/Dominiek Savio/Humival stack.",
    ),
]
for a, b in reps:
    t = t.replace(a, b)
Path("docs/doge/scripts/_tick2327_mivalti.py").write_text(t, encoding="utf-8")
print("script ready")

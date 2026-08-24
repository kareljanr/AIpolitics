from pathlib import Path

src = Path("docs/doge/data/raw/tick2324/write_tick2324.py").read_text(encoding="utf-8")
t = src
t = t.replace("# tick 2324:", "# tick 2325:")
t = t.replace("after Dominiek Savio@2323", "after Ritmica@2324")
t = t.replace("2026-08-24T13:30:00Z", "2026-08-24T13:35:00Z")
t = t.replace("src_apart_kbo_2324", "src_apart_kbo_2325")
t = t.replace("src_apart_site_contact_2324", "src_apart_site_contact_2325")
t = t.replace("tick2324", "tick2325")
# claim/close unit id
t = t.replace('row["task_id"] == "rq_2324"', 'row["task_id"] == "rq_2325"')
t = t.replace("rq_2324 already done", "rq_2325 already done")
t = t.replace("rq_2324 claimed by other", "rq_2325 claimed by other")
t = t.replace('"last_unit_id": "rq_2324"', '"last_unit_id": "rq_2325"')
t = t.replace('"ticks_completed": "2324"', '"ticks_completed": "2325"')
t = t.replace("next rq_2325;", "next rq_2326;")
t = t.replace('"unit": "rq_2324"', '"unit": "rq_2325"')
t = t.replace('"tick": "2324"', '"tick": "2325"')
# spawn next
t = t.replace("has_2325", "has_2326")
t = t.replace('row["task_id"] == "rq_2325"', 'row["task_id"] == "rq_2326"', 1)  # only spawn-check line after has_
# Fix: the replace above may have hit claim line too. Re-read approach.

# Safer: rewrite spawn block markers
t = src
t = t.replace("# tick 2324:", "# tick 2325:")
t = t.replace("after Dominiek Savio@2323", "after Ritmica@2324")
t = t.replace("After Dominiek Savio.", "After Ritmica.")
t = t.replace("Dominiek Savio/Merlijn/Humival/Heder", "Ritmica/Dominiek Savio/Merlijn/Humival/Heder")
t = t.replace("2026-08-24T13:30:00Z", "2026-08-24T13:35:00Z")
t = t.replace("src_apart_kbo_2324", "src_apart_kbo_2325")
t = t.replace("src_apart_site_contact_2324", "src_apart_site_contact_2325")
t = t.replace("tick2324", "tick2325")
t = t.replace("2324", "2325")  # broad but ok for tick numbers / rq after other replaces?
# Wait broad 2324->2325 turns spawn rq_2325 into rq_2326? No: 2324->2325 only.
# Spawn was rq_2325 -> becomes rq_2326 if we do 2325->2326 after.

t = src
replacements = [
    ("# tick 2324:", "# tick 2325:"),
    ("after Dominiek Savio@2323", "after Ritmica@2324"),
    ("After Dominiek Savio.", "After Ritmica."),
    ("Do NOT redo Dominiek Savio/Merlijn/Humival/Heder stack.", "Do NOT redo Ritmica/Dominiek Savio/Merlijn/Humival/Heder stack."),
    ("Do NOT redo aPart/Dominiek Savio/Merlijn/Humival/Heder/Kindervriend/Homevil stack.", "Do NOT redo aPart/Ritmica/Dominiek Savio/Merlijn/Humival/Heder/Kindervriend/Homevil stack."),
    ("2026-08-24T13:30:00Z", "2026-08-24T13:35:00Z"),
    ("src_apart_kbo_2324", "src_apart_kbo_2325"),
    ("src_apart_site_contact_2324", "src_apart_site_contact_2325"),
    ("tick2324", "tick2325"),
    ('== "rq_2324"', '== "rq_2325"'),
    ("rq_2324 already", "rq_2325 already"),
    ("rq_2324 claimed", "rq_2325 claimed"),
    ('"last_unit_id": "rq_2324"', '"last_unit_id": "rq_2325"'),
    ('"ticks_completed": "2324"', '"ticks_completed": "2325"'),
    ("next rq_2325;", "next rq_2326;"),
    ('"unit": "rq_2324"', '"unit": "rq_2325"'),
    ('"tick": "2324"', '"tick": "2325"'),
    ("has_2325", "has_2326"),
    ('task_id"] == "rq_2325"', 'task_id"] == "rq_2326"'),  # spawn has check — BUT also closes claim if already changed
    ('"task_id": "rq_2325"', '"task_id": "rq_2326"'),
    ("spawned after tick2325 aPart", "spawned after tick2325 aPart"),
    ("leftover dual after aPart", "leftover dual after aPart"),
]
t = src
for a, b in replacements:
    t = t.replace(a, b)

# Fix double-bump: claim line may have become rq_2326 from spawn replace.
# Ensure claim/close uses rq_2325 and spawn uses rq_2326.
t = t.replace('if row["task_id"] == "rq_2326":\n        if row["status"] == "done":\n            raise SystemExit("rq_2325 already done',
              'if row["task_id"] == "rq_2325":\n        if row["status"] == "done":\n            raise SystemExit("rq_2325 already done')
t = t.replace('if row["task_id"] == "rq_2326":\n        if row["status"] == "done":\n            raise SystemExit("rq_2326 already done',
              'if row["task_id"] == "rq_2325":\n        if row["status"] == "done":\n            raise SystemExit("rq_2325 already done')

# Fix close-unit loop that may have been bumped
t = t.replace(
    'if row["task_id"] == "rq_2326":\n        row["title"]',
    'if row["task_id"] == "rq_2325":\n        row["title"]',
)

out = Path("docs/doge/data/raw/tick2325/write_tick2325.py")
out.write_text(t, encoding="utf-8")
print("wrote", out)
for i, l in enumerate(t.splitlines(), 1):
    if "rq_232" in l and ("task_id" in l or "already" in l or "claimed" in l or "last_unit" in l or "spawned" in l or "next rq" in l):
        print(f"{i}:{l.strip()[:120]}")

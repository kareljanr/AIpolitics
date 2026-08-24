from pathlib import Path

src = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\_tick2215_write.py")
t = src.read_text(encoding="utf-8")
t = t.replace("src_constructief_kbo_2215", "src_constructief_kbo_2216")
t = t.replace("src_constructief_site_contact_2215", "src_constructief_site_contact_2216")
t = t.replace("tick2215", "tick2216")
t = t.replace("Tick 2215", "Tick 2216")
t = t.replace("2026-08-26T17:30:00Z", "2026-08-26T17:40:00Z")
t = t.replace("after OptimaT", "after Groep Maatwerk")
t = t.replace("Do not redo OptimaT", "Do not redo Groep Maatwerk/OptimaT")
t = t.replace("do not redo OptimaT", "do not redo Groep Maatwerk/OptimaT")
t = t.replace("rq_2216", "rq_2217")
t = t.replace("rq_2215", "rq_2216")
t = t.replace('row["ticks_completed"] = "2215"', 'row["ticks_completed"] = "2216"')
t = t.replace(
    "Do NOT redo Constructief, OptimaT",
    "Do NOT redo Constructief, Groep Maatwerk, OptimaT",
)
Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\_tick2216_write.py").write_text(
    t, encoding="utf-8"
)
print("rq_2216", t.count("rq_2216"), "rq_2217", t.count("rq_2217"))
print("ticks2216", 'ticks_completed"] = "2216"' in t)

from pathlib import Path

p = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\_tick2214_write.py")
t = p.read_text(encoding="utf-8")
t = t.replace('row["ticks_completed"] = "2213"', 'row["ticks_completed"] = "2214"')
t = t.replace("row['ticks_completed'] = '2213'", "row['ticks_completed'] = '2214'")
# ensure update targets rq_2214
if '"rq_2214":' not in t and "'rq_2214':" not in t:
    t = t.replace('"rq_2215": {', '"rq_2214": {', 1)
p.write_text(t, encoding="utf-8")
print("ticks2214", 'ticks_completed"] = "2214"' in t)
idx = t.find("update_csv_rows")
print(t[idx : idx + 600])
idx2 = t.find('task_id="rq_')
print("spawn lines:")
for line in t.splitlines():
    if "task_id=" in line or "last_unit_id" in line or "ticks_completed" in line:
        print(line.strip())

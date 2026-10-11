from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2543_stamp.txt").read_text().strip().splitlines()
path = DATA / "loop_state.csv"
raw = path.read_text(encoding="utf-8")
if not raw.endswith("\n"):
    raise SystemExit("state no LF")
rows = list(csv.DictReader(io.StringIO(raw)))
fields = list(csv.DictReader(io.StringIO(raw)).fieldnames)
assert len(rows) == 1
row = rows[0]
row["last_tick_utc"] = STAMP
row["last_unit_id"] = "rq_2543"
row["ticks_completed"] = "2543"
row["paused"] = "no"
row["mode"] = "continuous"
row["current_sprint"] = "hole_fill"
row["notes"] = (
    "tick2543 leftover dual Iona Nijlen 0410.269.814 leftover city_nijlen leftover VAPH Strong PDF deposit 2026-00186964 VKT-VZW 56658 B 15p bruto JUMP 5573753 9901 JUMP 219000 pnl JUMP 252169 cash JUMP 958823 official zetel Nieuwe Bevelsesteenweg 66 2560 Nijlen 1 VE leftover-mined AGB-only; after Bindkracht@2542; FIRST LOCK leftover city_nijlen leftover VAPH; next rq_2544 leftover dual (NOT every-10; next every-10 2550)"
)
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
w.writeheader(); w.writerow(row)
path.write_text(buf.getvalue(), encoding="utf-8")
print("state ok", STAMP, row["ticks_completed"])

from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2544_stamp.txt").read_text().strip().splitlines()
path = DATA / "loop_state.csv"
raw = path.read_text(encoding="utf-8")
if not raw.endswith("\n"):
    raise SystemExit("state no LF")
rows = list(csv.DictReader(io.StringIO(raw)))
fields = list(csv.DictReader(io.StringIO(raw)).fieldnames)
assert len(rows) == 1
row = rows[0]
row["last_tick_utc"] = STAMP
row["last_unit_id"] = "rq_2544"
row["ticks_completed"] = "2544"
row["paused"] = "no"
row["mode"] = "continuous"
row["current_sprint"] = "hole_fill"
row["notes"] = (
    "tick2544 leftover dual Ritmica Hove 0408.389.794 leftover city_hove leftover VAPH Strong PDF deposit 2026-00226136 VOL-VZW 1348852 B 41p 70/76A JUMP 5420432 73 JUMP 5215346 pnl LOSS narrower -53443 cash DROP 205034 official zetel Wouwstraat 44 2540 Hove 3 VE leftover-mined AGB-only; after Iona@2543; FIRST LOCK leftover city_hove leftover VAPH; next rq_2545 leftover dual (NOT every-10; next every-10 2550)"
)
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
w.writeheader(); w.writerow(row)
path.write_text(buf.getvalue(), encoding="utf-8")
print("state ok", STAMP, row["ticks_completed"])

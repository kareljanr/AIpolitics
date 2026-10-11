from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2541_stamp.txt").read_text().strip().splitlines()
path = DATA / "loop_state.csv"
raw = path.read_text(encoding="utf-8")
if not raw.endswith("\n"):
    raise SystemExit("state no LF")
rows = list(csv.DictReader(io.StringIO(raw)))
fields = list(csv.DictReader(io.StringIO(raw)).fieldnames)
assert len(rows) == 1
row = rows[0]
row["last_tick_utc"] = STAMP
row["last_unit_id"] = "rq_2541"
row["ticks_completed"] = "2541"
row["paused"] = "no"
row["mode"] = "continuous"
row["current_sprint"] = "hole_fill"
row["notes"] = (
    "tick2541 leftover dual De Plek Rotselaar 0822.360.357 leftover city_rotselaar leftover VAPH Strong PDF deposit 2026-00317818 MIC-VZW 34977 B 8p bruto DROP 8964 omzet DROP 17185 73 JUMP 2322 cash JUMP 12686 official zetel Hanewijk 44A 3118 Rotselaar 1 VE leftover-mined AGB-only unused leftover type; "
    "skipped Noorderhart Pelt SCAN Xerox AltaLink Toontjeshuis Schelle holding CV NACE 64.210 Megusta/Rommeshoef BV MIC-inb Ter Loke/Bindkracht/Den Ateljee YE2024-only Aalternatief 0 deposits Klaverhof Agten CommV farm; "
    "leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael@2535 leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; "
    "NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_rotselaar leftover VAPH; next rq_2542 leftover dual (NOT every-10; next every-10 2550)"
)
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
w.writeheader(); w.writerow(row)
path.write_text(buf.getvalue(), encoding="utf-8")
print("state ok", STAMP, row["ticks_completed"])

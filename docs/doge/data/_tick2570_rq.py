#!/usr/bin/env python3
"""tick2570 — surgical rq_2570 done + spawn rq_2571 + loop_state + loop_log (EVERY-10)."""
import csv, io, json, os, sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
os.chdir("/workspace/AIpolitics")
ids = json.loads(Path("/tmp/tick2570/IDS.json").read_text())
NOW, eid, gap_id = ids["NOW"], ids["eid"], ids["gap_id"]

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, "rb") as f:
    f.seek(0, 2); size = f.tell()
    f.seek(max(0, size - 200000)); tail = f.read()
assert tail.endswith(b"\n")
body = tail[:-1]
last_line = body[body.rfind(b"\n") + 1:]
start = size - 1 - len(last_line)
fields = ["task_id","title","sprint","priority","status","hierarchy_target","entity_id","instructions","blocked_gap_id","created_utc","updated_utc","notes"]
row = next(csv.DictReader(io.StringIO(",".join(fields) + "\n" + last_line.decode("utf-8"))))
if row["task_id"] != "rq_2570":
    raise SystemExit(f"last row is {row['task_id']} not rq_2570")
prev_instr = row["instructions"]
row.update({
    "status": "done", "entity_id": eid, "blocked_gap_id": gap_id, "updated_utc": NOW,
    "title": "leftover dual Het Balanske Tielt-Winge YE2025 PLUS every-10",
    "notes": "tick2570 DONE EVERY-10 leftover city_tielt_winge Het Balanske 0448.595.801 YE2025 VKT-VZW deposit 2026-00206974 73 JUMP 1608109 bruto 9900 1273778 62 1146505 9901 DROP 12273 debt JUMP 2308489 (+193%) overige leningen 1644111 aanbouw 1359758 cash 1282461 FTE 17,9 zetel Halensebaan 2 3390 Tielt-Winge 2 VE (Villa84 Diest); progress_every_10 + top10 refreshed (top10 stable)",
})
instr = prev_instr.replace("PLUS every-10 progress (ticks_completed 2570).", "").rstrip()
instr = instr.replace("HARD SKIP ", "HARD SKIP leftover city_tielt_winge leftover VAPH Het Balanske remine@2570 leftover Eyckenborgh Gooik WZC/Gravenkasteel not VAPH leftover Zwart Goor Merksplas Klavier=Emmaus leftover-via-VE ", 1)
instr += " RECHECK (pause 2026-08-29→2026-10-12): earlier 0-deposit / YE2024-only skips (VillaVip, Aalternatief, De Beukheuvel, OpWeg, Nethedal, Levenslust, De Ark Moerkerke, Woonondersteuning Vlaanderen, Mok, Wijzersterk) may now have YE2025 deposits via NBB published-deposits API. CDN staatsbladmonitor may hang: use official NBB broker PDF endpoint consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/{id}."
rq_2571 = {
    "task_id": "rq_2571", "title": "leftover dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "sprint": "hole_fill", "priority": "8", "status": "open", "hierarchy_target": "L5", "entity_id": "",
    "instructions": instr, "blocked_gap_id": "", "created_utc": NOW, "updated_utc": NOW,
    "notes": "spawned tick2570 after Het Balanske Tielt-Winge EVERY-10; leftover public dual unused leftover VAPH of leftover-mined Flanders city",
}
out = io.StringIO()
w = csv.DictWriter(out, fieldnames=fields, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
w.writerow(row); w.writerow(rq_2571)
with open(rq_path, "r+b") as f:
    f.seek(start); f.truncate(); f.write(out.getvalue().encode("utf-8"))
print("surgical rq: patched rq_2570 + spawned rq_2571 at", start)

ls_path = "docs/doge/data/loop_state.csv"
with open(ls_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f); ls_fields = r.fieldnames; ls_rows = list(r)
if ls_rows[0]["paused"].strip().lower() == "yes":
    raise SystemExit("PAUSED by human mid-tick — abort state write")
ls_rows[0].update({"last_tick_utc": NOW, "last_unit_id": "rq_2570", "ticks_completed": "2570", "paused": "no",
    "notes": "tick2570 EVERY-10 (first tick after resume 2026-10-12) leftover dual Het Balanske Tielt-Winge 0448.595.801 Strong PDF deposit 2026-00206974 VKT-VZW 51107 B 13p 73 JUMP 1608109 9901 DROP 12273 debt JUMP 2308489 overige leningen 1644111 aanbouw 1359758 Villa84 Diest; progress_every_10 + top10 refreshed (top10 stable); next rq_2571 leftover dual"})
with open(ls_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writeheader(); [w.writerow(x) for x in ls_rows]

log = f"""

## Tick 2570 — {NOW} — rq_2570 leftover dual Het Balanske Tielt-Winge YE2025 PLUS every-10

- Context: first tick after human resume (paused 2026-08-29 → resumed 2026-10-12 00:32 CEST).
- Hunt (time-boxed): Eyckenborgh Gooik 0434.019.372 REJECT (WZC; Eyckenborch assistentiewoningen run by Gravenkasteel 0874.863.091, not VAPH). Zwart Goor Merksplas REJECT (Klavier = Emmaüs 0411.515.075, zetel Mechelen → leftover-via-VE). Het Balanske Tielt-Winge 0448.595.801 unused (0 rows on KBO number) → LOCK.
- KBO: Actief since 05.11.1992; VZW; zetel Halensebaan 2 3390 Tielt-Winge; 2 VE (Tielt-Winge + Villa 84 Hasseltsestraat 84 Diest since 23.01.2026); RSZ2025 88.106 dagcentra volwassenen met mentale handicap.
- Found: official NBB VKT-VZW native PDF **2026-00206974** (51107 B / 13p; AV 15-06-2026; neergelegd 23/06/2026; MD5 c9a5f896cbd4f7cf6d2865fdc1073aa4; CDN staatsbladmonitor hung → official NBB broker PDF). 73 **EUR1608109** JUMP +11.41% (was 1443428); bruto 9900 **EUR1273778** JUMP +14.41%; 62 **EUR1146505** JUMP +18.10%; 630 **EUR110947** flat; 9901 **EUR12273** DROP −58.68% (was 29700); 9904 **EUR36784** DROP −41.11% (was 62462); equity **EUR2557203** flat; assets **EUR4865692** JUMP +45.92%; debt 17/49 **EUR2308489** JUMP +193.11% (was 787577; overige leningen 174/0 **EUR1644111** vs 190614; >5j 1507092); aanbouw 27 **EUR1359758** (was 123824); capex 8169 **EUR1241939**; cash **EUR1282461** JUMP +28.35%; kapitaalsubsidies 1018667; FTE 17,9 (was 15,7).
- Wrote: sources +3; budgets +11; commitments +1; leaderboard +1 pi 5.30; entities +1 (parent city_tielt_winge); FOI **{gap_id}** prio7 ready (NOT sent) + draft; raw PDF+txt+KBO docs/doge/raw/tick2570/; rq_2570=done; spawn **rq_2571**; ticks=2570.
- EVERY-10: progress_every_10_ticks.md → snapshot tick 2570 (A 100% / B 100% / C ~99% / D ~74-88% generous band unchanged / E 2254 FOI ready, 2306 rows). doge_waste_top10_current.md → as-of 2570, 8426 rows; pure top10 **stable** (new 2561-2570 rows pi 5.30-6.00 ≪ 8.4 cut-off). Top 3: GIP 2.5bn monitor fail (8.7) · federal fossil direct 13.3bn (8.55) · fossil accises 10.5bn (8.5).
- Data-quality note: foi_queue.csv has ~14 legacy rows with malformed status column (column shift); not touched this tick.
- Next: **rq_2571 leftover dual** (incl. recheck of earlier 0-deposit / YE2024-only skips for new YE2025 deposits).
"""
with open("docs/doge/loop_log.md", "a", encoding="utf-8") as f:
    f.write(log)
print("rq/state/log updated", NOW)

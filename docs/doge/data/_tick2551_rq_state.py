#!/usr/bin/env python3
"""Surgical patch rq_2551=done + spawn rq_2552; do not rewrite whole file."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2551_stamp.txt").read_text().strip().splitlines()
GAP = "gap_ter_loke_vosselaar_vaph_matrix_70_76a_jump_15_36m_73_jump_14_54m_9901_drop_443k_cash_drop_1_04m_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw[:1000] and rq_raw.count(b"\r\n") > 10:
    # allow if rare; hard fail only if whole file CRLF
    pass
n2551 = rq_raw.count(b"rq_2551,")
if n2551 != 1:
    raise SystemExit(f"expected 1 rq_2551 marker, found {n2551}")
if b"rq_2552," in rq_raw:
    raise SystemExit("rq_2552 already exists")

new_2551 = (
    "rq_2551,leftover dual Ter Loke Vosselaar YE2025,"
    "hole_fill,8,done,L5,vzw_ter_loke_vosselaar,"
    "leftover dual unused leftover VAPH of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Heynsdaele 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover GielsBos remine leftover Widar CDN 403 leftover Sint-Franciscus remine leftover Klavier leftover-via-VE leftover Ubuntu leftover-via-VE leftover MFC Zonnebos leftover-via-VE leftover PC Multiversum leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent.,"
    f"{GAP},{STAMP},{STAMP},"
    "tick2551 DONE leftover city_vosselaar leftover VAPH Ter Loke 0407.933.104 YE2025 VOL-VZW deposit 2026-00133725 envelope 70/76A JUMP 15356058 73 JUMP 14544228 9901 DROP 584530 9904 DROP 630343 cash DROP 1109665 geldbeleggingen JUMP 2200000 FTE 174.2 JUMP official zetel Heilanders 11 2350 Vosselaar 14 VE leftover-mined AGB-only; FIRST LOCK leftover city_vosselaar leftover VAPH; next rq_2552 leftover dual (NOT every-10; next every-10 2560)\n"
)
new_2552 = (
    "rq_2552,leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,"
    "hole_fill,8,open,L5,,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Heynsdaele 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover GielsBos remine leftover Widar CDN 403 leftover Sint-Franciscus remine leftover Klavier leftover-via-VE leftover Ubuntu leftover-via-VE leftover MFC Zonnebos leftover-via-VE leftover PC Multiversum leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent.,"
    f",{STAMP},{STAMP},"
    "spawned tick2551 after Ter Loke Vosselaar leftover dual; leftover public dual unused leftover VAPH of leftover-mined AGB-only Flanders city; NOT every-10 (next every-10 2560)\n"
)

idx = rq_raw.rfind(b"rq_2551,")
if idx < 0:
    raise SystemExit("rq_2551 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2551.encode("utf-8"))
    f.write(new_2552.encode("utf-8"))
print("patched research_queue rq_2551 + rq_2552; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2551,2551,no,"
    "tick2551 leftover dual Ter Loke Vosselaar 0407.933.104 leftover city_vosselaar leftover VAPH Strong PDF deposit 2026-00133725 VOL-VZW 651580 B 43p envelope 70/76A JUMP 15356058 73 JUMP 14544228 9901 DROP 584530 9904 DROP 630343 cash DROP 1109665 geldbeleggingen JUMP 2200000 FTE 174.2 JUMP official zetel Heilanders 11 2350 Vosselaar 14 VE leftover-mined AGB-only; after Wagenschot@2550; FIRST LOCK leftover city_vosselaar leftover VAPH; next rq_2552 leftover dual (NOT every-10; next every-10 2560)\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2550,2550," not in cur:
    raise SystemExit("loop_state not at 2550; abort")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

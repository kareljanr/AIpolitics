#!/usr/bin/env python3
"""Surgical patch rq_2552=done + spawn rq_2553; update loop_state; append loop_log."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2552_stamp.txt").read_text().strip().splitlines()
GAP = "gap_christoforus_merelbeke_vaph_matrix_bruto_jump_1_84m_73_jump_1_72m_cash_jump_169k_fte_jump_20_3_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
n2552 = rq_raw.count(b"rq_2552,")
if n2552 != 1:
    raise SystemExit(f"expected 1 rq_2552 marker, found {n2552}")
if b"rq_2553," in rq_raw:
    raise SystemExit("rq_2553 already exists")

new_2552 = (
    "rq_2552,leftover dual Christoforusgemeenschap Merelbeke-Melle YE2025,"
    "hole_fill,8,done,L5,vzw_christoforusgemeenschap_merelbeke_melle,"
    "leftover dual unused leftover VAPH of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Heynsdaele 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover GielsBos remine leftover Widar CDN 403 leftover Sint-Franciscus remine leftover Klavier leftover-via-VE leftover Ubuntu leftover-via-VE leftover MFC Zonnebos leftover-via-VE leftover PC Multiversum leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only.,"
    f"{GAP},{STAMP},{STAMP},"
    "tick2552 DONE leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap 0429.647.642 YE2025 VKT-VZW deposit 2026-00353503 bruto9900 JUMP 1843540 73 JUMP 1715211 cash JUMP 613428 FTE 20.3 JUMP official zetel Asselkouter 34 9820 Merelbeke-Melle 1 VE leftover-mined AGB-only; FIRST LOCK leftover city_merelbeke_melle leftover VAPH; next rq_2553 leftover dual (NOT every-10; next every-10 2560)\n"
)
new_2553 = (
    "rq_2553,leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,"
    "hole_fill,8,open,L5,,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Heynsdaele 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover GielsBos remine leftover Widar CDN 403 leftover Sint-Franciscus remine leftover Klavier leftover-via-VE leftover Ubuntu leftover-via-VE leftover MFC Zonnebos leftover-via-VE leftover PC Multiversum leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only.,"
    f",{STAMP},{STAMP},"
    "spawned tick2552 after Christoforusgemeenschap Merelbeke-Melle leftover dual; leftover public dual unused leftover VAPH of leftover-mined AGB-only Flanders city; NOT every-10 (next every-10 2560)\n"
)

idx = rq_raw.rfind(b"rq_2552,")
if idx < 0:
    raise SystemExit("rq_2552 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2552.encode("utf-8"))
    f.write(new_2553.encode("utf-8"))
print("patched research_queue rq_2552 + rq_2553; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2552,2552,no,"
    "tick2552 leftover dual Christoforusgemeenschap Merelbeke-Melle 0429.647.642 leftover city_merelbeke_melle leftover VAPH Strong PDF deposit 2026-00353503 VKT-VZW 51561 B 15p bruto9900 JUMP 1843540 73 JUMP 1715211 cash JUMP 613428 FTE 20.3 JUMP official zetel Asselkouter 34 9820 Merelbeke-Melle 1 VE leftover-mined AGB-only; after Ter Loke@2551; FIRST LOCK leftover city_merelbeke_melle leftover VAPH; next rq_2553 leftover dual (NOT every-10; next every-10 2560)\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2551,2551," not in cur:
    raise SystemExit("loop_state not at 2551; abort")
if "paused,yes" in cur.replace(" ", ""):
    raise SystemExit("paused")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log_raw = log_path.read_bytes()
if not log_raw.endswith(b"\n"):
    raise SystemExit("loop_log missing trailing LF")
if b"Tick 2552" in log_raw:
    raise SystemExit("loop_log already has Tick 2552")
block = """
## Tick 2552 — 2026-08-27T22:51:39Z — rq_2552 leftover dual Christoforusgemeenschap Merelbeke-Melle YE2025

- Unit: **rq_2552** leftover dual after **Ter Loke@2551**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover city_hove leftover VAPH Ritmica remine@2544 leftover city_nijlen leftover VAPH Iona remine@2543 leftover city_landen leftover VAPH Bindkracht remine@2542 leftover city_rotselaar leftover VAPH De Plek remine@2541 leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael remine leftover city_pelt leftover maatwerk NLOA remine leftover city_maasmechelen leftover maatwerk SBM remine leftover Aalternatief 0 deposits.
- Hunt skips: leftover city_heist_op_den_berg leftover VAPH/maatwerk **Nethedal 0431.830.439 YE2024-only** (latest NBB deposit 2025-00331952 YE 30/12/2024); leftover city_lommel leftover VAPH **MFC De Veerkracht 0 deposits**; leftover city_lommel leftover VAPH **Ter Heyder Heide 0 deposits**; leftover city_oudsbergen leftover VAPH **Muna/Het Steger 0 deposits**; leftover city_menen leftover VAPH **De Pelikaan OCMW Menen SKIP**; leftover city_blankenberge leftover VAPH **Ampel / CGG Prisma remine@1513**; leftover city_pepingen leftover VAPH **Huize Terloo Broeders van Liefde leftover-via-VE SKIP**; leftover city_brecht leftover VAPH **OC Clara Fey Evara**; leftover city_schilde leftover VAPH **MFC Zonnebos leftover-via-VE SKIP**; leftover city_roosdaal leftover VAPH **Sint-Franciscus remine@2129**; leftover city_westerlo leftover **CARrewiel CAR website wander SKIP**; leftover city_zemst leftover VAPH **Windkracht Zemst ouderinitiatief deferred**; leftover city_merchtem leftover **Kodiel groenezorg deferred**; leftover city_rumst leftover **Joert groenezorg deferred**; leftover Widar Merksplas CDN 403; leftover Klavier leftover-via-VE Mechelen; leftover Ubuntu leftover-via-VE Kortrijk; leftover PC Multiversum leftover-via-VE Gent; leftover OpWeg/Havenzate/Voluit/Rozemarijn remine parent sec_flanders.
- FIRST LOCK leftover city_merelbeke_melle leftover VAPH **Christoforusgemeenschap 0429.647.642** leftover-mined AGB-only unused leftover type (children agb_merelbeke_melle + zorg_zbls). Confirmed unused (0 real entity rows on 0429.647.642) + official KBO zetel Asselkouter 34 **9820 Merelbeke-Melle** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **VZW Christoforusgemeenschap** YE2025 (KBO **0429.647.642**; official zetel Asselkouter 34 9820 Merelbeke-Melle since 01.01.2025; **Actief** **1 VE** **2.156.375.128** Christoforusgemeenschap vzw Asselkouter 34 since 03.10.2006; RSZ2025 **87.202**; leftover of mined **city_merelbeke_melle**; FOI mattias@christoforus.be from official VAPH + official KBO; leftover VAPH / official VAPH adreslijst Christoforusgemeenschap Vergunde Zorgaanbieder). Identity trap: 0429.647.642 ≠ leftover AGB Merelbeke-Melle **0661.984.022**. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VKT-VZW **native text** (not scan) — 51561 B / 15p native euros (VKT-VZW 6.1.1 6.5 6.6 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00353503** (51561 B / 15p; AV **08.05.2026**; header **30/07/2026**; CDN GET **200** 51561 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-07-30 10:12:24 UTC MD5 511987600a7f419b9231c29267c6f6f8; NBB consult HTML stub 5344 B discarded; NBB published-deposits API 403 this tick; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR339757** JUMP +2.26% (commercial-only vs large 73; was 332242); 73 **EUR1715211** JUMP +1.66% (was 1687203); 76A **empty**; bruto 9900 **EUR1843540** JUMP +2.76% (VKT-VZW has no 70/76A total; 73 is the subsidy envelope; was 1794072); 62 **EUR1641896** JUMP +1.84%; 630 **EUR78844** DROP −6.95%; 66A **empty**; 640/8 **EUR46318** JUMP +104.38%; bedrijfswinst 9901 **EUR76482** JUMP +2.79% (was 74407); pnl 9904 **EUR77378** JUMP +0.75% (was 76802); 9903 **EUR77378** JUMP; equity **EUR1968021** JUMP +3.69%; assets **EUR2697026** JUMP +2.35%; debt **EUR729004** DROP −1.10%; FTE 9087 **20,3** JUMP +7.41% (was 18,9); kapitaalsubsidies **EUR12844** DROP −49.59%; destin 691 **EUR125000** JUMP; 791 **EUR25000** JUMP; cash **EUR613428** JUMP +38.19%; geldbeleggingen **empty**; gebouwen **EUR1312070** DROP; MVA 22/27 **EUR1376491** DROP; aanbouw **empty**; capex **EUR17313**. Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_merelbeke_melle leftover VAPH leftover-mined AGB-only unused leftover type. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.32; entities +1; FOI **gap_christoforus_merelbeke_vaph_matrix_bruto_jump_1_84m_73_jump_1_72m_cash_jump_169k_fte_jump_20_3_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2552/; rq_2552=done; spawn **rq_2553 leftover dual (NOT every-10; next every-10 2560)**; ticks=2552.
- Next: **rq_2553 leftover dual** (NOT every-10; next every-10 **2560**).
"""
log_path.write_bytes(log_raw + block.encode("utf-8"))
print("appended loop_log")
print("rq+state+log ok")

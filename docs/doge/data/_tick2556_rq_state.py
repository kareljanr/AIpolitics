#!/usr/bin/env python3
"""Surgical patch rq_2556=done + spawn rq_2557; update loop_state; append loop_log."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2556_stamp.txt").read_text().strip().splitlines()
GAP = "gap_monsheide_peer_vaph_matrix_70_76a_jump_6_36m_73_jump_5_28m_cash_jump_368k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
n2556 = rq_raw.count(b"rq_2556,")
if n2556 != 1:
    raise SystemExit(f"expected 1 rq_2556 marker, found {n2556}")
if b"rq_2557," in rq_raw:
    raise SystemExit("rq_2557 already exists")

new_2556 = (
    "rq_2556,leftover dual Monsheide Peer YE2025,"
    "hole_fill,8,done,L5,vzw_monsheide_peer,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only.,"
    f"{GAP},{STAMP},{STAMP},"
    "tick2556 DONE leftover city_peer leftover VAPH Monsheide 0419.081.867 YE2025 VOL-VZW deposit 2026-00180864 envelope JUMP 6359534 73 JUMP 5281699 cash JUMP 1222197 (+368k) FTE 66.8 JUMP official zetel Monsheide 4 3990 Peer 1 VE leftover-mined city GE tick1099; FIRST LOCK leftover city_peer leftover VAPH Monsheide; next rq_2557 leftover dual (NOT every-10; next every-10 2560)\n"
)
new_2557 = (
    "rq_2557,leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,"
    "hole_fill,8,open,L5,,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_peer leftover VAPH Monsheide remine@2556 leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only leftover BC Sint-Elisabeth Peer remine under sec_flanders leftover Buseloc Peer remine under sec_flanders leftover Rozemarijn Keerbergen remine@2295.,"
    f",{STAMP},{STAMP},"
    "spawned tick2556 after Monsheide Peer leftover dual; leftover public dual unused leftover VAPH of leftover-mined AGB-only Flanders city; NOT every-10 (next every-10 2560)\n"
)

idx = rq_raw.rfind(b"rq_2556,")
if idx < 0:
    raise SystemExit("rq_2556 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2556.encode("utf-8"))
    f.write(new_2557.encode("utf-8"))
print("patched research_queue rq_2556 + rq_2557; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2556,2556,no,"
    "tick2556 leftover dual Monsheide Peer 0419.081.867 leftover city_peer leftover VAPH Strong PDF deposit 2026-00180864 VOL-VZW 3133349 B 39p envelope JUMP 6359534 73 JUMP 5281699 cash JUMP 1222197 (+368k) FTE 66.8 JUMP official zetel Monsheide 4 3990 Peer 1 VE leftover-mined city GE tick1099; FIRST LOCK leftover city_peer leftover VAPH Monsheide; next rq_2557 leftover dual (NOT every-10; next every-10 2560)\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2555,2555," not in cur:
    raise SystemExit("loop_state not at 2555; abort")
if "paused,yes" in cur.replace(" ", ""):
    raise SystemExit("paused")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log_raw = log_path.read_bytes()
if not log_raw.endswith(b"\n"):
    raise SystemExit("loop_log missing trailing LF")
if b"Tick 2556" in log_raw:
    raise SystemExit("loop_log already has Tick 2556")
block = f"""
## Tick 2556 — {STAMP} — rq_2556 leftover dual Monsheide Peer YE2025

- Unit: **rq_2556** leftover dual after **VLOTTER@2555**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only.
- Hunt skips: leftover VAPH 0-deposit / no YE2025 NBB deps **Klavertje7 Rumst**, **Toontjeshuis Schelle**, **Think out-of-the-box Schilde**, **Mispelhoef Glabbeek**, **Witte Hoeve Assenede**, **Blend Zemst**; leftover city_boom leftover **Vlotter Maatwerk VZW YE2024-only**; leftover city_heist_op_den_berg leftover VAPH/maatwerk **Nethedal YE2024-only**; leftover city_lommel leftover VAPH **MFC De Veerkracht 0 deposits**; leftover city_lommel leftover VAPH **Ter Heyder Heide 0 deposits**; leftover city_oudsbergen leftover VAPH **Muna/Het Steger 0 deposits**; leftover **Forena Menen remine@2194** under sec_flanders; leftover **Rozemarijn Keerbergen remine@2295**; leftover **BC Sint-Elisabeth Peer remine@2304** under sec_flanders; leftover **Buseloc Peer remine@2290** under sec_flanders; leftover city_menen leftover VAPH **De Pelikaan OCMW SKIP**; leftover city_duffel leftover VAPH **ErgoEzel groenezorg SKIP**; leftover **Het Raster leftover-via-VE Vilvoorde SKIP**; leftover AGB-only VAPH hunt continued stalling on 0-deposit/YE2024/hard-skips — took NON-stall leftover mined **city_peer** leftover VAPH (city GE tick1099; no AGB child; Monsheide unused).
- FIRST LOCK leftover city_peer leftover VAPH **Monsheide 0419.081.867** leftover-mined city GE tick1099 unused leftover type (no agb_peer child; Monsheide itself unused; BC Sint-Elisabeth/Buseloc remine under sec_flanders). Confirmed unused (0 real entity rows on 0419.081.867) + official KBO zetel Monsheide 4 **3990 Peer** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **Monsheide** YE2025 (KBO **0419.081.867**; official zetel Monsheide 4 3990 Peer since 21.03.2001; **Actief** **1 VE** **2.154.985.949** Home Monsheide vzw; VZW; RSZ2025 **87.202**; leftover of mined **city_peer**; FOI onthaal@monsheide.be from official KBO + official VAPH adreslijst Vergunde Zorgaanbieder + RTH). Identity trap: 0419.081.867 ≠ leftover city GE Peer **0207.474.189** ≠ leftover OCMW Peer **0212.207.888** ≠ leftover Buseloc **0433.160.527** ≠ leftover BC Sint-Elisabeth Peer **0418.714.851**. Confirmed leftover public leftover dual not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-VZW **native text** (not scan) — 3133349 B / 39p native euros (VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.5 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.10 6.11 6.14 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00180864** (3133349 B / 39p; AV **18.06.2026**; header **22/06/2026**; CDN GET **200** 3133349 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-06-22 09:06:17 UTC MD5 a59e63763f14857612bd6ce1c0508d17; NBB consult HTML stub discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR810370** JUMP +2.33% (was 791927); 73 **EUR5281699** JUMP +10.00% (was 4801399; subsidies 733 **EUR5273599**; schenkingen 731 **EUR8100**); 76A **empty**; envelope 70/76A **EUR6359534** JUMP +8.93% (was 5838281); 74 **EUR267465** JUMP +9.19% (was 244955); 62 **EUR4786225** JUMP +9.71%; 630 **EUR312175** JUMP +0.62%; 640/8 **EUR40091** DROP; bedrijfswinst 9901 **EUR518731** JUMP +10.45% (was 469641); pnl 9904 **EUR603637** JUMP +6.21% (was 568352); 9903 **EUR603637**; equity **EUR6747285** JUMP +9.16%; assets **EUR8536334** JUMP +5.91%; debt **EUR1789049** DROP −4.78%; FTE 9087 **66,8** JUMP +7.22% (was 62,3; 9086 YE 101); kapitaalsubsidies **EUR147793** DROP −20.11%; destin 691 **EUR351637** JUMP; 791 **empty**; cash **EUR1222197** JUMP +43.08% (+368k vs 854185); geldbeleggingen **EUR4131000** JUMP +11.35%; gebouwen **EUR2193089** DROP; MVA 22/27 **EUR2899357** DROP; aanbouw **EUR122965** JUMP; capex **EUR139328**. Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_peer leftover VAPH unused leftover type after city GE tick1099. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.65; entities +1; FOI **{GAP}** prio7 ready + draft; raw PDF docs/doge/raw/tick2556/; rq_2556=done; spawn **rq_2557 leftover dual (NOT every-10; next every-10 2560)**; ticks=2556.
- Next: **rq_2557 leftover dual** (NOT every-10; next every-10 **2560**).
"""
log_path.write_bytes(log_raw + block.encode("utf-8"))
print("appended loop_log")
print("rq+state+log ok")

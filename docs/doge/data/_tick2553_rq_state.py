#!/usr/bin/env python3
"""Surgical patch rq_2553=done + spawn rq_2554; update loop_state; append loop_log."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2553_stamp.txt").read_text().strip().splitlines()
GAP = "gap_intesa_tongeren_vaph_matrix_envelope_jump_16_06m_73_jump_13_73m_cash_jump_549k_pnl_drop_62k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
n2553 = rq_raw.count(b"rq_2553,")
if n2553 != 1:
    raise SystemExit(f"expected 1 rq_2553 marker, found {n2553}")
if b"rq_2554," in rq_raw:
    raise SystemExit("rq_2554 already exists")

new_2553 = (
    "rq_2553,leftover dual Intesa Tongeren-Borgloon YE2025,"
    "hole_fill,8,done,L5,vzw_intesa_tongeren,"
    "leftover dual unused leftover VAPH of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Heynsdaele 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover GielsBos remine leftover Widar CDN 403 leftover Sint-Franciscus remine leftover Klavier leftover-via-VE leftover Ubuntu leftover-via-VE leftover MFC Zonnebos leftover-via-VE leftover PC Multiversum leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster Antwerpen zetel leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg.,"
    f"{GAP},{STAMP},{STAMP},"
    "tick2553 DONE leftover city_tongeren_borgloon leftover VAPH Intesa 0419.696.036 YE2025 VOL-VZW deposit 2026-00285863 envelope JUMP 16064584 73 JUMP 13728493 cash JUMP 1403971 pnl DROP 276541 FTE 162 JUMP official zetel Tongersesteenweg 74 3840 Tongeren-Borgloon 14 VE leftover-mined AGB-only after Nederheem remine@2549; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH Intesa; next rq_2554 leftover dual (NOT every-10; next every-10 2560)\n"
)
new_2554 = (
    "rq_2554,leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,"
    "hole_fill,8,open,L5,,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Heynsdaele 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover GielsBos remine leftover Widar CDN 403 leftover Sint-Franciscus remine leftover Klavier leftover-via-VE leftover Ubuntu leftover-via-VE leftover MFC Zonnebos leftover-via-VE leftover PC Multiversum leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster Antwerpen zetel leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg.,"
    f",{STAMP},{STAMP},"
    "spawned tick2553 after Intesa Tongeren-Borgloon leftover dual; leftover public dual unused leftover VAPH of leftover-mined AGB-only Flanders city; NOT every-10 (next every-10 2560)\n"
)

idx = rq_raw.rfind(b"rq_2553,")
if idx < 0:
    raise SystemExit("rq_2553 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2553.encode("utf-8"))
    f.write(new_2554.encode("utf-8"))
print("patched research_queue rq_2553 + rq_2554; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2553,2553,no,"
    "tick2553 leftover dual Intesa Tongeren-Borgloon 0419.696.036 leftover city_tongeren_borgloon leftover VAPH Strong PDF deposit 2026-00285863 VOL-VZW 2752547 B 49p envelope JUMP 16064584 73 JUMP 13728493 cash JUMP 1403971 pnl DROP 276541 FTE 162 JUMP official zetel Tongersesteenweg 74 3840 Tongeren-Borgloon 14 VE leftover-mined AGB-only after Nederheem remine@2549; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH Intesa; next rq_2554 leftover dual (NOT every-10; next every-10 2560)\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2552,2552," not in cur:
    raise SystemExit("loop_state not at 2552; abort")
if "paused,yes" in cur.replace(" ", ""):
    raise SystemExit("paused")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log_raw = log_path.read_bytes()
if not log_raw.endswith(b"\n"):
    raise SystemExit("loop_log missing trailing LF")
if b"Tick 2553" in log_raw:
    raise SystemExit("loop_log already has Tick 2553")
block = f"""
## Tick 2553 — {STAMP} — rq_2553 leftover dual Intesa Tongeren-Borgloon YE2025

- Unit: **rq_2553** leftover dual after **Christoforusgemeenschap@2552**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover city_hove leftover VAPH Ritmica remine@2544 leftover city_nijlen leftover VAPH Iona remine@2543 leftover city_landen leftover VAPH Bindkracht remine@2542 leftover city_rotselaar leftover VAPH De Plek remine@2541 leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael remine leftover city_pelt leftover maatwerk NLOA remine leftover city_maasmechelen leftover maatwerk SBM remine leftover Aalternatief 0 deposits.
- Hunt skips: leftover city_heist_op_den_berg leftover VAPH/maatwerk **Nethedal YE2024-only**; leftover city_lommel leftover VAPH **MFC De Veerkracht 0 deposits**; leftover city_lommel leftover VAPH **Ter Heyder Heide 0 deposits**; leftover city_oudsbergen leftover VAPH **Muna/Het Steger 0 deposits**; leftover city_menen leftover VAPH **De Pelikaan OCMW Menen SKIP**; leftover city_blankenberge leftover VAPH **Ampel / CGG Prisma remine**; leftover city_pepingen leftover VAPH **Huize Terloo leftover-via-VE SKIP**; leftover city_brecht leftover VAPH **OC Clara Fey Evara**; leftover city_schilde leftover VAPH **MFC Zonnebos leftover-via-VE SKIP**; leftover city_roosdaal leftover VAPH **Sint-Franciscus remine@2129**; leftover city_westerlo leftover **CARrewiel CAR website wander SKIP**; leftover city_zemst leftover VAPH **Windkracht deferred**; leftover city_merchtem leftover **Kodiel deferred**; leftover city_rumst leftover **Joert deferred**; leftover Widar Merksplas CDN 403; leftover Klavier leftover-via-VE Mechelen; leftover Ubuntu leftover-via-VE Kortrijk; leftover PC Multiversum leftover-via-VE Gent; leftover OpWeg/Havenzate/Voluit/Rozemarijn remine parent sec_flanders; leftover **Het Raster 0476.639.588 Antwerpen zetel leftover-via-VE Vilvoorde SKIP**; leftover city_duffel leftover VAPH **ErgoEzel groenezorg SKIP**; leftover city_overijse / city_leopoldsburg no AGB children SKIP; leftover city_kontich leftover VAPH Huize Iris remine under sec_flanders.
- FIRST LOCK leftover city_tongeren_borgloon leftover VAPH **Intesa 0419.696.036** leftover-mined AGB-only unused leftover type (children agb_tongeren_borgloon + vzw_kinderopvang_mereltjes + vzw_nederheem_tongeren; Intesa itself unused). Confirmed unused (0 real entity rows on 0419.696.036) + official KBO zetel Tongersesteenweg 74 **3840 Tongeren-Borgloon** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **VZW INTESA** YE2025 (KBO **0419.696.036**; official zetel Tongersesteenweg 74 3840 Tongeren-Borgloon since 01.01.2025; **Actief** **14 VE**; RSZ2025 **87.202**; leftover of mined **city_tongeren_borgloon**; FOI directie@intesa.be from official VAPH; leftover VAPH / official VAPH adreslijst Intesa RTH+Vergunde Zorgaanbieder). Identity trap: 0419.696.036 ≠ leftover AGB Tongeren-Borgloon **0820.533.292** ≠ leftover Nederheem **0476.473.403** remine@2549. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-VZW **native text** (not scan) — 2752547 B / 49p native euros (VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.6 6.4.1 6.5.2 6.5.3 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00285863** (2752547 B / 49p; AV **12.06.2026**; header **13/07/2026**; CDN GET **200** 2752547 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-07-13 22:20:30 UTC MD5 6627334f182741ae6c90a5a08efd14d1; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR1942845** JUMP +3.66% (commercial-only vs large 73; was 1874305); 73 **EUR13728493** JUMP +4.22% (was 13173198; 733 13715881 JUMP +4.24%; 73−733 gap 12612 FOI); 76A **EUR19874** JUMP (was 2526); envelope 70/76A **EUR16064584** JUMP +3.88% (VZW because 70 present and commercial-only vs large 73; was 15465302); 74 **EUR373372** DROP −10.09%; 62 **EUR12875390** JUMP +4.76%; 630 **EUR603813** JUMP +4.48%; 66A **EUR7238** DROP; 640/8 **EUR228083** DROP −6.30%; bedrijfswinst 9901 **EUR369462** DROP −13.19% (was 425578); pnl 9904 **EUR276541** DROP −18.26% (was 338306); 9903 **EUR276541** DROP; equity **EUR4914980** JUMP +3.74%; assets **EUR9948991** JUMP +2.33%; debt **EUR4513152** JUMP +0.89%; FTE 9087 **162** JUMP +1.82% (was 159.1; 9086 YE 213); kapitaalsubsidies **EUR1383066** DROP −6.70%; destin 691 **EUR1553199** JUMP; 791 **empty**; cash **EUR1403971** JUMP +64.13%; geldbeleggingen **empty**; gebouwen **EUR6735974** DROP; MVA 22/27 **EUR7456224** DROP; aanbouw **empty**; capex **EUR334892**. Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 14 VE leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.92; entities +1; FOI **{GAP}** prio7 ready + draft; raw PDF docs/doge/raw/tick2553/; rq_2553=done; spawn **rq_2554 leftover dual (NOT every-10; next every-10 2560)**; ticks=2553.
- Next: **rq_2554 leftover dual** (NOT every-10; next every-10 **2560**).
"""
log_path.write_bytes(log_raw + block.encode("utf-8"))
print("appended loop_log")
print("rq+state+log ok")

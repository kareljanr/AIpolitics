#!/usr/bin/env python3
"""Surgical patch rq_2555=done + spawn rq_2556; update loop_state; append loop_log."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2555_stamp.txt").read_text().strip().splitlines()
GAP = "gap_vlotter_boom_dv_matrix_70_76a_jump_7_50m_74_jump_4_95m_9901_jump_loss_narrow_298k_cash_jump_917k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
n2555 = rq_raw.count(b"rq_2555,")
if n2555 != 1:
    raise SystemExit(f"expected 1 rq_2555 marker, found {n2555}")
if b"rq_2556," in rq_raw:
    raise SystemExit("rq_2556 already exists")

new_2555 = (
    "rq_2555,leftover dual VLOTTER Boom YE2025,"
    "hole_fill,8,done,L5,dv_vlotter_boom,"
    "leftover dual unused leftover VAPH/maatwerk/WZC of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover GielsBos remine leftover Widar CDN 403 leftover Sint-Franciscus remine leftover Klavier leftover-via-VE leftover Ubuntu leftover-via-VE leftover MFC Zonnebos leftover-via-VE leftover PC Multiversum leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster Antwerpen zetel leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only.,"
    f"{GAP},{STAMP},{STAMP},"
    "tick2555 DONE leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER 0200.762.878 YE2025 VOL-inb deposit 2026-00303036 envelope JUMP 7498740 74 JUMP 4946203 9901 JUMP LOSS narrower -297897 cash JUMP 4373528 FTE 112.3 DROP official zetel Colonel Silvertopstraat 15 2850 Boom 2 VE leftover-mined AGB-only; FIRST LOCK leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER; next rq_2556 leftover dual (NOT every-10; next every-10 2560)\n"
)
new_2556 = (
    "rq_2556,leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,"
    "hole_fill,8,open,L5,,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only.,"
    f",{STAMP},{STAMP},"
    "spawned tick2555 after VLOTTER Boom leftover dual; leftover public dual unused leftover VAPH of leftover-mined AGB-only Flanders city; NOT every-10 (next every-10 2560)\n"
)

idx = rq_raw.rfind(b"rq_2555,")
if idx < 0:
    raise SystemExit("rq_2555 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2555.encode("utf-8"))
    f.write(new_2556.encode("utf-8"))
print("patched research_queue rq_2555 + rq_2556; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2555,2555,no,"
    "tick2555 leftover dual VLOTTER Boom 0200.762.878 leftover city_boom leftover maatwerk/thuiszorg dual Strong PDF deposit 2026-00303036 VOL-inb 476231 B 51p envelope JUMP 7498740 74 JUMP 4946203 9901 JUMP LOSS narrower -297897 cash JUMP 4373528 FTE 112.3 DROP official zetel Colonel Silvertopstraat 15 2850 Boom 2 VE leftover-mined AGB-only; FIRST LOCK leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER; next rq_2556 leftover dual (NOT every-10; next every-10 2560)\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2554,2554," not in cur:
    raise SystemExit("loop_state not at 2554; abort")
if "paused,yes" in cur.replace(" ", ""):
    raise SystemExit("paused")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log_raw = log_path.read_bytes()
if not log_raw.endswith(b"\n"):
    raise SystemExit("loop_log missing trailing LF")
if b"Tick 2555" in log_raw:
    raise SystemExit("loop_log already has Tick 2555")
block = f"""
## Tick 2555 — {STAMP} — rq_2555 leftover dual VLOTTER Boom YE2025

- Unit: **rq_2555** leftover dual after **Kadodder@2554**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover city_hove leftover VAPH Ritmica remine@2544 leftover city_nijlen leftover VAPH Iona remine@2543 leftover city_landen leftover VAPH Bindkracht remine@2542 leftover city_rotselaar leftover VAPH De Plek remine@2541 leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael remine leftover city_pelt leftover maatwerk NLOA remine leftover city_maasmechelen leftover maatwerk SBM remine leftover Aalternatief 0 deposits.
- Hunt skips: leftover VAPH 0-deposit / no YE2025 NBB deps **Klavertje7 Rumst**, **Toontjeshuis Schelle**, **Think out-of-the-box Schilde**, **Mispelhoef Glabbeek**, **Witte Hoeve Assenede**, **Blend Zemst**; leftover city_boom leftover **Vlotter Maatwerk VZW 0841.843.796 YE2024-only** (deposit 2025-00236826); leftover **Forena Menen remine@2194** under sec_flanders; leftover **Entiris Leuven zetel leftover-via-VE**; leftover city_heist_op_den_berg leftover VAPH/maatwerk **Nethedal YE2024-only**; leftover city_lommel leftover VAPH **MFC De Veerkracht 0 deposits**; leftover city_lommel leftover VAPH **Ter Heyder Heide 0 deposits**; leftover city_oudsbergen leftover VAPH **Muna/Het Steger 0 deposits**; leftover city_menen leftover VAPH **De Pelikaan OCMW Menen SKIP**; leftover city_blankenberge leftover VAPH **Ampel / CGG Prisma remine**; leftover city_pepingen leftover VAPH **Huize Terloo leftover-via-VE SKIP**; leftover city_brecht leftover VAPH **OC Clara Fey Evara**; leftover city_schilde leftover VAPH **MFC Zonnebos leftover-via-VE SKIP**; leftover city_roosdaal leftover VAPH **Sint-Franciscus remine@2129**; leftover city_westerlo leftover **CARrewiel CAR website wander SKIP**; leftover city_zemst leftover VAPH **Windkracht deferred**; leftover city_merchtem leftover **Kodiel deferred**; leftover city_rumst leftover **Joert deferred**; leftover Widar Merksplas CDN 403; leftover Klavier leftover-via-VE Mechelen; leftover Ubuntu leftover-via-VE Kortrijk; leftover PC Multiversum leftover-via-VE Gent; leftover OpWeg/Havenzate/Voluit/Rozemarijn remine parent sec_flanders; leftover **Het Raster Antwerpen zetel leftover-via-VE Vilvoorde SKIP**; leftover city_duffel leftover VAPH **ErgoEzel groenezorg SKIP**; leftover city_tessenderlo_ham leftover VAPH **Juffertje 0 YE2025 deps**; leftover city_essen leftover VAPH **Perron-Geluk 0 YE2025 deps**; leftover city_hamont_achel leftover **Flaming Star Ranch VOF commercial SKIP**; leftover city_zonnebeke leftover **Passchoeve BV Bisschophoeve SKIP**; leftover city_bredene leftover **VillaVip wrong city SKIP**; leftover city_zoersel leftover VAPH **Monnikenheide Emmaüs leftover-via-VE SKIP**; leftover city_tongeren_borgloon city VAPH type already two locks; leftover city_zoersel leftover VAPH Kadodder remine@2554 (do not remine).
- FIRST LOCK leftover city_boom leftover maatwerk/thuiszorg dual **VLOTTER 0200.762.878** leftover-mined AGB-only unused leftover type (children agb_boom_plus + wm_wkdr; VLOTTER itself unused). Confirmed unused (0 real entity rows on 0200.762.878) + official KBO zetel Colonel Silvertopstraat 15 **2850 Boom** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **VLOTTER** YE2025 (KBO **0200.762.878**; official zetel Colonel Silvertopstraat 15 2850 Boom since 20.04.2001; **Actief** **2 VE** **2.162.917.579** Vlotter + **2.171.339.159** Beschermde Werkplaats IMSIR; Dienstverlenende vereniging (Vlaams Gewest); RSZ2025 **88.993**+**88.101**; leftover of mined **city_boom**; FOI thuiszorg@vlotter.be from official Sociale Kaart; leftover maatwerk/thuiszorg dual after VAPH hunt stall). Identity trap: 0200.762.878 ≠ leftover AGB Boom Plus **0862.976.336** ≠ leftover WM Woonkade **0452.753.537** ≠ leftover Vlotter Maatwerk VZW **0841.843.796** YE2024-only. Confirmed leftover public leftover dual not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-inb **native text** (not scan) — 476231 B / 51p native euros (VOL-inb 6.1 6.2.1 6.2.2 6.2.4 6.2.5 6.3.4 6.3.5 6.3.6 6.4.1 6.5.2 6.7.2 6.15 6.17 6.18.1 6.18.2 6.20 9 11 12 13 14 15 niet dienstig).
- Found: official NBB VOL-inb native PDF deposit **2026-00303036** (476231 B / 51p; AV **24.06.2026**; header **15/07/2026**; CDN GET **200** 476231 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-07-17 08:06:31 UTC MD5 5415025ef790a927f4f01f04d84dafe5; NBB consult HTML stub 5344 B discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR2365768** DROP −6.89% (was 2540869); 73 **empty**; 76A **EUR186769** JUMP (was 22); envelope 70/76A **EUR7498740** JUMP +5.61% (was 7100145); 74 **EUR4946203** JUMP +8.49% (was 4559254; exploitatiesubsidies 740 **EUR4663519** FOI); 62 **EUR6163331** DROP −2.88%; 630 **EUR173026** JUMP +2.94%; 66A **EUR11399** JUMP from empty; 640/8 **EUR573106** JUMP; bedrijfswinst 9901 **EUR−297897** JUMP LOSS narrower (was −784330); pnl 9904 **EUR−277551** JUMP LOSS narrower (was −753303); 9903 **EUR−277551**; equity **EUR2208777** DROP −11.65%; assets **EUR8342340** JUMP +2.73%; debt **EUR4361960** JUMP +12.64%; FTE 9087 **112,3** DROP −3.61% (was 116,5; 9086 YE 165); kapitaalsubsidies **EUR201075** DROP −6.33%; destin 691/791 **empty**; cash **EUR4373528** JUMP +26.54%; geldbeleggingen **empty**; gebouwen **EUR2117863** DROP; MVA 22/27 **EUR2227394** DROP; aanbouw **empty**; capex **EUR57207**. Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 2 VE leftover mined city_boom leftover maatwerk/thuiszorg dual leftover-mined AGB-only unused leftover type. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.72; entities +1; FOI **{GAP}** prio7 ready + draft; raw PDF docs/doge/raw/tick2555/; rq_2555=done; spawn **rq_2556 leftover dual (NOT every-10; next every-10 2560)**; ticks=2555.
- Next: **rq_2556 leftover dual** (NOT every-10; next every-10 **2560**).
"""
log_path.write_bytes(log_raw + block.encode("utf-8"))
print("appended loop_log")
print("rq+state+log ok")

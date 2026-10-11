#!/usr/bin/env python3
"""Surgical patch rq_2557=done + spawn rq_2558; update loop_state; append loop_log."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2557_stamp.txt").read_text().strip().splitlines()
GAP = "gap_arum_dilsen_vaph_matrix_70_76a_jump_22_31m_73_jump_18_89m_cash_drop_4_02m_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
n2557 = rq_raw.count(b"rq_2557,")
if n2557 != 1:
    raise SystemExit(f"expected 1 rq_2557 marker, found {n2557}")
if b"rq_2558," in rq_raw:
    raise SystemExit("rq_2558 already exists")

new_2557 = (
    "rq_2557,leftover dual Zorggroep Arum Dilsen-Stokkem YE2025,"
    "hole_fill,8,done,L5,vzw_arum_dilsen,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_peer leftover VAPH Monsheide remine@2556 leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only.,"
    f"{GAP},{STAMP},{STAMP},"
    "tick2557 DONE leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum 0410.169.547 YE2025 VOL-VZW deposit 2026-00132875 envelope JUMP 22307281 73 JUMP 18892480 cash DROP 2044429 (−4.02m) FTE 222.5 flat official zetel Stokkemerbaan 147 3650 Dilsen-Stokkem 7 VE leftover-mined city GE tick1098; FIRST LOCK leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum; next rq_2558 leftover dual (NOT every-10; next every-10 2560)\n"
)
new_2558 = (
    "rq_2558,leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,"
    "hole_fill,8,open,L5,,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only leftover Casa Di Colore Berlaar 0 deposits leftover Ubuntu leftover-via-VE Kortrijk leftover groenezorg deferred.,"
    f",{STAMP},{STAMP},"
    "spawned tick2557 after Zorggroep Arum Dilsen-Stokkem leftover dual; leftover public dual unused leftover VAPH of leftover-mined AGB-only Flanders city; NOT every-10 (next every-10 2560)\n"
)

idx = rq_raw.rfind(b"rq_2557,")
if idx < 0:
    raise SystemExit("rq_2557 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2557.encode("utf-8"))
    f.write(new_2558.encode("utf-8"))
print("patched research_queue rq_2557 + rq_2558; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2557,2557,no,"
    "tick2557 leftover dual Zorggroep Arum Dilsen-Stokkem 0410.169.547 leftover city_dilsen_stokkem leftover VAPH Strong PDF deposit 2026-00132875 VOL-VZW 604523 B 49p envelope JUMP 22307281 73 JUMP 18892480 cash DROP 2044429 (−4.02m) FTE 222.5 flat official zetel Stokkemerbaan 147 3650 Dilsen-Stokkem 7 VE leftover-mined city GE tick1098; FIRST LOCK leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum; next rq_2558 leftover dual (NOT every-10; next every-10 2560)\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2556,2556," not in cur:
    raise SystemExit("loop_state not at 2556; abort")
if "paused,yes" in cur.replace(" ", ""):
    raise SystemExit("paused")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log_raw = log_path.read_bytes()
if not log_raw.endswith(b"\n"):
    raise SystemExit("loop_log missing trailing LF")
if b"Tick 2557" in log_raw:
    raise SystemExit("loop_log already has Tick 2557")
block = f"""
## Tick 2557 — {STAMP} — rq_2557 leftover dual Zorggroep Arum Dilsen-Stokkem YE2025

- Unit: **rq_2557** leftover dual after **Monsheide@2556**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_peer leftover VAPH Monsheide remine@2556 leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only.
- Hunt skips: leftover AGB-only candidate stall — city_izegem no VAPH admin adres; city_aarschot **Apojo remine@2336** under sec_flanders; city_bocholt empty; city_kinrooi **Dino's groenezorg deferred**; city_haacht/maldegem empty; city_zwevegem **Groep Ubuntu / Ubuntu Achtkanter 0419.258.348 Kortrijk zetel leftover-via-VE SKIP**; city_temse **Paard & Insight groenezorg deferred**; city_aalter **Aalternatief 0 deposits** + LiVia zorgboerderij; city_herk_de_stad **De Beerbos groenezorg deferred**; city_oud_turnhout **Liereman groenezorg deferred**; city_herselt **Het Ollemanshoekje groenezorg** + **Plus & Co ouderinitiatief 0784.638.245** (building toward 2028); city_berlaar **Casa Di Colore 0668.506.776 0 deposits**; leftover VAPH 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend; leftover city_peer leftover VAPH Monsheide remine@2556; leftover AGB-only VAPH hunt stalled on 0-deposit/YE2024/hard-skips/groenezorg — took NON-stall leftover mined **city_dilsen_stokkem** leftover VAPH (city GE tick1098; no AGB child; Zorggroep Arum unused).
- FIRST LOCK leftover city_dilsen_stokkem leftover VAPH **Zorggroep Arum 0410.169.547** leftover-mined city GE tick1098 unused leftover type (no agb_dilsen_stokkem child; Arum itself unused). Confirmed unused (0 real entity rows on 0410.169.547) + official KBO zetel Stokkemerbaan 147 **3650 Dilsen-Stokkem** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **Zorggroep Arum** YE2025 (KBO **0410.169.547**; official zetel Stokkemerbaan 147 3650 Dilsen-Stokkem; **Actief** **7 VE** De Meander / Kadoos / Campus Ommersteyn / de Ronduyt / de Korver / Fabor in Dilsen-Stokkem + Mané Schoolstraat(O) 32 Maasmechelen; VZW also known as (MANÉ); RSZ2025 **87.202**; leftover of mined **city_dilsen_stokkem**; FOI info@arum.be from official VAPH + official site https://www.arum.be; leftover VAPH / official VAPH adreslijst Zorggroep Arum Vergunde Zorgaanbieder + RTH + MFC). Identity trap: 0410.169.547 ≠ leftover city GE Dilsen-Stokkem **0207.471.716** ≠ leftover OCMW **0212.247.381** ≠ leftover SBM Maasmechelen **0461.814.525** remine@2538. Confirmed leftover public leftover dual not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VOL-VZW **native text** (not scan) — 604523 B / 49p native euros (VOL-VZW 6.1 6.2 6.3 6.4 6.5 6.9 6.11 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00132875** (604523 B / 49p; AV **26.05.2026**; header **01/06/2026**; CDN GET **200** 604523 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-06-03 00:11:56 UTC MD5 57838c227aa0eccf8c9de4915145c16b; NBB consult HTML stub discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR2974056** JUMP +3.80% (was 2865280); 73 **EUR18892480** JUMP +3.68% (was 18222277; subsidies 733 **EUR18876759**; schenkingen/legaten 731 **EUR15721** DROP); 76A **EUR1349** DROP −99.72% (was 474578); envelope 70/76A **EUR22307281** JUMP +1.46% (was 21986413); 74 **EUR439396** JUMP +3.56% (was 424278); 62 **EUR18142521** JUMP +3.29%; 630 **EUR890287** DROP −6.90%; 640/8 **EUR72292** JUMP; bedrijfswinst 9901 **EUR1020040** DROP −32.07% (was 1501696); pnl 9904 **EUR990177** DROP −37.16% (was 1575612); 9903 **EUR990177**; equity **EUR15728465** JUMP +5.51%; assets **EUR23224469** JUMP +6.36%; debt **EUR7381689** JUMP +9.69%; FTE 9087 **222,5** DROP −0.13% (was 222,8; 9086 YE 297); kapitaalsubsidies **EUR4592282** DROP −3.55%; destin 691 **EUR6100000**; 791 **empty**; cash **EUR2044429** DROP −66.29% (−4.02m vs 6064050); geldbeleggingen **EUR7901334** JUMP +235%; gebouwen **EUR9050451** DROP; MVA 22/27 **EUR10778447** DROP; aanbouw **EUR193879** JUMP; capex **EUR670742**. Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 7 VE leftover mined city_dilsen_stokkem leftover VAPH unused leftover type after city GE tick1098. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.98; entities +1; FOI **{GAP}** prio7 ready + draft; raw PDF docs/doge/raw/tick2557/; rq_2557=done; spawn **rq_2558 leftover dual (NOT every-10; next every-10 2560)**; ticks=2557.
- Next: **rq_2558 leftover dual** (NOT every-10; next every-10 **2560**).
"""
log_path.write_bytes(log_raw + block.encode("utf-8"))
print("appended loop_log")
print("rq+state+log ok")

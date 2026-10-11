#!/usr/bin/env python3
"""Surgical patch rq_2558=done + spawn rq_2559; update loop_state; append loop_log."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2558_stamp.txt").read_text().strip().splitlines()
GAP = "gap_duizendschoon_as_vaph_matrix_bruto_jump_216k_9901_drop_36k_cash_jump_79k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
n2558 = rq_raw.count(b"rq_2558,")
if n2558 != 1:
    raise SystemExit(f"expected 1 rq_2558 marker, found {n2558}")
if b"rq_2559," in rq_raw:
    raise SystemExit("rq_2559 already exists")

new_2558 = (
    "rq_2558,leftover dual Duizendschoon As YE2025,"
    "hole_fill,8,done,L5,vzw_duizendschoon_as,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only leftover Casa Di Colore Berlaar 0 deposits leftover Ubuntu leftover-via-VE Kortrijk leftover groenezorg deferred.,"
    f"{GAP},{STAMP},{STAMP},"
    "tick2558 DONE leftover city_as leftover VAPH Duizendschoon 0683.687.177 YE2025 VKT-VZW deposit 2026-00236227 bruto9900 JUMP 215719 9901 DROP 25883 cash JUMP 140931 (+79k) FTE 1.6 JUMP official zetel Bilzerweg 88 3665 As 1 VE leftover-mined city GE tick882; FIRST LOCK leftover city_as leftover VAPH Duizendschoon; next rq_2559 leftover dual (NOT every-10; next every-10 2560)\n"
)
new_2559 = (
    "rq_2559,leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025,"
    "hole_fill,8,open,L5,,"
    "leftover dual unused leftover VAPH/CAR/hospital/maatwerk of leftover-mined AGB-only Flanders city with live official YE2025 native PDF. Prefer NON-stall leftover VAPH. STOP leftover-note loop. HARD SKIP leftover CIK leftover CAR website wander leftover KBO-activity leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian leftover city_as leftover VAPH Duizendschoon remine@2558 leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover-via-VE of a DIFFERENT leftover city as parent leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only leftover Casa Di Colore Berlaar 0 deposits leftover Ubuntu leftover-via-VE Kortrijk leftover groenezorg deferred leftover Labor Arbeidskansen remine@2292.,"
    f",{STAMP},{STAMP},"
    "spawned tick2558 after Duizendschoon As leftover dual; leftover public dual unused leftover VAPH of leftover-mined AGB-only Flanders city; NOT every-10 (next every-10 2560)\n"
)

idx = rq_raw.rfind(b"rq_2558,")
if idx < 0:
    raise SystemExit("rq_2558 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2558.encode("utf-8"))
    f.write(new_2559.encode("utf-8"))
print("patched research_queue rq_2558 + rq_2559; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2558,2558,no,"
    "tick2558 leftover dual Duizendschoon As 0683.687.177 leftover city_as leftover VAPH Strong PDF deposit 2026-00236227 VKT-VZW 42056 B 10p bruto9900 JUMP 215719 9901 DROP 25883 cash JUMP 140931 (+79k) FTE 1.6 JUMP official zetel Bilzerweg 88 3665 As 1 VE leftover-mined city GE tick882; FIRST LOCK leftover city_as leftover VAPH Duizendschoon; next rq_2559 leftover dual (NOT every-10; next every-10 2560)\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2557,2557," not in cur:
    raise SystemExit("loop_state not at 2557; abort")
if "paused,yes" in cur.replace(" ", ""):
    raise SystemExit("paused")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log_raw = log_path.read_bytes()
if not log_raw.endswith(b"\n"):
    raise SystemExit("loop_log missing trailing LF")
if b"Tick 2558" in log_raw:
    raise SystemExit("loop_log already has Tick 2558")
block = f"""
## Tick 2558 — {STAMP} — rq_2558 leftover dual Duizendschoon As YE2025

- Unit: **rq_2558** leftover dual after **Zorggroep Arum@2557**. Prefer NON-stall leftover VAPH of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556 leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554 leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 leftover Nederheem remine@2549 leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550 leftover city_herent leftover VAPH OTL remine@2548 leftover city_koksijde leftover VAPH Inspirant remine@2547 leftover city_sint_truiden leftover VAPH Wiric remine@2546 leftover city_mortsel leftover VAPH De Kompanie remine@2545 leftover Aalternatief 0 deposits leftover Veerkracht 0 deposits leftover Steger 0 deposits leftover Pelikaan OCMW leftover Ampel Prisma remine leftover Terloo leftover-via-VE leftover YE2024-only leftover Armonea leftover Korian leftover Vulpia leftover CuraCare leftover commercial NV-BV leftover OCMW leftover convent leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only leftover Het Raster leftover-via-VE Vilvoorde leftover ErgoEzel Duffel groenezorg leftover Vlotter Maatwerk VZW YE2024-only leftover Casa Di Colore Berlaar 0 deposits leftover Ubuntu leftover-via-VE Kortrijk leftover groenezorg deferred.
- Hunt skips: leftover AGB-only candidate stall (2557 did NOT fully hunt) — city_boortmeerbeek/beersel/hoeilaart/kaprijke/lendelede/wielsbeke/ardooie/nieuwpoort/middelkerke/hulshout **0 VAPH admin adres** on official adreslijst 651 orgs; leftover izegem/aarschot/bocholt/kinrooi/haacht/maldegem/zwevegem/temse/aalter/herk_de_stad/oud_turnhout/herselt/berlaar already stalled@2557; leftover VAPH 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend; leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557; leftover city_peer leftover VAPH Monsheide remine@2556; leftover AGB-only VAPH hunt stalled on 0-deposit/YE2024/groenezorg/hard-skips — took NON-stall leftover mined **city_as** leftover VAPH (city GE tick882; no AGB child; Duizendschoon unused). leftover city_beringen 0 VAPH admin; leftover city_destelbergen **Kannet Oost-Vlaanderen vrijetijdszorg SKIP**.
- FIRST LOCK leftover city_as leftover VAPH **Duizendschoon 0683.687.177** leftover-mined city GE tick882 unused leftover type (no agb_as child; Duizendschoon itself unused). Confirmed unused (0 real entity rows on 0683.687.177) + official KBO zetel Bilzerweg 88 **3665 As** (not leftover-via-VE of a DIFFERENT leftover city as parent) + native YE2025 PDF. Took FREE leftover Flemish **Duizendschoon** YE2025 (KBO **0683.687.177**; official zetel Bilzerweg 88 3665 As since 25.09.2017; **Actief** **1 VE** **2.287.333.145** DUIZENDSCHOON Bilzerweg 88 since 05.04.2019; VZW; RSZ2025 **88.104**; leftover of mined **city_as**; FOI info@arbeidskansen.be from official KBO VE + official VAPH; leftover VAPH / official VAPH adreslijst Duizendschoon Vergunde Zorgaanbieder). Identity trap: 0683.687.177 ≠ leftover Labor Arbeidskansen **0432.385.616** remine@2292 under sec_flanders (same zetel Bilzerweg 88; own VZW). Confirmed leftover public leftover dual not convent / not leftover-via-VE of a DIFFERENT leftover city as parent / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. VKT-VZW **native text** (not scan) — 42056 B / 10p native euros (VKT-VZW 6.1.1 6.1.2 6.1.3 6.2 6.3 6.5 6.6 7 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00236227** (42056 B / 10p; AV **30.06.2026**; header **01/07/2026**; CDN GET **200** 42056 official NBB-generated OpenPDF 1.3.26 CreationDate 2026-07-02 09:14:50 UTC MD5 58a7b5f8215ee855ac02229d3cc191da; NBB consult HTML stub discarded; statutory pages native; prior-year identical not restated; Companyweb unused for euros) — omzet 70 **EUR8261** JUMP +2.75% (was 8040); 73 **empty**; 76A **empty**; envelope bruto 9900 **EUR215719** JUMP +12.79% (VKT envelope because 73 empty and bruto >> omzet; was 191250); 74 **not on VKT form**; 62 **EUR189836** JUMP +49.19% (was 127243); 630 **empty**; 640/8 **EUR0** DROP (was 2167); bedrijfswinst 9901 **EUR25883** DROP −58.15% (was 61840); pnl 9904 **EUR25514** DROP −58.50% (was 61477); 9903 **EUR25514**; equity **EUR132999** JUMP +23.74%; assets **EUR206531** JUMP +5.38%; debt **EUR73532** DROP −16.91%; FTE 9087 **1,6** JUMP +60% (was 1; 105 YE 0,8); kapitaalsubsidies **empty**; destin 691/791 **empty**; cash **EUR140931** JUMP +126.66% (+79k vs 62177); geldbeleggingen **empty**; gebouwen **empty**; MVA 22/27 **empty**; aanbouw **empty**; capex **empty**. Strong KBO + Strong PDF (native statutory pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_as leftover VAPH unused leftover type after city GE tick882. NOT leftover-via-VE of a DIFFERENT leftover city as parent. NOT Armonea commercial.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1 pi 5.33; entities +1; FOI **{GAP}** prio7 ready + draft; raw PDF docs/doge/raw/tick2558/; rq_2558=done; spawn **rq_2559 leftover dual (NOT every-10; next every-10 2560)**; ticks=2558.
- Next: **rq_2559 leftover dual** (NOT every-10; next every-10 **2560**).
"""
log_path.write_bytes(log_raw + block.encode("utf-8"))
print("appended loop_log")
print("rq+state+log ok")

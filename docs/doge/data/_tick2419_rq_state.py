#!/usr/bin/env python3
"""Surgical patch rq_2419=done + spawn rq_2420; do not rewrite whole 63MB file."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2419_stamp.txt").read_text().strip().splitlines()
GAP = "gap_pagadder_opgroeien_matrix_opbr_1_61m_73_1_31m_omzet_298k_pnl_drop_83k_destin_0_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
n2419 = rq_raw.count(b"rq_2419,")
if n2419 != 1:
    raise SystemExit(f"expected 1 rq_2419 marker, found {n2419}")
if b"rq_2420," in rq_raw:
    raise SystemExit("rq_2420 already exists")

new_2419 = (
    "rq_2419,leftover dual — Kinderopvang De Pagadder YE2025 Strong (opbr FLAT 1.61m / 73 1.31m / omzet 298k / pnl DROP 83k / destin 0),"
    "hole_fill,8,done,L5,vzw_pagadder,"
    "Tick 2419 leftover after KOS. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi; NOT LDSST; NOT De Schans; NOT CAR Houtland; NOT Zonnebloem; NOT ZWZ; NOT CAR Horizon; NOT CAR Accent; NOT Waas; NOT CAR Halle Asse; NOT Heuvelheem; NOT ARC; NOT VERBINT; NOT CFR Zelzate; NOT De Kade; NOT Ter Eecken; NOT De Hoeksteen; NOT De Mereltjes; NOT 3Wplus; NOT t Eekhoorntje; NOT Elfenbankje; NOT Zonnestraal Junior; NOT KINDEROPVANG ZONNESTRAAL; NOT Kinderopvang Turnhout; NOT Bengelhof; NOT Buitenschoolse Opvang Ieper; NOT Kinderopvang Mariawende; NOT Denderkind; NOT BKO GENK-OOST; NOT KOS). "
    "Took De Pagadder 0888.028.268 deposit 2026-00133513 leftover city_kortrijk. Distinct from KOS 0891.472.362 and from Vormingscentrum 0413.342.338 training. Distinct from WZC De Ruyschaert 0434.996.993 leftover city_kortrijk not taken this tick. "
    "Do NOT redo KOS/BKO GENK-OOST/Denderkind/Kinderopvang Mariawende/Buitenschoolse Opvang Ieper/Bengelhof/Kinderopvang Turnhout/KINDEROPVANG ZONNESTRAAL/Zonnestraal Junior/Elfenbankje/t Eekhoorntje/3Wplus/De Mereltjes/De Hoeksteen/Ter Eecken/De Kade/CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg/Zonnestraal parent stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Vriendenkring 0436.787.139 stopgezet 16.11.1995 skip. CAR Antenne 3000 0433.184.479 CDN 403 skip. AZ Sint-Maria 0467.967.491 CDN 403 skip. CAR Noorderkempen 0408.078.010 YE2025 2026-00145984 SCAN skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T04:22:46Z,{STAMP},"
    "tick2419 De Pagadder 0888.028.268 YE2025 Strong official native PDF 2026-00133513; opbr 70+73+76A JUMP 1607724 VZW envelope; omzet70 JUMP 297790 commercial-only; 73 JUMP 1307284; 76A JUMP 2650; bruto9900 DROP 1330335; pnl DROP 82665; 9901 DROP 72984; equity JUMP 947907; assets JUMP 1193085; debt JUMP 245179; FTE JUMP 21.3; kapitaalsubsidies empty; destin691 empty; cash JUMP 167197; geldbeleggingen JUMP 786842; gebouwen DROP 16904; 2 VE Kloosterstraat + Marktstraat leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; FOI ready NOT sent; leftover city_kortrijk; NOT every-10 (next 2420); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum\n"
)
new_2420 = (
    "rq_2420,leftover dual after De Pagadder — EVERY-10 + hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "EVERY-10 after De Pagadder YE2025. MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT De Schans 0430.473.231; NOT CAR Houtland 0408.436.019; NOT Zonnebloem 0421.039.386; NOT ZWZ 0832.024.923; NOT CAR Horizon 0418.529.759; NOT CAR Accent 0413.208.122; NOT Waas 0415.472.279; NOT CAR Halle Asse 0425.788.230; NOT Heuvelheem 0413.210.201; NOT ARC 0408.434.930; NOT VERBINT 0408.032.379; NOT CFR Zelzate 0419.645.952; NOT De Kade 0413.650.659; NOT Ter Eecken 0432.465.392; NOT De Hoeksteen 0765.439.866; NOT De Mereltjes 0412.778.352; NOT 3Wplus 0893.870.539; NOT t Eekhoorntje 0414.453.680; NOT Elfenbankje 0417.638.151; NOT Zonnestraal Junior 0866.116.859; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Kinderopvang Turnhout 0465.284.947; NOT Bengelhof 0455.442.813; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Kinderopvang Mariawende 0411.611.184; NOT Denderkind 0479.127.045; NOT BKO GENK-OOST 0475.432.830; NOT KOS 0891.472.362; NOT De Pagadder 0888.028.268). "
    "Do NOT redo De Pagadder/KOS/BKO GENK-OOST/Denderkind/Kinderopvang Mariawende/Buitenschoolse Opvang Ieper/Bengelhof/Kinderopvang Turnhout/KINDEROPVANG ZONNESTRAAL/Zonnestraal Junior/Elfenbankje/t Eekhoorntje/3Wplus/De Mereltjes/De Hoeksteen/Ter Eecken/De Kade/CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Vriendenkring 0436.787.139 stopgezet skip. CAR Antenne 3000 leftover city_leuven CDN 403 re-HEAD only. AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB 2026-00299006 CDN 403 skip unless official PDF downloads. CAR Noorderkempen 0408.078.010 leftover city_wuustwezel YE2025 2026-00145984 SCAN 1.09MB Ricoh no native euros — skip unless OCR. Zeepreventorium still YE2024. De Bolster still YE2024. Vormingscentrum 0413.342.338 leftover city_gent 2026-00134360 53k training not CIK — only if leftover training of mined parent is in LOOP.md priority. Helan Kinderopvang 0464.151.037 leftover city_antwerpen 2026-00206337 909k Helan-HH-adjacent skip (Helan HH family already skipped). NOW leftover WZC candidate: WZC De Ruyschaert 0434.996.993 leftover city_kortrijk (adjacent same board/email as Pagadder; Kloosterstraat 25 Marke) — take ONLY if unused + official YE2025 PDF euros; do NOT invent from Companyweb/Belscope. Confirm unused before treating as leftover.,"
    f",{STAMP},{STAMP},"
    "spawned after tick2419; De Pagadder taken leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; Noorderkempen scan skip; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; AGB/FARO/Gandae still YE2024; THIS TICK IS EVERY-10 — must refresh progress_every_10_ticks.md + doge_waste_top10_current.md\n"
)

idx = rq_raw.rfind(b"rq_2419,")
if idx < 0:
    raise SystemExit("rq_2419 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2419.encode("utf-8"))
    f.write(new_2420.encode("utf-8"))
print("patched research_queue rq_2419 + rq_2420; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2419,2419,no,"
    "tick2419 leftover dual De Pagadder 0888.028.268 Strong native PDF (opbr 70+73+76A JUMP 1607724 VZW envelope; omzet70 JUMP 297790 commercial-only; 73 JUMP 1307284; 76A JUMP 2650; bruto9900 DROP 1330335; pnl DROP 82665; 9901 DROP 72984; equity JUMP 947907; assets JUMP 1193085; debt JUMP 245179; FTE JUMP 21.3; kapitaalsubsidies empty; destin691 empty; cash JUMP 167197; geldbeleggingen JUMP 786842; gebouwen DROP 16904; 2 VE Kloosterstraat + Marktstraat); leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; NOT every-10 (next 2420); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum; AGB/FARO/Gandae YE2024; next rq_2420 EVERY-10; next every-10 2420\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2418,2418," not in cur:
    raise SystemExit("loop_state not at 2418; abort")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

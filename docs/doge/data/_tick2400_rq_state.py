#!/usr/bin/env python3
"""Surgical patch rq_2400=done + spawn rq_2401; do not rewrite whole 63MB file."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2400_stamp.txt").read_text().strip().splitlines()
GAP = "gap_arc_riziv_vl_vaph_matrix_bruto_2_49m_omzet73_empty_pnl_jump_destin_170k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
if rq_raw.count(b"\nrq_2400,") + (1 if rq_raw.startswith(b"rq_2400,") else 0) != 1:
    # safer unique check
    pass
n2400 = rq_raw.count(b"rq_2400,")
if n2400 != 1:
    raise SystemExit(f"expected 1 rq_2400 marker, found {n2400}")
if b"rq_2401," in rq_raw:
    raise SystemExit("rq_2401 already exists")

new_2400 = (
    "rq_2400,EVERY-10 + leftover dual — Antwerps Revalidatiecentrum YE2025 Strong (bruto FLAT 2.49m / omzet+73 empty / pnl JUMP 174k / destin DROP 170k),"
    "hole_fill,8,done,L5,vzw_car_antwerpen,"
    "Tick 2400 EVERY-10 leftover after Heuvelheem. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi; NOT LDSST; NOT De Schans; NOT CAR Houtland; NOT Zonnebloem; NOT ZWZ; NOT CAR Horizon; NOT CAR Accent; NOT Waas; NOT CAR Halle Asse; NOT Heuvelheem). "
    "Took Antwerps Revalidatiecentrum 0408.434.930 deposit 2026-00272201 leftover city_antwerpen. Distinct from Heuvelheem 0413.210.201 just mined. "
    "Do NOT redo Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Vriendenkring 0436.787.139 stopgezet 16.11.1995 skip. CAR Antenne 3000 0433.184.479 CDN 403 skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T01:49:19Z,{STAMP},"
    "tick2400 EVERY-10 ARC 0408.434.930 YE2025 Strong official native PDF 2026-00272201; bruto9900 DROP 2489143 VKT envelope; omzet70 empty; 73 empty; pnl JUMP 174281; equity JUMP 1771285; assets JUMP 2168233; debt DROP 396948; FTE 30; kapitaalsubsidies DROP 81587; destin691 DROP 170000; cash JUMP 779521; FOI ready NOT sent; leftover city_antwerpen after Heuvelheem@2399; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF Vriendenkring OFF Antenne 3000\n"
)
new_2401 = (
    "rq_2401,leftover dual after ARC Antwerpen — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After ARC Antwerpen YE2025 EVERY-10. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT De Schans 0430.473.231; NOT CAR Houtland 0408.436.019; NOT Zonnebloem 0421.039.386; NOT ZWZ 0832.024.923; NOT CAR Horizon 0418.529.759; NOT CAR Accent 0413.208.122; NOT Waas 0415.472.279; NOT CAR Halle Asse 0425.788.230; NOT Heuvelheem 0413.210.201; NOT ARC 0408.434.930). "
    "Do NOT redo ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Vriendenkring 0436.787.139 stopgezet skip. CAR Antenne 3000 leftover city_leuven CDN 403 re-HEAD only. AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB 2026-00299006 CDN 403 skip unless official PDF downloads. CFR Zelzate 0419.645.952 leftover city_zelzate unused still YE2024. Zeepreventorium still YE2024. De Bolster still YE2024. Next every-10 is 2410.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2400 EVERY-10; ARC taken leftover city_antwerpen after Heuvelheem; AGB/FARO/Gandae still YE2024; next every-10 2410\n"
)

idx = rq_raw.rfind(b"rq_2400,")
if idx < 0:
    raise SystemExit("rq_2400 line not found")
# surgical: truncate at last-line start and append replacement + spawn
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2400.encode("utf-8"))
    f.write(new_2401.encode("utf-8"))
print("patched research_queue rq_2400 + rq_2401; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2400,2400,no,"
    "tick2400 EVERY-10 leftover dual ARC Antwerpen 0408.434.930 Strong native PDF (omzet70 empty; 73 empty; bruto9900 DROP 2489143 CAR envelope; pnl JUMP 174281; equity JUMP 1771285; assets JUMP 2168233; debt DROP 396948; FTE 30; kapitaalsubsidies DROP 81587; destin691 DROP 170000; cash JUMP 779521; 1 VE RSZ2025 86.959); leftover city_antwerpen after Heuvelheem@2399; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000; AGB/FARO/Gandae YE2024; next rq_2401; next every-10 2410\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

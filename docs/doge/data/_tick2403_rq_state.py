#!/usr/bin/env python3
"""Surgical patch rq_2403=done + spawn rq_2404; do not rewrite whole 63MB file."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2403_stamp.txt").read_text().strip().splitlines()
GAP = "gap_dekade_vaph_car_matrix_opbr_60_22m_73_51_29m_pnl_drop_destin_800k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
n2403 = rq_raw.count(b"rq_2403,")
if n2403 != 1:
    raise SystemExit(f"expected 1 rq_2403 marker, found {n2403}")
if b"rq_2404," in rq_raw:
    raise SystemExit("rq_2404 already exists")

new_2403 = (
    "rq_2403,leftover dual — De Kade YE2025 Strong (opbr JUMP 60.22m / 73 51.29m / pnl DROP 803k / destin 800k),"
    "hole_fill,8,done,L5,vzw_de_kade,"
    "Tick 2403 leftover after CFR Zelzate. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi; NOT LDSST; NOT De Schans; NOT CAR Houtland; NOT Zonnebloem; NOT ZWZ; NOT CAR Horizon; NOT CAR Accent; NOT Waas; NOT CAR Halle Asse; NOT Heuvelheem; NOT ARC; NOT VERBINT; NOT CFR Zelzate). "
    "Took De Kade 0413.650.659 deposit 2026-00300772 leftover city_brugge. Distinct from CFR Zelzate 0419.645.952 just mined. "
    "Do NOT redo CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Vriendenkring 0436.787.139 stopgezet 16.11.1995 skip. CAR Antenne 3000 0433.184.479 CDN 403 skip. AZ Sint-Maria 0467.967.491 CDN 403 skip. CAR Noorderkempen 0408.078.010 YE2025 2026-00145984 SCAN skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T02:16:17Z,{STAMP},"
    "tick2403 De Kade 0413.650.659 YE2025 Strong official native PDF 2026-00300772; 70/76A JUMP 60221495 VAPH+CAR+BuO envelope; omzet70 7767727 commercial-only; 73 JUMP 51285974; pnl DROP 803199; equity JUMP 64477006; assets JUMP 86453940; debt JUMP 20196222; FTE 657.5; kapitaalsubsidies DROP 11803327; destin691 DROP 800000; cash DROP 5301142; geldbeleggingen JUMP 21930224; capex 2185673; FOI ready NOT sent; leftover city_brugge after CFR Zelzate@2402; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos\n"
)
new_2404 = (
    "rq_2404,leftover dual after De Kade — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After De Kade YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT De Schans 0430.473.231; NOT CAR Houtland 0408.436.019; NOT Zonnebloem 0421.039.386; NOT ZWZ 0832.024.923; NOT CAR Horizon 0418.529.759; NOT CAR Accent 0413.208.122; NOT Waas 0415.472.279; NOT CAR Halle Asse 0425.788.230; NOT Heuvelheem 0413.210.201; NOT ARC 0408.434.930; NOT VERBINT 0408.032.379; NOT CFR Zelzate 0419.645.952; NOT De Kade 0413.650.659). "
    "Do NOT redo De Kade/CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Vriendenkring 0436.787.139 stopgezet skip. CAR Antenne 3000 leftover city_leuven CDN 403 re-HEAD only. AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB 2026-00299006 CDN 403 skip unless official PDF downloads. CAR Noorderkempen 0408.078.010 leftover city_wuustwezel YE2025 2026-00145984 SCAN 1.09MB Ricoh no native euros — skip unless OCR. Zeepreventorium still YE2024. De Bolster still YE2024. Next every-10 is 2410.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2403; De Kade taken leftover city_brugge after CFR Zelzate; Noorderkempen scan skip; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; AGB/FARO/Gandae still YE2024; next every-10 2410\n"
)

idx = rq_raw.rfind(b"rq_2403,")
if idx < 0:
    raise SystemExit("rq_2403 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2403.encode("utf-8"))
    f.write(new_2404.encode("utf-8"))
print("patched research_queue rq_2403 + rq_2404; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2403,2403,no,"
    "tick2403 leftover dual De Kade 0413.650.659 Strong native PDF (70/76A JUMP 60221495 VAPH+CAR+BuO envelope; omzet70 7767727 commercial-only; 73 JUMP 51285974; pnl DROP 803199; equity JUMP 64477006; assets JUMP 86453940; debt JUMP 20196222; FTE 657.5; kapitaalsubsidies DROP 11803327; destin691 DROP 800000; cash DROP 5301142; geldbeleggingen JUMP 21930224; capex 2185673; 35 VE RSZ2025 87.201); leftover city_brugge after CFR Zelzate@2402; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos; AGB/FARO/Gandae YE2024; next rq_2404; next every-10 2410\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

#!/usr/bin/env python3
"""Surgical patch rq_2401=done + spawn rq_2402; do not rewrite whole 63MB file."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2401_stamp.txt").read_text().strip().splitlines()
GAP = "gap_verbint_car_clb_wzc_vaph_matrix_omzet_12_89m_73_10_06m_pnl_jump_6_0m_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
n2401 = rq_raw.count(b"rq_2401,")
if n2401 != 1:
    raise SystemExit(f"expected 1 rq_2401 marker, found {n2401}")
if b"rq_2402," in rq_raw:
    raise SystemExit("rq_2402 already exists")

new_2401 = (
    "rq_2401,leftover dual — VERBINT / Carrewiel YE2025 Strong (omzet JUMP 12.89m / 73 10.06m / pnl JUMP 6.0m / destin 284k),"
    "hole_fill,8,done,L5,vzw_verbint,"
    "Tick 2401 leftover after ARC. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi; NOT LDSST; NOT De Schans; NOT CAR Houtland; NOT Zonnebloem; NOT ZWZ; NOT CAR Horizon; NOT CAR Accent; NOT Waas; NOT CAR Halle Asse; NOT Heuvelheem; NOT ARC). "
    "Took VERBINT 0408.032.379 deposit 2026-00297392 leftover city_turnhout + leftover city_mechelen + leftover city_westerlo (Carrewiel = fusie CAR Turnhout + CAR Zuiderkempen + CAR Vijfhoek). Distinct from ARC 0408.434.930 just mined. "
    "Do NOT redo ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Vriendenkring 0436.787.139 stopgezet 16.11.1995 skip. CAR Antenne 3000 0433.184.479 CDN 403 skip. CAR Noorderkempen 0408.078.010 YE2025 2026-00145984 SCAN skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T01:58:43Z,{STAMP},"
    "tick2401 VERBINT 0408.032.379 YE2025 Strong official native PDF 2026-00297392; omzet70 JUMP 12890158; 73 JUMP 10059857; 70/76A JUMP 31375466; 76A 6524604; pnl JUMP 5963538; equity JUMP 30969115; assets JUMP 48228242; debt JUMP 16245572; FTE 207.7; kapitaalsubsidies DROP 2615933; destin691 JUMP 284439; cash JUMP 6890725; FOI ready NOT sent; leftover city_turnhout after ARC@2400; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan\n"
)
new_2402 = (
    "rq_2402,leftover dual after VERBINT / Carrewiel — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After VERBINT / Carrewiel YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT De Schans 0430.473.231; NOT CAR Houtland 0408.436.019; NOT Zonnebloem 0421.039.386; NOT ZWZ 0832.024.923; NOT CAR Horizon 0418.529.759; NOT CAR Accent 0413.208.122; NOT Waas 0415.472.279; NOT CAR Halle Asse 0425.788.230; NOT Heuvelheem 0413.210.201; NOT ARC 0408.434.930; NOT VERBINT 0408.032.379). "
    "Do NOT redo VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Vriendenkring 0436.787.139 stopgezet skip. CAR Antenne 3000 leftover city_leuven CDN 403 re-HEAD only. AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB 2026-00299006 CDN 403 skip unless official PDF downloads. CFR Zelzate 0419.645.952 leftover city_zelzate unused NOW LIVE YE2025 2026-00243990 CDN HEAD 200 / 57128 B — prefer smaller native. CAR Noorderkempen 0408.078.010 leftover city_wuustwezel YE2025 2026-00145984 SCAN 1.09MB Ricoh no native euros — skip unless OCR. Zeepreventorium still YE2024. De Bolster still YE2024. Next every-10 is 2410.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2401; VERBINT taken leftover city_turnhout after ARC; Zelzate now live 2026-00243990 prefer next; Noorderkempen scan skip; AGB/FARO/Gandae still YE2024; next every-10 2410\n"
)

idx = rq_raw.rfind(b"rq_2401,")
if idx < 0:
    raise SystemExit("rq_2401 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2401.encode("utf-8"))
    f.write(new_2402.encode("utf-8"))
print("patched research_queue rq_2401 + rq_2402; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2401,2401,no,"
    "tick2401 leftover dual VERBINT / Carrewiel 0408.032.379 Strong native PDF (omzet70 JUMP 12890158; 73 JUMP 10059857; 70/76A JUMP 31375466; 76A 6524604; pnl JUMP 5963538; equity JUMP 30969115; assets JUMP 48228242; debt JUMP 16245572; FTE 207.7; kapitaalsubsidies DROP 2615933; destin691 JUMP 284439; cash JUMP 6890725; 20 VE RSZ2025 85.691); leftover city_turnhout + city_mechelen + city_westerlo after ARC@2400; KMSI fusion 31.03.2025; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan; Zelzate now live 2026-00243990 not taken; AGB/FARO/Gandae YE2024; next rq_2402; next every-10 2410\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

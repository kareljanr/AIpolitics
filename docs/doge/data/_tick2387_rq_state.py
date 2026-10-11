#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2387_stamp.txt").read_text().strip().splitlines()
GAP = "gap_dehert_riziv_vl_vaph_matrix_omzet_1_87m_73_634k_pnl_jump_destin_empty_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2387,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2387 line, found {n}")
if "rq_2388," in rq_text:
    raise SystemExit("rq_2388 already exists")

new_2387 = (
    "rq_2387,leftover dual — CAR De Hert Aalst YE2025 Strong (omzet JUMP 1.87m / 73 634k / pnl JUMP 31k / destin empty),"
    "hole_fill,8,done,L5,vzw_car_de_hert,"
    "Tick 2387 leftover after CAR De Klinker. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker). "
    "Took CAR De Hert Aalst 0409.371.672 deposit 2026-00174560 leftover city_aalst. "
    "Do NOT redo CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T00:13:44Z,{STAMP},"
    "tick2387 CAR De Hert 0409.371.672 YE2025 Strong official native PDF 2026-00174560; omzet70 JUMP 1869719 CAR envelope; 73 JUMP 634363; bruto JUMP 2409407; pnl JUMP 31450; equity DROP 2657601; assets JUMP 3220530; debt JUMP 562928; FTE 27 JUMP; kapitaalsubsidies DROP 1066108; destin691 empty; cash JUMP 924004; FOI ready NOT sent; leftover city_aalst after De Klinker@2386; OFF Drongen OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2387,"):
        parts.append(new_2387)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2387 replace count {replaced}")
new_rq = "".join(parts)
new_2388 = (
    "rq_2388,leftover dual after CAR De Hert — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR De Hert Aalst YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672). "
    "Do NOT redo CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. Candidate leftover REVA Kohesi 0410.121.641 leftover city_hasselt YE2025 filed 03.07.2026 (need live 2026pdf deposit-id; NOT CGG Kohesi 0472.466.907 already mined). Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2387; CAR De Hert taken leftover city_aalst after De Klinker; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2388
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2387 + rq_2388; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2387,2387,no,"
    "tick2387 leftover dual CAR De Hert Aalst 0409.371.672 Strong native PDF (omzet70 JUMP 1869719 CAR envelope; 73 JUMP 634363; bruto JUMP 2409407; pnl JUMP 31450; equity DROP 2657601; assets JUMP 3220530; debt JUMP 562928; FTE 27 JUMP; kapitaalsubsidies DROP 1066108; destin691 empty; cash JUMP 924004; 1 VE RSZ2025 86.959 VAZG 9.65.105.45 VAPH R/105); leftover city_aalst after De Klinker@2386; OFF Drongen OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie; AGB/FARO/Gandae YE2024; next rq_2388; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

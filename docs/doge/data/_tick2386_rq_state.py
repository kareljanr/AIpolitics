#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2386_stamp.txt").read_text().strip().splitlines()
GAP = "gap_deklinker_riziv_vl_vaph_matrix_bruto_1_62m_omzet73_empty_destin_179k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2386,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2386 line, found {n}")
if "rq_2387," in rq_text:
    raise SystemExit("rq_2387 already exists")

new_2386 = (
    "rq_2386,leftover dual — CAR De Klinker Ieper YE2025 Strong (bruto JUMP 1.62m / omzet+73 empty / destin 179k / cash 269k),"
    "hole_fill,8,done,L5,vzw_car_deklinker,"
    "Tick 2386 leftover after Ascendere. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere). "
    "Took CAR De Klinker Ieper 0430.535.290 deposit 2026-00241698 leftover city_ieper. "
    "Do NOT redo Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T00:04:21Z,{STAMP},"
    "tick2386 CAR De Klinker 0430.535.290 YE2025 Strong official native PDF 2026-00241698; omzet70 empty VKT; 73 empty VKT; bruto JUMP 1615845 CAR envelope; pnl JUMP 68250; equity JUMP 421965; assets JUMP 835288; debt JUMP 413323; FTE 18.6 JUMP; kapitaalsubsidies DROP 127157; destin691 JUMP 179028; cash JUMP 268878; FOI ready NOT sent; leftover city_ieper after Ascendere@2385; OFF Drongen OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2386,"):
        parts.append(new_2386)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2386 replace count {replaced}")
new_rq = "".join(parts)
new_2387 = (
    "rq_2387,leftover dual after CAR De Klinker — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR De Klinker Ieper YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290). "
    "Do NOT redo CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2386; CAR De Klinker taken leftover city_ieper after Ascendere; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2387
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2386 + rq_2387; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2386,2386,no,"
    "tick2386 leftover dual CAR De Klinker Ieper 0430.535.290 Strong native PDF (omzet70 empty VKT; 73 empty VKT; bruto JUMP 1615845 CAR envelope; pnl JUMP 68250; equity JUMP 421965; assets JUMP 835288; debt JUMP 413323; FTE 18.6 JUMP; kapitaalsubsidies DROP 127157; destin691 JUMP 179028; cash JUMP 268878; 1 VE RSZ2025 86.959 RIZIV 9.53.579.28 VAPH 579); leftover city_ieper after Ascendere@2385; OFF Drongen OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie; AGB/FARO/Gandae YE2024; next rq_2387; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

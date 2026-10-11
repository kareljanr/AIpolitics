#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2388_stamp.txt").read_text().strip().splitlines()
GAP = "gap_revakohesi_riziv_vl_vaph_matrix_omzet_5_96m_73_1_86m_pnl_drop_destin_54k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2388,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2388 line, found {n}")
if "rq_2389," in rq_text:
    raise SystemExit("rq_2389 already exists")

new_2388 = (
    "rq_2388,leftover dual — REVA Kohesi Hasselt YE2025 Strong (omzet DROP 5.96m / 73 1.86m / pnl DROP 104k / destin 54k),"
    "hole_fill,8,done,L5,vzw_reva_kohesi,"
    "Tick 2388 leftover after CAR De Hert. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert). "
    "Took REVA Kohesi 0410.121.641 deposit 2026-00244637 leftover city_hasselt. Distinct from CGG Kohesi 0472.466.907 already mined. "
    "Do NOT redo REVA Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T00:23:16Z,{STAMP},"
    "tick2388 REVA Kohesi 0410.121.641 YE2025 Strong official native PDF 2026-00244637; omzet70 DROP 5960431 CAR envelope; 73 DROP 1863434; 70/76A JUMP 8755588; pnl DROP 104069; equity JUMP 6474902; assets DROP 8501347; debt DROP 2026445; FTE 85.2 JUMP; kapitaalsubsidies DROP 1102703; destin691 DROP 53728; cash DROP 1533265; FOI ready NOT sent; leftover city_hasselt after De Hert@2387; OFF Drongen OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF CGG Kohesi\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2388,"):
        parts.append(new_2388)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2388 replace count {replaced}")
new_rq = "".join(parts)
new_2389 = (
    "rq_2389,leftover dual after REVA Kohesi — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After REVA Kohesi Hasselt YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907). "
    "Do NOT redo REVA Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. Candidate leftover same-family Beschut Wonen Kohesi / De Schans / LDSST (BTW-eenheid with REVA+CGG) only if unused + live 2026pdf. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2388; REVA Kohesi taken leftover city_hasselt after De Hert; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2389
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2388 + rq_2389; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2388,2388,no,"
    "tick2388 leftover dual REVA Kohesi 0410.121.641 Strong native PDF (omzet70 DROP 5960431 CAR envelope; 73 DROP 1863434; 70/76A JUMP 8755588; pnl DROP 104069; equity JUMP 6474902; assets DROP 8501347; debt DROP 2026445; FTE 85.2 JUMP; kapitaalsubsidies DROP 1102703; destin691 DROP 53728; cash DROP 1533265; 8 VE RSZ2025 88.999); leftover city_hasselt after De Hert@2387; OFF Drongen OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF CGG Kohesi; AGB/FARO/Gandae YE2024; next rq_2389; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

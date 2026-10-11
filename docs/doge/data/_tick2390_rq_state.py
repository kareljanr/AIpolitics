#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2390_stamp.txt").read_text().strip().splitlines()
GAP = "gap_ldsst_riziv_vl_logopedie_matrix_bruto_591k_73_179k_pnl_flip_destin_59k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2390,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2390 line, found {n}")
if "rq_2391," in rq_text:
    raise SystemExit("rq_2391 already exists")

new_2390 = (
    "rq_2390,EVERY-10 + leftover dual — LDSST Hasselt YE2025 Strong (bruto JUMP 591k / 73 179k / pnl PROFIT FLIP 99k / destin 59k),"
    "hole_fill,8,done,L5,vzw_ldsst,"
    "Tick 2390 EVERY-10 leftover after Beschut Wonen Kohesi. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi). "
    "Took LDSST 0410.121.344 deposit 2026-00243690 leftover city_hasselt same-family Kohesi. Distinct from REVA Kohesi 0410.121.641 / CGG Kohesi 0472.466.907 / Beschut Wonen Kohesi 0451.932.995 just mined. "
    "Do NOT redo LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T00:37:25Z,{STAMP},"
    "tick2390 EVERY-10 LDSST 0410.121.344 YE2025 Strong official native PDF 2026-00243690; bruto9900 JUMP 591161 MIC envelope; omzet70 DROP 35784 commercial-only; 73 DROP 179055; pnl PROFIT FLIP 98656; equity JUMP 162403; assets JUMP 437505; debt JUMP 275102; FTE 6.9 JUMP; kapitaalsubsidies empty; destin691 JUMP 59104; cash DROP 35597; FOI ready NOT sent; leftover city_hasselt after BW Kohesi@2389; OFF Drongen OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2390,"):
        parts.append(new_2390)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2390 replace count {replaced}")
new_rq = "".join(parts)
new_2391 = (
    "rq_2391,leftover dual after LDSST — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After LDSST YE2025 EVERY-10. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344). "
    "Do NOT redo LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. Candidate leftover same-family De Schans 0430.473.231 Belscope YE2025 microschema unused (need live 2026pdf deposit-id). Next every-10 is 2400.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2390 EVERY-10; LDSST taken leftover city_hasselt after BW Kohesi; AGB/FARO/Gandae still YE2024; next every-10 2400\n"
)
new_rq = new_rq + new_2391
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2390 + rq_2391; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2390,2390,no,"
    "tick2390 EVERY-10 leftover dual LDSST 0410.121.344 Strong native PDF (bruto9900 JUMP 591161 MIC envelope; omzet70 DROP 35784 commercial-only; 73 DROP 179055; pnl PROFIT FLIP 98656; equity JUMP 162403; assets JUMP 437505; debt JUMP 275102; FTE 6.9 JUMP; kapitaalsubsidies empty; destin691 JUMP 59104; cash DROP 35597; 1 VE RSZ2025 86.996); leftover city_hasselt after BW Kohesi@2389; OFF Drongen OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie; AGB/FARO/Gandae YE2024; next rq_2391; next every-10 2400\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP = "2026-08-25T00:04:21Z"
GAP = "gap_ascendere_riziv_vl_vaph_matrix_omzet_4_34m_73_866k_pnl_drop_destin_empty_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2385,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2385 line, found {n}")
if "rq_2386," in rq_text:
    raise SystemExit("rq_2386 already exists")

new_2385 = (
    "rq_2385,leftover dual — Ascendere CAR Eeklo/Lede/Ninove/Wetteren YE2025 Strong (omzet JUMP 4.34m / 73 866k / pnl DROP 27k / destin empty),"
    "hole_fill,8,done,L5,vzw_ascendere,"
    "Tick 2385 leftover after CAR Roeselare. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare). "
    "Took Ascendere 0409.470.553 deposit 2026-00209823 leftover city_eeklo. "
    "Do NOT redo CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:55:21Z,{STAMP},"
    "tick2385 Ascendere 0409.470.553 YE2025 Strong official native PDF 2026-00209823; omzet JUMP 4338634 CAR envelope; bruto DROP 4821515; 73 DROP 865623; pnl DROP 27286; equity DROP 3529703; assets DROP 5657078; debt DROP 2127375; FTE 52.5 DROP; kapitaalsubsidies DROP 1098275; destin691 empty; cash JUMP 1688162; geldbeleggingen emptied; FOI ready NOT sent; leftover city_eeklo after CAR Roeselare@2384; OFF Drongen OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2385,"):
        parts.append(new_2385)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2385 replace count {replaced}")
new_rq = "".join(parts)
new_2386 = (
    "rq_2386,leftover dual after Ascendere — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Ascendere YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553). "
    "Do NOT redo Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2385; Ascendere taken leftover city_eeklo after CAR Roeselare; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2386
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2385 + rq_2386; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2385,2385,no,"
    "tick2385 leftover dual Ascendere 0409.470.553 Strong native PDF (omzet JUMP 4338634 CAR envelope; bruto DROP 4821515; 73 DROP 865623; pnl DROP 27286; equity DROP 3529703; assets DROP 5657078; debt DROP 2127375; FTE 52.5 DROP; kapitaalsubsidies DROP 1098275; destin691 empty; cash JUMP 1688162; geldbeleggingen emptied; 4 VE RSZ2025 86.959); leftover city_eeklo after CAR Roeselare@2384; OFF Drongen OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie; AGB/FARO/Gandae YE2024; next rq_2386; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

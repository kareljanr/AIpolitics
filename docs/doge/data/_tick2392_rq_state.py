#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2392_stamp.txt").read_text().strip().splitlines()
GAP = "gap_houtland_riziv_vl_vaph_matrix_omzet_4_93m_73_1_06m_pnl_flip_destin_empty_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2392,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2392 line, found {n}")
if "rq_2393," in rq_text:
    raise SystemExit("rq_2393 already exists")

new_2392 = (
    "rq_2392,leftover dual — CAR Houtland-Westkust YE2025 Strong (omzet JUMP 4.93m / 73 1.06m / pnl PROFIT FLIP 34k / destin empty),"
    "hole_fill,8,done,L5,vzw_car_houtland,"
    "Tick 2392 leftover after De Schans. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi; NOT LDSST; NOT De Schans). "
    "Took CAR Houtland-Westkust 0408.436.019 deposit 2026-00115391 leftover city_zedelgem + leftover city_nieuwpoort. Distinct from De Schans 0430.473.231 / LDSST 0410.121.344 / REVA Kohesi 0410.121.641 / CGG Kohesi 0472.466.907 / Beschut Wonen Kohesi 0451.932.995 just mined. "
    "Do NOT redo CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Kohesi family exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T00:50:10Z,{STAMP},"
    "tick2392 CAR Houtland-Westkust 0408.436.019 YE2025 Strong official native PDF 2026-00115391; omzet70 JUMP 4926107 CAR envelope; 73 JUMP 1056007; 70/76A JUMP 6109882; pnl PROFIT FLIP 34332; equity JUMP 3945582; assets DROP 6149424; debt DROP 2103842; FTE 63; kapitaalsubsidies JUMP 1231624; destin691 empty; cash DROP 837963; FOI ready NOT sent; leftover city_zedelgem + leftover city_nieuwpoort after De Schans@2391; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2392,"):
        parts.append(new_2392)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2392 replace count {replaced}")
new_rq = "".join(parts)
new_2393 = (
    "rq_2393,leftover dual after CAR Houtland-Westkust — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR Houtland-Westkust YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT De Schans 0430.473.231; NOT CAR Houtland-Westkust 0408.436.019). "
    "Do NOT redo CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Kohesi family exhausted (CGG/REVA/BW/LDSST/De Schans). CAR Overleie YE2024 skip. Ben already in entities skip. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. CAR Antenne 3000 0433.184.479 leftover city_leuven NBB 2026-00375503 YE2025 but CDN 403 / SBM still YE2024 — re-HEAD only. Next every-10 is 2400.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2392; CAR Houtland-Westkust taken leftover city_zedelgem + leftover city_nieuwpoort after De Schans; Kohesi family exhausted; AGB/FARO/Gandae still YE2024; next every-10 2400\n"
)
new_rq = new_rq + new_2393
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2392 + rq_2393; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2392,2392,no,"
    "tick2392 leftover dual CAR Houtland-Westkust 0408.436.019 Strong native PDF (omzet70 JUMP 4926107 CAR envelope; 73 JUMP 1056007; 70/76A JUMP 6109882; pnl PROFIT FLIP 34332; equity JUMP 3945582; assets DROP 6149424; debt DROP 2103842; FTE 63; kapitaalsubsidies JUMP 1231624; destin691 empty; cash DROP 837963; 2 VE RSZ2025 86.959); leftover city_zedelgem + leftover city_nieuwpoort after De Schans@2391; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie; AGB/FARO/Gandae YE2024; next rq_2393; next every-10 2400\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")

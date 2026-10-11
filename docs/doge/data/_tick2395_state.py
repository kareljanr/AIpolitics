#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP = (DATA / "_tick2395_stamp.txt").read_text().strip().splitlines()[0]
state_path = DATA / "loop_state.csv"
hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2395,2395,no,"
    "tick2395 leftover dual CAR Horizon 0418.529.759 Strong native PDF (omzet70 DROP 3001208 CAR envelope; 73 JUMP 464125; bruto9900 DROP 2680880; pnl DROP 246289; equity JUMP 2542581; assets JUMP 2952629; debt DROP 410048; FTE 35; kapitaalsubsidies FLAT 131925; destin691 DROP 246289; cash DROP 958792; geldbeleggingen JUMP 1352010; 1 VE RSZ2025 86.959); leftover city_geraardsbergen after ZWZ@2394; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Ten Anker OFF Leieborg; AGB/FARO/Gandae YE2024; next rq_2396; next every-10 2400\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(hdr + row, encoding="utf-8")
print("wrote loop_state", STAMP)

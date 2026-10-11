from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2501_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_samen_jr2025_nbb_pdf_2501"
EID="vzw_samen_tielt"
GAP="gap_samen_tielt_wzc_matrix_omzet_14_79m_73_jump_2_81m_pnl_loss_305k_cash_drop_1_22m_l5"
COMM="comm_samen_jr2025_statutory_omzet_14_79m_73_jump_2_81m_pnl_loss_305k"
LB="lb_samen_omzet_1479m_73_jump_281m_pnl_loss_305k_cash_drop_122m_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":14791167,\"\"2025_73\"\":2813573,\"\"2025_76A\"\":72928,"
"\"\"2025_opbr7076A\"\":18017846,\"\"2025_bruto9900\"\":0,"
"\"\"2025_pnl\"\":-305249,\"\"2025_bedrijfswinst\"\":247706,"
"\"\"2025_equity\"\":6321909,\"\"2025_assets\"\":39656390,\"\"2025_debt\"\":33334481,"
"\"\"2025_fte\"\":177.6,\"\"2025_kapitaalsubsidies\"\":527989,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":2242270,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":11898410,\"\"2025_gebouwen22\"\":33031510,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":218387,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":5370001,\"\"2025_overgedragen14\"\":423920,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":1840163,\"\"2025_capex\"\":777795,"
"\"\"2025_6408\"\":128921,\"\"2025_74\"\":340177,\"\"2025_9903\"\":-304978,"
"\"\"2024_omzet\"\":12146758,\"\"2024_73\"\":2714341,"
"\"\"2024_opbr7076A\"\":15279508,\"\"2024_bruto9900\"\":0,\"\"2024_pnl\"\":-469342,\"\"2024_bedrijfswinst\"\":-134997,"
"\"\"2024_equity\"\":6541650,\"\"2024_assets\"\":42649653,"
"\"\"2024_debt\"\":36100071,\"\"2024_cash\"\":3455661,\"\"2024_fte\"\":160.1,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":442480,\"\"2024_76A\"\":205923,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},SAMEN YE2025 (omzet JUMP 14.79m / 73 JUMP 2.81m / pnl LOSS 305k IMPROVED / cash DROP 1.21m / Strong PDF),{EID},WZC + leftover city_tielt WZC,SAMEN VZW (KBO 0728.627.079; Actief; 3 VE; official zetel Tielt),2026-06-22,2025,2025,14791167,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00229914.pdf,Public WZC dual of mined city_tielt,Publish RIZIV/VL/zorgkas/gemeente matrix behind omzet 14.79m + 73 2.81m and why pnl LOSS 305k IMPROVED while 9901 FLIP and cash DROP 1.21m,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Tielt>SAMEN>JR2025_statutory_L5,tick2501; Strong official native PDF; leftover mined city_tielt WZC; 3 VE; prior-year identical; NOT De Zonnewende remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"SAMEN omzet JUMP 14.79m / 73 JUMP 2.81m / pnl LOSS 305k IMPROVED / cash DROP 1.21m (YE2025 leftover city_tielt WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Tielt>SAMEN>JR2025",
"14791167",
"14791167",
"PDF envelope 14791167 = omzet 70 because material not commercial-only; 73 JUMP 2813573; 76A DROP 72928; 70/76A JUMP 18017846; bedrijfswinst FLIP 247706; pnl IMPROVED LOSS -305249; equity DROP 6321909; assets DROP 39656390; debt DROP 33334481; FTE JUMP 177.6; kapitaalsubsidies JUMP 527989; destin691 empty; cash DROP 2242270; capex 777795; leftover city_tielt WZC",
"strong",
SRC_PDF,
"WZC + leftover city_tielt WZC",
"WZC leftover city_tielt",
"14.79m omzet; 73 JUMP 2.81m; pnl LOSS 305k IMPROVED; 9901 FLIP; cash DROP 1.21m; leftover city_tielt WZC",
"5.62",
"5.60",
"5.20",
"5.58",
"FOI RIZIV/VL/zorgkas/gemeente matrix behind omzet 14791167 + 73 2813573 and why pnl LOSS -305249 IMPROVED after YE2024 LOSS -469342 while 9901 FLIP 247706 and cash DROP 2242270",
"active",
"",
"tick2501 leftover mined city_tielt WZC after leftover-type hunt; 3 VE; prior-year identical; next rq_2502 leftover dual; next every-10 2510; NOT De Zonnewende remine; NOT De Luifel remine; NOT Mivalti remine; NOT leftover city_dentergem; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Tielt>SAMEN>WZC",
"entity_id": EID,
"what_is_missing": "RIZIV / Vlaamse overheid / zorgkas / gemeente Tielt / gemeente Dentergem / eigen bijdragen split behind omzet 70 14791167 + 73 2813573 and why pnl LOSS -305249 IMPROVED while 9901 FLIP 247706 and cash DROP 2242270",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_tielt; VOL-VZW envelope omzet 70 14.79m because material not commercial-only; public WZC 3 VE (official zetel Tielt; Dentergem VE only); pnl LOSS 305k IMPROVED; 9901 FLIP; cash DROP 1.21m",
"priority": "8",
"recipient_body": "SAMEN VZW / Raad van Bestuur",
"recipient_email": "samentielt@gvo.be",
"recipient_postal": "Krommewalstraat 9 8700 Tielt",
"draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
"status": "ready",
"date_ready": DAY,
"date_sent": "",
"date_due": "",
"date_answered": "",
"response_summary": "",
"linked_commitment_id": COMM,
"linked_leaderboard_id": LB,
"created_utc": STAMP,
"updated_utc": STAMP,
"notes": "tick2501; ready NOT sent; Strong official native NBB PDF; leftover mined city_tielt WZC after leftover-type hunt; 3 VE; prior-year identical; next rq_2502 leftover dual; next every-10 2510; off De Zonnewende remine; off De Luifel remine; off Mivalti remine; off leftover city_dentergem; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")

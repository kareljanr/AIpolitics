from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2499_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_ten_dries_jr2025_nbb_pdf_2499"
EID="vzw_ten_dries_deinze"
GAP="gap_ten_dries_deinze_vaph_matrix_70_76A_9_39m_omzet_commercial_73_jump_8_65m_pnl_drop_106k_l5"
COMM="comm_ten_dries_jr2025_statutory_70_76A_9_39m_73_jump_8_65m_pnl_drop_106k"
LB="lb_ten_dries_7076A_939m_73_jump_865m_pnl_drop_106k_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":357127,\"\"2025_73\"\":8648576,\"\"2025_76A\"\":1666,"
"\"\"2025_opbr7076A\"\":9392001,\"\"2025_bruto9900\"\":0,"
"\"\"2025_pnl\"\":106116,\"\"2025_bedrijfswinst\"\":129620,"
"\"\"2025_equity\"\":8249399,\"\"2025_assets\"\":12364030,\"\"2025_debt\"\":4114631,"
"\"\"2025_fte\"\":104,\"\"2025_kapitaalsubsidies\"\":3272755,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":386799,\"\"2025_geldbeleggingen\"\":2773494,"
"\"\"2025_personnel62\"\":7904740,\"\"2025_gebouwen22\"\":8461114,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":110674,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":852623,\"\"2025_overgedragen14\"\":2293920,"
"\"\"2025_bestemdefondsen13\"\":1830101,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":417814,\"\"2025_capex\"\":5258768,"
"\"\"2025_6408\"\":34038,\"\"2025_74\"\":384632,\"\"2025_9903\"\":116805,"
"\"\"2024_omzet\"\":337685,\"\"2024_73\"\":8442241,"
"\"\"2024_opbr7076A\"\":9235672,\"\"2024_bruto9900\"\":0,\"\"2024_pnl\"\":426430,\"\"2024_bedrijfswinst\"\":290502,"
"\"\"2024_equity\"\":6149819,\"\"2024_assets\"\":9314476,"
"\"\"2024_debt\"\":3164657,\"\"2024_cash\"\":567131,\"\"2024_fte\"\":104.2,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":1279291,\"\"2024_76A\"\":143409,"
"\"\"2024_geldbeleggingen\"\":4573112}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Ten Dries YE2025 (70/76A JUMP 9.39m / 73 JUMP 8.65m / pnl DROP 106k / cash DROP 387k / Strong PDF),{EID},VAPH/MFC + leftover city_deinze VAPH,Ten Dries VZW (KBO 0410.571.207; Actief; 1 VE; official zetel Deinze),2026-06-17,2025,2025,9392001,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00212085.pdf,Public VAPH/MFC dual of mined city_deinze,Publish VAPH/VL/PVB/RTH/MFC/gemeente matrix behind omzet 0.36m + 73 8.65m and why pnl DROP 106k while cash DROP 387k,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Deinze>Ten Dries>JR2025_statutory_L5,tick2499; Strong official native PDF; leftover mined city_deinze VAPH/MFC; 1 VE; prior-year identical; NOT Vierklaver remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Ten Dries 70/76A JUMP 9.39m / 73 JUMP 8.65m / pnl DROP 106k / cash DROP 387k (YE2025 leftover city_deinze VAPH/MFC)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Deinze>Ten Dries>JR2025",
"9392001",
"9392001",
"PDF envelope 9392001 = 70/76A because omzet commercial-only vs large 73; omzet70 JUMP 357127; 73 JUMP 8648576; 76A DROP 1666; bedrijfswinst DROP 129620; pnl DROP 106116; equity JUMP 8249399; assets JUMP 12364030; debt JUMP 4114631; FTE 104; kapitaalsubsidies JUMP 3272755; destin691 empty; cash DROP 386799; capex 5258768; leftover city_deinze VAPH/MFC",
"strong",
SRC_PDF,
"VAPH/MFC + leftover city_deinze VAPH",
"VAPH leftover city_deinze",
"9.39m 70/76A; 73 JUMP 8.65m; pnl DROP 106k; cash DROP 387k; leftover city_deinze VAPH/MFC",
"5.50",
"5.40",
"5.10",
"5.44",
"FOI VAPH/VL/PVB/RTH/MFC/gemeente matrix behind omzet 0.36m + 73 8.65m and why pnl DROP 106116 after YE2024 profit 426430 while cash DROP 386799 and capex 5258768 nieuwbouw",
"active",
"",
"tick2499 leftover mined city_deinze VAPH/MFC after leftover-type hunt; 1 VE; prior-year identical; next rq_2500 EVERY-10; NOT Vierklaver remine; NOT leftover city_eeklo via Vierklaver VE; NOT Leieborg remine; NOT Demival remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Deinze>Ten Dries>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / Vlaamse overheid / PVB / RTH / MFC / gemeente Deinze / eigen bijdragen split behind omzet 70 357127 + 73 8648576 (733 8586829) and why pnl DROP 106116 while cash DROP 386799 and capex 5258768 nieuwbouw",
"why_it_matters": "Strong official PDF leftover public VAPH/MFC of mined city_deinze; VOL-VZW envelope 70/76A 9.39m because omzet commercial-only vs large 73; public VAPH/MFC 1 VE (official zetel Deinze); pnl DROP 106k; cash DROP 387k; capex 5.26m nieuwbouw",
"priority": "8",
"recipient_body": "MFC TEN DRIES VZW / Raad van Bestuur",
"recipient_email": "tendries@tendries.be",
"recipient_postal": "Poeldendries 32 9850 Deinze",
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
"notes": "tick2499; ready NOT sent; Strong official native NBB PDF; leftover mined city_deinze VAPH/MFC after leftover-type hunt; 1 VE; prior-year identical; next rq_2500 EVERY-10; off Vierklaver remine; off leftover city_eeklo via Vierklaver VE; off Leieborg remine; off Demival remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")

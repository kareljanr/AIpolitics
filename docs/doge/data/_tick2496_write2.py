from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2496_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_vierklaver_jr2025_nbb_pdf_2496"
EID="vzw_vierklaver_deinze"
GAP="gap_vierklaver_deinze_vaph_matrix_70_76A_13_91m_omzet_commercial_73_jump_11_51m_destin_jump_3_50m_pnl_flip_213k_l5"
COMM="comm_vierklaver_jr2025_statutory_70_76A_13_91m_73_jump_11_51m_destin_jump_3_50m"
LB="lb_vierklaver_7076A_1391m_73_jump_1151m_destin_jump_350m_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":1746754,\"\"2025_73\"\":11513087,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":13914807,\"\"2025_bruto9900\"\":0,"
"\"\"2025_pnl\"\":-213049,\"\"2025_bedrijfswinst\"\":-234486,"
"\"\"2025_equity\"\":6745980,\"\"2025_assets\"\":9723578,\"\"2025_debt\"\":2977598,"
"\"\"2025_fte\"\":138,\"\"2025_kapitaalsubsidies\"\":1894593,\"\"2025_destin691\"\":3500000,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":3450957,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":11379257,\"\"2025_gebouwen22\"\":3623552,"
"\"\"2025_aanbouw27\"\":256647,\"\"2025_66A\"\":4072,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":126525,\"\"2025_overgedragen14\"\":574862,"
"\"\"2025_bestemdefondsen13\"\":4150000,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":688570,\"\"2025_capex\"\":213405,"
"\"\"2025_6408\"\":451333,\"\"2025_74\"\":654966,\"\"2025_9903\"\":-213049,"
"\"\"2024_omzet\"\":1646162,\"\"2024_73\"\":11114718,"
"\"\"2024_opbr7076A\"\":13443065,\"\"2024_bruto9900\"\":0,\"\"2024_pnl\"\":32058,\"\"2024_bedrijfswinst\"\":-2120,"
"\"\"2024_equity\"\":7187755,\"\"2024_assets\"\":9574696,"
"\"\"2024_debt\"\":2386941,\"\"2024_cash\"\":2403820,\"\"2024_fte\"\":134,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":2123319,\"\"2024_76A\"\":9275,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Vierklaver YE2025 (70/76A JUMP 13.91m / 73 JUMP 11.51m / destin JUMP 3.50m / pnl FLIP LOSS 213k / Strong PDF),{EID},VAPH + leftover city_deinze VAPH,De Vierklaver VZW (KBO 0436.015.889; Actief; 6 VE; zetel Deinze),2026-06-15,2025,2025,13914807,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00178582.pdf,Public VAPH dual of mined city_deinze,Publish VAPH/VL/PVB/RTH/gemeente matrix behind 70/76A 13.91m + 73 11.51m and why destin JUMP 3.50m while pnl FLIP LOSS 213k,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Deinze>Vierklaver>JR2025_statutory_L5,tick2496; Strong official native PDF; leftover mined city_deinze VAPH; 6 VE; prior-year identical; NOT leftover city_eeklo; NOT Leieborg remine; NOT Demival remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Vierklaver 70/76A JUMP 13.91m / 73 JUMP 11.51m / destin JUMP 3.50m / pnl FLIP LOSS 213k (YE2025 leftover city_deinze VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Deinze>Vierklaver>JR2025",
"13914807",
"13914807",
"PDF envelope 13914807 = 70/76A VZW because omzet commercial-only vs large 73; omzet 1746754; 73 JUMP 11513087; 76A empty; bedrijfswinst DEEPER LOSS 234486; pnl FLIP LOSS 213049; equity DROP 6745980; assets JUMP 9723578; debt JUMP 2977598; FTE 138; kapitaalsubsidies DROP 1894593; destin691 JUMP 3500000; cash JUMP 3450957; capex 213405; leftover city_deinze VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_deinze VAPH",
"VAPH leftover city_deinze",
"13.91m 70/76A; 73 JUMP 11.51m; destin JUMP 3.50m; pnl FLIP LOSS 213k; leftover city_deinze VAPH",
"5.60",
"5.50",
"5.15",
"5.54",
"FOI VAPH/VL/PVB/RTH/gemeente matrix behind 70/76A 13.91m + 73 11.51m and why destin JUMP 3500000 after YE2024 empty while pnl FLIP LOSS 213049",
"active",
"",
"tick2496 leftover mined city_deinze VAPH after leftover-type hunt; 6 VE; prior-year identical; NOT every-10 (next 2500); NOT leftover city_eeklo; NOT Leieborg remine; NOT Demival remine; NOT Ascendere remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Deinze>Vierklaver>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / Vlaamse overheid / PVB / RTH / MFC / gemeente Deinze / gemeente Maldegem / gemeente Eeklo / eigen bijdragen split behind omzet 70 1746754 + 73 11513087 (733 11485019) and why destin 691 JUMP 3500000 after YE2024 empty while pnl FLIP LOSS 213049",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_deinze; VOL-VZW envelope 70/76A 13.91m because omzet commercial-only vs large 73; public VAPH 6 VE (Deinze x2 + Maldegem x3 + Eeklo); destin JUMP 3.50m; pnl FLIP LOSS",
"priority": "8",
"recipient_body": "De Vierklaver VZW / Raad van Bestuur",
"recipient_email": "secretariaat@de-vierklaver.be",
"recipient_postal": "Haarkenstraat 32 bus A000 9850 Deinze",
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
"notes": "tick2496; ready NOT sent; Strong official native NBB PDF; leftover mined city_deinze VAPH after leftover-type hunt; 6 VE; prior-year identical; NOT every-10 (next 2500); off leftover city_eeklo; off Leieborg remine; off Demival remine; off Ascendere remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")

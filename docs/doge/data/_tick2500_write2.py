from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2500_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_luifel_jr2025_nbb_pdf_2500"
EID="vzw_luifel_tielt"
GAP="gap_luifel_tielt_vaph_matrix_70_76A_1_78m_omzet_commercial_73_jump_1_71m_pnl_drop_20k_l5"
COMM="comm_luifel_jr2025_statutory_70_76A_1_78m_73_jump_1_71m_pnl_drop_20k"
LB="lb_luifel_7076A_178m_73_jump_171m_pnl_drop_20k_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":71267,\"\"2025_73\"\":1711321,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":1782588,\"\"2025_bruto9900\"\":1681424,"
"\"\"2025_pnl\"\":19557,\"\"2025_bedrijfswinst\"\":26431,"
"\"\"2025_equity\"\":683911,\"\"2025_assets\"\":1561492,\"\"2025_debt\"\":877581,"
"\"\"2025_fte\"\":21.4,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":535798,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":1591291,\"\"2025_gebouwen22\"\":960827,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":683911,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":53797,\"\"2025_capex\"\":44199,"
"\"\"2025_6408\"\":5686,\"\"2025_74\"\":0,\"\"2025_9903\"\":19557,"
"\"\"2024_omzet\"\":64190,\"\"2024_73\"\":1623463,"
"\"\"2024_opbr7076A\"\":1687653,\"\"2024_bruto9900\"\":1571265,\"\"2024_pnl\"\":47313,\"\"2024_bedrijfswinst\"\":115382,"
"\"\"2024_equity\"\":664354,\"\"2024_assets\"\":1548971,"
"\"\"2024_debt\"\":884617,\"\"2024_cash\"\":312225,\"\"2024_fte\"\":18.7,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":200000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Luifel YE2025 (70/76A JUMP 1.78m / 73 JUMP 1.71m / pnl DROP 20k / cash JUMP 536k / Strong PDF),{EID},VAPH + leftover city_tielt VAPH,De Luifel VZW (KBO 0434.011.652; Actief; 2 VE; official zetel Tielt),2026-06-17,2025,2025,1782588,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00245078.pdf,Public VAPH dual of mined city_tielt,Publish VAPH/VL/PVB/RTH/gemeente matrix behind omzet 71k + 73 1.71m and why pnl DROP 20k while cash JUMP 536k,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Tielt>De Luifel>JR2025_statutory_L5,tick2500; Strong official native PDF; leftover mined city_tielt VAPH; 2 VE; prior-year identical; NOT De Zonnewende remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"De Luifel 70/76A JUMP 1.78m / 73 JUMP 1.71m / pnl DROP 20k / cash JUMP 536k (YE2025 leftover city_tielt VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Tielt>De Luifel>JR2025",
"1782588",
"1782588",
"PDF envelope 1782588 = 70/76A because omzet commercial-only vs large 73; omzet70 JUMP 71267; 73 JUMP 1711321; 76A empty; bedrijfswinst DROP 26431; pnl DROP 19557; equity JUMP 683911; assets JUMP 1561492; debt DROP 877581; FTE JUMP 21.4; kapitaalsubsidies empty; destin691 empty; cash JUMP 535798; capex 44199; leftover city_tielt VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_tielt VAPH",
"VAPH leftover city_tielt",
"1.78m 70/76A; 73 JUMP 1.71m; pnl DROP 20k; cash JUMP 536k; leftover city_tielt VAPH",
"5.30",
"5.20",
"5.10",
"5.23",
"FOI VAPH/VL/PVB/RTH/gemeente matrix behind omzet 71267 + 73 1711321 and why pnl DROP 19557 after YE2024 profit 47313 while cash JUMP 535798",
"active",
"",
"tick2500 leftover mined city_tielt VAPH after leftover-type hunt; 2 VE; prior-year identical; EVERY-10; next rq_2501 leftover dual; NOT De Zonnewende remine; NOT Mivalti remine; NOT De Harlekijntjes remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Tielt>De Luifel>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / Vlaamse overheid / PVB / RTH / gemeente Tielt / eigen bijdragen split behind omzet 70 71267 + 73 1711321 and why pnl DROP 19557 while cash JUMP 535798",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_tielt; VKT-VZW envelope 70/76A 1.78m because omzet commercial-only vs large 73; public VAPH 2 VE (official zetel Tielt); pnl DROP 20k; cash JUMP 536k",
"priority": "8",
"recipient_body": "DE LUIFEL VZW / Raad van Bestuur",
"recipient_email": "info@deluifel.be",
"recipient_postal": "Tramstraat 42 8700 Tielt",
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
"notes": "tick2500; ready NOT sent; Strong official native NBB PDF; leftover mined city_tielt VAPH after leftover-type hunt; 2 VE; prior-year identical; EVERY-10; next rq_2501 leftover dual; off De Zonnewende remine; off Mivalti remine; off De Harlekijntjes remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")

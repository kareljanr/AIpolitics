from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2503_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_avalon_jr2025_nbb_pdf_2503"
EID="vzw_avalon_buggenhout"
GAP="gap_avalon_buggenhout_vaph_matrix_70_76A_3_56m_omzet_commercial_73_jump_3_10m_pnl_improved_loss_33k_l5"
COMM="comm_avalon_jr2025_statutory_70_76A_3_56m_omzet_commercial_73_jump_3_10m_pnl_improved_loss_33k"
LB="lb_avalon_70_76A_356m_omzet_commercial_73_jump_3_10m_pnl_improved_loss_33k_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":451254,\"\"2025_73\"\":3100234,\"\"2025_76A\"\":6579,"
"\"\"2025_opbr7076A\"\":3558067,\"\"2025_bruto9900\"\":3392631,"
"\"\"2025_pnl\"\":-32618,\"\"2025_bedrijfswinst\"\":-36635,"
"\"\"2025_equity\"\":4344137,\"\"2025_assets\"\":6039963,\"\"2025_debt\"\":1573776,"
"\"\"2025_fte\"\":37.7,\"\"2025_kapitaalsubsidies\"\":1831111,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1086798,\"\"2025_geldbeleggingen\"\":250000,"
"\"\"2025_personnel62\"\":3165200,\"\"2025_gebouwen22\"\":3659056,"
"\"\"2025_aanbouw27\"\":317040,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":1283861,\"\"2025_overgedragen14\"\":373416,"
"\"\"2025_bestemdefondsen13\"\":855749,"
"\"\"2025_voorzieningen16\"\":122050,\"\"2025_630\"\":254913,\"\"2025_capex\"\":119601,"
"\"\"2025_6408\"\":40453,\"\"2025_74\"\":0,\"\"2025_9903\"\":-32618,"
"\"\"2024_omzet\"\":396248,\"\"2024_73\"\":2960163,"
"\"\"2024_opbr7076A\"\":3356411,\"\"2024_bruto9900\"\":3245701,\"\"2024_pnl\"\":-90830,\"\"2024_bedrijfswinst\"\":-89948,"
"\"\"2024_equity\"\":4451022,\"\"2024_assets\"\":6235881,"
"\"\"2024_debt\"\":1631509,\"\"2024_cash\"\":987971,\"\"2024_fte\"\":37,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":1905378,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":250000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Avalon YE2025 (70/76A JUMP 3.56m / omzet commercial vs 73 JUMP 3.10m / pnl IMPROVED LOSS 33k / cash JUMP 1.09m / Strong PDF),{EID},VAPH + leftover city_buggenhout VAPH,Avalon VZW (KBO 0464.778.666; Actief; 1 VE; official zetel Buggenhout),2026-06-22,2025,2025,3558067,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00195078.pdf,Public VAPH dual of mined city_buggenhout,Publish VAPH/gemeente Buggenhout/eigen-bijdrage matrix behind 70/76A 3.56m and why omzet commercial 451k while 73 JUMP 3.10m pnl IMPROVED LOSS 33k and cash JUMP 1.09m,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Buggenhout>Avalon>JR2025_statutory_L5,tick2503; Strong official native PDF; leftover mined city_buggenhout VAPH; 1 VE; prior-year identical; NOT De Heymeulen YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Avalon 70/76A JUMP 3.56m / omzet commercial vs 73 JUMP 3.10m / pnl IMPROVED LOSS 33k / cash JUMP 1.09m (YE2025 leftover city_buggenhout VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Buggenhout>Avalon>JR2025",
"3558067",
"3558067",
"PDF envelope 3558067 = 70+73+76A because VZW omzet 451254 commercial-only vs large 73 JUMP 3100234; 76A JUMP 6579; bruto9900 JUMP 3392631; bedrijfswinst IMPROVED LOSS -36635; pnl IMPROVED LOSS -32618; equity DROP 4344137; assets DROP 6039963; debt DROP 1573776; FTE JUMP 37.7; kapitaalsubsidies DROP 1831111; destin691 empty; cash JUMP 1086798; geldbeleggingen 250000 FLAT; capex 119601; leftover city_buggenhout VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_buggenhout VAPH",
"VAPH leftover city_buggenhout",
"3.56m 70/76A; omzet commercial 451k; 73 JUMP 3.10m; pnl IMPROVED LOSS 33k; cash JUMP 1.09m; leftover city_buggenhout VAPH",
"5.40",
"5.38",
"5.10",
"5.36",
"FOI VAPH/gemeente Buggenhout/eigen-bijdrage matrix behind 70/76A 3558067 and why omzet commercial 451254 while 73 JUMP 3100234 pnl IMPROVED LOSS -32618 and cash JUMP 1086798",
"active",
"",
"tick2503 leftover mined city_buggenhout VAPH after leftover-type hunt; 1 VE; prior-year identical; next rq_2504 leftover dual; next every-10 2510; NOT De Heymeulen YE2024; NOT Hunnegem YE2024; NOT Kinderdagverblijf Sint-Jozef remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Buggenhout>Avalon>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / gemeente Buggenhout / eigen-bijdragen split behind 70/76A 3558067 and why omzet commercial 451254 while 73 JUMP 3100234 pnl IMPROVED LOSS -32618 and cash JUMP 1086798",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_buggenhout; VKT-VZW envelope 70/76A 3.56m because omzet commercial-only vs large 73; public VAPH 1 VE (official zetel Buggenhout); pnl IMPROVED LOSS 33k; cash JUMP 1.09m",
"priority": "8",
"recipient_body": "Avalon VZW / Raad van Bestuur",
"recipient_email": "info@avalon-vzw.be",
"recipient_postal": "Broekstraat 27 9255 Buggenhout",
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
"notes": "tick2503; ready NOT sent; Strong official native NBB PDF; leftover mined city_buggenhout VAPH after leftover-type hunt; 1 VE; prior-year identical; next rq_2504 leftover dual; next every-10 2510; off De Heymeulen YE2024; off Hunnegem YE2024; off Kinderdagverblijf Sint-Jozef remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")

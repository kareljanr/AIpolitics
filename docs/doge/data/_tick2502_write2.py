from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2502_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_sjwetteren_jr2025_nbb_pdf_2502"
EID="vzw_kdv_sint_jozef_wetteren"
GAP="gap_kdv_sint_jozef_wetteren_opgroeien_matrix_bruto_2_13m_omzet_drop_541k_pnl_jump_231k_destin_150k_l5"
COMM="comm_sjwetteren_jr2025_statutory_bruto_2_13m_omzet_drop_541k_pnl_jump_231k"
LB="lb_sjwetteren_bruto_213m_omzet_drop_541k_pnl_jump_231k_destin_150k_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":540560,\"\"2025_73\"\":0,\"\"2025_76A\"\":447,"
"\"\"2025_opbr7076A\"\":541007,\"\"2025_bruto9900\"\":2133695,"
"\"\"2025_pnl\"\":230508,\"\"2025_bedrijfswinst\"\":249335,"
"\"\"2025_equity\"\":2847914,\"\"2025_assets\"\":3855305,\"\"2025_debt\"\":912391,"
"\"\"2025_fte\"\":29.6,\"\"2025_kapitaalsubsidies\"\":1776246,\"\"2025_destin691\"\":150000,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":205430,\"\"2025_geldbeleggingen\"\":813476,"
"\"\"2025_personnel62\"\":1696590,\"\"2025_gebouwen22\"\":2641534,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":115803,\"\"2025_overgedragen14\"\":805865,"
"\"\"2025_bestemdefondsen13\"\":150000,"
"\"\"2025_voorzieningen16\"\":95000,\"\"2025_630\"\":163491,\"\"2025_capex\"\":31803,"
"\"\"2025_6408\"\":4279,\"\"2025_74\"\":0,\"\"2025_9903\"\":230508,"
"\"\"2024_omzet\"\":572365,\"\"2024_73\"\":0,"
"\"\"2024_opbr7076A\"\":572365,\"\"2024_bruto9900\"\":2081000,\"\"2024_pnl\"\":144192,\"\"2024_bedrijfswinst\"\":157809,"
"\"\"2024_equity\"\":2704254,\"\"2024_assets\"\":3645241,"
"\"\"2024_debt\"\":865987,\"\"2024_cash\"\":678059,\"\"2024_fte\"\":26.6,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":1863094,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf Sint-Jozef YE2025 (bruto JUMP 2.13m / omzet DROP 541k / pnl JUMP 231k / destin JUMP 150k / cash DROP 473k / Strong PDF),{EID},CIK + leftover city_wetteren CIK,Kinderdagverblijf Sint-Jozef VZW (KBO 0408.475.314; Actief; 2 VE; official zetel Wetteren),2026-06-04,2025,2025,2133695,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00174836.pdf,Public CIK dual of mined city_wetteren,Publish Opgroeien/Kind en Gezin/gemeente Wetteren/ouder matrix behind bruto 2.13m and why omzet DROP 541k while pnl JUMP 231k destin JUMP 150k and cash DROP 473k,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Wetteren>Kinderdagverblijf Sint-Jozef>JR2025_statutory_L5,tick2502; Strong official native PDF; leftover mined city_wetteren CIK; 2 VE; prior-year identical; NOT AGB Wetteren remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Kinderdagverblijf Sint-Jozef bruto JUMP 2.13m / omzet DROP 541k / pnl JUMP 231k / destin JUMP 150k / cash DROP 473k (YE2025 leftover city_wetteren CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Wetteren>Kinderdagverblijf Sint-Jozef>JR2025",
"2133695",
"2133695",
"PDF envelope 2133695 = bruto 9900 because VKT 73 empty and bruto much larger than omzet 540560 DROP; 76A JUMP 447; 70/76A 541007; bedrijfswinst JUMP 249335; pnl JUMP 230508; equity JUMP 2847914; assets JUMP 3855305; debt JUMP 912391; FTE JUMP 29.6; kapitaalsubsidies DROP 1776246; destin691 JUMP 150000; cash DROP 205430; geldbeleggingen JUMP 813476; capex 31803; leftover city_wetteren CIK",
"strong",
SRC_PDF,
"CIK + leftover city_wetteren CIK",
"CIK leftover city_wetteren",
"2.13m bruto; omzet DROP 541k; pnl JUMP 231k; destin JUMP 150k; cash DROP 473k; leftover city_wetteren CIK",
"5.62",
"5.60",
"5.20",
"5.58",
"FOI Opgroeien/Kind en Gezin/gemeente Wetteren/ouder matrix behind bruto 2133695 and why omzet DROP 540560 while pnl JUMP 230508 destin JUMP 150000 and cash DROP 205430 (geldbeleggingen JUMP 813476)",
"active",
"",
"tick2502 leftover mined city_wetteren CIK after leftover-type hunt; 2 VE; prior-year identical; next rq_2503 leftover dual; next every-10 2510; NOT AGB Wetteren remine; NOT Trianval remine; NOT Zorg-Saam leftover-via-VE; NOT leftover city_buggenhout; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Wetteren>Kinderdagverblijf Sint-Jozef>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien / Kind en Gezin / gemeente Wetteren / ouderbijdragen split behind bruto 9900 2133695 and why omzet DROP 540560 while pnl JUMP 230508 destin JUMP 150000 and cash DROP 205430 (geldbeleggingen JUMP 813476)",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_wetteren; VKT-VZW envelope bruto 9900 2.13m because 73 empty and bruto much larger than omzet; public CIK 2 VE (official zetel Wetteren); pnl JUMP 231k; destin JUMP 150k; cash DROP 473k",
"priority": "8",
"recipient_body": "Kinderdagverblijf Sint-Jozef VZW / Raad van Bestuur",
"recipient_email": "karen.meirlaen@kinderdagverblijfsintjozef.be",
"recipient_postal": "Wegvoeringstraat 61 9230 Wetteren",
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
"notes": "tick2502; ready NOT sent; Strong official native NBB PDF; leftover mined city_wetteren CIK after leftover-type hunt; 2 VE; prior-year identical; next rq_2503 leftover dual; next every-10 2510; off AGB Wetteren remine; off Trianval remine; off Zorg-Saam leftover-via-VE; off leftover city_buggenhout; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")

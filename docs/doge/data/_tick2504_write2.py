from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2504_stamp.txt").read_text().strip().splitlines()
SRC_PDF="src_hunnegem_jr2025_nbb_pdf_2504"
EID="vzw_hunnegem_herzele"
GAP="gap_hunnegem_herzele_wzc_matrix_bruto_2_39m_omzet73_empty_pnl_jump_148k_cash_drop_921k_l5"
COMM="comm_hunnegem_jr2025_statutory_bruto_2_39m_omzet73_empty_pnl_jump_148k_cash_drop_921k"
LB="lb_hunnegem_bruto_239m_omzet73_empty_pnl_jump_148k_cash_drop_921k_jr2025"

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":0,\"\"2025_bruto9900\"\":2386211,"
"\"\"2025_pnl\"\":147610,\"\"2025_bedrijfswinst\"\":72121,"
"\"\"2025_equity\"\":1780022,\"\"2025_assets\"\":2368480,\"\"2025_debt\"\":588458,"
"\"\"2025_fte\"\":35.3,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":491327,\"\"2025_geldbeleggingen\"\":1000000,"
"\"\"2025_personnel62\"\":2268308,\"\"2025_gebouwen22\"\":65029,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,\"\"2025_66B\"\":3229,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":1780022,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":44463,\"\"2025_capex\"\":11872,"
"\"\"2025_6408\"\":1319,\"\"2025_74\"\":0,\"\"2025_9903\"\":147610,\"\"2025_76B\"\":79454,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr7076A\"\":0,\"\"2024_bruto9900\"\":2117050,\"\"2024_pnl\"\":10661,\"\"2024_bedrijfswinst\"\":-21551,"
"\"\"2024_equity\"\":1632412,\"\"2024_assets\"\":2033743,"
"\"\"2024_debt\"\":401331,\"\"2024_cash\"\":1412310,\"\"2024_fte\"\":31.3,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Hunnegem YE2025 (bruto JUMP 2.39m / omzet73 empty / pnl JUMP 148k / cash DROP 921k / Strong PDF),{EID},WZC + leftover city_herzele WZC,Hunnegem VZW (KBO 0808.756.504; Actief; 2 VE; official zetel Herzele),2026-06-30,2025,2025,2386211,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00302624.pdf,Public WZC dual of mined city_herzele,Publish RIZIV/VL zorgkas/gemeente Herzele/eigen-bijdrage matrix behind bruto 2.39m and why omzet73 empty while pnl JUMP 148k and cash DROP 921k with geldbeleggingen JUMP 1.00m,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Herzele>Hunnegem>JR2025_statutory_L5,tick2504; Strong official native PDF; leftover mined city_herzele WZC; 2 VE; prior-year identical; NOT De Heymeulen still YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Hunnegem bruto JUMP 2.39m / omzet73 empty / pnl JUMP 148k / cash DROP 921k (YE2025 leftover city_herzele WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Herzele>Hunnegem>JR2025",
"2386211",
"2386211",
"PDF envelope bruto9900 2386211 JUMP because VKT omzet70+73 empty; 76A empty; bedrijfswinst FLIP PROFIT 72121; pnl JUMP 147610; equity JUMP 1780022; assets JUMP 2368480; debt JUMP 588458; FTE JUMP 35.3; kapitaalsubsidies empty; destin691 empty; cash DROP 491327; geldbeleggingen JUMP 1000000; capex 11872; leftover city_herzele WZC",
"strong",
SRC_PDF,
"WZC + leftover city_herzele WZC",
"WZC leftover city_herzele",
"2.39m bruto; omzet73 empty; pnl JUMP 148k; cash DROP 921k; geldbeleggingen JUMP 1.00m; leftover city_herzele WZC",
"5.40",
"5.20",
"5.10",
"5.28",
"FOI RIZIV/VL zorgkas/gemeente Herzele/eigen-bijdrage matrix behind bruto 2386211 and why omzet73 empty while pnl JUMP 147610 and cash DROP 491327 with geldbeleggingen JUMP 1000000",
"active",
"",
"tick2504 leftover mined city_herzele WZC after Re-HEAD YE2024->YE2025; 2 VE; prior-year identical; next rq_2505 leftover dual; next every-10 2510; NOT De Heymeulen still YE2024; NOT Avalon remine; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT Meredal/Avondzon remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Herzele>Hunnegem>WZC",
"entity_id": EID,
"what_is_missing": "RIZIV / VL zorgkas / gemeente Herzele / eigen-bijdragen split behind bruto 2386211 and why omzet73 empty while pnl JUMP 147610 and cash DROP 491327 with geldbeleggingen JUMP 1000000",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_herzele; VKT-VZW envelope bruto 2.39m because omzet73 empty; public WZC 2 VE (official zetel Herzele); pnl JUMP 148k; cash DROP 921k",
"priority": "8",
"recipient_body": "Hunnegem VZW / Raad van Bestuur",
"recipient_email": "wzc.ocmwterleen@herzele.be",
"recipient_postal": "Lindestraat 33 9550 Herzele",
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
"notes": "tick2504; ready NOT sent; Strong official native NBB PDF; leftover mined city_herzele WZC after Re-HEAD YE2024->YE2025; 2 VE; prior-year identical; next rq_2505 leftover dual; next every-10 2510; off De Heymeulen still YE2024; off Avalon remine; off WZC Sint-Vincentius Erpe-Mere YE2024; off Meredal/Avondzon remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE2 DONE")

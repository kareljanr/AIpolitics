from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2516_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_honighsdries_scherpenheuvel_jr2025_nbb_pdf_2516"
EID = "vzw_honighsdries_scherpenheuvel"
GAP = "gap_honighsdries_scherpenheuvel_wzc_matrix_bruto_6_31m_omzet73_empty_pnl_jump_127k_cash_jump_878k_l5"
COMM = "comm_honighsdries_scherpenheuvel_jr2025_statutory_bruto_6_31m_omzet73_empty_pnl_jump_127k_cash_jump_878k"
LB = "lb_honighsdries_scherpenheuvel_bruto_6_31m_omzet73_empty_pnl_jump_127k_cash_jump_878k_jr2025"

def append_rows(path, rows, fieldnames):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} no LF")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", lineterminator="\n")
        for row in rows:
            w.writerow(row)
    print("appended", len(rows), "->", path.name)

cash = {
    "2025_omzet": 0, "2025_73": 0, "2025_76A": 0,
    "2025_opbr7076A": 0, "2025_bruto9900": 6311576,
    "2025_pnl": 126816, "2025_bedrijfswinst": 170450, "2025_9903": 126816,
    "2025_equity": -113700, "2025_assets": 3990698, "2025_debt": 4104398,
    "2025_fte": 80.5, "2025_fte9087": 80.5, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 877928, "2025_geldbeleggingen": 1893976,
    "2025_personnel62": 6050220, "2025_gebouwen22": 0,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_fondsen10": 0,
    "2025_overgedragen14": -113700, "2025_voorzieningen16": 0,
    "2025_630": 81997, "2025_capex": 76053,
    "2025_6408": 8909, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 425,
    "2024_pnl": 57161, "2024_bedrijfswinst": 177484,
    "2024_equity": -240516, "2024_assets": 3822651, "2024_debt": 4063166,
    "2024_cash": 842088, "2024_fte": 83, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 1808361,
    "2024_74": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Huyze Honighsdries YE2025 (bruto JUMP 6.31m / omzet73 empty / pnl JUMP 127k / cash JUMP 878k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg + RIZIV + leftover city_scherpenheuvel_zichem leftover WZC",
    "legal_basis": "Huyze Honighsdries VZW (KBO 0891.481.666; Actief; 1 VE; official zetel Scherpenheuvel-Zichem; CoBRHA HCO 22558)",
    "decision_date": "2026-06-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "6311576",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00393713.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_scherpenheuvel_zichem",
    "cut_option": "Publish Departement Zorg / RIZIV / Scherpenheuvel-Zichem matrix behind bruto 6.31m and why omzet73 empty while pnl JUMP 127k and equity still negative -114k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>HuyzeHonighsdries>JR2025_statutory_L5",
    "notes": "tick2516; Strong official native PDF; leftover mined city_scherpenheuvel_zichem leftover WZC; 1 VE; prior-year identical; NOT WZC Voortberg Armonea; NOT leftover VAPH Huize Levensruimte; NOT De Vlaspit leftover maatwerk@2515; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Huyze Honighsdries bruto JUMP 6.31m / omzet73 empty / pnl JUMP 127k / cash JUMP 878k (YE2025 leftover city_scherpenheuvel_zichem leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>HuyzeHonighsdries>JR2025",
    "annual_cost_eur": "6311576",
    "total_cost_eur": "6311576",
    "tco_notes": "PDF envelope bruto9900 6311576 JUMP because VKT and 73 empty and bruto >> omzet; 70 empty; 73 empty; 76A empty DROP was 425; bedrijfswinst DROP 170450; pnl JUMP 126816; equity JUMP -113700 still negative; assets JUMP 3990698; debt JUMP 4104398; FTE DROP 80.5; kapitaalsubsidies empty; destin691 empty; cash JUMP 877928; geldbeleggingen JUMP 1893976; leftover city_scherpenheuvel_zichem leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg + RIZIV + leftover city_scherpenheuvel_zichem leftover WZC",
    "stated_goal": "leftover WZC leftover city_scherpenheuvel_zichem",
    "measured_outcome": "6.31m bruto JUMP; omzet73 empty; pnl JUMP 127k; cash JUMP 878k; leftover city_scherpenheuvel_zichem leftover WZC",
    "absurdity_score": "5.32",
    "cost_score": "5.42",
    "difficulty": "5.10",
    "priority_index": "5.34",
    "cut_proposal": "FOI Departement Zorg / RIZIV / gemeente Scherpenheuvel-Zichem matrix behind bruto 6311576 and why omzet73 empty while pnl JUMP 126816 and equity still negative -113700 with 17 FLAT 1000000",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2516 leftover mined city_scherpenheuvel_zichem leftover WZC after leftover maatwerk De Vlaspit@2515; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2517 leftover dual; NOT WZC Voortberg Armonea; NOT leftover VAPH Huize Levensruimte; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>HuyzeHonighsdries>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / gemeente Scherpenheuvel-Zichem split behind bruto 6311576 and why omzet73 empty while pnl JUMP 126816 and equity still negative -113700 with 17 FLAT 1000000",
    "why_it_matters": "Strong official PDF leftover WZC of mined city_scherpenheuvel_zichem; VKT-VZW envelope bruto 6.31m because 73 empty and bruto >> omzet; leftover WZC 1 VE official zetel Scherpenheuvel-Zichem; pnl JUMP 127k / cash JUMP 878k / equity still negative -114k",
    "priority": "8",
    "recipient_body": "Huyze Honighsdries VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "postbus@huyzehonighsdries.be",
    "recipient_postal": "Prins De Merodelaan 1 3271 Scherpenheuvel-Zichem",
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
    "notes": "tick2516; ready NOT sent; Strong official native NBB PDF; leftover mined city_scherpenheuvel_zichem leftover WZC after leftover maatwerk De Vlaspit@2515; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2517 leftover dual; off WZC Voortberg Armonea; off leftover VAPH Huize Levensruimte; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

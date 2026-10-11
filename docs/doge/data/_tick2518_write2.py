from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2518_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_schommel_scherpenheuvel_jr2025_nbb_pdf_2518"
EID = "vzw_schommel_scherpenheuvel"
GAP = "gap_schommel_scherpenheuvel_cik_matrix_70_76A_6_34m_73_jump_6_19m_pnl_drop_265k_cash_jump_1_02m_l5"
COMM = "comm_schommel_scherpenheuvel_jr2025_statutory_70_76A_6_34m_73_jump_6_19m_pnl_drop_265k_cash_jump_1_02m"
LB = "lb_schommel_scherpenheuvel_70_76A_6_34m_73_jump_6_19m_pnl_drop_265k_cash_jump_1_02m_jr2025"

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
    "2025_omzet": 47971, "2025_73": 6186326, "2025_76A": 9000,
    "2025_opbr7076A": 6341052, "2025_bruto9900": 0,
    "2025_pnl": 265345, "2025_bedrijfswinst": 269556, "2025_9903": 265345,
    "2025_equity": 4000132, "2025_assets": 5526522, "2025_debt": 1260751,
    "2025_fte": 63, "2025_fte9087": 63, "2025_kapitaalsubsidies": 40622,
    "2025_destin691": 66337, "2025_791": 0,
    "2025_cash": 1022183, "2025_geldbeleggingen": 0,
    "2025_personnel62": 5177863, "2025_gebouwen22": 3543082,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_fondsen10": 51976,
    "2025_overgedragen14": 2808070, "2025_voorzieningen16": 265638,
    "2025_630": 171859, "2025_capex": 132494,
    "2025_6408": 26152, "2025_74": 97755, "2025_733": 6145696,
    "2024_omzet": 42646, "2024_73": 5859726, "2024_76A": 0,
    "2024_pnl": 410752, "2024_bedrijfswinst": 401717,
    "2024_equity": 3735853, "2024_assets": 4904805, "2024_debt": 961010,
    "2024_cash": 470483, "2024_fte": 60.6, "2024_destin691": 148438,
    "2024_kapitaalsubsidies": 41689, "2024_geldbeleggingen": 0,
    "2024_74": 81958,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Schommel YE2025 (70/76A JUMP 6.34m / 73 JUMP 6.19m / pnl DROP 265k / cash JUMP 1.02m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Opgroeien + leftover city_scherpenheuvel_zichem leftover CIK",
    "legal_basis": "De Schommel VZW (KBO 0462.203.119; Actief; 2 VE; official zetel Scherpenheuvel-Zichem; RSZ2025 87.991)",
    "decision_date": "2026-06-11",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "6341052",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00270709.pdf",
    "stated_goal": "Public leftover CIK dual of mined city_scherpenheuvel_zichem",
    "cut_option": "Publish Opgroeien / CKG / Scherpenheuvel-Zichem matrix behind 70/76A 6.34m and why omzet commercial-only while 73 JUMP 6.19m pnl DROP 265k and cash JUMP 1.02m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>DeSchommel>JR2025_statutory_L5",
    "notes": "tick2518; Strong official native PDF; leftover mined city_scherpenheuvel_zichem leftover CIK; 2 VE; 1 VE Tienen is VE of SZ-seated parent; site Leuven not a KBO VE; prior-year identical; NOT leftover VAPH Huize Levensruimte@2517; NOT leftover WZC Huyze Honighsdries@2516; NOT leftover maatwerk De Vlaspit@2515; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Schommel 70/76A JUMP 6.34m / 73 JUMP 6.19m / pnl DROP 265k / cash JUMP 1.02m (YE2025 leftover city_scherpenheuvel_zichem leftover CIK)",
    "level": "L5",
    "type": "cik_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>DeSchommel>JR2025",
    "annual_cost_eur": "6341052",
    "total_cost_eur": "6341052",
    "tco_notes": "PDF envelope 70/76A 6341052 JUMP because VZW and omzet commercial-only vs large 73; 70 47971 JUMP; 73 6186326 JUMP; 76A 9000 JUMP; bedrijfswinst DROP 269556; pnl DROP 265345; equity JUMP 4000132; assets JUMP 5526522; debt JUMP 1260751; FTE JUMP 63; kapitaalsubsidies DROP 40622; destin691 DROP 66337; cash JUMP 1022183; leftover city_scherpenheuvel_zichem leftover CIK",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Opgroeien + leftover city_scherpenheuvel_zichem leftover CIK",
    "stated_goal": "leftover CIK leftover city_scherpenheuvel_zichem",
    "measured_outcome": "6.34m 70/76A JUMP; 73 JUMP 6.19m; pnl DROP 265k; cash JUMP 1.02m; leftover city_scherpenheuvel_zichem leftover CIK",
    "absurdity_score": "5.44",
    "cost_score": "5.33",
    "difficulty": "5.10",
    "priority_index": "5.37",
    "cut_proposal": "FOI Opgroeien / CKG / gemeente Scherpenheuvel-Zichem matrix behind 70/76A 6341052 and why omzet commercial-only while 73 JUMP 6186326 pnl DROP 265345 and cash JUMP 1022183 with debt JUMP 1260751",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2518 leftover mined city_scherpenheuvel_zichem leftover CIK after leftover VAPH Huize Levensruimte@2517 + leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; 2 VE; 1 VE Tienen is VE of SZ-seated parent; site Leuven not a KBO VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2519 leftover dual; NOT leftover VAPH Huize Levensruimte; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Wonozo leftover jeugdhulp",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>DeSchommel>leftover_cik",
    "entity_id": EID,
    "what_is_missing": "Opgroeien / CKG / gemeente Scherpenheuvel-Zichem split behind 70/76A 6341052 and why omzet commercial-only while 73 JUMP 6186326 pnl DROP 265345 and cash JUMP 1022183 with debt JUMP 1260751",
    "why_it_matters": "Strong official PDF leftover CIK of mined city_scherpenheuvel_zichem; VOL-VZW envelope 70/76A 6.34m because omzet commercial-only vs large 73; leftover CIK 2 VE official zetel Scherpenheuvel-Zichem; pnl DROP 265k / cash JUMP 1.02m / debt JUMP 1.26m",
    "priority": "8",
    "recipient_body": "De Schommel VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "averbode@deschommel.org",
    "recipient_postal": "Westelsebaan 108 3271 Scherpenheuvel-Zichem",
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
    "notes": "tick2518; ready NOT sent; Strong official native NBB PDF; leftover mined city_scherpenheuvel_zichem leftover CIK after leftover VAPH Huize Levensruimte@2517 + leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; 2 VE; 1 VE Tienen is VE of SZ-seated parent; site Leuven not a KBO VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2519 leftover dual; off leftover VAPH Huize Levensruimte; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine; off Wonozo leftover jeugdhulp",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

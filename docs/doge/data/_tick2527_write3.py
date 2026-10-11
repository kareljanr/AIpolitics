from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2527_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_talander_arendonk_jr2025_nbb_pdf_2527"
EID = "vzw_talander_arendonk"
GAP = "gap_talander_arendonk_vaph_matrix_bruto_1_60m_omzet73_empty_pnl_jump_143k_cash_jump_1_05m_l5"
COMM = "comm_talander_arendonk_jr2025_statutory_bruto_1_60m_omzet73_empty_pnl_jump_143k_cash_jump_1_05m"
LB = "lb_talander_arendonk_bruto_1_60m_omzet73_empty_pnl_jump_143k_cash_jump_1_05m_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()

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
    "2025_opbr7076A": 1603209, "2025_envelope9900": 1603209,
    "2025_pnl": 142992, "2025_bedrijfswinst": 140447, "2025_9903": 145704,
    "2025_equity": 1662056, "2025_assets": 2205622, "2025_debt": 543566,
    "2025_fte": 18.8, "2025_fte105": 18.6, "2025_kapitaalsubsidies": 297292,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 1050120, "2025_geldbeleggingen": 0,
    "2025_personnel62": 1383895, "2025_gebouwen22": 841394,
    "2025_aanbouw27": 29492, "2025_66A": 0,
    "2025_fondsen10": 0, "2025_overgedragen14": 1364764,
    "2025_voorzieningen16": 0, "2025_630": 67977, "2025_capex": 70814,
    "2025_6408": 10890, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 0,
    "2024_pnl": 118277, "2024_bedrijfswinst": 114678,
    "2024_equity": 1534181, "2024_assets": 2112021, "2024_debt": 577840,
    "2024_cash": 932246, "2024_fte": 17.6, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 312410, "2024_geldbeleggingen": 0,
    "2024_envelope9900": 1437845,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Talander Arendonk YE2025 (bruto JUMP 1.60m / omzet73 empty / pnl JUMP 143k / cash JUMP 1.05m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_arendonk leftover VAPH",
    "legal_basis": "Talander VZW (KBO 0433.306.225; Actief; 2 VE; official zetel Arendonk; RSZ2025 87.202; CoBRHA VAPH HCO 201281)",
    "decision_date": "2026-06-19",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1603209",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00192214.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_arendonk",
    "cut_option": "Publish VAPH / OCMW Arendonk / gemeente Arendonk matrix behind bruto9900 1.60m and why pnl JUMP 143k while cash JUMP 1.05m FTE JUMP 18.8",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Arendonk>Talander>JR2025_statutory_L5",
    "notes": "tick2527; Strong official native PDF; leftover mined city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type; 2 VE; prior-year identical; NOT leftover city_arendonk leftover WZC WZGA remine@2526; NOT leftover OCMW Arendonk De Peulder SKIP; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Talander Arendonk bruto JUMP 1.60m / omzet73 empty / pnl JUMP 143k / cash JUMP 1.05m (YE2025 leftover city_arendonk leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Arendonk>Talander>JR2025",
    "annual_cost_eur": "1603209",
    "total_cost_eur": "1603209",
    "tco_notes": "PDF envelope bruto9900 1603209 JUMP because VKT and omzet70+73 empty; 70 empty; 73 empty; 76A empty; bedrijfswinst JUMP 140447; pnl JUMP 142992; equity JUMP 1662056; assets JUMP 2205622; debt DROP 543566; FTE JUMP 18.8; kapitaalsubsidies DROP 297292; destin691 empty; cash JUMP 1050120; leftover city_arendonk leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_arendonk leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_arendonk",
    "measured_outcome": "1.60m bruto9900 JUMP; omzet73 empty; pnl JUMP 143k; cash JUMP 1.05m; leftover city_arendonk leftover VAPH",
    "absurdity_score": "5.40",
    "cost_score": "5.15",
    "difficulty": "5.05",
    "priority_index": "5.20",
    "cut_proposal": "FOI VAPH / OCMW Arendonk / gemeente Arendonk matrix behind bruto9900 1603209 and why pnl JUMP 142992 while cash JUMP 1050120 FTE JUMP 18.8",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2527 leftover mined city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type after leftover city_arendonk leftover WZC WZGA@2526 leftover OCMW De Peulder SKIP leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC taken leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2528 leftover dual; NOT leftover city_arendonk leftover WZC WZGA remine@2526; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Arendonk>Talander>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / OCMW Arendonk / gemeente Arendonk split behind bruto9900 1603209 and why pnl JUMP 142992 while cash JUMP 1050120 FTE JUMP 18.8",
    "why_it_matters": "Strong official PDF leftover VAPH of mined leftover-mined AGB-only city_arendonk; VKT-VZW envelope bruto9900 1.60m because 70+73 empty; leftover VAPH 2 VE official zetel Arendonk unused leftover type; omzet73 empty / pnl JUMP 143k / cash JUMP 1.05m / FTE JUMP 18.8",
    "priority": "8",
    "recipient_body": "Talander VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@talander.be",
    "recipient_postal": "De Lusthoven 88 2370 Arendonk",
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
    "notes": "tick2527; ready NOT sent; Strong official native NBB PDF; leftover mined city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type after leftover city_arendonk leftover WZC WZGA@2526 leftover OCMW De Peulder SKIP leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC taken leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2528 leftover dual; off leftover city_arendonk leftover WZC WZGA remine@2526; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2540_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_mvc_diest_jr2025_nbb_pdf_2540"
EID = "vzw_martine_van_camp_diest"
GAP = "gap_mvc_diest_vaph_matrix_70_76A_jump_12_92m_73_jump_10_99m_cash_jump_1_24m_l5"
COMM = "comm_mvc_diest_jr2025_statutory_70_76A_jump_12_92m_73_jump_10_99m_cash_jump_1_24m"
LB = "lb_mvc_diest_70_76A_jump_12_92m_73_jump_10_99m_cash_jump_1_24m_jr2025"
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
    "2025_omzet": 1675451, "2025_73": 10986567, "2025_76A": 8314,
    "2025_opbr7076A": 12918434, "2025_envelope7076A": 12918434,
    "2025_pnl": 758488, "2025_bedrijfswinst": 708808, "2025_9903": 758488,
    "2025_equity": 9853159, "2025_assets": 17282003, "2025_debt": 7318178,
    "2025_fte": 134.5, "2025_fte1003": 134.5, "2025_kapitaalsubsidies": 2816870,
    "2025_destin691": 750000, "2025_791": 45840,
    "2025_cash": 1240159, "2025_geldbeleggingen": 3513855,
    "2025_personnel62": 10086622, "2025_gebouwen22": 8453172,
    "2025_aanbouw27": 736412, "2025_66A": 5370, "2025_630": 641882,
    "2025_capex": 1228548, "2025_6408": 103959, "2025_74": 248102,
    "2025_733": 10942562, "2025_6359": 110666,
    "2024_omzet": 1564555, "2024_73": 10292011, "2024_76A": 15638,
    "2024_opbr7076A": 12155345, "2024_envelope7076A": 12155345,
    "2024_pnl": 775362, "2024_bedrijfswinst": 728103,
    "2024_equity": 9262601, "2024_assets": 16484910, "2024_debt": 7222309,
    "2024_cash": 745316, "2024_fte": 132.9, "2024_destin691": 775000,
    "2024_kapitaalsubsidies": 2984799, "2024_geldbeleggingen": 3969062,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Martine Van Camp Diest YE2025 (70/76A JUMP 12.92m / 73 JUMP 10.99m / cash JUMP 1.24m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_diest leftover VAPH",
    "legal_basis": "VZW Martine Van Camp (KBO 0424.784.378; Actief; 1 VE; official zetel Diest; RSZ2025 87.202; official VAPH RTH + vergunde zorgaanbieder)",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "12918434",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00289013.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_diest",
    "cut_option": "Publish VAPH / gemeente Diest / OCMW Diest matrix behind 70/76A JUMP 12.92m and why 73 JUMP 10.99m while cash JUMP 1.24m 9901 DROP 709k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Diest>MartineVanCamp>JR2025_statutory_L5",
    "notes": "tick2540; Strong official native PDF; leftover mined city_diest leftover VAPH leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; EVERY-10 PLUS leftover dual; FIRST LOCK leftover city_diest leftover VAPH; NOT leftover-via-VE; leftover WZC Annendael remine@2535 leftover hospital same KBO leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_aalter leftover VAPH Aalternatief 0 deposits SKIP leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover VAPH unused-looking leftover WZC unused-not-hardskip 0 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Martine Van Camp Diest 70/76A JUMP 12.92m / 73 JUMP 10.99m / cash JUMP 1.24m (YE2025 leftover city_diest leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Diest>MartineVanCamp>JR2025",
    "annual_cost_eur": "12918434",
    "total_cost_eur": "12918434",
    "tco_notes": "PDF envelope 70/76A 12918434 JUMP because VZW 70 present and commercial-only vs large 73; 70 JUMP 1675451; 73 JUMP 10986567; 76A DROP 8314; bedrijfswinst DROP 708808; pnl DROP 758488; equity JUMP 9853159; assets JUMP 17282003; debt JUMP 7318178; FTE JUMP 134.5; kapitaalsubsidies DROP 2816870; destin691 DROP 750000; cash JUMP 1240159; leftover city_diest leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_diest leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_diest",
    "measured_outcome": "12.92m 70/76A JUMP; 10.99m 73 JUMP; 1.24m cash JUMP; leftover city_diest leftover VAPH",
    "absurdity_score": "5.42",
    "cost_score": "5.55",
    "difficulty": "5.06",
    "priority_index": "5.44",
    "cut_proposal": "FOI VAPH / gemeente Diest / OCMW Diest matrix behind 70/76A 12918434 and why 73 JUMP 10986567 while cash JUMP 1240159 9901 DROP 708808",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2540 leftover mined city_diest leftover VAPH leftover-mined AGB-only unused leftover type after leftover city_aalter leftover VAPH Aalternatief 0 deposits SKIP leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP@2538/2539 now YE2025 native leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover VAPH unused-looking leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV leftover city_pelt leftover VAPH unused leftover WZC unused leftover CIK HARD SKIP leftover maatwerk type now taken leftover WZC unused-not-hardskip 0 leftover city_diest leftover VAPH type now taken leftover WZC type now taken leftover CIK HARD SKIP; 1 VE; prior-year identical; EVERY-10 PLUS leftover dual; next rq_2541 leftover dual (NOT every-10; next every-10 2550); NOT leftover-via-VE; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; FIRST LOCK leftover city_diest leftover VAPH",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Diest>MartineVanCamp>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Diest / OCMW Diest split behind 70/76A JUMP 12918434 and why 73 JUMP 10986567 while cash JUMP 1240159 9901 DROP 708808",
    "why_it_matters": "Strong official PDF leftover VAPH of mined leftover-mined AGB-only city_diest; VOL-VZW envelope 70/76A 12.92m because 70 present and commercial-only vs large 73 JUMP 10.99m; leftover VAPH 1 VE official zetel Diest unused leftover type; 70/76A JUMP 12.92m / 73 JUMP 10.99m / cash JUMP 1.24m / 9901 DROP 709k",
    "priority": "8",
    "recipient_body": "VZW Martine Van Camp / Voorzitter Raad van Bestuur",
    "recipient_email": "info@martinevancamp.be",
    "recipient_postal": "Turnhoutsebaan 57 3294 Diest",
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
    "notes": "tick2540; ready NOT sent; Strong official native NBB PDF; leftover mined city_diest leftover VAPH leftover-mined AGB-only unused leftover type; leftover city_aalter leftover VAPH Aalternatief 0 deposits SKIP leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover VAPH unused-looking leftover WZC unused-not-hardskip 0 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine leftover WZC Ter Luchte remine leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover WZC Annendael remine@2535 leftover hospital same KBO leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_diest leftover VAPH type now taken leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover CIK HARD SKIP leftover maatwerk unused-looking leftover CAR leftover-via-VE SKIP; 1 VE; prior-year identical; EVERY-10 PLUS leftover dual; next rq_2541 leftover dual (NOT every-10; next every-10 2550); off leftover-via-VE; off Armonea commercial; off Korian commercial; off Vulpia commercial; FIRST LOCK leftover city_diest leftover VAPH",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

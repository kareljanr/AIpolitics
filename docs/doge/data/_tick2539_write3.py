from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2539_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_nloa_pelt_jr2025_nbb_pdf_2539"
EID = "vzw_nloa_pelt"
GAP = "gap_nloa_pelt_maatwerk_matrix_bruto_jump_2_49m_9901_drop_55k_pnl_drop_63k_cash_jump_362k_l5"
COMM = "comm_nloa_pelt_jr2025_statutory_bruto_jump_2_49m_9901_drop_55k_pnl_drop_63k_cash_jump_362k"
LB = "lb_nloa_pelt_bruto_jump_2_49m_9901_drop_55k_pnl_drop_63k_cash_jump_362k_jr2025"
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
    "2025_omzet": 0, "2025_73": 0, "2025_76A": 12640,
    "2025_envelope9900": 2492647, "2025_pnl": 187972, "2025_bedrijfswinst": 204001,
    "2025_9903": 187972, "2025_equity": 1138826, "2025_assets": 2231233,
    "2025_debt": 1092407, "2025_fte": 55, "2025_kapitaalsubsidies": 80775,
    "2025_destin691": 0, "2025_791": 0, "2025_cash": 831185,
    "2025_geldbeleggingen": 0, "2025_personnel62": 2100801, "2025_gebouwen22": 465100,
    "2025_aanbouw27": 0, "2025_66A": 2474, "2025_630": 163222, "2025_capex": 373330,
    "2025_6408": 22149, "2025_leasing25": 223009, "2025_lt17": 310241,
    "2024_omzet": 0, "2024_73": 0, "2024_envelope9900": 2272999,
    "2024_pnl": 250684, "2024_bedrijfswinst": 258566, "2024_equity": 970537,
    "2024_assets": 1722092, "2024_debt": 751555, "2024_cash": 468647,
    "2024_fte": 47.8, "2024_destin691": 0, "2024_kapitaalsubsidies": 101052,
    "2024_geldbeleggingen": 0, "2024_leasing25": 51007, "2024_lt17": 57439,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "NLOA Pelt YE2025 (bruto JUMP 2.49m / 9901 DROP 55k / pnl DROP 63k / cash JUMP 362k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "WSE + leftover city_pelt leftover maatwerk",
    "legal_basis": "VZW Noord-Limburgs Open Atelier (KBO 0451.320.313; Actief; 2 VE; official zetel Pelt; RSZ2025 85.591; official maatwerk list cmw05)",
    "decision_date": "2026-06-15",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "2492647",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00202608.pdf",
    "stated_goal": "Public leftover maatwerk dual of mined city_pelt",
    "cut_option": "Publish WSE / gemeente Pelt / OCMW Pelt matrix behind bruto JUMP 2.49m and why 9901 DROP 55k pnl DROP 63k while cash JUMP 362k debt JUMP 1.09m leasing JUMP 223k LT JUMP 310k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Pelt>NLOA>JR2025_statutory_L5",
    "notes": "tick2539; Strong official native PDF; leftover mined city_pelt leftover maatwerk leftover-mined AGB-only unused leftover type; 2 VE; prior-year identical; FIRST LOCK leftover city_pelt leftover maatwerk; NOT leftover-via-VE of leftover city_lommel; leftover maatwerk SBM remine@2538 leftover maatwerk t rad remine@2537 leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC unused-not-hardskip 0 leftover CIK HARD SKIP leftover maatwerk type now taken; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "NLOA bruto JUMP 2.49m / 9901 DROP 55k / pnl DROP 63k / cash JUMP 362k (YE2025 leftover city_pelt leftover maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Pelt>NLOA>JR2025",
    "annual_cost_eur": "2492647",
    "total_cost_eur": "2492647",
    "tco_notes": "PDF envelope bruto9900 2492647 JUMP because VKT 70/73 empty; 76A JUMP 12640; bedrijfswinst DROP 204001; pnl DROP 187972; equity JUMP 1138826; assets JUMP 2231233; debt JUMP 1092407; FTE JUMP 55; kapitaalsubsidies DROP 80775; destin691 empty; cash JUMP 831185; geldbeleggingen empty; leasing JUMP 223009; LT JUMP 310241; leftover city_pelt leftover maatwerk",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "WSE + leftover city_pelt leftover maatwerk",
    "stated_goal": "leftover maatwerk leftover city_pelt",
    "measured_outcome": "2.49m bruto JUMP; 55k 9901 DROP; 63k pnl DROP; 362k cash JUMP; leftover city_pelt leftover maatwerk",
    "absurdity_score": "5.38",
    "cost_score": "4.90",
    "difficulty": "5.08",
    "priority_index": "5.11",
    "cut_proposal": "FOI WSE / gemeente Pelt / OCMW Pelt matrix behind bruto 2492647 and why 9901 DROP 204001 pnl DROP 187972 while cash JUMP 831185 debt JUMP 1092407 leasing JUMP 223009 LT JUMP 310241",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2539 leftover mined city_pelt leftover maatwerk leftover-mined AGB-only unused leftover type after leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV leftover VAPH unused-looking leftover CIK HARD SKIP leftover maatwerk type now taken leftover WZC unused-not-hardskip 0 leftover city_pelt leftover maatwerk NLOA YE2024 SKIP@2538 now YE2025 native leftover maatwerk type now taken leftover WZC unused-not-hardskip 0; 2 VE; prior-year identical; next rq_2540 leftover dual PLUS every-10; NOT leftover-via-VE of leftover city_lommel; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; FIRST LOCK leftover city_pelt leftover maatwerk",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Pelt>NLOA>leftover_maatwerk",
    "entity_id": EID,
    "what_is_missing": "WSE / gemeente Pelt / OCMW Pelt split behind bruto JUMP 2492647 and why 9901 DROP 204001 pnl DROP 187972 while cash JUMP 831185 debt JUMP 1092407 leasing JUMP 223009 LT JUMP 310241",
    "why_it_matters": "Strong official PDF leftover maatwerk of mined leftover-mined AGB-only city_pelt; VKT-VZW envelope bruto9900 2.49m because 70/73 empty; leftover maatwerk 2 VE official zetel Pelt unused leftover type; bruto JUMP 2.49m / 9901 DROP 55k / pnl DROP 63k / cash JUMP 362k / debt JUMP 1.09m / leasing JUMP 223k / LT JUMP 310k",
    "priority": "8",
    "recipient_body": "VZW Noord-Limburgs Open Atelier / Voorzitter Raad van Bestuur",
    "recipient_email": "info@openatelier.be",
    "recipient_postal": "Haltstraat 90 bus 1 3900 Pelt",
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
    "notes": "tick2539; ready NOT sent; Strong official native NBB PDF; leftover mined city_pelt leftover maatwerk leftover-mined AGB-only unused leftover type; leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV leftover VAPH unused-looking leftover CIK HARD SKIP leftover maatwerk type now taken leftover WZC unused-not-hardskip 0 leftover city_pelt leftover maatwerk type now taken leftover WZC unused-not-hardskip 0; 2 VE; prior-year identical; next rq_2540 leftover dual PLUS every-10; off leftover-via-VE of leftover city_lommel; off Armonea commercial; off Korian commercial; off Vulpia commercial; FIRST LOCK leftover city_pelt leftover maatwerk",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

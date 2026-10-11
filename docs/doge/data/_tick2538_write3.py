from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2538_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_sbm_maasmechelen_jr2025_nbb_pdf_2538"
EID = "vzw_sbm_maasmechelen"
GAP = "gap_sbm_maasmechelen_maatwerk_matrix_bruto_drop_2_41m_9901_drop_143k_pnl_drop_142k_cash_jump_1_76m_l5"
COMM = "comm_sbm_maasmechelen_jr2025_statutory_bruto_drop_2_41m_9901_drop_143k_pnl_drop_142k_cash_jump_1_76m"
LB = "lb_sbm_maasmechelen_bruto_drop_2_41m_9901_drop_143k_pnl_drop_142k_cash_jump_1_76m_jr2025"
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
    "2025_envelope9900": 2414981, "2025_pnl": 141998, "2025_bedrijfswinst": 142905,
    "2025_9903": 141998, "2025_equity": 3146562, "2025_assets": 3853791,
    "2025_debt": 646153, "2025_fte": 49.1, "2025_kapitaalsubsidies": 1035604,
    "2025_destin691": 108486, "2025_791": 0, "2025_cash": 1761744,
    "2025_geldbeleggingen": 0, "2025_personnel62": 2073468, "2025_gebouwen22": 1113773,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_630": 189163, "2025_capex": 290871,
    "2025_6408": 9446, "2025_leasing25": 219464,
    "2024_omzet": 0, "2024_73": 0, "2024_envelope9900": 2493955,
    "2024_pnl": 376408, "2024_bedrijfswinst": 379662, "2024_equity": 2861618,
    "2024_assets": 3397278, "2024_debt": 474584, "2024_cash": 1512332,
    "2024_fte": 46.6, "2024_destin691": 88362, "2024_kapitaalsubsidies": 892659,
    "2024_geldbeleggingen": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "SBM Maasmechelen YE2025 (bruto DROP 2.41m / 9901 DROP 143k / pnl DROP 142k / cash JUMP 1.76m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "WSE + leftover city_maasmechelen leftover maatwerk",
    "legal_basis": "VZW Sociaal Bedrijvencentrum Maasmechelen (KBO 0461.814.525; Actief; 1 VE; official zetel Maasmechelen; RSZ2025 88.993; official maatwerk list cmw05)",
    "decision_date": "2026-06-04",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "2414981",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00154620.pdf",
    "stated_goal": "Public leftover maatwerk dual of mined city_maasmechelen",
    "cut_option": "Publish WSE / gemeente Maasmechelen / OCMW Maasmechelen matrix behind bruto DROP 2.41m and why 9901 DROP 143k pnl DROP 142k while cash JUMP 1.76m debt JUMP 646k kapitaalsubsidies JUMP 1.04m leasing JUMP 219k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Maasmechelen>SBM>JR2025_statutory_L5",
    "notes": "tick2538; Strong official native PDF; leftover mined city_maasmechelen leftover maatwerk leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; FIRST LOCK leftover city_maasmechelen leftover maatwerk; NOT leftover-via-VE of a DIFFERENT leftover city; leftover maatwerk Kringwinkel Maasland remine@2223 leftover maatwerk MAASBIJ YE2024 leftover WZC Heyvis OCMW leftover WZC Maasmeander BV commercial leftover WZC unused-not-hardskip 0 leftover VAPH unused-looking leftover CIK HARD SKIP leftover maatwerk type now taken; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "SBM bruto DROP 2.41m / 9901 DROP 143k / pnl DROP 142k / cash JUMP 1.76m (YE2025 leftover city_maasmechelen leftover maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Maasmechelen>SBM>JR2025",
    "annual_cost_eur": "2414981",
    "total_cost_eur": "2414981",
    "tco_notes": "PDF envelope bruto9900 2414981 DROP because VKT 70/73 empty; 76A empty; bedrijfswinst DROP 142905; pnl DROP 141998; equity JUMP 3146562; assets JUMP 3853791; debt JUMP 646153; FTE JUMP 49.1; kapitaalsubsidies JUMP 1035604; destin691 JUMP 108486; cash JUMP 1761744; geldbeleggingen empty; leasing JUMP 219464; leftover city_maasmechelen leftover maatwerk",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "WSE + leftover city_maasmechelen leftover maatwerk",
    "stated_goal": "leftover maatwerk leftover city_maasmechelen",
    "measured_outcome": "2.41m bruto DROP; 143k 9901 DROP; 142k pnl DROP; 1.76m cash JUMP; leftover city_maasmechelen leftover maatwerk",
    "absurdity_score": "5.40",
    "cost_score": "4.88",
    "difficulty": "5.08",
    "priority_index": "5.12",
    "cut_proposal": "FOI WSE / gemeente Maasmechelen / OCMW Maasmechelen matrix behind bruto 2414981 and why 9901 DROP 142905 pnl DROP 141998 while cash JUMP 1761744 debt JUMP 646153 kapitaalsubsidies JUMP 1035604 leasing JUMP 219464",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2538 leftover mined city_maasmechelen leftover maatwerk leftover-mined AGB-only unused leftover type after leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV commercial leftover VAPH unused-looking leftover CIK HARD SKIP leftover maatwerk type now taken leftover WZC unused-not-hardskip 0; 1 VE; prior-year identical; next rq_2539 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_maasmechelen leftover maatwerk",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Maasmechelen>SBM>leftover_maatwerk",
    "entity_id": EID,
    "what_is_missing": "WSE / gemeente Maasmechelen / OCMW Maasmechelen split behind bruto DROP 2414981 and why 9901 DROP 142905 pnl DROP 141998 while cash JUMP 1761744 debt JUMP 646153 kapitaalsubsidies JUMP 1035604 leasing JUMP 219464",
    "why_it_matters": "Strong official PDF leftover maatwerk of mined leftover-mined AGB-only city_maasmechelen; VKT-VZW envelope bruto9900 2.41m because 70/73 empty; leftover maatwerk 1 VE official zetel Maasmechelen unused leftover type; bruto DROP 2.41m / 9901 DROP 143k / pnl DROP 142k / cash JUMP 1.76m / debt JUMP 646k / kapitaalsubsidies JUMP 1.04m / leasing JUMP 219k",
    "priority": "8",
    "recipient_body": "VZW Sociaal Bedrijvencentrum Maasmechelen / Voorzitter Raad van Bestuur",
    "recipient_email": "info@sociaalbedrijvencentrum.be",
    "recipient_postal": "Boorsemstraat 2 3630 Maasmechelen",
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
    "notes": "tick2538; ready NOT sent; Strong official native NBB PDF; leftover mined city_maasmechelen leftover maatwerk leftover-mined AGB-only unused leftover type; leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV commercial leftover VAPH unused-looking leftover CIK HARD SKIP leftover maatwerk type now taken leftover WZC unused-not-hardskip 0; 1 VE; prior-year identical; next rq_2539 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE of a DIFFERENT leftover city; off Armonea commercial; off Vulpia commercial; FIRST LOCK leftover city_maasmechelen leftover maatwerk",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

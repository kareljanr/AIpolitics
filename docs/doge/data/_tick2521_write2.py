from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2521_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_torkenshof_wichelen_jr2025_nbb_pdf_2521"
EID = "vzw_torkenshof_wichelen"
GAP = "gap_torkenshof_wichelen_wzc_matrix_bruto_3_66m_omzet73_empty_cash_drop_148k_investments_jump_1_20m_l5"
COMM = "comm_torkenshof_wichelen_jr2025_statutory_bruto_3_66m_omzet73_empty_cash_drop_148k_investments_jump_1_20m"
LB = "lb_torkenshof_wichelen_bruto_3_66m_omzet73_empty_cash_drop_148k_investments_jump_1_20m_jr2025"

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
    "2025_opbr7076A": 0, "2025_bruto9900": 3663093,
    "2025_pnl": 224437, "2025_bedrijfswinst": 225437, "2025_9903": 225019,
    "2025_equity": 2323799, "2025_assets": 2994450, "2025_debt": 670652,
    "2025_fte": 47.5, "2025_fte100": 47.5, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 148212, "2025_geldbeleggingen": 1202068,
    "2025_personnel62": 3327968, "2025_gebouwen22": 945616,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_fondsen10": 0,
    "2025_overgedragen14": 2323799, "2025_voorzieningen16": 0,
    "2025_630": 77729, "2025_capex": 75754,
    "2025_6408": 31959, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 0,
    "2024_pnl": 228972, "2024_bedrijfswinst": 232328,
    "2024_equity": 2099362, "2024_assets": 2733400, "2024_debt": 634038,
    "2024_cash": 1061939, "2024_fte": 48, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 1058,
    "2024_bruto9900": 3539316,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Torkenshof YE2025 (bruto JUMP 3.66m / omzet73 empty / cash DROP 148k / investments JUMP 1.20m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg + leftover city_wichelen leftover WZC",
    "legal_basis": "Torkenshof VZW (KBO 0812.060.838; Actief; 1 VE; official zetel Wichelen; RSZ2025 87.301 ROB)",
    "decision_date": "2026-06-23",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3663093",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00381878.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_wichelen",
    "cut_option": "Publish Departement Zorg / RIZIV / OCMW Wichelen matrix behind bruto 3.66m and why omzet73 empty while cash DROP 148k geldbeleggingen JUMP 1.20m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Wichelen>Torkenshof>JR2025_statutory_L5",
    "notes": "tick2521; Strong official native PDF; leftover mined city_wichelen leftover WZC; 1 VE; prior-year identical; NOT leftover WZC Molenkouter OCMW; NOT leftover city_lebbeke leftover WZC Reva Tersig remine@2520; NOT leftover city_meerhout leftover WZC Ter Kempen remine@2519; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Torkenshof / Den Anker bruto JUMP 3.66m / omzet73 empty / cash DROP 148k / investments JUMP 1.20m (YE2025 leftover city_wichelen leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Wichelen>Torkenshof>JR2025",
    "annual_cost_eur": "3663093",
    "total_cost_eur": "3663093",
    "tco_notes": "PDF envelope bruto9900 3663093 JUMP because VKT and omzet empty; 70 empty; 73 empty; 76A empty; bedrijfswinst DROP 225437; pnl DROP 224437; equity JUMP 2323799; assets JUMP 2994450; debt JUMP 670652; FTE DROP 47.5; kapitaalsubsidies empty; destin691 empty; cash DROP 148212; geldbeleggingen JUMP 1202068; leftover city_wichelen leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg + leftover city_wichelen leftover WZC",
    "stated_goal": "leftover WZC leftover city_wichelen",
    "measured_outcome": "3.66m bruto JUMP; omzet73 empty; cash DROP 148k; investments JUMP 1.20m; leftover city_wichelen leftover WZC",
    "absurdity_score": "5.50",
    "cost_score": "5.15",
    "difficulty": "5.15",
    "priority_index": "5.26",
    "cut_proposal": "FOI Departement Zorg / RIZIV / OCMW Wichelen / gemeente Wichelen matrix behind bruto 3663093 and why omzet73 empty while cash DROP 148212 geldbeleggingen JUMP 1202068 FTE DROP 47.5",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2521 leftover mined city_wichelen leftover WZC after leftover city_lebbeke leftover WZC Reva Tersig@2520 + leftover city_meerhout leftover WZC Ter Kempen@2519; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2522 leftover dual; NOT leftover WZC Molenkouter OCMW; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Wichelen>Torkenshof>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / OCMW Wichelen / gemeente Wichelen split behind bruto 3663093 and why omzet73 empty while cash DROP 148212 geldbeleggingen JUMP 1202068 FTE DROP 47.5",
    "why_it_matters": "Strong official PDF leftover WZC of mined city_wichelen; VKT-VZW envelope bruto 3.66m because omzet73 empty; leftover WZC 1 VE official zetel Wichelen; cash DROP 148k / investments JUMP 1.20m / equity JUMP 2.32m / FTE DROP 47.5",
    "priority": "8",
    "recipient_body": "Torkenshof VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "den.anker@torkenshof.be",
    "recipient_postal": "Anker 15 9260 Wichelen",
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
    "notes": "tick2521; ready NOT sent; Strong official native NBB PDF; leftover mined city_wichelen leftover WZC after leftover city_lebbeke leftover WZC Reva Tersig@2520 + leftover city_meerhout leftover WZC Ter Kempen@2519; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2522 leftover dual; off leftover WZC Molenkouter OCMW; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

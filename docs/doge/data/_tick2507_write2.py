from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2507_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_capelderij_buggenhout_jr2025_nbb_pdf_2507"
EID = "vzw_capelderij_buggenhout"
GAP = "gap_capelderij_buggenhout_vaph_matrix_bruto_3_84m_omzet73_empty_cash_drop_1_02m_pnl_improved_loss_2_6k_l5"
COMM = "comm_capelderij_buggenhout_jr2025_statutory_bruto_3_84m_omzet73_empty_cash_drop_1_02m_pnl_improved_loss_2_6k"
LB = "lb_capelderij_buggenhout_bruto_384m_omzet73_empty_cash_drop_102m_pnl_improved_loss_26k_jr2025"

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
    "2025_opbr7076A": 0, "2025_bruto9900": 3841282,
    "2025_pnl": -2621, "2025_bedrijfswinst": -22415, "2025_9903": 6260,
    "2025_equity": 2764099, "2025_assets": 3376776, "2025_debt": 612676,
    "2025_fte": 48.1, "2025_fte105": 46.2, "2025_kapitaalsubsidies": 981457,
    "2025_destin691": 0, "2025_791": 0, "2025_cash": 100666,
    "2025_geldbeleggingen": 1500000, "2025_personnel62": 3506508,
    "2025_gebouwen22": 510077, "2025_aanbouw27": 0, "2025_66A": 0,
    "2025_fondsen10": 0, "2025_overgedragen14": 1782642,
    "2025_bestemdefondsen13": 0, "2025_voorzieningen16": 0,
    "2025_630": 327591, "2025_capex": 69237, "2025_8179": 3168382,
    "2025_6408": 29598, "2025_74": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 10257,
    "2024_bruto9900": 3617984, "2024_pnl": -9384, "2024_bedrijfswinst": -25578,
    "2024_equity": 2956384, "2024_assets": 3564015, "2024_debt": 607631,
    "2024_cash": 1118612, "2024_fte": 0, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 1171120, "2024_geldbeleggingen": 500000,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Capelderij YE2025 (bruto JUMP 3.84m / omzet73 empty / cash DROP 1.02m / pnl IMPROVED LOSS 2.6k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + Opgroeien + leftover city_buggenhout leftover VAPH",
    "legal_basis": "Begeleidingscentrum Capelderij VZW (KBO 0417.002.505; Actief; 1 VE; official zetel Buggenhout)",
    "decision_date": "2026-06-22",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3841282",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00310005.pdf",
    "stated_goal": "Public leftover VAPH MFC/BuSO dual of mined city_buggenhout",
    "cut_option": "Publish VAPH / Opgroeien / gemeente Buggenhout / BuSO matrix behind bruto 3.84m and why omzet73 empty while cash DROP 1.02m and pnl IMPROVED LOSS 2.6k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Buggenhout>Capelderij>JR2025_statutory_L5",
    "notes": "tick2507; Strong official native PDF; leftover mined city_buggenhout leftover VAPH; 1 VE; prior-year identical; NOT Avalon remine; NOT De Heymeulen YE2024; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Capelderij bruto JUMP 3.84m / omzet73 empty / cash DROP 1.02m / pnl IMPROVED LOSS 2.6k (YE2025 leftover city_buggenhout leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Buggenhout>Capelderij>JR2025",
    "annual_cost_eur": "3841282",
    "total_cost_eur": "3841282",
    "tco_notes": "PDF envelope bruto9900 3841282 JUMP because VKT omzet70+73 empty; 76A 0 DROP; bedrijfswinst IMPROVED LOSS -22415; pnl IMPROVED LOSS -2621; equity DROP 2764099; assets DROP 3376776; debt JUMP 612676; FTE JUMP 48.1 from empty/0; kapitaalsubsidies DROP 981457; destin691 empty; cash DROP 100666; geldbeleggingen JUMP 1500000; capex 69237; leftover city_buggenhout leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + Opgroeien + leftover city_buggenhout leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_buggenhout",
    "measured_outcome": "3.84m bruto; omzet73 empty; cash DROP 1.02m; pnl IMPROVED LOSS 2.6k; leftover city_buggenhout leftover VAPH",
    "absurdity_score": "5.42",
    "cost_score": "5.26",
    "difficulty": "5.18",
    "priority_index": "5.31",
    "cut_proposal": "FOI VAPH / Opgroeien / gemeente Buggenhout / BuSO matrix behind bruto 3841282 and why omzet73 empty while cash DROP 100666 and pnl IMPROVED LOSS -2621 with geldbeleggingen JUMP 1500000",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2507 leftover mined city_buggenhout leftover VAPH after Avalon@2503 leftover VAPH lock; 1 VE; prior-year identical; next rq_2508 leftover dual; next every-10 2510; NOT Avalon remine; NOT De Heymeulen YE2024; NOT CAR Buggenhout leftover-via-VE; NOT Blijdorp remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Buggenhout>Capelderij>leftover_VAPH",
    "entity_id": EID,
    "what_is_missing": "VAPH / Opgroeien / gemeente Buggenhout / BuSO split behind bruto 3841282 and why omzet73 empty while cash DROP 100666 and pnl IMPROVED LOSS -2621 with geldbeleggingen JUMP 1500000",
    "why_it_matters": "Strong official PDF leftover public leftover VAPH of mined city_buggenhout; VKT-VZW envelope bruto 3.84m because omzet73 empty; public leftover VAPH MFC/BuSO 1 VE official zetel Buggenhout; cash DROP 1.02m / pnl IMPROVED LOSS 2.6k",
    "priority": "8",
    "recipient_body": "Begeleidingscentrum Capelderij VZW / Raad van Bestuur",
    "recipient_email": "info@capelderij.be",
    "recipient_postal": "Vekenstraat 1 9255 Buggenhout",
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
    "notes": "tick2507; ready NOT sent; Strong official native NBB PDF; leftover mined city_buggenhout leftover VAPH after Avalon@2503 leftover VAPH lock; 1 VE; prior-year identical; next rq_2508 leftover dual; next every-10 2510; off Avalon remine; off De Heymeulen YE2024; off CAR Buggenhout leftover-via-VE; off Blijdorp remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2509_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_kinderpret_asse_jr2025_nbb_pdf_2509"
EID = "vzw_kinderpret_asse"
GAP = "gap_kinderpret_asse_cik_matrix_bruto_1_68m_omzet73_empty_cash_jump_715k_pnl_jump_164k_l5"
COMM = "comm_kinderpret_asse_jr2025_statutory_bruto_1_68m_omzet73_empty_cash_jump_715k_pnl_jump_164k"
LB = "lb_kinderpret_asse_bruto_168m_omzet73_empty_cash_jump_715k_pnl_jump_164k_jr2025"

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
    "2025_opbr7076A": 0, "2025_bruto9900": 1681501,
    "2025_pnl": 163831, "2025_bedrijfswinst": 177966, "2025_9903": 163831,
    "2025_equity": 2769915, "2025_assets": 3679473, "2025_debt": 909558,
    "2025_fte": 21.2, "2025_fte105": 21.3, "2025_kapitaalsubsidies": 1322230,
    "2025_destin691": 0, "2025_791": 0, "2025_cash": 714672,
    "2025_geldbeleggingen": 373688, "2025_personnel62": 1383369,
    "2025_gebouwen22": 2439134, "2025_aanbouw27": 0, "2025_66A": 0,
    "2025_fondsen10": 150073, "2025_overgedragen14": 1244752,
    "2025_bestemdefondsen13": 52860, "2025_voorzieningen16": 0,
    "2025_630": 120111, "2025_capex": 0, "2025_8179": 0,
    "2025_6408": 55, "2025_6359": 0, "2025_74": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 0,
    "2024_bruto9900": 1573304, "2024_pnl": 140480, "2024_bedrijfswinst": 155392,
    "2024_equity": 2667128, "2024_assets": 3698839, "2024_debt": 1031711,
    "2024_cash": 598653, "2024_fte": 21.6, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 1383274, "2024_geldbeleggingen": 373431,
    "2024_6359": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Kribbe Kinderpret YE2025 (bruto JUMP 1.68m / omzet73 empty / cash JUMP 715k / pnl JUMP 164k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Opgroeien + leftover city_asse leftover CIK",
    "legal_basis": "Kribbe Kinderpret VZW (KBO 0421.200.724; Actief; 1 VE; official zetel Asse)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1681501",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00338297.pdf",
    "stated_goal": "Public leftover CIK dual of mined city_asse",
    "cut_option": "Publish Opgroeien / gemeente Asse matrix behind bruto 1.68m and why omzet73 empty while cash JUMP 715k and pnl JUMP 164k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Asse>KribbeKinderpret>JR2025_statutory_L5",
    "notes": "tick2509; Strong official native PDF; leftover mined city_asse leftover CIK; 1 VE; prior-year identical; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek remine; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Kribbe Kinderpret bruto JUMP 1.68m / omzet73 empty / cash JUMP 715k / pnl JUMP 164k (YE2025 leftover city_asse leftover CIK)",
    "level": "L5",
    "type": "cik_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Asse>KribbeKinderpret>JR2025",
    "annual_cost_eur": "1681501",
    "total_cost_eur": "1681501",
    "tco_notes": "PDF envelope bruto9900 1681501 JUMP because VKT omzet70+73 empty; 76A empty; bedrijfswinst JUMP 177966; pnl JUMP 163831; equity JUMP 2769915; assets DROP 3679473; debt DROP 909558; FTE DROP 21.2; kapitaalsubsidies DROP 1322230; destin691 empty; cash JUMP 714672; geldbeleggingen 373688; leftover city_asse leftover CIK",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Opgroeien + leftover city_asse leftover CIK",
    "stated_goal": "leftover CIK leftover city_asse",
    "measured_outcome": "1.68m bruto; omzet73 empty; cash JUMP 715k; pnl JUMP 164k; leftover city_asse leftover CIK",
    "absurdity_score": "5.20",
    "cost_score": "5.12",
    "difficulty": "5.10",
    "priority_index": "5.15",
    "cut_proposal": "FOI Opgroeien / gemeente Asse matrix behind bruto 1681501 and why omzet73 empty while cash JUMP 714672 and pnl JUMP 163831",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2509 leftover mined city_asse leftover CIK after 3Wplus Kinderopvang@2407 + Vijverbeek@2469 leftover CIK locks; 1 VE; prior-year identical; next rq_2510 leftover dual EVERY-10; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Asse>KribbeKinderpret>leftover_cik",
    "entity_id": EID,
    "what_is_missing": "Opgroeien / gemeente Asse split behind bruto 1681501 and why omzet73 empty while cash JUMP 714672 and pnl JUMP 163831",
    "why_it_matters": "Strong official PDF leftover public leftover CIK of mined city_asse; VKT-VZW envelope bruto 1.68m because omzet73 empty; public leftover CIK 1 VE official zetel Asse; cash JUMP 715k / pnl JUMP 164k",
    "priority": "8",
    "recipient_body": "Kribbe Kinderpret VZW / Raad van Bestuur",
    "recipient_email": "",
    "recipient_postal": "Keesdal 13 1730 Asse",
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
    "notes": "tick2509; ready NOT sent; Strong official native NBB PDF; leftover mined city_asse leftover CIK after 3Wplus Kinderopvang@2407 + Vijverbeek@2469 leftover CIK locks; 1 VE; prior-year identical; FOI via official site contact form (NBB PDF email empty); next rq_2510 leftover dual EVERY-10; off 3Wplus Kinderopvang remine; off Vijverbeek remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2541_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_de_plek_rotselaar_jr2025_nbb_pdf_2541"
EID = "vzw_de_plek_rotselaar"
GAP = "gap_de_plek_rotselaar_vaph_matrix_bruto_drop_8964_omzet_drop_17185_73_jump_2322_cash_jump_12686_l5"
COMM = "comm_de_plek_rotselaar_jr2025_statutory_bruto_drop_8964_73_jump_2322_cash_jump_12686"
LB = "lb_de_plek_rotselaar_bruto_drop_8964_omzet_drop_17185_73_jump_2322_cash_jump_12686_jr2025"
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
    "2025_bruto9900": 8964, "2025_omzet": 17185, "2025_73": 2322, "2025_76A": 216,
    "2025_envelope_bruto9900": 8964, "2025_pnl": 2750, "2025_bedrijfswinst": 2822, "2025_9903": 2750,
    "2025_equity": 23262, "2025_assets": 39124, "2025_debt": 15863,
    "2025_cash": 12686, "2025_kapitaalsubsidies": 9556,
    "2025_personnel62": 289, "2025_630": 5580, "2025_6408": 273,
    "2025_mva": 19432, "2025_capex": 21649, "2025_6061": 10824,
    "2024_bruto9900": 13360, "2024_omzet": 23059, "2024_73": 0, "2024_76A": 136,
    "2024_pnl": 5130, "2024_bedrijfswinst": 5197,
    "2024_equity": 10956, "2024_assets": 12622, "2024_debt": 1666,
    "2024_cash": 4383, "2024_personnel62": 6608, "2024_630": 1348,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Plek Rotselaar YE2025 (bruto DROP 8.96k / omzet DROP 17.19k / 73 JUMP 2.32k / cash JUMP 12.69k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_rotselaar leftover VAPH",
    "legal_basis": "VZW De Plek (KBO 0822.360.357; Actief; 1 VE; official zetel Rotselaar; RSZ2025 88.106; official VAPH adreslijst)",
    "decision_date": "2026-06-28",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "8964",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00317818.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_rotselaar",
    "cut_option": "Publish VAPH / gemeente Rotselaar / OCMW Rotselaar matrix behind bruto DROP 8964 and why 73 JUMP 2322 while cash JUMP 12686 personnel DROP 289",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Rotselaar>DePlek>JR2025_statutory_L5",
    "notes": "tick2541; Strong official native PDF; leftover mined city_rotselaar leftover VAPH leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; FIRST LOCK leftover city_rotselaar leftover VAPH; NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Plek Rotselaar bruto DROP 8.96k / omzet DROP 17.19k / 73 JUMP 2.32k / cash JUMP 12.69k (YE2025 leftover city_rotselaar leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Rotselaar>DePlek>JR2025",
    "annual_cost_eur": "8964",
    "total_cost_eur": "8964",
    "tco_notes": "PDF envelope bruto9900 8964 DROP; omzet70 DROP 17185; 73 JUMP 2322 from empty; bedrijfswinst DROP 2822; pnl DROP 2750; equity JUMP 23262; assets JUMP 39124; debt JUMP 15863; cash JUMP 12686; kapitaalsubsidies JUMP 9556; personnel62 DROP 289; leftover city_rotselaar leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_rotselaar leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_rotselaar",
    "measured_outcome": "8.96k bruto DROP; 17.19k omzet DROP; 2.32k 73 JUMP; 12.69k cash JUMP; leftover city_rotselaar leftover VAPH",
    "absurdity_score": "4.85",
    "cost_score": "2.10",
    "difficulty": "4.20",
    "priority_index": "3.72",
    "cut_proposal": "FOI VAPH / gemeente Rotselaar matrix behind bruto 8964 and why 73 JUMP 2322 while cash JUMP 12686 personnel DROP 289",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2541 leftover mined city_rotselaar leftover VAPH leftover-mined AGB-only unused leftover type after Noorderhart Pelt SCAN SKIP Toontjeshuis Schelle holding SKIP Megusta/Rommeshoef BV SKIP Ter Loke YE2024 SKIP Aalternatief 0 deposits SKIP leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; 1 VE; prior-year identical; next rq_2542 leftover dual (NOT every-10; next every-10 2550); NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_rotselaar leftover VAPH",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Rotselaar>DePlek>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Rotselaar matrix behind MIC-VZW YE2025 bruto DROP 8964, omzet DROP 17185, new code 73 JUMP 2322, cash JUMP 12686, personnel DROP 289, new kapitaalsubsidies 9556",
    "why_it_matters": "Public leftover VAPH dual of mined city_rotselaar shows subsidy line appearing while commercial omzet and personnel collapse and cash/debt jump — need sourced matrix before ranking waste",
    "priority": "7",
    "recipient_body": "VZW De Plek / Voorzitter Raad van Bestuur",
    "recipient_email": "deplek@telenet.be",
    "recipient_postal": "Hanewijk 44A, 3118 Rotselaar",
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
    "notes": "tick2541; ready NOT sent; Strong PDF + Strong KBO; leftover city_rotselaar leftover VAPH",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2544_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_ritmica_hove_jr2025_nbb_pdf_2544"
EID = "vzw_ritmica_hove"
GAP = "gap_ritmica_hove_vaph_matrix_70_76a_jump_5_42m_73_jump_5_22m_pnl_loss_narrower_53k_cash_drop_254k_l5"
COMM = "comm_ritmica_hove_jr2025_statutory_70_76a_jump_5_42m_73_jump_5_22m_pnl_loss_narrower_53k_cash_drop_254k"
LB = "lb_ritmica_hove_70_76a_jump_5_42m_73_jump_5_22m_pnl_loss_narrower_53k_cash_drop_254k_jr2025"
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
    "2025_envelope_70_76A": 5420432, "2025_omzet": 168625, "2025_73": 5215346, "2025_76A": None,
    "2025_pnl": -53443, "2025_bedrijfswinst": -53079, "2025_9903": -53443,
    "2025_equity": 751941, "2025_assets": 1767362, "2025_debt": 1015420,
    "2025_cash": 205034, "2025_kapitaalsubsidies": 51625,
    "2025_personnel62": 4599885, "2025_630": 52678, "2025_6408": 43461, "2025_66A": 7514,
    "2025_mva": 294040, "2025_capex": 9669, "2025_fte": 64.7,
    "2024_envelope_70_76A": 4995178, "2024_omzet": 164261, "2024_73": 4789809, "2024_76A": None,
    "2024_pnl": -130112, "2024_bedrijfswinst": -129832,
    "2024_equity": 808611, "2024_assets": 2085594, "2024_debt": 1276983,
    "2024_cash": 458809, "2024_personnel62": 4211483, "2024_630": 70714, "2024_fte": 58.5,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Ritmica Hove YE2025 (70/76A JUMP 5.42m / 73 JUMP 5.22m / pnl LOSS narrower 53k / cash DROP 254k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_hove leftover VAPH",
    "legal_basis": "VZW Medisch - Pedagogisch Instituut Ritmica (KBO 0408.389.794; Actief; 3 VE; official zetel Hove; RSZ2025 88.105; official VAPH adreslijst)",
    "decision_date": "2026-06-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "5420432",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00226136.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_hove",
    "cut_option": "Publish VAPH / gemeente Hove / OCMW Hove matrix behind 70/76A JUMP 5420432 and 73 JUMP 5215346 and why pnl LOSS narrower -53443 while cash DROP 205034 equity DROP 751941",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Hove>Ritmica>JR2025_statutory_L5",
    "notes": "tick2544; Strong official native PDF; leftover mined city_hove leftover VAPH leftover-mined AGB-only unused leftover type; 3 VE; prior-year identical; FIRST LOCK leftover city_hove leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Ritmica Hove 70/76A JUMP 5.42m / 73 JUMP 5.22m / pnl LOSS narrower 53k / cash DROP 254k (YE2025 leftover city_hove leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Hove>Ritmica>JR2025",
    "annual_cost_eur": "5420432",
    "total_cost_eur": "5420432",
    "tco_notes": "PDF envelope 70/76A 5420432 JUMP; 73 JUMP 5215346; omzet70 JUMP 168625 commercial-only; 76A empty; bedrijfswinst LOSS narrower -53079; pnl LOSS narrower -53443; equity DROP 751941; assets DROP 1767362; debt DROP 1015420; cash DROP 205034; kapitaalsubsidies DROP 51625; personnel62 JUMP 4599885; leftover city_hove leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_hove leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_hove",
    "measured_outcome": "5.42m 70/76A JUMP; 5.22m 73 JUMP; 53k pnl LOSS narrower; 254k cash DROP; leftover city_hove leftover VAPH",
    "absurdity_score": "5.20",
    "cost_score": "5.20",
    "difficulty": "4.40",
    "priority_index": "5.21",
    "cut_proposal": "FOI VAPH / gemeente Hove matrix behind 70/76A 5420432 and 73 5215346 and why pnl LOSS narrower -53443 while cash DROP 205034 equity DROP 751941",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2544 leftover mined city_hove leftover VAPH leftover-mined AGB-only unused leftover type after Aalternatief 0 deposits Apojo remine Therapiedier 0 deposits Kodiel 0 deposits Blend BV commercial Madee leftover-via-VE Turnhout leftover city_nijlen leftover VAPH Iona remine@2543 leftover city_landen leftover VAPH Bindkracht remine@2542 leftover city_rotselaar leftover VAPH De Plek remine@2541 leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover Stijn Sint-Oda/Klimroos leftover-via-VE Hasselt leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; 3 VE; prior-year identical; next rq_2545 leftover dual (NOT every-10; next every-10 2550); NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_hove leftover VAPH",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Hove>Ritmica>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Hove matrix behind VOL-VZW YE2025 70/76A JUMP 5420432, 73 JUMP 5215346, 73-733 gap 85517, pnl LOSS narrower -53443, cash DROP 205034, equity DROP 751941",
    "why_it_matters": "Public leftover VAPH dual of mined city_hove shows 5.42m bedrijfsopbrengsten and 5.22m subsidies while VAPH/gemeente matrix, 73-733 gap and cash DROP 55pct stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Medisch - Pedagogisch Instituut Ritmica / Voorzitter Raad van Bestuur",
    "recipient_email": "personeel@ritmica.be",
    "recipient_postal": "Wouwstraat 44, 2540 Hove",
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
    "notes": "tick2544; ready NOT sent; Strong PDF + Strong KBO; leftover city_hove leftover VAPH",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2543_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_iona_nijlen_jr2025_nbb_pdf_2543"
EID = "vzw_iona_nijlen"
GAP = "gap_iona_nijlen_vaph_matrix_bruto_jump_5_57m_9901_jump_219k_pnl_jump_96k_cash_jump_150k_l5"
COMM = "comm_iona_nijlen_jr2025_statutory_bruto_jump_5_57m_9901_jump_219k_pnl_jump_96k_cash_jump_150k"
LB = "lb_iona_nijlen_bruto_jump_5_57m_9901_jump_219k_pnl_jump_96k_cash_jump_150k_jr2025"
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
    "2025_bruto9900": 5573753, "2025_omzet": None, "2025_73": None, "2025_76A": 3155,
    "2025_envelope_bruto9900": 5573753, "2025_pnl": 252169, "2025_bedrijfswinst": 219000, "2025_9903": 252169,
    "2025_equity": 2951999, "2025_assets": 4055293, "2025_debt": 1080294,
    "2025_cash": 958823, "2025_kapitaalsubsidies": 13159,
    "2025_personnel62": 5160505, "2025_630": 101262, "2025_6408": 39795, "2025_66A": 56009,
    "2025_mva": 919927, "2025_capex": 147795, "2025_fte": 70,
    "2024_bruto9900": 5317391, "2024_omzet": None, "2024_73": None, "2024_76A": 9139,
    "2024_pnl": 156055, "2024_bedrijfswinst": 114312,
    "2024_equity": 2715739, "2024_assets": 3659615, "2024_debt": 920876,
    "2024_cash": 809171, "2024_personnel62": 5006886, "2024_630": 120580, "2024_fte": 69.9,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Iona Nijlen YE2025 (bruto JUMP 5.57m / 9901 JUMP 219k / pnl JUMP 96k / cash JUMP 150k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_nijlen leftover VAPH",
    "legal_basis": "VZW Iona voor heilpedagogie en sociaaltherapie (KBO 0410.269.814; Actief; 1 VE; official zetel Nijlen; RSZ2025 87.201; official VAPH adreslijst)",
    "decision_date": "2026-06-06",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "5573753",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00186964.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_nijlen",
    "cut_option": "Publish VAPH / gemeente Nijlen / OCMW Nijlen matrix behind bruto JUMP 5573753 and why 9901 JUMP 219000 pnl JUMP 252169 while kapitaalsubsidies DROP 13159 cash JUMP 958823",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Nijlen>Iona>JR2025_statutory_L5",
    "notes": "tick2543; Strong official native PDF; leftover mined city_nijlen leftover VAPH leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; FIRST LOCK leftover city_nijlen leftover VAPH; NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Iona Nijlen bruto JUMP 5.57m / 9901 JUMP 219k / pnl JUMP 96k / cash JUMP 150k (YE2025 leftover city_nijlen leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Nijlen>Iona>JR2025",
    "annual_cost_eur": "5573753",
    "total_cost_eur": "5573753",
    "tco_notes": "PDF envelope bruto9900 5573753 JUMP; 73 empty VKT; omzet70 empty VKT; 76A DROP 3155; bedrijfswinst JUMP 219000; pnl JUMP 252169; equity JUMP 2951999; assets JUMP 4055293; debt JUMP 1080294; cash JUMP 958823; kapitaalsubsidies DROP 13159; personnel62 JUMP 5160505; leftover city_nijlen leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_nijlen leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_nijlen",
    "measured_outcome": "5.57m bruto JUMP; 219k 9901 JUMP; 96k pnl JUMP; 150k cash JUMP; leftover city_nijlen leftover VAPH",
    "absurdity_score": "5.10",
    "cost_score": "5.30",
    "difficulty": "4.40",
    "priority_index": "5.18",
    "cut_proposal": "FOI VAPH / gemeente Nijlen matrix behind bruto 5573753 and why 9901 JUMP 219000 pnl JUMP 252169 while kapitaalsubsidies DROP 13159 cash JUMP 958823",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2543 leftover mined city_nijlen leftover VAPH leftover-mined AGB-only unused leftover type after Aalternatief 0 deposits Apojo remine Therapiedier 0 deposits Kodiel 0 deposits Blend BV commercial Madee leftover-via-VE Turnhout leftover city_rotselaar leftover VAPH De Plek remine@2541 leftover city_landen leftover VAPH Bindkracht remine@2542 leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; 1 VE; prior-year identical; next rq_2544 leftover dual (NOT every-10; next every-10 2550); NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_nijlen leftover VAPH",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Nijlen>Iona>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Nijlen matrix behind VKT-VZW YE2025 bruto JUMP 5573753, 9901 JUMP 219000, pnl JUMP 252169, cash JUMP 958823, kapitaalsubsidies DROP 13159, 73/70 empty",
    "why_it_matters": "Public leftover VAPH dual of mined city_nijlen shows 5.57m bruto and doubled bedrijfswinst while VAPH/gemeente matrix and empty 70/73 VKT lines stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Iona voor heilpedagogie en sociaaltherapie / Voorzitter Raad van Bestuur",
    "recipient_email": "info@ionavzw.be",
    "recipient_postal": "Nieuwe Bevelsesteenweg 66, 2560 Nijlen",
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
    "notes": "tick2543; ready NOT sent; Strong PDF + Strong KBO; leftover city_nijlen leftover VAPH",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

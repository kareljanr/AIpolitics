from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2517_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_levensruimte_scherpenheuvel_jr2025_nbb_pdf_2517"
EID = "vzw_levensruimte_scherpenheuvel"
GAP = "gap_levensruimte_scherpenheuvel_vaph_matrix_bruto_3_97m_omzet73_empty_pnl_drop_33k_cash_jump_486k_l5"
COMM = "comm_levensruimte_scherpenheuvel_jr2025_statutory_bruto_3_97m_omzet73_empty_pnl_drop_33k_cash_jump_486k"
LB = "lb_levensruimte_scherpenheuvel_bruto_3_97m_omzet73_empty_pnl_drop_33k_cash_jump_486k_jr2025"

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
    "2025_opbr7076A": 0, "2025_bruto9900": 3970477,
    "2025_pnl": 33452, "2025_bedrijfswinst": 26750, "2025_9903": 33452,
    "2025_equity": 6156850, "2025_assets": 7131536, "2025_debt": 974687,
    "2025_fte": 49.9, "2025_fte9087": 49.9, "2025_kapitaalsubsidies": 2712291,
    "2025_destin691": 150000, "2025_791": 0,
    "2025_cash": 485753, "2025_geldbeleggingen": 1309750,
    "2025_personnel62": 3650263, "2025_gebouwen22": 4668493,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_fondsen10": 1150000,
    "2025_overgedragen14": 1844559, "2025_voorzieningen16": 0,
    "2025_630": 243984, "2025_capex": 123235,
    "2025_6408": 49480, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 0,
    "2024_pnl": 267164, "2024_bedrijfswinst": 263468,
    "2024_equity": 6243127, "2024_assets": 6881215, "2024_debt": 638088,
    "2024_cash": 150920, "2024_fte": 46.9, "2024_destin691": 150000,
    "2024_kapitaalsubsidies": 2832020, "2024_geldbeleggingen": 1250000,
    "2024_74": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Huize Levensruimte YE2025 (bruto JUMP 3.97m / omzet73 empty / pnl DROP 33k / cash JUMP 486k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Opgroeien + leftover city_scherpenheuvel_zichem leftover VAPH",
    "legal_basis": "Huize Levensruimte VZW (KBO 0407.731.976; Actief; 2 VE; official zetel Scherpenheuvel-Zichem; RSZ2025 87.991)",
    "decision_date": "2026-04-25",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3970477",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00290688.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_scherpenheuvel_zichem",
    "cut_option": "Publish Opgroeien / VAPH / Scherpenheuvel-Zichem matrix behind bruto 3.97m and why omzet73 empty while pnl DROP 33k and cash JUMP 486k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>HuizeLevensruimte>JR2025_statutory_L5",
    "notes": "tick2517; Strong official native PDF; leftover mined city_scherpenheuvel_zichem leftover VAPH; 2 VE; 1 VE Perron Z Aarschot is VE of SZ-seated parent; prior-year identical; NOT leftover WZC Huyze Honighsdries@2516; NOT leftover maatwerk De Vlaspit@2515; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Huize Levensruimte bruto JUMP 3.97m / omzet73 empty / pnl DROP 33k / cash JUMP 486k (YE2025 leftover city_scherpenheuvel_zichem leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>HuizeLevensruimte>JR2025",
    "annual_cost_eur": "3970477",
    "total_cost_eur": "3970477",
    "tco_notes": "PDF envelope bruto9900 3970477 JUMP because VKT and 73 empty and bruto >> omzet; 70 empty; 73 empty; 76A empty; bedrijfswinst DROP 26750; pnl DROP 33452; equity DROP 6156850; assets JUMP 7131536; debt JUMP 974687; FTE JUMP 49.9; kapitaalsubsidies DROP 2712291; destin691 FLAT 150000; cash JUMP 485753; geldbeleggingen JUMP 1309750; leftover city_scherpenheuvel_zichem leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Opgroeien + leftover city_scherpenheuvel_zichem leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_scherpenheuvel_zichem",
    "measured_outcome": "3.97m bruto JUMP; omzet73 empty; pnl DROP 33k; cash JUMP 486k; leftover city_scherpenheuvel_zichem leftover VAPH",
    "absurdity_score": "5.38",
    "cost_score": "5.22",
    "difficulty": "5.10",
    "priority_index": "5.30",
    "cut_proposal": "FOI Opgroeien / VAPH / gemeente Scherpenheuvel-Zichem matrix behind bruto 3970477 and why omzet73 empty while pnl DROP 33452 and cash JUMP 485753 with debt JUMP 974687",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2517 leftover mined city_scherpenheuvel_zichem leftover VAPH after leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; 2 VE; 1 VE Perron Z Aarschot is VE of SZ-seated parent; prior-year identical; NOT every-10 (next every-10 2520); next rq_2518 leftover dual; NOT leftover WZC Huyze Honighsdries; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Wonozo leftover jeugdhulp",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>HuizeLevensruimte>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "Opgroeien / VAPH / gemeente Scherpenheuvel-Zichem split behind bruto 3970477 and why omzet73 empty while pnl DROP 33452 and cash JUMP 485753 with debt JUMP 974687",
    "why_it_matters": "Strong official PDF leftover VAPH of mined city_scherpenheuvel_zichem; VKT-VZW envelope bruto 3.97m because 73 empty and bruto >> omzet; leftover VAPH 2 VE official zetel Scherpenheuvel-Zichem; pnl DROP 33k / cash JUMP 486k / debt JUMP 975k",
    "priority": "8",
    "recipient_body": "Huize Levensruimte VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "onthaal@huizelevensruimte.be",
    "recipient_postal": "Pater De Grootstraat 6 3271 Scherpenheuvel-Zichem",
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
    "notes": "tick2517; ready NOT sent; Strong official native NBB PDF; leftover mined city_scherpenheuvel_zichem leftover VAPH after leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; 2 VE; 1 VE Perron Z Aarschot is VE of SZ-seated parent; prior-year identical; NOT every-10 (next every-10 2520); next rq_2518 leftover dual; off leftover WZC Huyze Honighsdries; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine; off Wonozo leftover jeugdhulp",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

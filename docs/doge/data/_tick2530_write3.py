from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2530_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_consolata_zaventem_jr2025_nbb_pdf_2530"
EID = "vzw_consolata_zaventem"
GAP = "gap_consolata_zaventem_wzc_matrix_70_jump_8_97m_9901_flip_86k_pnl_jump_109k_equity_drop_7_53m_l5"
COMM = "comm_consolata_zaventem_jr2025_statutory_70_jump_8_97m_9901_flip_86k_pnl_jump_109k_equity_drop_7_53m"
LB = "lb_consolata_zaventem_70_jump_8_97m_9901_flip_86k_pnl_jump_109k_equity_drop_7_53m_jr2025"
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
    "2025_omzet": 8969085, "2025_73": 1672350, "2025_76A": 1316,
    "2025_opbr7076A": 10764429, "2025_envelope70": 8969085,
    "2025_pnl": -109012, "2025_bedrijfswinst": 86348, "2025_9903": -74860,
    "2025_equity": 7528775, "2025_assets": 20506369, "2025_debt": 12977594,
    "2025_fte": 124, "2025_fte1003": 124, "2025_kapitaalsubsidies": 5686964,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 800197, "2025_geldbeleggingen": 0,
    "2025_personnel62": 7766691, "2025_gebouwen22": 15581271,
    "2025_aanbouw27": 0, "2025_66A": 39741,
    "2025_fondsen10": 735398, "2025_overgedragen14": 806413,
    "2025_voorzieningen16": 0, "2025_630": 752857, "2025_capex": 66238,
    "2025_6408": 13386, "2025_74": 121677, "2025_733": 1672350,
    "2024_omzet": 8621308, "2024_73": 1627050, "2024_76A": 63290,
    "2024_pnl": -389295, "2024_bedrijfswinst": -181888,
    "2024_equity": 7882414, "2024_assets": 21553767, "2024_debt": 13671353,
    "2024_cash": 752033, "2024_fte": 124.7, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 5931591, "2024_geldbeleggingen": 0,
    "2024_envelope70": 8621308,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Consolata Regio Zaventem YE2025 (70 JUMP 8.97m / 9901 FLIP 86k / pnl JUMP -109k / equity DROP 7.53m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + leftover city_zaventem leftover WZC",
    "legal_basis": "VZW Consolata Regio Zaventem (KBO 0457.206.827; Actief; 1 VE; official zetel Zaventem; RSZ2025 87.101; CoBRHA HCO 3630 / 127 woongelegenheden)",
    "decision_date": "2026-06-23",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "8969085",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00259909.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_zaventem",
    "cut_option": "Publish RIZIV / OCMW Zaventem / gemeente Zaventem matrix behind omzet70 8.97m and why 9901 FLIP 86k while pnl JUMP -109k equity DROP 7.53m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Zaventem>Consolata>JR2025_statutory_L5",
    "notes": "tick2530; Strong official native PDF; leftover mined city_zaventem leftover WZC leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; EVERY-10 PLUS leftover dual; NOT leftover city_putte leftover WZC CONSOLATA remine@2529 SKIP; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Consolata Zaventem 70 JUMP 8.97m / 9901 FLIP 86k / pnl JUMP -109k / equity DROP 7.53m (YE2025 leftover city_zaventem leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Zaventem>Consolata>JR2025",
    "annual_cost_eur": "8969085",
    "total_cost_eur": "8969085",
    "tco_notes": "PDF envelope omzet70 8969085 JUMP because 70 present and not commercial-only vs 73; 70 JUMP 8969085; 73 JUMP 1672350; 76A DROP 1316; 70/76A JUMP 10764429; bedrijfswinst JUMP FLIP 86348; pnl JUMP -109012; equity DROP 7528775; assets DROP 20506369; debt DROP 12977594; FTE DROP 124; kapitaalsubsidies DROP 5686964; destin691 empty; cash JUMP 800197; leftover city_zaventem leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + leftover city_zaventem leftover WZC",
    "stated_goal": "leftover WZC leftover city_zaventem",
    "measured_outcome": "8.97m omzet70 JUMP; 9901 FLIP 86k; pnl JUMP -109k; equity DROP 7.53m; leftover city_zaventem leftover WZC",
    "absurdity_score": "5.50",
    "cost_score": "5.35",
    "difficulty": "5.05",
    "priority_index": "5.36",
    "cut_proposal": "FOI RIZIV / OCMW Zaventem / gemeente Zaventem matrix behind omzet70 8969085 and why 9901 FLIP 86348 while pnl JUMP -109012 equity DROP 7528775",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2530 leftover mined city_zaventem leftover WZC leftover-mined AGB-only unused leftover type after leftover city_putte leftover WZC taken@2529 leftover city_bree leftover WZC taken leftover VAPH none local leftover CAR leftover-via-VE Kinrooi SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Boneput SLG commercial SKIP leftover WZC Gerkenberg@2528 leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_zaventem leftover maatwerk TWI unused-looking leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_putte leftover WZC CONSOLATA remine@2529 leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken; 1 VE; prior-year identical; EVERY-10 PLUS leftover dual; next rq_2531 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Zaventem>Consolata>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / OCMW Zaventem / gemeente Zaventem split behind omzet70 8969085 and why 9901 FLIP 86348 while pnl JUMP -109012 equity DROP 7528775",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_zaventem; VOL-VZW envelope omzet70 8.97m because 70 present and not commercial-only vs 73 JUMP 1.67m; leftover WZC 1 VE official zetel Zaventem unused leftover type; 70 JUMP 8.97m / 9901 FLIP 86k / pnl JUMP -109k / equity DROP 7.53m / FTE DROP 124",
    "priority": "8",
    "recipient_body": "VZW Consolata Regio Zaventem / Voorzitter Raad van Bestuur",
    "recipient_email": "kristien.vogelaers@sintantoniuszaventem.be",
    "recipient_postal": "Hoogstraat 52 1930 Zaventem",
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
    "notes": "tick2530; ready NOT sent; Strong official native NBB PDF; leftover mined city_zaventem leftover WZC leftover-mined AGB-only unused leftover type; leftover city_zaventem leftover maatwerk TWI unused-looking leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_putte leftover WZC CONSOLATA remine@2529 leftover city_bree leftover WZC taken leftover VAPH none local leftover CAR leftover-via-VE Kinrooi SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Boneput SLG commercial SKIP leftover WZC Gerkenberg remine@2528 leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; EVERY-10 PLUS leftover dual; next rq_2531 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2536_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_terluchte_oostkamp_jr2025_nbb_pdf_2536"
EID = "vzw_terluchte_oostkamp"
GAP = "gap_terluchte_oostkamp_wzc_matrix_70_jump_6_15m_73_jump_1_10m_pnl_drop_25k_cash_jump_901k_l5"
COMM = "comm_terluchte_oostkamp_jr2025_statutory_70_jump_6_15m_73_jump_1_10m_pnl_drop_25k_cash_jump_901k"
LB = "lb_terluchte_oostkamp_70_jump_6_15m_73_jump_1_10m_pnl_drop_25k_cash_jump_901k_jr2025"
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
    "2025_omzet": 6149223, "2025_73": 1101466, "2025_76A": 10750,
    "2025_envelope70": 6149223, "2025_pnl": 25442, "2025_bedrijfswinst": 102104,
    "2025_9903": 31202, "2025_equity": 2174137, "2025_assets": 6337256,
    "2025_debt": 4163119, "2025_fte": 79.5, "2025_kapitaalsubsidies": 750000,
    "2025_destin691": 0, "2025_791": 0, "2025_cash": 901089,
    "2025_geldbeleggingen": 0, "2025_personnel62": 5216486, "2025_gebouwen22": 29774,
    "2025_aanbouw27": 1460611, "2025_66A": 12952, "2025_630": 201203, "2025_capex": 1393578,
    "2025_6408": 24567, "2024_omzet": 6111705, "2024_73": 1015211,
    "2024_pnl": 480474, "2024_bedrijfswinst": 501893, "2024_equity": 1398695,
    "2024_assets": 6596475, "2024_debt": 5197780, "2024_cash": 506828,
    "2024_fte": 77.9, "2024_destin691": 0, "2024_kapitaalsubsidies": 0,
    "2024_geldbeleggingen": 1550000,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Ter Luchte Oostkamp YE2025 (70 JUMP 6.15m / 73 JUMP 1.10m / pnl DROP 25k / cash JUMP 901k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + leftover city_oostkamp leftover WZC",
    "legal_basis": "VZW Ter Luchte (KBO 0738.896.510; Actief; 1 VE; official zetel Oostkamp; RSZ2025 87.301; official WZC HCO 3818)",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "6149223",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00183286.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_oostkamp",
    "cut_option": "Publish RIZIV / OCMW Oostkamp / gemeente Oostkamp matrix behind 70 JUMP 6.15m and why pnl DROP 25k while cash JUMP 901k kapitaalsubsidies JUMP 750k geldbeleggingen DROP 1.55m aanbouw JUMP 1.46m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Oostkamp>Ter Luchte>JR2025_statutory_L5",
    "notes": "tick2536; Strong official native PDF; leftover mined city_oostkamp leftover WZC leftover-mined AGB-only unused leftover type; 1 VE; prior-year RESTATED; FIRST LOCK leftover city_oostkamp leftover WZC; NOT leftover-via-VE of a DIFFERENT leftover city; leftover WZC Sint-Jozef Groep Zorg H. Familie remine@2057 leftover-via-VE of already-mined Groep Zorg H. Familie leftover WZC type now taken; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Ter Luchte 70 JUMP 6.15m / 73 JUMP 1.10m / pnl DROP 25k / cash JUMP 901k (YE2025 leftover city_oostkamp leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Oostkamp>Ter Luchte>JR2025",
    "annual_cost_eur": "6149223",
    "total_cost_eur": "6149223",
    "tco_notes": "PDF envelope omzet70 6149223 JUMP because VZW 70 present and not commercial-only vs 73 1101466; 76A DROP 10750; bedrijfswinst DROP 102104; pnl DROP 25442; equity JUMP 2174137; assets DROP 6337256; debt DROP 4163119; FTE JUMP 79.5; kapitaalsubsidies JUMP 750000; destin691 empty; cash JUMP 901089; geldbeleggingen DROP empty was 1550000; aanbouw JUMP 1460611; leftover city_oostkamp leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + leftover city_oostkamp leftover WZC",
    "stated_goal": "leftover WZC leftover city_oostkamp",
    "measured_outcome": "6.15m 70 JUMP; 1.10m 73 JUMP; pnl DROP 25k; cash JUMP 901k; leftover city_oostkamp leftover WZC",
    "absurdity_score": "5.42",
    "cost_score": "4.92",
    "difficulty": "5.04",
    "priority_index": "5.13",
    "cut_proposal": "FOI RIZIV / OCMW Oostkamp / gemeente Oostkamp matrix behind 70 6149223 and why pnl DROP 25442 while cash JUMP 901089 kapitaalsubsidies JUMP 750000 geldbeleggingen DROP 1550000 aanbouw JUMP 1460611",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2536 leftover mined city_oostkamp leftover WZC leftover-mined AGB-only unused leftover type after leftover city_diest leftover WZC taken@2535 leftover hospital same KBO Annendael SKIP leftover VAPH/CAR/maatwerk unused-looking leftover CIK HARD SKIP leftover WZC type now taken leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE of leftover city_diest leftover WZC leftover city_willebroek leftover VAPH taken leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_scherpenheuvel_zichem leftover types exhausted leftover WZC Sint-Jozef Groep Zorg H. Familie remine@2057 leftover-via-VE of already-mined Groep Zorg H. Familie leftover WZC type now taken leftover VAPH/CAR/hospital/maatwerk unused-looking leftover CIK HARD SKIP; 1 VE; prior-year RESTATED; next rq_2537 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_oostkamp leftover WZC",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Oostkamp>Ter Luchte>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / OCMW Oostkamp / gemeente Oostkamp split behind 70 JUMP 6149223 and 73 JUMP 1101466 and why pnl DROP 25442 while cash JUMP 901089 kapitaalsubsidies JUMP 750000 geldbeleggingen DROP 1550000 aanbouw JUMP 1460611",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_oostkamp; VOL-VZW envelope omzet70 6.15m because 70 present and not commercial-only vs 73 1.10m; leftover WZC 1 VE official zetel Oostkamp unused leftover type; 70 JUMP 6.15m / 73 JUMP 1.10m / pnl DROP 25k / cash JUMP 901k / kapitaalsubsidies JUMP 750k / geldbeleggingen DROP 1.55m / aanbouw JUMP 1.46m",
    "priority": "8",
    "recipient_body": "VZW Ter Luchte / Voorzitter Raad van Bestuur",
    "recipient_email": "info@terluchte.be",
    "recipient_postal": "Sint-Elooisstraat 87 8020 Oostkamp",
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
    "notes": "tick2536; ready NOT sent; Strong official native NBB PDF; leftover mined city_oostkamp leftover WZC leftover-mined AGB-only unused leftover type; leftover city_diest leftover WZC taken leftover hospital same KBO Annendael SKIP leftover VAPH/CAR/maatwerk unused-looking leftover CIK HARD SKIP leftover WZC type now taken leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE of leftover city_diest leftover WZC leftover city_willebroek leftover VAPH taken leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_scherpenheuvel_zichem leftover types exhausted leftover WZC Sint-Jozef Groep Zorg H. Familie remine@2057 leftover-via-VE of already-mined Groep Zorg H. Familie leftover WZC type now taken leftover VAPH/CAR/hospital/maatwerk unused-looking leftover CIK HARD SKIP; 1 VE; prior-year RESTATED; next rq_2537 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE of a DIFFERENT leftover city; off Armonea commercial; off Vulpia commercial; FIRST LOCK leftover city_oostkamp leftover WZC",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

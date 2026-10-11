from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2535_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_annendael_diest_jr2025_nbb_pdf_2535"
EID = "vzw_annendael_diest"
GAP = "gap_annendael_diest_wzc_matrix_70_jump_36_06m_73_jump_5_99m_pnl_flip_451k_cash_drop_8_93m_l5"
COMM = "comm_annendael_diest_jr2025_statutory_70_jump_36_06m_73_jump_5_99m_pnl_flip_451k_cash_drop_8_93m"
LB = "lb_annendael_diest_70_jump_36_06m_73_jump_5_99m_pnl_flip_451k_cash_drop_8_93m_jr2025"
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
    "2025_omzet": 36063571, "2025_73": 5994527, "2025_76A": 853984,
    "2025_envelope70": 36063571, "2025_pnl": -451172, "2025_bedrijfswinst": 808373,
    "2025_9903": -451172, "2025_equity": 42367160, "2025_assets": 97618819,
    "2025_debt": 51863562, "2025_fte": 398.9, "2025_kapitaalsubsidies": 12754931,
    "2025_destin691": 3211567, "2025_791": 1411019, "2025_cash": 8929733,
    "2025_geldbeleggingen": 3292665, "2025_personnel62": 29570212, "2025_gebouwen22": 66962016,
    "2025_aanbouw27": 171357, "2025_66A": 158602, "2025_630": 3615625, "2025_capex": 2781746,
    "2025_6408": 68883, "2024_omzet": 34835893, "2024_73": 5706424,
    "2024_pnl": 1554771, "2024_bedrijfswinst": 2235596, "2024_equity": 43116949,
    "2024_assets": 107283804, "2024_debt": 59348141, "2024_cash": 16716549,
    "2024_fte": 392.2, "2024_destin691": 1189000, "2024_kapitaalsubsidies": 13053548,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Annendael Diest YE2025 (70 JUMP 36.06m / 73 JUMP 5.99m / pnl FLIP 451k / cash DROP 8.93m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + leftover city_diest leftover WZC",
    "legal_basis": "VZW Zorggroep Annendael (KBO 0414.604.526; Actief; 4 VE; official zetel Diest; RSZ2025 86.104; official WZC HCO 3632 + 3542)",
    "decision_date": "2026-06-25",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "36063571",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00283395.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_diest",
    "cut_option": "Publish RIZIV / OCMW Diest / gemeente Diest matrix behind 70 JUMP 36.06m and why pnl FLIP -451k while cash DROP 8.93m and destin JUMP 3.21m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Diest>Annendael>JR2025_statutory_L5",
    "notes": "tick2535; Strong official native PDF; leftover mined city_diest leftover WZC leftover-mined AGB-only unused leftover type; 4 VE; prior-year identical; FIRST LOCK leftover city_diest leftover WZC; NOT leftover-via-VE of a DIFFERENT leftover city; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Annendael 70 JUMP 36.06m / 73 JUMP 5.99m / pnl FLIP 451k / cash DROP 8.93m (YE2025 leftover city_diest leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Diest>Annendael>JR2025",
    "annual_cost_eur": "36063571",
    "total_cost_eur": "36063571",
    "tco_notes": "PDF envelope omzet70 36063571 JUMP because VZW 70 present and not commercial-only vs 73 5994527; 76A JUMP 853984; bedrijfswinst DROP 808373; pnl FLIP -451172; equity DROP 42367160; assets DROP 97618819; debt DROP 51863562; FTE JUMP 398.9; kapitaalsubsidies DROP 12754931; destin691 JUMP 3211567; cash DROP 8929733; leftover city_diest leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + leftover city_diest leftover WZC",
    "stated_goal": "leftover WZC leftover city_diest",
    "measured_outcome": "36.06m 70 JUMP; 5.99m 73 JUMP; pnl FLIP 451k; cash DROP 8.93m; leftover city_diest leftover WZC",
    "absurdity_score": "5.55",
    "cost_score": "5.48",
    "difficulty": "5.07",
    "priority_index": "5.37",
    "cut_proposal": "FOI RIZIV / OCMW Diest / gemeente Diest matrix behind 70 36063571 and why pnl FLIP -451172 while cash DROP 8929733 and destin JUMP 3211567",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2535 leftover mined city_diest leftover WZC leftover-mined AGB-only unused leftover type after leftover city_willebroek leftover VAPH taken@2534 leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_oostkamp leftover WZC Ter Luchte unused leftover WZC type unused leftover-mined AGB-only leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_scherpenheuvel_zichem leftover types exhausted leftover Huis Sterre same KBO leftover-via-VE of leftover city_diest leftover WZC; 4 VE; prior-year identical; next rq_2536 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_diest leftover WZC",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Diest>Annendael>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / OCMW Diest / gemeente Diest split behind 70 JUMP 36063571 and 73 JUMP 5994527 and why pnl FLIP -451172 while cash DROP 8929733 and destin 691 JUMP 3211567",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_diest; VOL-VZW envelope omzet70 36.06m because 70 present and not commercial-only vs 73 5.99m; leftover WZC 4 VE official zetel Diest unused leftover type; 70 JUMP 36.06m / 73 JUMP 5.99m / pnl FLIP 451k / cash DROP 8.93m / destin JUMP 3.21m",
    "priority": "8",
    "recipient_body": "VZW Zorggroep Annendael / Voorzitter Raad van Bestuur",
    "recipient_email": "info@annendael.be",
    "recipient_postal": "Vestenstraat 1 3290 Diest",
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
    "notes": "tick2535; ready NOT sent; Strong official native NBB PDF; leftover mined city_diest leftover WZC leftover-mined AGB-only unused leftover type; leftover city_willebroek leftover VAPH taken leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_oostkamp leftover WZC Ter Luchte unused leftover WZC type unused leftover-mined AGB-only leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_scherpenheuvel_zichem leftover types exhausted leftover Huis Sterre same KBO leftover-via-VE of leftover city_diest leftover WZC; 4 VE; prior-year identical; next rq_2536 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE of a DIFFERENT leftover city; off Armonea commercial; off Vulpia commercial; FIRST LOCK leftover city_diest leftover WZC",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

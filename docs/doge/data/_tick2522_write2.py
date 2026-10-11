from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2522_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_cuypers_stabroek_jr2025_nbb_pdf_2522"
EID = "vzw_cuypers_stabroek"
GAP = "gap_cuypers_stabroek_wzc_matrix_omzet_6_27m_73_drop_1_16m_pnl_drop_102k_cash_drop_49k_l5"
COMM = "comm_cuypers_stabroek_jr2025_statutory_omzet_6_27m_73_drop_1_16m_pnl_drop_102k_cash_drop_49k"
LB = "lb_cuypers_stabroek_omzet_6_27m_73_drop_1_16m_pnl_drop_102k_cash_drop_49k_jr2025"

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
    "2025_omzet": 6273758, "2025_73": 1161030, "2025_76A": 8890,
    "2025_opbr7076A": 7568448, "2025_bruto9900": 0,
    "2025_pnl": -101734, "2025_bedrijfswinst": 148842, "2025_9903": -101510,
    "2025_equity": 2629512, "2025_assets": 9598296, "2025_debt": 6878783,
    "2025_fte": 75.9, "2025_fte100": 75.9, "2025_kapitaalsubsidies": 1070581,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 49222, "2025_geldbeleggingen": 704504,
    "2025_personnel62": 5346431, "2025_gebouwen22": 7851502,
    "2025_aanbouw27": 0, "2025_66A": 75487, "2025_fondsen10": 893485,
    "2025_overgedragen14": -35581, "2025_voorzieningen16": 90000,
    "2025_630": 641878, "2025_capex": 71328,
    "2025_6408": 4323, "2025_74": 124770, "2025_733": 1160830,
    "2024_omzet": 5794361, "2024_73": 1352069, "2024_76A": 23991,
    "2024_pnl": -45907, "2024_bedrijfswinst": 202203,
    "2024_equity": 2827230, "2024_assets": 10121337, "2024_debt": 7203107,
    "2024_cash": 86556, "2024_fte": 74.1, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 1166564, "2024_geldbeleggingen": 704504,
    "2024_bruto9900": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Aalmoezenier Cuypers YE2025 (omzet JUMP 6.27m / 73 DROP 1.16m / pnl DROP 102k / cash DROP 49k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg + leftover city_stabroek leftover WZC",
    "legal_basis": "De Vrienden van Aalmoezenier Cuypers VZW (KBO 0408.704.847; Actief; 1 VE; official zetel Stabroek; RSZ2025 87.101 RVT)",
    "decision_date": "2026-06-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "6273758",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00325553.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_stabroek",
    "cut_option": "Publish Departement Zorg / RIZIV / OCMW Stabroek matrix behind omzet 6.27m and why 73 DROP 1.16m while pnl DROP 102k cash DROP 49k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Stabroek>AalmoezenierCuypers>JR2025_statutory_L5",
    "notes": "tick2522; Strong official native PDF; leftover mined city_stabroek leftover WZC leftover-mined AGB-only; 1 VE; prior-year identical; NOT leftover WZC Villa ter Molen Vulpia; NOT leftover city_wichelen leftover WZC Torkenshof remine@2521; NOT leftover city_meerhout leftover VAPH t Volderke SCAN; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Aalmoezenier Cuypers omzet JUMP 6.27m / 73 DROP 1.16m / pnl DROP 102k / cash DROP 49k (YE2025 leftover city_stabroek leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Stabroek>AalmoezenierCuypers>JR2025",
    "annual_cost_eur": "6273758",
    "total_cost_eur": "6273758",
    "tco_notes": "PDF envelope omzet70 6273758 JUMP because 70 present and not commercial-only vs 73; 73 DROP 1161030; 76A DROP 8890; bedrijfswinst DROP 148842; pnl DROP -101734; equity DROP 2629512; assets DROP 9598296; debt DROP 6878783; FTE JUMP 75.9; kapitaalsubsidies DROP 1070581; destin691 empty; cash DROP 49222; geldbeleggingen FLAT 704504; leftover city_stabroek leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg + leftover city_stabroek leftover WZC",
    "stated_goal": "leftover WZC leftover city_stabroek",
    "measured_outcome": "6.27m omzet JUMP; 73 DROP 1.16m; pnl DROP 102k loss; cash DROP 49k; leftover city_stabroek leftover WZC",
    "absurdity_score": "5.55",
    "cost_score": "5.25",
    "difficulty": "5.15",
    "priority_index": "5.32",
    "cut_proposal": "FOI Departement Zorg / RIZIV / OCMW Stabroek / gemeente Stabroek matrix behind omzet 6273758 and why 73 DROP 1161030 while pnl DROP -101734 cash DROP 49222 FTE JUMP 75.9",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2522 leftover mined city_stabroek leftover WZC leftover-mined AGB-only after leftover city_wichelen leftover VAPH/CAR/maatwerk none local + leftover city_lebbeke leftover VAPH/CAR/maatwerk none local + leftover city_meerhout leftover VAPH t Volderke SCAN; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2523 leftover dual; NOT leftover WZC Villa ter Molen Vulpia; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Stabroek>AalmoezenierCuypers>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / OCMW Stabroek / gemeente Stabroek split behind omzet 6273758 and why 73 DROP 1161030 while pnl DROP -101734 cash DROP 49222 FTE JUMP 75.9",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_stabroek; VOL-VZW envelope omzet 6.27m because 70 present and not commercial-only; leftover WZC 1 VE official zetel Stabroek; 73 DROP 1.16m / pnl DROP 102k loss / cash DROP 49k / FTE JUMP 75.9",
    "priority": "8",
    "recipient_body": "De Vrienden van Aalmoezenier Cuypers VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@wzcac.be",
    "recipient_postal": "Torense Weg 1 2940 Stabroek",
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
    "notes": "tick2522; ready NOT sent; Strong official native NBB PDF; leftover mined city_stabroek leftover WZC leftover-mined AGB-only after leftover city_wichelen leftover VAPH/CAR/maatwerk none local + leftover city_lebbeke leftover VAPH/CAR/maatwerk none local + leftover city_meerhout leftover VAPH t Volderke SCAN; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2523 leftover dual; off leftover WZC Villa ter Molen Vulpia; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

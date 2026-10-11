from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2525_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_het_laar_wingene_jr2025_nbb_pdf_2525"
EID = "vzw_het_laar_wingene"
GAP = "gap_het_laar_wingene_wzc_matrix_70_jump_6_63m_73_jump_943k_pnl_drop_216k_cash_jump_2_39m_l5"
COMM = "comm_het_laar_wingene_jr2025_statutory_70_jump_6_63m_73_jump_943k_pnl_drop_216k_cash_jump_2_39m"
LB = "lb_het_laar_wingene_70_jump_6_63m_73_jump_943k_pnl_drop_216k_cash_jump_2_39m_jr2025"
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
    "2025_omzet": 6634002, "2025_73": 943247, "2025_76A": 39781,
    "2025_opbr7076A": 7752280, "2025_envelope70": 6634002,
    "2025_pnl": 215832, "2025_bedrijfswinst": 332059, "2025_9903": 216088,
    "2025_equity": 3727774, "2025_assets": 13833205, "2025_debt": 10105432,
    "2025_fte": 76.9, "2025_fte105": 77.8, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 2393834, "2025_geldbeleggingen": 0,
    "2025_personnel62": 5138482, "2025_gebouwen22": 9800608,
    "2025_aanbouw27": 0, "2025_66A": 0,
    "2025_fondsen10": 353152, "2025_overgedragen14": 1177865,
    "2025_voorzieningen16": 0, "2025_630": 800777, "2025_capex": 166225,
    "2025_6408": 9732, "2025_74": 135250, "2025_733": 943247,
    "2024_omzet": 6573951, "2024_73": 894610, "2024_76A": 87590,
    "2024_pnl": 353774, "2024_bedrijfswinst": 478207,
    "2024_equity": 3511941, "2024_assets": 14155911, "2024_debt": 10643970,
    "2024_cash": 2178385, "2024_fte": 72.0, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 0,
    "2024_opbr7076A": 7657327,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Het Laar Wingene YE2025 (70 JUMP 6.63m / 73 JUMP 943k / pnl DROP 216k / cash JUMP 2.39m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg / RIZIV + leftover city_wingene leftover WZC",
    "legal_basis": "Het Laar VZW (KBO 0469.123.870; Actief; 1 VE; official zetel Wingene; RSZ2025 87.301 ROB)",
    "decision_date": "2026-06-15",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "6634002",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00216674.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_wingene",
    "cut_option": "Publish Departement Zorg / RIZIV / OCMW Wingene / gemeente Wingene matrix behind omzet70 6.63m and why pnl DROP 216k while cash JUMP 2.39m FTE JUMP 76.9",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Wingene>HetLaar>JR2025_statutory_L5",
    "notes": "tick2525; Strong official native PDF; leftover mined city_wingene leftover WZC leftover-mined AGB-only; 1 VE; prior-year identical; NOT leftover city_wingene leftover WZC Curando remine@2046; NOT leftover city_wingene leftover WZC Amphora unused leftover WZC type now taken; NOT leftover city_wichelen leftover WZC Torkenshof remine@2521; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Het Laar Wingene 70 JUMP 6.63m / 73 JUMP 943k / pnl DROP 216k / cash JUMP 2.39m (YE2025 leftover city_wingene leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Wingene>HetLaar>JR2025",
    "annual_cost_eur": "6634002",
    "total_cost_eur": "6634002",
    "tco_notes": "PDF envelope omzet70 6634002 JUMP because 70 present and not commercial-only vs 73; 70 JUMP 6634002; 73 JUMP 943247; 76A DROP 39781; 70/76A JUMP 7752280; bedrijfswinst DROP 332059; pnl DROP 215832; equity JUMP 3727774; assets DROP 13833205; debt DROP 10105432; FTE JUMP 76.9; kapitaalsubsidies empty; destin691 empty; cash JUMP 2393834; leftover city_wingene leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg / RIZIV + leftover city_wingene leftover WZC",
    "stated_goal": "leftover WZC leftover city_wingene",
    "measured_outcome": "6.63m omzet70 JUMP; 73 JUMP 943k; pnl DROP 216k; cash JUMP 2.39m; leftover city_wingene leftover WZC",
    "absurdity_score": "5.40",
    "cost_score": "5.20",
    "difficulty": "5.10",
    "priority_index": "5.23",
    "cut_proposal": "FOI Departement Zorg / RIZIV / OCMW Wingene / gemeente Wingene matrix behind omzet70 6634002 and why pnl DROP 215832 while cash JUMP 2393834 FTE JUMP 76.9",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2525 leftover mined city_wingene leftover WZC leftover-mined AGB-only after leftover city_bertem leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine@2523 leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken; leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2526 leftover dual; NOT leftover city_wichelen leftover WZC Torkenshof remine@2521; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Wingene>HetLaar>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / OCMW Wingene / gemeente Wingene split behind omzet70 6634002 and why pnl DROP 215832 while cash JUMP 2393834 FTE JUMP 76.9",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_wingene; VOL-VZW envelope omzet70 6.63m because 70 present and not commercial-only vs 73; leftover WZC 1 VE official zetel Wingene; 73 JUMP 943k / pnl DROP 216k / cash JUMP 2.39m / FTE JUMP 76.9",
    "priority": "8",
    "recipient_body": "Het Laar VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "hetlaar@gvo.be",
    "recipient_postal": "Pastorijstraat 56 8750 Wingene",
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
    "notes": "tick2525; ready NOT sent; Strong official native NBB PDF; leftover mined city_wingene leftover WZC leftover-mined AGB-only after leftover city_bertem leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine@2523 leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken; leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2526 leftover dual; off leftover city_wichelen leftover WZC Torkenshof remine@2521; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

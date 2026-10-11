from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2526_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_wzga_arendonk_jr2025_nbb_pdf_2526"
EID = "vzw_wzga_arendonk"
GAP = "gap_wzga_arendonk_wzc_matrix_70_jump_9_98m_73_jump_2_45m_pnl_jump_632k_equity_jump_719k_l5"
COMM = "comm_wzga_arendonk_jr2025_statutory_70_jump_9_98m_73_jump_2_45m_pnl_jump_632k_equity_jump_719k"
LB = "lb_wzga_arendonk_70_jump_9_98m_73_jump_2_45m_pnl_jump_632k_equity_jump_719k_jr2025"
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
    "2025_omzet": 9984424, "2025_73": 2447880, "2025_76A": 1,
    "2025_opbr7076A": 12676553, "2025_envelope70": 9984424,
    "2025_pnl": 631859, "2025_bedrijfswinst": 621238, "2025_9903": 631859,
    "2025_equity": 718945, "2025_assets": 3576196, "2025_debt": 2857251,
    "2025_fte": 139.1, "2025_fte105": 140.9, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 1391879, "2025_geldbeleggingen": 0,
    "2025_personnel62": 9322064, "2025_gebouwen22": 20370,
    "2025_aanbouw27": 0, "2025_66A": 0,
    "2025_fondsen10": 537213, "2025_overgedragen14": 181732,
    "2025_voorzieningen16": 0, "2025_630": 167681, "2025_capex": 35766,
    "2025_6408": 23781, "2025_74": 244248, "2025_733": 2447880,
    "2024_omzet": 9106668, "2024_73": 2336242, "2024_76A": 0,
    "2024_pnl": 56539, "2024_bedrijfswinst": 44267,
    "2024_equity": 87087, "2024_assets": 3365232, "2024_debt": 3278145,
    "2024_cash": 1289324, "2024_fte": 136.9, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 0,
    "2024_opbr7076A": 11536331,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "WZGA Arendonk YE2025 (70 JUMP 9.98m / 73 JUMP 2.45m / pnl JUMP 632k / equity JUMP 719k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg / RIZIV + leftover city_arendonk leftover WZC",
    "legal_basis": "WoonZorgGroep Arendonk VZW (KBO 0696.665.975; Actief; 2 VE; official zetel Arendonk; RSZ2025 87.101 RVT)",
    "decision_date": "2026-06-03",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "9984424",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00239172.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_arendonk",
    "cut_option": "Publish Departement Zorg / RIZIV / OCMW Arendonk / gemeente Arendonk matrix behind omzet70 9.98m and why pnl JUMP 632k while equity JUMP 719k FTE JUMP 139.1",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Arendonk>WZGA>JR2025_statutory_L5",
    "notes": "tick2526; Strong official native PDF; leftover mined city_arendonk leftover WZC leftover-mined AGB-only unused leftover type; 2 VE; prior-year identical; NOT leftover city_wingene leftover WZC Het Laar remine@2525; NOT leftover city_wingene leftover WZC Curando remine@2046; NOT leftover city_wingene leftover WZC Amphora unused leftover WZC type now taken; NOT leftover city_meerhout leftover maatwerk DE SPRONG remine@2286; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "WZGA Arendonk 70 JUMP 9.98m / 73 JUMP 2.45m / pnl JUMP 632k / equity JUMP 719k (YE2025 leftover city_arendonk leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Arendonk>WZGA>JR2025",
    "annual_cost_eur": "9984424",
    "total_cost_eur": "9984424",
    "tco_notes": "PDF envelope omzet70 9984424 JUMP because 70 present and not commercial-only vs 73; 70 JUMP 9984424; 73 JUMP 2447880; 76A JUMP 1; 70/76A JUMP 12676553; bedrijfswinst JUMP 621238; pnl JUMP 631859; equity JUMP 718945; assets JUMP 3576196; debt DROP 2857251; FTE JUMP 139.1; kapitaalsubsidies empty; destin691 empty; cash JUMP 1391879; leftover city_arendonk leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg / RIZIV + leftover city_arendonk leftover WZC",
    "stated_goal": "leftover WZC leftover city_arendonk",
    "measured_outcome": "9.98m omzet70 JUMP; 73 JUMP 2.45m; pnl JUMP 632k; equity JUMP 719k; leftover city_arendonk leftover WZC",
    "absurdity_score": "5.60",
    "cost_score": "5.45",
    "difficulty": "5.05",
    "priority_index": "5.37",
    "cut_proposal": "FOI Departement Zorg / RIZIV / OCMW Arendonk / gemeente Arendonk matrix behind omzet70 9984424 and why pnl JUMP 631859 while equity JUMP 718945 FTE JUMP 139.1",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2526 leftover mined city_arendonk leftover WZC leftover-mined AGB-only unused leftover type after leftover city_wingene leftover WZC Het Laar@2525 leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover maatwerk DE SPRONG remine@2286 HARD SKIP leftover VAPH t Volderke SCAN leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2527 leftover dual; NOT leftover city_wingene leftover WZC Het Laar remine@2525; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Arendonk>WZGA>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / OCMW Arendonk / gemeente Arendonk split behind omzet70 9984424 and why pnl JUMP 631859 while equity JUMP 718945 FTE JUMP 139.1",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_arendonk; VOL-VZW envelope omzet70 9.98m because 70 present and not commercial-only vs 73; leftover WZC 2 VE official zetel Arendonk unused leftover type; 73 JUMP 2.45m / pnl JUMP 632k / equity JUMP 719k / FTE JUMP 139.1",
    "priority": "8",
    "recipient_body": "WoonZorgGroep Arendonk VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@wzga.be",
    "recipient_postal": "Vrijheid 100 2370 Arendonk",
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
    "notes": "tick2526; ready NOT sent; Strong official native NBB PDF; leftover mined city_arendonk leftover WZC leftover-mined AGB-only unused leftover type after leftover city_wingene leftover WZC Het Laar@2525 leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover maatwerk DE SPRONG remine@2286 HARD SKIP leftover VAPH t Volderke SCAN leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2527 leftover dual; off leftover city_wingene leftover WZC Het Laar remine@2525; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

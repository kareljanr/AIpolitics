from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2528_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_gerkenberg_bree_jr2025_nbb_pdf_2528"
EID = "vzw_gerkenberg_bree"
GAP = "gap_gerkenberg_bree_wzc_matrix_70_jump_3_34m_73_jump_4_76m_pnl_flip_542_cash_drop_553k_l5"
COMM = "comm_gerkenberg_bree_jr2025_statutory_70_jump_3_34m_73_jump_4_76m_pnl_flip_542_cash_drop_553k"
LB = "lb_gerkenberg_bree_70_jump_3_34m_73_jump_4_76m_pnl_flip_542_cash_drop_553k_jr2025"
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
    "2025_omzet": 3341320, "2025_73": 4764956, "2025_76A": 0,
    "2025_opbr7076A": 8626038, "2025_envelope70": 3341320,
    "2025_pnl": 542, "2025_bedrijfswinst": 267165, "2025_9903": 542,
    "2025_equity": 1628000, "2025_assets": 14245271, "2025_debt": 12617271,
    "2025_fte": 97.3, "2025_fte105": 97.5, "2025_kapitaalsubsidies": 63013,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 553077, "2025_geldbeleggingen": 0,
    "2025_personnel62": 6162053, "2025_gebouwen22": 11771549,
    "2025_aanbouw27": 514120, "2025_66A": 0,
    "2025_fondsen10": 250000, "2025_overgedragen14": 1314988,
    "2025_voorzieningen16": 0, "2025_630": 774120, "2025_capex": 276645,
    "2025_6408": 19431, "2025_74": 519763, "2025_733": 4764956,
    "2024_omzet": 3184464, "2024_73": 4748560, "2024_76A": 1543,
    "2024_pnl": -112002, "2024_bedrijfswinst": 202986,
    "2024_equity": 1632375, "2024_assets": 14719525, "2024_debt": 13087151,
    "2024_cash": 586854, "2024_fte": 100.5, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 67929, "2024_geldbeleggingen": 0,
    "2024_envelope70": 3184464,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Welzijnscampus Gerkenberg Bree YE2025 (70 JUMP 3.34m / 73 JUMP 4.76m / pnl FLIP 542 / cash DROP 553k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + leftover city_bree leftover WZC",
    "legal_basis": "Welzijnscampus Gerkenberg VZW (KBO 0867.804.659; Actief; 1 VE; official zetel Bree; RSZ2025 87.101; CoBRHA HCO 15723 / 95 woongelegenheden)",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3341320",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00239951.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_bree",
    "cut_option": "Publish RIZIV / OCMW Bree / gemeente Bree matrix behind omzet70 3.34m and why pnl FLIP 542 while cash DROP 553k FTE DROP 97.3",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Bree>Gerkenberg>JR2025_statutory_L5",
    "notes": "tick2528; Strong official native PDF; leftover mined city_bree leftover WZC leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; NOT leftover city_bree leftover WZC Boneput SLG commercial SKIP; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Gerkenberg Bree 70 JUMP 3.34m / 73 JUMP 4.76m / pnl FLIP 542 / cash DROP 553k (YE2025 leftover city_bree leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Bree>Gerkenberg>JR2025",
    "annual_cost_eur": "3341320",
    "total_cost_eur": "3341320",
    "tco_notes": "PDF envelope omzet70 3341320 JUMP because 70 present and not commercial-only vs 73; 70 JUMP 3341320; 73 JUMP 4764956; 76A DROP 0; 70/76A JUMP 8626038; bedrijfswinst JUMP 267165; pnl FLIP 542; equity DROP 1628000; assets DROP 14245271; debt DROP 12617271; FTE DROP 97.3; kapitaalsubsidies DROP 63013; destin691 empty; cash DROP 553077; leftover city_bree leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + leftover city_bree leftover WZC",
    "stated_goal": "leftover WZC leftover city_bree",
    "measured_outcome": "3.34m omzet70 JUMP; 73 JUMP 4.76m; pnl FLIP 542; cash DROP 553k; leftover city_bree leftover WZC",
    "absurdity_score": "5.45",
    "cost_score": "5.20",
    "difficulty": "5.05",
    "priority_index": "5.24",
    "cut_proposal": "FOI RIZIV / OCMW Bree / gemeente Bree matrix behind omzet70 3341320 and why pnl FLIP 542 while cash DROP 553077 FTE DROP 97.3",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2528 leftover mined city_bree leftover WZC leftover-mined AGB-only unused leftover type after leftover city_arendonk leftover WZC+VAPH taken leftover OCMW De Peulder SKIP leftover CAR/maatwerk none local leftover CIK Dol-Fijn leftover-via-VE Turnhout SKIP leftover CIK Toverbos/Kroontje BV commercial SKIP leftover CIK fallback not taken; leftover city_wingene leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Amphora unused leftover WZC type now taken leftover WZC Curando remine leftover WZC Het Laar remine; leftover city_oud_turnhout leftover maatwerk De Troef YE2024 SKIP leftover WZC Smeedeshof Armonea SKIP leftover city_middelkerke leftover WZC Haerlebout Squatina leftover-via-VE Oostende SKIP; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2529 leftover dual; NOT leftover city_bree leftover WZC Boneput SLG commercial SKIP; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Bree>Gerkenberg>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / OCMW Bree / gemeente Bree split behind omzet70 3341320 and why pnl FLIP 542 while cash DROP 553077 FTE DROP 97.3",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_bree; VOL-VZW envelope omzet70 3.34m because 70 present and not commercial-only vs 73 JUMP 4.76m; leftover WZC 1 VE official zetel Bree unused leftover type; 70 JUMP 3.34m / 73 JUMP 4.76m / pnl FLIP 542 / cash DROP 553k / FTE DROP 97.3",
    "priority": "8",
    "recipient_body": "Welzijnscampus Gerkenberg VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@gerkenberg.be",
    "recipient_postal": "Meeuwerkiezel 90A 3960 Bree",
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
    "notes": "tick2528; ready NOT sent; Strong official native NBB PDF; leftover mined city_bree leftover WZC leftover-mined AGB-only unused leftover type after leftover city_arendonk leftover WZC+VAPH taken leftover OCMW De Peulder SKIP leftover CAR/maatwerk none local leftover CIK Dol-Fijn leftover-via-VE Turnhout SKIP leftover CIK Toverbos/Kroontje BV commercial SKIP leftover CIK fallback not taken; leftover city_wingene leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Amphora unused leftover WZC type now taken leftover WZC Curando remine leftover WZC Het Laar remine; leftover city_oud_turnhout leftover maatwerk De Troef YE2024 SKIP leftover WZC Smeedeshof Armonea SKIP leftover city_middelkerke leftover WZC Haerlebout Squatina leftover-via-VE Oostende SKIP; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2529 leftover dual; off leftover city_bree leftover WZC Boneput SLG commercial SKIP; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2508_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_dagmoed_geraardsbergen_jr2025_nbb_pdf_2508"
EID = "vzw_dagmoed_geraardsbergen"
GAP = "gap_dagmoed_geraardsbergen_maatwerk_matrix_bruto_3_93m_omzet73_empty_cash_drop_329k_635_9_jump_185k_l5"
COMM = "comm_dagmoed_geraardsbergen_jr2025_statutory_bruto_3_93m_omzet73_empty_cash_drop_329k_635_9_jump_185k"
LB = "lb_dagmoed_geraardsbergen_bruto_393m_omzet73_empty_cash_drop_329k_635_9_jump_185k_jr2025"

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
    "2025_opbr7076A": 0, "2025_bruto9900": 3928555,
    "2025_pnl": 122649, "2025_bedrijfswinst": 118329, "2025_9903": 122649,
    "2025_equity": 2137199, "2025_assets": 4296270, "2025_debt": 1111269,
    "2025_fte": 89.3, "2025_fte105": 88.3, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_791": 0, "2025_cash": 397386,
    "2025_geldbeleggingen": 2000000, "2025_personnel62": 3478587,
    "2025_gebouwen22": 1209021, "2025_aanbouw27": 0, "2025_66A": 53,
    "2025_fondsen10": 203754, "2025_overgedragen14": 1791240,
    "2025_bestemdefondsen13": 142204, "2025_voorzieningen16": 1047802,
    "2025_630": 134547, "2025_capex": 324771, "2025_8179": 53669,
    "2025_6408": 11739, "2025_6359": 185300, "2025_74": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 0,
    "2024_bruto9900": 3301704, "2024_pnl": 119445, "2024_bedrijfswinst": 121438,
    "2024_equity": 2014550, "2024_assets": 3894633, "2024_debt": 1017581,
    "2024_cash": 726849, "2024_fte": 86.2, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 1500000,
    "2024_6359": 8400,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Dagmoed YE2025 (bruto JUMP 3.93m / omzet73 empty / cash DROP 329k / 635/9 JUMP 185k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "WEWIS + VDAB + leftover city_geraardsbergen leftover maatwerk",
    "legal_basis": "De Dagmoed VZW (KBO 0416.317.070; Actief; 1 VE; official zetel Geraardsbergen)",
    "decision_date": "2026-05-26",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3928555",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00131365.pdf",
    "stated_goal": "Public leftover maatwerk dual of mined city_geraardsbergen",
    "cut_option": "Publish WEWIS / VDAB / gemeente Geraardsbergen matrix behind bruto 3.93m and why omzet73 empty while cash DROP 329k and 635/9 JUMP 185k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Geraardsbergen>DeDagmoed>JR2025_statutory_L5",
    "notes": "tick2508; Strong official native PDF; leftover mined city_geraardsbergen leftover maatwerk; 1 VE; prior-year identical; NOT Wonozo skip jeugdhulp; NOT CAR Horizon remine; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Dagmoed bruto JUMP 3.93m / omzet73 empty / cash DROP 329k / 635/9 JUMP 185k (YE2025 leftover city_geraardsbergen leftover maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Geraardsbergen>DeDagmoed>JR2025",
    "annual_cost_eur": "3928555",
    "total_cost_eur": "3928555",
    "tco_notes": "PDF envelope bruto9900 3928555 JUMP because VKT omzet70+73 empty; 76A empty; bedrijfswinst DROP 118329; pnl JUMP 122649; equity JUMP 2137199; assets JUMP 4296270; debt JUMP 1111269; FTE JUMP 89.3; kapitaalsubsidies empty; destin691 empty; cash DROP 397386; geldbeleggingen JUMP 2000000; 635/9 JUMP 185300; capex 324771; leftover city_geraardsbergen leftover maatwerk",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "WEWIS + VDAB + leftover city_geraardsbergen leftover maatwerk",
    "stated_goal": "leftover maatwerk leftover city_geraardsbergen",
    "measured_outcome": "3.93m bruto; omzet73 empty; cash DROP 329k; 635/9 JUMP 185k; leftover city_geraardsbergen leftover maatwerk",
    "absurdity_score": "5.44",
    "cost_score": "5.28",
    "difficulty": "5.20",
    "priority_index": "5.33",
    "cut_proposal": "FOI WEWIS / VDAB / gemeente Geraardsbergen matrix behind bruto 3928555 and why omzet73 empty while cash DROP 397386 and 635/9 JUMP 185300 with geldbeleggingen JUMP 2000000",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2508 leftover mined city_geraardsbergen leftover maatwerk after CAR Horizon@2395 leftover CAR lock; 1 VE; prior-year identical; next rq_2509 leftover dual; next every-10 2510; NOT Wonozo skip jeugdhulp; NOT CAR Horizon remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Geraardsbergen>DeDagmoed>leftover_maatwerk",
    "entity_id": EID,
    "what_is_missing": "WEWIS / VDAB / gemeente Geraardsbergen split behind bruto 3928555 and why omzet73 empty while cash DROP 397386 and 635/9 JUMP 185300 with geldbeleggingen JUMP 2000000",
    "why_it_matters": "Strong official PDF leftover public leftover maatwerk of mined city_geraardsbergen; VKT-VZW envelope bruto 3.93m because omzet73 empty; public leftover maatwerk 1 VE official zetel Geraardsbergen; cash DROP 329k / 635/9 JUMP 185k",
    "priority": "8",
    "recipient_body": "De Dagmoed VZW / Raad van Bestuur",
    "recipient_email": "info@dagmoed.be",
    "recipient_postal": "Dagmoedstraat 107 9506 Geraardsbergen",
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
    "notes": "tick2508; ready NOT sent; Strong official native NBB PDF; leftover mined city_geraardsbergen leftover maatwerk after CAR Horizon@2395 leftover CAR lock; 1 VE; prior-year identical; next rq_2509 leftover dual; next every-10 2510; off Wonozo skip jeugdhulp; off CAR Horizon remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

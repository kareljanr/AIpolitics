from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2520_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_reva_tersig_lebbeke_jr2025_nbb_pdf_2520"
EID = "vzw_reva_tersig_lebbeke"
GAP = "gap_reva_tersig_lebbeke_wzc_matrix_bruto_3_12m_omzet73_empty_pnl_flip_454k_loss_cash_drop_163k_equity_drop_958k_l5"
COMM = "comm_reva_tersig_lebbeke_jr2025_statutory_bruto_3_12m_omzet73_empty_pnl_flip_454k_loss_cash_drop_163k_equity_drop_958k"
LB = "lb_reva_tersig_lebbeke_bruto_3_12m_omzet73_empty_pnl_flip_454k_loss_cash_drop_163k_equity_drop_958k_jr2025"

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
    "2025_omzet": 0, "2025_73": 0, "2025_76A": 66043,
    "2025_opbr7076A": 66043, "2025_bruto9900": 3117153,
    "2025_pnl": -454073, "2025_bedrijfswinst": -453340, "2025_9903": -452666,
    "2025_equity": 958018, "2025_assets": 2483710, "2025_debt": 1525692,
    "2025_fte": 50.8, "2025_fte100": 50.8, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 162617, "2025_geldbeleggingen": 0,
    "2025_personnel62": 3336858, "2025_gebouwen22": 537315,
    "2025_aanbouw27": 0, "2025_66A": 41664, "2025_fondsen10": 0,
    "2025_overgedragen14": 678018, "2025_voorzieningen16": 0,
    "2025_630": 123125, "2025_capex": 101725,
    "2025_6408": 68846, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 0,
    "2024_pnl": 27599, "2024_bedrijfswinst": 26963,
    "2024_equity": 1412092, "2024_assets": 2737413, "2024_debt": 1325322,
    "2024_cash": 472775, "2024_fte": 46.8, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 0,
    "2024_bruto9900": 3221361,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Reva Tersig YE2025 (bruto DROP 3.12m / omzet73 empty / pnl FLIP 454k loss / cash DROP 163k / equity DROP 958k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg + leftover city_lebbeke leftover WZC",
    "legal_basis": "Reva Tersig VZW (KBO 0860.679.020; Actief; 1 VE; official zetel Lebbeke; RSZ2025 86.101/86.103)",
    "decision_date": "2026-06-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3117153",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00307029.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_lebbeke",
    "cut_option": "Publish Departement Zorg / RIZIV / OCMW Lebbeke matrix behind bruto 3.12m and why omzet73 empty while pnl FLIP 454k loss cash DROP 163k equity DROP 958k FTE JUMP 50.8",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Lebbeke>RevaTersig>JR2025_statutory_L5",
    "notes": "tick2520; Strong official native PDF; leftover mined city_lebbeke leftover WZC; 1 VE; prior-year identical; NOT leftover WZC Hof ter Veldeken OCMW; NOT leftover WZC Seniorie Ter Minne/Minneveld BV commercial; NOT leftover city_lennik leftover maatwerk Pajottenland remine@2201; NOT leftover city_meerhout leftover WZC Ter Kempen remine@2519; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Reva Tersig bruto DROP 3.12m / omzet73 empty / pnl FLIP 454k loss / cash DROP 163k / equity DROP 958k (YE2025 leftover city_lebbeke leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Lebbeke>RevaTersig>JR2025",
    "annual_cost_eur": "3117153",
    "total_cost_eur": "3117153",
    "tco_notes": "PDF envelope bruto9900 3117153 DROP because VKT and omzet empty; 70 empty; 73 empty; 76A JUMP 66043; bedrijfswinst FLIP -453340; pnl FLIP -454073; equity DROP 958018; assets DROP 2483710; debt JUMP 1525692; FTE JUMP 50.8; kapitaalsubsidies empty; destin691 empty; cash DROP 162617; leftover city_lebbeke leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg + leftover city_lebbeke leftover WZC",
    "stated_goal": "leftover WZC leftover city_lebbeke",
    "measured_outcome": "3.12m bruto DROP; omzet73 empty; pnl FLIP 454k loss; cash DROP 163k; equity DROP 958k; leftover city_lebbeke leftover WZC",
    "absurdity_score": "5.45",
    "cost_score": "5.10",
    "difficulty": "5.10",
    "priority_index": "5.20",
    "cut_proposal": "FOI Departement Zorg / RIZIV / OCMW Lebbeke / gemeente Lebbeke matrix behind bruto 3117153 and why omzet73 empty while pnl FLIP -454073 cash DROP 162617 equity DROP 958018 FTE JUMP 50.8",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2520 leftover mined city_lebbeke leftover WZC after leftover city_meerhout leftover WZC Ter Kempen@2519 + leftover city_lennik leftover maatwerk Pajottenland remine@2201; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; EVERY-10 (next every-10 2530); next rq_2521 leftover dual; NOT leftover WZC Hof ter Veldeken OCMW; NOT leftover WZC Seniorie Ter Minne/Minneveld BV commercial; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>OostVlaanderen>Lebbeke>RevaTersig>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / OCMW Lebbeke / gemeente Lebbeke split behind bruto 3117153 and why omzet73 empty while pnl FLIP -454073 cash DROP 162617 equity DROP 958018 FTE JUMP 50.8",
    "why_it_matters": "Strong official PDF leftover WZC of mined city_lebbeke; VKT-VZW envelope bruto 3.12m because omzet73 empty; leftover WZC 1 VE official zetel Lebbeke; pnl FLIP 454k loss / cash DROP 163k / equity DROP 958k / FTE JUMP 50.8",
    "priority": "8",
    "recipient_body": "Reva Tersig VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@tersig.be",
    "recipient_postal": "Hoeksken 3 9280 Lebbeke",
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
    "notes": "tick2520; ready NOT sent; Strong official native NBB PDF; leftover mined city_lebbeke leftover WZC after leftover city_meerhout leftover WZC Ter Kempen@2519 + leftover city_lennik leftover maatwerk Pajottenland remine@2201; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; EVERY-10 (next every-10 2530); next rq_2521 leftover dual; off leftover WZC Hof ter Veldeken OCMW; off leftover WZC Seniorie Ter Minne/Minneveld BV commercial; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

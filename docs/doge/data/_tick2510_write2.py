from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2510_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_diepen_boomgaard_grimbergen_jr2025_nbb_pdf_2510"
EID = "vzw_diepen_boomgaard_grimbergen"
GAP = "gap_diepen_boomgaard_grimbergen_maatwerk_matrix_bruto_1_85m_omzet73_empty_pnl_deeper_loss_395k_cash_drop_81k_l5"
COMM = "comm_diepen_boomgaard_grimbergen_jr2025_statutory_bruto_1_85m_omzet73_empty_pnl_deeper_loss_395k_cash_drop_81k"
LB = "lb_diepen_boomgaard_grimbergen_bruto_185m_omzet73_empty_pnl_deeper_loss_395k_cash_drop_81k_jr2025"

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
    "2025_omzet": 0, "2025_73": 0, "2025_76A": 3146,
    "2025_opbr7076A": 3146, "2025_bruto9900": 1847578,
    "2025_pnl": -395094, "2025_bedrijfswinst": -320017, "2025_9903": -392366,
    "2025_equity": 699914, "2025_assets": 4732148, "2025_debt": 4032234,
    "2025_fte": 56, "2025_fte105": 58, "2025_kapitaalsubsidies": 1441277,
    "2025_destin691": 0, "2025_791": 0, "2025_cash": 121016,
    "2025_geldbeleggingen": 0, "2025_personnel62": 1932629,
    "2025_gebouwen22": 1296907, "2025_aanbouw27": 1355153, "2025_66A": 14288,
    "2025_fondsen10": 0, "2025_overgedragen14": -741363,
    "2025_bestemdefondsen13": 0, "2025_voorzieningen16": 0,
    "2025_630": 219100, "2025_capex": 961669, "2025_8179": 0,
    "2025_6408": 1578, "2025_6359": 0, "2025_74": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 1811,
    "2024_bruto9900": 1796569, "2024_pnl": -198263, "2024_bedrijfswinst": -157487,
    "2024_equity": 1155438, "2024_assets": 3688714, "2024_debt": 2533276,
    "2024_cash": 202067, "2024_fte": 52, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 1501707, "2024_geldbeleggingen": 0,
    "2024_6359": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Den Diepen Boomgaard YE2025 (bruto JUMP 1.85m / omzet73 empty / pnl DEEPER LOSS 395k / cash DROP 81k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "WEWIS + VDAB + leftover city_grimbergen leftover maatwerk",
    "legal_basis": "Den Diepen Boomgaard VZW (KBO 0421.285.252; Actief; 1 VE; official zetel Grimbergen)",
    "decision_date": "2026-06-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1847578",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00314106.pdf",
    "stated_goal": "Public leftover maatwerk dual of mined city_grimbergen",
    "cut_option": "Publish WEWIS / VDAB / gemeente Grimbergen matrix behind bruto 1.85m and why omzet73 empty while pnl DEEPER LOSS 395k and cash DROP 81k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Grimbergen>DenDiepenBoomgaard>JR2025_statutory_L5",
    "notes": "tick2510; Strong official native PDF; leftover mined city_grimbergen leftover maatwerk; 1 VE; prior-year identical; NOT Havinet remine; NOT WZC Heilig Hart remine; NOT Evara remine; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Den Diepen Boomgaard bruto JUMP 1.85m / omzet73 empty / pnl DEEPER LOSS 395k / cash DROP 81k (YE2025 leftover city_grimbergen leftover maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Grimbergen>DenDiepenBoomgaard>JR2025",
    "annual_cost_eur": "1847578",
    "total_cost_eur": "1847578",
    "tco_notes": "PDF envelope bruto9900 1847578 JUMP because VKT omzet70+73 empty; 76A JUMP 3146; bedrijfswinst DEEPER LOSS 320017; pnl DEEPER LOSS 395094; equity DROP 699914; assets JUMP 4732148; debt JUMP 4032234; FTE JUMP 56; kapitaalsubsidies DROP 1441277; destin691 empty; cash DROP 121016; geldbeleggingen empty; capex 961669; leftover city_grimbergen leftover maatwerk",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "WEWIS + VDAB + leftover city_grimbergen leftover maatwerk",
    "stated_goal": "leftover maatwerk leftover city_grimbergen",
    "measured_outcome": "1.85m bruto; omzet73 empty; pnl DEEPER LOSS 395k; cash DROP 81k; leftover city_grimbergen leftover maatwerk",
    "absurdity_score": "5.36",
    "cost_score": "5.18",
    "difficulty": "5.14",
    "priority_index": "5.21",
    "cut_proposal": "FOI WEWIS / VDAB / gemeente Grimbergen matrix behind bruto 1847578 and why omzet73 empty while pnl DEEPER LOSS 395094 and cash DROP 121016 with debt JUMP 4032234",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2510 leftover mined city_grimbergen leftover maatwerk after leftover VAPH Havinet remine@2301 + leftover WZC Heilig Hart remine@2074; 1 VE; prior-year identical; EVERY-10 2510; next rq_2511 leftover dual; next every-10 2520; NOT Havinet remine; NOT WZC Heilig Hart remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Grimbergen>DenDiepenBoomgaard>leftover_maatwerk",
    "entity_id": EID,
    "what_is_missing": "WEWIS / VDAB / gemeente Grimbergen split behind bruto 1847578 and why omzet73 empty while pnl DEEPER LOSS 395094 and cash DROP 121016 with debt JUMP 4032234",
    "why_it_matters": "Strong official PDF leftover public leftover maatwerk of mined city_grimbergen; VKT-VZW envelope bruto 1.85m because omzet73 empty; public leftover maatwerk 1 VE official zetel Grimbergen; pnl DEEPER LOSS 395k / cash DROP 81k",
    "priority": "8",
    "recipient_body": "Den Diepen Boomgaard VZW / Raad van Bestuur",
    "recipient_email": "info@diepenboomgaard.be",
    "recipient_postal": "Rijkenhoekstraat 80 1850 Grimbergen",
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
    "notes": "tick2510; ready NOT sent; Strong official native NBB PDF; leftover mined city_grimbergen leftover maatwerk after leftover VAPH Havinet remine@2301 + leftover WZC Heilig Hart remine@2074; 1 VE; prior-year identical; EVERY-10 2510; next rq_2511 leftover dual; next every-10 2520; off Havinet remine; off WZC Heilig Hart remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2515_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_vlaspit_scherpenheuvel_jr2025_nbb_pdf_2515"
EID = "vzw_vlaspit_scherpenheuvel"
GAP = "gap_vlaspit_scherpenheuvel_maatwerk_matrix_omzet_2_25m_73_jump_1_62m_pnl_flip_loss_49k_cash_jump_863k_l5"
COMM = "comm_vlaspit_scherpenheuvel_jr2025_statutory_omzet_2_25m_73_jump_1_62m_pnl_flip_loss_49k_cash_jump_863k"
LB = "lb_vlaspit_scherpenheuvel_omzet_2_25m_73_jump_1_62m_pnl_flip_loss_49k_cash_jump_863k_jr2025"

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
    "2025_omzet": 2246566, "2025_73": 1618984, "2025_76A": 9800,
    "2025_opbr7076A": 2256366, "2025_bruto9900": 2796278,
    "2025_pnl": -49340, "2025_bedrijfswinst": -48031, "2025_9903": -49340,
    "2025_equity": 1219243, "2025_assets": 2398819, "2025_debt": 1136291,
    "2025_fte": 63.3, "2025_fte9087": 63.3, "2025_kapitaalsubsidies": 150107,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 862927, "2025_geldbeleggingen": 0,
    "2025_personnel62": 2615515, "2025_gebouwen22": 959124,
    "2025_aanbouw27": 0, "2025_66A": 13038, "2025_fondsen10": 0,
    "2025_overgedragen14": 949136, "2025_voorzieningen16": 43286,
    "2025_630": 198381, "2025_capex": 331386,
    "2025_6408": 13849, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 2175928, "2024_73": 1453185, "2024_76A": 1588,
    "2024_pnl": 168871, "2024_bedrijfswinst": 177754,
    "2024_equity": 1302586, "2024_assets": 2504219, "2024_debt": 1158347,
    "2024_cash": 337575, "2024_fte": 62.4, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 184110, "2024_geldbeleggingen": 650000,
    "2024_74": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Vlaspit YE2025 (70 JUMP 2.25m / 73 JUMP 1.62m / pnl FLIP LOSS 49k / cash JUMP 863k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "WEWIS + VDAB + leftover city_scherpenheuvel_zichem leftover maatwerk",
    "legal_basis": "De Vlaspit VZW (KBO 0461.019.224; Actief; 4 VE; official zetel Scherpenheuvel-Zichem; official Flanders CMW05)",
    "decision_date": "2026-06-22",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "2246566",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00196614.pdf",
    "stated_goal": "Public leftover maatwerk dual of mined city_scherpenheuvel_zichem",
    "cut_option": "Publish WEWIS / VDAB / Scherpenheuvel-Zichem matrix behind omzet70 2.25m and 73 JUMP 1.62m and why pnl FLIP LOSS 49k while cash JUMP 863k and geldbeleggingen DROP 650k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>DeVlaspit>JR2025_statutory_L5",
    "notes": "tick2515; Strong official native PDF; leftover mined city_scherpenheuvel_zichem leftover maatwerk; 4 VE; prior-year identical; NOT De Vlaspit Dienstencheques sister; NOT leftover-via-VE Diest of a Diest-seated parent; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Vlaspit 70 JUMP 2.25m / 73 JUMP 1.62m / pnl FLIP LOSS 49k / cash JUMP 863k (YE2025 leftover city_scherpenheuvel_zichem leftover maatwerk)",
    "level": "L5",
    "type": "maatwerk_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>DeVlaspit>JR2025",
    "annual_cost_eur": "2246566",
    "total_cost_eur": "2246566",
    "tco_notes": "PDF envelope omzet70 2246566 JUMP because VZW and 70 present and not commercial-only vs 73 JUMP 1618984; 76A JUMP 9800; 70/76A JUMP 2256366; bedrijfswinst FLIP LOSS -48031; pnl FLIP LOSS -49340; equity DROP 1219243; assets DROP 2398819; debt DROP 1136291; FTE JUMP 63.3; kapitaalsubsidies DROP 150107; destin691 empty; cash JUMP 862927; geldbeleggingen DROP empty (was 650000); leftover city_scherpenheuvel_zichem leftover maatwerk",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "WEWIS + VDAB + leftover city_scherpenheuvel_zichem leftover maatwerk",
    "stated_goal": "leftover maatwerk leftover city_scherpenheuvel_zichem",
    "measured_outcome": "2.25m omzet70 JUMP; 73 JUMP 1.62m; pnl FLIP LOSS 49k; cash JUMP 863k; leftover city_scherpenheuvel_zichem leftover maatwerk",
    "absurdity_score": "5.22",
    "cost_score": "5.12",
    "difficulty": "5.10",
    "priority_index": "5.14",
    "cut_proposal": "FOI WEWIS / VDAB / gemeente Scherpenheuvel-Zichem matrix behind omzet70 2246566 and 73 JUMP 1618984 and why pnl FLIP LOSS -49340 while 62 JUMP 2615515 and cash JUMP 862927 with geldbeleggingen DROP 650000",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2515 leftover mined city_scherpenheuvel_zichem leftover maatwerk after leftover city_zottegem leftover WZC/VAPH/CIK 2512-2514; 4 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2516 leftover dual; NOT De Vlaspit Dienstencheques sister; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>ScherpenheuvelZichem>DeVlaspit>leftover_maatwerk",
    "entity_id": EID,
    "what_is_missing": "WEWIS / VDAB / gemeente Scherpenheuvel-Zichem split behind omzet70 2246566 and 73 JUMP 1618984 and why pnl FLIP LOSS -49340 while 62 JUMP 2615515 and cash JUMP 862927 with geldbeleggingen DROP 650000",
    "why_it_matters": "Strong official PDF leftover maatwerk of mined city_scherpenheuvel_zichem; VKT-VZW envelope omzet70 2.25m because 70 present and not commercial-only vs 73 JUMP 1.62m; leftover maatwerk 4 VE official zetel Scherpenheuvel-Zichem; pnl FLIP LOSS 49k / cash JUMP 863k / geldbeleggingen DROP 650k",
    "priority": "8",
    "recipient_body": "De Vlaspit VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@devlaspit.be",
    "recipient_postal": "Basilieklaan 53 3270 Scherpenheuvel-Zichem",
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
    "notes": "tick2515; ready NOT sent; Strong official native NBB PDF; leftover mined city_scherpenheuvel_zichem leftover maatwerk after leftover city_zottegem leftover WZC/VAPH/CIK 2512-2514; 4 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2516 leftover dual; off De Vlaspit Dienstencheques sister; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

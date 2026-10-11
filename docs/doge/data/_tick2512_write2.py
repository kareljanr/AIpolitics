from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2512_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_de_bron_zottegem_jr2025_nbb_pdf_2512"
EID = "vzw_de_bron_zottegem"
GAP = "gap_de_bron_zottegem_wzc_matrix_omzet_7_45m_73_jump_1_07m_pnl_jump_317k_cash_drop_201k_l5"
COMM = "comm_de_bron_zottegem_jr2025_statutory_omzet_7_45m_73_jump_1_07m_pnl_jump_317k_cash_drop_201k"
LB = "lb_de_bron_zottegem_omzet_745m_73_jump_107m_pnl_jump_317k_cash_drop_201k_jr2025"

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
    "2025_omzet": 7450435, "2025_73": 1070214, "2025_76A": 8251,
    "2025_opbr7076A": 8987103, "2025_bruto9900": 0,
    "2025_pnl": 316649, "2025_bedrijfswinst": 511019, "2025_9903": 316649,
    "2025_equity": 9977020, "2025_assets": 23805911, "2025_debt": 13828891,
    "2025_fte": 82.7, "2025_fte9086": 121, "2025_kapitaalsubsidies": 911560,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 201059, "2025_geldbeleggingen": 2166587,
    "2025_personnel62": 5729109, "2025_gebouwen22": 19900666,
    "2025_aanbouw27": 40660, "2025_66A": 11339, "2025_fondsen10": 6633279,
    "2025_overgedragen14": 2052224, "2025_voorzieningen16": 0,
    "2025_630": 936438, "2025_capex": 288007,
    "2025_6408": 38144, "2025_74": 458203, "2025_733": 1070214,
    "2024_omzet": 7343120, "2024_73": 1016231, "2024_76A": 23940,
    "2024_pnl": 245758, "2024_bedrijfswinst": 454549,
    "2024_equity": 9647360, "2024_assets": 24287024, "2024_debt": 14639664,
    "2024_cash": 309649, "2024_fte": 84, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 898549, "2024_geldbeleggingen": 1766416,
    "2024_74": 404564,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Bron YE2025 (omzet JUMP 7.45m / 73 JUMP 1.07m / pnl JUMP 317k / cash DROP 201k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + Vlaamse zorg / zorgkas + leftover city_zottegem leftover WZC",
    "legal_basis": "De Bron VZW (KBO 0892.673.479; Actief; 3 VE; official zetel Zottegem)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "7450435",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00244305.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_zottegem",
    "cut_option": "Publish RIZIV / zorgkas / OCMW Zottegem matrix behind omzet 7.45m and 73 JUMP 1.07m and why cash DROP 201k while pnl JUMP 317k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>DeBron>JR2025_statutory_L5",
    "notes": "tick2512; Strong official native PDF; leftover mined city_zottegem leftover WZC; 3 VE; prior-year identical; NOT WZC Egmont OCMW; NOT De Hoop leftover VAPH unused sister; NOT Werkplus remine; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Bron omzet JUMP 7.45m / 73 JUMP 1.07m / pnl JUMP 317k / cash DROP 201k (YE2025 leftover city_zottegem leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>DeBron>JR2025",
    "annual_cost_eur": "7450435",
    "total_cost_eur": "7450435",
    "tco_notes": "PDF envelope omzet70 7450435 JUMP because 70 present and not commercial-only vs 73 JUMP 1070214; 76A DROP 8251; 70/76A JUMP 8987103; bedrijfswinst JUMP 511019; pnl JUMP 316649; equity JUMP 9977020; assets DROP 23805911; debt DROP 13828891; FTE DROP 82.7; kapitaalsubsidies JUMP 911560; destin691 empty; cash DROP 201059; geldbeleggingen JUMP 2166587; leftover city_zottegem leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + Vlaamse zorg / zorgkas + leftover city_zottegem leftover WZC",
    "stated_goal": "leftover WZC leftover city_zottegem",
    "measured_outcome": "7.45m omzet; 73 JUMP 1.07m; pnl JUMP 317k; cash DROP 201k; leftover city_zottegem leftover WZC",
    "absurdity_score": "5.48",
    "cost_score": "5.50",
    "difficulty": "5.10",
    "priority_index": "5.36",
    "cut_proposal": "FOI RIZIV / zorgkas / OCMW Zottegem matrix behind omzet 7450435 and 73 JUMP 1070214 and why cash DROP 201059 while pnl JUMP 316649",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2512 leftover mined city_zottegem leftover WZC after leftover city_grimbergen leftover WZC Den Bogaet@2511; 3 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2513 leftover dual; NOT WZC Egmont OCMW; NOT De Hoop leftover VAPH unused sister; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>DeBron>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / zorgkas / OCMW Zottegem split behind omzet 7450435 and 73 JUMP 1070214 and why cash DROP 201059 while pnl JUMP 316649",
    "why_it_matters": "Strong official PDF leftover WZC of mined city_zottegem; VOL-VZW envelope omzet 7.45m because 70 present and not commercial-only vs 73 JUMP 1.07m; leftover WZC 3 VE official zetel Zottegem; cash DROP 201k / pnl JUMP 317k",
    "priority": "8",
    "recipient_body": "De Bron VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "boekhoudng.debron@sezz.be",
    "recipient_postal": "Marie Popelinstraat 8 9620 Zottegem",
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
    "notes": "tick2512; ready NOT sent; Strong official native NBB PDF; leftover mined city_zottegem leftover WZC after leftover city_grimbergen leftover WZC Den Bogaet@2511; 3 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2513 leftover dual; off WZC Egmont OCMW; off De Hoop leftover VAPH unused sister; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

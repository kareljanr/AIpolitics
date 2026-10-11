from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2511_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_den_bogaet_grimbergen_jr2025_nbb_pdf_2511"
EID = "bv_den_bogaet_grimbergen"
GAP = "gap_den_bogaet_grimbergen_wzc_matrix_omzet_7_59m_694_2_50m_equity_drop_4_38m_debt_jump_3_57m_l5"
COMM = "comm_den_bogaet_grimbergen_jr2025_statutory_omzet_7_59m_694_2_50m_equity_drop_4_38m_debt_jump_3_57m"
LB = "lb_den_bogaet_grimbergen_omzet_759m_694_250m_equity_drop_438m_debt_jump_357m_jr2025"

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
    "2025_omzet": 7593721, "2025_73": 0, "2025_76A": 0,
    "2025_opbr7076A": 8252332, "2025_bruto9900": 0,
    "2025_pnl": 166838, "2025_bedrijfswinst": 143914, "2025_9903": 224487,
    "2025_equity": 4375649, "2025_assets": 7947826, "2025_debt": 3572177,
    "2025_fte": 73.8, "2025_fte9086": 88, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_694": 2500000, "2025_792": 2500000,
    "2025_cash": 272100, "2025_geldbeleggingen": 5417200,
    "2025_personnel62": 5542523, "2025_gebouwen22": 387377,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_fondsen10": 31000,
    "2025_reserves13": 4344649, "2025_voorzieningen16": 0,
    "2025_630": 164605, "2025_capex": 144164, "2025_8179": 0,
    "2025_6408": 999, "2025_6358": 0, "2025_74": 658611,
    "2025_ocmw": 51256, "2025_mutualiteit": 3677526, "2025_aw": 172686,
    "2024_omzet": 7325433, "2024_73": 0, "2024_76A": 12000,
    "2024_pnl": -264935, "2024_bedrijfswinst": 160535,
    "2024_equity": 6708811, "2024_assets": 7948153, "2024_debt": 1239341,
    "2024_cash": 659742, "2024_fte": 78.1, "2024_destin691": 0,
    "2024_694": 0, "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 4282200,
    "2024_74": 786847,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Den Bogaet YE2025 (omzet JUMP 7.59m / 694 JUMP 2.50m / equity DROP 4.38m / debt JUMP 3.57m / cash DROP 272k / pnl FLIP 167k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + Vlaamse zorg / zorgkas + leftover city_grimbergen leftover WZC",
    "legal_basis": "DEN BOGAET BV (KBO 0471.673.980; Actief; 1 VE; official zetel Grimbergen)",
    "decision_date": "2026-06-12",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "7593721",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00341036.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_grimbergen",
    "cut_option": "Publish RIZIV / zorgkas / OCMW Grimbergen matrix behind omzet 7.59m and why 694 JUMP 2.50m while equity DROP 4.38m and debt JUMP 3.57m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Grimbergen>DenBogaet>JR2025_statutory_L5",
    "notes": "tick2511; Strong official native PDF; leftover mined city_grimbergen leftover WZC; 1 VE; prior-year identical; NOT WZC Heilig Hart remine; NOT Havinet remine; NOT Den Diepen Boomgaard remine; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Den Bogaet omzet JUMP 7.59m / 694 JUMP 2.50m / equity DROP 4.38m / debt JUMP 3.57m / cash DROP 272k / pnl FLIP 167k (YE2025 leftover city_grimbergen leftover WZC)",
    "level": "L5",
    "type": "wzc_bv_statutory",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Grimbergen>DenBogaet>JR2025",
    "annual_cost_eur": "7593721",
    "total_cost_eur": "7593721",
    "tco_notes": "PDF envelope omzet70 7593721 JUMP because 70 present and not commercial-only (6.10 OCMW 51256 + mutualiteit 3677526 inside 70); 73 empty VOL; 76A empty DROP; 694 JUMP 2500000; bedrijfswinst DROP 143914; pnl FLIP PROFIT 166838; equity DROP 4375649; assets FLAT 7947826; debt JUMP 3572177; FTE DROP 73.8; kapitaalsubsidies empty; destin691 empty; cash DROP 272100; geldbeleggingen JUMP 5417200; leftover city_grimbergen leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + Vlaamse zorg / zorgkas + leftover city_grimbergen leftover WZC",
    "stated_goal": "leftover WZC leftover city_grimbergen",
    "measured_outcome": "7.59m omzet; 694 JUMP 2.50m; equity DROP 4.38m; debt JUMP 3.57m; cash DROP 272k; pnl FLIP 167k; leftover city_grimbergen leftover WZC",
    "absurdity_score": "5.72",
    "cost_score": "5.48",
    "difficulty": "5.16",
    "priority_index": "5.45",
    "cut_proposal": "FOI RIZIV / zorgkas / OCMW Grimbergen matrix behind omzet 7593721 and why 694 JUMP 2500000 while equity DROP 4375649 and debt JUMP 3572177 with cash DROP 272100",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2511 leftover mined city_grimbergen leftover WZC after leftover maatwerk Den Diepen Boomgaard@2510 + leftover VAPH Havinet remine@2301 + leftover WZC Heilig Hart remine@2074; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2512 leftover dual; NOT WZC Heilig Hart remine; NOT Havinet remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Grimbergen>DenBogaet>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / zorgkas / OCMW Grimbergen split behind omzet 7593721 and why 694 JUMP 2500000 while equity DROP 4375649 and debt JUMP 3572177 with cash DROP 272100",
    "why_it_matters": "Strong official PDF leftover WZC of mined city_grimbergen; VOL-inb envelope omzet 7.59m because 70 present and not commercial-only (mutualiteit 3.68m + OCMW 51k inside 70); leftover WZC 1 VE official zetel Grimbergen; 694 JUMP 2.50m / equity DROP 4.38m / debt JUMP 3.57m",
    "priority": "8",
    "recipient_body": "DEN BOGAET BV / Bestuurder",
    "recipient_email": "info@denbogaet.be",
    "recipient_postal": "Dorpsstraat 1 1851 Grimbergen",
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
    "notes": "tick2511; ready NOT sent; Strong official native NBB PDF; leftover mined city_grimbergen leftover WZC after leftover maatwerk Den Diepen Boomgaard@2510 + leftover VAPH Havinet remine@2301 + leftover WZC Heilig Hart remine@2074; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2512 leftover dual; off WZC Heilig Hart remine; off Havinet remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

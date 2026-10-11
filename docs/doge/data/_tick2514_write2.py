from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2514_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_sint_elisabeth_zottegem_jr2025_nbb_pdf_2514"
EID = "vzw_kdv_sint_elisabeth_zottegem"
GAP = "gap_sint_elisabeth_zottegem_cik_matrix_70_76A_822k_73_jump_811k_pnl_drop_30k_cash_drop_66k_l5"
COMM = "comm_sint_elisabeth_zottegem_jr2025_statutory_70_76A_822k_73_jump_811k_pnl_drop_30k_cash_drop_66k"
LB = "lb_sint_elisabeth_zottegem_70_76A_822k_73_jump_811k_pnl_drop_30k_cash_drop_66k_jr2025"

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
    "2025_omzet": 10657, "2025_73": 811093, "2025_76A": 448,
    "2025_opbr7076A": 822198, "2025_bruto9900": 750639,
    "2025_pnl": 29849, "2025_bedrijfswinst": 26552, "2025_9903": 29849,
    "2025_equity": 360023, "2025_assets": 690321, "2025_debt": 330298,
    "2025_fte": 9.8, "2025_fte9087": 9.8, "2025_kapitaalsubsidies": 75221,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 65765, "2025_geldbeleggingen": 275000,
    "2025_personnel62": 671815, "2025_gebouwen22": 0,
    "2025_aanbouw27": 8218, "2025_66A": 3143, "2025_fondsen10": 0,
    "2025_overgedragen14": 284802, "2025_voorzieningen16": 0,
    "2025_630": 41303, "2025_capex": 28646,
    "2025_6408": 7826, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 10106, "2024_73": 795913, "2024_76A": 1514,
    "2024_pnl": 81721, "2024_bedrijfswinst": 77460,
    "2024_equity": 344278, "2024_assets": 647617, "2024_debt": 303339,
    "2024_cash": 90893, "2024_fte": 10.7, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 89325, "2024_geldbeleggingen": 200000,
    "2024_74": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Kinderdagverblijf Sint-Elisabeth YE2025 (70/76A JUMP 822k / 73 JUMP 811k / pnl DROP 30k / cash DROP 66k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Opgroeien + leftover city_zottegem leftover CIK",
    "legal_basis": "Kinderdagverblijf Sint-Elisabeth, Zottegem VZW (KBO 0452.614.767; Actief; 1 VE; official zetel Zottegem)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "822198",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00271050.pdf",
    "stated_goal": "Public leftover CIK dual of mined city_zottegem",
    "cut_option": "Publish Opgroeien / Zottegem / SEZZ matrix behind 70/76A 822k and 73 JUMP 811k and why pnl DROP 30k while 62 JUMP and cash DROP 66k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>SintElisabeth>JR2025_statutory_L5",
    "notes": "tick2514; Strong official native PDF; leftover mined city_zottegem leftover CIK; 1 VE; prior-year identical; NOT De Hoop leftover VAPH; NOT De Bron leftover WZC; NOT De Bolster leftover-via-VE; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Sint-Elisabeth 70/76A JUMP 822k / 73 JUMP 811k / pnl DROP 30k / cash DROP 66k (YE2025 leftover city_zottegem leftover CIK)",
    "level": "L5",
    "type": "cik_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>SintElisabeth>JR2025",
    "annual_cost_eur": "822198",
    "total_cost_eur": "822198",
    "tco_notes": "PDF envelope 70/76A 822198 JUMP because VZW and omzet commercial-only vs large 73 JUMP 811093; 76A DROP 448; bedrijfswinst DROP 26552; pnl DROP 29849; equity JUMP 360023; assets JUMP 690321; debt JUMP 330298; FTE DROP 9.8; kapitaalsubsidies DROP 75221; destin691 empty; cash DROP 65765; geldbeleggingen JUMP 275000; leftover city_zottegem leftover CIK",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Opgroeien + leftover city_zottegem leftover CIK",
    "stated_goal": "leftover CIK leftover city_zottegem",
    "measured_outcome": "822k 70/76A JUMP; 73 JUMP 811k; pnl DROP 30k; cash DROP 66k; leftover city_zottegem leftover CIK",
    "absurdity_score": "5.25",
    "cost_score": "4.65",
    "difficulty": "5.15",
    "priority_index": "5.16",
    "cut_proposal": "FOI Opgroeien / Zottegem / SEZZ matrix behind 70/76A 822198 and 73 JUMP 811093 and why pnl DROP 29849 while 62 JUMP 671815 and cash DROP 65765",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2514 leftover mined city_zottegem leftover CIK after leftover city_zottegem leftover WZC De Bron@2512 + leftover VAPH De Hoop@2513; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2515 leftover dual; NOT De Hoop leftover VAPH; NOT De Bron leftover WZC; NOT De Bolster leftover-via-VE; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>SintElisabeth>leftover_cik",
    "entity_id": EID,
    "what_is_missing": "Opgroeien / Zottegem / SEZZ split behind 70/76A 822198 and 73 JUMP 811093 and why pnl DROP 29849 while 62 JUMP 671815 and cash DROP 65765",
    "why_it_matters": "Strong official PDF leftover CIK of mined city_zottegem; VKT-VZW envelope 70/76A 822k because omzet commercial-only vs large 73 JUMP 811k; leftover CIK 1 VE official zetel Zottegem; pnl DROP 30k / cash DROP 66k / FTE DROP 9.8",
    "priority": "8",
    "recipient_body": "Kinderdagverblijf Sint-Elisabeth, Zottegem VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "yvan.lenssens@sezz.be",
    "recipient_postal": "Godveerdegemstraat 69 9620 Zottegem",
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
    "notes": "tick2514; ready NOT sent; Strong official native NBB PDF; leftover mined city_zottegem leftover CIK after leftover city_zottegem leftover WZC De Bron@2512 + leftover VAPH De Hoop@2513; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2515 leftover dual; off De Hoop leftover VAPH; off De Bron leftover WZC; off De Bolster leftover-via-VE; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

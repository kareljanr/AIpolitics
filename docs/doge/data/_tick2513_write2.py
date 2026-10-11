from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2513_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_de_hoop_zottegem_jr2025_nbb_pdf_2513"
EID = "vzw_de_hoop_zottegem"
GAP = "gap_de_hoop_zottegem_vaph_matrix_bruto_145k_73_drop_21k_pnl_jump_80k_fte_drop_0_l5"
COMM = "comm_de_hoop_zottegem_jr2025_statutory_bruto_145k_73_drop_21k_pnl_jump_80k_fte_drop_0"
LB = "lb_de_hoop_zottegem_bruto_145k_73_drop_21k_pnl_jump_80k_fte_drop_0_jr2025"

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
    "2025_omzet": 0, "2025_73": 20846, "2025_76A": 3269,
    "2025_opbr7076A": 3269, "2025_bruto9900": 145460,
    "2025_pnl": 80173, "2025_bedrijfswinst": 45595, "2025_9903": 80173,
    "2025_equity": 328381, "2025_assets": 1840258, "2025_debt": 1511877,
    "2025_fte": 0, "2025_fte9087": 0, "2025_kapitaalsubsidies": 291843,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 542495, "2025_geldbeleggingen": 0,
    "2025_personnel62": 0, "2025_gebouwen22": 1276535,
    "2025_aanbouw27": 0, "2025_66A": 13714, "2025_fondsen10": 0,
    "2025_overgedragen14": 36538, "2025_voorzieningen16": 0,
    "2025_630": 84183, "2025_capex": 9603,
    "2025_6408": 1968, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 69057, "2024_73": 806649, "2024_76A": 7067,
    "2024_pnl": 3709, "2024_bedrijfswinst": -27,
    "2024_equity": 269054, "2024_assets": 2665951, "2024_debt": 2396897,
    "2024_cash": 645659, "2024_fte": 13.3, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 312689, "2024_geldbeleggingen": 618166,
    "2024_74": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Hoop YE2025 (bruto DROP 145k / 73 DROP 21k / pnl JUMP 80k / FTE DROP 0 / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_zottegem leftover VAPH",
    "legal_basis": "De Hoop VZW (KBO 0870.779.490; Actief; 0 VE; official zetel Zottegem)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "145460",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00269926.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_zottegem",
    "cut_option": "Publish VAPH / Zottegem / De Bolster transfer matrix behind bruto DROP 145k and 73 DROP 21k and why FTE DROP 0 while pnl JUMP 80k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>DeHoop>JR2025_statutory_L5",
    "notes": "tick2513; Strong official native PDF; leftover mined city_zottegem leftover VAPH; 0 VE; prior-year identical; NOT De Bron leftover WZC; NOT WZC Egmont OCMW; NOT De Bolster leftover-via-VE; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Hoop bruto DROP 145k / 73 DROP 21k / pnl JUMP 80k / FTE DROP 0 (YE2025 leftover city_zottegem leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>DeHoop>JR2025",
    "annual_cost_eur": "145460",
    "total_cost_eur": "145460",
    "tco_notes": "PDF envelope bruto9900 145460 DROP because VKT and omzet empty vs 73 DROP 20846; 76A DROP 3269; bedrijfswinst FLIP 45595; pnl JUMP 80173; equity JUMP 328381; assets DROP 1840258; debt DROP 1511877; FTE DROP 0; kapitaalsubsidies DROP 291843; destin691 empty; cash DROP 542495; geldbeleggingen empty DROP; leftover city_zottegem leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_zottegem leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_zottegem",
    "measured_outcome": "145k bruto DROP; 73 DROP 21k; pnl JUMP 80k; FTE DROP 0; leftover city_zottegem leftover VAPH",
    "absurdity_score": "5.42",
    "cost_score": "4.50",
    "difficulty": "5.15",
    "priority_index": "5.08",
    "cut_proposal": "FOI VAPH / Zottegem / De Bolster transfer matrix behind bruto 145460 and 73 DROP 20846 and why FTE DROP 0 while pnl JUMP 80173",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2513 leftover mined city_zottegem leftover VAPH after leftover city_zottegem leftover WZC De Bron@2512; 0 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2514 leftover dual; NOT De Bron leftover WZC; NOT WZC Egmont OCMW; NOT De Bolster leftover-via-VE; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Zottegem>DeHoop>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / Zottegem / De Bolster transfer split behind bruto 145460 and 73 DROP 20846 and why FTE DROP 0 while pnl JUMP 80173",
    "why_it_matters": "Strong official PDF leftover VAPH of mined city_zottegem; VKT-VZW envelope bruto 145k because omzet empty vs 73 DROP 21k; leftover VAPH 0 VE official zetel Zottegem; FTE DROP 0 / pnl JUMP 80k / ops appear transferred to De Bolster",
    "priority": "8",
    "recipient_body": "De Hoop VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "yvan.lenssens@sezz.be",
    "recipient_postal": "Zuster Angelalaan 1 9620 Zottegem",
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
    "notes": "tick2513; ready NOT sent; Strong official native NBB PDF; leftover mined city_zottegem leftover VAPH after leftover city_zottegem leftover WZC De Bron@2512; 0 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2514 leftover dual; off De Bron leftover WZC; off WZC Egmont OCMW; off De Bolster leftover-via-VE; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine; off Zorg-Saam remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

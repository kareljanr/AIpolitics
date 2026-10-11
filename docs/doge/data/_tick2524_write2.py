from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2524_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_eglantier_bertem_jr2025_nbb_pdf_2524"
EID = "vzw_eglantier_bertem"
GAP = "gap_eglantier_bertem_vaph_matrix_70_76A_1_95m_73_jump_1_73m_pnl_flip_18k_cash_drop_120k_l5"
COMM = "comm_eglantier_bertem_jr2025_statutory_70_76A_1_95m_73_jump_1_73m_pnl_flip_18k_cash_drop_120k"
LB = "lb_eglantier_bertem_70_76A_1_95m_73_jump_1_73m_pnl_flip_18k_cash_drop_120k_jr2025"

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
    "2025_omzet": 88481, "2025_73": 1732649, "2025_76A": 130588,
    "2025_opbr7076A": 1951718, "2025_bruto9900": 1800928,
    "2025_pnl": 18173, "2025_bedrijfswinst": -3269, "2025_9903": 18173,
    "2025_equity": 4228756, "2025_assets": 5219768, "2025_debt": 991012,
    "2025_fte": 24.1, "2025_fte100": 24.4, "2025_kapitaalsubsidies": 838237,
    "2025_destin691": 43130, "2025_791": 0,
    "2025_cash": 119855, "2025_geldbeleggingen": 1664865,
    "2025_personnel62": 1649088, "2025_gebouwen22": 2969487,
    "2025_aanbouw27": 0, "2025_66A": 13365, "2025_fondsen10": 1207743,
    "2025_overgedragen14": 1863952, "2025_voorzieningen16": 0,
    "2025_630": 129052, "2025_capex": 68620,
    "2025_6408": 12692, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 93176, "2024_73": 1646175, "2024_76A": 68118,
    "2024_pnl": -27430, "2024_bedrijfswinst": 33301,
    "2024_equity": 4109756, "2024_assets": 5097760, "2024_debt": 988004,
    "2024_cash": 208500, "2024_fte": 23.3, "2024_destin691": 16000,
    "2024_kapitaalsubsidies": 885104, "2024_geldbeleggingen": 1515956,
    "2024_bruto9900": 1683032, "2024_opbr7076A": 1807469,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Eglantier Bertem YE2025 (70/76A JUMP 1.95m / 73 JUMP 1.73m / pnl FLIP 18k / cash DROP 120k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_bertem leftover VAPH",
    "legal_basis": "De Eglantier VZW (KBO 0418.747.911; Actief; 1 VE; official zetel Bertem; RSZ2025 88.999 MFC)",
    "decision_date": "2026-04-23",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1951718",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00119829.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_bertem",
    "cut_option": "Publish VAPH / OCMW Bertem / gemeente Bertem matrix behind 70/76A 1.95m and why 73 JUMP 1.73m while 9901 FLIP LOSS 3k cash DROP 120k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Bertem>DeEglantier>JR2025_statutory_L5",
    "notes": "tick2524; Strong official native PDF; leftover mined city_bertem leftover VAPH leftover-mined AGB-only; 1 VE; prior-year identical; NOT leftover city_bertem leftover WZC Sint-Bernardus remine@2523; NOT leftover VAPH A-Tipi leftover-via-VE Leuven; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Eglantier Bertem 70/76A JUMP 1.95m / 73 JUMP 1.73m / pnl FLIP 18k / cash DROP 120k (YE2025 leftover city_bertem leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Bertem>DeEglantier>JR2025",
    "annual_cost_eur": "1951718",
    "total_cost_eur": "1951718",
    "tco_notes": "PDF envelope 70/76A 1951718 JUMP because omzet commercial-only vs large 73; 70 DROP 88481; 73 JUMP 1732649; 76A JUMP 130588; bruto9900 JUMP 1800928; bedrijfswinst FLIP LOSS -3269; pnl FLIP 18173; equity JUMP 4228756; assets JUMP 5219768; debt JUMP 991012; FTE JUMP 24.1; kapitaalsubsidies DROP 838237; destin691 JUMP 43130; cash DROP 119855; geldbeleggingen JUMP 1664865; leftover city_bertem leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_bertem leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_bertem",
    "measured_outcome": "1.95m 70/76A JUMP; 73 JUMP 1.73m; pnl FLIP 18k; cash DROP 120k; leftover city_bertem leftover VAPH",
    "absurdity_score": "5.40",
    "cost_score": "5.05",
    "difficulty": "5.10",
    "priority_index": "5.18",
    "cut_proposal": "FOI VAPH / OCMW Bertem / gemeente Bertem matrix behind 70/76A 1951718 and why 73 JUMP 1732649 while 9901 FLIP LOSS -3269 cash DROP 119855 FTE JUMP 24.1",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2524 leftover mined city_bertem leftover VAPH leftover-mined AGB-only after leftover WZC Sint-Bernardus@2523; leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2525 leftover dual; NOT leftover city_bertem leftover WZC Sint-Bernardus remine@2523; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Bertem>DeEglantier>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / OCMW Bertem / gemeente Bertem split behind 70/76A 1951718 and why 73 JUMP 1732649 while 9901 FLIP LOSS -3269 cash DROP 119855 FTE JUMP 24.1",
    "why_it_matters": "Strong official PDF leftover VAPH of mined leftover-mined AGB-only city_bertem; VKT-VZW envelope 70/76A 1.95m because omzet commercial-only vs large 73; leftover VAPH 1 VE official zetel Bertem; 73 JUMP 1.73m / pnl FLIP 18k / cash DROP 120k / 9901 FLIP LOSS 3k",
    "priority": "8",
    "recipient_body": "De Eglantier VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@eglantier.be",
    "recipient_postal": "Coige-steenweg 19 3061 Bertem",
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
    "notes": "tick2524; ready NOT sent; Strong official native NBB PDF; leftover mined city_bertem leftover VAPH leftover-mined AGB-only after leftover WZC Sint-Bernardus@2523; leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2525 leftover dual; off leftover city_bertem leftover WZC Sint-Bernardus remine@2523; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

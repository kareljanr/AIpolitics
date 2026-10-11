from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2519_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_ter_kempen_meerhout_jr2025_nbb_pdf_2519"
EID = "vzw_ter_kempen_meerhout"
GAP = "gap_ter_kempen_meerhout_wzc_matrix_bruto_3_19m_omzet73_empty_pnl_empty_cash_drop_55k_equity_drop_916k_l5"
COMM = "comm_ter_kempen_meerhout_jr2025_statutory_bruto_3_19m_omzet73_empty_pnl_empty_cash_drop_55k_equity_drop_916k"
LB = "lb_ter_kempen_meerhout_bruto_3_19m_omzet73_empty_pnl_empty_cash_drop_55k_equity_drop_916k_jr2025"

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
    "2025_opbr7076A": 0, "2025_bruto9900": 3190771,
    "2025_pnl": 0, "2025_bedrijfswinst": 8203, "2025_9903": 0,
    "2025_equity": 916229, "2025_assets": 2457213, "2025_debt": 1532610,
    "2025_fte": 40, "2025_fte9087": 40, "2025_kapitaalsubsidies": 916229,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 55356, "2025_geldbeleggingen": 0,
    "2025_personnel62": 2980040, "2025_gebouwen22": 2164947,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_fondsen10": 0,
    "2025_overgedragen14": 0, "2025_voorzieningen16": 8374,
    "2025_630": 186072, "2025_capex": 14001,
    "2025_6408": 16456, "2025_74": 0, "2025_733": 0,
    "2024_omzet": 0, "2024_73": 0, "2024_76A": 0,
    "2024_pnl": 0, "2024_bedrijfswinst": 8731,
    "2024_equity": 982917, "2024_assets": 2796334, "2024_debt": 1805042,
    "2024_cash": 83505, "2024_fte": 42.3, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 982917, "2024_geldbeleggingen": 0,
    "2024_bruto9900": 3077246,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Ter Kempen YE2025 (bruto JUMP 3.19m / omzet73 empty / pnl empty / cash DROP 55k / equity DROP 916k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg + leftover city_meerhout leftover WZC",
    "legal_basis": "Ter Kempen VZW (KBO 0871.619.135; Actief; 1 VE; official zetel Meerhout; RSZ2025 87.101)",
    "decision_date": "2026-06-04",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3190771",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00251692.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_meerhout",
    "cut_option": "Publish Departement Zorg / RIZIV / OCMW Meerhout matrix behind bruto 3.19m and why omzet73 empty while cash DROP 55k equity DROP 916k (entirely kapitaalsubsidies) FTE DROP 40 and pnl empty",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Meerhout>TerKempen>JR2025_statutory_L5",
    "notes": "tick2519; Strong official native PDF; leftover mined city_meerhout leftover WZC; 1 VE; prior-year identical; NOT leftover WZC De Berk OCMW; NOT leftover maatwerk De Sprong remine@2286; NOT leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142; NOT leftover city_herselt leftover WZC Sint-Barbara remine@2019; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Ter Kempen bruto JUMP 3.19m / omzet73 empty / pnl empty / cash DROP 55k / equity DROP 916k (YE2025 leftover city_meerhout leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Meerhout>TerKempen>JR2025",
    "annual_cost_eur": "3190771",
    "total_cost_eur": "3190771",
    "tco_notes": "PDF envelope bruto9900 3190771 JUMP because VKT and omzet empty; 70 empty; 73 empty; 76A empty; bedrijfswinst DROP 8203; pnl empty break-even; equity DROP 916229; assets DROP 2457213; debt DROP 1532610; FTE DROP 40; kapitaalsubsidies DROP 916229; destin691 empty; cash DROP 55356; leftover city_meerhout leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg + leftover city_meerhout leftover WZC",
    "stated_goal": "leftover WZC leftover city_meerhout",
    "measured_outcome": "3.19m bruto JUMP; omzet73 empty; pnl empty; cash DROP 55k; equity DROP 916k; leftover city_meerhout leftover WZC",
    "absurdity_score": "5.35",
    "cost_score": "5.10",
    "difficulty": "5.10",
    "priority_index": "5.25",
    "cut_proposal": "FOI Departement Zorg / RIZIV / OCMW Meerhout / gemeente Meerhout matrix behind bruto 3190771 and why omzet73 empty while cash DROP 55356 equity DROP 916229 (entirely kapitaalsubsidies) FTE DROP 40 and pnl empty",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2519 leftover mined city_meerhout leftover WZC after leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142 + leftover city_herselt leftover WZC Sint-Barbara remine@2019; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2520 leftover dual PLUS every-10; NOT leftover WZC De Berk OCMW; NOT leftover maatwerk De Sprong remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Meerhout>TerKempen>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / OCMW Meerhout / gemeente Meerhout split behind bruto 3190771 and why omzet73 empty while cash DROP 55356 equity DROP 916229 (entirely kapitaalsubsidies) FTE DROP 40 and pnl empty",
    "why_it_matters": "Strong official PDF leftover WZC of mined city_meerhout; VKT-VZW envelope bruto 3.19m because omzet73 empty; leftover WZC 1 VE official zetel Meerhout; cash DROP 55k / equity DROP 916k entirely kapitaalsubsidies / FTE DROP 40 / pnl empty",
    "priority": "8",
    "recipient_body": "Ter Kempen VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@terkempen.be",
    "recipient_postal": "Smissestraat 8 2450 Meerhout",
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
    "notes": "tick2519; ready NOT sent; Strong official native NBB PDF; leftover mined city_meerhout leftover WZC after leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142 + leftover city_herselt leftover WZC Sint-Barbara remine@2019; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2520 leftover dual PLUS every-10; off leftover WZC De Berk OCMW; off leftover maatwerk De Sprong remine; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

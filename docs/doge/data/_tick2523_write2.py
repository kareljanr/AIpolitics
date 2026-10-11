from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2523_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_sint_bernardus_bertem_jr2025_nbb_pdf_2523"
EID = "vzw_sint_bernardus_bertem"
GAP = "gap_sint_bernardus_bertem_wzc_matrix_omzet_14_53m_73_drop_2_66m_pnl_flip_loss_284k_cash_drop_1_26m_l5"
COMM = "comm_sint_bernardus_bertem_jr2025_statutory_omzet_14_53m_73_drop_2_66m_pnl_flip_loss_284k_cash_drop_1_26m"
LB = "lb_sint_bernardus_bertem_omzet_14_53m_73_drop_2_66m_pnl_flip_loss_284k_cash_drop_1_26m_jr2025"

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
    "2025_omzet": 14533086, "2025_73": 2661412, "2025_76A": 0,
    "2025_opbr7076A": 17532054, "2025_bruto9900": 0,
    "2025_pnl": -283512, "2025_bedrijfswinst": -254666, "2025_9903": -310218,
    "2025_equity": 11925827, "2025_assets": 17198350, "2025_debt": 5272522,
    "2025_fte": 189, "2025_fte100": 189, "2025_kapitaalsubsidies": 31528,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 1258185, "2025_geldbeleggingen": 4237589,
    "2025_personnel62": 13484952, "2025_gebouwen22": 6416495,
    "2025_aanbouw27": 2033423, "2025_66A": 118678, "2025_fondsen10": 2031437,
    "2025_overgedragen14": 4536144, "2025_voorzieningen16": 0,
    "2025_630": 1035591, "2025_capex": 1506779,
    "2025_6408": 10256, "2025_74": 337555, "2025_733": 0,
    "2024_omzet": 14696348, "2024_73": 3397449, "2024_76A": 0,
    "2024_pnl": 1398444, "2024_bedrijfswinst": 1390308,
    "2024_equity": 12234360, "2024_assets": 16794915, "2024_debt": 4560555,
    "2024_cash": 1727317, "2024_fte": 200.7, "2024_destin691": 1398444,
    "2024_kapitaalsubsidies": 56549, "2024_geldbeleggingen": 3920405,
    "2024_bruto9900": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Sint-Bernardus Bertem YE2025 (omzet DROP 14.53m / 73 DROP 2.66m / pnl FLIP LOSS 284k / cash DROP 1.26m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "Departement Zorg + leftover city_bertem leftover WZC",
    "legal_basis": "Woon en Zorgcentrum Sint-Bernardus Bertem VZW (KBO 0435.723.406; Actief; 2 VE; official zetel Bertem; RSZ2025 87.101 RVT)",
    "decision_date": "2026-06-25",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "14533086",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00268836.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_bertem",
    "cut_option": "Publish Departement Zorg / RIZIV / OCMW Bertem matrix behind omzet 14.53m and why 73 DROP 2.66m while pnl FLIP LOSS 284k cash DROP 1.26m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Bertem>SintBernardus>JR2025_statutory_L5",
    "notes": "tick2523; Strong official native PDF; leftover mined city_bertem leftover WZC leftover-mined AGB-only; 2 VE; prior-year identical; NOT leftover city_stabroek leftover WZC Aalmoezenier Cuypers remine@2522; NOT leftover WZC Sint-Bernardus Assenede remine; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Sint-Bernardus Bertem omzet DROP 14.53m / 73 DROP 2.66m / pnl FLIP LOSS 284k / cash DROP 1.26m (YE2025 leftover city_bertem leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Bertem>SintBernardus>JR2025",
    "annual_cost_eur": "14533086",
    "total_cost_eur": "14533086",
    "tco_notes": "PDF envelope omzet70 14533086 DROP because 70 present and not commercial-only vs 73; 73 DROP 2661412; 76A empty; bedrijfswinst FLIP LOSS -254666; pnl FLIP LOSS -283512; equity DROP 11925827; assets JUMP 17198350; debt JUMP 5272522; FTE DROP 189; kapitaalsubsidies DROP 31528; destin691 empty; cash DROP 1258185; geldbeleggingen JUMP 4237589; leftover city_bertem leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "Departement Zorg + leftover city_bertem leftover WZC",
    "stated_goal": "leftover WZC leftover city_bertem",
    "measured_outcome": "14.53m omzet DROP; 73 DROP 2.66m; pnl FLIP LOSS 284k; cash DROP 1.26m; leftover city_bertem leftover WZC",
    "absurdity_score": "5.60",
    "cost_score": "5.40",
    "difficulty": "5.15",
    "priority_index": "5.38",
    "cut_proposal": "FOI Departement Zorg / RIZIV / OCMW Bertem / gemeente Bertem matrix behind omzet 14533086 and why 73 DROP 2661412 while pnl FLIP LOSS -283512 cash DROP 1258185 FTE DROP 189",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2523 leftover mined city_bertem leftover WZC leftover-mined AGB-only after leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2524 leftover dual; NOT leftover city_stabroek leftover WZC Aalmoezenier Cuypers remine@2522; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Bertem>SintBernardus>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "Departement Zorg / RIZIV / OCMW Bertem / gemeente Bertem split behind omzet 14533086 and why 73 DROP 2661412 while pnl FLIP LOSS -283512 cash DROP 1258185 FTE DROP 189",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_bertem; VOL-VZW envelope omzet 14.53m because 70 present and not commercial-only; leftover WZC 2 VE official zetel Bertem; 73 DROP 2.66m / pnl FLIP LOSS 284k / cash DROP 1.26m / FTE DROP 189",
    "priority": "8",
    "recipient_body": "Woon en Zorgcentrum Sint-Bernardus Bertem VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "boekhouding@stbernardus.be",
    "recipient_postal": "Egenhovenstraat 22 3060 Bertem",
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
    "notes": "tick2523; ready NOT sent; Strong official native NBB PDF; leftover mined city_bertem leftover WZC leftover-mined AGB-only after leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 2 VE; prior-year identical; NOT every-10 (next every-10 2530); next rq_2524 leftover dual; off leftover city_stabroek leftover WZC Aalmoezenier Cuypers remine@2522; off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial; off Evara remine",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

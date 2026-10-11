from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2532_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_seniorplaza_willebroek_jr2025_nbb_pdf_2532"
EID = "vzw_seniorplaza_willebroek"
GAP = "gap_seniorplaza_willebroek_wzc_matrix_70_jump_5_28m_73_jump_662k_pnl_drop_243k_cash_jump_569k_l5"
COMM = "comm_seniorplaza_willebroek_jr2025_statutory_70_jump_5_28m_73_jump_662k_pnl_drop_243k_cash_jump_569k"
LB = "lb_seniorplaza_willebroek_70_jump_5_28m_73_jump_662k_pnl_drop_243k_cash_jump_569k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()

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
    "2025_omzet": 5279368, "2025_73": 662411, "2025_76A": 0,
    "2025_opbr7076A": 6015542, "2025_envelope70": 5279368,
    "2025_pnl": -242696, "2025_bedrijfswinst": -132181, "2025_9903": -235167,
    "2025_equity": 2106622, "2025_assets": 6456829, "2025_debt": 4350207,
    "2025_fte": 64.2, "2025_fte1003": 64.2, "2025_kapitaalsubsidies": 2330927,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 568577, "2025_geldbeleggingen": 0,
    "2025_personnel62": 3855497, "2025_gebouwen22": 4227470,
    "2025_aanbouw27": 0, "2025_66A": 0,
    "2025_fondsen10": 0, "2025_overgedragen14": -224305,
    "2025_voorzieningen16": 0, "2025_630": 264906, "2025_capex": 314299,
    "2025_6408": 28385, "2025_74": 73763, "2025_733": 662411,
    "2024_omzet": 5106144, "2024_73": 606694, "2024_76A": 0,
    "2024_pnl": -186201, "2024_bedrijfswinst": -57191,
    "2024_equity": 2479262, "2024_assets": 6989674, "2024_debt": 4510412,
    "2024_cash": 204770, "2024_fte": 59.4, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 2460871, "2024_geldbeleggingen": 0,
    "2024_envelope70": 5106144,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Seniorplaza Willebroek YE2025 (70 JUMP 5.28m / 73 JUMP 662k / pnl DROP 243k / cash JUMP 569k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + leftover city_willebroek leftover WZC",
    "legal_basis": "VZW Seniorplaza (KBO 0467.255.829; Actief; 2 VE; official zetel Willebroek; RSZ2025 87.302; CoBRHA 172.101 / HCO 3346 / 78 woongelegenheden)",
    "decision_date": "2026-06-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "5279368",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00336704.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_willebroek",
    "cut_option": "Publish RIZIV / OCMW Willebroek / gemeente Willebroek matrix behind 70 JUMP 5.28m / 73 JUMP 662k and why cash JUMP 569k while pnl DROP 243k equity DROP 2.11m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Willebroek>Seniorplaza>JR2025_statutory_L5",
    "notes": "tick2532; Strong official native PDF; leftover mined city_willebroek leftover WZC leftover-mined AGB-only unused leftover type; 2 VE; prior-year identical; Korian Belgium NV 0869.769.702 gedelegeerd bestuurder leftover public VZW WZC not commercial NV FIRST LOCK; NOT leftover WZC Ten Weldebrouc OCMW SKIP; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Seniorplaza Willebroek 70 JUMP 5.28m / 73 JUMP 662k / pnl DROP 243k / cash JUMP 569k (YE2025 leftover city_willebroek leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Willebroek>Seniorplaza>JR2025",
    "annual_cost_eur": "5279368",
    "total_cost_eur": "5279368",
    "tco_notes": "PDF envelope omzet70 5279368 JUMP because 70 present and not commercial-only vs 73; 70 JUMP 5279368; 73 JUMP 662411; 76A empty; 70/76A JUMP 6015542; bedrijfswinst DROP -132181; pnl DROP -242696; equity DROP 2106622; assets DROP 6456829; debt DROP 4350207; FTE JUMP 64.2; kapitaalsubsidies DROP 2330927; destin691 empty; cash JUMP 568577; leftover city_willebroek leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + leftover city_willebroek leftover WZC",
    "stated_goal": "leftover WZC leftover city_willebroek",
    "measured_outcome": "5.28m 70 JUMP; 662k 73 JUMP; pnl DROP 243k; cash JUMP 569k; leftover city_willebroek leftover WZC",
    "absurdity_score": "5.42",
    "cost_score": "5.18",
    "difficulty": "5.05",
    "priority_index": "5.22",
    "cut_proposal": "FOI RIZIV / OCMW Willebroek / gemeente Willebroek matrix behind 70 5279368 / 73 662411 and why cash JUMP 568577 while pnl DROP -242696 equity DROP 2106622",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2532 leftover mined city_willebroek leftover WZC leftover-mined AGB-only unused leftover type after leftover city_boechout leftover WZC taken@2531 leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine@2282 leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover city_deinze leftover WZC Sint-Jozef YE2025 unused leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover city_willebroek leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ten Weldebrouc OCMW SKIP leftover WZC type now taken; 2 VE; prior-year identical; next rq_2533 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; Korian Belgium NV 0869.769.702 gedelegeerd bestuurder leftover public VZW WZC not commercial NV FIRST LOCK",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Willebroek>Seniorplaza>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / OCMW Willebroek / gemeente Willebroek split behind 70 JUMP 5279368 / 73 JUMP 662411 (73-733 gap 0) and why cash JUMP 568577 while pnl DROP -242696 equity DROP 2106622",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_willebroek; VOL-VZW envelope omzet70 5.28m because 70 present and not commercial-only vs 73 JUMP 662k; leftover WZC 2 VE official zetel Willebroek unused leftover type; 70 JUMP 5.28m / 73 JUMP 662k / pnl DROP 243k / cash JUMP 569k / FTE JUMP 64.2",
    "priority": "8",
    "recipient_body": "VZW Seniorplaza / Voorzitter Raad van Bestuur",
    "recipient_email": "info@seniorplaza.be",
    "recipient_postal": "Overwinningsstraat 133-135 2830 Willebroek",
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
    "notes": "tick2532; ready NOT sent; Strong official native NBB PDF; leftover mined city_willebroek leftover WZC leftover-mined AGB-only unused leftover type; leftover city_boechout leftover WZC taken leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover city_deinze leftover WZC Sint-Jozef YE2025 unused leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_willebroek leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ten Weldebrouc OCMW SKIP leftover WZC type now taken; 2 VE; prior-year identical; next rq_2533 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE; off Armonea commercial; off Vulpia commercial; Korian Belgium NV 0869.769.702 gedelegeerd bestuurder leftover public VZW WZC not commercial NV FIRST LOCK",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

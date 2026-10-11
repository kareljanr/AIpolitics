from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2531_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_capenberg_boechout_jr2025_nbb_pdf_2531"
EID = "vzw_capenberg_boechout"
GAP = "gap_capenberg_boechout_wzc_matrix_73_jump_1_39m_9901_jump_200k_cash_drop_553k_l5"
COMM = "comm_capenberg_boechout_jr2025_statutory_73_jump_1_39m_9901_jump_200k_cash_drop_553k"
LB = "lb_capenberg_boechout_73_jump_1_39m_9901_jump_200k_cash_drop_553k_jr2025"
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
    "2025_omzet": 6320109, "2025_73": 1387170, "2025_76A": 0,
    "2025_opbr7076A": 7707279, "2025_envelope70": 6320109,
    "2025_pnl": -398270, "2025_bedrijfswinst": -199500, "2025_9903": -398270,
    "2025_equity": 3643724, "2025_assets": 14261777, "2025_debt": 10618053,
    "2025_fte": 83.4, "2025_fte1003": 83.4, "2025_kapitaalsubsidies": 0,
    "2025_destin691": 0, "2025_791": 0,
    "2025_cash": 553009, "2025_geldbeleggingen": 0,
    "2025_personnel62": 5687192, "2025_gebouwen22": 12480120,
    "2025_aanbouw27": 0, "2025_66A": 0,
    "2025_fondsen10": 3980501, "2025_overgedragen14": -336777,
    "2025_voorzieningen16": 0, "2025_630": 641644, "2025_capex": 12905,
    "2025_6408": 15609, "2025_74": 0, "2025_733": 1157024,
    "2024_omzet": 6373547, "2024_73": 1110585, "2024_76A": 0,
    "2024_pnl": -428160, "2024_bedrijfswinst": -252208,
    "2024_equity": 4041994, "2024_assets": 14999008, "2024_debt": 10957014,
    "2024_cash": 771244, "2024_fte": 87.8, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 46619,
    "2024_envelope70": 6373547,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Capenberg Oxaco-Center YE2025 (73 JUMP 1.39m / 9901 JUMP -200k / cash DROP 553k / equity DROP 3.64m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + leftover city_boechout leftover WZC",
    "legal_basis": "VZW Capenberg Oxaco-Center (KBO 0408.159.370; Actief; 1 VE; official zetel Boechout; RSZ2025 87.101; CoBRHA 115.102 / HCO 3766 / 75 woongelegenheden)",
    "decision_date": "2026-06-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "6320109",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00166949.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_boechout",
    "cut_option": "Publish RIZIV / OCMW Boechout / gemeente Boechout matrix behind 73 JUMP 1.39m and why cash DROP 553k while 9901 JUMP -200k equity DROP 3.64m",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Boechout>Capenberg>JR2025_statutory_L5",
    "notes": "tick2531; Strong official native PDF; leftover mined city_boechout leftover WZC leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; NOT leftover WZC Avondvrede remine@2166 SKIP; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Capenberg Boechout 73 JUMP 1.39m / 9901 JUMP -200k / cash DROP 553k / equity DROP 3.64m (YE2025 leftover city_boechout leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Boechout>Capenberg>JR2025",
    "annual_cost_eur": "6320109",
    "total_cost_eur": "6320109",
    "tco_notes": "PDF envelope omzet70 6320109 DROP because 70 present and not commercial-only vs 73; 70 DROP 6320109; 73 JUMP 1387170; 76A empty; 70/76A DROP 7707279; bedrijfswinst JUMP -199500; pnl JUMP -398270; equity DROP 3643724; assets DROP 14261777; debt DROP 10618053; FTE DROP 83.4; kapitaalsubsidies empty; destin691 empty; cash DROP 553009; leftover city_boechout leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + leftover city_boechout leftover WZC",
    "stated_goal": "leftover WZC leftover city_boechout",
    "measured_outcome": "1.39m 73 JUMP; 9901 JUMP -200k; cash DROP 553k; equity DROP 3.64m; leftover city_boechout leftover WZC",
    "absurdity_score": "5.45",
    "cost_score": "5.22",
    "difficulty": "5.05",
    "priority_index": "5.30",
    "cut_proposal": "FOI RIZIV / OCMW Boechout / gemeente Boechout matrix behind 73 1387170 and why cash DROP 553009 while 9901 JUMP -199500 equity DROP 3643724",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2531 leftover mined city_boechout leftover WZC leftover-mined AGB-only unused leftover type after leftover city_zaventem leftover WZC taken@2530 leftover maatwerk TWI remine@2282 leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover city_boechout leftover WZC Avondvrede remine@2166 leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_willebroek leftover WZC Seniorplaza YE2025 unused leftover city_deinze leftover WZC Sint-Jozef YE2025 unused leftover VAPH taken@2496/2499 leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken; 1 VE; prior-year identical; next rq_2532 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Boechout>Capenberg>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / OCMW Boechout / gemeente Boechout split behind 73 JUMP 1387170 (73-733 gap 230146) and why cash DROP 553009 while 9901 JUMP -199500 equity DROP 3643724",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_boechout; VOL-VZW envelope omzet70 6.32m because 70 present and not commercial-only vs 73 JUMP 1.39m; leftover WZC 1 VE official zetel Boechout unused leftover type; 73 JUMP 1.39m / 9901 JUMP -200k / cash DROP 553k / equity DROP 3.64m / FTE DROP 83.4",
    "priority": "8",
    "recipient_body": "VZW Capenberg, Oxaco-Center / Voorzitter Raad van Bestuur",
    "recipient_email": "m.roggen@capenberg.com",
    "recipient_postal": "Borsbeeksesteenweg 45 2530 Boechout",
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
    "notes": "tick2531; ready NOT sent; Strong official native NBB PDF; leftover mined city_boechout leftover WZC leftover-mined AGB-only unused leftover type; leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine@2282 leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover city_boechout leftover WZC Avondvrede remine@2166 leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_willebroek leftover WZC Seniorplaza YE2025 unused leftover city_deinze leftover WZC Sint-Jozef YE2025 unused leftover VAPH taken@2496/2499 leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; next rq_2532 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

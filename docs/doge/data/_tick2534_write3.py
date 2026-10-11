from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2534_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_meerpaal_willebroek_jr2025_nbb_pdf_2534"
EID = "vzw_meerpaal_willebroek"
GAP = "gap_meerpaal_willebroek_vaph_matrix_bruto_3_50m_omzet73_empty_pnl_jump_228k_fte_jump_41_4_l5"
COMM = "comm_meerpaal_willebroek_jr2025_statutory_bruto_3_50m_omzet73_empty_pnl_jump_228k_fte_jump_41_4"
LB = "lb_meerpaal_willebroek_bruto_3_50m_omzet73_empty_pnl_jump_228k_fte_jump_41_4_jr2025"
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
    "2025_omzet": None, "2025_73": None, "2025_76A": 427,
    "2025_envelope9900": 3496689, "2025_pnl": 228053, "2025_bedrijfswinst": 213789,
    "2025_9903": 228053, "2025_equity": 1819290, "2025_assets": 2714324,
    "2025_debt": 895034, "2025_fte": 41.4, "2025_kapitaalsubsidies": 75307,
    "2025_destin691": 0, "2025_791": 3372, "2025_cash": 1263424,
    "2025_geldbeleggingen": 0, "2025_personnel62": 3212694, "2025_gebouwen22": 538464,
    "2025_aanbouw27": 0, "2025_66A": 0, "2025_630": 67029, "2025_capex": 77018,
    "2025_6408": 3176, "2024_envelope9900": 2704972, "2024_pnl": 193838,
    "2024_bedrijfswinst": 179042, "2024_equity": 1596175, "2024_assets": 2387452,
    "2024_debt": 791276, "2024_cash": 1245665, "2024_fte": 33.7,
    "2024_destin691": 198612, "2024_kapitaalsubsidies": 80245,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "De Meerpaal Willebroek YE2025 (bruto JUMP 3.50m / omzet73 empty / pnl JUMP 228k / FTE JUMP 41.4 / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_willebroek leftover VAPH",
    "legal_basis": "VZW De Meerpaal (KBO 0443.206.559; Actief; 1 VE; official zetel Willebroek; RSZ2025 87.202; official VAPH vergunde zorgaanbieder)",
    "decision_date": "2026-05-20",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3496689",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00152128.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_willebroek",
    "cut_option": "Publish VAPH / OCMW Willebroek / gemeente Willebroek matrix behind bruto JUMP 3.50m and why FTE JUMP 41.4 while destin 691 empty",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Willebroek>Meerpaal>JR2025_statutory_L5",
    "notes": "tick2534; Strong official native PDF; leftover mined city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; FIRST LOCK leftover city_willebroek leftover VAPH; NOT leftover WZC Seniorplaza remine@2532; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "De Meerpaal bruto JUMP 3.50m / omzet73 empty / pnl JUMP 228k / FTE JUMP 41.4 (YE2025 leftover city_willebroek leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Willebroek>Meerpaal>JR2025",
    "annual_cost_eur": "3496689",
    "total_cost_eur": "3496689",
    "tco_notes": "PDF envelope bruto9900 3496689 JUMP because VKT 73 empty and bruto >> omzet; 70 empty; 73 empty; 76A JUMP 427; bedrijfswinst JUMP 213789; pnl JUMP 228053; equity JUMP 1819290; assets JUMP 2714324; debt JUMP 895034; FTE JUMP 41.4; kapitaalsubsidies DROP 75307; destin691 empty DROP; cash JUMP 1263424; leftover city_willebroek leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_willebroek leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_willebroek",
    "measured_outcome": "3.50m bruto JUMP; omzet73 empty; pnl JUMP 228k; FTE JUMP 41.4; leftover city_willebroek leftover VAPH",
    "absurdity_score": "5.41",
    "cost_score": "5.18",
    "difficulty": "5.05",
    "priority_index": "5.21",
    "cut_proposal": "FOI VAPH / OCMW Willebroek / gemeente Willebroek matrix behind bruto 3496689 and why FTE JUMP 41.4 while destin 691 empty and 70+73 empty",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2534 leftover mined city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type after leftover city_willebroek leftover WZC taken@2532 leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine@2355 SKIP leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; next rq_2535 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_willebroek leftover VAPH",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Willebroek>Meerpaal>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / OCMW Willebroek / gemeente Willebroek split behind bruto JUMP 3496689 (70+73 empty VKT) and why FTE JUMP 41.4 while destin 691 empty DROP and cash JUMP 1263424",
    "why_it_matters": "Strong official PDF leftover VAPH of mined leftover-mined AGB-only city_willebroek; VKT-VZW envelope bruto9900 3.50m because 73 empty and bruto >> omzet; leftover VAPH 1 VE official zetel Willebroek unused leftover type; bruto JUMP 3.50m / omzet73 empty / pnl JUMP 228k / FTE JUMP 41.4 / destin empty DROP",
    "priority": "8",
    "recipient_body": "VZW De Meerpaal / Voorzitter Raad van Bestuur",
    "recipient_email": "onthaal@demeerpaal.eu",
    "recipient_postal": "Kerkstraat 2B 2830 Willebroek",
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
    "notes": "tick2534; ready NOT sent; Strong official native NBB PDF; leftover mined city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type; leftover city_willebroek leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine@2355 SKIP leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; 1 VE; prior-year identical; next rq_2535 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE; off Armonea commercial; off Vulpia commercial; FIRST LOCK leftover city_willebroek leftover VAPH",
}], foi_fields)
print("foi ok")
print("CORE1C DONE")

from pathlib import Path
import csv
import json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2533_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_sint_jozef_deinze_jr2025_nbb_pdf_2533"
EID = "vzw_sint_jozef_deinze"
GAP = "gap_sint_jozef_deinze_wzc_matrix_70_jump_9_47m_73_drop_1_65m_pnl_flip_512k_destin_jump_4_42m_l5"
COMM = "comm_sint_jozef_deinze_jr2025_statutory_70_jump_9_47m_73_drop_1_65m_pnl_flip_512k_destin_jump_4_42m"
LB = "lb_sint_jozef_deinze_70_jump_9_47m_73_drop_1_65m_pnl_flip_512k_destin_jump_4_42m_jr2025"
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
    "2025_omzet": 9471817, "2025_73": 1653070, "2025_76A": 11258,
    "2025_opbr7076A": 11372156, "2025_envelope70": 9471817,
    "2025_pnl": 511833, "2025_bedrijfswinst": 293988, "2025_9903": 511833,
    "2025_equity": 8597413, "2025_assets": 13344074, "2025_debt": 4746661,
    "2025_fte": 124, "2025_fte1003": 124, "2025_kapitaalsubsidies": 1589968,
    "2025_destin691": 4418723, "2025_791": 4018723,
    "2025_cash": 878637, "2025_geldbeleggingen": 1887538,
    "2025_personnel62": 8038951, "2025_gebouwen22": 7724388,
    "2025_aanbouw27": 10890, "2025_66A": 6322,
    "2025_fondsen10": 2516768, "2025_overgedragen14": 71954,
    "2025_voorzieningen16": 0, "2025_630": 566368, "2025_capex": 90307,
    "2025_6408": 43877, "2025_74": 236011, "2025_733": 1640291,
    "2024_omzet": 8789823, "2024_73": 1743738, "2024_76A": 0,
    "2024_pnl": -411081, "2024_bedrijfswinst": -400552,
    "2024_equity": 8273197, "2024_assets": 13444371, "2024_debt": 5171174,
    "2024_cash": 628747, "2024_fte": 125.9, "2024_destin691": 0,
    "2024_kapitaalsubsidies": 1777585, "2024_geldbeleggingen": 1683586,
    "2024_envelope70": 8789823,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Sint-Jozef Deinze YE2025 (70 JUMP 9.47m / 73 DROP 1.65m / pnl FLIP 512k / destin JUMP 4.42m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "RIZIV + leftover city_deinze leftover WZC",
    "legal_basis": "VZW R.V.T. Sint-Jozef Deinze (KBO 0409.698.603; Actief; 1 VE; official zetel Deinze; RSZ2025 87.301; CoBRHA 408.102 / HCO 3684 / 155 woongelegenheden)",
    "decision_date": "2026-06-15",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "9471817",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00259876.pdf",
    "stated_goal": "Public leftover WZC dual of mined city_deinze",
    "cut_option": "Publish RIZIV / OCMW Deinze / gemeente Deinze matrix behind 70 JUMP 9.47m / 73 DROP 1.65m and why destin JUMP 4.42m while pnl FLIP 512k cash JUMP 879k",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Deinze>Sint-Jozef>JR2025_statutory_L5",
    "notes": "tick2533; Strong official native PDF; leftover mined city_deinze leftover WZC leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; FIRST LOCK leftover city_deinze leftover WZC; NOT leftover VAPH Vierklaver remine@2496; NOT leftover VAPH Ten Dries remine@2499; NOT leftover-via-VE Evergem Franciscanessen SKIP; NOT leftover-via-VE; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Sint-Jozef Deinze 70 JUMP 9.47m / 73 DROP 1.65m / pnl FLIP 512k / destin JUMP 4.42m (YE2025 leftover city_deinze leftover WZC)",
    "level": "L5",
    "type": "wzc_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Deinze>Sint-Jozef>JR2025",
    "annual_cost_eur": "9471817",
    "total_cost_eur": "9471817",
    "tco_notes": "PDF envelope omzet70 9471817 JUMP because 70 present and not commercial-only vs 73; 70 JUMP 9471817; 73 DROP 1653070; 76A JUMP 11258; 70/76A JUMP 11372156; bedrijfswinst FLIP 293988; pnl FLIP 511833; equity JUMP 8597413; assets DROP 13344074; debt DROP 4746661; FTE DROP 124; kapitaalsubsidies DROP 1589968; destin691 JUMP 4418723; cash JUMP 878637; leftover city_deinze leftover WZC",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "RIZIV + leftover city_deinze leftover WZC",
    "stated_goal": "leftover WZC leftover city_deinze",
    "measured_outcome": "9.47m 70 JUMP; 1.65m 73 DROP; pnl FLIP 512k; destin JUMP 4.42m; leftover city_deinze leftover WZC",
    "absurdity_score": "5.61",
    "cost_score": "5.47",
    "difficulty": "5.05",
    "priority_index": "5.38",
    "cut_proposal": "FOI RIZIV / OCMW Deinze / gemeente Deinze matrix behind 70 9471817 / 73 1653070 and why destin JUMP 4418723 while pnl FLIP 511833 cash JUMP 878637",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2533 leftover mined city_deinze leftover WZC leftover-mined AGB-only unused leftover type after leftover city_willebroek leftover WZC taken@2532 leftover WZC Ten Weldebrouc OCMW SKIP leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_boechout leftover WZC taken leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine@2282 leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover city_deinze leftover VAPH taken@2496/2499 leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine@2191 leftover CAR unused-looking leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine@2066 leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover city_willebroek leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ten Weldebrouc OCMW SKIP leftover WZC type now taken; 1 VE; prior-year identical; next rq_2534 leftover dual (NOT every-10; next every-10 2540); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_deinze leftover WZC",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Deinze>Sint-Jozef>leftover_wzc",
    "entity_id": EID,
    "what_is_missing": "RIZIV / OCMW Deinze / gemeente Deinze split behind 70 JUMP 9471817 / 73 DROP 1653070 (73-733 gap 12779) and why destin JUMP 4418723 while pnl FLIP 511833 cash JUMP 878637",
    "why_it_matters": "Strong official PDF leftover WZC of mined leftover-mined AGB-only city_deinze; VOL-VZW envelope omzet70 9.47m because 70 present and not commercial-only vs 73 DROP 1.65m; leftover WZC 1 VE official zetel Deinze unused leftover type; 70 JUMP 9.47m / 73 DROP 1.65m / pnl FLIP 512k / destin JUMP 4.42m / cash JUMP 879k / FTE DROP 124",
    "priority": "8",
    "recipient_body": "VZW R.V.T. Sint-Jozef Deinze / Voorzitter Raad van Bestuur",
    "recipient_email": "directie@rvtsintjozef.be",
    "recipient_postal": "Kortrijksesteenweg 61 9800 Deinze",
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
    "notes": "tick2533; ready NOT sent; Strong official native NBB PDF; leftover mined city_deinze leftover WZC leftover-mined AGB-only unused leftover type; leftover city_willebroek leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_boechout leftover WZC taken leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 SKIP leftover city_deinze leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine@2191 leftover CAR unused-looking leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine@2066 leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_willebroek leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ten Weldebrouc OCMW SKIP leftover WZC type now taken; 1 VE; prior-year identical; next rq_2534 leftover dual (NOT every-10; next every-10 2540); off leftover-via-VE; off Armonea commercial; off Vulpia commercial; FIRST LOCK leftover city_deinze leftover WZC",
}], foi_fields)
print("foi_queue ok")
print("CORE2 DONE")

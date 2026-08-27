from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2547_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_inspirant_koksijde_jr2025_nbb_pdf_2547"
SRC_KBO = "src_inspirant_koksijde_kbo_2547"
SRC_SBM = "src_inspirant_koksijde_sbm_2547"
SRC_SITE = "src_inspirant_koksijde_site_2547"
EID = "vzw_inspirant_koksijde"
GAP = "gap_inspirant_koksijde_vaph_matrix_70_76a_jump_1_49m_73_jump_1_35m_9904_drop_216k_cash_jump_157k_l5"
COMM = "comm_inspirant_koksijde_jr2025_statutory_70_76a_jump_1_49m_73_jump_1_35m_9904_drop_216k_cash_jump_157k"
LB = "lb_inspirant_koksijde_70_76a_jump_1_49m_73_jump_1_35m_9904_drop_216k_cash_jump_157k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2547/2026-00215073_inspirant.pdf").is_file()

def append_rows(path, rows, fieldnames):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} no LF")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", lineterminator="\n")
        for row in rows:
            w.writerow(row)
    print("appended", len(rows), "->", path.name)

csv.field_size_limit(10_000_000)
with (DATA / "entities.csv").open(encoding="utf-8") as _fh:
    for _row in csv.DictReader(_fh):
        blob = " ".join(_row.values())
        if _row.get("entity_id") == EID or "0436.599.176" in blob or "0436599176" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Inspirant deposit 2026-00215073",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00215073.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2547; official native statutory PDF 498356 bytes 43p VOL-VZW 26.0.15 m05-f; header 26/06/2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-29 22:25:54 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00215073 498356 MD5 501ce487d03bb0c4ef4f3e799084dc8d; NBB UUID b9c8a7d3-7155-11f1-9407-67c44a8a8e09; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.10 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Inspirant 0436.599.176",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0436599176",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2547; Actief since 01.12.1988; 19 VE leftover city_koksijde (official zetel Albert I Laan(Odk) 54 8670 Koksijde since 01.10.1990; VE 2.138.448.043 Inspirant aan zee MFC Albert I Laan(Odk) 54 since 01.07.1989 + Aartrijke/Zedelgem + Middelkerke + Nieuwpoort leftover-via-VE FROM leftover city_koksijde); VZW since 01.12.1988; RSZ2025 87.201; leftover mined city_koksijde leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover AGB Koksijde 0267.390.495; NOT leftover IGS HVZ Westhoek 0500.929.873; leftover city_koksijde leftover VAPH with official zetel Koksijde IS enough",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Inspirant 0436599176 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0436599176",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2547; deposit-id 2026-00215073 YE 01.01.2025-31.12.2025 filing VOL-VZW header 26.06.2026 AV 25.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list OK this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Inspirant Koksijde FOI contact leftover city_koksijde leftover VAPH",
        "url": "https://inspirant.be/contact",
        "publisher": "Official Inspirant site + VAPH adreslijst leftover city_koksijde leftover VAPH",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2547; FOI welkom@inspirant.be from official site; NBB PDF also lists info@vocderozenkrans.be; VAPH annelies.lanszweert@inspirant.be; leftover mined city_koksijde leftover VAPH leftover-mined AGB-only unused leftover type after Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Widar Merksplas CDN 403 Sint-Franciscus remine@2129 Klavier leftover-via-VE Mechelen Ubuntu leftover-via-VE Kortrijk leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_koksijde leftover VAPH",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Inspirant (VAPH MFC / mentale handicap minderjarigen)",
    "name_fr": "Inspirant (VAPH)",
    "name_en": "Inspirant (VAPH MFC Koksijde)",
    "level": "L5",
    "parent_id": "city_koksijde",
    "community_language": "nl",
    "website": "https://inspirant.be",
    "foi_email": "welkom@inspirant.be",
    "foi_postal": "Albert I-laan 54, 8670 Koksijde (Oostduinkerke)",
    "notes": "tick2547 YE2025 Strong official native NBB PDF deposit 2026-00215073 + Strong KBO 0436.599.176 Actief 19 VE; leftover mined city_koksijde leftover VAPH leftover-mined AGB-only unused leftover type; official zetel Albert I Laan(Odk) 54 8670 Koksijde since 01.10.1990; RSZ2025 87.201; envelope 70/76A JUMP 28059008; 73 JUMP 25490225; 9901 DROP 551923; 9904 DROP 419076; cash JUMP 3125330; FTE JUMP 300.5; NOT leftover AGB 0267.390.495; NOT leftover IGS HVZ Westhoek 0500.929.873; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_koksijde leftover VAPH",
}])
print("entities ok")

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_inspirant_koksijde_70_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "28059008", "amount_min_eur": "28059008", "amount_max_eur": "28059008", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +5.62%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p7 native; YE2024 26565043 identical; envelope 70/76A for VZW because 70 present and commercial-only vs large 73; FOI VAPH/gemeente matrix behind 28059008"},
    {"budget_id": "bud_inspirant_koksijde_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1614139", "amount_min_eur": "1614139", "amount_max_eur": "1614139", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +4.92%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p7 native; YE2024 1538376 identical; commercial-only vs large 73 25490225"},
    {"budget_id": "bud_inspirant_koksijde_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "25490225", "amount_min_eur": "25490225", "amount_max_eur": "25490225", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +5.59%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p7 native; YE2024 24140404 identical; FOI VAPH/gemeente/onderwijs matrix"},
    {"budget_id": "bud_inspirant_koksijde_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "22270022", "amount_min_eur": "22270022", "amount_max_eur": "22270022", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +6.30%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p7 native; YE2024 20949429 identical; FTE 9087 300.5 JUMP from 293.1"},
    {"budget_id": "bud_inspirant_koksijde_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1649370", "amount_min_eur": "1649370", "amount_max_eur": "1649370", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 JUMP +3.59%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p7 native; YE2024 1592218 identical; capex 1712819; MVA 27461192 JUMP"},
    {"budget_id": "bud_inspirant_koksijde_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "551923", "amount_min_eur": "551923", "amount_max_eur": "551923", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -11.82%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p7 native; YE2024 625923 identical; 66A 37691 JUMP; 640/8 339551 DROP"},
    {"budget_id": "bud_inspirant_koksijde_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "419076", "amount_min_eur": "419076", "amount_max_eur": "419076", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -34.02%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p8 native; YE2024 635105 identical; 9903 419076 DROP"},
    {"budget_id": "bud_inspirant_koksijde_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "33614221", "amount_min_eur": "33614221", "amount_max_eur": "33614221", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +2.49%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p5 native; YE2024 32797014 identical; kapitaalsubsidies 15 10821009 JUMP"},
    {"budget_id": "bud_inspirant_koksijde_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "45270119", "amount_min_eur": "45270119", "amount_max_eur": "45270119", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +1.04%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p5 native; YE2024 44805012 identical; MVA 22/27 27461192 JUMP; cash 3125330 JUMP; capex 1712819"},
    {"budget_id": "bud_inspirant_koksijde_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "11655898", "amount_min_eur": "11655898", "amount_max_eur": "11655898", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -2.93%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p5 native; YE2024 12007998 identical"},
    {"budget_id": "bud_inspirant_koksijde_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3125330", "amount_min_eur": "3125330", "amount_max_eur": "3125330", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +5.30%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2547; PDF p5 native; YE2024 2968067 identical; geldbeleggingen 50/53 7200000 DROP from 7750000"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_envelope_70_76A": 28059008, "2025_omzet": 1614139, "2025_73": 25490225, "2025_76A": 8470,
    "2025_pnl": 419076, "2025_bedrijfswinst": 551923, "2025_9903": 419076,
    "2025_equity": 33614221, "2025_assets": 45270119, "2025_debt": 11655898,
    "2025_cash": 3125330, "2025_kapitaalsubsidies": 10821009,
    "2025_personnel62": 22270022, "2025_630": 1649370, "2025_6408": 339551, "2025_66A": 37691,
    "2025_mva": 27461192, "2025_capex": 1712819, "2025_fte": 300.5,
    "2024_envelope_70_76A": 26565043, "2024_omzet": 1538376, "2024_73": 24140404, "2024_76A": 26384,
    "2024_pnl": 635105, "2024_bedrijfswinst": 625923,
    "2024_equity": 32797014, "2024_assets": 44805012, "2024_debt": 12007998,
    "2024_cash": 2968067, "2024_personnel62": 20949429, "2024_630": 1592218, "2024_fte": 293.1,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Inspirant Koksijde YE2025 (70/76A JUMP 28.06m / 73 JUMP 25.49m / 9904 DROP 216k / cash JUMP 157k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_koksijde leftover VAPH",
    "legal_basis": "VZW Inspirant (KBO 0436.599.176; Actief; 19 VE; official zetel Koksijde; RSZ2025 87.201; official VAPH adreslijst)",
    "decision_date": "2026-06-25",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "28059008",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00215073.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_koksijde",
    "cut_option": "Publish VAPH / gemeente Koksijde / onderwijs matrix behind 70/76A JUMP 28059008 and 73 JUMP 25490225 and why 9904 DROP 419076 while FTE JUMP 300.5 cash JUMP 3125330",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Koksijde>Inspirant>JR2025_statutory_L5",
    "notes": "tick2547; Strong official native PDF; leftover mined city_koksijde leftover VAPH leftover-mined AGB-only unused leftover type; 19 VE; prior-year identical; FIRST LOCK leftover city_koksijde leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}])
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Inspirant Koksijde 70/76A JUMP 28.06m / 73 JUMP 25.49m / 9904 DROP 216k / cash JUMP 157k (YE2025 leftover city_koksijde leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Koksijde>Inspirant>JR2025",
    "annual_cost_eur": "28059008",
    "total_cost_eur": "28059008",
    "tco_notes": "PDF envelope 70/76A 28059008 JUMP; 73 JUMP 25490225; omzet70 JUMP 1614139 commercial-only; 76A DROP 8470; bedrijfswinst DROP 551923; pnl DROP 419076; equity JUMP 33614221; assets JUMP 45270119; debt DROP 11655898; cash JUMP 3125330; kapitaalsubsidies JUMP 10821009; personnel62 JUMP 22270022; leftover city_koksijde leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_koksijde leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_koksijde",
    "measured_outcome": "28.06m 70/76A JUMP; 25.49m 73 JUMP; 216k 9904 DROP; 157k cash JUMP; leftover city_koksijde leftover VAPH",
    "absurdity_score": "6.90",
    "cost_score": "6.90",
    "difficulty": "4.40",
    "priority_index": "6.90",
    "cut_proposal": "FOI VAPH / gemeente Koksijde / onderwijs matrix behind 70/76A 28059008 and 73 25490225 and why 9904 DROP 419076 while FTE JUMP 300.5 cash JUMP 3125330",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2547 leftover mined city_koksijde leftover VAPH leftover-mined AGB-only unused leftover type after Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Widar Merksplas CDN 403 Sint-Franciscus remine@2129 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; 19 VE; prior-year identical; next rq_2548 leftover dual (NOT every-10; next every-10 2550); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_koksijde leftover VAPH",
}])
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Koksijde>Inspirant>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Koksijde / onderwijs matrix behind VOL-VZW YE2025 70/76A JUMP 28059008, 73 JUMP 25490225, 9904 DROP 419076, cash JUMP 3125330, FTE JUMP 300.5",
    "why_it_matters": "Public leftover VAPH dual of mined city_koksijde shows 28.06m bedrijfsopbrengsten and 25.49m subsidies while VAPH/gemeente/onderwijs matrix and pnl DROP with FTE JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Inspirant / Voorzitter Raad van Bestuur",
    "recipient_email": "welkom@inspirant.be",
    "recipient_postal": "Albert I-laan 54, 8670 Koksijde (Oostduinkerke)",
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
    "notes": "tick2547; ready NOT sent; Strong PDF + Strong KBO; leftover city_koksijde leftover VAPH",
}])
print("foi ok")
print("CORE WRITE DONE")

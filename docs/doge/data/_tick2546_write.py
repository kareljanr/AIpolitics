from pathlib import Path
import csv, json, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2546_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_wiric_sint_truiden_jr2025_nbb_pdf_2546"
SRC_KBO = "src_wiric_sint_truiden_kbo_2546"
SRC_SBM = "src_wiric_sint_truiden_sbm_2546"
SRC_SITE = "src_wiric_sint_truiden_site_2546"
EID = "vzw_wiric_sint_truiden"
GAP = "gap_wiric_sint_truiden_vaph_matrix_70_76a_jump_8_01m_73_jump_6_44m_9901_jump_281k_cash_jump_728k_l5"
COMM = "comm_wiric_sint_truiden_jr2025_statutory_70_76a_jump_8_01m_73_jump_6_44m_9901_jump_281k_cash_jump_728k"
LB = "lb_wiric_sint_truiden_70_76a_jump_8_01m_73_jump_6_44m_9901_jump_281k_cash_jump_728k_jr2025"
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

csv.field_size_limit(10_000_000)
with (DATA / "entities.csv").open(encoding="utf-8") as _fh:
    for _row in csv.DictReader(_fh):
        blob = " ".join(_row.values())
        if _row.get("entity_id") == EID or "0420.607.341" in blob or "0420607341" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Wiric deposit 2026-00255614",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00255614.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2546; official native statutory PDF 361983 bytes 41p VOL-VZW 23.0.10 m05-f; header 01/07/2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-06 13:59:39 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00255614 361983 MD5 6e35b896a17e2087a7bfb1b5e270aee7; NBB published-deposits 403 this tick; NBB consult HTML stub unused; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.10 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Wiric 0420.607.341",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420607341",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2546; Actief since 11.04.1980; 3 VE leftover city_sint_truiden (official zetel Diestersteenweg 59 3800 Sint-Truiden since 09.08.1999; VE 2.143.435.823 WIRIC VZW Diestersteenweg 59 3800 Sint-Truiden since 11.04.1980 + VE 2.143.435.922 Gildestraat 16 3800 Sint-Truiden since 11.04.1980 + VE 2.143.436.021 Korenbloemstraat 25 3800 Sint-Truiden since 11.04.1980); VZW since 11.04.1980; RSZ2025 88.993 Beschutte en sociale werkplaatsen; leftover mined city_sint_truiden leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover AGB AGOST 0810.744.410; NOT leftover AGB Trupark 0761.818.697; NOT leftover AGB PTRI 0635.564.190; NOT leftover NV Droneport 0647.642.076; leftover city_sint_truiden leftover VAPH with official zetel Sint-Truiden IS enough",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Wiric 0420607341 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0420607341",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2546; deposit-id 2026-00255614 YE 01.01.2025-31.12.2025 filing VOL-VZW header 01.07.2026 AV 17.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits 403 this tick; NBB consult HTML stub unused; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Wiric Sint-Truiden FOI contact leftover city_sint_truiden leftover VAPH",
        "url": "https://www.vaph.be/organisaties/adressen/wiric",
        "publisher": "Official VAPH adreslijst leftover city_sint_truiden leftover VAPH 3 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2546; FOI info@wiric.be from official VAPH; leftover mined city_sint_truiden leftover VAPH leftover-mined AGB-only unused leftover type after De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Aalternatief 0 deposits Sint-Gerardus Instituut 0 NBB deposits Resonans YE2024-only Plus & Co parent-init Casa Di Colore parent-init Sanamento natural person The Hedge groenezorg Heynsdaele 0 deposits PC Multiversum leftover-via-VE Gent Stijn leftover-via-VE Hasselt DC De Companie leftover-via-VE Roeselare leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_sint_truiden leftover VAPH",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Wiric (VAPH + beschutte/sociale werkplaats)",
    "name_fr": "ASBL Wiric (VAPH)",
    "name_en": "Wiric Sint-Truiden VZW (leftover city_sint_truiden leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_sint_truiden",
    "community_language": "nl",
    "website": "https://www.vaph.be/organisaties/adressen/wiric",
    "foi_email": "info@wiric.be",
    "foi_postal": "Diestersteenweg 59 3800 Sint-Truiden",
    "notes": "tick2546 YE2025 Strong official native NBB PDF deposit 2026-00255614 + Strong KBO 0420.607.341 Actief 3 VE; 70/76A JUMP 8013377; omzet70 JUMP 1272149 commercial-only vs large 73; 73 JUMP 6444532; 76A JUMP 19618; envelope 70/76A JUMP 8013377; 9901 JUMP 490094; pnl JUMP 475104; equity JUMP 5878670; assets JUMP 8271924; debt JUMP 2393253; cash JUMP 3741161; kapitaalsubsidies DROP 391698; 62 JUMP 5921396; 630 JUMP 272287; 66A DROP 102; MVA JUMP 4117868; capex 357905; FTE DROP 75.9; 3 VE leftover city_sint_truiden leftover VAPH leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_sint_truiden leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_wiric_sint_truiden_70_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8013377", "amount_min_eur": "8013377", "amount_max_eur": "8013377", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +8.11%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p6 native; YE2024 7411838 identical; envelope 70/76A for VZW because 70 present and commercial-only vs large 73; FOI VAPH/maatwerk matrix behind 8013377"},
    {"budget_id": "bud_wiric_sint_truiden_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1272149", "amount_min_eur": "1272149", "amount_max_eur": "1272149", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +9.02%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p6 native; YE2024 1166887 identical; commercial-only vs large 73 6444532"},
    {"budget_id": "bud_wiric_sint_truiden_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6444532", "amount_min_eur": "6444532", "amount_max_eur": "6444532", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +7.67%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p6 native; YE2024 5985610 identical; 733 6416532 JUMP +7.36%; 73-733 gap 28000 = 731 schenkingen FOI"},
    {"budget_id": "bud_wiric_sint_truiden_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5921396", "amount_min_eur": "5921396", "amount_max_eur": "5921396", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +5.09%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p6 native; YE2024 5634636 identical; FTE 9087 75.9 DROP from 77.2"},
    {"budget_id": "bud_wiric_sint_truiden_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "272287", "amount_min_eur": "272287", "amount_max_eur": "272287", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 JUMP +13.34%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p6 native; YE2024 240232 identical; capex 357905; MVA 4117868 JUMP"},
    {"budget_id": "bud_wiric_sint_truiden_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "490094", "amount_min_eur": "490094", "amount_max_eur": "490094", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +134.55%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p6 native; YE2024 208948 identical; 66A 102 DROP; 640/8 53320 DROP"},
    {"budget_id": "bud_wiric_sint_truiden_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "475104", "amount_min_eur": "475104", "amount_max_eur": "475104", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +110.29%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p7 native; YE2024 225924 identical; 9903 483107 JUMP"},
    {"budget_id": "bud_wiric_sint_truiden_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5878670", "amount_min_eur": "5878670", "amount_max_eur": "5878670", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +7.53%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p5 native; YE2024 5467204 identical; overgedragen 14 3126140 JUMP; kapitaalsubsidies 15 391698 DROP"},
    {"budget_id": "bud_wiric_sint_truiden_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8271924", "amount_min_eur": "8271924", "amount_max_eur": "8271924", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +9.69%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p5 native; YE2024 7541095 identical; MVA 22/27 4117868 JUMP; cash 3741161 JUMP; capex 357905"},
    {"budget_id": "bud_wiric_sint_truiden_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2393253", "amount_min_eur": "2393253", "amount_max_eur": "2393253", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 JUMP +15.40%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p5 native; YE2024 2073891 identical; ST 42/48 1427261 JUMP; LT 17 952490 JUMP"},
    {"budget_id": "bud_wiric_sint_truiden_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3741161", "amount_min_eur": "3741161", "amount_max_eur": "3741161", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +24.16%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2546; PDF p5 native; YE2024 3013291 identical; geldbeleggingen 50/53 empty vs 261188 DROP"},
], bud_fields)
print("entities+budgets ok")

cash = {
    "2025_envelope_70_76A": 8013377, "2025_omzet": 1272149, "2025_73": 6444532, "2025_76A": 19618,
    "2025_pnl": 475104, "2025_bedrijfswinst": 490094, "2025_9903": 483107,
    "2025_equity": 5878670, "2025_assets": 8271924, "2025_debt": 2393253,
    "2025_cash": 3741161, "2025_kapitaalsubsidies": 391698,
    "2025_personnel62": 5921396, "2025_630": 272287, "2025_6408": 53320, "2025_66A": 102,
    "2025_mva": 4117868, "2025_capex": 357905, "2025_fte": 75.9,
    "2024_envelope_70_76A": 7411838, "2024_omzet": 1166887, "2024_73": 5985610, "2024_76A": 19480,
    "2024_pnl": 225924, "2024_bedrijfswinst": 208948,
    "2024_equity": 5467204, "2024_assets": 7541095, "2024_debt": 2073891,
    "2024_cash": 3013291, "2024_personnel62": 5634636, "2024_630": 240232, "2024_fte": 77.2,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id", "title", "entity_id", "beneficiary", "legal_basis", "decision_date", "start_year", "end_year", "total_envelope_eur", "cash_by_year", "remaining_eur", "status", "evaluation_url", "stated_goal", "cut_option", "source_id", "confidence", "hierarchy_path", "notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Wiric Sint-Truiden YE2025 (70/76A JUMP 8.01m / 73 JUMP 6.44m / 9901 JUMP 281k / cash JUMP 728k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_sint_truiden leftover VAPH",
    "legal_basis": "VZW Wiric (KBO 0420.607.341; Actief; 3 VE; official zetel Sint-Truiden; RSZ2025 88.993; official VAPH adreslijst)",
    "decision_date": "2026-06-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "8013377",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00255614.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_sint_truiden",
    "cut_option": "Publish VAPH / WSE maatwerk / gemeente Sint-Truiden matrix behind 70/76A JUMP 8013377 and 73 JUMP 6444532 and why 9901 JUMP 490094 while FTE DROP 75.9 cash JUMP 3741161",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>Wiric>JR2025_statutory_L5",
    "notes": "tick2546; Strong official native PDF; leftover mined city_sint_truiden leftover VAPH leftover-mined AGB-only unused leftover type; 3 VE; prior-year identical; FIRST LOCK leftover city_sint_truiden leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id", "name", "level", "type", "hierarchy_path", "annual_cost_eur", "total_cost_eur", "tco_notes", "confidence", "source_id", "beneficiaries", "stated_goal", "measured_outcome", "absurdity_score", "cost_score", "difficulty", "priority_index", "cut_proposal", "status", "struck_reason", "notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Wiric Sint-Truiden 70/76A JUMP 8.01m / 73 JUMP 6.44m / 9901 JUMP 281k / cash JUMP 728k (YE2025 leftover city_sint_truiden leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>Wiric>JR2025",
    "annual_cost_eur": "8013377",
    "total_cost_eur": "8013377",
    "tco_notes": "PDF envelope 70/76A 8013377 JUMP; 73 JUMP 6444532; omzet70 JUMP 1272149 commercial-only; 76A JUMP 19618; bedrijfswinst JUMP 490094; pnl JUMP 475104; equity JUMP 5878670; assets JUMP 8271924; debt JUMP 2393253; cash JUMP 3741161; kapitaalsubsidies DROP 391698; personnel62 JUMP 5921396; leftover city_sint_truiden leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_sint_truiden leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_sint_truiden",
    "measured_outcome": "8.01m 70/76A JUMP; 6.44m 73 JUMP; 281k 9901 JUMP; 728k cash JUMP; leftover city_sint_truiden leftover VAPH",
    "absurdity_score": "5.35",
    "cost_score": "5.35",
    "difficulty": "4.40",
    "priority_index": "5.35",
    "cut_proposal": "FOI VAPH / WSE maatwerk / gemeente Sint-Truiden matrix behind 70/76A 8013377 and 73 6444532 and why 9901 JUMP 490094 while FTE DROP 75.9 cash JUMP 3741161",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2546 leftover mined city_sint_truiden leftover VAPH leftover-mined AGB-only unused leftover type after De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Aalternatief 0 deposits Sint-Gerardus Instituut 0 NBB deposits Resonans YE2024-only leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover Stijn leftover-via-VE Hasselt leftover DC De Companie leftover-via-VE Roeselare leftover PC Multiversum leftover-via-VE Gent; 3 VE; prior-year identical; next rq_2547 leftover dual (NOT every-10; next every-10 2550); NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_sint_truiden leftover VAPH",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id", "hierarchy_path", "entity_id", "what_is_missing", "why_it_matters", "priority", "recipient_body", "recipient_email", "recipient_postal", "draft_letter_path", "status", "date_ready", "date_sent", "date_due", "date_answered", "response_summary", "linked_commitment_id", "linked_leaderboard_id", "created_utc", "updated_utc", "notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>Wiric>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / WSE maatwerk / gemeente Sint-Truiden matrix behind VOL-VZW YE2025 70/76A JUMP 8013377, 73 JUMP 6444532, 73-733 gap 28000, 9901 JUMP 490094, cash JUMP 3741161, FTE DROP 75.9",
    "why_it_matters": "Public leftover VAPH dual of mined city_sint_truiden shows 8.01m bedrijfsopbrengsten and 6.44m subsidies while VAPH/maatwerk/gemeente matrix and doubled bedrijfswinst with FTE DROP stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Wiric / Voorzitter Raad van Bestuur",
    "recipient_email": "info@wiric.be",
    "recipient_postal": "Diestersteenweg 59, 3800 Sint-Truiden",
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
    "notes": "tick2546; ready NOT sent; Strong PDF + Strong KBO; leftover city_sint_truiden leftover VAPH",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

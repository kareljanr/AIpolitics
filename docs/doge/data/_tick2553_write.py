from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2553_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_intesa_tongeren_jr2025_nbb_pdf_2553"
SRC_KBO = "src_intesa_tongeren_kbo_2553"
SRC_SBM = "src_intesa_tongeren_sbm_2553"
SRC_SITE = "src_intesa_tongeren_site_2553"
EID = "vzw_intesa_tongeren"
GAP = "gap_intesa_tongeren_vaph_matrix_envelope_jump_16_06m_73_jump_13_73m_cash_jump_549k_pnl_drop_62k_l5"
COMM = "comm_intesa_tongeren_jr2025_statutory_envelope_jump_16_06m_73_jump_13_73m_cash_jump_549k_pnl_drop_62k"
LB = "lb_intesa_tongeren_envelope_jump_16_06m_73_jump_13_73m_cash_jump_549k_pnl_drop_62k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2553/2026-00285863_intesa.pdf").is_file()

def append_rows(path, rows, fieldnames=None):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} no LF")
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", lineterminator="\n")
        for row in rows:
            w.writerow(row)
    print("appended", len(rows), "->", path.name)

csv.field_size_limit(10_000_000)
with (DATA / "entities.csv").open(encoding="utf-8") as _fh:
    for _row in csv.DictReader(_fh):
        blob = " ".join(_row.values())
        if _row.get("entity_id") == EID or "0419.696.036" in blob or "0419696036" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Intesa deposit 2026-00285863",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00285863.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2553; official native statutory PDF 2752547 bytes 49p VOL-VZW 23.0.10 m05-f; header 13/07/2026; AV 12.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-13 22:20:30 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00285863 2752547 MD5 6627334f182741ae6c90a5a08efd14d1; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.6 6.4.1 6.5.2 6.5.3 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW INTESA 0419.696.036",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419696036",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2553; Actief Normale toestand since 13.09.1979; VZW; official zetel Tongersesteenweg 74 3840 Tongeren-Borgloon since 01.01.2025; 14 VE; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; FOI directie@intesa.be; NOT leftover AGB 0820.533.292; NOT leftover Nederheem 0476.473.403 remine@2549",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Intesa 0419696036 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0419696036",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2553; deposit-id 2026-00285863 YE 01.01.2025-31.12.2025 filing VOL-VZW header 13.07.2026 AV 12.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused; deposit-id from Northdata publicationTitle Cbso 2026-00285863 date 2026-07 matching Companyweb neerlegging 14-07-2026; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope not Northdata",
    },
    {
        "source_id": SRC_SITE,
        "title": "Intesa site + official VAPH adreslijst",
        "url": "https://www.vaph.be/organisaties/adressen/intesa",
        "publisher": "Intesa VZW / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2553; FOI directie@intesa.be from official VAPH adreslijst Intesa (RTH+Vergunde Zorgaanbieder) + site https://intesa.be; leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type after Christoforusgemeenschap remine@2552 Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH Intesa (distinct from Nederheem remine@2549); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "INTESA VZW (Tongeren-Borgloon / VAPH Vergunde Zorgaanbieder + RTH woonondersteuning volwassenen)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_tongeren_borgloon",
    "community_language": "nl",
    "website": "https://intesa.be",
    "foi_email": "directie@intesa.be",
    "foi_postal": "Tongersesteenweg 74, 3840 Tongeren-Borgloon",
    "notes": "tick2553 YE2025 Strong official native NBB PDF deposit 2026-00285863 + Strong KBO 0419.696.036 Actief 14 VE; leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type after Nederheem remine@2549; official zetel Tongersesteenweg 74 3840 Tongeren-Borgloon since 01.01.2025; RSZ2025 87.202; envelope 70/76A JUMP 16064584; 73 JUMP 13728493; cash JUMP 1403971; pnl DROP 276541; FTE 162 JUMP; NOT leftover AGB 0820.533.292; NOT leftover Nederheem 0476.473.403; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH Intesa",
}], ent_fields)
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_intesa_tongeren_envelope_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "16064584", "amount_min_eur": "16064584", "amount_max_eur": "16064584", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +3.88%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p5 native; YE2024 15465302 identical; VZW envelope because 70 present and commercial-only vs large 73"},
    {"budget_id": "bud_intesa_tongeren_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1942845", "amount_min_eur": "1942845", "amount_max_eur": "1942845", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +3.66%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p5 native; YE2024 1874305 identical; commercial-only vs large 73"},
    {"budget_id": "bud_intesa_tongeren_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "13728493", "amount_min_eur": "13728493", "amount_max_eur": "13728493", "basis": "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +4.22%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p5 native; YE2024 13173198 identical; 733 13715881 JUMP +4.24%; 73-733 gap 12612 FOI"},
    {"budget_id": "bud_intesa_tongeren_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12875390", "amount_min_eur": "12875390", "amount_max_eur": "12875390", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +4.76%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p5 native; YE2024 12290038 identical; FTE 9087 162 JUMP from 159.1"},
    {"budget_id": "bud_intesa_tongeren_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "603813", "amount_min_eur": "603813", "amount_max_eur": "603813", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 JUMP +4.48%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p5 native; YE2024 577947 identical; capex ~334892; MVA 22/27 7456224 DROP"},
    {"budget_id": "bud_intesa_tongeren_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "369462", "amount_min_eur": "369462", "amount_max_eur": "369462", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -13.19%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p6 native; YE2024 425578 identical; 66A 7238 DROP; 640/8 228083 DROP"},
    {"budget_id": "bud_intesa_tongeren_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "276541", "amount_min_eur": "276541", "amount_max_eur": "276541", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -18.26%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p6 native; YE2024 338306 identical; 9903 276541 DROP"},
    {"budget_id": "bud_intesa_tongeren_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4914980", "amount_min_eur": "4914980", "amount_max_eur": "4914980", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +3.74%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p4 native; YE2024 4737707 identical; kapitaalsubsidies 15 1383066 DROP -6.70%"},
    {"budget_id": "bud_intesa_tongeren_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9948991", "amount_min_eur": "9948991", "amount_max_eur": "9948991", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +2.33%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p4 native; YE2024 9722193 identical; MVA 22/27 7456224 DROP; gebouwen 22 6735974 DROP; cash 1403971 JUMP; capex ~334892"},
    {"budget_id": "bud_intesa_tongeren_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4513152", "amount_min_eur": "4513152", "amount_max_eur": "4513152", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 JUMP +0.89%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p4 native; YE2024 4473401 identical"},
    {"budget_id": "bud_intesa_tongeren_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1403971", "amount_min_eur": "1403971", "amount_max_eur": "1403971", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +64.13%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2553; PDF p4 native; YE2024 855376 identical; geldbeleggingen 50/53 empty"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_envelope": 16064584, "2025_omzet": 1942845, "2025_73": 13728493, "2025_76A": 19874, "2025_733": 13715881,
    "2025_pnl": 276541, "2025_bedrijfswinst": 369462, "2025_9903": 276541,
    "2025_equity": 4914980, "2025_assets": 9948991, "2025_debt": 4513152,
    "2025_cash": 1403971, "2025_kapitaalsubsidies": 1383066, "2025_geldbeleggingen": 0,
    "2025_personnel62": 12875390, "2025_630": 603813, "2025_6408": 228083, "2025_66A": 7238,
    "2025_mva": 7456224, "2025_capex": 334892, "2025_fte": 162, "2025_gebouwen": 6735974,
    "2025_aanbouw": 0, "2025_destin691": 1553199, "2025_destin791": 0,
    "2024_envelope": 15465302, "2024_omzet": 1874305, "2024_73": 13173198, "2024_76A": 2526, "2024_733": 13157671,
    "2024_pnl": 338306, "2024_bedrijfswinst": 425578,
    "2024_equity": 4737707, "2024_assets": 9722193, "2024_debt": 4473401,
    "2024_cash": 855376, "2024_personnel62": 12290038, "2024_630": 577947, "2024_fte": 159.1,
    "2024_kapitaalsubsidies": 1482335, "2024_geldbeleggingen": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Intesa Tongeren-Borgloon YE2025 (envelope JUMP 16.06m / 73 JUMP 13.73m / cash JUMP 549k / pnl DROP 62k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_tongeren_borgloon leftover VAPH",
    "legal_basis": "VZW INTESA (KBO 0419.696.036; Actief; 14 VE; official zetel Tongeren-Borgloon; RSZ2025 87.202; official VAPH adreslijst RTH+Vergunde Zorgaanbieder)",
    "decision_date": "2026-06-12",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "16064584",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00285863.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_tongeren_borgloon",
    "cut_option": "Publish VAPH / gemeente Tongeren-Borgloon matrix behind 73 JUMP 13728493 and envelope 70/76A JUMP 16064584 and why cash JUMP 1403971 while pnl DROP 276541 and FTE JUMP 162",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Tongeren-Borgloon>Intesa>JR2025_statutory_L5",
    "notes": "tick2553; Strong official native PDF; leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type after Nederheem remine@2549; 14 VE; prior-year identical; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH Intesa; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Intesa Tongeren-Borgloon envelope JUMP 16.06m / 73 JUMP 13.73m / cash JUMP 549k / pnl DROP 62k (YE2025 leftover city_tongeren_borgloon leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Tongeren-Borgloon>Intesa>JR2025",
    "annual_cost_eur": "16064584",
    "total_cost_eur": "16064584",
    "tco_notes": "PDF envelope 70/76A 16064584 JUMP; 73 subsidies 13728493 JUMP; 733 13715881; omzet70 JUMP 1942845 commercial-only; 76A JUMP 19874; bedrijfswinst DROP 369462; pnl DROP 276541; equity JUMP 4914980; assets JUMP 9948991; debt JUMP 4513152; cash JUMP 1403971; geldbeleggingen empty; kapitaalsubsidies DROP 1383066; personnel62 JUMP 12875390; leftover city_tongeren_borgloon leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_tongeren_borgloon leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_tongeren_borgloon",
    "measured_outcome": "16.06m envelope JUMP; 13.73m 73 JUMP; 549k cash JUMP; 62k pnl DROP; 162 FTE JUMP; leftover city_tongeren_borgloon leftover VAPH",
    "absurdity_score": "5.85",
    "cost_score": "6.15",
    "difficulty": "4.55",
    "priority_index": "5.92",
    "cut_proposal": "FOI VAPH / gemeente Tongeren-Borgloon matrix behind 73 13728493 and envelope 16064584 and why cash JUMP 1403971 while pnl DROP 276541 and FTE JUMP 162",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2553 leftover mined city_tongeren_borgloon leftover VAPH Intesa leftover-mined AGB-only unused leftover type after Christoforusgemeenschap remine@2552 Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Veerkracht 0 deposits Steger 0 deposits Pelikaan OCMW Ampel Prisma remine Terloo Broeders Gent leftover-via-VE leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover city_merelbeke_melle leftover VAPH Christoforusgemeenschap remine@2552 leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only SKIP leftover Het Raster Antwerpen zetel leftover-via-VE Vilvoorde SKIP leftover ErgoEzel Duffel groenezorg SKIP; 14 VE; prior-year identical; next rq_2554 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH Intesa",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Tongeren-Borgloon>Intesa>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Tongeren-Borgloon matrix behind VOL-VZW YE2025 73 JUMP 13728493, envelope 70/76A JUMP 16064584, cash JUMP 1403971, pnl DROP 276541, FTE JUMP 162 with 62 JUMP 12875390, destin 691 1553199",
    "why_it_matters": "Public leftover VAPH dual of mined city_tongeren_borgloon shows 13.73m subsidies and 16.06m envelope while VAPH/gemeente matrix and cash JUMP 64 percent with pnl DROP 18 percent stay unsourced",
    "priority": "7",
    "recipient_body": "VZW INTESA / Voorzitter Raad van Bestuur",
    "recipient_email": "directie@intesa.be",
    "recipient_postal": "Tongersesteenweg 74, 3840 Tongeren-Borgloon",
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
    "notes": "tick2553; ready NOT sent; Strong PDF + Strong KBO; leftover city_tongeren_borgloon leftover VAPH Intesa",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

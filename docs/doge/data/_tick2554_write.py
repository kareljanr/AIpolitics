from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2554_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_kadodder_zoersel_jr2025_nbb_pdf_2554"
SRC_KBO = "src_kadodder_zoersel_kbo_2554"
SRC_SBM = "src_kadodder_zoersel_sbm_2554"
SRC_SITE = "src_kadodder_zoersel_site_2554"
EID = "vzw_kadodder_zoersel"
GAP = "gap_kadodder_zoersel_vaph_matrix_bruto_jump_4_09m_73_jump_4_12m_9901_flip_profit_319k_cash_drop_16k_l5"
COMM = "comm_kadodder_zoersel_jr2025_statutory_bruto_jump_4_09m_73_jump_4_12m_9901_flip_profit_319k_cash_drop_16k"
LB = "lb_kadodder_zoersel_bruto_jump_4_09m_73_jump_4_12m_9901_flip_profit_319k_cash_drop_16k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2554/2026-00134366_kadodder.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0434.504.174" in blob or "0434504174" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Kadodder deposit 2026-00134366",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00134366.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2554; official native statutory PDF 53458 bytes 15p VKT-VZW 26.0.11 m04-f; header 03/06/2026; AV 20.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-03 10:53:43 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00134366 53458 MD5 c024db11630e42d1b911dc80f6db7f70; VKT-VZW 6.1.3 6.5 6.6 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Kadodder VZW 0434.504.174",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0434504174",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2554; Actief Normale toestand since 12.01.1988; VZW; official zetel Oostmallebaan 50 2980 Zoersel since 26.05.2010; 1 VE 2.235.547.815 DIENST VROEG- EN THUISBEGELEIDING - PROVINCIE ANTWERPEN Oostmallebaan 50 since 26.05.2010; RSZ2025 88.999 Andere vormen van maatschappelijke dienstverlening zonder huisvesting; Werkgever RSZ; FOI thuisbegeleiding@kadodder.be; NOT leftover AGB Zoersel 0687.958.543; NOT leftover Doppa 0836.745.160 remine@2493",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Kadodder 0434504174 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0434504174",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2554; deposit-id 2026-00134366 YE 01.01.2025-31.12.2025 filing VKT-VZW header 03.06.2026 AV 20.05.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused; deposit-id from Northdata publicationTitle Cbso 2026-00134366 date 2026-06-03; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope not Northdata",
    },
    {
        "source_id": SRC_SITE,
        "title": "Kadodder official VAPH adreslijst",
        "url": "https://www.vaph.be/organisaties/adressen/kadodder",
        "publisher": "Kadodder VZW / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2554; FOI thuisbegeleiding@kadodder.be from official VAPH adreslijst Kadodder (thuisbegeleiding / vroegbegeleiding) Oostmallebaan 50 2980 Zoersel; leftover mined city_zoersel leftover VAPH leftover-mined AGB-only after Doppa remine@2493 Intesa remine@2553 Christoforusgemeenschap remine@2552 Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546; FIRST LOCK leftover city_zoersel leftover VAPH Kadodder (distinct from Doppa remine@2493); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Kadodder VZW (Zoersel / VAPH vroeg- en thuisbegeleiding provincie Antwerpen)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_zoersel",
    "community_language": "nl",
    "website": "https://www.vaph.be/organisaties/adressen/kadodder",
    "foi_email": "thuisbegeleiding@kadodder.be",
    "foi_postal": "Oostmallebaan 50, 2980 Zoersel",
    "notes": "tick2554 YE2025 Strong official native NBB PDF deposit 2026-00134366 + Strong KBO 0434.504.174 Actief 1 VE; leftover mined city_zoersel leftover VAPH leftover-mined AGB-only after Doppa remine@2493; official zetel Oostmallebaan 50 2980 Zoersel since 26.05.2010; RSZ2025 88.999; bruto9900 JUMP 4085529; 73 JUMP 4122472; 9901 FLIP PROFIT 318864; cash DROP 570520; FTE 42.2 JUMP; NOT leftover AGB 0687.958.543; NOT leftover Doppa 0836.745.160; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_zoersel leftover VAPH Kadodder",
}], ent_fields)
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_kadodder_zoersel_bruto9900_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4085529", "amount_min_eur": "4085529", "amount_max_eur": "4085529", "basis": "NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +16.70%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p5 native; YE2024 3500753 identical; VKT envelope because 73 is the subsidy envelope and bruto >> omzet70"},
    {"budget_id": "bud_kadodder_zoersel_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "85398", "amount_min_eur": "85398", "amount_max_eur": "85398", "basis": "NBB VKT-VZW code 70 omzet YE2025 JUMP +6.37%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p5 native; YE2024 80282 identical; commercial-only vs large 73"},
    {"budget_id": "bud_kadodder_zoersel_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4122472", "amount_min_eur": "4122472", "amount_max_eur": "4122472", "basis": "NBB VKT-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +16.04%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p5 native; YE2024 3552767 identical; 76A empty; 733 not on VKT face"},
    {"budget_id": "bud_kadodder_zoersel_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3716350", "amount_min_eur": "3716350", "amount_max_eur": "3716350", "basis": "NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +5.49%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p5 native; YE2024 3523035 identical; FTE 9087 42.2 JUMP from 41.1"},
    {"budget_id": "bud_kadodder_zoersel_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "39552", "amount_min_eur": "39552", "amount_max_eur": "39552", "basis": "NBB VKT-VZW code 630 afschrijvingen YE2025 JUMP +4.74%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p5 native; YE2024 37761 identical; capex ~30098; MVA 22/27 530285 DROP"},
    {"budget_id": "bud_kadodder_zoersel_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "318864", "amount_min_eur": "318864", "amount_max_eur": "318864", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP PROFIT", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p5 native; YE2024 -73751 identical; 66A empty; 640/8 10763 DROP -21.48%"},
    {"budget_id": "bud_kadodder_zoersel_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "339673", "amount_min_eur": "339673", "amount_max_eur": "339673", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP PROFIT", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p5 native; YE2024 -38969 identical; 9903 339673 FLIP PROFIT"},
    {"budget_id": "bud_kadodder_zoersel_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2010802", "amount_min_eur": "2010802", "amount_max_eur": "2010802", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +20.32%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p4 native; YE2024 1671130 identical; kapitaalsubsidies 15 empty; destin 691 16984; 791 empty"},
    {"budget_id": "bud_kadodder_zoersel_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2887650", "amount_min_eur": "2887650", "amount_max_eur": "2887650", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +10.76%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p3 native; YE2024 2607092 identical; MVA 22/27 530285 DROP; gebouwen 22 473680 DROP; cash 570520 DROP; geldbeleggingen 1395553 JUMP; capex ~30098"},
    {"budget_id": "bud_kadodder_zoersel_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "876848", "amount_min_eur": "876848", "amount_max_eur": "876848", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 DROP -6.32%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p4 native; YE2024 935963 identical"},
    {"budget_id": "bud_kadodder_zoersel_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "570520", "amount_min_eur": "570520", "amount_max_eur": "570520", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -2.73%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2554; PDF p3 native; YE2024 586543 identical; geldbeleggingen 50/53 1395553 JUMP +2.95%"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_bruto9900": 4085529, "2025_omzet": 85398, "2025_73": 4122472, "2025_76A": 0,
    "2025_pnl": 339673, "2025_bedrijfswinst": 318864, "2025_9903": 339673,
    "2025_equity": 2010802, "2025_assets": 2887650, "2025_debt": 876848,
    "2025_cash": 570520, "2025_kapitaalsubsidies": 0, "2025_geldbeleggingen": 1395553,
    "2025_personnel62": 3716350, "2025_630": 39552, "2025_6408": 10763, "2025_66A": 0,
    "2025_mva": 530285, "2025_capex": 30098, "2025_fte": 42.2, "2025_gebouwen": 473680,
    "2025_aanbouw": 0, "2025_destin691": 16984, "2025_destin791": 0,
    "2024_bruto9900": 3500753, "2024_omzet": 80282, "2024_73": 3552767, "2024_76A": 0,
    "2024_pnl": -38969, "2024_bedrijfswinst": -73751,
    "2024_equity": 1671130, "2024_assets": 2607092, "2024_debt": 935963,
    "2024_cash": 586543, "2024_personnel62": 3523035, "2024_630": 37761, "2024_fte": 41.1,
    "2024_kapitaalsubsidies": 0, "2024_geldbeleggingen": 1355499,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Kadodder Zoersel YE2025 (bruto9900 JUMP 4.09m / 73 JUMP 4.12m / 9901 FLIP PROFIT 319k / cash DROP 16k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_zoersel leftover VAPH",
    "legal_basis": "Kadodder VZW (KBO 0434.504.174; Actief; 1 VE; official zetel Zoersel; RSZ2025 88.999; official VAPH adreslijst thuisbegeleiding)",
    "decision_date": "2026-05-20",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "4085529",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00134366.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_zoersel",
    "cut_option": "Publish VAPH / gemeente Zoersel matrix behind 73 JUMP 4122472 and bruto9900 JUMP 4085529 and why 9901 FLIP PROFIT 318864 while cash DROP 570520 and FTE JUMP 42.2",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Zoersel>Kadodder>JR2025_statutory_L5",
    "notes": "tick2554; Strong official native PDF; leftover mined city_zoersel leftover VAPH leftover-mined AGB-only after Doppa remine@2493; 1 VE; prior-year identical; FIRST LOCK leftover city_zoersel leftover VAPH Kadodder; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Kadodder Zoersel bruto9900 JUMP 4.09m / 73 JUMP 4.12m / 9901 FLIP PROFIT 319k / cash DROP 16k (YE2025 leftover city_zoersel leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Zoersel>Kadodder>JR2025",
    "annual_cost_eur": "4085529",
    "total_cost_eur": "4085529",
    "tco_notes": "PDF bruto9900 4085529 JUMP; 73 subsidies 4122472 JUMP; omzet70 JUMP 85398 commercial-only; 76A empty; bedrijfswinst FLIP PROFIT 318864; pnl FLIP PROFIT 339673; equity JUMP 2010802; assets JUMP 2887650; debt DROP 876848; cash DROP 570520; geldbeleggingen JUMP 1395553; kapitaalsubsidies empty; personnel62 JUMP 3716350; leftover city_zoersel leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_zoersel leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_zoersel",
    "measured_outcome": "4.09m bruto JUMP; 4.12m 73 JUMP; 319k 9901 FLIP PROFIT; 16k cash DROP; 42.2 FTE JUMP; leftover city_zoersel leftover VAPH",
    "absurdity_score": "5.45",
    "cost_score": "5.70",
    "difficulty": "4.40",
    "priority_index": "5.58",
    "cut_proposal": "FOI VAPH / gemeente Zoersel matrix behind 73 4122472 and bruto9900 4085529 and why 9901 FLIP PROFIT 318864 while cash DROP 570520 and FTE JUMP 42.2",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2554 leftover mined city_zoersel leftover VAPH Kadodder leftover-mined AGB-only after Doppa remine@2493 Intesa remine@2553 Christoforusgemeenschap remine@2552 Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540; hunt skips Veerkracht 0 deposits Steger 0 deposits Pelikaan OCMW Ampel Prisma remine Terloo leftover-via-VE Juffertje Tessenderlo 0 Northdata YE2025 deps Perron-Geluk Essen 0 Northdata YE2025 deps Passchoeve KBO mismatch BV Bisschophoeve Flaming Star VOF commercial VillaVip Bredene wrong-city Zele Monnikenheide Emmaus leftover-via-VE ErgoEzel Duffel groenezorg Het Raster leftover-via-VE Vilvoorde Nethedal YE2024-only leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover city_tongeren_borgloon leftover VAPH Intesa remine@2553 Nederheem remine@2549 (city VAPH type now has two locks); 1 VE; prior-year identical; next rq_2555 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_zoersel leftover VAPH Kadodder",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Zoersel>Kadodder>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Zoersel matrix behind VKT-VZW YE2025 73 JUMP 4122472, bruto9900 JUMP 4085529, 9901 FLIP PROFIT 318864, cash DROP 570520, FTE JUMP 42.2 with 62 JUMP 3716350, destin 691 16984",
    "why_it_matters": "Public leftover VAPH dual of mined city_zoersel shows 4.12m subsidies and 4.09m bruto while VAPH/gemeente matrix and FLIP to 319k profit with cash DROP stay unsourced",
    "priority": "7",
    "recipient_body": "Kadodder VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "thuisbegeleiding@kadodder.be",
    "recipient_postal": "Oostmallebaan 50, 2980 Zoersel",
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
    "notes": "tick2554; ready NOT sent; Strong PDF + Strong KBO; leftover city_zoersel leftover VAPH Kadodder",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

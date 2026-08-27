from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2555_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_vlotter_boom_jr2025_nbb_pdf_2555"
SRC_KBO = "src_vlotter_boom_kbo_2555"
SRC_SBM = "src_vlotter_boom_sbm_2555"
SRC_SITE = "src_vlotter_boom_site_2555"
EID = "dv_vlotter_boom"
GAP = "gap_vlotter_boom_dv_matrix_70_76a_jump_7_50m_74_jump_4_95m_9901_jump_loss_narrow_298k_cash_jump_917k_l5"
COMM = "comm_vlotter_boom_jr2025_statutory_70_76a_jump_7_50m_74_jump_4_95m_9901_jump_loss_narrow_298k_cash_jump_917k"
LB = "lb_vlotter_boom_70_76a_jump_7_50m_74_jump_4_95m_9901_jump_loss_narrow_298k_cash_jump_917k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2555/2026-00303036.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0200.762.878" in blob or "0200762878" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-inb jaarrekening 2025 VLOTTER deposit 2026-00303036",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00303036.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2555; official native statutory PDF 476231 bytes 51p VOL-inb 26.0.15 m82-f; header 15/07/2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-17 08:06:31 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00303036 476231 MD5 5415025ef790a927f4f01f04d84dafe5; VOL-inb 6.1 6.2.1 6.2.2 6.2.4 6.2.5 6.3.4 6.3.5 6.3.6 6.4.1 6.5.2 6.7.2 6.15 6.17 6.18.1 6.18.2 6.20 9 11 12 13 14 15 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VLOTTER 0200.762.878",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0200762878",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2555; Actief Normale toestand; Dienstverlenende vereniging (Vlaams Gewest) since 25.11.2003; official zetel Colonel Silvertopstraat 15 2850 Boom since 20.04.2001; Begindatum 01.07.1964; 2 VE 2.162.917.579 Vlotter Colonel Silvertopstraat 15 since 01.07.2000 + 2.171.339.159 Beschermde Werkplaats IMSIR Industrieweg 1 since 07.10.1995; RSZ2025 88.993 Beschutte en sociale werkplaatsen + 88.101 Activiteiten van gezins- en bejaardenzorg; Werkgever RSZ; FOI thuiszorg@vlotter.be; NOT leftover AGB Boom Plus 0862.976.336; NOT leftover WM Woonkade 0452.753.537; NOT leftover Vlotter Maatwerk VZW 0841.843.796 YE2024-only",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / Northdata fiche VLOTTER 0200762878 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0200762878",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2555; deposit-id 2026-00303036 YE 01.01.2025-31.12.2025 filing VOL-inb header 15.07.2026 AV 24.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused; deposit-id from Northdata publicationTitle Cbso 2026-00303036 date 2026-07-15; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope not Northdata",
    },
    {
        "source_id": SRC_SITE,
        "title": "VLOTTER official site / Sociale Kaart thuiszorg",
        "url": "https://www.vlotter.be/",
        "publisher": "VLOTTER / Sociale Kaart",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2555; FOI thuiszorg@vlotter.be from official Sociale Kaart Vlotter Thuiszorg fiche + info@vlotter.be; leftover mined city_boom leftover maatwerk/thuiszorg dual leftover-mined AGB-only after Kadodder remine@2554 Intesa remine@2553 Christoforusgemeenschap remine@2552 Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546; FIRST LOCK leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER (VAPH hunt stalled on 0-deposit groenezorg / YE2024-only Vlotter Maatwerk VZW); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "VLOTTER (Boom / IMSIR maatwerk + thuiszorg dienstverlenende vereniging)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_boom",
    "community_language": "nl",
    "website": "https://www.vlotter.be/",
    "foi_email": "thuiszorg@vlotter.be",
    "foi_postal": "Colonel Silvertopstraat 15, 2850 Boom",
    "notes": "tick2555 YE2025 Strong official native NBB PDF deposit 2026-00303036 + Strong KBO 0200.762.878 Actief 2 VE; leftover mined city_boom leftover maatwerk/thuiszorg dual leftover-mined AGB-only; official zetel Colonel Silvertopstraat 15 2850 Boom since 20.04.2001; RSZ2025 88.993+88.101; envelope 70/76A JUMP 7498740; 74 JUMP 4946203; 9901 JUMP LOSS narrower -297897; cash JUMP 4373528; FTE 112.3 DROP; NOT leftover AGB 0862.976.336; NOT leftover WM 0452.753.537; NOT leftover Vlotter Maatwerk VZW 0841.843.796 YE2024-only; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER",
}], ent_fields)
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_vlotter_boom_envelope70_76a_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7498740", "amount_min_eur": "7498740", "amount_max_eur": "7498740", "basis": "NBB VOL-inb code 70/76A bedrijfsopbrengsten YE2025 JUMP +5.61%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 7100145 identical; 73 empty; subsidies sit in 74/740"},
    {"budget_id": "bud_vlotter_boom_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2365768", "amount_min_eur": "2365768", "amount_max_eur": "2365768", "basis": "NBB VOL-inb code 70 omzet YE2025 DROP -6.89%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 2540869 identical; commercial vs large 74 subsidies"},
    {"budget_id": "bud_vlotter_boom_74_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4946203", "amount_min_eur": "4946203", "amount_max_eur": "4946203", "basis": "NBB VOL-inb code 74 andere bedrijfsopbrengsten YE2025 JUMP +8.49%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 4559254 identical; exploitatiesubsidies 740 4663519 FOI; 73 empty"},
    {"budget_id": "bud_vlotter_boom_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "186769", "amount_min_eur": "186769", "amount_max_eur": "186769", "basis": "NBB VOL-inb code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 22 identical"},
    {"budget_id": "bud_vlotter_boom_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6163331", "amount_min_eur": "6163331", "amount_max_eur": "6163331", "basis": "NBB VOL-inb code 62 bezoldigingen YE2025 DROP -2.88%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 6345908 identical; FTE 9087 112.3 DROP from 116.5"},
    {"budget_id": "bud_vlotter_boom_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "173026", "amount_min_eur": "173026", "amount_max_eur": "173026", "basis": "NBB VOL-inb code 630 afschrijvingen YE2025 JUMP +2.94%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 168084 identical; capex ~57207; MVA 22/27 2227394 DROP"},
    {"budget_id": "bud_vlotter_boom_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-297897", "amount_min_eur": "-297897", "amount_max_eur": "-297897", "basis": "NBB VOL-inb code 9901 bedrijfsverlies YE2025 JUMP LOSS narrower", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 -784330 identical; 66A 11399; 640/8 573106 JUMP"},
    {"budget_id": "bud_vlotter_boom_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-277551", "amount_min_eur": "-277551", "amount_max_eur": "-277551", "basis": "NBB VOL-inb code 9904 verlies van het boekjaar YE2025 JUMP LOSS narrower", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 -753303 identical; 9903 -277551"},
    {"budget_id": "bud_vlotter_boom_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2208777", "amount_min_eur": "2208777", "amount_max_eur": "2208777", "basis": "NBB VOL-inb code 10/15 eigen vermogen YE2025 DROP -11.65%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 2499926 identical; kapitaalsubsidies 15 201075 DROP; destin 691/791 empty"},
    {"budget_id": "bud_vlotter_boom_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8342340", "amount_min_eur": "8342340", "amount_max_eur": "8342340", "basis": "NBB VOL-inb code 20/58 totaal activa YE2025 JUMP +2.73%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 8120547 identical; MVA 22/27 2227394 DROP; gebouwen 22 2117863 DROP; cash 4373528 JUMP; geldbeleggingen empty; capex ~57207"},
    {"budget_id": "bud_vlotter_boom_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4373528", "amount_min_eur": "4373528", "amount_max_eur": "4373528", "basis": "NBB VOL-inb code 54/58 liquide middelen YE2025 JUMP +26.54%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2555; PDF p native; YE2024 3456184 identical; debt 17/49 4361960 JUMP +12.64%"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_envelope70_76A": 7498740, "2025_omzet": 2365768, "2025_73": 0, "2025_74": 4946203, "2025_76A": 186769,
    "2025_pnl": -277551, "2025_bedrijfswinst": -297897, "2025_9903": -277551,
    "2025_equity": 2208777, "2025_assets": 8342340, "2025_debt": 4361960,
    "2025_cash": 4373528, "2025_kapitaalsubsidies": 201075, "2025_geldbeleggingen": 0,
    "2025_personnel62": 6163331, "2025_630": 173026, "2025_6408": 573106, "2025_66A": 11399,
    "2025_mva": 2227394, "2025_capex": 57207, "2025_fte": 112.3, "2025_gebouwen": 2117863,
    "2025_aanbouw": 0, "2025_destin691": 0, "2025_destin791": 0, "2025_740": 4663519,
    "2024_envelope70_76A": 7100145, "2024_omzet": 2540869, "2024_73": 0, "2024_74": 4559254, "2024_76A": 22,
    "2024_pnl": -753303, "2024_bedrijfswinst": -784330,
    "2024_equity": 2499926, "2024_assets": 8120547, "2024_debt": 3872360,
    "2024_cash": 3456184, "2024_personnel62": 6345908, "2024_630": 168084, "2024_fte": 116.5,
    "2024_kapitaalsubsidies": 214674, "2024_geldbeleggingen": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "VLOTTER Boom YE2025 (70/76A JUMP 7.50m / 74 JUMP 4.95m / 9901 JUMP LOSS narrower 298k / cash JUMP 917k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "maatwerk+thuiszorg + leftover city_boom leftover dual",
    "legal_basis": "VLOTTER (KBO 0200.762.878; Actief; 2 VE; official zetel Boom; RSZ2025 88.993+88.101; Dienstverlenende vereniging)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "7498740",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00303036.pdf",
    "stated_goal": "Public leftover maatwerk/thuiszorg dual of mined city_boom",
    "cut_option": "Publish Vlaamse/gemeentelijke matrix behind 70/76A JUMP 7498740 and 74 JUMP 4946203 and why 9901 JUMP LOSS narrower -297897 while cash JUMP 4373528 and FTE DROP 112.3",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Boom>VLOTTER>JR2025_statutory_L5",
    "notes": "tick2555; Strong official native PDF; leftover mined city_boom leftover maatwerk/thuiszorg dual leftover-mined AGB-only; 2 VE; prior-year identical; FIRST LOCK leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "VLOTTER Boom 70/76A JUMP 7.50m / 74 JUMP 4.95m / 9901 JUMP LOSS narrower 298k / cash JUMP 917k (YE2025 leftover city_boom leftover maatwerk/thuiszorg dual)",
    "level": "L5",
    "type": "maatwerk_thuiszorg_dv_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Boom>VLOTTER>JR2025",
    "annual_cost_eur": "7498740",
    "total_cost_eur": "7498740",
    "tco_notes": "PDF envelope 70/76A 7498740 JUMP; 74 4946203 JUMP (740 exploitatiesubsidies 4663519); omzet70 DROP 2365768; 73 empty; 76A JUMP 186769; bedrijfswinst JUMP LOSS narrower -297897; pnl JUMP LOSS narrower -277551; equity DROP 2208777; assets JUMP 8342340; debt JUMP 4361960; cash JUMP 4373528; geldbeleggingen empty; kapitaalsubsidies DROP 201075; personnel62 DROP 6163331; leftover city_boom leftover maatwerk/thuiszorg dual",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "maatwerk+thuiszorg + leftover city_boom leftover dual",
    "stated_goal": "leftover maatwerk/thuiszorg dual leftover city_boom",
    "measured_outcome": "7.50m 70/76A JUMP; 4.95m 74 JUMP; 298k 9901 JUMP LOSS narrower; 917k cash JUMP; 112.3 FTE DROP; leftover city_boom leftover maatwerk/thuiszorg dual",
    "absurdity_score": "5.50",
    "cost_score": "5.85",
    "difficulty": "4.50",
    "priority_index": "5.72",
    "cut_proposal": "FOI Vlaamse/gemeentelijke matrix behind 70/76A 7498740 and 74 4946203 and why 9901 JUMP LOSS narrower -297897 while cash JUMP 4373528 and FTE DROP 112.3",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2555 leftover mined city_boom leftover maatwerk/thuiszorg dual VLOTTER leftover-mined AGB-only after Kadodder remine@2554 Intesa remine@2553 Christoforusgemeenschap remine@2552 Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540; hunt skips VAPH 0-deposit groenezorg Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend no NBB YE2025 deps; Vlotter Maatwerk VZW 0841.843.796 YE2024-only; Forena Menen remine@2194 under sec_flanders; Entiris Leuven zetel leftover-via-VE; Veerkracht 0 deposits Steger 0 deposits Pelikaan OCMW Ampel Prisma remine Terloo leftover-via-VE Juffertje 0 deps Perron-Geluk 0 deps Passchoeve BV mismatch Flaming Star VOF VillaVip wrong city Monnikenheide leftover-via-VE ErgoEzel groenezorg Het Raster leftover-via-VE Nethedal YE2024-only leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover city_zoersel leftover VAPH Kadodder remine@2554; 2 VE; prior-year identical; next rq_2556 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Boom>VLOTTER>leftover_maatwerk_thuiszorg",
    "entity_id": EID,
    "what_is_missing": "Vlaamse/gemeentelijke matrix behind VOL-inb YE2025 70/76A JUMP 7498740, 74 JUMP 4946203 (740 4663519), 9901 JUMP LOSS narrower -297897, cash JUMP 4373528, FTE DROP 112.3 with 62 DROP 6163331",
    "why_it_matters": "Public leftover maatwerk/thuiszorg dual of mined city_boom shows 7.50m envelope and 4.95m andere opbrengsten while subsidy matrix and why loss narrows while cash JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "VLOTTER / Voorzitter Raad van Bestuur",
    "recipient_email": "thuiszorg@vlotter.be",
    "recipient_postal": "Colonel Silvertopstraat 15, 2850 Boom",
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
    "notes": "tick2555; ready NOT sent; Strong PDF + Strong KBO; leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

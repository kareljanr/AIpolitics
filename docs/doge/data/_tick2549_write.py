from pathlib import Path
import csv, json, re

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2549_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_nederheem_tongeren_jr2025_nbb_pdf_2549"
SRC_KBO = "src_nederheem_tongeren_kbo_2549"
SRC_SBM = "src_nederheem_tongeren_sbm_2549"
SRC_SITE = "src_nederheem_tongeren_site_2549"
EID = "vzw_nederheem_tongeren"
GAP = "gap_nederheem_tongeren_vaph_matrix_70_76a_jump_3_98m_73_jump_3_40m_9901_drop_200k_cash_drop_36k_l5"
COMM = "comm_nederheem_tongeren_jr2025_statutory_70_76a_jump_3_98m_73_jump_3_40m_9901_drop_200k_cash_drop_36k"
LB = "lb_nederheem_tongeren_70_76a_jump_3_98m_73_jump_3_40m_9901_drop_200k_cash_drop_36k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2549/2026-00116325_nederheem.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0476.473.403" in blob or "0476473403" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Nederheem deposit 2026-00116325",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00116325.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2549; official native statutory PDF 81393 bytes 28p VOL-VZW 26.0.11 m05-f; header 21/05/2026; AV 21.04.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-21 08:20:50 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00116325 81393 MD5 e944f6f9d1bd95319a5c00076ce047c5; VOL-VZW 6.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.3.6 6.4.2 6.4.3 6.5.2 6.5.3 6.6 6.13 6.15 6.16 6.18 7 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN; kapitaalsubsidies 15 YE2024 PDF column bleed with debt 1642832 — YE2024 806919 from equity identity 10/15=fondsen10+overgedragen14+kapitaalsubsidies15",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Nederheem 0476.473.403",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0476473403",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2549; Actief Normale toestand since 07.11.2001; VZW; official zetel Heurkensberg 3 3700 Tongeren-Borgloon since 01.01.2025; 2 VE 2.271.718.422 Heurkensberg 3 + 2.271.965.969 Tomstraat 81 both Tongeren-Borgloon; RSZ2025 87.202; Werkgever RSZ since 01.01.2002; NOT leftover AGB 0820.533.292",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Nederheem 0476473403 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0476473403",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2549; deposit-id 2026-00116325 YE 01.01.2025-31.12.2025 filing VOL-VZW header 21.05.2026 AV 21.04.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits 403 this tick; NBB consult HTML stub unused; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Nederheem site + official VAPH adreslijst",
        "url": "https://nederheem.be",
        "publisher": "Nederheem VZW / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2549; FOI administratie@nederheem.be from official site + official VAPH adreslijst Nederheem Heurkensberg 3 3700 Tongeren-Borgloon; leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type after OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545; Veerkracht/Steger 0 deposits; Pelikaan OCMW; Ampel Prisma remine; Terloo Broeders Gent leftover-via-VE; Ter Heyder 0 deposits; GielsBos remine@2334; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW",
    },
])
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Nederheem VZW (Tongeren-Borgloon / VAPH woonondersteuning)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_tongeren_borgloon",
    "community_language": "nl",
    "website": "https://nederheem.be",
    "foi_email": "administratie@nederheem.be",
    "foi_postal": "Heurkensberg 3, 3700 Tongeren-Borgloon",
    "notes": "tick2549 YE2025 Strong official native NBB PDF deposit 2026-00116325 + Strong KBO 0476.473.403 Actief 2 VE; leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type; official zetel Heurkensberg 3 3700 Tongeren-Borgloon since 01.01.2025; RSZ2025 87.202; envelope 70/76A JUMP 3982274; 73 JUMP 3404137; 9901 DROP 18804; 9904 DROP 16319; cash DROP 1236896; FTE 46.9 flat; NOT leftover AGB 0820.533.292; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH",
}])
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_nederheem_tongeren_envelope_70_76a_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3982274", "amount_min_eur": "3982274", "amount_max_eur": "3982274", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +5.41%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p6 native; YE2024 3777881 identical; omzet70 460932 JUMP commercial-only vs large 73; 76A empty (was 68983)"},
    {"budget_id": "bud_nederheem_tongeren_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "460932", "amount_min_eur": "460932", "amount_max_eur": "460932", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +5.09%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p6 native; YE2024 438617 identical; commercial-only vs large 73"},
    {"budget_id": "bud_nederheem_tongeren_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3404137", "amount_min_eur": "3404137", "amount_max_eur": "3404137", "basis": "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +8.14%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p6 native; YE2024 3147864 identical; FOI VAPH/gemeente/onderwijs matrix"},
    {"budget_id": "bud_nederheem_tongeren_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3201119", "amount_min_eur": "3201119", "amount_max_eur": "3201119", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +13.13%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p6 native; YE2024 2829609 identical; FTE 9087 46.9 flat from 46.9"},
    {"budget_id": "bud_nederheem_tongeren_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "151604", "amount_min_eur": "151604", "amount_max_eur": "151604", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 JUMP +7.56%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p6 native; YE2024 140947 identical; capex 72980 (8161+8162+8163); MVA 2018127 DROP"},
    {"budget_id": "bud_nederheem_tongeren_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "18804", "amount_min_eur": "18804", "amount_max_eur": "18804", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -91.40%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p6 native; YE2024 218641 identical; 66A empty (was 9335); 640/8 37566 JUMP"},
    {"budget_id": "bud_nederheem_tongeren_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "16319", "amount_min_eur": "16319", "amount_max_eur": "16319", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -91.53%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p7 native; YE2024 192777 identical; 9903 16319 DROP"},
    {"budget_id": "bud_nederheem_tongeren_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2010623", "amount_min_eur": "2010623", "amount_max_eur": "2010623", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -1.09%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p5 native; YE2024 2032728 identical; kapitaalsubsidies 15 768495 DROP (YE2024 equity-identity 806919; PDF prior column bleed)"},
    {"budget_id": "bud_nederheem_tongeren_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3581908", "amount_min_eur": "3581908", "amount_max_eur": "3581908", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -2.55%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p4 native; YE2024 3675561 identical; MVA 22/27 2018127 DROP; gebouwen 22 1814127 DROP; cash 1236896 DROP; capex 72980"},
    {"budget_id": "bud_nederheem_tongeren_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1571285", "amount_min_eur": "1571285", "amount_max_eur": "1571285", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -4.36%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p5 native; YE2024 1642832 identical"},
    {"budget_id": "bud_nederheem_tongeren_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1236896", "amount_min_eur": "1236896", "amount_max_eur": "1236896", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -2.86%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2549; PDF p4 native; YE2024 1273306 identical; geldbeleggingen 50/53 empty"},
])
print("budgets ok")

cash = {
    "2025_envelope_70_76A": 3982274, "2025_omzet": 460932, "2025_73": 3404137, "2025_76A": 0,
    "2025_pnl": 16319, "2025_bedrijfswinst": 18804, "2025_9903": 16319,
    "2025_equity": 2010623, "2025_assets": 3581908, "2025_debt": 1571285,
    "2025_cash": 1236896, "2025_kapitaalsubsidies": 768495,
    "2025_personnel62": 3201119, "2025_630": 151604, "2025_6408": 37566, "2025_66A": 0,
    "2025_mva": 2018127, "2025_capex": 72980, "2025_fte": 46.9, "2025_gebouwen": 1814127,
    "2024_envelope_70_76A": 3777881, "2024_omzet": 438617, "2024_73": 3147864, "2024_76A": 68983,
    "2024_pnl": 192777, "2024_bedrijfswinst": 218641,
    "2024_equity": 2032728, "2024_assets": 3675561, "2024_debt": 1642832,
    "2024_cash": 1273306, "2024_personnel62": 2829609, "2024_630": 140947, "2024_fte": 46.9,
    "2024_kapitaalsubsidies_equity_identity": 806919,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Nederheem Tongeren-Borgloon YE2025 (70/76A JUMP 3.98m / 73 JUMP 3.40m / 9901 DROP 200k / cash DROP 36k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_tongeren_borgloon leftover VAPH",
    "legal_basis": "VZW Nederheem (KBO 0476.473.403; Actief; 2 VE; official zetel Tongeren-Borgloon; RSZ2025 87.202; official VAPH adreslijst)",
    "decision_date": "2026-04-21",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "3982274",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00116325.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_tongeren_borgloon",
    "cut_option": "Publish VAPH / gemeente Tongeren-Borgloon / onderwijs matrix behind 70/76A JUMP 3982274 and 73 JUMP 3404137 and why 9901 DROP 18804 while FTE flat 46.9 and 62 JUMP 3201119",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Tongeren-Borgloon>Nederheem>JR2025_statutory_L5",
    "notes": "tick2549; Strong official native PDF; leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type; 2 VE; prior-year identical; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}])
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Nederheem Tongeren-Borgloon 70/76A JUMP 3.98m / 73 JUMP 3.40m / 9901 DROP 200k / cash DROP 36k (YE2025 leftover city_tongeren_borgloon leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Tongeren-Borgloon>Nederheem>JR2025",
    "annual_cost_eur": "3982274",
    "total_cost_eur": "3982274",
    "tco_notes": "PDF envelope 70/76A 3982274 JUMP; 73 JUMP 3404137; omzet70 JUMP 460932 commercial-only; 76A empty; bedrijfswinst DROP 18804; pnl DROP 16319; equity DROP 2010623; assets DROP 3581908; debt DROP 1571285; cash DROP 1236896; kapitaalsubsidies DROP 768495; personnel62 JUMP 3201119; leftover city_tongeren_borgloon leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_tongeren_borgloon leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_tongeren_borgloon",
    "measured_outcome": "3.98m 70/76A JUMP; 3.40m 73 JUMP; 200k 9901 DROP; 36k cash DROP; leftover city_tongeren_borgloon leftover VAPH",
    "absurdity_score": "5.55",
    "cost_score": "5.55",
    "difficulty": "4.40",
    "priority_index": "5.55",
    "cut_proposal": "FOI VAPH / gemeente Tongeren-Borgloon / onderwijs matrix behind 70/76A 3982274 and 73 3404137 and why 9901 DROP 18804 while FTE flat 46.9 and 62 JUMP 3201119",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2549 leftover mined city_tongeren_borgloon leftover VAPH leftover-mined AGB-only unused leftover type after OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Veerkracht 0 deposits Steger 0 deposits Pelikaan OCMW Ampel Prisma remine Terloo Broeders Gent leftover-via-VE Ter Heyder 0 deposits GielsBos remine@2334 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; 2 VE; prior-year identical; next rq_2550 leftover dual PLUS every-10; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_tongeren_borgloon leftover VAPH",
}])
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Tongeren-Borgloon>Nederheem>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Tongeren-Borgloon / onderwijs matrix behind VOL-VZW YE2025 70/76A JUMP 3982274, 73 JUMP 3404137, 9901 DROP 18804, cash DROP 1236896, FTE flat 46.9 with 62 JUMP 3201119",
    "why_it_matters": "Public leftover VAPH dual of mined city_tongeren_borgloon shows 3.98m bedrijfsopbrengsten and 3.40m subsidies while VAPH/gemeente/onderwijs matrix and pnl DROP with FTE flat / 62 JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Nederheem / Voorzitter Raad van Bestuur",
    "recipient_email": "administratie@nederheem.be",
    "recipient_postal": "Heurkensberg 3, 3700 Tongeren-Borgloon",
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
    "notes": "tick2549; ready NOT sent; Strong PDF + Strong KBO; leftover city_tongeren_borgloon leftover VAPH",
}])
print("foi ok")
print("CORE WRITE DONE")

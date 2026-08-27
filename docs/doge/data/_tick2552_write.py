from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2552_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_christoforus_merelbeke_jr2025_nbb_pdf_2552"
SRC_KBO = "src_christoforus_merelbeke_kbo_2552"
SRC_SBM = "src_christoforus_merelbeke_sbm_2552"
SRC_SITE = "src_christoforus_merelbeke_site_2552"
EID = "vzw_christoforusgemeenschap_merelbeke_melle"
GAP = "gap_christoforus_merelbeke_vaph_matrix_bruto_jump_1_84m_73_jump_1_72m_cash_jump_169k_fte_jump_20_3_l5"
COMM = "comm_christoforus_merelbeke_jr2025_statutory_bruto_jump_1_84m_73_jump_1_72m_cash_jump_169k_fte_jump_20_3"
LB = "lb_christoforus_merelbeke_bruto_jump_1_84m_73_jump_1_72m_cash_jump_169k_fte_jump_20_3_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2552/2026-00353503_christoforusgemeenschap.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0429.647.642" in blob or "0429647642" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Christoforusgemeenschap deposit 2026-00353503",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00353503.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2552; official native statutory PDF 51561 bytes 15p VKT-VZW 23.0.10 m04-f; header 30/07/2026; AV 08.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-30 10:12:24 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00353503 51561 MD5 511987600a7f419b9231c29267c6f6f8; VKT-VZW 6.1.1 6.5 6.6 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Christoforusgemeenschap 0429.647.642",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0429647642",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2552; Actief Normale toestand since 05.04.1984; VZW; official zetel Asselkouter 34 9820 Merelbeke-Melle since 01.01.2025; 1 VE 2.156.375.128 Christoforusgemeenschap vzw Asselkouter 34 9820 Merelbeke-Melle since 03.10.2006; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; FOI Mattias@christoforus.be since 09.01.2026; NOT leftover AGB 0661.984.022",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Christoforusgemeenschap 0429647642 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0429647642",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2552; deposit-id 2026-00353503 YE 01.01.2025-31.12.2025 filing VKT-VZW header 30.07.2026 AV 08.05.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused; NBB published-deposits API 403 this tick (deposit-id from official CBSO listing via Northdata publicationTitle Cbso 2026-00353503 date 2026-07-30 matching Companyweb neerlegging 30-07-2026); Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope not Northdata",
    },
    {
        "source_id": SRC_SITE,
        "title": "Christoforusgemeenschap site + official VAPH adreslijst",
        "url": "https://www.vaph.be/organisaties/adressen/christoforusgemeenschap",
        "publisher": "Christoforusgemeenschap VZW / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2552; FOI mattias@christoforus.be from official VAPH adreslijst Christoforusgemeenschap (Vergunde Zorgaanbieder tid=1389) + official KBO + site https://www.christoforusgemeenschap.be; leftover mined city_merelbeke_melle leftover VAPH leftover-mined AGB-only unused leftover type after Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546; FIRST LOCK leftover city_merelbeke_melle leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover Nethedal Heist-op-den-Berg YE2024-only",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Christoforusgemeenschap VZW (Merelbeke-Melle / VAPH Vergunde Zorgaanbieder woonondersteuning volwassenen)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_merelbeke_melle",
    "community_language": "nl",
    "website": "https://www.christoforusgemeenschap.be",
    "foi_email": "mattias@christoforus.be",
    "foi_postal": "Asselkouter 34, 9820 Merelbeke-Melle",
    "notes": "tick2552 YE2025 Strong official native NBB PDF deposit 2026-00353503 + Strong KBO 0429.647.642 Actief 1 VE; leftover mined city_merelbeke_melle leftover VAPH leftover-mined AGB-only unused leftover type; official zetel Asselkouter 34 9820 Merelbeke-Melle since 01.01.2025; RSZ2025 87.202; bruto9900 JUMP 1843540; 73 JUMP 1715211; cash JUMP 613428; FTE 20.3 JUMP; NOT leftover AGB 0661.984.022; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_merelbeke_melle leftover VAPH",
}], ent_fields)
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_christoforus_merelbeke_9900_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1843540", "amount_min_eur": "1843540", "amount_max_eur": "1843540", "basis": "NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.76%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p5 native; YE2024 1794072 identical; VKT-VZW has no 70/76A total; 76A empty; 73 is the subsidy envelope vs commercial-only 70"},
    {"budget_id": "bud_christoforus_merelbeke_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "339757", "amount_min_eur": "339757", "amount_max_eur": "339757", "basis": "NBB VKT-VZW code 70 omzet YE2025 JUMP +2.26%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p5 native; YE2024 332242 identical; commercial-only vs large 73"},
    {"budget_id": "bud_christoforus_merelbeke_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1715211", "amount_min_eur": "1715211", "amount_max_eur": "1715211", "basis": "NBB VKT-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +1.66%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p5 native; YE2024 1687203 identical; FOI VAPH/gemeente matrix; VKT has no 733 split"},
    {"budget_id": "bud_christoforus_merelbeke_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1641896", "amount_min_eur": "1641896", "amount_max_eur": "1641896", "basis": "NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +1.84%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p5 native; YE2024 1612270 identical; FTE 9087 20.3 JUMP from 18.9"},
    {"budget_id": "bud_christoforus_merelbeke_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "78844", "amount_min_eur": "78844", "amount_max_eur": "78844", "basis": "NBB VKT-VZW code 630 afschrijvingen YE2025 DROP -6.95%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p5 native; YE2024 84732 identical; capex 8169 17313; MVA 22/27 1376491 DROP"},
    {"budget_id": "bud_christoforus_merelbeke_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "76482", "amount_min_eur": "76482", "amount_max_eur": "76482", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +2.79%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p5 native; YE2024 74407 identical; 66A empty; 640/8 46318 JUMP +104.38%"},
    {"budget_id": "bud_christoforus_merelbeke_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "77378", "amount_min_eur": "77378", "amount_max_eur": "77378", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +0.75%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p5 native; YE2024 76802 identical; 9903 77378 JUMP"},
    {"budget_id": "bud_christoforus_merelbeke_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1968021", "amount_min_eur": "1968021", "amount_max_eur": "1968021", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +3.69%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p4 native; YE2024 1897897 identical; kapitaalsubsidies 15 12844 DROP -49.59%"},
    {"budget_id": "bud_christoforus_merelbeke_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2697026", "amount_min_eur": "2697026", "amount_max_eur": "2697026", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.35%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p3 native; YE2024 2635022 identical; MVA 22/27 1376491 DROP; gebouwen 22 1312070 DROP; cash 613428 JUMP; capex 17313"},
    {"budget_id": "bud_christoforus_merelbeke_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "729004", "amount_min_eur": "729004", "amount_max_eur": "729004", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.10%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p4 native; YE2024 737125 identical"},
    {"budget_id": "bud_christoforus_merelbeke_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "613428", "amount_min_eur": "613428", "amount_max_eur": "613428", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +38.19%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2552; PDF p3 native; YE2024 443912 identical; geldbeleggingen 50/53 empty"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_bruto9900": 1843540, "2025_omzet": 339757, "2025_73": 1715211, "2025_76A": 0,
    "2025_pnl": 77378, "2025_bedrijfswinst": 76482, "2025_9903": 77378,
    "2025_equity": 1968021, "2025_assets": 2697026, "2025_debt": 729004,
    "2025_cash": 613428, "2025_kapitaalsubsidies": 12844, "2025_geldbeleggingen": 0,
    "2025_personnel62": 1641896, "2025_630": 78844, "2025_6408": 46318, "2025_66A": 0,
    "2025_mva": 1376491, "2025_capex": 17313, "2025_fte": 20.3, "2025_gebouwen": 1312070,
    "2025_aanbouw": 0, "2025_destin691": 125000, "2025_destin791": 25000,
    "2024_bruto9900": 1794072, "2024_omzet": 332242, "2024_73": 1687203, "2024_76A": 0,
    "2024_pnl": 76802, "2024_bedrijfswinst": 74407,
    "2024_equity": 1897897, "2024_assets": 2635022, "2024_debt": 737125,
    "2024_cash": 443912, "2024_personnel62": 1612270, "2024_630": 84732, "2024_fte": 18.9,
    "2024_kapitaalsubsidies": 25478, "2024_geldbeleggingen": 0,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Christoforusgemeenschap Merelbeke-Melle YE2025 (bruto9900 JUMP 1.84m / 73 JUMP 1.72m / cash JUMP 169k / FTE JUMP 20.3 / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_merelbeke_melle leftover VAPH",
    "legal_basis": "VZW Christoforusgemeenschap (KBO 0429.647.642; Actief; 1 VE; official zetel Merelbeke-Melle; RSZ2025 87.202; official VAPH adreslijst Vergunde Zorgaanbieder)",
    "decision_date": "2026-05-08",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1715211",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00353503.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_merelbeke_melle",
    "cut_option": "Publish VAPH / gemeente Merelbeke-Melle matrix behind 73 JUMP 1715211 and bruto9900 JUMP 1843540 and why cash JUMP 613428 while 640/8 JUMP 46318 and kapitaalsubsidies DROP 12844 and FTE JUMP 20.3",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Merelbeke-Melle>Christoforusgemeenschap>JR2025_statutory_L5",
    "notes": "tick2552; Strong official native PDF; leftover mined city_merelbeke_melle leftover VAPH leftover-mined AGB-only unused leftover type; 1 VE; prior-year identical; FIRST LOCK leftover city_merelbeke_melle leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Christoforusgemeenschap Merelbeke-Melle bruto9900 JUMP 1.84m / 73 JUMP 1.72m / cash JUMP 169k / FTE JUMP 20.3 (YE2025 leftover city_merelbeke_melle leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Merelbeke-Melle>Christoforusgemeenschap>JR2025",
    "annual_cost_eur": "1715211",
    "total_cost_eur": "1715211",
    "tco_notes": "PDF 73 subsidies 1715211 JUMP; bruto9900 1843540 JUMP; omzet70 JUMP 339757 commercial-only; 76A empty; bedrijfswinst JUMP 76482; pnl JUMP 77378; equity JUMP 1968021; assets JUMP 2697026; debt DROP 729004; cash JUMP 613428; geldbeleggingen empty; kapitaalsubsidies DROP 12844; personnel62 JUMP 1641896; leftover city_merelbeke_melle leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_merelbeke_melle leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_merelbeke_melle",
    "measured_outcome": "1.84m bruto9900 JUMP; 1.72m 73 JUMP; 169k cash JUMP; 20.3 FTE JUMP; leftover city_merelbeke_melle leftover VAPH",
    "absurdity_score": "5.45",
    "cost_score": "4.95",
    "difficulty": "4.40",
    "priority_index": "5.32",
    "cut_proposal": "FOI VAPH / gemeente Merelbeke-Melle matrix behind 73 1715211 and bruto9900 1843540 and why cash JUMP 613428 while 640/8 JUMP 46318 and kapitaalsubsidies DROP 12844 and FTE JUMP 20.3",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2552 leftover mined city_merelbeke_melle leftover VAPH leftover-mined AGB-only unused leftover type after Ter Loke remine@2551 Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Veerkracht 0 deposits Steger 0 deposits Pelikaan OCMW Ampel Prisma remine Terloo Broeders Gent leftover-via-VE leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover city_vosselaar leftover VAPH Ter Loke remine@2551 leftover city_heist_op_den_berg leftover VAPH Nethedal YE2024-only SKIP; 1 VE; prior-year identical; next rq_2553 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_merelbeke_melle leftover VAPH",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Merelbeke-Melle>Christoforusgemeenschap>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Merelbeke-Melle matrix behind VKT-VZW YE2025 73 JUMP 1715211, bruto9900 JUMP 1843540, cash JUMP 613428, 640/8 JUMP 46318, kapitaalsubsidies DROP 12844, FTE JUMP 20.3 with 62 JUMP 1641896",
    "why_it_matters": "Public leftover VAPH dual of mined city_merelbeke_melle shows 1.72m subsidies and 1.84m brutomarge while VAPH/gemeente matrix and cash JUMP 38 percent with 640/8 JUMP 104 percent stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Christoforusgemeenschap / Voorzitter Raad van Bestuur",
    "recipient_email": "mattias@christoforus.be",
    "recipient_postal": "Asselkouter 34, 9820 Merelbeke-Melle",
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
    "notes": "tick2552; ready NOT sent; Strong PDF + Strong KBO; leftover city_merelbeke_melle leftover VAPH",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

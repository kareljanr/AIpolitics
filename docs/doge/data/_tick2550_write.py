from pathlib import Path
import csv, json, re

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2550_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_wagenschot_nazareth_jr2025_nbb_pdf_2550"
SRC_KBO = "src_wagenschot_nazareth_kbo_2550"
SRC_SBM = "src_wagenschot_nazareth_sbm_2550"
SRC_SITE = "src_wagenschot_nazareth_site_2550"
EID = "vzw_wagenschot_nazareth"
GAP = "gap_wagenschot_nazareth_vaph_matrix_70_76a_jump_14_53m_73_jump_14_17m_9901_flip_profit_272k_cash_drop_617k_l5"
COMM = "comm_wagenschot_nazareth_jr2025_statutory_70_76a_jump_14_53m_73_jump_14_17m_9901_flip_profit_272k_cash_drop_617k"
LB = "lb_wagenschot_nazareth_70_76a_jump_14_53m_73_jump_14_17m_9901_flip_profit_272k_cash_drop_617k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2550/2026-00232932_wagenschot.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0435.044.505" in blob or "0435044505" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Pedagogisch Centrum Wagenschot deposit 2026-00232932",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00232932.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2550; official native statutory PDF 762239 bytes 47p VOL-VZW 25.0.13 m05-f; header 30/06/2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-01 13:28:28 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00232932 762239 MD5 fbf369abeb026ff076008a4cfe491c43; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.6 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.11 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Pedagogisch Centrum Wagenschot 0435.044.505",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435044505",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2550; Actief Normale toestand since 29.01.1988; VZW; official zetel Steenweg 2 9810 Nazareth-De Pinte since 01.01.2025; 2 VE 2.320.873.072 Pedagogisch Centrum Wagenschot vzw - Marc Tieberghien Steenweg 2 9810 Nazareth-De Pinte since 01.01.2025 (begindatum 29.01.1988) + 2.270.015.279 MFC Heynsdaele Eisdale 1 9600 Ronse leftover-via-VE FROM leftover city_nazareth_depinte since 01.01.2018; RSZ2025 87.991; Werkgever RSZ since 01.10.1989; Aanbestedende overheid since 18.01.2003; NOT leftover AGB 0643.819.583",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Wagenschot 0435044505 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0435044505",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2550; deposit-id 2026-00232932 YE 01.01.2025-31.12.2025 filing VOL-VZW header 30.06.2026 AV 24.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Wagenschot site + official VAPH adreslijst",
        "url": "https://www.vaph.be/organisaties/adressen/wagenschot",
        "publisher": "Pedagogisch Centrum Wagenschot VZW / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2550; FOI info@wagenschot.be from official VAPH adreslijst Wagenschot + official KBO; PDF pedagogisch.centrum@wagenschot.be; site https://www.wagenschot.be; leftover mined city_nazareth_depinte leftover VAPH leftover-mined AGB-only unused leftover type after Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545; Veerkracht/Steger 0 deposits; Pelikaan OCMW; Ampel Prisma remine; Terloo Broeders Gent leftover-via-VE; Ter Heyder 0 deposits; GielsBos remine@2334; Heynsdaele 0 deposits is VE of this parent not leftover-via-VE of leftover city_ronse as parent; FIRST LOCK leftover city_nazareth_depinte leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW",
    },
])
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Pedagogisch Centrum Wagenschot VZW (Nazareth-De Pinte / VAPH jeugdhulp + MFC Heynsdaele)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_nazareth_depinte",
    "community_language": "nl",
    "website": "https://www.wagenschot.be",
    "foi_email": "info@wagenschot.be",
    "foi_postal": "Steenweg 2, 9810 Nazareth-De Pinte",
    "notes": "tick2550 YE2025 Strong official native NBB PDF deposit 2026-00232932 + Strong KBO 0435.044.505 Actief 2 VE; leftover mined city_nazareth_depinte leftover VAPH leftover-mined AGB-only unused leftover type; official zetel Steenweg 2 9810 Nazareth-De Pinte since 01.01.2025; RSZ2025 87.991; envelope 70/76A JUMP 14532585; 73 JUMP 14167695; 9901 FLIP PROFIT 272407; 9904 FLIP PROFIT 158604; cash DROP 832350; FTE 163 DROP; NOT leftover AGB 0643.819.583; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_nazareth_depinte leftover VAPH",
}])
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_wagenschot_nazareth_envelope_70_76a_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "14532585", "amount_min_eur": "14532585", "amount_max_eur": "14532585", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +9.84%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p7 native; YE2024 13230498 identical; omzet70 175185 DROP commercial-only vs large 73; 76A empty"},
    {"budget_id": "bud_wagenschot_nazareth_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "175185", "amount_min_eur": "175185", "amount_max_eur": "175185", "basis": "NBB VOL-VZW code 70 omzet YE2025 DROP -12.03%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p7 native; YE2024 199137 identical; commercial-only vs large 73"},
    {"budget_id": "bud_wagenschot_nazareth_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "14167695", "amount_min_eur": "14167695", "amount_max_eur": "14167695", "basis": "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +10.27%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p7 native; YE2024 12848539 identical; 733 13877847 JUMP; 73-733 gap 289848 FOI"},
    {"budget_id": "bud_wagenschot_nazareth_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12279689", "amount_min_eur": "12279689", "amount_max_eur": "12279689", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +4.79%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p7 native; YE2024 11718713 identical; FTE 9087 163 DROP from 164.5"},
    {"budget_id": "bud_wagenschot_nazareth_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "600295", "amount_min_eur": "600295", "amount_max_eur": "600295", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 DROP -1.06%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p7 native; YE2024 606710 identical; capex 106722 (8161+8162+8163+8164+8165); MVA 8145304 DROP"},
    {"budget_id": "bud_wagenschot_nazareth_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "272407", "amount_min_eur": "272407", "amount_max_eur": "272407", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 FLIP PROFIT", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p7 native; YE2024 -457013 identical; 66A empty; 640/8 78142 DROP"},
    {"budget_id": "bud_wagenschot_nazareth_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "158604", "amount_min_eur": "158604", "amount_max_eur": "158604", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 FLIP PROFIT", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p8 native; YE2024 -580679 identical; 9903 158604 FLIP PROFIT"},
    {"budget_id": "bud_wagenschot_nazareth_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4757008", "amount_min_eur": "4757008", "amount_max_eur": "4757008", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -2.43%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p6 native; YE2024 4875577 identical; kapitaalsubsidies 15 3963755 DROP"},
    {"budget_id": "bud_wagenschot_nazareth_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "11120506", "amount_min_eur": "11120506", "amount_max_eur": "11120506", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -3.17%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p5 native; YE2024 11484809 identical; MVA 22/27 8145304 DROP; gebouwen 22 6244499 DROP; cash 832350 DROP; capex 106722"},
    {"budget_id": "bud_wagenschot_nazareth_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6363498", "amount_min_eur": "6363498", "amount_max_eur": "6363498", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -3.72%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p6 native; YE2024 6609232 identical"},
    {"budget_id": "bud_wagenschot_nazareth_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "832350", "amount_min_eur": "832350", "amount_max_eur": "832350", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -42.57%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2550; PDF p5 native; YE2024 1449252 identical; geldbeleggingen 50/53 empty"},
])
print("budgets ok")

cash = {
    "2025_envelope_70_76A": 14532585, "2025_omzet": 175185, "2025_73": 14167695, "2025_76A": 0,
    "2025_733": 13877847, "2025_74": 189704, "2025_731": 34376,
    "2025_pnl": 158604, "2025_bedrijfswinst": 272407, "2025_9903": 158604,
    "2025_equity": 4757008, "2025_assets": 11120506, "2025_debt": 6363498,
    "2025_cash": 832350, "2025_kapitaalsubsidies": 3963755,
    "2025_personnel62": 12279689, "2025_630": 600295, "2025_6408": 78142, "2025_66A": 0,
    "2025_mva": 8145304, "2025_capex": 106722, "2025_fte": 163.0, "2025_gebouwen": 6244499,
    "2024_envelope_70_76A": 13230498, "2024_omzet": 199137, "2024_73": 12848539, "2024_76A": 0,
    "2024_pnl": -580679, "2024_bedrijfswinst": -457013,
    "2024_equity": 4875577, "2024_assets": 11484809, "2024_debt": 6609232,
    "2024_cash": 1449252, "2024_personnel62": 11718713, "2024_630": 606710, "2024_fte": 164.5,
    "2024_kapitaalsubsidies": 4240928,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Wagenschot Nazareth-De Pinte YE2025 (70/76A JUMP 14.53m / 73 JUMP 14.17m / 9901 FLIP PROFIT 272k / cash DROP 617k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_nazareth_depinte leftover VAPH",
    "legal_basis": "VZW Pedagogisch Centrum Wagenschot (KBO 0435.044.505; Actief; 2 VE; official zetel Nazareth-De Pinte; RSZ2025 87.991; official VAPH adreslijst)",
    "decision_date": "2026-06-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "14532585",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00232932.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_nazareth_depinte",
    "cut_option": "Publish VAPH / gemeente Nazareth-De Pinte / onderwijs / Ronse matrix behind 70/76A JUMP 14532585 and 73 JUMP 14167695 and why 9901 FLIP PROFIT 272407 while cash DROP 832350 and FTE DROP 163",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Nazareth-De Pinte>Wagenschot>JR2025_statutory_L5",
    "notes": "tick2550; Strong official native PDF; leftover mined city_nazareth_depinte leftover VAPH leftover-mined AGB-only unused leftover type; 2 VE; prior-year identical; FIRST LOCK leftover city_nazareth_depinte leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}])
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Wagenschot Nazareth-De Pinte 70/76A JUMP 14.53m / 73 JUMP 14.17m / 9901 FLIP PROFIT 272k / cash DROP 617k (YE2025 leftover city_nazareth_depinte leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Nazareth-De Pinte>Wagenschot>JR2025",
    "annual_cost_eur": "14532585",
    "total_cost_eur": "14532585",
    "tco_notes": "PDF envelope 70/76A 14532585 JUMP; 73 JUMP 14167695; omzet70 DROP 175185 commercial-only; 76A empty; bedrijfswinst FLIP PROFIT 272407; pnl FLIP PROFIT 158604; equity DROP 4757008; assets DROP 11120506; debt DROP 6363498; cash DROP 832350; kapitaalsubsidies DROP 3963755; personnel62 JUMP 12279689; leftover city_nazareth_depinte leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_nazareth_depinte leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_nazareth_depinte",
    "measured_outcome": "14.53m 70/76A JUMP; 14.17m 73 JUMP; 272k 9901 FLIP PROFIT; 617k cash DROP; leftover city_nazareth_depinte leftover VAPH",
    "absurdity_score": "6.00",
    "cost_score": "5.50",
    "difficulty": "4.50",
    "priority_index": "5.68",
    "cut_proposal": "FOI VAPH / gemeente Nazareth-De Pinte / onderwijs / Ronse matrix behind 70/76A 14532585 and 73 14167695 and why 9901 FLIP PROFIT 272407 while cash DROP 832350 and FTE DROP 163",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2550 leftover mined city_nazareth_depinte leftover VAPH leftover-mined AGB-only unused leftover type after Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Veerkracht 0 deposits Steger 0 deposits Pelikaan OCMW Ampel Prisma remine Terloo Broeders Gent leftover-via-VE Ter Heyder 0 deposits GielsBos remine@2334 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover city_tongeren_borgloon leftover VAPH Nederheem remine@2549; 2 VE; prior-year identical; next rq_2551 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_nazareth_depinte leftover VAPH",
}])
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Nazareth-De Pinte>Wagenschot>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / gemeente Nazareth-De Pinte / onderwijs / Ronse matrix behind VOL-VZW YE2025 70/76A JUMP 14532585, 73 JUMP 14167695, 9901 FLIP PROFIT 272407, cash DROP 832350, FTE DROP 163 with 62 JUMP 12279689",
    "why_it_matters": "Public leftover VAPH dual of mined city_nazareth_depinte shows 14.53m bedrijfsopbrengsten and 14.17m subsidies while VAPH/gemeente/onderwijs/Ronse matrix and 9901 FLIP PROFIT with cash DROP 43 percent stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Pedagogisch Centrum Wagenschot / Voorzitter Raad van Bestuur",
    "recipient_email": "info@wagenschot.be",
    "recipient_postal": "Steenweg 2, 9810 Nazareth-De Pinte",
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
    "notes": "tick2550; ready NOT sent; Strong PDF + Strong KBO; leftover city_nazareth_depinte leftover VAPH",
}])
print("foi ok")
print("CORE WRITE DONE")

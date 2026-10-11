from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2558_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_duizendschoon_as_jr2025_nbb_pdf_2558"
SRC_KBO = "src_duizendschoon_as_kbo_2558"
SRC_VAPH = "src_duizendschoon_as_vaph_2558"
SRC_SITE = "src_duizendschoon_as_site_2558"
EID = "vzw_duizendschoon_as"
GAP = "gap_duizendschoon_as_vaph_matrix_bruto_jump_216k_9901_drop_36k_cash_jump_79k_l5"
COMM = "comm_duizendschoon_as_jr2025_statutory_bruto_jump_216k_9901_drop_36k_cash_jump_79k"
LB = "lb_duizendschoon_as_bruto_jump_216k_9901_drop_36k_cash_jump_79k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2558/2026-00236227.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0683.687.177" in blob or "0683687177" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Duizendschoon deposit 2026-00236227",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00236227.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2558; official native statutory PDF 42056 bytes 10p VKT-VZW 26.0.15 m04-f; header 01/07/2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-02 09:14:50 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00236227 42056 MD5 58a7b5f8215ee855ac02229d3cc191da; VKT-VZW 6.1.1 6.1.2 6.1.3 6.2 6.3 6.5 6.6 7 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Duizendschoon 0683.687.177",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0683687177",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2558; Actief Normale toestand; VZW; official zetel Bilzerweg 88 3665 As since 25.09.2017; 1 VE 2.287.333.145 DUIZENDSCHOON Bilzerweg 88 since 05.04.2019; RSZ2025 88.104 Activiteiten van dagcentra voor volwassenen met een lichamelijke handicap; Werkgever RSZ; FOI info@arbeidskansen.be from official KBO VE; NOT leftover Labor Arbeidskansen 0432.385.616 remine@2292 under sec_flanders",
    },
    {
        "source_id": SRC_VAPH,
        "title": "VAPH adreslijst Duizendschoon Vergunde Zorgaanbieder",
        "url": "https://www.vaph.be/organisaties/adressen/duizendschoon-0",
        "publisher": "VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2558; official VAPH adreslijst Type organisatie Vergunde Zorgaanbieder; admin adres Bilzerweg 88 3665 As; FOI annelies.resink@arbeidskansen.be on VAPH teaser / info@arbeidskansen.be on official KBO VE; leftover mined city_as leftover VAPH after city GE tick882; FIRST LOCK leftover city_as leftover VAPH Duizendschoon",
    },
    {
        "source_id": SRC_SITE,
        "title": "Arbeidskansen / Duizendschoon official site FOI email",
        "url": "https://www.arbeidskansen.be/",
        "publisher": "Arbeidskansen / Duizendschoon VZW",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2558; FOI info@arbeidskansen.be from official KBO VE; Duizendschoon is dagondersteuningscentrum of Arbeidskansen group but own VZW 0683.687.177; leftover mined city_as leftover VAPH unused leftover type after city GE tick882; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover Labor Arbeidskansen remine@2292",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Duizendschoon VZW (As / VAPH Vergunde Zorgaanbieder; dagondersteuning)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_as",
    "community_language": "nl",
    "website": "https://www.arbeidskansen.be/",
    "foi_email": "info@arbeidskansen.be",
    "foi_postal": "Bilzerweg 88, 3665 As",
    "notes": "tick2558 YE2025 Strong official native NBB PDF deposit 2026-00236227 + Strong KBO 0683.687.177 Actief 1 VE; leftover mined city_as leftover VAPH unused leftover type after city GE tick882; official zetel Bilzerweg 88 3665 As; RSZ2025 88.104; bruto9900 JUMP 215719; 9901 DROP 25883; cash JUMP 140931 (+79k); FTE 1.6 JUMP; NOT leftover Labor Arbeidskansen 0432.385.616 remine@2292; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_as leftover VAPH Duizendschoon",
}], ent_fields)
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_duizendschoon_as_bruto9900_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "215719", "amount_min_eur": "215719", "amount_max_eur": "215719", "basis": "NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +12.79%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 191250 identical; VKT envelope because 73 empty and bruto >> omzet70; FOI VAPH matrix behind 215719"},
    {"budget_id": "bud_duizendschoon_as_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8261", "amount_min_eur": "8261", "amount_max_eur": "8261", "basis": "NBB VKT-VZW code 70 omzet YE2025 JUMP +2.75%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 8040 identical; commercial-only vs empty 73; envelope is bruto 9900 not 70"},
    {"budget_id": "bud_duizendschoon_as_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; 73 empty VKT; FOI VAPH/gemeente matrix behind empty 73 vs bruto 215719"},
    {"budget_id": "bud_duizendschoon_as_74_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 74 andere bedrijfsopbrengsten YE2025 not on VKT form", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; 74 not on VKT-VZW 4; 76A empty; 60/61 48001 DROP from 84355"},
    {"budget_id": "bud_duizendschoon_as_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "189836", "amount_min_eur": "189836", "amount_max_eur": "189836", "basis": "NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +49.19%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 127243 identical; FTE 9087 1.6 JUMP from 1; 105 YE 0.8"},
    {"budget_id": "bud_duizendschoon_as_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 630 afschrijvingen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; 630 empty; MVA 22/27 empty; capex empty; 640/8 0 DROP from 2167"},
    {"budget_id": "bud_duizendschoon_as_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "25883", "amount_min_eur": "25883", "amount_max_eur": "25883", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -58.15%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 61840 identical; 66A empty; 640/8 0 DROP"},
    {"budget_id": "bud_duizendschoon_as_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "25514", "amount_min_eur": "25514", "amount_max_eur": "25514", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -58.50%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 61477 identical; 9903 25514 DROP"},
    {"budget_id": "bud_duizendschoon_as_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "132999", "amount_min_eur": "132999", "amount_max_eur": "132999", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +23.74%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 107485 identical; overgedragen 14 132999 JUMP; kapitaalsubsidies 15 empty; destin 691/791 empty"},
    {"budget_id": "bud_duizendschoon_as_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "206531", "amount_min_eur": "206531", "amount_max_eur": "206531", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +5.38%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 195986 identical; MVA 22/27 empty; cash 140931 JUMP; vorderingen 40/41 46520 DROP from 115692"},
    {"budget_id": "bud_duizendschoon_as_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "140931", "amount_min_eur": "140931", "amount_max_eur": "140931", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +126.66%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2558; PDF p native; YE2024 62177 identical; debt 17/49 73532 DROP from 88500; geldbeleggingen 50/53 empty"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_bruto9900": 215719, "2025_omzet": 8261, "2025_73": None, "2025_74": None, "2025_76A": None,
    "2025_pnl": 25514, "2025_bedrijfswinst": 25883, "2025_9903": 25514,
    "2025_equity": 132999, "2025_assets": 206531, "2025_debt": 73532,
    "2025_cash": 140931, "2025_kapitaalsubsidies": None, "2025_geldbeleggingen": None,
    "2025_personnel62": 189836, "2025_630": None, "2025_6408": 0,
    "2025_mva": None, "2025_capex": None, "2025_fte": 1.6, "2025_gebouwen": None,
    "2025_aanbouw": None, "2025_destin691": None, "2025_destin791": None, "2025_60_61": 48001,
    "2024_bruto9900": 191250, "2024_omzet": 8040, "2024_73": None,
    "2024_pnl": 61477, "2024_bedrijfswinst": 61840,
    "2024_equity": 107485, "2024_assets": 195986, "2024_debt": 88500,
    "2024_cash": 62177, "2024_personnel62": 127243, "2024_630": None, "2024_fte": 1,
    "2024_6408": 2167, "2024_60_61": 84355,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Duizendschoon As YE2025 (bruto9900 JUMP 216k / 9901 DROP 36k / cash JUMP 79k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_as leftover dual",
    "legal_basis": "Duizendschoon VZW (KBO 0683.687.177; Actief; 1 VE; official zetel As; RSZ2025 88.104; VAPH Vergunde Zorgaanbieder)",
    "decision_date": "2026-06-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "215719",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00236227.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_as",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind bruto9900 JUMP 215719 vs empty 73 and why 9901 DROP 25883 while cash JUMP 140931 and 62 JUMP 189836",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>As>Duizendschoon>JR2025_statutory_L5",
    "notes": "tick2558; Strong official native PDF; leftover mined city_as leftover VAPH unused leftover type after city GE tick882; 1 VE; prior-year identical; FIRST LOCK leftover city_as leftover VAPH Duizendschoon; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Duizendschoon As bruto9900 JUMP 216k / 9901 DROP 36k / cash JUMP 79k (YE2025 leftover city_as leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>As>Duizendschoon>JR2025",
    "annual_cost_eur": "215719",
    "total_cost_eur": "215719",
    "tco_notes": "PDF bruto9900 215719 JUMP; 73 empty; omzet70 JUMP 8261; 76A empty; bedrijfswinst DROP 25883; pnl DROP 25514; equity JUMP 132999; assets JUMP 206531; debt DROP 73532; cash JUMP 140931; kapitaalsubsidies empty; personnel62 JUMP 189836; leftover city_as leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_as leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_as",
    "measured_outcome": "216k bruto9900 JUMP; 36k 9901 DROP; 79k cash JUMP; 1.6 FTE JUMP; leftover city_as leftover VAPH",
    "absurdity_score": "5.50",
    "cost_score": "5.20",
    "difficulty": "4.40",
    "priority_index": "5.33",
    "cut_proposal": "FOI VAPH/gemeentelijke matrix behind bruto9900 215719 vs empty 73 and why 9901 DROP 25883 while cash JUMP 140931 and 62 JUMP 189836 with FTE 1.6",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2558 leftover mined city_as leftover VAPH Duizendschoon after city GE tick882; hunt skips AGB-only VAPH stall boortmeerbeek/beersel/hoeilaart/kaprijke/lendelede/wielsbeke/ardooie/nieuwpoort/middelkerke/hulshout 0 VAPH admin adres; leftover city_beringen 0 VAPH admin; leftover city_destelbergen Kannet vrijetijdszorg SKIP; leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum remine@2557 leftover city_peer leftover VAPH Monsheide remine@2556; 1 VE; prior-year identical; next rq_2559 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_as leftover VAPH Duizendschoon; never mix off-TE dual into 348bn TE pie",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>As>Duizendschoon>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VKT-VZW YE2025 bruto9900 JUMP 215719 vs empty 73, 9901 DROP 25883 with cash JUMP 140931 (+79k), FTE JUMP 1.6 with 62 JUMP 189836",
    "why_it_matters": "Public leftover VAPH dual of mined city_as shows 216k bruto envelope while subsidy matrix and 9901 DROP 36k / cash JUMP 79k stay unsourced",
    "priority": "7",
    "recipient_body": "Duizendschoon VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@arbeidskansen.be",
    "recipient_postal": "Bilzerweg 88, 3665 As",
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
    "notes": "tick2558; ready NOT sent; Strong PDF + Strong KBO; leftover city_as leftover VAPH Duizendschoon",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

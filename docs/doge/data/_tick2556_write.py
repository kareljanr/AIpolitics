from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2556_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_monsheide_peer_jr2025_nbb_pdf_2556"
SRC_KBO = "src_monsheide_peer_kbo_2556"
SRC_SBM = "src_monsheide_peer_sbm_2556"
SRC_SITE = "src_monsheide_peer_site_2556"
EID = "vzw_monsheide_peer"
GAP = "gap_monsheide_peer_vaph_matrix_70_76a_jump_6_36m_73_jump_5_28m_cash_jump_368k_l5"
COMM = "comm_monsheide_peer_jr2025_statutory_70_76a_jump_6_36m_73_jump_5_28m_cash_jump_368k"
LB = "lb_monsheide_peer_70_76a_jump_6_36m_73_jump_5_28m_cash_jump_368k_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2556/2026-00180864.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0419.081.867" in blob or "0419081867" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Monsheide deposit 2026-00180864",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00180864.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2556; official native statutory PDF 3133349 bytes 39p VOL-VZW 26.0.15 m05-f; header 22/06/2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-22 09:06:17 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00180864 3133349 MD5 a59e63763f14857612bd6ce1c0508d17; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.5 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.10 6.11 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Monsheide 0419.081.867",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419081867",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2556; Actief Normale toestand; VZW since 20.11.1978; official zetel Monsheide 4 3990 Peer since 21.03.2001; Begindatum 20.11.1978; 1 VE 2.154.985.949 Home Monsheide vzw Monsheide 4 since 10.07.2006; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een handicap; Werkgever RSZ; Aanbestedende overheid; FOI onthaal@monsheide.be; NOT leftover city GE Peer 0207.474.189; NOT leftover OCMW Peer 0212.207.888; NOT leftover Buseloc 0433.160.527; NOT leftover BC Sint-Elisabeth Peer 0418.714.851 (sec_flanders remine)",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / Northdata fiche Monsheide 0419081867 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0419081867",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2556; deposit-id 2026-00180864 YE 01.01.2025-31.12.2025 filing VOL-VZW header 22.06.2026 AV 18.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub unused; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope not Northdata",
    },
    {
        "source_id": SRC_SITE,
        "title": "Monsheide official site / VAPH adreslijst",
        "url": "https://www.monsheide.be/",
        "publisher": "Monsheide / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2556; FOI onthaal@monsheide.be from official KBO + official VAPH adreslijst https://www.vaph.be/organisaties/adressen/monsheide Vergunde Zorgaanbieder + RTH; leftover mined city_peer leftover VAPH after city GE tick1099; FIRST LOCK leftover city_peer leftover VAPH Monsheide; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover BC Sint-Elisabeth Peer remine under sec_flanders",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Monsheide VZW (Peer / VAPH Vergunde Zorgaanbieder + RTH woonondersteuning)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_peer",
    "community_language": "nl",
    "website": "https://www.monsheide.be/",
    "foi_email": "onthaal@monsheide.be",
    "foi_postal": "Monsheide 4, 3990 Peer",
    "notes": "tick2556 YE2025 Strong official native NBB PDF deposit 2026-00180864 + Strong KBO 0419.081.867 Actief 1 VE; leftover mined city_peer leftover VAPH unused leftover type after city GE tick1099; official zetel Monsheide 4 3990 Peer since 21.03.2001; RSZ2025 87.202; envelope 70/76A JUMP 6359534; 73 JUMP 5281699; cash JUMP 1222197 (+368k); FTE 66.8 JUMP; NOT leftover city GE 0207.474.189; NOT leftover OCMW 0212.207.888; NOT leftover Buseloc 0433.160.527; NOT leftover BC Sint-Elisabeth 0418.714.851; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_peer leftover VAPH Monsheide",
}], ent_fields)
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_monsheide_peer_envelope70_76a_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6359534", "amount_min_eur": "6359534", "amount_max_eur": "6359534", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +8.93%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 5838281 identical; 76A empty; subsidies sit in 73/733"},
    {"budget_id": "bud_monsheide_peer_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "810370", "amount_min_eur": "810370", "amount_max_eur": "810370", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +2.33%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 791927 identical; commercial-only vs large 73"},
    {"budget_id": "bud_monsheide_peer_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5281699", "amount_min_eur": "5281699", "amount_max_eur": "5281699", "basis": "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +10.00%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 4801399 identical; subsidies 733 5273599 JUMP; schenkingen 731 8100"},
    {"budget_id": "bud_monsheide_peer_74_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "267465", "amount_min_eur": "267465", "amount_max_eur": "267465", "basis": "NBB VOL-VZW code 74 andere bedrijfsopbrengsten YE2025 JUMP +9.19%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 244955 identical; 76A empty"},
    {"budget_id": "bud_monsheide_peer_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4786225", "amount_min_eur": "4786225", "amount_max_eur": "4786225", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +9.71%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 4362725 identical; FTE 9087 66.8 JUMP from 62.3"},
    {"budget_id": "bud_monsheide_peer_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "312175", "amount_min_eur": "312175", "amount_max_eur": "312175", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 JUMP +0.62%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 310266 identical; capex ~139328; MVA 22/27 2899357 DROP"},
    {"budget_id": "bud_monsheide_peer_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "518731", "amount_min_eur": "518731", "amount_max_eur": "518731", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +10.45%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 469641 identical; 640/8 40091 DROP"},
    {"budget_id": "bud_monsheide_peer_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "603637", "amount_min_eur": "603637", "amount_max_eur": "603637", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +6.21%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 568352 identical; 9903 603637"},
    {"budget_id": "bud_monsheide_peer_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6747285", "amount_min_eur": "6747285", "amount_max_eur": "6747285", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +9.16%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 6180840 identical; kapitaalsubsidies 15 147793 DROP; destin 691 351637 JUMP"},
    {"budget_id": "bud_monsheide_peer_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8536334", "amount_min_eur": "8536334", "amount_max_eur": "8536334", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +5.91%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 8059785 identical; MVA 22/27 2899357 DROP; gebouwen 22 2193089 DROP; cash 1222197 JUMP; geldbeleggingen 4131000 JUMP; capex ~139328"},
    {"budget_id": "bud_monsheide_peer_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1222197", "amount_min_eur": "1222197", "amount_max_eur": "1222197", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +43.08%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2556; PDF p native; YE2024 854185 identical; debt 17/49 1789049 DROP; geldbeleggingen 50/53 4131000 JUMP"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_envelope70_76A": 6359534, "2025_omzet": 810370, "2025_73": 5281699, "2025_733": 5273599, "2025_731": 8100, "2025_74": 267465, "2025_76A": 0,
    "2025_pnl": 603637, "2025_bedrijfswinst": 518731, "2025_9903": 603637,
    "2025_equity": 6747285, "2025_assets": 8536334, "2025_debt": 1789049,
    "2025_cash": 1222197, "2025_kapitaalsubsidies": 147793, "2025_geldbeleggingen": 4131000,
    "2025_personnel62": 4786225, "2025_630": 312175, "2025_6408": 40091,
    "2025_mva": 2899357, "2025_capex": 139328, "2025_fte": 66.8, "2025_gebouwen": 2193089,
    "2025_aanbouw": 122965, "2025_destin691": 351637, "2025_destin791": 0,
    "2024_envelope70_76A": 5838281, "2024_omzet": 791927, "2024_73": 4801399, "2024_74": 244955, "2024_76A": 0,
    "2024_pnl": 568352, "2024_bedrijfswinst": 469641,
    "2024_equity": 6180840, "2024_assets": 8059785, "2024_debt": 1878945,
    "2024_cash": 854185, "2024_personnel62": 4362725, "2024_630": 310266, "2024_fte": 62.3,
    "2024_kapitaalsubsidies": 184986, "2024_geldbeleggingen": 3710000,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Monsheide Peer YE2025 (70/76A JUMP 6.36m / 73 JUMP 5.28m / cash JUMP 368k / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_peer leftover dual",
    "legal_basis": "Monsheide VZW (KBO 0419.081.867; Actief; 1 VE; official zetel Peer; RSZ2025 87.202; VAPH Vergunde Zorgaanbieder + RTH)",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "6359534",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00180864.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_peer",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind 70/76A JUMP 6359534 and 73 JUMP 5281699 and why cash JUMP 1222197 (+368k) while FTE JUMP 66.8",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Peer>Monsheide>JR2025_statutory_L5",
    "notes": "tick2556; Strong official native PDF; leftover mined city_peer leftover VAPH unused leftover type after city GE tick1099; 1 VE; prior-year identical; FIRST LOCK leftover city_peer leftover VAPH Monsheide; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Monsheide Peer 70/76A JUMP 6.36m / 73 JUMP 5.28m / cash JUMP 368k (YE2025 leftover city_peer leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Peer>Monsheide>JR2025",
    "annual_cost_eur": "6359534",
    "total_cost_eur": "6359534",
    "tco_notes": "PDF envelope 70/76A 6359534 JUMP; 73 5281699 JUMP (733 subsidies 5273599); omzet70 JUMP 810370; 76A empty; bedrijfswinst JUMP 518731; pnl JUMP 603637; equity JUMP 6747285; assets JUMP 8536334; debt DROP 1789049; cash JUMP 1222197; geldbeleggingen JUMP 4131000; kapitaalsubsidies DROP 147793; personnel62 JUMP 4786225; leftover city_peer leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_peer leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_peer",
    "measured_outcome": "6.36m 70/76A JUMP; 5.28m 73 JUMP; 368k cash JUMP; 66.8 FTE JUMP; leftover city_peer leftover VAPH",
    "absurdity_score": "5.45",
    "cost_score": "5.75",
    "difficulty": "4.50",
    "priority_index": "5.65",
    "cut_proposal": "FOI VAPH/gemeentelijke matrix behind 70/76A 6359534 and 73 5281699 and why cash JUMP 1222197 while FTE JUMP 66.8",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2556 leftover mined city_peer leftover VAPH Monsheide after city GE tick1099; hunt skips VAPH 0-deposit Klavertje7/Toontjeshuis/Think/Mispelhoef/Witte Hoeve/Blend no NBB YE2025 deps; Vlotter Maatwerk VZW YE2024-only; Nethedal YE2024-only; Veerkracht 0 deposits Steger 0 deposits; Rozemarijn remine parent city_keerbergen@2295; Forena Menen remine@2194 under sec_flanders; leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_boom leftover maatwerk/thuiszorg dual VLOTTER remine@2555 leftover city_zoersel leftover VAPH Kadodder remine@2554; 1 VE; prior-year identical; next rq_2557 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_peer leftover VAPH Monsheide",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Peer>Monsheide>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VOL-VZW YE2025 70/76A JUMP 6359534, 73 JUMP 5281699 (733 5273599), cash JUMP 1222197 (+368k), FTE JUMP 66.8 with 62 JUMP 4786225",
    "why_it_matters": "Public leftover VAPH dual of mined city_peer shows 6.36m envelope and 5.28m subsidies while subsidy matrix and cash JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "Monsheide VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "onthaal@monsheide.be",
    "recipient_postal": "Monsheide 4, 3990 Peer",
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
    "notes": "tick2556; ready NOT sent; Strong PDF + Strong KBO; leftover city_peer leftover VAPH Monsheide",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

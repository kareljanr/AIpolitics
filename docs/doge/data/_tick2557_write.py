from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2557_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_arum_dilsen_jr2025_nbb_pdf_2557"
SRC_KBO = "src_arum_dilsen_kbo_2557"
SRC_SBM = "src_arum_dilsen_sbm_2557"
SRC_SITE = "src_arum_dilsen_site_2557"
EID = "vzw_arum_dilsen"
GAP = "gap_arum_dilsen_vaph_matrix_70_76a_jump_22_31m_73_jump_18_89m_cash_drop_4_02m_l5"
COMM = "comm_arum_dilsen_jr2025_statutory_70_76a_jump_22_31m_73_jump_18_89m_cash_drop_4_02m"
LB = "lb_arum_dilsen_70_76a_jump_22_31m_73_jump_18_89m_cash_drop_4_02m_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2557/2026-00132875.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0410.169.547" in blob or "0410169547" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Zorggroep Arum deposit 2026-00132875",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00132875.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2557; official native statutory PDF 604523 bytes 49p VOL-VZW 26.0.11 m05-f; header 01/06/2026; AV 26.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-03 00:11:56 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00132875 604523 MD5 57838c227aa0eccf8c9de4915145c16b; VOL-VZW 6.1 6.2 6.3 6.4 6.5 6.9 6.11 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Zorggroep Arum 0410.169.547",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410169547",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2557; Actief Normale toestand; VZW; official zetel Stokkemerbaan 147 3650 Dilsen-Stokkem; also known as (MANÉ); 7 VE: 2.151.390.021 DE MEANDER Stokkemerbaan 147 + 2.241.614.867 Kadoos + 2.292.641.916 Campus Ommersteyn + 2.305.482.439 de Ronduyt + 2.305.482.637 de Korver + 2.305.486.102 Fabor (all 3650 Dilsen-Stokkem) + 2.311.404.783 Mané Schoolstraat(O) 32 3630 Maasmechelen; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een handicap; Werkgever RSZ; FOI info@arum.be; NOT leftover city GE Dilsen-Stokkem 0207.471.716; NOT leftover OCMW 0212.247.381; NOT leftover SBM Maasmechelen 0461.814.525 remine@2538",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / Northdata fiche Zorggroep Arum 0410169547 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0410169547",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2557; deposit-id 2026-00132875 YE 01.01.2025-31.12.2025 filing VOL-VZW header 01.06.2026 AV 26.05.2026; prior deposit 2025-00170208; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub unused; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope not Northdata",
    },
    {
        "source_id": SRC_SITE,
        "title": "Zorggroep Arum official site / VAPH adreslijst",
        "url": "https://www.arum.be/",
        "publisher": "Zorggroep Arum / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2557; FOI info@arum.be from official VAPH adreslijst https://www.vaph.be/organisaties/adressen/zorggroep-arum Vergunde Zorgaanbieder + RTH + MFC; leftover mined city_dilsen_stokkem leftover VAPH after city GE tick1098; FIRST LOCK leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum; NOT leftover-via-VE of a DIFFERENT leftover city as parent (Mané is own VE of this parent); NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover SBM Maasmechelen remine@2538",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Zorggroep Arum VZW (Dilsen-Stokkem / VAPH Vergunde Zorgaanbieder + RTH + MFC; ex De Meander + Mané)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_dilsen_stokkem",
    "community_language": "nl",
    "website": "https://www.arum.be/",
    "foi_email": "info@arum.be",
    "foi_postal": "Stokkemerbaan 147, 3650 Dilsen-Stokkem",
    "notes": "tick2557 YE2025 Strong official native NBB PDF deposit 2026-00132875 + Strong KBO 0410.169.547 Actief 7 VE; leftover mined city_dilsen_stokkem leftover VAPH unused leftover type after city GE tick1098; official zetel Stokkemerbaan 147 3650 Dilsen-Stokkem; RSZ2025 87.202; envelope 70/76A JUMP 22307281; 73 JUMP 18892480; cash DROP 2044429 (−4.02m); FTE 222.5 flat; NOT leftover city GE 0207.471.716; NOT leftover OCMW 0212.247.381; NOT leftover SBM Maasmechelen 0461.814.525; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum",
}], ent_fields)
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_arum_dilsen_envelope70_76a_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "22307281", "amount_min_eur": "22307281", "amount_max_eur": "22307281", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +1.46%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 21986413 identical; 76A 1349 DROP from 474578; subsidies sit in 73/733"},
    {"budget_id": "bud_arum_dilsen_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2974056", "amount_min_eur": "2974056", "amount_max_eur": "2974056", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +3.80%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 2865280 identical; commercial-only vs large 73"},
    {"budget_id": "bud_arum_dilsen_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "18892480", "amount_min_eur": "18892480", "amount_max_eur": "18892480", "basis": "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +3.68%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 18222277 identical; subsidies 733 18876759 JUMP; schenkingen/legaten 731 15721 DROP"},
    {"budget_id": "bud_arum_dilsen_74_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "439396", "amount_min_eur": "439396", "amount_max_eur": "439396", "basis": "NBB VOL-VZW code 74 andere bedrijfsopbrengsten YE2025 JUMP +3.56%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 424278 identical; 76A 1349 DROP"},
    {"budget_id": "bud_arum_dilsen_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "18142521", "amount_min_eur": "18142521", "amount_max_eur": "18142521", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +3.29%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 17564732 identical; FTE 9087 222.5 DROP −0.13% from 222.8"},
    {"budget_id": "bud_arum_dilsen_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "890287", "amount_min_eur": "890287", "amount_max_eur": "890287", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 DROP −6.90%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 956311 identical; capex ~670742; MVA 22/27 10778447 DROP"},
    {"budget_id": "bud_arum_dilsen_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1020040", "amount_min_eur": "1020040", "amount_max_eur": "1020040", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP −32.07%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 1501696 identical; 640/8 72292 JUMP; 66A 33640"},
    {"budget_id": "bud_arum_dilsen_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "990177", "amount_min_eur": "990177", "amount_max_eur": "990177", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP −37.16%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 1575612 identical; 9903 990177"},
    {"budget_id": "bud_arum_dilsen_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "15728465", "amount_min_eur": "15728465", "amount_max_eur": "15728465", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +5.51%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 14907166 identical; kapitaalsubsidies 15 4592282 DROP; destin 691 6100000"},
    {"budget_id": "bud_arum_dilsen_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "23224469", "amount_min_eur": "23224469", "amount_max_eur": "23224469", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +6.36%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 21835024 identical; MVA 22/27 10778447 DROP; gebouwen 22 9050451 DROP; cash 2044429 DROP; geldbeleggingen 7901334 JUMP; capex ~670742"},
    {"budget_id": "bud_arum_dilsen_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2044429", "amount_min_eur": "2044429", "amount_max_eur": "2044429", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP −66.29%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2557; PDF p native; YE2024 6064050 identical; debt 17/49 7381689 JUMP; geldbeleggingen 50/53 7901334 JUMP (+5.54m)"},
], bud_fields)
print("budgets ok")

cash = {
    "2025_envelope70_76A": 22307281, "2025_omzet": 2974056, "2025_73": 18892480, "2025_733": 18876759, "2025_731": 15721, "2025_74": 439396, "2025_76A": 1349,
    "2025_pnl": 990177, "2025_bedrijfswinst": 1020040, "2025_9903": 990177,
    "2025_equity": 15728465, "2025_assets": 23224469, "2025_debt": 7381689,
    "2025_cash": 2044429, "2025_kapitaalsubsidies": 4592282, "2025_geldbeleggingen": 7901334,
    "2025_personnel62": 18142521, "2025_630": 890287, "2025_6408": 72292,
    "2025_mva": 10778447, "2025_capex": 670742, "2025_fte": 222.5, "2025_gebouwen": 9050451,
    "2025_aanbouw": 193879, "2025_destin691": 6100000, "2025_destin791": 0,
    "2024_envelope70_76A": 21986413, "2024_omzet": 2865280, "2024_73": 18222277, "2024_733": 18178733, "2024_731": 43544, "2024_74": 424278, "2024_76A": 474578,
    "2024_pnl": 1575612, "2024_bedrijfswinst": 1501696,
    "2024_equity": 14907166, "2024_assets": 21835024, "2024_debt": 6729299,
    "2024_cash": 6064050, "2024_personnel62": 17564732, "2024_630": 956311, "2024_fte": 222.8,
    "2024_kapitaalsubsidies": 4761160, "2024_geldbeleggingen": 2357476,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Zorggroep Arum Dilsen-Stokkem YE2025 (70/76A JUMP 22.31m / 73 JUMP 18.89m / cash DROP 4.02m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_dilsen_stokkem leftover dual",
    "legal_basis": "Zorggroep Arum VZW (KBO 0410.169.547; Actief; 7 VE; official zetel Dilsen-Stokkem; RSZ2025 87.202; VAPH Vergunde Zorgaanbieder + RTH + MFC)",
    "decision_date": "2026-05-26",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "22307281",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00132875.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_dilsen_stokkem",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind 70/76A JUMP 22307281 and 73 JUMP 18892480 and why cash DROP 2044429 (−4.02m) while geldbeleggingen JUMP 7901334",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Dilsen-Stokkem>Zorggroep_Arum>JR2025_statutory_L5",
    "notes": "tick2557; Strong official native PDF; leftover mined city_dilsen_stokkem leftover VAPH unused leftover type after city GE tick1098; 7 VE; prior-year identical; FIRST LOCK leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}], comm_fields)
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Zorggroep Arum Dilsen-Stokkem 70/76A JUMP 22.31m / 73 JUMP 18.89m / cash DROP 4.02m (YE2025 leftover city_dilsen_stokkem leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Limburg>Dilsen-Stokkem>Zorggroep_Arum>JR2025",
    "annual_cost_eur": "22307281",
    "total_cost_eur": "22307281",
    "tco_notes": "PDF envelope 70/76A 22307281 JUMP; 73 18892480 JUMP (733 subsidies 18876759); omzet70 JUMP 2974056; 76A DROP 1349; bedrijfswinst DROP 1020040; pnl DROP 990177; equity JUMP 15728465; assets JUMP 23224469; debt JUMP 7381689; cash DROP 2044429; geldbeleggingen JUMP 7901334; kapitaalsubsidies DROP 4592282; personnel62 JUMP 18142521; leftover city_dilsen_stokkem leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_dilsen_stokkem leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_dilsen_stokkem",
    "measured_outcome": "22.31m 70/76A JUMP; 18.89m 73 JUMP; 4.02m cash DROP; 222.5 FTE flat; leftover city_dilsen_stokkem leftover VAPH",
    "absurdity_score": "5.95",
    "cost_score": "6.40",
    "difficulty": "4.55",
    "priority_index": "5.98",
    "cut_proposal": "FOI VAPH/gemeentelijke matrix behind 70/76A 22307281 and 73 18892480 and why cash DROP 2044429 (−4.02m) while geldbeleggingen JUMP 7901334 and FTE flat 222.5",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2557 leftover mined city_dilsen_stokkem leftover VAPH Zorggroep Arum after city GE tick1098; hunt skips AGB-only VAPH stall izegem/aarschot Apojo remine/bocholt empty/kinrooi Dino groenezorg/haacht empty/maldegem empty/zwevegem Ubuntu Kortrijk zetel leftover-via-VE/temse Paard groenezorg/aalter Aalternatief 0 deposits+LiVia zorgboerderij/herk_de_stad Beerbos groenezorg/oud_turnhout Liereman groenezorg/herselt Ollemanshoekje groenezorg+PlusCo ouderinitiatief 0 deps/berlaar CasaDiColore 0 deposits; leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_peer leftover VAPH Monsheide remine@2556; 7 VE; prior-year identical; next rq_2558 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum",
}], lb_fields)
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Limburg>Dilsen-Stokkem>Zorggroep_Arum>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VOL-VZW YE2025 70/76A JUMP 22307281, 73 JUMP 18892480 (733 18876759), cash DROP 2044429 (−4.02m) with geldbeleggingen JUMP 7901334, FTE flat 222.5 with 62 JUMP 18142521",
    "why_it_matters": "Public leftover VAPH dual of mined city_dilsen_stokkem shows 22.31m envelope and 18.89m subsidies while subsidy matrix and cash DROP 4.02m / geldbeleggingen JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "Zorggroep Arum VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@arum.be",
    "recipient_postal": "Stokkemerbaan 147, 3650 Dilsen-Stokkem",
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
    "notes": "tick2557; ready NOT sent; Strong PDF + Strong KBO; leftover city_dilsen_stokkem leftover VAPH Zorggroep Arum",
}], foi_fields)
print("foi ok")
print("CORE WRITE DONE")

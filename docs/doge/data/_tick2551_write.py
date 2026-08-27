from pathlib import Path
import csv, json

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2551_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_ter_loke_vosselaar_jr2025_nbb_pdf_2551"
SRC_KBO = "src_ter_loke_vosselaar_kbo_2551"
SRC_SBM = "src_ter_loke_vosselaar_sbm_2551"
SRC_SITE = "src_ter_loke_vosselaar_site_2551"
EID = "vzw_ter_loke_vosselaar"
GAP = "gap_ter_loke_vosselaar_vaph_matrix_70_76a_jump_15_36m_73_jump_14_54m_9901_drop_443k_cash_drop_1_04m_l5"
COMM = "comm_ter_loke_vosselaar_jr2025_statutory_70_76a_jump_15_36m_73_jump_14_54m_9901_drop_443k_cash_drop_1_04m"
LB = "lb_ter_loke_vosselaar_70_76a_jump_15_36m_73_jump_14_54m_9901_drop_443k_cash_drop_1_04m_jr2025"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()
assert (ROOT / "docs/doge/raw/tick2551/2026-00133725_ter_loke.pdf").is_file()

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
        if _row.get("entity_id") == EID or "0407.933.104" in blob or "0407933104" in blob.replace(".", ""):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Ter Loke deposit 2026-00133725",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00133725.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2551; official native statutory PDF 651580 bytes 43p VOL-VZW 26.0.11 m05-f; header 01/06/2026; AV 21.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-03 02:43:14 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00133725 651580 MD5 474d67ed474b2717246dacc8e765102c; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Ter Loke 0407.933.104",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407933104",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2551; Actief Normale toestand since 16.04.1955; VZW; official zetel Heilanders 11 2350 Vosselaar since 01.07.2011; 14 VE incl 2.138.251.964 Ter Loke - de Centrale Heilanders 11 bus 1 2350 Vosselaar + 2.138.252.063 OPB De Berken Heilanders 11 Vosselaar + 2.309.726.089 OPB De Loot Schoolstraat 1 Vosselaar + 2.327.568.151 OPB De Pluk Vosselaar + Turnhout/Kasterlee/Malle VEs (BJB Het Klavier DNV/VL are own VEs of this parent NOT Emmaus Mechelen Klavier leftover-via-VE); RSZ2025 87.991 Integrale jeugdhulp met huisvesting; NOT leftover AGB 0664.728.726",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Ter Loke 0407933104 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0407933104",
        "publisher": "NBB Central Balance Sheet Office Consult",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2551; deposit-id 2026-00133725 YE 01.01.2025-31.12.2025 filing VOL-VZW header 01.06.2026 AV 21.05.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused; NBB published-deposits API 403 this tick (deposit-id from official consult listing via search index); Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Ter Loke site + official VAPH adreslijst",
        "url": "https://www.vaph.be/organisaties/adressen/ter-loke",
        "publisher": "Ter Loke VZW / VAPH",
        "accessed_date": DAY,
        "source_class": "org",
        "notes": "tick2551; FOI info-oph@terloke.be from official VAPH adreslijst Ter Loke (RTH) + site https://www.terloke.be; leftover mined city_vosselaar leftover VAPH leftover-mined AGB-only unused leftover type after Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546; FIRST LOCK leftover city_vosselaar leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover Klavier Emmaus Mechelen",
    },
])
print("sources ok")

ent_fields = ["entity_id","name_nl","name_fr","name_en","level","parent_id","community_language","website","foi_email","foi_postal","notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Ter Loke VZW (Vosselaar / VAPH RTH + OPH/BJB/CIG jeugdhulp)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_vosselaar",
    "community_language": "nl",
    "website": "https://www.terloke.be",
    "foi_email": "info-oph@terloke.be",
    "foi_postal": "Heilanders 11, 2350 Vosselaar",
    "notes": "tick2551 YE2025 Strong official native NBB PDF deposit 2026-00133725 + Strong KBO 0407.933.104 Actief 14 VE; leftover mined city_vosselaar leftover VAPH leftover-mined AGB-only unused leftover type; official zetel Heilanders 11 2350 Vosselaar since 01.07.2011; RSZ2025 87.991; envelope 70/76A JUMP 15356058; 73 JUMP 14544228; 9901 DROP 584530; 9904 DROP 630343; cash DROP 1109665; FTE 174.2 JUMP; NOT leftover AGB 0664.728.726; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/OCMW; FIRST LOCK leftover city_vosselaar leftover VAPH",
}])
print("entities ok")

bud_fields = ["budget_id","entity_id","year","amount_eur","amount_min_eur","amount_max_eur","basis","source_id","confidence","notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_ter_loke_vosselaar_envelope_70_76a_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "15356058", "amount_min_eur": "15356058", "amount_max_eur": "15356058", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +1.59%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p7 native; YE2024 15115295 identical; omzet70 459684 JUMP commercial-only vs large 73; 76A 2903 DROP"},
    {"budget_id": "bud_ter_loke_vosselaar_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "459684", "amount_min_eur": "459684", "amount_max_eur": "459684", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +2.68%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p7 native; YE2024 447689 identical; commercial-only vs large 73"},
    {"budget_id": "bud_ter_loke_vosselaar_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "14544228", "amount_min_eur": "14544228", "amount_max_eur": "14544228", "basis": "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +3.86%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p7 native; YE2024 14003780 identical; 733 14532035; 73-733 gap 12193 FOI"},
    {"budget_id": "bud_ter_loke_vosselaar_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12771398", "amount_min_eur": "12771398", "amount_max_eur": "12771398", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +5.02%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p7 native; YE2024 12161270 identical; FTE 9087 174.2 JUMP from 171.9"},
    {"budget_id": "bud_ter_loke_vosselaar_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "572266", "amount_min_eur": "572266", "amount_max_eur": "572266", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 JUMP +0.09%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p7 native; YE2024 571759 identical; capex 1064678 (8161+8162+8163+8166); MVA 14340895 JUMP"},
    {"budget_id": "bud_ter_loke_vosselaar_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "584530", "amount_min_eur": "584530", "amount_max_eur": "584530", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -43.11%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p7 native; YE2024 1027468 identical; 66A 944 DROP; 640/8 43869 DROP"},
    {"budget_id": "bud_ter_loke_vosselaar_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "630343", "amount_min_eur": "630343", "amount_max_eur": "630343", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -41.33%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p8 native; YE2024 1074391 identical; 9903 630343 DROP"},
    {"budget_id": "bud_ter_loke_vosselaar_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "16735557", "amount_min_eur": "16735557", "amount_max_eur": "16735557", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +2.29%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p6 native; YE2024 16361217 identical; kapitaalsubsidies 15 6379052 DROP"},
    {"budget_id": "bud_ter_loke_vosselaar_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "20148744", "amount_min_eur": "20148744", "amount_max_eur": "20148744", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +2.02%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p5 native; YE2024 19749874 identical; MVA 22/27 14340895 JUMP; gebouwen 22 13562813 JUMP; cash 1109665 DROP; capex 1064678"},
    {"budget_id": "bud_ter_loke_vosselaar_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3293219", "amount_min_eur": "3293219", "amount_max_eur": "3293219", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 JUMP +0.91%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p6 native; YE2024 3263657 identical"},
    {"budget_id": "bud_ter_loke_vosselaar_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1109665", "amount_min_eur": "1109665", "amount_max_eur": "1109665", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -48.33%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2551; PDF p5 native; YE2024 2147713 identical; geldbeleggingen 50/53 2200000 JUMP"},
])
print("budgets ok")

cash = {
    "2025_envelope_70_76A": 15356058, "2025_omzet": 459684, "2025_73": 14544228, "2025_76A": 2903,
    "2025_733": 14532035, "2025_74": 349242,
    "2025_pnl": 630343, "2025_bedrijfswinst": 584530, "2025_9903": 630343,
    "2025_equity": 16735557, "2025_assets": 20148744, "2025_debt": 3293219,
    "2025_cash": 1109665, "2025_kapitaalsubsidies": 6379052, "2025_geldbeleggingen": 2200000,
    "2025_personnel62": 12771398, "2025_630": 572266, "2025_6408": 43869, "2025_66A": 944,
    "2025_mva": 14340895, "2025_capex": 1064678, "2025_fte": 174.2, "2025_gebouwen": 13562813,
    "2025_aanbouw": 118301, "2025_destin691": 630343, "2025_destin791": 40315,
    "2024_envelope_70_76A": 15115295, "2024_omzet": 447689, "2024_73": 14003780, "2024_76A": 514068,
    "2024_pnl": 1074391, "2024_bedrijfswinst": 1027468,
    "2024_equity": 16361217, "2024_assets": 19749874, "2024_debt": 3263657,
    "2024_cash": 2147713, "2024_personnel62": 12161270, "2024_630": 571759, "2024_fte": 171.9,
    "2024_kapitaalsubsidies": 6635055, "2024_geldbeleggingen": 1450000,
}
cash_json = json.dumps(cash, separators=(",", ":"))

comm_fields = ["commitment_id","title","entity_id","beneficiary","legal_basis","decision_date","start_year","end_year","total_envelope_eur","cash_by_year","remaining_eur","status","evaluation_url","stated_goal","cut_option","source_id","confidence","hierarchy_path","notes"]
append_rows(DATA / "commitments.csv", [{
    "commitment_id": COMM,
    "title": "Ter Loke Vosselaar YE2025 (70/76A JUMP 15.36m / 73 JUMP 14.54m / 9901 DROP 443k / cash DROP 1.04m / Strong PDF)",
    "entity_id": EID,
    "beneficiary": "VAPH + leftover city_vosselaar leftover VAPH",
    "legal_basis": "VZW Ter Loke (KBO 0407.933.104; Actief; 14 VE; official zetel Vosselaar; RSZ2025 87.991; official VAPH adreslijst)",
    "decision_date": "2026-05-21",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "15356058",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00133725.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_vosselaar",
    "cut_option": "Publish VAPH / Opgroeien / gemeente Vosselaar / Turnhout / Kasterlee / Malle matrix behind 70/76A JUMP 15356058 and 73 JUMP 14544228 and why 9901 DROP 584530 while cash DROP 1109665 and geldbeleggingen JUMP 2200000 and FTE JUMP 174.2",
    "source_id": SRC_PDF,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Vosselaar>Ter_Loke>JR2025_statutory_L5",
    "notes": "tick2551; Strong official native PDF; leftover mined city_vosselaar leftover VAPH leftover-mined AGB-only unused leftover type; 14 VE; prior-year identical; FIRST LOCK leftover city_vosselaar leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}])
print("commitments ok")

lb_fields = ["item_id","name","level","type","hierarchy_path","annual_cost_eur","total_cost_eur","tco_notes","confidence","source_id","beneficiaries","stated_goal","measured_outcome","absurdity_score","cost_score","difficulty","priority_index","cut_proposal","status","struck_reason","notes"]
append_rows(DATA / "leaderboard.csv", [{
    "item_id": LB,
    "name": "Ter Loke Vosselaar 70/76A JUMP 15.36m / 73 JUMP 14.54m / 9901 DROP 443k / cash DROP 1.04m (YE2025 leftover city_vosselaar leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Antwerpen>Vosselaar>Ter_Loke>JR2025",
    "annual_cost_eur": "15356058",
    "total_cost_eur": "15356058",
    "tco_notes": "PDF envelope 70/76A 15356058 JUMP; 73 JUMP 14544228; omzet70 JUMP 459684 commercial-only; 76A DROP 2903; bedrijfswinst DROP 584530; pnl DROP 630343; equity JUMP 16735557; assets JUMP 20148744; debt JUMP 3293219; cash DROP 1109665; geldbeleggingen JUMP 2200000; kapitaalsubsidies DROP 6379052; personnel62 JUMP 12771398; leftover city_vosselaar leftover VAPH",
    "confidence": "strong",
    "source_id": SRC_PDF,
    "beneficiaries": "VAPH + leftover city_vosselaar leftover VAPH",
    "stated_goal": "leftover VAPH leftover city_vosselaar",
    "measured_outcome": "15.36m 70/76A JUMP; 14.54m 73 JUMP; 443k 9901 DROP; 1.04m cash DROP; leftover city_vosselaar leftover VAPH",
    "absurdity_score": "6.10",
    "cost_score": "5.55",
    "difficulty": "4.50",
    "priority_index": "5.72",
    "cut_proposal": "FOI VAPH / Opgroeien / gemeente Vosselaar / Turnhout / Kasterlee / Malle matrix behind 70/76A 15356058 and 73 14544228 and why 9901 DROP 584530 while cash DROP 1109665 and geldbeleggingen JUMP 2200000 and FTE JUMP 174.2",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2551 leftover mined city_vosselaar leftover VAPH leftover-mined AGB-only unused leftover type after Wagenschot remine@2550 Nederheem remine@2549 OTL remine@2548 Inspirant remine@2547 Wiric remine@2546 De Kompanie remine@2545 Ritmica remine@2544 Iona remine@2543 Bindkracht remine@2542 De Plek remine@2541 Martine Van Camp remine@2540 Veerkracht 0 deposits Steger 0 deposits Pelikaan OCMW Ampel Prisma remine Terloo Broeders Gent leftover-via-VE Ter Heyder 0 deposits GielsBos remine@2334 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover city_nazareth_depinte leftover VAPH Wagenschot remine@2550; 14 VE; prior-year identical; next rq_2552 leftover dual (NOT every-10; next every-10 2560); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_vosselaar leftover VAPH",
}])
print("leaderboard ok")

foi_fields = ["gap_id","hierarchy_path","entity_id","what_is_missing","why_it_matters","priority","recipient_body","recipient_email","recipient_postal","draft_letter_path","status","date_ready","date_sent","date_due","date_answered","response_summary","linked_commitment_id","linked_leaderboard_id","created_utc","updated_utc","notes"]
append_rows(DATA / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Antwerpen>Vosselaar>Ter_Loke>leftover_vaph",
    "entity_id": EID,
    "what_is_missing": "VAPH / Opgroeien / gemeente Vosselaar / Turnhout / Kasterlee / Malle matrix behind VOL-VZW YE2025 70/76A JUMP 15356058, 73 JUMP 14544228, 9901 DROP 584530, cash DROP 1109665, geldbeleggingen JUMP 2200000, FTE JUMP 174.2 with 62 JUMP 12771398",
    "why_it_matters": "Public leftover VAPH dual of mined city_vosselaar shows 15.36m bedrijfsopbrengsten and 14.54m subsidies while VAPH/Opgroeien/gemeente matrix and 9901 DROP 43 percent with cash DROP 48 percent stay unsourced",
    "priority": "7",
    "recipient_body": "VZW Ter Loke / Voorzitter Raad van Bestuur",
    "recipient_email": "info-oph@terloke.be",
    "recipient_postal": "Heilanders 11, 2350 Vosselaar",
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
    "notes": "tick2551; ready NOT sent; Strong PDF + Strong KBO; leftover city_vosselaar leftover VAPH",
}])
print("foi ok")
print("CORE WRITE DONE")

from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2513_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_de_hoop_zottegem_jr2025_nbb_pdf_2513"
SRC_KBO = "src_de_hoop_zottegem_kbo_2513"
SRC_SBM = "src_de_hoop_zottegem_sbm_2513"
SRC_SITE = "src_de_hoop_zottegem_site_2513"
EID = "vzw_de_hoop_zottegem"
GAP = "gap_de_hoop_zottegem_vaph_matrix_bruto_145k_73_drop_21k_pnl_jump_80k_fte_drop_0_l5"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_rows(path, rows, fieldnames):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} no LF")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", lineterminator="\n")
        for row in rows:
            w.writerow(row)
    print("appended", len(rows), "->", path.name)

import csv as _csv
_csv.field_size_limit(10_000_000)
with (DATA / "entities.csv").open(encoding="utf-8") as _fh:
    for _row in _csv.DictReader(_fh):
        if _row.get("entity_id") == EID:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 De Hoop Zottegem deposit 2026-00269926",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00269926.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2513; official native statutory PDF 433152 bytes 14p VKT-VZW 25.0.13 m04-f; header 06/07/2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-09 02:34:10 UTC OpenPDF 1.3.26; CDN Last-Modified 28.07.2026; statutory pages native; CDN 2026-00269926 GET 200 433152 MD5 dda49fc523f22ac7f2d727811f0ea499; prior-year identical not restated; no commissaris on VKT-VZW 2; VKT-VZW 6.1.3 6.2 6.5 6.6 6.7 7 8 niet dienstig; NBB published-deposits/ids 403 this tick; NBB broker 403 discarded; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO De Hoop 0870.779.490",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0870779490",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2513; Actief since 27.12.2004; 0 VE leftover city_zottegem (official zetel Zuster Angelalaan 1 9620 Zottegem since 22.06.2015); VZW since 17.12.2004; BTW since 01.12.2017; BTW2025 87.202 + 88.106 + 88.104 + 87.304; jaarvergadering mei; boekjaar 31 december; leftover mined city_zottegem leftover VAPH; official KBO Actief toestand 26.08.2026 vs Companyweb Status Stopgezet discarded; NOT De Bron 0892.673.479 leftover WZC@2512; NOT WZC Egmont OCMW 0212.187.302; NOT De Bolster 0861.680.989 leftover-via-VE Zwalm; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Hoop 0870779490 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0870779490",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2513; deposit-id 2026-00269926 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 09.07.2026; SBM fiche + Companyweb last-balansjaar 2025 + neerlegging 09.07.2026 used for deposit-id discovery; Companyweb last-balansjaar 2025 discovery OK euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Hoop FOI contact leftover city_zottegem leftover VAPH",
        "url": "https://dehoopzottegem.be/",
        "publisher": "De Hoop VZW leftover city_zottegem leftover VAPH 0 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2513; FOI yvan.lenssens@sezz.be from official NBB PDF header / secretariaat.dehoop@vzwdebolster.be from official site; leftover mined city_zottegem leftover VAPH after leftover city_zottegem leftover WZC De Bron@2512; site dagcentrum / begeleid werken / wooncoaching + maakt deel uit van vzw De Bolster 0861.680.989 zetel Zwalm leftover-via-VE SKIP; NOT De Bron leftover WZC; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "De Hoop, voorziening voor personen met een beperking",
    "name_fr": "De Hoop ASBL",
    "name_en": "De Hoop VZW (leftover city_zottegem leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_zottegem",
    "community_language": "nl",
    "website": "https://dehoopzottegem.be/",
    "foi_email": "yvan.lenssens@sezz.be",
    "foi_postal": "Zuster Angelalaan 1 9620 Zottegem",
    "notes": "tick2513 YE2025 Strong official native NBB PDF deposit 2026-00269926 + Strong KBO 0870.779.490 Actief 0 VE; omzet70 empty (VKT was 69057); 73 DROP 20846; 76A DROP 3269; envelope bruto9900 DROP 145460; pnl JUMP 80173; 9901 FLIP 45595; equity JUMP 328381; assets DROP 1840258; debt DROP 1511877; FTE DROP 0; kapitaalsubsidies DROP 291843; destin691 empty; cash DROP 542495; geldbeleggingen empty DROP; leftover city_zottegem leftover VAPH 0 VE official zetel Zottegem; prior-year identical; NOT De Bron leftover WZC@2512; NOT WZC Egmont OCMW; NOT De Bolster leftover-via-VE Zwalm; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_de_hoop_zottegem_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT; was 69057)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p6 native; YE2024 69057; envelope bruto9900 145460 DROP because VKT and omzet empty; FOI VAPH/Zottegem/De Bolster matrix behind empty 70"},
    {"budget_id": "bud_de_hoop_zottegem_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "20846", "amount_min_eur": "20846", "amount_max_eur": "20846", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -97.42%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p6 native; YE2024 806649; FOI VAPH matrix behind DROP 20846 and transfer to De Bolster"},
    {"budget_id": "bud_de_hoop_zottegem_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "145460", "amount_min_eur": "145460", "amount_max_eur": "145460", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 DROP -82.58% (VKT envelope because omzet empty)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p6 native; YE2024 834819; 70 empty; 73 20846 DROP; 76A 3269 DROP"},
    {"budget_id": "bud_de_hoop_zottegem_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3269", "amount_min_eur": "3269", "amount_max_eur": "3269", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -53.74%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p6 native; YE2024 7067; 76B empty"},
    {"budget_id": "bud_de_hoop_zottegem_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "80173", "amount_min_eur": "80173", "amount_max_eur": "80173", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +2061.58%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p6 native; YE2024 3709; bedrijfswinst 9901 45595 FLIP PROFIT; destin691 empty"},
    {"budget_id": "bud_de_hoop_zottegem_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "45595", "amount_min_eur": "45595", "amount_max_eur": "45595", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP PROFIT (was -27)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p6 native; YE2024 -27; 62 empty; 630 84183 DROP; 66A 13714 JUMP; 640/8 1968 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_de_hoop_zottegem_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "328381", "amount_min_eur": "328381", "amount_max_eur": "328381", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +22.05%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p5 native; YE2024 269054; kapitaalsubsidies 15 291843 DROP; fondsen 10 empty; overgedragen 14 36538 FLIP"},
    {"budget_id": "bud_de_hoop_zottegem_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1840258", "amount_min_eur": "1840258", "amount_max_eur": "1840258", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -30.97%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p4 native; YE2024 2665951; MVA 22/27 1285478 DROP; cash 542495 DROP; geldbeleggingen empty DROP; aanbouw 27 empty; capex 9603"},
    {"budget_id": "bud_de_hoop_zottegem_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1511877", "amount_min_eur": "1511877", "amount_max_eur": "1511877", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 DROP -36.92%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p5 native; YE2024 2396897; 17 1210000 DROP; 42/48 empty; 178/9 1210000; voorzieningen 16 empty"},
    {"budget_id": "bud_de_hoop_zottegem_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "542495", "amount_min_eur": "542495", "amount_max_eur": "542495", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -15.98%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p4 native; YE2024 645659; geldbeleggingen 50/53 empty DROP (was 618166); combined liquidity 542495 DROP; capex 9603"},
    {"budget_id": "bud_de_hoop_zottegem_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2513; PDF p7 native; YE2024 691 empty; 791 empty; 9905 80173 overgedragen to 14"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")

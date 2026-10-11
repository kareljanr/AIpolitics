from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2510_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_diepen_boomgaard_grimbergen_jr2025_nbb_pdf_2510"
SRC_KBO = "src_diepen_boomgaard_grimbergen_kbo_2510"
SRC_SBM = "src_diepen_boomgaard_grimbergen_sbm_2510"
SRC_SITE = "src_diepen_boomgaard_grimbergen_site_2510"
EID = "vzw_diepen_boomgaard_grimbergen"
GAP = "gap_diepen_boomgaard_grimbergen_maatwerk_matrix_bruto_1_85m_omzet73_empty_pnl_deeper_loss_395k_cash_drop_81k_l5"
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

ent_raw = (DATA / "entities.csv").read_text(encoding="utf-8")
if "0421.285.252" in ent_raw or "0421285252" in ent_raw or EID in ent_raw:
    raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Den Diepen Boomgaard Grimbergen deposit 2026-00314106",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00314106.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2510; official native statutory PDF 57158 bytes 16p VKT-VZW 26.0.15 m04-f; header 10.07.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-21 21:15:48 UTC OpenPDF 1.3.26; CDN Last-Modified 03.08.2026; statutory pages native; CDN 2026-00314106 GET 200 57158 MD5 f444adff755f83f10cf5c76feae71522; NBB broker HTML unused this tick; VKT-VZW 6.2 6.5 6.6 8 niet dienstig; prior-year identical not restated; official PDF 9904 395094 / equity 699914 not jaarverslag rounding 395095 / 699913; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Den Diepen Boomgaard 0421.285.252",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421285252",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2510; Actief since 20.11.1980; 1 VE leftover city_grimbergen (official zetel Rijkenhoekstraat 80 1850 Grimbergen since 10.05.2000; VE 2.154.402.860 DEN DIEPEN BOOMGAARD Rijkenhoekstraat 80 since 12.06.2006); VZW since 20.11.1980; RSZ-werkgever; RSZ2025 88.993 Beschutte en sociale werkplaatsen; leftover mined city_grimbergen leftover maatwerk; NOT Havinet 0642.602.234 remine leftover city_grimbergen leftover VAPH; NOT WZC Heilig Hart Grimbergen 0409.724.238 remine; NOT Evara remine (groep-Evara partners note; official zetel + 1/1 VE Grimbergen not leftover-via-VE); NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Den Diepen Boomgaard 0421285252 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0421285252",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2510; deposit-id 2026-00314106 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 2026-07-21; NBB Consult + SBM CDN used for deposit-id discovery; Companyweb last-balansjaar 2025 discovery OK euros NOT OK; official PDF 9904 395094 not jaarverslag rounding; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Den Diepen Boomgaard FOI contact leftover city_grimbergen leftover maatwerk",
        "url": "https://www.diepenboomgaard.be/",
        "publisher": "Den Diepen Boomgaard VZW leftover city_grimbergen leftover maatwerk 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2510; FOI info@diepenboomgaard.be from official site (NBB PDF email empty; phone 02 270 00 35); leftover mined city_grimbergen leftover maatwerk after leftover VAPH Havinet remine@2301 + leftover WZC Heilig Hart remine@2074; NOT Havinet remine; NOT WZC Heilig Hart remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Den Diepen Boomgaard",
    "name_fr": "ASBL Den Diepen Boomgaard",
    "name_en": "Den Diepen Boomgaard VZW (leftover city_grimbergen leftover maatwerk)",
    "level": "parastatal",
    "parent_id": "city_grimbergen",
    "community_language": "nl",
    "website": "https://www.diepenboomgaard.be/",
    "foi_email": "info@diepenboomgaard.be",
    "foi_postal": "Rijkenhoekstraat 80 1850 Grimbergen",
    "notes": "tick2510 YE2025 Strong official native NBB PDF deposit 2026-00314106 + Strong KBO 0421.285.252 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A JUMP 3146; envelope bruto9900 JUMP 1847578; pnl DEEPER LOSS 395094; 9901 DEEPER LOSS 320017; equity DROP 699914; assets JUMP 4732148; debt JUMP 4032234; FTE JUMP 56; kapitaalsubsidies DROP 1441277; destin691 empty; cash DROP 121016; geldbeleggingen empty; leftover city_grimbergen leftover maatwerk 1 VE official zetel Grimbergen; prior-year identical; NOT Havinet 0642.602.234 remine leftover city_grimbergen leftover VAPH; NOT WZC Heilig Hart Grimbergen 0409.724.238 remine; NOT Evara remine (groep-Evara partners note; official zetel + 1/1 VE Grimbergen not leftover-via-VE); NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_diepen_boomgaard_grimbergen_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p6 native; YE2024 empty; 73 empty; envelope bruto9900 1847578 JUMP; FOI WEWIS/VDAB/gemeente matrix behind bruto 1847578"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p6 native; YE2024 empty; FOI WEWIS/VDAB matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1847578", "amount_min_eur": "1847578", "amount_max_eur": "1847578", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +2.84% (VKT because 73 empty and bruto ≫ omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p6 native; YE2024 1796569; omzet70 empty; 73 empty; 76A JUMP 3146"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3146", "amount_min_eur": "3146", "amount_max_eur": "3146", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +73.72%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p6/p12 native; YE2024 1811; 76B empty"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-395094", "amount_min_eur": "-395094", "amount_max_eur": "-395094", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DEEPER LOSS (was -198263)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p6 native; YE2024 -198263; bedrijfswinst 9901 -320017 DEEPER LOSS; destin691 empty; official 395094 not jaarverslag 395095"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-320017", "amount_min_eur": "-320017", "amount_max_eur": "-320017", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DEEPER LOSS (was -157487)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p6 native; YE2024 -157487; 62 1932629 JUMP; 630 219100 JUMP; 66A 14288 DROP; 640/8 1578 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "699914", "amount_min_eur": "699914", "amount_max_eur": "699914", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -39.42%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p5 native; YE2024 1155438; kapitaalsubsidies 15 1441277 DROP; overgedragen 14 -741363 DEEPER LOSS; fondsen 10 empty; bestemde 13 empty; official 699914 not jaarverslag 699913"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4732148", "amount_min_eur": "4732148", "amount_max_eur": "4732148", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +28.29%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p4 native; YE2024 3688714; MVA 22/27 3008633 JUMP; cash 121016 DROP; geldbeleggingen empty; aanbouw 27 1355153 JUMP; capex 8169 961669"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4032234", "amount_min_eur": "4032234", "amount_max_eur": "4032234", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +59.17%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p5 native; YE2024 2533276; 17 1589943 DROP; 42/48 1662471 JUMP; 439 1075000 JUMP from empty; voorzieningen 16 empty"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "121016", "amount_min_eur": "121016", "amount_max_eur": "121016", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -40.11%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p4 native; YE2024 202067; geldbeleggingen 50/53 empty; combined liquidity 121016; capex 8169 961669; overdrachten 8179 empty"},
    {"budget_id": "bud_diepen_boomgaard_grimbergen_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2510; PDF p7 native; YE2024 destin empty; 791 empty; overgedragen 14 -741363 DEEPER LOSS; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")

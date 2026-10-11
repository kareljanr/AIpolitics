from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2532_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_seniorplaza_willebroek_jr2025_nbb_pdf_2532"
SRC_KBO = "src_seniorplaza_willebroek_kbo_2532"
SRC_SBM = "src_seniorplaza_willebroek_sbm_2532"
SRC_SITE = "src_seniorplaza_willebroek_site_2532"
EID = "vzw_seniorplaza_willebroek"
GAP = "gap_seniorplaza_willebroek_wzc_matrix_70_jump_5_28m_73_jump_662k_pnl_drop_243k_cash_jump_569k_l5"
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

csv.field_size_limit(10_000_000)
with (DATA / "entities.csv").open(encoding="utf-8") as _fh:
    for _row in csv.DictReader(_fh):
        blob = " ".join(_row.values())
        if _row.get("entity_id") == EID or "0467.255.829" in blob or "0467255829" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Seniorplaza deposit 2026-00336704",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00336704.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2532; official native statutory PDF 303353 bytes 45p VOL-VZW 23.0.10 m05-f; header 23/07/2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-28 00:16:39 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00336704 303353 MD5 d735f1df5cdee0904e7b52ca21c67a0e; NBB UUID 3692056e-869e-11f1-b284-530b40574791; NBB consult HTML stub 5344 B discarded; NBB published-deposits list 20 this tick from prior-tick cache; NBB ids API 403 this tick; prior-year identical not restated; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.6 6.4.2 6.4.3 6.5.2 6.5.3 6.7 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Seniorplaza 0467.255.829",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0467255829",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2532; Actief since 21.05.1999; 2 VE leftover city_willebroek (official zetel Overwinningsstraat 133-135 2830 Willebroek since 21.05.1999; VE 2.144.144.319 seniorplaza Overwinningsstraat 139 since 13.04.2011 begindatum 21.12.2004 + VE 2.366.062.305 Gezinszorg Mechelen Overwinningsstraat 133-135 since 01.11.2024); VZW since 21.05.1999; naam Seniorplaza since 16.04.2010; RSZ-werkgever since 01.01.2000; RSZ2025 87.302 Serviceflats voor ouderen; official WZC list Willebroek Seniorplaza VZW 0467255829 / CoBRHA 172.101 / HCO 3346 / 78 woongelegenheden; leftover mined city_willebroek leftover WZC leftover-mined AGB-only unused leftover type; Korian Belgium NV 0869.769.702 gedelegeerd bestuurder since 18.01.2017 + SL Finance NV 0894.020.690 bestuurder (leftover public VZW WZC not commercial NV; FIRST LOCK leftover city_willebroek leftover WZC); NOT leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Seniorplaza 0467255829 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0467255829",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2532; deposit-id 2026-00336704 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial header 23.07.2026; NBB UUID 3692056e-869e-11f1-b284-530b40574791; NBB consult HTML stub 5344 B discarded; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list 20 this tick from prior-tick cache; NBB ids API 403 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "WZC Seniorplaza FOI contact leftover city_willebroek leftover WZC",
        "url": "https://www.korian.be/woonzorgcentra/seniorplaza/woonzorgcentrum-seniorplaza/",
        "publisher": "VZW Seniorplaza leftover city_willebroek leftover WZC 2 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2532; FOI info@seniorplaza.be from official site https://www.korian.be/woonzorgcentra/seniorplaza/woonzorgcentrum-seniorplaza/; leftover mined city_willebroek leftover WZC leftover-mined AGB-only unused leftover type after leftover city_boechout leftover WZC taken@2531 leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine@2282 leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 m140-f-p CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover city_deinze leftover WZC Sint-Jozef YE2025 unused leftover VAPH taken@2496/2499 leftover-via-VE Evergem Franciscanessen SKIP leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken; leftover city_willebroek leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ten Weldebrouc OCMW SKIP leftover WZC type now taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; Korian Belgium NV 0869.769.702 gedelegeerd bestuurder leftover public VZW WZC not commercial NV FIRST LOCK",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")

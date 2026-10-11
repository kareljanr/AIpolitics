from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2534_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_meerpaal_willebroek_jr2025_nbb_pdf_2534"
SRC_KBO = "src_meerpaal_willebroek_kbo_2534"
SRC_SBM = "src_meerpaal_willebroek_sbm_2534"
SRC_SITE = "src_meerpaal_willebroek_site_2534"
EID = "vzw_meerpaal_willebroek"
GAP = "gap_meerpaal_willebroek_vaph_matrix_bruto_3_50m_omzet73_empty_pnl_jump_228k_fte_jump_41_4_l5"
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
        if _row.get("entity_id") == EID or "0443.206.559" in blob or "0443206559" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 De Meerpaal deposit 2026-00152128",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00152128.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2534; official native statutory PDF 954005 bytes 25p VKT-VZW 23.0.9 m04-f; header 11/06/2026; AV 20.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-11 08:06:55 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00152128 954005 MD5 1dc1faf578f7d81d1733b04d0db7dc0c; NBB UUID 448d1b07-6560-11f1-9d75-bbdbdb72d0d3; NBB consult HTML stub 5344 B discarded; NBB broker PDF stub 5344 B discarded; NBB published-deposits list 8 this tick with sort=depositDate,desc; prior-year identical not restated; VKT-VZW 6.1.1 6.1.2 6.2 6.3 6.4 6.5 6.1.3 7 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW De Meerpaal 0443.206.559",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443206559",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2534; Actief since 15.05.1990; 1 VE leftover city_willebroek (official zetel Kerkstraat 2 bus B 2830 Willebroek since 24.02.2023; VE 2.154.891.127 DE MEERPAAL Kerkstraat 2B since 24.02.2023); VZW since 15.05.1990; naam DE MEERPAAL since 15.05.1990; RSZ-werkgever since 02.01.1995; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; leftover mined city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover WZC Seniorplaza 0467.255.829 remine@2532; NOT leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP; NOT leftover AGB Willebroek 0679.456.888; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Meerpaal 0443206559 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0443206559",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2534; deposit-id 2026-00152128 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial header 11.06.2026; NBB UUID 448d1b07-6560-11f1-9d75-bbdbdb72d0d3; NBB consult HTML stub 5344 B discarded; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list 8 this tick; NBB broker PDF stub 5344 B discarded; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Meerpaal FOI contact leftover city_willebroek leftover VAPH",
        "url": "https://demeerpaal.eu/contact",
        "publisher": "VZW De Meerpaal leftover city_willebroek leftover VAPH 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2534; FOI onthaal@demeerpaal.eu from official site https://demeerpaal.eu/contact; leftover mined city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type after leftover city_willebroek leftover WZC taken@2532 leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine@2355 SKIP leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_willebroek leftover VAPH",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")

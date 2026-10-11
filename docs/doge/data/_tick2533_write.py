from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2533_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_sint_jozef_deinze_jr2025_nbb_pdf_2533"
SRC_KBO = "src_sint_jozef_deinze_kbo_2533"
SRC_SBM = "src_sint_jozef_deinze_sbm_2533"
SRC_SITE = "src_sint_jozef_deinze_site_2533"
EID = "vzw_sint_jozef_deinze"
GAP = "gap_sint_jozef_deinze_wzc_matrix_70_jump_9_47m_73_drop_1_65m_pnl_flip_512k_destin_jump_4_42m_l5"
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
        if _row.get("entity_id") == EID or "0409.698.603" in blob or "0409698603" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 R.V.T. Sint-Jozef Deinze deposit 2026-00259876",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00259876.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2533; official native statutory PDF 454738 bytes 42p VOL-VZW 26.0.15 m05-f; header 06/07/2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-07 06:37:45 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00259876 454738 MD5 b52458777eb370d6fc6d5466b219cbe8; NBB UUID 396121f4-7944-11f1-878e-19feaa39bb97; NBB consult HTML stub 5344 B discarded; NBB published-deposits list 20 this tick from prior-tick cache; NBB ids API 403 this tick; prior-year identical not restated; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.13 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW R.V.T. Sint-Jozef Deinze 0409.698.603",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409698603",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2533; Actief since 11.03.1922; 1 VE leftover city_deinze (official zetel Kortrijksesteenweg 61 9800 Deinze since 01.01.2019 technical; VE 2.153.809.675 RVT Sint-Jozef Deinze Vzw Kortrijksesteenweg 61 since 01.06.2006); VZW since 11.03.1922; naam R.V.T. Sint-Jozef Deinze since 15.05.2007; RSZ-werkgever since 29.08.1997; RSZ2025 87.301 Rusthuizen voor ouderen (ROB); aanbestedende overheid since 11.03.1922; official WZC list Deinze Sint-Jozef VZW R.V.T. Sint-Jozef Deinze 0409698603 / CoBRHA 408.102 / HCO 3684 / 155 woongelegenheden; leftover mined city_deinze leftover WZC leftover-mined AGB-only unused leftover type; NOT leftover VAPH Vierklaver 0436.015.889 remine@2496; NOT leftover VAPH Ten Dries 0410.571.207 remine@2499; NOT leftover-via-VE Evergem Uitbating Zusters Franciscanessen 0451.818.080 SKIP; NOT leftover WZC Bejaardenzorg Zusters 0454.090.355 remine@2066; NOT leftover OCMW Karel Picque 0697.663.689 SKIP; NOT leftover Zorgbedrijf Ter Leenen 0666.615.870 SKIP; NOT leftover city_zonnebeke leftover WZC Sint-Jozef remine@2326; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche R.V.T. Sint-Jozef Deinze 0409698603 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0409698603",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2533; deposit-id 2026-00259876 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial header 06.07.2026; NBB UUID 396121f4-7944-11f1-878e-19feaa39bb97; NBB consult HTML stub 5344 B discarded; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list 20 this tick from prior-tick cache; NBB ids API 403 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "WZC Sint-Jozef FOI contact leftover city_deinze leftover WZC",
        "url": "https://www.rvtsintjozef.be",
        "publisher": "VZW R.V.T. Sint-Jozef Deinze leftover city_deinze leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2533; FOI directie@rvtsintjozef.be from official KBO + site https://www.rvtsintjozef.be; leftover mined city_deinze leftover WZC leftover-mined AGB-only unused leftover type after leftover city_willebroek leftover WZC taken@2532 leftover WZC Ten Weldebrouc OCMW SKIP leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_boechout leftover WZC taken leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine@2282 leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 m140-f-p CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover city_deinze leftover VAPH taken@2496/2499 leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine@2191 leftover CAR unused-looking leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine@2066 leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT leftover city_zonnebeke leftover WZC Sint-Jozef remine@2326",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")

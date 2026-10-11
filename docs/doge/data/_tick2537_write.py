from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2537_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_KBO = "src_trad_oostkamp_kbo_2537"
SRC_MW = "src_trad_oostkamp_maatwerk_list_2537"
SRC_SITE = "src_trad_oostkamp_site_2537"
SRC_NBB = "src_trad_oostkamp_nbb_consult_2537"
EID = "vzw_leefbaar_wonen_oostkamp"
GAP = "gap_trad_oostkamp_maatwerk_ye2025_nbb_pdf_403_l5"
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
        if _row.get("entity_id") == EID or "0457.516.831" in blob or "0457516831" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_KBO,
        "title": "KBO Leefbaar Wonen-Kringloopcentrum 0457.516.831",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0457516831",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2537; Actief since 27.12.1995; 12 VE leftover city_oostkamp (official zetel Terluchtestraat 38 8020 Oostkamp since 30.05.2016; VE 2.269.503.258 Kringloopcentrum Leefbaar Wonen vzw Terluchtestraat 38 8020 Oostkamp since 01.07.2008 + VE 2.281.998.640 Blijzaak Terluchtestraat 40 8020 Oostkamp since 27.11.2018 + VE 2.363.065.597 Kringwinkel Outlet Leitemolenstraat 8 8020 Oostkamp since 01.09.2024 + 9 VE leftover-via-VE FROM leftover city_oostkamp in Brugge/Beernem/Zedelgem/Blankenberge/Jabbeke); VZW since 27.12.1995; commerciële naam De Kringwinkel 't rad since 20.12.2004; RSZ-werkgever since 01.10.1996; btw since 01.01.1997; RSZ2025 88.993 Beschutte en sociale werkplaatsen; leftover mined city_oostkamp leftover maatwerk leftover-mined AGB-only unused leftover type; NOT leftover AGB Oostkamp 0894.294.369; NOT leftover WZC Ter Luchte 0738.896.510; NOT leftover-via-VE of a DIFFERENT leftover city",
    },
    {
        "source_id": SRC_MW,
        "title": "Official maatwerk list Leefbaar Wonen-Kringloopcentrum / De Kringwinkel 't rad Oostkamp 0457516831",
        "url": "https://www.vlaanderen.be/maatwerkbedrijven",
        "publisher": "Vlaanderen official maatwerk zetel list (tick2515/maatwerk.csv reuse)",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2537; official maatwerk zetel Oostkamp 8020 ZETELNUMMER 0457516831 Leefbaar Wonen-Kringloopcentrum / vestiging De Kringwinkel 't rad; leftover public leftover maatwerk of leftover-mined AGB-only city_oostkamp; unused leftover type after leftover WZC Ter Luchte@2536; euros NOT taken from this list",
    },
    {
        "source_id": SRC_SITE,
        "title": "Kringwinkel 't rad FOI contact leftover city_oostkamp leftover maatwerk",
        "url": "https://www.kringwinkel.be/centra/trad",
        "publisher": "VZW Leefbaar Wonen-Kringloopcentrum leftover city_oostkamp leftover maatwerk 12 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2537; FOI info@trad.be from official site https://www.kringwinkel.be/centra/trad (also info@kringwinkel.be); zetel Terluchtestraat 38 8020 Oostkamp; leftover mined city_oostkamp leftover maatwerk leftover-mined AGB-only unused leftover type; FIRST LOCK leftover city_oud_heverlee leftover WZC De Kouter 0848.738.221 SKIP Korian PPS + NBB 403; leftover WZC unused-not-hardskip of leftover-mined AGB-only cities 0; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_oostkamp leftover maatwerk FOI-ready last resort",
    },
    {
        "source_id": SRC_NBB,
        "title": "NBB Consult fiche Leefbaar Wonen-Kringloopcentrum 0457516831 (deposit-id blocked 403)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0457516831",
        "publisher": "NBB Consult",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2537; NBB consult HTML stub 5344 B discarded; NBB /api/external/published-deposits HTTP 403 this tick; NBB /api/external/company 403; NBB broker without deposit-id unused; SBM IP-blacklist; no YE2025 native PDF this tick; Companyweb unused for euros; FOI-ready last resort asks VZW for official NBB YE2025 deposit PDF + deposit-id",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Leefbaar Wonen-Kringloopcentrum (De Kringwinkel 't rad)",
    "name_fr": "ASBL Leefbaar Wonen-Kringloopcentrum (De Kringwinkel 't rad)",
    "name_en": "Leefbaar Wonen-Kringloopcentrum VZW (leftover city_oostkamp leftover maatwerk)",
    "level": "parastatal",
    "parent_id": "city_oostkamp",
    "community_language": "nl",
    "website": "https://www.kringwinkel.be/centra/trad",
    "foi_email": "info@trad.be",
    "foi_postal": "Terluchtestraat 38 8020 Oostkamp",
    "notes": "tick2537 YE2025 FOI-ready last resort NBB published-deposits 403 no deposit-id no native PDF + Strong KBO 0457.516.831 Actief 12 VE; official zetel Terluchtestraat 38 8020 Oostkamp since 30.05.2016; RSZ2025 88.993; leftover mined city_oostkamp leftover maatwerk leftover-mined AGB-only unused leftover type after leftover WZC Ter Luchte@2536; no invented euros; Companyweb unused for euros; FIRST LOCK leftover city_oud_heverlee leftover WZC De Kouter 0848.738.221 SKIP Korian PPS + NBB 403; NOT leftover-via-VE of a DIFFERENT leftover city; leftover WZC unused-not-hardskip of leftover-mined AGB-only cities 0; not TE-additive",
}], ent_fields)
print("entities ok")
print("CORE1A DONE")

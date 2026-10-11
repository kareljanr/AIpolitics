#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2428_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_duinhuisjes_jr2025_nbb_pdf_2428"
SRC_KBO = "src_duinhuisjes_kbo_2428"
SRC_SBM = "src_duinhuisjes_sbm_2428"
SRC_SITE = "src_duinhuisjes_site_2428"
GAP = "gap_duinhuisjes_opgroeien_matrix_opbr_7_50m_omzet_1_31m_73_5_85m_pnl_jump_458k_destin_0_l5"
if not (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file():
    raise SystemExit("FOI draft missing")

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Kinderopvang de Duinhuisjes deposit 2026-00190043,http://cdn.staatsbladmonitor.be/2026pdf/2026-00190043.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2428; official native PDF 4092966 bytes 40p VOL-VZW 25.0.13 m05-f; header 22.06.2026; AV 19.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-24 01:59:34 UTC OpenPDF 1.3.26; financial + waarderingsregels pp.1-35 native; commissarisverslag pp.36-40 scan; VOL-VZW 7 not filed; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang de Duinhuisjes 0413.323.037,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413323037,KBO Public Search FOD Economie,{DAY},official_register,tick2428; Actief; 11 VE; naam Kinderopvang de Duinhuisjes since 28.11.1996; VZW since 03.07.1973; begindatum 03.07.1973; zetel Bremlaan 37 8300 Knokke-Heist since 01.12.2004; RSZ2025 88.911; RSZ-werkgever since 01.04.1974; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; aanbestedende overheid since 03.07.1973; 8 functiehouders; voorzitter Lieven Vandenberghe since 25.02.2025; dagelijks bestuur Agnetha Delacauw since 23.06.2023; related 0445.265.533 t Bremhuisje; FOI melissa.veldkamp@duinhuisjes.be; NOT KISME 0894.549.440; NOT Kinderlach 0450.275.186; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT Kinderopvang Baloo BV 0762.684.274; NOT Helan 0464.151.037; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6 9031 Drongen",
    f"{SRC_SBM},NBB Consult / SBM fiche Duinhuisjes 0413323037 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0413323037,NBB Consult,{DAY},official_register,tick2428; deposit-id 2026-00190043 YE 31/12/2025 filing header 22/06/2026 VOL-VZW Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Duinhuisjes FOI contact leftover city_knokke_heist CIK,https://wp.duinhuisjes.be/,VZW Kinderopvang de Duinhuisjes,{DAY},foi_contact,tick2428; FOI melissa.veldkamp@duinhuisjes.be zetel Bremhuisje; zetel Bremlaan 37 8300 Knokke-Heist; leftover mined city_knokke_heist after AGSO / Het Dak / BVK; also leftover mined city_brugge / city_maldegem / city_de_haan; 11 VE KDV+BKO+onthaalouders; NOT Kloosterstraat 6 Drongen; NOT KISME; NOT Kinderlach YE2024; NOT Kindercentrum; NOT KOS; NOT Vormingscentrum; NOT Helan Kinderopvang",
])
print("sources ok")

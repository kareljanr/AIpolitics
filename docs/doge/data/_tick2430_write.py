#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2430_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_beregoed_jr2025_nbb_pdf_2430"
SRC_KBO = "src_beregoed_kbo_2430"
SRC_SBM = "src_beregoed_sbm_2430"
SRC_SITE = "src_beregoed_site_2430"
GAP = "gap_beregoed_opgroeien_matrix_omzet_2_98m_73_empty_pnl_jump_177k_destin_177k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KINDERDAGVERBLIJF BEREGOED deposit 2026-00295160,http://cdn.staatsbladmonitor.be/2026pdf/2026-00295160.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2430; official native PDF 103655 bytes 21p VKT-VZW 26.0.15 m04-f-p; header 14.07.2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-01; CreationDate 2026-07-07 16:58:47 +02 Nuance PDF Create; modified using OpenPDF 1.3.26; all 21p native text; PDF-Verkort is native euros not scan; prior-year published on same PDF; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO KINDERDAGVERBLIJF BEREGOED 0447.515.042,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0447515042,KBO Public Search FOD Economie,{DAY},official_register,tick2430; Actief; 3 VE 2.150.842.168 Michel Thieryhof 10 9000 Gent since 03.01.2006 + 2.218.504.618 De Bereboom Lostraat 28 9880 Aalter since 27.04.2013 + 2.311.240.873 t Berenest Lostraat 30 9880 Aalter since 01.01.2021; naam KINDERDAGVERBLIJF BEREGOED since 15.02.2000; VZW since 30.03.1992; begindatum 30.03.1992; zetel Michel Thieryhof 10 9000 Gent since 11.06.2020; RSZ2025 88.911; RSZ-werkgever since 01.01.1996; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; 5 bestuurders; FOI mireille.verwilst@azstlucas.be; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; NOT Kloosterstraat 6 9031 Drongen",
    f"{SRC_SBM},NBB Consult / SBM fiche Beregoed 0447515042 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0447515042,NBB Consult,{DAY},official_register,tick2430; deposit-id 2026-00295160 YE 31/12/2025 filing header 14/07/2026 VKT-VZW PDF-Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Beregoed FOI contact leftover city_gent CIK,https://www.kinderdagverblijfberegoed.be/,VZW KINDERDAGVERBLIJF BEREGOED,{DAY},foi_contact,tick2430; FOI mireille.verwilst@azstlucas.be / beregoed@azstlucas.be; zetel Michel Thieryhof 10 9000 Gent; leftover mined city_gent after Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 3 VE Gent 87 plaatsen 6 leefgroepen AZ Sint-Lucas campus + De Bereboom + t Berenest Aalter same KBO; NOT Kloosterstraat 6 Drongen; NOT Windekind; NOT Elfenbankje; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Duinhuisjes; NOT t Bremhuisje stopgezet 1993",
])
print("sources ok")

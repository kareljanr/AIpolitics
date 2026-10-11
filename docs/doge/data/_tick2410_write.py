#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2410_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_zonnestraal_junior_jr2025_nbb_pdf_2410"
SRC_KBO = "src_zonnestraal_junior_kbo_2410"
SRC_SBM = "src_zonnestraal_junior_sbm_2410"
SRC_SITE = "src_zonnestraal_junior_site_2410"
GAP = "gap_zonnestraal_junior_opgroeien_matrix_73_200k_omzet_empty_bruto_neg88_pnl_loss_294_destin_0_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"
if not (ROOT / DRAFT).is_file():
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang Zonnestraal Junior deposit 2026-00244618,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244618.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2410 EVERY-10; official native PDF 31198 bytes 8p VKT-VZW 25.0.13 m04-f; header 30.06.2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 02:06:44 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang Zonnestraal Junior 0866.116.859,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0866116859,KBO Public Search FOD Economie,{DAY},official_register,tick2410 EVERY-10; Actief; 20 VE; zetel Gladiolenstraat 10 9100 Sint-Niklaas since 30.12.2003; naam Kinderopvang Zonnestraal Junior since 30.12.2003; begindatum 02.07.2004; RSZ2025 88.911; RSZ-werkgever since 01.04.2003; FOI info@kinderopvangzonnestraal.be; NOT parent KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Grimbergen VAPH Zonnestraal Havinet; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539",
    f"{SRC_SBM},Staatsbladmonitor fiche Zonnestraal Junior 0866116859 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0866116859,Staatsbladmonitor,{DAY},official_register,tick2410 EVERY-10; deposit-id 2026-00244618 YE 2025-01-01>2025-12-31 neerlegging 2026-06-30 and CDN Last-Modified 2026-07-25; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Zonnestraal Junior FOI contact leftover city_sint_niklaas CIK,https://www.kinderopvangzonnestraal.be/,Kinderopvang Zonnestraal vzw,{DAY},foi_contact,tick2410 EVERY-10; FOI info@kinderopvangzonnestraal.be; zetel Gladiolenstraat 10 9100 Sint-Niklaas; 20 VE residual dual vs parent 0413.351.642 1 VE same address same board; leftover city_sint_niklaas after Elfenbankje@2409; NOT Grimbergen VAPH Zonnestraal; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")

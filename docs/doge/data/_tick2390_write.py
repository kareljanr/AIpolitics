#!/usr/bin/env python3
"""Surgical tick 2390 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2390_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_ldsst"
SRC_PDF = "src_ldsst_jr2025_nbb_pdf_2390"
SRC_KBO = "src_ldsst_kbo_2390"
SRC_SBM = "src_ldsst_sbm_2390"
SRC_SITE = "src_ldsst_site_2390"
GAP = "gap_ldsst_riziv_vl_logopedie_matrix_bruto_591k_73_179k_pnl_flip_destin_59k_l5"
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
    f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 LDSST deposit 2026-00243690,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243690.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2390 EVERY-10; official native PDF 65456 bytes 19p MIC-VZW 25.0.13 m08-f; header 29.06.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 01:18:34 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Limburgse Dienst voor Stem- en Spraaktherapie vzw LDSST 0410.121.344,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410121344,KBO Public Search FOD Economie,{DAY},official_register,tick2390; Actief; 1 VE 2.156.599.812 Ilgatlaan 11 Hasselt since 10.10.2006; zetel Ilgatlaan 11 bus 7 3500 Hasselt since 01.01.2025; RSZ2025 86.996 logopedie; BTW2025 86.931 psychologie; voorzitter Erik Ottenbourgs; dagelijks bestuur Kris s Hertogen / Johan Gommers / Joris Smets; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT De Schans 0430.473.231",
    f"{SRC_SBM},Staatsbladmonitor fiche LDSST 0410121344 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410121344,Staatsbladmonitor,{DAY},official_register,tick2390; deposit-id 2026-00243690 YE 2025-01-01>2025-12-31 neerlegging 2026-06-29 and CDN Last-Modified 2026-07-25; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},LDSST FOI contact / Kohesi-family logopedie leftover city_hasselt,https://www.kohesi.be/,LDSST vzw,{DAY},foi_contact,tick2390; FOI info@kohesi.be; zetel Ilgatlaan 11 bus 7 3500 Hasselt; leftover city_hasselt after BW Kohesi@2389; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT De Schans 0430.473.231; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")

#!/usr/bin/env python3
"""Surgical tick 2389 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2389_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_bw_kohesi"
SRC_PDF = "src_bwkohesi_jr2025_nbb_pdf_2389"
SRC_KBO = "src_bwkohesi_kbo_2389"
SRC_SBM = "src_bwkohesi_sbm_2389"
SRC_SITE = "src_bwkohesi_site_2389"
GAP = "gap_bwkohesi_riziv_vl_ibw_matrix_omzet_1_29m_73_488k_pnl_jump_destin_empty_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Beschut Wonen Kohesi deposit 2026-00243983,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243983.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2389; official native PDF 851816 bytes 28p VKT-VZW 25.0.13 m04-f; header 29.06.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 01:27:25 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Beschut Wonen Kohesi vzw 0451.932.995,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0451932995,KBO Public Search FOD Economie,{DAY},official_register,tick2389; Actief; 2 VE 2.150.841.475 Heusden-Zolder + 2.283.384.849 Harmoniestraat 9 Beringen; zetel Pastoor Paquaylaan 123 bus 1 3550 Heusden-Zolder; RSZ2025 87.205; voorzitter Erik Ottenbourgs; dagelijks bestuur Kris s Hertogen / Johan Gommers / Joris Smets; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907",
    f"{SRC_SBM},Staatsbladmonitor fiche Beschut Wonen Kohesi 0451932995 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0451932995,Staatsbladmonitor,{DAY},official_register,tick2389; deposit-id 2026-00243983 YE 2025-01-01>2025-12-31 neerlegging 2026-06-29 and CDN Last-Modified 2026-07-25; NBB consult reference 2026-00243983 year-end 30.12.2025; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Beschut Wonen Kohesi FOI contact / IBW campuses Heusden-Zolder+Beringen,https://www.kohesi.be/,Beschut Wonen Kohesi vzw,{DAY},foi_contact,tick2389; FOI info@kohesi.be; zetel Pastoor Paquaylaan 123 bus 1 3550 Heusden-Zolder; leftover city_heusden_zolder + leftover city_beringen; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")

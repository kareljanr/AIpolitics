#!/usr/bin/env python3
"""Surgical tick 2391 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2391_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_de_schans"
SRC_PDF = "src_deschans_jr2025_nbb_pdf_2391"
SRC_KBO = "src_deschans_kbo_2391"
SRC_SBM = "src_deschans_sbm_2391"
SRC_SITE = "src_deschans_site_2391"
GAP = "gap_deschans_vl_property_matrix_bruto_76k_73_51k_cash_jump_165k_debt_821k_l5"
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
    f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 De Schans deposit 2026-00242881,http://cdn.staatsbladmonitor.be/2026pdf/2026-00242881.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2391; official native PDF 58927 bytes 17p MIC-VZW 25.0.13 m08-f; header 29.06.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 01:03:16 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO De Schans vzw 0430.473.231,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430473231,KBO Public Search FOD Economie,{DAY},official_register,tick2391; Actief; 0 VE; zetel Pastoor Paquaylaan 123 bus 1 3550 Heusden-Zolder since 02.02.1992; BTW2025 86.931 psychologie + 68.321 syndici; BTW2008 86.904 + 68.321; voorzitter Erik Ottenbourgs; dagelijks bestuur Kris s Hertogen / Johan Gommers / Joris Smets; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344",
    f"{SRC_SBM},Staatsbladmonitor fiche De Schans 0430473231 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0430473231,Staatsbladmonitor,{DAY},official_register,tick2391; deposit-id 2026-00242881 YE 2025-01-01>2025-12-31 neerlegging 2026-07-03 and CDN Last-Modified 2026-07-25; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},De Schans FOI contact / Kohesi-family property leftover city_heusden_zolder + city_beringen,https://www.kohesi.be/,De Schans vzw,{DAY},foi_contact,tick2391; FOI info@kohesi.be; zetel Pastoor Paquaylaan 123 bus 1 3550 Heusden-Zolder; leftover city_heusden_zolder + leftover city_beringen after LDSST@2390; Harmoniestraat 9 Beringen onverdeeldheid; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")

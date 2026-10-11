#!/usr/bin/env python3
"""Surgical tick 2399 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2399_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_heuvelheem_jr2025_nbb_pdf_2399"
SRC_KBO = "src_heuvelheem_kbo_2399"
SRC_SBM = "src_heuvelheem_sbm_2399"
SRC_SITE = "src_heuvelheem_site_2399"
GAP = "gap_heuvelheem_vaph_matrix_opbr_15_17m_73_12_22m_pnl_flip_destin_empty_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Heuvelheem deposit 2026-00243798,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243798.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2399; official native PDF 740477 bytes 50p VOL-VZW 23.0.10 m05-f; header 30.06.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-24; CreationDate 2026-07-03 01:21:03 UTC OpenPDF 1.3.26; prior-year restated after Ons Tehuis inbreng; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Heuvelheem 0413.210.201,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413210201,KBO Public Search FOD Economie,{DAY},official_register,tick2399; Actief; 8 VE; zetel Nokerepontweg (WAN) 1 9772 Kruisem; RSZ2025 87.202; Aanbestedende overheid since 13.04.1973; absorbed Ons Tehuis 0418.338.729 since 22.03.2024; NOT Vijvens 0415.093.385; NOT CAR Halle Asse 0425.788.230",
    f"{SRC_SBM},Staatsbladmonitor fiche Heuvelheem 0413210201 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0413210201,Staatsbladmonitor,{DAY},official_register,tick2399; deposit-id 2026-00243798 YE 2025-01-01>2025-12-31 neerlegging 2026-06-30 and CDN Last-Modified 2026-07-24; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Heuvelheem FOI contact / leftover city_kruisem + leftover city_oudenaarde VAPH zorgaanbieder,https://www.heuvelheem.be/contact/,Heuvelheem vzw,{DAY},foi_contact,tick2399; FOI info@heuvelheem.be; zetel Nokerepontweg 1 9772 Kruisem; VAPH HCO 201276; leftover city_kruisem after CAR Halle Asse@2398; NOT Vijvens; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo",
])
print("sources ok")

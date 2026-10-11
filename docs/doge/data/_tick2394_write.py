#!/usr/bin/env python3
"""Surgical tick 2394 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2394_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_zwz_jr2025_nbb_pdf_2394"
SRC_KBO = "src_zwz_kbo_2394"
SRC_SBM = "src_zwz_sbm_2394"
SRC_SITE = "src_zwz_site_2394"
GAP = "gap_zwz_zorgkas_riziv_wzc_matrix_omzet_10_69m_73_1_97m_pnl_drop_destin_empty_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 ZWZ Zedelgem deposit 2026-00228427,http://cdn.staatsbladmonitor.be/2026pdf/2026-00228427.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2394; official native PDF 2245845 bytes 49p VOL-VZW 25.0.13 m05-f; header 25.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-18; CreationDate 2026-07-01 01:19:30 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Zorg en Welzijn Zedelgem vzw 0832.024.923,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0832024923,KBO Public Search FOD Economie,{DAY},official_register,tick2394; Actief; 1 VE 2.249.329.931 Fazantenlaan 89 Zedelgem; zetel Fazantenlaan 89 8210 Zedelgem since 19.04.2016; RSZ2025 87.101 RVT; 17 functiehouders; NOT CAR Houtland-Westkust 0408.436.019; NOT Zonnebloem 0421.039.386",
    f"{SRC_SBM},Staatsbladmonitor fiche ZWZ 0832024923 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0832024923,Staatsbladmonitor,{DAY},official_register,tick2394; deposit-id 2026-00228427 YE 2025-01-01>2025-12-31 neerlegging 2026-07-01 and CDN Last-Modified 2026-07-18; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},ZWZ FOI contact / leftover city_zedelgem WZC Klaverveld PPS,https://www.klaverveld.gvo.be/,Zorg en Welzijn Zedelgem vzw,{DAY},foi_contact,tick2394; FOI info@zwz.be gvo-secretariaat@gvo.be; zetel Fazantenlaan 89 8210 Zedelgem; leftover city_zedelgem after Zonnebloem@2393; NOT CAR Houtland; NOT Zonnebloem; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker",
])
print("sources ok")

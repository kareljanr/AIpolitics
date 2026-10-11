#!/usr/bin/env python3
"""Surgical tick 2400 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2400_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_arc_jr2025_nbb_pdf_2400"
SRC_KBO = "src_arc_kbo_2400"
SRC_SBM = "src_arc_sbm_2400"
SRC_SITE = "src_arc_site_2400"
GAP = "gap_arc_riziv_vl_vaph_matrix_bruto_2_49m_omzet73_empty_pnl_jump_destin_170k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Antwerps Revalidatiecentrum deposit 2026-00272201,http://cdn.staatsbladmonitor.be/2026pdf/2026-00272201.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2400 EVERY-10; official native PDF 48895 bytes 12p VKT-VZW 26.0.15 m04-f; header 09.07.2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-29; CreationDate 2026-07-09 11:40:47 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Antwerps Revalidatiecentrum 0408.434.930,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408434930,KBO Public Search FOD Economie,{DAY},official_register,tick2400; Actief; 1 VE 2.150.801.190 Lange Elzenstraat 52-54 2018 Antwerpen since 03.01.2006; zetel Lange Elzenstraat 52-54 2018 Antwerpen since 23.06.2004; RSZ2025 86.959; VAZG HCO 29610; RIZIV 95326551; algemeen directeur Celine de Bruyn; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT CAR Antenne 3000 0433.184.479",
    f"{SRC_SBM},Staatsbladmonitor fiche ARC 0408434930 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0408434930,Staatsbladmonitor,{DAY},official_register,tick2400; deposit-id 2026-00272201 YE 2025-01-01>2025-12-31 neerlegging 2026-07-09 and CDN Last-Modified 2026-07-29; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},ARC FOI contact / leftover city_antwerpen CAR,https://www.antwerpsrevalidatiecentrum.be/contact,Antwerps Revalidatiecentrum vzw,{DAY},foi_contact,tick2400 EVERY-10; FOI info@arc-reva.be; zetel Lange Elzenstraat 52-54 2018 Antwerpen; VAZG HCO 29610; leftover city_antwerpen after Heuvelheem@2399; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo; NOT Vriendenkring; NOT CAR Antenne 3000",
])
print("sources ok")

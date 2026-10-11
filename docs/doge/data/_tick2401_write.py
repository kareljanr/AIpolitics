#!/usr/bin/env python3
"""Surgical tick 2401 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2401_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_verbint_jr2025_nbb_pdf_2401"
SRC_KBO = "src_verbint_kbo_2401"
SRC_SBM = "src_verbint_sbm_2401"
SRC_SITE = "src_verbint_site_2401"
GAP = "gap_verbint_car_clb_wzc_vaph_matrix_omzet_12_89m_73_10_06m_pnl_jump_6_0m_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 VERBINT deposit 2026-00297392,http://cdn.staatsbladmonitor.be/2026pdf/2026-00297392.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2401; official native PDF 851596 bytes 56p VOL-VZW 26.0.15 m05-f; header 14.07.2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-01; CreationDate 2026-07-16 02:22:24 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee; KMSI fusion 31.03.2025 not like-for-like",
    f"{SRC_KBO},KBO VERBINT 0408.032.379,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408032379,KBO Public Search FOD Economie,{DAY},official_register,tick2401; Actief; 20 VE; zetel Korte Begijnenstraat 22 2300 Turnhout since 04.02.1993; naam VERBINT since 31.03.2025; slorpte KMSI 0412.746.282 since 31.03.2025; RSZ2025 85.691 CLB; Aanbestedende overheid; Carrewiel Turnhout VE 2.138.253.449; Carrewiel Zuiderkempen VE 2.138.253.548; Carrewiel Mechelen Vijfhoek VE 2.138.253.746; NOT ARC 0408.434.930; NOT Noorderkempen 0408.078.010",
    f"{SRC_SBM},Staatsbladmonitor fiche VERBINT 0408032379 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0408032379,Staatsbladmonitor,{DAY},official_register,tick2401; deposit-id 2026-00297392 YE 2025-01-01>2025-12-31 neerlegging 2026-07-14 and CDN Last-Modified 2026-08-01; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},VERBINT / Carrewiel FOI contact leftover city_turnhout CAR,https://www.verbint.be/,VERBINT vzw,{DAY},foi_contact,tick2401; FOI info@verbint.be boekhouding@verbint.be; zetel Korte Begijnenstraat 22 2300 Turnhout; Carrewiel https://www.carrewiel.be/ fusie CAR Turnhout + CAR Zuiderkempen + CAR Vijfhoek; leftover city_turnhout + city_mechelen + city_westerlo after ARC@2400; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan",
])
print("sources ok")

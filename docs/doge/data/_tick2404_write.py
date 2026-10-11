#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2404_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_tereecken_jr2025_nbb_pdf_2404"
SRC_KBO = "src_tereecken_kbo_2404"
SRC_SBM = "src_tereecken_sbm_2404"
SRC_SITE = "src_tereecken_site_2404"
GAP = "gap_tereecken_riziv_vl_matrix_bruto_3_72m_omzet73_empty_pnl_loss_widen_208k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Ter Eecken deposit 2026-00107832,http://cdn.staatsbladmonitor.be/2026pdf/2026-00107832.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2404; official native PDF 56067 bytes 16p VKT-VZW 23.0.8 m04-f; header 07.05.2026; AV 21.04.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-05; CreationDate 2026-05-11 22:37:43 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Ter Eecken 0432.465.392,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0432465392,KBO Public Search FOD Economie,{DAY},official_register,tick2404; Actief; 1 VE 2.156.368.495; zetel Vlaanderenstraat 2 9700 Oudenaarde since 28.05.1997; naam Ter Eecken since 01.10.1992; begindatum 30.09.1986; RSZ2025 86.101; RSZ-werkgever since 03.11.1986; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT H.Hart Oudenaarde 0407.644.082; NOT Heuvelheem 0413.210.201",
    f"{SRC_SBM},Staatsbladmonitor fiche Ter Eecken 0432465392 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0432465392,Staatsbladmonitor,{DAY},official_register,tick2404; deposit-id 2026-00107832 YE 2025-01-01>2025-12-31 neerlegging 2026-05-07 and CDN Last-Modified 2026-06-05; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Ter Eecken FOI contact leftover city_oudenaarde CAR,https://www.cartereecken.be/,Ter Eecken vzw,{DAY},foi_contact,tick2404; FOI onthaal@cartereecken.be; zetel Vlaanderenstraat 2 9700 Oudenaarde; leftover city_oudenaarde after De Kade@2403; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000; NOT H.Hart Oudenaarde",
])
print("sources ok")

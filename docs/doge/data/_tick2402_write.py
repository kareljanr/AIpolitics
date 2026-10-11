#!/usr/bin/env python3
"""Surgical tick 2402 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2402_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_cfrzelzate_jr2025_nbb_pdf_2402"
SRC_KBO = "src_cfrzelzate_kbo_2402"
SRC_SBM = "src_cfrzelzate_sbm_2402"
SRC_SITE = "src_cfrzelzate_site_2402"
GAP = "gap_cfrzelzate_riziv_vl_vaph_matrix_bruto_1_42m_omzet73_empty_pnl_loss_flip_128k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CFR Zelzate deposit 2026-00243990,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243990.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2402; official native PDF 57128 bytes 18p VKT-VZW 26.0.15 m04-f; header 30.06.2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 01:27:41 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO CFR Zelzate 0419.645.952,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419645952,KBO Public Search FOD Economie,{DAY},official_register,tick2402; Actief; 1 VE 2.187.068.896; zetel Stationsstraat 40 9060 Zelzate since 01.07.1990; naam Centrum voor Functionele Revalidatie / C.F.R. since 13.07.1979; vervangt 0850.493.921 afgesloten 01.03.2011; RSZ2025 86.959 Andere ambulante revalidatieactiviteiten; Aanbestedende overheid since 18.01.2003; NOT VERBINT 0408.032.379; NOT WZC Zilverbos 0644.984.078; NOT ARC 0408.434.930; NOT CAR Noorderkempen 0408.078.010",
    f"{SRC_SBM},Staatsbladmonitor fiche CFR Zelzate 0419645952 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0419645952,Staatsbladmonitor,{DAY},official_register,tick2402; deposit-id 2026-00243990 YE 2025-01-01>2025-12-31 neerlegging 2026-06-30 and CDN Last-Modified 2026-07-25; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CFR Zelzate FOI contact leftover city_zelzate CAR,https://www.revalidatiecentrum.be/,Centrum voor Functionele Revalidatie vzw,{DAY},foi_contact,tick2402; FOI info@revalidatiecentrum.be greet.vanmossevelde@revalidatiecentrum.be; zetel Stationsstraat 40 9060 Zelzate; leftover city_zelzate after VERBINT@2401; ~135 kinderen 0-19 multidisciplinaire therapie; officiële opening nieuw centrum 24.04.2026; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT WZC Zilverbos Zelzate",
])
print("sources ok")

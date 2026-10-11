#!/usr/bin/env python3
"""Surgical tick 2403 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2403_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_dekade_jr2025_nbb_pdf_2403"
SRC_KBO = "src_dekade_kbo_2403"
SRC_SBM = "src_dekade_sbm_2403"
SRC_SITE = "src_dekade_site_2403"
GAP = "gap_dekade_vaph_car_matrix_opbr_60_22m_73_51_29m_pnl_drop_destin_800k_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 De Kade deposit 2026-00300772,http://cdn.staatsbladmonitor.be/2026pdf/2026-00300772.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2403; official native PDF 2366484 bytes 63p VOL-VZW 26.0.15 m05-f; header 15.07.2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-02; CreationDate 2026-07-17 01:04:38 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee not amlcompany",
    f"{SRC_KBO},KBO De Kade 0413.650.659,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413650659,KBO Public Search FOD Economie,{DAY},official_register,tick2403; Actief; 35 VE; zetel Potterierei 42 8000 Brugge since 21.12.2010; naam De Kade since 21.12.2010; begindatum 17.09.1973; RSZ2025 87.201 Instellingen met huisvesting voor minderjarigen met een mentale handicap; slorpte 0408.646.746 Ter Spermalie + 0409.669.107 Revalidatiecentrum Spermalie + 0410.706.710 Jongensinstituut Spermalie + 0432.620.889 BO-school Het Anker + 0432.984.244 Het Anker since 21.12.2010; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930",
    f"{SRC_SBM},Staatsbladmonitor fiche De Kade 0413650659 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0413650659,Staatsbladmonitor,{DAY},official_register,tick2403; deposit-id 2026-00300772 YE 2025-01-01>2025-12-31 neerlegging 2026-07-17 and CDN Last-Modified 2026-08-02; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},De Kade FOI contact leftover city_brugge VAPH+CAR Spermalie+BuO,https://de-kade.be/,De Kade vzw,{DAY},foi_contact,tick2403; FOI info@de-kade.be car@de-kade.be; zetel Potterierei 42 8000 Brugge; leftover city_brugge after CFR Zelzate@2402; CAR Spermalie Ruddershove 6; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")

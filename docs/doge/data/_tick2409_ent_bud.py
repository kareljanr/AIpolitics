#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2409_stamp.txt").read_text().strip().splitlines()
EID = "vzw_elfenbankje"
SRC_PDF = "src_elfenbankje_jr2025_nbb_pdf_2409"

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

append_lines(DATA / "entities.csv", [
    f'{EID},Kinderopvang Elfenbankje VZW Gent,ASBL Kinderopvang Elfenbankje Gand,Kinderopvang Elfenbankje VZW (leftover city_gent CIK),parastatal,city_gent,nl,https://www.elfenbankje.be/,kdv@elfenbankje.be,"Sint-Pietersaalststraat 80, 9000 Gent",tick2409 YE2025 Strong official native NBB PDF deposit 2026-00072866 + Strong KBO 0417.638.151 Actief 1 VE 2.153.866.093 RSZ2025 88.911 Kinderopvang Vlaamse Gemeenschap since 12.12.2025 slorpte ELFENBANKJE D.V.O. 0862.573.884 since 30.03.2026 post-YE2025; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 2185717 CIK envelope; pnl DROP 197033; equity JUMP 2825006; assets JUMP 3552531; debt DROP 727525; FTE DROP 32.1; kapitaalsubsidies DROP 965541; destin691 0 was 1000000; cash JUMP 1286323; geldbeleggingen empty; gebouwen DROP 1896642; aanbouw empty; capex 20654; leftover city_gent after t Eekhoorntje@2408; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_elfenbankje_bruto_jr2025_statutory,{EID},2025,2185717,2185717,2185717,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.73% (primary L5 envelope; omzet 70 empty and 73 empty so bruto is envelope),{SRC_PDF},strong,tick2409; PDF p5 native; YE2024 2127706; omzet70 empty; 73 empty; 76A 2557",
    f"bud_elfenbankje_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; commercial line not published; envelope is bruto 9900),{SRC_PDF},strong,tick2409; PDF p5 native; 73 empty",
    f"bud_elfenbankje_pnl_jr2025_statutory,{EID},2025,197033,197033,197033,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -3.72% vs YE2024 204636,{SRC_PDF},strong,tick2409; PDF p5 native; YE2024 204636; bedrijfswinst 9901 203285 DROP; destin691 0",
    f"bud_elfenbankje_bedrijfswinst_jr2025_statutory,{EID},2025,203285,203285,203285,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -1.99% vs YE2024 207419,{SRC_PDF},strong,tick2409; PDF p5 native; YE2024 207419; 62 1842406; 630 137265; 76A 2557",
    f"bud_elfenbankje_equity_jr2025_statutory,{EID},2025,2825006,2825006,2825006,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +4.92%,{SRC_PDF},strong,tick2409; PDF p4 native; YE2024 2692476; kapitaalsubsidies 965541; overgedragen 14 708004; bestemde 13 1140000; fondsen 10 11461",
    f"bud_elfenbankje_assets_jr2025_statutory,{EID},2025,3552531,3552531,3552531,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.15%,{SRC_PDF},strong,tick2409; PDF p3 native; YE2024 3477682; gebouwen 22 1896642; aanbouw 27 empty",
    f"bud_elfenbankje_debt_jr2025_statutory,{EID},2025,727525,727525,727525,NBB VKT-VZW code 17/49 schulden YE2025 DROP -7.35%,{SRC_PDF},strong,tick2409; PDF p4 native; YE2024 785206; LT 17 387000; ST 42/48 333775; 9061 423000",
    f"bud_elfenbankje_cash_jr2025_statutory,{EID},2025,1286323,1286323,1286323,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +13.10%,{SRC_PDF},strong,tick2409; PDF p3 native; YE2024 1137339; geldbeleggingen 50/53 empty",
    f"bud_elfenbankje_fte_jr2025_statutory,{EID},2025,32.1,32.1,32.1,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 DROP -1.83%,{SRC_PDF},strong,tick2409; PDF p10 native; YE2024 32.7; personeel 62 1842406",
    f"bud_elfenbankje_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 0 DROP (was 1000000),{SRC_PDF},strong,tick2409; PDF p6 native; YE2024 1000000; post 13 1140000 FLAT; 9905 197033 fully to overgedragen 14",
])
print("entities+budgets ok")

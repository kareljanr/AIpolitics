#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2406_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kinderopvang_mereltjes"
SRC_PDF = "src_mereltjes_jr2025_nbb_pdf_2406"

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
    f'{EID},Kinderopvang De Mereltjes VZW Tongeren-Borgloon,ASBL Kinderopvang De Mereltjes Tongres-Borgloon,Kinderopvang De Mereltjes VZW (leftover city_tongeren_borgloon CIK groepsopvang),parastatal,city_tongeren_borgloon,nl,https://mereltjes.be/,kinderdagverblijf@mereltjes.be,"Hasseltsesteenweg 16, 3700 Tongeren-Borgloon",tick2406 YE2025 Strong official native NBB PDF deposit 2026-00216076 + Strong KBO 0412.778.352 Actief 1 VE 2.150.768.627 RSZ2025 88.911 Kinderopvang Vlaamse Gemeenschap since 01.04.2014 Aanbestedende overheid since 18.01.2003; omzet70 empty VKT; 73 empty VKT; bruto9900 DROP 3028501 CIK envelope; pnl JUMP 105317; equity JUMP 3341795; assets DROP 3681651; debt DROP 339856; FTE DROP 46.4; kapitaalsubsidies DROP 452828; destin691 empty; cash JUMP 425878; geldbeleggingen JUMP 1010540; capex 31291; leftover city_tongeren_borgloon after De Hoeksteen@2405; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_mereltjes_bruto_jr2025_statutory,{EID},2025,3028501,3028501,3028501,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -2.09% (primary L5 envelope; omzet 70 empty + 73 empty so bruto is envelope),{SRC_PDF},strong,tick2406; PDF p5 native; YE2024 3092998; omzet70 empty; 73 empty; 76A 117472 JUMP",
    f"bud_mereltjes_pnl_jr2025_statutory,{EID},2025,105317,105317,105317,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +224.42% vs YE2024 32463,{SRC_PDF},strong,tick2406; PDF p5 native; YE2024 32463; bedrijfswinst 9901 74712 PROFIT FLIP; destin691 empty",
    f"bud_mereltjes_bedrijfswinst_jr2025_statutory,{EID},2025,74712,74712,74712,NBB VKT-VZW code 9901 bedrijfswinst YE2025 PROFIT FLIP vs YE2024 -22080,{SRC_PDF},strong,tick2406; PDF p5 native; YE2024 -22080; 62 2794513; 630 154020; 76A 117472",
    f"bud_mereltjes_equity_jr2025_statutory,{EID},2025,3341795,3341795,3341795,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.16%,{SRC_PDF},strong,tick2406; PDF p4 native; YE2024 3271088; kapitaalsubsidies 452828; overgedragen 14 1353438; bestemde 13 955533; fondsen 10 579996",
    f"bud_mereltjes_assets_jr2025_statutory,{EID},2025,3681651,3681651,3681651,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -5.60%,{SRC_PDF},strong,tick2406; PDF p3 native; YE2024 3900196; gebouwen 22 1983174 was 2235870; aanbouw 27 60854 FLAT",
    f"bud_mereltjes_debt_jr2025_statutory,{EID},2025,339856,339856,339856,NBB VKT-VZW code 17/49 schulden YE2025 DROP -45.98%,{SRC_PDF},strong,tick2406; PDF p4 native; YE2024 629109; LT 17 empty was 48406; ST 42/48 339633",
    f"bud_mereltjes_cash_jr2025_statutory,{EID},2025,425878,425878,425878,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +84.53%,{SRC_PDF},strong,tick2406; PDF p3 native; YE2024 230795; geldbeleggingen 50/53 1010540 JUMP +1.05%",
    f"bud_mereltjes_fte_jr2025_statutory,{EID},2025,46.4,46.4,46.4,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 DROP -1.69%,{SRC_PDF},strong,tick2406; PDF p8 native; YE2024 47.2; personeel 62 2794513; year-end 105 39.1",
    f"bud_mereltjes_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2406; PDF p6 native; YE2024 empty; 9905 105317 fully to overgedragen 14",
    f"bud_mereltjes_capex_jr2025_statutory,{EID},2025,31291,31291,31291,NBB VKT-VZW code 8169 aanschaffingen materiële vaste activa YE2025,{SRC_PDF},strong,tick2406; PDF p7 native; overdrachten 8179 262147; gebouwen 22 1983174; machines 23 41407",
])
print("entities+budgets ok")

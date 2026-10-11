#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2407_stamp.txt").read_text().strip().splitlines()
EID = "vzw_3wplus_kinderopvang"
SRC_PDF = "src_3wplus_jr2025_nbb_pdf_2407"

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
    f'{EID},3Wplus Kinderopvang VZW Asse,ASBL 3Wplus Kinderopvang Asse,3Wplus Kinderopvang VZW (leftover city_asse CIK Halle-Vilvoorde),parastatal,city_asse,nl,https://3wplus.be/kinderopvang,kinderopvang@3wplus.be,"Z. 5 Mollem 250, 1730 Asse",tick2407 YE2025 Strong official native NBB PDF deposit 2026-00273048 + Strong KBO 0893.870.539 Actief 54 VE RSZ2025 88.919 Kinderopvang Vlaamse Gemeenschap since 01.04.2014; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 7160626 CIK envelope; pnl JUMP 551218; equity JUMP 1682311; assets JUMP 4301389; debt JUMP 2619078; FTE JUMP 125.2; kapitaalsubsidies JUMP 85875; destin691 JUMP 75000; cash JUMP 871472; geldbeleggingen empty; gebouwen JUMP 602648; aanbouw JUMP 338536; capex 1242169; leftover city_asse after De Mereltjes@2406; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_3wplus_bruto_jr2025_statutory,{EID},2025,7160626,7160626,7160626,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.99% (primary L5 envelope; omzet 70 empty + 73 empty so bruto is envelope),{SRC_PDF},strong,tick2407; PDF p6 native; YE2024 6952580; omzet70 empty; 73 empty; 76A empty",
    f"bud_3wplus_pnl_jr2025_statutory,{EID},2025,551218,551218,551218,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +634.41% vs YE2024 75056,{SRC_PDF},strong,tick2407; PDF p6 native; YE2024 75056; bedrijfswinst 9901 544758 JUMP; destin691 75000",
    f"bud_3wplus_bedrijfswinst_jr2025_statutory,{EID},2025,544758,544758,544758,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +706.92% vs YE2024 67511,{SRC_PDF},strong,tick2407; PDF p6 native; YE2024 67511; 62 6491189; 630 88591; 76A empty",
    f"bud_3wplus_equity_jr2025_statutory,{EID},2025,1682311,1682311,1682311,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +56.69%,{SRC_PDF},strong,tick2407; PDF p5 native; YE2024 1073649; kapitaalsubsidies 85875; overgedragen 14 1346436; bestemde 13 250000; fondsen 10 empty",
    f"bud_3wplus_assets_jr2025_statutory,{EID},2025,4301389,4301389,4301389,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +67.52%,{SRC_PDF},strong,tick2407; PDF p4 native; YE2024 2567712; gebouwen 22 602648 was 0; aanbouw 27 338536 JUMP",
    f"bud_3wplus_debt_jr2025_statutory,{EID},2025,2619078,2619078,2619078,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +80.20%,{SRC_PDF},strong,tick2407; PDF p5 native; YE2024 1453396; LT 17 668719 was 0; ST 42/48 1923474",
    f"bud_3wplus_cash_jr2025_statutory,{EID},2025,871472,871472,871472,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +23.15%,{SRC_PDF},strong,tick2407; PDF p4 native; YE2024 707639; geldbeleggingen 50/53 empty",
    f"bud_3wplus_fte_jr2025_statutory,{EID},2025,125.2,125.2,125.2,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +17.89%,{SRC_PDF},strong,tick2407; PDF p13 native; YE2024 106.2; personeel 62 6491189",
    f"bud_3wplus_destin_jr2025_statutory,{EID},2025,75000,75000,75000,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP sociaal passief,{SRC_PDF},strong,tick2407; PDF p7 native; YE2024 0; post 13 250000 was 175000",
    f"bud_3wplus_capex_jr2025_statutory,{EID},2025,1242169,1242169,1242169,NBB VKT-VZW code 8169 aanschaffingen materiële vaste activa YE2025,{SRC_PDF},strong,tick2407; PDF p9 native; immaterieel 8029 41999; gebouwen 22 602648; aanbouw 27 338536",
])
print("entities+budgets ok")

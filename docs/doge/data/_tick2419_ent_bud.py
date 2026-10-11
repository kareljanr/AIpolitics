#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2419_stamp.txt").read_text().strip().splitlines()
EID = "vzw_pagadder"
SRC_PDF = "src_pagadder_jr2025_nbb_pdf_2419"

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
    f'{EID},Kinderopvang De Pagadder VZW,ASBL Accueil extra-scolaire De Pagadder,De Pagadder VZW (leftover city_kortrijk CIK),parastatal,city_kortrijk,nl,https://de-pagadder.be/,boekhouding@de-ruyschaert.be,"Kloosterstraat 18, 8510 Marke",tick2419 YE2025 Strong official native NBB PDF deposit 2026-00133513 + Strong KBO 0888.028.268 Actief 2 VE 2.163.753.759 Kloosterstraat + 2.278.022.927 Marktstraat RSZ2025 88.911; opbr 70+73+76A JUMP 1607724 VZW envelope; omzet70 JUMP 297790 commercial-only vs large 73; 73 JUMP 1307284; 76A JUMP 2650; bruto9900 DROP 1330335; pnl DROP 82665; 9901 DROP 72984; equity JUMP 947907; assets JUMP 1193085; debt JUMP 245179; FTE JUMP 21.3; kapitaalsubsidies empty; destin691 empty; cash JUMP 167197; geldbeleggingen JUMP 786842; gebouwen DROP 16904; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; NOT Kloosterstraat 6 Drongen; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_pagadder_opbr_jr2025_statutory,{EID},2025,1607724,1607724,1607724,NBB VKT-VZW codes 70+73+76A bedrijfsopbrengsten YE2025 JUMP +1.32% (primary L5 envelope; omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2419; PDF p5 native; YE2024 1586776; omzet70 297790; 73 1307284; 76A 2650",
    f"bud_pagadder_73_jr2025_statutory,{EID},2025,1307284,1307284,1307284,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +0.33% (Kind en Gezin CIK; jaarverslag voornamelijk Kind en Gezin),{SRC_PDF},strong,tick2419; PDF p5 native; YE2024 1302994; envelope is 70+73+76A",
    f"bud_pagadder_omzet_jr2025_statutory,{EID},2025,297790,297790,297790,NBB VKT-VZW code 70 omzet YE2025 JUMP +5.15% (ouderbijdragen; commercial-only vs large 73),{SRC_PDF},strong,tick2419; PDF p5 native; YE2024 283210; envelope is 70+73+76A",
    f"bud_pagadder_bruto_jr2025_statutory,{EID},2025,1330335,1330335,1330335,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -5.82%,{SRC_PDF},strong,tick2419; PDF p5 native; YE2024 1412537; 60/61 current empty (YE2024 212575); envelope is 70+73+76A",
    f"bud_pagadder_pnl_jr2025_statutory,{EID},2025,82665,82665,82665,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -64.88%,{SRC_PDF},strong,tick2419; PDF p5 native; YE2024 235343; bedrijfswinst 9901 72984 DROP; destin691 empty",
    f"bud_pagadder_bedrijfswinst_jr2025_statutory,{EID},2025,72984,72984,72984,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -66.84%,{SRC_PDF},strong,tick2419; PDF p5 native; YE2024 220104; 62 1247312 JUMP +5.53%",
    f"bud_pagadder_equity_jr2025_statutory,{EID},2025,947907,947907,947907,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +9.55%,{SRC_PDF},strong,tick2419; PDF p4 native; YE2024 865241; kapitaalsubsidies empty; overgedragen 14 947907; fondsen 10 empty; bestemde 13 empty",
    f"bud_pagadder_assets_jr2025_statutory,{EID},2025,1193085,1193085,1193085,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +14.15%,{SRC_PDF},strong,tick2419; PDF p3 native; YE2024 1045203; gebouwen 22 16904 DROP; 2 VE",
    f"bud_pagadder_debt_jr2025_statutory,{EID},2025,245179,245179,245179,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +36.24%,{SRC_PDF},strong,tick2419; PDF p4 native; YE2024 179961; 42/48 237529 JUMP; 44 77077 JUMP was 21092; 45 131651",
    f"bud_pagadder_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (9905 82665 fully to overgedragen 14),{SRC_PDF},strong,tick2419; PDF p6 native; 9905 82665 to overgedragen 14 947907; destin691 empty",
])
print("entities+budgets ok")

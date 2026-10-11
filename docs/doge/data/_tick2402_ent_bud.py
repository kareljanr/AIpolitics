#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2402_stamp.txt").read_text().strip().splitlines()
EID = "vzw_cfr_zelzate"
SRC_PDF = "src_cfrzelzate_jr2025_nbb_pdf_2402"

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
    f'{EID},Centrum voor Functionele Revalidatie VZW / C.F.R. Zelzate,Centre de revalidation fonctionnelle ASBL Zelzate,CFR Zelzate VZW (leftover city_zelzate ambulante revalidatie),parastatal,city_zelzate,nl,https://www.revalidatiecentrum.be/,info@revalidatiecentrum.be,"Stationsstraat 40, 9060 Zelzate",tick2402 YE2025 Strong official native NBB PDF deposit 2026-00243990 + Strong KBO 0419.645.952 Actief 1 VE RSZ2025 86.959; omzet70 empty VKT; 73 empty VKT; bruto9900 DROP 1419621 CAR envelope; pnl LOSS FLIP -127569; equity JUMP 1259125; assets JUMP 2709376; debt JUMP 1450251; FTE 16.7; kapitaalsubsidies JUMP 1005973; destin691 empty; cash JUMP 441005; capex 1630690 gebouwen JUMP 1874287; leftover city_zelzate after VERBINT@2401; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT WZC Zilverbos 0644.984.078; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_cfrzelzate_bruto_jr2025_statutory,{EID},2025,1419621,1419621,1419621,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -2.94% (primary L5 envelope; omzet 70 empty so bruto is envelope),{SRC_PDF},strong,tick2402; PDF p5 native; YE2024 1462566; omzet70 empty; 73 empty; 76A empty",
    f"bud_cfrzelzate_pnl_jr2025_statutory,{EID},2025,-127569,-127569,-127569,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 LOSS FLIP (was +9867),{SRC_PDF},strong,tick2402; PDF p5 native; YE2024 9867; bedrijfswinst 9901 -129899 LOSS FLIP; destin691 empty",
    f"bud_cfrzelzate_bedrijfswinst_jr2025_statutory,{EID},2025,-129899,-129899,-129899,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 LOSS FLIP (was +10167),{SRC_PDF},strong,tick2402; PDF p5 native; YE2024 10167; 640/8 43668 JUMP; 630 35559 JUMP",
    f"bud_cfrzelzate_equity_jr2025_statutory,{EID},2025,1259125,1259125,1259125,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +90.05% (kapitaalsubsidies JUMP),{SRC_PDF},strong,tick2402; PDF p4 native; YE2024 662527; kapitaalsubsidies 1005973 JUMP; overgedragen 14 234266 DROP",
    f"bud_cfrzelzate_assets_jr2025_statutory,{EID},2025,2709376,2709376,2709376,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +140.29% (nieuw gebouw Stationsstraat),{SRC_PDF},strong,tick2402; PDF p3 native; YE2024 1127549; gebouwen 22 1874287 JUMP; aanbouw 27 empty",
    f"bud_cfrzelzate_debt_jr2025_statutory,{EID},2025,1450251,1450251,1450251,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +211.87% (nieuw bouwkrediet),{SRC_PDF},strong,tick2402; PDF p4 native; YE2024 465022; LT 17 794980; ST 42/48 651021; 174/0 140000 nieuw",
    f"bud_cfrzelzate_cash_jr2025_statutory,{EID},2025,441005,441005,441005,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +31.50%,{SRC_PDF},strong,tick2402; PDF p3 native; YE2024 335361; geldbeleggingen 50/53 empty",
    f"bud_cfrzelzate_fte_jr2025_statutory,{EID},2025,16.7,16.7,16.7,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +0.60%,{SRC_PDF},strong,tick2402; PDF p12 native; YE2024 16.6; personeel 62 1470293; 9086 not filed VKT",
    f"bud_cfrzelzate_kapitaalsubsidies_jr2025_statutory,{EID},2025,1005973,1005973,1005973,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 JUMP +256.97% (nieuw gebouw),{SRC_PDF},strong,tick2402; PDF p4 native; YE2024 281806; capex 8169 1630690",
    f"bud_cfrzelzate_capex_jr2025_statutory,{EID},2025,1630690,1630690,1630690,NBB VKT-VZW code 8169 aanschaffingen materiele VA YE2025 (nieuw gebouw Stationsstraat),{SRC_PDF},strong,tick2402; PDF p8 native; overdrachten 8179 612598; hypotheek 91621 248000 on 91611 1874287",
])
print("entities+budgets ok")

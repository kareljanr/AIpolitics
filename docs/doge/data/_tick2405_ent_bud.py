#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2405_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kinderopvang_hoeksteen"
SRC_PDF = "src_hoeksteen_jr2025_nbb_pdf_2405"

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
    f'{EID},Kinderopvang De Hoeksteen VZW / KoDH Diksmuide,ASBL Kinderopvang De Hoeksteen Dixmude,Kinderopvang De Hoeksteen VZW (leftover city_diksmuide CIK groepsopvang),parastatal,city_diksmuide,nl,https://publiek.departementzorg.be/Cobrha/Companies/Company/0765439866,gerdy.desmedt@de-hoeksteen.be,"Beerststraat 36, 8600 Diksmuide",tick2405 YE2025 Strong official native NBB PDF deposit 2026-00224895 + Strong KBO 0765.439.866 Actief 9 VE RSZ2025 88.911 Kinderopvang Vlaamse Gemeenschap since 16.08.2022; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 1870177 CIK envelope; pnl LOSS FLIP -7060; equity DROP 8031; assets JUMP 536744; debt JUMP 528713; FTE JUMP 31; kapitaalsubsidies empty; destin691 empty; cash JUMP 27702; geldbeleggingen DROP 142106; capex 59167; leftover city_diksmuide after Ter Eecken@2404; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT Heuvelheem 0413.210.201; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_hoeksteen_bruto_jr2025_statutory,{EID},2025,1870177,1870177,1870177,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +49.59% (primary L5 envelope; omzet 70 empty + 73 empty so bruto is envelope),{SRC_PDF},strong,tick2405; PDF p6 native; YE2024 1250221; omzet70 empty; 73 empty; 76A empty",
    f"bud_hoeksteen_pnl_jr2025_statutory,{EID},2025,-7060,-7060,-7060,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 LOSS FLIP vs YE2024 +100566,{SRC_PDF},strong,tick2405; PDF p6 native; YE2024 100566; bedrijfswinst 9901 -9026 LOSS FLIP; destin691 empty",
    f"bud_hoeksteen_bedrijfswinst_jr2025_statutory,{EID},2025,-9026,-9026,-9026,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 LOSS FLIP vs YE2024 +102884,{SRC_PDF},strong,tick2405; PDF p6 native; YE2024 102884; 62 1855310; 630 22310; 66A 151",
    f"bud_hoeksteen_equity_jr2025_statutory,{EID},2025,8031,8031,8031,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -46.78%,{SRC_PDF},strong,tick2405; PDF p5 native; YE2024 15091; kapitaalsubsidies empty; overgedragen 14 -4041; bestemde 13 12073",
    f"bud_hoeksteen_assets_jr2025_statutory,{EID},2025,536744,536744,536744,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +40.10%,{SRC_PDF},strong,tick2405; PDF p4 native; YE2024 383113; gebouwen 22 empty; aanbouw 27 empty; 41 other recv 157607 was 105864",
    f"bud_hoeksteen_debt_jr2025_statutory,{EID},2025,528713,528713,528713,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +43.66%,{SRC_PDF},strong,tick2405; PDF p5 native; YE2024 368022; LT 17 empty; ST 42/48 520149",
    f"bud_hoeksteen_cash_jr2025_statutory,{EID},2025,27702,27702,27702,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +190.44%,{SRC_PDF},strong,tick2405; PDF p4 native; YE2024 9538; geldbeleggingen 50/53 142106 DROP -3.68%",
    f"bud_hoeksteen_fte_jr2025_statutory,{EID},2025,31,31,31,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +58.16%,{SRC_PDF},strong,tick2405; PDF p11 native; YE2024 19.6; personeel 62 1855310; year-end 105 36.6",
    f"bud_hoeksteen_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (was 12073),{SRC_PDF},strong,tick2405; PDF p7 native; YE2024 12073; 80pct nettowinst rule unused because LOSS FLIP",
    f"bud_hoeksteen_capex_jr2025_statutory,{EID},2025,59167,59167,59167,NBB VKT-VZW code 8169 aanschaffingen materiële vaste activa YE2025,{SRC_PDF},strong,tick2405; PDF p8 native; machines 23 27649; meubilair 24 78335",
])
print("entities+budgets ok")

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2404_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_ter_eecken"
SRC_PDF = "src_tereecken_jr2025_nbb_pdf_2404"

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
    f'{EID},Ter Eecken VZW / CAR Ter Eecken Oudenaarde,ASBL Ter Eecken Audenarde,Ter Eecken VZW (leftover city_oudenaarde ambulante revalidatie),parastatal,city_oudenaarde,nl,https://www.cartereecken.be/,onthaal@cartereecken.be,"Vlaanderenstraat 2, 9700 Oudenaarde",tick2404 YE2025 Strong official native NBB PDF deposit 2026-00107832 + Strong KBO 0432.465.392 Actief 1 VE 2.156.368.495 RSZ2025 86.101 VAZG HCO 29586 RIZIV 96560332; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 3717716 CAR envelope; pnl LOSS WIDEN -207524; equity DROP 3873571; assets DROP 6549101; debt DROP 2675530; FTE 42.3 FLAT; kapitaalsubsidies DROP 3177969; destin691 empty; cash JUMP 177912; geldbeleggingen JUMP 180306; capex 125324; leftover city_oudenaarde after De Kade@2403; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT Heuvelheem 0413.210.201; NOT H.Hart Oudenaarde 0407.644.082; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_tereecken_bruto_jr2025_statutory,{EID},2025,3717716,3717716,3717716,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +7.97% (primary L5 envelope; omzet 70 empty + 73 empty so bruto is envelope),{SRC_PDF},strong,tick2404; PDF p6 native; YE2024 3443276; omzet70 empty; 73 empty; 76A 2800",
    f"bud_tereecken_pnl_jr2025_statutory,{EID},2025,-207524,-207524,-207524,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 LOSS WIDEN vs YE2024 -12939,{SRC_PDF},strong,tick2404; PDF p6 native; YE2024 -12939; bedrijfswinst 9901 -105938 LOSS WIDEN; destin691 empty",
    f"bud_tereecken_bedrijfswinst_jr2025_statutory,{EID},2025,-105938,-105938,-105938,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 LOSS WIDEN vs YE2024 -70103,{SRC_PDF},strong,tick2404; PDF p6 native; YE2024 -70103; 62 3515328; 630 192110; 66A 102348",
    f"bud_tereecken_equity_jr2025_statutory,{EID},2025,3873571,3873571,3873571,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -7.37%,{SRC_PDF},strong,tick2404; PDF p5 native; YE2024 4181780; kapitaalsubsidies 3177969 DROP; overgedragen 14 395602; bestemde 13 300000",
    f"bud_tereecken_assets_jr2025_statutory,{EID},2025,6549101,6549101,6549101,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -13.28%,{SRC_PDF},strong,tick2404; PDF p4 native; YE2024 7552374; gebouwen 22 5824359; aanbouw 27 empty; 41 other recv 696 was 1067374",
    f"bud_tereecken_debt_jr2025_statutory,{EID},2025,2675530,2675530,2675530,NBB VKT-VZW code 17/49 schulden YE2025 DROP -20.62%,{SRC_PDF},strong,tick2404; PDF p5 native; YE2024 3370594; LT 17 1958409; ST 42/48 710642",
    f"bud_tereecken_cash_jr2025_statutory,{EID},2025,177912,177912,177912,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +17.32%,{SRC_PDF},strong,tick2404; PDF p4 native; YE2024 151641; geldbeleggingen 50/53 180306 JUMP +76.51%",
    f"bud_tereecken_fte_jr2025_statutory,{EID},2025,42.3,42.3,42.3,NBB VKT-VZW code 100 gemiddeld personeelsbestand VTE YE2025 FLAT,{SRC_PDF},strong,tick2404; PDF p14 native; YE2024 42.3; personeel 62 3515328; year-end 105 42.4",
    f"bud_tereecken_kapitaalsubsidies_jr2025_statutory,{EID},2025,3177969,3177969,3177969,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -3.07%,{SRC_PDF},strong,tick2404; PDF p5 native; YE2024 3278654; destin691 empty",
    f"bud_tereecken_capex_jr2025_statutory,{EID},2025,125324,125324,125324,NBB VKT-VZW code 8169 aanschaffingen materiële vaste activa YE2025,{SRC_PDF},strong,tick2404; PDF p8 native; hypotheek 91621 400000; mandaat 91631 1445000; 91611 5824359",
])
print("entities+budgets ok")

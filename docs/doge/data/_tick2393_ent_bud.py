#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2393_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zonnebloem"
SRC_PDF = "src_zonnebloem_jr2025_nbb_pdf_2393"

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
    f'{EID},Zonnebloem VZW (VAPH MFC Kortrijk-Heule + inclusief KDV Madelief),Zonnebloem ASBL (MFC Courtrai-Heule + creche inclusive Madelief),Zonnebloem VZW (VAPH MFC leftover city_kortrijk + inclusive daycare Madelief),parastatal,city_kortrijk,nl,https://www.zonnebloemvzw.be/,algemeen@zonnebloemvzw.be,"Steenstraat 14, 8501 Kortrijk",tick2393 YE2025 Strong official native NBB PDF deposit 2026-00254348 + Strong KBO 0421.039.386 Actief 2 VE RSZ2025 87.201; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 4579601 VAPH envelope; pnl DROP 182958; equity JUMP 2994675; assets JUMP 3793570; debt DROP 798895; FTE 60.8; kapitaalsubsidies DROP 711539; destin691 empty; cash JUMP 983179; leftover city_kortrijk after Houtland@2392; AGB/FARO/Gandae YE2024; NOT CAR Houtland-Westkust 0408.436.019; NOT Leieborg; NOT CAR Overleie 0454.250.505; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_zonnebloem_bruto_jr2025_statutory,{EID},2025,4579601,4579601,4579601,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +6.05% (primary L5 envelope; omzet 70 empty so bruto is envelope; 73 empty),{SRC_PDF},strong,tick2393; PDF p6 native; YE2024 4318309; omzet70 empty; 73 empty",
    f"bud_zonnebloem_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 4579601),{SRC_PDF},strong,tick2393; PDF p6 native; YE2024 also empty",
    f"bud_zonnebloem_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2393; PDF p6 native; YE2024 also empty",
    f"bud_zonnebloem_pnl_jr2025_statutory,{EID},2025,182958,182958,182958,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -19.27%,{SRC_PDF},strong,tick2393; PDF p6 native; YE2024 226641; bedrijfswinst 9901 176097 DROP vs YE2024 212692; destin691 empty; 791 empty",
    f"bud_zonnebloem_equity_jr2025_statutory,{EID},2025,2994675,2994675,2994675,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.24%,{SRC_PDF},strong,tick2393; PDF p5 native; YE2024 2845599; kapitaalsubsidies 711539 DROP; overgedragen 14 1068808; fondsen 10 24167; bestemde 13 1190161",
    f"bud_zonnebloem_assets_jr2025_statutory,{EID},2025,3793570,3793570,3793570,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.60%,{SRC_PDF},strong,tick2393; PDF p4 native; YE2024 3697414; gebouwen 22 2380480; aanbouw 27 empty",
    f"bud_zonnebloem_debt_jr2025_statutory,{EID},2025,798895,798895,798895,NBB VKT-VZW code 17/49 schulden YE2025 DROP -6.21%,{SRC_PDF},strong,tick2393; PDF p5 native; YE2024 851815; ST 797548; LT empty",
    f"bud_zonnebloem_cash_jr2025_statutory,{EID},2025,983179,983179,983179,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +12.28%,{SRC_PDF},strong,tick2393; PDF p4 native; YE2024 875660; geldbeleggingen 50/53 empty",
    f"bud_zonnebloem_kapitaalsubsidies_jr2025_statutory,{EID},2025,711539,711539,711539,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -4.55%,{SRC_PDF},strong,tick2393; PDF p5 native; YE2024 745421",
    f"bud_zonnebloem_fte_jr2025_statutory,{EID},2025,60.8,60.8,60.8,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +2.53%,{SRC_PDF},strong,tick2393; PDF p11 native; YE2024 59.3; personeel 62 4162454; capex 8169 133836",
])
print("entities+budgets ok")

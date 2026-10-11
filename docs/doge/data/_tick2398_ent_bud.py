#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2398_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_halle_asse"
SRC_PDF = "src_halleasse_jr2025_nbb_pdf_2398"

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
    f'{EID},CAR "Land van Halle en Asse" VZW / CAR Halle Asse,Centre de revalidation ambulatoire Halle-Asse ASBL,CAR Halle Asse VZW (leftover city_halle + leftover city_asse ambulante revalidatie),parastatal,city_halle,nl,https://www.car-halle-asse.be/,halle@car-halle-asse.be,"Ziekenhuislaan 35, 1500 Halle",tick2398 YE2025 Strong official native NBB PDF deposit 2026-00364866 + Strong KBO 0425.788.230 Actief 1 VE RSZ2025 86.959; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 2343257 CAR envelope; pnl JUMP 255548; equity JUMP 2180458; assets JUMP 3012006; debt DROP 831548; FTE 28; kapitaalsubsidies DROP 725722; destin691 JUMP 505074 bouwfonds; cash JUMP 1268818; leftover city_halle@867 + leftover city_asse@911 after Waas@2397; AGB/FARO/Gandae YE2024; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_halleasse_bruto_jr2025_statutory,{EID},2025,2343257,2343257,2343257,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +9.06% (primary L5 envelope; omzet 70 empty so bruto is envelope),{SRC_PDF},strong,tick2398; PDF p5 native; YE2024 2148623; omzet70 empty; 73 empty; 76A 848",
    f"bud_halleasse_pnl_jr2025_statutory,{EID},2025,255548,255548,255548,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +16.60%,{SRC_PDF},strong,tick2398; PDF p5 native; YE2024 219167; bedrijfswinst 9901 256459 JUMP; destin691 505074 JUMP bouwfonds",
    f"bud_halleasse_bedrijfswinst_jr2025_statutory,{EID},2025,256459,256459,256459,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +13.44%,{SRC_PDF},strong,tick2398; PDF p5 native; YE2024 226071; 66A 1987",
    f"bud_halleasse_equity_jr2025_statutory,{EID},2025,2180458,2180458,2180458,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +11.66%,{SRC_PDF},strong,tick2398; PDF p4 native; YE2024 1952822; kapitaalsubsidies 725722 DROP; bestemde 13 1451192 JUMP",
    f"bud_halleasse_assets_jr2025_statutory,{EID},2025,3012006,3012006,3012006,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +7.52%,{SRC_PDF},strong,tick2398; PDF p3 native; YE2024 2801331; gebouwen 22 1540395; aanbouw 27 0",
    f"bud_halleasse_debt_jr2025_statutory,{EID},2025,831548,831548,831548,NBB VKT-VZW code 17/49 schulden YE2025 DROP -2.00%,{SRC_PDF},strong,tick2398; PDF p4 native; YE2024 848508; LT 17 440885; ST 42/48 376864",
    f"bud_halleasse_cash_jr2025_statutory,{EID},2025,1268818,1268818,1268818,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +12.26%,{SRC_PDF},strong,tick2398; PDF p3 native; YE2024 1130222; geldbeleggingen 50/53 empty",
    f"bud_halleasse_kapitaalsubsidies_jr2025_statutory,{EID},2025,725722,725722,725722,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -3.70%,{SRC_PDF},strong,tick2398; PDF p4 native; YE2024 753634",
    f"bud_halleasse_fte_jr2025_statutory,{EID},2025,28,28,28,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +6.46%,{SRC_PDF},strong,tick2398; PDF p10 native; YE2024 26.3; personeel 62 2007104; capex 35384",
    f"bud_halleasse_destin_jr2025_statutory,{EID},2025,505074,505074,505074,NBB VKT-VZW code 691 toevoeging bestemde fondsen (bouwfonds) YE2025 JUMP +130.45%,{SRC_PDF},strong,tick2398; PDF p6 native; YE2024 219167; 791 empty; 9906 505074",
])
print("entities+budgets ok")

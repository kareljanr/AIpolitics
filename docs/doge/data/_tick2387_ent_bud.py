#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2387_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_de_hert"
SRC_PDF = "src_dehert_jr2025_nbb_pdf_2387"

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
    f'{EID},CAR De Hert Aalst VZW (Centrum voor Ambulante Revalidatie),CAR De Hert Alost ASBL (centre de revalidation ambulatoire),CAR De Hert Aalst VZW (outpatient CAR children developmental),parastatal,city_aalst,nl,https://www.cardehert.be/,info@cardehert.be,"Rozendreef 250, 9300 Aalst",tick2387 YE2025 Strong official native NBB PDF deposit 2026-00174560 + Strong KBO 0409.371.672 Actief 1 VE 2.153.754.445 RSZ2025 86.959 VAZG 9.65.105.45 VAPH R/105; omzet70 JUMP 1869719 CAR envelope; 73 JUMP 634363; bruto JUMP 2409407; pnl JUMP 31450; equity DROP 2657601; assets JUMP 3220530; debt JUMP 562928; FTE 27 JUMP; kapitaalsubsidies DROP 1066108; destin691 empty; cash JUMP 924004; leftover city_aalst after De Klinker@2386; AGB/FARO/Gandae YE2024; NOT CGG Kohesi 0472.466.907; NOT REVA Kohesi 0410.121.641; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_dehert_omzet_jr2025_statutory,{EID},2025,1869719,1869719,1869719,NBB VKT-VZW code 70 omzet YE2025 JUMP +2.57% (primary L5 envelope; CAR Departement Zorg/VAPH; not commercial-only),{SRC_PDF},strong,tick2387; PDF p5 native; YE2024 1822944; 73 634363; bruto 2409407",
    f"bud_dehert_73_jr2025_statutory,{EID},2025,634363,634363,634363,NBB VKT-VZW code 73 lidgeld schenkingen subsidies YE2025 JUMP +17.80%,{SRC_PDF},strong,tick2387; PDF p5 native; YE2024 538499",
    f"bud_dehert_bruto_jr2025_statutory,{EID},2025,2409407,2409407,2409407,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +7.00% (~1.29x omzet),{SRC_PDF},strong,tick2387; PDF p5 native; YE2024 2251797; 76A 17014",
    f"bud_dehert_pnl_jr2025_statutory,{EID},2025,31450,31450,31450,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +970%,{SRC_PDF},strong,tick2387; PDF p5 native; YE2024 2939; bedrijfswinst 9901 31824 JUMP vs YE2024 3683; destin691 empty",
    f"bud_dehert_equity_jr2025_statutory,{EID},2025,2657601,2657601,2657601,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -0.64%,{SRC_PDF},strong,tick2387; PDF p4 native; YE2024 2674611; kapitaalsubsidies 1066108; overgedragen 14 1358628; fondsen 10 232865; bestemde 13 empty",
    f"bud_dehert_assets_jr2025_statutory,{EID},2025,3220530,3220530,3220530,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +0.77%,{SRC_PDF},strong,tick2387; PDF p3 native; YE2024 3195892",
    f"bud_dehert_debt_jr2025_statutory,{EID},2025,562928,562928,562928,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +7.99%,{SRC_PDF},strong,tick2387; PDF p4 native; YE2024 521280; LT 114750; ST 438475; handel 8315; sociaal 391561",
    f"bud_dehert_cash_jr2025_statutory,{EID},2025,924004,924004,924004,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +36.54%,{SRC_PDF},strong,tick2387; PDF p3 native; YE2024 676724; geldbeleggingen 50/53 empty",
    f"bud_dehert_kapitaalsubsidies_jr2025_statutory,{EID},2025,1066108,1066108,1066108,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -4.35%,{SRC_PDF},strong,tick2387; PDF p4 native; YE2024 1114568",
    f"bud_dehert_fte_jr2025_statutory,{EID},2025,27,27,27,NBB VKT-VZW gemiddeld personeelseffectief VTE YE2025 27 JUMP +9.31%,{SRC_PDF},strong,tick2387; PDF p10 native code 9087; YE2024 24.7; personnel 62 2217469",
])
print("entities+budgets ok")

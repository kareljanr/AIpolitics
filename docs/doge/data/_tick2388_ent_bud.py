#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2388_stamp.txt").read_text().strip().splitlines()
EID = "vzw_reva_kohesi"
SRC_PDF = "src_revakohesi_jr2025_nbb_pdf_2388"

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
    f'{EID},REVA Kohesi VZW (CAR Hasselt/Genk/Beringen + Reval + KDV Maasmechelen),REVA Kohesi ASBL (CAR Hasselt/Genk/Beringen + Reval + creche Maasmechelen),REVA Kohesi VZW (outpatient CAR + Reval campuses + KDV leftover city_hasselt),parastatal,city_hasselt,nl,https://www.kohesi.be/,info@kohesi.be,"Ilgatlaan 11 bus 4, 3500 Hasselt",tick2388 YE2025 Strong official native NBB PDF deposit 2026-00244637 + Strong KBO 0410.121.641 Actief 8 VE RSZ2025 88.999; omzet70 DROP 5960431 CAR envelope; 73 DROP 1863434; 70/76A JUMP 8755588; pnl DROP 104069; equity JUMP 6474902; assets DROP 8501347; debt DROP 2026445; FTE 85.2 JUMP; kapitaalsubsidies DROP 1102703; destin691 DROP 53728; cash DROP 1533265; leftover city_hasselt after De Hert@2387; AGB/FARO/Gandae YE2024; NOT CGG Kohesi 0472.466.907; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_revakohesi_omzet_jr2025_statutory,{EID},2025,5960431,5960431,5960431,NBB VOL-VZW code 70 omzet YE2025 DROP -2.93% (primary L5 envelope; CAR/Reval Departement Zorg; not commercial-only),{SRC_PDF},strong,tick2388; PDF p7 native; YE2024 6140547; 73 1863434; 70/76A 8755588",
    f"bud_revakohesi_73_jr2025_statutory,{EID},2025,1863434,1863434,1863434,NBB VOL-VZW code 73 lidgeld schenkingen subsidies YE2025 DROP -0.84% (731 4642 + 733 1858791),{SRC_PDF},strong,tick2388; PDF p7+6.9 native; YE2024 1879253",
    f"bud_revakohesi_opbr_jr2025_statutory,{EID},2025,8755588,8755588,8755588,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +0.33% (74 788410; 76A 143314),{SRC_PDF},strong,tick2388; PDF p7 native; YE2024 8726460; no 9900 on VOL-VZW",
    f"bud_revakohesi_pnl_jr2025_statutory,{EID},2025,104069,104069,104069,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -70.81%,{SRC_PDF},strong,tick2388; PDF p8 native; YE2024 356497; bedrijfswinst 9901 107392 DROP vs YE2024 348267; destin691 53728",
    f"bud_revakohesi_equity_jr2025_statutory,{EID},2025,6474902,6474902,6474902,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +0.40%,{SRC_PDF},strong,tick2388; PDF p6 native; YE2024 6448986; kapitaalsubsidies 1102703; overgedragen 14 3542964; fondsen 10 78086; bestemde 13 1751148",
    f"bud_revakohesi_assets_jr2025_statutory,{EID},2025,8501347,8501347,8501347,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -2.38%,{SRC_PDF},strong,tick2388; PDF p5 native; YE2024 8708551",
    f"bud_revakohesi_debt_jr2025_statutory,{EID},2025,2026445,2026445,2026445,NBB VOL-VZW code 17/49 schulden YE2025 DROP -10.32%,{SRC_PDF},strong,tick2388; PDF p6 native; YE2024 2259565; LT 488558; ST 1500150; handel 207580; sociaal 960593",
    f"bud_revakohesi_cash_jr2025_statutory,{EID},2025,1533265,1533265,1533265,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -21.96%,{SRC_PDF},strong,tick2388; PDF p5 native; YE2024 1964824; geldbeleggingen 50/53 empty was 500000",
    f"bud_revakohesi_kapitaalsubsidies_jr2025_statutory,{EID},2025,1102703,1102703,1102703,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -6.62%,{SRC_PDF},strong,tick2388; PDF p6 native; YE2024 1180857",
    f"bud_revakohesi_fte_jr2025_statutory,{EID},2025,85.2,85.2,85.2,NBB VOL-VZW gemiddeld personeelseffectief VTE YE2025 85.2 JUMP +4.03%,{SRC_PDF},strong,tick2388; PDF 6.9 native code 9087; YE2024 81.9; personnel 62 7004590; koppen 9086 126",
])
print("entities+budgets ok")

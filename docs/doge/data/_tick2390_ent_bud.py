#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2390_stamp.txt").read_text().strip().splitlines()
EID = "vzw_ldsst"
SRC_PDF = "src_ldsst_jr2025_nbb_pdf_2390"

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
    f'{EID},Limburgse Dienst voor Stem- en Spraaktherapie VZW (LDSST / Kohesi-family logopedie Hasselt),Service limbourgeois de therapie vocale et de la parole ASBL (LDSST),LDSST VZW (speech-voice therapy leftover city_hasselt),parastatal,city_hasselt,nl,https://www.kohesi.be/,info@kohesi.be,"Ilgatlaan 11 bus 7, 3500 Hasselt",tick2390 EVERY-10 YE2025 Strong official native NBB PDF deposit 2026-00243690 + Strong KBO 0410.121.344 Actief 1 VE RSZ2025 86.996; omzet70 DROP 35784 commercial-only; 73 DROP 179055; bruto JUMP 591161 MIC envelope; pnl PROFIT FLIP 98656; equity JUMP 162403; assets JUMP 437505; debt JUMP 275102; FTE 6.9 JUMP; kapitaalsubsidies empty; destin691 JUMP 59104; cash DROP 35597; leftover city_hasselt after BW Kohesi@2389; AGB/FARO/Gandae YE2024; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_ldsst_bruto_jr2025_statutory,{EID},2025,591161,591161,591161,NBB MIC-VZW code 9900 brutomarge YE2025 JUMP +30.49% (primary L5 envelope; MIC; omzet 35784 commercial-only vs large 73 179055; 70/76A not published),{SRC_PDF},strong,tick2390; PDF p6 native; YE2024 453044; omzet 35784; 73 179055",
    f"bud_ldsst_omzet_jr2025_statutory,{EID},2025,35784,35784,35784,NBB MIC-VZW code 70 omzet YE2025 DROP -3.30% (commercial-only logopedie fees; not envelope),{SRC_PDF},strong,tick2390; PDF p6 native; YE2024 37007",
    f"bud_ldsst_73_jr2025_statutory,{EID},2025,179055,179055,179055,NBB MIC-VZW code 73 lidgeld schenkingen subsidies YE2025 DROP -4.40%,{SRC_PDF},strong,tick2390; PDF p6 native; YE2024 187301",
    f"bud_ldsst_pnl_jr2025_statutory,{EID},2025,98656,98656,98656,NBB MIC-VZW code 9904 winst van het boekjaar YE2025 PROFIT FLIP,{SRC_PDF},strong,tick2390; PDF p6 native; YE2024 -7767; bedrijfswinst 9901 98983 PROFIT FLIP vs YE2024 -7440; destin691 59104; 791 empty",
    f"bud_ldsst_equity_jr2025_statutory,{EID},2025,162403,162403,162403,NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +154.76%,{SRC_PDF},strong,tick2390; PDF p5 native; YE2024 63747; kapitaalsubsidies empty; overgedragen 14 39552; bestemde 13 122851",
    f"bud_ldsst_assets_jr2025_statutory,{EID},2025,437505,437505,437505,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +94.27%,{SRC_PDF},strong,tick2390; PDF p4 native; YE2024 225201",
    f"bud_ldsst_debt_jr2025_statutory,{EID},2025,275102,275102,275102,NBB MIC-VZW code 17/49 schulden YE2025 JUMP +70.39%,{SRC_PDF},strong,tick2390; PDF p5 native; YE2024 161454; LT empty; ST 275102; handel 5638; sociaal 60826; overige 205439 JUMP",
    f"bud_ldsst_cash_jr2025_statutory,{EID},2025,35597,35597,35597,NBB MIC-VZW code 54/58 liquide middelen YE2025 DROP -10.63%,{SRC_PDF},strong,tick2390; PDF p4 native; YE2024 39831; geldbeleggingen 50/53 empty; overige vorderingen 41 400657 JUMP",
    f"bud_ldsst_personnel_jr2025_statutory,{EID},2025,491403,491403,491403,NBB MIC-VZW code 62 bezoldigingen YE2025 JUMP +6.71%,{SRC_PDF},strong,tick2390; PDF p6 native; YE2024 460484; sociale balans 102 491403 vs 460463",
    f"bud_ldsst_fte_jr2025_statutory,{EID},2025,6.9,6.9,6.9,NBB MIC-VZW gemiddeld personeelseffectief VTE YE2025 6.9 JUMP +2.99%,{SRC_PDF},strong,tick2390; PDF 6.4 native code 100; YE2024 6.7; jaar einde 105 9 koppen / 6.5 VTE all part-time",
])
print("entities+budgets ok")

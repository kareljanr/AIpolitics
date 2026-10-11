#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2386_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_deklinker"
SRC_PDF = "src_deklinker_jr2025_nbb_pdf_2386"

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
    f'{EID},CAR De Klinker Ieper VZW (Centrum voor Ambulante Revalidatie),CAR De Klinker Ypres ASBL (centre de revalidation ambulatoire),CAR De Klinker Ieper VZW (outpatient CAR children language/speech/motor/development/hearing),parastatal,city_ieper,nl,https://www.cardeklinker.be/,info@cardeklinker.be,"Cartonstraat 53, 8900 Ieper",tick2386 YE2025 Strong official native NBB PDF deposit 2026-00241698 + Strong KBO 0430.535.290 Actief 1 VE 2.154.433.940 RSZ2025 86.959 RIZIV 9.53.579.28 VAPH 579; omzet70 empty VKT; 73 empty VKT; bruto JUMP 1615845 VKT envelope; pnl JUMP 68250; equity JUMP 421965; assets JUMP 835288; debt JUMP 413323; FTE 18.6 JUMP; kapitaalsubsidies DROP 127157; destin691 JUMP 179028; cash JUMP 268878; leftover city_ieper after Ascendere@2385; AGB/FARO/Gandae YE2024; NOT school Rotselaar 0464.016.326; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_deklinker_bruto_jr2025_statutory,{EID},2025,1615845,1615845,1615845,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +9.04% (primary L5 envelope; VKT omzet 70 empty and 73 empty; CAR RIZIV/Departement Zorg/VAPH),{SRC_PDF},strong,tick2386; PDF p6 native; YE2024 1481932; omzet70 empty; 73 empty",
    f"bud_deklinker_pnl_jr2025_statutory,{EID},2025,68250,68250,68250,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +6.76%,{SRC_PDF},strong,tick2386; PDF p6 native; YE2024 63931; bedrijfswinst 9901 68351 JUMP vs YE2024 61257; destin691 179028",
    f"bud_deklinker_equity_jr2025_statutory,{EID},2025,421965,421965,421965,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +16.12%,{SRC_PDF},strong,tick2386; PDF p5 native; YE2024 363391; kapitaalsubsidies 127157; overgedragen 14 empty; fondsen 10 115780; bestemde 13 179028",
    f"bud_deklinker_assets_jr2025_statutory,{EID},2025,835288,835288,835288,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +11.57%,{SRC_PDF},strong,tick2386; PDF p4 native; YE2024 748693",
    f"bud_deklinker_debt_jr2025_statutory,{EID},2025,413323,413323,413323,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +7.27%,{SRC_PDF},strong,tick2386; PDF p5 native; YE2024 385302; LT 61000; ST 316539; handel 49711; sociaal 209284",
    f"bud_deklinker_cash_jr2025_statutory,{EID},2025,268878,268878,268878,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +22.95%,{SRC_PDF},strong,tick2386; PDF p4 native; YE2024 218697; geldbeleggingen 50/53 empty",
    f"bud_deklinker_kapitaalsubsidies_jr2025_statutory,{EID},2025,127157,127157,127157,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -7.07%,{SRC_PDF},strong,tick2386; PDF p5 native; YE2024 136832",
    f"bud_deklinker_fte_jr2025_statutory,{EID},2025,18.6,18.6,18.6,NBB VKT-VZW gemiddeld personeelseffectief VTE YE2025 18.6 JUMP +12.05%,{SRC_PDF},strong,tick2386; PDF p13 native code 9087; YE2024 16.6; personnel 62 1517396; PC 330",
    f"bud_deklinker_destin691_jr2025_statutory,{EID},2025,179028,179028,179028,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was empty),{SRC_PDF},strong,tick2386; PDF p7 native; YE2024 empty; 14P 110779 + 9905 68250 allocated; overgedragen 14 emptied",
    f"bud_deklinker_personnel62_jr2025_statutory,{EID},2025,1517396,1517396,1517396,NBB VKT-VZW code 62 bezoldigingen sociale lasten pensioenen YE2025 JUMP +9.31%,{SRC_PDF},strong,tick2386; PDF p6 native; YE2024 1388158; FTE 18.6",
])
print("entities+budgets ok")

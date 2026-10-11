#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2389_stamp.txt").read_text().strip().splitlines()
EID = "vzw_bw_kohesi"
SRC_PDF = "src_bwkohesi_jr2025_nbb_pdf_2389"

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
    f'{EID},Beschut Wonen Kohesi VZW (IBW Heusden-Zolder + Beringen Harmoniestraat 9),Habitat protege Kohesi ASBL (IBW Heusden-Zolder + Beringen),Beschut Wonen Kohesi VZW (supported housing leftover city_heusden_zolder),parastatal,city_heusden_zolder,nl,https://www.kohesi.be/,info@kohesi.be,"Pastoor Paquaylaan 123 bus 1, 3550 Heusden-Zolder",tick2389 YE2025 Strong official native NBB PDF deposit 2026-00243983 + Strong KBO 0451.932.995 Actief 2 VE RSZ2025 87.205; omzet70 JUMP 1294776 IBW envelope; 73 DROP 487682; bruto DROP 1243451; pnl JUMP 18602; equity JUMP 615414; assets JUMP 1101290; debt JUMP 485876; FTE 15.2 JUMP; kapitaalsubsidies empty; destin691 empty; cash DROP 645903; leftover city_heusden_zolder + leftover city_beringen after REVA@2388; AGB/FARO/Gandae YE2024; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_bwkohesi_omzet_jr2025_statutory,{EID},2025,1294776,1294776,1294776,NBB VKT-VZW code 70 omzet YE2025 JUMP +3.04% (primary L5 envelope; IBW Departement Zorg; not commercial-only),{SRC_PDF},strong,tick2389; PDF p6 native; YE2024 1256608; 73 487682; bruto 1243451",
    f"bud_bwkohesi_73_jr2025_statutory,{EID},2025,487682,487682,487682,NBB VKT-VZW code 73 lidgeld schenkingen subsidies YE2025 DROP -2.74%,{SRC_PDF},strong,tick2389; PDF p6 native; YE2024 501440",
    f"bud_bwkohesi_bruto_jr2025_statutory,{EID},2025,1243451,1243451,1243451,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -2.05% (omzet present so envelope is 70 not 9900),{SRC_PDF},strong,tick2389; PDF p6 native; YE2024 1269419; 76A 0; no 70/76A total on VKT",
    f"bud_bwkohesi_pnl_jr2025_statutory,{EID},2025,18602,18602,18602,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +68.85%,{SRC_PDF},strong,tick2389; PDF p6 native; YE2024 11017; bedrijfswinst 9901 18146 JUMP vs YE2024 9962; destin691 empty; 791 4046",
    f"bud_bwkohesi_equity_jr2025_statutory,{EID},2025,615414,615414,615414,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +3.12%,{SRC_PDF},strong,tick2389; PDF p5 native; YE2024 596811; kapitaalsubsidies empty; overgedragen 14 289600; fondsen 10 21533; bestemde 13 304281",
    f"bud_bwkohesi_assets_jr2025_statutory,{EID},2025,1101290,1101290,1101290,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.83%,{SRC_PDF},strong,tick2389; PDF p4 native; YE2024 1070944",
    f"bud_bwkohesi_debt_jr2025_statutory,{EID},2025,485876,485876,485876,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +2.48%,{SRC_PDF},strong,tick2389; PDF p5 native; YE2024 474132; LT empty; ST 485857; handel 220312; sociaal 170174",
    f"bud_bwkohesi_cash_jr2025_statutory,{EID},2025,645903,645903,645903,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -12.01%,{SRC_PDF},strong,tick2389; PDF p4 native; YE2024 734043; geldbeleggingen 50/53 empty",
    f"bud_bwkohesi_personnel_jr2025_statutory,{EID},2025,1217122,1217122,1217122,NBB VKT-VZW code 62 bezoldigingen YE2025 DROP -2.90%,{SRC_PDF},strong,tick2389; PDF p6 native; YE2024 1253416; sociale balans 102 1217122",
    f"bud_bwkohesi_fte_jr2025_statutory,{EID},2025,15.2,15.2,15.2,NBB VKT-VZW gemiddeld personeelseffectief VTE YE2025 15.2 JUMP +0.66%,{SRC_PDF},strong,tick2389; PDF 6.4 native code 9087; YE2024 15.1; jaar einde 105 3+19=22 koppen / 15.7 VTE",
])
print("entities+budgets ok")

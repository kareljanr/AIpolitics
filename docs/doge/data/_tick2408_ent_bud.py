#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2408_stamp.txt").read_text().strip().splitlines()
EID = "vzw_eekhoorntje"
SRC_PDF = "src_eekhoorntje_jr2025_nbb_pdf_2408"

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
    f'{EID},Kinderopvang t Eekhoorntje VZW Leuven,ASBL Kinderopvang t Eekhoorntje Louvain,Kinderopvang t Eekhoorntje VZW (leftover city_leuven CIK),parastatal,city_leuven,nl,https://eekhoorntje.eu/,info@eekhoorntje.be,"Guldensporenlaan 65, 3010 Leuven",tick2408 YE2025 Strong official native NBB PDF deposit 2026-00131193 + Strong KBO 0414.453.680 Actief 2 VE first VE 2.150.803.269 RSZ2025 88.911 Kinderopvang Vlaamse Gemeenschap since 01.04.2014 slorpte Het Kinderhofje 0459.530.471 since 01.01.2025; omzet70 JUMP 433265 commercial vs empty 73; 73 empty VKT; bruto9900 JUMP 2138490 CIK envelope; pnl DROP 271456; equity JUMP 2983796; assets JUMP 3242913; debt JUMP 259117; FTE JUMP 30.4; kapitaalsubsidies DROP 66913; destin691 DROP 271456; cash JUMP 770104; geldbeleggingen DROP 500000; gebouwen JUMP 1707909; aanbouw 4931; capex 485850; leftover city_leuven after 3Wplus@2407; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_eekhoorntje_bruto_jr2025_statutory,{EID},2025,2138490,2138490,2138490,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +5.98% (primary L5 envelope; 73 empty so bruto is envelope vs commercial-only omzet 70 433265),{SRC_PDF},strong,tick2408; PDF p5 native; YE2024 2017762; omzet70 433265; 73 empty; 76A 53372",
    f"bud_eekhoorntje_omzet_jr2025_statutory,{EID},2025,433265,433265,433265,NBB VKT-VZW code 70 omzet YE2025 JUMP +3.43% (ouderbijdragen; commercial-only vs empty 73 / large bruto),{SRC_PDF},strong,tick2408; PDF p5 native; YE2024 418884; 73 empty",
    f"bud_eekhoorntje_pnl_jr2025_statutory,{EID},2025,271456,271456,271456,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -10.02% vs YE2024 301691,{SRC_PDF},strong,tick2408; PDF p5 native; YE2024 301691; bedrijfswinst 9901 246424 DROP; destin691 271456",
    f"bud_eekhoorntje_bedrijfswinst_jr2025_statutory,{EID},2025,246424,246424,246424,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -11.44% vs YE2024 278262,{SRC_PDF},strong,tick2408; PDF p5 native; YE2024 278262; 62 1857057; 630 100435; 76A 53372",
    f"bud_eekhoorntje_equity_jr2025_statutory,{EID},2025,2983796,2983796,2983796,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +21.42%,{SRC_PDF},strong,tick2408; PDF p4 native; YE2024 2457392; kapitaalsubsidies 66913; overgedragen 14 172243; bestemde 13 1704554; fondsen 10 1040087",
    f"bud_eekhoorntje_assets_jr2025_statutory,{EID},2025,3242913,3242913,3242913,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +15.10%,{SRC_PDF},strong,tick2408; PDF p3 native; YE2024 2817485; gebouwen 22 1707909; aanbouw 27 4931",
    f"bud_eekhoorntje_debt_jr2025_statutory,{EID},2025,259117,259117,259117,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +10.22%,{SRC_PDF},strong,tick2408; PDF p4 native; YE2024 235093; LT 17 empty; ST 42/48 258212",
    f"bud_eekhoorntje_cash_jr2025_statutory,{EID},2025,770104,770104,770104,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +245.42%,{SRC_PDF},strong,tick2408; PDF p3 native; YE2024 222947; geldbeleggingen 50/53 500000 DROP",
    f"bud_eekhoorntje_fte_jr2025_statutory,{EID},2025,30.4,30.4,30.4,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +6.29%,{SRC_PDF},strong,tick2408; PDF p10 native; YE2024 28.6; personeel 62 1857057",
    f"bud_eekhoorntje_destin_jr2025_statutory,{EID},2025,271456,271456,271456,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 DROP 100pct of 9905,{SRC_PDF},strong,tick2408; PDF p6 native; YE2024 301691; post 13 1704554 was 1433098",
])
print("entities+budgets ok")

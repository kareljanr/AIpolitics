#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP = "2026-08-25T00:04:21Z"
EID = "vzw_ascendere"
SRC_PDF = "src_ascendere_jr2025_nbb_pdf_2385"

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
    f'{EID},Ascendere VZW (CAR Klim Op Eeklo + De Springplank Lede + De Locomotief Ninove + De Schakel Wetteren),Ascendere ASBL (CAR Klim Op Eeklo + De Springplank Lede + De Locomotief Ninove + De Schakel Wetteren),Ascendere VZW (4 outpatient CAR campuses Eeklo/Lede/Ninove/Wetteren),parastatal,city_eeklo,nl,https://ascendere.be/,info@ascendere.be,"Melkerij 25, 9900 Eeklo",tick2385 YE2025 Strong official native NBB PDF deposit 2026-00209823 + Strong KBO 0409.470.553 Actief 4 VE RSZ2025 86.959 VAZG 9.53.608.96 VAPH REV.1003.2363; omzet JUMP 4338634 CAR envelope; bruto DROP 4821515; 73 DROP 865623; pnl DROP 27286; equity DROP 3529703; assets DROP 5657078; debt DROP 2127375; FTE 52.5 DROP; kapitaalsubsidies DROP 1098275; destin691 empty; cash JUMP 1688162; geldbeleggingen emptied; leftover city_eeklo after CAR Roeselare@2384; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_ascendere_omzet_jr2025_statutory,{EID},2025,4338634,4338634,4338634,NBB VKT-VZW code 70 omzet YE2025 JUMP +0.46% (primary L5 envelope; CAR RIZIV/Departement Zorg/VAPH not commercial-only),{SRC_PDF},strong,tick2385; PDF p6 native; YE2024 4318609; 73 865623; bruto 4821515 ~1.11x",
    f"bud_ascendere_bruto_jr2025_statutory,{EID},2025,4821515,4821515,4821515,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -0.02%,{SRC_PDF},strong,tick2385; PDF p6 native; YE2024 4822639; 76A empty",
    f"bud_ascendere_subs73_jr2025_statutory,{EID},2025,865623,865623,865623,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -4.42%,{SRC_PDF},strong,tick2385; PDF p6 native; YE2024 905659",
    f"bud_ascendere_pnl_jr2025_statutory,{EID},2025,27286,27286,27286,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -81.26%,{SRC_PDF},strong,tick2385; PDF p6 native; YE2024 145593; bedrijfswinst 9901 43210 DROP vs YE2024 165869; destin691 empty",
    f"bud_ascendere_equity_jr2025_statutory,{EID},2025,3529703,3529703,3529703,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -0.62%,{SRC_PDF},strong,tick2385; PDF p5 native; YE2024 3551681; kapitaalsubsidies 1098275; overgedragen 14 1426204; fondsen 10 1005224; bestemde 13 empty",
    f"bud_ascendere_assets_jr2025_statutory,{EID},2025,5657078,5657078,5657078,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -1.10%,{SRC_PDF},strong,tick2385; PDF p4 native; YE2024 5719819",
    f"bud_ascendere_debt_jr2025_statutory,{EID},2025,2127375,2127375,2127375,NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.88%,{SRC_PDF},strong,tick2385; PDF p5 native; YE2024 2168138; LT 1173275; ST 893908; handel 106489; sociaal 587255",
    f"bud_ascendere_cash_jr2025_statutory,{EID},2025,1688162,1688162,1688162,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +15.47%,{SRC_PDF},strong,tick2385; PDF p4 native; YE2024 1462037; geldbeleggingen 50/53 emptied vs 250000",
    f"bud_ascendere_kapitaalsubsidies_jr2025_statutory,{EID},2025,1098275,1098275,1098275,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -4.29%,{SRC_PDF},strong,tick2385; PDF p5 native; YE2024 1147539; geldbeleggingen emptied",
    f"bud_ascendere_fte_jr2025_statutory,{EID},2025,52.5,52.5,52.5,NBB VKT-VZW gemiddeld personeelseffectief VTE YE2025 52.5 DROP -3.49%,{SRC_PDF},strong,tick2385; PDF p13 native code 9087; YE2024 54.4; personnel 62 4483299; uitzend empty",
])
print("entities+budgets ok")

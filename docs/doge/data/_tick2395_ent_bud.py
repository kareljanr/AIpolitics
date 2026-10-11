#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2395_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_horizon"
SRC_PDF = "src_horizon_jr2025_nbb_pdf_2395"

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
    f'{EID},Horizon VZW / CAR Horizon Geraardsbergen,Horizon ASBL / CAR Horizon Grammont,CAR Horizon VZW (leftover city_geraardsbergen ambulante revalidatie),parastatal,city_geraardsbergen,nl,https://www.horizonvzw.be/,erwin.franceus@horizonvzw.be,"Oudenaardsestraat 215, 9500 Geraardsbergen",tick2395 YE2025 Strong official native NBB PDF deposit 2026-00268911 + Strong KBO 0418.529.759 Actief 1 VE RSZ2025 86.959; omzet70 DROP 3001208 CAR envelope; 73 JUMP 464125; bruto9900 DROP 2680880; pnl DROP 246289; equity JUMP 2542581; assets JUMP 2952629; debt DROP 410048; FTE 35; kapitaalsubsidies FLAT 131925; destin691 DROP 246289; cash DROP 958792; leftover city_geraardsbergen after ZWZ@2394; AGB/FARO/Gandae YE2024; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_horizon_omzet_jr2025_statutory,{EID},2025,3001208,3001208,3001208,NBB VKT-VZW code 70 omzet YE2025 DROP -4.24% (primary L5 envelope; CAR ambulante revalidatie not commercial-only),{SRC_PDF},strong,tick2395; PDF p5 native; YE2024 3134235; 73 464125; bruto9900 2680880; 76A empty",
    f"bud_horizon_73_jr2025_statutory,{EID},2025,464125,464125,464125,NBB VKT-VZW code 73 lidgeld schenkingen subsidies YE2025 JUMP +1.40%,{SRC_PDF},strong,tick2395; PDF p5 native; YE2024 457696",
    f"bud_horizon_bruto_jr2025_statutory,{EID},2025,2680880,2680880,2680880,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -3.72%,{SRC_PDF},strong,tick2395; PDF p5 native; YE2024 2784424; 76A empty",
    f"bud_horizon_pnl_jr2025_statutory,{EID},2025,246289,246289,246289,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -37.97%,{SRC_PDF},strong,tick2395; PDF p5 native; YE2024 397075; bedrijfswinst 9901 143692 DROP vs YE2024 316341; destin691 246289",
    f"bud_horizon_equity_jr2025_statutory,{EID},2025,2542581,2542581,2542581,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +10.73%,{SRC_PDF},strong,tick2395; PDF p4 native; YE2024 2296293; kapitaalsubsidies 131925 FLAT; bestemde 13 2410656",
    f"bud_horizon_assets_jr2025_statutory,{EID},2025,2952629,2952629,2952629,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +7.77%,{SRC_PDF},strong,tick2395; PDF p3 native; YE2024 2739676; gebouwen 22 96635; aanbouw 27 empty",
    f"bud_horizon_debt_jr2025_statutory,{EID},2025,410048,410048,410048,NBB VKT-VZW code 17/49 schulden YE2025 DROP -7.52%,{SRC_PDF},strong,tick2395; PDF p4 native; YE2024 443383; ST 42/48 384945",
    f"bud_horizon_cash_jr2025_statutory,{EID},2025,958792,958792,958792,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -26.59%,{SRC_PDF},strong,tick2395; PDF p3 native; YE2024 1305994; geldbeleggingen 50/53 1352010 JUMP",
    f"bud_horizon_kapitaalsubsidies_jr2025_statutory,{EID},2025,131925,131925,131925,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 FLAT,{SRC_PDF},strong,tick2395; PDF p4 native; YE2024 131925",
    f"bud_horizon_fte_jr2025_statutory,{EID},2025,35,35,35,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +10.76%,{SRC_PDF},strong,tick2395; PDF p9 native; YE2024 31.6; personeel 62 2426658; capex 115289",
])
print("entities+budgets ok")

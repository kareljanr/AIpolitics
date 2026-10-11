#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2396_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_accent"
SRC_PDF = "src_accent_jr2025_nbb_pdf_2396"

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
    f'{EID},Centrum voor Ambulante Revalidatie Accent VZW / CAR Accent Kortrijk,Centre de revalidation ambulatoire Accent ASBL,CAR Accent VZW (leftover city_kortrijk ambulante revalidatie),parastatal,city_kortrijk,nl,https://www.revaccent.be/,info@revaccent.be,"Lagaeplein 12/14, 8501 Kortrijk-Heule",tick2396 YE2025 Strong official native NBB PDF deposit 2026-00215981 + Strong KBO 0413.208.122 Actief 1 VE RSZ2025 86.959; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 1242740 CAR envelope; pnl LOSS NARROW -17304; equity DROP 1988694; assets DROP 2194549; debt JUMP 205855; FTE 14.1; kapitaalsubsidies DROP 411; destin691 empty; cash DROP 1320711; leftover city_kortrijk after CAR Horizon@2395; AGB/FARO/Gandae YE2024; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT m-accent Eeklo 0465.841.411; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_accent_bruto_jr2025_statutory,{EID},2025,1242740,1242740,1242740,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +10.39% (primary L5 envelope; omzet 70 empty so bruto is envelope),{SRC_PDF},strong,tick2396; PDF p5 native; YE2024 1125749; omzet70 empty; 73 empty; 76A 1404",
    f"bud_accent_pnl_jr2025_statutory,{EID},2025,-17304,-17304,-17304,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 LOSS NARROW -39.65%,{SRC_PDF},strong,tick2396; PDF p5 native; YE2024 -28673; bedrijfswinst 9901 -96083 LOSS NARROW vs YE2024 -104678; destin691 empty",
    f"bud_accent_bedrijfswinst_jr2025_statutory,{EID},2025,-96083,-96083,-96083,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 LOSS NARROW -8.21%,{SRC_PDF},strong,tick2396; PDF p5 native; YE2024 -104678; 66A 19077",
    f"bud_accent_equity_jr2025_statutory,{EID},2025,1988694,1988694,1988694,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -0.87%,{SRC_PDF},strong,tick2396; PDF p4 native; YE2024 2006203; kapitaalsubsidies 411 DROP; bestemde 13 3000 FLAT",
    f"bud_accent_assets_jr2025_statutory,{EID},2025,2194549,2194549,2194549,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -0.74%,{SRC_PDF},strong,tick2396; PDF p3 native; YE2024 2210889; gebouwen 22 66004; aanbouw 27 empty",
    f"bud_accent_debt_jr2025_statutory,{EID},2025,205855,205855,205855,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +0.57%,{SRC_PDF},strong,tick2396; PDF p4 native; YE2024 204686; ST 42/48 205423",
    f"bud_accent_cash_jr2025_statutory,{EID},2025,1320711,1320711,1320711,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -3.06%,{SRC_PDF},strong,tick2396; PDF p3 native; YE2024 1362450; geldbeleggingen 50/53 725000 FLAT",
    f"bud_accent_kapitaalsubsidies_jr2025_statutory,{EID},2025,411,411,411,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -33.28%,{SRC_PDF},strong,tick2396; PDF p4 native; YE2024 616",
    f"bud_accent_fte_jr2025_statutory,{EID},2025,14.1,14.1,14.1,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 DROP -4.73%,{SRC_PDF},strong,tick2396; PDF p9 native; YE2024 14.8; personeel 62 1293483; capex 2698",
    f"bud_accent_geldbeleggingen_jr2025_statutory,{EID},2025,725000,725000,725000,NBB VKT-VZW code 50/53 geldbeleggingen YE2025 FLAT,{SRC_PDF},strong,tick2396; PDF p3 native; YE2024 725000",
])
print("entities+budgets ok")

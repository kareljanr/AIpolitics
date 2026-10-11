#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2397_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_waas"
SRC_PDF = "src_waas_jr2025_nbb_pdf_2397"

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
    f'{EID},Waas Revalidatiecentrum Lokeren VZW / CAR Waas,Centre de revalidation ambulatoire Waas ASBL,CAR Waas VZW (leftover city_lokeren ambulante revalidatie),parastatal,city_lokeren,nl,https://www.waasrevalidatiecentrum.be/,kaat.degeest@waasrevalidatiecentrum.be,"Luikstraat 109, 9160 Lokeren",tick2397 YE2025 Strong official native NBB PDF deposit 2026-00243160 + Strong KBO 0415.472.279 Actief 1 VE RSZ2025 86.959; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 1636836 CAR envelope; pnl DROP 3351; equity DROP 1550659; assets DROP 1801270; debt JUMP 250611; FTE 21.1; kapitaalsubsidies DROP 269052; destin691 empty; cash DROP 376211; leftover city_lokeren after CAR Accent@2396; AGB/FARO/Gandae YE2024; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_waas_bruto_jr2025_statutory,{EID},2025,1636836,1636836,1636836,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +0.25% (primary L5 envelope; omzet 70 empty so bruto is envelope),{SRC_PDF},strong,tick2397; PDF p5 native; YE2024 1632676; omzet70 empty; 73 empty; 76A empty",
    f"bud_waas_pnl_jr2025_statutory,{EID},2025,3351,3351,3351,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -95.43%,{SRC_PDF},strong,tick2397; PDF p5 native; YE2024 73282; bedrijfswinst 9901 -49573 LOSS FLIP vs YE2024 26680; destin691 empty",
    f"bud_waas_bedrijfswinst_jr2025_statutory,{EID},2025,-49573,-49573,-49573,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 LOSS FLIP,{SRC_PDF},strong,tick2397; PDF p5 native; YE2024 26680; 66A empty",
    f"bud_waas_equity_jr2025_statutory,{EID},2025,1550659,1550659,1550659,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -2.21%,{SRC_PDF},strong,tick2397; PDF p4 native; YE2024 1585744; kapitaalsubsidies 269052 DROP; bestemde 13 600000 FLAT",
    f"bud_waas_assets_jr2025_statutory,{EID},2025,1801270,1801270,1801270,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -1.52%,{SRC_PDF},strong,tick2397; PDF p3 native; YE2024 1829025; gebouwen 22 720801; aanbouw 27 empty",
    f"bud_waas_debt_jr2025_statutory,{EID},2025,250611,250611,250611,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +3.01%,{SRC_PDF},strong,tick2397; PDF p4 native; YE2024 243281; ST 42/48 250611",
    f"bud_waas_cash_jr2025_statutory,{EID},2025,376211,376211,376211,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -15.21%,{SRC_PDF},strong,tick2397; PDF p3 native; YE2024 443678; geldbeleggingen 50/53 425831 DROP; overige vorderingen 41 140000 JUMP",
    f"bud_waas_kapitaalsubsidies_jr2025_statutory,{EID},2025,269052,269052,269052,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -12.50%,{SRC_PDF},strong,tick2397; PDF p4 native; YE2024 307488",
    f"bud_waas_fte_jr2025_statutory,{EID},2025,21.1,21.1,21.1,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +6.03%,{SRC_PDF},strong,tick2397; PDF p10 native; YE2024 19.9; personeel 62 1586724; capex 60067",
    f"bud_waas_geldbeleggingen_jr2025_statutory,{EID},2025,425831,425831,425831,NBB VKT-VZW code 50/53 geldbeleggingen YE2025 DROP -19.39%,{SRC_PDF},strong,tick2397; PDF p3 native; YE2024 528272",
])
print("entities+budgets ok")

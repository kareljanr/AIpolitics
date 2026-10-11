#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2414_stamp.txt").read_text().strip().splitlines()
EID = "vzw_boi"
SRC_PDF = "src_boi_jr2025_nbb_pdf_2414"

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
    f'{EID},Buitenschoolse Opvang Ieper VZW,ASBL Accueil extrascolaire Ypres,Buitenschoolse Opvang Ieper VZW (leftover city_ieper BKO),parastatal,city_ieper,nl,https://www.buitenschoolseopvangieper.be/,info@buitenschoolseopvangieper.be,"Appèlstraat 1, 8900 Ieper",tick2414 YE2025 Strong official native NBB PDF deposit 2026-00173514 + Strong KBO 0431.691.669 Actief 3 VE 2.155.709.192 / 2.216.097.236 Holderdebolder / 2.216.097.533 Klavertje 4 RSZ2025 88.911; omzet70 empty; 73 empty; 76A empty; bruto9900 JUMP 484201 BKO envelope; pnl DROP 3005; 9901 LOSS FLIP -61; equity JUMP 307897; assets DROP 384848; debt DROP 76951; FTE JUMP 9.1; kapitaalsubsidies empty; destin691 empty; cash DROP 289668; geldbeleggingen empty; gebouwen empty; leftover city_ieper after CAR De Klinker@2386; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Mariawende 0411.611.184; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_boi_bruto_jr2025_statutory,{EID},2025,484201,484201,484201,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +1.55% (primary L5 envelope; omzet 70 empty and 73 empty so bruto is envelope),{SRC_PDF},strong,tick2414; PDF p5 native; YE2024 476815; omzet70 empty; 73 empty; 76A empty",
    f"bud_boi_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2414; PDF p5 native; YE2024 empty; 73 empty",
    f"bud_boi_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2414; PDF p5 native; YE2024 empty",
    f"bud_boi_pnl_jr2025_statutory,{EID},2025,3005,3005,3005,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -82.54%,{SRC_PDF},strong,tick2414; PDF p5 native; YE2024 17211; bedrijfswinst 9901 -61 LOSS FLIP; destin691 empty",
    f"bud_boi_bedrijfswinst_jr2025_statutory,{EID},2025,-61,-61,-61,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 LOSS FLIP (was 17090),{SRC_PDF},strong,tick2414; PDF p5 native; YE2024 17090; 62 482300 JUMP +5.39%",
    f"bud_boi_equity_jr2025_statutory,{EID},2025,307897,307897,307897,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +0.99%,{SRC_PDF},strong,tick2414; PDF p4 native; YE2024 304892; kapitaalsubsidies empty; overgedragen 14 241798; fondsen 10 66099 FLAT; bestemde 13 empty",
    f"bud_boi_assets_jr2025_statutory,{EID},2025,384848,384848,384848,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -6.94%,{SRC_PDF},strong,tick2414; PDF p3 native; YE2024 413564; gebouwen 22 empty; 3 VE",
    f"bud_boi_cash_jr2025_statutory,{EID},2025,289668,289668,289668,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -9.06%,{SRC_PDF},strong,tick2414; PDF p3 native; YE2024 318522; geldbeleggingen 50/53 empty",
    f"bud_boi_debt_jr2025_statutory,{EID},2025,76951,76951,76951,NBB VKT-VZW code 17/49 schulden YE2025 DROP -29.19%,{SRC_PDF},strong,tick2414; PDF p4 native; YE2024 108672; bezoldigingen 45 58716 was 89649",
    f"bud_boi_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2414; PDF p6 native; 9905 3005 fully to overgedragen 14 now 241798",
])
print("entities+budgets ok")

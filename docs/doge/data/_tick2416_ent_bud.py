#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2416_stamp.txt").read_text().strip().splitlines()
EID = "vzw_denderkind"
SRC_PDF = "src_denderkind_jr2025_nbb_pdf_2416"

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
    f'{EID},Denderkind VZW Aalst,ASBL Denderkind Alost,Denderkind VZW (leftover city_aalst CIK+BKO),parastatal,city_aalst,nl,https://www.denderkind.be/,info@denderkind.be,"Korte Zoutstraat 32 bus K, 9300 Aalst",tick2416 YE2025 Strong official native NBB PDF deposit 2026-00065367 + Strong KBO 0479.127.045 Actief 16 VE HQ 2.157.744.016 + 15 KDV-sites incl. Ede-kind 2.388.220.073 since 05.01.2026 post-YE2025 RSZ2025 88.911; omzet70 empty; 73 empty; 76A empty; bruto9900 JUMP 3957120 CIK envelope; pnl DROP 25088; 9901 LOSS FLIP -17514; equity JUMP 1896227; assets JUMP 3918204; debt JUMP 2021977; FTE JUMP 59.9; kapitaalsubsidies empty; destin691 empty; cash JUMP 1338704; geldbeleggingen DROP 0; gebouwen JUMP 2420068; leftover city_aalst after CAR De Hert; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_denderkind_bruto_jr2025_statutory,{EID},2025,3957120,3957120,3957120,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +3.46% (primary L5 envelope; omzet 70 empty and 73 empty so bruto is envelope),{SRC_PDF},strong,tick2416; PDF p5 native; YE2024 3824624; omzet70 empty; 73 empty; 76A empty",
    f"bud_denderkind_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2416; PDF p5 native; YE2024 empty; 73 empty",
    f"bud_denderkind_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2416; PDF p5 native; YE2024 empty",
    f"bud_denderkind_pnl_jr2025_statutory,{EID},2025,25088,25088,25088,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -89.75%,{SRC_PDF},strong,tick2416; PDF p6 native; YE2024 244823; bedrijfswinst 9901 -17514 LOSS FLIP; destin691 empty",
    f"bud_denderkind_bedrijfswinst_jr2025_statutory,{EID},2025,-17514,-17514,-17514,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 LOSS FLIP,{SRC_PDF},strong,tick2416; PDF p6 native; YE2024 246160; 62 3788253 JUMP +12.30%",
    f"bud_denderkind_equity_jr2025_statutory,{EID},2025,1896227,1896227,1896227,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +1.34%,{SRC_PDF},strong,tick2416; PDF p5 native; YE2024 1871139; kapitaalsubsidies empty; overgedragen 14 1896227; fondsen 10 empty; bestemde 13 empty",
    f"bud_denderkind_assets_jr2025_statutory,{EID},2025,3918204,3918204,3918204,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +27.27%,{SRC_PDF},strong,tick2416; PDF p4 native; YE2024 3078743; gebouwen 22 2420068; 16 VE",
    f"bud_denderkind_cash_jr2025_statutory,{EID},2025,1338704,1338704,1338704,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +70.78%,{SRC_PDF},strong,tick2416; PDF p4 native; YE2024 783860; geldbeleggingen 50/53 0 DROP was 300000",
    f"bud_denderkind_debt_jr2025_statutory,{EID},2025,2021977,2021977,2021977,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +67.44%,{SRC_PDF},strong,tick2416; PDF p5 native; YE2024 1207604; 42/48 802710 JUMP; 45 511888 JUMP",
    f"bud_denderkind_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (9905 25088 fully to overgedragen 14),{SRC_PDF},strong,tick2416; PDF p7 native; 9905 25088 to overgedragen 14 1896227; destin691 empty",
])
print("entities+budgets ok")

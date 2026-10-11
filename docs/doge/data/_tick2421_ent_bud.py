#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2421_stamp.txt").read_text().strip().splitlines()
EID = "vzw_quattro"
SRC_PDF = "src_quattro_jr2025_nbb_pdf_2421"

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
    f'{EID},QUATTRO VZW,ASBL QUATTRO,Quattro VZW (leftover city_kortrijk WZC-collab),parastatal,city_kortrijk,nl,https://quattrosamenwerkenaanzorg.be/,boekhouding@de-ruyschaert.be,"Kloosterstraat 18, 8510 Marke",tick2421 YE2025 Strong official native NBB PDF deposit 2026-00188800 + Strong KBO 0555.667.072 Actief 1 VE 2.239.182.147 Kloosterstraat 18 Marke RSZ2025 88.109; omzet70 JUMP 247410 envelope (73 empty so omzet is envelope not commercial-only); 73 empty; 76A empty; bruto9900 JUMP 239381; pnl LOSS IMPROVE -9071; 9901 LOSS IMPROVE -10194; equity DROP 81093; assets JUMP 264015; debt JUMP 182922; FTE 2.8; kapitaalsubsidies empty; destin691 empty; cash DROP 68360; geldbeleggingen JUMP 100000; gebouwen empty; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder / WZC De Ruyschaert; NOT Kloosterstraat 6 Drongen; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_quattro_omzet_jr2025_statutory,{EID},2025,247410,247410,247410,NBB MIC-VZW code 70 omzet YE2025 JUMP +106.18% (primary L5 envelope; 73 empty so omzet is envelope not commercial-only; jaarverslag bijdragen huizen + toetreding De Linde 25k),{SRC_PDF},strong,tick2421; PDF p5 native; YE2024 120000; 73 empty so omzet is envelope",
    f"bud_quattro_73_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty (MIC-VZW; envelope is omzet 70),{SRC_PDF},strong,tick2421; PDF p5 native; YE2024 empty; envelope is omzet 70",
    f"bud_quattro_bruto_jr2025_statutory,{EID},2025,239381,239381,239381,NBB MIC-VZW code 9900 brutomarge YE2025 JUMP +130.50%,{SRC_PDF},strong,tick2421; PDF p5 native; YE2024 103853; envelope remains omzet 70",
    f"bud_quattro_76A_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2421; PDF p5 native; YE2024 empty",
    f"bud_quattro_pnl_jr2025_statutory,{EID},2025,-9071,-9071,-9071,NBB MIC-VZW code 9904 verlies van het boekjaar YE2025 LOSS IMPROVE,{SRC_PDF},strong,tick2421; PDF p5 native; YE2024 LOSS -66794; bedrijfswinst 9901 -10194 IMPROVE; destin691 empty",
    f"bud_quattro_bedrijfswinst_jr2025_statutory,{EID},2025,-10194,-10194,-10194,NBB MIC-VZW code 9901 bedrijfsverlies YE2025 LOSS IMPROVE,{SRC_PDF},strong,tick2421; PDF p5 native; YE2024 LOSS -67985; 62 232282 JUMP +38.27%",
    f"bud_quattro_equity_jr2025_statutory,{EID},2025,81093,81093,81093,NBB MIC-VZW code 10/15 eigen vermogen YE2025 DROP -10.06%,{SRC_PDF},strong,tick2421; PDF p4 native; YE2024 90164; kapitaalsubsidies empty; overgedragen 14 -68907; fondsen 10 150000 FLAT; bestemde 13 empty",
    f"bud_quattro_assets_jr2025_statutory,{EID},2025,264015,264015,264015,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +51.85%,{SRC_PDF},strong,tick2421; PDF p3 native; YE2024 173863; gebouwen 22 empty; 1 VE",
    f"bud_quattro_debt_jr2025_statutory,{EID},2025,182922,182922,182922,NBB MIC-VZW code 17/49 schulden YE2025 JUMP +118.55%,{SRC_PDF},strong,tick2421; PDF p4 native; YE2024 83699; 42/48 45533 DROP; 44 7159 DROP; 45 38374; 492/3 137389 JUMP was empty; 17 empty",
    f"bud_quattro_destin_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 691 toevoeging bestemde fondsen YE2025 empty (9905 -9071 fully to overgedragen 14),{SRC_PDF},strong,tick2421; PDF p6 native; 9905 -9071 + 14P -59836 = overgedragen 14 -68907; destin691 empty",
])
print("entities+budgets ok")

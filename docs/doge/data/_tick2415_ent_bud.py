#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2415_stamp.txt").read_text().strip().splitlines()
EID = "vzw_mariawende"
SRC_PDF = "src_mariawende_jr2025_nbb_pdf_2415"

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
    f'{EID},Kinderopvang Mariawende VZW,ASBL Accueil extrafamilial Mariawende,Kinderopvang Mariawende VZW (leftover city_brugge CIK+BKO),parastatal,city_brugge,nl,https://www.ko-mariawende.be/,directeur@ko-mariawende.be,"Keizerstraat 14 A, 8310 Brugge",tick2415 YE2025 Strong official native NBB PDF deposit 2026-00302442 + Strong KBO 0411.611.184 Actief 2 VE 2.153.783.446 Ons Tuintje / 2.212.055.306 t speelhuis RSZ2025 88.911; omzet70 empty; 73 empty; 76A empty; bruto9900 JUMP 3345554 CIK envelope; pnl JUMP 735612; 9901 JUMP 588557; equity JUMP 6465476; assets JUMP 6896666; debt DROP 431190; FTE JUMP 45.2; kapitaalsubsidies DROP 1287136; destin691 JUMP 735612; cash JUMP 331722; geldbeleggingen JUMP 2537774; gebouwen DROP 2697443; leftover city_brugge after Mintus@1269; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_mariawende_bruto_jr2025_statutory,{EID},2025,3345554,3345554,3345554,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +9.42% (primary L5 envelope; omzet 70 empty and 73 empty so bruto is envelope),{SRC_PDF},strong,tick2415; PDF p5 native; YE2024 3057583; omzet70 empty; 73 empty; 76A empty",
    f"bud_mariawende_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2415; PDF p5 native; YE2024 empty; 73 empty",
    f"bud_mariawende_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2415; PDF p5 native; YE2024 empty",
    f"bud_mariawende_pnl_jr2025_statutory,{EID},2025,735612,735612,735612,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +81.13%,{SRC_PDF},strong,tick2415; PDF p5 native; YE2024 406134; bedrijfswinst 9901 588557 JUMP; destin691 735612",
    f"bud_mariawende_bedrijfswinst_jr2025_statutory,{EID},2025,588557,588557,588557,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +73.15%,{SRC_PDF},strong,tick2415; PDF p5 native; YE2024 339908; 62 2600896 JUMP +4.02%",
    f"bud_mariawende_equity_jr2025_statutory,{EID},2025,6465476,6465476,6465476,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +11.70%,{SRC_PDF},strong,tick2415; PDF p4 native; YE2024 5788504; kapitaalsubsidies 1287136 DROP; overgedragen 14 2113842 FLAT; fondsen 10 20507 FLAT; bestemde 13 3043990",
    f"bud_mariawende_assets_jr2025_statutory,{EID},2025,6896666,6896666,6896666,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +10.79%,{SRC_PDF},strong,tick2415; PDF p3 native; YE2024 6225112; gebouwen 22 2697443; 2 VE",
    f"bud_mariawende_cash_jr2025_statutory,{EID},2025,331722,331722,331722,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +675.61%,{SRC_PDF},strong,tick2415; PDF p3 native; YE2024 42769; geldbeleggingen 50/53 2537774 JUMP +2.94%",
    f"bud_mariawende_debt_jr2025_statutory,{EID},2025,431190,431190,431190,NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.24%,{SRC_PDF},strong,tick2415; PDF p4 native; YE2024 436608; bezoldigingen 45 235813 was 297082",
    f"bud_mariawende_destin_jr2025_statutory,{EID},2025,735612,735612,735612,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +80.48% (100% of 9905),{SRC_PDF},strong,tick2415; PDF p6 native; 9905 735612 fully to destin 691; overgedragen 14 FLAT 2113842",
])
print("entities+budgets ok")

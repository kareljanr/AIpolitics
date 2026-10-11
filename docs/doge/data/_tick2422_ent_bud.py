#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2422_stamp.txt").read_text().strip().splitlines()
EID = "vzw_wintershove"
SRC_PDF = "src_wintershove_jr2025_nbb_pdf_2422"

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
    f'{EID},WINTERSHOVE VZW,ASBL WINTERSHOVE,Wintershove VZW (leftover city_ieper Quattro-lid WZC),parastatal,city_ieper,nl,https://www.wintershove.be/,info@wintershove.be,"Poperingseweg 288, 8908 Vlamertinge",tick2422 YE2025 Strong official native NBB PDF deposit 2026-00178085 + Strong KBO 0459.245.312 Actief 1 VE 2.156.473.910 Poperingseweg 288 Vlamertinge RSZ2025 87.301; omzet70 JUMP 6653784 envelope (not commercial-only vs 73 1039037); 73 DROP 1039037 all 733; 76A empty; opbr 70/76A DROP 7794859; pnl LOSS FLIP -22737; 9901 DROP 41192; equity DROP 2728813; assets DROP 5998955; debt DROP 2808568; FTE 95.7; kapitaalsubsidies DROP 383488; destin691 empty; cash DROP 516794; geldbeleggingen 0; gebouwen DROP 3736734; leftover city_ieper after Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT WZC De Linde Lievegem 0467.355.403; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_wintershove_omzet_jr2025_statutory,{EID},2025,6653784,6653784,6653784,NBB VOL-VZW code 70 omzet YE2025 JUMP +0.78% (primary L5 envelope; omzet present and not commercial-only vs 73 1039037),{SRC_PDF},strong,tick2422; PDF p7 native; YE2024 6602468; envelope is omzet 70",
    f"bud_wintershove_73_jr2025_statutory,{EID},2025,1039037,1039037,1039037,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -10.66% (all subsidies 733),{SRC_PDF},strong,tick2422; PDF p7+p23 native; YE2024 1162972; 730/731/732 empty; envelope remains omzet 70",
    f"bud_wintershove_opbr_jr2025_statutory,{EID},2025,7794859,7794859,7794859,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 DROP -0.69% (VZW total; envelope remains omzet 70 because not commercial-only),{SRC_PDF},strong,tick2422; PDF p7 native; YE2024 7849363; 74 JUMP 102038; 76A empty",
    f"bud_wintershove_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2422; PDF p7 native; YE2024 empty",
    f"bud_wintershove_pnl_jr2025_statutory,{EID},2025,-22737,-22737,-22737,NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 LOSS FLIP,{SRC_PDF},strong,tick2422; PDF p8 native; YE2024 PROFIT 28270; bedrijfswinst 9901 41192 DROP; destin691 empty",
    f"bud_wintershove_bedrijfswinst_jr2025_statutory,{EID},2025,41192,41192,41192,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -55.44%,{SRC_PDF},strong,tick2422; PDF p7 native; YE2024 92449; 62 6188219 JUMP +1.11%",
    f"bud_wintershove_equity_jr2025_statutory,{EID},2025,2728813,2728813,2728813,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -3.64%,{SRC_PDF},strong,tick2422; PDF p6 native; YE2024 2831860; kapitaalsubsidies DROP 383488; overgedragen 14 1046441; fondsen 10 1298884 FLAT; bestemde 13 empty",
    f"bud_wintershove_assets_jr2025_statutory,{EID},2025,5998955,5998955,5998955,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -4.02%,{SRC_PDF},strong,tick2422; PDF p5 native; YE2024 6249930; gebouwen 22 DROP 3736734; 1 VE",
    f"bud_wintershove_debt_jr2025_statutory,{EID},2025,2808568,2808568,2808568,NBB VOL-VZW code 17/49 schulden YE2025 DROP -4.46%,{SRC_PDF},strong,tick2422; PDF p6 native; YE2024 2939779; 173 1091351 DROP; 42/48 1709848; 44 349721 JUMP; 45 1073771; 17 1091611",
    f"bud_wintershove_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (9905 -22737 fully to overgedragen 14 1046441),{SRC_PDF},strong,tick2422; PDF p9 native; 9905 -22737 + 14P 1069178 = overgedragen 14 1046441; destin691 empty",
])
print("entities+budgets ok")

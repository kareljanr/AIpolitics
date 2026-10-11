#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2426_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kindercentrum"
SRC_PDF = "src_kindercentrum_jr2025_nbb_pdf_2426"

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
    f'{EID},Kindercentrum VZW,ASBL Kindercentrum,Kindercentrum VZW (leftover city_waregem CIK),parastatal,city_waregem,nl,https://kindercentrum.be/,info@kindercentrum.be,"Koning Albertstraat 43, 8791 Waregem",tick2426 YE2025 Strong official native NBB PDF deposit 2026-00194179 + Strong KBO 0408.226.775 Actief 14 VE zetel Koning Albertstraat 43 8791 Waregem RSZ2025 88.911; omzet70 JUMP 2193637 commercial-only vs large 74 9130994; 73 DROP 55829; 76A DROP 21401; opbr 70/76A JUMP 11401861 envelope; pnl DROP 482202; 9901 DROP 540739; equity JUMP 4163926; assets JUMP 7834315; debt JUMP 3615215; FTE 126.6; kapitaalsubsidies DROP 999715; destin691 empty; cash JUMP 2576815; geldbeleggingen empty; gebouwen DROP 3662927; aanbouw empty; leftover mined city_waregem after WAGSO / Werkplus Maatwerk Waregem@2204; NOT Kloosterstraat 6 Drongen; NOT WZC De Linde Wortegem-Petegem 0425.773.085; NOT WZC De Linde Lievegem 0467.355.403; NOT De Linde Ronse 0778.279.401; NOT Curando 0445.499.422; NOT Kinderopvang Mariawende 0411.611.184; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_kindercentrum_omzet_jr2025_statutory,{EID},2025,2193637,2193637,2193637,NBB VOL-VZW code 70 omzet YE2025 JUMP +5.43% (ouderbijdragen; commercial-only vs large 74 9130994),{SRC_PDF},strong,tick2426; PDF p6 native; YE2024 2080573; envelope is 70/76A 11401861",
    f"bud_kindercentrum_73_jr2025_statutory,{EID},2025,55829,55829,55829,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -0.29%,{SRC_PDF},strong,tick2426; PDF p6 native; YE2024 55990; all 733 subsidies; jaarverslag kapitaal- en intrestsubsidies 56k",
    f"bud_kindercentrum_opbr_jr2025_statutory,{EID},2025,11401861,11401861,11401861,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +4.69% (VZW envelope; omzet commercial-only vs large 74),{SRC_PDF},strong,tick2426; PDF p6 native; YE2024 10890888; 74 JUMP 9130994; 76A DROP 21401",
    f"bud_kindercentrum_76A_jr2025_statutory,{EID},2025,21401,21401,21401,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -77.18%,{SRC_PDF},strong,tick2426; PDF p6 native; YE2024 93784; 7620 20381 + 764/8 1020",
    f"bud_kindercentrum_pnl_jr2025_statutory,{EID},2025,482202,482202,482202,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -12.74%,{SRC_PDF},strong,tick2426; PDF p7 native; YE2024 552616; bedrijfswinst 9901 540739 DROP; destin691 empty",
    f"bud_kindercentrum_bedrijfswinst_jr2025_statutory,{EID},2025,540739,540739,540739,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -5.01%,{SRC_PDF},strong,tick2426; PDF p6 native; YE2024 569244; 62 7222574 JUMP +7.76%",
    f"bud_kindercentrum_equity_jr2025_statutory,{EID},2025,4163926,4163926,4163926,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +11.41%,{SRC_PDF},strong,tick2426; PDF p5 native; YE2024 3737553; kapitaalsubsidies DROP 999715; overgedragen 14 2631926; fondsen 10 60392 FLAT",
    f"bud_kindercentrum_assets_jr2025_statutory,{EID},2025,7834315,7834315,7834315,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +10.11%,{SRC_PDF},strong,tick2426; PDF p4 native; YE2024 7114847; gebouwen 22 DROP 3662927; aanbouw 27 empty; 14 VE",
    f"bud_kindercentrum_debt_jr2025_statutory,{EID},2025,3615215,3615215,3615215,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +9.78%,{SRC_PDF},strong,tick2426; PDF p5 native; YE2024 3293038; 173 2412476 JUMP",
    f"bud_kindercentrum_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2426; PDF p8 native; 9905 482202 + destin691 empty = overgedragen 14 2631926; YE2024 destin691 empty",
])
print("entities+budgets ok")

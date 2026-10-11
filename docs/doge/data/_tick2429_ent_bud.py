#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2429_stamp.txt").read_text().strip().splitlines()
EID = "vzw_windekind"
SRC_PDF = "src_windekind_jr2025_nbb_pdf_2429"

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
    f'{EID},KINDERDAGVERBLIJF WINDEKIND VZW,ASBL KINDERDAGVERBLIJF WINDEKIND,Windekind VZW (leftover city_gent CIK),parastatal,city_gent,nl,https://windekind.gent/,info@windekind.gent,"Roggestraat 17, 9000 Gent",tick2429 YE2025 Strong official native NBB PDF deposit 2026-00320133 + Strong KBO 0431.806.386 Actief 1 VE 2.154.448.588 Roggestraat 17 9000 Gent RSZ2025 88.911; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto9900 JUMP 1184568 CIK envelope; pnl DROP 61273; 9901 DROP 62541; equity JUMP 500665; assets JUMP 631200; debt JUMP 130534; FTE 16.5; kapitaalsubsidies empty; destin691 JUMP 61273; cash JUMP 520891; geldbeleggingen JUMP 20000; gebouwen DROP 29869; aanbouw empty; leftover mined city_gent after Elfenbankje / AGB Kunsten / AGB Erfgoed; 69 Opgroeien plaatsen; NOT Kloosterstraat 6 Drongen; NOT Elfenbankje 0417.638.151; NOT Beregoed 0447.515.042; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT WZC De Linde Wortegem-Petegem 0425.773.085; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_windekind_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty,{SRC_PDF},strong,tick2429; PDF p5 native; VKT omzet unpublished; envelope is bruto 9900 1184568",
    f"bud_windekind_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty,{SRC_PDF},strong,tick2429; PDF p5 native; VKT 73 unpublished; site Opgroeien 69 plaatsen not booked on 73",
    f"bud_windekind_bruto_jr2025_statutory,{EID},2025,1184568,1184568,1184568,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +9.18% (CIK envelope; omzet empty so bruto is envelope),{SRC_PDF},strong,tick2429; PDF p5 native; YE2024 1084985; 76A empty",
    f"bud_windekind_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2429; PDF p5 native; 76A empty both years",
    f"bud_windekind_pnl_jr2025_statutory,{EID},2025,61273,61273,61273,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -8.72%,{SRC_PDF},strong,tick2429; PDF p5 native; YE2024 67127; bedrijfswinst 9901 62541 DROP; destin691 61273",
    f"bud_windekind_bedrijfswinst_jr2025_statutory,{EID},2025,62541,62541,62541,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -9.77%,{SRC_PDF},strong,tick2429; PDF p5 native; YE2024 69317; 62 1094857 JUMP +11.01%",
    f"bud_windekind_equity_jr2025_statutory,{EID},2025,500665,500665,500665,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +13.94%,{SRC_PDF},strong,tick2429; PDF p4 native; YE2024 439392; kapitaalsubsidies empty; overgedragen 14 empty; fondsen 10 500665",
    f"bud_windekind_assets_jr2025_statutory,{EID},2025,631200,631200,631200,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +13.53%,{SRC_PDF},strong,tick2429; PDF p3 native; YE2024 555952; gebouwen 22 DROP 29869; aanbouw 27 empty; 1 VE",
    f"bud_windekind_debt_jr2025_statutory,{EID},2025,130534,130534,130534,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +11.99%,{SRC_PDF},strong,tick2429; PDF p4 native; YE2024 116560; 42/48 130534; 44 21626; 45 108908",
    f"bud_windekind_destin_jr2025_statutory,{EID},2025,61273,61273,61273,NBB VKT-VZW code 691 toevoeging fondsen YE2025 DROP -8.72%,{SRC_PDF},strong,tick2429; PDF p6 native; 9905 61273 + destin691 61273 = fondsen 10 500665; code 13 empty; YE2024 destin691 67127",
])
print("entities+budgets ok")

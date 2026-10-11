from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2431_stamp.txt").read_text().strip().splitlines()
EID="vzw_witje_wiebel"
SRC_PDF="src_witje_wiebel_jr2025_nbb_pdf_2431"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},KINDERDAGVERBLIJF WITJE WIEBEL VZW,ASBL KINDERDAGVERBLIJF WITJE WIEBEL,Witje Wiebel VZW (leftover city_gent CIK),parastatal,city_gent,nl,https://witjewiebel.be/,witje.wiebel@mijnziekenhuis.be,\"Kortrijksesteenweg 1020, 9000 Gent\",tick2431 YE2025 Strong official native NBB PDF deposit 2026-00143338 + Strong KBO 0443.654.937 Actief 2 VE 2.150.816.533 Kortrijksesteenweg 1020 9000 Gent + 2.152.579.656 Smidsestraat 88 9000 Gent RSZ2025 88.911; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto9900 FLAT 1878999 envelope; pnl JUMP 301158; 9901 DROP 304658; equity JUMP 2307857; assets JUMP 2843864; debt DROP 536007; FTE 25.3; kapitaalsubsidies DROP 560470; destin691 300000; cash JUMP 804896; geldbeleggingen FLAT 650000; gebouwen DROP 1134601; aanbouw empty; leftover mined city_gent after Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 2 VE campus Maria Middelares + Sint-Pieters same KBO; NOT Kloosterstraat 6 Drongen; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_witje_wiebel_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty,{SRC_PDF},strong,tick2431; PDF p5 native; VKT omzet unpublished; envelope is bruto 9900 1878999",
f"bud_witje_wiebel_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty,{SRC_PDF},strong,tick2431; PDF p5 native; VKT 73 unpublished; site 2 Gent campussen not booked on 73",
f"bud_witje_wiebel_bruto_jr2025_statutory,{EID},2025,1878999,1878999,1878999,NBB VKT-VZW code 9900 brutomarge YE2025 FLAT +0.06% (CIK envelope; omzet empty so bruto is envelope),{SRC_PDF},strong,tick2431; PDF p5 native; YE2024 1877813; 76A empty",
f"bud_witje_wiebel_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2431; PDF p5 native",
f"bud_witje_wiebel_pnl_jr2025_statutory,{EID},2025,301158,301158,301158,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +0.52%,{SRC_PDF},strong,tick2431; PDF p5 native; YE2024 299585; bedrijfswinst 9901 304658 DROP; destin691 300000",
f"bud_witje_wiebel_bedrijfswinst_jr2025_statutory,{EID},2025,304658,304658,304658,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -1.12%,{SRC_PDF},strong,tick2431; PDF p5 native; YE2024 308105; 62 1490455 FLAT",
f"bud_witje_wiebel_equity_jr2025_statutory,{EID},2025,2307857,2307857,2307857,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +13.15%,{SRC_PDF},strong,tick2431; PDF p4 native; YE2024 2039571; kapitaalsubsidies 560470 DROP; overgedragen 14 1059090; bestemde fondsen 13 599585",
f"bud_witje_wiebel_assets_jr2025_statutory,{EID},2025,2843864,2843864,2843864,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +7.94%,{SRC_PDF},strong,tick2431; PDF p3 native; YE2024 2634687; gebouwen 22 DROP 1134601; aanbouw 27 empty; 2 VE",
f"bud_witje_wiebel_debt_jr2025_statutory,{EID},2025,536007,536007,536007,NBB VKT-VZW code 17/49 schulden YE2025 DROP -9.93%,{SRC_PDF},strong,tick2431; PDF p4 native; YE2024 595116; 42/48 379163; 44 82377; 45 165488",
f"bud_witje_wiebel_destin_jr2025_statutory,{EID},2025,300000,300000,300000,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +0.14%,{SRC_PDF},strong,tick2431; PDF p6 native; 9905 301158 + destin691 300000 to code 13 599585; overgedragen 14 1059090; YE2024 destin691 299585",
])
print("entities+budgets ok")

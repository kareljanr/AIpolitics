from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2432_stamp.txt").read_text().strip().splitlines()
EID="vzw_home_emmaus"
SRC_PDF="src_home_emmaus_jr2025_nbb_pdf_2432"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Home Emmaus VZW,ASBL Home Emmaus,Home Emmaus VZW (leftover city_gent VAPH),parastatal,city_gent,nl,https://dovencentrum-emmaus.be/,boekhouding@dovencentrum-emmaus.be,\"Van den Heckestraat 41-43, 9050 Gent\",tick2432 YE2025 Strong official native NBB PDF deposit 2026-00339558 + Strong KBO 0451.749.190 Actief 1 VE 2.156.748.775 Van den Heckestraat 41-43 9050 Gent RSZ2025 88.104; omzet70 JUMP 279413 commercial-only vs large 73; 73 JUMP 1951139; 76A 0; opbr 70+73+76A JUMP 2230552 envelope; bruto9900 JUMP 2086695; pnl JUMP 270624; 9901 JUMP 193689; equity JUMP 2562446; assets JUMP 2911569; debt JUMP 349123; FTE 26.6 DROP; kapitaalsubsidies JUMP 27614; destin691 empty; cash DROP 736197; geldbeleggingen JUMP 1841875; gebouwen empty; aanbouw empty; leftover mined city_gent after Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 1 VE Gent-Ledeberg same KBO; NOT Kloosterstraat 6 Drongen; NOT Emmaus AZ 0411.515.075; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Knuffelboom 0478.310.859; NOT De Zeppelin 0454.001.867; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_home_emmaus_omzet_jr2025_statutory,{EID},2025,279413,279413,279413,NBB VKT-VZW code 70 omzet YE2025 JUMP +3.82% (commercial-only vs large 73),{SRC_PDF},strong,tick2432; PDF p5 native; YE2024 restated 269143; envelope is 70+73+76A 2230552",
f"bud_home_emmaus_73_jr2025_statutory,{EID},2025,1951139,1951139,1951139,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +5.22%,{SRC_PDF},strong,tick2432; PDF p5 native; YE2024 restated 1854327; VAPH/PVF/RTH matrix FOI",
f"bud_home_emmaus_opbr_jr2025_statutory,{EID},2025,2230552,2230552,2230552,NBB VKT-VZW 70+73+76A bedrijfsopbrengsten YE2025 JUMP +5.04% (VZW envelope; omzet commercial-only vs large 73),{SRC_PDF},strong,tick2432; PDF p5 native; 279413+1951139+0; YE2024 restated 2123470",
f"bud_home_emmaus_bruto_jr2025_statutory,{EID},2025,2086695,2086695,2086695,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +4.95%,{SRC_PDF},strong,tick2432; PDF p5 native; YE2024 restated 1988358; 76A 0",
f"bud_home_emmaus_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2432; PDF p5 native",
f"bud_home_emmaus_pnl_jr2025_statutory,{EID},2025,270624,270624,270624,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +19.50%,{SRC_PDF},strong,tick2432; PDF p5 native; YE2024 restated 226461; bedrijfswinst 9901 193689 JUMP; destin691 empty",
f"bud_home_emmaus_bedrijfswinst_jr2025_statutory,{EID},2025,193689,193689,193689,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +37.07%,{SRC_PDF},strong,tick2432; PDF p5 native; YE2024 restated 141307; 62 1859718 JUMP",
f"bud_home_emmaus_equity_jr2025_statutory,{EID},2025,2562446,2562446,2562446,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +13.17%,{SRC_PDF},strong,tick2432; PDF p4 native; YE2024 restated 2264207; kapitaalsubsidies 27614 JUMP from empty; overgedragen 14 2399832; bestemde fondsen 13 135000",
f"bud_home_emmaus_assets_jr2025_statutory,{EID},2025,2911569,2911569,2911569,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +12.93%,{SRC_PDF},strong,tick2432; PDF p3 native; YE2024 restated 2578270; gebouwen 22 empty; aanbouw 27 empty; 1 VE",
f"bud_home_emmaus_debt_jr2025_statutory,{EID},2025,349123,349123,349123,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +11.16%,{SRC_PDF},strong,tick2432; PDF p4 native; YE2024 restated 314063; 42/48 346877; 44 25481; 45 237270",
f"bud_home_emmaus_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2432; PDF p6 native; 9905 270624 + destin691 empty; overgedragen 14 2399832; YE2024 destin691 empty",
])
print("entities+budgets ok")

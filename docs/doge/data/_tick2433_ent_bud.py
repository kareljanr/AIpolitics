from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2433_stamp.txt").read_text().strip().splitlines()
EID="vzw_wzc_sint_coleta_gent"
SRC_PDF="src_sint_coleta_jr2025_nbb_pdf_2433"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Woon- en Zorgcentrum Sint-Coleta Gent VZW,ASBL WZC Sint-Coleta Gand,WZC Sint-Coleta Gent VZW (leftover city_gent WZC),parastatal,city_gent,nl,https://www.sintcoleta.be/,info@sintcoleta.be,\"Sint-Coletastraat 4, 9000 Gent\",tick2433 YE2025 Strong official native NBB PDF deposit 2026-00192499 + Strong KBO 0448.294.507 Actief 1 VE 2.156.526.863 Sint-Coletastraat 4 9000 Gent RSZ2025 87.101; omzet70 JUMP 5614657 envelope (not commercial-only vs 73); 73 DROP 982687; 76A 70552; 70/76A JUMP 6796611; bruto9900 empty VOL; pnl DROP 75406; 9901 DROP 69308; equity JUMP 2789036; assets DROP 4673967; debt DROP 1884932; FTE 66.8 JUMP; kapitaalsubsidies DROP 173334; destin691 empty; cash JUMP 478451; geldbeleggingen JUMP 650876; gebouwen DROP 2042258; aanbouw 0; leftover mined city_gent after Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 1 VE Gent same KBO; NOT Kloosterstraat 6 Drongen; NOT Home Emmaus 0451.749.190; NOT De Foyer 0413.796.456; NOT Emmaus AZ 0411.515.075; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Knuffelboom 0478.310.859; NOT De Zeppelin 0454.001.867; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_sint_coleta_omzet_jr2025_statutory,{EID},2025,5614657,5614657,5614657,NBB VOL-VZW code 70 omzet YE2025 JUMP +10.18% (ouderenzorg; envelope; not commercial-only vs 73 982687),{SRC_PDF},strong,tick2433; PDF p6 native; YE2024 identical 5095783; envelope is omzet 70",
f"bud_sint_coleta_73_jr2025_statutory,{EID},2025,982687,982687,982687,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -8.46%,{SRC_PDF},strong,tick2433; PDF p6 native; YE2024 identical 1073507; 731 26481; 733 956206 DROP; WZC/RIZIV/Vlaams matrix FOI",
f"bud_sint_coleta_opbr_jr2025_statutory,{EID},2025,6796611,6796611,6796611,NBB VOL-VZW 70/76A bedrijfsopbrengsten YE2025 JUMP +8.20%,{SRC_PDF},strong,tick2433; PDF p6 native; YE2024 identical 6281450; envelope is omzet 70 5614657 because not commercial-only vs 73",
f"bud_sint_coleta_76A_jr2025_statutory,{EID},2025,70552,70552,70552,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP,{SRC_PDF},strong,tick2433; PDF p6 native; YE2024 identical 6558",
f"bud_sint_coleta_pnl_jr2025_statutory,{EID},2025,75406,75406,75406,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -61.15%,{SRC_PDF},strong,tick2433; PDF p8 native; YE2024 identical 194096; bedrijfswinst 9901 69308 DROP; destin691 empty",
f"bud_sint_coleta_bedrijfswinst_jr2025_statutory,{EID},2025,69308,69308,69308,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -64.05%,{SRC_PDF},strong,tick2433; PDF p7 native; YE2024 identical 192776; 62 4729997 JUMP",
f"bud_sint_coleta_equity_jr2025_statutory,{EID},2025,2789036,2789036,2789036,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +1.86%,{SRC_PDF},strong,tick2433; PDF p5 native; YE2024 identical 2738152; kapitaalsubsidies 173334 DROP; overgedragen 14 1890348; bestemde fondsen 13 425746 FLAT",
f"bud_sint_coleta_assets_jr2025_statutory,{EID},2025,4673967,4673967,4673967,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -1.31%,{SRC_PDF},strong,tick2433; PDF p5 native; YE2024 identical 4735989; gebouwen 22 2042258 DROP; aanbouw 27 0; 1 VE",
f"bud_sint_coleta_debt_jr2025_statutory,{EID},2025,1884932,1884932,1884932,NBB VOL-VZW code 17/49 schulden YE2025 DROP -5.65%,{SRC_PDF},strong,tick2433; PDF p5 native; YE2024 identical 1997837; 17 373141; 173 248141; 174 125000",
f"bud_sint_coleta_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2433; PDF p9 native; 9905 75406 + destin691 empty; overgedragen 14 1890348; YE2024 destin691 empty",
])
print("entities+budgets ok")

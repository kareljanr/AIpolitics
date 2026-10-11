from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2435_stamp.txt").read_text().strip().splitlines()
EID="vzw_izw_leuven"
SRC_PDF="src_izw_jr2025_nbb_pdf_2435"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Integratie en Zelfstandig Wonen IZW VZW,ASBL Integration et logement autonome IZW,IZW VZW (leftover city_leuven VAPH),parastatal,city_leuven,nl,https://izw.be/,info@izw.be,Riddersstraat 60 bus 02 3000 Leuven,tick2435 YE2025 Strong official native NBB PDF deposit 2026-00262459 + Strong KBO 0430.278.439 Actief 3 VE zetel Riddersstraat 60 bus 02 3000 Leuven RSZ2025 88.999; omzet70 JUMP 530078 commercial-only vs large 73; 73 DROP 802987; 76A 163; 70+73+76A DROP 1333228 envelope; bruto9900 DROP 815478 VKT; pnl DROP 10323; 9901 DROP 5047; equity JUMP 867134; assets DROP 1468447; debt DROP 601313; FTE 17.3 JUMP; kapitaalsubsidies empty; destin691 JUMP 35000; cash DROP 1444638; geldbeleggingen empty; gebouwen empty; aanbouw empty; 66A 62904; leftover mined city_leuven after Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf / MFC Combo; 3 VE Leuven+Grimbergen same KBO; NOT Kloosterstraat 6 Drongen; NOT Ferm Kinderopvang 0416.117.627; NOT Alvinnenberg 0434.390.150; NOT Hejmen 0426.383.987; NOT Staf 0431.333.660; NOT Grimbergen VAPH Zonnestraal; NOT WZC Sint-Coleta Gent 0448.294.507; NOT Home Emmaus 0451.749.190; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Helan 0464.151.037; NOT Knuffelboom 0478.310.859; NOT De Zeppelin 0454.001.867; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_izw_omzet_jr2025_statutory,{EID},2025,530078,530078,530078,NBB VKT-VZW code 70 omzet YE2025 JUMP +4.94% (commercial-only vs large 73 802987),{SRC_PDF},strong,tick2435; PDF p5 native; YE2024 identical 505113; envelope is 70+73+76A 1333228",
f"bud_izw_73_jr2025_statutory,{EID},2025,802987,802987,802987,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -4.57%,{SRC_PDF},strong,tick2435; PDF p5 native; YE2024 identical 841458; VAPH/Vlaams/Leuven/Grimbergen matrix FOI",
f"bud_izw_opbr_jr2025_statutory,{EID},2025,1333228,1333228,1333228,NBB VKT-VZW 70+73+76A bedrijfsopbrengsten YE2025 DROP -0.99% (VZW envelope; omzet commercial-only vs large 73),{SRC_PDF},strong,tick2435; PDF p5 native; YE2024 identical 1346571; envelope is 70+73+76A not omzet 70",
f"bud_izw_76A_jr2025_statutory,{EID},2025,163,163,163,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025,{SRC_PDF},strong,tick2435; PDF p5 native; YE2024 identical empty",
f"bud_izw_bruto_jr2025_statutory,{EID},2025,815478,815478,815478,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -12.89%,{SRC_PDF},strong,tick2435; PDF p5 native; YE2024 identical 936197; VKT publishes 9900",
f"bud_izw_pnl_jr2025_statutory,{EID},2025,10323,10323,10323,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -94.51%,{SRC_PDF},strong,tick2435; PDF p5 native; YE2024 identical 188046; bedrijfswinst 9901 5047 DROP; destin691 35000 JUMP",
f"bud_izw_bedrijfswinst_jr2025_statutory,{EID},2025,5047,5047,5047,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -97.27%,{SRC_PDF},strong,tick2435; PDF p5 native; YE2024 identical 184611; 62 742756 DROP; 66A 62904 vakantiegeld afboeking",
f"bud_izw_equity_jr2025_statutory,{EID},2025,867134,867134,867134,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +1.20%,{SRC_PDF},strong,tick2435; PDF p4 native; YE2024 identical 856811; kapitaalsubsidies empty; overgedragen 14 561991 DROP; bestemde fondsen 13 185000 JUMP",
f"bud_izw_assets_jr2025_statutory,{EID},2025,1468447,1468447,1468447,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -7.94%,{SRC_PDF},strong,tick2435; PDF p3 native; YE2024 identical 1595128; gebouwen 22 empty; aanbouw 27 empty; cash 1444638; 3 VE",
f"bud_izw_debt_jr2025_statutory,{EID},2025,601313,601313,601313,NBB VKT-VZW code 17/49 schulden YE2025 DROP -18.56%,{SRC_PDF},strong,tick2435; PDF p4 native; YE2024 identical 738316; 42/48 601313; 44 70999; 48 413062 DROP",
f"bud_izw_destin_jr2025_statutory,{EID},2025,35000,35000,35000,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (destin > pnl 10323),{SRC_PDF},strong,tick2435; PDF p6 native; 9905 10323 + destin691 35000; overgedragen 14 561991; YE2024 destin691 empty",
])
print("entities+budgets ok")

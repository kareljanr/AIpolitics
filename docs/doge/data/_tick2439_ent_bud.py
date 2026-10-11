from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2439_stamp.txt").read_text().strip().splitlines()
EID="vzw_slabbertjes"
SRC_PDF="src_slabbertjes_jr2025_nbb_pdf_2439"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf De Slabbertjes VZW,ASBL Kinderdagverblijf De Slabbertjes,Kinderdagverblijf De Slabbertjes VZW (leftover city_leuven CIK),parastatal,city_leuven,nl,https://www.deslabbertjes.be/,info@deslabbertjes.be,Mechelsevest 4 3000 Leuven,tick2439 YE2025 Strong official native NBB PDF deposit 2026-00138923 + Strong KBO 0411.972.064 Actief 1 VE zetel Mechelsevest 4 3000 Leuven RSZ2025 88.911; omzet70 empty; 73 empty; 76A DROP 2808; bruto9900 DROP 519885 envelope; pnl DROP 48280; 9901 DROP 47360; equity JUMP 599876; assets JUMP 662430; debt DROP 62554; FTE 10.6 JUMP; kapitaalsubsidies DROP 71963; destin691 JUMP 375400 destin>>pnl; cash DROP 138351; geldbeleggingen JUMP 257760; gebouwen DROP 208808; aanbouw empty; leftover mined city_leuven after De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf; 1 VE Leuven; Opgroeien CIK 30 plaatsen; NOT Kloosterstraat 6 Drongen; NOT Ferm Kinderopvang 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT De Wissel 0421.913.376; NOT Monte Rosa 0413.350.751; NOT IZW 0430.278.439; NOT Grauwzusters 0409.771.748 convent; NOT Kinderlach; NOT Helan; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_slabbertjes_bruto_jr2025_statutory,{EID},2025,519885,519885,519885,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -6.20% (CIK envelope; omzet 70 empty so bruto is envelope),{SRC_PDF},strong,tick2439; PDF p5 native; YE2024 identical 554244; 73 empty; 76A 2808 DROP; 62 442718 DROP",
f"bud_slabbertjes_pnl_jr2025_statutory,{EID},2025,48280,48280,48280,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -20.88%,{SRC_PDF},strong,tick2439; PDF p5 native; YE2024 identical 61023; bedrijfswinst 9901 47360 DROP; destin691 375400 JUMP destin>>pnl",
f"bud_slabbertjes_bedrijfswinst_jr2025_statutory,{EID},2025,47360,47360,47360,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -20.55%,{SRC_PDF},strong,tick2439; PDF p5 native; YE2024 identical 59613; 62 442718 DROP; 630 27786; 66A 1326",
f"bud_slabbertjes_equity_jr2025_statutory,{EID},2025,599876,599876,599876,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +7.01%,{SRC_PDF},strong,tick2439; PDF p4 native; YE2024 identical 560592; kapitaalsubsidies 71963 DROP; overgedragen 14 empty DROP; fondsen 10 91491 FLAT; bestemde fondsen 13 436423 JUMP",
f"bud_slabbertjes_assets_jr2025_statutory,{EID},2025,662430,662430,662430,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.74%,{SRC_PDF},strong,tick2439; PDF p3 native; YE2024 identical 644742; gebouwen 22 208808 DROP; cash 138351 DROP; geldbeleggingen 257760 JUMP",
f"bud_slabbertjes_debt_jr2025_statutory,{EID},2025,62554,62554,62554,NBB VKT-VZW code 17/49 schulden YE2025 DROP -25.66%,{SRC_PDF},strong,tick2439; PDF p4 native; YE2024 identical 84150; 42/48 62014; 44 3120",
f"bud_slabbertjes_cash_jr2025_statutory,{EID},2025,138351,138351,138351,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -58.34%,{SRC_PDF},strong,tick2439; PDF p3 native; YE2024 identical 332128; geldbeleggingen 50/53 257760 JUMP was 0",
f"bud_slabbertjes_destin_jr2025_statutory,{EID},2025,375400,375400,375400,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +515.18% (destin >> pnl 48280),{SRC_PDF},strong,tick2439; PDF p6 native; YE2024 identical 61023; bestemde fondsen 13 436423 JUMP FOI",
f"bud_slabbertjes_kapitaalsubsidies_jr2025_statutory,{EID},2025,71963,71963,71963,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -11.11%,{SRC_PDF},strong,tick2439; PDF p4 native; YE2024 identical 80958",
f"bud_slabbertjes_76A_jr2025_statutory,{EID},2025,2808,2808,2808,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -38.10%,{SRC_PDF},strong,tick2439; PDF p5 native; YE2024 identical 4536",
])
print("entities+budgets ok")

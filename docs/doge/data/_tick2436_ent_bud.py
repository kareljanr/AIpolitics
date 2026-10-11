from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2436_stamp.txt").read_text().strip().splitlines()
EID="vzw_avida"
SRC_PDF="src_avida_jr2025_nbb_pdf_2436"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Avida VZW,ASBL Avida,Avida VZW (leftover city_gent WZC Conecto+Exalta merger),parastatal,city_gent,nl,https://www.avida.be/,info@avida.be,Molenaarsstraat 34 9000 Gent,tick2436 YE2025 Strong official native NBB PDF deposit 2026-00206951 + Strong KBO 0438.814.241 Actief 7 VE zetel Molenaarsstraat 34 9000 Gent RSZ2025 87.101; omzet70 JUMP 42857494 envelope not commercial-only vs 73; 73 JUMP 11552982; 76A 37803; 70/76A JUMP 55138086; bruto9900 empty VOL; pnl DROP -784162; 9901 DROP -484969; equity JUMP 32531263; assets JUMP 67049389; debt JUMP 34448367; FTE 624.2 JUMP; kapitaalsubsidies JUMP 10271770; destin691 empty; cash JUMP 6847926; geldbeleggingen DROP 0; gebouwen JUMP 43981165; aanbouw JUMP 1256730; leftover mined city_gent after IZW / Ferm Kinderopvang / WZC Sint-Coleta Gent / Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 7 VE Gent+Lochristi+Damme+Beveren same KBO; Conecto 0433.961.964 absorbed 01.01.2025; naam Avida since 11.12.2024 voorheen Exalta; NOT Kloosterstraat 6 Drongen; NOT WZC Sint-Coleta Gent 0448.294.507; NOT Home Emmaus 0451.749.190; NOT De Foyer 0413.796.456; NOT Groep Zorg H. Familie; NOT IZW 0430.278.439; NOT Ferm Kinderopvang 0416.117.627; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_avida_omzet_jr2025_statutory,{EID},2025,42857494,42857494,42857494,NBB VOL-VZW code 70 omzet YE2025 JUMP +119.55% (ouderenzorg envelope; not commercial-only vs 73 11552982; merger-driven),{SRC_PDF},strong,tick2436; PDF p7 native; YE2024 identical 19520867; envelope is omzet 70; pro-forma combined 2024 42111174",
f"bud_avida_73_jr2025_statutory,{EID},2025,11552982,11552982,11552982,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +48.66%,{SRC_PDF},strong,tick2436; PDF p7 native; YE2024 identical 7771490; 731 5867; 732 25155; 733 11521960; Zorg/RIZIV/steden matrix FOI",
f"bud_avida_opbr_jr2025_statutory,{EID},2025,55138086,55138086,55138086,NBB VOL-VZW 70/76A bedrijfsopbrengsten YE2025 JUMP +97.14% (VZW operating income; envelope is omzet 70 not commercial-only),{SRC_PDF},strong,tick2436; PDF p7 native; YE2024 identical 27968542; 74 689807; 76A 37803",
f"bud_avida_76A_jr2025_statutory,{EID},2025,37803,37803,37803,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP,{SRC_PDF},strong,tick2436; PDF p7 native; YE2024 identical 31696",
f"bud_avida_pnl_jr2025_statutory,{EID},2025,-784162,-784162,-784162,NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 DROP -88.59% (meer verlies; consecutive loss years),{SRC_PDF},strong,tick2436; PDF p8 native; YE2024 identical -415792; bedrijfswinst 9901 -484969 DROP; destin691 empty; commissaris -784161.76",
f"bud_avida_bedrijfswinst_jr2025_statutory,{EID},2025,-484969,-484969,-484969,NBB VOL-VZW code 9901 bedrijfsverlies YE2025 DROP -91.16%,{SRC_PDF},strong,tick2436; PDF p7 native; YE2024 identical -253696; 62 40657596 JUMP; 630 3074601; 66A 85058",
f"bud_avida_equity_jr2025_statutory,{EID},2025,32531263,32531263,32531263,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +141.02%,{SRC_PDF},strong,tick2436; PDF p6 native; YE2024 identical 13497519; kapitaalsubsidies 10271770 JUMP; overgedragen 14 8676365; fondsen 10 12928239 JUMP; bestemde fondsen 13 654148 FLAT",
f"bud_avida_assets_jr2025_statutory,{EID},2025,67049389,67049389,67049389,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +113.52%,{SRC_PDF},strong,tick2436; PDF p5 native; YE2024 identical 31401611; gebouwen 22 43981165 JUMP; aanbouw 27 1256730 JUMP; cash 6847926; commissaris 67049389.05",
f"bud_avida_debt_jr2025_statutory,{EID},2025,34448367,34448367,34448367,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +93.22%,{SRC_PDF},strong,tick2436; PDF p6 native; YE2024 identical 17828901; 17 24625739; 173 24385236; 42/48 8793050",
f"bud_avida_cash_jr2025_statutory,{EID},2025,6847926,6847926,6847926,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +243.60%,{SRC_PDF},strong,tick2436; PDF p5 native; YE2024 identical 1993021; geldbeleggingen 50/53 0 DROP was 4000000",
f"bud_avida_kapitaalsubsidies_jr2025_statutory,{EID},2025,10271770,10271770,10271770,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 JUMP +273.89%,{SRC_PDF},strong,tick2436; PDF p6 native; YE2024 identical 2747291; merger Conecto opening",
])
print("entities+budgets ok")

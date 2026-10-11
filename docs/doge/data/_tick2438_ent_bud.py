from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2438_stamp.txt").read_text().strip().splitlines()
EID="vzw_de_wissel"
SRC_PDF="src_de_wissel_jr2025_nbb_pdf_2438"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},De Wissel VZW,ASBL De Wissel,De Wissel VZW (leftover city_leuven OVBJ CANO-jeugdhulp),parastatal,city_leuven,nl,https://www.wissel.be/,info@wissel.be,Parkstraat 64 3000 Leuven,tick2438 YE2025 Strong official native NBB PDF deposit 2026-00213923 + Strong KBO 0421.913.376 Actief 1 VE zetel Parkstraat 64 3000 Leuven RSZ2025 87.991; omzet70 empty; 73 JUMP 8101474; 76A 200; 70/76A JUMP 8576450 envelope; bruto9900 empty VOL; pnl JUMP 101865; 9901 JUMP 109342; equity JUMP 3645083; assets JUMP 6189923; debt JUMP 2466620; FTE 82.7 JUMP; kapitaalsubsidies JUMP 1651366; destin691 JUMP 200000; cash JUMP 656811; geldbeleggingen DROP empty; gebouwen JUMP 3467123; aanbouw JUMP 366190; leftover mined city_leuven after Monte Rosa / IZW / Ferm Kinderopvang / Alvinnenberg / Hejmen / Staf / Annuntiaten / Woonzorgnet-Dijleland; 1 VE Leuven; Opgroeien CANO/OVBJ; NOT Kloosterstraat 6 Drongen; NOT Monte Rosa 0413.350.751; NOT MFC Combo; NOT Jeugdhulp Don Bosco 0408.666.344; NOT Ferm Kinderopvang 0416.117.627; NOT IZW 0430.278.439; NOT Avida 0438.814.241; NOT Witje Wiebel; NOT Beregoed; NOT Windekind; NOT Helan; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_de_wissel_opbr_jr2025_statutory,{EID},2025,8576450,8576450,8576450,NBB VOL-VZW 70/76A bedrijfsopbrengsten YE2025 JUMP +8.55% (VZW envelope; omzet 70 empty so 70/76A is envelope vs large 73),{SRC_PDF},strong,tick2438; PDF p6 native; YE2024 identical 7900651; 73 8101474; 74 474775 JUMP; 76A 200",
f"bud_de_wissel_73_jr2025_statutory,{EID},2025,8101474,8101474,8101474,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +6.80%,{SRC_PDF},strong,tick2438; PDF p6 native; YE2024 identical 7585632; 731 102807 JUMP; 733 7998667 JUMP; Opgroeien matrix FOI",
f"bud_de_wissel_pnl_jr2025_statutory,{EID},2025,101865,101865,101865,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP (was -97512),{SRC_PDF},strong,tick2438; PDF p7 native; YE2024 identical -97512; bedrijfswinst 9901 109342 JUMP; destin691 200000 JUMP destin>pnl",
f"bud_de_wissel_bedrijfswinst_jr2025_statutory,{EID},2025,109342,109342,109342,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP (was -125021),{SRC_PDF},strong,tick2438; PDF p6 native; YE2024 identical -125021; 62 6477401 JUMP; 61 1702588 FLAT; 630 182536 JUMP",
f"bud_de_wissel_equity_jr2025_statutory,{EID},2025,3645083,3645083,3645083,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +77.15%,{SRC_PDF},strong,tick2438; PDF p5 native; YE2024 identical 2057619; kapitaalsubsidies 1651366 JUMP; overgedragen 14 9337 DROP; fondsen 10 850000 JUMP; bestemde fondsen 13 1134379 JUMP",
f"bud_de_wissel_assets_jr2025_statutory,{EID},2025,6189923,6189923,6189923,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +35.20%,{SRC_PDF},strong,tick2438; PDF p4 native; YE2024 identical 4578283; gebouwen 22 3467123 JUMP; aanbouw 27 366190 JUMP; cash 656811; geldbeleggingen empty DROP",
f"bud_de_wissel_debt_jr2025_statutory,{EID},2025,2466620,2466620,2466620,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +1.38%,{SRC_PDF},strong,tick2438; PDF p5 native; YE2024 identical 2432922; 17 269599; 173 269599; 42/48 1889915",
f"bud_de_wissel_cash_jr2025_statutory,{EID},2025,656811,656811,656811,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +101.04%,{SRC_PDF},strong,tick2438; PDF p4 native; YE2024 identical 326708; geldbeleggingen 50/53 empty DROP was 750000",
f"bud_de_wissel_destin_jr2025_statutory,{EID},2025,200000,200000,200000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was empty; destin > pnl 101865),{SRC_PDF},strong,tick2438; PDF p8 native; YE2024 empty; bestemde fondsen 13 1134379 JUMP FOI",
f"bud_de_wissel_kapitaalsubsidies_jr2025_statutory,{EID},2025,1651366,1651366,1651366,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 JUMP +62.57%,{SRC_PDF},strong,tick2438; PDF p5 native; YE2024 identical 1015768",
f"bud_de_wissel_74_jr2025_statutory,{EID},2025,474775,474775,474775,NBB VOL-VZW code 74 andere bedrijfsopbrengsten YE2025 JUMP +51.49%,{SRC_PDF},strong,tick2438; PDF p6 native; YE2024 identical 313399",
])
print("entities+budgets ok")

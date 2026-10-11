from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2437_stamp.txt").read_text().strip().splitlines()
EID="vzw_monte_rosa"
SRC_PDF="src_monte_rosa_jr2025_nbb_pdf_2437"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Monte Rosa VZW,ASBL Monte Rosa,Monte Rosa VZW (leftover city_leuven OVBJ jeugdzorg),parastatal,city_leuven,nl,https://monterosa.be/,info@monterosa.be,Heidebergstraat 249 3010 Leuven,tick2437 YE2025 Strong official native NBB PDF deposit 2026-00093041 + Strong KBO 0413.350.751 Actief 4 VE zetel Heidebergstraat 249 3010 Leuven RSZ2025 87.991; omzet70 empty; 73 JUMP 5323280; 76A empty; 70/76A FLAT 5424143 envelope; bruto9900 empty VOL; pnl JUMP 348642; 9901 JUMP 369456; equity JUMP 5395536; assets JUMP 7358796; debt JUMP 1963260; FTE 63.0 DROP; kapitaalsubsidies DROP 1749682; destin691 JUMP 2050000; cash JUMP 823541; geldbeleggingen JUMP 1662593; gebouwen DROP 1478450; aanbouw JUMP 2333389; leftover mined city_leuven after IZW / Ferm Kinderopvang / Alvinnenberg / Hejmen / Staf / Annuntiaten / Woonzorgnet-Dijleland; also leftover mined city_herent + leftover mined city_antwerpen same KBO; 4 VE Leuven+Herent+Deurne; Opgroeien OVBJ HCO 27693; NOT Kloosterstraat 6 Drongen; NOT Jeugdhulp Don Bosco 0408.666.344; NOT Ferm Kinderopvang 0416.117.627; NOT IZW 0430.278.439; NOT Avida 0438.814.241; NOT Konekt 0524.936.680; NOT Witje Wiebel; NOT Beregoed; NOT Windekind; NOT Helan; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_monte_rosa_opbr_jr2025_statutory,{EID},2025,5424143,5424143,5424143,NBB VOL-VZW 70/76A bedrijfsopbrengsten YE2025 FLAT +0.04% (VZW envelope; omzet 70 empty so 70/76A is envelope vs large 73),{SRC_PDF},strong,tick2437; PDF p7 native; YE2024 identical 5421846; 73 5323280; 74 100863 DROP; 76A empty",
f"bud_monte_rosa_73_jr2025_statutory,{EID},2025,5323280,5323280,5323280,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +0.93%,{SRC_PDF},strong,tick2437; PDF p7 native; YE2024 identical 5274009; 731 40044 DROP; 733 5283236 JUMP; Opgroeien matrix FOI",
f"bud_monte_rosa_pnl_jr2025_statutory,{EID},2025,348642,348642,348642,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +63.55%,{SRC_PDF},strong,tick2437; PDF p8 native; YE2024 identical 213173; bedrijfswinst 9901 369456 JUMP; destin691 2050000 JUMP destin>>pnl",
f"bud_monte_rosa_bedrijfswinst_jr2025_statutory,{EID},2025,369456,369456,369456,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +71.60%,{SRC_PDF},strong,tick2437; PDF p7 native; YE2024 identical 215304; 62 4348869 JUMP; 61 363665 DROP; 60 204493 DROP; 630 84853 DROP; 66A 84",
f"bud_monte_rosa_equity_jr2025_statutory,{EID},2025,5395536,5395536,5395536,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +6.11%,{SRC_PDF},strong,tick2437; PDF p6 native; YE2024 identical 5085007; kapitaalsubsidies 1749682 DROP; overgedragen 14 223125 DROP; fondsen 10 294730 FLAT; bestemde fondsen 13 3128000 JUMP",
f"bud_monte_rosa_assets_jr2025_statutory,{EID},2025,7358796,7358796,7358796,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +4.81%,{SRC_PDF},strong,tick2437; PDF p5 native; YE2024 identical 7020817; gebouwen 22 1478450 DROP; aanbouw 27 2333389 JUMP; cash 823541; geldbeleggingen 1662593",
f"bud_monte_rosa_debt_jr2025_statutory,{EID},2025,1963260,1963260,1963260,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +1.42%,{SRC_PDF},strong,tick2437; PDF p6 native; YE2024 identical 1935811; 17 1095964; 173 1095964; 42/48 855043",
f"bud_monte_rosa_cash_jr2025_statutory,{EID},2025,823541,823541,823541,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +43.02%,{SRC_PDF},strong,tick2437; PDF p5 native; YE2024 identical 575837; geldbeleggingen 50/53 1662593 JUMP was 1604926; jaarverslag pandkorf + termijndeposito's",
f"bud_monte_rosa_destin_jr2025_statutory,{EID},2025,2050000,2050000,2050000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +1063.61% (destin >> pnl 348642),{SRC_PDF},strong,tick2437; PDF p9 native; YE2024 identical 176176; investeringsfonds 2428000 + fonds sociaal passief FOI",
f"bud_monte_rosa_kapitaalsubsidies_jr2025_statutory,{EID},2025,1749682,1749682,1749682,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -2.13%,{SRC_PDF},strong,tick2437; PDF p6 native; YE2024 identical 1787794",
f"bud_monte_rosa_74_jr2025_statutory,{EID},2025,100863,100863,100863,NBB VOL-VZW code 74 andere bedrijfsopbrengsten YE2025 DROP -31.77%,{SRC_PDF},strong,tick2437; PDF p7 native; YE2024 identical 147837",
])
print("entities+budgets ok")

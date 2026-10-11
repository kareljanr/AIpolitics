from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2442_stamp.txt").read_text().strip().splitlines()
EID="vzw_anemoontje"
SRC_PDF="src_anemoontje_jr2025_nbb_pdf_2442"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf t Anemoontje vzw,ASBL Kinderdagverblijf t Anemoontje,Kinderdagverblijf t Anemoontje VZW (leftover city_leuven CIK),parastatal,city_leuven,nl,https://www.kinderdagverblijfanemoontje.be/,info@kinderdagverblijfanemoontje.be,Bosstraat 30 3012 Leuven,tick2442 YE2025 Strong official native NBB PDF deposit 2026-00213975 + Strong KBO 0413.354.612 Actief 1 VE 2.150.886.809 Bosstraat 30 3012 Leuven RSZ2025 88.911; omzet70 JUMP 136595 commercial-only; 73 JUMP 698331; 76A empty; 70+73 JUMP 834926 envelope; bruto9900 JUMP 759661; pnl JUMP 105278; 9901 JUMP 109330; equity JUMP 1329241; assets JUMP 1575233; debt DROP 245992; FTE 8.1 DROP; kapitaalsubsidies DROP 515543; destin691 JUMP 598014 destin>>pnl; cash JUMP 332675; geldbeleggingen FLAT 250000; gebouwen DROP 898992; leftover mined city_leuven after De Hummeltjes / De Ukkies / De Slabbertjes / De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje; 1 VE Leuven; Opgroeien CIK 40 plaatsen; NOT Duinhuisjes VE t Anemoontje 2.375.207.425; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT De Wissel; NOT Monte Rosa; NOT IZW; NOT De Hummeltjes; NOT De Ukkies; NOT Kinderlach; NOT Helan; NOT Kloosterstraat 6 Drongen; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco 2026-00259885 1.10MB re-HEAD next; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_anemoontje_opbr_jr2025_statutory,{EID},2025,834926,834926,834926,NBB VKT-VZW code 70+73+76A bedrijfsopbrengsten YE2025 JUMP +9.29% (VZW envelope; omzet 70 136595 commercial-only vs large 73 698331),{SRC_PDF},strong,tick2442; PDF p5 native; YE2024 identical 763975; 73 698331 JUMP; 76A empty",
f"bud_anemoontje_omzet_jr2025_statutory,{EID},2025,136595,136595,136595,NBB VKT-VZW code 70 omzet YE2025 JUMP +1.68% (ouderbijdragen; commercial-only vs large 73),{SRC_PDF},strong,tick2442; PDF p5 native; YE2024 identical 134340",
f"bud_anemoontje_73_jr2025_statutory,{EID},2025,698331,698331,698331,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +10.91%,{SRC_PDF},strong,tick2442; PDF p5 native; YE2024 identical 629635",
f"bud_anemoontje_pnl_jr2025_statutory,{EID},2025,105278,105278,105278,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +90.22%,{SRC_PDF},strong,tick2442; PDF p5 native; YE2024 identical 55346; bedrijfswinst 9901 109330 JUMP; destin691 598014 JUMP destin>>pnl",
f"bud_anemoontje_bedrijfswinst_jr2025_statutory,{EID},2025,109330,109330,109330,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +83.23%,{SRC_PDF},strong,tick2442; PDF p5 native; YE2024 identical 59669; 62 573449 JUMP; 630 74800 FLAT",
f"bud_anemoontje_equity_jr2025_statutory,{EID},2025,1329241,1329241,1329241,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.21%,{SRC_PDF},strong,tick2442; PDF p4 native; YE2024 identical 1263408; kapitaalsubsidies 515543 DROP; overgedragen 14 202982 DROP; fondsen 10 12702 FLAT; bestemde fondsen 13 598014 JUMP",
f"bud_anemoontje_assets_jr2025_statutory,{EID},2025,1575233,1575233,1575233,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +3.53%,{SRC_PDF},strong,tick2442; PDF p3 native; YE2024 identical 1521581; gebouwen 22 898992 DROP; cash 332675 JUMP; geldbeleggingen 250000 FLAT",
f"bud_anemoontje_debt_jr2025_statutory,{EID},2025,245992,245992,245992,NBB VKT-VZW code 17/49 schulden YE2025 DROP -4.72%,{SRC_PDF},strong,tick2442; PDF p4 native; YE2024 identical 258172; 17 129824 DROP; 42/48 115026",
f"bud_anemoontje_cash_jr2025_statutory,{EID},2025,332675,332675,332675,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +47.92%,{SRC_PDF},strong,tick2442; PDF p3 native; YE2024 identical 224895; geldbeleggingen 50/53 250000 FLAT",
f"bud_anemoontje_destin_jr2025_statutory,{EID},2025,598014,598014,598014,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP from empty (destin >> pnl 105278),{SRC_PDF},strong,tick2442; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 598014 JUMP FOI",
f"bud_anemoontje_62_jr2025_statutory,{EID},2025,573449,573449,573449,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +2.12%,{SRC_PDF},strong,tick2442; PDF p5 native; YE2024 identical 561571; FTE 8.1 DROP",
])
print("entities+budgets ok")

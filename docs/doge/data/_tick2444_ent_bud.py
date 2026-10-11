from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2444_stamp.txt").read_text().strip().splitlines()
EID="vzw_wigwam"
SRC_PDF="src_wigwam_jr2025_nbb_pdf_2444"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Wigwam vzw / KDV Wigwam,ASBL Wigwam,Wigwam VZW (leftover city_leuven CIK),parastatal,city_leuven,nl,https://www.dewigwam.be/,info@dewigwam.be,Diestsesteenweg 379c 3010 Leuven,tick2444 YE2025 Strong official native NBB PDF deposit 2026-00159445 + Strong KBO 0435.015.207 Actief 1 VE 2.155.773.431 Diestsesteenweg 379/c 3010 Leuven RSZ2025 88.911; omzet70 empty VKT; 73 empty VKT; 76A JUMP 22522; bruto9900 JUMP 1068827 envelope; pnl DROP 36; 9901 DROP 26727; equity DROP 896597; assets DROP 2053811; debt DROP 1157214; FTE 18.6 JUMP; kapitaalsubsidies DROP 644459; destin691 JUMP 149849 destin>>pnl; cash JUMP 207008; geldbeleggingen empty; gebouwen DROP 1739199; leftover mined city_leuven after Jeugdhulp Don Bosco / t Anemoontje / De Slabbertjes / De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje; 1 VE Leuven; Opgroeien CIK 45 plaatsen; NOT Kloosterstraat 6 Drongen; NOT t Anemoontje 0413.354.612; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT De Wissel 0421.913.376; NOT Monte Rosa 0413.350.751; NOT IZW 0430.278.439; NOT Jeugdhulp Don Bosco 0408.666.344; NOT Kinderlach 0450.275.186; NOT Helan; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_wigwam_bruto_jr2025_statutory,{EID},2025,1068827,1068827,1068827,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +1.03% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2444; PDF p5 native; YE2024 identical 1057980; 76A 22522 JUMP",
f"bud_wigwam_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2444; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_wigwam_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2444; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 1068827",
f"bud_wigwam_pnl_jr2025_statutory,{EID},2025,36,36,36,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -99.96%,{SRC_PDF},strong,tick2444; PDF p5 native; YE2024 identical 98132; bedrijfswinst 9901 26727 DROP; destin691 149849 JUMP destin>>pnl",
f"bud_wigwam_bedrijfswinst_jr2025_statutory,{EID},2025,26727,26727,26727,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -78.84%,{SRC_PDF},strong,tick2444; PDF p5 native; YE2024 identical 126283; 62 946597 JUMP; 630 84903 DROP; 66A 5113 JUMP",
f"bud_wigwam_equity_jr2025_statutory,{EID},2025,896597,896597,896597,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -3.70%,{SRC_PDF},strong,tick2444; PDF p4 native; YE2024 identical 931072; kapitaalsubsidies 644459 DROP; overgedragen 14 empty; fondsen 10 0; bestemde fondsen 13 252138 JUMP",
f"bud_wigwam_assets_jr2025_statutory,{EID},2025,2053811,2053811,2053811,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -3.73%,{SRC_PDF},strong,tick2444; PDF p3 native; YE2024 identical 2133288; gebouwen 22 1739199 DROP; cash 207008 JUMP; geldbeleggingen empty",
f"bud_wigwam_debt_jr2025_statutory,{EID},2025,1157214,1157214,1157214,NBB VKT-VZW code 17/49 schulden YE2025 DROP -3.74%,{SRC_PDF},strong,tick2444; PDF p4 native; YE2024 identical 1202216; 17 940064 DROP; 42/48 215365 JUMP",
f"bud_wigwam_cash_jr2025_statutory,{EID},2025,207008,207008,207008,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +1.55%,{SRC_PDF},strong,tick2444; PDF p3 native; YE2024 identical 203846; geldbeleggingen 50/53 empty",
f"bud_wigwam_destin_jr2025_statutory,{EID},2025,149849,149849,149849,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +52.70% (destin 149849 >> pnl 36; 14P 149814 transferred),{SRC_PDF},strong,tick2444; PDF p6 native; YE2024 destin 98132; bestemde fondsen 13 252138 JUMP FOI",
f"bud_wigwam_62_jr2025_statutory,{EID},2025,946597,946597,946597,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +13.43%,{SRC_PDF},strong,tick2444; PDF p5 native; YE2024 identical 834492; FTE 18.6 JUMP",
])
print("entities+budgets ok")

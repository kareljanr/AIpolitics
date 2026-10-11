from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2449_stamp.txt").read_text().strip().splitlines()
EID="vzw_familia_genk"
SRC_PDF="src_familia_jr2025_nbb_pdf_2449"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf Familia VZW,ASBL Kinderdagverblijf Familia,Kinderdagverblijf Familia VZW (leftover city_genk CIK),parastatal,city_genk,nl,https://kdvfamilia.be,info@kdvfamilia.be,Halmstraat 3 3600 Genk,tick2449 YE2025 Strong official native NBB PDF deposit 2026-00272867 + Strong KBO 0461.401.779 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 JUMP 1249649 commercial-only; 73 JUMP 6232638 subsidies; 76A DROP 26485; opbr70/76A JUMP 7571995 envelope; pnl JUMP 645105; 9901 JUMP 642132; equity JUMP 4554709; assets JUMP 5674553; debt DROP 1065188; FTE 103.5 JUMP; kapitaalsubsidies DROP 1169221; destin691 JUMP 462255; 791 empty; cash DROP 256788; geldbeleggingen JUMP 1334280; leftover mined city_genk after BKO GENK-OOST; 1 VE CIK not private; NOT Kloosterstraat 6 Drongen; NOT BKO GENK-OOST 0475.432.830 remine; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_familia_opbr_jr2025_statutory,{EID},2025,7571995,7571995,7571995,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +7.38% (envelope because omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2449; PDF p6 native; YE2024 identical 7051844; omzet 1249649 commercial-only; 73 6232638; 76A 26485 DROP",
f"bud_familia_omzet_jr2025_statutory,{EID},2025,1249649,1249649,1249649,NBB VOL-VZW code 70 omzet YE2025 JUMP +3.44% (commercial-only dagprijs vs large 73; envelope is 70/76A),{SRC_PDF},strong,tick2449; PDF p6 native; YE2024 identical 1208052; 6.9 dagprijs 1249649",
f"bud_familia_73_jr2025_statutory,{EID},2025,6232638,6232638,6232638,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +8.41% (733 subsidies only),{SRC_PDF},strong,tick2449; PDF p6 native; YE2024 identical 5748993; FOI Opgroeien split behind 73 6232638",
f"bud_familia_pnl_jr2025_statutory,{EID},2025,645105,645105,645105,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +5.63% (was 610700),{SRC_PDF},strong,tick2449; PDF p7 native; YE2024 identical 610700; bedrijfswinst 9901 642132 JUMP; destin691 462255 JUMP",
f"bud_familia_bedrijfswinst_jr2025_statutory,{EID},2025,642132,642132,642132,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +5.12% (was 610849),{SRC_PDF},strong,tick2449; PDF p6 native; YE2024 identical 610849; 62 5952762 JUMP; 630 220335 JUMP; 66A 1915 DROP; 635/9 9823",
f"bud_familia_equity_jr2025_statutory,{EID},2025,4554709,4554709,4554709,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +14.49%,{SRC_PDF},strong,tick2449; PDF p4 native; YE2024 identical 3978358; kapitaalsubsidies 1169221 DROP; overgedragen 14 358479 JUMP; fondsen 10 454161 FLAT; bestemde fondsen 13 2572848 JUMP",
f"bud_familia_assets_jr2025_statutory,{EID},2025,5674553,5674553,5674553,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +8.17%,{SRC_PDF},strong,tick2449; PDF p4 native; YE2024 identical 5246173; MVA 22/27 3159296 DROP; cash 256788 DROP; geldbeleggingen 1334280 JUMP; aanbouw 27 604487 JUMP",
f"bud_familia_debt_jr2025_statutory,{EID},2025,1065188,1065188,1065188,NBB VOL-VZW code 17/49 schulden YE2025 DROP -12.90%,{SRC_PDF},strong,tick2449; PDF p5 native; YE2024 identical 1222982; 17 172500 DROP; 42/48 860980 DROP",
f"bud_familia_cash_jr2025_statutory,{EID},2025,256788,256788,256788,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -14.75%,{SRC_PDF},strong,tick2449; PDF p4 native; YE2024 identical 301202; geldbeleggingen 50/53 1334280 JUMP",
f"bud_familia_destin_jr2025_statutory,{EID},2025,462255,462255,462255,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +0.37% (791 empty; 13 JUMP 2572848),{SRC_PDF},strong,tick2449; PDF p8 native; YE2024 destin 460535; overgedragen 14 358479 JUMP FOI",
f"bud_familia_62_jr2025_statutory,{EID},2025,5952762,5952762,5952762,NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +5.81%,{SRC_PDF},strong,tick2449; PDF p6 native; YE2024 identical 5626139; FTE 103.5 JUMP",
])
print("entities+budgets ok")

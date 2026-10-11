from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2448_stamp.txt").read_text().strip().splitlines()
EID="vzw_peutertuinen_go_mariakerke"
SRC_PDF="src_peutertuinen_jr2025_nbb_pdf_2448"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Peutertuinen Gemeenschapsonderwijs Mariakerke VZW (Peutertuinen GO! Mariakerke),ASBL Peutertuinen GO Mariakerke,Peutertuinen GO! Mariakerke VZW (leftover city_gent CIK),parastatal,city_gent,nl,https://peutertuin.be,info@peutertuin.be,Amand Casier de ter Bekenlaan 26 9030 Gent,tick2448 YE2025 Strong official native NBB PDF deposit 2026-00288310 + Strong KBO 0410.221.116 Actief 2 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A DROP 0; bruto9900 DROP 872268 envelope; pnl JUMP 115219; 9901 JUMP 126095; equity JUMP 1316171; assets JUMP 1658146; debt JUMP 341975; FTE 13.7 DROP; kapitaalsubsidies JUMP 491875; destin691 empty FLAT; 791 empty; cash DROP 550474; geldbeleggingen empty; leftover mined city_gent after Avida / WZC Sint-Coleta / Home Emmaus / Witje Wiebel / Beregoed / Windekind; 2 VE CIK not private; NOT Kloosterstraat 6 Drongen; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Stad Gent peutertuinen; NOT Villa Boempatat 0660.616.520 YE2024; NOT COB Annuntiaten 0447.017.570; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_peutertuinen_bruto_jr2025_statutory,{EID},2025,872268,872268,872268,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -6.60% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2448; PDF p5 native; YE2024 identical 933927; 76A 0 DROP",
f"bud_peutertuinen_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2448; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_peutertuinen_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2448; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 872268",
f"bud_peutertuinen_pnl_jr2025_statutory,{EID},2025,115219,115219,115219,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +58.76% (was 72573),{SRC_PDF},strong,tick2448; PDF p5 native; YE2024 identical 72573; bedrijfswinst 9901 126095 JUMP; destin691 empty FLAT",
f"bud_peutertuinen_bedrijfswinst_jr2025_statutory,{EID},2025,126095,126095,126095,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +72.77% (was 72986),{SRC_PDF},strong,tick2448; PDF p5 native; YE2024 identical 72986; 62 784405 DROP; 630 27380 DROP; 66A 53048 JUMP; 635/9 -120000",
f"bud_peutertuinen_equity_jr2025_statutory,{EID},2025,1316171,1316171,1316171,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +33.99%,{SRC_PDF},strong,tick2448; PDF p4 native; YE2024 identical 982265; kapitaalsubsidies 491875 JUMP; overgedragen 14 824297 JUMP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_peutertuinen_assets_jr2025_statutory,{EID},2025,1658146,1658146,1658146,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +31.59%,{SRC_PDF},strong,tick2448; PDF p3 native; YE2024 identical 1260098; MVA 22/27 1011815 JUMP; cash 550474 DROP; geldbeleggingen empty; aanbouw 27 627877 JUMP",
f"bud_peutertuinen_debt_jr2025_statutory,{EID},2025,341975,341975,341975,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +116.67%,{SRC_PDF},strong,tick2448; PDF p4 native; YE2024 identical 157833; 17 180067 JUMP; 42/48 159408 JUMP",
f"bud_peutertuinen_cash_jr2025_statutory,{EID},2025,550474,550474,550474,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -17.52%,{SRC_PDF},strong,tick2448; PDF p3 native; YE2024 identical 667369; geldbeleggingen 50/53 empty",
f"bud_peutertuinen_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (791 empty; 13 empty; pnl 115219 not destined),{SRC_PDF},strong,tick2448; PDF p6 native; YE2024 destin empty; overgedragen 14 824297 JUMP FOI",
f"bud_peutertuinen_62_jr2025_statutory,{EID},2025,784405,784405,784405,NBB VKT-VZW code 62 bezoldigingen YE2025 DROP -3.81%,{SRC_PDF},strong,tick2448; PDF p5 native; YE2024 identical 815459; FTE 13.7 DROP",
])
print("entities+budgets ok")

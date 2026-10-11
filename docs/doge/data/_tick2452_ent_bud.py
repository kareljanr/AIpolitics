from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2452_stamp.txt").read_text().strip().splitlines()
EID="vzw_harlekijntjes_tielt"
SRC_PDF="src_harlekijntjes_jr2025_nbb_pdf_2452"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},KINDEROPVANG De Harlekijntjes VZW,ASBL KINDEROPVANG De Harlekijntjes,KINDEROPVANG De Harlekijntjes VZW (leftover city_tielt CIK),parastatal,city_tielt,nl,https://deharlekijntjes.be,info@deharlekijntjes.be,Keidamstraat 77 8700 Tielt,tick2452 YE2025 Strong official native NBB PDF deposit 2026-00161949 + Strong KBO 0407.700.403 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A JUMP 1700; bruto JUMP 1896924 envelope; pnl DROP 144205; 9901 DROP 136158; equity JUMP 1405811; assets JUMP 1693592; debt DROP 287780; FTE 27 DROP; kapitaalsubsidies DROP 203433; destin691 JUMP 661844; 791 empty; cash DROP 141324; geldbeleggingen JUMP 847580; leftover mined city_tielt after Kinderdagverblijf De Hartjes Ninove different-KBO skip; 1 VE CIK not private; NOT Kloosterstraat 6 Drongen; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT OKO & ZO 0862.154.608 leftover city_zele; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_harlekijntjes_bruto_jr2025_statutory,{EID},2025,1896924,1896924,1896924,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +1.61% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2452; PDF p5 native; YE2024 identical 1866805; 76A JUMP 1700",
f"bud_harlekijntjes_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2452; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_harlekijntjes_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2452; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 1896924",
f"bud_harlekijntjes_pnl_jr2025_statutory,{EID},2025,144205,144205,144205,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -18.32% (was 176554),{SRC_PDF},strong,tick2452; PDF p5 native; YE2024 identical 176554; bedrijfswinst 9901 136158 DROP; destin691 JUMP 661844",
f"bud_harlekijntjes_bedrijfswinst_jr2025_statutory,{EID},2025,136158,136158,136158,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -3.56% (was 141180),{SRC_PDF},strong,tick2452; PDF p5 native; YE2024 identical 141180; 62 1705156 JUMP; 630 44081 DROP; 66A 10248 JUMP",
f"bud_harlekijntjes_equity_jr2025_statutory,{EID},2025,1405811,1405811,1405811,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +10.16%,{SRC_PDF},strong,tick2452; PDF p4 native; YE2024 identical 1276125; kapitaalsubsidies 203433 DROP; overgedragen 14 165461 DROP; fondsen 10 375073 FLAT; bestemde fondsen 13 661844 JUMP",
f"bud_harlekijntjes_assets_jr2025_statutory,{EID},2025,1693592,1693592,1693592,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +7.90%,{SRC_PDF},strong,tick2452; PDF p3 native; YE2024 identical 1569532; MVA 22/27 479005 DROP; cash 141324 DROP; geldbeleggingen 847580 JUMP; aanbouw 27 2040 JUMP",
f"bud_harlekijntjes_debt_jr2025_statutory,{EID},2025,287780,287780,287780,NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.92%,{SRC_PDF},strong,tick2452; PDF p4 native; YE2024 identical 293407; 42/48 287297 DROP",
f"bud_harlekijntjes_cash_jr2025_statutory,{EID},2025,141324,141324,141324,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -79.98%,{SRC_PDF},strong,tick2452; PDF p3 native; YE2024 identical 705796; geldbeleggingen 50/53 847580 JUMP +326.63%",
f"bud_harlekijntjes_destin_jr2025_statutory,{EID},2025,661844,661844,661844,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was empty; 791 empty; 13 661844; 80pct nettowinst to investeringsfonds per toelichting),{SRC_PDF},strong,tick2452; PDF p6 native; YE2024 destin empty; overgedragen 14 165461 DROP FOI",
f"bud_harlekijntjes_62_jr2025_statutory,{EID},2025,1705156,1705156,1705156,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +1.98%,{SRC_PDF},strong,tick2452; PDF p5 native; YE2024 identical 1671991; FTE 27 DROP",
])
print("entities+budgets ok")

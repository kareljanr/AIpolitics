from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2453_stamp.txt").read_text().strip().splitlines()
EID="vzw_oko_zo_zele"
SRC_PDF="src_oko_zo_jr2025_nbb_pdf_2453"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},OKO & ZO VZW,ASBL OKO & ZO,OKO & ZO VZW (leftover city_zele CIK),parastatal,city_zele,nl,https://www.oko-en-zo.be,oko@skynet.be,Rotstraat 20 9240 Zele,tick2453 YE2025 Strong official native NBB PDF deposit 2026-00191153 + Strong KBO 0862.154.608 Actief 2 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto DROP 914033 envelope; pnl FLIP LOSS -15184; 9901 FLIP LOSS -20522; equity DROP 668157; assets DROP 858840; debt DROP 190683; FTE 14.2 DROP; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 419271; geldbeleggingen DROP 0; leftover mined city_zele after KINDEROPVANG De Harlekijntjes different-KBO skip; 2 VE CIK BKO + dienst opvanggezinnen not private; NOT Kloosterstraat 6 Drongen; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_oko_zo_bruto_jr2025_statutory,{EID},2025,914033,914033,914033,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -3.97% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2453; PDF p5 native; YE2024 identical 951799; 76A empty",
f"bud_oko_zo_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2453; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_oko_zo_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2453; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 914033",
f"bud_oko_zo_pnl_jr2025_statutory,{EID},2025,-15184,-15184,-15184,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP LOSS (was 17773),{SRC_PDF},strong,tick2453; PDF p5 native; YE2024 identical 17773; bedrijfswinst 9901 -20522 FLIP LOSS; destin691 empty",
f"bud_oko_zo_bedrijfswinst_jr2025_statutory,{EID},2025,-20522,-20522,-20522,NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP LOSS (was 11600),{SRC_PDF},strong,tick2453; PDF p5 native; YE2024 identical 11600; 62 925505 DROP; 630 8924 JUMP; 640/8 125 DROP",
f"bud_oko_zo_equity_jr2025_statutory,{EID},2025,668157,668157,668157,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -2.22%,{SRC_PDF},strong,tick2453; PDF p4 native; YE2024 identical 683341; kapitaalsubsidies empty; overgedragen 14 668157 DROP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_oko_zo_assets_jr2025_statutory,{EID},2025,858840,858840,858840,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -4.12%,{SRC_PDF},strong,tick2453; PDF p3 native; YE2024 identical 895781; MVA 22/27 150296 DROP; cash 419271 JUMP; geldbeleggingen 0 DROP; aanbouw 27 empty",
f"bud_oko_zo_debt_jr2025_statutory,{EID},2025,190683,190683,190683,NBB VKT-VZW code 17/49 schulden YE2025 DROP -10.24%,{SRC_PDF},strong,tick2453; PDF p4 native; YE2024 identical 212441; 42/48 190683 DROP",
f"bud_oko_zo_cash_jr2025_statutory,{EID},2025,419271,419271,419271,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +35.42%,{SRC_PDF},strong,tick2453; PDF p3 native; YE2024 identical 309603; geldbeleggingen 50/53 0 DROP (was 65000)",
f"bud_oko_zo_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (791 empty; destin empty vs pnl -15184),{SRC_PDF},strong,tick2453; PDF p6 native; YE2024 destin empty; overgedragen 14 668157 DROP FOI",
f"bud_oko_zo_62_jr2025_statutory,{EID},2025,925505,925505,925505,NBB VKT-VZW code 62 bezoldigingen YE2025 DROP -0.63%,{SRC_PDF},strong,tick2453; PDF p5 native; YE2024 identical 931353; FTE 14.2 DROP",
])
print("entities+budgets ok")

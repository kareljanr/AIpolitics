from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2451_stamp.txt").read_text().strip().splitlines()
EID="vzw_hartjes_ninove"
SRC_PDF="src_hartjes_ninove_jr2025_nbb_pdf_2451"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf De Hartjes VZW,ASBL Kinderdagverblijf De Hartjes,Kinderdagverblijf De Hartjes VZW (leftover city_ninove CIK),parastatal,city_ninove,nl,https://dehartjesninove.be,info@dehartjesninove.be,Onderwijslaan 14 9400 Ninove,tick2451 YE2025 Strong official native NBB PDF deposit 2026-00170536 + Strong KBO 0446.391.327 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto JUMP 483796 envelope; pnl JUMP 31142; 9901 FLIP PROFIT 21273; equity JUMP 437479; assets JUMP 478634; debt DROP 41156; FTE 8.2 DROP; kapitaalsubsidies DROP 27420; destin691 empty FLAT; 791 empty; cash JUMP 391809; geldbeleggingen empty; leftover mined city_ninove after Groepsopvang De Hartjes Tienen different-KBO skip; 1 VE CIK not private; NOT Kloosterstraat 6 Drongen; NOT Groepsopvang De Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hartjes_ninove_bruto_jr2025_statutory,{EID},2025,483796,483796,483796,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +1.11% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2451; PDF p5 native; YE2024 identical 478464; 76A empty",
f"bud_hartjes_ninove_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2451; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_hartjes_ninove_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2451; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 483796",
f"bud_hartjes_ninove_pnl_jr2025_statutory,{EID},2025,31142,31142,31142,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +413.39% (was 6066),{SRC_PDF},strong,tick2451; PDF p5 native; YE2024 identical 6066; bedrijfswinst 9901 21273 FLIP PROFIT; destin691 empty FLAT",
f"bud_hartjes_ninove_bedrijfswinst_jr2025_statutory,{EID},2025,21273,21273,21273,NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP PROFIT (was -9920),{SRC_PDF},strong,tick2451; PDF p5 native; YE2024 identical -9920; 62 441255 DROP; 630 20246 JUMP; 66A empty",
f"bud_hartjes_ninove_equity_jr2025_statutory,{EID},2025,437479,437479,437479,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.06%,{SRC_PDF},strong,tick2451; PDF p4 native; YE2024 identical 416397; kapitaalsubsidies 27420 DROP; overgedragen 14 285876 JUMP; fondsen 10 124183 FLAT; bestemde fondsen 13 empty",
f"bud_hartjes_ninove_assets_jr2025_statutory,{EID},2025,478634,478634,478634,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +4.20%,{SRC_PDF},strong,tick2451; PDF p3 native; YE2024 identical 459328; MVA 22/27 58310 DROP; cash 391809 JUMP; geldbeleggingen empty; aanbouw 27 empty",
f"bud_hartjes_ninove_debt_jr2025_statutory,{EID},2025,41156,41156,41156,NBB VKT-VZW code 17/49 schulden YE2025 DROP -4.13%,{SRC_PDF},strong,tick2451; PDF p4 native; YE2024 identical 42931; 42/48 41156 DROP",
f"bud_hartjes_ninove_cash_jr2025_statutory,{EID},2025,391809,391809,391809,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +11.80%,{SRC_PDF},strong,tick2451; PDF p3 native; YE2024 identical 350440; geldbeleggingen 50/53 empty",
f"bud_hartjes_ninove_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (791 empty; 13 empty; pnl 31142 not destined),{SRC_PDF},strong,tick2451; PDF p6 native; YE2024 destin empty; overgedragen 14 285876 JUMP FOI",
f"bud_hartjes_ninove_62_jr2025_statutory,{EID},2025,441255,441255,441255,NBB VKT-VZW code 62 bezoldigingen YE2025 DROP -5.72%,{SRC_PDF},strong,tick2451; PDF p5 native; YE2024 identical 468028; FTE 8.2 DROP",
])
print("entities+budgets ok")

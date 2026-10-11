from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2446_stamp.txt").read_text().strip().splitlines()
EID="vzw_kinderkuren"
SRC_PDF="src_kinderkuren_jr2025_nbb_pdf_2446"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Kinderkuren VZW (ex Kinderopvang Leuven),ASBL Kinderkuren,Kinderkuren VZW (leftover city_leuven EVA BKO),parastatal,city_leuven,nl,https://www.leuven.be/kinderopvang-kinderkuren,kinderkuren@leuven.be,Professor Van Overstraetenplein 1 3000 Leuven,tick2446 YE2025 Strong official native NBB PDF deposit 2026-00321398 + Strong KBO 0478.167.834 Actief 37 VE naam Kinderkuren since 18.12.2025 PDF header Kinderopvang Leuven RSZ2025 88.919 EVA aanbestedende overheid Stad Leuven; omzet70 empty VKT; 73 empty VKT; 76A DROP 2432; bruto9900 DROP 4674661 envelope; pnl FLIP LOSS -617961; 9901 FLIP LOSS -615411; equity DROP 857351; assets DROP 1762362; debt DROP 905011; FTE 81.6 JUMP; kapitaalsubsidies empty; destin691 DROP 0 (was 680000); 791 680000; cash JUMP 1417387; geldbeleggingen empty; leftover mined city_leuven after Wigwam / t Anemoontje / IZW / Monte Rosa / De Wissel / De Slabbertjes / t Zonnetje; 37 VE; EVA BKO not private; NOT Kloosterstraat 6 Drongen; NOT Wigwam 0435.015.207; NOT t Anemoontje 0413.354.612; NOT IZW 0430.278.439; NOT Monte Rosa 0413.350.751; NOT De Wissel 0421.913.376; NOT De Slabbertjes 0411.972.064; NOT t Zonnetje 0443.648.306; NOT Kinderdagverblijven Leuven 0413.321.255 absorbed; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_kinderkuren_bruto_jr2025_statutory,{EID},2025,4674661,4674661,4674661,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -17.46% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2446; PDF p6 native; YE2024 identical 5663317; 76A 2432 DROP",
f"bud_kinderkuren_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2446; PDF p6 native; YE2024 identical empty; 73 also empty VKT",
f"bud_kinderkuren_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2446; PDF p6 native; YE2024 identical empty; FOI Opgroeien/Stad Leuven split behind bruto 4674661",
f"bud_kinderkuren_pnl_jr2025_statutory,{EID},2025,-617961,-617961,-617961,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 FLIP LOSS (was +837483),{SRC_PDF},strong,tick2446; PDF p6 native; YE2024 identical 837483; bedrijfswinst 9901 -615411 FLIP; destin691 0 DROP",
f"bud_kinderkuren_bedrijfswinst_jr2025_statutory,{EID},2025,-615411,-615411,-615411,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 FLIP LOSS (was +839176),{SRC_PDF},strong,tick2446; PDF p6 native; YE2024 identical 839176; 62 5127146 JUMP; 630 29822 JUMP; 66A 112 DROP",
f"bud_kinderkuren_equity_jr2025_statutory,{EID},2025,857351,857351,857351,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -41.89%,{SRC_PDF},strong,tick2446; PDF p5 native; YE2024 identical 1475312; kapitaalsubsidies empty; overgedragen 14 840134 JUMP; fondsen 10 17217 FLAT; bestemde fondsen 13 0 DROP",
f"bud_kinderkuren_assets_jr2025_statutory,{EID},2025,1762362,1762362,1762362,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -26.29%,{SRC_PDF},strong,tick2446; PDF p4 native; YE2024 identical 2390826; MVA 22/27 33231 DROP; cash 1417387 JUMP; geldbeleggingen empty",
f"bud_kinderkuren_debt_jr2025_statutory,{EID},2025,905011,905011,905011,NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.15%,{SRC_PDF},strong,tick2446; PDF p5 native; YE2024 identical 915514; 17 empty; 42/48 904913 DROP",
f"bud_kinderkuren_cash_jr2025_statutory,{EID},2025,1417387,1417387,1417387,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +5.73%,{SRC_PDF},strong,tick2446; PDF p4 native; YE2024 identical 1340576; geldbeleggingen 50/53 empty",
f"bud_kinderkuren_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 0 DROP (was 680000; 791 onttrekking 680000; 13 DROP to 0),{SRC_PDF},strong,tick2446; PDF p7 native; YE2024 destin 680000; bestemde fondsen 13 0 FOI",
f"bud_kinderkuren_62_jr2025_statutory,{EID},2025,5127146,5127146,5127146,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +10.37%,{SRC_PDF},strong,tick2446; PDF p6 native; YE2024 identical 4645540; FTE 81.6 JUMP",
])
print("entities+budgets ok")

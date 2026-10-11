from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2440_stamp.txt").read_text().strip().splitlines()
EID="vzw_ukkies"
SRC_PDF="src_ukkies_jr2025_nbb_pdf_2440"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},De Ukkies VZW,ASBL De Ukkies,De Ukkies VZW (leftover city_hasselt CIK+BOA),parastatal,city_hasselt,nl,https://www.ukkies.be/,secretariaat@ukkies.be,Erasmuslaan 14 3500 Hasselt,tick2440 YE2025 Strong official native NBB PDF deposit 2026-00164180 + Strong KBO 0412.729.654 Actief 3 VE zetel Erasmuslaan 14 3500 Hasselt RSZ2025 88.911; omzet70 empty; 73 empty; 76A JUMP 42695; bruto9900 JUMP 5126812 envelope; pnl FLAT 308628; 9901 JUMP 300046; equity JUMP 3995693; assets FLAT 4695584; debt DROP 699892; FTE 79.3 FLAT; kapitaalsubsidies DROP 705041; destin691 FLAT 308628 destin=pnl; cash JUMP 1065696; geldbeleggingen JUMP 1287959; gebouwen DROP 1766727; aanbouw empty; leftover mined city_hasselt after Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; 3 VE Hasselt; Opgroeien CIK 212 plaatsen + 5 BOA; site 462 kindplaatsen; NOT Kloosterstraat 6 Drongen; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT Grauwzusters 0409.771.748 convent; NOT Jessa 0821.142.117; NOT Kinderlach; NOT Helan; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_ukkies_bruto_jr2025_statutory,{EID},2025,5126812,5126812,5126812,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +1.29% (CIK envelope; omzet 70 empty so bruto is envelope),{SRC_PDF},strong,tick2440; PDF p6 native; YE2024 identical 5061722; 73 empty; 76A 42695 JUMP; 62 4620455 JUMP",
f"bud_ukkies_pnl_jr2025_statutory,{EID},2025,308628,308628,308628,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLAT -0.42%,{SRC_PDF},strong,tick2440; PDF p6 native; YE2024 identical 309932; bedrijfswinst 9901 300046 JUMP; destin691 308628 FLAT destin=pnl",
f"bud_ukkies_bedrijfswinst_jr2025_statutory,{EID},2025,300046,300046,300046,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +9.67%,{SRC_PDF},strong,tick2440; PDF p6 native; YE2024 identical 273579; 62 4620455 JUMP; 630 190242 JUMP; 66A 3736",
f"bud_ukkies_equity_jr2025_statutory,{EID},2025,3995693,3995693,3995693,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +6.93%,{SRC_PDF},strong,tick2440; PDF p5 native; YE2024 identical 3736723; kapitaalsubsidies 705041 DROP; overgedragen 14 1484169 FLAT; fondsen 10 1187923 FLAT; bestemde fondsen 13 618560 JUMP",
f"bud_ukkies_assets_jr2025_statutory,{EID},2025,4695584,4695584,4695584,NBB VKT-VZW code 20/58 totaal activa YE2025 FLAT -0.30%,{SRC_PDF},strong,tick2440; PDF p4 native; YE2024 identical 4709533; gebouwen 22 1766727 DROP; cash 1065696 JUMP; geldbeleggingen 1287959 JUMP",
f"bud_ukkies_debt_jr2025_statutory,{EID},2025,699892,699892,699892,NBB VKT-VZW code 17/49 schulden YE2025 DROP -28.05%,{SRC_PDF},strong,tick2440; PDF p5 native; YE2024 identical 972810; 42/48 664730; 44 91319",
f"bud_ukkies_cash_jr2025_statutory,{EID},2025,1065696,1065696,1065696,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +42.82%,{SRC_PDF},strong,tick2440; PDF p4 native; YE2024 identical 746188; geldbeleggingen 50/53 1287959 JUMP",
f"bud_ukkies_destin_jr2025_statutory,{EID},2025,308628,308628,308628,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 FLAT -0.42% (destin = pnl 308628),{SRC_PDF},strong,tick2440; PDF p7 native; YE2024 identical 309932; bestemde fondsen 13 618560 JUMP FOI",
f"bud_ukkies_kapitaalsubsidies_jr2025_statutory,{EID},2025,705041,705041,705041,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -6.58%,{SRC_PDF},strong,tick2440; PDF p5 native; YE2024 identical 754700",
f"bud_ukkies_76A_jr2025_statutory,{EID},2025,42695,42695,42695,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +10.18%,{SRC_PDF},strong,tick2440; PDF p6 native; YE2024 identical 38750",
f"bud_ukkies_62_jr2025_statutory,{EID},2025,4620455,4620455,4620455,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +0.52%,{SRC_PDF},strong,tick2440; PDF p6 native; YE2024 identical 4596615; FTE 79.3 FLAT",
])
print("entities+budgets ok")

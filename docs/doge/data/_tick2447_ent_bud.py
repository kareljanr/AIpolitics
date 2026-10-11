from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2447_stamp.txt").read_text().strip().splitlines()
EID="vzw_cob_annuntiaten_heverlee"
SRC_PDF="src_cobah_jr2025_nbb_pdf_2447"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Centra voor Opvang en Begeleiding Annuntiaten Heverlee VZW (COBAH),ASBL COB Annuntiaten Heverlee,COB Annuntiaten Heverlee VZW (leftover city_leuven CIK),parastatal,city_leuven,nl,https://www.kinderopvangleuven.be/nl/opvanglocatie/11,veerle.mertens@kdv.annuntiaten.be,Naamsesteenweg 355 3001 Heverlee,tick2447 YE2025 Strong official native NBB PDF deposit 2026-00216711 + Strong KBO 0447.017.570 Actief 4 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A JUMP 3698; bruto9900 DROP 2462444 envelope; pnl DROP 8845; 9901 DROP 12020; equity DROP 2993102; assets JUMP 4525424; debt JUMP 1532322; FTE 43.5 JUMP; kapitaalsubsidies DROP 1792722; destin691 empty FLAT; 791 empty; cash JUMP 433864; geldbeleggingen empty; leftover mined city_leuven after Kinderkuren / Wigwam / t Anemoontje / IZW / Monte Rosa / De Wissel / De Slabbertjes; 4 VE CIK not private; NOT Kloosterstraat 6 Drongen; NOT WZC Annuntiaten 0895.366.220 already in entities; NOT Kinderkuren 0478.167.834; NOT Kinderdagverblijven Leuven 0413.321.255 absorbed; NOT Wigwam 0435.015.207; NOT t Anemoontje 0413.354.612; NOT t Zonnetje 0443.648.306; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_cobah_bruto_jr2025_statutory,{EID},2025,2462444,2462444,2462444,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -1.20% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2447; PDF p5 native; YE2024 identical 2492228; 76A 3698 JUMP",
f"bud_cobah_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2447; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_cobah_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2447; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 2462444",
f"bud_cobah_pnl_jr2025_statutory,{EID},2025,8845,8845,8845,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -95.74% (was 207684),{SRC_PDF},strong,tick2447; PDF p5 native; YE2024 identical 207684; bedrijfswinst 9901 12020 DROP; destin691 empty FLAT",
f"bud_cobah_bedrijfswinst_jr2025_statutory,{EID},2025,12020,12020,12020,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -94.26% (was 209533),{SRC_PDF},strong,tick2447; PDF p5 native; YE2024 identical 209533; 62 2246000 JUMP; 630 198320 DROP; 66A empty",
f"bud_cobah_equity_jr2025_statutory,{EID},2025,2993102,2993102,2993102,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -0.44%,{SRC_PDF},strong,tick2447; PDF p4 native; YE2024 identical 3006278; kapitaalsubsidies 1792722 DROP; overgedragen 14 329763 JUMP; fondsen 10 370618 FLAT; bestemde fondsen 13 500000 FLAT",
f"bud_cobah_assets_jr2025_statutory,{EID},2025,4525424,4525424,4525424,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +0.59%,{SRC_PDF},strong,tick2447; PDF p3 native; YE2024 identical 4498862; MVA 22/27 3582019 DROP; cash 433864 JUMP; geldbeleggingen empty",
f"bud_cobah_debt_jr2025_statutory,{EID},2025,1532322,1532322,1532322,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +2.66%,{SRC_PDF},strong,tick2447; PDF p4 native; YE2024 identical 1492584; 17 1117643 DROP; 42/48 414366 JUMP",
f"bud_cobah_cash_jr2025_statutory,{EID},2025,433864,433864,433864,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +107.95%,{SRC_PDF},strong,tick2447; PDF p3 native; YE2024 identical 208643; geldbeleggingen 50/53 empty (was 755)",
f"bud_cobah_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (791 empty; 13 FLAT 500000 sociaal passief),{SRC_PDF},strong,tick2447; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 500000 FOI",
f"bud_cobah_62_jr2025_statutory,{EID},2025,2246000,2246000,2246000,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +8.08%,{SRC_PDF},strong,tick2447; PDF p5 native; YE2024 identical 2078007; FTE 43.5 JUMP",
])
print("entities+budgets ok")

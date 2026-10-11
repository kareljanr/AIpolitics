from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2445_stamp.txt").read_text().strip().splitlines()
EID="vzw_t_zonnetje"
SRC_PDF="src_zonnetje_jr2025_nbb_pdf_2445"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},t Zonnetje kinderdagverblijven VZW,ASBL t Zonnetje,t Zonnetje VZW (leftover city_waregem + city_kruisem CIK),parastatal,city_waregem,nl,https://www.kdvzonnetje.be/,inge.moens@kdvzonnetje.be,Kasteellaan 1 9840 Nazareth-De Pinte,tick2445 YE2025 Strong official native NBB PDF deposit 2026-00162372 + Strong KBO 0443.648.306 Actief 3 VE 2.154.838.667 BKO Dol-fijn Nazareth-De Pinte + 2.218.012.589 KDV t sprookjesparadijs Kruisem + 2.218.012.886 KDV t Regenboogje Waregem RSZ2025 88.911; omzet70 empty VKT; 73 empty VKT; 76A JUMP 10445; bruto9900 JUMP 2113971 envelope; pnl DROP 175969; 9901 DROP 158114; equity JUMP 1652293; assets JUMP 2101178; debt JUMP 448885; FTE 30.5 JUMP; kapitaalsubsidies DROP 213065; destin691 empty; cash DROP 279435; geldbeleggingen JUMP 900000; leftover mined city_waregem after Kindercentrum + leftover mined city_kruisem after Wigwam / Jeugdhulp Don Bosco; 3 VE; Opgroeien CIK + BKO; NOT Kloosterstraat 6 Drongen; NOT Kindercentrum 0408.226.775; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Zonnestraal Junior 0866.116.859; NOT KDV De Regenboog 0671.670.560 BV; NOT Wigwam 0435.015.207; NOT Jeugdhulp Don Bosco 0408.666.344; NOT t Anemoontje 0413.354.612; NOT Kinderlach 0450.275.186; NOT Helan; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_zonnetje_bruto_jr2025_statutory,{EID},2025,2113971,2113971,2113971,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +1.90% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2445; PDF p5 native; YE2024 identical 2074478; 76A 10445 JUMP",
f"bud_zonnetje_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2445; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_zonnetje_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2445; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 2113971",
f"bud_zonnetje_pnl_jr2025_statutory,{EID},2025,175969,175969,175969,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -41.22%,{SRC_PDF},strong,tick2445; PDF p5 native; YE2024 identical 299368; bedrijfswinst 9901 158114 DROP; destin691 empty",
f"bud_zonnetje_bedrijfswinst_jr2025_statutory,{EID},2025,158114,158114,158114,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -43.62%,{SRC_PDF},strong,tick2445; PDF p5 native; YE2024 identical 280456; 62 1848937 JUMP; 630 104433 JUMP; 66A 453 DROP",
f"bud_zonnetje_equity_jr2025_statutory,{EID},2025,1652293,1652293,1652293,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +9.38%,{SRC_PDF},strong,tick2445; PDF p4 native; YE2024 identical 1510639; kapitaalsubsidies 213065 DROP; overgedragen 14 1391528 JUMP; fondsen 10 47700 FLAT; bestemde fondsen 13 empty",
f"bud_zonnetje_assets_jr2025_statutory,{EID},2025,2101178,2101178,2101178,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +13.26%,{SRC_PDF},strong,tick2445; PDF p3 native; YE2024 identical 1855217; overige MVA 26 594766 JUMP; cash 279435 DROP; geldbeleggingen 900000 JUMP",
f"bud_zonnetje_debt_jr2025_statutory,{EID},2025,448885,448885,448885,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +30.27%,{SRC_PDF},strong,tick2445; PDF p4 native; YE2024 identical 344578; 17 empty; 42/48 441941 JUMP",
f"bud_zonnetje_cash_jr2025_statutory,{EID},2025,279435,279435,279435,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -54.40%,{SRC_PDF},strong,tick2445; PDF p3 native; YE2024 identical 612863; geldbeleggingen 50/53 900000 JUMP",
f"bud_zonnetje_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (destin empty vs pnl 175969; 14 JUMP 1391528),{SRC_PDF},strong,tick2445; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 empty FOI",
f"bud_zonnetje_62_jr2025_statutory,{EID},2025,1848937,1848937,1848937,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +8.42%,{SRC_PDF},strong,tick2445; PDF p5 native; YE2024 identical 1705255; FTE 30.5 JUMP",
])
print("entities+budgets ok")

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2412_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kinderopvang_turnhout"
SRC_PDF = "src_koturnhout_jr2025_nbb_pdf_2412"

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

append_lines(DATA / "entities.csv", [
    f'{EID},Kinderopvang Turnhout VZW,ASBL Kinderopvang Turnhout,Kinderopvang Turnhout VZW (leftover city_turnhout CIK/BKO EVA),parastatal,city_turnhout,nl,https://www.turnhout.be/nl/kinderopvang,kinderopvang@turnhout.be,"Druivenstraat 19, 2300 Turnhout",tick2412 YE2025 Strong official native NBB PDF deposit 2026-00286204 + Strong KBO 0465.284.947 Actief 5 VE RSZ2025 88.911; Stad Turnhout 0207.533.082 bestuurder; EVA BKO 2.5-12 residual after creches to Orion 01.04.2024; omzet70 JUMP 314264 commercial-only vs large 73; 73 DROP 2232684; 76A empty; bedrijfsopbrengsten 70+73+76A FLAT 2546948 VZW envelope; bruto9900 JUMP 2187383; pnl FLIP 260; equity DROP 134128; assets JUMP 765516; debt JUMP 631388; FTE DROP 32; kapitaalsubsidies DROP 49295; destin691 empty; cash JUMP 537544; geldbeleggingen empty; gebouwen empty; vooruitbetalingen 46 JUMP 270000; voorzieningen 16 released 110000; leftover city_turnhout after VERBINT@2401; NOT Zonnestraal 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_koturnhout_opbr_jr2025_statutory,{EID},2025,2546948,2546948,2546948,NBB VKT-VZW bedrijfsopbrengsten 70+73+76A YE2025 FLAT +0.34% (primary L5 envelope; omzet 70 314264 commercial-only vs large 73 2232684 so 70/76A-class envelope),{SRC_PDF},strong,tick2412; PDF p6 native; YE2024 2538233 restated; omzet70 314264; 73 2232684; 76A empty",
    f"bud_koturnhout_73_jr2025_statutory,{EID},2025,2232684,2232684,2232684,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -1.20%,{SRC_PDF},strong,tick2412; PDF p6 native; YE2024 2259836 restated; envelope is 70+73+76A 2546948",
    f"bud_koturnhout_omzet_jr2025_statutory,{EID},2025,314264,314264,314264,NBB VKT-VZW code 70 omzet YE2025 JUMP +15.64% (ouderbijdragen BKO; commercial-only vs large 73),{SRC_PDF},strong,tick2412; PDF p6 native; YE2024 271753 restated; 73 2232684",
    f"bud_koturnhout_bruto_jr2025_statutory,{EID},2025,2187383,2187383,2187383,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +7.02% (margin after 60/61 359566; envelope is 70+73+76A),{SRC_PDF},strong,tick2412; PDF p6 native; YE2024 2043935 restated",
    f"bud_koturnhout_pnl_jr2025_statutory,{EID},2025,260,260,260,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 PROFIT FLIP (was LOSS -277088),{SRC_PDF},strong,tick2412; PDF p6 native; YE2024 -277088 restated; bedrijfswinst 9901 3559 PROFIT FLIP; destin691 empty",
    f"bud_koturnhout_bedrijfswinst_jr2025_statutory,{EID},2025,3559,3559,3559,NBB VKT-VZW code 9901 bedrijfswinst YE2025 PROFIT FLIP (was -278901),{SRC_PDF},strong,tick2412; PDF p6 native; YE2024 -278901 restated; 62 2249341; 635/9 -110000 provision release",
    f"bud_koturnhout_equity_jr2025_statutory,{EID},2025,134128,134128,134128,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -12.82%,{SRC_PDF},strong,tick2412; PDF p5 native; YE2024 153850 restated; kapitaalsubsidies 49295; overgedragen 14 34832; fondsen 10 empty; bestemde 13 50000",
    f"bud_koturnhout_assets_jr2025_statutory,{EID},2025,765516,765516,765516,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +27.09%,{SRC_PDF},strong,tick2412; PDF p4 native; YE2024 602327 restated; gebouwen 22 empty; 5 VE EVA",
    f"bud_koturnhout_cash_jr2025_statutory,{EID},2025,537544,537544,537544,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +68.44%,{SRC_PDF},strong,tick2412; PDF p4 native; YE2024 319132 restated; geldbeleggingen 50/53 empty",
    f"bud_koturnhout_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2412; PDF p7 native; 9905 260 fully to overgedragen 14 now 34832; post 13 50000 FLAT max city agreement",
])
print("entities+budgets ok")

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2411_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zonnestraal"
SRC_PDF = "src_zonnestraal_jr2025_nbb_pdf_2411"

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
    f'{EID},KINDEROPVANG ZONNESTRAAL VZW Sint-Niklaas,ASBL KINDEROPVANG ZONNESTRAAL Saint-Nicolas,KINDEROPVANG ZONNESTRAAL VZW (leftover city_sint_niklaas CIK parent),parastatal,city_sint_niklaas,nl,https://www.kinderopvangzonnestraal.be/,info@kinderopvangzonnestraal.be,"Gladiolenstraat 10, 9100 Sint-Niklaas",tick2411 YE2025 Strong official native NBB PDF deposit 2026-00244239 + Strong KBO 0413.351.642 Actief 1 VE RSZ2025 88.911 Kinderopvang VL since 01.04.2014; omzet70 DROP 1353656 commercial-only vs large 73; 73 JUMP 2202564; 76A 286; bedrijfsopbrengsten 70+73+76A FLAT 3556506 VZW envelope; bruto9900 JUMP 1563939; pnl DROP 112283; equity JUMP 1228898; assets JUMP 1789323; debt JUMP 560425; FTE JUMP 21.4; kapitaalsubsidies DROP 83575; destin691 empty; cash DROP 513151; geldbeleggingen JUMP 833500; gebouwen 112546; leftover city_sint_niklaas after Junior@2410 same zetel same board; NOT Junior 0866.116.859; NOT Grimbergen VAPH Zonnestraal Havinet; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_zonnestraal_opbr_jr2025_statutory,{EID},2025,3556506,3556506,3556506,NBB VKT-VZW bedrijfsopbrengsten 70+73+76A YE2025 FLAT +0.18% (primary L5 envelope; omzet 70 1353656 commercial-only vs large 73 2202564 so 70/76A-class envelope),{SRC_PDF},strong,tick2411; PDF p7 native; YE2024 3550184; omzet70 1353656; 73 2202564; 76A 286",
    f"bud_zonnestraal_73_jr2025_statutory,{EID},2025,2202564,2202564,2202564,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +1.51%,{SRC_PDF},strong,tick2411; PDF p7 native; YE2024 2169811; envelope is 70+73+76A 3556506",
    f"bud_zonnestraal_omzet_jr2025_statutory,{EID},2025,1353656,1353656,1353656,NBB VKT-VZW code 70 omzet YE2025 DROP -1.88% (ouderbijdragen; commercial-only vs large 73),{SRC_PDF},strong,tick2411; PDF p7 native; YE2024 1379534; 73 2202564",
    f"bud_zonnestraal_bruto_jr2025_statutory,{EID},2025,1563939,1563939,1563939,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +11.76% (margin after 60/61 2000414; envelope is 70+73+76A),{SRC_PDF},strong,tick2411; PDF p7 native; YE2024 1399358",
    f"bud_zonnestraal_pnl_jr2025_statutory,{EID},2025,112283,112283,112283,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -45.67%,{SRC_PDF},strong,tick2411; PDF p7 native; YE2024 206670; bedrijfswinst 9901 97457 DROP; destin691 empty",
    f"bud_zonnestraal_bedrijfswinst_jr2025_statutory,{EID},2025,97457,97457,97457,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -48.73%,{SRC_PDF},strong,tick2411; PDF p7 native; YE2024 190101; 62 1356137; 66A 62995",
    f"bud_zonnestraal_equity_jr2025_statutory,{EID},2025,1228898,1228898,1228898,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +32.17%,{SRC_PDF},strong,tick2411; PDF p6 native; YE2024 929811; kapitaalsubsidies 83575; overgedragen 14 557891; fondsen 10 387432; bestemde 13 200000",
    f"bud_zonnestraal_assets_jr2025_statutory,{EID},2025,1789323,1789323,1789323,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +6.40%,{SRC_PDF},strong,tick2411; PDF p5 native; YE2024 1681646; gebouwen 22 112546; 1 VE parent",
    f"bud_zonnestraal_cash_jr2025_statutory,{EID},2025,513151,513151,513151,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -24.03%,{SRC_PDF},strong,tick2411; PDF p5 native; YE2024 675489; geldbeleggingen 50/53 JUMP 833500",
    f"bud_zonnestraal_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (was 200000),{SRC_PDF},strong,tick2411; PDF p8 native; 9905 112283 fully to overgedragen 14 now 557891; post 13 200000 prior destin parked",
])
print("entities+budgets ok")

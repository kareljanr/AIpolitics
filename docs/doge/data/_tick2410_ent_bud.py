#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2410_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zonnestraal_junior"
SRC_PDF = "src_zonnestraal_junior_jr2025_nbb_pdf_2410"

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
    f'{EID},Kinderopvang Zonnestraal Junior VZW Sint-Niklaas,ASBL Kinderopvang Zonnestraal Junior Saint-Nicolas,Kinderopvang Zonnestraal Junior VZW (leftover city_sint_niklaas CIK),parastatal,city_sint_niklaas,nl,https://www.kinderopvangzonnestraal.be/,info@kinderopvangzonnestraal.be,"Gladiolenstraat 10, 9100 Sint-Niklaas",tick2410 EVERY-10 YE2025 Strong official native NBB PDF deposit 2026-00244618 + Strong KBO 0866.116.859 Actief 20 VE RSZ2025 88.911; omzet70 empty VKT; 73 DROP 200083 CIK envelope; bruto9900 -88; pnl LOSS -294; equity DROP 4522; assets DROP 13118; debt DROP 8596; FTE unpublished VKT 6.x; kapitaalsubsidies empty; destin691 empty; cash DROP 4522; geldbeleggingen empty; gebouwen empty; leftover city_sint_niklaas after Elfenbankje@2409; NOT parent 0413.351.642; NOT Grimbergen VAPH Zonnestraal Havinet; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_zonnestraal_junior_73_jr2025_statutory,{EID},2025,200083,200083,200083,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -3.48% (primary L5 envelope; omzet 70 empty so 73 is envelope vs bruto -88 margin),{SRC_PDF},strong,tick2410 EVERY-10; PDF p7 native; YE2024 207298; omzet70 empty; bruto9900 -88",
    f"bud_zonnestraal_junior_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; commercial line not published; envelope is 73 200083),{SRC_PDF},strong,tick2410 EVERY-10; PDF p7 native; 73 200083",
    f"bud_zonnestraal_junior_bruto_jr2025_statutory,{EID},2025,-88,-88,-88,NBB VKT-VZW code 9900 brutomarge YE2025 -88 (was -243; margin after 60/61 200170 vs 73 200083; envelope is 73),{SRC_PDF},strong,tick2410 EVERY-10; PDF p7 native; YE2024 -243",
    f"bud_zonnestraal_junior_pnl_jr2025_statutory,{EID},2025,-294,-294,-294,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 LOSS -294 (was LOSS -449),{SRC_PDF},strong,tick2410 EVERY-10; PDF p7 native; YE2024 -449; bedrijfswinst 9901 -88; destin691 empty",
    f"bud_zonnestraal_junior_bedrijfswinst_jr2025_statutory,{EID},2025,-88,-88,-88,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 -88 (was -243),{SRC_PDF},strong,tick2410 EVERY-10; PDF p7 native; YE2024 -243; 62 empty; 65 206",
    f"bud_zonnestraal_junior_equity_jr2025_statutory,{EID},2025,4522,4522,4522,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -6.10%,{SRC_PDF},strong,tick2410 EVERY-10; PDF p6 native; YE2024 4816; kapitaalsubsidies empty; overgedragen 14 345; fondsen 10 4177",
    f"bud_zonnestraal_junior_assets_jr2025_statutory,{EID},2025,13118,13118,13118,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -47.45%,{SRC_PDF},strong,tick2410 EVERY-10; PDF p5 native; YE2024 24962; gebouwen 22 empty; 20 VE residual",
    f"bud_zonnestraal_junior_debt_jr2025_statutory,{EID},2025,8596,8596,8596,NBB VKT-VZW code 17/49 schulden YE2025 DROP -57.33%,{SRC_PDF},strong,tick2410 EVERY-10; PDF p6 native; YE2024 20147; LT 17 empty; ST 42/48 8596; 454/9 8596",
    f"bud_zonnestraal_junior_cash_jr2025_statutory,{EID},2025,4522,4522,4522,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -6.10%,{SRC_PDF},strong,tick2410 EVERY-10; PDF p5 native; YE2024 4816; geldbeleggingen 50/53 empty",
    f"bud_zonnestraal_junior_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2410 EVERY-10; PDF p8 native; 9905 -294 fully to overgedragen 14 now 345",
])
print("entities+budgets ok")

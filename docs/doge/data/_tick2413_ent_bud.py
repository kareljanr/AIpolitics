#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2413_stamp.txt").read_text().strip().splitlines()
EID = "vzw_bengelhof"
SRC_PDF = "src_bengelhof_jr2025_nbb_pdf_2413"

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
    f'{EID},Bengelhof VZW Gent,ASBL Bengelhof Gand,Bengelhof VZW (leftover city_gent CIK groepsopvang),parastatal,city_gent,nl,https://www.bengelhofvzw.be/,bengelhof@dominovzw.be,"Sint-Margrietstraat 36, 9000 Gent",tick2413 YE2025 Strong official native NBB PDF deposit 2026-00191897 + Strong KBO 0455.442.813 Actief 1 VE 2.159.891.971 RSZ2025 88.911; Kinderopvang VG since 01.04.2014; 72 plaatsen inkomenstarief; omzet70 empty; 73 empty; 76A empty; bruto9900 JUMP 933326 CIK envelope; pnl DROP 10667; equity JUMP 433400; assets DROP 667298; debt DROP 212898; FTE JUMP 17.4; kapitaalsubsidies empty; destin691 empty; cash DROP 224013; geldbeleggingen JUMP 363981; gebouwen empty; leftover city_gent after Elfenbankje@2409; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_bengelhof_bruto_jr2025_statutory,{EID},2025,933326,933326,933326,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +16.26% (primary L5 envelope; omzet 70 empty and 73 empty so bruto is envelope),{SRC_PDF},strong,tick2413; PDF p6 native; YE2024 802755; omzet70 empty; 73 empty; 76A empty",
    f"bud_bengelhof_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2413; PDF p6 native; YE2024 empty; 73 empty",
    f"bud_bengelhof_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2413; PDF p6 native; YE2024 empty",
    f"bud_bengelhof_pnl_jr2025_statutory,{EID},2025,10667,10667,10667,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -61.48%,{SRC_PDF},strong,tick2413; PDF p6 native; YE2024 27690; bedrijfswinst 9901 9876 DROP -63.14%; destin691 empty",
    f"bud_bengelhof_bedrijfswinst_jr2025_statutory,{EID},2025,9876,9876,9876,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -63.14%,{SRC_PDF},strong,tick2413; PDF p6 native; YE2024 26790; 62 916206 JUMP +18.61%",
    f"bud_bengelhof_equity_jr2025_statutory,{EID},2025,433400,433400,433400,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.52%,{SRC_PDF},strong,tick2413; PDF p5 native; YE2024 422734; kapitaalsubsidies empty; overgedragen 14 432954; fondsen 10 446 FLAT; bestemde 13 empty",
    f"bud_bengelhof_assets_jr2025_statutory,{EID},2025,667298,667298,667298,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -14.54%,{SRC_PDF},strong,tick2413; PDF p4 native; YE2024 780792; gebouwen 22 empty; 1 VE",
    f"bud_bengelhof_cash_jr2025_statutory,{EID},2025,224013,224013,224013,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -35.42%,{SRC_PDF},strong,tick2413; PDF p4 native; YE2024 346873; geldbeleggingen 50/53 363981 JUMP +0.34%",
    f"bud_bengelhof_debt_jr2025_statutory,{EID},2025,212898,212898,212898,NBB VKT-VZW code 17/49 schulden YE2025 DROP -36.84%,{SRC_PDF},strong,tick2413; PDF p5 native; YE2024 337058; leveranciers 52.979 was 193.004",
    f"bud_bengelhof_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2413; PDF p7 native; 9905 10667 fully to overgedragen 14 now 432954",
])
print("entities+budgets ok")

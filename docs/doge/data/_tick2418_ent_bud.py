#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2418_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kos"
SRC_PDF = "src_kos_jr2025_nbb_pdf_2418"

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
    f'{EID},KOS / Kinderopvang Scholengroep Stroom VZW,ASBL KOS / Accueil extra-scolaire Scholengroep Stroom,KOS VZW (leftover city_oostende CIK),parastatal,city_oostende,nl,https://www.sterkescholen.be/,info@sterkescholen.be,"Leffingestraat 1, 8400 Oostende",tick2418 YE2025 Strong official native NBB PDF deposit 2026-00167075 + Strong KBO 0891.472.362 Actief 5 VE Vogelzang 2.166.011.978 + De Klimop 2.177.050.479 + De Lettertuin 2.177.050.578 + t Arnoldje 2.177.050.875 + t groeiboompje 2.214.729.338 RSZ2025 88.911; omzet70 JUMP 1857493 CIK envelope; 73 empty; 76A empty; bruto9900 JUMP 1704362; pnl JUMP 67833; 9901 JUMP 56600; equity JUMP 1257420; assets JUMP 1357837; debt DROP 100417; FTE JUMP 27.3; kapitaalsubsidies empty; destin691 empty; cash DROP 1102512; geldbeleggingen empty; gebouwen empty; leftover city_oostende after AG-O / IVOO / OVCO / Woonsprong; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_kos_omzet_jr2025_statutory,{EID},2025,1857493,1857493,1857493,NBB VKT-VZW code 70 omzet YE2025 JUMP +3.06% (primary L5 envelope; 73 empty so omzet is envelope not commercial-only vs large 73),{SRC_PDF},strong,tick2418; PDF p5 native; YE2024 1802296; 73 empty; 76A empty; bruto9900 1704362",
    f"bud_kos_bruto_jr2025_statutory,{EID},2025,1704362,1704362,1704362,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +3.33% (omzet 1857493 minus 60/61 153132),{SRC_PDF},strong,tick2418; PDF p5 native; YE2024 1649474; envelope is omzet 70",
    f"bud_kos_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty (VKT; envelope is omzet 70),{SRC_PDF},strong,tick2418; PDF p5 native; YE2024 empty",
    f"bud_kos_pnl_jr2025_statutory,{EID},2025,67833,67833,67833,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +46.63%,{SRC_PDF},strong,tick2418; PDF p5 native; YE2024 46260; bedrijfswinst 9901 56600 JUMP; destin691 empty",
    f"bud_kos_bedrijfswinst_jr2025_statutory,{EID},2025,56600,56600,56600,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +90.15%,{SRC_PDF},strong,tick2418; PDF p5 native; YE2024 29766; 62 1628145 JUMP +1.54%",
    f"bud_kos_equity_jr2025_statutory,{EID},2025,1257420,1257420,1257420,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.70%,{SRC_PDF},strong,tick2418; PDF p4 native; YE2024 1189587; kapitaalsubsidies empty; overgedragen 14 1245043; fondsen 10 12377 FLAT; bestemde 13 empty",
    f"bud_kos_assets_jr2025_statutory,{EID},2025,1357837,1357837,1357837,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.89%,{SRC_PDF},strong,tick2418; PDF p3 native; YE2024 1319739; gebouwen 22 empty; 5 VE",
    f"bud_kos_cash_jr2025_statutory,{EID},2025,1102512,1102512,1102512,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -3.29%,{SRC_PDF},strong,tick2418; PDF p3 native; YE2024 1140020; geldbeleggingen 50/53 empty",
    f"bud_kos_debt_jr2025_statutory,{EID},2025,100417,100417,100417,NBB VKT-VZW code 17/49 schulden YE2025 DROP -22.85%,{SRC_PDF},strong,tick2418; PDF p4 native; YE2024 130152; 42/48 97923 JUMP was 1554; 45 empty",
    f"bud_kos_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (9905 67833 fully to overgedragen 14),{SRC_PDF},strong,tick2418; PDF p6 native; 9905 67833 to overgedragen 14 1245043; destin691 empty",
])
print("entities+budgets ok")

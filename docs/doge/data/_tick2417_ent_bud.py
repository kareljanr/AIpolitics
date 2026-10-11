#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2417_stamp.txt").read_text().strip().splitlines()
EID = "vzw_bko_genk_oost"
SRC_PDF = "src_bkogenkoost_jr2025_nbb_pdf_2417"

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
    f'{EID},BKO GENK-OOST VZW / De Apenstaart,ASBL BKO GENK-OOST / De Apenstaart,BKO GENK-OOST VZW (leftover city_genk BKO IBO),parastatal,city_genk,nl,https://deapenstaart.be/,info@deapenstaart.be,"Reinpadstraat 169, 3600 Genk",tick2417 YE2025 Strong official native NBB PDF deposit 2026-00112540 + Strong KBO 0475.432.830 Actief 2 VE zetel Reinpadstraat 169 + De Bonobo 2.160.424.877 Jaarbeurslaan 12 RSZ2025 88.919; omzet70 empty; 73 empty; 76A empty; bruto9900 JUMP 1280713 BKO envelope; pnl JUMP 217320; 9901 JUMP 205436; equity JUMP 1085679; assets JUMP 1237904; debt DROP 152226; FTE DROP 18.8; kapitaalsubsidies JUMP 21116; destin691 empty; cash JUMP 912920; geldbeleggingen empty; gebouwen empty; leftover city_genk after CAW Limburg / BWOL; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_bkogenkoost_bruto_jr2025_statutory,{EID},2025,1280713,1280713,1280713,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +9.20% (primary L5 envelope; omzet 70 empty and 73 empty so bruto is envelope),{SRC_PDF},strong,tick2417; PDF p5 native; YE2024 1172805; omzet70 empty; 73 empty; 76A empty",
    f"bud_bkogenkoost_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2417; PDF p5 native; YE2024 empty; 73 empty",
    f"bud_bkogenkoost_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2417; PDF p5 native; YE2024 empty",
    f"bud_bkogenkoost_pnl_jr2025_statutory,{EID},2025,217320,217320,217320,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +68.76%,{SRC_PDF},strong,tick2417; PDF p5 native; YE2024 128777; bedrijfswinst 9901 205436 JUMP; destin691 empty",
    f"bud_bkogenkoost_bedrijfswinst_jr2025_statutory,{EID},2025,205436,205436,205436,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +76.15%,{SRC_PDF},strong,tick2417; PDF p5 native; YE2024 116626; 62 1065918 JUMP +2.50%",
    f"bud_bkogenkoost_equity_jr2025_statutory,{EID},2025,1085679,1085679,1085679,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +25.48%,{SRC_PDF},strong,tick2417; PDF p4 native; YE2024 865241; kapitaalsubsidies 21116; overgedragen 14 1064563; fondsen 10 empty; bestemde 13 empty",
    f"bud_bkogenkoost_assets_jr2025_statutory,{EID},2025,1237904,1237904,1237904,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +17.18%,{SRC_PDF},strong,tick2417; PDF p3 native; YE2024 1056395; gebouwen 22 empty; 2 VE",
    f"bud_bkogenkoost_cash_jr2025_statutory,{EID},2025,912920,912920,912920,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +20.84%,{SRC_PDF},strong,tick2417; PDF p3 native; YE2024 755507; geldbeleggingen 50/53 empty",
    f"bud_bkogenkoost_debt_jr2025_statutory,{EID},2025,152226,152226,152226,NBB VKT-VZW code 17/49 schulden YE2025 DROP -20.36%,{SRC_PDF},strong,tick2417; PDF p4 native; YE2024 191154; 42/48 152226 DROP; 45 133026 DROP",
    f"bud_bkogenkoost_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (9905 217320 fully to overgedragen 14),{SRC_PDF},strong,tick2417; PDF p6 native; 9905 217320 to overgedragen 14 1064563; destin691 empty",
])
print("entities+budgets ok")

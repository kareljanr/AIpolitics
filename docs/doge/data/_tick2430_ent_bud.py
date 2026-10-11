#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2430_stamp.txt").read_text().strip().splitlines()
EID = "vzw_beregoed"
SRC_PDF = "src_beregoed_jr2025_nbb_pdf_2430"

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
    f'{EID},KINDERDAGVERBLIJF BEREGOED VZW,ASBL KINDERDAGVERBLIJF BEREGOED,Beregoed VZW (leftover city_gent CIK),parastatal,city_gent,nl,https://www.kinderdagverblijfberegoed.be/,mireille.verwilst@azstlucas.be,"Michel Thieryhof 10, 9000 Gent",tick2430 YE2025 Strong official native NBB PDF deposit 2026-00295160 + Strong KBO 0447.515.042 Actief 3 VE 2.150.842.168 Michel Thieryhof 10 9000 Gent + 2.218.504.618 De Bereboom Lostraat 28 9880 Aalter + 2.311.240.873 t Berenest Lostraat 30 9880 Aalter RSZ2025 88.911; omzet70 JUMP 2979885 CIK envelope (73 empty); 73 empty VKT; 76A 10934; bruto9900 JUMP 2661706; pnl JUMP 176840; 9901 JUMP 162907; equity JUMP 1801386; assets JUMP 2457953; debt DROP 456567; FTE 40; kapitaalsubsidies DROP 377347; destin691 JUMP 176840; cash DROP 158322; geldbeleggingen JUMP 1000000; gebouwen DROP 875162; aanbouw empty; leftover mined city_gent after Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; Gent 87 Opgroeien plaatsen 6 leefgroepen AZ Sint-Lucas campus; De Bereboom / t Berenest same KBO not separate city_aalter leftover; NOT Kloosterstraat 6 Drongen; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT WZC De Linde Wortegem-Petegem 0425.773.085; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_beregoed_omzet_jr2025_statutory,{EID},2025,2979885,2979885,2979885,NBB VKT-VZW code 70 omzet YE2025 JUMP +4.41% (CIK envelope; omzet present and 73 empty so not commercial-only vs large 73),{SRC_PDF},strong,tick2430; PDF p5 native; YE2024 2854091; 76A 10934",
    f"bud_beregoed_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty,{SRC_PDF},strong,tick2430; PDF p5 native; VKT 73 unpublished; site Opgroeien 87 plaatsen Gent + 2 Aalter VEs not booked on 73",
    f"bud_beregoed_bruto_jr2025_statutory,{EID},2025,2661706,2661706,2661706,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +2.08%,{SRC_PDF},strong,tick2430; PDF p5 native; YE2024 2607558; 76A 10934; envelope is omzet 70 2979885",
    f"bud_beregoed_76A_jr2025_statutory,{EID},2025,10934,10934,10934,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP,{SRC_PDF},strong,tick2430; PDF p5 native; YE2024 16278",
    f"bud_beregoed_pnl_jr2025_statutory,{EID},2025,176840,176840,176840,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +111.75%,{SRC_PDF},strong,tick2430; PDF p5 native; YE2024 83515; bedrijfswinst 9901 162907 JUMP; destin691 176840",
    f"bud_beregoed_bedrijfswinst_jr2025_statutory,{EID},2025,162907,162907,162907,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +113.56%,{SRC_PDF},strong,tick2430; PDF p5 native; YE2024 76283; 62 2401863 JUMP +9.40%",
    f"bud_beregoed_equity_jr2025_statutory,{EID},2025,1801386,1801386,1801386,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +8.99%,{SRC_PDF},strong,tick2430; PDF p4 native; YE2024 1652761; kapitaalsubsidies 377347 DROP; overgedragen 14 102412; bestemde fondsen 13 1321627",
    f"bud_beregoed_assets_jr2025_statutory,{EID},2025,2457953,2457953,2457953,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +5.75%,{SRC_PDF},strong,tick2430; PDF p3 native; YE2024 2324383; gebouwen 22 DROP 875162; aanbouw 27 empty; 3 VE",
    f"bud_beregoed_debt_jr2025_statutory,{EID},2025,456567,456567,456567,NBB VKT-VZW code 17/49 schulden YE2025 DROP -3.19%,{SRC_PDF},strong,tick2430; PDF p4 native; YE2024 471622; 42/48 410413; 44 29570; 45 268281",
    f"bud_beregoed_destin_jr2025_statutory,{EID},2025,176840,176840,176840,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +111.75%,{SRC_PDF},strong,tick2430; PDF p6 native; 9905 176840 + destin691 176840 to code 13 1321627; overgedragen 14 stays 102412; YE2024 destin691 83515",
])
print("entities+budgets ok")

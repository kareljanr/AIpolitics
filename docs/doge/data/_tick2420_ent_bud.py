#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2420_stamp.txt").read_text().strip().splitlines()
EID = "vzw_ruyschaert"
SRC_PDF = "src_ruyschaert_jr2025_nbb_pdf_2420"

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
    f'{EID},Integrale Bejaardenzorg Sint-Jozef VZW / WZC De Ruyschaert,ASBL Soins integres aux personnes agees Saint-Joseph / MRS De Ruyschaert,WZC De Ruyschaert VZW (leftover city_kortrijk WZC),parastatal,city_kortrijk,nl,https://de-ruyschaert.be/,boekhouding@de-ruyschaert.be,"Kloosterstraat 25, 8510 Marke",tick2420 YE2025 Strong official native NBB PDF deposit 2026-00183610 + Strong KBO 0434.996.993 Actief 1 VE 2.191.002.247 Kloosterstraat 25 Marke RSZ2025 87.301; omzet70 JUMP 8827505 envelope not commercial-only (BTZ 4269117 + dagprijs 3492815); 73 JUMP 1681843 subsidies; 74 JUMP 357939; 76A JUMP 343692 (Marcade/GroenWest huurcorrectie 317692 + wagen 26000); opbr 70/76A JUMP 11210979; pnl FLIP 241655; 9901 FLIP 231417; equity JUMP 449438; assets DROP 2398167; debt DROP 1797724; FTE DROP 121.2; kapitaalsubsidies DROP 3504; destin691 empty; cash DROP 667324; geldbeleggingen empty; gebouwen empty; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder; NOT Kloosterstraat 6 Drongen; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_ruyschaert_omzet_jr2025_statutory,{EID},2025,8827505,8827505,8827505,NBB VOL-VZW code 70 omzet YE2025 JUMP +2.23% (primary L5 envelope; not commercial-only; jaarverslag BTZ 4269117 + dagprijs RVT/DVC/AW 3492815),{SRC_PDF},strong,tick2420; PDF p7 native; YE2024 8634912; 73 1681843 smaller so omzet is envelope",
    f"bud_ruyschaert_73_jr2025_statutory,{EID},2025,1681843,1681843,1681843,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +4.20% (all subsidies 733; Vlaams Departement Zorg / RIZIV / zorgkas),{SRC_PDF},strong,tick2420; PDF p7+p21 native; YE2024 1614070; envelope is omzet 70",
    f"bud_ruyschaert_opbr_jr2025_statutory,{EID},2025,11210979,11210979,11210979,NBB VOL-VZW codes 70/76A bedrijfsopbrengsten YE2025 JUMP +6.31% (full VZW operating; includes 73 1681843 + 74 357939 + 76A 343692 one-off),{SRC_PDF},strong,tick2420; PDF p7 native; YE2024 10545142; envelope remains omzet 70",
    f"bud_ruyschaert_76A_jr2025_statutory,{EID},2025,343692,343692,343692,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP (7630 meerwaarde wagen 26000 + 764/8 GroenWest/Marcade huurcorrectie 317692),{SRC_PDF},strong,tick2420; PDF p7+p23 native; YE2024 2168",
    f"bud_ruyschaert_pnl_jr2025_statutory,{EID},2025,241655,241655,241655,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 PROFIT FLIP,{SRC_PDF},strong,tick2420; PDF p8 native; YE2024 LOSS -479473; bedrijfswinst 9901 231417 FLIP; destin691 empty",
    f"bud_ruyschaert_bedrijfswinst_jr2025_statutory,{EID},2025,231417,231417,231417,NBB VOL-VZW code 9901 bedrijfswinst YE2025 PROFIT FLIP,{SRC_PDF},strong,tick2420; PDF p7 native; YE2024 LOSS -492989; 62 8461817 JUMP +0.23%",
    f"bud_ruyschaert_equity_jr2025_statutory,{EID},2025,449438,449438,449438,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +114.49%,{SRC_PDF},strong,tick2420; PDF p6 native; YE2024 209534; kapitaalsubsidies 3504 DROP; overgedragen 14 143980; fondsen 10 301954 FLAT; bestemde 13 empty",
    f"bud_ruyschaert_assets_jr2025_statutory,{EID},2025,2398167,2398167,2398167,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -4.90%,{SRC_PDF},strong,tick2420; PDF p5 native; YE2024 2521760; gebouwen 22 empty; 1 VE",
    f"bud_ruyschaert_debt_jr2025_statutory,{EID},2025,1797724,1797724,1797724,NBB VOL-VZW code 17/49 schulden YE2025 DROP -16.03%,{SRC_PDF},strong,tick2420; PDF p6 native; YE2024 2140726; 42/48 1776893 DROP; 44 221755 JUMP; 45 1325814; 48 229324 DROP was 541225; 17 empty",
    f"bud_ruyschaert_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (9905 241655 fully to overgedragen 14),{SRC_PDF},strong,tick2420; PDF p9 native; 9905 241655 + 14P -97675 = overgedragen 14 143980; destin691 empty",
])
print("entities+budgets ok")

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2427_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kisme"
SRC_PDF = "src_kisme_jr2025_nbb_pdf_2427"

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
    f'{EID},Kinderopvang Scholengroep Meetjesland VZW / KISME,ASBL Kinderopvang Scholengroep Meetjesland / KISME,KISME VZW (leftover city_eeklo CIK),parastatal,city_eeklo,nl,https://go-dynamiek.be/,kinderopvang@go-dynamiek.be,"Beukenstraat 1, 9900 Eeklo",tick2427 YE2025 Strong official native NBB PDF deposit 2026-00117266 + Strong KBO 0894.549.440 Actief 3 VE zetel Beukenstraat 1 9900 Eeklo RSZ2025 88.911; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto9900 DROP 630193 CIK envelope; pnl DROP 119349; 9901 DROP 110897; equity JUMP 1128223; assets JUMP 1232071; debt JUMP 103848; FTE 14.5; kapitaalsubsidies JUMP 144415; destin691 empty; cash DROP 77248; geldbeleggingen JUMP 469393; gebouwen empty; aanbouw JUMP 643866; leftover mined city_eeklo after Welzijnsband / Woonmaatschappij Meetjesland / HVZ Meetjesland / Ascendere; also leftover mined city_aalter Het Klaverwolkje; NOT Kloosterstraat 6 Drongen; NOT Kinderlach 0450.275.186; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT Kinderopvang Baloo BV 0762.684.274; NOT WZC De Linde Wortegem-Petegem 0425.773.085; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_kisme_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty,{SRC_PDF},strong,tick2427; PDF p5 native; VKT omzet unpublished; envelope is bruto 9900 630193",
    f"bud_kisme_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 empty,{SRC_PDF},strong,tick2427; PDF p5 native; VKT 73 unpublished; jaarverslag Opgroeien werkingssubsidies 621747.92 not booked on 73",
    f"bud_kisme_bruto_jr2025_statutory,{EID},2025,630193,630193,630193,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -0.44% (CIK envelope; omzet empty so bruto is envelope),{SRC_PDF},strong,tick2427; PDF p5 native; YE2024 632964; 76A empty",
    f"bud_kisme_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2427; PDF p5 native; 76A empty both years",
    f"bud_kisme_pnl_jr2025_statutory,{EID},2025,119349,119349,119349,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -31.78%,{SRC_PDF},strong,tick2427; PDF p5 native; YE2024 174950; bedrijfswinst 9901 110897 DROP; destin691 empty",
    f"bud_kisme_bedrijfswinst_jr2025_statutory,{EID},2025,110897,110897,110897,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -32.25%,{SRC_PDF},strong,tick2427; PDF p5 native; YE2024 163691; 62 519248 JUMP +10.65%",
    f"bud_kisme_equity_jr2025_statutory,{EID},2025,1128223,1128223,1128223,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +30.51%,{SRC_PDF},strong,tick2427; PDF p4 native; YE2024 864459; kapitaalsubsidies JUMP 144415; overgedragen 14 981808; fondsen 10 2000 FLAT",
    f"bud_kisme_assets_jr2025_statutory,{EID},2025,1232071,1232071,1232071,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +37.25%,{SRC_PDF},strong,tick2427; PDF p3 native; YE2024 897686; gebouwen 22 empty; aanbouw 27 JUMP 643866; 3 VE",
    f"bud_kisme_debt_jr2025_statutory,{EID},2025,103848,103848,103848,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +212.54%,{SRC_PDF},strong,tick2427; PDF p4 native; YE2024 33227; 42/48 103848; 44 49425; 45 52073",
    f"bud_kisme_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2427; PDF p6 native; 9905 119349 + destin691 empty = overgedragen 14 981808; YE2024 destin691 empty",
])
print("entities+budgets ok")

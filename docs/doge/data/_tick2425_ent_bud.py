#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2425_stamp.txt").read_text().strip().splitlines()
EID = "vzw_wzc_de_linde_wortegem"
SRC_PDF = "src_de_linde_wortegem_jr2025_nbb_pdf_2425"

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
    f'{EID},De Linde VZW / WZC De Linde (Wortegem-Petegem),ASBL De Linde / MRS De Linde Wortegem-Petegem,WZC De Linde Wortegem-Petegem VZW (leftover city_oudenaarde Quattro-lid WZC),parastatal,city_oudenaarde,nl,https://wzc-de-linde.be/,nadine@wzcdelinde.be,"Lindestraat 16, 9790 Wortegem-Petegem",tick2425 YE2025 Strong official native NBB PDF deposit 2026-00162292 + Strong KBO 0425.773.085 Actief 1 VE 2.189.365.521 Lindestraat 16 9790 Wortegem-Petegem RSZ2025 87.301; omzet70 JUMP 5515186 envelope (not commercial-only vs 73 1049648); 73 DROP 1049648; 76A JUMP 1500; opbr 70/76A JUMP 6683103; pnl PROFIT FLIP 62128; 9901 PROFIT FLIP 90793; equity JUMP 3155455; assets DROP 6379220; debt DROP 3223765; FTE 71.4; kapitaalsubsidies DROP 36182; destin691 JUMP 62128; cash JUMP 1196793; geldbeleggingen DROP 19621; gebouwen DROP 4339615; aanbouw empty; leftover nearby mined city_oudenaarde after SOLVA / HVVA; leftover unmined city_wortegem_petegem city GE; Quattro-lid after OLV Gasthuis Poperinge@2424 / Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT WZC De Linde Lievegem 0467.355.403; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_de_linde_wortegem_omzet_jr2025_statutory,{EID},2025,5515186,5515186,5515186,NBB VOL-VZW code 70 omzet YE2025 JUMP +5.94% (primary L5 envelope; omzet present and not commercial-only vs 73 1049648),{SRC_PDF},strong,tick2425; PDF p6 native; YE2024 5206034; envelope is omzet 70",
    f"bud_de_linde_wortegem_73_jr2025_statutory,{EID},2025,1049648,1049648,1049648,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -0.08%,{SRC_PDF},strong,tick2425; PDF p6 native; YE2024 1050540; 730-733 empty in notes; envelope remains omzet 70",
    f"bud_de_linde_wortegem_opbr_jr2025_statutory,{EID},2025,6683103,6683103,6683103,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +4.82% (VZW total; envelope remains omzet 70 because not commercial-only),{SRC_PDF},strong,tick2425; PDF p6 native; YE2024 6375889; 74 116769; 76A JUMP 1500",
    f"bud_de_linde_wortegem_76A_jr2025_statutory,{EID},2025,1500,1500,1500,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +135.85%,{SRC_PDF},strong,tick2425; PDF p6 native; YE2024 636; 7630 1500",
    f"bud_de_linde_wortegem_pnl_jr2025_statutory,{EID},2025,62128,62128,62128,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 PROFIT FLIP (was -151989),{SRC_PDF},strong,tick2425; PDF p7 native; YE2024 -151989; bedrijfswinst 9901 90793 PROFIT FLIP; destin691 62128",
    f"bud_de_linde_wortegem_bedrijfswinst_jr2025_statutory,{EID},2025,90793,90793,90793,NBB VOL-VZW code 9901 bedrijfswinst YE2025 PROFIT FLIP (was -126874),{SRC_PDF},strong,tick2425; PDF p6 native; YE2024 -126874; 62 4987141 JUMP +5.64%",
    f"bud_de_linde_wortegem_equity_jr2025_statutory,{EID},2025,3155455,3155455,3155455,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +1.65%,{SRC_PDF},strong,tick2425; PDF p5 native; YE2024 3104102; kapitaalsubsidies DROP 36182; overgedragen 14 empty; fondsen 10 1807689 FLAT; bestemde 13 1311584",
    f"bud_de_linde_wortegem_assets_jr2025_statutory,{EID},2025,6379220,6379220,6379220,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -0.54%,{SRC_PDF},strong,tick2425; PDF p4 native; YE2024 6413779; gebouwen 22 DROP 4339615; aanbouw 27 empty; 1 VE",
    f"bud_de_linde_wortegem_debt_jr2025_statutory,{EID},2025,3223765,3223765,3223765,NBB VOL-VZW code 17/49 schulden YE2025 DROP -2.60%,{SRC_PDF},strong,tick2425; PDF p5 native; YE2024 3309677; 173 1970545 DROP; 42 138600; 44 195580 DROP; 45 918898; 17 1970545",
    f"bud_de_linde_wortegem_destin_jr2025_statutory,{EID},2025,62128,62128,62128,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (100% of 9905),{SRC_PDF},strong,tick2425; PDF p8 native; 9905 62128 + destin691 62128 = overgedragen 14 empty; YE2024 destin691 empty (791 onttrekking 151989)",
])
print("entities+budgets ok")

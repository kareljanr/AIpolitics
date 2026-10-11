#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2423_stamp.txt").read_text().strip().splitlines()
EID = "vzw_huize_zonnelied"
SRC_PDF = "src_huize_zonnelied_jr2025_nbb_pdf_2423"

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
    f'{EID},Huize Zonnelied VZW,ASBL Huize Zonnelied,Huize Zonnelied VZW (leftover city_ieper Quattro-lid WZC),parastatal,city_ieper,nl,https://huizezonnelied.be/,info@huizezonnelied.be,"Stationsstraat 24, 8900 Ieper",tick2423 YE2025 Strong official native NBB PDF deposit 2026-00185108 + Strong KBO 0415.082.497 Actief 1 VE 2.150.803.764 Stationsstraat 24 Ieper RSZ2025 87.301; omzet70 JUMP 10947653 envelope (not commercial-only vs 73 2431251); 73 DROP 2431251 all 733; 76A empty; opbr 70/76A JUMP 13607953; pnl JUMP 280337; 9901 DROP 411779; equity JUMP 9780553; assets DROP 20080302; debt DROP 10217646; FTE 147.6; kapitaalsubsidies DROP 4944671; destin691 JUMP 240169; cash DROP 190094; geldbeleggingen JUMP 2390338; gebouwen DROP 10636541; aanbouw JUMP 1686141; leftover city_ieper after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT Zonnelied Roosdaal 0420.607.638; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT WZC De Linde Lievegem 0467.355.403; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_huize_zonnelied_omzet_jr2025_statutory,{EID},2025,10947653,10947653,10947653,NBB VOL-VZW code 70 omzet YE2025 JUMP +3.56% (primary L5 envelope; omzet present and not commercial-only vs 73 2431251),{SRC_PDF},strong,tick2423; PDF p7 native; YE2024 10571109; envelope is omzet 70",
    f"bud_huize_zonnelied_73_jr2025_statutory,{EID},2025,2431251,2431251,2431251,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 DROP -0.47% (all subsidies 733),{SRC_PDF},strong,tick2423; PDF p7+p26 native; YE2024 2442799; 730/731/732 empty; envelope remains omzet 70",
    f"bud_huize_zonnelied_opbr_jr2025_statutory,{EID},2025,13607953,13607953,13607953,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.85% (VZW total; envelope remains omzet 70 because not commercial-only),{SRC_PDF},strong,tick2423; PDF p7 native; YE2024 13230939; 74 JUMP 229049; 76A empty",
    f"bud_huize_zonnelied_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty,{SRC_PDF},strong,tick2423; PDF p7 native; YE2024 0",
    f"bud_huize_zonnelied_pnl_jr2025_statutory,{EID},2025,280337,280337,280337,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +65.15%,{SRC_PDF},strong,tick2423; PDF p8 native; YE2024 169750; bedrijfswinst 9901 411779 DROP; destin691 JUMP 240169",
    f"bud_huize_zonnelied_bedrijfswinst_jr2025_statutory,{EID},2025,411779,411779,411779,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -26.34%,{SRC_PDF},strong,tick2423; PDF p7 native; YE2024 559045; 62 10187453 JUMP +2.84%",
    f"bud_huize_zonnelied_equity_jr2025_statutory,{EID},2025,9780553,9780553,9780553,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +0.29%,{SRC_PDF},strong,tick2423; PDF p6 native; YE2024 9752721; kapitaalsubsidies DROP 4944671; overgedragen 14 1078730; fondsen 10 1590591 FLAT; bestemde 13 2166561",
    f"bud_huize_zonnelied_assets_jr2025_statutory,{EID},2025,20080302,20080302,20080302,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -4.62%,{SRC_PDF},strong,tick2423; PDF p5 native; YE2024 21052718; gebouwen 22 DROP 10636541; aanbouw 27 JUMP 1686141; 1 VE",
    f"bud_huize_zonnelied_debt_jr2025_statutory,{EID},2025,10217646,10217646,10217646,NBB VOL-VZW code 17/49 schulden YE2025 DROP -8.86%,{SRC_PDF},strong,tick2423; PDF p6 native; YE2024 11210419; 173 5873000 DROP; 42 1108124; 44 471876 JUMP; 45 1601773; 17 6322254",
    f"bud_huize_zonnelied_destin_jr2025_statutory,{EID},2025,240169,240169,240169,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +20.08% (200000 VIPA-aflossing + 40169 half-of-rest investeringen),{SRC_PDF},strong,tick2423; PDF p9 native; 9905 280337 + 14P 1038562 - destin691 240169 = overgedragen 14 1078730; destin691 JUMP vs YE2024 200000",
])
print("entities+budgets ok")

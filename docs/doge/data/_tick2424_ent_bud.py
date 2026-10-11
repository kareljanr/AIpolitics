#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2424_stamp.txt").read_text().strip().splitlines()
EID = "vzw_olv_gasthuis_poperinge"
SRC_PDF = "src_olv_gasthuis_jr2025_nbb_pdf_2424"

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
    f'{EID},Onze-Lieve-Vrouw Gasthuis VZW,ASBL Onze-Lieve-Vrouw Gasthuis,OLV Gasthuis Poperinge VZW (leftover city_poperinge Quattro-lid WZC),parastatal,city_poperinge,nl,https://www.gasthuis.be/,info@gasthuis.be,"Ieperstraat 130, 8970 Poperinge",tick2424 YE2025 Strong official native NBB PDF deposit 2026-00306712 + Strong KBO 0445.066.385 Actief 2 VE 2.150.784.463 Ieperstraat 130 + 2.272.821.549 WZC Emmaus Oostlaan 15 Poperinge RSZ2025 87.101; omzet70 JUMP 14151870 envelope (not commercial-only vs 73 2641315); 73 JUMP 2641315 (733 2637182 + 731 4133); 76A DROP 12831; opbr 70/76A JUMP 17008889; pnl LOSS IMPROVE -95063; 9901 LOSS IMPROVE -69796; equity DROP 9772731; assets DROP 15603053; debt DROP 5830322; FTE 191.8; kapitaalsubsidies DROP 0; destin691 empty; cash JUMP 1426890; geldbeleggingen DROP 2516447; gebouwen DROP 8807680; aanbouw DROP 466721; leftover city_poperinge after AGB De Kouter / De Lovie; Quattro-lid after Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT WZC OLV Roosdaal 0421.031.171; NOT Emmaus AZ 0411.515.075; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT WZC De Linde Lievegem 0467.355.403; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_olv_gasthuis_omzet_jr2025_statutory,{EID},2025,14151870,14151870,14151870,NBB VOL-VZW code 70 omzet YE2025 JUMP +4.32% (primary L5 envelope; omzet present and not commercial-only vs 73 2641315),{SRC_PDF},strong,tick2424; PDF p7 native; YE2024 13565417; uitsplitsing ouderenzorg 14151870; envelope is omzet 70",
    f"bud_olv_gasthuis_73_jr2025_statutory,{EID},2025,2641315,2641315,2641315,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +3.40% (subsidies 733 2637182 + schenkingen 731 4133),{SRC_PDF},strong,tick2424; PDF p7+p20 native; YE2024 2554343; 730/732 empty; envelope remains omzet 70",
    f"bud_olv_gasthuis_opbr_jr2025_statutory,{EID},2025,17008889,17008889,17008889,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +4.12% (VZW total; envelope remains omzet 70 because not commercial-only),{SRC_PDF},strong,tick2424; PDF p7 native; YE2024 16336359; 74 JUMP 202872; 76A DROP 12831",
    f"bud_olv_gasthuis_76A_jr2025_statutory,{EID},2025,12831,12831,12831,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -54.06%,{SRC_PDF},strong,tick2424; PDF p7 native; YE2024 27928",
    f"bud_olv_gasthuis_pnl_jr2025_statutory,{EID},2025,-95063,-95063,-95063,NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 LOSS IMPROVE (was -244629),{SRC_PDF},strong,tick2424; PDF p8 native; YE2024 -244629; bedrijfswinst 9901 -69796 LOSS IMPROVE; destin691 empty",
    f"bud_olv_gasthuis_bedrijfswinst_jr2025_statutory,{EID},2025,-69796,-69796,-69796,NBB VOL-VZW code 9901 bedrijfsverlies YE2025 LOSS IMPROVE (was -263284),{SRC_PDF},strong,tick2424; PDF p7 native; YE2024 -263284; 62 13300785 JUMP +4.01%",
    f"bud_olv_gasthuis_equity_jr2025_statutory,{EID},2025,9772731,9772731,9772731,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -0.97%,{SRC_PDF},strong,tick2424; PDF p6 native; YE2024 9868117; kapitaalsubsidies DROP 0; overgedragen 14 926671; fondsen 10 922191 FLAT; bestemde 13 7923868 FLAT",
    f"bud_olv_gasthuis_assets_jr2025_statutory,{EID},2025,15603053,15603053,15603053,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -2.55%,{SRC_PDF},strong,tick2424; PDF p5 native; YE2024 16011350; gebouwen 22 DROP 8807680; aanbouw 27 DROP 466721; 2 VE",
    f"bud_olv_gasthuis_debt_jr2025_statutory,{EID},2025,5830322,5830322,5830322,NBB VOL-VZW code 17/49 schulden YE2025 DROP -5.09%,{SRC_PDF},strong,tick2424; PDF p6 native; YE2024 6143233; 173 2777780 DROP; 42 352011; 44 395303 JUMP; 45 2170827; 17 2777780",
    f"bud_olv_gasthuis_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2424; PDF p9 native; 9905 -95063 + 14P 1021735 - destin691 0 = overgedragen 14 926671; destin691 empty vs YE2024 empty",
])
print("entities+budgets ok")

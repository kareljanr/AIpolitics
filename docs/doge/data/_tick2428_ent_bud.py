#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2428_stamp.txt").read_text().strip().splitlines()
EID = "vzw_duinhuisjes"
SRC_PDF = "src_duinhuisjes_jr2025_nbb_pdf_2428"

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
    f'{EID},Kinderopvang de Duinhuisjes VZW,ASBL Kinderopvang de Duinhuisjes,Kinderopvang de Duinhuisjes VZW (leftover city_knokke_heist CIK),parastatal,city_knokke_heist,nl,https://wp.duinhuisjes.be/,melissa.veldkamp@duinhuisjes.be,"Bremlaan 37, 8300 Knokke-Heist",tick2428 YE2025 Strong official native NBB PDF deposit 2026-00190043 + Strong KBO 0413.323.037 Actief 11 VE zetel Bremlaan 37 8300 Knokke-Heist RSZ2025 88.911 aanbestedende overheid; omzet70 JUMP 1311503 commercial-only vs large 73 5853919; 73 JUMP 5853919 all 733; 76A JUMP 313551; opbr 70/76A JUMP 7496361 envelope; pnl JUMP 457505; 9901 JUMP 474999; equity JUMP 2635555; assets JUMP 4697470; debt JUMP 2061915; FTE 93.4; kapitaalsubsidies DROP 863854; destin691 empty; cash JUMP 352995; geldbeleggingen empty; gebouwen JUMP 3185865; aanbouw empty; leftover mined city_knokke_heist after AGSO / Het Dak / BVK; also leftover mined city_brugge De Peuterhaven + leftover mined city_maldegem + leftover mined city_de_haan; NOT Kloosterstraat 6 Drongen; NOT t Bremhuisje 0445.265.533; NOT KISME 0894.549.440; NOT Kinderlach 0450.275.186; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT Kinderopvang Baloo BV 0762.684.274; NOT WZC De Linde Wortegem-Petegem 0425.773.085; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Jeugdhulp Don Bosco YE2024 not taken; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_duinhuisjes_omzet_jr2025_statutory,{EID},2025,1311503,1311503,1311503,NBB VOL-VZW code 70 omzet YE2025 JUMP +11.38% (ouderbijdragen; commercial-only vs large 73),{SRC_PDF},strong,tick2428; PDF p7 native; YE2024 1177535; envelope is 70/76A 7496361",
    f"bud_duinhuisjes_73_jr2025_statutory,{EID},2025,5853919,5853919,5853919,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +8.22% (all 733),{SRC_PDF},strong,tick2428; PDF p7+p21 native; YE2024 5409238; 730/731/732 empty",
    f"bud_duinhuisjes_opbr_jr2025_statutory,{EID},2025,7496361,7496361,7496361,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +13.14% (VZW envelope; omzet commercial-only vs large 73),{SRC_PDF},strong,tick2428; PDF p7 native; YE2024 6625762; 74 17388; 76A JUMP 313551",
    f"bud_duinhuisjes_76A_jr2025_statutory,{EID},2025,313551,313551,313551,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +1165.39% (764/8 andere),{SRC_PDF},strong,tick2428; PDF p7+p22 native; YE2024 24779; unexplained",
    f"bud_duinhuisjes_pnl_jr2025_statutory,{EID},2025,457505,457505,457505,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +13.74%,{SRC_PDF},strong,tick2428; PDF p8 native; YE2024 402233; bedrijfswinst 9901 474999 JUMP; destin691 empty",
    f"bud_duinhuisjes_bedrijfswinst_jr2025_statutory,{EID},2025,474999,474999,474999,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +15.73%,{SRC_PDF},strong,tick2428; PDF p7 native; YE2024 410449; 62 5450806 JUMP +8.12%",
    f"bud_duinhuisjes_equity_jr2025_statutory,{EID},2025,2635555,2635555,2635555,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +17.29%,{SRC_PDF},strong,tick2428; PDF p6 native; YE2024 2246966; kapitaalsubsidies DROP 863854; overgedragen 14 1646701; fondsen 10 125000 FLAT",
    f"bud_duinhuisjes_assets_jr2025_statutory,{EID},2025,4697470,4697470,4697470,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +15.86%,{SRC_PDF},strong,tick2428; PDF p5 native; YE2024 4054395; gebouwen 22 JUMP 3185865; aanbouw 27 empty; 11 VE",
    f"bud_duinhuisjes_debt_jr2025_statutory,{EID},2025,2061915,2061915,2061915,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +14.08%,{SRC_PDF},strong,tick2428; PDF p6 native; YE2024 1807429; 17 795481; 42/48 1262679",
    f"bud_duinhuisjes_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2428; PDF p9 native; 9905 457505 + destin691 empty = overgedragen 14 1646701; YE2024 destin691 empty",
])
print("entities+budgets ok")

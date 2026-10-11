#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2392_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_houtland"
SRC_PDF = "src_houtland_jr2025_nbb_pdf_2392"

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
    f'{EID},CAR Houtland-Westkust VZW (CAR t Veld Aartrijke-Zedelgem + CAR Elora Nieuwpoort),CAR Houtland-Westkust ASBL (CAR t Veld Aartrijke + CAR Elora Nieuport),CAR Houtland-Westkust VZW (2 outpatient CAR campuses leftover city_zedelgem + city_nieuwpoort),parastatal,city_zedelgem,nl,https://www.carelora.be/,info@carelora.be,"Ichtegemsestraat 32, 8211 Zedelgem",tick2392 YE2025 Strong official native NBB PDF deposit 2026-00115391 + Strong KBO 0408.436.019 Actief 2 VE RSZ2025 86.959; omzet70 JUMP 4926107 CAR envelope; 73 JUMP 1056007; 70/76A JUMP 6109882; pnl PROFIT FLIP 34332; equity JUMP 3945582; assets DROP 6149424; debt DROP 2103842; FTE 63; kapitaalsubsidies JUMP 1231624; destin691 empty; cash DROP 837963; leftover city_zedelgem + leftover city_nieuwpoort after De Schans@2391; AGB/FARO/Gandae YE2024; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_houtland_omzet_jr2025_statutory,{EID},2025,4926107,4926107,4926107,NBB VOL-VZW code 70 omzet YE2025 JUMP +2.51% (primary L5 envelope; CAR not commercial-only; 73 1056007; 70/76A 6109882),{SRC_PDF},strong,tick2392; PDF p6 native; YE2024 4805460; 73 1056007",
    f"bud_houtland_73_jr2025_statutory,{EID},2025,1056007,1056007,1056007,NBB VOL-VZW code 73 lidgeld schenkingen subsidies YE2025 JUMP +11.68%,{SRC_PDF},strong,tick2392; PDF p6 native; YE2024 945586; 731 9514; 733 1046493",
    f"bud_houtland_7076a_jr2025_statutory,{EID},2025,6109882,6109882,6109882,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.20%,{SRC_PDF},strong,tick2392; PDF p6 native; YE2024 5978212; 74 18455; 76A 109313",
    f"bud_houtland_pnl_jr2025_statutory,{EID},2025,34332,34332,34332,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 PROFIT FLIP,{SRC_PDF},strong,tick2392; PDF p7 native; YE2024 -86910; bedrijfswinst 9901 19339 PROFIT FLIP vs YE2024 -90942; destin691 empty; 791 empty",
    f"bud_houtland_equity_jr2025_statutory,{EID},2025,3945582,3945582,3945582,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +5.85%,{SRC_PDF},strong,tick2392; PDF p5 native; YE2024 3727458; kapitaalsubsidies 1231624 JUMP; overgedragen 14 326681; fondsen 10 900747; bestemde 13 1486530",
    f"bud_houtland_assets_jr2025_statutory,{EID},2025,6149424,6149424,6149424,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -0.08%,{SRC_PDF},strong,tick2392; PDF p4 native; YE2024 6154150; gebouwen 22 3531617; aanbouw 27 136226 JUMP",
    f"bud_houtland_debt_jr2025_statutory,{EID},2025,2103842,2103842,2103842,NBB VOL-VZW code 17/49 schulden YE2025 DROP -9.58%,{SRC_PDF},strong,tick2392; PDF p5 native; YE2024 2326692; LT 1100000; ST 1002615",
    f"bud_houtland_cash_jr2025_statutory,{EID},2025,837963,837963,837963,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -23.42%,{SRC_PDF},strong,tick2392; PDF p4 native; YE2024 1094248; geldbeleggingen 50/53 999454 JUMP vs 890998",
    f"bud_houtland_kapitaalsubsidies_jr2025_statutory,{EID},2025,1231624,1231624,1231624,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 JUMP +17.54%,{SRC_PDF},strong,tick2392; PDF p5 native; YE2024 1047832",
    f"bud_houtland_fte_jr2025_statutory,{EID},2025,63,63,63,NBB VOL-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 DROP -0.47%,{SRC_PDF},strong,tick2392; PDF p20 native; YE2024 63.3; personeel 62 5429501; 79 koppen code 9086",
])
print("entities+budgets ok")

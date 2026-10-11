#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2403_stamp.txt").read_text().strip().splitlines()
EID = "vzw_de_kade"
SRC_PDF = "src_dekade_jr2025_nbb_pdf_2403"

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
    f'{EID},De Kade VZW (Brugge / VAPH + CAR Spermalie + BuO Het Anker),ASBL De Kade Bruges,De Kade VZW (leftover city_brugge VAPH+CAR+BuO),parastatal,city_brugge,nl,https://de-kade.be/,info@de-kade.be,"Potterierei 42, 8000 Brugge",tick2403 YE2025 Strong official native NBB PDF deposit 2026-00300772 + Strong KBO 0413.650.659 Actief 35 VE RSZ2025 87.201; omzet70 JUMP 7767727 commercial-only vs large 73; 73 JUMP 51285974; 70/76A JUMP 60221495 VAPH+CAR+BuO envelope; pnl DROP 803199; equity JUMP 64477006; assets JUMP 86453940; debt JUMP 20196222; FTE 657.5; kapitaalsubsidies DROP 11803327; destin691 DROP 800000; cash DROP 5301142; geldbeleggingen JUMP 21930224; capex 2185673; leftover city_brugge after CFR Zelzate@2402; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_dekade_opbr_jr2025_statutory,{EID},2025,60221495,60221495,60221495,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.81% (primary L5 envelope; omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2403; PDF p7 native; YE2024 58577339; omzet70 7767727 JUMP +0.45%; 73 51285974 JUMP +3.02%; 74 1165704; 76A 2090",
    f"bud_dekade_73_jr2025_statutory,{EID},2025,51285974,51285974,51285974,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +3.02%,{SRC_PDF},strong,tick2403; PDF p7 native; YE2024 49782751; 731 62195 DROP; 732 1305; 733 51179710 JUMP",
    f"bud_dekade_pnl_jr2025_statutory,{EID},2025,803199,803199,803199,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -66.04%,{SRC_PDF},strong,tick2403; PDF p8 native; YE2024 2365138; bedrijfswinst 9901 747615 DROP -55.46%; destin691 800000 DROP",
    f"bud_dekade_bedrijfswinst_jr2025_statutory,{EID},2025,747615,747615,747615,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -55.46%,{SRC_PDF},strong,tick2403; PDF p7 native; YE2024 1678673; 62 48609106; 630 3575060",
    f"bud_dekade_equity_jr2025_statutory,{EID},2025,64477006,64477006,64477006,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +0.27%,{SRC_PDF},strong,tick2403; PDF p6 native; YE2024 64301634; kapitaalsubsidies 11803327 DROP; overgedragen 14 7260; bestemde 13 26226361",
    f"bud_dekade_assets_jr2025_statutory,{EID},2025,86453940,86453940,86453940,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +0.87%,{SRC_PDF},strong,tick2403; PDF p5 native; YE2024 85708946; gebouwen 22 40253767; aanbouw 27 10885",
    f"bud_dekade_debt_jr2025_statutory,{EID},2025,20196222,20196222,20196222,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +1.83%,{SRC_PDF},strong,tick2403; PDF p6 native; YE2024 19833252; LT 17 7019503; ST 42/48 11180415",
    f"bud_dekade_cash_jr2025_statutory,{EID},2025,5301142,5301142,5301142,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -71.99%,{SRC_PDF},strong,tick2403; PDF p5 native; YE2024 18926306; geldbeleggingen 50/53 21930224 JUMP +255.08%",
    f"bud_dekade_fte_jr2025_statutory,{EID},2025,657.5,657.5,657.5,NBB VOL-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +1.31%,{SRC_PDF},strong,tick2403; PDF p25 native; YE2024 649; personeel 62 48609106; 9086 828",
    f"bud_dekade_destin_jr2025_statutory,{EID},2025,800000,800000,800000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -66.60%,{SRC_PDF},strong,tick2403; PDF p9 native; YE2024 2395000; capex 2185673",
])
print("entities+budgets ok")

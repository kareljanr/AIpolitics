#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2401_stamp.txt").read_text().strip().splitlines()
EID = "vzw_verbint"
SRC_PDF = "src_verbint_jr2025_nbb_pdf_2401"

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
    f'{EID},VERBINT VZW / Carrewiel (fusie CAR Turnhout + CAR Zuiderkempen + CAR Vijfhoek),VERBINT ASBL / Carrewiel,VERBINT VZW (leftover city_turnhout CAR/CLB/WZC/VAPH after KMSI fusion),parastatal,city_turnhout,nl,https://www.verbint.be/,info@verbint.be,"Korte Begijnenstraat 22, 2300 Turnhout",tick2401 YE2025 Strong official native NBB PDF deposit 2026-00297392 + Strong KBO 0408.032.379 Actief 20 VE RSZ2025 85.691; omzet70 JUMP 12890158 not commercial-only; 73 JUMP 10059857; opbr7076A JUMP 31375466; 76A 6524604 meerwaarden; pnl JUMP 5963538 fusion+76A; equity JUMP 30969115; assets JUMP 48228242; debt JUMP 16245572; FTE 207.7; kapitaalsubsidies DROP 2615933; destin691 JUMP 284439; cash JUMP 6890725; leftover city_turnhout + city_mechelen + city_westerlo after ARC@2400; AGB/FARO/Gandae YE2024; Zelzate now live 2026-00243990 not taken; Noorderkempen scan not taken; NOT ARC 0408.434.930; NOT CAR Noorderkempen 0408.078.010; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_verbint_omzet_jr2025_statutory,{EID},2025,12890158,12890158,12890158,NBB VOL-VZW code 70 omzet YE2025 JUMP +79.21% (primary L5 envelope; not commercial-only; KMSI fusion not like-for-like),{SRC_PDF},strong,tick2401; PDF p6 native; YE2024 7192948; 73 10059857; 70/76A 31375466; 76A 6524604",
    f"bud_verbint_opbr_jr2025_statutory,{EID},2025,31375466,31375466,31375466,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +78.76% (includes 76A meerwaarden 6524604),{SRC_PDF},strong,tick2401; PDF p6 native; YE2024 17551685; 74 1900847; 66A 1388882",
    f"bud_verbint_73_jr2025_statutory,{EID},2025,10059857,10059857,10059857,NBB VOL-VZW code 73 lidgeld schenkingen subsidies YE2025 JUMP +12.69%,{SRC_PDF},strong,tick2401; PDF p6 native; YE2024 8927185; 6.9 731 2550 + 733 7583885 does not sum to 73",
    f"bud_verbint_pnl_jr2025_statutory,{EID},2025,5963538,5963538,5963538,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +791.4% (fusion + 76A meerwaarden),{SRC_PDF},strong,tick2401; PDF p7 native; YE2024 668995; bedrijfswinst 9901 5978070 JUMP; destin691 284439 JUMP",
    f"bud_verbint_bedrijfswinst_jr2025_statutory,{EID},2025,5978070,5978070,5978070,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +871.5%,{SRC_PDF},strong,tick2401; PDF p6 native; YE2024 615325; 76A 6524604; 66A 1388882",
    f"bud_verbint_equity_jr2025_statutory,{EID},2025,30969115,30969115,30969115,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +109.72% (KMSI fusion),{SRC_PDF},strong,tick2401; PDF p5 native; YE2024 14766643; kapitaalsubsidies 2615933 DROP; bestemde 13 6031592 JUMP",
    f"bud_verbint_assets_jr2025_statutory,{EID},2025,48228242,48228242,48228242,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +102.08% (KMSI fusion),{SRC_PDF},strong,tick2401; PDF p4 native; YE2024 23865928; gebouwen 22 24214101; aanbouw 27 65325",
    f"bud_verbint_debt_jr2025_statutory,{EID},2025,16245572,16245572,16245572,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +100.64% (includes KMSI-overgenomen kredieten),{SRC_PDF},strong,tick2401; PDF p5 native; YE2024 8097298; LT 17 10575609; ST 42/48 5192316",
    f"bud_verbint_cash_jr2025_statutory,{EID},2025,6890725,6890725,6890725,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +121.89%,{SRC_PDF},strong,tick2401; PDF p4 native; YE2024 3105490; geldbeleggingen 50/53 12298772 JUMP",
    f"bud_verbint_fte_jr2025_statutory,{EID},2025,207.7,207.7,207.7,NBB VOL-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +30.06%,{SRC_PDF},strong,tick2401; PDF p26 native; YE2024 159.7; personeel 62 16642024; 9086 223",
])
print("entities+budgets ok")

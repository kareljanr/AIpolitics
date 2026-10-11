#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2399_stamp.txt").read_text().strip().splitlines()
EID = "vzw_heuvelheem"
SRC_PDF = "src_heuvelheem_jr2025_nbb_pdf_2399"

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
    f'{EID},Heuvelheem VZW (VAPH zorgaanbieder / MFC + RTH + geïnterneerden Kruisem + Oudenaarde),Heuvelheem ASBL (prestataire VAPH Kruisem + Audenarde),Heuvelheem VZW (leftover city_kruisem + leftover city_oudenaarde VAPH care provider),parastatal,city_kruisem,nl,https://www.heuvelheem.be/,info@heuvelheem.be,"Nokerepontweg 1, 9772 Kruisem",tick2399 YE2025 Strong official native NBB PDF deposit 2026-00243798 + Strong KBO 0413.210.201 Actief 8 VE RSZ2025 87.202; omzet70 JUMP 181042 commercial-only; 73 JUMP 12221891; opbr7076A JUMP 15172213 VAPH envelope; pnl PROFIT FLIP 404772; equity JUMP 7254780; assets JUMP 10879683; debt JUMP 3267730; FTE 152.3; kapitaalsubsidies DROP 942213; destin691 empty; cash DROP 772792; leftover city_kruisem@932 + leftover city_oudenaarde after Halle Asse@2398; AGB/FARO/Gandae YE2024; NOT Vijvens 0415.093.385; NOT CAR Halle Asse 0425.788.230; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_heuvelheem_opbr_jr2025_statutory,{EID},2025,15172213,15172213,15172213,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +7.16% (primary L5 envelope; omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2399; PDF p6 native; YE2024 14158123; omzet70 181042; 73 12221891; 74 2503828; 76A 265452",
    f"bud_heuvelheem_73_jr2025_statutory,{EID},2025,12221891,12221891,12221891,NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +6.37%,{SRC_PDF},strong,tick2399; PDF p6 native; YE2024 11490437; 731 64024; 733 12157867",
    f"bud_heuvelheem_omzet_jr2025_statutory,{EID},2025,181042,181042,181042,NBB VOL-VZW code 70 omzet YE2025 JUMP +20.03% (commercial-only vs large 73),{SRC_PDF},strong,tick2399; PDF p6 native; YE2024 150825",
    f"bud_heuvelheem_pnl_jr2025_statutory,{EID},2025,404772,404772,404772,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 PROFIT FLIP,{SRC_PDF},strong,tick2399; PDF p7 native; YE2024 -72089; bedrijfswinst 9901 453416 PROFIT FLIP; destin691 empty",
    f"bud_heuvelheem_equity_jr2025_statutory,{EID},2025,7254780,7254780,7254780,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +4.65%,{SRC_PDF},strong,tick2399; PDF p5 native; YE2024 6932417; kapitaalsubsidies 942213 DROP; overgedragen 14 685153 JUMP",
    f"bud_heuvelheem_assets_jr2025_statutory,{EID},2025,10879683,10879683,10879683,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +13.22%,{SRC_PDF},strong,tick2399; PDF p4 native; YE2024 9609483; gebouwen 22 6132505; aanbouw 27 867145",
    f"bud_heuvelheem_debt_jr2025_statutory,{EID},2025,3267730,3267730,3267730,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +32.42%,{SRC_PDF},strong,tick2399; PDF p5 native; YE2024 2467775; LT 17 1699439; ST 42/48 1528231",
    f"bud_heuvelheem_cash_jr2025_statutory,{EID},2025,772792,772792,772792,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -43.83%,{SRC_PDF},strong,tick2399; PDF p4 native; YE2024 1375924; geldbeleggingen 50/53 206185",
    f"bud_heuvelheem_fte_jr2025_statutory,{EID},2025,152.3,152.3,152.3,NBB VOL-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 DROP -2.62%,{SRC_PDF},strong,tick2399; PDF p23 native; YE2024 156.4; personeel 62 11821579; capex 1894318",
    f"bud_heuvelheem_76A_jr2025_statutory,{EID},2025,265452,265452,265452,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP (VAPH 2024 afrekening surplus),{SRC_PDF},strong,tick2399; PDF p6+p39 native; YE2024 41633; VAPH 2024 afrekening 766904 minus raming 501452",
])
print("entities+budgets ok")

#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2400_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_antwerpen"
SRC_PDF = "src_arc_jr2025_nbb_pdf_2400"

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
    f'{EID},Antwerps Revalidatiecentrum VZW / CAR ARC Antwerpen,Centre de revalidation ambulatoire d Anvers ASBL,Antwerps Revalidatiecentrum VZW (leftover city_antwerpen ambulante revalidatie),parastatal,city_antwerpen,nl,https://www.antwerpsrevalidatiecentrum.be/,info@arc-reva.be,"Lange Elzenstraat 52-54, 2018 Antwerpen",tick2400 EVERY-10 YE2025 Strong official native NBB PDF deposit 2026-00272201 + Strong KBO 0408.434.930 Actief 1 VE RSZ2025 86.959; omzet70 empty VKT; 73 empty VKT; bruto9900 DROP 2489143 CAR envelope; pnl JUMP 174281; equity JUMP 1771285; assets JUMP 2168233; debt DROP 396948; FTE 30; kapitaalsubsidies DROP 81587; destin691 DROP 170000 nieuwbouwfonds; cash JUMP 779521; leftover city_antwerpen after Heuvelheem@2399; AGB/FARO/Gandae YE2024; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT CAR Antenne 3000 0433.184.479; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_arc_bruto_jr2025_statutory,{EID},2025,2489143,2489143,2489143,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -0.14% (primary L5 envelope; omzet 70 empty so bruto is envelope),{SRC_PDF},strong,tick2400 EVERY-10; PDF p5 native; YE2024 2492732; omzet70 empty; 73 empty; 76A 0",
    f"bud_arc_pnl_jr2025_statutory,{EID},2025,174281,174281,174281,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +11.86%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p5 native; YE2024 155804; bedrijfswinst 9901 156794 JUMP; destin691 170000 DROP nieuwbouwfonds",
    f"bud_arc_bedrijfswinst_jr2025_statutory,{EID},2025,156794,156794,156794,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +2.92%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p5 native; YE2024 152349; 76A 0; 66A 0",
    f"bud_arc_equity_jr2025_statutory,{EID},2025,1771285,1771285,1771285,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +9.55%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p4 native; YE2024 1616919; kapitaalsubsidies 81587 DROP; bestemde 13 1050000 JUMP",
    f"bud_arc_assets_jr2025_statutory,{EID},2025,2168233,2168233,2168233,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +6.04%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p3 native; YE2024 2044774; gebouwen 22 280301; aanbouw 27 empty",
    f"bud_arc_debt_jr2025_statutory,{EID},2025,396948,396948,396948,NBB VKT-VZW code 17/49 schulden YE2025 DROP -7.22%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p4 native; YE2024 427855; LT 17 empty; ST 42/48 374241",
    f"bud_arc_cash_jr2025_statutory,{EID},2025,779521,779521,779521,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +66.91%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p3 native; YE2024 467035; geldbeleggingen 50/53 880000 FLAT",
    f"bud_arc_kapitaalsubsidies_jr2025_statutory,{EID},2025,81587,81587,81587,NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -19.62%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p4 native; YE2024 101502",
    f"bud_arc_fte_jr2025_statutory,{EID},2025,30,30,30,NBB VKT-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +2.39%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p9 native; YE2024 29.3; personeel 62 2264763; capex 95710",
    f"bud_arc_destin_jr2025_statutory,{EID},2025,170000,170000,170000,NBB VKT-VZW code 691 toevoeging bestemde fondsen (nieuwbouwfonds) YE2025 DROP -80.68%,{SRC_PDF},strong,tick2400 EVERY-10; PDF p6 native; YE2024 880000; 791 empty; fonds 13 now 1050000",
])
print("entities+budgets ok")

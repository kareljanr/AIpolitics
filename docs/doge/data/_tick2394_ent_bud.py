#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2394_stamp.txt").read_text().strip().splitlines()
EID = "vzw_zwz"
SRC_PDF = "src_zwz_jr2025_nbb_pdf_2394"

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
    f'{EID},Zorg en Welzijn Zedelgem VZW / ZWZ (WZC Klaverveld + CKV + DVC Klaverbilk + Residentie Klaverhof),Zorg en Welzijn Zedelgem ASBL / ZWZ (MRPA Klaverveld + court sejour + centre de jour + residences assistees),ZWZ VZW (WZC leftover city_zedelgem PPS OCMW+Familiehulp+GVO),parastatal,city_zedelgem,nl,https://www.klaverveld.gvo.be/,info@zwz.be,"Fazantenlaan 89, 8210 Zedelgem",tick2394 YE2025 Strong official native NBB PDF deposit 2026-00228427 + Strong KBO 0832.024.923 Actief 1 VE RSZ2025 87.101; omzet70 JUMP 10693272 WZC envelope; 73 JUMP 1971245; 70/76A JUMP 13006495; pnl DROP 45054; equity DROP 12902648; assets JUMP 33038468; debt JUMP 20135821; FTE 120.2; kapitaalsubsidies DROP 5917611; destin691 empty; cash DROP 4229666; leftover city_zedelgem after Zonnebloem@2393; AGB/FARO/Gandae YE2024; NOT CAR Houtland-Westkust 0408.436.019; NOT Zonnebloem 0421.039.386; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_zwz_omzet_jr2025_statutory,{EID},2025,10693272,10693272,10693272,NBB VOL-VZW code 70 omzet YE2025 JUMP +5.08% (primary L5 envelope; WZC ouderenzorg not commercial-only),{SRC_PDF},strong,tick2394; PDF p7 native; YE2024 10175910; 73 1971245; 70/76A 13006495",
    f"bud_zwz_73_jr2025_statutory,{EID},2025,1971245,1971245,1971245,NBB VOL-VZW code 73 lidgeld schenkingen subsidies YE2025 JUMP +2.47% (733 subsidies 1971245; 731 empty),{SRC_PDF},strong,tick2394; PDF p7+p20 native; YE2024 1923731",
    f"bud_zwz_7076A_jr2025_statutory,{EID},2025,13006495,13006495,13006495,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +4.33%,{SRC_PDF},strong,tick2394; PDF p7 native; YE2024 12466269; 74 258178; 76A 83799",
    f"bud_zwz_pnl_jr2025_statutory,{EID},2025,45054,45054,45054,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -94.25%,{SRC_PDF},strong,tick2394; PDF p8 native; YE2024 783928; bedrijfswinst 9901 256073 DROP vs YE2024 802457; destin691 empty; 791 empty",
    f"bud_zwz_equity_jr2025_statutory,{EID},2025,12902648,12902648,12902648,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -3.92%,{SRC_PDF},strong,tick2394; PDF p6 native; YE2024 13429711; kapitaalsubsidies 5917611 DROP; overgedragen 14 3610743; fondsen 10 2625000; bestemde 13 749293",
    f"bud_zwz_assets_jr2025_statutory,{EID},2025,33038468,33038468,33038468,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +19.92%,{SRC_PDF},strong,tick2394; PDF p5 native; YE2024 27549707; gebouwen 22 21049473; aanbouw 27 0",
    f"bud_zwz_debt_jr2025_statutory,{EID},2025,20135821,20135821,20135821,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +42.61%,{SRC_PDF},strong,tick2394; PDF p6 native; YE2024 14119996; LT 16452173; ST 3384680; 173 bank 16452173",
    f"bud_zwz_cash_jr2025_statutory,{EID},2025,4229666,4229666,4229666,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -4.71%,{SRC_PDF},strong,tick2394; PDF p5 native; YE2024 4438804; geldbeleggingen 50/53 empty",
    f"bud_zwz_kapitaalsubsidies_jr2025_statutory,{EID},2025,5917611,5917611,5917611,NBB VOL-VZW code 15 kapitaalsubsidies YE2025 DROP -8.82%,{SRC_PDF},strong,tick2394; PDF p6 native; YE2024 6489728",
    f"bud_zwz_fte_jr2025_statutory,{EID},2025,120.2,120.2,120.2,NBB VOL-VZW code 9087 gemiddeld personeelsbestand VTE YE2025 JUMP +5.25%,{SRC_PDF},strong,tick2394; PDF p20 native; YE2024 114.2; personeel 62 8388859; capex 7363513",
])
print("entities+budgets ok")

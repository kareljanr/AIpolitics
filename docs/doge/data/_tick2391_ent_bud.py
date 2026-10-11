#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2391_stamp.txt").read_text().strip().splitlines()
EID = "vzw_de_schans"
SRC_PDF = "src_deschans_jr2025_nbb_pdf_2391"

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
    f'{EID},De Schans VZW (Kohesi-family property / psychosocial Heusden-Zolder + Beringen),De Schans ASBL (vehicule immobilier Kohesi),De Schans VZW (Kohesi-family property leftover city_heusden_zolder + city_beringen),parastatal,city_heusden_zolder,nl,https://www.kohesi.be/,info@kohesi.be,"Pastoor Paquaylaan 123 bus 1, 3550 Heusden-Zolder",tick2391 YE2025 Strong official native NBB PDF deposit 2026-00242881 + Strong KBO 0430.473.231 Actief 0 VE BTW2025 86.931+68.321; omzet70 empty; 73 FLAT 51177; bruto DROP 76192 MIC envelope; pnl DROP 12486; equity JUMP 529278; assets JUMP 1350530; debt JUMP 821252; FTE empty; kapitaalsubsidies DROP 15027; destin691 empty; cash JUMP 165386; leftover city_heusden_zolder + leftover city_beringen after LDSST@2390; AGB/FARO/Gandae YE2024; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT LDSST 0410.121.344; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_deschans_bruto_jr2025_statutory,{EID},2025,76192,76192,76192,NBB MIC-VZW code 9900 brutomarge YE2025 DROP -7.21% (primary L5 envelope; MIC; omzet empty so bruto is envelope; 73 51177 FLAT; 70/76A empty),{SRC_PDF},strong,tick2391; PDF p6 native; YE2024 82109; omzet empty; 73 51177",
    f"bud_deschans_73_jr2025_statutory,{EID},2025,51177,51177,51177,NBB MIC-VZW code 73 lidgeld schenkingen subsidies YE2025 FLAT,{SRC_PDF},strong,tick2391; PDF p6 native; YE2024 51177",
    f"bud_deschans_pnl_jr2025_statutory,{EID},2025,12486,12486,12486,NBB MIC-VZW code 9904 winst van het boekjaar YE2025 DROP -28.47%,{SRC_PDF},strong,tick2391; PDF p6 native; YE2024 17456; bedrijfswinst 9901 19901 DROP vs YE2024 25980; destin691 empty; 791 empty",
    f"bud_deschans_equity_jr2025_statutory,{EID},2025,529278,529278,529278,NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +2.18%,{SRC_PDF},strong,tick2391; PDF p5 native; YE2024 517969; kapitaalsubsidies 15027 DROP; overgedragen 14 149845; fondsen 10 364405",
    f"bud_deschans_assets_jr2025_statutory,{EID},2025,1350530,1350530,1350530,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +8.22%,{SRC_PDF},strong,tick2391; PDF p4 native; YE2024 1247977; gebouwen 22 1114602; aanbouw 27 30559 JUMP",
    f"bud_deschans_debt_jr2025_statutory,{EID},2025,821252,821252,821252,NBB MIC-VZW code 17/49 schulden YE2025 JUMP +12.50%,{SRC_PDF},strong,tick2391; PDF p5 native; YE2024 730008; LT 763239; financial LT 244279; overige LT 518960 JUMP vs 372000; ST 57909",
    f"bud_deschans_cash_jr2025_statutory,{EID},2025,165386,165386,165386,NBB MIC-VZW code 54/58 liquide middelen YE2025 JUMP +499.94%,{SRC_PDF},strong,tick2391; PDF p4 native; YE2024 27567; geldbeleggingen 50/53 empty; vlottend 168291 JUMP vs 30182",
    f"bud_deschans_kapitaalsubsidies_jr2025_statutory,{EID},2025,15027,15027,15027,NBB MIC-VZW code 15 kapitaalsubsidies YE2025 DROP -7.26%,{SRC_PDF},strong,tick2391; PDF p5 native; YE2024 16204",
    f"bud_deschans_gebouwen_jr2025_statutory,{EID},2025,1114602,1114602,1114602,NBB MIC-VZW code 22 terreinen en gebouwen YE2025,{SRC_PDF},strong,tick2391; PDF p4 native; YE2024 1160572; Harmoniestraat 9 Beringen onverdeeldheid REVA+CGG; hypotheek 91611 1114602",
    f"bud_deschans_capex_jr2025_statutory,{EID},2025,18346,18346,18346,NBB MIC-VZW code 8169 aanschaffingen MVA YE2025,{SRC_PDF},strong,tick2391; PDF p9 native; aanbouw 27 30559 JUMP vs 12760",
])
print("entities+budgets ok")

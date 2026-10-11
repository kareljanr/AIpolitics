#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgpr"
SRC = "src_cgpr_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgpr_assets_2025,{ENT},2025,8441644,,,executed,{SRC},strong,2025 assets 8441644 UP (was 8278112); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_vaste_2025,{ENT},2025,4371002,,,executed,{SRC},strong,2025 vaste activa 21/28 4371002 UP (was 2717402); IVA 21 empty; FVA 28 empty; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_mva_2025,{ENT},2025,4371002,,,executed,{SRC},strong,2025 MVA 22/27 4371002 UP (was 2717402); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_gebouwen_2025,{ENT},2025,2205089,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 2205089 (was 2256092); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_meubilair_2025,{ENT},2025,155254,,,executed,{SRC},strong,2025 meubilair 24 155254 UP (was 54652); installaties 23 empty; leasing 25 empty; overige 26 empty; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_inb_2025,{ENT},2025,2010659,,,executed,{SRC},strong,2025 in aanbouw 27 2010659 JUMP (was 406658); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_current_2025,{ENT},2025,4070642,,,executed,{SRC},strong,2025 vlottende 29/58 4070642 DROP (was 5560710); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_ltrecv_2025,{ENT},2025,167090,,,executed,{SRC},strong,2025 LT vorderingen 29 167090 (was 303891; all other 291); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_strecv_2025,{ENT},2025,907749,,,executed,{SRC},strong,2025 ST vorderingen 40/41 907749 (trade 239389 + other 668359 DROP was 1140357); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_beleg_2025,{ENT},2025,2165812,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 2165812 DROP (was 2368756); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_cash_2025,{ENT},2025,288830,,,executed,{SRC},strong,2025 liquide middelen 54/58 288830 DROP (was 953279); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_prepaid_2025,{ENT},2025,541161,,,executed,{SRC},strong,2025 overlopend actief 490/1 541161 (was 546678); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_equity_2025,{ENT},2025,5198486,,,executed,{SRC},strong,2025 eigen vermogen 10/15 5198486 DROP (was 5312636); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_fondsen_2025,{ENT},2025,4121,,,executed,{SRC},strong,2025 fondsen 10 4121 stable; overgedragen 14 empty; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_bestemde_2025,{ENT},2025,1855168,,,executed,{SRC},strong,2025 bestemde fondsen 13 1855168 DROP (was 1945727; onttrekking 791 90558; patrim 996460.90 / overige 146761.79 / sociaal 711945.57 = 19 pct pers); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_kapsubs_2025,{ENT},2025,3339197,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 3339197 (was 3362788); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_voorz_2025,{ENT},2025,8969,,,executed,{SRC},strong,2025 voorzieningen 16 8969 (all other 164/5; was 8969); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_debt_2025,{ENT},2025,3234189,,,executed,{SRC},strong,2025 schulden 17/49 3234189 UP (was 2956507); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_ltdebt_2025,{ENT},2025,2175076,,,executed,{SRC},strong,2025 LT schulden 17 2175076 UP (all krediet 172/3; was 1756201); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_stdebt_2025,{ENT},2025,1059113,,,executed,{SRC},strong,2025 ST schulden 42/48 1059113 (was 1178317; 42 100445 / lev 96214 / vooruit 1690 / taxsoc 852002 / other 8761); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_lev_2025,{ENT},2025,96214,,,executed,{SRC},strong,2025 leveranciers 440/4 96214 DROP (was 354344); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_taxsoc_2025,{ENT},2025,852002,,,executed,{SRC},strong,2025 tax/soc 45 852002 (tax 144390 + bezold 707612); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_bruto_2025,{ENT},2025,4186449,,,executed,{SRC},strong,2025 brutomarge 9900 4186449 UP (was 4083235); annual envelope VKT (omzet 70 empty; 73 empty); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_omzet_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 omzet 70 empty VKT; 73 empty; 60/61 empty; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_nrec_2025,{ENT},2025,38650,,,executed,{SRC},strong,2025 nrec 76A 38650 JUMP (was 9809); nrec kost 66A 5712; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_pers_2025,{ENT},2025,4142732,,,executed,{SRC},strong,2025 pers 62 4142732 / 47.8 VTE (was 3841213 / 44.2); YE 60 / YE VTE 50.7; 63110 uur; PC 331; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_afschr_2025,{ENT},2025,70101,,,executed,{SRC},strong,2025 afschrijvingen 630 70101 (was 199989); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_andere_2025,{ENT},2025,29856,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 29856 (was 16223); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_expl_2025,{ENT},2025,-61952,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -61952 LOSS (was +46827); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_finopbr_2025,{ENT},2025,54401,,,executed,{SRC},strong,2025 financiele opbrengsten 75 54401 (was 48416); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_finkost_2025,{ENT},2025,66704,,,executed,{SRC},strong,2025 financiele kosten 65 66704 JUMP (was 27289); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_tax_2025,{ENT},2025,16303,,,executed,{SRC},strong,2025 belastingen 67/77 16303 (was 13644); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_pnl_2025,{ENT},2025,-90558,,,executed,{SRC},strong,2025 verlies 9904 -90558 LOSS (was +54310); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_capex_2025,{ENT},2025,1723701,,,executed,{SRC},strong,2025 capex 8169 1723701 (VKT combined aanschaffingen; in aanbouw JUMP); tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
    f"bud_cgpr_hypotheek_2025,{ENT},2025,960228,,,executed,{SRC},strong,2025 hypotheek boekwaarde 91611 960228; inschrijving 25000; mandaat 975000; pand 500000; zakelijke zekerheid 1847999; tick1513; primary official NBB WVV VKT-VZW 2026-00209149",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

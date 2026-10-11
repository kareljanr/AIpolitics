#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwkp"
SRC = "src_cwkp_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwkp_assets_2025,{ENT},2025,19957060,,,executed,{SRC},strong,2025 assets 19957060 DROP (was 20021254); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_vaste_2025,{ENT},2025,15536639,,,executed,{SRC},strong,2025 vaste activa 21/28 15536639 DROP (was 16443067); IVA 21 63107 JUMP; FVA 28 empty; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_mva_2025,{ENT},2025,15473532,,,executed,{SRC},strong,2025 MVA 22/27 15473532 DROP (was 16443067); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_gebouwen_2025,{ENT},2025,9763949,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 9763949 DROP (was 10131824); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_install_2025,{ENT},2025,4992361,,,executed,{SRC},strong,2025 installaties 23 4992361 DROP (was 5397967); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_meubilair_2025,{ENT},2025,604220,,,executed,{SRC},strong,2025 meubilair 24 604220 DROP (was 786770); leasing 25 empty; overige 26 39155; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_inaanbouw_2025,{ENT},2025,73848,,,executed,{SRC},strong,2025 in aanbouw 27 73848 (was 73488); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_iva_2025,{ENT},2025,63107,,,executed,{SRC},strong,2025 IVA 21 63107 JUMP (was empty; aanschaffingen 8024 63107); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_current_2025,{ENT},2025,4420421,,,executed,{SRC},strong,2025 vlottende 29/58 4420421 UP (was 3578187); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_strecv_2025,{ENT},2025,1432935,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1432935 (trade 118203 + other 1314732); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_handelsrecv_2025,{ENT},2025,118203,,,executed,{SRC},strong,2025 handelsvorderingen 40 118203 DROP (was 127458); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_otherrecv_2025,{ENT},2025,1314732,,,executed,{SRC},strong,2025 overige ST 41 1314732 UP (was 1266095); LT other 291 2000; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_cash_2025,{ENT},2025,674251,,,executed,{SRC},strong,2025 liquide middelen 54/58 674251 UP (was 593135); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_beleg_2025,{ENT},2025,2200000,,,executed,{SRC},strong,2025 beleggingen 50/53 2200000 JUMP (was 1500000; termijn 53 1m-1y); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_prepaid_2025,{ENT},2025,111235,,,executed,{SRC},strong,2025 overlopende 490/1 111235 UP (was 78499); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_equity_2025,{ENT},2025,12442247,,,executed,{SRC},strong,2025 eigen vermogen 10/15 12442247 DROP (was 12949656); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_fondsen_2025,{ENT},2025,221756,,,executed,{SRC},strong,2025 fondsen 10 221756 stable; bestemde 13 775000 stable; overgedragen 14 2039319; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_kapsubs_2025,{ENT},2025,9406172,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 9406172 DROP (was 10023025); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_debt_2025,{ENT},2025,7514813,,,executed,{SRC},strong,2025 schulden 17/49 7514813 UP (was 7071598); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_ltdebt_2025,{ENT},2025,3712409,,,executed,{SRC},strong,2025 LT schulden 17 3712409 DROP (krediet 173 3712409 was 4044899); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_stdebt_2025,{ENT},2025,3616102,,,executed,{SRC},strong,2025 ST schulden 42/48 3616102 JUMP (was 2805385; current portion 336964 / lev 388136 / taxsoc 1936788 / other 954214); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_lev_2025,{ENT},2025,388136,,,executed,{SRC},strong,2025 leveranciers 440/4 388136 JUMP (was 271460); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_taxsoc_2025,{ENT},2025,1936788,,,executed,{SRC},strong,2025 tax/soc 45 1936788 JUMP (tax 143526 + bezold 1793262 was 1141844); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_otherst_2025,{ENT},2025,954214,,,executed,{SRC},strong,2025 overige ST 48 954214 UP (was 870454); overlopend 492/3 186302; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_opbr_2025,{ENT},2025,13824525,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 13824525 DROP (was 14072869); annual envelope; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_omzet_2025,{ENT},2025,595237,,,executed,{SRC},strong,2025 omzet 70 595237 DROP (was 671886); 6.9 category/geo empty; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_subs_2025,{ENT},2025,12796950,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 12796950 DROP (6.9 only 733 616853 + 731 143437 = 760290 of 12.80m); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_subs733_2025,{ENT},2025,616853,,,executed,{SRC},strong,2025 subsidies 733 disclosed 616853 (same prior); schenkingen 731 143437; 6.9 split incomplete vs 73 12796950; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_andere74_2025,{ENT},2025,432338,,,executed,{SRC},strong,2025 andere 74 432338 (was 434261); nrec 76A empty (was 20326); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_diensten_2025,{ENT},2025,1611119,,,executed,{SRC},strong,2025 diensten 61 1611119 JUMP (was 1427099); handelsgoederen 60 107297; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_pers_2025,{ENT},2025,10852214,,,executed,{SRC},strong,2025 pers 62 10852214 / 148 VTE (was 10568195 / 148.4); YE 190 / 208382 uur; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_afschr_2025,{ENT},2025,1026302,,,executed,{SRC},strong,2025 afschrijvingen 630 1026302 (was 1043150); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_expl_2025,{ENT},2025,112979,,,executed,{SRC},strong,2025 bedrijfswinst 9901 112979 DROP (was 818514); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_finopbr_2025,{ENT},2025,86736,,,executed,{SRC},strong,2025 financiele opbrengsten 75 86736 (was 102081); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_finkost_2025,{ENT},2025,64253,,,executed,{SRC},strong,2025 financiele kosten 65 64253 (schulden 62822); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_nrec_2025,{ENT},2025,5052,,,executed,{SRC},strong,2025 nrec 66A 5052 (was 4301); 76A empty; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_pnl_2025,{ENT},2025,109444,,,executed,{SRC},strong,2025 winst 9904 109444 DROP (was 818572); tax 67/77 26018; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; uit te keren winst empty); tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_capex_2025,{ENT},2025,125774,,,executed,{SRC},strong,2025 capex IVA 8024 63107 + MVA 8161 24264 + 8162 32143 + 8163 0 + 8166 6260 = 125774; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
    f"bud_cwkp_commissaris_2025,{ENT},2025,10250,,,executed,{SRC},strong,2025 commissaris 9505 10250; tick1526; primary official NBB WVV VOL-VZW 2026-00128692",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

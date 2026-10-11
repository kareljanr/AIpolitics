#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_wvwa"
SRC = "src_wvwa_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_wvwa_assets_2025,{ENT},2025,116281420,,,executed,{SRC},strong,2025 assets 116281420 DROP (was 178981322); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_current_2025,{ENT},2025,7199974,,,executed,{SRC},strong,2025 vlottend 7199974 DROP (was 10556842); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_cash_2025,{ENT},2025,2894405,,,executed,{SRC},strong,2025 liquide middelen 2894405 DROP (was 5636147); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_strecv_2025,{ENT},2025,1192316,,,executed,{SRC},strong,2025 ST vorderingen 1192316 (was 1080888); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_trade_2025,{ENT},2025,358509,,,executed,{SRC},strong,2025 handelsvorderingen 358509 DROP (was 378321); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_othrecv_2025,{ENT},2025,833807,,,executed,{SRC},strong,2025 overige ST vorderingen 833807 (was 702567); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_voorr_2025,{ENT},2025,1701979,,,executed,{SRC},strong,2025 voorraden 1701979 DROP (was 1989355; onroerend 35); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_prepaid_2025,{ENT},2025,1410332,,,executed,{SRC},strong,2025 overlopend actief 1410332 DROP (was 1849511); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_fixed_2025,{ENT},2025,109081446,,,executed,{SRC},strong,2025 vaste activa 109081446 DROP (was 168424480); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_mva_2025,{ENT},2025,109079702,,,executed,{SRC},strong,2025 MVA 109079702 DROP (was 168422736; terreinen/gebouwen 107891489); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_fva_2025,{ENT},2025,1744,,,executed,{SRC},strong,2025 FVA 1744 stable (was 1744); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_equity_2025,{ENT},2025,16952289,,,executed,{SRC},strong,2025 eigen vermogen 16952289 DROP (was 24842725); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_inbreng_2025,{ENT},2025,37986,,,executed,{SRC},strong,2025 inbreng 37986 onbeschikbaar (was 72967); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_reserves_2025,{ENT},2025,6162331,,,executed,{SRC},strong,2025 reserves 6162331 DROP (was 8862299); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_kapsubs_2025,{ENT},2025,10751972,,,executed,{SRC},strong,2025 kapitaalsubsidies 10751972 DROP (was 15907459); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_voorz_2025,{ENT},2025,1013298,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 1013298 (uitgestelde 377517); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_debt_2025,{ENT},2025,98315832,,,executed,{SRC},strong,2025 schulden 98315832 DROP (was 152277444; LT 89249713 + ST 8761200 + deferred 304920); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_ltdebt_2025,{ENT},2025,89249713,,,executed,{SRC},strong,2025 LT schulden 89249713 DROP (was 140837751; fin krediet 87065225); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_stdebt_2025,{ENT},2025,8761200,,,executed,{SRC},strong,2025 ST schulden 8761200 DROP (was 10675670; 42 4167090 + leveranciers 1826105); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_lev_2025,{ENT},2025,1826105,,,executed,{SRC},strong,2025 leveranciers 1826105 UP (was 1271832); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_deferred_2025,{ENT},2025,304920,,,executed,{SRC},strong,2025 overlopend passief 304920 DROP (was 764023); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_omzet_2025,{ENT},2025,11795988,,,executed,{SRC},strong,2025 omzet 70 11795988 UP (was 11766080); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_diensten_2025,{ENT},2025,7038929,,,executed,{SRC},strong,2025 diensten 61 7038929 JUMP (was 5686000); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_pers_2025,{ENT},2025,1918960,,,executed,{SRC},strong,2025 pers 62 1918960 UP; 22.7 VTE vs 22.2; YE 28; tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_afschr_2025,{ENT},2025,3898648,,,executed,{SRC},strong,2025 afschrijvingen 3898648 DROP (was 5239047); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_expl_2025,{ENT},2025,-251322,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -251322 vs -1146730; tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_finopbr_2025,{ENT},2025,1018477,,,executed,{SRC},strong,2025 financiele opbrengsten 1018477 DROP (was 2239079); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_finkost_2025,{ENT},2025,1739638,,,executed,{SRC},strong,2025 financiele kosten 1739638 DROP (was 3042291); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_pnl_2025,{ENT},2025,-960306,,,executed,{SRC},strong,2025 PnL 9904 -960306 vs -1919997; tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 empty; tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_capex_2025,{ENT},2025,1292536,,,executed,{SRC},strong,2025 capex MVA aanschaf 8161+8162+8163+8166 1292536; tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_in_aanbouw_2025,{ENT},2025,1018203,,,executed,{SRC},strong,2025 activa in aanbouw 1018203 DROP (was 4441362); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_krediet_2025,{ENT},2025,87065225,,,executed,{SRC},strong,2025 LT kredietinstellingen 87065225 DROP (was 138579146); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_terreinen_2025,{ENT},2025,107891489,,,executed,{SRC},strong,2025 terreinen en gebouwen 107891489 DROP (was 163903540); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_explsubs_2025,{ENT},2025,173498,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 173498 DROP (was 288329); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_nrec_opbr_2025,{ENT},2025,313964,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 313964 (was 164463); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_nrec_kost_2025,{ENT},2025,796,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 796; tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_andere_2025,{ENT},2025,1194303,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 1194303 (was 1130807); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_meubilair_2025,{ENT},2025,100165,,,executed,{SRC},strong,2025 meubilair en rollend materieel 100165 (was 75994); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_bestuur_2025,{ENT},2025,24068,,,executed,{SRC},strong,2025 bestuurders 9503 24068; commissaris 9505 18640 + extra 10890; tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_interim_2025,{ENT},2025,195567,,,executed,{SRC},strong,2025 interim 617 195567 / 1.7 VTE (was 10663 / 0.1); tick1502; primary official NBB WVV VOL",
    f"bud_wvwa_geldbeleg_2025,{ENT},2025,942,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 942 stable (was 942); tick1502; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

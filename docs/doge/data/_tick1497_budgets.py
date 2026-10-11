#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_thbw"
SRC = "src_thbw_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_thbw_assets_2025,{ENT},2025,202554297,,,executed,{SRC},strong,2025 assets 202554297 DROP (was 203592601); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_current_2025,{ENT},2025,23949367,,,executed,{SRC},strong,2025 vlottend 23949367 UP (was 20978216); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_cash_2025,{ENT},2025,10773820,,,executed,{SRC},strong,2025 liquide middelen 10773820 DROP (was 18259080); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_strecv_2025,{ENT},2025,3028259,,,executed,{SRC},strong,2025 ST vorderingen 3028259 JUMP (was 701660); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_trade_2025,{ENT},2025,284257,,,executed,{SRC},strong,2025 handelsvorderingen 284257 (was 237583); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_othrecv_2025,{ENT},2025,2744002,,,executed,{SRC},strong,2025 overige ST vorderingen 2744002 JUMP (was 464077); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_voorr_2025,{ENT},2025,438130,,,executed,{SRC},strong,2025 voorraden 438130 (was 438454); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_prepaid_2025,{ENT},2025,1709159,,,executed,{SRC},strong,2025 overlopend actief 1709159 (was 1579022); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_geldbeleg_2025,{ENT},2025,8000000,,,executed,{SRC},strong,2025 geldbeleggingen 8000000 JUMP (was empty); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_fixed_2025,{ENT},2025,178604930,,,executed,{SRC},strong,2025 vaste activa 178604930 DROP (was 182614385); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 0 empty; tick1497; primary official NBB WVV VOL",
    f"bud_thbw_mva_2025,{ENT},2025,178153092,,,executed,{SRC},strong,2025 MVA 178153092 DROP (was 182195796; terreinen/gebouwen 162980348); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_fva_2025,{ENT},2025,451839,,,executed,{SRC},strong,2025 FVA 451839 (was 418589); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_equity_2025,{ENT},2025,75921924,,,executed,{SRC},strong,2025 eigen vermogen 75921924 UP (was 72048131); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_inbreng_2025,{ENT},2025,17921,,,executed,{SRC},strong,2025 inbreng 17921 onbeschikbaar (was 18748); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_reserves_2025,{ENT},2025,53333210,,,executed,{SRC},strong,2025 reserves 53333210 (was 50608601); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_kapsubs_2025,{ENT},2025,22570793,,,executed,{SRC},strong,2025 kapitaalsubsidies 22570793 UP (was 21420782); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_voorz_2025,{ENT},2025,1567674,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 1567674 (uitgestelde 1494198); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_debt_2025,{ENT},2025,125064700,,,executed,{SRC},strong,2025 schulden 125064700 DROP (was 130108554; LT 115591074 + ST 8426778 + deferred 1046849); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_ltdebt_2025,{ENT},2025,115591074,,,executed,{SRC},strong,2025 LT schulden 115591074 DROP (was 121305078; fin krediet 113798252); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_stdebt_2025,{ENT},2025,8426778,,,executed,{SRC},strong,2025 ST schulden 8426778 (was 7729207; 42 4167143 + leveranciers 2554178); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_lev_2025,{ENT},2025,2554178,,,executed,{SRC},strong,2025 leveranciers 2554178 UP (was 2064797); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_deferred_2025,{ENT},2025,1046849,,,executed,{SRC},strong,2025 overlopend passief 1046849 (was 1074269); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_omzet_2025,{ENT},2025,12474312,,,executed,{SRC},strong,2025 omzet 70 12474312 DROP (was 12782802); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_diensten_2025,{ENT},2025,4084164,,,executed,{SRC},strong,2025 diensten 61 4084164 UP (was 3878691); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_pers_2025,{ENT},2025,1868369,,,executed,{SRC},strong,2025 pers 62 1868369 DROP; 20.1 VTE vs 19.6; 30638 uur; YE 28; tick1497; primary official NBB WVV VOL",
    f"bud_thbw_afschr_2025,{ENT},2025,4749085,,,executed,{SRC},strong,2025 afschrijvingen 4749085 (was 5118141); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_expl_2025,{ENT},2025,1828371,,,executed,{SRC},strong,2025 bedrijfswinst 9901 1828371 (was 1505908); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_finopbr_2025,{ENT},2025,3218545,,,executed,{SRC},strong,2025 financiele opbrengsten 3218545 (was 3014270); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_finkost_2025,{ENT},2025,2908658,,,executed,{SRC},strong,2025 financiele kosten 2908658 (was 2846943); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_pnl_2025,{ENT},2025,2048234,,,executed,{SRC},strong,2025 PnL 9904 2048234 UP (was 1590676); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_div_2025,{ENT},2025,1075,,,executed,{SRC},strong,2025 dividend 1075 (was 704); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_capex_2025,{ENT},2025,12121406,,,executed,{SRC},strong,2025 capex MVA aanschaf 8161+8163+8166 12121406; tick1497; primary official NBB WVV VOL",
    f"bud_thbw_in_aanbouw_2025,{ENT},2025,14985396,,,executed,{SRC},strong,2025 activa in aanbouw 14985396 DROP (was 18733801); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_krediet_2025,{ENT},2025,113798252,,,executed,{SRC},strong,2025 LT kredietinstellingen 113798252 DROP (was 119393315); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_terreinen_2025,{ENT},2025,162980348,,,executed,{SRC},strong,2025 terreinen en gebouwen 162980348 (was 163182259); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_explsubs_2025,{ENT},2025,302926,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 302926 UP (was 184251); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_nrec_opbr_2025,{ENT},2025,814059,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 814059 (was 934993); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_nrec_kost_2025,{ENT},2025,9363,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 9363 (was 197932); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_andere_2025,{ENT},2025,1187426,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 1187426 (was 1231742); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_meubilair_2025,{ENT},2025,109552,,,executed,{SRC},strong,2025 meubilair en rollend materieel 109552 (was 109583); tick1497; primary official NBB WVV VOL",
    f"bud_thbw_bestuur_2025,{ENT},2025,47446,,,executed,{SRC},strong,2025 bestuurders 9503 47446; commissaris 9505 12500; tick1497; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

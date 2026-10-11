#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_vivs"
SRC = "src_vivs_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_vivs_assets_2025,{ENT},2025,303989219,,,executed,{SRC},strong,2025 assets 303989219 UP (was 294143852); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_current_2025,{ENT},2025,15863617,,,executed,{SRC},strong,2025 vlottend 15863617 (was 15731829); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_cash_2025,{ENT},2025,10772582,,,executed,{SRC},strong,2025 liquide middelen 10772582 DROP (was 11076675); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_strecv_2025,{ENT},2025,543960,,,executed,{SRC},strong,2025 ST vorderingen 543960 (was 489550); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_trade_2025,{ENT},2025,350420,,,executed,{SRC},strong,2025 handelsvorderingen 350420 DROP (was 368993); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_othrecv_2025,{ENT},2025,193541,,,executed,{SRC},strong,2025 overige ST vorderingen 193541 (was 120557); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_voorr_2025,{ENT},2025,11768,,,executed,{SRC},strong,2025 voorraden 11768 (was 10673); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_prepaid_2025,{ENT},2025,2535307,,,executed,{SRC},strong,2025 overlopend actief 2535307 (was 2154932); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_geldbeleg_2025,{ENT},2025,2000000,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 2000000 stable (was 2000000); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_fixed_2025,{ENT},2025,288125601,,,executed,{SRC},strong,2025 vaste activa 288125601 UP (was 278412023); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_iva_2025,{ENT},2025,89954,,,executed,{SRC},strong,2025 IVA 89954 DROP (was 137535); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_mva_2025,{ENT},2025,287607993,,,executed,{SRC},strong,2025 MVA 287607993 UP (was 277937213; terreinen/gebouwen 283869779); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_fva_2025,{ENT},2025,427654,,,executed,{SRC},strong,2025 FVA 427654 (was 337275); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_equity_2025,{ENT},2025,63760761,,,executed,{SRC},strong,2025 eigen vermogen 63760761 UP (was 62928072); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_inbreng_2025,{ENT},2025,15300,,,executed,{SRC},strong,2025 inbreng 15300 onbeschikbaar (was 15666); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_reserves_2025,{ENT},2025,41164617,,,executed,{SRC},strong,2025 reserves 41164617 (was 40141357); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_kapsubs_2025,{ENT},2025,14970391,,,executed,{SRC},strong,2025 kapitaalsubsidies 14970391 (was 15160597); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_voorz_2025,{ENT},2025,2499879,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 2499879 (uitgestelde 1423406); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_debt_2025,{ENT},2025,237728579,,,executed,{SRC},strong,2025 schulden 237728579 UP (was 228854371; LT 224566356 + ST 11278017 + deferred 1884206); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_ltdebt_2025,{ENT},2025,224566356,,,executed,{SRC},strong,2025 LT schulden 224566356 UP (was 214722551; fin krediet 221592918); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_stdebt_2025,{ENT},2025,11278017,,,executed,{SRC},strong,2025 ST schulden 11278017 DROP (was 12522064; 42 7423796 + leveranciers 2123830); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_lev_2025,{ENT},2025,2123830,,,executed,{SRC},strong,2025 leveranciers 2123830 DROP (was 3489792); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_deferred_2025,{ENT},2025,1884206,,,executed,{SRC},strong,2025 overlopend passief 1884206 (was 1609756); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_omzet_2025,{ENT},2025,19547175,,,executed,{SRC},strong,2025 omzet 70 19547175 UP (was 18767838); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_diensten_2025,{ENT},2025,8278094,,,executed,{SRC},strong,2025 diensten 61 8278094 UP (was 7488449); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_pers_2025,{ENT},2025,3214483,,,executed,{SRC},strong,2025 pers 62 3214483 UP; 34.8 VTE vs 34.9; YE 44; tick1500; primary official NBB WVV VOL",
    f"bud_vivs_afschr_2025,{ENT},2025,8615672,,,executed,{SRC},strong,2025 afschrijvingen 8615672 (was 7723063); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_expl_2025,{ENT},2025,822724,,,executed,{SRC},strong,2025 bedrijfswinst 9901 822724 (was 1041828); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_finopbr_2025,{ENT},2025,5275612,,,executed,{SRC},strong,2025 financiele opbrengsten 5275612 (was 4707961); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_finkost_2025,{ENT},2025,5049365,,,executed,{SRC},strong,2025 financiele kosten 5049365 (was 4727677); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_pnl_2025,{ENT},2025,1023260,,,executed,{SRC},strong,2025 PnL 9904 1023260 (was 1022275); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 empty; tick1500; primary official NBB WVV VOL",
    f"bud_vivs_capex_2025,{ENT},2025,18581782,,,executed,{SRC},strong,2025 capex MVA aanschaf 8161+8163+8166 18581782; tick1500; primary official NBB WVV VOL",
    f"bud_vivs_in_aanbouw_2025,{ENT},2025,3421563,,,executed,{SRC},strong,2025 activa in aanbouw 3421563 DROP (was 9759103); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_krediet_2025,{ENT},2025,221592918,,,executed,{SRC},strong,2025 LT kredietinstellingen 221592918 UP (was 211912340); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_terreinen_2025,{ENT},2025,283869779,,,executed,{SRC},strong,2025 terreinen en gebouwen 283869779 UP (was 267805887); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_explsubs_2025,{ENT},2025,927449,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 927449 (was 889046); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_nrec_opbr_2025,{ENT},2025,745039,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 745039 (was 642245); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_nrec_kost_2025,{ENT},2025,240243,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 240243 (was 14672); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_andere_2025,{ENT},2025,1336909,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 1336909 UP (was 1166199); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_meubilair_2025,{ENT},2025,225485,,,executed,{SRC},strong,2025 meubilair en rollend materieel 225485 (was 256533); tick1500; primary official NBB WVV VOL",
    f"bud_vivs_bestuur_2025,{ENT},2025,43700,,,executed,{SRC},strong,2025 bestuurders 9503 43700; commissaris 9505 14757 + extra 3267; tick1500; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_wpij"
SRC = "src_wpij_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_wpij_assets_2025,{ENT},2025,105006637,,,executed,{SRC},strong,2025 assets 105006637 UP (was 89532767); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_current_2025,{ENT},2025,5235187,,,executed,{SRC},strong,2025 vlottend 5235187 DROP (was 6085108); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_cash_2025,{ENT},2025,2667094,,,executed,{SRC},strong,2025 liquide middelen 2667094 DROP (was 3462411); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_strecv_2025,{ENT},2025,755044,,,executed,{SRC},strong,2025 ST vorderingen 755044 DROP (was 995249); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_trade_2025,{ENT},2025,100530,,,executed,{SRC},strong,2025 handelsvorderingen 100530 DROP (was 196906); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_othrecv_2025,{ENT},2025,654515,,,executed,{SRC},strong,2025 overige ST vorderingen 654515 DROP (was 798343); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_voorr_2025,{ENT},2025,899504,,,executed,{SRC},strong,2025 voorraden 899504 (was 900689; onroerend te koop 896822); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_prepaid_2025,{ENT},2025,913545,,,executed,{SRC},strong,2025 overlopend actief 913545 UP (was 726759); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_geldbeleg_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 empty; tick1498; primary official NBB WVV VOL",
    f"bud_wpij_fixed_2025,{ENT},2025,99771450,,,executed,{SRC},strong,2025 vaste activa 99771450 UP (was 83447659); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 0 empty; tick1498; primary official NBB WVV VOL",
    f"bud_wpij_mva_2025,{ENT},2025,99714624,,,executed,{SRC},strong,2025 MVA 99714624 UP (was 83409192; terreinen/gebouwen 76634177); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_fva_2025,{ENT},2025,56826,,,executed,{SRC},strong,2025 FVA 56826 (was 38467); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_equity_2025,{ENT},2025,12170207,,,executed,{SRC},strong,2025 eigen vermogen 12170207 DROP (was 12368760); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_inbreng_2025,{ENT},2025,8032,,,executed,{SRC},strong,2025 inbreng 8032 onbeschikbaar (was 8032); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_reserves_2025,{ENT},2025,7250595,,,executed,{SRC},strong,2025 reserves 7250595 (was 7250595); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_kapsubs_2025,{ENT},2025,5374676,,,executed,{SRC},strong,2025 kapitaalsubsidies 5374676 UP (was 5110133); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_voorz_2025,{ENT},2025,399139,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 399139 (uitgestelde 287817); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_debt_2025,{ENT},2025,92437291,,,executed,{SRC},strong,2025 schulden 92437291 UP (was 76794722; LT 84995570 + ST 6806450 + deferred 635271); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_ltdebt_2025,{ENT},2025,84995570,,,executed,{SRC},strong,2025 LT schulden 84995570 UP (was 71660311; fin krediet 83973820); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_stdebt_2025,{ENT},2025,6806450,,,executed,{SRC},strong,2025 ST schulden 6806450 UP (was 4531562; 42 2863677 + leveranciers 2863589); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_lev_2025,{ENT},2025,2863589,,,executed,{SRC},strong,2025 leveranciers 2863589 JUMP (was 1218838); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_deferred_2025,{ENT},2025,635271,,,executed,{SRC},strong,2025 overlopend passief 635271 (was 602849); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_omzet_2025,{ENT},2025,7083881,,,executed,{SRC},strong,2025 omzet 70 7083881 UP (was 5652106); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_diensten_2025,{ENT},2025,2759089,,,executed,{SRC},strong,2025 diensten 61 2759089 UP (was 2190916); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_pers_2025,{ENT},2025,1513868,,,executed,{SRC},strong,2025 pers 62 1513868 UP; 17.4 VTE vs 16.5; 25207 uur; YE 19; tick1498; primary official NBB WVV VOL",
    f"bud_wpij_afschr_2025,{ENT},2025,2574649,,,executed,{SRC},strong,2025 afschrijvingen 2574649 (was 2501751); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_expl_2025,{ENT},2025,-335978,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -335978 (was 386049); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_finopbr_2025,{ENT},2025,1776533,,,executed,{SRC},strong,2025 financiele opbrengsten 1776533 (was 1400973); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_finkost_2025,{ENT},2025,1899558,,,executed,{SRC},strong,2025 financiele kosten 1899558 (was 1579165); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_pnl_2025,{ENT},2025,-463096,,,executed,{SRC},strong,2025 PnL 9904 -463096 LOSS (was 212474); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 empty; tick1498; primary official NBB WVV VOL",
    f"bud_wpij_capex_2025,{ENT},2025,19327583,,,executed,{SRC},strong,2025 capex MVA aanschaf 8161+8162+8163+8166 19327583; tick1498; primary official NBB WVV VOL",
    f"bud_wpij_in_aanbouw_2025,{ENT},2025,22959832,,,executed,{SRC},strong,2025 activa in aanbouw 22959832 JUMP (was 8646578); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_krediet_2025,{ENT},2025,83973820,,,executed,{SRC},strong,2025 LT kredietinstellingen 83973820 UP (was 70799754); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_terreinen_2025,{ENT},2025,76634177,,,executed,{SRC},strong,2025 terreinen en gebouwen 76634177 UP (was 74670842); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_explsubs_2025,{ENT},2025,401622,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 401622 DROP (was 758180); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_nrec_opbr_2025,{ENT},2025,514,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 514 (was 23124); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_nrec_kost_2025,{ENT},2025,447503,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 447503 JUMP (was empty); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_andere_2025,{ENT},2025,731267,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 731267 UP (was 409574); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_meubilair_2025,{ENT},2025,81265,,,executed,{SRC},strong,2025 meubilair en rollend materieel 81265 (was 50572); tick1498; primary official NBB WVV VOL",
    f"bud_wpij_bestuur_2025,{ENT},2025,44703,,,executed,{SRC},strong,2025 bestuurders 9503 44703; commissaris 9505 15400; tick1498; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

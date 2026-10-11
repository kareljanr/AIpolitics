#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_elan"
SRC = "src_elan_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_elan_assets_2025,{ENT},2025,179416827,,,executed,{SRC},strong,2025 assets 179416827 UP (was 168700695); tick1499; primary official NBB WVV VOL",
    f"bud_elan_current_2025,{ENT},2025,26684346,,,executed,{SRC},strong,2025 vlottend 26684346 DROP (was 27558192); tick1499; primary official NBB WVV VOL",
    f"bud_elan_cash_2025,{ENT},2025,9893916,,,executed,{SRC},strong,2025 liquide middelen 9893916 DROP (was 25619244); tick1499; primary official NBB WVV VOL",
    f"bud_elan_strecv_2025,{ENT},2025,564962,,,executed,{SRC},strong,2025 ST vorderingen 564962 DROP (was 762579); tick1499; primary official NBB WVV VOL",
    f"bud_elan_trade_2025,{ENT},2025,215204,,,executed,{SRC},strong,2025 handelsvorderingen 215204 DROP (was 423739); tick1499; primary official NBB WVV VOL",
    f"bud_elan_othrecv_2025,{ENT},2025,349758,,,executed,{SRC},strong,2025 overige ST vorderingen 349758 (was 338840); tick1499; primary official NBB WVV VOL",
    f"bud_elan_voorr_2025,{ENT},2025,18430,,,executed,{SRC},strong,2025 voorraden 18430 (was 9772); tick1499; primary official NBB WVV VOL",
    f"bud_elan_prepaid_2025,{ENT},2025,1207038,,,executed,{SRC},strong,2025 overlopend actief 1207038 (was 1166597); tick1499; primary official NBB WVV VOL",
    f"bud_elan_geldbeleg_2025,{ENT},2025,15000000,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 15000000 JUMP (was 0); tick1499; primary official NBB WVV VOL",
    f"bud_elan_fixed_2025,{ENT},2025,152732481,,,executed,{SRC},strong,2025 vaste activa 152732481 UP (was 141142503); tick1499; primary official NBB WVV VOL",
    f"bud_elan_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 0 empty; tick1499; primary official NBB WVV VOL",
    f"bud_elan_mva_2025,{ENT},2025,152618169,,,executed,{SRC},strong,2025 MVA 152618169 UP (was 141091928; terreinen/gebouwen 133946458); tick1499; primary official NBB WVV VOL",
    f"bud_elan_fva_2025,{ENT},2025,114312,,,executed,{SRC},strong,2025 FVA 114312 (was 50575); tick1499; primary official NBB WVV VOL",
    f"bud_elan_equity_2025,{ENT},2025,40289353,,,executed,{SRC},strong,2025 eigen vermogen 40289353 UP (was 38559133); tick1499; primary official NBB WVV VOL",
    f"bud_elan_inbreng_2025,{ENT},2025,20502,,,executed,{SRC},strong,2025 inbreng 20502 onbeschikbaar (was 21133); tick1499; primary official NBB WVV VOL",
    f"bud_elan_reserves_2025,{ENT},2025,32000618,,,executed,{SRC},strong,2025 reserves 32000618 (was 30320590); tick1499; primary official NBB WVV VOL",
    f"bud_elan_kapsubs_2025,{ENT},2025,8268234,,,executed,{SRC},strong,2025 kapitaalsubsidies 8268234 (was 8217410); tick1499; primary official NBB WVV VOL",
    f"bud_elan_voorz_2025,{ENT},2025,2189417,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 2189417 (uitgestelde 696565); tick1499; primary official NBB WVV VOL",
    f"bud_elan_debt_2025,{ENT},2025,136938057,,,executed,{SRC},strong,2025 schulden 136938057 UP (was 127894325; LT 123437889 + ST 12815600 + deferred 684569); tick1499; primary official NBB WVV VOL",
    f"bud_elan_ltdebt_2025,{ENT},2025,123437889,,,executed,{SRC},strong,2025 LT schulden 123437889 UP (was 120210089; fin krediet 121852403); tick1499; primary official NBB WVV VOL",
    f"bud_elan_stdebt_2025,{ENT},2025,12815600,,,executed,{SRC},strong,2025 ST schulden 12815600 UP (was 6969649; 42 9793499 + leveranciers 1403540); tick1499; primary official NBB WVV VOL",
    f"bud_elan_lev_2025,{ENT},2025,1403540,,,executed,{SRC},strong,2025 leveranciers 1403540 (was 1261547); tick1499; primary official NBB WVV VOL",
    f"bud_elan_deferred_2025,{ENT},2025,684569,,,executed,{SRC},strong,2025 overlopend passief 684569 (was 714587); tick1499; primary official NBB WVV VOL",
    f"bud_elan_omzet_2025,{ENT},2025,10963582,,,executed,{SRC},strong,2025 omzet 70 10963582 UP (was 9886881); tick1499; primary official NBB WVV VOL",
    f"bud_elan_diensten_2025,{ENT},2025,3874175,,,executed,{SRC},strong,2025 diensten 61 3874175 UP (was 3094399); tick1499; primary official NBB WVV VOL",
    f"bud_elan_pers_2025,{ENT},2025,2241828,,,executed,{SRC},strong,2025 pers 62 2241828 UP; 26.8 VTE vs 22.5; 39839 uur; YE 31; tick1499; primary official NBB WVV VOL",
    f"bud_elan_afschr_2025,{ENT},2025,4544707,,,executed,{SRC},strong,2025 afschrijvingen 4544707 (was 4432056); tick1499; primary official NBB WVV VOL",
    f"bud_elan_expl_2025,{ENT},2025,1749827,,,executed,{SRC},strong,2025 bedrijfswinst 9901 1749827 (was 759596); tick1499; primary official NBB WVV VOL",
    f"bud_elan_finopbr_2025,{ENT},2025,2588861,,,executed,{SRC},strong,2025 financiele opbrengsten 2588861 (was 2121370); tick1499; primary official NBB WVV VOL",
    f"bud_elan_finkost_2025,{ENT},2025,2590525,,,executed,{SRC},strong,2025 financiele kosten 2590525 (was 2340622); tick1499; primary official NBB WVV VOL",
    f"bud_elan_pnl_2025,{ENT},2025,1657825,,,executed,{SRC},strong,2025 PnL 9904 1657825 (was 499290); tick1499; primary official NBB WVV VOL",
    f"bud_elan_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 empty; tick1499; primary official NBB WVV VOL",
    f"bud_elan_capex_2025,{ENT},2025,16411769,,,executed,{SRC},strong,2025 capex MVA aanschaf 8161+8163+8166 16411769; tick1499; primary official NBB WVV VOL",
    f"bud_elan_in_aanbouw_2025,{ENT},2025,18379907,,,executed,{SRC},strong,2025 activa in aanbouw 18379907 (was 13812479); tick1499; primary official NBB WVV VOL",
    f"bud_elan_krediet_2025,{ENT},2025,121852403,,,executed,{SRC},strong,2025 LT kredietinstellingen 121852403 UP (was 118688936); tick1499; primary official NBB WVV VOL",
    f"bud_elan_terreinen_2025,{ENT},2025,133946458,,,executed,{SRC},strong,2025 terreinen en gebouwen 133946458 UP (was 126982222); tick1499; primary official NBB WVV VOL",
    f"bud_elan_explsubs_2025,{ENT},2025,122022,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 122022 DROP (was 320786); tick1499; primary official NBB WVV VOL",
    f"bud_elan_nrec_opbr_2025,{ENT},2025,2144408,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 2144408 JUMP (was 993235); tick1499; primary official NBB WVV VOL",
    f"bud_elan_nrec_kost_2025,{ENT},2025,2458,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 2458 (was 7244); tick1499; primary official NBB WVV VOL",
    f"bud_elan_andere_2025,{ENT},2025,1385354,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 1385354 UP (was 1059474); tick1499; primary official NBB WVV VOL",
    f"bud_elan_meubilair_2025,{ENT},2025,187747,,,executed,{SRC},strong,2025 meubilair en rollend materieel 187747 (was 175562); tick1499; primary official NBB WVV VOL",
    f"bud_elan_bestuur_2025,{ENT},2025,51066,,,executed,{SRC},strong,2025 bestuurders 9503 51066; commissaris 9505 10238 + extra 3200; tick1499; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

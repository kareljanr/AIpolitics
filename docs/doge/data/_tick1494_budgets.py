#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_ijez"
SRC = "src_ijez_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_ijez_assets_2025,{ENT},2025,182256295,,,executed,{SRC},strong,2025 assets 182256295 DROP (was 192614151); tick1494; primary official NBB WVV",
    f"bud_ijez_current_2025,{ENT},2025,26514377,,,executed,{SRC},strong,2025 vlottend 26514377 (was 26409113); tick1494; primary official NBB WVV",
    f"bud_ijez_cash_2025,{ENT},2025,13132132,,,executed,{SRC},strong,2025 liquide middelen 13132132 UP (was 12782367); tick1494; primary official NBB WVV",
    f"bud_ijez_beleg_2025,{ENT},2025,5000000,,,executed,{SRC},strong,2025 geldbeleggingen 5000000 JUMP (was 3500000); tick1494; primary official NBB WVV",
    f"bud_ijez_strecv_2025,{ENT},2025,689130,,,executed,{SRC},strong,2025 ST vorderingen 689130 (was 440529); tick1494; primary official NBB WVV",
    f"bud_ijez_trade_2025,{ENT},2025,430320,,,executed,{SRC},strong,2025 handelsvorderingen 430320 (was 324233); tick1494; primary official NBB WVV",
    f"bud_ijez_othrecv_2025,{ENT},2025,258809,,,executed,{SRC},strong,2025 overige ST vorderingen 258809 (was 116296); tick1494; primary official NBB WVV",
    f"bud_ijez_voorr_2025,{ENT},2025,6512284,,,executed,{SRC},strong,2025 voorraden 6512284 DROP (was 8509760; onroerend verkoop 6512284); tick1494; primary official NBB WVV",
    f"bud_ijez_prepaid_2025,{ENT},2025,1180831,,,executed,{SRC},strong,2025 overlopend actief 1180831 (was 1176458); tick1494; primary official NBB WVV",
    f"bud_ijez_fixed_2025,{ENT},2025,155741918,,,executed,{SRC},strong,2025 vaste activa 155741918 DROP (was 166205037); tick1494; primary official NBB WVV",
    f"bud_ijez_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 0 empty; tick1494; primary official NBB WVV",
    f"bud_ijez_mva_2025,{ENT},2025,155688519,,,executed,{SRC},strong,2025 MVA 155688519 DROP (was 166142640; terreinen/gebouwen 153430074); tick1494; primary official NBB WVV",
    f"bud_ijez_fva_2025,{ENT},2025,53399,,,executed,{SRC},strong,2025 FVA 53399 (was 62397; andere FVA aandelen 35558 + borg 17841); tick1494; primary official NBB WVV",
    f"bud_ijez_equity_2025,{ENT},2025,39032061,,,executed,{SRC},strong,2025 eigen vermogen 39032061 DROP (was 40072241); tick1494; primary official NBB WVV",
    f"bud_ijez_inbreng_2025,{ENT},2025,132547,,,executed,{SRC},strong,2025 inbreng 132547 onbeschikbaar (was 145583); tick1494; primary official NBB WVV",
    f"bud_ijez_reserves_2025,{ENT},2025,27494256,,,executed,{SRC},strong,2025 reserves 27494256 (was 28042405); tick1494; primary official NBB WVV",
    f"bud_ijez_kapsubs_2025,{ENT},2025,11405258,,,executed,{SRC},strong,2025 kapitaalsubsidies 11405258 (was 11884253); tick1494; primary official NBB WVV",
    f"bud_ijez_voorz_2025,{ENT},2025,2703922,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 2703922 (herstel 1902920; overige 190000; uitgestelde 611002); tick1494; primary official NBB WVV",
    f"bud_ijez_debt_2025,{ENT},2025,140520313,,,executed,{SRC},strong,2025 schulden 140520313 DROP (was 149978585; LT 129770286 + ST 9082335 + deferred 1667692); tick1494; primary official NBB WVV",
    f"bud_ijez_ltdebt_2025,{ENT},2025,129770286,,,executed,{SRC},strong,2025 LT schulden 129770286 DROP (was 140589269; fin krediet 127800377); tick1494; primary official NBB WVV",
    f"bud_ijez_stdebt_2025,{ENT},2025,9082335,,,executed,{SRC},strong,2025 ST schulden 9082335 (was 7519406; 42 5810227 + leveranciers 1074875); tick1494; primary official NBB WVV",
    f"bud_ijez_lev_2025,{ENT},2025,1074875,,,executed,{SRC},strong,2025 leveranciers 1074875 (was 1251682); tick1494; primary official NBB WVV",
    f"bud_ijez_deferred_2025,{ENT},2025,1667692,,,executed,{SRC},strong,2025 overlopend passief 1667692 (was 1869909); tick1494; primary official NBB WVV",
    f"bud_ijez_omzet_2025,{ENT},2025,17969403,,,executed,{SRC},strong,2025 omzet 70 17969403 DROP (was 19393837; 6.10 split unpublished); tick1494; primary official NBB WVV",
    f"bud_ijez_diensten_2025,{ENT},2025,5683226,,,executed,{SRC},strong,2025 diensten 61 5683226 (was 5259072); tick1494; primary official NBB WVV",
    f"bud_ijez_pers_2025,{ENT},2025,2550095,,,executed,{SRC},strong,2025 pers 62 2550095; 30.6 VTE vs 30.5; 48495 uur; YE 32; tick1494; primary official NBB WVV",
    f"bud_ijez_afschr_2025,{ENT},2025,4950809,,,executed,{SRC},strong,2025 afschrijvingen 4950809; tick1494; primary official NBB WVV",
    f"bud_ijez_expl_2025,{ENT},2025,2312113,,,executed,{SRC},strong,2025 bedrijfswinst 9901 2312113 DROP (was 2436582); tick1494; primary official NBB WVV",
    f"bud_ijez_finopbr_2025,{ENT},2025,2511660,,,executed,{SRC},strong,2025 financiele opbrengsten 2511660 (interestsubs 1758826); tick1494; primary official NBB WVV",
    f"bud_ijez_finkost_2025,{ENT},2025,2955355,,,executed,{SRC},strong,2025 financiele kosten 2955355; tick1494; primary official NBB WVV",
    f"bud_ijez_pnl_2025,{ENT},2025,1773977,,,executed,{SRC},strong,2025 PnL 9904 1773977 (was 1734748); tick1494; primary official NBB WVV",
    f"bud_ijez_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0; tick1494; primary official NBB WVV",
    f"bud_ijez_capex_2025,{ENT},2025,15386690,,,executed,{SRC},strong,2025 capex MVA aanschaf 15386690 (terreinen 10139779 meubilair 29600 in aanbouw 5217311); tick1494; primary official NBB WVV",
    f"bud_ijez_in_aanbouw_2025,{ENT},2025,2021643,,,executed,{SRC},strong,2025 activa in aanbouw 2021643 DROP (was 12996628); tick1494; primary official NBB WVV",
    f"bud_ijez_krediet_2025,{ENT},2025,127800377,,,executed,{SRC},strong,2025 LT kredietinstellingen 127800377 DROP (was 138739253); tick1494; primary official NBB WVV",
    f"bud_ijez_terreinen_2025,{ENT},2025,153430074,,,executed,{SRC},strong,2025 terreinen en gebouwen 153430074 (was 152910919); tick1494; primary official NBB WVV",
    f"bud_ijez_commissaris_2025,{ENT},2025,8904,,,executed,{SRC},strong,2025 commissaris fee 8904 Callens Vandelanotte nv; tick1494; primary official NBB WVV 6.16",
    f"bud_ijez_explsubs_2025,{ENT},2025,884446,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 884446 DROP (was 951390); tick1494; primary official NBB WVV",
    f"bud_ijez_bedrijfsopbr_2025,{ENT},2025,19762126,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 19762126 (was 21197133); tick1494; primary official NBB WVV",
    f"bud_ijez_interestsubs_2025,{ENT},2025,1758826,,,executed,{SRC},strong,2025 interestsubsidies 9126 1758826 (was 1751220); tick1494; primary official NBB WVV",
    f"bud_ijez_bestuurders_2025,{ENT},2025,46610,,,executed,{SRC},strong,2025 bestuurders 9503 46610; tick1494; primary official NBB WVV 6.16",
    f"bud_ijez_goederen_2025,{ENT},2025,2659159,,,executed,{SRC},strong,2025 handelsgoederen 60 2659159 DROP (was 4933690); tick1494; primary official NBB WVV",
]
import csv, io
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

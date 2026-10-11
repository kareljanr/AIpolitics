#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_thws"
SRC = "src_thws_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = []
    for r in rows:
        out.append(r.rstrip("\r\n") + "\r\n")
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_thws_assets_2025,{ENT},2025,603044813,,,executed,{SRC},strong,2025 assets 603044813 (was 603409744); tick1493; primary official NBB WVV",
    f"bud_thws_current_2025,{ENT},2025,48302242,,,executed,{SRC},strong,2025 vlottend 48302242 DROP (was 53095296); tick1493; primary official NBB WVV",
    f"bud_thws_cash_2025,{ENT},2025,24569716,,,executed,{SRC},strong,2025 liquide middelen 24569716 UP (was 21998883); tick1493; primary official NBB WVV",
    f"bud_thws_beleg_2025,{ENT},2025,15261099,,,executed,{SRC},strong,2025 geldbeleggingen 15261099 DROP (was 20260008); tick1493; primary official NBB WVV",
    f"bud_thws_strecv_2025,{ENT},2025,2385406,,,executed,{SRC},strong,2025 ST vorderingen 2385406 (was 3041355); tick1493; primary official NBB WVV",
    f"bud_thws_trade_2025,{ENT},2025,956239,,,executed,{SRC},strong,2025 handelsvorderingen 956239 DROP (was 1741142); tick1493; primary official NBB WVV",
    f"bud_thws_othrecv_2025,{ENT},2025,1429167,,,executed,{SRC},strong,2025 overige ST vorderingen 1429167 (was 1300213); tick1493; primary official NBB WVV",
    f"bud_thws_voorr_2025,{ENT},2025,1110614,,,executed,{SRC},strong,2025 voorraden 1110614 (onroerend verkoop 1003897); tick1493; primary official NBB WVV",
    f"bud_thws_prepaid_2025,{ENT},2025,4975407,,,executed,{SRC},strong,2025 overlopend actief 4975407 (was 4757787); tick1493; primary official NBB WVV",
    f"bud_thws_fixed_2025,{ENT},2025,554742571,,,executed,{SRC},strong,2025 vaste activa 554742571 UP (was 550314448); tick1493; primary official NBB WVV",
    f"bud_thws_iva_2025,{ENT},2025,6658,,,executed,{SRC},strong,2025 IVA 6658 (was 10663); tick1493; primary official NBB WVV",
    f"bud_thws_mva_2025,{ENT},2025,553383547,,,executed,{SRC},strong,2025 MVA 553383547 UP (was 549222485; terreinen/gebouwen 529411224); tick1493; primary official NBB WVV",
    f"bud_thws_fva_2025,{ENT},2025,1352366,,,executed,{SRC},strong,2025 FVA 1352366 (andere FVA aandelen 1349735 + borg 2631); tick1493; primary official NBB WVV",
    f"bud_thws_equity_2025,{ENT},2025,148379349,,,executed,{SRC},strong,2025 eigen vermogen 148379349 DROP (was 149363103); tick1493; primary official NBB WVV",
    f"bud_thws_inbreng_2025,{ENT},2025,53517,,,executed,{SRC},strong,2025 inbreng 53517 onbeschikbaar; tick1493; primary official NBB WVV",
    f"bud_thws_reserves_2025,{ENT},2025,121213284,,,executed,{SRC},strong,2025 reserves 121213284 (was 123093034); tick1493; primary official NBB WVV",
    f"bud_thws_kapsubs_2025,{ENT},2025,27112548,,,executed,{SRC},strong,2025 kapitaalsubsidies 27112548 (was 26216552); tick1493; primary official NBB WVV",
    f"bud_thws_voorz_2025,{ENT},2025,4665713,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 4665713 (herstel 1547790; uitgestelde 3117923); tick1493; primary official NBB WVV",
    f"bud_thws_debt_2025,{ENT},2025,449999751,,,executed,{SRC},strong,2025 schulden 449999751 (LT 417423265 + ST 29374197 + deferred 3202289); tick1493; primary official NBB WVV",
    f"bud_thws_ltdebt_2025,{ENT},2025,417423265,,,executed,{SRC},strong,2025 LT schulden 417423265 (was 418571694; fin krediet 408746068); tick1493; primary official NBB WVV",
    f"bud_thws_stdebt_2025,{ENT},2025,29374197,,,executed,{SRC},strong,2025 ST schulden 29374197 (42 18594786 + leveranciers 6352871); tick1493; primary official NBB WVV",
    f"bud_thws_lev_2025,{ENT},2025,6352871,,,executed,{SRC},strong,2025 leveranciers 6352871 (was 4625093); tick1493; primary official NBB WVV",
    f"bud_thws_deferred_2025,{ENT},2025,3202289,,,executed,{SRC},strong,2025 overlopend passief 3202289 (was 3201649); tick1493; primary official NBB WVV",
    f"bud_thws_omzet_2025,{ENT},2025,40776434,,,executed,{SRC},strong,2025 omzet 70 40776434 UP (was 36565841; 6.10 split unpublished); tick1493; primary official NBB WVV",
    f"bud_thws_diensten_2025,{ENT},2025,18193236,,,executed,{SRC},strong,2025 diensten 61 18193236 (was 16020600); tick1493; primary official NBB WVV",
    f"bud_thws_pers_2025,{ENT},2025,7596389,,,executed,{SRC},strong,2025 pers 62 7596389; 90.9 VTE vs 88.8; 134626 uur; YE 98; tick1493; primary official NBB WVV",
    f"bud_thws_afschr_2025,{ENT},2025,14400825,,,executed,{SRC},strong,2025 afschrijvingen 14400825; tick1493; primary official NBB WVV",
    f"bud_thws_expl_2025,{ENT},2025,-2007531,,,executed,{SRC},strong,2025 bedrijfswinst 9901 -2007531 DROP (was 36300); tick1493; primary official NBB WVV",
    f"bud_thws_finopbr_2025,{ENT},2025,8707910,,,executed,{SRC},strong,2025 financiele opbrengsten 8707910 (interestsubs 7529472); tick1493; primary official NBB WVV",
    f"bud_thws_finkost_2025,{ENT},2025,8643727,,,executed,{SRC},strong,2025 financiele kosten 8643727; tick1493; primary official NBB WVV",
    f"bud_thws_pnl_2025,{ENT},2025,-1879750,,,executed,{SRC},strong,2025 PnL 9904 -1879750 DROP (was 222838); tick1493; primary official NBB WVV",
    f"bud_thws_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0; tick1493; primary official NBB WVV",
    f"bud_thws_capex_2025,{ENT},2025,19362596,,,executed,{SRC},strong,2025 capex MVA aanschaf 19362596 (terreinen 1626448 install 34161 meubilair 35826 in aanbouw 17666161); tick1493; primary official NBB WVV",
    f"bud_thws_in_aanbouw_2025,{ENT},2025,22115489,,,executed,{SRC},strong,2025 activa in aanbouw 22115489 (was 22992435); tick1493; primary official NBB WVV",
    f"bud_thws_krediet_2025,{ENT},2025,408746068,,,executed,{SRC},strong,2025 LT kredietinstellingen 408746068 (was 412304305); tick1493; primary official NBB WVV",
    f"bud_thws_terreinen_2025,{ENT},2025,529411224,,,executed,{SRC},strong,2025 terreinen en gebouwen 529411224 (was 524188156); tick1493; primary official NBB WVV",
    f"bud_thws_commissaris_2025,{ENT},2025,19488,,,executed,{SRC},strong,2025 commissaris fee 19488 Callens Vandelanotte nv; tick1493; primary official NBB WVV 6.16",
    f"bud_thws_commissaris_extra_2025,{ENT},2025,11638,,,executed,{SRC},strong,2025 commissaris extra verbonden 95083 11638; tick1493; primary official NBB WVV 6.16",
    f"bud_thws_explsubs_2025,{ENT},2025,2180609,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 2180609 DROP (was 4367356); tick1493; primary official NBB WVV",
    f"bud_thws_bedrijfsopbr_2025,{ENT},2025,44418454,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 44418454 (was 42544427); tick1493; primary official NBB WVV",
    f"bud_thws_interestsubs_2025,{ENT},2025,7529472,,,executed,{SRC},strong,2025 interestsubsidies 9126 7529472 (was 6886665); tick1493; primary official NBB WVV",
    f"bud_thws_bestuurders_2025,{ENT},2025,43662,,,executed,{SRC},strong,2025 bestuurders 9503 43662; tick1493; primary official NBB WVV 6.16",
]
# verify no extra commas breaking field count
import csv, io
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

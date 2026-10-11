#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_stk9"
SRC = "src_stk9_jr2025_nbb"
BUDGETS = [
    ("bud_stk9_assets_2025", "2025", "228254549", "2025 assets 228254549 DROP (was 230434855); tick1482; primary official NBB WVV VOL-inb 2026-00288124"),
    ("bud_stk9_current_2025", "2025", "32937166", "2025 vlottend 32937166 (was 38355874); tick1482; primary official NBB WVV"),
    ("bud_stk9_cash_2025", "2025", "18887511", "2025 liquide middelen 18887511 DROP (was 25075051); tick1482; primary official NBB WVV"),
    ("bud_stk9_strecv_2025", "2025", "2319166", "2025 ST vorderingen 2319166 (was 2327893); tick1482; primary official NBB WVV"),
    ("bud_stk9_trade_2025", "2025", "887443", "2025 handelsvorderingen 887443 (was 1058675); tick1482; primary official NBB WVV"),
    ("bud_stk9_othrecv_2025", "2025", "1431723", "2025 overige ST vorderingen 1431723 (was 1269218); tick1482; primary official NBB WVV"),
    ("bud_stk9_voorraden_2025", "2025", "9813656", "2025 voorraden 9813656 (was 9062544; onroerend verkoop 9810526); tick1482; primary official NBB WVV"),
    ("bud_stk9_prepaid_2025", "2025", "1916387", "2025 overlopend actief 1916387 (was 1889939); tick1482; primary official NBB WVV"),
    ("bud_stk9_fixed_2025", "2025", "195317383", "2025 vaste activa 195317383 (was 192078981); tick1482; primary official NBB WVV"),
    ("bud_stk9_iva_2025", "2025", "47663", "2025 IVA 47663 (was 98757); tick1482; primary official NBB WVV"),
    ("bud_stk9_mva_2025", "2025", "195266378", "2025 MVA 195266378 (was 191976882; terreinen/gebouwen 170878345 installaties 47272 meubilair 115172 overige 1159449 in aanbouw 23066141); tick1482; primary official NBB WVV"),
    ("bud_stk9_fva_2025", "2025", "3341", "2025 FVA 3341 (was 3341); tick1482; primary official NBB WVV"),
    ("bud_stk9_equity_2025", "2025", "58118603", "2025 eigen vermogen 58118603 DROP (was 58766021); tick1482; primary official NBB WVV"),
    ("bud_stk9_inbreng_2025", "2025", "40216621", "2025 inbreng 40216621 onbeschikbaar; tick1482; primary official NBB WVV"),
    ("bud_stk9_reserves_2025", "2025", "6904163", "2025 reserves 6904163 (was 6904163); tick1482; primary official NBB WVV"),
    ("bud_stk9_kapsubs_2025", "2025", "14747379", "2025 kapitaalsubsidies 14747379 UP (was 13848429); tick1482; primary official NBB WVV"),
    ("bud_stk9_voorz_2025", "2025", "1347033", "2025 voorzieningen+uitgestelde belasting 1347033 (herstel 302056); tick1482; primary official NBB WVV"),
    ("bud_stk9_debt_2025", "2025", "168788912", "2025 schulden 168788912 DROP (was 169559780); tick1482; primary official NBB WVV"),
    ("bud_stk9_ltdebt_2025", "2025", "155332770", "2025 LT schulden 155332770 (was 157005966; fin krediet 153334678); tick1482; primary official NBB WVV"),
    ("bud_stk9_stdebt_2025", "2025", "11903523", "2025 ST schulden 11903523 (42 6530745 + leveranciers 2966310); tick1482; primary official NBB WVV"),
    ("bud_stk9_lev_2025", "2025", "2966310", "2025 leveranciers 2966310 (was 1919164); tick1482; primary official NBB WVV"),
    ("bud_stk9_bezold_2025", "2025", "506614", "2025 bezoldigingen-schulden 506614 (was 508731); tick1482; primary official NBB WVV"),
    ("bud_stk9_taxpay_2025", "2025", "999539", "2025 belastingschulden 999539 (was 1281862); tick1482; primary official NBB WVV"),
    ("bud_stk9_deferred_2025", "2025", "1552619", "2025 overlopend passief 1552619 (was 1655009); tick1482; primary official NBB WVV"),
    ("bud_stk9_omzet_2025", "2025", "14564880", "2025 omzet 70 14564880 DROP (was 14586153; 6.10 split unpublished); tick1482; primary official NBB WVV"),
    ("bud_stk9_diensten_2025", "2025", "6016120", "2025 diensten 61 6016120 DROP (was 6973553); tick1482; primary official NBB WVV"),
    ("bud_stk9_pers_2025", "2025", "5207321", "2025 pers 62 5207321; 48.5 VTE vs 48.1; 73605 uur; YE 53 / 48.5 VTE; tick1482; primary official NBB WVV"),
    ("bud_stk9_afschr_2025", "2025", "5616518", "2025 afschrijvingen 5616518; tick1482; primary official NBB WVV"),
    ("bud_stk9_expl_2025", "2025", "-1723012", "2025 bedrijfsverlies 1723012 (was 1576837); tick1482; primary official NBB WVV"),
    ("bud_stk9_finopbr_2025", "2025", "3849245", "2025 financiele opbrengsten 3849245 (interestsubs 2847642); tick1482; primary official NBB WVV"),
    ("bud_stk9_finkost_2025", "2025", "3711094", "2025 financiele kosten 3711094; tick1482; primary official NBB WVV"),
    ("bud_stk9_pnl_2025", "2025", "-1546368", "2025 PnL -1546368 LOSS (was -1223605); tick1482; primary official NBB WVV"),
    ("bud_stk9_div_2025", "2025", "0", "2025 dividend 0; tick1482; primary official NBB WVV"),
    ("bud_stk9_capex_2025", "2025", "9157319", "2025 capex MVA aanschaf 9157319 (terreinen 310456 installaties 1876 meubilair 14148 in aanbouw 8830839); tick1482; primary official NBB WVV"),
    ("bud_stk9_in_aanbouw_2025", "2025", "23066141", "2025 activa in aanbouw 23066141 JUMP (was 16152248); tick1482; primary official NBB WVV"),
    ("bud_stk9_krediet_2025", "2025", "153334678", "2025 LT kredietinstellingen 153334678 (was 155057617); tick1482; primary official NBB WVV"),
    ("bud_stk9_terreinen_2025", "2025", "170878345", "2025 terreinen en gebouwen 170878345 (was 174447047); tick1482; primary official NBB WVV"),
    ("bud_stk9_commissaris_2025", "2025", "7000", "2025 commissaris fee 7000 Verifin BV; tick1482; primary official NBB WVV"),
    ("bud_stk9_tax_2025", "2025", "400", "2025 belastingen op het resultaat 400; tick1482; primary official NBB WVV"),
    ("bud_stk9_interestsubs_2025", "2025", "2847642", "2025 interestsubsidies 2847642 (was 2519792); tick1482; primary official NBB WVV 6.11"),
    ("bud_stk9_explsubs_2025", "2025", "798626", "2025 exploitatiesubsidies 798626 (was 912699); tick1482; primary official NBB WVV 6.10"),
    ("bud_stk9_geldbeleg_2025", "2025", "446", "2025 geldbeleggingen 446 (was 446); tick1482; primary official NBB WVV"),
    ("bud_stk9_bestuurders_2025", "2025", "61077", "2025 bestuurders 9503 61077; tick1482; primary official NBB WVV 6.16"),
]
bp = DATA / "budgets.csv"
braw = bp.read_bytes()
if braw and not braw.endswith(b"\n"):
    braw += b"\n"
existing = set()
for brow in csv.reader(io.StringIO(braw.decode("utf-8"))):
    if brow:
        existing.add(brow[0])
added = []
for bid, year, amt, notes in BUDGETS:
    if bid in existing:
        continue
    added.append(f"{bid},{ENT},{year},{amt},,,executed,{SRC},strong,{notes}\n")
bp.write_bytes(braw + "".join(added).encode("utf-8"))
print("budgets", len(added))

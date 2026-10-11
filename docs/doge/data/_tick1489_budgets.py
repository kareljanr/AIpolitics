#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_ivlv"
SRC = "src_ivlv_jr2025_nbb"
BUDGETS = [
    ("bud_ivlv_assets_2025", "2025", "175606699", "2025 assets 175606699 UP (was 165009232); tick1489; primary official NBB WVV VOL-inb 2026-00138038"),
    ("bud_ivlv_current_2025", "2025", "25434259", "2025 vlottend 25434259 UP (was 22083195); tick1489; primary official NBB WVV"),
    ("bud_ivlv_cash_2025", "2025", "22766208", "2025 liquide middelen 22766208 JUMP (was 20393831); tick1489; primary official NBB WVV"),
    ("bud_ivlv_strecv_2025", "2025", "2084851", "2025 ST vorderingen 2084851 (was 1299150); tick1489; primary official NBB WVV"),
    ("bud_ivlv_trade_2025", "2025", "732643", "2025 handelsvorderingen 732643 (was 631169); tick1489; primary official NBB WVV"),
    ("bud_ivlv_othrecv_2025", "2025", "1352208", "2025 overige ST vorderingen 1352208 JUMP (was 667982); tick1489; primary official NBB WVV"),
    ("bud_ivlv_ltrecv_2025", "2025", "46186", "2025 LT vorderingen 46186 (was 41179); tick1489; primary official NBB WVV"),
    ("bud_ivlv_prepaid_2025", "2025", "537014", "2025 overlopend actief 537014 (was 349035); tick1489; primary official NBB WVV"),
    ("bud_ivlv_fixed_2025", "2025", "150172440", "2025 vaste activa 150172440 UP (was 142926036); tick1489; primary official NBB WVV"),
    ("bud_ivlv_iva_2025", "2025", "0", "2025 IVA 21 empty; tick1489; primary official NBB WVV"),
    ("bud_ivlv_mva_2025", "2025", "150096603", "2025 MVA 150096603 UP (was 142858766; terreinen/gebouwen 118971850 installaties 0 meubilair 45211 in aanbouw 31079542); tick1489; primary official NBB WVV"),
    ("bud_ivlv_fva_2025", "2025", "75837", "2025 FVA 75837 (was 67270; andere FVA aandelen 75014 + borg 824); tick1489; primary official NBB WVV"),
    ("bud_ivlv_equity_2025", "2025", "38667098", "2025 eigen vermogen 38667098 (was 35345780); tick1489; primary official NBB WVV"),
    ("bud_ivlv_inbreng_2025", "2025", "64501", "2025 inbreng 64501 onbeschikbaar; tick1489; primary official NBB WVV"),
    ("bud_ivlv_reserves_2025", "2025", "26391242", "2025 reserves 26391242 (was 25429779); tick1489; primary official NBB WVV"),
    ("bud_ivlv_kapsubs_2025", "2025", "7444086", "2025 kapitaalsubsidies 7444086 JUMP (was 5084231); tick1489; primary official NBB WVV"),
    ("bud_ivlv_voorz_2025", "2025", "1058086", "2025 voorzieningen+uitgestelde belasting 1058086 (herstel 358985; uitgestelde 699101); tick1489; primary official NBB WVV"),
    ("bud_ivlv_debt_2025", "2025", "135881516", "2025 schulden 135881516 (was 128714570); tick1489; primary official NBB WVV"),
    ("bud_ivlv_ltdebt_2025", "2025", "126750875", "2025 LT schulden 126750875 (was 120707340; fin krediet 125161194); tick1489; primary official NBB WVV"),
    ("bud_ivlv_stdebt_2025", "2025", "8704707", "2025 ST schulden 8704707 (42 4347291 + leveranciers 2615993); tick1489; primary official NBB WVV"),
    ("bud_ivlv_lev_2025", "2025", "2615993", "2025 leveranciers 2615993 (was 2077455); tick1489; primary official NBB WVV"),
    ("bud_ivlv_deferred_2025", "2025", "425934", "2025 overlopend passief 425934 (was 338239); tick1489; primary official NBB WVV"),
    ("bud_ivlv_omzet_2025", "2025", "9370627", "2025 omzet 70 9370627 (was 9368788; 6.10 sociale verhuur 9173233 / doorverhuur 197393); tick1489; primary official NBB WVV"),
    ("bud_ivlv_diensten_2025", "2025", "3298243", "2025 diensten 61 3298243 (was 3309716); tick1489; primary official NBB WVV"),
    ("bud_ivlv_pers_2025", "2025", "1996874", "2025 pers 62 1996874; 20.8 VTE vs 20.7; 31945 uur; YE 21; tick1489; primary official NBB WVV"),
    ("bud_ivlv_afschr_2025", "2025", "4067712", "2025 afschrijvingen 4067712; tick1489; primary official NBB WVV"),
    ("bud_ivlv_expl_2025", "2025", "1376742", "2025 bedrijfswinst 1376742 DROP (was 2243674); tick1489; primary official NBB WVV"),
    ("bud_ivlv_finopbr_2025", "2025", "2060840", "2025 financiele opbrengsten 2060840 (interestsubs 1619049); tick1489; primary official NBB WVV"),
    ("bud_ivlv_finkost_2025", "2025", "2443860", "2025 financiele kosten 2443860; tick1489; primary official NBB WVV"),
    ("bud_ivlv_pnl_2025", "2025", "961462", "2025 PnL 961462 DROP (was 1690890); tick1489; primary official NBB WVV"),
    ("bud_ivlv_div_2025", "2025", "0", "2025 dividend 0; tick1489; primary official NBB WVV"),
    ("bud_ivlv_capex_2025", "2025", "12018842", "2025 capex MVA aanschaf 12018842 (terreinen 278387 meubilair 16097 in aanbouw 11724358); tick1489; primary official NBB WVV"),
    ("bud_ivlv_in_aanbouw_2025", "2025", "31079542", "2025 activa in aanbouw 31079542 (was 26865637); tick1489; primary official NBB WVV"),
    ("bud_ivlv_krediet_2025", "2025", "125161194", "2025 LT kredietinstellingen 125161194 (was 119044331); tick1489; primary official NBB WVV"),
    ("bud_ivlv_terreinen_2025", "2025", "118971850", "2025 terreinen en gebouwen 118971850 (was 115928427); tick1489; primary official NBB WVV"),
    ("bud_ivlv_commissaris_2025", "2025", "11616", "2025 commissaris fee 11616 Luc Callaert BV BTW incl; tick1489; primary official NBB WVV"),
    ("bud_ivlv_tax_2025", "2025", "55055", "2025 belastingen op het resultaat 55055; tick1489; primary official NBB WVV"),
    ("bud_ivlv_interestsubs_2025", "2025", "1619049", "2025 interestsubsidies 9126 1619049 (was 1475942); tick1489; primary official NBB WVV 6.11"),
    ("bud_ivlv_explsubs_2025", "2025", "123634", "2025 exploitatiesubsidies 740 123634 (was 78601); tick1489; primary official NBB WVV 6.10"),
    ("bud_ivlv_verhuur_2025", "2025", "9173233", "2025 6.10 sociale verhuur 9173233 (was 9168556); tick1489; primary official NBB WVV"),
    ("bud_ivlv_doorverhuur_2025", "2025", "197393", "2025 6.10 sociale doorverhuur 197393 (was 200233); tick1489; primary official NBB WVV"),
    ("bud_ivlv_kapsubs_amort_2025", "2025", "166893", "2025 kapitaalsubsidies 9125 166893 (was 127089); tick1489; primary official NBB WVV 6.11"),
    ("bud_ivlv_bestuurders_2025", "2025", "13800", "2025 bestuurders 9503 13800; tick1489; primary official NBB WVV 6.16"),
    ("bud_ivlv_herwaard_2025", "2025", "4767269", "2025 herwaarderingsmeerwaarden 4767269; tick1489; primary official NBB WVV"),
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

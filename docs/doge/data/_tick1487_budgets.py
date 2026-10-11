#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_dvpk"
SRC = "src_dvpk_jr2025_nbb"
BUDGETS = [
    ("bud_dvpk_assets_2025", "2025", "352377695", "2025 assets 352377695 UP (was 339616219); tick1487; primary official NBB WVV VOL-inb 2026-00192551"),
    ("bud_dvpk_current_2025", "2025", "22856768", "2025 vlottend 22856768 DROP (was 25535968); tick1487; primary official NBB WVV"),
    ("bud_dvpk_cash_2025", "2025", "5091590", "2025 liquide middelen 5091590 JUMP (was 4853096); tick1487; primary official NBB WVV"),
    ("bud_dvpk_strecv_2025", "2025", "1499542", "2025 ST vorderingen 1499542 DROP (was 3922768); tick1487; primary official NBB WVV"),
    ("bud_dvpk_trade_2025", "2025", "805904", "2025 handelsvorderingen 805904 DROP (was 1090547); tick1487; primary official NBB WVV"),
    ("bud_dvpk_othrecv_2025", "2025", "693639", "2025 overige ST vorderingen 693639 DROP (was 2832221); tick1487; primary official NBB WVV"),
    ("bud_dvpk_ltrecv_2025", "2025", "9515625", "2025 LT vorderingen 9515625 DROP (was 9843750); tick1487; primary official NBB WVV"),
    ("bud_dvpk_voorraden_2025", "2025", "2723969", "2025 voorraden 2723969 DROP (was 2889011; onroerend verkoop); tick1487; primary official NBB WVV"),
    ("bud_dvpk_prepaid_2025", "2025", "4026041", "2025 overlopend actief 4026041 (was 3330926); tick1487; primary official NBB WVV"),
    ("bud_dvpk_fixed_2025", "2025", "329520927", "2025 vaste activa 329520927 (was 314080251); tick1487; primary official NBB WVV"),
    ("bud_dvpk_iva_2025", "2025", "7521", "2025 IVA 7521 (was 3498); tick1487; primary official NBB WVV"),
    ("bud_dvpk_mva_2025", "2025", "329147246", "2025 MVA 329147246 (was 313724991; terreinen/gebouwen 316306764 installaties 59661 meubilair 132842 overige 16992 in aanbouw 12630986); tick1487; primary official NBB WVV"),
    ("bud_dvpk_fva_2025", "2025", "366161", "2025 FVA 366161 (was 351763); tick1487; primary official NBB WVV"),
    ("bud_dvpk_equity_2025", "2025", "42644547", "2025 eigen vermogen 42644547 (was 42281134); tick1487; primary official NBB WVV"),
    ("bud_dvpk_inbreng_2025", "2025", "74286", "2025 inbreng 74286 onbeschikbaar; tick1487; primary official NBB WVV"),
    ("bud_dvpk_reserves_2025", "2025", "28748266", "2025 reserves 28748266 (was 28743600); tick1487; primary official NBB WVV"),
    ("bud_dvpk_kapsubs_2025", "2025", "13821995", "2025 kapitaalsubsidies 13821995 (was 13463248); tick1487; primary official NBB WVV"),
    ("bud_dvpk_voorz_2025", "2025", "2747627", "2025 voorzieningen+uitgestelde belasting 2747627 (pensioen 103683; overige 1593039; uitgestelde 1050905); tick1487; primary official NBB WVV"),
    ("bud_dvpk_debt_2025", "2025", "306985521", "2025 schulden 306985521 JUMP (was 294597444); tick1487; primary official NBB WVV"),
    ("bud_dvpk_ltdebt_2025", "2025", "284245982", "2025 LT schulden 284245982 (was 274287399; fin krediet 281475127); tick1487; primary official NBB WVV"),
    ("bud_dvpk_stdebt_2025", "2025", "19331652", "2025 ST schulden 19331652 (42 15273881 + leveranciers 603508); tick1487; primary official NBB WVV"),
    ("bud_dvpk_lev_2025", "2025", "603508", "2025 leveranciers 603508 DROP (was 1957801); tick1487; primary official NBB WVV"),
    ("bud_dvpk_deferred_2025", "2025", "3407887", "2025 overlopend passief 3407887 (was 2385806); tick1487; primary official NBB WVV"),
    ("bud_dvpk_omzet_2025", "2025", "19566170", "2025 omzet 70 19566170 DROP (was 20993841; 6.10 verhuur 19375576 / koop 190594); tick1487; primary official NBB WVV"),
    ("bud_dvpk_diensten_2025", "2025", "8811074", "2025 diensten 61 8811074 JUMP (was 8713442); tick1487; primary official NBB WVV"),
    ("bud_dvpk_pers_2025", "2025", "4716427", "2025 pers 62 4716427; 58.5 VTE vs 51.7; 86467 uur; YE 63; tick1487; primary official NBB WVV"),
    ("bud_dvpk_afschr_2025", "2025", "7941136", "2025 afschrijvingen 7941136; tick1487; primary official NBB WVV"),
    ("bud_dvpk_expl_2025", "2025", "796139", "2025 bedrijfswinst 796139 (was -294938); tick1487; primary official NBB WVV"),
    ("bud_dvpk_finopbr_2025", "2025", "6277437", "2025 financiele opbrengsten 6277437 (interestsubs 5713245); tick1487; primary official NBB WVV"),
    ("bud_dvpk_finkost_2025", "2025", "7069932", "2025 financiele kosten 7069932; tick1487; primary official NBB WVV"),
    ("bud_dvpk_pnl_2025", "2025", "4666", "2025 PnL 4666 JUMP (was -1266832); tick1487; primary official NBB WVV"),
    ("bud_dvpk_div_2025", "2025", "0", "2025 dividend 0; tick1487; primary official NBB WVV"),
    ("bud_dvpk_capex_2025", "2025", "32271841", "2025 capex MVA aanschaf 32271841 (terreinen 23312975 installaties 12048 meubilair 5676 overige 8844 in aanbouw 8932298); tick1487; primary official NBB WVV"),
    ("bud_dvpk_in_aanbouw_2025", "2025", "12630986", "2025 activa in aanbouw 12630986 DROP (was 15628323); tick1487; primary official NBB WVV"),
    ("bud_dvpk_krediet_2025", "2025", "281475127", "2025 LT kredietinstellingen 281475127 (was 271820855); tick1487; primary official NBB WVV"),
    ("bud_dvpk_terreinen_2025", "2025", "316306764", "2025 terreinen en gebouwen 316306764 (was 297858575); tick1487; primary official NBB WVV"),
    ("bud_dvpk_commissaris_2025", "2025", "15698", "2025 commissaris fee 15698 Compass Audit BV; tick1487; primary official NBB WVV"),
    ("bud_dvpk_tax_2025", "2025", "28417", "2025 belastingen op het resultaat 28417; tick1487; primary official NBB WVV"),
    ("bud_dvpk_interestsubs_2025", "2025", "5713245", "2025 interestsubsidies 9126 5713245 (was 4711628); tick1487; primary official NBB WVV 6.11"),
    ("bud_dvpk_explsubs_2025", "2025", "959043", "2025 exploitatiesubsidies 740 959043 DROP (was 1320035); tick1487; primary official NBB WVV 6.10"),
    ("bud_dvpk_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen 50/53 0 DROP (was 696417); tick1487; primary official NBB WVV"),
    ("bud_dvpk_handelsgoederen_2025", "2025", "178342", "2025 handelsgoederen 60 178342 DROP (was 1921359); tick1487; primary official NBB WVV"),
    ("bud_dvpk_verhuur_2025", "2025", "19375576", "2025 6.10 verhuur 19375576 (was 18835088); tick1487; primary official NBB WVV"),
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

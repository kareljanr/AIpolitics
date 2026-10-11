#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_wsbn"
SRC = "src_wsbn_jr2025_nbb"
BUDGETS = [
    ("bud_wsbn_assets_2025", "2025", "155658879", "2025 assets 155658879 UP (was 154525213); tick1488; primary official NBB WVV VOL-inb 2026-00131692"),
    ("bud_wsbn_current_2025", "2025", "7481966", "2025 vlottend 7481966 JUMP (was 4674713); tick1488; primary official NBB WVV"),
    ("bud_wsbn_cash_2025", "2025", "3462126", "2025 liquide middelen 3462126 JUMP (was 3139025); tick1488; primary official NBB WVV"),
    ("bud_wsbn_strecv_2025", "2025", "456481", "2025 ST vorderingen 456481 (was 336823); tick1488; primary official NBB WVV"),
    ("bud_wsbn_trade_2025", "2025", "390215", "2025 handelsvorderingen 390215 (was 226222); tick1488; primary official NBB WVV"),
    ("bud_wsbn_othrecv_2025", "2025", "66266", "2025 overige ST vorderingen 66266 DROP (was 110601); tick1488; primary official NBB WVV"),
    ("bud_wsbn_voorraden_2025", "2025", "2429386", "2025 voorraden 2429386 JUMP (was 70882; onroerend verkoop 2414485); tick1488; primary official NBB WVV"),
    ("bud_wsbn_prepaid_2025", "2025", "1133931", "2025 overlopend actief 1133931 (was 1127943); tick1488; primary official NBB WVV"),
    ("bud_wsbn_fixed_2025", "2025", "148176913", "2025 vaste activa 148176913 DROP (was 149850499); tick1488; primary official NBB WVV"),
    ("bud_wsbn_iva_2025", "2025", "0", "2025 IVA 21 empty; tick1488; primary official NBB WVV"),
    ("bud_wsbn_mva_2025", "2025", "148173399", "2025 MVA 148173399 DROP (was 149846985; terreinen/gebouwen 147203274 installaties 19641 meubilair 37877 overige 39559 in aanbouw 873048); tick1488; primary official NBB WVV"),
    ("bud_wsbn_fva_2025", "2025", "3514", "2025 FVA 3514 (was 3514; verbonden deelnemingen); tick1488; primary official NBB WVV"),
    ("bud_wsbn_equity_2025", "2025", "19159867", "2025 eigen vermogen 19159867 (was 19064798); tick1488; primary official NBB WVV"),
    ("bud_wsbn_inbreng_2025", "2025", "21581", "2025 inbreng 21581 onbeschikbaar; tick1488; primary official NBB WVV"),
    ("bud_wsbn_reserves_2025", "2025", "12064945", "2025 reserves 12064945 (was 11716733); tick1488; primary official NBB WVV"),
    ("bud_wsbn_kapsubs_2025", "2025", "7073342", "2025 kapitaalsubsidies 7073342 DROP (was 7326360); tick1488; primary official NBB WVV"),
    ("bud_wsbn_voorz_2025", "2025", "433820", "2025 voorzieningen+uitgestelde belasting 433820 (herstel 40000; milieu 11413; uitgestelde 382407); tick1488; primary official NBB WVV"),
    ("bud_wsbn_debt_2025", "2025", "136065192", "2025 schulden 136065192 (was 135064350); tick1488; primary official NBB WVV"),
    ("bud_wsbn_ltdebt_2025", "2025", "125074991", "2025 LT schulden 125074991 DROP (was 127226257; fin krediet 123184025); tick1488; primary official NBB WVV"),
    ("bud_wsbn_stdebt_2025", "2025", "10269524", "2025 ST schulden 10269524 (42 7201428 + leveranciers 2142862); tick1488; primary official NBB WVV"),
    ("bud_wsbn_lev_2025", "2025", "2142862", "2025 leveranciers 2142862 JUMP (was 1133117); tick1488; primary official NBB WVV"),
    ("bud_wsbn_deferred_2025", "2025", "720677", "2025 overlopend passief 720677 DROP (was 921068); tick1488; primary official NBB WVV"),
    ("bud_wsbn_omzet_2025", "2025", "10995862", "2025 omzet 70 10995862 JUMP (was 9176950; 6.10 huur 10290178 / andere 705690); tick1488; primary official NBB WVV"),
    ("bud_wsbn_diensten_2025", "2025", "4799320", "2025 diensten 61 4799320 JUMP (was 3348423); tick1488; primary official NBB WVV"),
    ("bud_wsbn_pers_2025", "2025", "1957328", "2025 pers 62 1957328; 21.7 VTE vs 17.7; 34664 uur; YE 24; tick1488; primary official NBB WVV"),
    ("bud_wsbn_afschr_2025", "2025", "4109976", "2025 afschrijvingen 4109976; tick1488; primary official NBB WVV"),
    ("bud_wsbn_expl_2025", "2025", "299658", "2025 bedrijfswinst 299658 DROP (was 450884); tick1488; primary official NBB WVV"),
    ("bud_wsbn_finopbr_2025", "2025", "2754303", "2025 financiele opbrengsten 2754303 (interestsubs 2473246); tick1488; primary official NBB WVV"),
    ("bud_wsbn_finkost_2025", "2025", "2702981", "2025 financiele kosten 2702981; tick1488; primary official NBB WVV"),
    ("bud_wsbn_pnl_2025", "2025", "348212", "2025 PnL 348212 DROP (was 425988); tick1488; primary official NBB WVV"),
    ("bud_wsbn_div_2025", "2025", "0", "2025 dividend 0; tick1488; primary official NBB WVV"),
    ("bud_wsbn_capex_2025", "2025", "13398259", "2025 capex MVA aanschaf 13398259 (terreinen 13150461 meubilair 23737 in aanbouw 224061); tick1488; primary official NBB WVV"),
    ("bud_wsbn_in_aanbouw_2025", "2025", "873048", "2025 activa in aanbouw 873048 DROP (was 11307352); tick1488; primary official NBB WVV"),
    ("bud_wsbn_krediet_2025", "2025", "123184025", "2025 LT kredietinstellingen 123184025 DROP (was 125816129); tick1488; primary official NBB WVV"),
    ("bud_wsbn_terreinen_2025", "2025", "147203274", "2025 terreinen en gebouwen 147203274 (was 138444393); tick1488; primary official NBB WVV"),
    ("bud_wsbn_commissaris_2025", "2025", "8000", "2025 commissaris fee 8000 Compass Audit BV; tick1488; primary official NBB WVV"),
    ("bud_wsbn_tax_2025", "2025", "16426", "2025 belastingen op het resultaat 16426; tick1488; primary official NBB WVV"),
    ("bud_wsbn_interestsubs_2025", "2025", "2473246", "2025 interestsubsidies 9126 2473246 (was 2250382); tick1488; primary official NBB WVV 6.11"),
    ("bud_wsbn_explsubs_2025", "2025", "619219", "2025 exploitatiesubsidies 740 619219 DROP (was 695048); tick1488; primary official NBB WVV 6.10"),
    ("bud_wsbn_geldbeleg_2025", "2025", "41", "2025 geldbeleggingen 50/53 41 (was 41); tick1488; primary official NBB WVV"),
    ("bud_wsbn_handelsgoederen_2025", "2025", "18456", "2025 handelsgoederen 60 18456 (was 16714); tick1488; primary official NBB WVV"),
    ("bud_wsbn_verhuur_2025", "2025", "10290178", "2025 6.10 huuropbrengsten 10290178 (was 8614389); tick1488; primary official NBB WVV"),
    ("bud_wsbn_kapsubs_amort_2025", "2025", "253019", "2025 kapitaalsubsidies 9125 253019 (was 256347); tick1488; primary official NBB WVV 6.11"),
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

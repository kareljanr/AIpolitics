#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_wlim"
SRC = "src_wlim_jr2025_nbb"
BUDGETS = [
    ("bud_wlim_assets_2025", "2025", "2060381293", "2025 assets 2060381293 UP (was 2009660060); tick1486; primary official NBB WVV VOL-inb 2026-00206025"),
    ("bud_wlim_current_2025", "2025", "292335286", "2025 vlottend 292335286 DROP (was 296001848); tick1486; primary official NBB WVV"),
    ("bud_wlim_cash_2025", "2025", "96287038", "2025 liquide middelen 96287038 DROP (was 156033570); tick1486; primary official NBB WVV"),
    ("bud_wlim_strecv_2025", "2025", "10284873", "2025 ST vorderingen 10284873 (was 9808453); tick1486; primary official NBB WVV"),
    ("bud_wlim_trade_2025", "2025", "5094119", "2025 handelsvorderingen 5094119 (was 3498433); tick1486; primary official NBB WVV"),
    ("bud_wlim_othrecv_2025", "2025", "5190754", "2025 overige ST vorderingen 5190754 (was 6310020); tick1486; primary official NBB WVV"),
    ("bud_wlim_voorraden_2025", "2025", "82007845", "2025 voorraden 82007845 JUMP (was 67270536; onroerend verkoop 80513951); tick1486; primary official NBB WVV"),
    ("bud_wlim_prepaid_2025", "2025", "15107935", "2025 overlopend actief 15107935 (was 14251642); tick1486; primary official NBB WVV"),
    ("bud_wlim_fixed_2025", "2025", "1768046007", "2025 vaste activa 1768046007 (was 1713658212); tick1486; primary official NBB WVV"),
    ("bud_wlim_iva_2025", "2025", "2235435", "2025 IVA 2235435 (was 1060132); tick1486; primary official NBB WVV"),
    ("bud_wlim_mva_2025", "2025", "1762607646", "2025 MVA 1762607646 (was 1710067826; terreinen/gebouwen 1660204680 installaties 378178 meubilair 1815135 leasing 2022355 overige 1672420 in aanbouw 96514878); tick1486; primary official NBB WVV"),
    ("bud_wlim_fva_2025", "2025", "3202926", "2025 FVA 3202926 (was 2530254); tick1486; primary official NBB WVV"),
    ("bud_wlim_equity_2025", "2025", "591815458", "2025 eigen vermogen 591815458 (was 579831494); tick1486; primary official NBB WVV"),
    ("bud_wlim_inbreng_2025", "2025", "1373924", "2025 inbreng 1373924 onbeschikbaar; tick1486; primary official NBB WVV"),
    ("bud_wlim_reserves_2025", "2025", "455018195", "2025 reserves 455018195 (was 449310275); tick1486; primary official NBB WVV"),
    ("bud_wlim_kapsubs_2025", "2025", "135423339", "2025 kapitaalsubsidies 135423339 (was 129147295); tick1486; primary official NBB WVV"),
    ("bud_wlim_voorz_2025", "2025", "9295644", "2025 voorzieningen+uitgestelde belasting 9295644 (pensioen 37677; uitgestelde 9257967); tick1486; primary official NBB WVV"),
    ("bud_wlim_debt_2025", "2025", "1459270191", "2025 schulden 1459270191 JUMP (was 1420762323); tick1486; primary official NBB WVV"),
    ("bud_wlim_ltdebt_2025", "2025", "1361408350", "2025 LT schulden 1361408350 (was 1318850916; fin krediet 1340664945); tick1486; primary official NBB WVV"),
    ("bud_wlim_stdebt_2025", "2025", "84196624", "2025 ST schulden 84196624 (42 49668259 + leveranciers 17535213); tick1486; primary official NBB WVV"),
    ("bud_wlim_lev_2025", "2025", "17535213", "2025 leveranciers 17535213 DROP (was 23321943); tick1486; primary official NBB WVV"),
    ("bud_wlim_bezold_2025", "2025", "4015708", "2025 bezoldigingen-schulden 4015708 (was 3787254); tick1486; primary official NBB WVV"),
    ("bud_wlim_taxpay_2025", "2025", "8759341", "2025 belastingschulden 8759341 (was 10857845); tick1486; primary official NBB WVV"),
    ("bud_wlim_deferred_2025", "2025", "13665217", "2025 overlopend passief 13665217 (was 9894650); tick1486; primary official NBB WVV"),
    ("bud_wlim_omzet_2025", "2025", "149755087", "2025 omzet 70 149755087 DROP (was 159522539; 6.10 split unpublished); tick1486; primary official NBB WVV"),
    ("bud_wlim_diensten_2025", "2025", "51702656", "2025 diensten 61 51702656 JUMP (was 50511252); tick1486; primary official NBB WVV"),
    ("bud_wlim_pers_2025", "2025", "32782938", "2025 pers 62 32782938; 397.5 VTE vs 367; 579100 uur; YE 438; tick1486; primary official NBB WVV"),
    ("bud_wlim_afschr_2025", "2025", "53677088", "2025 afschrijvingen 53677088; tick1486; primary official NBB WVV"),
    ("bud_wlim_expl_2025", "2025", "3347875", "2025 bedrijfswinst 3347875 (was 8952384); tick1486; primary official NBB WVV"),
    ("bud_wlim_finopbr_2025", "2025", "33783624", "2025 financiele opbrengsten 33783624 (interestsubs 27151774); tick1486; primary official NBB WVV"),
    ("bud_wlim_finkost_2025", "2025", "31226612", "2025 financiele kosten 31226612; tick1486; primary official NBB WVV"),
    ("bud_wlim_pnl_2025", "2025", "5708426", "2025 PnL 5708426 DROP (was 10494226); tick1486; primary official NBB WVV"),
    ("bud_wlim_div_2025", "2025", "0", "2025 dividend 0; tick1486; primary official NBB WVV"),
    ("bud_wlim_capex_2025", "2025", "106984224", "2025 capex MVA aanschaf 106984224 (terreinen 16873173 installaties 77099 meubilair 687781 overige 46171 in aanbouw 89300000); tick1486; primary official NBB WVV"),
    ("bud_wlim_in_aanbouw_2025", "2025", "96514878", "2025 activa in aanbouw 96514878 JUMP (was 81633379); tick1486; primary official NBB WVV"),
    ("bud_wlim_krediet_2025", "2025", "1340664945", "2025 LT kredietinstellingen 1340664945 (was 1298523649); tick1486; primary official NBB WVV"),
    ("bud_wlim_terreinen_2025", "2025", "1660204680", "2025 terreinen en gebouwen 1660204680 (was 1622400570); tick1486; primary official NBB WVV"),
    ("bud_wlim_commissaris_2025", "2025", "158695", "2025 commissaris fee 158695 BDO Bedrijfsrevisoren BV; tick1486; primary official NBB WVV"),
    ("bud_wlim_tax_2025", "2025", "403886", "2025 belastingen op het resultaat 403886; tick1486; primary official NBB WVV"),
    ("bud_wlim_interestsubs_2025", "2025", "27151774", "2025 interestsubsidies 9126 27151774 (was 23643524); tick1486; primary official NBB WVV 6.11"),
    ("bud_wlim_explsubs_2025", "2025", "7505447", "2025 exploitatiesubsidies 740 7505447 (was 5856866); tick1486; primary official NBB WVV 6.10"),
    ("bud_wlim_geldbeleg_2025", "2025", "88647595", "2025 geldbeleggingen 50/53 88647595 JUMP (was 48637647); tick1486; primary official NBB WVV"),
    ("bud_wlim_bestuurders_2025", "2025", "63607", "2025 bestuurders 9503 63607; tick1486; primary official NBB WVV"),
    ("bud_wlim_handelsgoederen_2025", "2025", "11770677", "2025 handelsgoederen 60 11770677 DROP (was 27607449); tick1486; primary official NBB WVV"),
    ("bud_wlim_interim_2025", "2025", "617406", "2025 interim 617406 / 4.4 VTE / 5 personen; tick1486; primary official NBB WVV 6.10"),
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

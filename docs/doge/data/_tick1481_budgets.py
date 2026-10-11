#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_zkem"
SRC = "src_zkem_jr2025_nbb"
BUDGETS = [
    ("bud_zkem_assets_2025", "2025", "570754360", "2025 assets 570754360 UP (was 551927033); tick1481; primary official NBB WVV VOL-inb 2026-00157303"),
    ("bud_zkem_current_2025", "2025", "56922348", "2025 vlottend 56922348 (was 57674726); tick1481; primary official NBB WVV"),
    ("bud_zkem_cash_2025", "2025", "16924292", "2025 liquide middelen 16924292 JUMP (was 10988951); tick1481; primary official NBB WVV"),
    ("bud_zkem_strecv_2025", "2025", "2641441", "2025 ST vorderingen 2641441 (was 2023825); tick1481; primary official NBB WVV"),
    ("bud_zkem_trade_2025", "2025", "1624716", "2025 handelsvorderingen 1624716 (was 1019638); tick1481; primary official NBB WVV"),
    ("bud_zkem_othrecv_2025", "2025", "1016725", "2025 overige ST vorderingen 1016725 (was 1004187); tick1481; primary official NBB WVV"),
    ("bud_zkem_voorraden_2025", "2025", "31583791", "2025 voorraden 31583791 (was 32299806); tick1481; primary official NBB WVV"),
    ("bud_zkem_prepaid_2025", "2025", "5519774", "2025 overlopend actief 5519774 (was 4702314); tick1481; primary official NBB WVV"),
    ("bud_zkem_fixed_2025", "2025", "513832012", "2025 vaste activa 513832012 (was 494252307); tick1481; primary official NBB WVV"),
    ("bud_zkem_iva_2025", "2025", "3472", "2025 IVA 3472 (was 11873); tick1481; primary official NBB WVV"),
    ("bud_zkem_mva_2025", "2025", "511966023", "2025 MVA 511966023 (was 492763912; terreinen/gebouwen 484330629 installaties 49994 meubilair 180140 overige 5745539 in aanbouw 21659721); tick1481; primary official NBB WVV"),
    ("bud_zkem_fva_2025", "2025", "1862517", "2025 FVA 1862517 (was 1476522); tick1481; primary official NBB WVV"),
    ("bud_zkem_equity_2025", "2025", "92517644", "2025 eigen vermogen 92517644 UP (was 90734575); tick1481; primary official NBB WVV"),
    ("bud_zkem_inbreng_2025", "2025", "502837", "2025 inbreng 502837 (onbeschikbaar 380434); tick1481; primary official NBB WVV"),
    ("bud_zkem_reserves_2025", "2025", "59555133", "2025 reserves 59555133 (was 59138014); tick1481; primary official NBB WVV"),
    ("bud_zkem_kapsubs_2025", "2025", "32459674", "2025 kapitaalsubsidies 32459674 UP (was 31095392); tick1481; primary official NBB WVV"),
    ("bud_zkem_voorz_2025", "2025", "1930508", "2025 voorzieningen+uitgestelde belasting 1930508 (geschillen 40671); tick1481; primary official NBB WVV"),
    ("bud_zkem_debt_2025", "2025", "476306208", "2025 schulden 476306208 JUMP (was 459121965); tick1481; primary official NBB WVV"),
    ("bud_zkem_ltdebt_2025", "2025", "439083134", "2025 LT schulden 439083134 (was 429562679; fin krediet 434791212); tick1481; primary official NBB WVV"),
    ("bud_zkem_stdebt_2025", "2025", "33990641", "2025 ST schulden 33990641 (42 23206023 + leveranciers 5339428); tick1481; primary official NBB WVV"),
    ("bud_zkem_lev_2025", "2025", "5339428", "2025 leveranciers 5339428 (was 7270579); tick1481; primary official NBB WVV"),
    ("bud_zkem_bezold_2025", "2025", "1082940", "2025 bezoldigingen-schulden 1082940 (was 1015529); tick1481; primary official NBB WVV"),
    ("bud_zkem_taxpay_2025", "2025", "2402976", "2025 belastingschulden 2402976 (was 1206638); tick1481; primary official NBB WVV"),
    ("bud_zkem_deferred_2025", "2025", "3232433", "2025 overlopend passief 3232433 (was 2662471); tick1481; primary official NBB WVV"),
    ("bud_zkem_omzet_2025", "2025", "35325415", "2025 omzet 70 35325415 DROP (was 42853240; verhuur 29018840 verkoop 3531700 andere 2774875); tick1481; primary official NBB WVV"),
    ("bud_zkem_diensten_2025", "2025", "10462898", "2025 diensten 61 10462898 JUMP (was 9490243); tick1481; primary official NBB WVV"),
    ("bud_zkem_pers_2025", "2025", "7117830", "2025 pers 62 7117830; 86.6 VTE vs 85.5; 124828 uur; YE 89 / 89.1 VTE; tick1481; primary official NBB WVV"),
    ("bud_zkem_afschr_2025", "2025", "15440732", "2025 afschrijvingen 15440732; tick1481; primary official NBB WVV"),
    ("bud_zkem_expl_2025", "2025", "1415819", "2025 bedrijfswinst 1415819 JUMP (was -45241); tick1481; primary official NBB WVV"),
    ("bud_zkem_finopbr_2025", "2025", "9106157", "2025 financiele opbrengsten 9106157 (interestsubs 7924341); tick1481; primary official NBB WVV"),
    ("bud_zkem_finkost_2025", "2025", "10149101", "2025 financiele kosten 10149101; tick1481; primary official NBB WVV"),
    ("bud_zkem_pnl_2025", "2025", "417118", "2025 PnL 417118 JUMP (was -1143473); tick1481; primary official NBB WVV"),
    ("bud_zkem_div_2025", "2025", "0", "2025 dividend 0; tick1481; primary official NBB WVV"),
    ("bud_zkem_capex_2025", "2025", "34832940", "2025 capex MVA aanschaf 34832940 (terreinen 5145863 meubilair 18739 in aanbouw 29668338); tick1481; primary official NBB WVV"),
    ("bud_zkem_in_aanbouw_2025", "2025", "21659721", "2025 activa in aanbouw 21659721 DROP (was 34042290); tick1481; primary official NBB WVV"),
    ("bud_zkem_krediet_2025", "2025", "434791212", "2025 LT kredietinstellingen 434791212 (was 424984546); tick1481; primary official NBB WVV"),
    ("bud_zkem_terreinen_2025", "2025", "484330629", "2025 terreinen en gebouwen 484330629 (was 452411899); tick1481; primary official NBB WVV"),
    ("bud_zkem_commissaris_2025", "2025", "12415", "2025 commissaris fee 12415 Compass Audit BV; tick1481; primary official NBB WVV"),
    ("bud_zkem_tax_2025", "2025", "275", "2025 belastingen op het resultaat 275; tick1481; primary official NBB WVV"),
    ("bud_zkem_interestsubs_2025", "2025", "7924341", "2025 interestsubsidies 7924341 (was 6663760); tick1481; primary official NBB WVV 6.11"),
    ("bud_zkem_explsubs_2025", "2025", "1242594", "2025 exploitatiesubsidies 1242594 (was 1233996); tick1481; primary official NBB WVV 6.10"),
    ("bud_zkem_geldbeleg_2025", "2025", "2990", "2025 geldbeleggingen 2990 DROP (was 7299770); tick1481; primary official NBB WVV"),
    ("bud_zkem_bestuurders_2025", "2025", "37276", "2025 bestuurders 9503 37276; tick1481; primary official NBB WVV 6.16"),
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

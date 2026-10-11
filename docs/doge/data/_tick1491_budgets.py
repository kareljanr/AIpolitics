#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_onod"
SRC = "src_onod_jr2025_nbb"
BUDGETS = [
    ("bud_onod_assets_2025", "2025", "136782795", "2025 assets 136782795 UP (was 130780757); tick1491; primary official NBB WVV VOL-inb 2026-00189814"),
    ("bud_onod_current_2025", "2025", "15155591", "2025 vlottend 15155591 DROP (was 16518599); tick1491; primary official NBB WVV"),
    ("bud_onod_cash_2025", "2025", "5008962", "2025 liquide middelen 5008962 DROP (was 5485677); tick1491; primary official NBB WVV"),
    ("bud_onod_strecv_2025", "2025", "1487676", "2025 ST vorderingen 1487676 JUMP (was 685922); tick1491; primary official NBB WVV"),
    ("bud_onod_trade_2025", "2025", "155569", "2025 handelsvorderingen 155569 DROP (was 479568); tick1491; primary official NBB WVV"),
    ("bud_onod_othrecv_2025", "2025", "1332106", "2025 overige ST vorderingen 1332106 JUMP (was 206354); tick1491; primary official NBB WVV"),
    ("bud_onod_voorr_2025", "2025", "4227696", "2025 voorraden onroerend verkoop 4227696 DROP (was 6006993); tick1491; primary official NBB WVV"),
    ("bud_onod_geldbeleg_2025", "2025", "3000000", "2025 geldbeleggingen termijnrekeningen 3000000; tick1491; primary official NBB WVV"),
    ("bud_onod_prepaid_2025", "2025", "1431258", "2025 overlopend actief 1431258 (was 1340007); tick1491; primary official NBB WVV"),
    ("bud_onod_fixed_2025", "2025", "121627204", "2025 vaste activa 121627204 UP (was 114262157); tick1491; primary official NBB WVV"),
    ("bud_onod_iva_2025", "2025", "0", "2025 IVA 21 empty; tick1491; primary official NBB WVV"),
    ("bud_onod_mva_2025", "2025", "120977914", "2025 MVA 120977914 UP (was 113678738; terreinen/gebouwen 110450065 installaties 2996 meubilair 104380 overige 6929 in aanbouw 10413545); tick1491; primary official NBB WVV"),
    ("bud_onod_fva_2025", "2025", "649290", "2025 FVA 649290 (was 583420; andere FVA aandelen 604490 + borg 44800); tick1491; primary official NBB WVV"),
    ("bud_onod_equity_2025", "2025", "34735657", "2025 eigen vermogen 34735657 (was 32706509); tick1491; primary official NBB WVV"),
    ("bud_onod_inbreng_2025", "2025", "55094", "2025 inbreng 55094 onbeschikbaar (was 55131); tick1491; primary official NBB WVV"),
    ("bud_onod_reserves_2025", "2025", "29179802", "2025 reserves 29179802 (was 28857874); tick1491; primary official NBB WVV"),
    ("bud_onod_kapsubs_2025", "2025", "5500761", "2025 kapitaalsubsidies 5500761 JUMP (was 3793504); tick1491; primary official NBB WVV"),
    ("bud_onod_voorz_2025", "2025", "456691", "2025 voorzieningen+uitgestelde belasting 456691 (herstel 159573; uitgestelde 297118); tick1491; primary official NBB WVV"),
    ("bud_onod_debt_2025", "2025", "101590448", "2025 schulden 101590448 (was 97691302); tick1491; primary official NBB WVV"),
    ("bud_onod_ltdebt_2025", "2025", "93370945", "2025 LT schulden 93370945 (was 88254700; fin krediet 91993798); tick1491; primary official NBB WVV"),
    ("bud_onod_stdebt_2025", "2025", "7480686", "2025 ST schulden 7480686 (42 3837016 + leveranciers 1863354); tick1491; primary official NBB WVV"),
    ("bud_onod_lev_2025", "2025", "1863354", "2025 leveranciers 1863354 (was 1746442); tick1491; primary official NBB WVV"),
    ("bud_onod_deferred_2025", "2025", "738817", "2025 overlopend passief 738817 (was 692477); tick1491; primary official NBB WVV"),
    ("bud_onod_omzet_2025", "2025", "11511389", "2025 omzet 70 11511389 (was 10809659; 6.10 huur 9044302 / koop 2467087); tick1491; primary official NBB WVV"),
    ("bud_onod_diensten_2025", "2025", "3444762", "2025 diensten 61 3444762 (was 3439777); tick1491; primary official NBB WVV"),
    ("bud_onod_pers_2025", "2025", "1919909", "2025 pers 62 1919909; 23.3 VTE vs 23.4; 32742 uur; YE 27; tick1491; primary official NBB WVV"),
    ("bud_onod_afschr_2025", "2025", "3470137", "2025 afschrijvingen 3470137; tick1491; primary official NBB WVV"),
    ("bud_onod_expl_2025", "2025", "1004522", "2025 bedrijfswinst 1004522 DROP (was 1725847); tick1491; primary official NBB WVV"),
    ("bud_onod_finopbr_2025", "2025", "1590628", "2025 financiele opbrengsten 1590628 (interestsubs 1335992); tick1491; primary official NBB WVV"),
    ("bud_onod_finkost_2025", "2025", "2280233", "2025 financiele kosten 2280233; tick1491; primary official NBB WVV"),
    ("bud_onod_pnl_2025", "2025", "321927", "2025 PnL 321927 DROP (was 946143); tick1491; primary official NBB WVV"),
    ("bud_onod_div_2025", "2025", "0", "2025 dividend 0; tick1491; primary official NBB WVV"),
    ("bud_onod_capex_2025", "2025", "11194008", "2025 capex MVA aanschaf 11194008 (terreinen 610598 meubilair 51871 in aanbouw 10531539); tick1491; primary official NBB WVV"),
    ("bud_onod_in_aanbouw_2025", "2025", "10413545", "2025 activa in aanbouw 10413545 JUMP (was 4528169); tick1491; primary official NBB WVV"),
    ("bud_onod_krediet_2025", "2025", "91993798", "2025 LT kredietinstellingen 91993798 (was 86981533); tick1491; primary official NBB WVV"),
    ("bud_onod_terreinen_2025", "2025", "110450065", "2025 terreinen en gebouwen 110450065 (was 109044032); tick1491; primary official NBB WVV"),
    ("bud_onod_commissaris_2025", "2025", "7800", "2025 commissaris fee 7800 AUDITAS BV; tick1491; primary official NBB WVV"),
    ("bud_onod_interestsubs_2025", "2025", "1335992", "2025 interestsubsidies 9126 1335992 (was 1060223); tick1491; primary official NBB WVV 6.11"),
    ("bud_onod_explsubs_2025", "2025", "665184", "2025 exploitatiesubsidies 740 665184 (was 660282); tick1491; primary official NBB WVV 6.10"),
    ("bud_onod_huur_2025", "2025", "9044302", "2025 6.10 omzet huur 9044302 (was 8619701); tick1491; primary official NBB WVV"),
    ("bud_onod_koop_2025", "2025", "2467087", "2025 6.10 omzet koop 2467087 (was 2189959); tick1491; primary official NBB WVV"),
    ("bud_onod_kapsubs_amort_2025", "2025", "129442", "2025 kapitaalsubsidies 9125 129442 (was 122834); tick1491; primary official NBB WVV 6.11"),
    ("bud_onod_bestuurders_2025", "2025", "26515", "2025 bestuurders 9503 26515; tick1491; primary official NBB WVV 6.16"),
    ("bud_onod_bedrijfsopbr_2025", "2025", "13226619", "2025 bedrijfsopbrengsten 70/76A 13226619 (was 12954750); tick1491; primary official NBB WVV"),
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

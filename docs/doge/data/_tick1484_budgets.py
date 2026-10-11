#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_mpls"
SRC = "src_mpls_jr2025_nbb"
BUDGETS = [
    ("bud_mpls_assets_2025", "2025", "213864560", "2025 assets 213864560 UP (was 202097537); tick1484; primary official NBB WVV VOL-kap 2026-00117115"),
    ("bud_mpls_current_2025", "2025", "13511269", "2025 vlottend 13511269 DROP (was 18208563); tick1484; primary official NBB WVV"),
    ("bud_mpls_cash_2025", "2025", "9225512", "2025 liquide middelen 9225512 DROP (was 14391203); tick1484; primary official NBB WVV"),
    ("bud_mpls_strecv_2025", "2025", "1316844", "2025 ST vorderingen 1316844 (was 1364426); tick1484; primary official NBB WVV"),
    ("bud_mpls_trade_2025", "2025", "441685", "2025 handelsvorderingen 441685 (was 419440); tick1484; primary official NBB WVV"),
    ("bud_mpls_othrecv_2025", "2025", "875159", "2025 overige ST vorderingen 875159 (was 944986); tick1484; primary official NBB WVV"),
    ("bud_mpls_voorraden_2025", "2025", "88528", "2025 voorraden 88528 (onroerend verkoop 88528); tick1484; primary official NBB WVV"),
    ("bud_mpls_prepaid_2025", "2025", "2880385", "2025 overlopend actief 2880385 (was 2452934); tick1484; primary official NBB WVV"),
    ("bud_mpls_fixed_2025", "2025", "200353291", "2025 vaste activa 200353291 (was 183888974); tick1484; primary official NBB WVV"),
    ("bud_mpls_iva_2025", "2025", "9242", "2025 IVA 9242 (was 15777); tick1484; primary official NBB WVV"),
    ("bud_mpls_mva_2025", "2025", "199556705", "2025 MVA 199556705 (was 183104616; terreinen/gebouwen 179374629 meubilair 213058 leasing 31312 overige 1269942 in aanbouw 18667764); tick1484; primary official NBB WVV"),
    ("bud_mpls_fva_2025", "2025", "787344", "2025 FVA 787344 (was 768581); tick1484; primary official NBB WVV"),
    ("bud_mpls_equity_2025", "2025", "62364982", "2025 eigen vermogen 62364982 (was 60669016); tick1484; primary official NBB WVV"),
    ("bud_mpls_inbreng_2025", "2025", "113384", "2025 inbreng 113384 (kapitaal 117149 / buiten kapitaal -3765); tick1484; primary official NBB WVV"),
    ("bud_mpls_reserves_2025", "2025", "39350499", "2025 reserves 39350499 (was 38124590); tick1484; primary official NBB WVV"),
    ("bud_mpls_kapsubs_2025", "2025", "19817149", "2025 kapitaalsubsidies 19817149 UP (was 19344940); tick1484; primary official NBB WVV"),
    ("bud_mpls_voorz_2025", "2025", "2190568", "2025 voorzieningen+uitgestelde belasting 2190568 (herstel 1022406); tick1484; primary official NBB WVV"),
    ("bud_mpls_debt_2025", "2025", "149309010", "2025 schulden 149309010 JUMP (was 139111440); tick1484; primary official NBB WVV"),
    ("bud_mpls_ltdebt_2025", "2025", "137507382", "2025 LT schulden 137507382 (was 128269656; fin krediet 135359108); tick1484; primary official NBB WVV"),
    ("bud_mpls_stdebt_2025", "2025", "10357804", "2025 ST schulden 10357804 (42 5618682 + leveranciers 2939661); tick1484; primary official NBB WVV"),
    ("bud_mpls_lev_2025", "2025", "2939661", "2025 leveranciers 2939661 (was 2387500); tick1484; primary official NBB WVV"),
    ("bud_mpls_bezold_2025", "2025", "295663", "2025 bezoldigingen-schulden 295663 (was 270859); tick1484; primary official NBB WVV"),
    ("bud_mpls_taxpay_2025", "2025", "838583", "2025 belastingschulden 838583 (was 712423); tick1484; primary official NBB WVV"),
    ("bud_mpls_deferred_2025", "2025", "1443824", "2025 overlopend passief 1443824 (was 1364992); tick1484; primary official NBB WVV"),
    ("bud_mpls_omzet_2025", "2025", "13185888", "2025 omzet 70 13185888 UP (was 12760808; 6.10 split unpublished); tick1484; primary official NBB WVV"),
    ("bud_mpls_diensten_2025", "2025", "5317564", "2025 diensten 61 5317564 (was 5282951); tick1484; primary official NBB WVV"),
    ("bud_mpls_pers_2025", "2025", "2677490", "2025 pers 62 2677490; 33.4 VTE vs 31.7; 51173 uur; YE 37 / 32.9 VTE; tick1484; primary official NBB WVV"),
    ("bud_mpls_afschr_2025", "2025", "5472965", "2025 afschrijvingen 5472965; tick1484; primary official NBB WVV"),
    ("bud_mpls_expl_2025", "2025", "1083823", "2025 bedrijfswinst 1083823 (was 109963); tick1484; primary official NBB WVV"),
    ("bud_mpls_finopbr_2025", "2025", "3791404", "2025 financiele opbrengsten 3791404 (interestsubs 3036205 JUMP); tick1484; primary official NBB WVV"),
    ("bud_mpls_finkost_2025", "2025", "3614267", "2025 financiele kosten 3614267; tick1484; primary official NBB WVV"),
    ("bud_mpls_pnl_2025", "2025", "1225909", "2025 PnL 1225909 JUMP (was 267829); tick1484; primary official NBB WVV"),
    ("bud_mpls_div_2025", "2025", "0", "2025 dividend 0; tick1484; primary official NBB WVV"),
    ("bud_mpls_capex_2025", "2025", "22387387", "2025 capex MVA aanschaf 22387387 (terreinen 3938036 meubilair 13763 leasing 32487 in aanbouw 18403101); tick1484; primary official NBB WVV"),
    ("bud_mpls_in_aanbouw_2025", "2025", "18667764", "2025 activa in aanbouw 18667764 JUMP (was 10361975); tick1484; primary official NBB WVV"),
    ("bud_mpls_krediet_2025", "2025", "135359108", "2025 LT kredietinstellingen 135359108 JUMP (was 126234492); tick1484; primary official NBB WVV"),
    ("bud_mpls_terreinen_2025", "2025", "179374629", "2025 terreinen en gebouwen 179374629 (was 171125994); tick1484; primary official NBB WVV"),
    ("bud_mpls_commissaris_2025", "2025", "10876", "2025 commissaris fee 10876 VRC Bedrijfsrevisoren BV; tick1484; primary official NBB WVV"),
    ("bud_mpls_tax_2025", "2025", "68985", "2025 belastingen op het resultaat 68985; tick1484; primary official NBB WVV"),
    ("bud_mpls_interestsubs_2025", "2025", "3036205", "2025 interestsubsidies 9126 3036205 JUMP (was 179373); tick1484; primary official NBB WVV 6.11"),
    ("bud_mpls_explsubs_2025", "2025", "382344", "2025 exploitatiesubsidies 740 382344 (was 556874); tick1484; primary official NBB WVV 6.10"),
    ("bud_mpls_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen 50/53 empty; tick1484; primary official NBB WVV"),
    ("bud_mpls_bestuurders_2025", "2025", "37984", "2025 bestuurders 9503 empty; remuneratieverslag belastbaar 37983.50; tick1484; primary official NBB WVV"),
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

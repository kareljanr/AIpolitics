#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1558 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_meem"
SRC = "src_meemoo_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:180]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

rows = [
    f"bud_meemoo_bruto_2025,{ENT},2025,5412745,,,executed,{SRC},strong,2025 brutomarge 9900 5412745 envelope (leftover public koepel VZW; VKT and omzet 70 empty; 73 empty); UP was 5265269; tick1558; primary official NBB VKT-VZW AV 23.04.2026",
    f"bud_meemoo_assets_2025,{ENT},2025,3435584,,,executed,{SRC},strong,2025 balanstotaal 20/58 3435584 DROP was 3780032; VA+vlottend holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_va_2025,{ENT},2025,779864,,,executed,{SRC},strong,2025 vaste activa 21/28 779864 UP was 748026; IVA+MVA+FVA holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_iva_2025,{ENT},2025,279321,,,executed,{SRC},strong,2025 IVA 21 279321 DROP was 404100; aanschaffingen 8029 227174; YE afschr 1999893; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_mva_2025,{ENT},2025,473034,,,executed,{SRC},strong,2025 MVA 22/27 473034 UP was 316418; installaties 23 452738 JUMP; meubilair 24 19896 DROP; aanbouw 27 400; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_install_2025,{ENT},2025,452738,,,executed,{SRC},strong,2025 installaties machines uitrusting 23 452738 JUMP was 283406; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_fva_2025,{ENT},2025,27509,,,executed,{SRC},strong,2025 FVA 28 27509 identiek; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_vlottend_2025,{ENT},2025,2655720,,,executed,{SRC},strong,2025 vlottende 29/58 2655720 DROP was 3032006; recv+cash+prepaid holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_recv_2025,{ENT},2025,1232417,,,executed,{SRC},strong,2025 vorderingen ST 40/41 1232417 UP was 1086611; handelsrecv 40 23299 DROP; other recv 41 1209119 UP; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_otherrecv_2025,{ENT},2025,1209119,,,executed,{SRC},strong,2025 overige vorderingen 41 1209119 UP was 1048554; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_cash_2025,{ENT},2025,994688,,,executed,{SRC},strong,2025 liquide middelen 54/58 994688 DROP was 1487658; beleg 50/53 empty; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_prepaid_2025,{ENT},2025,428614,,,executed,{SRC},strong,2025 overlopend actief 490/1 428614 DROP was 457737; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_equity_2025,{ENT},2025,525301,,,executed,{SRC},strong,2025 eigen vermogen 10/15 525301 UP was 513751; reserves+overgedragen holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_reserves_2025,{ENT},2025,250000,,,executed,{SRC},strong,2025 bestemde fondsen 13 250000 UP was 150000; +100000 onbestemde reserve sociaal passief / subsidy-cut (PDF still names VIAA); tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_overgedragen_2025,{ENT},2025,275301,,,executed,{SRC},strong,2025 overgedragen resultaat 14 275301 DROP was 363751; 14P+9905-691 holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_debt_2025,{ENT},2025,2910282,,,executed,{SRC},strong,2025 schulden 17/49 2910282 DROP was 3266281; ST+accrued holds (1 euro NBB rounding); LT empty; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_st_2025,{ENT},2025,1939442,,,executed,{SRC},strong,2025 ST 42/48 1939442 JUMP was 1562305; lev+taxsoc+vooruit holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_lev_2025,{ENT},2025,1076339,,,executed,{SRC},strong,2025 handelsschulden 44 / leveranciers 440/4 1076339 JUMP was 738887; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_taxsoc_2025,{ENT},2025,838380,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 838380; tax 145177 + bezold 693203 holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_accrued_2025,{ENT},2025,970841,,,executed,{SRC},strong,2025 overlopend passief 492/3 970841 DROP was 1703976; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_pers_2025,{ENT},2025,4927717,,,executed,{SRC},strong,2025 bezoldigingen 62 4927717 / 64.9 VTE UP was 4794138 / 62.8; YE 60.8 / 45 voltijds + 19 deeltijds / 101126 uur; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_afschr_2025,{ENT},2025,452477,,,executed,{SRC},strong,2025 afschrijvingen 630 452477 DROP was 516643; IVA 351952 + MVA 100525 holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_othercosts_2025,{ENT},2025,37097,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 37097 DROP was 39811; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_expl_2025,{ENT},2025,-4546,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -4546 LOSS was -85324; bruto-pers-afschr-other holds; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_fininc_2025,{ENT},2025,25415,,,executed,{SRC},strong,2025 financiele opbrengsten 75 25415 DROP was 82935; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_fincost_2025,{ENT},2025,1693,,,executed,{SRC},strong,2025 financiele kosten 65 1693 UP was 1582; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_pnl_2025,{ENT},2025,11551,,,executed,{SRC},strong,2025 resultaat 9904/9905 11551 PROFIT was -28844 LOSS; tax 7624; 9903 19175; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_commissaris_2025,{ENT},2025,8600,,,executed,{SRC},strong,2025 commissaris 8600 (Moore Audit BV / Carmen Van Camp); extra auditopdrachten 2500; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_capex_2025,{ENT},2025,484316,,,executed,{SRC},strong,2025 IVA aanschaffingen 8029 227174 + MVA aanschaffingen 8169 257142 = 484316; tick1558; primary official NBB VKT-VZW",
    f"bud_meemoo_uren_2025,{ENT},2025,101126,,,executed,{SRC},strong,2025 sociale balans uren 101 101126 DROP was 101817; in 10.8 VTE / uit 15.8 VTE; opleiding formeel 72199 + informeel 131825; tick1558; primary official NBB VKT-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +%d" % len(rows), before, "->", after)

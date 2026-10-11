#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1559 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_knst"
SRC = "src_kunstenpunt_jr2025_nbb"

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
    f"bud_knst_bruto_2025,{ENT},2025,1713627,,,executed,{SRC},strong,2025 brutomarge 9900 1713627 envelope (leftover public koepel VZW; VKT and omzet 70 empty; 73 empty); DROP was 1880371; tick1559; primary official NBB VKT-VZW AV 23.03.2026",
    f"bud_knst_assets_2025,{ENT},2025,677951,,,executed,{SRC},strong,2025 balanstotaal 20/58 677951 DROP was 698077; VA+vlottend holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_va_2025,{ENT},2025,50772,,,executed,{SRC},strong,2025 vaste activa 21/28 50772 DROP was 73990; IVA+MVA+FVA holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_iva_2025,{ENT},2025,39212,,,executed,{SRC},strong,2025 IVA 21 39212 DROP was 54946; aanschaffingen 8029 empty; YE afschr 147706; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_mva_2025,{ENT},2025,9685,,,executed,{SRC},strong,2025 MVA 22/27 9685 DROP was 17169; installaties 23 8474 DROP; overige 26 1212; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_install_2025,{ENT},2025,8474,,,executed,{SRC},strong,2025 installaties machines uitrusting 23 8474 DROP was 14745; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_fva_2025,{ENT},2025,1875,,,executed,{SRC},strong,2025 FVA 28 1875 identiek; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_vlottend_2025,{ENT},2025,627179,,,executed,{SRC},strong,2025 vlottende 29/58 627179 UP was 624087; recv+cash+prepaid holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_recv_2025,{ENT},2025,259817,,,executed,{SRC},strong,2025 vorderingen ST 40/41 259817 UP was 243187; handelsrecv 40 25275 UP; other recv 41 234542 UP; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_otherrecv_2025,{ENT},2025,234542,,,executed,{SRC},strong,2025 overige vorderingen 41 234542 UP was 221550; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_cash_2025,{ENT},2025,324544,,,executed,{SRC},strong,2025 liquide middelen 54/58 324544 DROP was 368551; beleg 50/53 empty; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_prepaid_2025,{ENT},2025,42818,,,executed,{SRC},strong,2025 overlopend actief 490/1 42818 JUMP was 12349; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_equity_2025,{ENT},2025,366477,,,executed,{SRC},strong,2025 eigen vermogen 10/15 366477 DROP was 423811; fondsen+reserves+overgedragen holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_fondsen_2025,{ENT},2025,183615,,,executed,{SRC},strong,2025 fondsen 10 183615 identiek; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_reserves_2025,{ENT},2025,89870,,,executed,{SRC},strong,2025 bestemde fondsen 13 89870 DROP was 101529; onttrekking 791 11659 Overname fusie VTI + projecten; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_overgedragen_2025,{ENT},2025,92992,,,executed,{SRC},strong,2025 overgedragen resultaat 14 92992 DROP was 138667; 14P+9905+791 holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_debt_2025,{ENT},2025,311474,,,executed,{SRC},strong,2025 schulden 17/49 311474 UP was 274265; ST+accrued holds; LT empty; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_st_2025,{ENT},2025,254298,,,executed,{SRC},strong,2025 ST 42/48 254298 DROP was 254972; lev+taxsoc+vooruit holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_lev_2025,{ENT},2025,70453,,,executed,{SRC},strong,2025 handelsschulden 44 / leveranciers 440/4 70453 JUMP was 45202; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_taxsoc_2025,{ENT},2025,182745,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 182745; tax 371 + bezold 182374 holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_accrued_2025,{ENT},2025,57176,,,executed,{SRC},strong,2025 overlopend passief 492/3 57176 JUMP was 19293; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_pers_2025,{ENT},2025,1742627,,,executed,{SRC},strong,2025 bezoldigingen 62 1742627 / 20 VTE DROP was 1769511 / 20.8; YE 19 / 12 voltijds + 10 deeltijds / 32513 uur; pers exceeds bruto; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_afschr_2025,{ENT},2025,27192,,,executed,{SRC},strong,2025 afschrijvingen 630 27192 DROP was 34116; IVA 15734 + MVA 11458 holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_othercosts_2025,{ENT},2025,735,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 735 DROP was 7493; plus 66A 169; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_expl_2025,{ENT},2025,-57096,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -57096 LOSS was 61113 PROFIT; bruto-pers-afschr-other-66A holds; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_fininc_2025,{ENT},2025,476,,,executed,{SRC},strong,2025 financiele opbrengsten 75/76B 476 DROP was 18730; rec 408 + nonrec 68; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_fincost_2025,{ENT},2025,714,,,executed,{SRC},strong,2025 financiele kosten 65 714 DROP was 4288; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_pnl_2025,{ENT},2025,-57334,,,executed,{SRC},strong,2025 resultaat 9904/9905 -57334 LOSS was 75555 PROFIT; tax empty; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_capex_2025,{ENT},2025,8788,,,executed,{SRC},strong,2025 IVA aanschaffingen 8029 empty + MVA aanschaffingen 8169 8788 = 8788; MVA overdrachten 8179 5891; tick1559; primary official NBB VKT-VZW",
    f"bud_knst_uren_2025,{ENT},2025,32513,,,executed,{SRC},strong,2025 sociale balans uren 101 32513 DROP was 34300; in 6.6 VTE / uit 8.4 VTE; tick1559; primary official NBB VKT-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +%d" % len(rows), before, "->", after)

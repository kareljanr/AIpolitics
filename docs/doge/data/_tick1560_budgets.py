#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1560 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_soci"
SRC = "src_socius_jr2025_nbb"

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
    f"bud_soci_bruto_2025,{ENT},2025,1380002,,,executed,{SRC},strong,2025 brutomarge 9900 1380002 envelope (leftover public koepel VZW; VKT and omzet 70 empty; 73 empty); UP was 1285595; 76A 702; tick1560; primary official NBB VKT-VZW AV 25.03.2026",
    f"bud_soci_assets_2025,{ENT},2025,1356462,,,executed,{SRC},strong,2025 balanstotaal 20/58 1356462 UP was 1277859; VA+vlottend holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_va_2025,{ENT},2025,39032,,,executed,{SRC},strong,2025 vaste activa 21/28 39032 JUMP was 6888; IVA empty FVA empty; MVA holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_mva_2025,{ENT},2025,39032,,,executed,{SRC},strong,2025 MVA 22/27 39032 JUMP was 6888; installaties 23 38965 JUMP; meubilair 24 67 DROP; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_install_2025,{ENT},2025,38965,,,executed,{SRC},strong,2025 installaties machines uitrusting 23 38965 JUMP was 6754; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_vlottend_2025,{ENT},2025,1317430,,,executed,{SRC},strong,2025 vlottende 29/58 1317430 UP was 1270971; recv+beleg+cash+prepaid holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_recv_2025,{ENT},2025,192811,,,executed,{SRC},strong,2025 vorderingen ST 40/41 192811 UP was 173066; handelsrecv 40 15511 JUMP; other recv 41 177300 UP; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_handelsrecv_2025,{ENT},2025,15511,,,executed,{SRC},strong,2025 handelsvorderingen 40 15511 JUMP was 6733; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_otherrecv_2025,{ENT},2025,177300,,,executed,{SRC},strong,2025 overige vorderingen 41 177300 UP was 166333; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_beleg_2025,{ENT},2025,1044949,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1044949 UP was 1023645; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_cash_2025,{ENT},2025,74193,,,executed,{SRC},strong,2025 liquide middelen 54/58 74193 UP was 68525; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_prepaid_2025,{ENT},2025,5336,,,executed,{SRC},strong,2025 overlopend actief 490/1 5336 DROP was 5523; voorraden 140; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_equity_2025,{ENT},2025,919966,,,executed,{SRC},strong,2025 eigen vermogen 10/15 919966 UP was 816239; fondsen+reserves+overgedragen holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_fondsen_2025,{ENT},2025,39054,,,executed,{SRC},strong,2025 fondsen 10 39054 identiek permanente financiering; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_reserves_2025,{ENT},2025,583085,,,executed,{SRC},strong,2025 bestemde fondsen 13 583085 identiek; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_overgedragen_2025,{ENT},2025,297827,,,executed,{SRC},strong,2025 overgedragen resultaat 14 297827 UP was 194101; 14P 194101 + 9905 103727 holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_voorzien_2025,{ENT},2025,183251,,,executed,{SRC},strong,2025 voorzieningen 16 / 164/5 183251 identiek; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_debt_2025,{ENT},2025,253244,,,executed,{SRC},strong,2025 schulden 17/49 253244 DROP was 278368; ST+accrued holds; LT empty; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_st_2025,{ENT},2025,223244,,,executed,{SRC},strong,2025 ST 42/48 223244 DROP was 246368; lev+taxsoc+other holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_lev_2025,{ENT},2025,70980,,,executed,{SRC},strong,2025 handelsschulden 44 / leveranciers 440/4 70980 DROP was 115412; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_taxsoc_2025,{ENT},2025,142688,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 142688 UP was 130239; tax 3521 + bezold 139167 holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_otherst_2025,{ENT},2025,9576,,,executed,{SRC},strong,2025 overige ST 48 9576 JUMP was 716; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_accrued_2025,{ENT},2025,30000,,,executed,{SRC},strong,2025 overlopend passief 492/3 30000 DROP was 32000; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_pers_2025,{ENT},2025,1265278,,,executed,{SRC},strong,2025 bezoldigingen 62 1265278 / 12.2 VTE DROP was 1336892 / 13.7; YE 12.1 / 9 voltijds + 5 deeltijds / 18041 uur; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_afschr_2025,{ENT},2025,15703,,,executed,{SRC},strong,2025 afschrijvingen 630 15703 JUMP was 7132; MVA 8279 15703; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_othercosts_2025,{ENT},2025,7841,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 7841 JUMP was 3402; 66A empty; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_expl_2025,{ENT},2025,91179,,,executed,{SRC},strong,2025 bedrijfswinst 9901 91179 PROFIT was 12169; bruto-pers-afschr-other official 1-euro vs 91180; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_fininc_2025,{ENT},2025,12851,,,executed,{SRC},strong,2025 financiele opbrengsten 75 12851 UP was 8382; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_fincost_2025,{ENT},2025,303,,,executed,{SRC},strong,2025 financiele kosten 65 303 UP was 192; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_pnl_2025,{ENT},2025,103727,,,executed,{SRC},strong,2025 resultaat 9904/9905 103727 PROFIT was 20359; tax empty; 9903=expl+fin-fincost holds; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_capex_2025,{ENT},2025,47847,,,executed,{SRC},strong,2025 MVA aanschaffingen 8169 47847; overdrachten 8179 6014; YE aanschaf 355707; tick1560; primary official NBB VKT-VZW",
    f"bud_soci_uren_2025,{ENT},2025,18041,,,executed,{SRC},strong,2025 sociale balans uren 101 18041 DROP was 19782; in 1 VTE / uit 1 VTE; PC 329; tick1560; primary official NBB VKT-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +%d" % len(rows), before, "->", after)

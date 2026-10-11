#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1557 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "son_vlho"
SRC = "src_vlhora_jr2025_nbb"

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
    f"bud_vlhora_bruto_2025,{ENT},2025,1200770,,,executed,{SRC},strong,2025 brutomarge 9900 1200770 envelope (leftover public koepel SON; VKT and omzet 70 empty; 73 empty); UP was 980966; tick1557; primary official NBB VKT-VZW AV 27.03.2026",
    f"bud_vlhora_assets_2025,{ENT},2025,11929249,,,executed,{SRC},strong,2025 balanstotaal 20/58 11929249 UP was 9899952; VA+vlottend holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_va_2025,{ENT},2025,3789,,,executed,{SRC},strong,2025 vaste activa 21/28 3789 (prior empty / prior assets=vlottend); MVA only; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_mva_2025,{ENT},2025,3789,,,executed,{SRC},strong,2025 MVA 22/27 3789; meubilair 24 3789; aanschaffingen 8169 5683; YE afschr 303322; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_meubilair_2025,{ENT},2025,3789,,,executed,{SRC},strong,2025 meubilair en rollend materieel 24 3789; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_vlottend_2025,{ENT},2025,11925460,,,executed,{SRC},strong,2025 vlottende 29/58 11925460 JUMP was 9899952; recv+beleg+cash holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_handelsrecv_2025,{ENT},2025,7665740,,,executed,{SRC},strong,2025 handelsvorderingen 40 7665740 JUMP was 4964066; other recv 41 empty; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_beleg_2025,{ENT},2025,1287303,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1287303 DROP was 1292418; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_cash_2025,{ENT},2025,2972417,,,executed,{SRC},strong,2025 liquide middelen 54/58 2972417 DROP was 3643468; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_equity_2025,{ENT},2025,1931641,,,executed,{SRC},strong,2025 eigen vermogen 10/15 1931641 UP was 1788548; fondsen+reserves+overgedragen holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_fondsen_2025,{ENT},2025,181880,,,executed,{SRC},strong,2025 fondsen 10 181880 identiek; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_reserves_2025,{ENT},2025,254400,,,executed,{SRC},strong,2025 bestemde fondsen 13 254400 identiek (sociaal passief / Andere; pandemie-reserve; 2025 geen verandering); tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_overgedragen_2025,{ENT},2025,1495361,,,executed,{SRC},strong,2025 overgedragen resultaat 14 1495361 UP was 1352268; 14P+9905 holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_debt_2025,{ENT},2025,9997608,,,executed,{SRC},strong,2025 schulden 17/49 9997608 JUMP was 8111404; ST+accrued holds; LT empty; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_st_2025,{ENT},2025,626889,,,executed,{SRC},strong,2025 ST 42/48 626889 DROP was 1659750; lev+taxsoc holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_lev_2025,{ENT},2025,439394,,,executed,{SRC},strong,2025 handelsschulden 44 / leveranciers 440/4 439394 DROP was 1528468; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_taxsoc_2025,{ENT},2025,187495,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 187495 UP was 131282; tax 33272 + bezold 154223 holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_accrued_2025,{ENT},2025,9370719,,,executed,{SRC},strong,2025 overlopend passief 492/3 9370719 JUMP was 6451654; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_pers_2025,{ENT},2025,1052307,,,executed,{SRC},strong,2025 bezoldigingen 62 1052307 / 13.2 VTE UP was 919188 / 12.4; YE 13.2 / 8 voltijds + 10 deeltijds / 19240 uur; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_afschr_2025,{ENT},2025,1894,,,executed,{SRC},strong,2025 afschrijvingen 630 1894 (MVA only; prior empty); tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_othercosts_2025,{ENT},2025,2328,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 2328 UP was 1800; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_expl_2025,{ENT},2025,144241,,,executed,{SRC},strong,2025 bedrijfswinst 9901 144241 PROFIT was 59978; bruto-pers-afschr-other holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_fincost_2025,{ENT},2025,1148,,,executed,{SRC},strong,2025 financiele kosten 65 1148 DROP was 1177; 75 empty; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_pnl_2025,{ENT},2025,143093,,,executed,{SRC},strong,2025 resultaat 9904/9905 143093 PROFIT was 58801; 9903 143093; expl-fincost holds; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_commissaris_2025,{ENT},2025,4958,,,executed,{SRC},strong,2025 commissaris 4958 (EY Bedrijfsrevisoren BV / Elien De Greef); extra opdrachten 0; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_capex_2025,{ENT},2025,5683,,,executed,{SRC},strong,2025 MVA aanschaffingen 8169 5683; IVA empty; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_uren_2025,{ENT},2025,19240,,,executed,{SRC},strong,2025 sociale balans uren 101 19240 DROP was 19380; in 4.4 VTE / uit 2.9 VTE; opleiding 0; tick1557; primary official NBB VKT-VZW",
    f"bud_vlhora_tax_2025,{ENT},2025,33272,,,executed,{SRC},strong,2025 belastingen 450/3 33272 UP was 27646; tick1557; primary official NBB VKT-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +", len(rows), before, "->", after)

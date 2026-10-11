#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1561 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_pubq"
SRC = "src_publiq_jr2025_nbb"

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
    f"bud_pubq_bruto_2025,{ENT},2025,7291932,,,executed,{SRC},strong,2025 brutomarge 9900 7291932 envelope (leftover public koepel VZW; VKT and omzet 70 empty; 73 empty); UP was 6193464; 76A 723; tick1561; primary official NBB VKT-VZW AV 23.03.2026",
    f"bud_pubq_assets_2025,{ENT},2025,4196794,,,executed,{SRC},strong,2025 balanstotaal 20/58 4196794 UP was 3378909; VA+vlottend official 1-euro 4196793; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_va_2025,{ENT},2025,681169,,,executed,{SRC},strong,2025 vaste activa 21/28 681169 DROP was 866285; IVA+MVA+FVA holds; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_iva_2025,{ENT},2025,447279,,,executed,{SRC},strong,2025 IVA 21 447279 DROP was 573059; aanschaf YE 3516080; afschr YE 3068801; capex 8029 387777; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_mva_2025,{ENT},2025,202423,,,executed,{SRC},strong,2025 MVA 22/27 202423 DROP was 262508; install 21669 DROP; meubilair 33054 DROP; overige 147700 DROP; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_install_2025,{ENT},2025,21669,,,executed,{SRC},strong,2025 installaties machines uitrusting 23 21669 DROP was 48535; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_fva_2025,{ENT},2025,31467,,,executed,{SRC},strong,2025 FVA 28 31467 UP was 30719; aanschaf 8365 748; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_vlottend_2025,{ENT},2025,3515624,,,executed,{SRC},strong,2025 vlottende 29/58 3515624 JUMP was 2512624; recv+beleg+cash+prepaid holds; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_recv_2025,{ENT},2025,2328518,,,executed,{SRC},strong,2025 vorderingen ST 40/41 2328518 JUMP was 1669067; handelsrecv 40 869132 JUMP; other recv 41 1459386 JUMP; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_handelsrecv_2025,{ENT},2025,869132,,,executed,{SRC},strong,2025 handelsvorderingen 40 869132 JUMP was 632325; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_otherrecv_2025,{ENT},2025,1459386,,,executed,{SRC},strong,2025 overige vorderingen 41 1459386 JUMP was 1036742; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_beleg_2025,{ENT},2025,267028,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 267028 JUMP was 11703; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_cash_2025,{ENT},2025,862453,,,executed,{SRC},strong,2025 liquide middelen 54/58 862453 UP was 770942; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_prepaid_2025,{ENT},2025,57626,,,executed,{SRC},strong,2025 overlopend actief 490/1 57626 DROP was 60911; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_equity_2025,{ENT},2025,1342745,,,executed,{SRC},strong,2025 eigen vermogen 10/15 1342745 JUMP was 801522; fondsen empty; reserves 13 1342745; overgedragen 14 empty (was -978222); tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_reserves_2025,{ENT},2025,1342745,,,executed,{SRC},strong,2025 bestemde fondsen 13 1342745 DROP was 1779743; sociaal passief 924236 + afschr inv 150780 + gepland 390590 vs post 13; 791 onttrekking 827535; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_voorzien_2025,{ENT},2025,224282,,,executed,{SRC},strong,2025 voorzieningen 16 / 164/5 224282 UP was 207561; 635/9 16721; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_debt_2025,{ENT},2025,2629767,,,executed,{SRC},strong,2025 schulden 17/49 2629767 UP was 2369826; ST+accrued holds; LT empty; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_st_2025,{ENT},2025,1796113,,,executed,{SRC},strong,2025 ST 42/48 1796113 DROP was 2076527; lev+taxsoc+other official 1-euro 1796112; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_lev_2025,{ENT},2025,645327,,,executed,{SRC},strong,2025 handelsschulden 44 / leveranciers 440/4 645327 UP was 636489; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_taxsoc_2025,{ENT},2025,702676,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 702676 DROP was 992084; tax 84508 + bezold 618168 holds; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_otherst_2025,{ENT},2025,448109,,,executed,{SRC},strong,2025 overige ST 48 448109 identiek-ish was 447953; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_accrued_2025,{ENT},2025,833654,,,executed,{SRC},strong,2025 overlopend passief 492/3 833654 JUMP was 293299; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_pers_2025,{ENT},2025,6493450,,,executed,{SRC},strong,2025 bezoldigingen 62 6493450 / 81.2 VTE JUMP was 5666471 / 73.2; YE 77.5 / 48 voltijds + 39 deeltijds / 124502 uur; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_afschr_2025,{ENT},2025,597536,,,executed,{SRC},strong,2025 afschrijvingen 630 597536 DROP was 638053; IVA 8079 513557 + MVA 8279 83979; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_othercosts_2025,{ENT},2025,31815,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 31815 JUMP was 11792; 66A 492; 631/4 -19; 635/9 16721; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_expl_2025,{ENT},2025,151937,,,executed,{SRC},strong,2025 bedrijfswinst 9901 151937 PROFIT was -123964 LOSS; bruto-pers-afschr-wv-voorz-other-66A holds; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_fininc_2025,{ENT},2025,5808,,,executed,{SRC},strong,2025 financiele opbrengsten 75 5808 DROP was 40688; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_fincost_2025,{ENT},2025,7058,,,executed,{SRC},strong,2025 financiele kosten 65 7058 JUMP was 1558; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_pnl_2025,{ENT},2025,150686,,,executed,{SRC},strong,2025 resultaat 9904/9905 150686 PROFIT was -84834 LOSS; tax empty; 9903 official 1-euro vs expl+fin-fincost 150687; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_capex_2025,{ENT},2025,415834,,,executed,{SRC},strong,2025 capex IVA 8029 387777 + MVA 8169 27309 + FVA 8365 748 = 415834; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_onttrek_2025,{ENT},2025,827535,,,executed,{SRC},strong,2025 onttrekking eigen vermogen 791 827535; 9906 -827535; 14P -978222 + 9905 150686 official 1-euro vs -827536; tick1561; primary official NBB VKT-VZW",
    f"bud_pubq_uren_2025,{ENT},2025,124502,,,executed,{SRC},strong,2025 sociale balans uren 101 124502; in 18.9 VTE / uit 26 VTE; PC 329; opleiding 5227; tick1561; primary official NBB VKT-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +%d" % len(rows), before, "->", after)

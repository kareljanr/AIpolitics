#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1553 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vvp"
SRC = "src_vvp_jr2025_nbb"

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
    f"bud_vvp_bruto_2025,{ENT},2025,589640,,,executed,{SRC},strong,2025 brutomarge 9900 589640 envelope (leftover public koepel VZW; VKT and omzet 70 empty; 73 empty); UP was 527144; tick1553; primary official NBB VKT-VZW AV 08.05.2026",
    f"bud_vvp_assets_2025,{ENT},2025,3412677,,,executed,{SRC},strong,2025 balanstotaal 20/58 3412677 DROP was 3525936; VA+vlottend holds; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_va_2025,{ENT},2025,626851,,,executed,{SRC},strong,2025 vaste activa 21/28 626851 JUMP was 29402; IVA+MVA+FVA holds; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_iva_2025,{ENT},2025,38813,,,executed,{SRC},strong,2025 IVA 21 38813 JUMP was 14525; aanschaffingen 8029 34899; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_mva_2025,{ENT},2025,582447,,,executed,{SRC},strong,2025 MVA 22/27 582447 JUMP was 9886; gebouwen 142500 + in aanbouw 432014; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_gebouwen_2025,{ENT},2025,142500,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 142500 JUMP was 0; KBO zetel Groendreef 1 sinds 08.05.2026; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_install_2025,{ENT},2025,4720,,,executed,{SRC},strong,2025 installaties 23 4720 UP was 3333; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_meubilair_2025,{ENT},2025,3213,,,executed,{SRC},strong,2025 meubilair 24 3213 DROP was 6554; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_aanbouw_2025,{ENT},2025,432014,,,executed,{SRC},strong,2025 activa in aanbouw 27 432014 JUMP was 0; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_fva_2025,{ENT},2025,5591,,,executed,{SRC},strong,2025 FVA 28 5591 UP was 4991; aanschaffingen 8365 600; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_vlottend_2025,{ENT},2025,2785826,,,executed,{SRC},strong,2025 vlottende 29/58 2785826 DROP was 3496533; recv+beleg+cash+prepaid holds; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_handelsrecv_2025,{ENT},2025,15940,,,executed,{SRC},strong,2025 handelsvorderingen 40 15940 DROP was 19374; other recv 41 empty; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_beleg_2025,{ENT},2025,500028,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 500028 identiek; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_cash_2025,{ENT},2025,2256569,,,executed,{SRC},strong,2025 liquide middelen 54/58 2256569 DROP was 2957874; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_prepaid_2025,{ENT},2025,13289,,,executed,{SRC},strong,2025 overlopend actief 490/1 13289 DROP was 19148; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_equity_2025,{ENT},2025,3013849,,,executed,{SRC},strong,2025 eigen vermogen 10/15 3013849; fondsen 404909 + bestemde 330000 + overgedragen 2278940; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_fondsen_2025,{ENT},2025,404909,,,executed,{SRC},strong,2025 fondsen 10 404909 identiek; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_reserves_2025,{ENT},2025,330000,,,executed,{SRC},strong,2025 bestemde fondsen 13 330000 identiek (communicatie 80000 + sociaal passief 250000); tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_overgedragen_2025,{ENT},2025,2278940,,,executed,{SRC},strong,2025 overgedragen resultaat 14 2278940 DROP was 2289528; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_debt_2025,{ENT},2025,398828,,,executed,{SRC},strong,2025 schulden 17/49 398828 DROP was 501499; LT+ST+accrued holds; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_lt_2025,{ENT},2025,46100,,,executed,{SRC},strong,2025 LT 17 46100 DROP was 225691 (krediet 172/3); tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_st_2025,{ENT},2025,350747,,,executed,{SRC},strong,2025 ST 42/48 350747 JUMP was 270036; 42+44+45 holds; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_lt_current_2025,{ENT},2025,179591,,,executed,{SRC},strong,2025 LT binnen jaar 42 179591 UP was 172138; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_lev_2025,{ENT},2025,95590,,,executed,{SRC},strong,2025 handelsschulden 44 95590 JUMP was 28088; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_taxsoc_2025,{ENT},2025,75566,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 75566; tax 11917 + pers 63649; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_accrued_2025,{ENT},2025,1981,,,executed,{SRC},strong,2025 overlopend passief 492/3 1981 DROP was 5772; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_pers_2025,{ENT},2025,558980,,,executed,{SRC},strong,2025 bezoldigingen 62 558980 / 6.8 VTE UP was 514797 / 6.3; YE 7 / 10801 uur; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_afschr_2025,{ENT},2025,15669,,,executed,{SRC},strong,2025 afschrijvingen 630 15669 UP was 10676; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_othercosts_2025,{ENT},2025,3276,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 3276 DROP was 8435; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_66a_2025,{ENT},2025,17913,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 17913 UP was 7438; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_expl_2025,{ENT},2025,-6198,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -6198 LOSS was -14202; bruto-pers-afschr-other-66A holds; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_fin_2025,{ENT},2025,20488,,,executed,{SRC},strong,2025 financiele opbrengsten 75 20488 DROP was 90719; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_fincost_2025,{ENT},2025,18200,,,executed,{SRC},strong,2025 financiele kosten 65 18200 DROP was 25450; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_tax_2025,{ENT},2025,6678,,,executed,{SRC},strong,2025 belastingen 67/77 6678 DROP was 27354; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_pnl_2025,{ENT},2025,-10588,,,executed,{SRC},strong,2025 resultaat 9904/9905 -10588 LOSS was 23713 PROFIT; 9903 -3910; expl+fin-fincost-tax holds; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_commissaris_2025,{ENT},2025,6888,,,executed,{SRC},strong,2025 commissaris 6888 (Callens Vandelanotte NV / Filip Remmery); VKT no 95061 extra split; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_capex_2025,{ENT},2025,630430,,,executed,{SRC},strong,2025 IVA aanschaffingen 8029 34899 + MVA aanschaffingen 8169 595531 = 630430; tick1553; primary official NBB VKT-VZW",
    f"bud_vvp_opleiding_2025,{ENT},2025,186,,,executed,{SRC},strong,2025 formele opleiding nettokosten 186 (mannen 119 + vrouwen 67); tick1553; primary official NBB VKT-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +", len(rows), before, "->", after)

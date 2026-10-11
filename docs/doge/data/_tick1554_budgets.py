#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1554 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vleva"
SRC = "src_vleva_jr2025_nbb"

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
    f"bud_vleva_bruto_2025,{ENT},2025,1077899,,,executed,{SRC},strong,2025 brutomarge 9900 1077899 envelope (leftover public koepel VZW; VKT and omzet 70 empty; 73 empty); UP was 1047618; tick1554; primary official NBB VKT-VZW AV 26.03.2026",
    f"bud_vleva_assets_2025,{ENT},2025,433039,,,executed,{SRC},strong,2025 balanstotaal 20/58 433039 DROP was 557105; VA+vlottend 433040 official 1-euro; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_va_2025,{ENT},2025,262987,,,executed,{SRC},strong,2025 vaste activa 21/28 262987 DROP was 332333; IVA+MVA 262986 official 1-euro; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_iva_2025,{ENT},2025,23841,,,executed,{SRC},strong,2025 IVA 21 23841 DROP was 45765; aanschaffingen 8029 empty; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_mva_2025,{ENT},2025,239145,,,executed,{SRC},strong,2025 MVA 22/27 239145 DROP was 286569; overige 26 239145; meubilair 24 0; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_overige_mva_2025,{ENT},2025,239145,,,executed,{SRC},strong,2025 overige materiële vaste activa 26 239145 DROP was 286175; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_vlottend_2025,{ENT},2025,170053,,,executed,{SRC},strong,2025 vlottende 29/58 170053 DROP was 224772; recv+cash+prepaid holds; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_handelsrecv_2025,{ENT},2025,51587,,,executed,{SRC},strong,2025 handelsvorderingen 40 51587 DROP was 59612; other recv 41 680; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_cash_2025,{ENT},2025,104066,,,executed,{SRC},strong,2025 liquide middelen 54/58 104066 DROP was 133147; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_prepaid_2025,{ENT},2025,13720,,,executed,{SRC},strong,2025 overlopend actief 490/1 13720 DROP was 31338; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_equity_2025,{ENT},2025,230737,,,executed,{SRC},strong,2025 eigen vermogen 10/15 230737 DROP was 287026; reserves 141670 + overgedragen 89066 official 1-euro; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_reserves_2025,{ENT},2025,141670,,,executed,{SRC},strong,2025 bestemde fondsen 13 141670 identiek (sociaal passief 93130 + toekomstige projecten 48540); tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_overgedragen_2025,{ENT},2025,89066,,,executed,{SRC},strong,2025 overgedragen resultaat 14 89066 DROP was 145355; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_debt_2025,{ENT},2025,202302,,,executed,{SRC},strong,2025 schulden 17/49 202302 DROP was 270079; LT+ST+accrued official 1-euro; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_lt_2025,{ENT},2025,6016,,,executed,{SRC},strong,2025 LT 17 6016 DROP was 63545 (krediet 172/3); tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_st_2025,{ENT},2025,178651,,,executed,{SRC},strong,2025 ST 42/48 178651 DROP was 186831; 42+44+45 holds; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_lt_current_2025,{ENT},2025,57529,,,executed,{SRC},strong,2025 LT binnen jaar 42 57529 UP was 57327; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_lev_2025,{ENT},2025,20596,,,executed,{SRC},strong,2025 handelsschulden 44 20596 JUMP was 12722; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_taxsoc_2025,{ENT},2025,100526,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 100526; tax 3001 + pers 97524 official 1-euro; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_accrued_2025,{ENT},2025,17636,,,executed,{SRC},strong,2025 overlopend passief 492/3 17636 DROP was 19703; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_pers_2025,{ENT},2025,1021920,,,executed,{SRC},strong,2025 bezoldigingen 62 1021920 / 8.8 VTE DROP was 982307 / 9; YE 8 / 13748 uur; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_afschr_2025,{ENT},2025,69347,,,executed,{SRC},strong,2025 afschrijvingen 630 69347 DROP was 71785; IVA 21923 + MVA 47423 official 1-euro; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_othercosts_2025,{ENT},2025,41454,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 41454 UP was 37246; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_expl_2025,{ENT},2025,-54822,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -54822 LOSS was -43720; bruto-pers-afschr-other holds; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_fin_2025,{ENT},2025,568,,,executed,{SRC},strong,2025 financiele opbrengsten 75 568 DROP was 3870; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_fincost_2025,{ENT},2025,2036,,,executed,{SRC},strong,2025 financiele kosten 65 2036 DROP was 2238; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_pnl_2025,{ENT},2025,-56289,,,executed,{SRC},strong,2025 resultaat 9904/9905 -56289 LOSS was -42088; 9903 -56289; expl+fin-fincost official 1-euro; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_commissaris_2025,{ENT},2025,4160,,,executed,{SRC},strong,2025 commissaris 4160 (PKF Bofidi Audit BV / Jeroen Rans); VKT no 95061 extra split; tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_opleiding_2025,{ENT},2025,6656,,,executed,{SRC},strong,2025 formele opleiding nettokosten 6656 (vrouwen 6656 / 91 uur / 1 werknemer); tick1554; primary official NBB VKT-VZW",
    f"bud_vleva_huurwaarborg_2025,{ENT},2025,60170,,,executed,{SRC},strong,2025 huurwaarborg ten gunste van P&V 60170 (buitenbalans); tick1554; primary official NBB VKT-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +", len(rows), before, "->", after)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_ivrm"
SRC = "src_ivrm_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_ivrm_assets_2025,{ENT},2025,61398227,,,executed,{SRC},strong,2025 assets 61398227 UP (was 47925870); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_vaste_2025,{ENT},2025,38902941,,,executed,{SRC},strong,2025 vaste activa 21/28 38902941 UP (was 27212357); IVA 21 153501; FVA 28 610918; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_mva_2025,{ENT},2025,38138521,,,executed,{SRC},strong,2025 MVA 22/27 38138521 UP (was 26496272); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_gebouwen_2025,{ENT},2025,25121991,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 25121991 UP (was 16863533); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_install_2025,{ENT},2025,8171982,,,executed,{SRC},strong,2025 installaties 23 8171982 JUMP (was 4201829); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_meubilair_2025,{ENT},2025,4259628,,,executed,{SRC},strong,2025 meubilair 24 4259628 UP (was 2909951); leasing 25 empty; overige 26 8601; in aanbouw 27 576319 DROP was 2512359; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_inaanbouw_2025,{ENT},2025,576319,,,executed,{SRC},strong,2025 in aanbouw 27 576319 DROP (was 2512359; 8181 overboeking 2512359 naar gebouwen); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_fva_2025,{ENT},2025,610918,,,executed,{SRC},strong,2025 FVA 28 610918 (deelnemingen 282 602430 + andere 8488); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_current_2025,{ENT},2025,22495287,,,executed,{SRC},strong,2025 vlottende 29/58 22495287 UP (was 20713513); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_ltrecv_2025,{ENT},2025,550390,,,executed,{SRC},strong,2025 LT vorderingen 29 550390 DROP (all other 291; was 687988); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_strecv_2025,{ENT},2025,9747397,,,executed,{SRC},strong,2025 ST vorderingen 40/41 9747397 (trade 7332306 + other 2415092); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_handelsrecv_2025,{ENT},2025,7332306,,,executed,{SRC},strong,2025 handelsvorderingen 40 7332306 JUMP (was 5853702); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_otherrecv_2025,{ENT},2025,2415092,,,executed,{SRC},strong,2025 overige ST 41 2415092 UP (was 2232811); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_cash_2025,{ENT},2025,8106299,,,executed,{SRC},strong,2025 liquide middelen 54/58 8106299 JUMP (was 7258486); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_beleg_2025,{ENT},2025,4023373,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 4023373 DROP (was 4559411); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_prepaid_2025,{ENT},2025,20964,,,executed,{SRC},strong,2025 overlopende 490/1 20964 UP (was 15570); voorraden 46863; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_equity_2025,{ENT},2025,18801904,,,executed,{SRC},strong,2025 eigen vermogen 10/15 18801904 DROP (was 21115637); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_reserves_2025,{ENT},2025,18015627,,,executed,{SRC},strong,2025 reserves 13 18015627 DROP (was 20256772 via 792 2241145); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_kapsubs_2025,{ENT},2025,146140,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 146140 DROP (was 218729); inbreng 640137; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_prov_2025,{ENT},2025,5361070,,,executed,{SRC},strong,2025 voorzieningen 16 5361070 UP (was 4441936; milieu 4351130 JUMP was 3370094; pens 759245); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_debt_2025,{ENT},2025,37235254,,,executed,{SRC},strong,2025 schulden 17/49 37235254 JUMP (was 22368297); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_ltdebt_2025,{ENT},2025,18694875,,,executed,{SRC},strong,2025 LT schulden 17 18694875 JUMP (krediet 173 18680625 was 7025000); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_stdebt_2025,{ENT},2025,17972491,,,executed,{SRC},strong,2025 ST schulden 42/48 17972491 UP (was 14627144; current portion 2613500 / lev 7455656 / taxsoc 3249731 / other 4653605); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_lev_2025,{ENT},2025,7455656,,,executed,{SRC},strong,2025 leveranciers 440/4 7455656 UP (was 6988091); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_taxsoc_2025,{ENT},2025,3249731,,,executed,{SRC},strong,2025 tax/soc 45 3249731 (tax 479934 + bezold 2769796); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_otherst_2025,{ENT},2025,4653605,,,executed,{SRC},strong,2025 overige ST 47/48 4653605 JUMP (was 3021569); overlopend 492/3 567888; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_opbr_2025,{ENT},2025,35143041,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 35143041 UP (was 31165563); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_omzet_2025,{ENT},2025,34824643,,,executed,{SRC},strong,2025 omzet 70 34824643 UP (was 30759960); annual envelope; 73 empty VOL-inb; 740 empty; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_andere74_2025,{ENT},2025,318397,,,executed,{SRC},strong,2025 andere 74 318397 (was 405603); nrec 76A 0; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_diensten_2025,{ENT},2025,17687984,,,executed,{SRC},strong,2025 diensten 61 17687984 JUMP (was 14804898); handelsgoederen 60 196668; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_pers_2025,{ENT},2025,12430050,,,executed,{SRC},strong,2025 pers 62 12430050 / 165.8 VTE (was 11473543 / 159.5); YE 204 / 171.8 VTE / 235717 uur; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_afschr_2025,{ENT},2025,4676553,,,executed,{SRC},strong,2025 afschrijvingen 630 4676553 JUMP (was 3057678); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_expl_2025,{ENT},2025,-2080142,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -2080142 LOSS (was +842958); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_finopbr_2025,{ENT},2025,148231,,,executed,{SRC},strong,2025 financiele opbrengsten 75 148231 (was 173325); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_finkost_2025,{ENT},2025,284831,,,executed,{SRC},strong,2025 financiele kosten 65 284831 (schulden 283609); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_pnl_2025,{ENT},2025,-2241145,,,executed,{SRC},strong,2025 winst 9904 -2241145 LOSS (was +782442); tax 67/77 24403; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (uit te keren winst empty); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_capex_2025,{ENT},2025,16367406,,,executed,{SRC},strong,2025 capex IVA 8022 151579 + MVA 8161 7995044 + 8162 5312366 + 8163 2332098 + 8166 576319 = 16367406; tick1524; primary official NBB WVV VOL-inb 2026-00373329",
    f"bud_ivrm_bestuurders_2025,{ENT},2025,84954,,,executed,{SRC},strong,2025 bestuurders 9503 84954; commissaris fee unpublished (6.18 not filed); tick1524; primary official NBB WVV VOL-inb 2026-00373329",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwcw"
SRC = "src_cwcw_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwcw_assets_2025,{ENT},2025,8483960,,,executed,{SRC},strong,2025 assets 8483960 UP (was 7416471); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_vaste_2025,{ENT},2025,5020480,,,executed,{SRC},strong,2025 vaste activa 21/28 5020480 JUMP (was 3147068); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_mva_2025,{ENT},2025,4990589,,,executed,{SRC},strong,2025 MVA 22/27 4990589 JUMP (was 3098529); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_gebouwen_2025,{ENT},2025,2536378,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 2536378 DROP (was 2691128); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_install_2025,{ENT},2025,45254,,,executed,{SRC},strong,2025 installaties 23 45254 DROP (was 46619); meubilair 24 39757 DROP (was 70573); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_inb_2025,{ENT},2025,2369201,,,executed,{SRC},strong,2025 in aanbouw 27 2369201 JUMP (was 290209; aanschaffingen 8166 2078992); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_iva_2025,{ENT},2025,18696,,,executed,{SRC},strong,2025 IVA 21 18696 DROP (was 37391; aanschaffingen 8022 empty; afschr 8072 18695); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_fva_2025,{ENT},2025,11194,,,executed,{SRC},strong,2025 FVA 28 11194 (aandelen 284 50 + borg 285/8 11144); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_current_2025,{ENT},2025,3463480,,,executed,{SRC},strong,2025 vlottende 29/58 3463480 DROP (was 4269403); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_strecv_2025,{ENT},2025,1327314,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1327314 JUMP (was 1063295); LT recv 29 empty; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_handelsrecv_2025,{ENT},2025,83032,,,executed,{SRC},strong,2025 handelsvorderingen 40 83032 DROP (was 92788); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_otherrecv_2025,{ENT},2025,1244282,,,executed,{SRC},strong,2025 overige ST 41 1244282 JUMP (was 970506); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_beleg_2025,{ENT},2025,1173271,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1173271 DROP (was 2336418; 51 353374 + 52 819897 + 53 termijn 0 DROP was 1165000); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_cash_2025,{ENT},2025,901859,,,executed,{SRC},strong,2025 liquide middelen 54/58 901859 UP (was 831056); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_prepaid_2025,{ENT},2025,61035,,,executed,{SRC},strong,2025 overlopende 490/1 61035 JUMP (was 38635; 6.6 over te dragen 14853 + verkregen 46183); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_equity_2025,{ENT},2025,5379782,,,executed,{SRC},strong,2025 eigen vermogen 10/15 5379782 UP (was 4355826); fondsen 10 1590791; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_bestemde_2025,{ENT},2025,1964713,,,executed,{SRC},strong,2025 bestemde fondsen 13 1964713 DROP (was 2093052); overgedragen 14 -263318; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_kapsubs_2025,{ENT},2025,2087596,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 2087596 JUMP (was 964102); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_voorzieningen_2025,{ENT},2025,101824,,,executed,{SRC},strong,2025 voorzieningen 16 101824 DROP (was 298343; 162 herstelling 101824); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_debt_2025,{ENT},2025,3002354,,,executed,{SRC},strong,2025 schulden 17/49 3002354 UP (was 2762302); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_ltdebt_2025,{ENT},2025,194494,,,executed,{SRC},strong,2025 LT schulden 17 194494 DROP (bank 173 179494 + overige 174 15000); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_stdebt_2025,{ENT},2025,2575840,,,executed,{SRC},strong,2025 ST schulden 42/48 2575840 JUMP (was 1698849; current 42388 / lev 1233306 / taxsoc 1231037 / other 69110); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_lev_2025,{ENT},2025,1233306,,,executed,{SRC},strong,2025 leveranciers 440/4 1233306 JUMP (was 431918); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_taxsoc_2025,{ENT},2025,1231037,,,executed,{SRC},strong,2025 tax/soc 45 1231037 UP (tax 76352 + bezold 1154685 was 1170131); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_otherst_2025,{ENT},2025,69110,,,executed,{SRC},strong,2025 overige ST 48 69110 UP (was 55253); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_accrued_2025,{ENT},2025,232020,,,executed,{SRC},strong,2025 overlopend 492/3 232020 DROP (was 826571; 6.8 toe te kennen 22620 + over te dragen projectsubsidies 209400); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_opbr_2025,{ENT},2025,9188129,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 9188129 UP (was 8865863); annual envelope; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_omzet_2025,{ENT},2025,187872,,,executed,{SRC},strong,2025 omzet 70 187872 UP (was 185150); 6.9 category split empty; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_subs_2025,{ENT},2025,8739673,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 8739673 UP (731 19764 + 733 8719910; 730 empty 732 empty); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_subs733_2025,{ENT},2025,8719910,,,executed,{SRC},strong,2025 subsidies 733 8719910 UP (was 8019160); city vs Departement Zorg split unpublished; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_andere74_2025,{ENT},2025,104071,,,executed,{SRC},strong,2025 andere 74 104071 DROP (was 633721); nrec 76A 156513 JUMP (7620 154131 + 7630 1111 + 764/8 1271); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_diensten_2025,{ENT},2025,909889,,,executed,{SRC},strong,2025 diensten 61 909889 DROP (was 995001); handelsgoederen 60 58628; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_pers_2025,{ENT},2025,7318691,,,executed,{SRC},strong,2025 pers 62 7318691 / 108.9 VTE UP (was 7079729 / 108.5; YE 125 was 132 / 144333 uur); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_afschr_2025,{ENT},2025,226605,,,executed,{SRC},strong,2025 afschrijvingen 630 226605 (was 230566); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_nrec76a_2025,{ENT},2025,156513,,,executed,{SRC},strong,2025 nrec 76A 156513 JUMP (was 10246; 7620 154131 + 7630 1111 + 764/8 1271); 66A empty was 144520; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_expl_2025,{ENT},2025,-151354,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -151354 LOSS (was -510209); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_finopbr_2025,{ENT},2025,66083,,,executed,{SRC},strong,2025 financiele opbrengsten 75/76B 66083 DROP (was 104521; vlottend 751 60597); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_finkost_2025,{ENT},2025,2114,,,executed,{SRC},strong,2025 financiele kosten 65/66B 2114 (schulden 650 3952 + wv -11856 + andere 10018); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_pnl_2025,{ENT},2025,-99538,,,executed,{SRC},strong,2025 verlies 9904 -99538 LOSS (was -438424); tax 67/77 12153; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; 691 empty; 791 128339 onttrekking; overgedragen 14 -263318); tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_capex_2025,{ENT},2025,2099971,,,executed,{SRC},strong,2025 capex IVA 8022 0 + MVA 8161 5583 + 8162 5939 + 8163 9457 + 8166 2078992 = 2099971; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
    f"bud_cwcw_commissaris_2025,{ENT},2025,6732,,,executed,{SRC},strong,2025 commissaris 9505 6732; Callens Vandelanotte NV B00083 via Rysman Francis A01523; tick1533; primary official NBB WVV VOL-VZW 2026-00088320",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

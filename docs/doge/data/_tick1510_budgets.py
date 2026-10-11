#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgzo"
SRC = "src_cgzo_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgzo_assets_2025,{ENT},2025,6678603,,,executed,{SRC},strong,2025 assets 6678603 UP (was 6338518); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_vaste_2025,{ENT},2025,3134719,,,executed,{SRC},strong,2025 vaste activa 21/28 3134719 DROP (was 3278187); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_mva_2025,{ENT},2025,3129037,,,executed,{SRC},strong,2025 MVA 22/27 3129037 DROP (was 3272505); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_gebouwen_2025,{ENT},2025,2553611,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 2553611 (was 2666943); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_meubilair_2025,{ENT},2025,54582,,,executed,{SRC},strong,2025 meubilair 24 54582 (was 59617); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_leasing_2025,{ENT},2025,520844,,,executed,{SRC},strong,2025 leasing 25 520844 (was 545945); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_fva_2025,{ENT},2025,5682,,,executed,{SRC},strong,2025 FVA 28 5682 stable; in aanbouw 27 empty; tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_current_2025,{ENT},2025,3543884,,,executed,{SRC},strong,2025 vlottende 29/58 3543884 UP (was 3060331); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_strecv_2025,{ENT},2025,557913,,,executed,{SRC},strong,2025 ST vorderingen 40/41 557913 (trade 27490 + other 530423); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_beleggingen_2025,{ENT},2025,2375000,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 2375000 JUMP (was 1908480; all termijn 53); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_cash_2025,{ENT},2025,139180,,,executed,{SRC},strong,2025 liquide middelen 54/58 139180 JUMP (was 43482); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_prepaid_2025,{ENT},2025,471791,,,executed,{SRC},strong,2025 overlopend actief 490/1 471791 (was 575710; radar/karus 358706); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_equity_2025,{ENT},2025,5076165,,,executed,{SRC},strong,2025 eigen vermogen 10/15 5076165 UP (was 4982496); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_fondsen_2025,{ENT},2025,152070,,,executed,{SRC},strong,2025 fondsen 10 152070 (was 152071); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_bestemde_2025,{ENT},2025,3774306,,,executed,{SRC},strong,2025 bestemde fondsen 13 3774306 (was 3705905; toevoeging 98900); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_overgedragen_2025,{ENT},2025,168375,,,executed,{SRC},strong,2025 overgedragen winst 14 168375 (was 96372); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_kapsubs_2025,{ENT},2025,981414,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 981414 (was 1028148); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_voorz_2025,{ENT},2025,181752,,,executed,{SRC},strong,2025 voorzieningen 16 181752 JUMP (was 6672; toevoeging 175080); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_debt_2025,{ENT},2025,1420686,,,executed,{SRC},strong,2025 schulden 17/49 1420686 UP (was 1349350); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_ltdebt_2025,{ENT},2025,475000,,,executed,{SRC},strong,2025 LT schulden 17 475000 (all lease 172; was 500000); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_stdebt_2025,{ENT},2025,945686,,,executed,{SRC},strong,2025 ST schulden 42/48 945686 (was 849350); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_lev_2025,{ENT},2025,137246,,,executed,{SRC},strong,2025 leveranciers 440/4 137246 UP (was 85407); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_taxsoc_2025,{ENT},2025,783440,,,executed,{SRC},strong,2025 bezold 454/9 783440 (tax 450 empty); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_opbr_2025,{ENT},2025,7623192,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 7623192; annual envelope; tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_omzet_2025,{ENT},2025,112615,,,executed,{SRC},strong,2025 omzet 70 112615 UP (was 84380); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_lidgeld_2025,{ENT},2025,5295335,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 5295335 UP (was 5133020; all 733 subsidies); CGG-dotatie; tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_andere_opbr_2025,{ENT},2025,2043630,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 2043630 JUMP (was 1753075); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_nrec_2025,{ENT},2025,171612,,,executed,{SRC},strong,2025 nrec 76A 171612 (was empty; all 764/8); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_pers_2025,{ENT},2025,6091984,,,executed,{SRC},strong,2025 pers 62 6091984 / 65.8 VTE (was 5865633 / 62.7); YE 94; 89370 uur; tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_diensten_2025,{ENT},2025,1018389,,,executed,{SRC},strong,2025 diensten 61 1018389 JUMP (was 746207); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_aankopen_2025,{ENT},2025,5853,,,executed,{SRC},strong,2025 aankopen 60 5853 (was 4826); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_afschr_2025,{ENT},2025,178304,,,executed,{SRC},strong,2025 afschrijvingen 630 178304 (was 185200); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_voorz_kost_2025,{ENT},2025,175080,,,executed,{SRC},strong,2025 voorzieningen kost 635/9 175080 (was -100141); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_andere_2025,{ENT},2025,33146,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 33146 (was 37297); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_nrec_kost_2025,{ENT},2025,16257,,,executed,{SRC},strong,2025 nrec kosten 66A 16257 (was 39667); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_bedrijfskost_2025,{ENT},2025,7519013,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 7519013 (was 6778689); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_expl_2025,{ENT},2025,104179,,,executed,{SRC},strong,2025 bedrijfswinst 9901 104179 (was 191786); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_finopbr_2025,{ENT},2025,36962,,,executed,{SRC},strong,2025 financiele opbrengsten 75 36962 DROP (was 52324); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_finkost_2025,{ENT},2025,737,,,executed,{SRC},strong,2025 financiele kosten 65 737 (was 1099); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_tax_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 belastingen 67/77 0; tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_pnl_2025,{ENT},2025,140404,,,executed,{SRC},strong,2025 winst 9904 140404 (was 243011); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_capex_2025,{ENT},2025,34836,,,executed,{SRC},strong,2025 capex 8163 34836 (8161+8162+8164+8165 empty); tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
    f"bud_cgzo_commissaris_2025,{ENT},2025,9141,,,executed,{SRC},strong,2025 commissaris Callens Vandelanotte nv B00083 fee 9141; tick1510; primary official NBB WVV VOL-VZW 2026-00195156",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

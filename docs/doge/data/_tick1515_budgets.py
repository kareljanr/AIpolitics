#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgin"
SRC = "src_cgin_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgin_assets_2025,{ENT},2025,14975892,,,executed,{SRC},strong,2025 assets 14975892 UP (was 13594638); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_vaste_2025,{ENT},2025,6168764,,,executed,{SRC},strong,2025 vaste activa 21/28 6168764 UP (was 5080471); IVA 21 9173; FVA 28 11835; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_mva_2025,{ENT},2025,6147755,,,executed,{SRC},strong,2025 MVA 22/27 6147755 UP (was 5068650); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_gebouwen_2025,{ENT},2025,4263475,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 4263475 (was 4503131); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_install_2025,{ENT},2025,263554,,,executed,{SRC},strong,2025 installaties 23 263554 (was 169325); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_meubilair_2025,{ENT},2025,24093,,,executed,{SRC},strong,2025 meubilair 24 24093 (was 19116); leasing 25 empty; overige 26 empty; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_inb_2025,{ENT},2025,1596634,,,executed,{SRC},strong,2025 in aanbouw 27 1596634 JUMP (was 377078); 8166 aanschaffingen 1219555; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_current_2025,{ENT},2025,8807128,,,executed,{SRC},strong,2025 vlottende 29/58 8807128 (was 8514166); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_strecv_2025,{ENT},2025,4245815,,,executed,{SRC},strong,2025 ST vorderingen 40/41 4245815 (trade 2497765 DROP was 2624853 / other 1748051 JUMP was 1238981); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_beleg_2025,{ENT},2025,569006,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 569006 stable; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_cash_2025,{ENT},2025,3698941,,,executed,{SRC},strong,2025 liquide middelen 54/58 3698941 DROP (was 3818647); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_prepaid_2025,{ENT},2025,293365,,,executed,{SRC},strong,2025 overlopend actief 490/1 293365 (was 262679); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_equity_2025,{ENT},2025,9584897,,,executed,{SRC},strong,2025 eigen vermogen 10/15 9584897 UP (was 8652655); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_fondsen_2025,{ENT},2025,369246,,,executed,{SRC},strong,2025 fondsen 10 369246 stable; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_bestemde_2025,{ENT},2025,3536898,,,executed,{SRC},strong,2025 bestemde fondsen 13 3536898 (was 3436898; toevoeging 691 100000); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_overgedragen_2025,{ENT},2025,3457061,,,executed,{SRC},strong,2025 overgedragen winst 14 3457061 (was 3454355); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_kapsubs_2025,{ENT},2025,2221692,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 2221692 JUMP (was 1392156); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_voorz_2025,{ENT},2025,538111,,,executed,{SRC},strong,2025 voorzieningen 16 538111 (was 546690; all 164/5); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_debt_2025,{ENT},2025,4852883,,,executed,{SRC},strong,2025 schulden 17/49 4852883 UP (was 4395293); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_ltdebt_2025,{ENT},2025,1620167,,,executed,{SRC},strong,2025 LT schulden 17 1620167 (krediet 173 1616506; was 1729087); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_stdebt_2025,{ENT},2025,2843834,,,executed,{SRC},strong,2025 ST schulden 42/48 2843834 (was 2234569; 42 140698 / lev 821474 / taxsoc 1798134 / other 83528); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_lev_2025,{ENT},2025,821474,,,executed,{SRC},strong,2025 leveranciers 440/4 821474 JUMP (was 331047); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_taxsoc_2025,{ENT},2025,1798134,,,executed,{SRC},strong,2025 tax/soc 45 1798134 (tax 26950 + bezold 1771184); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_otherst_2025,{ENT},2025,83528,,,executed,{SRC},strong,2025 overige ST 48 83528 DROP (was 502048); overlopend passiva 492/3 388882; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_opbr_2025,{ENT},2025,19622796,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 19622796; annual envelope; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_omzet_2025,{ENT},2025,3978611,,,executed,{SRC},strong,2025 omzet 70 3978611 UP (was 3826570); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_lidgeld_2025,{ENT},2025,9254873,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 9254873 UP (was 8808800; 730-733 empty); CGG-dotatie; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_andere_opbr_2025,{ENT},2025,6200155,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 6200155 (was 5766631); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_nrec_2025,{ENT},2025,189157,,,executed,{SRC},strong,2025 nrec 76A 189157 DROP (was 441179; all 764/8 andere); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_pers_2025,{ENT},2025,16532661,,,executed,{SRC},strong,2025 pers 62 16532661 / 191.5 VTE (was 15485798 / 181.7); YE 277 / YE VTE 191.5; 277642 uur; andere 623 1163913 JUMP was 23432; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_diensten_2025,{ENT},2025,2141016,,,executed,{SRC},strong,2025 diensten 61 2141016 JUMP (was 1703047); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_afschr_2025,{ENT},2025,307893,,,executed,{SRC},strong,2025 afschrijvingen 630 307893 (was 301163); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_andere_2025,{ENT},2025,345264,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 345264 (was 291084); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_bedrijfskost_2025,{ENT},2025,19457815,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 19457815 (was 18298238); nrec 66A 76906; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_expl_2025,{ENT},2025,164981,,,executed,{SRC},strong,2025 bedrijfswinst 9901 164981 (was 544942); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_finopbr_2025,{ENT},2025,20775,,,executed,{SRC},strong,2025 financiele opbrengsten 75 20775 (was 30939); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_finkost_2025,{ENT},2025,76820,,,executed,{SRC},strong,2025 financiele kosten 65 76820 (was 69097; schulden 650 71727); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_tax_2025,{ENT},2025,6231,,,executed,{SRC},strong,2025 belastingen 67/77 6231 (was 9017); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_pnl_2025,{ENT},2025,102706,,,executed,{SRC},strong,2025 winst 9904 102706 DROP (was 497767); tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_capex_2025,{ENT},2025,167392,,,executed,{SRC},strong,2025 capex 8161+8162+8163 167392 (14884+142834+9674); 8166 in aanbouw 1219555; IVA 8022 9224; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
    f"bud_cgin_commissaris_2025,{ENT},2025,13790,,,executed,{SRC},strong,2025 commissaris FINVISION B00829 fee 13790; tick1515; primary official NBB WVV VOL-VZW 2026-00205082",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

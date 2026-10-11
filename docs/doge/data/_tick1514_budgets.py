#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgpt"
SRC = "src_cgpt_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgpt_assets_2025,{ENT},2025,7371989,,,executed,{SRC},strong,2025 assets 7371989 DROP (was 7859621); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_vaste_2025,{ENT},2025,3690215,,,executed,{SRC},strong,2025 vaste activa 21/28 3690215 DROP (was 3814037); IVA 21 empty; FVA 28 empty; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_mva_2025,{ENT},2025,3690215,,,executed,{SRC},strong,2025 MVA 22/27 3690215 DROP (was 3814037); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_gebouwen_2025,{ENT},2025,3492073,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 3492073 (was 3672560); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_install_2025,{ENT},2025,144935,,,executed,{SRC},strong,2025 installaties 23 144935 (was 121854); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_meubilair_2025,{ENT},2025,53207,,,executed,{SRC},strong,2025 meubilair 24 53207 UP (was 19623); leasing 25 empty; overige 26 empty; in aanbouw 27 empty; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_current_2025,{ENT},2025,3681774,,,executed,{SRC},strong,2025 vlottende 29/58 3681774 DROP (was 4045584); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_ltrecv_2025,{ENT},2025,10350,,,executed,{SRC},strong,2025 LT vorderingen 29 10350 (was 13050; all other 291); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_strecv_2025,{ENT},2025,1529229,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1529229 (trade 136175 + other 1393054 DROP was 1513523); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_beleg_2025,{ENT},2025,1170000,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1170000 DROP (was 1800000; all termijn 53); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_cash_2025,{ENT},2025,955481,,,executed,{SRC},strong,2025 liquide middelen 54/58 955481 JUMP (was 596423); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_prepaid_2025,{ENT},2025,16714,,,executed,{SRC},strong,2025 overlopend actief 490/1 16714 (was 1527); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_equity_2025,{ENT},2025,4737871,,,executed,{SRC},strong,2025 eigen vermogen 10/15 4737871 DROP (was 4907330); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_fondsen_2025,{ENT},2025,75370,,,executed,{SRC},strong,2025 fondsen 10 75370 stable; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_bestemde_2025,{ENT},2025,2876174,,,executed,{SRC},strong,2025 bestemde fondsen 13 2876174 JUMP (was 2121529; toevoeging 691 826052; onttrekking 791 71407; sociaal passief max 25 pct loonkosten); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_overgedragen_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 overgedragen winst 14 0 (was 816526; transferred into bestemde); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_kapsubs_2025,{ENT},2025,1786327,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 1786327 (was 1893905); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_debt_2025,{ENT},2025,2634118,,,executed,{SRC},strong,2025 schulden 17/49 2634118 DROP (was 2952291); voorzieningen 16 empty; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_ltdebt_2025,{ENT},2025,548026,,,executed,{SRC},strong,2025 LT schulden 17 548026 (all krediet 173; was 623514); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_stdebt_2025,{ENT},2025,1892500,,,executed,{SRC},strong,2025 ST schulden 42/48 1892500 (was 1898335; 42 75489 / lev 210782 / taxsoc 1575939 / other 30291); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_lev_2025,{ENT},2025,210782,,,executed,{SRC},strong,2025 leveranciers 440/4 210782 DROP (was 281491); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_taxsoc_2025,{ENT},2025,1575939,,,executed,{SRC},strong,2025 tax/soc 45 1575939 (tax 290023 + bezold 1285916); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_otherst_2025,{ENT},2025,30291,,,executed,{SRC},strong,2025 overige ST 48 30291 DROP (was 73325); overlopend passiva 492/3 193592 DROP (was 430442); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_opbr_2025,{ENT},2025,10287468,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 10287468; annual envelope; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_omzet_2025,{ENT},2025,485306,,,executed,{SRC},strong,2025 omzet 70 485306 UP (was 441727); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_lidgeld_2025,{ENT},2025,9488056,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 9488056 UP (was 8958156; all 733 subsidies); CGG-dotatie; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_andere_opbr_2025,{ENT},2025,180272,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 180272 (was 164683); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_nrec_2025,{ENT},2025,133835,,,executed,{SRC},strong,2025 nrec 76A 133835 JUMP (was 586; all 764/8 andere); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_pers_2025,{ENT},2025,9380342,,,executed,{SRC},strong,2025 pers 62 9380342 / 103.3 VTE (was 8368717 / 97); YE 141 / YE VTE 103.3; 144793 uur; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_diensten_2025,{ENT},2025,680994,,,executed,{SRC},strong,2025 diensten 61 680994 (was 617888); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_afschr_2025,{ENT},2025,254075,,,executed,{SRC},strong,2025 afschrijvingen 630 254075 (was 326913); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_andere_2025,{ENT},2025,29481,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 29481 (was 31951); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_bedrijfskost_2025,{ENT},2025,10344892,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 10344892 (was 9349417); nrec 66A 0 (was 3949); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_expl_2025,{ENT},2025,-57424,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -57424 (was +215734); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_finopbr_2025,{ENT},2025,29486,,,executed,{SRC},strong,2025 financiele opbrengsten 75 29486 (was 62459); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_finkost_2025,{ENT},2025,25190,,,executed,{SRC},strong,2025 financiele kosten 65 25190 (was 27956; schulden 650 25013); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_tax_2025,{ENT},2025,8753,,,executed,{SRC},strong,2025 belastingen 67/77 8753 (was empty); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_pnl_2025,{ENT},2025,-61881,,,executed,{SRC},strong,2025 verlies 9904 -61881 LOSS (was +250237); tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_capex_2025,{ENT},2025,130253,,,executed,{SRC},strong,2025 capex 8161+8162+8163 130253 (15875+71688+42690); 8164+8165 empty; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
    f"bud_cgpt_commissaris_2025,{ENT},2025,10467,,,executed,{SRC},strong,2025 commissaris Callens Vandelanotte B00003 fee 10467; tick1514; primary official NBB WVV VOL-VZW 2026-00167849",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

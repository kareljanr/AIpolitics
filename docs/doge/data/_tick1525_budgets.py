#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwan"
SRC = "src_cwan_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwan_assets_2025,{ENT},2025,16778368,,,executed,{SRC},strong,2025 assets 16778368 DROP (was 18317039); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_opricht_2025,{ENT},2025,233043,,,executed,{SRC},strong,2025 oprichtingskosten 20 233043 DROP (was 309087; herstruct 204); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_vaste_2025,{ENT},2025,12607380,,,executed,{SRC},strong,2025 vaste activa 21/28 12607380 UP (was 12104180); IVA 21 191535; FVA 28 18789; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_mva_2025,{ENT},2025,12397056,,,executed,{SRC},strong,2025 MVA 22/27 12397056 UP (was 11886722); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_gebouwen_2025,{ENT},2025,8412046,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 8412046 DROP (was 8763963); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_install_2025,{ENT},2025,1014291,,,executed,{SRC},strong,2025 installaties 23 1014291 UP (was 844346); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_meubilair_2025,{ENT},2025,655701,,,executed,{SRC},strong,2025 meubilair 24 655701 (was 656072); leasing 25 empty; overige 26 999976; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_inaanbouw_2025,{ENT},2025,1315042,,,executed,{SRC},strong,2025 in aanbouw 27 1315042 JUMP (was 589953); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_fva_2025,{ENT},2025,18789,,,executed,{SRC},strong,2025 FVA 28 18789 (aandelen 284 7008 + borg 285/8 11781); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_current_2025,{ENT},2025,3937945,,,executed,{SRC},strong,2025 vlottende 29/58 3937945 DROP (was 5903772); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_ltrecv_2025,{ENT},2025,88126,,,executed,{SRC},strong,2025 LT vorderingen 29 88126 DROP (all other 291; was 388126); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_strecv_2025,{ENT},2025,2627941,,,executed,{SRC},strong,2025 ST vorderingen 40/41 2627941 (trade 1386339 + other 1241602); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_handelsrecv_2025,{ENT},2025,1386339,,,executed,{SRC},strong,2025 handelsvorderingen 40 1386339 JUMP (was 909801); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_otherrecv_2025,{ENT},2025,1241602,,,executed,{SRC},strong,2025 overige ST 41 1241602 UP (was 1212200); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_cash_2025,{ENT},2025,1004443,,,executed,{SRC},strong,2025 liquide middelen 54/58 1004443 DROP (was 3170609); beleg 50/53 empty; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_prepaid_2025,{ENT},2025,189003,,,executed,{SRC},strong,2025 overlopende 490/1 189003 (was 194078); voorraden 28432; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_equity_2025,{ENT},2025,6183712,,,executed,{SRC},strong,2025 eigen vermogen 10/15 6183712 DROP (was 6584257); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_fondsen_2025,{ENT},2025,352246,,,executed,{SRC},strong,2025 fondsen 10 352246 stable; bestemde 13 703252 stable; overgedragen 14 1908759; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_kapsubs_2025,{ENT},2025,3219455,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 3219455 DROP (was 3543104); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_debt_2025,{ENT},2025,10594656,,,executed,{SRC},strong,2025 schulden 17/49 10594656 DROP (was 11732782); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_ltdebt_2025,{ENT},2025,2444483,,,executed,{SRC},strong,2025 LT schulden 17 2444483 DROP (krediet 173 2444483 was 2656444); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_stdebt_2025,{ENT},2025,7702525,,,executed,{SRC},strong,2025 ST schulden 42/48 7702525 DROP (was 8157894; current portion 211961 / lev 1334370 / taxsoc 5868970 / other 287224); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_lev_2025,{ENT},2025,1334370,,,executed,{SRC},strong,2025 leveranciers 440/4 1334370 UP (was 1294729); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_taxsoc_2025,{ENT},2025,5868970,,,executed,{SRC},strong,2025 tax/soc 45 5868970 JUMP (tax 135173 + bezold 5733797 was 5568438); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_otherst_2025,{ENT},2025,287224,,,executed,{SRC},strong,2025 overige ST 48 287224 DROP (was 1085099); overlopend 492/3 447647; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_opbr_2025,{ENT},2025,52460317,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 52460317 UP (was 49262909); annual envelope; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_omzet_2025,{ENT},2025,3691060,,,executed,{SRC},strong,2025 omzet 70 3691060 UP (was 2904711); 6.9 category/geo empty; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_prodva_2025,{ENT},2025,689591,,,executed,{SRC},strong,2025 geproduceerde VA 72 689591 JUMP (was 267934); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_subs_2025,{ENT},2025,47451115,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 47451115 UP (733 47054006 + 731 57420); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_subs733_2025,{ENT},2025,47054006,,,executed,{SRC},strong,2025 subsidies 733 47054006 UP (was 45552036); schenkingen 731 57420; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_andere74_2025,{ENT},2025,449175,,,executed,{SRC},strong,2025 andere 74 449175 JUMP (was 193238); nrec 76A 179376; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_diensten_2025,{ENT},2025,6708907,,,executed,{SRC},strong,2025 diensten 61 6708907 JUMP (was 4883932); handelsgoederen 60 1014476; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_pers_2025,{ENT},2025,43212061,,,executed,{SRC},strong,2025 pers 62 43212061 / 596.7 VTE (was 41977306 / 592.1); YE 742 / 829830 uur; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_afschr_2025,{ENT},2025,1245627,,,executed,{SRC},strong,2025 afschrijvingen 630 1245627 UP (was 1109083); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_expl_2025,{ENT},2025,-209028,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -209028 LOSS (was +269036); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_finopbr_2025,{ENT},2025,172160,,,executed,{SRC},strong,2025 financiele opbrengsten 75 172160 (was 207114); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_finkost_2025,{ENT},2025,90362,,,executed,{SRC},strong,2025 financiele kosten 65 90362 (schulden 80172); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_nrec_2025,{ENT},2025,133083,,,executed,{SRC},strong,2025 nrec 66A 133083 JUMP (was 40); 76A 179376; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_pnl_2025,{ENT},2025,-76893,,,executed,{SRC},strong,2025 winst 9904 -76893 LOSS (was +323385); tax 67/77 -50338; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; uit te keren winst empty); tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_capex_2025,{ENT},2025,1704942,,,executed,{SRC},strong,2025 capex IVA 8022 0 + MVA 8161 empty + 8162 210540 + 8163 97653 + 8165 47999 + 8166 1348750 = 1704942; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
    f"bud_cwan_commissaris_2025,{ENT},2025,17768,,,executed,{SRC},strong,2025 commissaris 9505 17768; tick1525; primary official NBB WVV VOL-VZW 2026-00112717",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

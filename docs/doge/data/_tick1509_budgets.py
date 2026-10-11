#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgvb"
SRC = "src_cgvb_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgvb_assets_2025,{ENT},2025,9329271,,,executed,{SRC},strong,2025 assets 9329271 DROP (was 9433286); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_vaste_2025,{ENT},2025,4060939,,,executed,{SRC},strong,2025 vaste activa 21/28 4060939 DROP (was 4191303); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_mva_2025,{ENT},2025,4029371,,,executed,{SRC},strong,2025 MVA 22/27 4029371 DROP (was 4161187); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_gebouwen_2025,{ENT},2025,3746890,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 3746890 (was 3845029); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_inst_2025,{ENT},2025,54826,,,executed,{SRC},strong,2025 installaties 23 54826 (was 50863); leasing 25 empty; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_meubilair_2025,{ENT},2025,111057,,,executed,{SRC},strong,2025 meubilair 24 111057 (was 122121); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_overige_mva_2025,{ENT},2025,116598,,,executed,{SRC},strong,2025 overige MVA 26 116598 (was 143173); in aanbouw 27 empty; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_fva_2025,{ENT},2025,31569,,,executed,{SRC},strong,2025 FVA 28 31569 (was 30117); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_current_2025,{ENT},2025,5268331,,,executed,{SRC},strong,2025 vlottende 29/58 5268331 (was 5241982); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_strecv_2025,{ENT},2025,1777215,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1777215 (was 1500958; all trade 40); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_beleggingen_2025,{ENT},2025,1000000,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1000000 stable; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_cash_2025,{ENT},2025,2477705,,,executed,{SRC},strong,2025 liquide middelen 54/58 2477705 DROP (was 2721858); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_prepaid_2025,{ENT},2025,13411,,,executed,{SRC},strong,2025 overlopend actief 490/1 13411 (was 17417); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_equity_2025,{ENT},2025,6996922,,,executed,{SRC},strong,2025 eigen vermogen 10/15 6996922 DROP (was 7049760); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_bestemde_2025,{ENT},2025,4963198,,,executed,{SRC},strong,2025 bestemde fondsen 13 4963198 (was 4928774; toevoeging 34423); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_overgedragen_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 overgedragen winst 14 0; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_kapsubs_2025,{ENT},2025,2033724,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 2033724 (was 2120985); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_debt_2025,{ENT},2025,2332348,,,executed,{SRC},strong,2025 schulden 17/49 2332348 DROP (was 2383526); LT 17 empty; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_stdebt_2025,{ENT},2025,1845534,,,executed,{SRC},strong,2025 ST schulden 42/48 1845534 (was 1898783); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_lev_2025,{ENT},2025,568313,,,executed,{SRC},strong,2025 leveranciers 440/4 568313 UP (was 488785); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_taxsoc_2025,{ENT},2025,1185017,,,executed,{SRC},strong,2025 tax+bezold 45 1185017 (tax 224439 + bezold 960578); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_otherst_2025,{ENT},2025,92203,,,executed,{SRC},strong,2025 overige schulden 48 92203 DROP (was 210450); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_deferred_2025,{ENT},2025,486814,,,executed,{SRC},strong,2025 overlopend passief 492/3 486814 (was 484743); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_opbr_2025,{ENT},2025,9335733,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 9335733; annual envelope; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_omzet_2025,{ENT},2025,1083816,,,executed,{SRC},strong,2025 omzet 70 1083816 UP (was 1003690); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_lidgeld_2025,{ENT},2025,6717617,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 6717617 UP (was 6692703; all 733 subsidies); CGG-dotatie; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_andere_opbr_2025,{ENT},2025,1459538,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 1459538 JUMP (was 1170732); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_nrec_2025,{ENT},2025,74763,,,executed,{SRC},strong,2025 nrec 76A 74763 (was 54595); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_pers_2025,{ENT},2025,6655129,,,executed,{SRC},strong,2025 pers 62 6655129 / 69.5 VTE (was 6621577 / 68.9); YE 98; 92163 uur; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_diensten_2025,{ENT},2025,2312175,,,executed,{SRC},strong,2025 diensten 61 2312175 JUMP (was 1991986); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_aankopen_2025,{ENT},2025,46440,,,executed,{SRC},strong,2025 aankopen 60 46440 (was 51853); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_afschr_2025,{ENT},2025,197534,,,executed,{SRC},strong,2025 afschrijvingen 630 197534 (was 190825); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_andere_2025,{ENT},2025,10745,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 10745 (was 12992); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_bedrijfskost_2025,{ENT},2025,9322115,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 9322115 (was 9030077); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_expl_2025,{ENT},2025,13619,,,executed,{SRC},strong,2025 bedrijfswinst 9901 13619 (was -108358); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_finopbr_2025,{ENT},2025,28823,,,executed,{SRC},strong,2025 financiele opbrengsten 75 28823 DROP (was 44159); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_finkost_2025,{ENT},2025,313,,,executed,{SRC},strong,2025 financiele kosten 65 313 (was 176); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_tax_2025,{ENT},2025,7705,,,executed,{SRC},strong,2025 belastingen 67/77 7705 (was 9839); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_pnl_2025,{ENT},2025,34423,,,executed,{SRC},strong,2025 winst 9904 34423 (was -74214); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_capex_2025,{ENT},2025,65717,,,executed,{SRC},strong,2025 capex 8161+8162+8163+8165 65717 (32254+26770+6693+0); tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
    f"bud_cgvb_commissaris_2025,{ENT},2025,7680,,,executed,{SRC},strong,2025 commissaris Callens-Vandelanotte NV B00083 fee 7680 + taxadvies 50; tick1509; primary official NBB WVV VOL-VZW 2026-00227270",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

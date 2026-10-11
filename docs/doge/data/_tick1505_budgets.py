#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_vitr"
SRC = "src_vitr_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_vitr_assets_2025,{ENT},2025,17056698,,,executed,{SRC},strong,2025 assets 17056698 UP (was 14871671); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_current_2025,{ENT},2025,39058,,,executed,{SRC},strong,2025 vlottend 39058 UP (was 29859); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_cash_2025,{ENT},2025,39058,,,executed,{SRC},strong,2025 liquide middelen 39058 UP (was 29859); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_voorr_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 voorraden 0 empty; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_strecv_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 ST vorderingen 0 empty; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_fixed_2025,{ENT},2025,17017640,,,executed,{SRC},strong,2025 vaste activa 17017640 UP (was 14841812); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_mva_2025,{ENT},2025,17017640,,,executed,{SRC},strong,2025 MVA 17017640 UP (was 14841812; all terreinen/gebouwen); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_terreinen_2025,{ENT},2025,17017640,,,executed,{SRC},strong,2025 terreinen en gebouwen 17017640 UP (was 14841812); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_in_aanbouw_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 activa in aanbouw 27 empty 0 (aanschaf 8196 still 119751); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_fva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 FVA 0 empty; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_equity_2025,{ENT},2025,-24315400,,,executed,{SRC},strong,2025 eigen vermogen -24315400 improved (was -26396035); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_inbreng_2025,{ENT},2025,612500,,,executed,{SRC},strong,2025 inbreng/kapitaal 612500 stable; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_herw_2025,{ENT},2025,116215,,,executed,{SRC},strong,2025 herwaarderingsmeerwaarden 116215 (was empty; 8211 116215); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_overgedr_2025,{ENT},2025,-25044115,,,executed,{SRC},strong,2025 overgedragen verlies -25044115 improved (was -27008535); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_voorz_2025,{ENT},2025,75000,,,executed,{SRC},strong,2025 voorzieningen 75000 stable (overige risico 164/5); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_debt_2025,{ENT},2025,41297098,,,executed,{SRC},strong,2025 schulden 41297098 UP (was 41192706; LT 32652441 + ST 8644657); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_ltdebt_2025,{ENT},2025,32652441,,,executed,{SRC},strong,2025 LT schulden 32652441 stable (all kredietinstellingen 173); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_krediet_2025,{ENT},2025,32652441,,,executed,{SRC},strong,2025 LT kredietinstellingen 32652441 (resterend 1-5 jaar 8802); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_stdebt_2025,{ENT},2025,8644657,,,executed,{SRC},strong,2025 ST schulden 8644657 UP (was 8540265; fin 8590265 + lev 38699 + tax 15693); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_stfin_2025,{ENT},2025,8590265,,,executed,{SRC},strong,2025 ST financieel 8590265 (krediet 7708507 + overige 881758); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_lev_2025,{ENT},2025,38699,,,executed,{SRC},strong,2025 leveranciers 38699 (was empty); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_omzet_2025,{ENT},2025,15730,,,executed,{SRC},strong,2025 omzet 70 15730 DROP (was 22555); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_bedrijfsopbr_2025,{ENT},2025,2321578,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 2321578 (omzet 15730 + 76A 2305848); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_nrec_opbr_2025,{ENT},2025,2305848,,,executed,{SRC},strong,2025 niet-recurrente 76A/760 2305848 terugneming WV MVA (Matexi/Vlaanderen 2022 estimates); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_diensten_2025,{ENT},2025,39923,,,executed,{SRC},strong,2025 diensten 61 39923 DROP (was 77099); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_pers_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 pers 62 empty 0; 9086/9087 empty 0 VTE; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_afschr_2025,{ENT},2025,246235,,,executed,{SRC},strong,2025 afschrijvingen 630/8271 246235 (was empty); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_andere_2025,{ENT},2025,54346,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 54346 (was 1579); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_expl_2025,{ENT},2025,1981073,,,executed,{SRC},strong,2025 bedrijfswinst 9901 1981073 vs -56122; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_finopbr_2025,{ENT},2025,4,,,executed,{SRC},strong,2025 financiele opbrengsten 4 (was empty); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_finkost_2025,{ENT},2025,963,,,executed,{SRC},strong,2025 financiele kosten 963 (was 1001); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_tax_2025,{ENT},2025,15694,,,executed,{SRC},strong,2025 belastingen 67/77 15694 (was empty); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_pnl_2025,{ENT},2025,1964420,,,executed,{SRC},strong,2025 PnL 9904 1964420 vs -57123; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 694/7 empty 0; resultaat overgedragen; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_capex_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 capex 8161+8166 empty 0; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_explsubs_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 empty 0; tick1505; primary official NBB WVV VOL",
    f"bud_vitr_bedrijfskost_2025,{ENT},2025,340505,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 340505 (was 78677); tick1505; primary official NBB WVV VOL",
    f"bud_vitr_mva_aanschaf_2025,{ENT},2025,32597756,,,executed,{SRC},strong,2025 MVA aanschafwaarde 8191 32597756 stable; WV 8321 15696331 after terugneming 8281 2305848; tick1505; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

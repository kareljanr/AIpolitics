# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_eddl"
SRC = "src_eddl_jr2025_nbb"
BUDGETS = [
    ("bud_eddl_assets_2025", "2025", "454221", "2025 assets 454221 MIC-VZW 20/58; tick1427; primary official NBB WVV"),
    ("bud_eddl_assets_2024", "2024", "484239", "2024 assets 484239 comparative; tick1427; primary official NBB WVV 20/58"),
    ("bud_eddl_fixed_2025", "2025", "15252", "2025 vaste activa 15252 vs 17157; tick1427; primary official NBB WVV 21/28"),
    ("bud_eddl_mva_2025", "2025", "15227", "2025 MVA 15227 vs 17132; tick1427; primary official NBB WVV 22/27"),
    ("bud_eddl_mva_meub_2025", "2025", "15227", "2025 meubilair 15227 vs 17132; tick1427; primary official NBB WVV 24"),
    ("bud_eddl_mva_aanschaf_2025", "2025", "19047", "2025 MVA aanschaf YE 19047; tick1427; primary official NBB WVV 8199"),
    ("bud_eddl_mva_afschr_2025", "2025", "3820", "2025 MVA afschr YE 3820; tick1427; primary official NBB WVV 8329"),
    ("bud_eddl_fva_2025", "2025", "25", "2025 FVA 25 vs 25; tick1427; primary official NBB WVV 28"),
    ("bud_eddl_current_2025", "2025", "438969", "2025 vlottend 438969 vs 467082; tick1427; primary official NBB WVV 29/58"),
    ("bud_eddl_strecv_2025", "2025", "118920", "2025 ST vorderingen 118920 vs 64235; tick1427; primary official NBB WVV 40/41"),
    ("bud_eddl_trade_recv_2025", "2025", "22951", "2025 handelsvorderingen 22951 JUMP vs empty unpublished counterpart; tick1427; primary official NBB WVV 40"),
    ("bud_eddl_other_recv_2025", "2025", "95969", "2025 overige vorderingen 95969 JUMP vs 64235 unpublished counterpart; tick1427; primary official NBB WVV 41"),
    ("bud_eddl_other_recv_2024", "2024", "64235", "2024 overige vorderingen 64235 comparative; tick1427; primary official NBB WVV 41"),
    ("bud_eddl_cash_2025", "2025", "320049", "2025 liquide middelen 320049 DROP vs 402847; tick1427; primary official NBB WVV 54/58"),
    ("bud_eddl_cash_2024", "2024", "402847", "2024 liquide middelen 402847 comparative; tick1427; primary official NBB WVV 54/58"),
    ("bud_eddl_equity_2025", "2025", "73209", "2025 EV 73209 DROP vs 149903; tick1427; primary official NBB WVV 10/15"),
    ("bud_eddl_equity_2024", "2024", "149903", "2024 EV 149903 comparative; tick1427; primary official NBB WVV 10/15"),
    ("bud_eddl_reserves_2025", "2025", "73209", "2025 bestemde fondsen 73209 vs 149903; tick1427; primary official NBB WVV 13"),
    ("bud_eddl_debt_2025", "2025", "381012", "2025 schulden 381012 vs 334336; tick1427; primary official NBB WVV 17/49"),
    ("bud_eddl_debt_2024", "2024", "334336", "2024 schulden 334336 comparative; tick1427; primary official NBB WVV 17/49"),
    ("bud_eddl_st_2025", "2025", "361155", "2025 ST 361155 vs 334336 no LT; tick1427; primary official NBB WVV 42/48"),
    ("bud_eddl_sttrade_2025", "2025", "361155", "2025 leveranciers 361155 vs 334336 unpublished counterpart; tick1427; primary official NBB WVV 440/4"),
    ("bud_eddl_deferred_2025", "2025", "19857", "2025 deferred 19857 vs empty; tick1427; primary official NBB WVV 492/3"),
    ("bud_eddl_brutomarge_2025", "2025", "-74789", "2025 brutomarge -74789 vs -17170; omzet 70 token 100; tick1427; primary official NBB WVV 9900"),
    ("bud_eddl_brutomarge_2024", "2024", "-17170", "2024 brutomarge -17170 comparative; tick1427; primary official NBB WVV 9900"),
    ("bud_eddl_omzet_2025", "2025", "100", "2025 omzet 70 token 100 vs 57; tick1427; primary official NBB WVV 70"),
    ("bud_eddl_lidgeld_2025", "2025", "498745", "2025 lidgeld/subsidies 498745 vs 555943 unpublished split; tick1427; primary official NBB WVV 73"),
    ("bud_eddl_lidgeld_2024", "2024", "555943", "2024 lidgeld/subsidies 555943 comparative; tick1427; primary official NBB WVV 73"),
    ("bud_eddl_diensten_2025", "2025", "573634", "2025 60/61 573634 vs 573144 unpublished as a split; tick1427; primary official NBB WVV 60/61"),
    ("bud_eddl_diensten_2024", "2024", "573144", "2024 60/61 573144 comparative; tick1427; primary official NBB WVV 60/61"),
    ("bud_eddl_afschr_2025", "2025", "1905", "2025 afschr 1905 vs 790; tick1427; primary official NBB WVV 630"),
    ("bud_eddl_expl_2025", "2025", "-76694", "2025 expl -76694 vs -17960; tick1427; primary official NBB WVV 9901"),
    ("bud_eddl_expl_2024", "2024", "-17960", "2024 expl -17960 comparative; tick1427; primary official NBB WVV 9901"),
    ("bud_eddl_fincost_2025", "2025", "1", "2025 fin kosten 1 vs 26; tick1427; primary official NBB WVV 65/66B"),
    ("bud_eddl_pnl_2025", "2025", "-76695", "2025 PnL -76695 vs -17986; tick1427; primary official NBB WVV 9904"),
    ("bud_eddl_pnl_2024", "2024", "-17986", "2024 PnL -17986 comparative; tick1427; primary official NBB WVV 9904"),
    ("bud_eddl_onttrekking_2025", "2025", "76695", "2025 onttrekking EV 76695 vs 25145; tick1427; primary official NBB WVV 791"),
    ("bud_eddl_div_2025", "2025", "0", "2025 dividend 0 / no 694 on MIC-VZW; tick1427; primary official NBB WVV"),
    ("bud_eddl_capex_2025", "2025", "0", "2025 capex MVA aanschaf 8169 empty; IVA/FVA aanschaf empty; tick1427; primary official NBB WVV 6.1.2"),
]
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
existing = set()
for row in csv.reader(io.StringIO(raw.decode("utf-8"))):
    if row:
        existing.add(row[0])
added = []
for bid, year, amt, notes in BUDGETS:
    if bid in existing:
        continue
    added.append(f"{bid},{ENT},{year},{amt},,,executed,{SRC},strong,{notes}\n")
p.write_bytes(raw + "".join(added).encode("utf-8"))
print("budgets", len(added))

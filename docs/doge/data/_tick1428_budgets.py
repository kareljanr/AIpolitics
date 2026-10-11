# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_ebk"
SRC = "src_ebk_jr2025_nbb"
BUDGETS = [
    ("bud_ebk_assets_2025", "2025", "200838", "2025 assets 200838 MIC-VZW 20/58; tick1428; primary official NBB WVV"),
    ("bud_ebk_assets_2024", "2024", "183780", "2024 assets 183780 comparative; tick1428; primary official NBB WVV 20/58"),
    ("bud_ebk_current_2025", "2025", "200838", "2025 vlottend 200838 vs 183780; no vaste activa; tick1428; primary official NBB WVV 29/58"),
    ("bud_ebk_cash_2025", "2025", "172470", "2025 liquide middelen 172470 vs 158950; tick1428; primary official NBB WVV 54/58"),
    ("bud_ebk_cash_2024", "2024", "158950", "2024 liquide middelen 158950 comparative; tick1428; primary official NBB WVV 54/58"),
    ("bud_ebk_prepaid_2025", "2025", "28368", "2025 prepaid 28368 vs 24829; tick1428; primary official NBB WVV 490/1"),
    ("bud_ebk_prepaid_2024", "2024", "24829", "2024 prepaid 24829 comparative; tick1428; primary official NBB WVV 490/1"),
    ("bud_ebk_equity_2025", "2025", "0", "2025 EV 10/15 empty / 0 (all equity lines blank; BS balances via schulden); tick1428; primary official NBB WVV 10/15"),
    ("bud_ebk_debt_2025", "2025", "200838", "2025 schulden 200838 vs 183780; tick1428; primary official NBB WVV 17/49"),
    ("bud_ebk_debt_2024", "2024", "183780", "2024 schulden 183780 comparative; tick1428; primary official NBB WVV 17/49"),
    ("bud_ebk_st_2025", "2025", "153718", "2025 ST 153718 vs 153718 no LT; tick1428; primary official NBB WVV 42/48"),
    ("bud_ebk_sttrade_2025", "2025", "153718", "2025 leveranciers 153718 vs 153718 unpublished counterpart; tick1428; primary official NBB WVV 440/4"),
    ("bud_ebk_deferred_2025", "2025", "47119", "2025 deferred 47119 vs 30062; tick1428; primary official NBB WVV 492/3"),
    ("bud_ebk_deferred_2024", "2024", "30062", "2024 deferred 30062 comparative; tick1428; primary official NBB WVV 492/3"),
    ("bud_ebk_brutomarge_2025", "2025", "0", "2025 brutomarge 0 vs 44; omzet 70 empty; 73 empty; 60/61 empty; tick1428; primary official NBB WVV 9900"),
    ("bud_ebk_brutomarge_2024", "2024", "44", "2024 brutomarge 44 comparative; tick1428; primary official NBB WVV 9900"),
    ("bud_ebk_expl_2025", "2025", "0", "2025 expl 0 vs 44; tick1428; primary official NBB WVV 9901"),
    ("bud_ebk_expl_2024", "2024", "44", "2024 expl 44 comparative; tick1428; primary official NBB WVV 9901"),
    ("bud_ebk_pnl_2025", "2025", "0", "2025 PnL 0 vs 0; tick1428; primary official NBB WVV 9904"),
    ("bud_ebk_pnl_2024", "2024", "0", "2024 PnL 0 comparative; tick1428; primary official NBB WVV 9904"),
    ("bud_ebk_div_2025", "2025", "0", "2025 dividend 0 / no 694 on MIC-VZW; tick1428; primary official NBB WVV"),
    ("bud_ebk_capex_2025", "2025", "0", "2025 capex 0; MVA/IVA/FVA empty; MIC-VZW 6.1.2 not filed; tick1428; primary official NBB WVV"),
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

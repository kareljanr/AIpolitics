# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_rpsk"
SRC = "src_rpsk_jr2025_nbb"
BUDGETS = [
    ("bud_rpsk_assets_2025", "2025", "58035", "2025 assets 58035 MIC-inb 20/58; tick1431; primary official NBB WVV"),
    ("bud_rpsk_assets_2024", "2024", "69033", "2024 assets 69033 comparative; tick1431; primary official NBB WVV 20/58"),
    ("bud_rpsk_current_2025", "2025", "58035", "2025 vlottend 58035 vs 69033; no vaste activa; tick1431; primary official NBB WVV 29/58"),
    ("bud_rpsk_cash_2025", "2025", "31653", "2025 liquide middelen 31653 DROP vs 38681; tick1431; primary official NBB WVV 54/58"),
    ("bud_rpsk_cash_2024", "2024", "38681", "2024 liquide middelen 38681 comparative; tick1431; primary official NBB WVV 54/58"),
    ("bud_rpsk_prepaid_2025", "2025", "26382", "2025 prepaid 26382 vs 30352; tick1431; primary official NBB WVV 490/1"),
    ("bud_rpsk_equity_2025", "2025", "58035", "2025 EV 58035 inbreng 20393 + overgedragen 37642 DROP vs 69033; tick1431; primary official NBB WVV 10/15"),
    ("bud_rpsk_equity_2024", "2024", "69033", "2024 EV 69033 comparative; tick1431; primary official NBB WVV 10/15"),
    ("bud_rpsk_inbreng_2025", "2025", "20393", "2025 inbreng onbeschikbaar 20393 vs 20393; tick1431; primary official NBB WVV 10/11 111"),
    ("bud_rpsk_overgedragen_2025", "2025", "37642", "2025 overgedragen 37642 DROP vs 48640; tick1431; primary official NBB WVV 14"),
    ("bud_rpsk_debt_2025", "2025", "0", "2025 schulden empty / 0 vs empty; tick1431; primary official NBB WVV 17/49"),
    ("bud_rpsk_brutomarge_2025", "2025", "-10959", "2025 brutomarge -10959 vs -6602; omzet 70 empty; 60/61 empty; tick1431; primary official NBB WVV 9900"),
    ("bud_rpsk_brutomarge_2024", "2024", "-6602", "2024 brutomarge -6602 comparative; tick1431; primary official NBB WVV 9900"),
    ("bud_rpsk_expl_2025", "2025", "-10959", "2025 expl -10959 vs -6602; tick1431; primary official NBB WVV 9901"),
    ("bud_rpsk_expl_2024", "2024", "-6602", "2024 expl -6602 comparative; tick1431; primary official NBB WVV 9901"),
    ("bud_rpsk_finkost_2025", "2025", "39", "2025 fin kosten 39 vs 38; tick1431; primary official NBB WVV 65"),
    ("bud_rpsk_pnl_2025", "2025", "-10998", "2025 PnL -10998 vs -6640; tick1431; primary official NBB WVV 9904"),
    ("bud_rpsk_pnl_2024", "2024", "-6640", "2024 PnL -6640 comparative; tick1431; primary official NBB WVV 9904"),
    ("bud_rpsk_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1431; primary official NBB WVV"),
    ("bud_rpsk_capex_2025", "2025", "0", "2025 capex 0; MVA/IVA/FVA empty; 6.1.1/6.1.2/6.1.3 not filed; tick1431; primary official NBB WVV"),
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

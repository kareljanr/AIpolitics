# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_vtrt"
SRC = "src_vtrt_jr2025_nbb"
BUDGETS = [
    ("bud_vtrt_assets_2025", "2025", "211378", "2025 assets 211378 MIC-inb 20/58; tick1421; primary official NBB WVV"),
    ("bud_vtrt_assets_2024", "2024", "229857", "2024 assets 229857 comparative; tick1421; primary official NBB WVV 20/58"),
    ("bud_vtrt_current_2025", "2025", "211378", "2025 vlottend 211378 vs 229857; tick1421; primary official NBB WVV 29/58"),
    ("bud_vtrt_strecv_2025", "2025", "22238", "2025 ST vorderingen 22238 vs empty; tick1421; primary official NBB WVV 40/41"),
    ("bud_vtrt_other_recv_2025", "2025", "22238", "2025 overige vorderingen 22238 counterpart unpublished; tick1421; primary official NBB WVV 41"),
    ("bud_vtrt_cash_2025", "2025", "189139", "2025 liquide middelen 189139 DROP vs 229857; tick1421; primary official NBB WVV 54/58"),
    ("bud_vtrt_cash_2024", "2024", "229857", "2024 liquide middelen 229857 comparative; tick1421; primary official NBB WVV 54/58"),
    ("bud_vtrt_equity_2025", "2025", "202586", "2025 EV 202586 vs 171929; tick1421; primary official NBB WVV 10/15"),
    ("bud_vtrt_equity_2024", "2024", "171929", "2024 EV 171929 comparative; tick1421; primary official NBB WVV 10/15"),
    ("bud_vtrt_reserves_2025", "2025", "226050", "2025 beschikbare reserves 226050; tick1421; primary official NBB WVV 133"),
    ("bud_vtrt_overgedragen_2025", "2025", "-23464", "2025 overgedragen -23464 vs -54121; tick1421; primary official NBB WVV 14"),
    ("bud_vtrt_overgedragen_2024", "2024", "-54121", "2024 overgedragen -54121 comparative; tick1421; primary official NBB WVV 14"),
    ("bud_vtrt_debt_2025", "2025", "8791", "2025 schulden 8791 vs 57927; tick1421; primary official NBB WVV 17/49"),
    ("bud_vtrt_debt_2024", "2024", "57927", "2024 schulden 57927 comparative; tick1421; primary official NBB WVV 17/49"),
    ("bud_vtrt_st_2025", "2025", "8791", "2025 ST schulden 8791 vs 19791; tick1421; primary official NBB WVV 42/48"),
    ("bud_vtrt_st_2024", "2024", "19791", "2024 ST schulden 19791 comparative; tick1421; primary official NBB WVV 42/48"),
    ("bud_vtrt_sttrade_2025", "2025", "47", "2025 leveranciers 47 vs 16944; tick1421; primary official NBB WVV 440/4"),
    ("bud_vtrt_soc_2025", "2025", "8744", "2025 bezoldigingen/sociale 8744 vs 2846; tick1421; primary official NBB WVV 454/9"),
    ("bud_vtrt_soc_2024", "2024", "2846", "2024 bezoldigingen/sociale 2846 comparative; tick1421; primary official NBB WVV 454/9"),
    ("bud_vtrt_deferred_pass_2024", "2024", "38136", "2024 overlopend passief 38136 (2025 empty); tick1421; primary official NBB WVV 492/3"),
    ("bud_vtrt_brutomarge_2025", "2025", "110397", "2025 brutomarge 110397 vs 68882; omzet 70 empty / 60/61 empty; tick1421; primary official NBB WVV 9900"),
    ("bud_vtrt_brutomarge_2024", "2024", "68882", "2024 brutomarge 68882 comparative; tick1421; primary official NBB WVV 9900"),
    ("bud_vtrt_pers_2025", "2025", "79534", "2025 pers 79534 vs 44359; VTE unpublished MIC-inb 6.2 not filed; tick1421; primary official NBB WVV 62"),
    ("bud_vtrt_pers_2024", "2024", "44359", "2024 pers 44359 comparative; tick1421; primary official NBB WVV 62"),
    ("bud_vtrt_expl_2025", "2025", "30863", "2025 expl 30863 vs 24523; tick1421; primary official NBB WVV 9901"),
    ("bud_vtrt_expl_2024", "2024", "24523", "2024 expl 24523 comparative; tick1421; primary official NBB WVV 9901"),
    ("bud_vtrt_fincost_2025", "2025", "206", "2025 fin kosten 206 vs 206; tick1421; primary official NBB WVV 65"),
    ("bud_vtrt_pnl_2025", "2025", "30657", "2025 PnL 30657 vs 24317; tick1421; primary official NBB WVV 9904"),
    ("bud_vtrt_pnl_2024", "2024", "24317", "2024 PnL 24317 comparative; tick1421; primary official NBB WVV 9904"),
    ("bud_vtrt_dest_year_2025", "2025", "30657", "2025 te bestemmen winst boekjaar 30657; tick1421; primary official NBB WVV 9905"),
    ("bud_vtrt_overgedragen_dest_2025", "2025", "-23464", "2025 over te dragen verlies -23464; tick1421; primary official NBB WVV 14"),
    ("bud_vtrt_div_2025", "2025", "0", "2025 vergoeding inbreng 0 / 694 empty; tick1421; primary official NBB WVV 694"),
    ("bud_vtrt_capex_2025", "2025", "0", "2025 capex 0 / MVA empty / 6.1.2 not filed; tick1421; primary official NBB WVV"),
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

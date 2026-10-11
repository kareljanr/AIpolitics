# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_co7"
SRC = "src_co7_jr2025_nbb"
BUDGETS = [
    ("bud_co7_assets_2025", "2025", "691225", "2025 assets 691225 MIC-inb 20/58; tick1420; primary official NBB WVV"),
    ("bud_co7_assets_2024", "2024", "615702", "2024 assets 615702 comparative; tick1420; primary official NBB WVV 20/58"),
    ("bud_co7_fixed_2025", "2025", "14026", "2025 vaste activa 14026 vs 4376; tick1420; primary official NBB WVV 21/28"),
    ("bud_co7_mva_2025", "2025", "14026", "2025 MVA 14026 vs 4376; tick1420; primary official NBB WVV 22/27"),
    ("bud_co7_meubilair_2025", "2025", "14026", "2025 meubilair 14026 vs 4376; tick1420; primary official NBB WVV 24"),
    ("bud_co7_current_2025", "2025", "677199", "2025 vlottend 677199 vs 611326; tick1420; primary official NBB WVV 29/58"),
    ("bud_co7_strecv_2025", "2025", "5183", "2025 ST vorderingen 5183 vs 3811; tick1420; primary official NBB WVV 40/41"),
    ("bud_co7_trade_recv_2025", "2025", "5183", "2025 handelsvorderingen 5183 vs 3811; tick1420; primary official NBB WVV 40"),
    ("bud_co7_cash_2025", "2025", "552517", "2025 liquide middelen 552517 vs 511474; tick1420; primary official NBB WVV 54/58"),
    ("bud_co7_cash_2024", "2024", "511474", "2024 liquide middelen 511474 comparative; tick1420; primary official NBB WVV 54/58"),
    ("bud_co7_prepaid_2025", "2025", "119499", "2025 overlopend actief 119499 JUMP vs 96041; tick1420; primary official NBB WVV 490/1"),
    ("bud_co7_prepaid_2024", "2024", "96041", "2024 overlopend actief 96041 comparative; tick1420; primary official NBB WVV 490/1"),
    ("bud_co7_equity_2025", "2025", "393922", "2025 EV 393922 vs 401062; tick1420; primary official NBB WVV 10/15"),
    ("bud_co7_overgedragen_2025", "2025", "393922", "2025 overgedragen 393922 vs 401062; tick1420; primary official NBB WVV 14"),
    ("bud_co7_debt_2025", "2025", "297303", "2025 schulden 297303 vs 214640; tick1420; primary official NBB WVV 17/49"),
    ("bud_co7_debt_2024", "2024", "214640", "2024 schulden 214640 comparative; tick1420; primary official NBB WVV 17/49"),
    ("bud_co7_st_2025", "2025", "284516", "2025 ST schulden 284516 vs 202219; tick1420; primary official NBB WVV 42/48"),
    ("bud_co7_sttrade_2025", "2025", "284516", "2025 leveranciers 284516 vs 202219; tick1420; primary official NBB WVV 440/4"),
    ("bud_co7_deferred_pass_2025", "2025", "12787", "2025 overlopend passief 12787 vs 12421; tick1420; primary official NBB WVV 492/3"),
    ("bud_co7_brutomarge_2025", "2025", "-917", "2025 brutomarge -917 vs +20438; omzet 899440 / 60/61 900356; tick1420; primary official NBB WVV 9900"),
    ("bud_co7_brutomarge_2024", "2024", "20438", "2024 brutomarge 20438 comparative; tick1420; primary official NBB WVV 9900"),
    ("bud_co7_omzet_2025", "2025", "899440", "2025 omzet 899440 vs 869377; 6.10 category/geo not filed; tick1420; primary official NBB WVV 70"),
    ("bud_co7_omzet_2024", "2024", "869377", "2024 omzet 869377 comparative; tick1420; primary official NBB WVV 70"),
    ("bud_co7_diensten_2025", "2025", "900356", "2025 60/61 900356 vs 848939 unpublished as a split; tick1420; primary official NBB WVV 60/61"),
    ("bud_co7_diensten_2024", "2024", "848939", "2024 60/61 848939 comparative; tick1420; primary official NBB WVV 60/61"),
    ("bud_co7_afschr_2025", "2025", "8062", "2025 afschrijvingen 8062 vs 3909; tick1420; primary official NBB WVV 630"),
    ("bud_co7_expl_2025", "2025", "-8979", "2025 expl -8979 vs +16529; tick1420; primary official NBB WVV 9901"),
    ("bud_co7_expl_2024", "2024", "16529", "2024 expl 16529 comparative; tick1420; primary official NBB WVV 9901"),
    ("bud_co7_finopbr_2025", "2025", "3429", "2025 fin opbr 3429 vs 6396; tick1420; primary official NBB WVV 75"),
    ("bud_co7_fincost_2025", "2025", "561", "2025 fin kosten 561 vs 256; tick1420; primary official NBB WVV 65"),
    ("bud_co7_tax_2025", "2025", "1029", "2025 tax 1029 vs 1918; tick1420; primary official NBB WVV 67/77"),
    ("bud_co7_pnl_2025", "2025", "-7140", "2025 PnL -7140 vs +20751; tick1420; primary official NBB WVV 9904"),
    ("bud_co7_pnl_2024", "2024", "20751", "2024 PnL 20751 comparative; tick1420; primary official NBB WVV 9904"),
    ("bud_co7_div_2025", "2025", "0", "2025 vergoeding inbreng 0 / 694 empty; tick1420; primary official NBB WVV 694"),
    ("bud_co7_overgedragen_dest_2025", "2025", "393922", "2025 over te dragen winst 393922; tick1420; primary official NBB WVV 14"),
    ("bud_co7_capex_2025", "2025", "17712", "2025 capex MVA aanschaf 17712; tick1420; primary official NBB WVV 8169"),
    ("bud_co7_mva_aanschaf_ye_2025", "2025", "76332", "2025 MVA aanschaf YE 76332 vs 59855; tick1420; primary official NBB WVV 8199"),
    ("bud_co7_mva_afschr_ye_2025", "2025", "62306", "2025 MVA afschr YE 62306 vs 55479; tick1420; primary official NBB WVV 8329"),
    ("bud_co7_disposal_2025", "2025", "1235", "2025 MVA overdrachten 1235; tick1420; primary official NBB WVV 8179"),
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

# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "agb_de_kluize_oosterzele"
SRC = "src_kluz_jr2025_nbb"
BUDGETS = [
    ("bud_kluz_assets_2025", "2025", "5831290", "2025 assets 5831290 VKT-kap 20/58; tick1414; primary official NBB WVV"),
    ("bud_kluz_assets_2024", "2024", "5817276", "2024 assets 5817276 comparative; tick1414; primary official NBB WVV 20/58"),
    ("bud_kluz_fixed_2025", "2025", "5009742", "2025 vaste activa 5009742 vs 5113157; tick1414; primary official NBB WVV 21/28"),
    ("bud_kluz_mva_2025", "2025", "5009715", "2025 MVA 5009715 vs 5113129; tick1414; primary official NBB WVV 22/27"),
    ("bud_kluz_gebouwen_2025", "2025", "416750", "2025 terreinen/gebouwen 416750 vs 457740; tick1414; primary official NBB WVV 22"),
    ("bud_kluz_machines_2025", "2025", "107612", "2025 machines 107612 vs 76975; tick1414; primary official NBB WVV 23"),
    ("bud_kluz_meubilair_2025", "2025", "1395", "2025 meubilair 1395 vs 2001; tick1414; primary official NBB WVV 24"),
    ("bud_kluz_lease_2025", "2025", "4483958", "2025 leasing/erfpacht 4483958 vs 4576414; tick1414; primary official NBB WVV 25"),
    ("bud_kluz_fva_2025", "2025", "27", "2025 FVA 27 unchanged; tick1414; primary official NBB WVV 28"),
    ("bud_kluz_current_2025", "2025", "821549", "2025 vlottend 821549 vs 704119; tick1414; primary official NBB WVV 29/58"),
    ("bud_kluz_strecv_2025", "2025", "97457", "2025 ST vorderingen 97457 vs 141663; tick1414; primary official NBB WVV 40/41"),
    ("bud_kluz_trade_recv_2025", "2025", "79188", "2025 handelsvorderingen 79188 vs 135965; tick1414; primary official NBB WVV 40"),
    ("bud_kluz_othrecv_2025", "2025", "18269", "2025 overige vorderingen 18269 vs 5698; tick1414; primary official NBB WVV 41"),
    ("bud_kluz_cash_2025", "2025", "724091", "2025 liquide middelen 724091 JUMP vs 553256; tick1414; primary official NBB WVV 54/58"),
    ("bud_kluz_cash_2024", "2024", "553256", "2024 liquide middelen 553256 comparative; tick1414; primary official NBB WVV 54/58"),
    ("bud_kluz_equity_2025", "2025", "69529", "2025 EV 69529 vs 45992; tick1414; primary official NBB WVV 10/15"),
    ("bud_kluz_inbreng_2025", "2025", "25000", "2025 kapitaal geplaatst 25000; tick1414; primary official NBB WVV 100"),
    ("bud_kluz_reserves_2025", "2025", "2257", "2025 wettelijke reserve 2257; tick1414; primary official NBB WVV 130"),
    ("bud_kluz_overgedragen_2025", "2025", "42272", "2025 overgedragen 42272 vs 18735; tick1414; primary official NBB WVV 14"),
    ("bud_kluz_debt_2025", "2025", "5761761", "2025 schulden 5761761 vs 5771284; tick1414; primary official NBB WVV 17/49"),
    ("bud_kluz_debt_2024", "2024", "5771284", "2024 schulden 5771284 comparative; tick1414; primary official NBB WVV 17/49"),
    ("bud_kluz_lt_2025", "2025", "5317332", "2025 LT schulden 5317332 vs 5399397; tick1414; primary official NBB WVV 17"),
    ("bud_kluz_lt_lease_2025", "2025", "4932885", "2025 LT lease/krediet 4932885 vs 4990922; tick1414; primary official NBB WVV 172/3"),
    ("bud_kluz_lt_other_2025", "2025", "384447", "2025 LT overige leningen 384447 vs 408475; tick1414; primary official NBB WVV 174/0"),
    ("bud_kluz_st_2025", "2025", "362077", "2025 ST schulden 362077 vs 302709; tick1414; primary official NBB WVV 42/48"),
    ("bud_kluz_ltdue_2025", "2025", "82065", "2025 LT-due binnen jaar 82065; tick1414; primary official NBB WVV 42"),
    ("bud_kluz_sttrade_2025", "2025", "206747", "2025 leveranciers 206747 vs 203737; tick1414; primary official NBB WVV 440/4"),
    ("bud_kluz_tax_st_2025", "2025", "3109", "2025 tax ST 3109 vs 1346; tick1414; primary official NBB WVV 450/3"),
    ("bud_kluz_soc_st_2025", "2025", "5645", "2025 soc ST 5645 vs 2258; tick1414; primary official NBB WVV 454/9"),
    ("bud_kluz_stother_2025", "2025", "64512", "2025 overige ST 64512 JUMP vs 13304; tick1414; primary official NBB WVV 47/48"),
    ("bud_kluz_deferred_pass_2025", "2025", "82352", "2025 overlopend passief 82352 vs 69177; tick1414; primary official NBB WVV 492/3"),
    ("bud_kluz_debt_1_5y_2025", "2025", "328261", "2025 debt 1-5y 328261; tick1414; primary official NBB WVV 8912"),
    ("bud_kluz_debt_gt5y_2025", "2025", "4989071", "2025 debt >5y 4989071; tick1414; primary official NBB WVV 8913"),
    ("bud_kluz_brutomarge_2025", "2025", "342519", "2025 brutomarge 342519 vs 266855; omzet 70 empty / 60/61 empty; tick1414; primary official NBB WVV 9900"),
    ("bud_kluz_brutomarge_2024", "2024", "266855", "2024 brutomarge 266855 comparative; tick1414; primary official NBB WVV 9900"),
    ("bud_kluz_afschr_2025", "2025", "191114", "2025 afschrijvingen 191114 vs 170263; tick1414; primary official NBB WVV 630"),
    ("bud_kluz_othcost_2025", "2025", "77867", "2025 andere bedrijfskosten 77867 vs 88281; tick1414; primary official NBB WVV 640/8"),
    ("bud_kluz_expl_2025", "2025", "73538", "2025 expl 73538 vs 8311; tick1414; primary official NBB WVV 9901"),
    ("bud_kluz_expl_2024", "2024", "8311", "2024 expl 8311 comparative; tick1414; primary official NBB WVV 9901"),
    ("bud_kluz_fincost_2025", "2025", "0", "2025 fin kosten 0; tick1414; primary official NBB WVV 65"),
    ("bud_kluz_pnl_2025", "2025", "73538", "2025 PnL 73538 vs 8310; tick1414; primary official NBB WVV 9904"),
    ("bud_kluz_pnl_2024", "2024", "8310", "2024 PnL 8310 comparative; tick1414; primary official NBB WVV 9904"),
    ("bud_kluz_div_2025", "2025", "50000", "2025 vergoeding inbreng 50000; tick1414; primary official NBB WVV 694"),
    ("bud_kluz_overgedragen_dest_2025", "2025", "42272", "2025 over te dragen winst 42272; tick1414; primary official NBB WVV 14"),
    ("bud_kluz_capex_2025", "2025", "87700", "2025 capex MVA aanschaf 87700; tick1414; primary official NBB WVV 8169"),
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

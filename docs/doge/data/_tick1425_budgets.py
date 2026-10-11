# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_evpk"
SRC = "src_evpk_jr2025_nbb"
BUDGETS = [
    ("bud_evpk_assets_2025", "2025", "623422", "2025 assets 623422 MIC-inb 20/58; tick1425; primary official NBB WVV"),
    ("bud_evpk_assets_2024", "2024", "713350", "2024 assets 713350 comparative; tick1425; primary official NBB WVV 20/58"),
    ("bud_evpk_fixed_2025", "2025", "1056", "2025 vaste activa 1056 vs 2234; tick1425; primary official NBB WVV 21/28"),
    ("bud_evpk_mva_2025", "2025", "1056", "2025 MVA 1056 vs 2234; tick1425; primary official NBB WVV 22/27"),
    ("bud_evpk_mva_mach_2025", "2025", "1056", "2025 machines 1056 vs 2234; tick1425; primary official NBB WVV 23"),
    ("bud_evpk_mva_aanschaf_2025", "2025", "3532", "2025 MVA aanschaf YE 3532; tick1425; primary official NBB WVV 8199"),
    ("bud_evpk_mva_afschr_2025", "2025", "2476", "2025 MVA afschr YE 2476; tick1425; primary official NBB WVV 8329"),
    ("bud_evpk_current_2025", "2025", "622365", "2025 vlottend 622365 vs 711116; tick1425; primary official NBB WVV 29/58"),
    ("bud_evpk_strecv_2025", "2025", "122961", "2025 ST vorderingen 122961 vs 154545; tick1425; primary official NBB WVV 40/41"),
    ("bud_evpk_trade_recv_2025", "2025", "8682", "2025 handelsvorderingen 8682 vs 2000; tick1425; primary official NBB WVV 40"),
    ("bud_evpk_other_recv_2025", "2025", "114279", "2025 overige vorderingen 114279 vs 152545 unpublished counterpart; tick1425; primary official NBB WVV 41"),
    ("bud_evpk_other_recv_2024", "2024", "152545", "2024 overige vorderingen 152545 comparative; tick1425; primary official NBB WVV 41"),
    ("bud_evpk_cash_2025", "2025", "499042", "2025 liquide middelen 499042 DROP vs 555586; tick1425; primary official NBB WVV 54/58"),
    ("bud_evpk_cash_2024", "2024", "555586", "2024 liquide middelen 555586 comparative; tick1425; primary official NBB WVV 54/58"),
    ("bud_evpk_prepaid_2025", "2025", "362", "2025 prepaid 362 vs 985; tick1425; primary official NBB WVV 490/1"),
    ("bud_evpk_equity_2025", "2025", "125438", "2025 EV 125438 vs 77184; tick1425; primary official NBB WVV 10/15"),
    ("bud_evpk_equity_2024", "2024", "77184", "2024 EV 77184 comparative; tick1425; primary official NBB WVV 10/15"),
    ("bud_evpk_reserves_2025", "2025", "125438", "2025 beschikbare reserves 125438 vs 77184; tick1425; primary official NBB WVV 133"),
    ("bud_evpk_debt_2025", "2025", "497984", "2025 schulden 497984 vs 636166; tick1425; primary official NBB WVV 17/49"),
    ("bud_evpk_debt_2024", "2024", "636166", "2024 schulden 636166 comparative; tick1425; primary official NBB WVV 17/49"),
    ("bud_evpk_st_2025", "2025", "453765", "2025 ST 453765 vs 433046 all leveranciers; tick1425; primary official NBB WVV 42/48"),
    ("bud_evpk_sttrade_2025", "2025", "453765", "2025 leveranciers 453765 vs 433046 unpublished counterpart; tick1425; primary official NBB WVV 440/4"),
    ("bud_evpk_sttrade_2024", "2024", "433046", "2024 leveranciers 433046 comparative; tick1425; primary official NBB WVV 440/4"),
    ("bud_evpk_deferred_2025", "2025", "44219", "2025 overlopend 44219 DROP vs 203120; tick1425; primary official NBB WVV 492/3"),
    ("bud_evpk_deferred_2024", "2024", "203120", "2024 overlopend 203120 comparative; tick1425; primary official NBB WVV 492/3"),
    ("bud_evpk_brutomarge_2025", "2025", "49498", "2025 brutomarge 49498 vs 22224; omzet 70 empty / 60/61 empty; tick1425; primary official NBB WVV 9900"),
    ("bud_evpk_brutomarge_2024", "2024", "22224", "2024 brutomarge 22224 comparative; tick1425; primary official NBB WVV 9900"),
    ("bud_evpk_afschr_2025", "2025", "1177", "2025 afschr 1177 vs 1176; tick1425; primary official NBB WVV 630"),
    ("bud_evpk_andere_kost_2025", "2025", "0", "2025 andere bedrijfskosten 0 vs 158; tick1425; primary official NBB WVV 640/8"),
    ("bud_evpk_expl_2025", "2025", "48321", "2025 expl 48321 vs 20890; tick1425; primary official NBB WVV 9901"),
    ("bud_evpk_expl_2024", "2024", "20890", "2024 expl 20890 comparative; tick1425; primary official NBB WVV 9901"),
    ("bud_evpk_fininc_2025", "2025", "69", "2025 fin opbr 69 vs 0; tick1425; primary official NBB WVV 75/76B"),
    ("bud_evpk_fincost_2025", "2025", "136", "2025 fin kosten 136 vs 146; tick1425; primary official NBB WVV 65/66B"),
    ("bud_evpk_pnl_2025", "2025", "48253", "2025 PnL 48253 vs 20744; tick1425; primary official NBB WVV 9904"),
    ("bud_evpk_pnl_2024", "2024", "20744", "2024 PnL 20744 comparative; tick1425; primary official NBB WVV 9904"),
    ("bud_evpk_div_2025", "2025", "0", "2025 vergoeding inbreng 0 / 694 empty; tick1425; primary official NBB WVV 694"),
    ("bud_evpk_to_res_2025", "2025", "48253", "2025 toevoeging overige reserves 48253; tick1425; primary official NBB WVV 6921"),
    ("bud_evpk_capex_2025", "2025", "0", "2025 capex aanschaf 8169 empty 0; tick1425; primary official NBB WVV 6.1.2"),
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

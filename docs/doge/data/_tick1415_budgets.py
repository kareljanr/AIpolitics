# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_westhoek_dv"
SRC = "src_whdv_jr2025_nbb"
BUDGETS = [
    ("bud_whdv_assets_2025", "2025", "3145801", "2025 assets 3145801 VKT-inb 20/58; tick1415; primary official NBB WVV"),
    ("bud_whdv_assets_2024", "2024", "2988210", "2024 assets 2988210 comparative; tick1415; primary official NBB WVV 20/58"),
    ("bud_whdv_fixed_2025", "2025", "89342", "2025 vaste activa 89342 vs 82854; tick1415; primary official NBB WVV 21/28"),
    ("bud_whdv_mva_2025", "2025", "87795", "2025 MVA 87795 vs 81306; tick1415; primary official NBB WVV 22/27"),
    ("bud_whdv_machines_2025", "2025", "69588", "2025 machines 69588 vs 78212; tick1415; primary official NBB WVV 23"),
    ("bud_whdv_meubilair_2025", "2025", "18207", "2025 meubilair 18207 vs 3094; tick1415; primary official NBB WVV 24"),
    ("bud_whdv_fva_2025", "2025", "1547", "2025 FVA 1547 unchanged; tick1415; primary official NBB WVV 28"),
    ("bud_whdv_current_2025", "2025", "3056458", "2025 vlottend 3056458 vs 2905357; tick1415; primary official NBB WVV 29/58"),
    ("bud_whdv_strecv_2025", "2025", "660589", "2025 ST vorderingen 660589 vs 532618; tick1415; primary official NBB WVV 40/41"),
    ("bud_whdv_trade_recv_2025", "2025", "121364", "2025 handelsvorderingen 121364 vs 152205; tick1415; primary official NBB WVV 40"),
    ("bud_whdv_othrecv_2025", "2025", "539225", "2025 overige vorderingen 539225 JUMP vs 380413; tick1415; primary official NBB WVV 41"),
    ("bud_whdv_invest_2025", "2025", "500000", "2025 geldbeleggingen 500000 vs 600000; tick1415; primary official NBB WVV 50/53"),
    ("bud_whdv_cash_2025", "2025", "1859774", "2025 liquide middelen 1859774 vs 1706742; tick1415; primary official NBB WVV 54/58"),
    ("bud_whdv_cash_2024", "2024", "1706742", "2024 liquide middelen 1706742 comparative; tick1415; primary official NBB WVV 54/58"),
    ("bud_whdv_prepaid_2025", "2025", "36096", "2025 overlopend actief 36096 vs 32793; tick1415; primary official NBB WVV 490/1"),
    ("bud_whdv_equity_2025", "2025", "1987351", "2025 EV 1987351 vs 1885491; tick1415; primary official NBB WVV 10/15"),
    ("bud_whdv_inbreng_2025", "2025", "543455", "2025 inbreng 543455; tick1415; primary official NBB WVV 10/11"),
    ("bud_whdv_reserves_2025", "2025", "1396929", "2025 reserves 1396929 vs 1344010; tick1415; primary official NBB WVV 13"),
    ("bud_whdv_overgedragen_2025", "2025", "46967", "2025 overgedragen 46967 vs -1974; tick1415; primary official NBB WVV 14"),
    ("bud_whdv_debt_2025", "2025", "1158449", "2025 schulden 1158449 vs 1102720; tick1415; primary official NBB WVV 17/49"),
    ("bud_whdv_debt_2024", "2024", "1102720", "2024 schulden 1102720 comparative; tick1415; primary official NBB WVV 17/49"),
    ("bud_whdv_st_2025", "2025", "787498", "2025 ST schulden 787498 vs 893319; tick1415; primary official NBB WVV 42/48"),
    ("bud_whdv_sttrade_2025", "2025", "135198", "2025 leveranciers 135198 vs 116273; tick1415; primary official NBB WVV 440/4"),
    ("bud_whdv_vooruit_2025", "2025", "3599", "2025 vooruitbetalingen 3599; tick1415; primary official NBB WVV 46"),
    ("bud_whdv_tax_st_2025", "2025", "70324", "2025 tax ST 70324 vs 64378; tick1415; primary official NBB WVV 450/3"),
    ("bud_whdv_soc_st_2025", "2025", "354597", "2025 soc ST 354597 vs 358521; tick1415; primary official NBB WVV 454/9"),
    ("bud_whdv_stother_2025", "2025", "223780", "2025 overige ST 223780 vs 354146; tick1415; primary official NBB WVV 47/48"),
    ("bud_whdv_deferred_pass_2025", "2025", "370952", "2025 overlopend passief 370952 JUMP vs 209401; tick1415; primary official NBB WVV 492/3"),
    ("bud_whdv_brutomarge_2025", "2025", "2859900", "2025 brutomarge 2859900 vs 3661785; omzet 70 empty / 60/61 empty; tick1415; primary official NBB WVV 9900"),
    ("bud_whdv_brutomarge_2024", "2024", "3661785", "2024 brutomarge 3661785 comparative; tick1415; primary official NBB WVV 9900"),
    ("bud_whdv_nrec_2025", "2025", "39299", "2025 niet-recurrente bedrijfsopbrengsten 39299; tick1415; primary official NBB WVV 76A"),
    ("bud_whdv_pers_2025", "2025", "2648974", "2025 pers 2648974 vs 2415645 / 34.2 VTE; tick1415; primary official NBB WVV 62"),
    ("bud_whdv_pers_2024", "2024", "2415645", "2024 pers 2415645 comparative; tick1415; primary official NBB WVV 62"),
    ("bud_whdv_afschr_2025", "2025", "11393", "2025 afschrijvingen 11393 vs 8212; tick1415; primary official NBB WVV 630"),
    ("bud_whdv_othcost_2025", "2025", "117720", "2025 andere bedrijfskosten 117720 vs 317984; tick1415; primary official NBB WVV 640/8"),
    ("bud_whdv_expl_2025", "2025", "81814", "2025 expl 81814 vs 917226; tick1415; primary official NBB WVV 9901"),
    ("bud_whdv_expl_2024", "2024", "917226", "2024 expl 917226 comparative; tick1415; primary official NBB WVV 9901"),
    ("bud_whdv_finopbr_2025", "2025", "29264", "2025 fin opbr 29264 vs 42356; tick1415; primary official NBB WVV 75"),
    ("bud_whdv_fincost_2025", "2025", "451", "2025 fin kosten 451 vs 1381; tick1415; primary official NBB WVV 65"),
    ("bud_whdv_tax_2025", "2025", "8766", "2025 tax 8766 vs 12689; tick1415; primary official NBB WVV 67/77"),
    ("bud_whdv_pnl_2025", "2025", "101860", "2025 PnL 101860 vs 945511; tick1415; primary official NBB WVV 9904"),
    ("bud_whdv_pnl_2024", "2024", "945511", "2024 PnL 945511 comparative; tick1415; primary official NBB WVV 9904"),
    ("bud_whdv_div_2025", "2025", "0", "2025 vergoeding inbreng 0 / 694 empty; tick1415; primary official NBB WVV 694"),
    ("bud_whdv_overgedragen_dest_2025", "2025", "46967", "2025 over te dragen winst 46967; tick1415; primary official NBB WVV 14"),
    ("bud_whdv_capex_2025", "2025", "17881", "2025 capex MVA aanschaf 17881; tick1415; primary official NBB WVV 8169"),
    ("bud_whdv_comm_fee_2025", "2025", "7277", "2025 commissaris Walter Hosten Bedrijfsrevisor BV 7277; tick1415; primary official NBB WVV 6.6"),
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

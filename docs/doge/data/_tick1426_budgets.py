# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_enpk"
SRC = "src_enpk_jr2025_nbb"
BUDGETS = [
    ("bud_enpk_assets_2025", "2025", "480193", "2025 assets 480193 VKT-inb 20/58; tick1426; primary official NBB WVV"),
    ("bud_enpk_assets_2024", "2024", "426347", "2024 assets 426347 comparative; tick1426; primary official NBB WVV 20/58"),
    ("bud_enpk_fixed_2025", "2025", "9553", "2025 vaste activa 9553 vs 12405; tick1426; primary official NBB WVV 21/28"),
    ("bud_enpk_iva_2025", "2025", "654", "2025 IVA 654 vs 1133; tick1426; primary official NBB WVV 21"),
    ("bud_enpk_mva_2025", "2025", "8824", "2025 MVA 8824 vs 11198; tick1426; primary official NBB WVV 22/27"),
    ("bud_enpk_mva_mach_2025", "2025", "1887", "2025 machines 1887 vs 5563; tick1426; primary official NBB WVV 23"),
    ("bud_enpk_mva_meub_2025", "2025", "6938", "2025 meubilair 6938 vs 5635; tick1426; primary official NBB WVV 24"),
    ("bud_enpk_mva_aanschaf_2025", "2025", "87559", "2025 MVA aanschaf YE 87559; tick1426; primary official NBB WVV 8199"),
    ("bud_enpk_mva_afschr_2025", "2025", "78735", "2025 MVA afschr YE 78735; tick1426; primary official NBB WVV 8329"),
    ("bud_enpk_fva_2025", "2025", "74", "2025 FVA 74 vs 74; tick1426; primary official NBB WVV 28"),
    ("bud_enpk_current_2025", "2025", "470640", "2025 vlottend 470640 vs 413942; tick1426; primary official NBB WVV 29/58"),
    ("bud_enpk_strecv_2025", "2025", "74951", "2025 ST vorderingen 74951 vs 73823; tick1426; primary official NBB WVV 40/41"),
    ("bud_enpk_trade_recv_2025", "2025", "3349", "2025 handelsvorderingen 3349 vs 2000; tick1426; primary official NBB WVV 40"),
    ("bud_enpk_other_recv_2025", "2025", "71602", "2025 overige vorderingen 71602 vs 71823 unpublished counterpart; tick1426; primary official NBB WVV 41"),
    ("bud_enpk_other_recv_2024", "2024", "71823", "2024 overige vorderingen 71823 comparative; tick1426; primary official NBB WVV 41"),
    ("bud_enpk_cash_2025", "2025", "376948", "2025 liquide middelen 376948 UP vs 325115; tick1426; primary official NBB WVV 54/58"),
    ("bud_enpk_cash_2024", "2024", "325115", "2024 liquide middelen 325115 comparative; tick1426; primary official NBB WVV 54/58"),
    ("bud_enpk_prepaid_2025", "2025", "18741", "2025 prepaid 18741 vs 15004; tick1426; primary official NBB WVV 490/1"),
    ("bud_enpk_equity_2025", "2025", "401292", "2025 EV 401292 vs 344661; tick1426; primary official NBB WVV 10/15"),
    ("bud_enpk_equity_2024", "2024", "344661", "2024 EV 344661 comparative; tick1426; primary official NBB WVV 10/15"),
    ("bud_enpk_overgedragen_2025", "2025", "401292", "2025 overgedragen winst 401292 vs 344661; tick1426; primary official NBB WVV 14"),
    ("bud_enpk_debt_2025", "2025", "78901", "2025 schulden 78901 vs 81686; tick1426; primary official NBB WVV 17/49"),
    ("bud_enpk_debt_2024", "2024", "81686", "2024 schulden 81686 comparative; tick1426; primary official NBB WVV 17/49"),
    ("bud_enpk_st_2025", "2025", "78901", "2025 ST 78901 vs 81686 no LT; tick1426; primary official NBB WVV 42/48"),
    ("bud_enpk_sttrade_2025", "2025", "14258", "2025 leveranciers 14258 vs 11154 unpublished counterpart; tick1426; primary official NBB WVV 440/4"),
    ("bud_enpk_taxsoc_2025", "2025", "64643", "2025 tax/soc 64643 vs 70532; tick1426; primary official NBB WVV 45"),
    ("bud_enpk_bezold_2025", "2025", "56529", "2025 bezoldigingen ST 56529 vs 63006; tick1426; primary official NBB WVV 454/9"),
    ("bud_enpk_brutomarge_2025", "2025", "831915", "2025 brutomarge 831915 vs 844635; omzet 70 empty / 60/61 empty; tick1426; primary official NBB WVV 9900"),
    ("bud_enpk_brutomarge_2024", "2024", "844635", "2024 brutomarge 844635 comparative; tick1426; primary official NBB WVV 9900"),
    ("bud_enpk_pers_2025", "2025", "767960", "2025 pers 767960 vs 778231; VTE 9.2 vs 11.7; tick1426; primary official NBB WVV 62"),
    ("bud_enpk_pers_2024", "2024", "778231", "2024 pers 778231 comparative; tick1426; primary official NBB WVV 62"),
    ("bud_enpk_afschr_2025", "2025", "6936", "2025 afschr 6936 vs 6815; tick1426; primary official NBB WVV 630"),
    ("bud_enpk_andere_kost_2025", "2025", "0", "2025 andere bedrijfskosten 0 vs 7; tick1426; primary official NBB WVV 640/8"),
    ("bud_enpk_expl_2025", "2025", "57018", "2025 expl 57018 vs 59582; tick1426; primary official NBB WVV 9901"),
    ("bud_enpk_expl_2024", "2024", "59582", "2024 expl 59582 comparative; tick1426; primary official NBB WVV 9901"),
    ("bud_enpk_fininc_2025", "2025", "0", "2025 fin opbr 0 vs 0; tick1426; primary official NBB WVV 75/76B"),
    ("bud_enpk_fincost_2025", "2025", "386", "2025 fin kosten 386 vs 370; tick1426; primary official NBB WVV 65/66B"),
    ("bud_enpk_pnl_2025", "2025", "56632", "2025 PnL 56632 vs 59212; tick1426; primary official NBB WVV 9904"),
    ("bud_enpk_pnl_2024", "2024", "59212", "2024 PnL 59212 comparative; tick1426; primary official NBB WVV 9904"),
    ("bud_enpk_div_2025", "2025", "0", "2025 vergoeding inbreng 0 / 694 empty; tick1426; primary official NBB WVV 694"),
    ("bud_enpk_capex_2025", "2025", "4084", "2025 capex MVA aanschaf 8169=4084; IVA/FVA aanschaf empty; tick1426; primary official NBB WVV 6.1.2"),
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

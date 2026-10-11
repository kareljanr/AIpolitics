# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_kstf"
SRC = "src_kstf_jr2025_nbb"
BUDGETS = [
    ("bud_kstf_assets_2025", "2025", "162729", "2025 assets 162729 MIC-VZW 20/58; tick1429; primary official NBB WVV"),
    ("bud_kstf_assets_2024", "2024", "175242", "2024 assets 175242 comparative; tick1429; primary official NBB WVV 20/58"),
    ("bud_kstf_fixed_2025", "2025", "512", "2025 vaste activa 512 vs 1521; tick1429; primary official NBB WVV 21/28"),
    ("bud_kstf_mva_2025", "2025", "512", "2025 MVA 512 meubilair only; aanschaf YE 18347 / afschr YE 17834; tick1429; primary official NBB WVV 22/27"),
    ("bud_kstf_current_2025", "2025", "162217", "2025 vlottend 162217 vs 173720; tick1429; primary official NBB WVV 29/58"),
    ("bud_kstf_recv_2025", "2025", "120", "2025 ST recv 120 all trade vs 0; tick1429; primary official NBB WVV 40/41"),
    ("bud_kstf_cash_2025", "2025", "153074", "2025 liquide middelen 153074 DROP vs 165432; tick1429; primary official NBB WVV 54/58"),
    ("bud_kstf_cash_2024", "2024", "165432", "2024 liquide middelen 165432 comparative; tick1429; primary official NBB WVV 54/58"),
    ("bud_kstf_prepaid_2025", "2025", "9023", "2025 prepaid 9023 vs 8289; tick1429; primary official NBB WVV 490/1"),
    ("bud_kstf_equity_2025", "2025", "100647", "2025 EV 100647 overgedragen DROP vs 116827; tick1429; primary official NBB WVV 10/15"),
    ("bud_kstf_equity_2024", "2024", "116827", "2024 EV 116827 comparative; tick1429; primary official NBB WVV 10/15"),
    ("bud_kstf_debt_2025", "2025", "62082", "2025 schulden 62082 vs 58415; tick1429; primary official NBB WVV 17/49"),
    ("bud_kstf_debt_2024", "2024", "58415", "2024 schulden 58415 comparative; tick1429; primary official NBB WVV 17/49"),
    ("bud_kstf_st_2025", "2025", "62082", "2025 ST 62082 vs 58415 no LT; tick1429; primary official NBB WVV 42/48"),
    ("bud_kstf_sttrade_2025", "2025", "9714", "2025 leveranciers 9714 JUMP vs 5542 unpublished counterpart; tick1429; primary official NBB WVV 440/4"),
    ("bud_kstf_taxsoc_2025", "2025", "52368", "2025 tax+soc 52368 vs 52872; tick1429; primary official NBB WVV 45"),
    ("bud_kstf_tax_2025", "2025", "13471", "2025 belastingen 13471 vs 14017; tick1429; primary official NBB WVV 450/3"),
    ("bud_kstf_soc_2025", "2025", "38897", "2025 bezoldigingen/sociale lasten 38897 vs 38855; tick1429; primary official NBB WVV 454/9"),
    ("bud_kstf_brutomarge_2025", "2025", "248766", "2025 brutomarge 248766 vs 209344; omzet 70 empty; 73 empty; 60/61 empty; tick1429; primary official NBB WVV 9900"),
    ("bud_kstf_brutomarge_2024", "2024", "209344", "2024 brutomarge 209344 comparative; tick1429; primary official NBB WVV 9900"),
    ("bud_kstf_pers_2025", "2025", "263807", "2025 pers 263807 / 3.4 VTE / 5792 uur / YE 2.9 vs 248754 / 3.0 VTE; tick1429; primary official NBB WVV 62 + 6.4"),
    ("bud_kstf_pers_2024", "2024", "248754", "2024 pers 248754 comparative; tick1429; primary official NBB WVV 62"),
    ("bud_kstf_afschr_2025", "2025", "1009", "2025 afschr 1009 vs 1140; tick1429; primary official NBB WVV 630"),
    ("bud_kstf_expl_2025", "2025", "-16116", "2025 expl -16116 vs -40614; tick1429; primary official NBB WVV 9901"),
    ("bud_kstf_expl_2024", "2024", "-40614", "2024 expl -40614 comparative; tick1429; primary official NBB WVV 9901"),
    ("bud_kstf_finopbr_2025", "2025", "1", "2025 fin opbr 1; tick1429; primary official NBB WVV 75"),
    ("bud_kstf_finkost_2025", "2025", "65", "2025 fin kosten 65 vs 141; tick1429; primary official NBB WVV 65"),
    ("bud_kstf_pnl_2025", "2025", "-16180", "2025 PnL -16180 vs -42415; tick1429; primary official NBB WVV 9904"),
    ("bud_kstf_pnl_2024", "2024", "-42415", "2024 PnL -42415 comparative; tick1429; primary official NBB WVV 9904"),
    ("bud_kstf_div_2025", "2025", "0", "2025 dividend 0 / no 694 on MIC-VZW; tick1429; primary official NBB WVV"),
    ("bud_kstf_capex_2025", "2025", "0", "2025 capex 0; MVA aanschaffingen 8169 empty; IVA aanschaffingen 8029 empty; tick1429; primary official NBB WVV 6.1.1/6.1.2"),
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

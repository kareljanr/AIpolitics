# -*- coding: utf-8 -*-
import csv, sys, io
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "nv_bnlg"
SRC = "src_bnlg_jr2025_nbb"
BUDGETS = [
    ("bud_bnlg_assets_2025", "2025", "3510439", "2025 assets 3510439 VOL-kap 20/58; tick1423; primary official NBB WVV"),
    ("bud_bnlg_assets_2024", "2024", "3671944", "2024 assets 3671944 comparative; tick1423; primary official NBB WVV 20/58"),
    ("bud_bnlg_fixed_2025", "2025", "2173442", "2025 vaste activa 2173442 vs 2286134; tick1423; primary official NBB WVV 21/28"),
    ("bud_bnlg_mva_2025", "2025", "2168237", "2025 MVA 2168237 vs 2280929; tick1423; primary official NBB WVV 22/27"),
    ("bud_bnlg_mva_geb_2025", "2025", "13258", "2025 terreinen/gebouwen 13258 vs 17443; tick1423; primary official NBB WVV 22"),
    ("bud_bnlg_mva_meub_2025", "2025", "1799979", "2025 meubilair/rollend 1799979 vs 2263486; tick1423; primary official NBB WVV 24"),
    ("bud_bnlg_mva_cip_2025", "2025", "355000", "2025 CIP/vooruit 355000 (elektrische vrachtwagen onderbouw); tick1423; primary official NBB WVV 27"),
    ("bud_bnlg_fva_2025", "2025", "5205", "2025 FVA 5205 (verbonden 2000 + borgtochten 3205); tick1423; primary official NBB WVV 28"),
    ("bud_bnlg_current_2025", "2025", "1336998", "2025 vlottend 1336998 vs 1385810; tick1423; primary official NBB WVV 29/58"),
    ("bud_bnlg_strecv_2025", "2025", "366260", "2025 ST vorderingen 366260 vs 403916; tick1423; primary official NBB WVV 40/41"),
    ("bud_bnlg_trade_recv_2025", "2025", "351381", "2025 handelsvorderingen 351381 vs 386105; tick1423; primary official NBB WVV 40"),
    ("bud_bnlg_other_recv_2025", "2025", "14879", "2025 overige vorderingen 14879 vs 17811; tick1423; primary official NBB WVV 41"),
    ("bud_bnlg_invest_2025", "2025", "10402", "2025 geldbeleggingen 10402 DROP vs 257441 (termijn); tick1423; primary official NBB WVV 50/53"),
    ("bud_bnlg_invest_2024", "2024", "257441", "2024 geldbeleggingen 257441 comparative; tick1423; primary official NBB WVV 50/53"),
    ("bud_bnlg_cash_2025", "2025", "956680", "2025 liquide middelen 956680 JUMP vs 718496; tick1423; primary official NBB WVV 54/58"),
    ("bud_bnlg_cash_2024", "2024", "718496", "2024 liquide middelen 718496 comparative; tick1423; primary official NBB WVV 54/58"),
    ("bud_bnlg_prepaid_2025", "2025", "3655", "2025 prepaid 3655 vs 5957; tick1423; primary official NBB WVV 490/1"),
    ("bud_bnlg_equity_2025", "2025", "1664756", "2025 EV 1664756 vs 1499933; tick1423; primary official NBB WVV 10/15"),
    ("bud_bnlg_equity_2024", "2024", "1499933", "2024 EV 1499933 comparative; tick1423; primary official NBB WVV 10/15"),
    ("bud_bnlg_kapitaal_2025", "2025", "1000000", "2025 geplaatst kapitaal 1000000; tick1423; primary official NBB WVV 100"),
    ("bud_bnlg_wett_res_2025", "2025", "44473", "2025 wettelijke reserve 44473 vs 37350; tick1423; primary official NBB WVV 130"),
    ("bud_bnlg_overgedragen_2025", "2025", "597918", "2025 overgedragen 597918 vs 462583; tick1423; primary official NBB WVV 14"),
    ("bud_bnlg_capsub_2025", "2025", "22365", "2025 kapitaalsubsidies 22365 (2024 empty); tick1423; primary official NBB WVV 15"),
    ("bud_bnlg_debt_2025", "2025", "1845683", "2025 schulden 1845683 vs 2172011; tick1423; primary official NBB WVV 17/49"),
    ("bud_bnlg_debt_2024", "2024", "2172011", "2024 schulden 2172011 comparative; tick1423; primary official NBB WVV 17/49"),
    ("bud_bnlg_lt_2025", "2025", "1134979", "2025 LT 1134979 vs 1479264 (kredietinstellingen); tick1423; primary official NBB WVV 17"),
    ("bud_bnlg_st_2025", "2025", "710704", "2025 ST 710704 vs 692747; tick1423; primary official NBB WVV 42/48"),
    ("bud_bnlg_ltdue_2025", "2025", "344285", "2025 LT-due-within-year 344285 vs 341988; tick1423; primary official NBB WVV 42"),
    ("bud_bnlg_sttrade_2025", "2025", "331702", "2025 leveranciers 331702 JUMP vs 100702; tick1423; primary official NBB WVV 440/4"),
    ("bud_bnlg_sttrade_2024", "2024", "100702", "2024 leveranciers 100702 comparative; tick1423; primary official NBB WVV 440/4"),
    ("bud_bnlg_tax_2025", "2025", "5428", "2025 belastingen 5428; tick1423; primary official NBB WVV 450/3"),
    ("bud_bnlg_other_st_2025", "2025", "29289", "2025 overige ST 29289 DROP vs 250057; tick1423; primary official NBB WVV 47/48"),
    ("bud_bnlg_other_st_2024", "2024", "250057", "2024 overige ST 250057 comparative; tick1423; primary official NBB WVV 47/48"),
    ("bud_bnlg_omzet_2025", "2025", "1717525", "2025 omzet 1717525 vs 1966670; 6.10 category/geo empty; tick1423; primary official NBB WVV 70"),
    ("bud_bnlg_omzet_2024", "2024", "1966670", "2024 omzet 1966670 comparative; tick1423; primary official NBB WVV 70"),
    ("bud_bnlg_othops_2025", "2025", "344859", "2025 andere bedrijfsopbrengsten 344859 JUMP vs 168286; tick1423; primary official NBB WVV 74"),
    ("bud_bnlg_opsinc_2025", "2025", "2062384", "2025 bedrijfsopbrengsten 2062384 vs 2139956; tick1423; primary official NBB WVV 70/76A"),
    ("bud_bnlg_diensten_2025", "2025", "1289949", "2025 diensten 1289949 vs 1367843 unpublished as a split; tick1423; primary official NBB WVV 61"),
    ("bud_bnlg_diensten_2024", "2024", "1367843", "2024 diensten 1367843 comparative; tick1423; primary official NBB WVV 61"),
    ("bud_bnlg_afschr_2025", "2025", "467692", "2025 afschr 467692 vs 469156; tick1423; primary official NBB WVV 630"),
    ("bud_bnlg_andere_kost_2025", "2025", "109134", "2025 andere bedrijfskosten 109134 (640 107048 + 641/8 2086); tick1423; primary official NBB WVV 640/8"),
    ("bud_bnlg_expl_2025", "2025", "194221", "2025 expl 194221 vs 205363; tick1423; primary official NBB WVV 9901"),
    ("bud_bnlg_expl_2024", "2024", "205363", "2024 expl 205363 comparative; tick1423; primary official NBB WVV 9901"),
    ("bud_bnlg_fininc_2025", "2025", "8508", "2025 fin opbr 8508 vs 7617; tick1423; primary official NBB WVV 75/76B"),
    ("bud_bnlg_fincost_2025", "2025", "12785", "2025 fin kosten 12785 vs 15454; tick1423; primary official NBB WVV 65/66B"),
    ("bud_bnlg_tax_pnl_2025", "2025", "47486", "2025 tax 47486 vs 54543; tick1423; primary official NBB WVV 67/77"),
    ("bud_bnlg_pnl_2025", "2025", "142458", "2025 PnL 142458 vs 142983; tick1423; primary official NBB WVV 9904"),
    ("bud_bnlg_pnl_2024", "2024", "142983", "2024 PnL 142983 comparative; tick1423; primary official NBB WVV 9904"),
    ("bud_bnlg_div_2025", "2025", "0", "2025 vergoeding inbreng 0 / 694 empty; tick1423; primary official NBB WVV 694"),
    ("bud_bnlg_capex_2025", "2025", "355000", "2025 capex 355000 CIP aanschaf 8166 (elektrische vrachtwagen onderbouw); meubilair aanschaf empty; tick1423; primary official NBB WVV 6.3.6"),
    ("bud_bnlg_commissaris_2025", "2025", "3740", "2025 commissaris BDO 3740; tick1423; primary official NBB WVV 9505"),
    ("bud_bnlg_rel_debt_2025", "2025", "153046", "2025 schulden verbonden 153046 vs 267534; tick1423; primary official NBB WVV 9351"),
    ("bud_bnlg_rel_recv_assoc_2025", "2025", "338386", "2025 vorderingen geassocieerde 338386 vs 385850; tick1423; primary official NBB WVV 9293"),
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

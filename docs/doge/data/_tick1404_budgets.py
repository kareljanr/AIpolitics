# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_psln"
SRC = "src_psln_jr2025_nbb"
BUDGETS = [
    ("bud_psln_assets_2025", "2025", "8627377", "2025 assets 8627377 VKT-inb 20/58; tick1404; primary official NBB WVV"),
    ("bud_psln_assets_2024", "2024", "8459315", "2024 assets 8459315 comparative; tick1404; primary official NBB WVV 20/58"),
    ("bud_psln_fixed_2025", "2025", "5572101", "2025 vaste activa 5572101 all MVA; tick1404; primary official NBB WVV 21/28"),
    ("bud_psln_mva_2025", "2025", "5572101", "2025 MVA 5572101 vs 5791883; tick1404; primary official NBB WVV 22/27"),
    ("bud_psln_gebouwen_2025", "2025", "5244300", "2025 terreinen/gebouwen 5244300; tick1404; primary official NBB WVV 22"),
    ("bud_psln_machines_2025", "2025", "203073", "2025 machines 203073 vs 262604; tick1404; primary official NBB WVV 23"),
    ("bud_psln_meubilair_2025", "2025", "109577", "2025 meubilair 109577 vs 101530; tick1404; primary official NBB WVV 24"),
    ("bud_psln_overige_mva_2025", "2025", "15151", "2025 overige MVA 15151; tick1404; primary official NBB WVV 26"),
    ("bud_psln_current_2025", "2025", "3055276", "2025 vlottend 3055276 vs 2667432; tick1404; primary official NBB WVV 29/58"),
    ("bud_psln_inventory_2025", "2025", "23818", "2025 voorraden 23818 (urnen+Horizon); tick1404; primary official NBB WVV 30/36"),
    ("bud_psln_strecv_2025", "2025", "325270", "2025 ST vorderingen 325270 DROP vs 461418; tick1404; primary official NBB WVV 40/41"),
    ("bud_psln_trade_recv_2025", "2025", "321464", "2025 handelsvorderingen 321464 DROP vs 442670; tick1404; primary official NBB WVV 40"),
    ("bud_psln_invest_2025", "2025", "1902705", "2025 geldbeleggingen 1902705 JUMP vs 1484358; tick1404; primary official NBB WVV 50/53"),
    ("bud_psln_invest_2024", "2024", "1484358", "2024 geldbeleggingen 1484358 comparative; tick1404; primary official NBB WVV 50/53"),
    ("bud_psln_cash_2025", "2025", "776217", "2025 liquide middelen 776217 JUMP vs 636453; tick1404; primary official NBB WVV 54/58"),
    ("bud_psln_cash_2024", "2024", "636453", "2024 liquide middelen 636453 comparative; tick1404; primary official NBB WVV 54/58"),
    ("bud_psln_prepaid_2025", "2025", "27266", "2025 overlopend actief 27266; tick1404; primary official NBB WVV 490/1"),
    ("bud_psln_equity_2025", "2025", "6113421", "2025 EV 6113421 vs 5668091; tick1404; primary official NBB WVV 10/15"),
    ("bud_psln_inbreng_2025", "2025", "2090100", "2025 onbeschikbare inbreng 2090100; tick1404; primary official NBB WVV 111"),
    ("bud_psln_reserves_2025", "2025", "212290", "2025 statutair onbeschikbare reserves 212290; tick1404; primary official NBB WVV 1311"),
    ("bud_psln_retained_2025", "2025", "2766813", "2025 overgedragen winst 2766813 vs 2267981; tick1404; primary official NBB WVV 14"),
    ("bud_psln_capsub_2025", "2025", "1044218", "2025 kapitaalsubsidies 1044218 vs 1097720; tick1404; primary official NBB WVV 15"),
    ("bud_psln_prov_2025", "2025", "327247", "2025 voorzieningen 327247 JUMP vs 180151 (herstel); tick1404; primary official NBB WVV 16"),
    ("bud_psln_prov_herstel_2025", "2025", "327247", "2025 voorziening herstel 327247 JUMP vs 180151; tick1404; primary official NBB WVV 162"),
    ("bud_psln_debt_2025", "2025", "2186709", "2025 schulden 2186709 DROP vs 2611073; tick1404; primary official NBB WVV 17/49"),
    ("bud_psln_debt_2024", "2024", "2611073", "2024 schulden 2611073 comparative; tick1404; primary official NBB WVV 17/49"),
    ("bud_psln_lt_2025", "2025", "1534741", "2025 LT bank 1534741 vs 1915266; tick1404; primary official NBB WVV 17"),
    ("bud_psln_st_2025", "2025", "651968", "2025 ST schulden 651968 vs 695742; tick1404; primary official NBB WVV 42/48"),
    ("bud_psln_ltdue_2025", "2025", "439578", "2025 LT-due binnen jaar 439578; tick1404; primary official NBB WVV 42"),
    ("bud_psln_sttrade_2025", "2025", "86981", "2025 leveranciers 86981 DROP vs 136255; tick1404; primary official NBB WVV 440/4"),
    ("bud_psln_taxsoc_2025", "2025", "125409", "2025 tax/soc 125409 (tax 11651 + soc 113758); tick1404; primary official NBB WVV 45"),
    ("bud_psln_govguar_2025", "2025", "1974319", "2025 door Belgische overheidsinstellingen gewaarborgde schulden 1974319; tick1404; primary official NBB WVV 9061"),
    ("bud_psln_vennoten_guar_2025", "2025", "6200000", "2025 openstaande fin schulden gewaarborgd door alle leden 6200000; tick1404; primary official NBB WVV 6.5"),
    ("bud_psln_brutomarge_2025", "2025", "1935397", "2025 brutomarge 1935397 vs 1881382; omzet 70 empty / 60/61 empty; tick1404; primary official NBB WVV 9900"),
    ("bud_psln_brutomarge_2024", "2024", "1881382", "2024 brutomarge 1881382 comparative; tick1404; primary official NBB WVV 9900"),
    ("bud_psln_pers_2025", "2025", "877307", "2025 personeel 877307 vs 906070; 9 VTE (was 10); tick1404; primary official NBB WVV 62"),
    ("bud_psln_pers_2024", "2024", "906070", "2024 personeel 906070 comparative; tick1404; primary official NBB WVV 62"),
    ("bud_psln_afschr_2025", "2025", "389875", "2025 afschrijvingen 389875 vs 359146; tick1404; primary official NBB WVV 630"),
    ("bud_psln_prov_add_2025", "2025", "147096", "2025 toevoeging voorzieningen 147096 vs 77208; tick1404; primary official NBB WVV 635/8"),
    ("bud_psln_expl_2025", "2025", "520061", "2025 expl 520061 vs 531879; tick1404; primary official NBB WVV 9901"),
    ("bud_psln_expl_2024", "2024", "531879", "2024 expl 531879 comparative; tick1404; primary official NBB WVV 9901"),
    ("bud_psln_fininc_2025", "2025", "76575", "2025 fin opbr 76575 (capsub in resultaat 53501.53); tick1404; primary official NBB WVV 75"),
    ("bud_psln_fincost_2025", "2025", "89940", "2025 fin kosten 89940 vs 156440; tick1404; primary official NBB WVV 65"),
    ("bud_psln_tax_2025", "2025", "7864", "2025 belastingen 7864 vs 9889; tick1404; primary official NBB WVV 67/77"),
    ("bud_psln_pnl_2025", "2025", "498832", "2025 PnL 498832 vs 450078 all overgedragen; tick1404; primary official NBB WVV 9904"),
    ("bud_psln_pnl_2024", "2024", "450078", "2024 PnL 450078 comparative; tick1404; primary official NBB WVV 9904"),
    ("bud_psln_capex_2025", "2025", "170092", "2025 capex MVA aanschaf 170092; tick1404; primary official NBB WVV 8169"),
    ("bud_psln_commissaris_2025", "2025", "4000", "2025 commissaris Boes & Verrue 4000; tick1404; primary official NBB WVV 6.6"),
    ("bud_psln_capsub_pnl_2025", "2025", "53502", "2025 kapitaalsubsidies in resultaat 53501.53; tick1404; primary official NBB WVV 6.8"),
]
rows = [{
    "budget_id": bid, "entity_id": ENT, "year": year, "amount_eur": amt,
    "amount_min_eur": "", "amount_max_eur": "", "basis": "executed",
    "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, year, amt, notes in BUDGETS]
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    seen = {row[fields[0]] for row in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    for row in rows:
        if row[fields[0]] in seen:
            continue
        w.writerow({k: row.get(k, "") for k in fields})
        added += 1
print("budgets", added)

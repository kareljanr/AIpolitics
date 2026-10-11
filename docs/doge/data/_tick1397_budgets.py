# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_ivbc"
SRC = "src_ivbc_jr2025_nbb"
BUDGETS = [
    ("bud_ivbc_assets_2025", "2025", "919753", "2025 assets 919753 VKT-inb 20/58; commissaris 919752.75; tick1397; primary official NBB WVV"),
    ("bud_ivbc_assets_2024", "2024", "780057", "2024 assets 780057 comparative; tick1397; primary official NBB WVV 20/58"),
    ("bud_ivbc_fixed_2025", "2025", "148430", "2025 vaste activa 148430 vs 121195; tick1397; primary official NBB WVV 21/28"),
    ("bud_ivbc_iva_2025", "2025", "15053", "2025 IVA 15053 vs empty; tick1397; primary official NBB WVV 21"),
    ("bud_ivbc_mva_2025", "2025", "133377", "2025 MVA 133377 vs 121195; tick1397; primary official NBB WVV 22/27"),
    ("bud_ivbc_buildings_2025", "2025", "4938", "2025 terreinen/gebouwen 4938 vs 5318; tick1397; primary official NBB WVV 22"),
    ("bud_ivbc_machines_2025", "2025", "90169", "2025 machines 90169 vs 102109; tick1397; primary official NBB WVV 23"),
    ("bud_ivbc_furniture_2025", "2025", "12549", "2025 meubilair 12549 vs 13769; tick1397; primary official NBB WVV 24"),
    ("bud_ivbc_othmva_2025", "2025", "25721", "2025 overige MVA 25721 vs empty; tick1397; primary official NBB WVV 26"),
    ("bud_ivbc_current_2025", "2025", "771323", "2025 vlottend 771323 vs 658862; tick1397; primary official NBB WVV 29/58"),
    ("bud_ivbc_stocks_2025", "2025", "137079", "2025 voorraden 137079 vs 136543 uitleenmateriaal; tick1397; primary official NBB WVV 30/36"),
    ("bud_ivbc_strecv_2025", "2025", "140032", "2025 ST vorderingen 140032 vs 59157; tick1397; primary official NBB WVV 40/41"),
    ("bud_ivbc_trade_2025", "2025", "105397", "2025 handelsvorderingen 105397 vs 45520; tick1397; primary official NBB WVV 40"),
    ("bud_ivbc_othrecv_2025", "2025", "34636", "2025 overige vorderingen 34636 JUMP vs 13636; tick1397; primary official NBB WVV 41"),
    ("bud_ivbc_invest_2025", "2025", "8728", "2025 geldbeleggingen 8728 unchanged; tick1397; primary official NBB WVV 50/53"),
    ("bud_ivbc_cash_2025", "2025", "455342", "2025 liquide middelen 455342 vs 420551; tick1397; primary official NBB WVV 54/58"),
    ("bud_ivbc_cash_2024", "2024", "420551", "2024 liquide middelen 420551 comparative; tick1397; primary official NBB WVV 54/58"),
    ("bud_ivbc_prepaid_2025", "2025", "30142", "2025 overlopend actief 30142 vs 33884; tick1397; primary official NBB WVV 490/1"),
    ("bud_ivbc_equity_2025", "2025", "581329", "2025 EV 581329 vs 520485; tick1397; primary official NBB WVV 10/15"),
    ("bud_ivbc_inbreng_2025", "2025", "449877", "2025 inbreng 449877 (beschikbaar 68875 / onbeschikbaar 381002); tick1397; primary official NBB WVV 10/11"),
    ("bud_ivbc_reserves_2025", "2025", "57058", "2025 reserves 57058 (onbeschikbaar 13557 / beschikbaar 43501); tick1397; primary official NBB WVV 13"),
    ("bud_ivbc_re_2025", "2025", "74394", "2025 overgedragen winst 74394 vs 28761; tick1397; primary official NBB WVV 14"),
    ("bud_ivbc_debt_2025", "2025", "338424", "2025 schulden 338424 vs 259572; tick1397; primary official NBB WVV 17/49"),
    ("bud_ivbc_debt_2024", "2024", "259572", "2024 schulden 259572 comparative; tick1397; primary official NBB WVV 17/49"),
    ("bud_ivbc_st_2025", "2025", "249943", "2025 ST schulden 249943 vs 195240; no LT; tick1397; primary official NBB WVV 42/48"),
    ("bud_ivbc_sttrade_2025", "2025", "86237", "2025 leveranciers 86237 vs 56191; tick1397; primary official NBB WVV 440/4"),
    ("bud_ivbc_stsoc_2025", "2025", "131780", "2025 bezoldigingen/sociale lasten 131780 vs 131377; tick1397; primary official NBB WVV 454/9"),
    ("bud_ivbc_deferred_2025", "2025", "88480", "2025 overlopend passief 88480 vs 64332; tick1397; primary official NBB WVV 492/3"),
    ("bud_ivbc_brutomarge_2025", "2025", "1211667", "2025 brutomarge 1211667 vs 1176709; omzet 70 empty; tick1397; primary official NBB WVV 9900"),
    ("bud_ivbc_brutomarge_2024", "2024", "1176709", "2024 brutomarge 1176709 comparative; tick1397; primary official NBB WVV 9900"),
    ("bud_ivbc_omzet_jv_2025", "2025", "207858", "2025 omzet 207858.25 jaarverslag (WVV 70 empty); tick1397; primary official NBB WVV jaarverslag"),
    ("bud_ivbc_othinc_jv_2025", "2025", "1382095", "2025 andere bedrijfsopbrengsten 1382095.14 jaarverslag; tick1397; primary official NBB WVV jaarverslag"),
    ("bud_ivbc_diensten_jv_2025", "2025", "370466", "2025 diverse goederen en diensten 370465.83 jaarverslag (60/61 empty); tick1397; primary official NBB WVV jaarverslag"),
    ("bud_ivbc_subs_2025", "2025", "148220", "2025 publieke subsidies listed 148220.28 (Maribel/VIA/Kunstkuur/academie); tick1397; primary official NBB WVV 6.8"),
    ("bud_ivbc_pers_2025", "2025", "1023843", "2025 pers 1023843 vs 1038305 / 12.2 VTE; tick1397; primary official NBB WVV 62"),
    ("bud_ivbc_pers_2024", "2024", "1038305", "2024 pers 1038305 / 12.8 VTE comparative; tick1397; primary official NBB WVV 62"),
    ("bud_ivbc_afschr_2025", "2025", "31356", "2025 afschr 31356 vs 30376; tick1397; primary official NBB WVV 630"),
    ("bud_ivbc_wv_2025", "2025", "69937", "2025 WV voorraden/collecties 69937 vs 71751; tick1397; primary official NBB WVV 631/4"),
    ("bud_ivbc_othcost_2025", "2025", "25780", "2025 andere bedrijfskosten 25780 vs empty; tick1397; primary official NBB WVV 640/8"),
    ("bud_ivbc_expl_2025", "2025", "60751", "2025 expl +60751 vs +36277; tick1397; primary official NBB WVV 9901"),
    ("bud_ivbc_expl_2024", "2024", "36277", "2024 expl +36277 comparative; tick1397; primary official NBB WVV 9901"),
    ("bud_ivbc_pnl_2025", "2025", "60844", "2025 PnL +60844 vs +38348; commissaris 60843.93; tick1397; primary official NBB WVV 9904"),
    ("bud_ivbc_pnl_2024", "2024", "38348", "2024 PnL +38348 comparative; tick1397; primary official NBB WVV 9904"),
    ("bud_ivbc_div_2025", "2025", "0", "2025 dividend 694 empty; tick1397; primary official NBB WVV 694"),
    ("bud_ivbc_capex_mva_2025", "2025", "42867", "2025 MVA aanschaf 42867 (8169); tick1397; primary official NBB WVV 6.1.2"),
    ("bud_ivbc_capex_iva_2025", "2025", "16928", "2025 IVA aanschaf 16928 (8029); tick1397; primary official NBB WVV 6.1.1"),
    ("bud_ivbc_comm_2025", "2025", "3751", "2025 commissaris Clybouw 3751 excl btw 3100; tick1397; primary official NBB WVV 6.6"),
]
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    ids = {x.get("budget_id") for x in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    for bid, year, amt, notes in BUDGETS:
        if bid in ids:
            continue
        w.writerow({
            "budget_id": bid, "entity_id": ENT, "year": year, "amount_eur": amt,
            "amount_min_eur": "", "amount_max_eur": "", "basis": "executed",
            "source_id": SRC, "confidence": "strong", "notes": notes,
        })
        added += 1
print("budgets", added)

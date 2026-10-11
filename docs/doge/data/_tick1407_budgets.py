# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "agb_ptri"
SRC = "src_ptri_jr2025_nbb"
BUDGETS = [
    ("bud_ptri_assets_2025", "2025", "9688747", "2025 assets 9688747 VKT-inb 20/58; tick1407; primary official NBB WVV"),
    ("bud_ptri_assets_2024", "2024", "9745079", "2024 assets 9745079 comparative; tick1407; primary official NBB WVV 20/58"),
    ("bud_ptri_fixed_2025", "2025", "7691172", "2025 vaste activa 7691172 vs 8001858; tick1407; primary official NBB WVV 21/28"),
    ("bud_ptri_iva_2025", "2025", "74085", "2025 IVA 74085 vs 80361; tick1407; primary official NBB WVV 21"),
    ("bud_ptri_mva_2025", "2025", "7615837", "2025 MVA 7615837 vs 7920247; tick1407; primary official NBB WVV 22/27"),
    ("bud_ptri_gebouwen_2025", "2025", "7005019", "2025 terreinen/gebouwen 7005019 vs 7220408; tick1407; primary official NBB WVV 22"),
    ("bud_ptri_machines_2025", "2025", "191572", "2025 machines 191572 vs 226318; tick1407; primary official NBB WVV 23"),
    ("bud_ptri_meubilair_2025", "2025", "394046", "2025 meubilair 394046 vs 437875; tick1407; primary official NBB WVV 24"),
    ("bud_ptri_cip_2025", "2025", "25199", "2025 CIP 25199 vs 35647; tick1407; primary official NBB WVV 27"),
    ("bud_ptri_fva_2025", "2025", "1250", "2025 FVA 1250 (aanschaf 5000 / niet-opgevraagd 3750); tick1407; primary official NBB WVV 28"),
    ("bud_ptri_current_2025", "2025", "1997575", "2025 vlottend 1997575 vs 1743221; tick1407; primary official NBB WVV 29/58"),
    ("bud_ptri_voorraden_2025", "2025", "37063", "2025 voorraden 37063 vs 32044; tick1407; primary official NBB WVV 30/36"),
    ("bud_ptri_strecv_2025", "2025", "1565883", "2025 ST vorderingen 1565883 vs 1511976; tick1407; primary official NBB WVV 40/41"),
    ("bud_ptri_trade_recv_2025", "2025", "939192", "2025 handelsvorderingen 939192 vs 925888; tick1407; primary official NBB WVV 40"),
    ("bud_ptri_othrecv_2025", "2025", "626691", "2025 overige vorderingen 626691 vs 586088; tick1407; primary official NBB WVV 41"),
    ("bud_ptri_cash_2025", "2025", "380295", "2025 liquide middelen 380295 JUMP vs 177397; tick1407; primary official NBB WVV 54/58"),
    ("bud_ptri_cash_2024", "2024", "177397", "2024 liquide middelen 177397 comparative; tick1407; primary official NBB WVV 54/58"),
    ("bud_ptri_prepaid_2025", "2025", "14334", "2025 overlopend actief 14334; tick1407; primary official NBB WVV 490/1"),
    ("bud_ptri_equity_2025", "2025", "5017317", "2025 EV 5017317 vs 4961497; tick1407; primary official NBB WVV 10/15"),
    ("bud_ptri_inbreng_2025", "2025", "4400000", "2025 inbreng onbeschikbaar 4400000; tick1407; primary official NBB WVV 111"),
    ("bud_ptri_reserves_2025", "2025", "40685", "2025 reserves 40685 statutair onbeschikbaar; tick1407; primary official NBB WVV 13"),
    ("bud_ptri_overgedragen_2025", "2025", "263147", "2025 overgedragen 263147 vs 195204; tick1407; primary official NBB WVV 14"),
    ("bud_ptri_capsub_2025", "2025", "313485", "2025 kapitaalsubsidies 313485 vs 325608; tick1407; primary official NBB WVV 15"),
    ("bud_ptri_deferred_tax_2025", "2025", "104495", "2025 uitgestelde belastingen 104495 vs 108536; tick1407; primary official NBB WVV 168"),
    ("bud_ptri_debt_2025", "2025", "4566935", "2025 schulden 4566935 vs 4675045; tick1407; primary official NBB WVV 17/49"),
    ("bud_ptri_debt_2024", "2024", "4675045", "2024 schulden 4675045 comparative; tick1407; primary official NBB WVV 17/49"),
    ("bud_ptri_lt_2025", "2025", "3403750", "2025 LT bank 3403750 vs 3693750; tick1407; primary official NBB WVV 17"),
    ("bud_ptri_st_2025", "2025", "916437", "2025 ST schulden 916437 vs 821150; tick1407; primary official NBB WVV 42/48"),
    ("bud_ptri_ltdue_2025", "2025", "290000", "2025 LT-due binnen jaar 290000; tick1407; primary official NBB WVV 42"),
    ("bud_ptri_sttrade_2025", "2025", "360666", "2025 leveranciers 360666 vs 476207; tick1407; primary official NBB WVV 440/4"),
    ("bud_ptri_tax_st_2025", "2025", "48809", "2025 tax ST 48809 JUMP vs 0; tick1407; primary official NBB WVV 450/3"),
    ("bud_ptri_stother_2025", "2025", "216962", "2025 overige ST 216962 JUMP vs 54943; tick1407; primary official NBB WVV 47/48"),
    ("bud_ptri_deferred_pass_2025", "2025", "246747", "2025 overlopend passief 246747 vs 160145; tick1407; primary official NBB WVV 492/3"),
    ("bud_ptri_debt_1_5y_2025", "2025", "870000", "2025 debt 1-5y 870000; tick1407; primary official NBB WVV 8912"),
    ("bud_ptri_debt_gt5y_2025", "2025", "2533750", "2025 debt >5y 2533750; tick1407; primary official NBB WVV 8913"),
    ("bud_ptri_brutomarge_2025", "2025", "574007", "2025 brutomarge 574007 vs 697646; omzet 70 empty / 60/61 empty; tick1407; primary official NBB WVV 9900"),
    ("bud_ptri_brutomarge_2024", "2024", "697646", "2024 brutomarge 697646 comparative; tick1407; primary official NBB WVV 9900"),
    ("bud_ptri_afschr_2025", "2025", "438530", "2025 afschrijvingen 438530 vs 425110; tick1407; primary official NBB WVV 630"),
    ("bud_ptri_othcost_2025", "2025", "19427", "2025 andere bedrijfskosten 19427; tick1407; primary official NBB WVV 640/8"),
    ("bud_ptri_expl_2025", "2025", "118902", "2025 expl 118902 vs 235413; tick1407; primary official NBB WVV 9901"),
    ("bud_ptri_expl_2024", "2024", "235413", "2024 expl 235413 comparative; tick1407; primary official NBB WVV 9901"),
    ("bud_ptri_fininc_2025", "2025", "12127", "2025 fin opbr 12127 (capsub 12124); tick1407; primary official NBB WVV 75"),
    ("bud_ptri_capsub_pnl_2025", "2025", "12124", "2025 kapitaal- en interestsubsidies 12124; tick1407; primary official NBB WVV 753"),
    ("bud_ptri_fincost_2025", "2025", "50140", "2025 fin kosten 50140 vs 54180; tick1407; primary official NBB WVV 65"),
    ("bud_ptri_pnl_2025", "2025", "84930", "2025 PnL 84930 vs 198214; tick1407; primary official NBB WVV 9904"),
    ("bud_ptri_pnl_2024", "2024", "198214", "2024 PnL 198214 comparative; tick1407; primary official NBB WVV 9904"),
    ("bud_ptri_div_2025", "2025", "16986", "2025 vergoeding inbreng 16986 vs 39643; tick1407; primary official NBB WVV 694"),
    ("bud_ptri_overgedragen_dest_2025", "2025", "263147", "2025 over te dragen winst 263147; tick1407; primary official NBB WVV 14"),
    ("bud_ptri_capex_mva_2025", "2025", "127844", "2025 capex MVA aanschaf 127844; tick1407; primary official NBB WVV 8169"),
    ("bud_ptri_capex_2025", "2025", "127844", "2025 capex MVA 127844 (IVA 8029 empty); tick1407; primary official NBB WVV 8169"),
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

# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "agb_tlt"
SRC = "src_tlt_jr2025_nbb"
BUDGETS = [
    ("bud_tlt_assets_2025", "2025", "19953810", "2025 assets 19953810 VKT-kap 20/58; tick1405; primary official NBB WVV"),
    ("bud_tlt_assets_2024", "2024", "19604830", "2024 assets 19604830 comparative; tick1405; primary official NBB WVV 20/58"),
    ("bud_tlt_fixed_2025", "2025", "18680838", "2025 vaste activa 18680838; tick1405; primary official NBB WVV 21/28"),
    ("bud_tlt_iva_2025", "2025", "102840", "2025 IVA 102840 vs 45503; tick1405; primary official NBB WVV 21"),
    ("bud_tlt_mva_2025", "2025", "18568245", "2025 MVA 18568245 vs 18561883; tick1405; primary official NBB WVV 22/27"),
    ("bud_tlt_gebouwen_2025", "2025", "8822099", "2025 terreinen/gebouwen 8822099; tick1405; primary official NBB WVV 22"),
    ("bud_tlt_machines_2025", "2025", "151045", "2025 machines 151045 vs 128415; tick1405; primary official NBB WVV 23"),
    ("bud_tlt_meubilair_2025", "2025", "25091", "2025 meubilair 25091 vs 36198; tick1405; primary official NBB WVV 24"),
    ("bud_tlt_leasing_2025", "2025", "9303045", "2025 leasing 9303045 vs 9412587; tick1405; primary official NBB WVV 25"),
    ("bud_tlt_cip_2025", "2025", "266964", "2025 CIP 266964 JUMP vs 52191; tick1405; primary official NBB WVV 27"),
    ("bud_tlt_fva_2025", "2025", "9753", "2025 FVA 9753 counterpart unpublished; tick1405; primary official NBB WVV 28"),
    ("bud_tlt_current_2025", "2025", "1272972", "2025 vlottend 1272972 vs 987691; tick1405; primary official NBB WVV 29/58"),
    ("bud_tlt_strecv_2025", "2025", "136960", "2025 ST vorderingen 136960 JUMP vs 53908; tick1405; primary official NBB WVV 40/41"),
    ("bud_tlt_trade_recv_2025", "2025", "25521", "2025 handelsvorderingen 25521 vs 16043; tick1405; primary official NBB WVV 40"),
    ("bud_tlt_othrecv_2025", "2025", "111438", "2025 overige vorderingen 111438 JUMP vs 37865; tick1405; primary official NBB WVV 41"),
    ("bud_tlt_cash_2025", "2025", "1132461", "2025 liquide middelen 1132461 JUMP vs 929908; tick1405; primary official NBB WVV 54/58"),
    ("bud_tlt_cash_2024", "2024", "929908", "2024 liquide middelen 929908 comparative; tick1405; primary official NBB WVV 54/58"),
    ("bud_tlt_prepaid_2025", "2025", "3551", "2025 overlopend actief 3551; tick1405; primary official NBB WVV 490/1"),
    ("bud_tlt_equity_2025", "2025", "5586840", "2025 EV 5586840 vs 5491221; tick1405; primary official NBB WVV 10/15"),
    ("bud_tlt_kapitaal_2025", "2025", "349200", "2025 kapitaal 349200 (geplaatst 500000 / niet-opgevraagd 150800); tick1405; primary official NBB WVV 10"),
    ("bud_tlt_reserves_2025", "2025", "296168", "2025 reserves 296168 vs 135507; tick1405; primary official NBB WVV 13"),
    ("bud_tlt_capsub_2025", "2025", "4941472", "2025 kapitaalsubsidies 4941472 vs 5006514; tick1405; primary official NBB WVV 15"),
    ("bud_tlt_deferred_tax_2025", "2025", "2467935", "2025 uitgestelde belastingen 2467935 vs 2498770; tick1405; primary official NBB WVV 168"),
    ("bud_tlt_debt_2025", "2025", "11899035", "2025 schulden 11899035 vs 11614838; tick1405; primary official NBB WVV 17/49"),
    ("bud_tlt_debt_2024", "2024", "11614838", "2024 schulden 11614838 comparative; tick1405; primary official NBB WVV 17/49"),
    ("bud_tlt_lt_2025", "2025", "11192307", "2025 LT 11192307 (lease/krediet 9202467 + overige 1989840); tick1405; primary official NBB WVV 17"),
    ("bud_tlt_lt_lease_2025", "2025", "9202467", "2025 LT lease/krediet 9202467 vs 9312020; tick1405; primary official NBB WVV 172/3"),
    ("bud_tlt_lt_other_2025", "2025", "1989840", "2025 LT overige leningen 1989840 vs 1765267; tick1405; primary official NBB WVV 174/0"),
    ("bud_tlt_st_2025", "2025", "706728", "2025 ST schulden 706728 vs 537550; tick1405; primary official NBB WVV 42/48"),
    ("bud_tlt_ltdue_2025", "2025", "250320", "2025 LT-due binnen jaar 250320; tick1405; primary official NBB WVV 42"),
    ("bud_tlt_sttrade_2025", "2025", "192572", "2025 leveranciers 192572 vs 176443; tick1405; primary official NBB WVV 440/4"),
    ("bud_tlt_tax_st_2025", "2025", "103175", "2025 tax ST 103175 JUMP vs 23399; tick1405; primary official NBB WVV 450/3"),
    ("bud_tlt_debt_1_5y_2025", "2025", "812302", "2025 debt 1-5y 812302; tick1405; primary official NBB WVV 8912"),
    ("bud_tlt_debt_gt5y_2025", "2025", "10380005", "2025 debt >5y 10380005; tick1405; primary official NBB WVV 8913"),
    ("bud_tlt_brutomarge_2025", "2025", "679356", "2025 brutomarge 679356 vs 395568; omzet 70 empty / 60/61 empty; tick1405; primary official NBB WVV 9900"),
    ("bud_tlt_brutomarge_2024", "2024", "395568", "2024 brutomarge 395568 comparative; tick1405; primary official NBB WVV 9900"),
    ("bud_tlt_afschr_2025", "2025", "324311", "2025 afschrijvingen 324311 vs 300708; tick1405; primary official NBB WVV 630"),
    ("bud_tlt_othcost_2025", "2025", "40997", "2025 andere bedrijfskosten 40997; tick1405; primary official NBB WVV 640/8"),
    ("bud_tlt_expl_2025", "2025", "314049", "2025 expl 314049 vs 44505; tick1405; primary official NBB WVV 9901"),
    ("bud_tlt_expl_2024", "2024", "44505", "2024 expl 44505 comparative; tick1405; primary official NBB WVV 9901"),
    ("bud_tlt_fininc_2025", "2025", "73556", "2025 fin opbr 73556 (capsub in resultaat 67002); tick1405; primary official NBB WVV 75"),
    ("bud_tlt_capsub_pnl_2025", "2025", "67002", "2025 kapitaal- en interestsubsidies 67002; tick1405; primary official NBB WVV 753"),
    ("bud_tlt_tax_2025", "2025", "97119", "2025 belastingen 97119 vs empty; tick1405; primary official NBB WVV 67/77"),
    ("bud_tlt_pnl_2025", "2025", "321320", "2025 PnL 321320 vs 151920; tick1405; primary official NBB WVV 9904"),
    ("bud_tlt_pnl_2024", "2024", "151920", "2024 PnL 151920 comparative; tick1405; primary official NBB WVV 9904"),
    ("bud_tlt_div_2025", "2025", "160660", "2025 vergoeding inbreng 160660 vs 121536; tick1405; primary official NBB WVV 694"),
    ("bud_tlt_to_reserves_2025", "2025", "160660", "2025 toevoeging EV 160660 (wettelijk 11839 + overige 148821); tick1405; primary official NBB WVV 691/2"),
    ("bud_tlt_capex_iva_2025", "2025", "72671", "2025 capex IVA aanschaf 72671; tick1405; primary official NBB WVV 8029"),
    ("bud_tlt_capex_mva_2025", "2025", "315339", "2025 capex MVA aanschaf 315339; tick1405; primary official NBB WVV 8169"),
    ("bud_tlt_capex_2025", "2025", "388010", "2025 capex IVA+MVA 388010 (72671+315339); tick1405; primary official NBB WVV 8029+8169"),
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

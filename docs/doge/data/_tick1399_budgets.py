# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "nv_otar"
SRC = "src_otar_jr2025_nbb"
BUDGETS = [
    ("bud_otar_assets_2025", "2025", "95625285", "2025 assets 95625285 VOL-kap 20/58; tick1399; primary official NBB WVV"),
    ("bud_otar_assets_2024", "2024", "92748879", "2024 assets 92748879 comparative; tick1399; primary official NBB WVV 20/58"),
    ("bud_otar_fixed_2025", "2025", "83333044", "2025 vaste activa 83333044; tick1399; primary official NBB WVV 21/28"),
    ("bud_otar_iva_2025", "2025", "3411", "2025 IVA 3411 vs 25838; tick1399; primary official NBB WVV 21"),
    ("bud_otar_mva_2025", "2025", "465396", "2025 MVA 465396 (machines 405570 + meubilair 59825); tick1399; primary official NBB WVV 22/27"),
    ("bud_otar_machines_2025", "2025", "405570", "2025 machines 405570; tick1399; primary official NBB WVV 23"),
    ("bud_otar_meubilair_2025", "2025", "59825", "2025 meubilair 59825; tick1399; primary official NBB WVV 24"),
    ("bud_otar_fva_2025", "2025", "82864237", "2025 FVA 82864237 vs 82871637; tick1399; primary official NBB WVV 28"),
    ("bud_otar_fva_rel_2025", "2025", "82856601", "2025 verbonden FVA 82856601; tick1399; primary official NBB WVV 280/1"),
    ("bud_otar_fva_part_2025", "2025", "72606601", "2025 verbonden deelnemingen 72606601 (Otary BIS 51pct + Rentel 52pct); tick1399; primary official NBB WVV 280"),
    ("bud_otar_fva_loan_2025", "2025", "10250000", "2025 verbonden vorderingen 10250000; tick1399; primary official NBB WVV 281"),
    ("bud_otar_fva_oth_2025", "2025", "7636", "2025 andere FVA vorderingen 7636 vs 15036; tick1399; primary official NBB WVV 285/8"),
    ("bud_otar_current_2025", "2025", "12292241", "2025 vlottend 12292241 vs 9399106; tick1399; primary official NBB WVV 29/58"),
    ("bud_otar_strecv_2025", "2025", "1292618", "2025 ST vorderingen 1292618 vs 2917169; tick1399; primary official NBB WVV 40/41"),
    ("bud_otar_trade_recv_2025", "2025", "872210", "2025 handelsvorderingen 872210 vs 2711218; tick1399; primary official NBB WVV 40"),
    ("bud_otar_oth_recv_2025", "2025", "420408", "2025 overige ST vorderingen 420408 vs 205951; tick1399; primary official NBB WVV 41"),
    ("bud_otar_cash_2025", "2025", "10999623", "2025 liquide middelen 10999623 JUMP vs 6481937; tick1399; primary official NBB WVV 54/58"),
    ("bud_otar_cash_2024", "2024", "6481937", "2024 liquide middelen 6481937 comparative; tick1399; primary official NBB WVV 54/58"),
    ("bud_otar_equity_2025", "2025", "81503955", "2025 EV 81503955 vs 79186525; tick1399; primary official NBB WVV 10/15"),
    ("bud_otar_kapitaal_2025", "2025", "72310606", "2025 geplaatst kapitaal 72310606 / 49232 aandelen op naam; tick1399; primary official NBB WVV 100"),
    ("bud_otar_wettres_2025", "2025", "7231061", "2025 wettelijke reserve 7231061; tick1399; primary official NBB WVV 130"),
    ("bud_otar_re_2025", "2025", "1962288", "2025 overgedragen winst 1962288 vs -355142; tick1399; primary official NBB WVV 14"),
    ("bud_otar_debt_2025", "2025", "14121330", "2025 schulden 14121330 vs 13562353; tick1399; primary official NBB WVV 17/49"),
    ("bud_otar_debt_2024", "2024", "13562353", "2024 schulden 13562353 comparative; tick1399; primary official NBB WVV 17/49"),
    ("bud_otar_lt_2025", "2025", "11000000", "2025 LT achtergesteld 11000000 vs 10250000 (resterend 1-5j); tick1399; primary official NBB WVV 170/8812"),
    ("bud_otar_st_2025", "2025", "3121330", "2025 ST schulden 3121330; tick1399; primary official NBB WVV 42/48"),
    ("bud_otar_sttrade_2025", "2025", "1506841", "2025 leveranciers 1506841 vs 1638573; tick1399; primary official NBB WVV 440/4"),
    ("bud_otar_taxsoc_2025", "2025", "715186", "2025 tax/soc 715186 (tax 58461 + soc 656724); tick1399; primary official NBB WVV 45"),
    ("bud_otar_stoth_2025", "2025", "899304", "2025 overige ST 899304 vs 926483; tick1399; primary official NBB WVV 47/48"),
    ("bud_otar_omzet_2025", "2025", "12426978", "2025 omzet 12426978 vs 13389031; 6.10 category/geo empty; tick1399; primary official NBB WVV 70"),
    ("bud_otar_omzet_2024", "2024", "13389031", "2024 omzet 13389031 comparative; tick1399; primary official NBB WVV 70"),
    ("bud_otar_othops_2025", "2025", "1391323", "2025 andere bedrijfsopbrengsten 1391323 JUMP vs 434814; tick1399; primary official NBB WVV 74"),
    ("bud_otar_diensten_2025", "2025", "10235828", "2025 diensten 10235828 vs 9563473; tick1399; primary official NBB WVV 61"),
    ("bud_otar_diensten_2024", "2024", "9563473", "2024 diensten 9563473 comparative; tick1399; primary official NBB WVV 61"),
    ("bud_otar_pers_2025", "2025", "5146243", "2025 personeel 5146243 vs 5008949; 42.7 VTE / 44 headcount; tick1399; primary official NBB WVV 62"),
    ("bud_otar_afschr_2025", "2025", "109035", "2025 afschrijvingen 109035; tick1399; primary official NBB WVV 630"),
    ("bud_otar_expl_2025", "2025", "-1688833", "2025 expl -1688833 vs -863022; tick1399; primary official NBB WVV 9901"),
    ("bud_otar_expl_2024", "2024", "-863022", "2024 expl -863022 comparative; tick1399; primary official NBB WVV 9901"),
    ("bud_otar_fininc_2025", "2025", "19774062", "2025 fin opbr 19774062 vs 64300765; tick1399; primary official NBB WVV 75/76B"),
    ("bud_otar_fva_inc_2025", "2025", "19116262", "2025 opbrengsten FVA 19116262 DROP vs 63719833; tick1399; primary official NBB WVV 750/9421"),
    ("bud_otar_fva_inc_2024", "2024", "63719833", "2024 opbrengsten FVA 63719833 comparative; tick1399; primary official NBB WVV 750"),
    ("bud_otar_finvlott_2025", "2025", "657776", "2025 opbrengsten vlottend 657776 vs 580933; tick1399; primary official NBB WVV 751"),
    ("bud_otar_fincost_2025", "2025", "808603", "2025 fin kosten 808603 vs 458368; tick1399; primary official NBB WVV 65/66B"),
    ("bud_otar_debtcost_2025", "2025", "807620", "2025 kosten van schulden 807620 vs 457269; tick1399; primary official NBB WVV 650"),
    ("bud_otar_tax_2025", "2025", "39156", "2025 belastingen 39156 vs 207741; tick1399; primary official NBB WVV 67/77"),
    ("bud_otar_pnl_2025", "2025", "17237470", "2025 PnL +17237470 vs +62771635; tick1399; primary official NBB WVV 9904"),
    ("bud_otar_pnl_2024", "2024", "62771635", "2024 PnL +62771635 comparative; tick1399; primary official NBB WVV 9904"),
    ("bud_otar_div_2025", "2025", "14471000", "2025 vergoeding inbreng 14471000 DROP vs 63006000; tick1399; primary official NBB WVV 694"),
    ("bud_otar_div_2024", "2024", "63006000", "2024 vergoeding inbreng 63006000 comparative; tick1399; primary official NBB WVV 694"),
    ("bud_otar_winstpremie_2025", "2025", "449041", "2025 werknemers winstpremie 449041 vs 534565; tick1399; primary official NBB WVV 696"),
    ("bud_otar_uitkering_2025", "2025", "14920041", "2025 uit te keren winst 14920041; tick1399; primary official NBB WVV 694/7"),
    ("bud_otar_capex_mach_2025", "2025", "99706", "2025 machines aanschaf 99706; IVA/meubilair aanschaf empty; tick1399; primary official NBB WVV 8162"),
    ("bud_otar_comm_2025", "2025", "16609", "2025 commissaris Deloitte 16609 + extra 6598; tick1399; primary official NBB WVV 9505"),
    ("bud_otar_rel_recv_2025", "2025", "901658", "2025 related-party ST vorderingen 901658 vs 1987828; tick1399; primary official NBB WVV 9311"),
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

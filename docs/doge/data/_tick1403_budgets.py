# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_vrko"
SRC = "src_vrko_jr2025_nbb"
BUDGETS = [
    ("bud_vrko_assets_2025", "2025", "38416495", "2025 assets 38416495 VOL-kap 20/58; tick1403; primary official NBB WVV"),
    ("bud_vrko_assets_2024", "2024", "38702689", "2024 assets 38702689 comparative; tick1403; primary official NBB WVV 20/58"),
    ("bud_vrko_fixed_2025", "2025", "29812581", "2025 vaste activa 29812581; tick1403; primary official NBB WVV 21/28"),
    ("bud_vrko_mva_2025", "2025", "29773483", "2025 MVA 29773483 vs 30876256; tick1403; primary official NBB WVV 22/27"),
    ("bud_vrko_gebouwen_2025", "2025", "24373263", "2025 terreinen/gebouwen 24373263; tick1403; primary official NBB WVV 22"),
    ("bud_vrko_machines_2025", "2025", "1352404", "2025 machines 1352404; tick1403; primary official NBB WVV 23"),
    ("bud_vrko_meubilair_2025", "2025", "1611020", "2025 meubilair 1611020 vs 2204351; tick1403; primary official NBB WVV 24"),
    ("bud_vrko_leasing_2025", "2025", "2155499", "2025 leasing 2155499 vs 1404446; tick1403; primary official NBB WVV 25"),
    ("bud_vrko_overige_mva_2025", "2025", "281296", "2025 overige MVA 281296; tick1403; primary official NBB WVV 26"),
    ("bud_vrko_fva_2025", "2025", "39099", "2025 FVA 39099 (deelnemingen 25000); tick1403; primary official NBB WVV 28"),
    ("bud_vrko_current_2025", "2025", "8603914", "2025 vlottend 8603914 vs 7787356; tick1403; primary official NBB WVV 29/58"),
    ("bud_vrko_inventory_2025", "2025", "142748", "2025 voorraden 142748; tick1403; primary official NBB WVV 30/36"),
    ("bud_vrko_strecv_2025", "2025", "2722976", "2025 ST vorderingen 2722976 DROP vs 4394865; tick1403; primary official NBB WVV 40/41"),
    ("bud_vrko_trade_recv_2025", "2025", "1769628", "2025 handelsvorderingen 1769628 DROP vs 3437791; tick1403; primary official NBB WVV 40"),
    ("bud_vrko_trade_recv_2024", "2024", "3437791", "2024 handelsvorderingen 3437791 comparative; tick1403; primary official NBB WVV 40"),
    ("bud_vrko_cash_2025", "2025", "3529851", "2025 liquide middelen 3529851 JUMP vs 1043325; tick1403; primary official NBB WVV 54/58"),
    ("bud_vrko_cash_2024", "2024", "1043325", "2024 liquide middelen 1043325 comparative; tick1403; primary official NBB WVV 54/58"),
    ("bud_vrko_prepaid_2025", "2025", "2208338", "2025 overlopend actief 2208338 (energie 1668k); tick1403; primary official NBB WVV 490/1"),
    ("bud_vrko_equity_2025", "2025", "4455729", "2025 EV 4455729 vs 4452575; tick1403; primary official NBB WVV 10/15"),
    ("bud_vrko_kapitaal_2025", "2025", "850450", "2025 geplaatst kapitaal 850450 / 34018 aandelen; tick1403; primary official NBB WVV 10"),
    ("bud_vrko_reserves_2025", "2025", "3598431", "2025 reserves 3598431 (onbeschikbaar 2904315); tick1403; primary official NBB WVV 13"),
    ("bud_vrko_capsub_2025", "2025", "6848", "2025 kapitaalsubsidies 6848 vs 10272; tick1403; primary official NBB WVV 15"),
    ("bud_vrko_prov_2025", "2025", "5233600", "2025 voorzieningen 5233600 vs 5533600; tick1403; primary official NBB WVV 16"),
    ("bud_vrko_prov_herstel_2025", "2025", "5218575", "2025 voorziening herstel compostering 5218575; tick1403; primary official NBB WVV 162"),
    ("bud_vrko_debt_2025", "2025", "28727165", "2025 schulden 28727165 vs 28716513; tick1403; primary official NBB WVV 17/49"),
    ("bud_vrko_debt_2024", "2024", "28716513", "2024 schulden 28716513 comparative; tick1403; primary official NBB WVV 17/49"),
    ("bud_vrko_lt_2025", "2025", "18895417", "2025 LT schulden 18895417 (bank 16851258 + lease 2044159); tick1403; primary official NBB WVV 17"),
    ("bud_vrko_ltbank_2025", "2025", "16851258", "2025 LT bank 16851258 vs 18207480; tick1403; primary official NBB WVV 173"),
    ("bud_vrko_ltlease_2025", "2025", "2044159", "2025 LT lease 2044159 vs 1300325; tick1403; primary official NBB WVV 172"),
    ("bud_vrko_st_2025", "2025", "8526903", "2025 ST schulden 8526903 vs 8338537; tick1403; primary official NBB WVV 42/48"),
    ("bud_vrko_sttrade_2025", "2025", "4048188", "2025 leveranciers 4048188; tick1403; primary official NBB WVV 440/4"),
    ("bud_vrko_taxsoc_2025", "2025", "1775991", "2025 tax/soc 1775991 (tax 291067 + soc 1484924); tick1403; primary official NBB WVV 45"),
    ("bud_vrko_omzet_2025", "2025", "26146600", "2025 omzet 26146600 vs 24949929 (lokale besturen 18552275); tick1403; primary official NBB WVV 70"),
    ("bud_vrko_omzet_2024", "2024", "24949929", "2024 omzet 24949929 comparative; tick1403; primary official NBB WVV 70"),
    ("bud_vrko_omzet_gov_2025", "2025", "18552275", "2025 omzet lokale besturen 18552275 vs 16618705; tick1403; primary official NBB WVV 6.10"),
    ("bud_vrko_omzet_fost_2025", "2025", "2723004", "2025 omzet Fost Plus 2723004 vs 2108554; tick1403; primary official NBB WVV 6.10"),
    ("bud_vrko_othops_2025", "2025", "1814797", "2025 andere bedrijfsopbrengsten 1814797 vs 1928849; 740 subsidies 986097; tick1403; primary official NBB WVV 74"),
    ("bud_vrko_subsidy_2025", "2025", "986097", "2025 exploitatiesubsidies 740 986097 vs 941868; tick1403; primary official NBB WVV 740"),
    ("bud_vrko_diensten_2025", "2025", "12448633", "2025 diensten 12448633 vs 12007670; tick1403; primary official NBB WVV 61"),
    ("bud_vrko_diensten_2024", "2024", "12007670", "2024 diensten 12007670 comparative; tick1403; primary official NBB WVV 61"),
    ("bud_vrko_pers_2025", "2025", "11760008", "2025 personeel 11760008 vs 11322047; 191.5 VTE / YE 190; tick1403; primary official NBB WVV 62"),
    ("bud_vrko_pers_2024", "2024", "11322047", "2024 personeel 11322047 comparative; tick1403; primary official NBB WVV 62"),
    ("bud_vrko_afschr_2025", "2025", "3214660", "2025 afschrijvingen 3214660; tick1403; primary official NBB WVV 630"),
    ("bud_vrko_expl_2025", "2025", "694693", "2025 expl 694693 vs 677574; tick1403; primary official NBB WVV 9901"),
    ("bud_vrko_expl_2024", "2024", "677574", "2024 expl 677574 comparative; tick1403; primary official NBB WVV 9901"),
    ("bud_vrko_fininc_2025", "2025", "8951", "2025 fin opbr 8951; tick1403; primary official NBB WVV 75"),
    ("bud_vrko_fincost_2025", "2025", "696585", "2025 fin kosten 696585; tick1403; primary official NBB WVV 65"),
    ("bud_vrko_tax_2025", "2025", "481", "2025 belastingen 481; tick1403; primary official NBB WVV 67/77"),
    ("bud_vrko_pnl_2025", "2025", "6578", "2025 PnL 6578 vs 4247; tick1403; primary official NBB WVV 9904"),
    ("bud_vrko_pnl_2024", "2024", "4247", "2024 PnL 4247 comparative; tick1403; primary official NBB WVV 9904"),
    ("bud_vrko_capex_2025", "2025", "2165409", "2025 capex MVA aanschaf 2165409 (lease 1125860 + geb 682874 + meub 200018 + mach 84783 + ov 71875); tick1403; primary official NBB WVV 8161-8165"),
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

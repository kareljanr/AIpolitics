# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_mlso"
SRC = "src_mlso_jr2025_nbb"
BUDGETS = [
    ("bud_mlso_assets_2025", "2025", "227277417", "2025 assets 227277417 VOL-inb 20/58; tick1406; primary official NBB WVV"),
    ("bud_mlso_assets_2024", "2024", "231030389", "2024 assets 231030389 comparative; tick1406; primary official NBB WVV 20/58"),
    ("bud_mlso_fixed_2025", "2025", "156090644", "2025 vaste activa 156090644; tick1406; primary official NBB WVV 21/28"),
    ("bud_mlso_iva_2025", "2025", "2127", "2025 IVA 2127 vs 5294; tick1406; primary official NBB WVV 21"),
    ("bud_mlso_mva_2025", "2025", "141212883", "2025 MVA 141212883 vs 142321245; tick1406; primary official NBB WVV 22/27"),
    ("bud_mlso_gebouwen_2025", "2025", "141150326", "2025 terreinen/gebouwen 141150326; tick1406; primary official NBB WVV 22"),
    ("bud_mlso_machines_2025", "2025", "16648", "2025 machines 16648 vs 20177; tick1406; primary official NBB WVV 23"),
    ("bud_mlso_meubilair_2025", "2025", "45908", "2025 meubilair 45908 vs 72945; tick1406; primary official NBB WVV 24"),
    ("bud_mlso_fva_2025", "2025", "14875633", "2025 FVA 14875633 (deeln 3088000 + vord 11787633); tick1406; primary official NBB WVV 28"),
    ("bud_mlso_fva_deeln_2025", "2025", "3088000", "2025 FVA deelnemingen 3088000 Ecluse 10pct + Railport 12.5pct + Wind Aan De Stroom 28pct; tick1406; primary official NBB WVV 282"),
    ("bud_mlso_fva_vord_2025", "2025", "11787633", "2025 FVA andere vorderingen 11787633 Grondenbank LSO II; tick1406; primary official NBB WVV 285/8"),
    ("bud_mlso_current_2025", "2025", "71186773", "2025 vlottend 71186773 vs 73899266; tick1406; primary official NBB WVV 29/58"),
    ("bud_mlso_strecv_2025", "2025", "5346615", "2025 ST vorderingen 5346615 vs 6391744; tick1406; primary official NBB WVV 40/41"),
    ("bud_mlso_trade_recv_2025", "2025", "2591131", "2025 handelsvorderingen 2591131 vs 3774670; tick1406; primary official NBB WVV 40"),
    ("bud_mlso_othrecv_2025", "2025", "2755484", "2025 overige vorderingen 2755484 vs 2617073; tick1406; primary official NBB WVV 41"),
    ("bud_mlso_invest_2025", "2025", "40040307", "2025 geldbeleggingen 40040307 (vastrent 20040307 + termijn 20000000); tick1406; primary official NBB WVV 50/53"),
    ("bud_mlso_cash_2025", "2025", "24924839", "2025 liquide middelen 24924839 DROP vs 26906762; tick1406; primary official NBB WVV 54/58"),
    ("bud_mlso_cash_2024", "2024", "26906762", "2024 liquide middelen 26906762 comparative; tick1406; primary official NBB WVV 54/58"),
    ("bud_mlso_prepaid_2025", "2025", "826346", "2025 overlopend actief 826346; tick1406; primary official NBB WVV 490/1"),
    ("bud_mlso_equity_2025", "2025", "213683129", "2025 EV 213683129 vs 209812042; tick1406; primary official NBB WVV 10/15"),
    ("bud_mlso_inbreng_2025", "2025", "73803318", "2025 inbreng 73803318 (beschikbaar 71719985 / onbeschikbaar 2083333); tick1406; primary official NBB WVV 10/11"),
    ("bud_mlso_reserves_2025", "2025", "138812354", "2025 reserves 138812354 vs 134023708; tick1406; primary official NBB WVV 13"),
    ("bud_mlso_capsub_2025", "2025", "1066985", "2025 kapitaalsubsidies 1066985 vs 1117794; tick1406; primary official NBB WVV 15"),
    ("bud_mlso_debt_2025", "2025", "13594288", "2025 schulden 13594288 DROP vs 21218347; tick1406; primary official NBB WVV 17/49"),
    ("bud_mlso_debt_2024", "2024", "21218347", "2024 schulden 21218347 comparative; tick1406; primary official NBB WVV 17/49"),
    ("bud_mlso_st_2025", "2025", "8495667", "2025 ST 8495667 vs 16166819; tick1406; primary official NBB WVV 42/48"),
    ("bud_mlso_ltdue_2025", "2025", "27516", "2025 LT-due binnen jaar 27516 DROP vs 6945998; tick1406; primary official NBB WVV 42"),
    ("bud_mlso_sttrade_2025", "2025", "619643", "2025 leveranciers 619643 vs 1799807; tick1406; primary official NBB WVV 440/4"),
    ("bud_mlso_taxsoc_st_2025", "2025", "1024780", "2025 tax/soc ST 1024780 (tax 786430 + soc 238350); tick1406; primary official NBB WVV 45"),
    ("bud_mlso_stother_2025", "2025", "6823728", "2025 overige schulden 6823728 vs 6428508; tick1406; primary official NBB WVV 47/48"),
    ("bud_mlso_deferred_2025", "2025", "5098621", "2025 overlopend passief 5098621 (over te dragen 4920734); tick1406; primary official NBB WVV 492/3"),
    ("bud_mlso_omzet_2025", "2025", "24044090", "2025 omzet 24044090 vs 21375666; tick1406; primary official NBB WVV 70"),
    ("bud_mlso_omzet_2024", "2024", "21375666", "2024 omzet 21375666 comparative; tick1406; primary official NBB WVV 70"),
    ("bud_mlso_omzet_conc_2025", "2025", "11127094", "2025 concessies LSO 11127094; tick1406; primary official NBB WVV 6.10"),
    ("bud_mlso_omzet_erf_2025", "2025", "7083980", "2025 erfpachten LSO 7083980; tick1406; primary official NBB WVV 6.10"),
    ("bud_mlso_othops_2025", "2025", "1582296", "2025 andere bedrijfsopbrengsten 1582296 (740 subsidies 1515000); tick1406; primary official NBB WVV 74"),
    ("bud_mlso_subs_2025", "2025", "1515000", "2025 exploitatiesubsidies 1515000; tick1406; primary official NBB WVV 740"),
    ("bud_mlso_diensten_2025", "2025", "7752488", "2025 diensten 7752488 JUMP vs 5994642; tick1406; primary official NBB WVV 61"),
    ("bud_mlso_diensten_2024", "2024", "5994642", "2024 diensten 5994642 comparative; tick1406; primary official NBB WVV 61"),
    ("bud_mlso_pers_2025", "2025", "1639799", "2025 pers 1639799 / 14.5 VTE / YE 16; tick1406; primary official NBB WVV 62"),
    ("bud_mlso_afschr_2025", "2025", "608958", "2025 afschrijvingen 608958 vs 615223; tick1406; primary official NBB WVV 630"),
    ("bud_mlso_wv_2025", "2025", "369323", "2025 WV handelsvorderingen 369323 DHollander; tick1406; primary official NBB WVV 631/4"),
    ("bud_mlso_othcost_2025", "2025", "3602585", "2025 andere bedrijfskosten 3602585 onroerende voorheffing; tick1406; primary official NBB WVV 640/8"),
    ("bud_mlso_nrec_2025", "2025", "4415758", "2025 niet-recurrent 66A 4415758 vs 3390408; tick1406; primary official NBB WVV 66A"),
    ("bud_mlso_expl_2025", "2025", "7320495", "2025 expl 7320495 vs 9888604; tick1406; primary official NBB WVV 9901"),
    ("bud_mlso_expl_2024", "2024", "9888604", "2024 expl 9888604 comparative; tick1406; primary official NBB WVV 9901"),
    ("bud_mlso_fininc_2025", "2025", "1980146", "2025 fin opbr 1980146 (FVA 560000 Wind Aan De Stroom); tick1406; primary official NBB WVV 75"),
    ("bud_mlso_tax_2025", "2025", "1693389", "2025 belastingen 1693389 vs 1820239; tick1406; primary official NBB WVV 67/77"),
    ("bud_mlso_pnl_2025", "2025", "7699101", "2025 PnL 7699101 vs 9520919; tick1406; primary official NBB WVV 9904"),
    ("bud_mlso_pnl_2024", "2024", "9520919", "2024 PnL 9520919 comparative; tick1406; primary official NBB WVV 9904"),
    ("bud_mlso_div_2025", "2025", "2910456", "2025 vergoeding inbreng 2910456 vs 2878774; tick1406; primary official NBB WVV 694"),
    ("bud_mlso_to_reserves_2025", "2025", "5659994", "2025 toevoeging overige reserves 5659994; tick1406; primary official NBB WVV 6921"),
    ("bud_mlso_capex_2025", "2025", "259767", "2025 capex MVA 259767 (geb 250734 + mach 9033); tick1406; primary official NBB WVV 8161+8162"),
    ("bud_mlso_interwaas_2025", "2025", "3762956", "2025 Interwaas schadevergoeding LPW 3762955.84 rounded 3762956; tick1406; primary official NBB WVV 6.20"),
    ("bud_mlso_commissaris_2025", "2025", "11635", "2025 commissaris 11635; tick1406; primary official NBB WVV 9505"),
    ("bud_mlso_bestuurders_2025", "2025", "29854", "2025 bestuurders 29854; tick1406; primary official NBB WVV 9503"),
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

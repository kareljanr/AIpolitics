# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_dds"
SRC = "src_dds_jr2025_nbb"
BUDGETS = [
    ("bud_dds_assets_2025", "2025", "48501395", "2025 assets 48501395 VOL-kap 20/58; tick1402; primary official NBB WVV"),
    ("bud_dds_assets_2024", "2024", "48751932", "2024 assets 48751932 comparative; tick1402; primary official NBB WVV 20/58"),
    ("bud_dds_fixed_2025", "2025", "24158220", "2025 vaste activa 24158220; tick1402; primary official NBB WVV 21/28"),
    ("bud_dds_mva_2025", "2025", "24150165", "2025 MVA 24150165 vs 24521006; tick1402; primary official NBB WVV 22/27"),
    ("bud_dds_gebouwen_2025", "2025", "5834733", "2025 terreinen/gebouwen 5834733; tick1402; primary official NBB WVV 22"),
    ("bud_dds_machines_2025", "2025", "85096", "2025 machines 85096; tick1402; primary official NBB WVV 23"),
    ("bud_dds_meubilair_2025", "2025", "189056", "2025 meubilair 189056 vs 158021; tick1402; primary official NBB WVV 24"),
    ("bud_dds_overige_mva_2025", "2025", "16311319", "2025 overige MVA 16311319 vs 16847415; tick1402; primary official NBB WVV 26"),
    ("bud_dds_cip_2025", "2025", "1729961", "2025 CIP 1729961 vs 1519953; tick1402; primary official NBB WVV 27"),
    ("bud_dds_fva_2025", "2025", "8055", "2025 FVA 8055; tick1402; primary official NBB WVV 28"),
    ("bud_dds_current_2025", "2025", "24343175", "2025 vlottend 24343175 vs 24222870; tick1402; primary official NBB WVV 29/58"),
    ("bud_dds_inventory_2025", "2025", "12793375", "2025 voorraden onroerend 12793375 vs 12959720; tick1402; primary official NBB WVV 35"),
    ("bud_dds_inventory_2024", "2024", "12959720", "2024 voorraden onroerend 12959720 comparative; tick1402; primary official NBB WVV 35"),
    ("bud_dds_strecv_2025", "2025", "1939451", "2025 ST vorderingen 1939451 JUMP vs 871108; tick1402; primary official NBB WVV 40/41"),
    ("bud_dds_trade_recv_2025", "2025", "1412267", "2025 handelsvorderingen 1412267 JUMP vs 604992; tick1402; primary official NBB WVV 40"),
    ("bud_dds_trade_recv_2024", "2024", "604992", "2024 handelsvorderingen 604992 comparative; tick1402; primary official NBB WVV 40"),
    ("bud_dds_invest_2025", "2025", "1500000", "2025 geldbeleggingen 1500000 vastrentend; tick1402; primary official NBB WVV 50/53"),
    ("bud_dds_cash_2025", "2025", "5533236", "2025 liquide middelen 5533236 DROP vs 7792016; tick1402; primary official NBB WVV 54/58"),
    ("bud_dds_cash_2024", "2024", "7792016", "2024 liquide middelen 7792016 comparative; tick1402; primary official NBB WVV 54/58"),
    ("bud_dds_prepaid_2025", "2025", "2559272", "2025 overlopend actief 2559272 JUMP vs 1075990; tick1402; primary official NBB WVV 490/1"),
    ("bud_dds_prepaid_2024", "2024", "1075990", "2024 overlopend actief 1075990 comparative; tick1402; primary official NBB WVV 490/1"),
    ("bud_dds_equity_2025", "2025", "38109541", "2025 EV 38109541 vs 38405812; tick1402; primary official NBB WVV 10/15"),
    ("bud_dds_kapitaal_2025", "2025", "870050", "2025 geplaatst kapitaal 870050 vs 865050; tick1402; primary official NBB WVV 10"),
    ("bud_dds_reserves_2025", "2025", "36846205", "2025 reserves 36846205 (onbeschikbaar 34636199); tick1402; primary official NBB WVV 13"),
    ("bud_dds_capsub_2025", "2025", "344721", "2025 kapitaalsubsidies 344721 vs 358682; tick1402; primary official NBB WVV 15"),
    ("bud_dds_prov_2025", "2025", "7847265", "2025 voorzieningen+latent 7847265 vs 7956431; tick1402; primary official NBB WVV 16"),
    ("bud_dds_prov_herstel_2025", "2025", "3345181", "2025 voorziening herstel 3345181; tick1402; primary official NBB WVV 162"),
    ("bud_dds_prov_overige_2025", "2025", "3866038", "2025 voorziening overige 3866038; tick1402; primary official NBB WVV 164/5"),
    ("bud_dds_debt_2025", "2025", "2544589", "2025 schulden 2544589 vs 2389688; no LT; tick1402; primary official NBB WVV 17/49"),
    ("bud_dds_debt_2024", "2024", "2389688", "2024 schulden 2389688 comparative; tick1402; primary official NBB WVV 17/49"),
    ("bud_dds_st_2025", "2025", "2193163", "2025 ST schulden 2193163 vs 1163926; tick1402; primary official NBB WVV 42/48"),
    ("bud_dds_sttrade_2025", "2025", "607606", "2025 leveranciers 607606 JUMP vs 354671; tick1402; primary official NBB WVV 440/4"),
    ("bud_dds_taxsoc_2025", "2025", "766511", "2025 tax/soc 766511 (tax 206022 + soc 560489); tick1402; primary official NBB WVV 45"),
    ("bud_dds_omzet_2025", "2025", "1262519", "2025 omzet 1262519 vs 1613144 (vastgoed 431533 + diensten 830986); tick1402; primary official NBB WVV 70"),
    ("bud_dds_omzet_2024", "2024", "1613144", "2024 omzet 1613144 comparative; tick1402; primary official NBB WVV 70"),
    ("bud_dds_othops_2025", "2025", "5219038", "2025 andere bedrijfsopbrengsten 5219038 vs 4665152; 740 subsidies 700935; tick1402; primary official NBB WVV 74"),
    ("bud_dds_othops_2024", "2024", "4665152", "2024 andere bedrijfsopbrengsten 4665152 comparative; tick1402; primary official NBB WVV 74"),
    ("bud_dds_subsidy_2025", "2025", "700935", "2025 exploitatiesubsidies 740 700935 JUMP vs 145248; tick1402; primary official NBB WVV 740"),
    ("bud_dds_diensten_2025", "2025", "1359141", "2025 diensten 1359141 vs 1308660; tick1402; primary official NBB WVV 61"),
    ("bud_dds_pers_2025", "2025", "3875923", "2025 personeel 3875923 vs 3528505; 40.6 VTE / YE 46; tick1402; primary official NBB WVV 62"),
    ("bud_dds_pers_2024", "2024", "3528505", "2024 personeel 3528505 comparative; tick1402; primary official NBB WVV 62"),
    ("bud_dds_afschr_2025", "2025", "1160666", "2025 afschrijvingen 1160666; tick1402; primary official NBB WVV 630"),
    ("bud_dds_expl_2025", "2025", "-506271", "2025 expl -506271 vs -314583; tick1402; primary official NBB WVV 9901"),
    ("bud_dds_expl_2024", "2024", "-314583", "2024 expl -314583 comparative; tick1402; primary official NBB WVV 9901"),
    ("bud_dds_fininc_2025", "2025", "166426", "2025 fin opbr 166426 (capsub 13960); tick1402; primary official NBB WVV 75"),
    ("bud_dds_fincost_2025", "2025", "6635", "2025 fin kosten 6635; tick1402; primary official NBB WVV 65"),
    ("bud_dds_tax_2025", "2025", "-37098", "2025 belastingen -37098 (credit); tick1402; primary official NBB WVV 67/77"),
    ("bud_dds_pnl_2025", "2025", "-287310", "2025 PnL -287310 vs -134014; tick1402; primary official NBB WVV 9904"),
    ("bud_dds_pnl_2024", "2024", "-134014", "2024 PnL -134014 comparative; tick1402; primary official NBB WVV 9904"),
    ("bud_dds_tebest_2025", "2025", "-235056", "2025 te bestemmen -235056 from reserves; tick1402; primary official NBB WVV 9905"),
    ("bud_dds_capex_2025", "2025", "789825", "2025 capex MVA aanschaf 789825 (meub 95828 + overige 483988 + CIP 210008); tick1402; primary official NBB WVV 8163/8165/8166"),
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

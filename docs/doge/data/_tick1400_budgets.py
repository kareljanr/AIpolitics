# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_iglg"
SRC = "src_iglg_jr2025_nbb"
BUDGETS = [
    ("bud_iglg_assets_2025", "2025", "65298610", "2025 assets 65298610 VOL-inb 20/58; tick1400; primary official NBB WVV"),
    ("bud_iglg_assets_2024", "2024", "63846592", "2024 assets 63846592 comparative; tick1400; primary official NBB WVV 20/58"),
    ("bud_iglg_fixed_2025", "2025", "46529826", "2025 vaste activa 46529826; tick1400; primary official NBB WVV 21/28"),
    ("bud_iglg_iva_2025", "2025", "71452", "2025 IVA 71452 vs 45966; tick1400; primary official NBB WVV 21"),
    ("bud_iglg_mva_2025", "2025", "46277588", "2025 MVA 46277588 vs 47472883; tick1400; primary official NBB WVV 22/27"),
    ("bud_iglg_gebouwen_2025", "2025", "43279559", "2025 gebouwen 43279559 JUMP vs 29109074 masterplan fase2; tick1400; primary official NBB WVV 22"),
    ("bud_iglg_machines_2025", "2025", "1922155", "2025 machines 1922155; tick1400; primary official NBB WVV 23"),
    ("bud_iglg_meubilair_2025", "2025", "867109", "2025 meubilair 867109 vs 781712; tick1400; primary official NBB WVV 24"),
    ("bud_iglg_lease_2025", "2025", "149976", "2025 leasing 149976; tick1400; primary official NBB WVV 25"),
    ("bud_iglg_cip_2025", "2025", "51090", "2025 CIP 51090 DROP vs 15476618; tick1400; primary official NBB WVV 27"),
    ("bud_iglg_cip_2024", "2024", "15476618", "2024 CIP 15476618 comparative; tick1400; primary official NBB WVV 27"),
    ("bud_iglg_fva_2025", "2025", "180786", "2025 FVA 180786 andere aandelen; tick1400; primary official NBB WVV 28"),
    ("bud_iglg_current_2025", "2025", "18768784", "2025 vlottend 18768784 vs 16146957; tick1400; primary official NBB WVV 29/58"),
    ("bud_iglg_ltrecv_2025", "2025", "338239", "2025 LT vorderingen 338239; tick1400; primary official NBB WVV 29"),
    ("bud_iglg_strecv_2025", "2025", "1647053", "2025 ST vorderingen 1647053 vs 1092145; tick1400; primary official NBB WVV 40/41"),
    ("bud_iglg_trade_recv_2025", "2025", "753734", "2025 handelsvorderingen 753734; tick1400; primary official NBB WVV 40"),
    ("bud_iglg_oth_recv_2025", "2025", "893319", "2025 overige ST vorderingen 893319 JUMP vs 437068; tick1400; primary official NBB WVV 41"),
    ("bud_iglg_invest_2025", "2025", "9500000", "2025 termijndeposito 9500000 vs 7570000 (1m-1y); tick1400; primary official NBB WVV 53"),
    ("bud_iglg_invest_2024", "2024", "7570000", "2024 termijndeposito 7570000 comparative; tick1400; primary official NBB WVV 53"),
    ("bud_iglg_cash_2025", "2025", "5894254", "2025 liquide middelen 5894254 vs 5462448; tick1400; primary official NBB WVV 54/58"),
    ("bud_iglg_prepaid_2025", "2025", "1389238", "2025 overlopend actief 1389238; tick1400; primary official NBB WVV 490/1"),
    ("bud_iglg_equity_2025", "2025", "33288549", "2025 EV 33288549 vs 30762045; tick1400; primary official NBB WVV 10/15"),
    ("bud_iglg_inbreng_2025", "2025", "1238031", "2025 inbreng 1238031; tick1400; primary official NBB WVV 10/11"),
    ("bud_iglg_reserves_2025", "2025", "22748587", "2025 reserves 22748587; tick1400; primary official NBB WVV 13"),
    ("bud_iglg_re_2025", "2025", "516039", "2025 overgedragen winst 516039; tick1400; primary official NBB WVV 14"),
    ("bud_iglg_capsub_2025", "2025", "8217525", "2025 kapitaalsubsidies 8217525 vs 8014066; tick1400; primary official NBB WVV 15"),
    ("bud_iglg_prov_2025", "2025", "243675", "2025 voorzieningen 243675 vs 570044; tick1400; primary official NBB WVV 16"),
    ("bud_iglg_debt_2025", "2025", "31766387", "2025 schulden 31766387 vs 32514503; tick1400; primary official NBB WVV 17/49"),
    ("bud_iglg_debt_2024", "2024", "32514503", "2024 schulden 32514503 comparative; tick1400; primary official NBB WVV 17/49"),
    ("bud_iglg_lt_2025", "2025", "20039581", "2025 LT bank 20039581 vs 21600012; tick1400; primary official NBB WVV 173"),
    ("bud_iglg_st_2025", "2025", "11214151", "2025 ST schulden 11214151; tick1400; primary official NBB WVV 42/48"),
    ("bud_iglg_ltdue_2025", "2025", "2021569", "2025 LT-due 2021569; tick1400; primary official NBB WVV 42"),
    ("bud_iglg_sttrade_2025", "2025", "1285113", "2025 leveranciers 1285113 JUMP vs 861098; tick1400; primary official NBB WVV 440/4"),
    ("bud_iglg_taxsoc_2025", "2025", "7078568", "2025 tax/soc 7078568 (tax 921470 + soc 6157098); tick1400; primary official NBB WVV 45"),
    ("bud_iglg_omzet_2025", "2025", "48156858", "2025 omzet 48156858 vs 45827192; 6.10 VL 40228178 / geo empty; tick1400; primary official NBB WVV 70"),
    ("bud_iglg_omzet_2024", "2024", "45827192", "2024 omzet 45827192 comparative; tick1400; primary official NBB WVV 70"),
    ("bud_iglg_vlsub_2025", "2025", "40228178", "2025 werkingsopbrengsten Vlaamse overheid 40228178; tick1400; primary official NBB WVV 6.10"),
    ("bud_iglg_othops_2025", "2025", "2500490", "2025 andere bedrijfsopbrengsten 2500490; tick1400; primary official NBB WVV 74"),
    ("bud_iglg_explsub_2025", "2025", "1072206", "2025 exploitatiesubsidies 740 1072206; tick1400; primary official NBB WVV 740"),
    ("bud_iglg_diensten_2025", "2025", "5366617", "2025 diensten 5366617 vs 5540729; tick1400; primary official NBB WVV 61"),
    ("bud_iglg_diensten_2024", "2024", "5540729", "2024 diensten 5540729 comparative; tick1400; primary official NBB WVV 61"),
    ("bud_iglg_pers_2025", "2025", "40508243", "2025 personeel 40508243 vs 39970571; 529.5 VTE / YE 680; tick1400; primary official NBB WVV 62"),
    ("bud_iglg_pers_2024", "2024", "39970571", "2024 personeel 39970571 comparative; tick1400; primary official NBB WVV 62"),
    ("bud_iglg_afschr_2025", "2025", "2471902", "2025 afschrijvingen 2471902; tick1400; primary official NBB WVV 630"),
    ("bud_iglg_expl_2025", "2025", "2273226", "2025 expl +2273226 vs +1722590; tick1400; primary official NBB WVV 9901"),
    ("bud_iglg_fininc_2025", "2025", "747317", "2025 fin opbr 747317; tick1400; primary official NBB WVV 75"),
    ("bud_iglg_fincost_2025", "2025", "657435", "2025 fin kosten 657435 (schulden); tick1400; primary official NBB WVV 650"),
    ("bud_iglg_tax_2025", "2025", "65065", "2025 belastingen 65065; tick1400; primary official NBB WVV 67/77"),
    ("bud_iglg_pnl_2025", "2025", "2298043", "2025 PnL +2298043 vs +1596063; tick1400; primary official NBB WVV 9904"),
    ("bud_iglg_pnl_2024", "2024", "1596063", "2024 PnL +1596063 comparative; tick1400; primary official NBB WVV 9904"),
    ("bud_iglg_to_res_2025", "2025", "2116190", "2025 toevoeging reserves 2116190; 694 empty; tick1400; primary official NBB WVV 6921"),
    ("bud_iglg_capex_2025", "2025", "1298097", "2025 capex aanschaf IVA 51306 + geb 59941 + mach 607398 + meub 259772 + CIP 319680; tick1400; primary official NBB WVV"),
    ("bud_iglg_comm_2025", "2025", "11495", "2025 commissaris Foederer 11495; tick1400; primary official NBB WVV 9505"),
    ("bud_iglg_bestuur_2025", "2025", "17987", "2025 bestuurders 9503 17987; tick1400; primary official NBB WVV 9503"),
    ("bud_iglg_hypo_2025", "2025", "28715000", "2025 hypotheekmandaat 28715000; tick1400; primary official NBB WVV 91631"),
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

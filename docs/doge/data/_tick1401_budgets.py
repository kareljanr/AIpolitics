# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_ovco"
SRC = "src_ovco_jr2025_nbb"
BUDGETS = [
    ("bud_ovco_assets_2025", "2025", "9368744", "2025 assets 9368744 VKT-kap 20/58; tick1401; primary official NBB WVV"),
    ("bud_ovco_assets_2024", "2024", "8251394", "2024 assets 8251394 comparative; tick1401; primary official NBB WVV 20/58"),
    ("bud_ovco_fixed_2025", "2025", "8192975", "2025 vaste activa 8192975; tick1401; primary official NBB WVV 21/28"),
    ("bud_ovco_iva_2025", "2025", "1415", "2025 IVA 1415 vs 3795; tick1401; primary official NBB WVV 21"),
    ("bud_ovco_mva_2025", "2025", "8191485", "2025 MVA 8191485 vs 7505866; tick1401; primary official NBB WVV 22/27"),
    ("bud_ovco_gebouwen_2025", "2025", "7087906", "2025 gebouwen 7087906 vs 7351909; tick1401; primary official NBB WVV 22"),
    ("bud_ovco_machines_2025", "2025", "63246", "2025 machines 63246 vs 74672; tick1401; primary official NBB WVV 23"),
    ("bud_ovco_meubilair_2025", "2025", "56557", "2025 meubilair 56557 vs 67044; tick1401; primary official NBB WVV 24"),
    ("bud_ovco_lease_2025", "2025", "7826", "2025 leasing 7826 vs 12241; tick1401; primary official NBB WVV 25"),
    ("bud_ovco_cip_2025", "2025", "975949", "2025 CIP 975949 new; tick1401; primary official NBB WVV 27"),
    ("bud_ovco_fva_2025", "2025", "74", "2025 FVA 74; tick1401; primary official NBB WVV 28"),
    ("bud_ovco_current_2025", "2025", "1175769", "2025 vlottend 1175769 vs 741659; tick1401; primary official NBB WVV 29/58"),
    ("bud_ovco_strecv_2025", "2025", "99940", "2025 ST vorderingen 99940 vs 204859; tick1401; primary official NBB WVV 40/41"),
    ("bud_ovco_trade_recv_2025", "2025", "95970", "2025 handelsvorderingen 95970 vs 180292; tick1401; primary official NBB WVV 40"),
    ("bud_ovco_invest_2025", "2025", "973616", "2025 geldbeleggingen 973616 JUMP vs 401623; tick1401; primary official NBB WVV 50/53"),
    ("bud_ovco_invest_2024", "2024", "401623", "2024 geldbeleggingen 401623 comparative; tick1401; primary official NBB WVV 50/53"),
    ("bud_ovco_cash_2025", "2025", "83941", "2025 liquide middelen 83941 DROP vs 120032; tick1401; primary official NBB WVV 54/58"),
    ("bud_ovco_cash_2024", "2024", "120032", "2024 liquide middelen 120032 comparative; tick1401; primary official NBB WVV 54/58"),
    ("bud_ovco_prepaid_2025", "2025", "18272", "2025 overlopend actief 18272; tick1401; primary official NBB WVV 490/1"),
    ("bud_ovco_equity_2025", "2025", "3054777", "2025 EV 3054777 vs 2734165; tick1401; primary official NBB WVV 10/15"),
    ("bud_ovco_kapitaal_2025", "2025", "571390", "2025 kapitaal 571390; tick1401; primary official NBB WVV 10"),
    ("bud_ovco_reserves_2025", "2025", "57139", "2025 wettelijke reserve 57139; tick1401; primary official NBB WVV 13"),
    ("bud_ovco_re_2025", "2025", "682868", "2025 overgedragen winst 682868 vs 297321; tick1401; primary official NBB WVV 14"),
    ("bud_ovco_capsub_2025", "2025", "1743380", "2025 kapitaalsubsidies 1743380 vs 1808315; tick1401; primary official NBB WVV 15"),
    ("bud_ovco_capsub_2024", "2024", "1808315", "2024 kapitaalsubsidies 1808315 comparative; tick1401; primary official NBB WVV 15"),
    ("bud_ovco_debt_2025", "2025", "6313967", "2025 schulden 6313967 vs 5517229; tick1401; primary official NBB WVV 17/49"),
    ("bud_ovco_debt_2024", "2024", "5517229", "2024 schulden 5517229 comparative; tick1401; primary official NBB WVV 17/49"),
    ("bud_ovco_lt_2025", "2025", "5608298", "2025 LT bank/lease 5608298 vs 5009962; tick1401; primary official NBB WVV 172/3"),
    ("bud_ovco_st_2025", "2025", "699198", "2025 ST schulden 699198 vs 502816; tick1401; primary official NBB WVV 42/48"),
    ("bud_ovco_ltdue_2025", "2025", "383521", "2025 LT-due 383521 vs 341801; tick1401; primary official NBB WVV 42"),
    ("bud_ovco_sttrade_2025", "2025", "198567", "2025 leveranciers 198567 JUMP vs 55511; tick1401; primary official NBB WVV 440/4"),
    ("bud_ovco_sttrade_2024", "2024", "55511", "2024 leveranciers 55511 comparative; tick1401; primary official NBB WVV 440/4"),
    ("bud_ovco_taxsoc_2025", "2025", "113950", "2025 tax/soc 113950 (tax 19995 + soc 93955); tick1401; primary official NBB WVV 45"),
    ("bud_ovco_govguar_2025", "2025", "5991820", "2025 overheidswaarborg 5991820; tick1401; primary official NBB WVV 9061"),
    ("bud_ovco_debt15_2025", "2025", "1581793", "2025 debt 1-5y 1581793; tick1401; primary official NBB WVV 8912"),
    ("bud_ovco_debtgt5_2025", "2025", "4026505", "2025 debt >5y 4026505; tick1401; primary official NBB WVV 8913"),
    ("bud_ovco_brutomarge_2025", "2025", "1163024", "2025 brutomarge 1163024 vs 1101524; omzet 70 empty; tick1401; primary official NBB WVV 9900"),
    ("bud_ovco_brutomarge_2024", "2024", "1101524", "2024 brutomarge 1101524 comparative; tick1401; primary official NBB WVV 9900"),
    ("bud_ovco_pers_2025", "2025", "459819", "2025 personeel 459819 vs 433534; 4.8 VTE / YE 5.7; tick1401; primary official NBB WVV 62"),
    ("bud_ovco_pers_2024", "2024", "433534", "2024 personeel 433534 comparative; tick1401; primary official NBB WVV 62"),
    ("bud_ovco_afschr_2025", "2025", "292709", "2025 afschrijvingen 292709; tick1401; primary official NBB WVV 630"),
    ("bud_ovco_expl_2025", "2025", "409206", "2025 expl +409206 vs +371516; tick1401; primary official NBB WVV 9901"),
    ("bud_ovco_fininc_2025", "2025", "78115", "2025 fin opbr 78115 (capsub 64936); tick1401; primary official NBB WVV 75"),
    ("bud_ovco_capsub_res_2025", "2025", "64936", "2025 capsub in resultaat 64936; tick1401; primary official NBB WVV 753"),
    ("bud_ovco_fincost_2025", "2025", "97851", "2025 fin kosten 97851; tick1401; primary official NBB WVV 65"),
    ("bud_ovco_tax_2025", "2025", "3923", "2025 belastingen 3923; tick1401; primary official NBB WVV 67/77"),
    ("bud_ovco_pnl_2025", "2025", "385548", "2025 PnL +385548 vs +361738; tick1401; primary official NBB WVV 9904"),
    ("bud_ovco_pnl_2024", "2024", "361738", "2024 PnL +361738 comparative; tick1401; primary official NBB WVV 9904"),
    ("bud_ovco_capex_2025", "2025", "975949", "2025 capex MVA aanschaf 975949 CIP; tick1401; primary official NBB WVV 8169"),
    ("bud_ovco_comm_2025", "2025", "5576", "2025 commissaris Callens 5576; tick1401; primary official NBB WVV 6.6"),
    ("bud_ovco_bestuur_2025", "2025", "36968", "2025 bestuurders presentiegeld 36967.75; tick1401; primary official NBB WVV remuneratieverslag"),
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

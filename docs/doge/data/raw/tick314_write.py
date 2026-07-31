# tick 314 — ETNIC FWB ICT dual Digipolis/Smals
from pathlib import Path

base = Path("docs/doge/data")

def append(name: str, text: str) -> None:
    path = base / name
    with open(path, "a", encoding="utf-8", newline="") as f:
        if not text.endswith("\n"):
            text += "\n"
        f.write(text)

append(
    "sources.csv",
    "src_ccrek_fwb_etnic_budget_2024_25,Cour des comptes FWB budget 2024A/2025I section Etnic OAP type1,"
    "https://www.ccrek.be/sites/default/files/Docs/2024_54_BudgetCF_2024A12025I.pdf,"
    "Cour des comptes / Rekenhof,2026-07-30,court_of_audit,"
    '"Strong: Etnic recettes 124.058m adj2024 / 132.841m init2025; liq 124.058m/143.729m; '
    'eng 180.024m/200.356m; reserve repay 11.5m; deficit 10.9m; raw ccrek_etnic_2025.pdf"\n'
    "src_rtbf_etnic_reset_2025,RTBF Galant ETNIC reset 380 agents budget >124m 2024,"
    "https://www.rtbf.be/article/l-etnic-ne-parvient-pas-a-garantir-un-niveau-de-qualite-optimal-vers-un-reset-de-la-structure-chargee-de-la-digitalisation-de-la-fwb-11497668,"
    "RTBF (minister quote),2026-07-30,press,"
    '"Medium: minister Galant 380 agents and budget >124m 2024; transition manager reset; dual CoA strong euros"',
)

append(
    "entities.csv",
    "etnic,ETNIC (Entreprise publique des technologies numeriques),ETNIC,"
    "FWB public digitalisation OAP type1 ICT agency,parastatal,fwb_gov,fr,"
    "https://www.etnic.be,,,,"
    "OAP type1 WBFin II; CoA recettes 124.1m adj2024 / 132.8m init2025 liq 143.7m; "
    "~380 staff medium press; dual Digipolis Smals Ypto; tick314",
)

append(
    "budgets.csv",
    "bud_etnic_recettes_2024,etnic,2024,124058426,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Etnic recettes projet budget ajuste 2024 124058426 EUR CoA\n"
    "bud_etnic_liq_2024,etnic,2024,124058426,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Etnic credits de liquidation ajuste 2024 124058426 EUR\n"
    "bud_etnic_eng_2024,etnic,2024,180024224,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Etnic credits d engagement ajuste 2024 180024224 EUR\n"
    "bud_etnic_recettes_2025,etnic,2025,132840803,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Etnic recettes projet budget initial 2025 132840803 EUR CoA\n"
    "bud_etnic_liq_2025,etnic,2025,143728841,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Etnic credits de liquidation initial 2025 143728841 EUR\n"
    "bud_etnic_eng_2025,etnic,2025,200355745,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Etnic credits d engagement initial 2025 200355745 EUR\n"
    "bud_etnic_reserve_repay_2025,etnic,2025,11500000,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Remboursement reserves Etnic a FWB 11.5m 2025 (deficit driver)\n"
    "bud_etnic_solde_2025,etnic,2025,-10900000,,,budgeted,src_ccrek_fwb_etnic_budget_2024_25,strong,"
    "Solde budgetaire deficit 10.9m 2025 after reserve repay; without repay +0.6m\n"
    "bud_etnic_staff_2024,etnic,2024,380,,,outturn,src_rtbf_etnic_reset_2025,medium,"
    "Minister Galant via RTBF: 380 agents 2024 class; official FTE FOI",
)

cash_etnic = (
    '"{""recettes_adj_2024"":124058426,""liq_2025"":143728841,""eng_2025"":200355745}"'
)
cash_repay = '"{""2025"":11500000}"'
cash_stack = (
    '"{""smals_2025"":578900000,""digipolis_2026"":245610183,'
    '""etnic_liq_2025"":143728841,""ypto_2025"":140170919}"'
)

append(
    "commitments.csv",
    "cmt_etnic_budget_2024_25,ETNIC FWB digitalisation agency budget path 2024-25,etnic,"
    "FWB administrations schools ONE Ares WBE,Decret WBFin II OAP type1 / budget FWB,"
    f"2024-11-01,2024,2025,267887667,{cash_etnic},,active,,"
    "Digitalisation of FWB administration and education systems,"
    "Publish L5 vendors FTE outturn; dual Digipolis Smals unit-cost,"
    "src_ccrek_fwb_etnic_budget_2024_25,strong,FWB>ETNIC>digitalisation,"
    "CoA strong recettes 124.1m adj2024 / 132.8m init2025; liq path 124->144m; reserve clawback 11.5m\n"
    "cmt_etnic_reserve_clawback_2025,ETNIC excess reserve repayment to FWB 11.5m 2025,etnic,"
    "Federation Wallonie-Bruxelles,Decret WBFin II reserve repayment OAP type1,"
    f"2024-11-01,2025,2025,11500000,{cash_repay},0,active,,"
    "Claw back unspent reserves to community budget,"
    "One-off; monitor multi-year reserve build,"
    "src_ccrek_fwb_etnic_budget_2024_25,strong,FWB>ETNIC>reserve_repay,"
    "Only OAP type1/2 with reserve repay in BI2025 per CoA\n"
    "cmt_public_ict_multi_entity_stack,Multi-entity public ICT stack Digipolis ETNIC Smals Ypto,"
    "gg_belgium,Public digital services users multi-level,Institutional dual map DOGE,"
    f"2024-01-01,2024,2025,1089000000,{cash_stack},,active,,"
    "Shared public ICT capacity multi-level Belgium,"
    "Open L5 vendors dual unit-cost; not additive perimeter caution,"
    "src_ccrek_fwb_etnic_budget_2024_25,strong,BE>ICT>public_shared_stack,"
    "Order-of-magnitude dual map only; do not sum as single TE euro without double-count filter",
)

append(
    "leaderboard.csv",
    "lb_etnic_budget_124m,ETNIC FWB ICT agency budget ~124-144m 2024-25,FWB,ops,"
    "FWB>ETNIC>budget,124058426,143728841,"
    "Strong CoA: recettes 124.058m adj2024 / liq 143.729m init2025; eng 200.4m; "
    "dual Digipolis 246m Smals 579m Ypto 140m,strong,src_ccrek_fwb_etnic_budget_2024_25,"
    "FWB admin schools education staff,Community digitalisation OAP type1,"
    "Core digital ops; minister reset narrative medium; reserve clawback 11.5m; L5 vendors FOI,"
    "5,7.5,4,6.2,Publish FTE outturn L5 vendors dual unit-cost Digipolis,seed,,tick314 dual ICT stack\n"
    "lb_etnic_reserve_clawback_11_5m,ETNIC reserve repayment to FWB 11.5m 2025,FWB,ops,"
    "FWB>ETNIC>reserve_repay,11500000,11500000,"
    "Strong CoA: only OAP type1/2 with 2025 reserve repay; drives 10.9m deficit else +0.6m,"
    "strong,src_ccrek_fwb_etnic_budget_2024_25,FWB taxpayers,Claw back unspent agency reserves,"
    "One-off transparency win; prior reserve build opacity,"
    "5,5.5,3,4.7,Annual reserve policy public; multi-year stock,seed,,tick314\n"
    "lb_public_ict_dual_stack_be,Public ICT dual stack Smals Digipolis ETNIC Ypto,federal+regions,ops,"
    "BE>ICT>multi_entity_stack,124058426,578900000,"
    "Strong multi-source dual map: Smals 579m Digipolis 246m ETNIC 124-144m Ypto 140m; "
    "not additive TE; middleman opacity shared pattern,strong,src_ccrek_fwb_etnic_budget_2024_25,"
    "Citizens multi-level public services,Fragmented public ICT delivery capacity,"
    "Dual structures across SS/fed/VL/FWB/rail; L5 external vendors residual,"
    "6,8.5,5,7.0,Consolidate transparency standards; open vendor L5 all entities,seed,,tick314 dual structure map",
)

append(
    "foi_queue.csv",
    "gap_etnic_l5_vendors,FWB>ETNIC>L5_vendors_FTE_outturn,etnic,"
    "Cash outturn 2023-2025 vs budget liq/eng; official FTE multi-year; top-20 external "
    "contractors/vendors EUR; split dotations organiques vs fonctionnelles vs specifiques; "
    "Cepage project cash-by-year; transition manager cost if any,"
    "CoA budget totals strong 124-144m; end-receiver L5 and dual unit-cost vs Digipolis/Smals residual,"
    "6,ETNIC / Federation Wallonie-Bruxelles publicite de l administration,,"
    "https://www.etnic.be,docs/doge/foi/drafts/gap_etnic_l5_vendors.md,ready,2026-07-30,,,,,"
    "cmt_etnic_budget_2024_25,lb_etnic_budget_124m,2026-07-30T19:45:00Z,2026-07-30T19:45:00Z,"
    "tick314 draft ready human send; dual Digipolis Smals",
)

# research_queue: close rq_305, spawn rq_306
rq_path = base / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_305,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; HR Rail deepen dual; other FOI-adjacent). "
    "Prefer before idle.,,2026-07-30T19:15:00Z,,Spawned tick313 after TUC Rail; rq_116 SWA deferred"
)
new = (
    "rq_305,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; HR Rail deepen dual; other FOI-adjacent). "
    "Prefer before idle.,gap_etnic_l5_vendors,2026-07-30T19:15:00Z,2026-07-30T19:45:00Z,"
    "tick314: ETNIC CoA 124-144m dual Digipolis/Smals; FOI L5; spawn rq_306\n"
    "rq_306,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; Cipal Schaubroeck dual Digipolis; "
    "HR Rail deepen; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T19:45:00Z,,Spawned tick314 after ETNIC; rq_116 SWA deferred"
)
if old not in text:
    raise SystemExit("rq_305 row not found for update")
rq_path.write_text(text.replace(old, new), encoding="utf-8")

# loop_state
loop_state = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T19:45:00Z,rq_305,314,no,"
    "Scheduler 60s. Next prio5 rq_306; rq_116 SWA deferred. FOI ready. "
    "tick314 ETNIC ~124-144m dual Digipolis/Smals.\n"
)
(base / "loop_state.csv").write_text(loop_state, encoding="utf-8")

print("tick314 CSV writes OK")

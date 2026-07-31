# tick486 write — FWB SEC path + dual Entity II quartet
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fwb_elements_cles_sec_path_2026_29,FWB elements-cles SEC multi-year path + 700/200/500 effort package,"
        "https://budget-finances.cfwb.be/budget-et-comptabilite/elements-cles-du-budget-annuel/,"
        "Ministère FWB Budget DGBF,2026-08-03,official_budget,"
        "Strong: SEC -1608/-1405/-1390/-1224 2026-29; effort ~700m for <200m new policies → SEC +>500m by 2029; "
        "dep 15.407 rec 13.602; edu 10.929bn; tick486\n"
    )
    f.write(
        "src_fwb_gov_cp_budget_2026_refresh,FWB GW CP Budget 2026-2029 500m net structural refresh,"
        "https://gouvernement.cfwb.be/home/presse--actualites/communiques-de-presse/presses/budget-2026-2029-accord-au-gouvernement-de-la-federation-wallonie-bruxelles-pour-garder-sous-controle-le-deficit-budgetaire.html,"
        "Gouvernement FWB 10 Oct 2025,2026-08-03,official_press,"
        "Strong: 500m structural net = 670m economies + 180m new policies; deficit 1.6bn 2026 path 1.2bn 2029; "
        "debt 12.782bn 2024 risk 21bn 2029; sector measures qualitative; tick486\n"
    )
    f.write(
        "src_fwb_economies_255m_2026_secondary,FWB 255m economies 2026 year-1 secondary multi-outlet,"
        "https://www.rtbf.be/article/quels-secteurs-devront-faire-des-economies-revivez-la-presentation-du-budget-de-la-federation-wallonie-bruxelles-11614064,"
        "RTBF/RTL/Le Soir multi-outlet Oct-Dec 2025,2026-08-03,secondary,"
        "Medium: 255m economies 2026; Le Soir 185 savings + 70 new policies = 255 to find; CSC 255/70; "
        "official year-1 cash table residual FOI; tick486\n"
    )
    f.write(
        "src_dual_entity2_quartet_tick486,Dual Entity II quartet VL+WAL+BRU+FWB consolidation 2026 class,"
        "https://budget-finances.cfwb.be/budget-et-comptabilite/elements-cles-du-budget-annuel/,"
        "DOGE synthesis primary VL+WAL+BRU+FWB,2026-08-03,synthesis,"
        "Strong dual method different perimeter: VL 1.832bn + WAL 270m + BRU 297m + FWB 255m medium year-1 "
        "= 2.654bn class 2026; FWB net 500m path 2029 strong; tick486\n"
    )

buds = [
    "bud_fwb_sec_2026,fwb_gov,2026,-1608000000,,,budgeted,src_fwb_elements_cles_sec_path_2026_29,strong,FWB SEC financing -1.608bn 2026 initial (elements-cles path); tick486",
    "bud_fwb_sec_2027,fwb_gov,2027,-1405000000,,,budgeted,src_fwb_elements_cles_sec_path_2026_29,strong,FWB SEC path -1.405bn 2027; tick486",
    "bud_fwb_sec_2028,fwb_gov,2028,-1390000000,,,budgeted,src_fwb_elements_cles_sec_path_2026_29,strong,FWB SEC path -1.390bn 2028; tick486",
    "bud_fwb_sec_2029,fwb_gov,2029,-1224000000,,,budgeted,src_fwb_elements_cles_sec_path_2026_29,strong,FWB SEC path -1.224bn 2029 (stabilize ~1.2bn DPC target); tick486",
    "bud_fwb_effort_package_2029,fwb_gov,2029,500000000,,,budgeted,src_fwb_elements_cles_sec_path_2026_29,strong,FWB SEC improvement >500m by 2029 from ~700m effort / <200m new policies; tick486",
    "bud_fwb_economies_gross_2029,fwb_gov,2029,670000000,,,budgeted,src_fwb_gov_cp_budget_2026_refresh,strong,FWB gross economies 670m path to 2029 (GW CP; with 180m new = 500 net); tick486",
    "bud_fwb_new_policies_2029,fwb_gov,2029,180000000,,,budgeted,src_fwb_gov_cp_budget_2026_refresh,strong,FWB politiques nouvelles 180m path to 2029; tick486",
    "bud_fwb_economies_2026_year1,fwb_gov,2026,255000000,,,budgeted,src_fwb_economies_255m_2026_secondary,medium,FWB year-1 economies class 255m 2026 (multi-outlet secondary; official L5 FOI); tick486",
    "bud_fwb_debt_stock_2024,fwb_gov,2024,12782100000,,,outturn,src_fwb_gov_cp_budget_2026_refresh,strong,FWB debt stock 12.7821bn 2024 (GW CP; risk path 21bn 2029 unmitigated); tick486",
    "bud_fwb_lsf_dotations_2026,fwb_gov,2026,12996000000,,,budgeted,src_fwb_elements_cles_sec_path_2026_29,strong,FWB LSF dotations 12.996bn of 13.602bn recettes 2026; tick486",
    "bud_fwb_dot_rw_cocof_2026,fwb_gov,2026,575316000,,,budgeted,src_fwb_elements_cles_sec_path_2026_29,strong,FWB dotations RW+COCOF Saint-Quentin 575.316m 2026; tick486",
    "bud_dual_entity2_quartet_2026,gg_belgium,2026,2654000000,,,derived,src_dual_entity2_quartet_tick486,medium,Entity II quartet class VL1.832+WAL0.270+BRU0.297+FWB0.255=2.654bn 2026 different perimeter; FWB year1 medium; tick486",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in buds:
        f.write(r + "\n")

cmt1 = (
    "cmt_fwb_sec_trajectory_2026_29,FWB SEC multi-year path -1.608bn to -1.224bn + effort package,"
    "fwb_gov,Education culture social community services,"
    "DGBF elements-cles + GW CP Budget 2026-2029,2025-10-10,2026,2029,500000000,"
    '"{""sec_2026"":-1608000000,""sec_2027"":-1405000000,""sec_2028"":-1390000000,""sec_2029"":-1224000000,'
    '""net_effort_2029"":500000000,""gross_economies_2029"":670000000,""new_policies_2029"":180000000,'
    '""effort_class_elements"":700000000,""new_policies_elements_lt"":200000000,'
    '""deficit_2026_class"":1600000000,""year1_economies_medium"":255000000,'
    '""debt_2024"":12782100000,""debt_risk_2029_unmitigated"":21000000000,'
    '""dep_2026"":15407000000,""rec_2026"":13602000000,""edu_2026"":10928638000,'
    '""note"":""Strong SEC path+package; year-1 255m secondary multi-outlet; L5 sector cash FOI""}",'
    "0,active,https://budget-finances.cfwb.be/budget-et-comptabilite/elements-cles-du-budget-annuel/,"
    "Stabilize FWB deficit ~1.2bn 2029 dual Entity II,Publish year-by-year L5 economies matrix FOI,"
    "src_fwb_elements_cles_sec_path_2026_29,strong,FWB>begroting>SEC_path_2026_29,tick486 dual quartet"
)
cmt2 = (
    "cmt_dual_entity2_quartet_consol_2026,Dual Entity II quartet VL+WAL+BRU+FWB consolidation 2026,"
    "gg_belgium,Communities Regions Entity II,"
    "VL centenboekje + WAL press + CoA BRU + FWB elements-cles,2025-01-01,2026,2026,2654000000,"
    '"{""vl_measures_2026"":1832000000,""wal_economies_2026"":270000000,'
    '""bru_measures_2026"":297000000,""fwb_economies_2026_medium"":255000000,'
    '""sum_class"":2654000000,""fwb_net_2029"":500000000,""fwb_sec_2029"":-1224000000,'
    '""note"":""not additive TE; different perimeter; FWB year1 medium secondary; dual Entity II map complete class""}",'
    "0,active,https://budget-finances.cfwb.be/budget-et-comptabilite/elements-cles-du-budget-annuel/,"
    "Entity II dual fiscal consolidation full map,Official FWB year1 cash table FOI,"
    "src_dual_entity2_quartet_tick486,medium,BE>dual>consolidation_Entity2_quartet_2026,tick486"
)
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt1 + "\n")
    f.write(cmt2 + "\n")

lbs = [
    "lb_fwb_sec_path_1_6bn,FWB SEC path -1.608bn 2026 to -1.224bn 2029,FWB,ops,FWB>begroting>SEC_path,-1608000000,-1224000000,Strong elements-cles multi-year; dual VL/WAL/BRU consolidation map,strong,src_fwb_elements_cles_sec_path_2026_29,FWB residents education,Community deficit stabilize 1.2bn,Education-heavy dual,3.5,9.0,5,6.1,L5 delivery FOI,seed,,tick486",
    "lb_fwb_effort_500m_2029,FWB structural net effort 500m by 2029,FWB,subsidy_reform,FWB>begroting>effort_structurel,500000000,670000000,Strong 670 economies +180 new =500 net GW CP + elements-cles; dual triad,strong,src_fwb_gov_cp_budget_2026_refresh,All FWB sectors,Fiscal sustainability path,Reform dual Entity II,3.5,8.0,5,5.6,gap_fwb_economies_l5,seed,,tick486",
    "lb_fwb_economies_255m_2026,FWB year-1 economies class 255m 2026,FWB,subsidy_reform,FWB>begroting>economies_2026,255000000,255000000,Medium multi-outlet; Le Soir 185+70; official year1 L5 FOI residual,medium,src_fwb_economies_255m_2026_secondary,Education culture youth,Year-1 consolidation cash,Opacity official table,4.0,7.0,5,5.4,gap_fwb_economies_l5,seed,,tick486",
    "lb_dual_entity2_quartet_2_65bn,Dual Entity II quartet consolidation class 2.65bn 2026,multi,programme,BE>dual>Entity2_quartet_2026,2654000000,2654000000,Medium/strong mix: VL1.83 WAL0.27 BRU0.30 FWB0.26; different perimeter not TE,medium,src_dual_entity2_quartet_tick486,Entity II,Full dual regional+community map,Closes Entity II dual slice,3.5,9.0,5,6.1,FWB year1 FOI,seed,,tick486",
    "lb_fwb_debt_12_8bn,FWB debt stock 12.78bn 2024 risk 21bn 2029,FWB,ops,FWB>dette,12782100000,21000000000,Strong GW CP stock 2024; risk path unmitigated class; dual regional debt,strong,src_fwb_gov_cp_budget_2026_refresh,FWB taxpayers,Debt sustainability,Interest snowball dual,4.0,8.5,5,6.0,Track mitigated path,seed,,tick486",
    "lb_fwb_dot_rw_cocof_575m,FWB Saint-Quentin dots RW+COCOF 575m 2026,FWB,transfer,FWB>dotations>RW_COCOF,575316000,575316000,Strong elements-cles; dual WAL/BRU receive side,strong,src_fwb_elements_cles_sec_path_2026_29,Wallonia COCOF,Competence transfer financing,Institutional transfer not waste,2.5,7.5,4,5.0,Map receive-side recon,seed,,tick486",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lbs:
        f.write(r + "\n")

foi = (
    "gap_fwb_economies_l5,FWB>begroting>economies_structurelles>L5,fwb_gov,"
    "Official cash-by-year L5 matrix of gross economies 670m and net 500m path 2026-2029 by sector/programme "
    "(confirm 255m year-1 2026; split enseignement culture ONE jeunesse AJ MDJ FP cabinets); "
    "reconcile elements-cles 700/200 package vs GW CP 670/180,"
    "Package totals strong public; year-1 and sector L5 opaque dual VL/WAL/BRU map incomplete,"
    "7,Ministère FWB Budget et Finances publicité de l administration / DGBF,,,"
    "docs/doge/foi/drafts/gap_fwb_economies_l5.md,"
    "ready,2026-08-03,,,,,cmt_fwb_sec_trajectory_2026_29,lb_fwb_effort_500m_2029,"
    "2026-08-03T09:45:00Z,2026-08-03T09:45:00Z,tick486 draft ready human send; SEC path filled"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi + "\n")

print("CSV writes OK")

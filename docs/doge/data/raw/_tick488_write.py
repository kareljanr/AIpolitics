# tick488 — CM Jul 2026 Entity I path effort 7.7bn + unallocated L5 dual
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_cm_jul2026_entity1,Comité de monitoring Jul 2026 Entity I actualisation deficit control-account,"
        "https://bosa.belgium.be/sites/default/files/publications/documents/260706%20Rapport%20Monitoringcomit%C3%A9%20-%20Version%20d%C3%A9finitive.pdf,"
        "SPF BOSA Comité de monitoring 6 Jul 2026,2026-08-03,official_budget,"
        "Strong: Entity I deficit -25.68/-30.34/-34.03/-38.28/-40.67/-44.50 bn 2026-31; control cum gap 7.7bn 2029; "
        "GG debt 110.7→122.6; E1 debt 86.3→97.7; net exp 197.6→219.6; unallocated measures L5; upgrades FPB 4.9bn Mar; tick488\n"
    )
    f.write(
        "src_cm_jul2026_bosa_news,BOSA news CM Jul 2026 headlines deficit debt,"
        "https://bosa.belgium.be/fr/news/comite-de-monitoring-actualisation-2026-estimation-2027-et-estimation-pluriannuelle-2028-2031,"
        "SPF BOSA 6 Jul 2026,2026-08-03,official_press,"
        "Strong headlines: E1 deficit 3.9pct/25.7bn 2026 5.7pct/44.5bn 2031; GG deficit 5.1pct 2025-27 to 6.2pct 2031; "
        "debt 107.9→122.6; tick488\n"
    )
    f.write(
        "src_dual_e1_control_gap_7_7_tick488,Dual Entity I control gap path 4.9 Mar→7.7 Jul 2026 vs E2 quartet,"
        "https://bosa.belgium.be/sites/default/files/publications/documents/260706%20Rapport%20Monitoringcomit%C3%A9%20-%20Version%20d%C3%A9finitive.pdf,"
        "DOGE synthesis CM+prior,2026-08-03,synthesis,"
        "Strong dual: residual control cum gap 7.7bn 2029 (was 4.9 Mar pre-Iran); path 0.6/2.4/5.8/7.7; "
        "vs E2 quartet 2.65bn class 2026 different metric; tick488\n"
    )

buds = [
    "bud_entity1_def_2026_cm,sec_federal,2026,-25680000000,,,estimated,src_cm_jul2026_entity1,strong,Entity I SEC deficit -25.680bn 2026 CM Jul (Mon column; -3.9pct GDP); tick488",
    "bud_entity1_def_2027_cm,sec_federal,2027,-30344000000,,,estimated,src_cm_jul2026_entity1,strong,Entity I SEC deficit -30.344bn 2027 CM Jul -4.4pct GDP; tick488",
    "bud_entity1_def_2028_cm,sec_federal,2028,-34028000000,,,estimated,src_cm_jul2026_entity1,strong,Entity I SEC deficit -34.028bn 2028 CM Jul -4.8pct GDP; tick488",
    "bud_entity1_def_2029_cm,sec_federal,2029,-38275000000,,,estimated,src_cm_jul2026_entity1,strong,Entity I SEC deficit -38.275bn 2029 CM Jul -5.2pct GDP; dual RTBF 38.5 class; tick488",
    "bud_entity1_def_2031_cm,sec_federal,2031,-44496000000,,,estimated,src_cm_jul2026_entity1,strong,Entity I SEC deficit -44.496bn 2031 CM Jul -5.7pct GDP; tick488",
    "bud_fed_def_2026_cm,sec_federal,2026,-25818000000,,,estimated,src_cm_jul2026_entity1,strong,Federal power deficit -25.818bn 2026 CM Jul; tick488",
    "bud_fed_def_2029_cm,sec_federal,2029,-41175000000,,,estimated,src_cm_jul2026_entity1,strong,Federal power deficit -41.175bn 2029 CM Jul; tick488",
    "bud_ss_balance_2026_cm,sec_ss,2026,-44000000,,,estimated,src_cm_jul2026_entity1,strong,SS balance -44m 2026 CM Jul (near zero); tick488",
    "bud_ss_balance_2027_cm,sec_ss,2027,1394000000,,,estimated,src_cm_jul2026_entity1,strong,SS surplus +1.394bn 2027 CM Jul; tick488",
    "bud_entity1_unalloc_2026,sec_federal,2026,183000000,,,budgeted,src_cm_jul2026_entity1,strong,Mesures non réparties total +183m 2026 (positive for saldo); tick488",
    "bud_entity1_unalloc_2027,sec_federal,2027,1415000000,,,budgeted,src_cm_jul2026_entity1,strong,Mesures non réparties +1.415bn 2027; tick488",
    "bud_entity1_unalloc_2029,sec_federal,2029,2192000000,,,budgeted,src_cm_jul2026_entity1,strong,Mesures non réparties +2.192bn 2029 path; tick488",
    "bud_entity1_control_gap_2029_cm,sec_federal,2029,7700000000,,,estimated,src_cm_jul2026_entity1,strong,Control-account cumulative deviation 7.7bn 2029 (Table16; upgrades Mar 4.9bn); tick488",
    "bud_entity1_control_gap_2028_cm,sec_federal,2028,5800000000,,,estimated,src_cm_jul2026_entity1,strong,Control cum gap 5.8bn 2028; tick488",
    "bud_entity1_control_gap_2031_cm,sec_federal,2031,9800000000,,,estimated,src_cm_jul2026_entity1,strong,Control cum gap 9.8bn 2031; tick488",
    "bud_entity1_netexp_2026_cm,sec_federal,2026,197600000000,,,estimated,src_cm_jul2026_entity1,strong,Entity I net expenditure 197.6bn 2026 CM; tick488",
    "bud_entity1_netexp_2029_cm,sec_federal,2029,219600000000,,,estimated,src_cm_jul2026_entity1,strong,Entity I net expenditure 219.6bn 2029 CM; tick488",
    "bud_gg_debt_pct_2026_cm,gg_belgium,2026,110.7,,,estimated,src_cm_jul2026_entity1,strong,GG debt 110.7pct GDP 2026 CM Jul path to 122.6 2031; tick488",
    "bud_gg_debt_pct_2029_cm,gg_belgium,2029,117.1,,,estimated,src_cm_jul2026_entity1,strong,GG debt 117.1pct GDP 2029 CM Jul; tick488",
    "bud_gg_debt_pct_2031_cm,gg_belgium,2031,122.6,,,estimated,src_cm_jul2026_entity1,strong,GG debt 122.6pct GDP 2031 CM Jul; tick488",
    "bud_entity1_debt_pct_2026_cm,sec_federal,2026,86.3,,,estimated,src_cm_jul2026_entity1,strong,Entity I debt 86.3pct GDP 2026 path 97.7 2031; tick488",
    "bud_entity1_debt_pct_2029_cm,sec_federal,2029,92.3,,,estimated,src_cm_jul2026_entity1,strong,Entity I debt 92.3pct GDP 2029; tick488",
    "bud_entity1_sousutil_2026,sec_federal,2026,1625000000,,,budgeted,src_cm_jul2026_entity1,strong,Sous-utilisation objective total 1.625bn 2026 (prim 1.255 OIP 0.148 IPSS 0.221); tick488",
    "bud_entity1_sousutil_2029,sec_federal,2029,1750000000,,,budgeted,src_cm_jul2026_entity1,strong,Sous-utilisation 1.750bn 2029; tick488",
    "bud_entity1_interest_2029_cm,sec_federal,2029,18600000000,,,estimated,src_cm_jul2026_entity1,strong,Interest charges ~18.6bn 2029 CM vs 17.5 CB2026 (Table9 diff); tick488",
    "bud_unalloc_subsidy_cut_2029,sec_federal,2029,199000000,,,budgeted,src_cm_jul2026_entity1,strong,Unalloc: reduction federal subsidies 199m 2029 path (49/74/99/199); tick488",
    "bud_unalloc_reorg_fed_2029,sec_federal,2029,150000000,,,budgeted,src_cm_jul2026_entity1,strong,Unalloc: federal reorg 150m + centralisation staff services 150m 2029; tick488",
    "bud_unalloc_fraud_pack_2029,sec_federal,2029,482000000,,,budgeted,src_cm_jul2026_entity1,strong,Unalloc: fraud fight+compliance FPS Finance 482m 2029 (0/147/446/482); tick488",
    "bud_unalloc_fiod_2029,sec_federal,2029,193000000,,,budgeted,src_cm_jul2026_entity1,strong,Unalloc: FIOD+national financial prosecutor 193m 2029; tick488",
    "bud_unalloc_replace_ratio_2029,sec_federal,2029,175000000,,,budgeted,src_cm_jul2026_entity1,strong,Unalloc: selective public replacement ratio 100→175m 2026-29; tick488",
    "bud_dual_e1_gap_7_7_2029,gg_belgium,2029,7700000000,,,derived,src_dual_e1_control_gap_7_7_tick488,strong,Dual E1 control residual 7.7bn 2029 vs E2 quartet 2.65bn 2026 class; tick488",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in buds:
        f.write(r + "\n")

cmt1 = (
    "cmt_cm_jul2026_entity1_path,Entity I multi-year path CM Jul 2026 deficit+control 7.7bn,"
    "sec_federal,Federal+SS taxpayers,"
    "Comité de monitoring rapport 6 Jul 2026 version définitive,2026-07-06,2026,2031,7700000000,"
    '"{""def_path_m"":[-25680,-30344,-34028,-38275,-40672,-44496],'
    '""years"":[2026,2027,2028,2029,2030,2031],'
    '""def_pct"":[-3.9,-4.4,-4.8,-5.2,-5.4,-5.7],'
    '""primary_pct"":[-2.0,-2.3,-2.4,-2.7,-2.6,-2.7],'
    '""interest_pct"":[1.9,2.1,2.3,2.5,2.8,3.0],'
    '""control_cum_bn"":[0.6,2.4,5.8,7.7,8.4,9.8],'
    '""netexp_bn"":[197.6,205.4,213.7,219.6,224.5,231.6],'
    '""gg_debt_pct"":[110.7,112.7,114.9,117.1,119.7,122.6],'
    '""e1_debt_pct"":[86.3,88.1,90.2,92.3,94.8,97.7],'
    '""unalloc_path_m"":[183,1415,1544,2192,2192,2192],'
    '""fed_def_2029_m"":-41175,""ss_2029_m"":708,'
    '""prior_mar_gap_bn"":4.9,""note"":""upgrades tick487 FPB 4.9bn Mar pre-Iran; Iran/macro Jun FPB parameters""}",'
    "0,active,https://bosa.belgium.be/sites/default/files/publications/documents/260706%20Rapport%20Monitoringcomit%C3%A9%20-%20Version%20d%C3%A9finitive.pdf,"
    "Track Entity I EU net-exp control account,"
    "Deliver 7.7bn residual measures by 2029; dual FPB options menu,"
    "src_cm_jul2026_entity1,strong,Entity_I>CM_jul2026>path,tick488 dual residual upgrade"
)
cmt2 = (
    "cmt_cm_unallocated_measures_l5_2026_31,Entity I unallocated measures package L5 multi-year,"
    "sec_federal,Admin fraud subsidy recipients,"
    "CM Jul 2026 Table11 mesures non réparties,2026-07-06,2026,2031,2192000000,"
    '"{""total_2029_m"":2192,""path_m"":[183,1415,1544,2192],'
    '""subsidy_cut_2029_m"":199,""reorg_2029_m"":150,""central_staff_2029_m"":150,'
    '""fraud_compliance_2029_m"":482,""fiod_2029_m"":193,""replace_ratio_2029_m"":175,'
    '""social_fraud_div_2029_m"":200,""tax_fraud_shoulders_2029_m"":200,'
    '""prestige_2029_m"":30,""note"":""positive for saldo if delivered; soft measures risk""}",'
    "0,active,https://bosa.belgium.be/sites/default/files/publications/documents/260706%20Rapport%20Monitoringcomit%C3%A9%20-%20Version%20d%C3%A9finitive.pdf,"
    "Deliver soft consolidation package inside Entity I path,"
    "Publish outturn vs plan each measure; FOI if under-delivery,"
    "src_cm_jul2026_entity1,strong,Entity_I>mesures_non_reparties_L5,tick488"
)
cmt3 = (
    "cmt_dual_e1_control_7_7_vs_e2,Dual E1 control residual 7.7bn 2029 vs E2 quartet,"
    "gg_belgium,All public entities,"
    "CM Jul 2026 + prior Entity II dual ticks,2026-07-06,2026,2029,7700000000,"
    '"{""e1_control_2029"":7700000000,""e1_prior_mar"":4900000000,""e1_decided_package"":9200000000,'
    '""e2_quartet_2026"":2654000000,""note"":""residual control after decided path; dual not additive TE""}",'
    "0,active,https://bosa.belgium.be/sites/default/files/publications/documents/260706%20Rapport%20Monitoringcomit%C3%A9%20-%20Version%20d%C3%A9finitive.pdf,"
    "Map dual federal residual vs regional consolidation,"
    "Comparable control accounts all entities,"
    "src_dual_e1_control_gap_7_7_tick488,strong,BE>dual>E1_7_7_vs_E2,tick488"
)
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt1 + "\n")
    f.write(cmt2 + "\n")
    f.write(cmt3 + "\n")

lbs = [
    "lb_entity1_control_gap_7_7bn,Entity I control-account residual gap 7.7bn 2029 CM Jul,federal,ops,Entity_I>control_account>gap_2029,7700000000,9800000000,Strong CM Table16 upgrades Mar 4.9bn; path to 9.8bn 2031; dual E2,strong,src_cm_jul2026_entity1,Public finances EU path,Close net-exp control account,Material residual dual,4.5,9.5,6,6.8,2027 budget package,seed,,tick488",
    "lb_entity1_def_38_3bn_2029,Entity I SEC deficit 38.3bn 2029 path CM Jul,federal,ops,Entity_I>SEC_deficit_2029,38275000000,44496000000,Strong Table8 -38.275bn 2029 -44.5bn 2031; dual prior 31.2 expose,strong,src_cm_jul2026_entity1,Taxpayers,Entity I financing balance,Primary+interest snowball,4.0,10.0,7,6.6,Primary surplus path,seed,,tick488",
    "lb_entity1_unalloc_2_2bn,Entity I unallocated measures package 2.192bn 2029,federal,subsidy_reform,Entity_I>mesures_non_reparties,2192000000,2192000000,Strong Table11 L5 fraud reorg subsidies FIOD replace-ratio; delivery risk soft,strong,src_cm_jul2026_entity1,Admin fraud subsidy,Soft consolidation delivery,Opacity if under-executed,5.0,8.0,5,6.0,Publish outturn FOI if miss,seed,,tick488",
    "lb_gg_debt_122_6pct_2031,GG debt path to 122.6pct GDP 2031 CM Jul,multi,ops,BE>GG>debt_path,0,0,Strong 107.9 2025 → 122.6 2031; dual NBB prior ~120 2030 class,strong,src_cm_jul2026_entity1,All residents,Debt sustainability,Snowball dual interest,4.5,9.5,6,6.8,Primary surplus all entities,seed,,tick488",
    "lb_unalloc_fraud_compliance_482m,Unalloc fraud+FPS compliance 482m 2029 path,federal,ops,Entity_I>fraude_compliance,482000000,482000000,Strong CM L5 0/147/446/482; dual prior antifraud soft,strong,src_cm_jul2026_entity1,Tax social fraud,Revenue compliance package,Delivery KPI risk,4.0,7.5,5,5.6,Publish cash outturn,seed,,tick488",
    "lb_unalloc_subsidy_cut_199m,Unalloc federal subsidy cut 199m 2029,federal,subsidy,Entity_I>subsidies>cut_path,199000000,199000000,Strong CM path 49/74/99/199; dual NBB firm subsidies,strong,src_cm_jul2026_entity1,Firm subsidy recipients,Discretionary subsidy cut,Named L5 residual,4.5,7.0,5,5.6,gap residual optional,seed,,tick488",
    "lb_dual_e1_7_7_e2_map,Dual E1 control 7.7bn + E2 quartet pressure map,multi,programme,BE>dual>E1_E2_pressure_v2,7700000000,10354000000,Strong upgraded dual; E1 residual control vs E2 2.65bn 2026 class,strong,src_dual_e1_control_gap_7_7_tick488,All public entities,Belgium consolidation pressure,Method dual map,3.5,9.5,5,6.2,Comparable ledgers,seed,,tick488",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lbs:
        f.write(r + "\n")

print("CSV writes OK")

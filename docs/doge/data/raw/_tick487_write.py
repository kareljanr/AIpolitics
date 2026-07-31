# tick487 — FPB 250+ measures inventory Entity I budget 2027 + dual residual gap
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fpb_budget2027_measures_report,FPB Report 13320 Options politiques budget 2027 250+ mesures,"
        "https://www.plan.be/sites/default/files/documents/REP_BUDGET2027_13320_FR.pdf,"
        "Bureau fédéral du Plan 1 Jun 2026,2026-08-03,official_research,"
        "Strong: 250+ measures inventory; Entity I control-account gap 4.9bn 2029 pre-Iran; "
        "SS 147.3 pens 72.3 health 41.3 invalid 15.9 chom 4.6; federal own 41.9 salaries 10.9 "
        "fonct 8.5 subs 7.9 inv 6.5 interest 12.3 UE 9.1 transfers C&R 81.5; recettes 267.4; tick487\n"
    )
    f.write(
        "src_fpb_budget2027_measures_xlsx,FPB DATA_BUDGET2027 xlsx 263 measures impulse column,"
        "https://www.plan.be/sites/default/files/documents/DATA_BUDGET2027_13320.xlsx,"
        "Bureau fédéral du Plan 1 Jun 2026,2026-08-03,official_data,"
        "Strong: 263 rows; 39 with 2029 annual impulse mEUR (DC2024 only); NOT additive alternatives; "
        "top cats niches 46 PIT 35 health 21; max single 15bn asset sale; tick487\n"
    )
    f.write(
        "src_fpb_budget2027_press,FPB press 250+ measures ~230 external +30 DC2024,"
        "https://www.plan.be/fr/publications/plus-de-250-mesures-pour-ameliorer-la-situation,"
        "Bureau fédéral du Plan PRESS_20260602,2026-08-03,official_press,"
        "Strong: gov request 17 Apr 2026; ~230 external + ~30 electoral DC; not ranked by FPB; tick487\n"
    )
    f.write(
        "src_dual_e1_e2_gap_tick487,Dual Entity I residual control gap 4.9bn vs Entity II quartet,"
        "https://www.plan.be/sites/default/files/documents/REP_BUDGET2027_13320_FR.pdf,"
        "DOGE synthesis FPB+prior Entity II,2026-08-03,synthesis,"
        "Strong dual: Entity I residual control-account 4.9bn 2029 (on top of prior 9.2bn package); "
        "Entity II quartet class 2.65bn 2026 different perimeter; tick487\n"
    )

buds = [
    # Entity I masses BI2026 from FPB report (strong BOSA via FPB)
    "bud_entity1_ss_dep_2026,sec_ss,2026,147300000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Entity I SS dep 147.3bn BI2026 (FPB; pens half health 28pct invalid 11pct); tick487",
    "bud_entity1_pens_2026,sec_ss,2026,72300000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Pensions 72.3bn BI2026 10.9pct GDP; reform cuts aging cost +1.4pp GDP 2024-70; tick487",
    "bud_entity1_health_2026,sec_ss,2026,41300000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Health care 41.3bn BI2026 6.2pct GDP; growth norm 2.0-3.0pct path; tick487",
    "bud_entity1_invalidity_2026,sec_ss,2026,15900000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Maladie-invalidite 15.9bn BI2026 2.4pct GDP; tick487",
    "bud_entity1_chomage_2026,sec_ss,2026,4600000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Chomage+interruptions 4.6bn BI2026 0.7pct GDP; tick487",
    "bud_entity1_ss_other_prest_2026,sec_ss,2026,10100000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Other SS prestations 10.1bn BI2026; tick487",
    "bud_entity1_ss_admin_2026,sec_ss,2026,3000000000,,,budgeted,src_fpb_budget2027_measures_report,strong,SS frais de gestion 3.0bn BI2026; tick487",
    "bud_entity1_transfers_cr_2026,sec_federal,2026,81500000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Transfers regions/communities LSF 81.5bn BI2026 12.3pct GDP; tick487",
    "bud_entity1_fed_own_2026,sec_federal,2026,41900000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Federal own dep 41.9bn BI2026 7.2pct GDP (vs 36.1bn 2024 defence-driven); tick487",
    "bud_entity1_salaries_2026,sec_federal,2026,10900000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Federal salaries 10.9bn; defence+police+justice+interior 5.9bn 54pct; tick487",
    "bud_entity1_fonct_2026,sec_federal,2026,8500000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Federal fonctionnement 8.5bn BI2026; tick487",
    "bud_entity1_subsidies_2026_confirm,sec_federal,2026,7900000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Federal subsidies 7.9bn confirm FPB (prior FPB/BOSA); tick487",
    "bud_entity1_invest_2026_confirm,sec_federal,2026,6500000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Federal invest 6.5bn; defence ~71pct Infrabel 17pct; tick487",
    "bud_entity1_handicap_grapa_2026,sec_federal,2026,4300000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Handicap+GRAPA 4.3bn BI2026 federal; tick487",
    "bud_entity1_ue_transfers_2026,sec_federal,2026,9100000000,,,budgeted,src_fpb_budget2027_measures_report,strong,UE budget transfers 9.1bn BI2026 1.4pct GDP; tick487",
    "bud_entity1_interest_2026_confirm,sec_federal,2026,12300000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Interest Entity I 12.3bn 1.9pct GDP path 2.5pct 2029; tick487",
    "bud_entity1_recettes_total_2026,sec_federal,2026,267400000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Entity I recettes total 267.4bn BI2026 40.2pct GDP; tick487",
    "bud_entity1_fiscal_rec_2026,sec_federal,2026,164300000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Fiscal receipts 164.3bn BI2026; tick487",
    "bud_entity1_ssc_rec_2026,sec_ss,2026,93700000000,,,budgeted,src_fpb_budget2027_measures_report,strong,SSC contributions 93.7bn BI2026 14.1pct GDP; tick487",
    "bud_entity1_ipp_2026,sec_federal,2026,64200000000,,,budgeted,src_fpb_budget2027_measures_report,strong,IPP 64.2bn BI2026 9.7pct GDP; tick487",
    "bud_entity1_isoc_2026,sec_federal,2026,26000000000,,,budgeted,src_fpb_budget2027_measures_report,strong,Corporate tax 26.0bn BI2026 3.9pct GDP; tick487",
    "bud_entity1_control_gap_2029,sec_federal,2029,4900000000,,,estimated,src_fpb_budget2027_measures_report,strong,Entity I control-account residual gap 4.9bn 2029 unchanged policy (CM Mar 2026 pre-Iran; FPB); NOT on top of decided 9.2 package conflation; tick487",
    "bud_fpb_measures_inventory_count_2026,sec_federal,2026,263,,,count,src_fpb_budget2027_measures_xlsx,strong,FPB inventory 263 measure rows (press 250+; ~230 external + ~30 DC2024); tick487",
    "bud_fpb_measures_quantified_2029,sec_federal,2029,39,,,count,src_fpb_budget2027_measures_xlsx,strong,39 of 263 measures have DC2024 annual impulse EUR m 2029; alternatives not additive; tick487",
    "bud_dual_e1_residual_gap_2029,gg_belgium,2029,4900000000,,,derived,src_dual_e1_e2_gap_tick487,strong,Entity I residual control gap 4.9bn 2029 dual vs Entity II quartet 2.65bn 2026 class different metric; tick487",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in buds:
        f.write(r + "\n")

cmt1 = (
    "cmt_fpb_budget2027_measures_inventory,FPB 250+ policy options inventory for federal budget 2027,"
    "sec_federal,Entity I federal+SS taxpayers beneficiaries,"
    "FPB Report 13320 + DATA xlsx gov request 17 Apr 2026,2026-06-01,2027,2029,4900000000,"
    '"{""n_measures_xlsx"":263,""n_press_class"":250,""external_class"":230,""dc2024_class"":30,'
    '""n_quantified_impulse_2029"":39,""control_gap_2029_bn"":4.9,""control_gap_pct_gdp"":0.67,'
    '""pre_iran_war"":true,""ss_dep_2026_bn"":147.3,""pens_bn"":72.3,""health_bn"":41.3,'
    '""invalid_bn"":15.9,""chom_bn"":4.6,""transfers_cr_bn"":81.5,""fed_own_bn"":41.9,'
    '""salaries_bn"":10.9,""fonct_bn"":8.5,""subs_bn"":7.9,""invest_bn"":6.5,""interest_bn"":12.3,'
    '""ue_bn"":9.1,""recettes_bn"":267.4,""fiscal_bn"":164.3,""ssc_bn"":93.7,""ipp_bn"":64.2,'
    '""isoc_bn"":26.0,""dc_health_norm_range_bn"":[3.3,4.5],""dc_invalid_range_bn"":[0.6,0.8],'
    '""dc_asylum_range_bn"":[0.55,0.7],""dc_dgd_cut_bn"":1.5,""dc_subs_cut_range_bn"":[0.9,1.3],'
    '""dc_cars_cheques_range_bn"":[4.5,5.5],""dc_fossil_transport_range_bn"":[0.8,1.25],'
    '""dc_globalisation_range_bn"":[5.5,11.3],""dc_wealth_tax_range_bn"":[2.0,7.5],'
    '""dc_capital_gains_range_bn"":[2.9,3.8],""admin_linear_1_8pct_yr"":true,'
    '""note"":""OPTIONS inventory not adopted budget; impulses not additive; dual residual gap vs 9.2bn decided package""}",'
    "0,active,https://www.plan.be/sites/default/files/documents/REP_BUDGET2027_13320_FR.pdf,"
    "Inform 2027 budget negotiations Entity I control account,"
    "Track which measures adopted; dual Entity II map,"
    "src_fpb_budget2027_measures_report,strong,Federal>budget2027>FPB_options_inventory,tick487 dual residual"
)
cmt2 = (
    "cmt_dual_e1_residual_vs_e2_quartet,Dual Entity I residual 4.9bn gap vs Entity II quartet consolidation,"
    "gg_belgium,Federal SS Communities Regions,"
    "FPB 13320 + prior dual Entity II ticks 483-486,2026-06-01,2026,2029,4900000000,"
    '"{""e1_control_gap_2029"":4900000000,""e1_prior_package_2029"":9200000000,'
    '""e2_quartet_2026_class"":2654000000,""vl"":1832000000,""wal"":270000000,'
    '""bru"":297000000,""fwb_medium"":255000000,'
    '""note"":""different metrics years; E1 residual is control-account after decided path; not sum TE""}",'
    "0,active,https://www.plan.be/sites/default/files/documents/REP_BUDGET2027_13320_FR.pdf,"
    "Map dual federal vs subnational consolidation pressure,"
    "Publish comparable HRF control accounts all entities,"
    "src_dual_e1_e2_gap_tick487,strong,BE>dual>E1_residual_vs_E2_quartet,tick487"
)
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt1 + "\n")
    f.write(cmt2 + "\n")

lbs = [
    "lb_fpb_measures_inventory_263,FPB 263 policy options inventory budget 2027,federal,programme,Federal>budget2027>options_menu,0,4900000000,Strong public inventory; OPTIONS not adopted euros; 39 quantified DC impulses not additive; dual residual gap,strong,src_fpb_budget2027_measures_xlsx,Policymakers taxpayers,Menu for Entity I consolidation,Not waste — reform menu opacity if ignored,3.0,9.0,4,5.4,Track adoption L5,seed,,tick487",
    "lb_entity1_control_gap_4_9bn,Entity I control-account residual gap 4.9bn 2029,federal,ops,Entity_I>control_account>gap_2029,4900000000,4900000000,Strong FPB citing CM Mar 2026 0.67pct GDP pre-Iran; dual prior 9.2bn package separate,strong,src_fpb_budget2027_measures_report,Public finances EU path,Close net-exp control account,Material residual dual E2,4.0,9.5,6,6.5,Adopt measure package 2027,seed,,tick487",
    "lb_entity1_ss_147bn,Entity I SS expenditure 147.3bn 2026,federal,ops,Entity_I>SS>total,147300000000,147300000000,Strong FPB/BOSA BI2026; pens 72.3 health 41.3 invalid 15.9; core social,strong,src_fpb_budget2027_measures_report,SS beneficiaries,Social insurance Entity I,Core not pure waste; dual reform options,2.5,10.0,7,5.8,Publish unit costs,seed,,tick487",
    "lb_entity1_transfers_cr_81_5bn,Entity I LSF transfers C&R 81.5bn 2026,federal,transfer,Entity_I>LSF>transfers,81500000000,81500000000,Strong FPB BI2026 12.3pct GDP; dual Entity II receive side,strong,src_fpb_budget2027_measures_report,Communities Regions,LSF financing,Institutional transfer dual,2.5,9.5,6,5.6,LSF reform long-term FOI optional,seed,,tick487",
    "lb_dc_cars_cheques_4_5_5_5bn,DC2024 company cars+cheques niche cut range 4.5-5.5bn,federal,taxex,Federal>taxex>cars_cheques_options,4500000000,5500000000,Strong FPB report DC2024 range; OPTIONS not adopted; dual prior TE maps,strong,src_fpb_budget2027_measures_report,Company-car cheque beneficiaries,Fiscal niche reform menu,High-impact option dual waste map,6.0,9.0,6,7.0,If adopted open L5 outturn,seed,,tick487",
    "lb_dc_globalisation_5_5_11_3bn,DC2024 income globalisation impulse range 5.5-11.3bn,federal,taxex,Federal>tax>globalisation_options,5500000000,11300000000,Strong FPB report DC range; OPTIONS not adopted; dual PIT reform,strong,src_fpb_budget2027_measures_report,Capital income earners,PIT base broadening menu,Large option class,5.0,9.0,7,6.6,If adopted publish design,seed,,tick487",
    "lb_dual_e1_e2_pressure_map,Dual E1 residual 4.9bn + E2 quartet 2.65bn pressure map,multi,programme,BE>dual>E1_E2_pressure,4900000000,7554000000,Strong dual different metrics; E1 residual control gap + E2 2026 measures class,strong,src_dual_e1_e2_gap_tick487,All public entities,Consolidation pressure map Belgium,Method dual Entity map,3.5,9.5,5,6.2,Comparable ledgers FOI,seed,,tick487",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lbs:
        f.write(r + "\n")

print("CSV writes OK")

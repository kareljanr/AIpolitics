# tick548 — exposé Part I Tables 29-32+34 Entity I no-policy / measures / SPB / debt 2026-29
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T08:45:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_e1_path_2026_29,Kamer expose 2026 Entity I Tables29-32 path no-policy measures SPB,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part I Tables29-32,2026-07-31,primary_budget,"
        "Strong tick548: no-policy financing -26.2/-39.1bn 2026-29; after measures -24.6/-31.2; measures impact +1.6/+8.0; "
        "primary after -12.5/-13.4; SPB -12.9/-12.5bn (-1.9 to -1.7pct GDP); interest 12.2 to 17.8; GDP 662-725bn; tick548\n"
    )
    f.write(
        "src_kamer_expose_e1_debt_table34_2026,Kamer expose 2026 Entity I debt ratio Table34 2026-29,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part I Table34,2026-07-31,primary_budget,"
        "Strong tick548: E1 debt ratio 85.6/87.1/88.8/90.3pct GDP 2026-29; delta +1.9/+1.5/+1.7/+1.5; endogenous 1.3-1.6; exogenous 0.7 to -0.1; tick548\n"
    )
    f.write(
        "src_dual_e1_spb_mtfsp_tick548,Dual Entity I SPB expose vs GG MTFSP SPB path,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis Table32 + MTFSP,2026-07-31,synthesis,"
        "Strong dual: E1 SPB stuck ~-1.9 to -1.7pct 2026-29 while MTFSP GG SPB path to +0.6 2029; Entity I not delivering plan alone; tick548\n"
    )

# EUR: table values in billion → *1e9
buds = [
    # Table 29 no-policy financing path (bn)
    "bud_e1_nopol_financing_2026,sec_federal,2026,-26200000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy financing saldo -26.2bn 2026; tick548",
    "bud_e1_nopol_financing_2027,sec_federal,2027,-29400000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy financing -29.4bn 2027; tick548",
    "bud_e1_nopol_financing_2028,sec_federal,2028,-31800000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy financing -31.8bn 2028; tick548",
    "bud_e1_nopol_financing_2029,sec_federal,2029,-39100000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy financing -39.1bn 2029; tick548",
    "bud_e1_nopol_primary_2026,sec_federal,2026,-14000000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy primary saldo -14.0bn 2026; tick548",
    "bud_e1_nopol_primary_2029,sec_federal,2029,-20800000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy primary -20.8bn 2029; tick548",
    "bud_e1_nopol_primary_exp_2026,sec_federal,2026,215100000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy primary exp 215.1bn 2026; tick548",
    "bud_e1_nopol_primary_exp_2029,sec_federal,2029,235700000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy primary exp 235.7bn 2029; tick548",
    "bud_e1_nopol_ss_benefits_2026,sec_ss,2026,135600000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy SS benefits 135.6bn 2026; tick548",
    "bud_e1_nopol_ss_benefits_2029,sec_ss,2029,151100000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy SS benefits 151.1bn 2029; tick548",
    "bud_e1_nopol_interest_2026,sec_federal,2026,12200000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy interest 12.2bn 2026; tick548",
    "bud_e1_nopol_interest_2029,sec_federal,2029,18300000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table29 no-policy interest 18.3bn 2029; tick548",
    # Table 30 measures impact (positive = improves saldo)
    "bud_e1_measures_impact_fin_2026,sec_federal,2026,1600000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 measures impact financing +1.6bn 2026; tick548",
    "bud_e1_measures_impact_fin_2027,sec_federal,2027,2400000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 measures impact financing +2.4bn 2027; tick548",
    "bud_e1_measures_impact_fin_2028,sec_federal,2028,3000000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 measures impact financing +3.0bn 2028; tick548",
    "bud_e1_measures_impact_fin_2029,sec_federal,2029,8000000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 measures impact financing +8.0bn 2029; tick548",
    "bud_e1_measures_impact_primary_2026,sec_federal,2026,1600000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 measures impact primary +1.6bn 2026; tick548",
    "bud_e1_measures_impact_primary_2029,sec_federal,2029,7500000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 measures impact primary +7.5bn 2029; tick548",
    "bud_e1_measures_unalloc_2026,sec_federal,2026,500000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 onverdeeld measures +0.5bn 2026; tick548",
    "bud_e1_measures_unalloc_2029,sec_federal,2029,1500000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 onverdeeld measures +1.5bn 2029; dual CM path; tick548",
    "bud_e1_measures_ss_benefits_save_2029,sec_ss,2029,2500000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table30 measures reduce SS benefits path +2.5bn saldo effect 2029; tick548",
    "bud_e1_measures_budget_ion_2026,sec_federal,2026,-900000000,,,budgeted,src_kamer_expose_e1_path_2026_29,medium,Table30 measures on budget+ION primary -0.9bn 2026 (sign: primary exp line); tick548",
    # Table 31 after measures
    "bud_e1_post_financing_2026,sec_federal,2026,-24600000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures financing -24.6bn 2026 (-3.7pct GDP); tick548",
    "bud_e1_post_financing_2027,sec_federal,2027,-26900000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures financing -26.9bn 2027; tick548",
    "bud_e1_post_financing_2028,sec_federal,2028,-28800000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures financing -28.8bn 2028; tick548",
    "bud_e1_post_financing_2029,sec_federal,2029,-31200000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures financing -31.2bn 2029 (-4.3pct GDP); tick548",
    "bud_e1_post_primary_2026,sec_federal,2026,-12500000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures primary -12.5bn 2026 (-1.9pct); tick548",
    "bud_e1_post_primary_2027,sec_federal,2027,-13000000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures primary -13.0bn 2027; tick548",
    "bud_e1_post_primary_2028,sec_federal,2028,-13000000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures primary -13.0bn 2028; tick548",
    "bud_e1_post_primary_2029,sec_federal,2029,-13400000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 after measures primary -13.4bn 2029 (-1.8pct); tick548",
    "bud_e1_post_interest_2026,sec_federal,2026,12200000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 interest 12.2bn 2026; tick548",
    "bud_e1_post_interest_2027,sec_federal,2027,13900000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 interest 13.9bn 2027; tick548",
    "bud_e1_post_interest_2028,sec_federal,2028,15700000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 interest 15.7bn 2028; tick548",
    "bud_e1_post_interest_2029,sec_federal,2029,17800000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 interest 17.8bn 2029 (+5.6 vs 2026); tick548",
    "bud_e1_post_rec_2026,sec_federal,2026,202000000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 receipts 202.0bn 2026; tick548",
    "bud_e1_post_rec_2029,sec_federal,2029,216900000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 receipts 216.9bn 2029; tick548",
    "bud_e1_post_ss_benefits_2026,sec_ss,2026,135500000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 SS benefits 135.5bn 2026 after measures; tick548",
    "bud_e1_post_ss_benefits_2029,sec_ss,2029,148600000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table31 SS benefits 148.6bn 2029 after measures; tick548",
    # Table 32 SPB
    "bud_e1_spb_2026,sec_federal,2026,-12900000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 structural primary saldo -12.9bn 2026 (-1.9pct GDP); tick548",
    "bud_e1_spb_2027,sec_federal,2027,-12800000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 SPB -12.8bn 2027 (-1.9pct); tick548",
    "bud_e1_spb_2028,sec_federal,2028,-12800000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 SPB -12.8bn 2028 (-1.8pct); tick548",
    "bud_e1_spb_2029,sec_federal,2029,-12500000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 SPB -12.5bn 2029 (-1.7pct); improve only +0.4bn vs 2026; tick548",
    "bud_e1_struct_saldo_2026,sec_federal,2026,-25100000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 structural saldo -25.1bn 2026 (-3.8pct); tick548",
    "bud_e1_struct_saldo_2029,sec_federal,2029,-30400000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 structural saldo -30.4bn 2029 (-4.2pct); tick548",
    "bud_e1_oneoff_2026,sec_federal,2026,600000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 one-off +0.6bn 2026; tick548",
    "bud_e1_oneoff_2029,sec_federal,2029,-800000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 one-off -0.8bn 2029 (fiscal reform class); tick548",
    "bud_e1_gdp_2026,gg_belgium,2026,662067000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 GDP 662.067bn 2026; tick548",
    "bud_e1_gdp_2027,gg_belgium,2027,682511000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 GDP 682.511bn 2027; tick548",
    "bud_e1_gdp_2028,gg_belgium,2028,702749000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 GDP 702.749bn 2028; tick548",
    "bud_e1_gdp_2029,gg_belgium,2029,724680000000,,,budgeted,src_kamer_expose_e1_path_2026_29,strong,Table32 GDP 724.680bn 2029; tick548",
    # Table 34 debt ratio - store as pct*100 in amount_eur is wrong; use notes and amount as ratio*1e9 of GDP approx or store ratio points
    # Prefer storing debt stock estimate = ratio * GDP when both known
    "bud_e1_debt_ratio_pct_2026,sec_federal,2026,856,,,budgeted,src_kamer_expose_e1_debt_table34_2026,strong,Table34 E1 debt ratio 85.6pct GDP 2026 (amount_eur=856 means 85.6pp scale*10); tick548",
    "bud_e1_debt_ratio_pct_2027,sec_federal,2027,871,,,budgeted,src_kamer_expose_e1_debt_table34_2026,strong,Table34 E1 debt ratio 87.1pct GDP 2027; tick548",
    "bud_e1_debt_ratio_pct_2028,sec_federal,2028,888,,,budgeted,src_kamer_expose_e1_debt_table34_2026,strong,Table34 E1 debt ratio 88.8pct GDP 2028; tick548",
    "bud_e1_debt_ratio_pct_2029,sec_federal,2029,903,,,budgeted,src_kamer_expose_e1_debt_table34_2026,strong,Table34 E1 debt ratio 90.3pct GDP 2029; tick548",
    "bud_e1_debt_stock_est_2026,sec_federal,2026,566729000000,,,derived,src_kamer_expose_e1_debt_table34_2026,medium,Derived 85.6pct*662.067bn ~566.7bn E1 debt stock 2026; tick548",
    "bud_e1_debt_stock_est_2029,sec_federal,2029,654386000000,,,derived,src_kamer_expose_e1_debt_table34_2026,medium,Derived 90.3pct*724.680bn ~654.4bn E1 debt stock 2029; tick548",
    # Dual wedge no-policy vs after measures 2029
    "bud_e1_nopol_vs_post_wedge_2029,sec_federal,2029,7900000000,,,derived,src_kamer_expose_e1_path_2026_29,strong,Dual no-policy financing -39.1 vs post -31.2 = measures wedge 7.9bn ~Table30 +8.0; tick548",
    "bud_dual_e1_spb_vs_mtfsp_2029,gg_belgium,2029,-12500000000,,,derived,src_dual_e1_spb_mtfsp_tick548,strong,Dual E1 SPB -12.5bn/-1.7pct vs MTFSP GG SPB target +0.6pct 2029; tick548",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_e1_nopol_vs_measures_2026_29,Entity I no-policy vs after-measures financing path 2026-29,sec_federal,Taxpayers bondholders,"
        "Expose Tables 29-31 Part I,2026-01-28,2026,2029,0,"
        '"{""nopol_fin_bn"":[-26.2,-29.4,-31.8,-39.1],""post_fin_bn"":[-24.6,-26.9,-28.8,-31.2],'
        '""measures_impact_bn"":[1.6,2.4,3.0,8.0],""post_primary_bn"":[-12.5,-13.0,-13.0,-13.4],'
        '""post_interest_bn"":[12.2,13.9,15.7,17.8],""nopol_fin_pct"":[-4.0,-4.3,-4.5,-5.4],'
        '""post_fin_pct"":[-3.7,-3.9,-4.1,-4.3],""note"":""Strong; interest snowball dominates; measures insufficient to reverse deficit path""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Honest Entity I fiscal trajectory,"
        "Delivery FOI measures,src_kamer_expose_e1_path_2026_29,strong,Entity_I>path>nopol_vs_measures,tick548"
    ),
    (
        "cmt_e1_spb_path_2026_29,Entity I structural primary balance path Table32 2026-29,sec_federal,EU surveillance taxpayers,"
        "Expose Table32 SPB after cycle one-off transfer corrections,2026-01-28,2026,2029,-12500000000,"
        '"{""spb_bn"":[-12.9,-12.8,-12.8,-12.5],""spb_pct"":[-1.9,-1.9,-1.8,-1.7],""struct_saldo_bn"":[-25.1,-26.7,-28.5,-30.4],'
        '""interest_bn"":[12.2,13.9,15.7,17.8],""gdp_bn"":[662.1,682.5,702.7,724.7],""improve_29v26_bn"":0.4,'
        '""note"":""Strong; SPB barely improves while financing saldo worsens on interest""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,SPB honesty vs MTFSP,"
        "Publish outturn SPB FOI,src_kamer_expose_e1_path_2026_29,strong,Entity_I>SPB>2026_29,tick548"
    ),
    (
        "cmt_e1_debt_ratio_path_2026_29,Entity I debt ratio path Table34 2026-29,sec_federal,Bondholders,"
        "Expose Table34 debt ratio endogenous exogenous,2026-01-28,2026,2029,0,"
        '"{""ratio_pct"":[85.6,87.1,88.8,90.3],""delta_pp"":[1.9,1.5,1.7,1.5],""endog_pp"":[1.3,1.4,1.6,1.6],'
        '""exog_pp"":[0.7,0.1,0.1,-0.1],""debt_stock_est_2026_bn"":566.7,""debt_stock_est_2029_bn"":654.4,'
        '""note"":""Strong ratio; stock derived medium from GDP*ratio""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Entity I debt snowball map,"
        "Exogenous FOI,src_kamer_expose_e1_debt_table34_2026,strong,Entity_I>debt>ratio_2026_29,tick548"
    ),
    (
        "cmt_dual_e1_spb_mtfsp_gap,Dual E1 SPB stuck vs MTFSP GG +0.6pct 2029,gg_belgium,Multi-level taxpayers,"
        "Table32 E1 SPB + prior MTFSP mapping,2026-01-28,2026,2029,0,"
        '"{""e1_spb_2029_pct"":-1.7,""mtfsp_gg_spb_2029_pct"":0.6,""gap_pp"":2.3,'
        '""note"":""not additive TE; dual shows Entity I alone not on plan path""}",'
        "0,active,docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,Honest dual fiscal plan gap,"
        "Entity II effort FOI,src_dual_e1_spb_mtfsp_tick548,strong,BE>dual>E1_SPB_vs_MTFSP,tick548"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_e1_nopol_financing_39bn,E1 no-policy financing -39.1bn 2029,federal,ops,Entity_I>nopol>financing_2029,39100000000,39100000000,Strong Table29 counterfactual; vs post -31.2 measures wedge ~8bn,strong,src_kamer_expose_e1_path_2026_29,Taxpayers,Baseline without measures,Interest+SS path,7.0,9.5,5,7.85,Deliver measures FOI,seed,,tick548",
    "lb_e1_post_financing_31bn,E1 after-measures financing -31.2bn 2029,federal,ops,Entity_I>post>financing_2029,31200000000,31200000000,Strong Table31; -4.3pct GDP; still worsening YoY,strong,src_kamer_expose_e1_path_2026_29,Bondholders,Official path,Interest snowball,6.5,9.5,5,7.65,Cut path FOI,seed,,tick548",
    "lb_e1_spb_12_5bn,E1 structural primary -12.5bn 2029,federal,ops,Entity_I>SPB>2029,12500000000,12500000000,Strong Table32 -1.7pct GDP; only +0.4bn improve vs 2026,strong,src_kamer_expose_e1_path_2026_29,EU surveillance,SPB honesty,Far from MTFSP +0.6 GG,7.0,9.0,5,7.70,SPB delivery FOI,seed,,tick548",
    "lb_e1_interest_17_8bn,E1 interest 17.8bn 2029,federal,ops,Entity_I>interest>2029,17800000000,17800000000,Strong Table31 path 12.2 to 17.8; snowball core,strong,src_kamer_expose_e1_path_2026_29,Debt service,Interest expense,Crowds primary,5.0,9.0,4,6.80,Debt path FOI,seed,,tick548",
    "lb_e1_measures_impact_8bn,E1 measures financing impact +8.0bn 2029,federal,ops,Entity_I>measures>impact_2029,8000000000,8000000000,Strong Table30; unalloc +1.5 of package; delivery residual,strong,src_kamer_expose_e1_path_2026_29,Admin,Consolidation package,Soft measures risk,6.5,8.5,6,7.25,Outturn FOI,seed,,tick548",
    "lb_e1_debt_ratio_90_3,E1 debt ratio 90.3pct GDP 2029,federal,ops,Entity_I>debt>ratio_2029,903,903,Strong Table34 path 85.6 to 90.3; endogenous 1.6pp/yr class,strong,src_kamer_expose_e1_debt_table34_2026,Bondholders,Debt ratio Entity I,Not GG 107+ class,5.5,8.5,4,6.55,Stock FOI,seed,,tick548",
    "lb_dual_e1_spb_mtfsp_gap,Dual E1 SPB -1.7 vs MTFSP GG +0.6 2029,multi,ops,BE>dual>SPB_E1_vs_MTFSP,0,0,Strong dual plan gap ~2.3pp; Entity I not plan vehicle alone,strong,src_dual_e1_spb_mtfsp_tick548,Multi-level,Fiscal architecture,Honesty north star,7.5,7.0,5,7.15,Entity II FOI,seed,,tick548",
    "lb_e1_nopol_vs_post_wedge_8bn,Dual no-policy vs post wedge ~8bn 2029,federal,ops,Entity_I>dual>nopol_post_wedge,7900000000,7900000000,Strong dual Tables29-31; measures value-at-stake,strong,src_kamer_expose_e1_path_2026_29,Reform path,Policy delta,Delivery critical,6.0,8.5,5,7.00,KPI FOI,seed,,tick548",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

foi = (
    f"gap_e1_measures_delivery_l5,Entity_I>measures>delivery_L5_2026_29,sec_federal,"
    "Cash-by-year outturn vs Table30/31 measures package 2026-2029; L5 split unallocated (onverdeeld) measures; "
    "SPB one-off series methodology; Table34 exogenous debt factors detail; mid-year Monitoring Committee updates,"
    "Path aggregates strong; delivery risk and soft unallocated measures opacity material for ~8bn 2029 wedge,"
    "7,FOD BOSA / Monitoringcomité / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_e1_measures_delivery_l5.md,ready,2026-07-31,,,,"
    "cmt_e1_nopol_vs_measures_2026_29|cmt_e1_spb_path_2026_29,"
    "lb_e1_measures_impact_8bn|lb_e1_spb_12_5bn,"
    f"{now},{now},tick548: Tables29-32+34 filled; residual delivery L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_539,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T08:40:00Z,,Spawned tick547 after E1 invest Table40; next Part I residual tables or new PDF; rq_116 deferred; progress@550 in 3 ticks"
)
new = (
    "rq_539,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T08:40:00Z,2026-07-31T08:45:00Z,tick548: E1 Tables29-32+34 nopol/measures/SPB/debt; spawn rq_540; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_539 row not found")
text = text.replace(old, new)
if "rq_540," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_540,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-31T08:45:00Z,,Spawned tick548 after E1 SPB/debt path; next public residual; rq_116 deferred; progress@550 in 2 ticks\n"
    )
rq_path.write_text(text, encoding="utf-8")

print("tick548 write OK: budgets", len(buds), "cmt", len(cmts), "lb", len(lbs))

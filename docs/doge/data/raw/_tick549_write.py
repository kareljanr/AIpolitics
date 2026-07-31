# tick549 — exposé Part I sensitivity Tables35-36 + SPB one-offs L5 + consol multi-year 2027-29
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T08:50:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_e1_sensitivity_2026,Kamer expose 2026 Entity I sensitivity Tables35-36 interest+GDP,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part I §7,2026-07-31,primary_budget,"
        "Strong tick549: +100bp rates interest cost 0.93/1.49/2.20/2.79bn 2026-29; -0.5pp GDP growth financing hit -1.4/-2.9/-4.6/-6.4bn; "
        "saldo after growth shock -26.0 to -37.5bn; tick549\n"
    )
    f.write(
        "src_kamer_expose_e1_spb_oneoffs_2025_26,Kamer expose 2026 Entity I SPB one-offs L5 + Table7 2025-26,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part I §3 Table7,2026-07-31,primary_budget,"
        "Strong tick549: SPB -11.056bn 2025 re-est / -11.601bn 2026 (-1.7/-1.8pct); cycle -1014/-1303m; Belfius div +500m both years; "
        "BVH -221; BFW -279/+234; textile -92; tax-free -159 2026; transfer corr -115/-140; tick549\n"
    )
    f.write(
        "src_kamer_expose_consol_multiyear_2027_29,Kamer expose 2026 consol orgs ESA saldo multi-year Tables37-39,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part I §8,2026-07-31,primary_budget,"
        "Strong tick549: ESA saldo +1097.7/+1209.4/+980.7m 2027-29; FPIM +610/622/650; Hedera +381/449/465; ASEVA +86/86/81; "
        "Infrabel -119/-121/-96; BIO +5.4/30.5/34.4; debt impact +1223/1327/1205m; dual 2026 consol +1392m; tick549\n"
    )

buds = [
    # Sensitivity interest +100bp
    "bud_e1_rate_shock_interest_2026,sec_federal,2026,930000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 +100bp from Sep2025 interest cost +0.93bn 2026 (0.14pct GDP); tick549",
    "bud_e1_rate_shock_interest_2027,sec_federal,2027,1490000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 rate shock interest +1.49bn 2027 (0.22pct); tick549",
    "bud_e1_rate_shock_interest_2028,sec_federal,2028,2200000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 rate shock interest +2.20bn 2028 (0.31pct); tick549",
    "bud_e1_rate_shock_interest_2029,sec_federal,2029,2790000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 rate shock interest +2.79bn 2029 (0.39pct); tick549",
    "bud_e1_rate_shock_lt_2026,sec_federal,2026,370000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 LT debt interest impact 0.37bn 2026; tick549",
    "bud_e1_rate_shock_st_2026,sec_federal,2026,550000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 ST debt interest impact 0.55bn 2026; tick549",
    "bud_e1_rate_shock_lt_2029,sec_federal,2029,2110000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 LT debt interest impact 2.11bn 2029; tick549",
    "bud_e1_rate_shock_st_2029,sec_federal,2029,680000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table35 ST debt interest impact 0.68bn 2029; tick549",
    # GDP growth -0.5pp
    "bud_e1_growth_shock_impact_2026,sec_federal,2026,-1400000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table36 -0.5pp growth each year from 2025: financing impact -1.4bn 2026; tick549",
    "bud_e1_growth_shock_impact_2027,sec_federal,2027,-2900000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table36 growth shock financing -2.9bn 2027; tick549",
    "bud_e1_growth_shock_impact_2028,sec_federal,2028,-4600000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table36 growth shock financing -4.6bn 2028; tick549",
    "bud_e1_growth_shock_impact_2029,sec_federal,2029,-6400000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table36 growth shock financing -6.4bn 2029 (0.9pct GDP); tick549",
    "bud_e1_financing_after_growth_shock_2026,sec_federal,2026,-26000000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table36 financing after growth shock -26.0bn 2026; tick549",
    "bud_e1_financing_after_growth_shock_2029,sec_federal,2029,-37500000000,,,budgeted,src_kamer_expose_e1_sensitivity_2026,strong,Table36 financing after growth shock -37.5bn 2029; tick549",
    # SPB one-offs L5 + Table7
    "bud_e1_spb_2025_reest,sec_federal,2025,-11056000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Table7 SPB re-est -11.056bn 2025 (-1.7pct GDP); tick549",
    "bud_e1_spb_2026_initial_t7,sec_federal,2026,-11601000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Table7 SPB initial -11.601bn 2026 (-1.8pct); dual Table32 -12.9bn multi-year path class; tick549",
    "bud_e1_spb_delta_2026_vs_2025,sec_federal,2026,-545000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Table7 SPB worsens -545m 2026 vs 2025 re-est; tick549",
    "bud_e1_financing_2025_reest,sec_federal,2025,-23046000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Table7 financing re-est -23.046bn 2025; tick549",
    "bud_e1_financing_2026_t7,sec_federal,2026,-24637000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Table7 financing initial -24.637bn 2026 dual Table31 -24.6; tick549",
    "bud_e1_struct_saldo_2025,sec_federal,2025,-21826000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Table7 structural saldo -21.826bn 2025; tick549",
    "bud_e1_struct_saldo_2026_t7,sec_federal,2026,-23769000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Table7 structural saldo -23.769bn 2026; tick549",
    "bud_e1_cycle_corr_2025,sec_federal,2025,-1014000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Cycle corr Entity I -1014m 2025 (OG -0.4pct); tick549",
    "bud_e1_cycle_corr_2026,sec_federal,2026,-1303000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Cycle corr Entity I -1303m 2026 (OG -0.5pct); tick549",
    "bud_e1_oneoff_bvh_2025,fod_finance,2025,-221000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,One-off bedrijfsvoorheffing reform -221m 2025; tick549",
    "bud_e1_oneoff_bfw_2025,sec_federal,2025,-279000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,One-off BFW settlements -279m 2025; tick549",
    "bud_e1_oneoff_bfw_2026,sec_federal,2026,234000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,One-off BFW settlements +234m 2026; tick549",
    "bud_e1_oneoff_textile_cn_2025,fod_finance,2025,-92000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,One-off Chinese textile late interest -92m 2025; tick549",
    "bud_e1_oneoff_belfius_div_2025,sec_federal,2025,500000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,One-off Belfius dividend +500m 2025; tick549",
    "bud_e1_oneoff_belfius_div_2026,sec_federal,2026,500000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,One-off Belfius dividend +500m 2026; tick549",
    "bud_e1_oneoff_taxfree_2026,fod_finance,2026,-159000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,One-off fiscal reform tax-free sum -159m 2026; tick549",
    "bud_e1_transfer_corr_2025,sec_federal,2025,-115000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Transfer correction HRF -115m 2025 (-0.02pct GDP); tick549",
    "bud_e1_transfer_corr_2026,sec_federal,2026,-140000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Transfer correction HRF -140m 2026; tick549",
    "bud_e1_primary_deficit_2026_exact,sec_federal,2026,-12469000000,,,budgeted,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Text primary deficit Entity I 12469m 2026 dual Table31 -12.5bn; tick549",
    # Consol multi-year
    "bud_consol_esa_saldo_2027,sec_federal,2027,1097700000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 consol ESA saldo +1097.7m 2027; tick549",
    "bud_consol_esa_saldo_2028,sec_federal,2028,1209400000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 consol ESA saldo +1209.4m 2028; tick549",
    "bud_consol_esa_saldo_2029,sec_federal,2029,980700000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 consol ESA saldo +980.7m 2029; tick549",
    "bud_consol_primary_esa_2027,sec_federal,2027,1166200000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 consol primary ESA +1166.2m 2027; tick549",
    "bud_consol_primary_esa_2029,sec_federal,2029,1054900000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 consol primary ESA +1054.9m 2029; tick549",
    "bud_consol_debt_impact_2027,sec_federal,2027,1222900000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table39 consol debt impact +1222.9m 2027; tick549",
    "bud_consol_debt_impact_2028,sec_federal,2028,1327200000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table39 consol debt impact +1327.2m 2028; tick549",
    "bud_consol_debt_impact_2029,sec_federal,2029,1204700000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table39 consol debt impact +1204.7m 2029; tick549",
    "bud_fpim_saldo_2027,sec_federal,2027,610300000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 FPIM ESA saldo +610.3m 2027; tick549",
    "bud_fpim_saldo_2028,sec_federal,2028,622200000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 FPIM +622.2m 2028; tick549",
    "bud_fpim_saldo_2029,sec_federal,2029,649700000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 FPIM +649.7m 2029; tick549",
    "bud_hedera_saldo_2027,sec_federal,2027,381000000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Hedera +381.0m 2027; tick549",
    "bud_hedera_saldo_2028,sec_federal,2028,449100000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Hedera +449.1m 2028; tick549",
    "bud_hedera_saldo_2029,sec_federal,2029,464900000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Hedera +464.9m 2029; tick549",
    "bud_aseva_saldo_2027,sec_federal,2027,85800000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 ASEVA/Apetra +85.8m 2027; tick549",
    "bud_aseva_saldo_2029,sec_federal,2029,81400000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 ASEVA +81.4m 2029; tick549",
    "bud_infrabel_saldo_2027,infrabel,2027,-119400000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Infrabel+SPV -119.4m 2027; tick549",
    "bud_infrabel_saldo_2028,infrabel,2028,-121200000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Infrabel+SPV -121.2m 2028; tick549",
    "bud_infrabel_saldo_2029,infrabel,2029,-95600000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Infrabel+SPV -95.6m 2029; tick549",
    "bud_bio_saldo_2027,sec_federal,2027,5400000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 BIO development finance +5.4m 2027; tick549",
    "bud_bio_saldo_2028,sec_federal,2028,30500000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 BIO +30.5m 2028; tick549",
    "bud_bio_saldo_2029,sec_federal,2029,34400000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 BIO +34.4m 2029; tick549",
    "bud_bipt_saldo_2027,bipt,2027,25000000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 BIPT +25.0m 2027; tick549",
    "bud_dexia_holding_saldo_2027,sec_federal,2027,-4900000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Dexia Holding -4.9m 2027; tick549",
    "bud_dexia_holding_saldo_2029,sec_federal,2029,4000000,,,budgeted,src_kamer_expose_consol_multiyear_2027_29,strong,Table38 Dexia Holding +4.0m 2029; tick549",
    "bud_dual_spb_t7_vs_t32_2026,sec_federal,2026,1299000000,,,derived,src_kamer_expose_e1_spb_oneoffs_2025_26,medium,Dual Table7 SPB -11.601 vs Table32 -12.9 = ~1.3bn path method residual; tick549",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_e1_sensitivity_rates_growth_2026_29,Entity I sensitivity +100bp rates and -0.5pp growth 2026-29,sec_federal,Debt Agency taxpayers,"
        "Expose Tables35-36 Debt Agency + EC elasticity 0.61,2026-01-28,2026,2029,2790000000,"
        '"{""rate_shock_bn"":[0.93,1.49,2.20,2.79],""rate_pct_gdp"":[0.14,0.22,0.31,0.39],'
        '""growth_shock_bn"":[-1.4,-2.9,-4.6,-6.4],""fin_after_growth_bn"":[-26.0,-29.8,-33.3,-37.5],'
        '""e1_share_growth"":0.674,""elasticity"":0.61,""note"":""Strong; snowball+cycle risk map""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Macro risk to Entity I path,"
        "Publish annual re-run FOI,src_kamer_expose_e1_sensitivity_2026,strong,Entity_I>sensitivity>rates_growth,tick549"
    ),
    (
        "cmt_e1_spb_oneoffs_l5_2025_26,Entity I SPB one-offs L5 package 2025-2026,sec_federal,ESA compilers Belfius,"
        "Expose Part I §3 one-off list + Table7,2026-01-28,2025,2026,-11601000000,"
        '"{""spb_2025_bn"":-11.056,""spb_2026_bn"":-11.601,""spb_pct"":[-1.7,-1.8],""cycle_m"":[-1014,-1303],'
        '""belfius_m"":500,""bvh_2025_m"":-221,""bfw_m"":[-279,234],""textile_m"":-92,""taxfree_2026_m"":-159,'
        '""transfer_corr_m"":[-115,-140],""note"":""Strong L5 one-offs; dual Table32 multi-year SPB residual""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,SPB honesty one-off map,"
        "Method FOI,src_kamer_expose_e1_spb_oneoffs_2025_26,strong,Entity_I>SPB>oneoffs_L5,tick549"
    ),
    (
        "cmt_consol_esa_multiyear_2027_29,Consol institutions ESA saldo multi-year path 2027-29,sec_federal,FPIM Hedera Infrabel ASEVA,"
        "Expose Tables37-39 multi-year consol,2026-01-28,2027,2029,1097700000,"
        '"{""esa_m"":[1097.7,1209.4,980.7],""primary_esa_m"":[1166.2,1284.9,1054.9],""debt_impact_m"":[1222.9,1327.2,1204.7],'
        '""fpim_m"":[610.3,622.2,649.7],""hedera_m"":[381.0,449.1,464.9],""infrabel_m"":[-119.4,-121.2,-95.6],'
        '""aseva_m"":[85.8,86.2,81.4],""bio_m"":[5.4,30.5,34.4],""note"":""Strong dual improves Entity I; FPIM+Hedera dominate""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Off-budget ESA buffer map,"
        "L5 FOI residual,src_kamer_expose_consol_multiyear_2027_29,strong,Federal>consol>ESA_2027_29,tick549"
    ),
    (
        "cmt_dual_spb_table7_table32,Dual SPB Table7 vs Table32 2026 method residual,sec_federal,ESA,"
        "Expose Table7 initial vs Table32 multi-year path,2026-01-28,2026,2026,0,"
        '"{""t7_spb_bn"":-11.601,""t32_spb_bn"":-12.9,""wedge_bn"":1.3,'
        '""note"":""not invent; document dual rows both strong primary""}",'
        "0,active,docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,Reconcile SPB presentations,"
        "Method FOI,src_kamer_expose_e1_spb_oneoffs_2025_26,medium,Entity_I>dual>SPB_T7_T32,tick549"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_e1_rate_shock_2_79bn,E1 +100bp interest cost 2.79bn 2029,federal,ops,Entity_I>sensitivity>rate_shock_2029,2790000000,2790000000,Strong Table35 Debt Agency; path 0.93 to 2.79; snowball risk,strong,src_kamer_expose_e1_sensitivity_2026,Bondholders,Rate risk,Material vs measures,6.5,8.0,4,6.90,Hedge FOI,seed,,tick549",
    "lb_e1_growth_shock_6_4bn,E1 -0.5pp growth financing hit 6.4bn 2029,federal,ops,Entity_I>sensitivity>growth_shock_2029,6400000000,6400000000,Strong Table36; saldo to -37.5bn; elasticity 0.61 E1 share 67.4pct,strong,src_kamer_expose_e1_sensitivity_2026,Taxpayers,Growth risk,Dominates soft measures,7.0,8.5,4,7.30,Buffer FOI,seed,,tick549",
    "lb_e1_spb_11_6bn_2026,E1 SPB -11.6bn 2026 Table7,federal,ops,Entity_I>SPB>2026_T7,11601000000,11601000000,Strong Table7 -1.8pct; dual Table32 -12.9 multi-year,strong,src_kamer_expose_e1_spb_oneoffs_2025_26,EU surveillance,SPB snapshot,Honesty dual,6.5,9.0,5,7.45,Method FOI,seed,,tick549",
    "lb_belfius_div_500m,Belfius dividend one-off 500m 2025-26,federal,ops,Entity_I>oneoff>Belfius_div,500000000,500000000,Strong SPB one-off both years; not structural revenue,strong,src_kamer_expose_e1_spb_oneoffs_2025_26,SOE path,One-off receipt,Masks SPB,6.0,7.0,3,6.00,Structural FOI,seed,,tick549",
    "lb_fpim_saldo_650m,FPIM consol ESA saldo 650m 2029,federal,ops,Federal>consol>FPIM_2029,649700000,649700000,Strong multi-year path 610-650; dominates consol surplus,strong,src_kamer_expose_consol_multiyear_2027_29,Holdings,SOE portfolio,Off-budget buffer,4.0,7.5,4,5.85,Portfolio FOI,seed,,tick549",
    "lb_hedera_saldo_465m,Hedera consol ESA saldo 465m 2029,federal,ops,Federal>consol>Hedera_2029,464900000,464900000,Strong path 381-465; dual energy class,strong,src_kamer_expose_consol_multiyear_2027_29,Energy perimeter,Holding vehicle,Dual consol,4.5,7.0,4,5.85,L5 FOI,seed,,tick549",
    "lb_infrabel_saldo_minus_96m,Infrabel+SPV ESA -96m 2029,federal,ops,Federal>consol>Infrabel_2029,95600000,95600000,Strong deficit path -119 to -96; dual rail invest,strong,src_kamer_expose_consol_multiyear_2027_29,Rail,Infra SOE,Dual NMBS stack,5.0,6.5,4,5.75,Rail FOI,seed,,tick549",
    "lb_consol_esa_1_1bn,Consol ESA saldo ~1.1bn 2027-28 path,federal,ops,Federal>consol>ESA_total,1097700000,1209400000,Strong +1.10/+1.21/+0.98bn 2027-29 improves E1; debt impact ~1.2-1.3bn,strong,src_kamer_expose_consol_multiyear_2027_29,Entity I,Off-budget ESA,Perimeter dual,4.0,8.0,4,6.00,Perimeter FOI,seed,,tick549",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

foi = (
    f"gap_e1_sensitivity_oneoff_method,Entity_I>SPB>sensitivity_oneoff_method,sec_federal,"
    "Full methodology note for SPB one-offs vs EC practice; Belfius dividend multi-year policy; "
    "Debt Agency rate-shock model assumptions; Table7 vs Table32 SPB reconciliation; consol L5 for FPIM/Hedera cash vs ESA,"
    "Path aggregates strong; method dual SPB presentations and one-off sustainability opacity,"
    "6,FOD BOSA / Agentschap van de Schuld / FPB / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_e1_sensitivity_oneoff_method.md,ready,2026-07-31,,,,"
    "cmt_e1_sensitivity_rates_growth_2026_29|cmt_e1_spb_oneoffs_l5_2025_26|cmt_dual_spb_table7_table32,"
    "lb_e1_growth_shock_6_4bn|lb_e1_spb_11_6bn_2026|lb_belfius_div_500m,"
    f"{now},{now},tick549 filled; residual method human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_540,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T08:45:00Z,,Spawned tick548 after E1 SPB/debt path; next public residual; rq_116 deferred; progress@550 in 2 ticks"
)
new = (
    "rq_540,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T08:45:00Z,2026-07-31T08:50:00Z,tick549: E1 sensitivity+SPB one-offs+consol multi-year; spawn rq_541; progress@550 next"
)
if old not in text:
    raise SystemExit("rq_540 not found")
text = text.replace(old, new)
if "rq_541," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_541,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-31T08:50:00Z,,Spawned tick549; **progress@550 on next tick**; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

print("tick549 OK", len(buds), "buds")

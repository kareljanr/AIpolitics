# tick552 — exposé Table4 fiscal measures L5 2026 + non-fiscal receipts dual
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T09:05:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_tax_measures_t4_2026,Kamer expose 2026 Table4 complementary fiscal measures L5,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part II Table4,2026-07-31,primary_budget,"
        "Strong tick552: Table4 measures total +1584.7m 2026 (VAT pure +511.2 excise +57.1 divers +1148); "
        "securities tax +414 capital gains +236 interest ded abolish +203.5 UI tax cut end +257 tax-free -531; "
        "meal vouchers -75.5 hotels 158 sports 253 takeaway 222 bank 150 VVPR 90; Dec package +1384.8; tick552\n"
    )
    f.write(
        "src_kamer_expose_nonfiscal_2026,Kamer expose 2026 non-fiscal receipts Table13 dual,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part II Afdeling2,2026-07-31,primary_budget,"
        "Strong tick552: non-fiscal corrected saldo-level 6971/5850m 2025-26; Middelen 6519/6470; Finance 4228/5126; "
        "SS 1190 to 2; sleeping assets +475; Fluxys +100; F35 hedge +321; RRF BOSA +143; passage -620 2026; tick552\n"
    )

buds = [
    # Table 4 totals
    "bud_tax_measures_total_2026,fod_finance,2026,1584700000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 complementary fiscal measures total +1584.7m 2026; tick552",
    "bud_tax_measures_vat_pure_2026,fod_finance,2026,511200000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 measures pure VAT +511.2m 2026; tick552",
    "bud_tax_measures_excise_2026,fod_finance,2026,57100000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 measures excise +57.1m 2026; tick552",
    "bud_tax_measures_divers_2026,fod_finance,2026,1148000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 measures divers +1148.0m 2026; tick552",
    "bud_tax_measures_bvh_2026,fod_finance,2026,-382900000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4/5 BVH measures impact -382.9m 2026; tick552",
    "bud_tax_measures_dec_conclave_2026,fod_finance,2026,1384800000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 Dec2025 conclave package +1384.8m 2026; tick552",
    "bud_tax_measures_summer_2026,fod_finance,2026,-138500000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 summer agreement net -138.5m 2026; tick552",
    "bud_tax_measures_feb_gvt_2026,fod_finance,2026,255600000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 Feb2025 GVT package +255.6m 2026; tick552",
    # Major L5 revenue raisers
    "bud_tact_securities_tax_2026,fod_finance,2026,414000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 annual securities account tax +414m 2026; dual CoA TACT; tick552",
    "bud_capital_gains_tax_2026,fod_finance,2026,236000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 capital gains tax +236m 2026; tick552",
    "bud_interest_ded_abolish_2026,fod_finance,2026,203450000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 abolish ordinary interest deduction +203.45m 2026; tick552",
    "bud_ui_tax_relief_end_2026,fod_finance,2026,257390000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 end UI benefit tax reduction +257.39m 2026; tick552",
    "bud_vat_hotels_camping_2026,fod_finance,2026,158000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VAT hotels/camping +158m 2026; tick552",
    "bud_vat_sport_leisure_2026,fod_finance,2026,253000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VAT sport/leisure facilities +253m 2026; tick552",
    "bud_vat_takeaway_nonalc_2026,fod_finance,2026,222000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VAT takeaway+non-alc drinks +222m 2026; tick552",
    "bud_bank_tax_2026,fod_finance,2026,150000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 bank tax +150m 2026; tick552",
    "bud_vvpr_liquidation_18pct_2026,fod_finance,2026,90000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VVPR/liquidation 18pct vs 15 +90m 2026; tick552",
    "bud_excise_gas_2026,fod_finance,2026,91000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 natural gas accise (EU dir anticipate) +91m 2026; tick552",
    "bud_excise_heatoil_up_2026,fod_finance,2026,19000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 heating oil accise +19m 2026; tick552",
    "bud_vat_pesticides_21pct_2026,fod_finance,2026,53000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VAT pesticides 12to21 +53m 2026; tick552",
    "bud_vat_boiler_21pct_2026,fod_finance,2026,57500000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VAT fuel boilers 21pct +57.5m 2026; tick552",
    "bud_insurance_tax_up_2026,fod_finance,2026,51000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 insurance tax 9.6 vs 9.25 +51m 2026; tick552",
    "bud_dbi_rdt_2026,fod_finance,2026,39600000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 DBI/RDT measure +39.6m 2026; tick552",
    "bud_embarkation_tax_2026,fod_finance,2026,25300000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 embarkation tax +25.3m 2026; tick552",
    "bud_marriage_quotient_phaseout_2026,fod_finance,2026,79310000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 marriage quotient phaseout non-retirees 66.3 + retirees 13.0 = 79.3m 2026; tick552",
    "bud_pension_relief_phaseout_high_2026,fod_finance,2026,33950000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 high-pension tax relief phaseout +33.95m 2026; tick552",
    # Major revenue costs (negative)
    "bud_taxfree_sum_cost_2026,fod_finance,2026,-530990000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 tax-free sum (quotité) -530.99m 2026; tick552",
    "bud_author_rights_it_cost_2026,fod_finance,2026,-142130000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 author rights IT sector -142.13m 2026; tick552",
    "bud_meal_voucher_face_up_2026,fod_finance,2026,-75500000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 meal vouchers 8to10 EUR face -75.5m 2026; tick552",
    "bud_vat_demo_rebuild_reduced_2026,fod_finance,2026,-124000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VAT demolition/rebuild reduced rate -124m 2026; tick552",
    "bud_excise_elec_residential_cut_2026,fod_finance,2026,-50000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 residential electricity accise cut -50m 2026; tick552",
    "bud_vat_heatpumps_reduced_2026,fod_finance,2026,-10100000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 VAT heat pumps reduced -10.1m 2026; tick552",
    "bud_overtime_tax_2026,fod_finance,2026,-26000000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 overtime measure net -26m 2026; tick552",
    "bud_consumption_transition_2026,fod_finance,2026,-105500000,,,budgeted,src_kamer_expose_tax_measures_t4_2026,strong,Table4 consumption transition measures -105.5m 2026; tick552",
    # Non-fiscal
    "bud_nonfiscal_corrected_2025,sec_federal,2025,6971000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Non-fiscal means after passage corr impact saldo 6971m 2025; tick552",
    "bud_nonfiscal_corrected_2026,sec_federal,2026,5850000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Non-fiscal means after passage 5850m 2026 (-1121m YoY); tick552",
    "bud_nonfiscal_receipts_2025,sec_federal,2025,6539000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 non-fiscal receipts before passage 6539m 2025; tick552",
    "bud_nonfiscal_receipts_2026,sec_federal,2026,6491000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 non-fiscal receipts 6491m 2026; tick552",
    "bud_nonfiscal_middelen_2025,sec_federal,2025,6519000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 non-fiscal Middelen 6519m 2025; tick552",
    "bud_nonfiscal_middelen_2026,sec_federal,2026,6470000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 non-fiscal Middelen 6470m 2026; tick552",
    "bud_nonfiscal_finance_2025,fod_finance,2025,4228000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 Finance non-fiscal 4228m 2025; tick552",
    "bud_nonfiscal_finance_2026,fod_finance,2026,5126000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 Finance non-fiscal 5126m 2026 (+898m); tick552",
    "bud_nonfiscal_ss_2025,sec_ss,2025,1190000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 SS non-fiscal 1190m 2025; tick552",
    "bud_nonfiscal_ss_2026,sec_ss,2026,2000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 SS non-fiscal 2m 2026 (-1188m dual); tick552",
    "bud_nonfiscal_bosa_2026,sec_federal,2026,447000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 BOSA non-fiscal 447m 2026 (RRF +143 class); tick552",
    "bud_nonfiscal_interior_2026,sec_federal,2026,198000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Table13 Interior non-fiscal 198m 2026 (AMIF/ISF); tick552",
    "bud_sleeping_assets_2026,fod_finance,2026,475000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Sleeping assets regulation +475m 2026 Finance art 56.50.01; tick552",
    "bud_fluxys_energy_norm_2026,sec_federal,2026,100000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Fluxys energy-norm contribution +100m 2026; tick552",
    "bud_f35_hedge_receipt_2026,mod_defensie,2026,321000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,F35/drones payment hedge receipt +321m 2026 debt agency; tick552",
    "bud_nonfiscal_passage_corr_2026,sec_federal,2026,-620000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Non-fiscal passage corrections -620m 2026 (code8 -1116 + others); tick552",
    "bud_nonfiscal_guarantee_fund_corr_2026,sec_federal,2026,248000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Guarantee fund financial institutions corr +248m 2026 (vs +790 2025); tick552",
    "bud_nonfiscal_pension_transfer_corr_2026,sec_federal,2026,375000000,,,budgeted,src_kamer_expose_nonfiscal_2026,strong,Firm pension-obligation transfer to State corr +375m 2026; tick552",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_tax_measures_l5_package_2026,Fiscal measures complementary impact L5 package 2026 Table4,fod_finance,Taxpayers firms workers,"
        "Expose Part II Table4 multi-conclave stack,2026-01-28,2026,2026,1584700000,"
        '"{""total_m"":1584.7,""vat_pure_m"":511.2,""excise_m"":57.1,""divers_m"":1148.0,""bvh_m"":-382.9,'
        '""tact_m"":414,""cgt_m"":236,""interest_ded_m"":203.5,""ui_tax_end_m"":257.4,""taxfree_m"":-531,'
        '""vat_hospitality_sport_takeaway_m"":633,""bank_m"":150,""dec_package_m"":1384.8,""summer_net_m"":-138.5,'
        '""note"":""Strong L5; DRM class dual EC DBP; delivery residual""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map 2026 tax reform cash impacts,"
        "Outturn FOI,src_kamer_expose_tax_measures_t4_2026,strong,Federal>Tax>measures_L5_2026,tick552"
    ),
    (
        "cmt_nonfiscal_dual_2025_26,Non-fiscal receipts dual Table13 2025-2026,sec_federal,SOE energy Finance SS,"
        "Expose Part II Afdeling2 non-fiscal,2026-01-28,2025,2026,5850000000,"
        '"{""corrected_2025_m"":6971,""corrected_2026_m"":5850,""receipts_2026_m"":6491,""finance_2026_m"":5126,'
        '""ss_drop_m"":-1188,""sleeping_m"":475,""fluxys_m"":100,""f35_hedge_m"":321,""passage_2026_m"":-620,'
        '""note"":""Strong dual; SS non-fiscal collapse + Finance capital receipts rise""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Non-tax revenue map,"
        "Article L5 FOI,src_kamer_expose_nonfiscal_2026,strong,Federal>Nonfiscal>2025_26,tick552"
    ),
    (
        "cmt_tact_cgt_bank_tax_2026,TACT securities + CGT + bank tax stack 2026,fod_finance,Wealth financial sector,"
        "Table4 Dec+summer packages,2026-01-28,2026,2026,800000000,"
        '"{""tact_m"":414,""cgt_m"":236,""bank_m"":150,""sum_m"":800,""note"":""Strong primary Table4; dual prior CoA TACT path""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Wealth/finance tax DRM,"
        "Yield FOI,src_kamer_expose_tax_measures_t4_2026,strong,Federal>Tax>wealth_finance_2026,tick552"
    ),
    (
        "cmt_vat_hospitality_stack_2026,VAT hospitality sport takeaway stack 2026,fod_finance,Hospitality leisure,"
        "Table4 Dec conclave consumption VAT,2026-01-28,2026,2026,633000000,"
        '"{""hotels_m"":158,""sport_m"":253,""takeaway_m"":222,""sum_m"":633,""transition_m"":-105.5,'
        '""note"":""Strong; rate increase path class""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,VAT consumption DRM,"
        "Sector FOI,src_kamer_expose_tax_measures_t4_2026,strong,Federal>Tax>VAT_hospitality_2026,tick552"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_tax_measures_1_58bn,Fiscal measures package +1.58bn 2026,federal,tax_expenditure,Federal>Tax>measures_package_2026,1584700000,1584700000,Strong Table4 net DRM; not pure waste — revenue path,strong,src_kamer_expose_tax_measures_t4_2026,Taxpayers,Consolidation DRM,Delivery residual,5.0,8.0,5,6.50,Outturn FOI,seed,,tick552",
    "lb_tact_414m_2026,Securities account tax TACT +414m 2026,federal,tax_expenditure,Federal>Tax>TACT_2026,414000000,414000000,Strong Table4; dual CoA declining due path prior,strong,src_kamer_expose_tax_measures_t4_2026,Wealth accounts,TACT yield,Base erosion risk,6.0,7.5,4,6.45,KPI FOI,seed,,tick552",
    "lb_cgt_236m_2026,Capital gains tax +236m 2026,federal,tax_expenditure,Federal>Tax>CGT_2026,236000000,236000000,Strong Table4 summer agreement,strong,src_kamer_expose_tax_measures_t4_2026,Investors,CGT,Design residual,5.5,7.5,5,6.40,Design FOI,seed,,tick552",
    "lb_taxfree_sum_531m_cost,Tax-free sum cost -531m 2026,federal,tax_expenditure,Federal>Tax>taxfree_sum_2026,530990000,530990000,Strong Table4 largest negative measure; dual SPB one-off class,strong,src_kamer_expose_tax_measures_t4_2026,Households,Quotité exemptée,Reform cost,5.0,7.5,4,6.15,Phase FOI,seed,,tick552",
    "lb_vat_hospitality_633m,VAT hospitality/sport/takeaway +633m 2026,federal,tax_expenditure,Federal>Tax>VAT_hospitality_2026,633000000,633000000,Strong hotels 158 sport 253 takeaway 222,strong,src_kamer_expose_tax_measures_t4_2026,Hospitality,Rate DRM,Sector incidence,5.5,8.0,4,6.55,Incidence FOI,seed,,tick552",
    "lb_ui_tax_relief_end_257m,End UI tax relief +257m 2026,federal,tax_expenditure,Federal>Tax>UI_relief_end_2026,257390000,257390000,Strong dual UI time-limit reform stack,strong,src_kamer_expose_tax_measures_t4_2026,Unemployed,Tax treatment UI,Spillover leefloon,6.5,7.5,5,6.75,Net fiscal FOI,seed,,tick552",
    "lb_nonfiscal_5_85bn,Non-fiscal corrected means 5.85bn 2026,federal,ops,Federal>Nonfiscal>corrected_2026,5850000000,5850000000,Strong -1.12bn YoY; Finance 5.13 SS collapse; not pure waste,strong,src_kamer_expose_nonfiscal_2026,SOE energy,Non-tax revenue,One-off heavy,4.0,9.0,4,6.40,Article FOI,seed,,tick552",
    "lb_sleeping_assets_475m,Sleeping assets receipts +475m 2026,federal,ops,Federal>Nonfiscal>sleeping_assets,475000000,475000000,Strong Finance art; one-off class regulation change,strong,src_kamer_expose_nonfiscal_2026,Dormant securities,One-off cash,Not structural,6.0,7.5,3,6.30,Recur FOI,seed,,tick552",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

foi = (
    f"gap_tax_measures_outturn_l5,Federal>Tax>measures_Table4>outturn_L5,fod_finance,"
    "Cash outturn vs Table4 complementary measures 2026 by line (TACT CGT bank VAT hospitality UI tax-free); "
    "mid-year Monitoring Committee yield vs plan; non-fiscal article outturn sleeping assets Fluxys F35 hedge,"
    "Budget L5 strong; delivery/yield residual material for 1.58bn DRM package,"
    "7,FOD Financiën / FOD BOSA / Monitoringcomité / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_tax_measures_outturn_l5.md,ready,2026-07-31,,,,"
    "cmt_tax_measures_l5_package_2026|cmt_tact_cgt_bank_tax_2026,"
    "lb_tax_measures_1_58bn|lb_tact_414m_2026,"
    f"{now},{now},tick552: Table4+nonfiscal filled; residual outturn human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq = root / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = "rq_543,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:00:00Z,,Spawned tick551 after fiscal receipts; next residual (Table4 tax measures L5 / non-fiscal / new PDF); rq_116 deferred"
new = "rq_543,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:00:00Z,2026-07-31T09:05:00Z,tick552: Table4 tax measures 1.58bn + nonfiscal dual; spawn rq_544; rq_116 deferred"
if old not in text:
    raise SystemExit("rq_543 not found")
text = text.replace(old, new)
if "rq_544," not in text:
    text = text.rstrip("\n") + "\n"
    text += "rq_544,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:05:00Z,,Spawned tick552 after tax measures+nonfiscal; next residual (new CoA PDF / residual dual); rq_116 deferred\n"
rq.write_text(text, encoding="utf-8")
print("tick552 OK", len(buds))

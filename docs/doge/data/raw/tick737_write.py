# tick737 — SWL Rapport d'activités 2024 residual dual VMSW/SLRB/SWCS (rq_728)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T05:45:00Z"
URL_RA = "https://www.swl.be/images/2025/RA2024-okVF-valideCR.pdf"
URL_BNB = "https://www.swl.be/images/2025/BNB_Comptes_annuels_SWL_31_12_2024.pdf"
URL_PAGE = "https://www.swl.be/brochures-et-publications-4.html"

SRC = "src_swl_ra2024_residual"
SRC_BNB = "src_swl_bnb_2024"
SRC_DUAL = "src_dual_swl_vmsw_slrb_swcs_tick737"

# --- entity note ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)
for e in ents:
    if e.get("entity_id") == "swl":
        e["notes"] = (
            "Type3 UAP; RA2024 residual tick737: 103293 dwellings / 213431 housed; "
            "SLSP works markets 364.3m; BS assets 3.509bn debt 2.742bn; "
            "reno plan envelope 1.1675bn; dual VMSW/SLRB/SWCS; Agency Habitation pending"
        )
with open(ent_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=efields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for e in ents:
        w.writerow({k: e.get(k, "") for k in efields})
print("entity swl notes updated")

# --- budgets ---
budgets = [
    # Stock / ops residual
    ("bud_swl_dwellings_103293_2024", "swl", 2024, 103293, "", "", "outturn", SRC, "strong", "Public utility dwellings managed by 62 SLSP COUNT 103293 eoy2024; tick737"),
    ("bud_swl_social_dwellings_98990_2024", "swl", 2024, 98990, "", "", "outturn", SRC, "strong", "Social dwellings 98990 of 103293 stock; tick737"),
    ("bud_swl_moyen_dwellings_1901_2024", "swl", 2024, 1901, "", "", "outturn", SRC, "strong", "Moyen dwellings 1901; tick737"),
    ("bud_swl_loyer_equilibre_1993_2024", "swl", 2024, 1993, "", "", "outturn", SRC, "strong", "Loyer d equilibre dwellings 1993; tick737"),
    ("bud_swl_persons_housed_213431_2024", "swl", 2024, 213431, "", "", "outturn", SRC, "strong", "Persons housed 213431 COUNT 2024; tick737"),
    ("bud_swl_mean_rent_352_2024", "swl", 2024, 352, "", "", "outturn", SRC, "strong", "Mean social rent 352 EUR/month 2024; tick737"),
    ("bud_swl_rotation_6_69pct_2024", "swl", 2024, 669, "", "", "outturn", SRC, "strong", "Turnover/rotation rate 6.69pct 2024; tick737"),
    ("bud_swl_precarious_income_77pct_2024", "swl", 2024, 77, "", "", "outturn", SRC, "strong", "Tenants with precarious income 77pct 2024; tick737"),
    ("bud_swl_waitlist_49945_2024", "swl", 2024, 49945, "", "", "outturn", SRC, "strong", "Candidate-tenant waitlist 49945 eoy2024; tick737"),
    ("bud_swl_mean_taxable_income_23497_2024", "swl", 2024, 23497, "", "", "outturn", SRC, "strong", "Mean taxable income tenant households 23497 EUR 2024; tick737"),
    ("bud_swl_staff_208_2024", "swl", 2024, 208, "", "", "outturn", SRC, "strong", "SWL collaborateurs COUNT 208 2024; tick737"),
    ("bud_swl_slsp_count_62_2024", "swl", 2024, 62, "", "", "outturn", SRC, "strong", "SLSP COUNT 62 under SWL tutelle 2024; tick737"),
    ("bud_swl_referents_sociaux_96_2024", "swl", 2024, 96, "", "", "outturn", SRC, "strong", "Referents sociaux COUNT 96 2024; tick737"),
    ("bud_swl_households_accompanied_9789_2024", "swl", 2024, 9789, "", "", "outturn", SRC, "strong", "Households accompanied 9789 (1157 intensive) 2024; tick737"),
    # Works / investment residual
    ("bud_swl_slsp_works_markets_364_3m_2024", "swl", 2024, 364300000, "", "", "outturn", SRC, "strong", "SLSP works markets awarded 364.3m 2024 (+34m / +10pct vs 2023); tick737"),
    ("bud_swl_works_creation_67_8m_2024", "swl", 2024, 67800000, "", "", "outturn", SRC, "strong", "Creation+equipment works 67.8m (19pct of markets) 2024; tick737"),
    ("bud_swl_works_reno_296m_2024", "swl", 2024, 296000000, "", "", "outturn", SRC, "strong", "Renovation works 296m incl frame+demolition (81pct) 2024 (+45m / +18pct); tick737"),
    ("bud_swl_slsp_construction_finance_81_994m_2024", "swl", 2024, 81993740.92, "", "", "outturn", SRC, "strong", "SLSP financed new construction 81.994m (subs+SWL advances+own) 2024; tick737"),
    ("bud_swl_new_starts_261_2024", "swl", 2024, 261, "", "", "outturn", SRC, "strong", "New dwellings started 261 (247 newbuild + 14 acq-rehab) 2024; tick737"),
    ("bud_swl_new_receptions_339_2024", "swl", 2024, 339, "", "", "outturn", SRC, "strong", "New dwellings receptioned 339 (+107 / +46pct) 2024; tick737"),
    ("bud_swl_sales_rental_119_units_15_117m_2024", "swl", 2024, 15116521.95, "", "", "outturn", SRC, "strong", "SLSP sold 119 rental units 15.117m avg 127030 2024; tick737"),
    ("bud_swl_sales_acquisitive_11_units_1_654m_2024", "swl", 2024, 1653823.71, "", "", "outturn", SRC, "strong", "SLSP sold 11 acquisitive units 1.654m avg 150348 2024; tick737"),
    ("bud_swl_reno_starts_5994_2024", "swl", 2024, 5994, "", "", "outturn", SRC, "strong", "Renovation starts COUNT 5994 dwellings 2024; tick737"),
    ("bud_swl_reno_receptions_8553_2024", "swl", 2024, 8553, "", "", "outturn", SRC, "strong", "Renovated dwellings receptioned 8553 2024; tick737"),
    ("bud_swl_pivert2_starts_71_2_910m_2024", "swl", 2024, 2910265, "", "", "outturn", SRC, "strong", "PIVERT2 starts 71 dwellings 2.910m 2024; tick737"),
    ("bud_swl_own_advances_reno_45_848m_2024", "swl", 2024, 45848431, "", "", "outturn", SRC, "strong", "Own funds/SWL advances reno 2795 dwellings 45.848m 2024; tick737"),
    ("bud_swl_plan_reno_invest_231_122m_2024", "swl", 2024, 231122246, "", "", "outturn", SRC, "strong", "Plan renovation 2020-25 investments 231.122m / 3128 starts 2024 (cumul 279.881m class); tick737"),
    ("bud_swl_plan_reno_envelope_1_1675bn", "swl", 2024, 1167500000, "", "", "budgeted", SRC, "strong", "Plan renovation 2020-25 subsidy envelope 1.1675bn (grant 875.625m + zero loan 291.875m); tick737"),
    ("bud_swl_plan_reno_grant_875_625m", "swl", 2024, 875625000, "", "", "budgeted", SRC, "strong", "Plan renovation grant component 875.625m of 1.1675bn envelope; tick737"),
    ("bud_swl_plan_reno_zero_loan_291_875m", "swl", 2024, 291875000, "", "", "budgeted", SRC, "strong", "Plan renovation zero-rate loan component 291.875m; tick737"),
    ("bud_swl_embellissement_23_8m", "swl", 2024, 23800000, "", "", "budgeted", SRC, "strong", "Plan embellissement 2020-23 subsidy 23.8m (38519 units; closed 2024; 187 receptions); tick737"),
    ("bud_swl_hpe_subsidy_137_195m", "swl", 2024, 137195000, "", "", "budgeted", SRC, "strong", "HPE programme subsidy 137.195m for 805 new dwellings (597 in study); tick737"),
    ("bud_swl_repowereu_dwellings_3918", "swl", 2024, 3918, "", "", "budgeted", SRC, "strong", "REPowerEU target dwellings 3918 (3535 PV + 383 PV+PAC); tick737"),
    ("bud_swl_social_ref_subs_4_381m_2024", "swl", 2024, 4381198.50, "", "", "outturn", SRC, "strong", "Social referents accompaniment subsidy 4.381m 2024; tick737"),
    ("bud_swl_reno_accompany_7_5m_2024", "swl", 2024, 7500000, "", "", "outturn", SRC, "strong", "Renovation plan accompaniment 7.5m (from 2023 two tranches); tick737"),
    ("bud_swl_cclp_213444_2024", "swl", 2024, 213444, "", "", "outturn", SRC, "strong", "CCLP financing 213444 EUR 2024 (edito residual); tick737"),
    ("bud_swl_awcclp_24000_2024", "swl", 2024, 24000, "", "", "outturn", SRC, "strong", "AWCCLP convention-cadre 24000 EUR 2024; tick737"),
    ("bud_swl_proportionate_housing_46pct_2024", "swl", 2024, 46, "", "", "outturn", SRC, "strong", "Only 46pct tenant households in size-proportionate dwelling 2024; tick737"),
    ("bud_swl_inactive_tenants_80pct_2024", "swl", 2024, 80, "", "", "outturn", SRC, "strong", "Inactive tenant heads 80pct (36pct retired class) 2024; tick737"),
    # BNB balance sheet residual
    ("bud_swl_assets_3_509bn_2024", "swl", 2024, 3509322270.22, "", "", "outturn", SRC_BNB, "strong", "BNB BS total assets eoy2024 3.509bn (was 3.643); tick737"),
    ("bud_swl_equity_663_044m_2024", "swl", 2024, 663043973.5, "", "", "outturn", SRC_BNB, "strong", "BNB equity 663.044m eoy2024; tick737"),
    ("bud_swl_debt_total_2_742bn_2024", "swl", 2024, 2742490276.86, "", "", "outturn", SRC_BNB, "strong", "BNB total debts 2.742bn eoy2024 (was 2.871); tick737"),
    ("bud_swl_lt_financial_debt_1_518bn_2024", "swl", 2024, 1518372004.77, "", "", "outturn", SRC_BNB, "strong", "BNB LT financial debt 1.518bn (bonds 426m banks 897.4m other 195.0m); tick737"),
    ("bud_swl_bonds_426m_2024", "swl", 2024, 426000000, "", "", "outturn", SRC_BNB, "strong", "BNB bond debt 426m eoy2024 (was 361m); tick737"),
    ("bud_swl_bank_debt_897_382m_2024", "swl", 2024, 897382125.02, "", "", "outturn", SRC_BNB, "strong", "BNB credit-institution LT debt 897.382m eoy2024; tick737"),
    ("bud_swl_cash_510_577m_2024", "swl", 2024, 510577224.46, "", "", "outturn", SRC_BNB, "strong", "BNB cash 510.577m eoy2024 (was 594.749); tick737"),
    ("bud_swl_provisions_103_788m_2024", "swl", 2024, 103788019.86, "", "", "outturn", SRC_BNB, "strong", "BNB provisions risks/charges 103.788m eoy2024; tick737"),
    ("bud_swl_ca_8_251m_2024", "swl", 2024, 8251097.35, "", "", "outturn", SRC_BNB, "strong", "BNB chiffre d affaires 8.251m 2024; tick737"),
    ("bud_swl_remuneration_20_874m_2024", "swl", 2024, 20874370.66, "", "", "outturn", SRC_BNB, "strong", "BNB remuneration charges 20.874m 2024; tick737"),
    ("bud_swl_fin_charges_57_078m_2024", "swl", 2024, 57078147.5, "", "", "outturn", SRC_BNB, "strong", "BNB financial charges 57.078m (debt charges 57.002m) 2024; tick737"),
    ("bud_swl_net_profit_0_506m_2024", "swl", 2024, 506224.65, "", "", "outturn", SRC_BNB, "strong", "BNB net profit 0.506m 2024 (was loss -1.461m 2023); tick737"),
    ("bud_swl_fin_income_51_611m_2024", "swl", 2024, 51610610.37, "", "", "outturn", SRC_BNB, "strong", "BNB financial income 51.611m 2024; tick737"),
    # Dual residual
    ("bud_dual_swl_debt_2_742bn_vs_housing_2024", "gg_belgium", 2024, 2742490276.86, "", "", "outturn", SRC_DUAL, "strong", "SWL debt 2.742bn dual VMSW 3.12bn / SLRB 1.67bn / SWCS book 1.75bn; not TE-additive; tick737"),
    ("bud_dual_swl_works_364_3m_vs_slrb_vmsw", "gg_belgium", 2024, 364300000, "", "", "outturn", SRC_DUAL, "strong", "SWL SLSP works 364.3m dual SLRB liq 802.7 / VMSW financing class; tick737"),
    ("bud_dual_swl_waitlist_49945_housing_pressure", "gg_belgium", 2024, 49945, "", "", "outturn", SRC_DUAL, "strong", "WAL waitlist 49945 dual BCR/VL social housing demand residual; tick737"),
]

bud_path = DATA / "budgets.csv"
with open(bud_path, encoding="utf-8", newline="") as f:
    br = csv.DictReader(f)
    bfields = br.fieldnames
    existing = {r["budget_id"] for r in br}
added_b = 0
with open(bud_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bfields, lineterminator="\n")
    for row in budgets:
        if row[0] in existing:
            continue
        w.writerow({
            "budget_id": row[0], "entity_id": row[1], "year": row[2],
            "amount_eur": row[3], "amount_min_eur": row[4], "amount_max_eur": row[5],
            "basis": row[6], "source_id": row[7], "confidence": row[8], "notes": row[9],
        })
        added_b += 1
print(f"budgets +{added_b}")

# --- commitments ---
commitments = [
    {
        "commitment_id": "cmt_swl_slsp_works_364_3m_2024",
        "title": "SLSP works markets 364.3m 2024 (creation 67.8 + reno 296)",
        "entity_id": "swl",
        "beneficiary": "62 SLSP / ~103k public utility dwellings",
        "legal_basis": "SWL RA2024 programmes investissement residual",
        "decision_date": "2024-12-31",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "364300000",
        "cash_by_year": '{"works_m":364.3,"creation_m":67.8,"reno_m":296,"path_plus_m":34,"new_starts_n":261,"new_receptions_n":339,"reno_starts_n":5994,"reno_receptions_n":8553}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Create and renovate public utility housing stock",
        "cut_option": "Unit-cost per dwelling dual VMSW/SLRB FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWL>works_markets",
        "notes": "tick737",
    },
    {
        "commitment_id": "cmt_swl_plan_reno_1_1675bn",
        "title": "Plan renovation 2020-25 envelope 1.1675bn (grant 875.6 + zero loan 291.9)",
        "entity_id": "swl",
        "beneficiary": "Target 20000 dwellings label B",
        "legal_basis": "SWL RA2024 Plan de renovation 2020-2025",
        "decision_date": "2020-01-01",
        "start_year": "2020",
        "end_year": "2025",
        "total_envelope_eur": "1167500000",
        "cash_by_year": '{"envelope_m":1167.5,"grant_m":875.625,"zero_loan_m":291.875,"invest_2024_m":231.122,"starts_2024_n":3128,"receptions_2024_n":126,"cumul_class_m":279.881}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "20000 dwellings to PEB B + long-term carbon neutrality 2050",
        "cut_option": "Cash-by-year drawdown + inflation rebasings FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWL>plan_renovation",
        "notes": "tick737 remaining Unknown without full drawdown table",
    },
    {
        "commitment_id": "cmt_swl_hpe_137_195m",
        "title": "HPE programme subsidy 137.195m for 805 new dwellings",
        "entity_id": "swl",
        "beneficiary": "New high environmental performance public housing",
        "legal_basis": "SWL RA2024 programme HPE residual",
        "decision_date": "2024-12-31",
        "start_year": "2024",
        "end_year": "2029",
        "total_envelope_eur": "137195000",
        "cash_by_year": '{"subsidy_m":137.195,"dwellings_n":805,"in_study_n":597,"build_start":"2025"}',
        "remaining_eur": "137195000",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Q-Zen -20pct primary energy + DNSH",
        "cut_option": "Unit cost vs modular / key-ready FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWL>HPE",
        "notes": "tick737",
    },
    {
        "commitment_id": "cmt_swl_debt_2_742bn_2024",
        "title": "SWL balance-sheet debt 2.742bn eoy2024 (LT fin 1.518bn)",
        "entity_id": "swl",
        "beneficiary": "Region-guaranteed SWL financing of SLSP programmes",
        "legal_basis": "BNB comptes annuels SWL 31/12/2024",
        "decision_date": "2024-12-31",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "2742490276.86",
        "cash_by_year": '{"debt_total_m":2742.5,"lt_fin_m":1518.4,"bonds_m":426,"banks_m":897.4,"other_lt_m":195.0,"cash_m":510.6,"assets_m":3509.3,"equity_m":663.0,"fin_charges_m":57.078,"net_profit_m":0.506}',
        "remaining_eur": "2742490276.86",
        "status": "active",
        "evaluation_url": URL_BNB,
        "stated_goal": "Finance SLSP investment with Region guarantee",
        "cut_option": "Guarantee stock + interest path dual VMSW FOI",
        "source_id": SRC_BNB,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWL>debt",
        "notes": "tick737",
    },
    {
        "commitment_id": "cmt_swl_social_pole_4_381m_2024",
        "title": "Social pole referents 4.381m + reno accompany 7.5m 2024",
        "entity_id": "swl",
        "beneficiary": "9789 households accompanied / 96 referents / 33 ITS",
        "legal_basis": "SWL RA2024 pole social residual",
        "decision_date": "2024-12-31",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "11881198.50",
        "cash_by_year": '{"ref_subs_m":4.381,"reno_accompany_m":7.5,"referents_n":96,"its_n":33,"households_n":9789,"intensive_n":1157,"cclp_eur":213444,"awcclp_eur":24000}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Social accompaniment of public housing tenants",
        "cut_option": "Outcome metrics vs cost FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWL>pole_social",
        "notes": "tick737",
    },
    {
        "commitment_id": "cmt_dual_swl_vmsw_slrb_swcs_tick737",
        "title": "Dual SWL RA2024 residual vs VMSW/SLRB/SWCS housing finance",
        "entity_id": "gg_belgium",
        "beneficiary": "BE public housing dual map",
        "legal_basis": "SWL RA2024 + BNB + prior duals tick735-736",
        "decision_date": "2026-06-18",
        "start_year": "2024",
        "end_year": "2025",
        "total_envelope_eur": "2742490276.86",
        "cash_by_year": '{"swl_debt_m":2742,"swl_works_m":364.3,"swl_dwellings_n":103293,"swl_waitlist_n":49945,"vmsw_debt_m":3123,"slrb_debt_m":1672,"slrb_liq_m":802.7,"swcs_encours_m":1748.5,"note":"not TE-additive dual housing OIPs"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Comparable regional public housing finance",
        "cut_option": "Single dual unit-cost + waitlist dashboard FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>SWL_VMSW_SLRB_SWCS",
        "notes": "tick737",
    },
]

cmt_path = DATA / "commitments.csv"
with open(cmt_path, encoding="utf-8", newline="") as f:
    cr = csv.DictReader(f)
    cfields = cr.fieldnames
    cexist = {r["commitment_id"] for r in cr}
added_c = 0
with open(cmt_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cfields, lineterminator="\n")
    for row in commitments:
        if row["commitment_id"] in cexist:
            continue
        w.writerow(row)
        added_c += 1
print(f"commitments +{added_c}")

# --- leaderboard ---
leaderboard = [
    {
        "item_id": "lb_swl_debt_2_742bn_2024",
        "name": "SWL BS debt 2.742bn eoy2024 (LT fin 1.518bn bonds 426m)",
        "level": "L5",
        "type": "stock",
        "hierarchy_path": "Wallonie>SWL>debt",
        "annual_cost_eur": "2742490276.86",
        "total_cost_eur": "2742490276.86",
        "tco_notes": "Stock; annual fin charges 57.1m separate; dual VMSW 3.12bn SLRB 1.67bn",
        "confidence": "strong",
        "source_id": SRC_BNB,
        "beneficiaries": "62 SLSP / 103k dwellings finance stack",
        "stated_goal": "Region-guaranteed financing of public housing investment",
        "measured_outcome": "Debt -129m YoY; bonds +65m; net profit 0.5m",
        "absurdity_score": "6.0",
        "cost_score": "8.5",
        "difficulty": "4",
        "priority_index": "6.85",
        "cut_proposal": "Publish guarantee stock + unit interest cost FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick737 stock often filtered from pure annual top10",
    },
    {
        "item_id": "lb_swl_plan_reno_1_1675bn",
        "name": "Plan renovation 2020-25 envelope 1.1675bn (only 231m invest 2024)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Wallonie>SWL>plan_renovation",
        "annual_cost_eur": "231122246",
        "total_cost_eur": "1167500000",
        "tco_notes": "Multi-year envelope grant+zero loan; 2024 invest 231m / 3128 starts / 126 receptions",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Target 20000 dwellings PEB B",
        "stated_goal": "Energy renovation of worst public stock",
        "measured_outcome": "Receptions lag starts (126 vs 3128); inflation rebasings noted",
        "absurdity_score": "7.0",
        "cost_score": "8.0",
        "difficulty": "4",
        "priority_index": "7.10",
        "cut_proposal": "Delivery gap audit + unit cost PEB upgrade FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick737 high priority delivery lag residual",
    },
    {
        "item_id": "lb_swl_works_364_3m_2024",
        "name": "SLSP works markets 364.3m 2024 (+10pct) creation lag vs reno",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Wallonie>SWL>works_markets",
        "annual_cost_eur": "364300000",
        "total_cost_eur": "364300000",
        "tco_notes": "Creation 67.8m (19pct) vs reno 296m (81pct); 261 starts vs 49945 waitlist",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Public housing tenants and candidates",
        "stated_goal": "Maintain and grow public utility stock",
        "measured_outcome": "339 new receptions vs 49945 waitlist; stock 103293",
        "absurdity_score": "6.5",
        "cost_score": "7.5",
        "difficulty": "3",
        "priority_index": "6.80",
        "cut_proposal": "Rebalance create vs renovate with unit-cost FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick737",
    },
    {
        "item_id": "lb_swl_waitlist_49945_2024",
        "name": "Public housing waitlist 49945 candidates vs 339 new receptions 2024",
        "level": "L5",
        "type": "outcome_gap",
        "hierarchy_path": "Wallonie>SWL>waitlist",
        "annual_cost_eur": "49945",
        "total_cost_eur": "49945",
        "tco_notes": "COUNT gap not euro stock; dual BCR/VL demand residual",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Candidate tenants 47pct isolés / 66pct precarious class",
        "stated_goal": "Right to decent housing",
        "measured_outcome": "Waitlist ~50k; rotation 6.69pct; new supply 339",
        "absurdity_score": "7.5",
        "cost_score": "5.0",
        "difficulty": "5",
        "priority_index": "6.00",
        "cut_proposal": "Supply acceleration + vacant stock audit FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick737 outcome gap; amount_eur is COUNT",
    },
    {
        "item_id": "lb_swl_fin_charges_57_1m_2024",
        "name": "SWL financial charges 57.1m 2024 on 2.74bn debt book",
        "level": "L5",
        "type": "overhead",
        "hierarchy_path": "Wallonie>SWL>fin_charges",
        "annual_cost_eur": "57078147.5",
        "total_cost_eur": "57078147.5",
        "tco_notes": "BNB debt charges 57.002m of 57.078m fin charges",
        "confidence": "strong",
        "source_id": SRC_BNB,
        "beneficiaries": "Intermediated via SLSP investment finance",
        "stated_goal": "Service Region-guaranteed debt",
        "measured_outcome": "Fin income 51.6m; net profit only 0.5m",
        "absurdity_score": "5.5",
        "cost_score": "6.5",
        "difficulty": "3",
        "priority_index": "5.90",
        "cut_proposal": "Interest rate path + guarantee fee transparency FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick737",
    },
    {
        "item_id": "lb_swl_proportionate_only_46pct",
        "name": "Only 46pct tenant households in size-proportionate dwelling 2024",
        "level": "L5",
        "type": "outcome_gap",
        "hierarchy_path": "Wallonie>SWL>allocation",
        "annual_cost_eur": "103293",
        "total_cost_eur": "103293",
        "tco_notes": "Stock allocation mismatch; 34pct under-occupy 19pct over-occupy class",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "213431 persons housed",
        "stated_goal": "Allocate housing to household size",
        "measured_outcome": "46pct proportionate only",
        "absurdity_score": "6.5",
        "cost_score": "5.5",
        "difficulty": "4",
        "priority_index": "5.85",
        "cut_proposal": "Mutation reform + under-occupy incentives FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick737",
    },
    {
        "item_id": "lb_dual_swl_vmsw_slrb_swcs_asymmetry",
        "name": "Dual SWL 2.74bn debt / 364m works vs VMSW 3.12bn / SLRB 1.67bn / SWCS 1.75bn",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>SWL_VMSW_SLRB_SWCS",
        "annual_cost_eur": "2742490276.86",
        "total_cost_eur": "2742490276.86",
        "tco_notes": "Not TE-additive; Agency Habitation merge pending SWL+SWCS+FLW+SPW TLPE",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE public housing dual map",
        "stated_goal": "Comparable regional housing finance",
        "measured_outcome": "Four OIPs separate books; unit-cost dual FOI",
        "absurdity_score": "7.0",
        "cost_score": "8.0",
        "difficulty": "4",
        "priority_index": "7.10",
        "cut_proposal": "Open dual dashboard unit-cost + waitlist + NPL",
        "status": "active",
        "struck_reason": "",
        "notes": "tick737",
    },
]

lb_path = DATA / "leaderboard.csv"
with open(lb_path, encoding="utf-8", newline="") as f:
    lr = csv.DictReader(f)
    lfields = lr.fieldnames
    lexist = {r["item_id"] for r in lr}
added_l = 0
with open(lb_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lfields, lineterminator="\n")
    for row in leaderboard:
        if row["item_id"] in lexist:
            continue
        w.writerow(row)
        added_l += 1
print(f"leaderboard +{added_l}")

# --- sources ---
sources = [
    {
        "source_id": SRC,
        "title": "SWL Rapport d'activités 2024 residual dual VMSW/SLRB/SWCS",
        "url": URL_RA,
        "publisher": "Société wallonne du Logement (SWL)",
        "accessed_date": "2026-08-02",
        "source_class": "official_annual_report",
        "notes": (
            "Strong tick737: 103293 dwellings 213431 housed waitlist 49945 mean rent 352; "
            "SLSP works 364.3m (creation 67.8 reno 296); plan reno envelope 1.1675bn invest 231.1; "
            "HPE 137.2; social ref 4.381; publications page " + URL_PAGE + "; raw swl_ra2024.pdf"
        ),
    },
    {
        "source_id": SRC_BNB,
        "title": "BNB comptes annuels SWL 31/12/2024 residual balance sheet",
        "url": URL_BNB,
        "publisher": "SWL / Banque Nationale de Belgique Centrale des bilans",
        "accessed_date": "2026-08-02",
        "source_class": "official_accounts",
        "notes": (
            "Strong tick737: assets 3.509bn debt 2.742bn LT fin 1.518bn bonds 426 cash 510.6; "
            "CA 8.251 rem 20.874 fin charges 57.078 net profit 0.506; raw swl_bnb_2024.pdf"
        ),
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual SWL RA2024 residual vs VMSW/SLRB/SWCS housing tick737",
        "url": URL_RA,
        "publisher": "DOGE synthesis SWL + prior duals",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": (
            "Strong dual not TE-additive: SWL debt 2.742 works 364.3 dwellings 103k waitlist 50k "
            "vs VMSW debt 3.123 SLRB debt 1.672 liq 802.7 SWCS encours 1.749; tick737"
        ),
    },
]

src_path = DATA / "sources.csv"
with open(src_path, encoding="utf-8", newline="") as f:
    sr = csv.DictReader(f)
    sfields = sr.fieldnames
    sexist = {r["source_id"] for r in sr}
added_s = 0
with open(src_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, lineterminator="\n")
    for row in sources:
        if row["source_id"] in sexist:
            continue
        w.writerow(row)
        added_s += 1
print(f"sources +{added_s}")

# --- FOI ---
foi_row = {
    "gap_id": "gap_swl_ra2024_residual_l5",
    "hierarchy_path": "Wallonie>SWL>RA2024_residual_L5",
    "entity_id": "swl",
    "what_is_missing": (
        "Machine-readable L5: (1) cash-by-year drawdown of Plan renovation 1.1675bn grant+zero-loan "
        "with PEB outcomes vs 20000 target; (2) unit construction/renovation cost per dwelling by "
        "programme dual VMSW/SLRB; (3) Region guarantee stock on SWL debt 2.742bn and interest path; "
        "(4) vacant/non-lettable stock count and arrears € sector total; (5) HPE 137.195m unit costs "
        "and 2025-29 cash calendar; (6) Agency Habitation perimeter SWL vs SWCS/FLW cost merge plan"
    ),
    "why_it_matters": (
        "RA2024 + BNB fill strong aggregates (works 364.3m debt 2.74bn waitlist 50k) but delivery lag "
        "on renovation plan, dual unit-costs, and guarantee economics remain opaque for waste ranking"
    ),
    "priority": "8",
    "recipient_body": "SWL publicité de l'administration / SPW TLPE Logement",
    "recipient_email": "communication@swl.be",
    "recipient_postal": "https://www.swl.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_swl_ra2024_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_swl_plan_reno_1_1675bn|cmt_swl_debt_2_742bn_2024|cmt_swl_slsp_works_364_3m_2024",
    "linked_leaderboard_id": "lb_swl_plan_reno_1_1675bn|lb_swl_debt_2_742bn_2024|lb_dual_swl_vmsw_slrb_swcs_asymmetry",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick737 SWL RA2024 residual dual; ready not sent",
}

foi_path = DATA / "foi_queue.csv"
with open(foi_path, encoding="utf-8", newline="") as f:
    fr = csv.DictReader(f)
    ffields = fr.fieldnames
    fexist = {r["gap_id"] for r in fr}
if foi_row["gap_id"] not in fexist:
    with open(foi_path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ffields, lineterminator="\n")
        w.writerow(foi_row)
    print("foi +gap_swl_ra2024_residual_l5")
else:
    print("foi already exists")

# --- research queue ---
rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_728":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick737 SWL RA2024 residual dual VMSW/SLRB/SWCS: dwellings 103293 waitlist 49945; "
            "works 364.3m; plan reno 1.1675bn invest 231; debt 2.742bn fin ch 57.1; "
            "FOI gap_swl_ra2024_residual_l5 ready"
        )
if not any(r.get("task_id") == "rq_729" for r in rqs):
    rqs.append({
        "task_id": "rq_729",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined or FLRBC residual dual housing "
            "or VWF residual dual SWCS/FLW or Entity II dual residual"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick737 after rq_728",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("research_queue rq_728=done rq_729=open")

# --- loop_state ---
ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys()) if ls else [
        "state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id",
        "ticks_completed", "paused", "notes",
    ]
if ls:
    ls[0]["mode"] = "continuous"
    ls[0]["current_sprint"] = "hole_fill"
    ls[0]["last_tick_utc"] = UTC
    ls[0]["last_unit_id"] = "rq_728"
    ls[0]["ticks_completed"] = "737"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        "tick737 SWL RA2024 residual dual VMSW/SLRB/SWCS; next rq_729; "
        "progress@740 in 3; rq_116 deferred"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=737")
print("DONE tick737")

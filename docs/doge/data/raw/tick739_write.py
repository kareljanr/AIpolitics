# tick739 — FLRBC Rapport annuel 2025 residual dual VWF/SWCS/SLRB (rq_730)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T06:45:00Z"
URL_RA = "https://fonds.brussels/sites/default/files/2026-05/RAPPORT%20ANNUEL%202025%20-%20WEB.pdf"
URL_CG = "https://fonds.brussels/sites/default/files/2026-05/FLRBC%20entit%C3%A9%20financi%C3%A8re%20Compte%20G%C3%A9n%C3%A9ral%202025.pdf"
URL_PUB = "https://fonds.brussels/fr/a-propos/nos-publications"

SRC = "src_flrbc_ra2025_residual"
SRC_CG = "src_flrbc_cg2025_fin"
SRC_DUAL = "src_dual_flrbc_vwf_swcs_slrb_tick739"

# --- entity seed ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)
if not any(e.get("entity_id") == "flrbc" for e in ents):
    with open(ent_path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow([
            "flrbc",
            "Fonds du Logement van het Brussels Hoofdstedelijk Gewest",
            "Fonds du Logement de la Region de Bruxelles-Capitale FLRBC",
            "Brussels Housing Fund FLRBC",
            "agency",
            "brussels_gov",
            "FR/NL",
            "https://fonds.brussels",
            "",
            "",
            "tick739 RA2025 residual: encours 1.607bn / 16015 loans; BS 2.128bn LT debt 1.603bn; credit freeze Jul-Dec2025; dual VWF/SWCS/SLRB",
        ])
    print("entity flrbc +")
else:
    for e in ents:
        if e.get("entity_id") == "flrbc":
            e["notes"] = (
                "tick739 RA2025 residual: encours 1.607bn / 16015; BS 2.128bn LT debt 1.603bn; "
                "credit freeze Jul-Dec2025; GL arrears 22pct; dual VWF/SWCS/SLRB"
            )
    with open(ent_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=efields, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for e in ents:
            w.writerow({k: e.get(k, "") for k in efields})
    print("entity flrbc notes updated")

budgets = [
    # Production residual
    ("bud_flrbc_hyp_ops_n_769_2025", "flrbc", 2025, 769, "", "", "outturn", SRC, "strong", "Hyp operations signed COUNT 769 2025 (was 810); tick739"),
    ("bud_flrbc_acq_ops_n_597_2025", "flrbc", 2025, 597, "", "", "outturn", SRC, "strong", "Acquisition ops COUNT 597 avg 220311 @3.39pct 2025; tick739"),
    ("bud_flrbc_acq_avg_220311_2025", "flrbc", 2025, 220311, "", "", "outturn", SRC, "strong", "Acquisition avg amount 220311 EUR 2025; tick739"),
    ("bud_flrbc_acq_rate_3_39pct_2025", "flrbc", 2025, 339, "", "", "outturn", SRC, "strong", "Acquisition average debtor rate 3.39pct 2025; tick739"),
    ("bud_flrbc_acq_amount_class_131_5m_2025", "flrbc", 2025, 131525667, "", "", "outturn", SRC, "medium", "Acquisition amount class 597*220311=131.5m not primary sum; tick739"),
    ("bud_flrbc_ecoreno_n_678_2025", "flrbc", 2025, 678, "", "", "outturn", SRC, "strong", "ECORENO total COUNT 678 (496 hyp + 182 conso) 2025; tick739"),
    ("bud_flrbc_ecoreno_hyp_n_496_2025", "flrbc", 2025, 496, "", "", "outturn", SRC, "strong", "ECORENO hyp COUNT 496 2025; tick739"),
    ("bud_flrbc_ecoreno_conso_n_182_2025", "flrbc", 2025, 182, "", "", "outturn", SRC, "strong", "ECORENO consumer COUNT 182 amount 2.7m avg 15123 2025; tick739"),
    ("bud_flrbc_ecoreno_conso_amount_2_7m_2025", "flrbc", 2025, 2700000, "", "", "outturn", SRC, "strong", "ECORENO consumer amount 2.7m 2025 (was 4.6m); tick739"),
    ("bud_flrbc_ecoreno_hyp_solo_n_120_5_4m_2025", "flrbc", 2025, 5400000, "", "", "outturn", SRC, "strong", "ECORENO hyp not with acq 120 ops 5.4m avg 45125 @1.57pct 2025; tick739"),
    ("bud_flrbc_social_scale_82pct_2025", "flrbc", 2025, 82, "", "", "outturn", SRC, "strong", "Borrower households on social housing income scales 82pct 2025; tick739"),
    ("bud_flrbc_invest_power_engaged_143_2m_2025", "flrbc", 2025, 143182059, "", "", "outturn", SRC, "strong", "Investment power engaged B2 credits 143.182m of 184.092 planned 2025; tick739"),
    ("bud_flrbc_invest_power_planned_184_1m_2025", "flrbc", 2025, 184092400, "", "", "budgeted", SRC, "strong", "Investment power initially planned B2 184.092m 2025; tick739"),
    ("bud_flrbc_new_credits_spend_149_5m_2025", "flrbc", 2025, 149500000, "", "", "outturn", SRC, "strong", "Cash spend new credit origination 149.5m of 385m total dep 2025; tick739"),
    ("bud_flrbc_total_dep_385m_2025", "flrbc", 2025, 385000000, "", "", "outturn", SRC, "strong", "Total cash expenditures 385m 2025; tick739"),
    ("bud_flrbc_debt_repay_116_8m_2025", "flrbc", 2025, 116800000, "", "", "outturn", SRC, "strong", "Debt capital repayment 116.8m 2025; tick739"),
    ("bud_flrbc_interest_comm_41_8m_2025", "flrbc", 2025, 41800000, "", "", "outturn", SRC, "strong", "Interest and guarantee commissions 41.8m 2025; tick739"),
    ("bud_flrbc_housing_invest_52_1m_2025", "flrbc", 2025, 52100000, "", "", "outturn", SRC, "strong", "Investment and construction of dwellings cash 52.1m 2025; tick739"),
    ("bud_flrbc_goods_services_24_3m_2025", "flrbc", 2025, 24300000, "", "", "outturn", SRC, "strong", "Goods and services current spend 24.3m 2025; tick739"),
    ("bud_flrbc_treasury_gap_minus_56m_2025", "flrbc", 2025, -56000000, "", "", "outturn", SRC, "strong", "Recettes-depenses gap -56m drawn from treasury eoy2025; tick739"),
    ("bud_flrbc_loans_raised_130m_2025", "flrbc", 2025, 130000000, "", "", "outturn", SRC, "strong", "Borrowings raised 130m 2025 (was 260m 2024) funding freeze residual; tick739"),
    ("bud_flrbc_region_dots_15_8m_2025", "flrbc", 2025, 15800000, "", "", "outturn", SRC, "strong", "Regional dots liquidated 15.8m (invest credits 11.1 + function 4.7) 2025; tick739"),
    ("bud_flrbc_dot_invest_credits_11_1m_2025", "flrbc", 2025, 11100000, "", "", "outturn", SRC, "strong", "Investment dot for credits 11.1m liquidated 2025; tick739"),
    ("bud_flrbc_dot_function_4_7m_2025", "flrbc", 2025, 4700000, "", "", "outturn", SRC, "strong", "Functioning dots 4.7m liquidated 2025; tick739"),
    # Portfolio residual
    ("bud_flrbc_encours_immo_1_607bn_2025", "flrbc", 2025, 1607000000, "", "", "outturn", SRC, "strong", "Real-estate credit encours 1.607bn / 16015 loans eoy2025; tick739"),
    ("bud_flrbc_encours_n_16015_2025", "flrbc", 2025, 16015, "", "", "outturn", SRC, "strong", "Real-estate credits COUNT 16015 eoy2025; tick739"),
    ("bud_flrbc_hyp_b2_1_595bn_2025", "flrbc", 2025, 1595143660, "", "", "outturn", SRC, "strong", "B2 hyp stock 1.595bn / 15073 loans excl impayes eoy2025; tick739"),
    ("bud_flrbc_hyp_b2_n_15073_2025", "flrbc", 2025, 15073, "", "", "outturn", SRC, "strong", "B2 hyp COUNT 15073 eoy2025 (+4pct); tick739"),
    ("bud_flrbc_ecoreno_conso_stock_11_785m_2025", "flrbc", 2025, 11785056, "", "", "outturn", SRC, "strong", "ECORENO consumer stock 11.785m / 942 loans eoy2025; tick739"),
    ("bud_flrbc_arrears_2_193m_2025", "flrbc", 2025, 2192708, "", "", "outturn", SRC, "strong", "Credit arrears total 2.193m / 840 clients (0.14pct of SRD) eoy2025; tick739"),
    ("bud_flrbc_arrears_gt3m_1_981m_2025", "flrbc", 2025, 1980906, "", "", "outturn", SRC, "strong", "Arrears >3 months 1.981m / 444 clients eoy2025; tick739"),
    ("bud_flrbc_ccp_default_2_52pct_2025", "flrbc", 2025, 252, "", "", "outturn", SRC, "strong", "CCP registered default contracts 2.52pct (403 of 16018) vs national 0.60pct; tick739"),
    ("bud_flrbc_loss_0_290m_2025", "flrbc", 2025, 289629.52, "", "", "outturn", SRC, "strong", "Exceptional credit losses 18 contracts 0.290m 2025; tick739"),
    ("bud_flrbc_early_repay_39_15m_2025", "flrbc", 2025, 39150000, "", "", "outturn", SRC, "strong", "Early full repayments 39.15m (353 credits) 2025; tick739"),
    # Garantie locative residual
    ("bud_flrbc_gl_helps_n_1254_2025", "flrbc", 2025, 1254, "", "", "outturn", SRC, "strong", "Rental deposit helps 1254 (746 credits + 508 BRU-GAL) 2025; tick739"),
    ("bud_flrbc_gl_credit_liquid_1_164m_2025", "flrbc", 2025, 1164177, "", "", "outturn", SRC, "strong", "GL installment credits liquidated 1.164m / 746 2025; tick739"),
    ("bud_flrbc_gl_stock_1_135m_2025", "flrbc", 2025, 1134747, "", "", "outturn", SRC, "strong", "GL credit stock 1.135m / 1290 eoy2025; tick739"),
    ("bud_flrbc_gl_arrears_0_252m_22pct_2025", "flrbc", 2025, 252230, "", "", "outturn", SRC, "strong", "GL credit arrears 0.252m ratio 22pct of stock (378 of 1290 clients 29pct); tick739"),
    ("bud_flrbc_brug_al_stock_2_333m_2025", "flrbc", 2025, 2332926, "", "", "outturn", SRC, "strong", "BRU-GAL fund stock 2.333m / 2369 affiliations eoy2025; tick739"),
    ("bud_flrbc_brug_al_advances_0_771m_2025", "flrbc", 2025, 771070, "", "", "outturn", SRC, "strong", "BRU-GAL advances paid 0.771m / 508 affiliations 2025; tick739"),
    ("bud_flrbc_gl_writeoff_0_037m_2025", "flrbc", 2025, 36859.5, "", "", "outturn", SRC, "strong", "GL exceptional losses 41 contracts 0.037m 2025; tick739"),
    # Housing stock residual
    ("bud_flrbc_patrimoine_1602_2025", "flrbc", 2025, 1602, "", "", "outturn", SRC, "strong", "Rental patrimoine dwellings COUNT 1602 eoy2025; tick739"),
    ("bud_flrbc_tenants_1546_2025", "flrbc", 2025, 1546, "", "", "outturn", SRC, "strong", "Tenant households 1546 eoy2025; tick739"),
    ("bud_flrbc_sales_90_2025", "flrbc", 2025, 90, "", "", "outturn", SRC, "strong", "Dwellings sold rights-recognized COUNT 90 2025; tick739"),
    ("bud_flrbc_acquisitive_delivered_319_2025", "flrbc", 2025, 319, "", "", "outturn", SRC, "strong", "Acquisitive dwellings delivered 319 2025; tick739"),
    ("bud_flrbc_in_production_262_2025", "flrbc", 2025, 262, "", "", "outturn", SRC, "strong", "Dwellings in production on acquired sites 262 eoy2025 (was 596); tick739"),
    ("bud_flrbc_staff_164_2025", "flrbc", 2025, 164, "", "", "outturn", SRC, "strong", "Staff COUNT 164 eoy2025; tick739"),
    ("bud_flrbc_bs_total_2_128bn_2025", "flrbc", 2025, 2128000000, "", "", "outturn", SRC, "strong", "RA key total balance sheet 2.128bn eoy2025 (full entity class); tick739"),
    ("bud_flrbc_equity_303m_2025", "flrbc", 2025, 303000000, "", "", "outturn", SRC, "strong", "RA key equity 303m eoy2025; tick739"),
    ("bud_flrbc_lt_debt_1_603bn_2025", "flrbc", 2025, 1603000000, "", "", "outturn", SRC, "strong", "RA key LT debt >1y 1.603bn eoy2025; tick739"),
    ("bud_flrbc_result_4m_2025", "flrbc", 2025, 4000000, "", "", "outturn", SRC, "strong", "RA key result 4m 2025 (was 10m); tick739"),
    ("bud_flrbc_guarantee_plafond_200m_2026", "flrbc", 2026, 200000000, "", "", "budgeted", SRC, "strong", "Region guarantee plafond max 200m nominal new loans 2026 project ordinance; tick739"),
    ("bud_flrbc_safety_net_loan_50m_2026", "flrbc", 2026, 50000000, "", "", "budgeted", SRC, "strong", "Region direct loan safety-net budget 50m 2026 art37; tick739"),
    # CG financial entity residual
    ("bud_flrbc_fin_assets_1_780bn_2025", "flrbc", 2025, 1779894093, "", "", "outturn", SRC_CG, "strong", "CG financial entity total assets 1.780bn eoy2025 (art47 S.1312 carveout); tick739"),
    ("bud_flrbc_fin_equity_169_4m_2025", "flrbc", 2025, 169447897, "", "", "outturn", SRC_CG, "strong", "CG financial entity equity 169.4m eoy2025; tick739"),
    ("bud_flrbc_fin_debts_1_603bn_2025", "flrbc", 2025, 1603198394, "", "", "outturn", SRC_CG, "strong", "CG financial entity debts 1.603bn eoy2025; tick739"),
    ("bud_flrbc_fin_hyp_lt_1_535bn_2025", "flrbc", 2025, 1534708371, "", "", "outturn", SRC_CG, "strong", "CG LT mortgage loans to third parties 1.535bn eoy2025; tick739"),
    ("bud_flrbc_fin_result_1_95m_2025", "flrbc", 2025, 1949571, "", "", "outturn", SRC_CG, "strong", "CG financial entity result (net asset increase) 1.95m 2025; tick739"),
    ("bud_flrbc_offbal_securities_3_397bn_2025", "flrbc", 2025, 3397087251, "", "", "outturn", SRC_CG, "strong", "Off-balance securities by third parties guaranteeing FLRBC debts 3.397bn eoy2025; tick739"),
    # Dual residual
    ("bud_dual_flrbc_encours_1_607bn_vs_vwf_swcs", "gg_belgium", 2025, 1607000000, "", "", "outturn", SRC_DUAL, "strong", "FLRBC encours 1.607bn dual VWF 9.698 / SWCS 1.749 / SWL debt 2.742 / SLRB 1.672; tick739"),
    ("bud_dual_flrbc_gl_npl_22pct_vs_vwf_swcs", "gg_belgium", 2025, 252230, "", "", "outturn", SRC_DUAL, "strong", "FLRBC GL arrears 22pct dual VWF HW 9pct / SWCS garantie 31pct; tick739"),
    ("bud_dual_flrbc_funding_freeze_2025", "gg_belgium", 2025, 130000000, "", "", "outturn", SRC_DUAL, "strong", "FLRBC loans raised only 130m (was 260) + credit freeze Jul-Dec dual caretaker funding risk; tick739"),
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

commitments = [
    {
        "commitment_id": "cmt_flrbc_new_credits_149_5m_2025",
        "title": "FLRBC new credit origination cash 149.5m / invest power 143.2m 2025",
        "entity_id": "flrbc",
        "beneficiary": "Brussels modest-income households (82pct social scales)",
        "legal_basis": "FLRBC RA2025 + contrat de gestion 2022-2026",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "149500000",
        "cash_by_year": '{"new_credits_m":149.5,"invest_power_engaged_m":143.2,"planned_m":184.1,"hyp_ops_n":769,"acq_n":597,"ecoreno_n":678,"freeze":"Jul-Dec2025"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Social mortgage and energy renovation credit in BCR",
        "cut_option": "Funding continuity + rate subsidy FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Bruxelles>FLRBC>credits",
        "notes": "tick739",
    },
    {
        "commitment_id": "cmt_flrbc_encours_1_607bn_2025",
        "title": "FLRBC real-estate credit encours 1.607bn / 16015 loans eoy2025",
        "entity_id": "flrbc",
        "beneficiary": "Active FLRBC borrowers",
        "legal_basis": "FLRBC RA2025 credits en cours residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1607000000",
        "cash_by_year": '{"encours_m":1607,"n":16015,"hyp_b2_m":1595.1,"hyp_n":15073,"arrears_m":2.193,"arrears_pct_srd":0.14,"ccp_default_pct":2.52}',
        "remaining_eur": "1607000000",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Sustain social mortgage book",
        "cut_option": "CCP default 2.52pct vs BE 0.60 FOI cash NPL",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Bruxelles>FLRBC>encours",
        "notes": "tick739",
    },
    {
        "commitment_id": "cmt_flrbc_debt_service_158_6m_2025",
        "title": "FLRBC debt service 158.6m (repay 116.8 + interest 41.8) 2025",
        "entity_id": "flrbc",
        "beneficiary": "Bond/bank lenders to FLRBC",
        "legal_basis": "FLRBC RA2025 financement residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "158600000",
        "cash_by_year": '{"repay_m":116.8,"interest_m":41.8,"loans_raised_m":130,"lt_debt_m":1603,"treasury_gap_m":-56}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Service guaranteed and non-guaranteed debt",
        "cut_option": "Guarantee stock + 2026 funding FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Bruxelles>FLRBC>debt_service",
        "notes": "tick739",
    },
    {
        "commitment_id": "cmt_flrbc_gl_brug_al_2025",
        "title": "Garantie locative + BRU-GAL 1254 helps; GL stock arrears 22pct",
        "entity_id": "flrbc",
        "beneficiary": "Private/AIS rental deposit beneficiaries",
        "legal_basis": "FLRBC RA2025 garantie locative residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1935247",
        "cash_by_year": '{"gl_credits_liquid_m":1.164,"brug_al_advances_m":0.771,"gl_stock_m":1.135,"brug_al_stock_m":2.333,"gl_arrears_m":0.252,"gl_arrears_pct":22}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Remove deposit barrier to rental housing",
        "cut_option": "Redesign if 22pct arrears persists dual VWF/SWCS",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Bruxelles>FLRBC>garantie_locative",
        "notes": "tick739",
    },
    {
        "commitment_id": "cmt_flrbc_funding_freeze_2025",
        "title": "Credit origination freeze Jul-Dec 2025 (caretaker + funding failure)",
        "entity_id": "flrbc",
        "beneficiary": "Potential borrowers blocked mid-2025",
        "legal_basis": "FLRBC RA2025 introduction residual",
        "decision_date": "2025-07-01",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "130000000",
        "cash_by_year": '{"loans_raised_m":130,"prior_year_m":260,"guarantee_2026_plafond_m":200,"safety_net_m":50,"note":"suspended treatment of most credit apps from 1 Jul 2025"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Protect debt service 2027 under funding uncertainty",
        "cut_option": "Institutional funding continuity FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Bruxelles>FLRBC>funding_risk",
        "notes": "tick739 high-governance residual",
    },
    {
        "commitment_id": "cmt_dual_flrbc_vwf_swcs_slrb_tick739",
        "title": "Dual FLRBC RA2025 residual vs VWF/SWCS/SLRB housing finance",
        "entity_id": "gg_belgium",
        "beneficiary": "BE social housing + social credit dual map",
        "legal_basis": "FLRBC RA2025 + prior duals ticks 735-738",
        "decision_date": "2026-06-18",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1607000000",
        "cash_by_year": '{"flrbc_encours_m":1607,"flrbc_bs_m":2128,"flrbc_lt_debt_m":1603,"vwf_portfolio_m":9698,"swcs_encours_m":1749,"slrb_debt_m":1672,"swl_debt_m":2742,"note":"not TE-additive dual housing/credit OIPs"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_RA,
        "stated_goal": "Comparable regional social credit and housing finance",
        "cut_option": "Open dual rate/NPL/unit-cost dashboard FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>FLRBC_VWF_SWCS_SLRB",
        "notes": "tick739",
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

leaderboard = [
    {
        "item_id": "lb_flrbc_funding_freeze_2025",
        "name": "FLRBC credit freeze Jul-Dec 2025 after funding fail (loans 130m vs 260m)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Bruxelles>FLRBC>funding_risk",
        "annual_cost_eur": "130000000",
        "total_cost_eur": "130000000",
        "tco_notes": "Caretaker government blocked full borrowing; debt service 158.6m prioritised over new credit",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Blocked credit applicants mid-2025",
        "stated_goal": "Protect 2027 debt service under uncertainty",
        "measured_outcome": "Suspension 1 Jul-31 Dec; only Fonds-produced housing purchases continued",
        "absurdity_score": "8.0",
        "cost_score": "7.0",
        "difficulty": "3",
        "priority_index": "7.20",
        "cut_proposal": "Publish multi-year funding plan + guarantee path FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick739 high-absurdity governance residual",
    },
    {
        "item_id": "lb_flrbc_encours_1_607bn_2025",
        "name": "FLRBC credit encours 1.607bn eoy2025 dual VWF/SWCS housing finance",
        "level": "L5",
        "type": "stock",
        "hierarchy_path": "Bruxelles>FLRBC>encours",
        "annual_cost_eur": "1607000000",
        "total_cost_eur": "1607000000",
        "tco_notes": "Stock; LT debt 1.603bn; annual debt service 158.6m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "16015 active real-estate credit contracts",
        "stated_goal": "Social mortgage access in BCR",
        "measured_outcome": "CCP default 2.52pct vs BE 0.60; arrears 0.14pct SRD",
        "absurdity_score": "5.5",
        "cost_score": "8.5",
        "difficulty": "4",
        "priority_index": "6.65",
        "cut_proposal": "Cash NPL + unit subsidy FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick739 stock filter often",
    },
    {
        "item_id": "lb_flrbc_gl_arrears_22pct_2025",
        "name": "FLRBC garantie locative arrears 22pct of stock (dual VWF 9 / SWCS 31)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Bruxelles>FLRBC>garantie_locative",
        "annual_cost_eur": "1164177",
        "total_cost_eur": "1134747",
        "tco_notes": "GL credit stock 1.135m arrears 0.252m; 29pct clients; CCP default 24pct of contracts",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "1290 GL installment borrowers eoy2025",
        "stated_goal": "Zero-rate deposit access to rental",
        "measured_outcome": "22pct arrears ratio; 41 write-offs 37k EUR",
        "absurdity_score": "7.5",
        "cost_score": "4.0",
        "difficulty": "2",
        "priority_index": "6.25",
        "cut_proposal": "Redesign deposit-loan products across regions FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick739 dual high-NPL deposit residual",
    },
    {
        "item_id": "lb_flrbc_debt_service_158_6m_2025",
        "name": "FLRBC debt service 158.6m 2025 (41pct of 385m spend) vs new credit 149.5m",
        "level": "L5",
        "type": "overhead",
        "hierarchy_path": "Bruxelles>FLRBC>debt_service",
        "annual_cost_eur": "158600000",
        "total_cost_eur": "158600000",
        "tco_notes": "Repay 116.8 + interest/guarantee 41.8; exceeds new credit origination",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Lenders / Region guarantee stack",
        "stated_goal": "Service past borrowing for social credit",
        "measured_outcome": "Debt service > new credit; treasury -56m",
        "absurdity_score": "6.5",
        "cost_score": "7.5",
        "difficulty": "3",
        "priority_index": "6.80",
        "cut_proposal": "Interest path + guarantee fee transparency FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick739",
    },
    {
        "item_id": "lb_flrbc_ccp_default_2_52pct",
        "name": "FLRBC CCP mortgage default 2.52pct vs national 0.60pct (4x)",
        "level": "L5",
        "type": "risk",
        "hierarchy_path": "Bruxelles>FLRBC>npl",
        "annual_cost_eur": "1607000000",
        "total_cost_eur": "1607000000",
        "tco_notes": "403 of 16018 CCP-default; cash arrears only 0.14pct SRD but COUNT default elevated",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Social-scale mortgage borrowers 82pct",
        "stated_goal": "Controlled social mortgage defaults",
        "measured_outcome": "4x national CCP default rate; 353 new CCP flags 2025",
        "absurdity_score": "7.0",
        "cost_score": "6.5",
        "difficulty": "3",
        "priority_index": "6.60",
        "cut_proposal": "Publish euro loss given default FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick739",
    },
    {
        "item_id": "lb_flrbc_bs_2_128bn_vs_fin_1_780bn",
        "name": "FLRBC full BS 2.128bn vs financial-entity CG 1.780bn art47 carveout opacity",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Bruxelles>FLRBC>perimeter",
        "annual_cost_eur": "2128000000",
        "total_cost_eur": "2128000000",
        "tco_notes": "CoA art47 consolidates only financial sub-entity; non-financial B2i opacity dual tick706",
        "confidence": "strong",
        "source_id": SRC_CG,
        "beneficiaries": "Regional consolidation perimeter",
        "stated_goal": "ESA consolidation of financial activities only",
        "measured_outcome": "0.35bn perimeter gap RA vs CG financial",
        "absurdity_score": "7.0",
        "cost_score": "7.5",
        "difficulty": "3",
        "priority_index": "6.95",
        "cut_proposal": "Publish full vs financial reconciliation FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick739 extends prior CFP carveout residual",
    },
    {
        "item_id": "lb_dual_flrbc_vwf_swcs_slrb_asymmetry",
        "name": "Dual FLRBC 1.61bn encours / freeze vs VWF 9.70bn / SWCS 1.75bn / SLRB 1.67bn",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>FLRBC_VWF_SWCS_SLRB",
        "annual_cost_eur": "1607000000",
        "total_cost_eur": "1607000000",
        "tco_notes": "Not TE-additive; BCR funding freeze unique among duals 2025",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE social housing + social credit dual map",
        "stated_goal": "Comparable regional social credit/housing finance",
        "measured_outcome": "Four OIPs; deposit NPL 9-31pct band; BCR freeze outlier",
        "absurdity_score": "7.0",
        "cost_score": "8.0",
        "difficulty": "4",
        "priority_index": "7.10",
        "cut_proposal": "Open dual dashboard rate/NPL/funding FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick739",
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

sources = [
    {
        "source_id": SRC,
        "title": "FLRBC Rapport annuel 2025 residual dual VWF/SWCS/SLRB",
        "url": URL_RA,
        "publisher": "Fonds du Logement de la Region de Bruxelles-Capitale",
        "accessed_date": "2026-08-02",
        "source_class": "official_annual_report",
        "notes": (
            "Strong tick739: hyp 769; encours 1.607bn/16015; invest power 143.2; loans raised 130 (freeze Jul-Dec); "
            "dep 385 debt service 158.6 new credit 149.5; GL arrears 22pct; CCP default 2.52pct; "
            "BS 2.128 equity 303 LT debt 1.603; pubs " + URL_PUB
        ),
    },
    {
        "source_id": SRC_CG,
        "title": "FLRBC entite financiere Compte general 2025 residual",
        "url": URL_CG,
        "publisher": "FLRBC / SPRB",
        "accessed_date": "2026-08-02",
        "source_class": "official_accounts",
        "notes": (
            "Strong tick739: assets 1.780bn equity 169.4 debts 1.603 hyp LT 1.535 result 1.95; "
            "off-balance securities 3.397bn; art47 S.1312 financial carveout"
        ),
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual FLRBC RA2025 residual vs VWF/SWCS/SLRB housing tick739",
        "url": URL_RA,
        "publisher": "DOGE synthesis FLRBC + prior duals",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": (
            "Strong dual not TE-additive: FLRBC encours 1.607 BS 2.128 freeze residual vs VWF 9.698 "
            "SWCS 1.749 SLRB debt 1.672 SWL 2.742; GL NPL 22pct dual band 9-31; tick739"
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

foi_row = {
    "gap_id": "gap_flrbc_ra2025_residual_l5",
    "hierarchy_path": "Bruxelles>FLRBC>RA2025_residual_L5",
    "entity_id": "flrbc",
    "what_is_missing": (
        "Machine-readable L5: (1) full vs financial-entity BS reconciliation (RA 2.128bn vs CG 1.780bn) "
        "and non-financial B2i cash; (2) multi-year funding plan 2026-27 with guarantee 200m and safety-net "
        "50m drawdowns; (3) euro interest-subsidy residual and guarantee fees on 1.603bn LT debt; "
        "(4) cash NPL/recovery beyond COUNT for mortgages CCP 2.52pct and GL 22pct arrears; "
        "(5) unit construction cost for 319 acquisitive deliveries dual SLRB/VMSW; "
        "(6) credit-freeze impact count of blocked applications Jul-Dec 2025"
    ),
    "why_it_matters": (
        "RA2025 fills strong aggregates and documents funding freeze but perimeter gap, funding "
        "continuity, and dual unit costs remain opaque for waste ranking"
    ),
    "priority": "8",
    "recipient_body": "FLRBC publicite / Bruxelles Logement / SPRB Finances",
    "recipient_email": "transparence@sprb.brussels",
    "recipient_postal": "https://fonds.brussels",
    "draft_letter_path": "docs/doge/foi/drafts/gap_flrbc_ra2025_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_flrbc_funding_freeze_2025|cmt_flrbc_encours_1_607bn_2025|cmt_flrbc_debt_service_158_6m_2025",
    "linked_leaderboard_id": "lb_flrbc_funding_freeze_2025|lb_flrbc_bs_2_128bn_vs_fin_1_780bn|lb_dual_flrbc_vwf_swcs_slrb_asymmetry",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick739 FLRBC RA2025 residual dual; ready not sent; prior gap_bru_proprete_slrb_routes_l5 FLRBC carveout remains",
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
    print("foi +gap_flrbc_ra2025_residual_l5")
else:
    print("foi already exists")

rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_730":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick739 FLRBC RA2025 residual dual VWF/SWCS/SLRB: encours 1.607bn; freeze Jul-Dec; "
            "debt service 158.6; GL arrears 22pct; BS 2.128 vs fin CG 1.780; "
            "FOI gap_flrbc_ra2025_residual_l5 ready"
        )
if not any(r.get("task_id") == "rq_731" for r in rqs):
    rqs.append({
        "task_id": "rq_731",
        "title": "Mandatory progress@740 coverage % + waste top10",
        "sprint": "continuous",
        "priority": "6",
        "status": "open",
        "hierarchy_target": "L0",
        "entity_id": "gg_belgium",
        "instructions": (
            "When ticks_completed hits 740: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
            "and doge_waste_top10_current.md by priority_index; append log; no invent euros; then spawn next hole-fill."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick739 after rq_730; progress@740 next tick",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("research_queue rq_730=done rq_731=open")

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
    ls[0]["last_unit_id"] = "rq_730"
    ls[0]["ticks_completed"] = "739"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        "tick739 FLRBC RA2025 residual dual VWF/SWCS/SLRB; next rq_731 progress@740; "
        "rq_116 deferred"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=739")
print("DONE tick739")

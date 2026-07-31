# tick736 — SWCS Rapport annuel 2025 residual dual VMSW/VWF/SLRB/FLW (rq_727)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T05:15:00Z"
URL = "https://www.swcs.be/rapports-annuels/rapport-annuel-swcs-2025"
URL_ENCOURS = "https://www.swcs.be/rapports-annuels/rapport-annuel-swcs-2025/le-recouvrement-des-creances-2"
URL_DG = "https://www.swcs.be/rapports-annuels/rapport-annuel-swcs-2025/le-mot-de-la-directrice-generale-2"
URL_PLAQUETTE = "https://www.swcs.be/uploads/documents/Rapport-annuel/Archives/PLAQUETTE_SWCS_2025_OK_FINAL_DIGITALE.pdf"
URL_FLW = "https://www.flw.be/wp-content/uploads/ra24_flw.pdf"

SRC = "src_swcs_ra2025_residual"
SRC_DUAL = "src_dual_swcs_vmsw_slrb_flw_tick736"
SRC_FLW = "src_flw_ra2024_dual_tick736"

# --- entity note update ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)
for e in ents:
    if e.get("entity_id") == "swcs":
        e["notes"] = (
            "Type3 CoA Table33 BI2025 SEC rec 218.077m dep 215.628m; "
            "RA2025 residual tick736: production 483m / 6878 households; "
            "encours 1.749bn (46355 loans) contentieux 3.2pct; "
            "garantie locative contentieux 31pct; BEI+CEB signed; dual VMSW/VWF/SLRB/FLW"
        )
with open(ent_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=efields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for e in ents:
        w.writerow({k: e.get(k, "") for k in efields})
print("entity swcs notes updated")

# --- budgets ---
budgets = [
    # Production 2025 residual
    ("bud_swcs_prod_global_483m_2025", "swcs", 2025, 483000000, "", "", "outturn", SRC, "strong", "Global production 483m EUR DG Ombelets RA2025 (6878 households); tick736"),
    ("bud_swcs_households_6878_2025", "swcs", 2025, 6878, "", "", "outturn", SRC, "strong", "Households accompanied COUNT 6878 2025; tick736"),
    ("bud_swcs_hyp_count_1557_2025", "swcs", 2025, 1557, "", "", "outturn", SRC, "strong", "Mortgage credits COUNT 1557 2025; tick736"),
    ("bud_swcs_hyp_amount_281_317m_2025", "swcs", 2025, 281317377, "", "", "outturn", SRC, "strong", "Mortgage amount lent 281.317m 2025; tick736"),
    ("bud_swcs_hyp_avg_180679_2025", "swcs", 2025, 180679, "", "", "outturn", SRC, "strong", "Average mortgage 180679 EUR 2025; tick736"),
    ("bud_swcs_hyp_zero_works_21_737m_2025", "swcs", 2025, 21737205, "", "", "outturn", SRC, "strong", "Of hyp: zero-rate works loans 21.737m 2025; tick736"),
    ("bud_swcs_reno_count_5575_2025", "swcs", 2025, 5575, "", "", "outturn", SRC, "strong", "Renovation loans COUNT 5575 (4711 temp + 864 joint hyp) 2025; tick736"),
    ("bud_swcs_reno_amount_222_567m_2025", "swcs", 2025, 222566840, "", "", "outturn", SRC, "strong", "Renovation amount lent 222.567m 2025; tick736"),
    ("bud_swcs_reno_avg_39922_2025", "swcs", 2025, 39922, "", "", "outturn", SRC, "strong", "Average renovation loan 39922 EUR 2025 (was 24093 in 2023); tick736"),
    ("bud_swcs_reno_zero_works_200_830m_2025", "swcs", 2025, 200829635, "", "", "outturn", SRC, "strong", "Of reno: pure zero-rate works 200.830m 2025; tick736"),
    ("bud_swcs_garantie_loc_count_610_2025", "swcs", 2025, 610, "", "", "outturn", SRC, "strong", "Rental deposit loans COUNT 610 2025; tick736"),
    ("bud_swcs_garantie_loc_amount_0_900m_2025", "swcs", 2025, 899927, "", "", "outturn", SRC, "strong", "Rental deposit amount lent 0.900m 2025; tick736"),
    ("bud_swcs_garantie_loc_avg_1475_2025", "swcs", 2025, 1475, "", "", "outturn", SRC, "strong", "Average rental deposit loan 1475 EUR 2025; tick736"),
    ("bud_swcs_prod_reconcile_483m_2025", "swcs", 2025, 483000000, "", "", "outturn", SRC, "strong", "Prod reconcil: hyp 281.3 + zero-works 200.8 + garantie 0.9 = 483.0 (avoids double-count 21.7 hyp-works); tick736"),
    # Encours eoy2025 residual
    ("bud_swcs_encours_global_1_749bn_2025", "swcs", 2025, 1748503838, "", "", "outturn", SRC, "strong", "Loan book encours global eoy2025 1.749bn / 46355 loans; tick736"),
    ("bud_swcs_encours_loans_count_46355_2025", "swcs", 2025, 46355, "", "", "outturn", SRC, "strong", "Active loans COUNT 46355 eoy2025; tick736"),
    ("bud_swcs_contentieux_global_3_2pct_2025", "swcs", 2025, 32, "", "", "outturn", SRC, "strong", "Global contentieux rate 3.2pct of loan COUNT eoy2025; tick736"),
    ("bud_swcs_encours_hyp_1_359bn_2025", "swcs", 2025, 1358671640, "", "", "outturn", SRC, "strong", "Mortgage encours 1.359bn / 15306 loans eoy2025; tick736"),
    ("bud_swcs_encours_hyp_count_15306_2025", "swcs", 2025, 15306, "", "", "outturn", SRC, "strong", "Mortgage stock COUNT 15306 eoy2025; tick736"),
    ("bud_swcs_encours_hyp_avg_88767_2025", "swcs", 2025, 88767, "", "", "outturn", SRC, "strong", "Mortgage stock avg balance 88767 EUR eoy2025; tick736"),
    ("bud_swcs_contentieux_hyp_3_3pct_2025", "swcs", 2025, 33, "", "", "outturn", SRC, "strong", "Hyp contentieux 3.3pct COUNT (was 2.8pct 2024) eoy2025; tick736"),
    ("bud_swcs_encours_temp_389_832m_2025", "swcs", 2025, 389832198, "", "", "outturn", SRC, "strong", "Installment loan encours 389.832m / 31049 loans eoy2025; tick736"),
    ("bud_swcs_encours_temp_count_31049_2025", "swcs", 2025, 31049, "", "", "outturn", SRC, "strong", "Installment stock COUNT 31049 eoy2025; tick736"),
    ("bud_swcs_encours_reno_temp_388_048m_2025", "swcs", 2025, 388048243, "", "", "outturn", SRC, "strong", "Reno installment encours 388.048m / 28551 loans eoy2025; tick736"),
    ("bud_swcs_encours_reno_temp_count_28551_2025", "swcs", 2025, 28551, "", "", "outturn", SRC, "strong", "Reno installment COUNT 28551 eoy2025; tick736"),
    ("bud_swcs_contentieux_reno_0_7pct_2025", "swcs", 2025, 7, "", "", "outturn", SRC, "strong", "Reno installment contentieux 0.7pct COUNT eoy2025; tick736"),
    ("bud_swcs_encours_garantie_1_665m_2025", "swcs", 2025, 1664731, "", "", "outturn", SRC, "strong", "Rental deposit stock 1.665m / 2471 loans eoy2025; tick736"),
    ("bud_swcs_encours_garantie_count_2471_2025", "swcs", 2025, 2471, "", "", "outturn", SRC, "strong", "Rental deposit stock COUNT 2471 eoy2025; tick736"),
    ("bud_swcs_contentieux_garantie_31pct_2025", "swcs", 2025, 310, "", "", "outturn", SRC, "strong", "Rental deposit contentieux 31pct COUNT eoy2025 (very high vs 0.7 reno); tick736"),
    ("bud_swcs_locapret_encours_17357_2025", "swcs", 2025, 17357, "", "", "outturn", SRC, "strong", "Locaprets residual 8 dossiers 17357 EUR eoy2025; tick736"),
    ("bud_swcs_frce_encours_41043_2025", "swcs", 2025, 41043, "", "", "outturn", SRC, "strong", "FRCE energy-cost residual 19 dossiers 41043 EUR eoy2025; tick736"),
    # Ops / structure residual
    ("bud_swcs_staff_agents_140_2025", "swcs", 2025, 140, "", "", "outturn", SRC, "strong", "SWCS staff 140 agents eoy2025 (+3 IFAPME interns); tick736"),
    ("bud_swcs_network_staff_102_2025", "swcs", 2025, 102, "", "", "outturn", SRC, "strong", "Guichets 17 + local entities 6 staff COUNT 102; total mobilised ~250 with SWCS; tick736"),
    ("bud_swcs_complaints_280_2025", "swcs", 2025, 280, "", "", "outturn", SRC, "strong", "Complaints treated 280 COUNT (-14pct vs 2024); founded 23pct; tick736"),
    ("bud_swcs_appicredit_share_60pct_2025", "swcs", 2025, 60, "", "", "outturn", SRC, "medium", "AppiCredit channel >60pct of dossiers 2025; 33000+ requests since launch; tick736"),
    ("bud_swcs_ltv_ge100_69_5pct_2025", "swcs", 2025, 695, "", "", "outturn", SRC, "strong", "Access mortgages LTV >=100pct share 69.5pct 2025; tick736"),
    ("bud_swcs_c1c2_share_89pct_2025", "swcs", 2025, 89, "", "", "outturn", SRC, "strong", "Access product loans to C1/C2 precarious/modest 89pct 2025; tick736"),
    ("bud_swcs_isoles_under30_450_2025", "swcs", 2025, 450, "", "", "outturn", SRC, "strong", "Loans to isolés under 30 COUNT 450 2025; tick736"),
    ("bud_swcs_reno_cap_hit_30pct_2025", "swcs", 2025, 30, "", "", "outturn", SRC, "strong", "Share of reno dossiers hitting 60k ceiling ~30pct 2025; tick736"),
    ("bud_swcs_reno_avg_2023_24093", "swcs", 2023, 24093, "", "", "outturn", SRC, "strong", "Reno zero-rate avg 24093 EUR 2023 path to 39922 in 2025; tick736"),
    # Dual residual housing finance
    ("bud_dual_swcs_prod_483m_vs_housing_2025", "gg_belgium", 2025, 483000000, "", "", "outturn", SRC_DUAL, "strong", "SWCS prod 483m dual VMSW loan auth 1bn class / SLRB liq 803m / FLW inv 273m; not TE-additive; tick736"),
    ("bud_dual_swcs_encours_1_749bn_housing", "gg_belgium", 2025, 1748503838, "", "", "outturn", SRC_DUAL, "strong", "SWCS loan book 1.749bn dual VMSW debt 3.12bn / SLRB debt 1.67bn / FLW BS 2.24bn; tick736"),
    ("bud_dual_swcs_garantie_contentieux_31pct", "gg_belgium", 2025, 1664731, "", "", "outturn", SRC_DUAL, "strong", "SWCS rental-deposit contentieux 31pct vs reno 0.7pct dual credit-risk residual; tick736"),
    # FLW dual class residual (RA2024 primary, dual to SWCS large-fam split)
    ("bud_flw_pied_bilan_2_239bn_2024", "flw", 2024, 2239047663, "", "", "outturn", SRC_FLW, "strong", "FLW balance-sheet total 2.239bn eoy2024; tick736 dual SWCS"),
    ("bud_flw_ca_73_903m_2024", "flw", 2024, 73903255, "", "", "outturn", SRC_FLW, "strong", "FLW chiffre d affaires 73.903m 2024; tick736"),
    ("bud_flw_invest_272_652m_2024", "flw", 2024, 272651529, "", "", "outturn", SRC_FLW, "strong", "FLW investments realisations 272.652m 2024 (family loans 256.410); tick736"),
    ("bud_flw_family_loans_real_256_410m_2024", "flw", 2024, 256409736, "", "", "outturn", SRC_FLW, "strong", "FLW family loans realisations 256.410m / 3155 credits 2024; tick736"),
    ("bud_flw_credits_stock_28795_2024", "flw", 2024, 28795, "", "", "outturn", SRC_FLW, "strong", "FLW credits en cours COUNT 28795 eoy2024; tick736"),
    ("bud_flw_credits_granted_3155_2024", "flw", 2024, 3155, "", "", "outturn", SRC_FLW, "strong", "FLW credits granted COUNT 3155 2024; tick736"),
    ("bud_flw_debt_claims_ratio_81pct_2024", "flw", 2024, 81, "", "", "outturn", SRC_FLW, "strong", "FLW dettes financieres LT / creances ratio 81pct eoy2024; tick736"),
    ("bud_dual_wal_credit_social_swcs_flw_2025", "gg_belgium", 2025, 483000000, "", "", "outturn", SRC_DUAL, "strong", "WAL social credit dual: SWCS prod 483m 2025 + FLW invest 273m 2024 class split max-2-kids vs large-fam; tick736"),
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
        bid = row[0]
        if bid in existing:
            continue
        w.writerow({
            "budget_id": row[0],
            "entity_id": row[1],
            "year": row[2],
            "amount_eur": row[3],
            "amount_min_eur": row[4],
            "amount_max_eur": row[5],
            "basis": row[6],
            "source_id": row[7],
            "confidence": row[8],
            "notes": row[9],
        })
        added_b += 1
print(f"budgets +{added_b}")

# --- commitments ---
commitments = [
    {
        "commitment_id": "cmt_swcs_prod_483m_2025",
        "title": "SWCS global production 483m 2025 (6878 households)",
        "entity_id": "swcs",
        "beneficiary": "Walloon modest households (C1/C2 ~89pct access)",
        "legal_basis": "SWCS RA2025 + contrat de gestion residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "483000000",
        "cash_by_year": '{"prod_m":483,"households":6878,"hyp_m":281.317,"hyp_n":1557,"reno_m":222.567,"reno_n":5575,"garantie_m":0.900,"garantie_n":610,"zero_works_in_hyp_m":21.737,"zero_works_pure_m":200.830,"note":"prod=hyp+zero_pure+garantie"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_DG,
        "stated_goal": "Social credit access + energy renovation for modest Walloon households",
        "cut_option": "Publish unit economics + NPL cash cost of 31pct deposit defaults FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWCS>production",
        "notes": "tick736",
    },
    {
        "commitment_id": "cmt_swcs_encours_1_749bn_2025",
        "title": "SWCS loan book encours 1.749bn eoy2025 (46355 loans)",
        "entity_id": "swcs",
        "beneficiary": "Active SWCS borrowers",
        "legal_basis": "SWCS RA2025 recouvrement residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1748503838",
        "cash_by_year": '{"encours_m":1748.5,"loans_n":46355,"hyp_m":1358.7,"hyp_n":15306,"hyp_npl_pct":3.3,"temp_m":389.8,"temp_n":31049,"reno_temp_m":388.0,"reno_npl_pct":0.7,"garantie_m":1.665,"garantie_n":2471,"garantie_npl_pct":31.0,"global_npl_pct":3.2}',
        "remaining_eur": "1748503838",
        "status": "active",
        "evaluation_url": URL_ENCOURS,
        "stated_goal": "Sustain social credit book with controlled defaults",
        "cut_option": "Garantie locative product redesign if 31pct default persists",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWCS>encours",
        "notes": "tick736",
    },
    {
        "commitment_id": "cmt_swcs_reno_zero_200_8m_2025",
        "title": "Rénopack/Rénoprêt zero-rate works production 200.8m 2025",
        "entity_id": "swcs",
        "beneficiary": "Walloon homeowners energy/salubrity works",
        "legal_basis": "SWCS RA2025 Rénopack residual + primes reform Feb2025",
        "decision_date": "2025-02-13",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "200829635",
        "cash_by_year": '{"zero_works_m":200.830,"reno_total_m":222.567,"avg_eur":39922,"avg_2023_eur":24093,"cap_eur":60000,"cap_hit_pct":30,"contentieux_pct":0.7}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Zero-rate renovation with energy performance focus",
        "cut_option": "Prime redesign cost + average ticket FOI dual FLW Renopack",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>SWCS>renopack",
        "notes": "tick736",
    },
    {
        "commitment_id": "cmt_swcs_bei_ceb_financing_2025",
        "title": "BEI + CEB financing contracts signed 2025 (diversify funding)",
        "entity_id": "swcs",
        "beneficiary": "SWCS funding base / Region guarantee stack",
        "legal_basis": "SWCS RA2025 DG letter + prior RW BEI guarantee residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2035",
        "total_envelope_eur": "",
        "cash_by_year": '{"note":"EUR envelope not in public RA2025 summary; FOI for signed amounts + 500m guarantee residual from parlement Q"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL_DG,
        "stated_goal": "Diversify funding away from commercial banks",
        "cut_option": "FOI signed BEI/CEB envelopes + interest subsidy path",
        "source_id": SRC,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>SWCS>BEI_CEB",
        "notes": "tick736 amount Unknown public — FOI",
    },
    {
        "commitment_id": "cmt_flw_invest_272_7m_2024",
        "title": "FLW investments 272.7m 2024 dual SWCS large-family channel",
        "entity_id": "flw",
        "beneficiary": "Large Walloon families (3+ children) + OFS",
        "legal_basis": "FLW Rapport annuel 2024",
        "decision_date": "2024-12-31",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "272651529",
        "cash_by_year": '{"invest_m":272.652,"family_loans_m":256.410,"family_n":3155,"acp_m":2.768,"ofs_m":2.399,"locative_m":11.074,"bs_m":2239,"ca_m":73.903,"credits_stock_n":28795}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_FLW,
        "stated_goal": "Social credit + locative aid for large families",
        "cut_option": "Dual unit-cost vs SWCS Accesspack FOI",
        "source_id": SRC_FLW,
        "confidence": "strong",
        "hierarchy_path": "Wallonie>FLW>invest",
        "notes": "tick736 dual residual",
    },
    {
        "commitment_id": "cmt_dual_swcs_vmsw_slrb_flw_tick736",
        "title": "Dual SWCS RA2025 residual vs VMSW/VWF/SLRB/FLW social credit-housing",
        "entity_id": "gg_belgium",
        "beneficiary": "BE social housing + social credit dual map",
        "legal_basis": "SWCS RA2025 + FLW RA2024 + prior SLRB/VMSW duals",
        "decision_date": "2026-06-18",
        "start_year": "2024",
        "end_year": "2025",
        "total_envelope_eur": "1748503838",
        "cash_by_year": '{"swcs_prod_m":483,"swcs_encours_m":1748.5,"swcs_garantie_npl_pct":31,"flw_invest_m":272.7,"flw_bs_m":2239,"slrb_liq_m":802.7,"slrb_debt_m":1672,"vmsw_debt_m":3123,"note":"not TE-additive dual housing/credit OIPs"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Comparable regional social credit and housing finance",
        "cut_option": "Publish cross-region unit-cost and NPL matrices FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>SWCS_VMSW_SLRB_FLW",
        "notes": "tick736",
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
# priority_index ≈ 0.45*absurdity + 0.40*cost + 0.15*(10-difficulty) rough match prior
leaderboard = [
    {
        "item_id": "lb_swcs_prod_483m_2025",
        "name": "SWCS social-credit production 483m 2025 (6878 households)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Wallonie>SWCS>production",
        "annual_cost_eur": "483000000",
        "total_cost_eur": "483000000",
        "tco_notes": "Production flow; loan book encours 1.749bn separate stock",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "6878 Walloon households 2025",
        "stated_goal": "Access to ownership + renovation for modest incomes",
        "measured_outcome": "483m lent; 89pct C1/C2 access; 69.5pct LTV>=100",
        "absurdity_score": "5.5",
        "cost_score": "8.0",
        "difficulty": "4",
        "priority_index": "6.45",
        "cut_proposal": "Publish unit subsidy vs private bank equivalent + default cost",
        "status": "active",
        "struck_reason": "",
        "notes": "tick736 RA2025 residual; not pure waste — dual opacity",
    },
    {
        "item_id": "lb_swcs_encours_1_749bn",
        "name": "SWCS loan book encours 1.749bn eoy2025 dual housing finance stock",
        "level": "L5",
        "type": "stock",
        "hierarchy_path": "Wallonie>SWCS>encours",
        "annual_cost_eur": "1748503838",
        "total_cost_eur": "1748503838",
        "tco_notes": "Stock not annual TE spend; dual VMSW 3.12bn debt / SLRB 1.67bn",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "46355 active loans",
        "stated_goal": "Sustainable social credit portfolio",
        "measured_outcome": "Global NPL 3.2pct; hyp NPL 3.3pct up from 2.8",
        "absurdity_score": "5.5",
        "cost_score": "8.5",
        "difficulty": "4",
        "priority_index": "6.65",
        "cut_proposal": "NPL cash cost + interest subsidy TCO FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick736 stock filtered from pure annual top10 often",
    },
    {
        "item_id": "lb_swcs_garantie_npl_31pct",
        "name": "SWCS rental-deposit loans contentieux 31pct (2471 loans 1.7m stock)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Wallonie>SWCS>garantie_locative",
        "annual_cost_eur": "899927",
        "total_cost_eur": "1664731",
        "tco_notes": "Stock 1.665m; 2025 production 0.900m; NPL 31pct COUNT vs reno 0.7pct",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Rental deposit borrowers modest incomes",
        "stated_goal": "Access to rental housing via zero-rate deposit loans",
        "measured_outcome": "31pct contentieux COUNT — product failure signal",
        "absurdity_score": "8.0",
        "cost_score": "4.0",
        "difficulty": "2",
        "priority_index": "6.50",
        "cut_proposal": "Redesign or suspend product until default <10pct; FOI recovery cash",
        "status": "active",
        "struck_reason": "",
        "notes": "tick736 high-absurdity residual",
    },
    {
        "item_id": "lb_swcs_reno_zero_200_8m",
        "name": "Rénopack zero-rate works 200.8m 2025 avg ticket 40k (+66pct vs 2023)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Wallonie>SWCS>renopack",
        "annual_cost_eur": "200829635",
        "total_cost_eur": "200829635",
        "tco_notes": "Zero-rate lending + regional primes stack; dual FLW Renopack 54.5m 2024",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "~5575 renovation borrowers class",
        "stated_goal": "Energy renovation for Walloon homes",
        "measured_outcome": "Avg 39922 from 24093; 30pct hit 60k cap; NPL only 0.7pct",
        "absurdity_score": "5.5",
        "cost_score": "7.5",
        "difficulty": "3",
        "priority_index": "6.40",
        "cut_proposal": "Prime reform impact + additionality vs private energy loans FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick736",
    },
    {
        "item_id": "lb_swcs_hyp_npl_rise_3_3pct",
        "name": "SWCS mortgage contentieux rise 2.8→3.3pct on 1.36bn stock",
        "level": "L5",
        "type": "risk",
        "hierarchy_path": "Wallonie>SWCS>hyp_npl",
        "annual_cost_eur": "1358671640",
        "total_cost_eur": "1358671640",
        "tco_notes": "Stock; cash NPL cost not published — FOI",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "15306 mortgage borrowers",
        "stated_goal": "Controlled social mortgage portfolio",
        "measured_outcome": "NPL rate up 0.5pp YoY; avg balance 88767",
        "absurdity_score": "6.0",
        "cost_score": "7.0",
        "difficulty": "3",
        "priority_index": "6.40",
        "cut_proposal": "Publish € NPL / recovery / write-off FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick736",
    },
    {
        "item_id": "lb_flw_invest_272_7m_2024",
        "name": "FLW investments 272.7m 2024 dual SWCS large-family social credit",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Wallonie>FLW>invest",
        "annual_cost_eur": "272651529",
        "total_cost_eur": "272651529",
        "tco_notes": "Family loans 256.4m of 272.7; BS 2.24bn dual SWCS 1.75bn book",
        "confidence": "strong",
        "source_id": SRC_FLW,
        "beneficiaries": "Large families 3+ children / OFS / locative",
        "stated_goal": "Social credit and locative aid for large families",
        "measured_outcome": "3155 credits; 28795 stock; CA 73.9m",
        "absurdity_score": "5.0",
        "cost_score": "7.5",
        "difficulty": "4",
        "priority_index": "6.00",
        "cut_proposal": "Dual unit-cost vs SWCS Accesspack; merge Agency Habitation FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick736 dual residual",
    },
    {
        "item_id": "lb_dual_swcs_vmsw_slrb_flw_asymmetry",
        "name": "Dual SWCS 483m prod / 1.75bn book vs VMSW 3.12bn / SLRB 1.67bn / FLW 2.24bn",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>SWCS_VMSW_SLRB_FLW",
        "annual_cost_eur": "1748503838",
        "total_cost_eur": "1748503838",
        "tco_notes": "Not TE-additive; institutional split opacity (Agency Habitation pending)",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE social housing + social credit dual map",
        "stated_goal": "Comparable regional housing finance",
        "measured_outcome": "Four OIPs separate books; unit-cost dual still FOI",
        "absurdity_score": "7.0",
        "cost_score": "8.0",
        "difficulty": "4",
        "priority_index": "7.10",
        "cut_proposal": "Single open dual dashboard unit-cost dwellings + NPL",
        "status": "active",
        "struck_reason": "",
        "notes": "tick736",
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
        "title": "SWCS Rapport annuel 2025 residual dual VMSW/VWF/SLRB/FLW",
        "url": URL,
        "publisher": "Société wallonne du crédit social (SWCS)",
        "accessed_date": "2026-08-02",
        "source_class": "official_annual_report",
        "notes": (
            "Strong tick736: prod 483m / 6878 hh; hyp 281.3m (1557) reno 222.6m (5575) garantie 0.9m (610); "
            "encours 1.749bn (46355) NPL 3.2pct; hyp NPL 3.3pct; garantie NPL 31pct; reno NPL 0.7pct; "
            "staff 140; BEI+CEB signed; plaquette "
            + URL_PLAQUETTE
            + "; encours page "
            + URL_ENCOURS
            + "; raw swcs_plaquette_2025.pdf + swcs_ra2025_extract.txt"
        ),
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual SWCS RA2025 residual vs VMSW/SLRB/FLW social credit-housing tick736",
        "url": URL,
        "publisher": "DOGE synthesis SWCS + FLW + prior duals",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": (
            "Strong dual not TE-additive: SWCS prod 483 / encours 1.749 vs VMSW debt 3.123 "
            "SLRB debt 1.672 liq 802.7 FLW BS 2.239 invest 272.7; garantie NPL 31pct residual; tick736"
        ),
    },
    {
        "source_id": SRC_FLW,
        "title": "FLW Rapport annuel 2024 dual residual SWCS large-family channel",
        "url": URL_FLW,
        "publisher": "Fonds du Logement des familles nombreuses de Wallonie (FLW)",
        "accessed_date": "2026-08-02",
        "source_class": "official_annual_report",
        "notes": (
            "Strong tick736 dual: pied de bilan 2.239bn; CA 73.903m; invest 272.652m; "
            "family loans 256.410m / 3155; stock 28795; debt/claims 81pct; raw flw_ra2024.pdf"
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

# --- FOI queue ---
foi_row = {
    "gap_id": "gap_swcs_ra2025_residual_l5",
    "hierarchy_path": "Wallonie>SWCS>RA2025_residual_L5",
    "entity_id": "swcs",
    "what_is_missing": (
        "Machine-readable L5: (1) cash NPL / recovery / write-off for hyp 3.3pct and garantie locative 31pct "
        "contentieux 2025; (2) signed BEI and CEB financing envelopes + interest subsidy and RW guarantee "
        "amounts; (3) production vs contrat-de-gestion target path (410m→350m residual) with monthly series; "
        "(4) unit subsidy equivalent vs private bank rates by RIG band; (5) dual unit-cost vs FLW Accesspack "
        "and VWF; (6) Le Phare HQ total cost + financing"
    ),
    "why_it_matters": (
        "RA2025 fills strong production and encours aggregates but € default cost, European funding size, "
        "and dual unit economics vs FLW/VMSW/SLRB remain opaque for waste ranking"
    ),
    "priority": "8",
    "recipient_body": "SWCS publicité de l'administration / SPW TLPE Logement",
    "recipient_email": "contact@swcs.be",
    "recipient_postal": "https://www.swcs.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_swcs_ra2025_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_swcs_prod_483m_2025|cmt_swcs_encours_1_749bn_2025|cmt_swcs_bei_ceb_financing_2025",
    "linked_leaderboard_id": "lb_swcs_garantie_npl_31pct|lb_swcs_encours_1_749bn|lb_dual_swcs_vmsw_slrb_flw_asymmetry",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick736 SWCS RA2025 residual dual; ready not sent",
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
    print("foi +gap_swcs_ra2025_residual_l5")
else:
    print("foi already exists")

# --- research queue: close rq_727, spawn rq_728 ---
rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_727":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick736 SWCS RA2025 residual dual VMSW/SLRB/FLW: prod 483m 6878hh; "
            "encours 1.749bn NPL 3.2; garantie NPL 31; reno zero 200.8; FLW invest 272.7 dual; "
            "FOI gap_swcs_ra2025_residual_l5 ready"
        )
if not any(r.get("task_id") == "rq_728" for r in rqs):
    rqs.append({
        "task_id": "rq_728",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined or SWL residual dual VMSW/SLRB "
            "or FLRBC residual dual housing or Entity II dual residual"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick736 after rq_727",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("research_queue rq_727=done rq_728=open")

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
    ls[0]["last_unit_id"] = "rq_727"
    ls[0]["ticks_completed"] = "736"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        "tick736 SWCS RA2025 residual dual VMSW/SLRB/FLW; next rq_728; "
        "progress@740 in 4; rq_116 deferred"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=736")
print("DONE tick736")

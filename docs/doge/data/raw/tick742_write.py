# tick742 — Wonen in Vlaanderen Jaarverslag 2025 residual dual VMSW/SWL (rq_733)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T08:15:00Z"
URL = "https://publicaties.vlaanderen.be/view-file/85714"
URL_PAGE = "https://www.vlaanderen.be/publicaties/jaarverslag-wonen-in-vlaanderen"

SRC = "src_wiv_jv2025_residual"
SRC_DUAL = "src_dual_wiv_vmsw_swl_tick742"

# --- entity ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)
if not any(e.get("entity_id") == "wonen_in_vlaanderen" for e in ents):
    with open(ent_path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow([
            "wonen_in_vlaanderen",
            "Agentschap Wonen in Vlaanderen",
            "Agence Logement en Flandre",
            "Flanders Housing Agency",
            "agency",
            "vlaanderen_gov",
            "nl",
            "https://www.vlaanderen.be/wonen-in-vlaanderen",
            "openbaarheid@vlaanderen.be",
            "",
            "tick742 JV2025 residual dual VMSW: stock 178743 waitlist 215337 vacancy 10.51pct; huursubsidie 68.5m huurpremie 63.5m; staff 480",
        ])
    print("entity wonen_in_vlaanderen +")
else:
    for e in ents:
        if e.get("entity_id") == "wonen_in_vlaanderen":
            e["notes"] = (
                "tick742 JV2025 residual dual VMSW: stock 178743 waitlist 215337 vacancy 10.51pct; "
                "huursubsidie 68.5m huurpremie 63.5m; staff 480; FS3 dual VMSW"
            )
    with open(ent_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=efields, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for e in ents:
            w.writerow({k: e.get(k, "") for k in efields})
    print("entity notes updated")

budgets = [
    # Stock / waitlist residual
    ("bud_wiv_social_stock_178743_2025", "wonen_in_vlaanderen", 2025, 178743, "", "", "outturn", SRC, "strong", "Social rental dwellings Flanders total 178743 eoy2025 (166077 owned + 12666 rented-in); tick742"),
    ("bud_wiv_owned_stock_166077_2025", "wonen_in_vlaanderen", 2025, 166077, "", "", "outturn", SRC, "strong", "WM-owned social rental stock 166077 eoy2025; tick742"),
    ("bud_wiv_rented_in_stock_12666_2025", "wonen_in_vlaanderen", 2025, 12666, "", "", "outturn", SRC, "strong", "Rented-in social stock 12666 eoy2025 (-5pct YoY); tick742"),
    ("bud_wiv_vacancy_owned_18793_2025", "wonen_in_vlaanderen", 2025, 18793, "", "", "outturn", SRC, "strong", "Vacant owned social dwellings 18793 (10.51pct of 166077); 59pct structural; tick742"),
    ("bud_wiv_vacancy_rate_10_51pct_2025", "wonen_in_vlaanderen", 2025, 1051, "", "", "outturn", SRC, "strong", "Owned stock vacancy rate 10.51pct eoy2025; structural +6pct path; tick742"),
    ("bud_wiv_waitlist_cir_215337_2025", "wonen_in_vlaanderen", 2025, 215337, "", "", "outturn", SRC, "strong", "CIR active social-housing waitlist inscriptions 215337 eoy2025 (15pct already social tenants); tick742"),
    ("bud_wiv_waitlist_new_44521_2025", "wonen_in_vlaanderen", 2025, 44521, "", "", "outturn", SRC, "strong", "New CIR inscriptions 44521 2025; deleted 34149; tick742"),
    ("bud_wiv_waitlist_deleted_34149_2025", "wonen_in_vlaanderen", 2025, 34149, "", "", "outturn", SRC, "strong", "CIR deletions 34149 2025 (assign accepted 12379 primary); tick742"),
    ("bud_wiv_avg_wait_5y_2025", "wonen_in_vlaanderen", 2025, 5, "", "", "outturn", SRC, "strong", "Average wait years before assign 5 years 2025; tick742"),
    ("bud_wiv_mean_social_rent_427_33_2025", "wonen_in_vlaanderen", 2025, 427.33, "", "", "outturn", SRC, "strong", "Mean social rent owned stock 427.33 EUR/mo 2025; tick742"),
    ("bud_wiv_adapted_housing_demand_11081_2025", "wonen_in_vlaanderen", 2025, 11081, "", "", "outturn", SRC, "strong", "CIR adapted-housing demand dossiers 11081 (5.15pct waitlist); tick742"),
    # Affordability programmes residual
    ("bud_wiv_huursubsidie_68_512m_2025", "wonen_in_vlaanderen", 2025, 68511515, "", "", "outturn", SRC, "strong", "Vlaamse huursubsidie paid 68.512m / 21877 beneficiaries eoy2025; tick742"),
    ("bud_wiv_huursubsidie_benef_21877_2025", "wonen_in_vlaanderen", 2025, 21877, "", "", "outturn", SRC, "strong", "Huursubsidie beneficiaries COUNT 21877 Dec2025; tick742"),
    ("bud_wiv_huursubsidie_apps_8421_2025", "wonen_in_vlaanderen", 2025, 8421, "", "", "outturn", SRC, "strong", "Huursubsidie applications 8421 (approve 3805 refuse 4969) 2025; tick742"),
    ("bud_wiv_huurpremie_63_508m_2025", "wonen_in_vlaanderen", 2025, 63507503, "", "", "outturn", SRC, "strong", "Vlaamse huurpremie paid 63.508m / 23353 beneficiaries avg 219.40/mo 2025; tick742"),
    ("bud_wiv_huurpremie_benef_23353_2025", "wonen_in_vlaanderen", 2025, 23353, "", "", "outturn", SRC, "strong", "Huurpremie beneficiaries COUNT 23353 Dec2025; tick742"),
    ("bud_wiv_ekm_loans_90_346m_2025", "wonen_in_vlaanderen", 2025, 90346386, "", "", "outturn", SRC, "strong", "EKM non-subsidised social mortgages 90.346m / 576 loans 2025; tick742"),
    ("bud_wiv_ekm_n_576_2025", "wonen_in_vlaanderen", 2025, 576, "", "", "outturn", SRC, "strong", "EKM loans COUNT 576 2025; tick742"),
    # Security residual
    ("bud_wiv_fbu_approved_256_2025", "wonen_in_vlaanderen", 2025, 256, "", "", "outturn", SRC, "strong", "FBU eviction-prevention agreements approved 256 of 278 filed 2025 (-15.5pct); tick742"),
    ("bud_wiv_noodwoningen_subs_10_189m_2025", "wonen_in_vlaanderen", 2025, 10189260, "", "", "outturn", SRC, "strong", "Emergency housing call 2025 subsidies 10.189m / 28 projects / 62 new + 92 reno; tick742"),
    ("bud_wiv_vgw_payouts_4_992m_2025", "wonen_in_vlaanderen", 2025, 4992035.49, "", "", "outturn", SRC, "strong", "VGW insurance Ethias payouts total 4.992m 2025 (+13.45pct; 1815 interventions); tick742"),
    # Financing residual (agency lens dual VMSW)
    ("bud_wiv_fs3_assign_on_2024_budget_761_7m", "wonen_in_vlaanderen", 2025, 761701053, "", "", "outturn", SRC, "strong", "FS3 assigned in 2025 on 2024 budget 761.7m of 870 (NB 345.9 reno 396.3 zero-rate transfer 19.5); tick742"),
    ("bud_wiv_fs3_zero_transfer_19_52m_2025", "wonen_in_vlaanderen", 2025, 19517170.70, "", "", "outturn", SRC, "strong", "Zero-rate loans for WM property transfers 19.52m 2025 (3pct of FS3 assign); tick742"),
    ("bud_wiv_market_finance_202_87m_2025", "wonen_in_vlaanderen", 2025, 202870000, "", "", "outturn", SRC, "strong", "Market-rate finance assigned 202.87m of max 220m 2025; tick742"),
    ("bud_wiv_market_finance_cap_220m_2025", "wonen_in_vlaanderen", 2025, 220000000, "", "", "budgeted", SRC, "strong", "Market-rate finance annual cap 220m 2024-25; tick742"),
    ("bud_wiv_doorverhuur_base_29_725m_2025", "wonen_in_vlaanderen", 2025, 29724551.56, "", "", "outturn", SRC, "strong", "Doorverhuur base+aanvullend subsidy 29.725m to 41 WM 2025; tick742"),
    ("bud_wiv_doorverhuur_growth_0_172m_2025", "wonen_in_vlaanderen", 2025, 171925.75, "", "", "outturn", SRC, "strong", "Doorverhuur growth subsidy 0.172m 2025; tick742"),
    ("bud_wiv_doorverhuur_via_1_380m_2025", "wonen_in_vlaanderen", 2025, 1380450.11, "", "", "outturn", SRC, "strong", "Doorverhuur VIA subsidy 1.380m 2025; tick742"),
    ("bud_wiv_doorverhuur_total_class_31_3m_2025", "wonen_in_vlaanderen", 2025, 31276927.42, "", "", "outturn", SRC, "strong", "Doorverhuur total class base+growth+VIA 31.277m 2025; tick742"),
    # Supply residual
    ("bud_wiv_newbuild_tender_rental_830_2025", "wonen_in_vlaanderen", 2025, 830, "", "", "outturn", SRC, "medium", "Newbuild tenders rental COUNT 830 2025 provisional undercount; tick742"),
    ("bud_wiv_newbuild_tender_sale_145_2025", "wonen_in_vlaanderen", 2025, 145, "", "", "outturn", SRC, "medium", "Newbuild tenders sale COUNT 145 2025 provisional; tick742"),
    ("bud_wiv_newbuild_delivered_rental_1190_2025", "wonen_in_vlaanderen", 2025, 1190, "", "", "outturn", SRC, "medium", "Newbuild delivered rental 1190 2025 provisional undercount; tick742"),
    ("bud_wiv_newbuild_delivered_sale_275_2025", "wonen_in_vlaanderen", 2025, 275, "", "", "outturn", SRC, "medium", "Newbuild delivered sale 275 2025 provisional; tick742"),
    ("bud_wiv_purchases_good_stock_141_2025", "wonen_in_vlaanderen", 2025, 141, "", "", "outturn", SRC, "strong", "Good existing dwellings purchased 141 2025; tick742"),
    ("bud_wiv_sales_social_261_2025", "wonen_in_vlaanderen", 2025, 261, "", "", "outturn", SRC, "strong", "Social rental dwellings sold 261 2025 (moratorium to 2028); tick742"),
    ("bud_wiv_reno_delivered_1566_2025", "wonen_in_vlaanderen", 2025, 1566, "", "", "outturn", SRC, "medium", "Renovated social dwellings delivered 1566 2025 provisional; tick742"),
    ("bud_wiv_replacement_build_648_2025", "wonen_in_vlaanderen", 2025, 648, "", "", "outturn", SRC, "medium", "Replacement builds delivered 648 2025 provisional; tick742"),
    ("bud_wiv_vkf_energy_prem_28_994m_2025", "wonen_in_vlaanderen", 2025, 28993525, "", "", "outturn", SRC, "strong", "VKF energy renovation premiums granted 28.994m 2025 (cum 2021-25 115.54m); tick742"),
    ("bud_wiv_vkf_energy_prem_cum_115_54m_2021_25", "wonen_in_vlaanderen", 2025, 115540000, "", "", "outturn", SRC, "strong", "VKF energy premiums cumulative 2021-2025 115.54m class; tick742"),
    ("bud_wiv_design_insulate_roofs_5_441m_2025", "wonen_in_vlaanderen", 2025, 5441176.78, "", "", "outturn", SRC, "strong", "Design&Insulate roofs framework assigned 5.441m 2025; tick742"),
    ("bud_wiv_design_insulate_cavity_1_943m_cum", "wonen_in_vlaanderen", 2025, 1942559.14, "", "", "outturn", SRC, "strong", "Design&Insulate cavity walls ordered cum 1.943m eoy2025; tick742"),
    ("bud_wiv_modular_framework_543_units", "wonen_in_vlaanderen", 2025, 543, "", "", "outturn", SRC, "strong", "Modular housing framework mini-competitions 543 dwellings (18 delivered 2025); tick742"),
    ("bud_wiv_basiskoten_100m_1744_2024", "wonen_in_vlaanderen", 2024, 100000000, "", "", "outturn", SRC, "strong", "Boost basiskot track3 100m fully assigned 2024 for 1744 rooms (864 net growth class); tick742"),
    # Org residual
    ("bud_wiv_staff_480_2025", "wonen_in_vlaanderen", 2025, 480, "", "", "outturn", SRC, "strong", "WiV staff COUNT 480 / 440.5 FTE eoy2025; tick742"),
    ("bud_wiv_staff_fte_440_5_2025", "wonen_in_vlaanderen", 2025, 440.5, "", "", "outturn", SRC, "strong", "WiV FTE 440.5 eoy2025; tick742"),
    ("bud_wiv_complaints_mvp_633_2025", "wonen_in_vlaanderen", 2025, 633, "", "", "outturn", SRC, "strong", "MVP MijnVerbouwPremie complaints receivable 633 (170 grounded) 2025; tick742"),
    ("bud_wiv_helpdesk_8825_2025", "wonen_in_vlaanderen", 2025, 8825, "", "", "outturn", SRC, "strong", "Helpdesk questions answered 8825 2025 (was 10979); tick742"),
    ("bud_wiv_municipal_vacancy_register_30807_2025", "wonen_in_vlaanderen", 2025, 30807, "", "", "outturn", SRC, "medium", "Municipal vacancy register stock ~30807 dwellings/buildings (~200 communes) eoy2025; tick742"),
    ("bud_wiv_vdab_fines_564_2025", "wonen_in_vlaanderen", 2025, 564, "", "", "outturn", SRC, "strong", "Toezicht VDAB-registration fines COUNT 564 2025 (many later waived for disability ~1/3); tick742"),
    # Dual residual
    ("bud_dual_wiv_stock_178743_vs_swl_103293", "gg_belgium", 2025, 178743, "", "", "outturn", SRC_DUAL, "strong", "VL social stock 178743 dual SWL 103293 / SLRB ~42k class / FLRBC 1602 own; not TE-additive; tick742"),
    ("bud_dual_wiv_waitlist_215337_vs_swl_49945", "gg_belgium", 2025, 215337, "", "", "outturn", SRC_DUAL, "strong", "VL CIR waitlist 215337 dual SWL 49945 / BCR demand residual; tick742"),
    ("bud_dual_wiv_vacancy_10_51pct_vs_housing", "gg_belgium", 2025, 18793, "", "", "outturn", SRC_DUAL, "strong", "VL owned vacancy 10.51pct (18793) dual SWL rotation 6.69pct / SLRB arrears residual; tick742"),
    ("bud_dual_wiv_huursubsidie_68_5m_vs_wal", "gg_belgium", 2025, 68511515, "", "", "outturn", SRC_DUAL, "strong", "VL huursubsidie 68.5m + huurpremie 63.5m dual WAL housing aids class; tick742"),
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
        "commitment_id": "cmt_wiv_social_stock_178743_2025",
        "title": "Flanders social rental stock 178743 eoy2025 (vacancy 10.51pct owned)",
        "entity_id": "wonen_in_vlaanderen",
        "beneficiary": "Social tenants + 215337 CIR waitlist",
        "legal_basis": "Wonen in Vlaanderen JV2025",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "178743",
        "cash_by_year": '{"stock_n":178743,"owned_n":166077,"rented_in_n":12666,"vacant_owned_n":18793,"vacancy_pct":10.51,"structural_vacancy_share_pct":59,"waitlist_n":215337,"avg_wait_y":5,"mean_rent_eur":427.33}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Affordable secure social rental supply",
        "cut_option": "Structural vacancy 59pct FOI + dual SWL unit-cost",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>social_stock",
        "notes": "tick742 amount_eur is COUNT stock",
    },
    {
        "commitment_id": "cmt_wiv_huursubsidie_huurpremie_132m_2025",
        "title": "Huursubsidie 68.5m + huurpremie 63.5m = ~132m private-rent support 2025",
        "entity_id": "wonen_in_vlaanderen",
        "beneficiary": "21877+23353 modest private renters",
        "legal_basis": "Wonen in Vlaanderen JV2025 betaalbaar wonen",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "132019018",
        "cash_by_year": '{"huursubsidie_m":68.512,"huursubsidie_benef":21877,"huurpremie_m":63.508,"huurpremie_benef":23353,"huursubsidie_refuse_n":4969}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Support modest private renters and long waitlist households",
        "cut_option": "Refuse rate path + dual WAL aids FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>huursubsidie",
        "notes": "tick742",
    },
    {
        "commitment_id": "cmt_wiv_fs3_market_finance_2025",
        "title": "FS3 assign 761.7m on 2024 budget + market finance 202.9m 2025",
        "entity_id": "wonen_in_vlaanderen",
        "beneficiary": "Woonmaatschappijen via VMSW bank function",
        "legal_basis": "WiV JV2025 + VMSW dual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "964571053",
        "cash_by_year": '{"fs3_assign_m":761.7,"fs3_nb_m":345.9,"fs3_reno_m":396.3,"zero_transfer_m":19.5,"market_m":202.9,"market_cap_m":220,"fs3_2025_budget_m":870,"fs3_2025_assign_m":0}',
        "remaining_eur": "870000000",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Finance social housing build/renovation",
        "cut_option": "2025 FS3 zero-assign lag FOI dual VMSW",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>FS3",
        "notes": "tick742",
    },
    {
        "commitment_id": "cmt_wiv_doorverhuur_31_3m_2025",
        "title": "Doorverhuur operating subsidies to 41 WM 31.3m class 2025",
        "entity_id": "wonen_in_vlaanderen",
        "beneficiary": "41 woonmaatschappijen rented-in stock ops",
        "legal_basis": "WiV JV2025 overgangsregeling doorverhuur",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "31276927.42",
        "cash_by_year": '{"base_m":29.725,"growth_m":0.172,"via_m":1.380,"rented_in_n":12666}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Fund private-to-social sublet activity",
        "cut_option": "Unit subsidy per rented-in dwelling FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>doorverhuur",
        "notes": "tick742",
    },
    {
        "commitment_id": "cmt_wiv_vkf_energy_29m_2025",
        "title": "VKF energy renovation premiums social stock 28.99m 2025",
        "entity_id": "wonen_in_vlaanderen",
        "beneficiary": "Social housing energy renovation",
        "legal_basis": "WiV JV2025 Klimaatfonds residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "28993525",
        "cash_by_year": '{"prem_m":28.994,"cum_2021_25_m":115.54,"reno_delivered_n":1566,"replacement_n":648,"design_insulate_roofs_m":5.441}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Accelerate social stock energy renovation to 2050",
        "cut_option": "EPC F/E share dual SWL FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>VKF",
        "notes": "tick742",
    },
    {
        "commitment_id": "cmt_dual_wiv_vmsw_swl_tick742",
        "title": "Dual WiV JV2025 residual vs VMSW/SWL/SLRB social housing systems",
        "entity_id": "gg_belgium",
        "beneficiary": "BE social housing dual map",
        "legal_basis": "WiV JV2025 + VMSW tick741 + SWL/SLRB duals",
        "decision_date": "2026-06-18",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "178743",
        "cash_by_year": '{"vl_stock_n":178743,"vl_waitlist_n":215337,"vl_vacancy_pct":10.51,"vl_huursubsidie_m":68.5,"vl_huurpremie_m":63.5,"swl_stock_n":103293,"swl_waitlist_n":49945,"slrb_liq_m":802.7,"vmsw_debt_m":10499,"note":"not TE-additive"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Comparable regional social housing outcomes",
        "cut_option": "Open dual vacancy/waitlist/unit-cost dashboard FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>WiV_VMSW_SWL",
        "notes": "tick742",
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
        "item_id": "lb_wiv_waitlist_215337_2025",
        "name": "CIR social-housing waitlist 215337 vs stock 178743 / avg wait 5y",
        "level": "L5",
        "type": "outcome_gap",
        "hierarchy_path": "Vlaanderen>Wonen>waitlist",
        "annual_cost_eur": "215337",
        "total_cost_eur": "215337",
        "tco_notes": "COUNT gap; 15pct already social tenants; dual SWL 49945",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Candidate social tenants Flanders",
        "stated_goal": "Access to social rental",
        "measured_outcome": "Waitlist > stock; 5y avg wait; newbuild tender only 830 rental provisional",
        "absurdity_score": "7.5",
        "cost_score": "5.5",
        "difficulty": "5",
        "priority_index": "6.20",
        "cut_proposal": "Supply acceleration + vacancy release FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick742 amount is COUNT",
    },
    {
        "item_id": "lb_wiv_vacancy_10_51pct_18793",
        "name": "Owned social stock vacancy 10.51pct (18793) with 59pct structural",
        "level": "L5",
        "type": "outcome_gap",
        "hierarchy_path": "Vlaanderen>Wonen>vacancy",
        "annual_cost_eur": "18793",
        "total_cost_eur": "18793",
        "tco_notes": "Structural vacancy +6pct YoY; dual FS3 reno underuse",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Empty social dwellings / waitlist pressure",
        "stated_goal": "Maximise occupied social stock",
        "measured_outcome": "10.51pct vacant owned; friction -5pct structural +6pct",
        "absurdity_score": "8.0",
        "cost_score": "5.5",
        "difficulty": "3",
        "priority_index": "6.55",
        "cut_proposal": "Structural vacancy cash cost + reno pipeline FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick742",
    },
    {
        "item_id": "lb_wiv_huursubsidie_huurpremie_132m",
        "name": "Private-rent support huursubsidie+huurpremie ~132m 2025",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Vlaanderen>Wonen>rent_support",
        "annual_cost_eur": "132019018",
        "total_cost_eur": "132019018",
        "tco_notes": "Huursubsidie refuse rate high (4969 of 8421 apps); dual social waitlist failure",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "~45k beneficiary households class",
        "stated_goal": "Affordable private rent for modest incomes",
        "measured_outcome": "68.5+63.5m; avg premie 219/mo",
        "absurdity_score": "5.5",
        "cost_score": "7.0",
        "difficulty": "3",
        "priority_index": "6.10",
        "cut_proposal": "Targeting audit FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick742",
    },
    {
        "item_id": "lb_wiv_fs3_2025_zero_assign_agency",
        "name": "FS3 2025 budget 870m still 0 assigned eoy (agency confirms VMSW lag)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Vlaanderen>Wonen>FS3",
        "annual_cost_eur": "870000000",
        "total_cost_eur": "870000000",
        "tco_notes": "2025 calendar used 2024 budget; dual VMSW underuse residual",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Future social housing projects",
        "stated_goal": "Annual FS3 investment programme",
        "measured_outcome": "0% 2025 FS3 assign; market finance 202.9 of 220",
        "absurdity_score": "6.5",
        "cost_score": "8.0",
        "difficulty": "3",
        "priority_index": "6.95",
        "cut_proposal": "Monthly assign dashboard FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick742",
    },
    {
        "item_id": "lb_wiv_newbuild_vs_waitlist_gap",
        "name": "Newbuild tenders 830 rental vs waitlist 215k / vacancy 19k",
        "level": "L5",
        "type": "outcome_gap",
        "hierarchy_path": "Vlaanderen>Wonen>supply_gap",
        "annual_cost_eur": "830",
        "total_cost_eur": "215337",
        "tco_notes": "Provisional tender counts understate; still tiny vs waitlist",
        "confidence": "medium",
        "source_id": SRC,
        "beneficiaries": "Waitlist households",
        "stated_goal": "Grow social supply",
        "measured_outcome": "830 tenders vs 215337 waitlist; 1190 delivered provisional",
        "absurdity_score": "7.5",
        "cost_score": "4.0",
        "difficulty": "4",
        "priority_index": "5.85",
        "cut_proposal": "Binding social objective delivery FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick742",
    },
    {
        "item_id": "lb_wiv_mvp_complaints_633_2025",
        "name": "MijnVerbouwPremie complaints 633 (170 grounded) 2025",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Wonen>MVP_complaints",
        "annual_cost_eur": "633",
        "total_cost_eur": "633",
        "tco_notes": "Admin quality residual; 143 grounded wrong decision class",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "MVP applicants",
        "stated_goal": "Correct premium decisions",
        "measured_outcome": "27pct grounded of receivable MVP complaints",
        "absurdity_score": "6.5",
        "cost_score": "2.0",
        "difficulty": "2",
        "priority_index": "4.85",
        "cut_proposal": "Decision-quality KPI FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick742",
    },
    {
        "item_id": "lb_dual_wiv_vmsw_swl_asymmetry",
        "name": "Dual WiV stock 179k waitlist 215k vacancy 10.5% vs SWL 103k/50k dual VMSW 10.5bn debt",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>WiV_VMSW_SWL",
        "annual_cost_eur": "178743",
        "total_cost_eur": "178743",
        "tco_notes": "Not TE-additive; completes agency+intermediary dual residual",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE social housing dual map",
        "stated_goal": "Comparable regional social housing outcomes",
        "measured_outcome": "VL waitlist > stock; vacancy 10.5%; FS3 assign lag dual freeze elsewhere",
        "absurdity_score": "7.0",
        "cost_score": "6.0",
        "difficulty": "4",
        "priority_index": "6.30",
        "cut_proposal": "Open dual vacancy/waitlist/unit-cost dashboard",
        "status": "active",
        "struck_reason": "",
        "notes": "tick742",
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
        "title": "Wonen in Vlaanderen Jaarverslag 2025 residual dual VMSW/SWL",
        "url": URL,
        "publisher": "Agentschap Wonen in Vlaanderen",
        "accessed_date": "2026-08-02",
        "source_class": "official_annual_report",
        "notes": (
            "Strong tick742: stock 178743 (owned 166077 rented-in 12666) vacancy 10.51pct; waitlist CIR 215337 avg 5y; "
            "huursubsidie 68.5m huurpremie 63.5m; FS3 assign 761.7 on 2024 budget 2025 still 0; market finance 202.9; "
            "doorverhuur 31.3; VKF 28.99; staff 480; page " + URL_PAGE
        ),
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual WiV JV2025 residual vs VMSW/SWL/SLRB social housing tick742",
        "url": URL,
        "publisher": "DOGE synthesis WiV + VMSW + SWL",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": (
            "Strong dual not TE-additive: VL stock 178743 waitlist 215337 vacancy 10.51 vs SWL 103293/49945; "
            "VMSW debt 10.5bn FS3 870; SLRB liq 803; tick742"
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
    "gap_id": "gap_wiv_jv2025_residual_l5",
    "hierarchy_path": "Vlaanderen>Wonen>JV2025_residual_L5",
    "entity_id": "wonen_in_vlaanderen",
    "what_is_missing": (
        "Machine-readable L5: (1) structural vacancy 18793 cash cost and renovation backlog by WM; "
        "(2) CIR waitlist 215337 vintage and assign rates by province/WM; (3) FS3 2025 assign pipeline "
        "monthly into 2026 dual VMSW; (4) unit cost newbuild/renovation per dwelling dual SWL/SLRB; "
        "(5) doorverhuur 31.3m per WM and quality outcomes on 12666 rented-in; "
        "(6) final 2025 newbuild/renovation delivery counts when late data arrive"
    ),
    "why_it_matters": (
        "JV2025 fills strong stock/waitlist/subsidy aggregates but vacancy economics, dual unit costs, "
        "and FS3 delivery lag remain opaque for waste ranking"
    ),
    "priority": "8",
    "recipient_body": "Agentschap Wonen in Vlaanderen openbaarheid",
    "recipient_email": "openbaarheid@vlaanderen.be",
    "recipient_postal": "https://www.vlaanderen.be/wonen-in-vlaanderen",
    "draft_letter_path": "docs/doge/foi/drafts/gap_wiv_jv2025_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_wiv_social_stock_178743_2025|cmt_wiv_fs3_market_finance_2025|cmt_wiv_huursubsidie_huurpremie_132m_2025",
    "linked_leaderboard_id": "lb_wiv_vacancy_10_51pct_18793|lb_wiv_waitlist_215337_2025|lb_dual_wiv_vmsw_swl_asymmetry",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick742 WiV JV2025 residual dual; ready not sent; related gap_vmsw_jv2025",
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
    print("foi +gap_wiv_jv2025_residual_l5")
else:
    print("foi already exists")

rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_733":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick742 WiV JV2025 residual dual VMSW/SWL: stock 178743 waitlist 215337 vacancy 10.51; "
            "huursubsidie 68.5 huurpremie 63.5; FS3 2025 assign 0; "
            "FOI gap_wiv_jv2025_residual_l5 ready"
        )
if not any(r.get("task_id") == "rq_734" for r in rqs):
    rqs.append({
        "task_id": "rq_734",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined or Entity II dual residual "
            "or fed Pillar2/VVPR recheck if new PDF or CoA 2026_37 activiteitenverslag residual"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick742 after rq_733",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("research_queue rq_733=done rq_734=open")

ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys())
if ls:
    ls[0]["mode"] = "continuous"
    ls[0]["current_sprint"] = "hole_fill"
    ls[0]["last_tick_utc"] = UTC
    ls[0]["last_unit_id"] = "rq_733"
    ls[0]["ticks_completed"] = "742"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        "tick742 WiV JV2025 residual dual VMSW/SWL; next rq_734; "
        "progress@750 in 8; rq_116 deferred"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=742")
print("DONE tick742")

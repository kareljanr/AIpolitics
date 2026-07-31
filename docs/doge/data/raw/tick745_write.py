# tick745 — CoA federal Jaarverslag 2025 residual (2026_30) rq_736
# Primary: capacity, budget/outturn, audit volume, rec follow-up dual VL AV2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T09:45:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_30_Jaarverslag2025.pdf"
URL_LOCAL = "docs/doge/data/raw/ccrek_2026_30_jaarverslag2025.pdf"

SRC = "src_ccrek_2026_30_jv2025_residual"
SRC_DUAL = "src_dual_coa_fed_vl_recs_tick745"

# --- entity rekenhof notes ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)

updated = False
for e in ents:
    if e.get("entity_id") == "rekenhof":
        note = e.get("notes") or ""
        if "tick745" not in note:
            e["notes"] = (
                (note + " | " if note else "")
                + "tick745 JV2025 residual: budget exp 71.569m / outturn 66.133m; FTE 475 of cadre 624; "
                "recs monitor 23pct full 48pct in progress 21pct not executed dual VL 15.8pct full"
            ).strip()
            updated = True
        break
else:
    ents.append({
        "entity_id": "rekenhof",
        "name_nl": "Rekenhof",
        "name_fr": "Cour des comptes",
        "name_en": "Court of Audit",
        "level": "agency",
        "parent_id": "gg_belgium",
        "community_language": "bi",
        "website": "https://www.ccrek.be",
        "foi_email": "",
        "foi_postal": "",
        "notes": "tick745 federal JV2025 residual dual VL chamber",
    })
    updated = True

with open(ent_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=efields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(ents)
print("entities", "updated" if updated else "ok")

# --- budgets residual ---
budgets = [
    # Budget plan 2025 (kEUR table as EUR)
    ("bud_ccrek_fed_budget_exp_2025", "rekenhof", 2025, 71569300, "", "", "budgeted", SRC, "strong", "CoA JV2025 T1: expenditure budget 71.5693m 2025 (+2.90pct vs 2024); tick745"),
    ("bud_ccrek_fed_budget_receipts_2025", "rekenhof", 2025, 65298700, "", "", "budgeted", SRC, "strong", "Budget receipts 65.2987m 2025; tick745"),
    ("bud_ccrek_fed_budget_dotatie_2025", "rekenhof", 2025, 64562800, "", "", "budgeted", SRC, "strong", "Dotatie 64.5628m 2025 (after own receipts+boni reduce need); tick745"),
    ("bud_ccrek_fed_budget_own_receipts_2025", "rekenhof", 2025, 735900, "", "", "budgeted", SRC, "strong", "Own receipts estimated 735.9k 2025; tick745"),
    ("bud_ccrek_fed_budget_boni_2023_used_2025", "rekenhof", 2025, 6270600, "", "", "outturn", SRC, "strong", "2023 boni 6.2706m used to finance 2025 exp; tick745"),
    ("bud_ccrek_fed_budget_pay_2025", "rekenhof", 2025, 58602500, "", "", "budgeted", SRC, "strong", "Loonmassa budget 58.6025m 2025 (81.89pct of exp); tick745"),
    ("bud_ccrek_fed_budget_other_pay_2025", "rekenhof", 2025, 4810000, "", "", "budgeted", SRC, "strong", "Other remuneration 4.810m 2025 (6.71pct); tick745"),
    ("bud_ccrek_fed_budget_it_2025", "rekenhof", 2025, 2516000, "", "", "budgeted", SRC, "strong", "IT+office material 2.516m 2025 (+20.85pct cloud/cyber); tick745"),
    ("bud_ccrek_fed_budget_exp_2024", "rekenhof", 2024, 69550700, "", "", "budgeted", SRC, "strong", "Budget exp 69.5507m 2024 T1; tick745"),
    ("bud_ccrek_fed_budget_exp_2023", "rekenhof", 2023, 65998900, "", "", "budgeted", SRC, "strong", "Budget exp 65.9989m 2023 T1; tick745"),
    # Outturn 2025 residual
    ("bud_ccrek_fed_outturn_exp_2025", "rekenhof", 2025, 66132527.49, "", "", "outturn", SRC, "strong", "Outturn exp 66.132527m 2025 (+1.98pct / +1.28554m); tick745"),
    ("bud_ccrek_fed_outturn_receipts_2025", "rekenhof", 2025, 65304193.19, "", "", "outturn", SRC, "strong", "Outturn receipts 65.304193m 2025 (-70.87k); tick745"),
    ("bud_ccrek_fed_outturn_deficit_2025", "rekenhof", 2025, 828340, "", "", "outturn", SRC, "strong", "Budget result deficit 828.34k 2025 (vs surplus 2024); tick745"),
    ("bud_ccrek_fed_global_result_2025", "rekenhof", 2025, 5422280, "", "", "outturn", SRC, "strong", "Global result after carried boni 5.42228m eoy2025; tick745"),
    ("bud_ccrek_fed_outturn_pay_2025", "rekenhof", 2025, 55224893.73, "", "", "outturn", SRC, "strong", "Outturn loonmassa 55.224894m (83.51pct); tick745"),
    ("bud_ccrek_fed_outturn_other_pay_2025", "rekenhof", 2025, 4675937.24, "", "", "outturn", SRC, "strong", "Other remuneration outturn 4.675937m (7.07pct); tick745"),
    ("bud_ccrek_fed_outturn_ops_2025", "rekenhof", 2025, 2630362.96, "", "", "outturn", SRC, "strong", "Ops+invest outturn 2.630363m (3.98pct); tick745"),
    ("bud_ccrek_fed_outturn_it_2025", "rekenhof", 2025, 1875042.56, "", "", "outturn", SRC, "strong", "IT+office outturn 1.875043m (2.84pct); tick745"),
    ("bud_ccrek_fed_outturn_building_fee_2025", "rekenhof", 2025, 1726291.00, "", "", "outturn", SRC, "strong", "Building occupation fee 1.726291m (2.61pct); tick745"),
    ("bud_ccrek_fed_outturn_exp_2024", "rekenhof", 2024, 64846990, "", "", "outturn", SRC, "strong", "Outturn exp 64.84699m 2024; tick745"),
    ("bud_ccrek_fed_outturn_receipts_2024", "rekenhof", 2024, 65375060, "", "", "outturn", SRC, "strong", "Outturn receipts 65.37506m 2024 (dotatie 64.644m incl); tick745"),
    ("bud_ccrek_fed_outturn_surplus_2024", "rekenhof", 2024, 528070, "", "", "outturn", SRC, "strong", "Budget surplus 528.07k 2024; tick745"),
    ("bud_ccrek_fed_global_result_2024", "rekenhof", 2024, 4709240, "", "", "outturn", SRC, "strong", "Global result 4.70924m eoy2024; tick745"),
    # HR residual
    ("bud_ccrek_fed_staff_headcount_2025", "rekenhof", 2025, 514, "", "", "outturn", SRC, "strong", "Staff headcount 514 eoy2025 (454 statutory + 60 contract); tick745"),
    ("bud_ccrek_fed_staff_fte_2025", "rekenhof", 2025, 475, "", "", "outturn", SRC, "strong", "Staff FTE 475 2025; tick745"),
    ("bud_ccrek_fed_cadre_624", "rekenhof", 2025, 624, "", "", "outturn", SRC, "strong", "Personnel cadre 624 posts (equal NL/FR); tick745"),
    ("bud_ccrek_fed_occupancy_92_41pct", "rekenhof", 2025, 9241, "", "", "outturn", SRC, "strong", "Occupancy 92.41pct of cadre (FTE/cadre*100 stored as 9241 bps); tick745"),
    ("bud_ccrek_fed_hires_2025", "rekenhof", 2025, 22, "", "", "outturn", SRC, "strong", "Hires 22 in 2025; tick745"),
    ("bud_ccrek_fed_exits_2025", "rekenhof", 2025, 21, "", "", "outturn", SRC, "strong", "Exits 21 in 2025; tick745"),
    ("bud_ccrek_fed_exits_expected_to_2028", "rekenhof", 2028, 22, "", "", "projection", SRC, "strong", "Expected exits to 2028 COUNT 22; tick745"),
    ("bud_ccrek_fed_training_days_2025", "rekenhof", 2025, 2057, "", "", "outturn", SRC, "strong", "Training days 2057 in 2025 (~2/3 internal); tick745"),
    # Audit volume residual
    ("bud_ccrek_fed_budget_reports_initial_2025", "rekenhof", 2025, 15, "", "", "outturn", SRC, "strong", "Budget review reports initial budgets COUNT 15 in 2025 (was 14/18); tick745"),
    ("bud_ccrek_fed_budget_reports_prov_credits_2025", "rekenhof", 2025, 13, "", "", "outturn", SRC, "strong", "Budget reviews on provisional credits COUNT 13 in 2025 (caretaker); tick745"),
    ("bud_ccrek_fed_budget_reports_amends_2025", "rekenhof", 2025, 18, "", "", "outturn", SRC, "strong", "Budget amendment reviews COUNT 18 in 2025; tick745"),
    ("bud_ccrek_fed_rekenplichtigen_closed_2025", "rekenhof", 2025, 2277, "", "", "outturn", SRC, "strong", "Rekenplichtigen accounts closed COUNT 2277 in 2025; tick745"),
    ("bud_ccrek_fed_reken_periodiek_1860", "rekenhof", 2025, 1860, "", "", "outturn", SRC, "strong", "Periodic rekenplichtigen accounts 1860 in 2025; tick745"),
    ("bud_ccrek_fed_reken_eindebeheer_414", "rekenhof", 2025, 414, "", "", "outturn", SRC, "strong", "End-of-management accounts 414 in 2025; tick745"),
    ("bud_ccrek_fed_reken_tekort_3", "rekenhof", 2025, 3, "", "", "outturn", SRC, "strong", "Deficit accounts 3 in 2025 (was 7/17); tick745"),
    ("bud_ccrek_fed_oisz_agency_certs_370", "rekenhof", 2025, 370, "", "", "outturn", SRC, "strong", "OISZ/agency/DAB accounts certified or checked COUNT 370 in 2025; tick745"),
    ("bud_ccrek_fed_agency_certs_2024_accounts_350", "rekenhof", 2025, 350, "", "", "outturn", SRC, "strong", "Of which 2024-year accounts 350; tick745"),
    ("bud_ccrek_fed_oisz_officieuze_16", "rekenhof", 2025, 16, "", "", "outturn", SRC, "strong", "Officieuze OISZ accounts checked but not yet formally submitted COUNT 16; tick745"),
    ("bud_ccrek_fed_thematic_reports_29_2025", "rekenhof", 2025, 29, "", "", "outturn", SRC, "strong", "Thematic audit reports COUNT 29 in 2025 (was 41/31); tick745"),
    ("bud_ccrek_fed_thematic_articles_8_2025", "rekenhof", 2025, 8, "", "", "outturn", SRC, "strong", "Thematic articles in Boeken COUNT 8 in 2025; tick745"),
    ("bud_ccrek_fed_thematic_products_37_2025", "rekenhof", 2025, 37, "", "", "outturn", SRC, "strong", "Thematic products 37 in 2025 incl 19 follow-ups; tick745"),
    ("bud_ccrek_fed_thematic_followups_19_2025", "rekenhof", 2025, 19, "", "", "outturn", SRC, "strong", "Follow-up audits COUNT 19 of 37 thematic products 2025; tick745"),
    # Mandates residual
    ("bud_ccrek_fed_mandatenlijsten_10972", "rekenhof", 2025, 10972, "", "", "outturn", SRC, "strong", "Mandates lists filed COUNT 10972 for year 2024; tick745"),
    ("bud_ccrek_fed_vermogens_5980", "rekenhof", 2025, 5980, "", "", "outturn", SRC, "strong", "Asset declarations filed COUNT 5980; tick745"),
    ("bud_ccrek_fed_mandate_fines_77", "rekenhof", 2025, 77, "", "", "outturn", SRC, "strong", "Definitive administrative fines COUNT 77 for declaration year 2024; tick745"),
    ("bud_ccrek_fed_no_asset_decl_16", "rekenhof", 2025, 16, "", "", "outturn", SRC, "strong", "Persons with no asset declaration COUNT 16; tick745"),
    ("bud_ccrek_fed_no_either_decl_15", "rekenhof", 2025, 15, "", "", "outturn", SRC, "strong", "Persons with neither mandates nor asset list COUNT 15; tick745"),
    # Judicial residual
    ("bud_ccrek_fed_niet_dagvaarding_n_8_2025", "rekenhof", 2025, 8, "", "", "outturn", SRC, "strong", "Non-summons decisions COUNT 8 in 2025; tick745"),
    ("bud_ccrek_fed_niet_dagvaarding_eur_185636", "rekenhof", 2025, 185636.94, "", "", "outturn", SRC, "strong", "Non-summons amounts 700+184936.94=185636.94 EUR 2025 T8; tick745"),
    ("bud_ccrek_fed_veroordelingen_0_2025", "rekenhof", 2025, 0, "", "", "outturn", SRC, "strong", "Convictions COUNT 0 / 0 EUR in 2025 (also 0 in 2023-24); tick745"),
    ("bud_ccrek_fed_kwijting_5y_n_5", "rekenhof", 2025, 5, "", "", "outturn", SRC, "strong", "Automatic discharges after 5 years COUNT 5 in 2025; tick745"),
    ("bud_ccrek_fed_kwijting_5y_eur_2_876m", "rekenhof", 2025, 2876269.11, "", "", "outturn", SRC, "strong", "Automatic discharge amounts 2.876269m EUR 2025; tick745"),
    # Parliament residual
    ("bud_ccrek_fed_bill_advice_42_2025", "rekenhof", 2025, 42, "", "", "outturn", SRC, "strong", "Financial-impact advice on bills/decrees COUNT 42 in 2025; tick745"),
    ("bud_ccrek_fed_mp_inzage_25_2025", "rekenhof", 2025, 25, "", "", "outturn", SRC, "strong", "MP individual access answers COUNT 25 to 21 MPs in 2025; tick745"),
    ("bud_ccrek_fed_exec_advice_recv_8", "rekenhof", 2025, 8, "", "", "outturn", SRC, "strong", "Executive advice requests received COUNT 8 in 2025; tick745"),
    ("bud_ccrek_fed_exec_advice_admissible_6", "rekenhof", 2025, 6, "", "", "outturn", SRC, "strong", "Admissible executive advice COUNT 6 (fed2 BRU3 DG1); tick745"),
    # Rec follow-up residual (monitor multi-entity)
    ("bud_ccrek_fed_recs_full_or_partial_71pct", "rekenhof", 2025, 71, "", "", "outturn", SRC, "strong", "Recs fully or partially followed 71pct (monitor); tick745"),
    ("bud_ccrek_fed_recs_full_23pct", "rekenhof", 2025, 23, "", "", "outturn", SRC, "strong", "Recs fully executed 23pct; tick745"),
    ("bud_ccrek_fed_recs_in_progress_48pct", "rekenhof", 2025, 48, "", "", "outturn", SRC, "strong", "Recs in progress 48pct; tick745"),
    ("bud_ccrek_fed_recs_not_executed_21pct", "rekenhof", 2025, 21, "", "", "outturn", SRC, "strong", "Recs not executed 21pct; tick745"),
    ("bud_ccrek_fed_recs_not_assessed_8pct", "rekenhof", 2025, 8, "", "", "outturn", SRC, "strong", "Recs not assessed by CoA 8pct; tick745"),
    # Dual residual vs VL
    ("bud_dual_coa_fed_full_23pct_vs_vl_15_8pct", "gg_belgium", 2025, 23, "", "", "outturn", SRC_DUAL, "strong", "Fed multi-entity monitor full-exec 23pct vs VL thematic full 15.8pct dual residual; tick745"),
    ("bud_dual_coa_fed_not_exec_21pct_vs_vl_dead", "gg_belgium", 2025, 21, "", "", "outturn", SRC_DUAL, "strong", "Fed not-executed 21pct dual VL no-action 14.2pct + intention 19pct class; tick745"),
    ("bud_dual_coa_capacity_fed_475_vs_vl_58_5", "gg_belgium", 2025, 475, "", "", "outturn", SRC_DUAL, "strong", "Fed CoA FTE 475 vs VL chamber VG-level 58.5 dual capacity map; tick745"),
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
        "commitment_id": "cmt_ccrek_fed_budget_71_6m_2025",
        "title": "Federal CoA budget 71.569m 2025 / outturn exp 66.133m / deficit 0.828m",
        "entity_id": "rekenhof",
        "beneficiary": "Parliament oversight of GG",
        "legal_basis": "Inrichtingswet Rekenhof art20bis + JV2025",
        "decision_date": "2026-06-24",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "71569300",
        "cash_by_year": '{"budget_exp_m":71.569,"outturn_exp_m":66.133,"dotatie_m":64.563,"own_receipts_k":735.9,"boni_used_m":6.271,"deficit_k":828.34,"global_result_m":5.422,"pay_share_pct":83.51}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Independent supreme audit institution capacity",
        "cut_option": "Core oversight — not cut target; publish dual VL capacity FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Federal>Rekenhof>budget_2025",
        "notes": "tick745",
    },
    {
        "commitment_id": "cmt_ccrek_fed_recs_monitor_71pct",
        "title": "CoA multi-entity rec monitor: 23% full / 48% in progress / 21% not executed / 8% not assessed",
        "entity_id": "rekenhof",
        "beneficiary": "Citizens via audit impact",
        "legal_basis": "ISSAI/INTOSAI P-12 + Monitor since Jun2023",
        "decision_date": "2026-06-24",
        "start_year": "2020",
        "end_year": "2025",
        "total_envelope_eur": "",
        "cash_by_year": '{"full_or_partial_pct":71,"full_pct":23,"in_progress_pct":48,"not_executed_pct":21,"not_assessed_pct":8,"followup_window_y":"2-5","update":"6-monthly"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://monitor.ccrek.be",
        "stated_goal": "Ensure recommendations produce real impact",
        "cut_option": "Cash-impact of open recs FOI dual VL 15.8pct full",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Federal>Rekenhof>recs_monitor",
        "notes": "tick745 multi-entity perimeter not identical to VL AV453",
    },
    {
        "commitment_id": "cmt_ccrek_fed_audit_volume_2025",
        "title": "CoA 2025 audit volume: 2277 rekenplichtigen / 370 agency certs / 37 thematic / 19 follow-ups",
        "entity_id": "rekenhof",
        "beneficiary": "Parliaments multi-level",
        "legal_basis": "JV2025 ch3 controls",
        "decision_date": "2026-06-24",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "",
        "cash_by_year": '{"rekenplichtigen_n":2277,"agency_certs_n":370,"thematic_products_n":37,"followups_n":19,"budget_reviews_initial_n":15,"bill_advice_n":42}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Full-spectrum public finance control",
        "cut_option": "Map open thematic recs to € programmes FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Federal>Rekenhof>audit_volume_2025",
        "notes": "tick745",
    },
    {
        "commitment_id": "cmt_ccrek_fed_capacity_475_fte",
        "title": "Federal CoA capacity 475 FTE / 514 headcount / cadre 624 (92.41% occupancy)",
        "entity_id": "rekenhof",
        "beneficiary": "Oversight of multi-level GG",
        "legal_basis": "JV2025 §1.3.1 HR",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2028",
        "total_envelope_eur": "475",
        "cash_by_year": '{"fte":475,"headcount":514,"cadre":624,"occupancy_pct":92.41,"hires":22,"exits":21,"exits_to_2028":22,"training_days":2057}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Adequate SAI staffing for BE public finance",
        "cut_option": "Capacity vs TE coverage dual VL FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Federal>Rekenhof>capacity",
        "notes": "tick745 amount is FTE",
    },
    {
        "commitment_id": "cmt_ccrek_fed_kwijting_2_876m_2025",
        "title": "Automatic 5-year discharges of accounting deficits 2.876m EUR (5 cases) 2025",
        "entity_id": "rekenhof",
        "beneficiary": "Rekenplichtigen / lost recovery path",
        "legal_basis": "Judicial competence after 5 years without summons",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "2876269.11",
        "cash_by_year": '{"n":5,"eur":2876269.11,"convictions_n":0,"non_summons_n":8,"non_summons_eur":185636.94}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Accountability of public accountants for deficits",
        "cut_option": "Faster ministerial summons FOI; name large discharges",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Federal>Rekenhof>judicial_kwijting",
        "notes": "tick745 residual waste-adjacent governance",
    },
    {
        "commitment_id": "cmt_dual_coa_fed_vl_recs_tick745",
        "title": "Dual CoA rec follow-through: fed monitor 23% full vs VL thematic 15.8% full",
        "entity_id": "gg_belgium",
        "beneficiary": "BE accountability dual map",
        "legal_basis": "CoA JV2025 ch4 + VL AV2025 residual tick743",
        "decision_date": "2026-06-24",
        "start_year": "2018",
        "end_year": "2025",
        "total_envelope_eur": "",
        "cash_by_year": '{"fed_full_pct":23,"fed_in_progress_pct":48,"fed_not_exec_pct":21,"vl_full_pct":15.8,"vl_no_action_pct":14.2,"vl_intention_pct":19,"note":"perimeters differ; not TE euros"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://monitor.ccrek.be",
        "stated_goal": "Comparable audit follow-through multi-level",
        "cut_option": "Unified open-rec cash dashboard FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>CoA_recs_fed_vl",
        "notes": "tick745",
    },
]

cmt_path = DATA / "commitments.csv"
with open(cmt_path, encoding="utf-8", newline="") as f:
    cr = csv.DictReader(f)
    cfields = cr.fieldnames
    existing_c = {r["commitment_id"] for r in cr}
added_c = 0
with open(cmt_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cfields, lineterminator="\n")
    for row in commitments:
        if row["commitment_id"] in existing_c:
            continue
        w.writerow(row)
        added_c += 1
print(f"commitments +{added_c}")

leaderboard = [
    {
        "item_id": "lb_ccrek_fed_recs_not_executed_21pct",
        "name": "Federal CoA multi-entity recs 21% not executed (monitor)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Federal>Rekenhof>recs_not_executed",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "JV2025: 21% not executed + 8% not assessed; only 23% fully done; dual VL 15.8% full",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Unfixed audit findings across BE",
        "stated_goal": "Implement CoA recommendations",
        "measured_outcome": "23% full / 48% in progress / 21% none / 8% not assessed",
        "absurdity_score": "7.5",
        "cost_score": "4.0",
        "difficulty": "3",
        "priority_index": "5.95",
        "cut_proposal": "Open-rec cash map + parliamentary follow-up FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick745 euro Unknown — FOI",
    },
    {
        "item_id": "lb_ccrek_fed_kwijting_2_876m",
        "name": "Automatic 5y accounting-deficit discharges €2.876m (5 cases) 2025",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Federal>Rekenhof>kwijting_5y",
        "annual_cost_eur": "2876269",
        "total_cost_eur": "2876269",
        "tco_notes": "Strong JV2025 T8: 5 automatic discharges after 5y without summons; 0 convictions 2023-25",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Rekenplichtigen escaping recovery",
        "stated_goal": "Recover public accountant deficits",
        "measured_outcome": "€2.876m discharged; 0 convictions",
        "absurdity_score": "8.0",
        "cost_score": "4.5",
        "difficulty": "3",
        "priority_index": "6.25",
        "cut_proposal": "Faster ministerial summons; publish named large cases FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick745",
    },
    {
        "item_id": "lb_ccrek_fed_recs_full_only_23pct",
        "name": "CoA multi-entity recs fully executed only 23% (monitor)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Federal>Rekenhof>recs_full_23pct",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "71% full or partial; still only 23% complete; dual VL 15.8%",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Taxpayers via slow fix of waste findings",
        "stated_goal": "Full implementation of audit recs",
        "measured_outcome": "23% full; 48% in progress",
        "absurdity_score": "7.0",
        "cost_score": "3.5",
        "difficulty": "3",
        "priority_index": "5.55",
        "cut_proposal": "Deadlines + public rec dashboard FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick745",
    },
    {
        "item_id": "lb_ccrek_fed_mandate_noncompliance",
        "name": "Mandate/asset declaration gaps: 77 fines + 31 non-filers (2024 year)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Federal>Rekenhof>mandaten",
        "annual_cost_eur": "77",
        "total_cost_eur": "77",
        "tco_notes": "10972 mandate lists / 5980 asset decls; 16 no asset + 15 neither; 77 definitive fines",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Integrity transparency users",
        "stated_goal": "Full declaration compliance of mandatarissen",
        "measured_outcome": "31 non-filers class + 77 fines",
        "absurdity_score": "6.0",
        "cost_score": "2.5",
        "difficulty": "2",
        "priority_index": "4.40",
        "cut_proposal": "Name non-filers already public; fine revenue FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick745 amount is fine COUNT",
    },
    {
        "item_id": "lb_ccrek_fed_oisz_officieuze_16",
        "name": "16 OISZ accounts still officieus (not formally submitted to CoA) 2025",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Federal>SS>OISZ>accounts_lag",
        "annual_cost_eur": "16",
        "total_cost_eur": "16",
        "tco_notes": "Approved by boards but not yet officially filed with CoA — formal certification blocked",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "SS institutions delaying formal control",
        "stated_goal": "Timely formal submission of OISZ accounts",
        "measured_outcome": "16 officieuze accounts checked informally only",
        "absurdity_score": "6.5",
        "cost_score": "3.0",
        "difficulty": "2",
        "priority_index": "4.85",
        "cut_proposal": "Name the 16 OISZ + submission deadlines FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick745 COUNT",
    },
    {
        "item_id": "lb_dual_coa_fed_vl_recs_gap",
        "name": "Dual CoA rec full-impl gap: fed monitor 23% vs VL thematic 15.8%",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>CoA_recs_fed_vl",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "Not TE; perimeter differs; both show weak full implementation dual capacity 475 vs 58.5 FTE",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE accountability dual map",
        "stated_goal": "Comparable multi-level audit follow-through",
        "measured_outcome": "Fed 23% full; VL 15.8% full; both large residual not-done",
        "absurdity_score": "7.5",
        "cost_score": "3.5",
        "difficulty": "3",
        "priority_index": "5.80",
        "cut_proposal": "Unified open-rec cash dashboard FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick745",
    },
    {
        "item_id": "lb_ccrek_fed_budget_deficit_828k",
        "name": "CoA own 2025 budget deficit €828k (first after surplus years)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Federal>Rekenhof>own_deficit_2025",
        "annual_cost_eur": "828340",
        "total_cost_eur": "828340",
        "tco_notes": "Not waste of GG TE; small own deficit covered by prior boni; global result still +5.4m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "CoA operations",
        "stated_goal": "Balanced CoA budget execution",
        "measured_outcome": "Deficit 828k; global still positive 5.4m",
        "absurdity_score": "3.0",
        "cost_score": "2.0",
        "difficulty": "2",
        "priority_index": "2.60",
        "cut_proposal": "Track dotatie freeze path dual Kamer peer",
        "status": "active",
        "struck_reason": "",
        "notes": "tick745 low-priority own-ops residual",
    },
]

lb_path = DATA / "leaderboard.csv"
with open(lb_path, encoding="utf-8", newline="") as f:
    lr = csv.DictReader(f)
    lfields = lr.fieldnames
    existing_l = {r["item_id"] for r in lr}
added_l = 0
with open(lb_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lfields, lineterminator="\n")
    for row in leaderboard:
        if row["item_id"] in existing_l:
            continue
        w.writerow(row)
        added_l += 1
print(f"leaderboard +{added_l}")

sources = [
    {
        "source_id": SRC,
        "title": "Rekenhof Jaarverslag 2025 residual L5 tick745 (budget capacity recs dual)",
        "url": URL,
        "publisher": "Rekenhof / Cour des comptes",
        "accessed_date": "2026-08-02",
        "source_class": "court_of_audit",
        "notes": "Strong tick745: AG 24 Jun 2026; budget exp 71.569m outturn 66.133m deficit 828k global 5.422m; FTE 475 cadre 624 92.41pct; rekenplichtigen 2277; agency certs 370; thematic 37/19 followups; recs full 23 in progress 48 not exec 21 not assessed 8; kwijting 2.876m n5; mandaten 10972 fines 77; raw ccrek_2026_30",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual CoA fed JV2025 vs VL AV2025 rec implementation tick745",
        "url": URL,
        "publisher": "DOGE synthesis CoA federal + VL chamber",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": "Strong dual not TE: fed monitor full 23pct vs VL thematic full 15.8pct; fed not-exec 21pct dual VL dead class; capacity 475 vs 58.5 FTE; tick745",
    },
]
src_path = DATA / "sources.csv"
with open(src_path, encoding="utf-8", newline="") as f:
    sr = csv.DictReader(f)
    sfields = sr.fieldnames
    existing_s = {r["source_id"] for r in sr}
added_s = 0
with open(src_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, lineterminator="\n")
    for row in sources:
        if row["source_id"] in existing_s:
            continue
        w.writerow(row)
        added_s += 1
print(f"sources +{added_s}")

foi_row = {
    "gap_id": "gap_ccrek_fed_jv2025_residual_l5",
    "hierarchy_path": "Federal>Rekenhof>JV2025_residual_L5",
    "entity_id": "rekenhof",
    "what_is_missing": "Machine-readable L5: (1) full monitor export of recs with full/in-progress/not-executed status and linked € programmes multi-entity; (2) names and amounts of the 5 automatic 5y discharges (2.876m) and 8 non-summons cases; (3) list of 16 officieuze OISZ accounts not yet formally submitted; (4) dual VL/fed rec full-impl gap root causes; (5) fine revenue from 77 mandate fines; (6) capacity FTE by chamber/sector vs TE coverage",
    "why_it_matters": "JV2025 shows only 23% full rec execution multi-entity and €2.876m automatic deficit discharges — cash-linked open recs and recovery failures remain opaque for waste ranking",
    "priority": "8",
    "recipient_body": "Rekenhof / Cour des comptes / Kamer Comptabiliteit",
    "recipient_email": "info@ccrek.be",
    "recipient_postal": "https://www.ccrek.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_ccrek_fed_jv2025_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_ccrek_fed_recs_monitor_71pct|cmt_ccrek_fed_kwijting_2_876m_2025|cmt_dual_coa_fed_vl_recs_tick745",
    "linked_leaderboard_id": "lb_ccrek_fed_kwijting_2_876m|lb_ccrek_fed_recs_not_executed_21pct|lb_dual_coa_fed_vl_recs_gap",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick745 CoA federal JV2025 residual dual VL; ready not sent; related gap_ccrek_av2025_recs_impl_l5",
}
foi_path = DATA / "foi_queue.csv"
with open(foi_path, encoding="utf-8", newline="") as f:
    fr = csv.DictReader(f)
    ffields = fr.fieldnames
    existing_f = {r["gap_id"] for r in fr}
if foi_row["gap_id"] not in existing_f:
    with open(foi_path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ffields, lineterminator="\n")
        w.writerow(foi_row)
    print("foi +1")
else:
    print("foi exists")

# research_queue
rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)

for r in rqs:
    if r.get("task_id") == "rq_736":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick745 CoA fed JV2025 residual: budget 71.569m outturn 66.133m FTE 475; "
            "recs full 23pct in progress 48 not exec 21; kwijting 2.876m; dual VL 15.8pct; "
            "FOI gap_ccrek_fed_jv2025_residual_l5 ready"
        )

if not any(r.get("task_id") == "rq_737" for r in rqs):
    rqs.append({
        "task_id": "rq_737",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined (prefer CoA 2026_24 prisons DBFM follow-up residual "
            "if new lines vs tick491, or Entity II dual residual) or fed Pillar2/VVPR recheck if new PDF"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick745 after rq_736",
    })

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rqs)
print("research_queue rq_736=done rq_737 open")

# loop_state
ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys()) if ls else [
        "state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id",
        "ticks_completed", "paused", "notes",
    ]
row = ls[0] if ls else {k: "" for k in lsfields}
row.update({
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_736",
    "ticks_completed": "745",
    "paused": "no",
    "notes": "tick745 CoA fed JV2025 residual recs/kwijting dual VL; next rq_737; progress@750 in 5; rq_116 deferred",
})
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerow(row)
print("loop_state -> 745")
print("DONE tick745")

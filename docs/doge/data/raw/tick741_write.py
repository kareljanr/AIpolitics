# tick741 — VMSW Jaarverslag + Jaarrekening 2025 residual dual SWL/SLRB/FLRBC (rq_732)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T07:45:00Z"
URL_JV = "https://publicaties.vlaanderen.be/view-file/84300"
URL_JR = "https://publicaties.vlaanderen.be/view-file/84301"
URL_PAGE = "https://www.vlaanderen.be/publicaties/jaarverslag-vlaamse-maatschappij-voor-sociaal-wonen-vmsw"

SRC = "src_vmsw_jv2025_residual"
SRC_JR = "src_vmsw_jr2025"
SRC_DUAL = "src_dual_vmsw_swl_slrb_flrbc_tick741"

# --- entity ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)
for e in ents:
    if e.get("entity_id") == "vmsw":
        e["notes"] = (
            "tick741 JV/JR2025 residual: FS3 870m/yr (2024 assign 761.7 87.55pct; 2025 assign 0 still open); "
            "BS assets 12.383bn debt 10.499bn LT fin 9.186bn; loan 1bn @0pct VL 2025; RC WM 589.4m; "
            "SSI 40.3m 75pct; dual SWL/SLRB/FLRBC"
        )
        e["website"] = "https://www.vlaanderen.be/publicaties/jaarverslag-vlaamse-maatschappij-voor-sociaal-wonen-vmsw"
with open(ent_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=efields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for e in ents:
        w.writerow({k: e.get(k, "") for k in efields})
print("entity vmsw notes updated")

budgets = [
    # FS3 residual
    ("bud_vmsw_fs3_budget_870m_2025", "vmsw", 2025, 870000000, "", "", "budgeted", SRC, "strong", "FS3 total annual budget 870m 2025 (NB 478.5 + RENO 391.5) same as 2024; tick741"),
    ("bud_vmsw_fs3nb_budget_478_5m_2025", "vmsw", 2025, 478500000, "", "", "budgeted", SRC, "strong", "FS3NB nieuwbouw budget 478.5m 2025; tick741"),
    ("bud_vmsw_fs3reno_budget_391_5m_2025", "vmsw", 2025, 391500000, "", "", "budgeted", SRC, "strong", "FS3RENO budget 391.5m 2025; tick741"),
    ("bud_vmsw_fs3_assigned_0_2025", "vmsw", 2025, 0, "", "", "outturn", SRC, "strong", "FS3 assigned 0 in calendar 2025 (can still assign in 2026 on 2025 budget); tick741"),
    ("bud_vmsw_fs3_budget_870m_2024", "vmsw", 2024, 870000000, "", "", "budgeted", SRC, "strong", "FS3 total budget 870m 2024; tick741"),
    ("bud_vmsw_fs3_assigned_761_701m_2024", "vmsw", 2024, 761701052.52, "", "", "outturn", SRC, "strong", "FS3 assigned 761.701m 2024 incl retro 2025 zero-rate WM formation loans (87.55pct); tick741"),
    ("bud_vmsw_fs3_underuse_108_299m_2024", "vmsw", 2024, 108298947.48, "", "", "outturn", SRC, "strong", "FS3 underuse 108.299m 2024; of which 100m reserved basiskoten 2026; effective lost 8.2m; tick741"),
    ("bud_vmsw_fs3_effective_lost_8_2m_2024", "vmsw", 2024, 8200000, "", "", "outturn", SRC, "strong", "FS3 effective lost budget 8.2m after 100m basiskoten re-auth 2026; tick741"),
    ("bud_vmsw_fs3nb_assigned_345_872m_2024", "vmsw", 2024, 345872271, "", "", "outturn", SRC, "strong", "FS3NB assigned 345.872m 2024; tick741"),
    ("bud_vmsw_fs3reno_assigned_396_312m_2024", "vmsw", 2024, 396311610.82, "", "", "outturn", SRC, "strong", "FS3RENO assigned 396.312m 2024 (over NB+RENO split via reclass); tick741"),
    # SSI residual
    ("bud_vmsw_ssi_budget_40_301m_2025", "vmsw", 2025, 40301000, "", "", "budgeted", SRC, "strong", "SSI infrastructure subsidy budget 40.301m 2025; tick741"),
    ("bud_vmsw_ssi_assigned_30_328m_2025", "vmsw", 2025, 30328023.47, "", "", "outturn", SRC, "strong", "SSI assigned 30.328m 2025 (75.25pct); tick741"),
    ("bud_vmsw_ssi_budget_43_601m_2024", "vmsw", 2024, 43601000, "", "", "budgeted", SRC, "strong", "SSI budget 43.601m 2024 100pct assigned; tick741"),
    # Ops residual
    ("bud_vmsw_loan_vl_1bn_0pct_2025", "vmsw", 2025, 1000000000, "", "", "outturn", SRC, "strong", "VMSW borrowed 1bn from Flanders at 0pct for FS3 fund 2025; tick741"),
    ("bud_vmsw_infra_subs_59_2m_2025", "vmsw", 2025, 59200000, "", "", "outturn", SRC, "strong", "Environment infrastructure subsidies assigned 59.2m 2025 (-3.5m vs 2024); tick741"),
    ("bud_vmsw_infra_tenlast_28_2m_2025", "vmsw", 2025, 28200000, "", "", "outturn", SRC, "strong", "Of infra: tenlasteneming ~28.2m 2025; tick741"),
    ("bud_vmsw_infra_dossiers_31m_2025", "vmsw", 2025, 31000000, "", "", "outturn", SRC, "strong", "Of infra: subsidy dossiers ~31m 2025; tick741"),
    ("bud_vmsw_infra_projects_tender_51_2025", "vmsw", 2025, 51, "", "", "outturn", SRC, "strong", "Road/sewer/env works projects tendered COUNT 51 covering 3336 rental + 149 sale dwellings; tick741"),
    ("bud_vmsw_infra_dwellings_rental_3336_2025", "vmsw", 2025, 3336, "", "", "outturn", SRC, "strong", "Rental dwellings in tendered infra projects 3336 COUNT 2025; tick741"),
    ("bud_vmsw_infra_projects_completed_24_2025", "vmsw", 2025, 24, "", "", "outturn", SRC, "strong", "Infra projects completed COUNT 24 2025; tick741"),
    ("bud_vmsw_wachtebeke_sale_4_353m_2025", "vmsw", 2025, 4353282.05, "", "", "outturn", SRC, "strong", "Wachtebeke stock sold to Woonpijler at outstanding debt 4.353m 31Jan2025; tick741"),
    ("bud_vmsw_budgethuren_subs_0_685m_2025", "vmsw", 2025, 684962.66, "", "", "outturn", SRC, "strong", "Budgethuren/geconventioneerd subsidies 0.685m to 20 private + 2 WM (84 social + 205 convent units); tick741"),
    ("bud_vmsw_solidarisering_6_593m_2025", "vmsw", 2025, 6592500.56, "", "", "outturn", SRC, "strong", "Solidarisering meerkost huursubsidie ingehuurde woningen 6.593m skimming 2025; tick741"),
    ("bud_vmsw_vlabinvest_loans_11_8m_2025", "vmsw", 2025, 11800000, "", "", "outturn", SRC, "strong", "New Vlabinvest zero-rate loans assigned 11.8m 2025; tick741"),
    ("bud_vmsw_basiskoten_100m_2024", "vmsw", 2024, 100000000, "", "", "outturn", SRC, "strong", "Basiskoten zero-rate loans to HE 100m for 1744 student rooms 2024; no new HE loans 2025; tick741"),
    ("bud_vmsw_basiskoten_rooms_1744_2024", "vmsw", 2024, 1744, "", "", "outturn", SRC, "strong", "Basiskoten rooms COUNT 1744 under 100m HE programme 2024; tick741"),
    # RC residual
    ("bud_vmsw_rc_total_589_425m_2025", "vmsw", 2025, 589424911.35, "", "", "outturn", SRC, "strong", "Woonmaatschappijen RC total 589.425m eoy2025 (was 654.771; -65.3m); tick741"),
    ("bud_vmsw_rc_kt_321_845m_2025", "vmsw", 2025, 321844967.55, "", "", "outturn", SRC, "strong", "RC short-term 321.845m eoy2025 (was 452.297); tick741"),
    ("bud_vmsw_rc_lt_189_646m_2025", "vmsw", 2025, 189645911.01, "", "", "outturn", SRC, "strong", "RC long-term 189.646m eoy2025 (was 140.193); tick741"),
    ("bud_vmsw_rc_herinvestering_76_032m_2025", "vmsw", 2025, 76031930.68, "", "", "outturn", SRC, "strong", "RC herinvestering sales 76.032m eoy2025 (ends Mar2026 into KT); tick741"),
    ("bud_vmsw_rc_herinvestering_wm_1_902m_2025", "vmsw", 2025, 1902102.11, "", "", "outturn", SRC, "strong", "RC herinvestering WM transfers 1.902m eoy2025; tick741"),
    # JR balance sheet residual
    ("bud_vmsw_assets_12_383bn_2025", "vmsw", 2025, 12382615326.78, "", "", "outturn", SRC_JR, "strong", "JR total assets 12.383bn eoy2025 (was 11.873); tick741"),
    ("bud_vmsw_equity_1_814bn_2025", "vmsw", 2025, 1814111427.99, "", "", "outturn", SRC_JR, "strong", "JR equity 1.814bn eoy2025 (was 1.877); tick741"),
    ("bud_vmsw_debt_total_10_499bn_2025", "vmsw", 2025, 10499249132.50, "", "", "outturn", SRC_JR, "strong", "JR total debts 10.499bn eoy2025 (was 9.926); prior CoA class 3.12bn may be subset — FOI; tick741"),
    ("bud_vmsw_lt_fin_debt_9_186bn_2025", "vmsw", 2025, 9186264727.93, "", "", "outturn", SRC_JR, "strong", "JR LT financial debt 9.186bn (banks 2.263 + other loans 6.924) eoy2025; tick741"),
    ("bud_vmsw_bank_debt_2_263bn_2025", "vmsw", 2025, 2262753568.54, "", "", "outturn", SRC_JR, "strong", "JR LT bank debt 2.263bn eoy2025; tick741"),
    ("bud_vmsw_other_lt_loans_6_924bn_2025", "vmsw", 2025, 6923511159.39, "", "", "outturn", SRC_JR, "strong", "JR other LT loans 6.924bn eoy2025 (VL 0pct path class); tick741"),
    ("bud_vmsw_lt_receivables_11_172bn_2025", "vmsw", 2025, 11171581893.64, "", "", "outturn", SRC_JR, "strong", "JR LT other receivables (loan book class) 11.172bn eoy2025; tick741"),
    ("bud_vmsw_cash_349_010m_2025", "vmsw", 2025, 349009546.52, "", "", "outturn", SRC_JR, "strong", "JR cash 349.010m eoy2025 (was 151.949); tick741"),
    ("bud_vmsw_investments_262_326m_2025", "vmsw", 2025, 262326140.06, "", "", "outturn", SRC_JR, "strong", "JR short-term investments 262.326m eoy2025 (was 321.5); tick741"),
    ("bud_vmsw_provisions_69_255m_2025", "vmsw", 2025, 69254766.29, "", "", "outturn", SRC_JR, "strong", "JR provisions+deferred tax 69.255m eoy2025; tick741"),
    ("bud_vmsw_net_profit_5_210m_2025", "vmsw", 2025, 5210442.79, "", "", "outturn", SRC_JR, "strong", "JR net profit 5.210m 2025 (GAF 21.165 + BOF -15.955); tick741"),
    ("bud_vmsw_gaf_result_21_165m_2025", "vmsw", 2025, 21165212.47, "", "", "outturn", SRC_JR, "strong", "GAF autonomous fund result 21.165m 2025; tick741"),
    ("bud_vmsw_bof_result_minus_15_955m_2025", "vmsw", 2025, -15954769.68, "", "", "outturn", SRC_JR, "strong", "BOF result after VL toelage floor -15.955m (FS3 Huur -16m path) 2025; tick741"),
    ("bud_vmsw_op_loss_8_093m_2025", "vmsw", 2025, -8092726.57, "", "", "outturn", SRC_JR, "strong", "Operating loss -8.093m 2025 (costs covered via fin income); tick741"),
    ("bud_vmsw_fin_income_363_616m_2025", "vmsw", 2025, 363616395.81, "", "", "outturn", SRC_JR, "strong", "Financial income 363.616m 2025; tick741"),
    ("bud_vmsw_fin_costs_353_713m_2025", "vmsw", 2025, 353712671.51, "", "", "outturn", SRC_JR, "strong", "Financial costs 353.713m (debt costs 333.339m) 2025; tick741"),
    ("bud_vmsw_debt_costs_333_339m_2025", "vmsw", 2025, 333338895.19, "", "", "outturn", SRC_JR, "strong", "Debt interest costs 333.339m 2025; tick741"),
    # Dual residual
    ("bud_dual_vmsw_assets_12_383bn_vs_housing_2025", "gg_belgium", 2025, 12382615326.78, "", "", "outturn", SRC_DUAL, "strong", "VMSW assets 12.383bn dual VWF 10.003 SWL 3.509 SLRB 2.370 FLRBC 2.128; not TE-additive; tick741"),
    ("bud_dual_vmsw_debt_10_499bn_vs_housing", "gg_belgium", 2025, 10499249132.50, "", "", "outturn", SRC_DUAL, "strong", "VMSW debt 10.499bn dual VWF 9.730 SWL 2.742 FLRBC 1.603 SLRB 1.672; tick741"),
    ("bud_dual_vmsw_fs3_870m_vs_swl_works", "gg_belgium", 2025, 870000000, "", "", "budgeted", SRC_DUAL, "strong", "VMSW FS3 870m/yr dual SWL works 364.3 / SLRB liq 803 / FLRBC invest power 143; tick741"),
    ("bud_dual_vmsw_fs3_underuse_108m_2024", "gg_belgium", 2024, 108298947.48, "", "", "outturn", SRC_DUAL, "strong", "VMSW FS3 underuse 108.3m (effective lost 8.2 after basiskoten reauth) dual delivery lag SWL plan reno; tick741"),
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
        "commitment_id": "cmt_vmsw_fs3_870m_2025",
        "title": "VMSW FS3 subsidised finance budget 870m/yr (2025 assign still open)",
        "entity_id": "vmsw",
        "beneficiary": "Woonmaatschappijen social rental projects",
        "legal_basis": "VMSW JV2025 + Vlaamse Codex Wonen art 4.13",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "870000000",
        "cash_by_year": '{"budget_m":870,"nb_m":478.5,"reno_m":391.5,"assigned_2025_m":0,"note":"2025 budget can still be assigned in calendar 2026; FS4 -2pct replaces FS3 -1pct from 2026 reform"}',
        "remaining_eur": "870000000",
        "status": "active",
        "evaluation_url": URL_JV,
        "stated_goal": "Subsidised finance for social housing projects",
        "cut_option": "FS3 underuse path + FS4 transition FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VMSW>FS3",
        "notes": "tick741",
    },
    {
        "commitment_id": "cmt_vmsw_fs3_underuse_108m_2024",
        "title": "FS3 2024 underuse 108.3m (effective lost 8.2m after 100m basiskoten reauth)",
        "entity_id": "vmsw",
        "beneficiary": "Unused social-housing finance capacity",
        "legal_basis": "VMSW JV2025 financing residual",
        "decision_date": "2026-01-01",
        "start_year": "2024",
        "end_year": "2026",
        "total_envelope_eur": "108298947.48",
        "cash_by_year": '{"underuse_m":108.299,"assigned_m":761.701,"util_pct":87.55,"basiskoten_reauth_m":100,"effective_lost_m":8.2}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_JV,
        "stated_goal": "Full use of FS3 annual envelope",
        "cut_option": "Delivery acceleration dual SWL plan reno lag FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VMSW>FS3_underuse",
        "notes": "tick741",
    },
    {
        "commitment_id": "cmt_vmsw_loan_1bn_0pct_2025",
        "title": "VMSW 1bn 0pct loan from Flanders for FS3 fund 2025",
        "entity_id": "vmsw",
        "beneficiary": "FS3 loan book / woonmaatschappijen",
        "legal_basis": "VMSW JV2025 beleggingen en financieringen",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1000000000",
        "cash_by_year": '{"loan_m":1000,"rate_pct":0,"lender":"Vlaanderen"}',
        "remaining_eur": "1000000000",
        "status": "active",
        "evaluation_url": URL_JV,
        "stated_goal": "Fund FS3 at zero cost to VMSW",
        "cut_option": "Opportunity cost of 0pct VL funding FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VMSW>VL_loan",
        "notes": "tick741",
    },
    {
        "commitment_id": "cmt_vmsw_bs_12_383bn_2025",
        "title": "VMSW balance sheet assets 12.383bn / debts 10.499bn eoy2025",
        "entity_id": "vmsw",
        "beneficiary": "Flanders social housing finance stack",
        "legal_basis": "VMSW Jaarrekening 2025",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "12382615326.78",
        "cash_by_year": '{"assets_m":12382.6,"debt_m":10499.2,"lt_fin_m":9186.3,"lt_recv_m":11171.6,"equity_m":1814.1,"cash_m":349.0,"fin_costs_m":353.7,"debt_costs_m":333.3,"net_profit_m":5.21}',
        "remaining_eur": "10499249132.50",
        "status": "active",
        "evaluation_url": URL_JR,
        "stated_goal": "Intermediary financing of social housing",
        "cut_option": "Reconcile JR 10.5bn debt vs prior CoA 3.12bn class FOI",
        "source_id": SRC_JR,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VMSW>balance_sheet",
        "notes": "tick741",
    },
    {
        "commitment_id": "cmt_vmsw_rc_wm_589m_2025",
        "title": "Woonmaatschappijen rekening-courant pool 589.4m eoy2025",
        "entity_id": "vmsw",
        "beneficiary": "Woonmaatschappijen cash management",
        "legal_basis": "VMSW JV2025 RC residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "589424911.35",
        "cash_by_year": '{"total_m":589.4,"kt_m":321.8,"lt_m":189.6,"herinvestering_m":76.0,"herinvestering_wm_m":1.9,"path_m":-65.3}',
        "remaining_eur": "589424911.35",
        "status": "active",
        "evaluation_url": URL_JV,
        "stated_goal": "Centralise non-operating cash of social housing companies",
        "cut_option": "RC LT vs invest opportunity FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VMSW>RC",
        "notes": "tick741",
    },
    {
        "commitment_id": "cmt_dual_vmsw_swl_slrb_flrbc_tick741",
        "title": "Dual VMSW JV/JR2025 residual vs SWL/SLRB/FLRBC social housing finance",
        "entity_id": "gg_belgium",
        "beneficiary": "BE social housing dual map",
        "legal_basis": "VMSW 2025 + prior duals ticks 735-739",
        "decision_date": "2026-06-18",
        "start_year": "2024",
        "end_year": "2025",
        "total_envelope_eur": "12382615326.78",
        "cash_by_year": '{"vmsw_assets_m":12383,"vmsw_debt_m":10499,"vmsw_fs3_m":870,"swl_debt_m":2742,"swl_works_m":364.3,"slrb_debt_m":1672,"slrb_liq_m":802.7,"flrbc_encours_m":1607,"note":"not TE-additive dual housing OIPs"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_JV,
        "stated_goal": "Comparable regional social housing finance",
        "cut_option": "Open dual unit-cost + underuse + NPL dashboard FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>VMSW_SWL_SLRB_FLRBC",
        "notes": "tick741 completes housing OIP residual wave",
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
        "item_id": "lb_vmsw_debt_10_499bn_2025",
        "name": "VMSW BS total debts 10.499bn eoy2025 (largest BE social-housing intermediary)",
        "level": "L5",
        "type": "stock",
        "hierarchy_path": "Vlaanderen>VMSW>debt",
        "annual_cost_eur": "10499249132.50",
        "total_cost_eur": "10499249132.50",
        "tco_notes": "Stock; debt costs 333.3m/yr; prior CoA class 3.12bn may be Maastricht subset — FOI",
        "confidence": "strong",
        "source_id": SRC_JR,
        "beneficiaries": "Woonmaatschappijen via FS3/SSI loan book",
        "stated_goal": "Intermediary financing of social housing",
        "measured_outcome": "Assets 12.383bn; LT fin 9.186bn; net profit 5.2m",
        "absurdity_score": "5.5",
        "cost_score": "9.5",
        "difficulty": "4",
        "priority_index": "7.05",
        "cut_proposal": "Publish debt composition dual CoA 3.12bn FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick741 stock filter often",
    },
    {
        "item_id": "lb_vmsw_fs3_underuse_108m_2024",
        "name": "FS3 2024 underuse 108.3m (only 8.2m truly lost after basiskoten reauth)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Vlaanderen>VMSW>FS3_underuse",
        "annual_cost_eur": "108298947.48",
        "total_cost_eur": "108298947.48",
        "tco_notes": "87.55pct util; 100m reallocated basiskoten; dual SWL plan reno delivery lag",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Unused social housing project finance",
        "stated_goal": "Full FS3 annual envelope use",
        "measured_outcome": "Assigned 761.7 of 870; 2025 assign still 0",
        "absurdity_score": "7.0",
        "cost_score": "7.5",
        "difficulty": "3",
        "priority_index": "6.95",
        "cut_proposal": "FS4 transition + project pipeline FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick741",
    },
    {
        "item_id": "lb_vmsw_fs3_870m_2025_zero_assign",
        "name": "FS3 870m 2025 budget still 0 assigned by eoy (open into 2026)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Vlaanderen>VMSW>FS3_2025",
        "annual_cost_eur": "870000000",
        "total_cost_eur": "870000000",
        "tco_notes": "Calendar assign lag structural; SSI only 75pct of 40.3m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Future WM project assignees",
        "stated_goal": "Annual FS3 invest programme",
        "measured_outcome": "0% FS3 assign eoy2025; SSI 75.25%",
        "absurdity_score": "6.5",
        "cost_score": "8.0",
        "difficulty": "3",
        "priority_index": "6.95",
        "cut_proposal": "Monthly assign dashboard FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick741",
    },
    {
        "item_id": "lb_vmsw_debt_costs_333m_2025",
        "name": "VMSW debt interest costs 333.3m 2025 on 10.5bn book",
        "level": "L5",
        "type": "overhead",
        "hierarchy_path": "Vlaanderen>VMSW>fin_costs",
        "annual_cost_eur": "333338895.19",
        "total_cost_eur": "333338895.19",
        "tco_notes": "Fin income 363.6m covers ops; 0pct VL 1bn loan reduces average cost",
        "confidence": "strong",
        "source_id": SRC_JR,
        "beneficiaries": "Intermediated via FS3 loan book",
        "stated_goal": "Service intermediary debt",
        "measured_outcome": "Net fin positive; op loss -8.1m covered by GAF",
        "absurdity_score": "5.5",
        "cost_score": "7.5",
        "difficulty": "3",
        "priority_index": "6.30",
        "cut_proposal": "Interest path transparency FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick741",
    },
    {
        "item_id": "lb_vmsw_loan_1bn_0pct_2025",
        "name": "VMSW 1bn 0pct loan from Flanders 2025 (opportunity-cost residual)",
        "level": "L5",
        "type": "funding",
        "hierarchy_path": "Vlaanderen>VMSW>VL_0pct",
        "annual_cost_eur": "1000000000",
        "total_cost_eur": "1000000000",
        "tco_notes": "Stock funding; opportunity cost at VL funding rate not published",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "FS3 fund",
        "stated_goal": "Cheap fund social housing loans",
        "measured_outcome": "1bn @0pct; dual VWF bonds @4.21pct asymmetry",
        "absurdity_score": "6.0",
        "cost_score": "8.5",
        "difficulty": "3",
        "priority_index": "6.90",
        "cut_proposal": "Publish opportunity cost vs market FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick741",
    },
    {
        "item_id": "lb_vmsw_bof_floor_minus_16m",
        "name": "BOF result floored at -16m via VL toelage (structural soft budget)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Vlaanderen>VMSW>BOF",
        "annual_cost_eur": "16000000",
        "total_cost_eur": "16000000",
        "tco_notes": "From 2023 VL tops up BOF at -16m loss floor; soft budget constraint",
        "confidence": "strong",
        "source_id": SRC_JR,
        "beneficiaries": "Subsidised rent funds inside VMSW",
        "stated_goal": "Stabilize BOF after consolidation",
        "measured_outcome": "BOF -15.955m both 2024 and 2025 near floor",
        "absurdity_score": "7.0",
        "cost_score": "5.0",
        "difficulty": "2",
        "priority_index": "6.10",
        "cut_proposal": "Publish BOF toelage formula FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick741",
    },
    {
        "item_id": "lb_dual_vmsw_swl_slrb_flrbc_asymmetry",
        "name": "Dual VMSW 12.4bn assets / 10.5bn debt vs SWL 2.74 / SLRB 1.67 / FLRBC 1.61",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>VMSW_SWL_SLRB_FLRBC",
        "annual_cost_eur": "12382615326.78",
        "total_cost_eur": "12382615326.78",
        "tco_notes": "Not TE-additive; completes dual housing OIP residual wave 735-741",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE social housing dual map",
        "stated_goal": "Comparable regional social housing finance",
        "measured_outcome": "VMSW scale >> other regions; FS3 underuse vs FLRBC freeze dual delivery risk",
        "absurdity_score": "6.5",
        "cost_score": "9.0",
        "difficulty": "4",
        "priority_index": "7.20",
        "cut_proposal": "Open dual unit-cost + underuse + NPL dashboard",
        "status": "active",
        "struck_reason": "",
        "notes": "tick741",
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
        "title": "VMSW Jaarverslag 2025 residual dual SWL/SLRB/FLRBC social housing",
        "url": URL_JV,
        "publisher": "VMSW / Agentschap Wonen in Vlaanderen",
        "accessed_date": "2026-08-02",
        "source_class": "official_annual_report",
        "notes": (
            "Strong tick741: FS3 870m/yr 2024 assign 761.7 87.55pct underuse 108.3 (lost 8.2); 2025 assign 0; "
            "SSI 40.3m 75pct; VL loan 1bn 0pct; RC WM 589.4m; infra 59.2m; solidarisering 6.59m; "
            "basiskoten 100m/1744 rooms 2024; page " + URL_PAGE
        ),
    },
    {
        "source_id": SRC_JR,
        "title": "VMSW Jaarrekening 2025 residual balance sheet",
        "url": URL_JR,
        "publisher": "VMSW / Agentschap Wonen in Vlaanderen",
        "accessed_date": "2026-08-02",
        "source_class": "official_accounts",
        "notes": (
            "Strong tick741: assets 12.383bn debt 10.499bn LT fin 9.186 LT recv 11.172 cash 349; "
            "net profit 5.21 (GAF 21.17 BOF -15.95); fin income 363.6 debt costs 333.3"
        ),
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual VMSW JV/JR2025 residual vs SWL/SLRB/FLRBC housing tick741",
        "url": URL_JV,
        "publisher": "DOGE synthesis VMSW + prior duals",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": (
            "Strong dual not TE-additive: VMSW assets 12.383 debt 10.499 FS3 870 vs SWL debt 2.742 works 364 "
            "SLRB debt 1.672 liq 803 FLRBC encours 1.607; underuse vs freeze dual delivery; tick741"
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
    "gap_id": "gap_vmsw_jv2025_residual_l5",
    "hierarchy_path": "Vlaanderen>VMSW>JV2025_residual_L5",
    "entity_id": "vmsw",
    "what_is_missing": (
        "Machine-readable L5: (1) reconciliation of JR total debts 10.499bn vs prior CoA VMSW debt class "
        "3.123bn (which subset / ESA perimeter); (2) FS3 2025 assign pipeline monthly into 2026 and project "
        "backlog by woonmaatschappij; (3) opportunity cost of 1bn 0pct VL loan; (4) unit cost per dwelling "
        "for FS3NB/FS3RENO dual SWL/SLRB; (5) RC LT 189.6m investment mandate vs idle cash; "
        "(6) BOF -16m floor toelage cash-by-year formula"
    ),
    "why_it_matters": (
        "JV/JR2025 fill strong FS3 and BS aggregates but debt perimeter mismatch, assign lag, and dual "
        "unit costs remain opaque for waste ranking"
    ),
    "priority": "8",
    "recipient_body": "VMSW / Agentschap Wonen in Vlaanderen openbaarheid",
    "recipient_email": "openbaarheid@vlaanderen.be",
    "recipient_postal": "https://www.vlaanderen.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_vmsw_jv2025_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_vmsw_fs3_870m_2025|cmt_vmsw_bs_12_383bn_2025|cmt_vmsw_loan_1bn_0pct_2025",
    "linked_leaderboard_id": "lb_vmsw_fs3_underuse_108m_2024|lb_vmsw_debt_10_499bn_2025|lb_dual_vmsw_swl_slrb_flrbc_asymmetry",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick741 VMSW JV/JR2025 residual dual; ready not sent",
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
    print("foi +gap_vmsw_jv2025_residual_l5")
else:
    print("foi already exists")

rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_732":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick741 VMSW JV/JR2025 residual dual SWL/SLRB/FLRBC: FS3 870m underuse 108; "
            "BS assets 12.383 debt 10.499; VL loan 1bn 0pct; RC 589; "
            "FOI gap_vmsw_jv2025_residual_l5 ready"
        )
if not any(r.get("task_id") == "rq_733" for r in rqs):
    rqs.append({
        "task_id": "rq_733",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined or Entity II dual residual "
            "or fed Pillar2/VVPR recheck if new PDF or Wonen in Vlaanderen residual dual VMSW"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick741 after rq_732",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("research_queue rq_732=done rq_733=open")

ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys())
if ls:
    ls[0]["mode"] = "continuous"
    ls[0]["current_sprint"] = "hole_fill"
    ls[0]["last_tick_utc"] = UTC
    ls[0]["last_unit_id"] = "rq_732"
    ls[0]["ticks_completed"] = "741"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        "tick741 VMSW JV/JR2025 residual dual SWL/SLRB/FLRBC; next rq_733; "
        "progress@750 in 9; rq_116 deferred"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=741")
print("DONE tick741")

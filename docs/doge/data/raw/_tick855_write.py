import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-06T00:30:00Z"
TICK = 855
SRC = "src_dendermonde_jr2025"
SRC_DUAL = "src_dual_dendermonde_waregem_tick855"
EID = "city_dendermonde"
URL = "https://www.dendermonde.be/jaarverslag-en-rekeningen"


def append_csv(path, rows):
    p = Path(path)
    with p.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing = list(reader)
    key = fields[0]
    ids = {r[key] for r in existing}
    new = [r for r in rows if r.get(key) not in ids]
    if not new:
        print(f"{path}: nothing new")
        return 0
    with p.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fields})
    print(f"{path}: +{len(new)}")
    return len(new)


budgets = [
    ("bud_dd_assets_2025", 258302587, "Consol stad+OCMW total assets YE2025 258.303m; tick855"),
    ("bud_dd_equity_2025", 157507669, "Nettoactief YE2025 157.508m; tick855"),
    ("bud_dd_debt_total_2025", 100794919, "Total schulden YE2025 100.795m (was 125.1m); tick855"),
    ("bud_dd_fin_debt_2025", 46722862, "T4 total financiele schulden YE2025 46.723m (LT 43.168 + ST due 3.555); tick855"),
    ("bud_dd_fin_debt_lt_2025", 43167932, "Financiele schulden LT YE2025 43.168m; tick855"),
    ("bud_dd_fin_debt_st_due_2025", 3554930, "Schulden LT vervallend binnen jaar YE2025 3.555m; tick855"),
    ("bud_dd_pension_prov_2025", 31872997, "Pensioenvoorzieningen LT YE2025 31.873m (was 60.365m YE2024); tick855"),
    ("bud_dd_cash_2025", 10860904, "Liquide middelen YE2025 10.861m; tick855"),
    ("bud_dd_cap_subs_2025", 38377911, "Kapitaalsubsidies YE2025 38.378m; tick855"),
    ("bud_dd_fva_total_2025", 37367628, "Financiele vaste activa YE2025 37.368m; tick855"),
    ("bud_dd_fva_igs_2025", 36687306, "Fin VA IGS YE2025 36.687m; tick855"),
    ("bud_dd_mva_2025", 181818116, "Materiele vaste activa YE2025 181.818m; tick855"),
    ("bud_dd_onbeschikbaar_2025", 1293, "Onbeschikbare gelden J2 1.3k; tick855"),
    ("bud_dd_expl_rec_2025", 128317823, "Exploitatieontvangsten 128.318m; tick855"),
    ("bud_dd_expl_exp_2025", 122372488, "Exploitatieuitgaven 122.372m; tick855"),
    ("bud_dd_expl_saldo_2025", 5945335, "Exploitatiesaldo +5.945m; tick855"),
    ("bud_dd_invest_exp_2025", 8895091, "Investeringsuitgaven J2 8.895m; tick855"),
    ("bud_dd_invest_rec_2025", 1725901, "Investeringsontvangsten J2 1.726m; tick855"),
    ("bud_dd_invest_saldo_2025", -7169190, "Investeringssaldo -7.169m; tick855"),
    ("bud_dd_fin_rec_2025", 10368439, "Financieringsontvangsten 10.368m; tick855"),
    ("bud_dd_fin_exp_2025", 4014638, "Financieringsuitgaven 4.015m; tick855"),
    ("bud_dd_new_loans_2025", 10060654, "Nieuwe leningen 10.061m; tick855"),
    ("bud_dd_aflossingen_2025", 3671178, "Periodieke aflossingen 3.671m; tick855"),
    ("bud_dd_afm_2025", 2581941, "AFM +2.582m; tick855"),
    ("bud_dd_afm_corr_2025", 3026448, "Gecorrigeerde AFM +3.026m; tick855"),
    ("bud_dd_bbr_2025", 14719934, "BBR 14.720m after onbeschikbaar 1.3k; tick855"),
    ("bud_dd_budget_result_2025", 5129946, "Budgettair resultaat boekjaar +5.130m; tick855"),
    ("bud_dd_cum_br_2025", 14721226, "Gecumuleerd budgettair resultaat 14.721m; tick855"),
    ("bud_dd_pnl_result_2025", 23779685, "Vennootschapsresultaat J5 +23.780m (pension release effect); tick855"),
    ("bud_dd_personnel_2025", 76644056, "J5/T2 bezoldigingen 76.644m (incl onderwijs other-gov 8.279m); tick855"),
    ("bud_dd_toelagen_2025", 18856916, "Toegestane werkingssubsidies 18.857m (politie 9.000 fire 1.272 IGS 4.478 AGB 1.130 other 2.557); tick855"),
    ("bud_dd_ocmw_aid_2025", 6949105, "OCMW individuele hulp 6.949m; tick855"),
    ("bud_dd_fiscal_2025", 42830861, "J5 fiscale opbrengsten en boetes 42.831m; tick855"),
    ("bud_dd_werk_subs_rec_2025", 52653104, "J5 werkingssubsidies ontvangen 52.653m; tick855"),
    ("bud_dd_gemeentefonds_2025", 18758284, "Gemeentefonds 18.758m; tick855"),
    ("bud_dd_fin_costs_2025", 1606657, "J5 financiele kosten 1.607m; tick855"),
    ("bud_dd_police_toelage_2025", 9000000, "Toelage politiezone 9.000m; tick855"),
    ("bud_dd_fire_toelage_2025", 1271882, "Toelage hulpverleningszone 1.272m; tick855"),
    ("bud_dd_pension_drop_yoy_2025", -28491970, "Pension provisions drop YE2024 60.365m to YE2025 31.873m; tick855"),
]
budget_rows = [{
    "budget_id": bid, "entity_id": EID, "year": "2025",
    "amount_eur": str(amt), "amount_min_eur": "", "amount_max_eur": "",
    "basis": "outturn", "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, amt, notes in budgets]
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_dd_balance_258m_2025",
        "title": "Dendermonde consol stad+OCMW balance YE2025 assets 258.3m",
        "entity_id": EID, "beneficiary": "Stad+OCMW Dendermonde",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-06-10",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "258302587", "cash_by_year": "2025:258302587",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal balance sheet", "cut_option": "Pension release FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde",
        "notes": "tick855 primary JR2025 pub 12.06.2026 GR 10.06.2026",
    },
    {
        "commitment_id": "cmt_dd_expl_128m_2025",
        "title": "Dendermonde exploitation receipts 128.3m expenses 122.4m 2025",
        "entity_id": EID, "beneficiary": "Stad+OCMW Dendermonde",
        "legal_basis": "BBC", "decision_date": "2026-06-10",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "128317823", "cash_by_year": "2025:128317823",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal operations", "cut_option": "Toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>exploitatie",
        "notes": "tick855",
    },
    {
        "commitment_id": "cmt_dd_fin_debt_47m_2025",
        "title": "Dendermonde financial debt stock 46.7m YE2025 (new loans 10.1m)",
        "entity_id": EID, "beneficiary": "creditors",
        "legal_basis": "BBC debt", "decision_date": "2026-06-10",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "46722862", "cash_by_year": "2025stock:46722862;new:10060654",
        "remaining_eur": "46722862", "status": "stock", "evaluation_url": URL,
        "stated_goal": "Capital finance", "cut_option": "Lender schedule FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>debt",
        "notes": "tick855 rising stock 40.3m YE2024 to 46.7m; new loans 10.1m",
    },
    {
        "commitment_id": "cmt_dd_afm_pension_2025",
        "title": "Dendermonde AFM +2.6m BBR 14.7m pension drop 60.4m to 31.9m 2025",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-06-10",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "14719934",
        "cash_by_year": "2025BBR:14719934;AFM:2581941;pension:31872997;pnl:23779685",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Financial equilibrium", "cut_option": "Pension actuarial FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>AFM",
        "notes": "tick855 P&L +23.8m driven by pension provision release; FOI-adjacent",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_dd_personnel_77m_2025",
        "name": "Dendermonde personnel/bezold 76.6m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>personeel",
        "annual_cost_eur": "76644056", "total_cost_eur": "76644056",
        "tco_notes": "Strong; dual Waregem 56.3m; includes other-gov onderwijs 8.3m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff Stad+OCMW Dendermonde",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "6.5", "difficulty": "7.0",
        "priority_index": "5.0", "cut_proposal": "Headcount FOI",
        "status": "active", "struck_reason": "", "notes": "tick855",
    },
    {
        "item_id": "lb_dd_toelagen_19m_2025",
        "name": "Dendermonde toelagen 18.9m 2025 (police 9.0 IGS 4.5 other 2.6 fire 1.3 AGB 1.1)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>toelagen",
        "annual_cost_eur": "18856916", "total_cost_eur": "18856916",
        "tco_notes": "Strong; dual Waregem 15.0m; police 9.0m large",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + IGS + AGB + other",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2 buckets",
        "absurdity_score": "4.5", "cost_score": "5.5", "difficulty": "5.5",
        "priority_index": "5.0", "cut_proposal": "Named matrix FOI other+IGS",
        "status": "active", "struck_reason": "", "notes": "tick855",
    },
    {
        "item_id": "lb_dd_afm_3m_2025",
        "name": "Dendermonde AFM +2.6m BBR 14.7m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "2581941",
        "tco_notes": "Strong positive; dual Waregem +11.1m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Dendermonde",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "4.0", "difficulty": "4.0",
        "priority_index": "3.5", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick855 positive",
    },
    {
        "item_id": "lb_dd_pension_release_28m_2025",
        "name": "Dendermonde pension provision drop -28.5m YE2024-25 (P&L +23.8m)",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>pension",
        "annual_cost_eur": "0", "total_cost_eur": "28491970",
        "tco_notes": "Strong FOI-adjacent one-off; stock 60.4m to 31.9m; J5 afschrijvingen -16.3m; not pure annual waste",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Accounting residual",
        "stated_goal": "Pension liability remeasurement", "measured_outcome": "J4 YoY",
        "absurdity_score": "7.0", "cost_score": "6.5", "difficulty": "5.5",
        "priority_index": "6.75", "cut_proposal": "Actuarial FOI",
        "status": "active", "struck_reason": "", "notes": "tick855 one-off FOI-adjacent",
    },
    {
        "item_id": "lb_dd_fin_debt_47m_2025",
        "name": "Dendermonde fin debt stock 46.7m YE2025 (new loans 10.1m)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>debt",
        "annual_cost_eur": "1606657", "total_cost_eur": "46722862",
        "tco_notes": "Strong rising stock; dual Waregem 32.7m declining; new loans 10.1m FOI-adjacent",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance", "measured_outcome": "T4 rising",
        "absurdity_score": "5.0", "cost_score": "5.5", "difficulty": "5.5",
        "priority_index": "5.25", "cut_proposal": "Lender FOI",
        "status": "active", "struck_reason": "", "notes": "tick855 stock",
    },
    {
        "item_id": "lb_dd_ocmw_aid_7m_2025",
        "name": "Dendermonde OCMW individual aid 6.9m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde>OCMW",
        "annual_cost_eur": "6949105", "total_cost_eur": "6949105",
        "tco_notes": "Strong; dual Waregem 4.3m Ieper 6.5m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0", "cost_score": "4.0", "difficulty": "7.0",
        "priority_index": "3.5", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick855 safety-net",
    },
    {
        "item_id": "lb_dual_dendermonde_waregem_tick855",
        "name": "Dual Dendermonde 258m vs Waregem 346m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "258302587",
        "tco_notes": "Strong dual not TE-additive; DD pension release + debt up vs WG high AFM + pension stock",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.5", "cost_score": "6.0", "difficulty": "5.0",
        "priority_index": "5.25", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick855",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Stad+OCMW Dendermonde Jaarrekening 2025 (BBC consolidatie, 286p)",
        "url": URL,
        "publisher": "Stad Dendermonde",
        "accessed_date": "2026-08-06",
        "source_class": "primary_jaarrekening",
        "notes": "GR/RMW 2026-06-10 pub 2026-06-12; assets 258.3m equity 157.5m fin debt 46.7m new loans 10.1m pension 31.9m (was 60.4m) expl 128.3/122.4m AFM +2.6m BBR 14.7m personnel 76.6m toelagen 18.9m P&L +23.8m; tick855",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Dendermonde JR2025 vs Waregem JR2025 tick855",
        "url": URL,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-06",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Dendermonde 258m vs Waregem 346m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Stad Dendermonde",
    "name_fr": "Ville de Termonde",
    "name_en": "City of Dendermonde",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.dendermonde.be",
    "foi_email": "info@dendermonde.be",
    "foi_postal": "Franz Courtensstraat 11 9200 Dendermonde",
    "notes": "JR2025 assets 258m equity 158m cash 11m expl 128/122m personnel 77m fin debt 47m new loans 10m pension drop 60to32m AFM +2.6m BBR 15m toelagen 19m P&L +24m; tick855",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_dendermonde_pension_loans_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Dendermonde_L5",
    "entity_id": EID,
    "what_is_missing": "Explanation and actuarial basis of pension provision drop from 60.365m YE2024 to 31.873m YE2025 (P&L +23.8m / afschrijvingen -16.3m); lender schedule for new loans 10.061m and stock 46.723m; named toelagen matrix for other 2.557m + IGS 4.478m within 18.857m package",
    "why_it_matters": "258m city+OCMW with rising debt and one-off pension release dominating P&L — residual L5 opacity vs Waregem dual peers",
    "priority": "8",
    "recipient_body": "Stad Dendermonde / financieel directeur / openbaarheid",
    "recipient_email": "info@dendermonde.be",
    "recipient_postal": "https://www.dendermonde.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_dendermonde_pension_loans_l5.md",
    "status": "ready",
    "date_ready": "2026-08-06",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_dd_afm_pension_2025",
    "linked_leaderboard_id": "lb_dd_pension_release_28m_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick855 primary JR2025; ready draft; do not send; prio8 pension release",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_845":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick855 Dendermonde JR2025 dual Waregem; assets 258m fin debt 47m pension drop 28m"
        print("rq_845 done")
        break

if not any(r["task_id"] == "rq_846" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_846",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Dendermonde JR2025 filled tick855; residual Roeselare portal/Lier portal/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick855 after Dendermonde dual Waregem",
    })
    print("spawned rq_846")

with rq_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    for r in rq_rows:
        w.writerow({k: r.get(k, "") for k in rq_fields})

ls_path = Path("docs/doge/data/loop_state.csv")
with ls_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    ls_fields = reader.fieldnames
    ls_rows = list(reader)
for r in ls_rows:
    if r["state_id"] == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = NOW
        r["last_unit_id"] = "rq_845"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick855 Dendermonde JR2025 dual Waregem; FOI gap_dendermonde_pension_loans_l5; next rq_846 residual dual L5; progress@860 in 5; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

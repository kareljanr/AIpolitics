import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-06T01:00:00Z"
TICK = 856
SRC = "src_lommel_jr2025"
SRC_DUAL = "src_dual_lommel_dendermonde_tick856"
EID = "city_lommel"
URL = "https://www.lommel.be/jaarrekening-2025-stad-lommel"


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
    ("bud_lm_assets_2025", 431950694, "Consol stad+OCMW total assets YE2025 431.951m; tick856"),
    ("bud_lm_equity_2025", 373745296, "Nettoactief YE2025 373.745m; tick856"),
    ("bud_lm_debt_total_2025", 58205398, "Total schulden YE2025 58.205m; tick856"),
    ("bud_lm_fin_debt_2025", 16018055, "T4 total financiele schulden YE2025 16.018m (LT 14.291 + ST due 1.727); tick856"),
    ("bud_lm_fin_debt_lt_2025", 14290913, "Financiele schulden LT YE2025 14.291m; tick856"),
    ("bud_lm_fin_debt_st_due_2025", 1727142, "Schulden LT vervallend binnen jaar YE2025 1.727m; tick856"),
    ("bud_lm_pension_prov_2025", 26687362, "Pensioenvoorzieningen LT YE2025 26.687m; tick856"),
    ("bud_lm_cash_2025", 28938845, "Liquide middelen YE2025 28.939m (spaarpot class); tick856"),
    ("bud_lm_cap_subs_2025", 44451108, "Kapitaalsubsidies YE2025 44.451m; tick856"),
    ("bud_lm_fva_total_2025", 71279686, "Financiele vaste activa YE2025 71.280m (was 39.8m); tick856"),
    ("bud_lm_fva_igs_2025", 61236029, "Fin VA IGS YE2025 61.236m (was 29.8m; reval FOI); tick856"),
    ("bud_lm_mva_2025", 297434569, "Materiele vaste activa YE2025 297.435m; tick856"),
    ("bud_lm_herwaard_2025", 31455519, "Herwaarderingsreserves YE2025 31.456m (was 0.019m); tick856"),
    ("bud_lm_onbeschikbaar_2025", 253333, "Onbeschikbare gelden J2 0.253m; tick856"),
    ("bud_lm_expl_rec_2025", 67279945, "Exploitatieontvangsten 67.280m; tick856"),
    ("bud_lm_expl_exp_2025", 61384026, "Exploitatieuitgaven 61.384m; tick856"),
    ("bud_lm_expl_saldo_2025", 5895919, "Exploitatiesaldo +5.896m; tick856"),
    ("bud_lm_invest_exp_2025", 24754757, "Investeringsuitgaven J2 24.755m; tick856"),
    ("bud_lm_invest_rec_2025", 7552002, "Investeringsontvangsten J2 7.552m; tick856"),
    ("bud_lm_invest_saldo_2025", -17202755, "Investeringssaldo -17.203m; tick856"),
    ("bud_lm_fin_rec_2025", 11252988, "Financieringsontvangsten 11.253m; tick856"),
    ("bud_lm_fin_exp_2025", 1888525, "Financieringsuitgaven 1.889m; tick856"),
    ("bud_lm_new_loans_2025", 8674545, "Nieuwe leningen 8.675m; tick856"),
    ("bud_lm_aflossingen_2025", 1439922, "Periodieke aflossingen 1.440m; tick856"),
    ("bud_lm_afm_2025", 5485717, "AFM +5.486m (strong); tick856"),
    ("bud_lm_afm_corr_2025", 6222964, "Gecorrigeerde AFM +6.223m; tick856"),
    ("bud_lm_bbr_2025", 25160052, "BBR 25.160m after onbeschikbaar 0.253m; tick856"),
    ("bud_lm_budget_result_2025", -1942372, "Budgettair resultaat boekjaar -1.942m; tick856"),
    ("bud_lm_cum_br_2025", 25413386, "Gecumuleerd budgettair resultaat 25.413m; tick856"),
    ("bud_lm_pnl_result_2025", -4833949, "Vennootschapsresultaat J5 -4.834m; tick856"),
    ("bud_lm_personnel_2025", 27997282, "J5/T2 bezoldigingen 27.997m; tick856"),
    ("bud_lm_toelagen_2025", 17926093, "Toegestane werkingssubsidies 17.926m (politie 4.720 fire 2.005 AGB 2.988 welzijn 2.991 other 3.296); tick856"),
    ("bud_lm_ocmw_aid_2025", 2407325, "OCMW individuele hulp 2.407m; tick856"),
    ("bud_lm_fiscal_2025", 33078005, "J5 fiscale opbrengsten en boetes 33.078m; tick856"),
    ("bud_lm_werk_subs_rec_2025", 23202923, "J5 werkingssubsidies ontvangen 23.203m; tick856"),
    ("bud_lm_gemeentefonds_2025", 11251654, "Gemeentefonds 11.252m; tick856"),
    ("bud_lm_fin_costs_2025", 527574, "J5 financiele kosten 0.528m; tick856"),
    ("bud_lm_police_toelage_2025", 4720000, "Toelage politiezone 4.720m; tick856"),
    ("bud_lm_fire_toelage_2025", 2004692, "Toelage hulpverleningszone 2.005m; tick856"),
]
budget_rows = [{
    "budget_id": bid, "entity_id": EID, "year": "2025",
    "amount_eur": str(amt), "amount_min_eur": "", "amount_max_eur": "",
    "basis": "outturn", "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, amt, notes in budgets]
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_lm_balance_432m_2025",
        "title": "Lommel consol stad+OCMW balance YE2025 assets 432.0m",
        "entity_id": EID, "beneficiary": "Stad+OCMW Lommel",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-06-24",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "431950694", "cash_by_year": "2025:431950694",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal balance sheet", "cut_option": "IGS reval FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel",
        "notes": "tick856 primary JR2025 known 24.06.2026",
    },
    {
        "commitment_id": "cmt_lm_expl_67m_2025",
        "title": "Lommel exploitation receipts 67.3m expenses 61.4m 2025",
        "entity_id": EID, "beneficiary": "Stad+OCMW Lommel",
        "legal_basis": "BBC", "decision_date": "2026-06-24",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "67279945", "cash_by_year": "2025:67279945",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal operations", "cut_option": "Toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>exploitatie",
        "notes": "tick856",
    },
    {
        "commitment_id": "cmt_lm_fin_debt_16m_2025",
        "title": "Lommel financial debt stock 16.0m YE2025 (new loans 8.7m)",
        "entity_id": EID, "beneficiary": "creditors",
        "legal_basis": "BBC debt", "decision_date": "2026-06-24",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "16018055", "cash_by_year": "2025stock:16018055;new:8674545",
        "remaining_eur": "16018055", "status": "stock", "evaluation_url": URL,
        "stated_goal": "Capital finance", "cut_option": "Lender schedule FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>debt",
        "notes": "tick856 jump from 8.8m YE2024; invest 24.8m",
    },
    {
        "commitment_id": "cmt_lm_afm_bbr_2025",
        "title": "Lommel AFM +5.5m and BBR 25.2m 2025 (cash 28.9m)",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-06-24",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "25160052",
        "cash_by_year": "2025BBR:25160052;AFM:5485717;cash:28938845;herwaard:31455519",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Financial equilibrium", "cut_option": "IGS reval FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>AFM",
        "notes": "tick856 strong AFM+BBR; FVA IGS reval 29.8to61.2m FOI-adjacent",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_lm_personnel_28m_2025",
        "name": "Lommel personnel/bezold 28.0m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>personeel",
        "annual_cost_eur": "27997282", "total_cost_eur": "27997282",
        "tco_notes": "Strong; dual Dendermonde 76.6m Waregem 56.3m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff Stad+OCMW Lommel",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "5.0", "difficulty": "7.0",
        "priority_index": "4.25", "cut_proposal": "Headcount FOI",
        "status": "active", "struck_reason": "", "notes": "tick856",
    },
    {
        "item_id": "lb_lm_toelagen_18m_2025",
        "name": "Lommel toelagen 17.9m 2025 (police 4.7 AGB 3.0 welzijn 3.0 other 3.3 fire 2.0)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>toelagen",
        "annual_cost_eur": "17926093", "total_cost_eur": "17926093",
        "tco_notes": "Strong; dual Dendermonde 18.9m; other 3.3m FOI-adjacent",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + AGB + welzijn + other",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2 buckets",
        "absurdity_score": "4.5", "cost_score": "5.5", "difficulty": "5.5",
        "priority_index": "5.0", "cut_proposal": "Named matrix FOI other",
        "status": "active", "struck_reason": "", "notes": "tick856",
    },
    {
        "item_id": "lb_lm_afm_5m_2025",
        "name": "Lommel AFM +5.5m BBR 25.2m cash 28.9m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "5485717",
        "tco_notes": "Strong high cash/BBR; dual Dendermonde +2.6m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Lommel",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "5.5", "difficulty": "4.0",
        "priority_index": "4.25", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick856 positive",
    },
    {
        "item_id": "lb_lm_fva_igs_reval_2025",
        "name": "Lommel FVA IGS jump 29.8m to 61.2m + herwaard 31.5m YE2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>FVA_IGS",
        "annual_cost_eur": "0", "total_cost_eur": "31436150",
        "tco_notes": "Strong FOI-adjacent reval; assets +36m YoY partly from IGS/herwaard not cash",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "IGS holdings",
        "stated_goal": "Financial fixed assets revaluation", "measured_outcome": "J4 YoY",
        "absurdity_score": "6.5", "cost_score": "6.0", "difficulty": "5.0",
        "priority_index": "6.25", "cut_proposal": "Reval method FOI",
        "status": "active", "struck_reason": "", "notes": "tick856 FOI-adjacent stock",
    },
    {
        "item_id": "lb_lm_fin_debt_16m_2025",
        "name": "Lommel fin debt stock 16.0m YE2025 (new loans 8.7m; invest 24.8m)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>debt",
        "annual_cost_eur": "441474", "total_cost_eur": "16018055",
        "tco_notes": "Strong jump from 8.8m; dual Dendermonde 46.7m; still low vs cash 28.9m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance invest", "measured_outcome": "T4 jump",
        "absurdity_score": "4.5", "cost_score": "4.5", "difficulty": "5.5",
        "priority_index": "4.5", "cut_proposal": "Lender FOI",
        "status": "active", "struck_reason": "", "notes": "tick856 stock",
    },
    {
        "item_id": "lb_lm_ocmw_aid_2m_2025",
        "name": "Lommel OCMW individual aid 2.4m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>OCMW",
        "annual_cost_eur": "2407325", "total_cost_eur": "2407325",
        "tco_notes": "Strong; dual Dendermonde 6.9m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0", "cost_score": "3.5", "difficulty": "7.0",
        "priority_index": "3.25", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick856 safety-net",
    },
    {
        "item_id": "lb_dual_lommel_dendermonde_tick856",
        "name": "Dual Lommel 432m vs Dendermonde 258m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "431950694",
        "tco_notes": "Strong dual not TE-additive; Lommel high cash/AFM/IGS reval vs DD pension release + debt up",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.5", "cost_score": "6.0", "difficulty": "5.0",
        "priority_index": "5.25", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick856",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Stad+OCMW Lommel Jaarrekening 2025 (BBC consolidatie, 274p)",
        "url": URL,
        "publisher": "Stad Lommel",
        "accessed_date": "2026-08-06",
        "source_class": "primary_jaarrekening",
        "notes": "Published 2026-06-24; assets 432.0m equity 373.7m cash 28.9m expl 67.3/61.4m AFM +5.5m BBR 25.2m fin debt 16.0m new loans 8.7m invest 24.8m FVA IGS 61.2m herwaard 31.5m personnel 28.0m toelagen 17.9m; tick856",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Lommel JR2025 vs Dendermonde JR2025 tick856",
        "url": URL,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-06",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Lommel 432m vs Dendermonde 258m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Stad Lommel",
    "name_fr": "Ville de Lommel",
    "name_en": "City of Lommel",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.lommel.be",
    "foi_email": "info@lommel.be",
    "foi_postal": "Hertog Janplein 1 3920 Lommel",
    "notes": "JR2025 assets 432m equity 374m cash 29m expl 67/61m personnel 28m fin debt 16m new loans 8.7m invest 25m AFM +5.5m BBR 25m FVA IGS reval 61m toelagen 18m; tick856",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_lommel_igs_reval_loans_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Lommel_L5",
    "entity_id": EID,
    "what_is_missing": "Method and counterpart entities for FVA IGS jump 29.8m to 61.2m and herwaarderingsreserves 0.019m to 31.5m; lender schedule for new loans 8.675m / stock 16.018m; named toelagen matrix for other 3.296m within 17.926m package; AGB Sport AFM negative residual",
    "why_it_matters": "432m city+OCMW with strong cash/BBR/AFM but balance sheet growth partly reval not cash; invest 24.8m + debt jump FOI-adjacent",
    "priority": "7",
    "recipient_body": "Stad Lommel / financieel directeur / openbaarheid",
    "recipient_email": "info@lommel.be",
    "recipient_postal": "https://www.lommel.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_lommel_igs_reval_loans_l5.md",
    "status": "ready",
    "date_ready": "2026-08-06",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_lm_afm_bbr_2025",
    "linked_leaderboard_id": "lb_lm_fva_igs_reval_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick856 primary JR2025; ready draft; do not send",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_846":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick856 Lommel JR2025 dual Dendermonde; assets 432m cash 29m AFM +5.5m FVA IGS reval"
        print("rq_846 done")
        break

if not any(r["task_id"] == "rq_847" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_847",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Lommel JR2025 filled tick856; residual Roeselare portal/Lier portal/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick856 after Lommel dual Dendermonde",
    })
    print("spawned rq_847")

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
        r["last_unit_id"] = "rq_846"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick856 Lommel JR2025 dual Dendermonde; FOI gap_lommel_igs_reval_loans_l5; next rq_847 residual dual L5; progress@860 in 4; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

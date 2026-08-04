import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-06T02:00:00Z"
TICK = 858
SRC = "src_geraardsbergen_jr2025"
SRC_DUAL = "src_dual_geraardsbergen_heist_tick858"
EID = "city_geraardsbergen"
URL = "https://www.geraardsbergen.be/jaarrekening-2025"


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
    ("bud_gb_assets_2025", 158893712, "Consol stad+OCMW total assets YE2025 158.894m; tick858"),
    ("bud_gb_equity_2025", 63247103, "Nettoactief YE2025 63.247m; tick858"),
    ("bud_gb_debt_total_2025", 95646609, "Total schulden YE2025 95.647m; tick858"),
    ("bud_gb_fin_debt_2025", 50732626, "T4 total financiele schulden YE2025 50.733m (LT 45.562 + ST due 5.171); tick858"),
    ("bud_gb_fin_debt_lt_2025", 45562059, "Financiele schulden LT YE2025 45.562m; tick858"),
    ("bud_gb_fin_debt_st_due_2025", 5170566, "Schulden LT vervallend binnen jaar YE2025 5.171m; tick858"),
    ("bud_gb_pension_prov_2025", 29849402, "Pensioenvoorzieningen LT YE2025 29.849m; tick858"),
    ("bud_gb_cash_2025", 11097698, "Liquide middelen YE2025 11.098m; tick858"),
    ("bud_gb_cap_subs_2025", 14597485, "Kapitaalsubsidies YE2025 14.597m; tick858"),
    ("bud_gb_fva_total_2025", 29073485, "Financiele vaste activa YE2025 29.073m; tick858"),
    ("bud_gb_fva_igs_2025", 20311797, "Fin VA IGS YE2025 20.312m; tick858"),
    ("bud_gb_mva_2025", 93125830, "Materiele vaste activa YE2025 93.126m; tick858"),
    ("bud_gb_onbeschikbaar_2025", 360000, "Onbeschikbare gelden J2 0.360m; tick858"),
    ("bud_gb_expl_rec_2025", 83125080, "Exploitatieontvangsten 83.125m; tick858"),
    ("bud_gb_expl_exp_2025", 73297855, "Exploitatieuitgaven 73.298m; tick858"),
    ("bud_gb_expl_saldo_2025", 9827225, "Exploitatiesaldo +9.827m; tick858"),
    ("bud_gb_invest_exp_2025", 10465903, "Investeringsuitgaven J2 10.466m; tick858"),
    ("bud_gb_invest_rec_2025", 691366, "Investeringsontvangsten J2 0.691m; tick858"),
    ("bud_gb_invest_saldo_2025", -9774537, "Investeringssaldo -9.775m; tick858"),
    ("bud_gb_fin_rec_2025", 6628324, "Financieringsontvangsten 6.628m; tick858"),
    ("bud_gb_fin_exp_2025", 5250276, "Financieringsuitgaven 5.250m; tick858"),
    ("bud_gb_new_loans_2025", 6335699, "Nieuwe leningen 6.336m; tick858"),
    ("bud_gb_aflossingen_2025", 5074807, "Periodieke aflossingen 5.075m; tick858"),
    ("bud_gb_afm_2025", 5560442, "AFM +5.560m; tick858"),
    ("bud_gb_afm_corr_2025", 6517510, "Gecorrigeerde AFM +6.518m; tick858"),
    ("bud_gb_bbr_2025", 12892119, "BBR 12.892m after onbeschikbaar 0.360m; tick858"),
    ("bud_gb_budget_result_2025", 1430736, "Budgettair resultaat boekjaar +1.431m; tick858"),
    ("bud_gb_cum_br_2025", 13252119, "Gecumuleerd budgettair resultaat 13.252m; tick858"),
    ("bud_gb_pnl_result_2025", 4364093, "Vennootschapsresultaat J5 +4.364m; tick858"),
    ("bud_gb_personnel_2025", 43367250, "J5 bezoldigingen 43.367m (T2 43.333m; incl onderwijs other-gov 3.187m); tick858"),
    ("bud_gb_toelagen_2025", 8766004, "Toegestane werkingssubsidies 8.766m (politie 5.159 fire 1.542 AGB 0.808 other 0.600); tick858"),
    ("bud_gb_ocmw_aid_2025", 4825973, "OCMW individuele hulp 4.826m; tick858"),
    ("bud_gb_fiscal_2025", 28752381, "J5 fiscale opbrengsten en boetes 28.752m; tick858"),
    ("bud_gb_werk_subs_rec_2025", 32589218, "J5 werkingssubsidies ontvangen 32.589m; tick858"),
    ("bud_gb_gemeentefonds_2025", 12235878, "Gemeentefonds 12.236m; tick858"),
    ("bud_gb_fin_costs_2025", 1366112, "J5 financiele kosten 1.366m; tick858"),
    ("bud_gb_police_toelage_2025", 5159223, "Toelage politiezone 5.159m; tick858"),
    ("bud_gb_fire_toelage_2025", 1541570, "Toelage hulpverleningszone 1.542m; tick858"),
]
budget_rows = [{
    "budget_id": bid, "entity_id": EID, "year": "2025",
    "amount_eur": str(amt), "amount_min_eur": "", "amount_max_eur": "",
    "basis": "outturn", "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, amt, notes in budgets]
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_gb_balance_159m_2025",
        "title": "Geraardsbergen consol stad+OCMW balance YE2025 assets 158.9m",
        "entity_id": EID, "beneficiary": "Stad+OCMW Geraardsbergen",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-05-26",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "158893712", "cash_by_year": "2025:158893712",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal balance sheet", "cut_option": "Debt FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen",
        "notes": "tick858 primary JR2025 GR 26.05.2026 pub 03.06.2026",
    },
    {
        "commitment_id": "cmt_gb_expl_83m_2025",
        "title": "Geraardsbergen exploitation receipts 83.1m expenses 73.3m 2025",
        "entity_id": EID, "beneficiary": "Stad+OCMW Geraardsbergen",
        "legal_basis": "BBC", "decision_date": "2026-05-26",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "83125080", "cash_by_year": "2025:83125080",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal operations", "cut_option": "Toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>exploitatie",
        "notes": "tick858",
    },
    {
        "commitment_id": "cmt_gb_fin_debt_51m_2025",
        "title": "Geraardsbergen financial debt stock 50.7m YE2025 (new loans 6.3m)",
        "entity_id": EID, "beneficiary": "creditors",
        "legal_basis": "BBC debt", "decision_date": "2026-05-26",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "50732626", "cash_by_year": "2025stock:50732626;new:6335699",
        "remaining_eur": "50732626", "status": "stock", "evaluation_url": URL,
        "stated_goal": "Capital finance", "cut_option": "Lender schedule FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>debt",
        "notes": "tick858 high debt intensity ~32pct assets; was 51.5m YE2024",
    },
    {
        "commitment_id": "cmt_gb_afm_bbr_2025",
        "title": "Geraardsbergen AFM +5.6m and BBR 12.9m 2025",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-05-26",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "12892119",
        "cash_by_year": "2025BBR:12892119;AFM:5560442;pension:29849402",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Financial equilibrium", "cut_option": "Debt+pension FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>AFM",
        "notes": "tick858 solid AFM; debt+pension stocks elevated vs equity 63m",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_gb_personnel_43m_2025",
        "name": "Geraardsbergen personnel/bezold 43.4m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>personeel",
        "annual_cost_eur": "43367250", "total_cost_eur": "43367250",
        "tco_notes": "Strong; dual Heist 38.6m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff Stad+OCMW",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "5.5", "difficulty": "7.0",
        "priority_index": "4.5", "cut_proposal": "Headcount FOI",
        "status": "active", "struck_reason": "", "notes": "tick858",
    },
    {
        "item_id": "lb_gb_toelagen_9m_2025",
        "name": "Geraardsbergen toelagen 8.8m 2025 (police 5.2 fire 1.5 AGB 0.8 other 0.6)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>toelagen",
        "annual_cost_eur": "8766004", "total_cost_eur": "8766004",
        "tco_notes": "Strong; dual Heist 13.6m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + fire + AGB + other",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2 buckets",
        "absurdity_score": "4.0", "cost_score": "4.5", "difficulty": "5.5",
        "priority_index": "4.25", "cut_proposal": "Named matrix FOI other",
        "status": "active", "struck_reason": "", "notes": "tick858",
    },
    {
        "item_id": "lb_gb_afm_6m_2025",
        "name": "Geraardsbergen AFM +5.6m BBR 12.9m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "5560442",
        "tco_notes": "Strong positive; dual Heist +10.8m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Geraardsbergen",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "5.0", "difficulty": "4.0",
        "priority_index": "4.0", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick858 positive",
    },
    {
        "item_id": "lb_gb_fin_debt_51m_2025",
        "name": "Geraardsbergen fin debt stock 50.7m YE2025 (~32pct assets; new loans 6.3m)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>debt",
        "annual_cost_eur": "1352129", "total_cost_eur": "50732626",
        "tco_notes": "Strong FOI-adjacent high intensity vs Heist 18m / Lommel 16m on larger assets; equity only 63m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance", "measured_outcome": "T4 stock",
        "absurdity_score": "6.5", "cost_score": "6.0", "difficulty": "5.5",
        "priority_index": "6.25", "cut_proposal": "Lender FOI",
        "status": "active", "struck_reason": "", "notes": "tick858 stock FOI-adjacent",
    },
    {
        "item_id": "lb_gb_pension_30m_2025",
        "name": "Geraardsbergen pension provisions 29.8m YE2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>pension",
        "annual_cost_eur": "0", "total_cost_eur": "29849402",
        "tco_notes": "Strong stock; dual Heist 24.8m; with debt 50.7m = large LT claims vs equity 63m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Former/current staff",
        "stated_goal": "Pension liability", "measured_outcome": "J4 provisions",
        "absurdity_score": "5.5", "cost_score": "5.5", "difficulty": "6.0",
        "priority_index": "5.5", "cut_proposal": "Composition FOI",
        "status": "active", "struck_reason": "", "notes": "tick858 stock",
    },
    {
        "item_id": "lb_gb_ocmw_aid_5m_2025",
        "name": "Geraardsbergen OCMW individual aid 4.8m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen>OCMW",
        "annual_cost_eur": "4825973", "total_cost_eur": "4825973",
        "tco_notes": "Strong; dual Heist 3.6m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0", "cost_score": "4.0", "difficulty": "7.0",
        "priority_index": "3.5", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick858 safety-net",
    },
    {
        "item_id": "lb_dual_geraardsbergen_heist_tick858",
        "name": "Dual Geraardsbergen 159m vs Heist 233m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "158893712",
        "tco_notes": "Strong dual not TE-additive; GB high debt intensity vs Heist high AFM",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.5", "cost_score": "5.5", "difficulty": "5.0",
        "priority_index": "5.0", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick858",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Stad+OCMW Geraardsbergen Jaarrekening 2025 (BBC consolidatie, 236p)",
        "url": URL,
        "publisher": "Lokaal Bestuur Geraardsbergen",
        "accessed_date": "2026-08-06",
        "source_class": "primary_jaarrekening",
        "notes": "GR 2026-05-26 pub 2026-06-03; assets 158.9m equity 63.2m cash 11.1m expl 83.1/73.3m AFM +5.6m BBR 12.9m fin debt 50.7m new loans 6.3m pension 29.8m personnel 43.4m toelagen 8.8m; tick858",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Geraardsbergen JR2025 vs Heist-op-den-Berg JR2025 tick858",
        "url": URL,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-06",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Geraardsbergen 159m vs Heist 233m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Stad Geraardsbergen",
    "name_fr": "Ville de Grammont",
    "name_en": "City of Geraardsbergen",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.geraardsbergen.be",
    "foi_email": "info@geraardsbergen.be",
    "foi_postal": "Weverijstraat 20 9500 Geraardsbergen",
    "notes": "JR2025 assets 159m equity 63m cash 11m expl 83/73m personnel 43m fin debt 51m (~32pct assets) new loans 6.3m pension 30m AFM +5.6m BBR 13m toelagen 8.8m; tick858",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_geraardsbergen_debt_loans_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Geraardsbergen_L5",
    "entity_id": EID,
    "what_is_missing": "Full lender schedule for fin debt 50.733m (~32pct of assets) and new loans 6.336m; pension provision composition 29.849m; named toelagen matrix for other 0.600m; AGB Geraardsbergen full JR2025 (consol BBR 0.672m / AFM 0.052m)",
    "why_it_matters": "159m city+OCMW with solid AFM +5.6m but elevated debt intensity and pension stock vs thin equity 63m — FOI-adjacent L5 residual",
    "priority": "8",
    "recipient_body": "Stad Geraardsbergen / financieel directeur / openbaarheid",
    "recipient_email": "info@geraardsbergen.be",
    "recipient_postal": "https://www.geraardsbergen.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_geraardsbergen_debt_loans_l5.md",
    "status": "ready",
    "date_ready": "2026-08-06",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_gb_fin_debt_51m_2025",
    "linked_leaderboard_id": "lb_gb_fin_debt_51m_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick858 primary JR2025; ready draft; do not send; prio8 debt intensity",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_848":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick858 Geraardsbergen JR2025 dual Heist; assets 159m fin debt 51m AFM +5.6m"
        print("rq_848 done")
        break

if not any(r["task_id"] == "rq_849" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_849",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Geraardsbergen JR2025 filled tick858; residual Roeselare portal/Lier portal/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick858 after Geraardsbergen dual Heist",
    })
    print("spawned rq_849")

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
        r["last_unit_id"] = "rq_848"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick858 Geraardsbergen JR2025 dual Heist; FOI gap_geraardsbergen_debt_loans_l5; next rq_849 residual dual L5; progress@860 in 2; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

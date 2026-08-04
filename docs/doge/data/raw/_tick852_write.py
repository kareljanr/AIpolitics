import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-05T23:00:00Z"
TICK = 852
SRC = "src_landen_jr2025"
SRC_DUAL = "src_dual_landen_ieper_tick852"
EID = "city_landen"


def append_csv(path, rows, fieldnames=None):
    p = Path(path)
    with p.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        existing_fields = reader.fieldnames
        existing = list(reader)
    if fieldnames is None:
        fieldnames = existing_fields
    key = fieldnames[0]
    existing_ids = {r[key] for r in existing}
    new = [r for r in rows if r[key] not in existing_ids]
    if not new:
        print(f"{path}: nothing new")
        return 0
    with p.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        for r in new:
            out = {k: r.get(k, "") for k in fieldnames}
            w.writerow(out)
    print(f"{path}: +{len(new)}")
    return len(new)


budgets = [
    ("bud_ld_assets_2025", 101347443, "Consol stad+OCMW total assets YE2025 101.347m; tick852"),
    ("bud_ld_equity_2025", 65035061, "Nettoactief YE2025 65.035m; tick852"),
    ("bud_ld_debt_total_2025", 36312382, "Total schulden YE2025 36.312m; tick852"),
    ("bud_ld_fin_debt_2025", 27046050, "T4 total financiele schulden YE2025 27.046m (LT 24.784 + ST due 2.262); tick852"),
    ("bud_ld_fin_debt_lt_2025", 24784088, "Financiele schulden LT YE2025 24.784m; tick852"),
    ("bud_ld_fin_debt_st_due_2025", 2261962, "Schulden LT vervallend binnen jaar YE2025 2.262m; tick852"),
    ("bud_ld_pension_prov_2025", 2664447, "Pensioenvoorzieningen LT YE2025 2.664m; tick852"),
    ("bud_ld_cash_2025", 13504702, "Liquide middelen YE2025 13.505m; tick852"),
    ("bud_ld_cap_subs_2025", 18803999, "Kapitaalsubsidies YE2025 18.804m; tick852"),
    ("bud_ld_fva_total_2025", 9311357, "Financiele vaste activa YE2025 9.311m; tick852"),
    ("bud_ld_fva_igs_2025", 8399643, "Fin VA IGS YE2025 8.400m; tick852"),
    ("bud_ld_mva_2025", 63849681, "Materiele vaste activa YE2025 63.850m; tick852"),
    ("bud_ld_onbeschikbaar_2025", 981393, "Onbeschikbare gelden J2 0.981m; tick852"),
    ("bud_ld_expl_rec_2025", 40341787, "Exploitatieontvangsten 40.342m; tick852"),
    ("bud_ld_expl_exp_2025", 35649256, "Exploitatieuitgaven 35.649m; tick852"),
    ("bud_ld_expl_saldo_2025", 4692531, "Exploitatiesaldo +4.693m; tick852"),
    ("bud_ld_invest_exp_2025", 4100474, "Investeringsuitgaven J2 4.100m; tick852"),
    ("bud_ld_invest_rec_2025", 1573928, "Investeringsontvangsten J2 1.574m; tick852"),
    ("bud_ld_invest_saldo_2025", -2526547, "Investeringssaldo -2.527m; tick852"),
    ("bud_ld_fin_rec_2025", 293725, "Financieringsontvangsten 0.294m; tick852"),
    ("bud_ld_fin_exp_2025", 2458846, "Financieringsuitgaven 2.459m; tick852"),
    ("bud_ld_new_loans_2025", 95820, "Nieuwe leningen 0.096m (other entities only); tick852"),
    ("bud_ld_aflossingen_2025", 2458846, "Periodieke aflossingen 2.459m; tick852"),
    ("bud_ld_afm_2025", 2769248, "AFM +2.769m; tick852"),
    ("bud_ld_afm_corr_2025", 2875367, "Gecorrigeerde AFM +2.875m; tick852"),
    ("bud_ld_bbr_2025", 15045123, "BBR 15.045m after onbeschikbaar 0.981m; tick852"),
    ("bud_ld_budget_result_2025", 864, "Budgettair resultaat boekjaar +0.001m; tick852"),
    ("bud_ld_cum_br_2025", 16026516, "Gecumuleerd budgettair resultaat 16.027m; tick852"),
    ("bud_ld_pnl_result_2025", 1835844, "Vennootschapsresultaat J5 +1.836m; tick852"),
    ("bud_ld_personnel_2025", 19613100, "J5/T2 bezoldigingen 19.613m; tick852"),
    ("bud_ld_toelagen_2025", 5011739, "Toegestane werkingssubsidies 5.012m (politie 2.284 fire 0.958 AGB 0.243 other 1.129); tick852"),
    ("bud_ld_ocmw_aid_2025", 2244031, "OCMW individuele hulp 2.244m; tick852"),
    ("bud_ld_fiscal_2025", 16577712, "J5 fiscale opbrengsten en boetes 16.578m; tick852"),
    ("bud_ld_werk_subs_rec_2025", 13792222, "J5 werkingssubsidies ontvangen 13.792m; tick852"),
    ("bud_ld_gemeentefonds_2025", 5091386, "Gemeentefonds 5.091m; tick852"),
    ("bud_ld_fin_costs_2025", 615582, "J5 financiele kosten 0.616m; tick852"),
    ("bud_ld_police_toelage_2025", 2284400, "Toelage politiezone 2.284m; tick852"),
    ("bud_ld_fire_toelage_2025", 957576, "Toelage hulpverleningszone 0.958m; tick852"),
]
budget_rows = []
for bid, amt, notes in budgets:
    budget_rows.append({
        "budget_id": bid,
        "entity_id": EID,
        "year": "2025",
        "amount_eur": str(amt),
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": SRC,
        "confidence": "strong",
        "notes": notes,
    })
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_ld_balance_101m_2025",
        "title": "Landen consol stad+OCMW balance YE2025 assets 101.3m",
        "entity_id": EID,
        "beneficiary": "Stad+OCMW Landen",
        "legal_basis": "BBC DLB jaarrekening",
        "decision_date": "2026-06-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "101347443",
        "cash_by_year": "2025:101347443",
        "remaining_eur": "0",
        "status": "outturn",
        "evaluation_url": "https://www.landen.be/stad-landen---ocmw---jaarrekening-2025",
        "stated_goal": "Municipal balance sheet",
        "cut_option": "Debt/subs FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen",
        "notes": "tick852 primary JR2025 GR 25.06.2026",
    },
    {
        "commitment_id": "cmt_ld_expl_40m_2025",
        "title": "Landen exploitation receipts 40.3m expenses 35.6m 2025",
        "entity_id": EID,
        "beneficiary": "Stad+OCMW Landen",
        "legal_basis": "BBC",
        "decision_date": "2026-06-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "40341787",
        "cash_by_year": "2025:40341787",
        "remaining_eur": "0",
        "status": "outturn",
        "evaluation_url": "https://www.landen.be/stad-landen---ocmw---jaarrekening-2025",
        "stated_goal": "Municipal operations",
        "cut_option": "Toelagen FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>exploitatie",
        "notes": "tick852",
    },
    {
        "commitment_id": "cmt_ld_fin_debt_27m_2025",
        "title": "Landen financial debt stock 27.0m YE2025",
        "entity_id": EID,
        "beneficiary": "creditors",
        "legal_basis": "BBC debt",
        "decision_date": "2026-06-25",
        "start_year": "2025",
        "end_year": "2035",
        "total_envelope_eur": "27046050",
        "cash_by_year": "2025stock:27046050",
        "remaining_eur": "27046050",
        "status": "stock",
        "evaluation_url": "https://www.landen.be/stad-landen---ocmw---jaarrekening-2025",
        "stated_goal": "Capital finance",
        "cut_option": "Lender schedule FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>debt",
        "notes": "tick852; fin debt ~same class as Ieper on ~3x smaller assets",
    },
    {
        "commitment_id": "cmt_ld_afm_bbr_2025",
        "title": "Landen AFM +2.8m and BBR 15.0m 2025",
        "entity_id": EID,
        "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht",
        "decision_date": "2026-06-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "15045123",
        "cash_by_year": "2025BBR:15045123;AFM:2769248;onbeschikbaar:981393",
        "remaining_eur": "0",
        "status": "outturn",
        "evaluation_url": "https://www.landen.be/stad-landen---ocmw---jaarrekening-2025",
        "stated_goal": "Financial equilibrium",
        "cut_option": "Named other toelagen FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>AFM",
        "notes": "tick852 solid AFM; low onbeschikbaar vs Ieper",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_ld_personnel_20m_2025",
        "name": "Landen personnel/bezold 19.6m 2025",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>personeel",
        "annual_cost_eur": "19613100",
        "total_cost_eur": "19613100",
        "tco_notes": "Strong; dual Ieper 35.6m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Staff Stad+OCMW Landen",
        "stated_goal": "Local public services",
        "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5",
        "cost_score": "4.5",
        "difficulty": "7.0",
        "priority_index": "4.0",
        "cut_proposal": "Headcount FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick852",
    },
    {
        "item_id": "lb_ld_toelagen_5m_2025",
        "name": "Landen toelagen 5.0m 2025 (police 2.3 fire 1.0 AGB 0.2 other 1.1)",
        "level": "L5",
        "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>toelagen",
        "annual_cost_eur": "5011739",
        "total_cost_eur": "5011739",
        "tco_notes": "Strong; dual Ieper 11.6m; other 1.1m FOI-adjacent",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "PZ + zone + AGB + other",
        "stated_goal": "Statutory transfers",
        "measured_outcome": "T2 named buckets",
        "absurdity_score": "4.0",
        "cost_score": "4.0",
        "difficulty": "5.5",
        "priority_index": "4.0",
        "cut_proposal": "Named matrix FOI >=50k other",
        "status": "active",
        "struck_reason": "",
        "notes": "tick852",
    },
    {
        "item_id": "lb_ld_afm_3m_2025",
        "name": "Landen AFM +2.8m BBR 15.0m 2025",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>AFM",
        "annual_cost_eur": "0",
        "total_cost_eur": "2769248",
        "tco_notes": "Strong positive AFM; dual Ieper +16.0m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Taxpayers Landen",
        "stated_goal": "Fiscal equilibrium",
        "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0",
        "cost_score": "4.0",
        "difficulty": "4.0",
        "priority_index": "3.5",
        "cut_proposal": "Sustain FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick852 positive",
    },
    {
        "item_id": "lb_ld_fin_debt_27m_2025",
        "name": "Landen fin debt stock 27.0m YE2025 (high vs 101m assets)",
        "level": "L5",
        "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>debt",
        "annual_cost_eur": "605077",
        "total_cost_eur": "27046050",
        "tco_notes": "Strong; ~same fin debt class as Ieper (24m) on ~3x smaller assets; declining from 29.4m YE2024",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance",
        "measured_outcome": "T4 stock declining",
        "absurdity_score": "5.5",
        "cost_score": "5.0",
        "difficulty": "5.5",
        "priority_index": "5.25",
        "cut_proposal": "Lender FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick852 stock FOI-adjacent",
    },
    {
        "item_id": "lb_ld_ocmw_aid_2m_2025",
        "name": "Landen OCMW individual aid 2.2m 2025",
        "level": "L5",
        "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Landen>OCMW",
        "annual_cost_eur": "2244031",
        "total_cost_eur": "2244031",
        "tco_notes": "Strong; dual Ieper 6.5m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net",
        "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0",
        "cost_score": "3.5",
        "difficulty": "7.0",
        "priority_index": "3.25",
        "cut_proposal": "Outcomes FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick852 safety-net",
    },
    {
        "item_id": "lb_ld_debt_intensity_vs_ieper",
        "name": "Landen fin debt/assets intensity vs Ieper (27m/101m vs 24m/333m)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities>debt_intensity",
        "annual_cost_eur": "0",
        "total_cost_eur": "27046050",
        "tco_notes": "Strong dual ratio insight not TE-additive; Landen ~27% fin-debt/assets vs Ieper ~7%",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "Comparative fiscal",
        "stated_goal": "Debt transparency dual",
        "measured_outcome": "JR2025 both cities",
        "absurdity_score": "6.0",
        "cost_score": "5.0",
        "difficulty": "5.0",
        "priority_index": "5.5",
        "cut_proposal": "Cross FOI lenders",
        "status": "active",
        "struck_reason": "",
        "notes": "tick852 dual ratio",
    },
    {
        "item_id": "lb_dual_landen_ieper_tick852",
        "name": "Dual Landen 101m vs Ieper 333m city residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0",
        "total_cost_eur": "101347443",
        "tco_notes": "Strong dual not TE-additive; Landen compact AFM +2.8m vs Ieper high cash/AFM +16m",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "VL mid/small cities",
        "stated_goal": "Residual dual hole-fill",
        "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.0",
        "cost_score": "5.5",
        "difficulty": "5.0",
        "priority_index": "4.75",
        "cut_proposal": "Cross FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick852",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Stad+OCMW Landen Jaarrekening 2025 (BBC consolidatie, 107p)",
        "url": "https://www.landen.be/stad-landen---ocmw---jaarrekening-2025",
        "publisher": "Stad Landen",
        "accessed_date": "2026-08-05",
        "source_class": "primary_jaarrekening",
        "notes": "GR/RMW 2026-06-25 published 2026-06-30; assets 101.3m equity 65.0m cash 13.5m expl 40.3/35.6m AFM +2.8m BBR 15.0m fin debt 27.0m personnel 19.6m toelagen 5.0m; tick852",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Landen JR2025 vs Ieper JR2025 tick852",
        "url": "https://www.landen.be/stad-landen---ocmw---jaarrekening-2025",
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-05",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Landen 101m vs Ieper 333m; similar fin debt stock class; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Stad Landen",
    "name_fr": "Ville de Landen",
    "name_en": "City of Landen",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.landen.be",
    "foi_email": "info@landen.be",
    "foi_postal": "Stationsstraat 29 3400 Landen",
    "notes": "JR2025 assets 101m equity 65m cash 13.5m expl 40/36m personnel 20m fin debt 27m AFM +2.8m BBR 15m toelagen 5.0m; tick852",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_landen_debt_subs_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Landen_L5",
    "entity_id": EID,
    "what_is_missing": "Full lender schedule for fin debt 27.0m (declining from 29.4m); named toelagen matrix for other beneficiaries within 1.13m of 5.01m package; AGB Landen full JR2025 (only consol BBR 0.14m / AFM 11k known); new loans path 2027 5.2m bank planned",
    "why_it_matters": "101m city+OCMW with fin debt intensity ~27pct of assets vs Ieper ~7pct on similar absolute debt class; residual L5 opacity on other grants + AGB",
    "priority": "7",
    "recipient_body": "Stad Landen / financieel directeur / openbaarheid",
    "recipient_email": "info@landen.be",
    "recipient_postal": "https://www.landen.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_landen_debt_subs_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_ld_fin_debt_27m_2025",
    "linked_leaderboard_id": "lb_ld_fin_debt_27m_2025",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "tick852 primary JR2025; ready draft; do not send",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

updated = False
for r in rq_rows:
    if r["task_id"] == "rq_842":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick852 Landen JR2025 dual Ieper; assets 101m fin debt 27m AFM +2.8m"
        updated = True
        break
print("rq_842 updated", updated)

if not any(r["task_id"] == "rq_843" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_843",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Landen JR2025 filled tick852; residual Roeselare portal/Lier/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick852 after Landen dual Ieper",
    })
    print("spawned rq_843")

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
        r["last_unit_id"] = "rq_842"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick852 Landen JR2025 dual Ieper; FOI gap_landen_debt_subs_l5; next rq_843 residual dual L5; progress@860 in 8; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("loop_state updated ticks=", TICK)
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

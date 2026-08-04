import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-06T02:30:00Z"
TICK = 859
SRC = "src_aarschot_jr2025"
SRC_DUAL = "src_dual_aarschot_geraardsbergen_tick859"
EID = "city_aarschot"
URL = "https://www.aarschot.be/jaarrekening-2026"


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
    ("bud_aa_assets_2025", 172190782, "Consol stad+OCMW total assets YE2025 172.191m; tick859"),
    ("bud_aa_equity_2025", 90340111, "Nettoactief YE2025 90.340m; tick859"),
    ("bud_aa_debt_total_2025", 81850670, "Total schulden YE2025 81.851m; tick859"),
    ("bud_aa_fin_debt_2025", 43274240, "T4 total financiele schulden YE2025 43.274m (LT 40.661 + ST due 2.614); tick859"),
    ("bud_aa_fin_debt_lt_2025", 40660620, "Financiele schulden LT YE2025 40.661m; tick859"),
    ("bud_aa_fin_debt_st_due_2025", 2613620, "Schulden LT vervallend binnen jaar YE2025 2.614m; tick859"),
    ("bud_aa_pension_prov_2025", 27496157, "Pensioenvoorzieningen LT YE2025 27.496m; tick859"),
    ("bud_aa_cash_2025", 6576384, "Liquide middelen YE2025 6.576m; tick859"),
    ("bud_aa_cap_subs_2025", 17901949, "Kapitaalsubsidies YE2025 17.902m; tick859"),
    ("bud_aa_fva_total_2025", 32697238, "Financiele vaste activa YE2025 32.697m; tick859"),
    ("bud_aa_fva_igs_2025", 27592610, "Fin VA IGS YE2025 27.593m; tick859"),
    ("bud_aa_mva_2025", 110129206, "Materiele vaste activa YE2025 110.129m; tick859"),
    ("bud_aa_onbeschikbaar_2025", 0, "Onbeschikbare gelden J2 0 (BBR=cum BR); tick859"),
    ("bud_aa_expl_rec_2025", 78904207, "Exploitatieontvangsten 78.904m; tick859"),
    ("bud_aa_expl_exp_2025", 72123411, "Exploitatieuitgaven 72.123m; tick859"),
    ("bud_aa_expl_saldo_2025", 6780796, "Exploitatiesaldo +6.781m; tick859"),
    ("bud_aa_invest_exp_2025", 16601343, "Investeringsuitgaven J2 16.601m; tick859"),
    ("bud_aa_invest_rec_2025", 488126, "Investeringsontvangsten J2 0.488m; tick859"),
    ("bud_aa_invest_saldo_2025", -16113217, "Investeringssaldo -16.113m; tick859"),
    ("bud_aa_fin_rec_2025", 11104651, "Financieringsontvangsten 11.105m; tick859"),
    ("bud_aa_fin_exp_2025", 2939839, "Financieringsuitgaven 2.940m; tick859"),
    ("bud_aa_new_loans_2025", 9791855, "Nieuwe leningen 9.792m; tick859"),
    ("bud_aa_aflossingen_2025", 2290105, "Periodieke aflossingen 2.290m; tick859"),
    ("bud_aa_afm_2025", 5051757, "AFM +5.052m; tick859"),
    ("bud_aa_afm_corr_2025", 4477408, "Gecorrigeerde AFM +4.477m; tick859"),
    ("bud_aa_bbr_2025", 9302520, "BBR 9.303m (onbeschikbaar 0); tick859"),
    ("bud_aa_budget_result_2025", -1167610, "Budgettair resultaat boekjaar -1.168m; tick859"),
    ("bud_aa_cum_br_2025", 9302520, "Gecumuleerd budgettair resultaat 9.303m; tick859"),
    ("bud_aa_pnl_result_2025", 1843427, "Vennootschapsresultaat J5 +1.843m; tick859"),
    ("bud_aa_personnel_2025", 42438696, "J5/T2 bezoldigingen 42.439m (incl onderwijs other-gov 8.115m); tick859"),
    ("bud_aa_toelagen_2025", 10052947, "Toegestane werkingssubsidies 10.053m (politie 5.476 fire 1.657 AGB 1.400 other 1.331); tick859"),
    ("bud_aa_ocmw_aid_2025", 3994134, "OCMW individuele hulp 3.994m; tick859"),
    ("bud_aa_fiscal_2025", 32258026, "J5 fiscale opbrengsten en boetes 32.258m; tick859"),
    ("bud_aa_werk_subs_rec_2025", 32387189, "J5 werkingssubsidies ontvangen 32.387m; tick859"),
    ("bud_aa_gemeentefonds_2025", 11881729, "Gemeentefonds 11.882m; tick859"),
    ("bud_aa_fin_costs_2025", 1131077, "J5 financiele kosten 1.131m; tick859"),
    ("bud_aa_police_toelage_2025", 5475877, "Toelage politiezone 5.476m; tick859"),
    ("bud_aa_fire_toelage_2025", 1656889, "Toelage hulpverleningszone 1.657m; tick859"),
]
budget_rows = [{
    "budget_id": bid, "entity_id": EID, "year": "2025",
    "amount_eur": str(amt), "amount_min_eur": "", "amount_max_eur": "",
    "basis": "outturn", "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, amt, notes in budgets]
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_aa_balance_172m_2025",
        "title": "Aarschot consol stad+OCMW balance YE2025 assets 172.2m",
        "entity_id": EID, "beneficiary": "Stad+OCMW Aarschot",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-05-21",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "172190782", "cash_by_year": "2025:172190782",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal balance sheet", "cut_option": "Debt FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot",
        "notes": "tick859 primary JR2025 GR 21.05.2026 pub 29.05.2026",
    },
    {
        "commitment_id": "cmt_aa_expl_79m_2025",
        "title": "Aarschot exploitation receipts 78.9m expenses 72.1m 2025",
        "entity_id": EID, "beneficiary": "Stad+OCMW Aarschot",
        "legal_basis": "BBC", "decision_date": "2026-05-21",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "78904207", "cash_by_year": "2025:78904207",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal operations", "cut_option": "Toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>exploitatie",
        "notes": "tick859",
    },
    {
        "commitment_id": "cmt_aa_fin_debt_43m_2025",
        "title": "Aarschot financial debt stock 43.3m YE2025 (new loans 9.8m)",
        "entity_id": EID, "beneficiary": "creditors",
        "legal_basis": "BBC debt", "decision_date": "2026-05-21",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "43274240", "cash_by_year": "2025stock:43274240;new:9791855",
        "remaining_eur": "43274240", "status": "stock", "evaluation_url": URL,
        "stated_goal": "Capital finance", "cut_option": "Lender schedule FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>debt",
        "notes": "tick859 rising from 35.8m YE2024; invest 16.6m",
    },
    {
        "commitment_id": "cmt_aa_afm_bbr_2025",
        "title": "Aarschot AFM +5.1m and BBR 9.3m 2025",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-05-21",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "9302520",
        "cash_by_year": "2025BBR:9302520;AFM:5051757;new_loans:9791855",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Financial equilibrium", "cut_option": "Debt FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>AFM",
        "notes": "tick859 solid AFM; debt jump FOI-adjacent",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_aa_personnel_42m_2025",
        "name": "Aarschot personnel/bezold 42.4m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>personeel",
        "annual_cost_eur": "42438696", "total_cost_eur": "42438696",
        "tco_notes": "Strong; dual Geraardsbergen 43.4m; incl other-gov onderwijs 8.1m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff Stad+OCMW",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "5.5", "difficulty": "7.0",
        "priority_index": "4.5", "cut_proposal": "Headcount FOI",
        "status": "active", "struck_reason": "", "notes": "tick859",
    },
    {
        "item_id": "lb_aa_toelagen_10m_2025",
        "name": "Aarschot toelagen 10.1m 2025 (police 5.5 fire 1.7 AGB 1.4 other 1.3)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>toelagen",
        "annual_cost_eur": "10052947", "total_cost_eur": "10052947",
        "tco_notes": "Strong; dual Geraardsbergen 8.8m; other 1.3m FOI-adjacent",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + fire + AGB + other",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2 buckets",
        "absurdity_score": "4.0", "cost_score": "5.0", "difficulty": "5.5",
        "priority_index": "4.5", "cut_proposal": "Named matrix FOI other",
        "status": "active", "struck_reason": "", "notes": "tick859",
    },
    {
        "item_id": "lb_aa_afm_5m_2025",
        "name": "Aarschot AFM +5.1m BBR 9.3m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "5051757",
        "tco_notes": "Strong positive; dual Geraardsbergen +5.6m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Aarschot",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "5.0", "difficulty": "4.0",
        "priority_index": "4.0", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick859 positive",
    },
    {
        "item_id": "lb_aa_fin_debt_43m_2025",
        "name": "Aarschot fin debt stock 43.3m YE2025 (new loans 9.8m; invest 16.6m)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>debt",
        "annual_cost_eur": "1114728", "total_cost_eur": "43274240",
        "tco_notes": "Strong rising 35.8to43.3m; dual Geraardsbergen 50.7m; FOI-adjacent new loans",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance invest", "measured_outcome": "T4 rising",
        "absurdity_score": "5.5", "cost_score": "5.5", "difficulty": "5.5",
        "priority_index": "5.5", "cut_proposal": "Lender FOI",
        "status": "active", "struck_reason": "", "notes": "tick859 stock FOI-adjacent",
    },
    {
        "item_id": "lb_aa_pension_27m_2025",
        "name": "Aarschot pension provisions 27.5m YE2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>pension",
        "annual_cost_eur": "0", "total_cost_eur": "27496157",
        "tco_notes": "Strong stock; dual Geraardsbergen 29.8m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Former/current staff",
        "stated_goal": "Pension liability", "measured_outcome": "J4 provisions",
        "absurdity_score": "5.0", "cost_score": "5.0", "difficulty": "6.0",
        "priority_index": "5.0", "cut_proposal": "Composition FOI",
        "status": "active", "struck_reason": "", "notes": "tick859 stock",
    },
    {
        "item_id": "lb_aa_ocmw_aid_4m_2025",
        "name": "Aarschot OCMW individual aid 4.0m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot>OCMW",
        "annual_cost_eur": "3994134", "total_cost_eur": "3994134",
        "tco_notes": "Strong; dual Geraardsbergen 4.8m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0", "cost_score": "3.5", "difficulty": "7.0",
        "priority_index": "3.25", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick859 safety-net",
    },
    {
        "item_id": "lb_dual_aarschot_geraardsbergen_tick859",
        "name": "Dual Aarschot 172m vs Geraardsbergen 159m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "172190782",
        "tco_notes": "Strong dual not TE-additive; both elevated debt stocks with solid AFM",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.5", "cost_score": "5.5", "difficulty": "5.0",
        "priority_index": "5.0", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick859",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Stad+OCMW Aarschot Jaarrekening 2025 (BBC consolidatie, 200p)",
        "url": URL,
        "publisher": "Stad Aarschot",
        "accessed_date": "2026-08-06",
        "source_class": "primary_jaarrekening",
        "notes": "GR 2026-05-21 pub 2026-05-29; assets 172.2m equity 90.3m cash 6.6m expl 78.9/72.1m AFM +5.1m BBR 9.3m fin debt 43.3m new loans 9.8m invest 16.6m personnel 42.4m toelagen 10.1m; tick859",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Aarschot JR2025 vs Geraardsbergen JR2025 tick859",
        "url": URL,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-06",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Aarschot 172m vs Geraardsbergen 159m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Stad Aarschot",
    "name_fr": "Ville d'Aarschot",
    "name_en": "City of Aarschot",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.aarschot.be",
    "foi_email": "info@aarschot.be",
    "foi_postal": "Stadhuis Aarschot",
    "notes": "JR2025 assets 172m equity 90m cash 6.6m expl 79/72m personnel 42m fin debt 43m new loans 9.8m invest 17m AFM +5.1m BBR 9.3m toelagen 10m; tick859",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_aarschot_debt_loans_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Aarschot_L5",
    "entity_id": EID,
    "what_is_missing": "Lender schedule for fin debt 43.274m and new loans 9.792m (invest 16.601m); named toelagen matrix for other 1.331m within 10.053m; AGB Aarschot full JR2025 (consol BBR 0.744m / AFM 0.187m / gecorr AFM -0.233m); pension composition 27.496m",
    "why_it_matters": "172m city+OCMW with solid AFM +5.1m but debt stock jump 35.8to43.3m and large new loans needs L5 transparency",
    "priority": "7",
    "recipient_body": "Stad Aarschot / financieel directeur / openbaarheid",
    "recipient_email": "info@aarschot.be",
    "recipient_postal": "https://www.aarschot.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_aarschot_debt_loans_l5.md",
    "status": "ready",
    "date_ready": "2026-08-06",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_aa_fin_debt_43m_2025",
    "linked_leaderboard_id": "lb_aa_fin_debt_43m_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick859 primary JR2025; ready draft; do not send",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_849":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick859 Aarschot JR2025 dual Geraardsbergen; assets 172m fin debt 43m new loans 9.8m"
        print("rq_849 done")
        break

if not any(r["task_id"] == "rq_860" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_860",
        "title": "MANDATORY progress@860 coverage % layers A-E + waste top10 refresh",
        "sprint": "hole_fill",
        "priority": "10",
        "status": "open",
        "hierarchy_target": "L0-L5",
        "entity_id": "gg_belgium",
        "instructions": "Mandatory progress@860: refresh progress_every_10_ticks.md (layers A-E % of EUR347.956bn TE) and doge_waste_top10_current.md (top 10 by priority_index); note recent VL city fills 851-859; no invented euros",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick859 for progress@860 NEXT",
    })
    print("spawned rq_860 progress")

if not any(r["task_id"] == "rq_851" for r in rq_rows if r["task_id"] == "rq_851"):
    # spawn residual after progress - use rq_861 to avoid clash with old numbering
    pass

if not any(r["task_id"] == "rq_861" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_861",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual after progress@860: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Aarschot JR2025 filled tick859; residual Roeselare portal/Lier portal/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick859 after Aarschot dual Geraardsbergen; after progress",
    })
    print("spawned rq_861")

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
        r["last_unit_id"] = "rq_849"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick859 Aarschot JR2025 dual Geraardsbergen; FOI gap_aarschot_debt_loans_l5; next progress@860 rq_860 THEN rq_861 residual; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

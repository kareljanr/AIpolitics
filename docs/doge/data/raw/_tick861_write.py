import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-06T03:30:00Z"
TICK = 861
SRC = "src_koksijde_jr2025"
SRC_DUAL = "src_dual_koksijde_aarschot_tick861"
EID = "city_koksijde"
URL = "https://www.koksijde.be/nl/menu/gemeente-bestuur/bestuur/bekendmakingen-en-reglementen/beleidsdocumenten/gemeente-en-ocmw/jaarrekening-gemeente-en-ocmw"


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
    ("bud_kx_assets_2025", 330404427, "Consol gemeente+OCMW total assets YE2025 330.404m; tick861"),
    ("bud_kx_equity_2025", 216485888, "Nettoactief YE2025 216.486m; tick861"),
    ("bud_kx_debt_total_2025", 113918539, "Total schulden YE2025 113.919m; tick861"),
    ("bud_kx_fin_debt_2025", 77761004, "T4 total financiele schulden YE2025 77.761m (LT 69.942 + ST due 7.819); tick861"),
    ("bud_kx_fin_debt_lt_2025", 69942217, "Financiele schulden LT YE2025 69.942m; tick861"),
    ("bud_kx_fin_debt_st_due_2025", 7818787, "Schulden LT vervallend binnen jaar YE2025 7.819m; tick861"),
    ("bud_kx_pension_prov_2025", 15605262, "Pensioenvoorzieningen LT YE2025 15.605m; tick861"),
    ("bud_kx_cash_2025", 16515522, "Liquide middelen YE2025 16.516m (was 5.680m); tick861"),
    ("bud_kx_cap_subs_2025", 30260798, "Kapitaalsubsidies YE2025 30.261m; tick861"),
    ("bud_kx_fva_total_2025", 36124550, "Financiele vaste activa YE2025 36.125m; tick861"),
    ("bud_kx_fva_igs_2025", 31487684, "Fin VA IGS YE2025 31.488m; tick861"),
    ("bud_kx_mva_2025", 260097080, "Materiele vaste activa YE2025 260.097m; tick861"),
    ("bud_kx_onbeschikbaar_2025", 0, "Onbeschikbare gelden J2 0; tick861"),
    ("bud_kx_expl_rec_2025", 90299459, "Exploitatieontvangsten 90.299m; tick861"),
    ("bud_kx_expl_exp_2025", 72265983, "Exploitatieuitgaven 72.266m; tick861"),
    ("bud_kx_expl_saldo_2025", 18033475, "Exploitatiesaldo +18.033m (very strong); tick861"),
    ("bud_kx_invest_exp_2025", 19732482, "Investeringsuitgaven J2 19.732m; tick861"),
    ("bud_kx_invest_rec_2025", 3495748, "Investeringsontvangsten J2 3.496m; tick861"),
    ("bud_kx_invest_saldo_2025", -16236734, "Investeringssaldo -16.237m; tick861"),
    ("bud_kx_fin_rec_2025", 24769159, "Financieringsontvangsten 24.769m; tick861"),
    ("bud_kx_fin_exp_2025", 7950916, "Financieringsuitgaven 7.951m; tick861"),
    ("bud_kx_new_loans_2025", 24528293, "Nieuwe leningen 24.528m (large); tick861"),
    ("bud_kx_aflossingen_2025", 7950916, "Periodieke aflossingen 7.951m; tick861"),
    ("bud_kx_afm_2025", 10323425, "AFM +10.323m (very strong); tick861"),
    ("bud_kx_afm_corr_2025", 12979651, "Gecorrigeerde AFM +12.980m; tick861"),
    ("bud_kx_bbr_2025", 13182615, "BBR 13.183m after onbeschikbaar 0; tick861"),
    ("bud_kx_budget_result_2025", 18614985, "Budgettair resultaat boekjaar +18.615m; tick861"),
    ("bud_kx_cum_br_2025", 13182615, "Gecumuleerd budgettair resultaat 13.183m (was -5.432m YE2024); tick861"),
    ("bud_kx_pnl_result_2025", 4469414, "Vennootschapsresultaat J5 +4.469m; tick861"),
    ("bud_kx_personnel_2025", 41306333, "J5/T2 bezoldigingen 41.306m (incl onderwijs other-gov 4.780m); tick861"),
    ("bud_kx_toelagen_2025", 10317935, "Toegestane werkingssubsidies 10.318m (politie 5.885 fire 1.118 other 2.779); tick861"),
    ("bud_kx_ocmw_aid_2025", 1438974, "OCMW individuele hulp 1.439m; tick861"),
    ("bud_kx_fiscal_2025", 57967199, "J5 fiscale opbrengsten en boetes 57.967m (coastal/tourist); tick861"),
    ("bud_kx_werk_subs_rec_2025", 21994329, "J5 werkingssubsidies ontvangen 21.994m; tick861"),
    ("bud_kx_gemeentefonds_2025", 5515653, "Gemeentefonds 5.516m; tick861"),
    ("bud_kx_fin_costs_2025", 2707988, "J5 financiele kosten 2.708m; tick861"),
    ("bud_kx_police_toelage_2025", 5885303, "Toelage politiezone 5.885m; tick861"),
    ("bud_kx_fire_toelage_2025", 1117626, "Toelage hulpverleningszone 1.118m; tick861"),
    ("bud_kx_mjp2026_new_loans_plan", 25057041, "MJP planned new loans 2026 25.057m; tick861"),
]
budget_rows = [{
    "budget_id": bid, "entity_id": EID, "year": "2025" if "mjp2026" not in bid else "2026",
    "amount_eur": str(amt), "amount_min_eur": "", "amount_max_eur": "",
    "basis": "outturn" if "mjp2026" not in bid else "budgeted",
    "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, amt, notes in budgets]
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_kx_balance_330m_2025",
        "title": "Koksijde consol gemeente+OCMW balance YE2025 assets 330.4m",
        "entity_id": EID, "beneficiary": "Gemeente+OCMW Koksijde",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "330404427", "cash_by_year": "2025:330404427",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal balance sheet", "cut_option": "Debt FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde",
        "notes": "tick861 primary JR2025 pub 25.06.2026 class",
    },
    {
        "commitment_id": "cmt_kx_expl_90m_2025",
        "title": "Koksijde exploitation receipts 90.3m expenses 72.3m 2025",
        "entity_id": EID, "beneficiary": "Gemeente+OCMW Koksijde",
        "legal_basis": "BBC", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "90299459", "cash_by_year": "2025:90299459",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal operations", "cut_option": "Toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>exploitatie",
        "notes": "tick861; fiscal 58.0m coastal",
    },
    {
        "commitment_id": "cmt_kx_fin_debt_78m_2025",
        "title": "Koksijde financial debt stock 77.8m YE2025 (new loans 24.5m)",
        "entity_id": EID, "beneficiary": "creditors",
        "legal_basis": "BBC debt", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "77761004", "cash_by_year": "2025stock:77761004;new:24528293",
        "remaining_eur": "77761004", "status": "stock", "evaluation_url": URL,
        "stated_goal": "Capital finance", "cut_option": "Lender schedule FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>debt",
        "notes": "tick861 rising 66.2to77.8m; MJP2026 plan +25m more FOI-adjacent",
    },
    {
        "commitment_id": "cmt_kx_afm_bbr_2025",
        "title": "Koksijde AFM +10.3m BBR 13.2m fiscal 58.0m 2025",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "13182615",
        "cash_by_year": "2025BBR:13182615;AFM:10323425;fiscal:57967199;new_loans:24528293",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Financial equilibrium", "cut_option": "Debt path FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>AFM",
        "notes": "tick861 very strong AFM+expl; debt jump FOI-adjacent",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_kx_personnel_41m_2025",
        "name": "Koksijde personnel/bezold 41.3m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>personeel",
        "annual_cost_eur": "41306333", "total_cost_eur": "41306333",
        "tco_notes": "Strong; dual Aarschot 42.4m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff gemeente+OCMW",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "5.5", "difficulty": "7.0",
        "priority_index": "4.5", "cut_proposal": "Headcount FOI",
        "status": "active", "struck_reason": "", "notes": "tick861",
    },
    {
        "item_id": "lb_kx_toelagen_10m_2025",
        "name": "Koksijde toelagen 10.3m 2025 (police 5.9 fire 1.1 other 2.8)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>toelagen",
        "annual_cost_eur": "10317935", "total_cost_eur": "10317935",
        "tco_notes": "Strong; dual Aarschot 10.1m; other 2.8m FOI-adjacent",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + fire + other",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2 buckets",
        "absurdity_score": "4.0", "cost_score": "5.0", "difficulty": "5.5",
        "priority_index": "4.5", "cut_proposal": "Named matrix FOI other",
        "status": "active", "struck_reason": "", "notes": "tick861",
    },
    {
        "item_id": "lb_kx_afm_10m_2025",
        "name": "Koksijde AFM +10.3m BBR 13.2m fiscal 58.0m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "10323425",
        "tco_notes": "Strong top-tier coastal AFM; dual Heist +10.8m Aarschot +5.1m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Koksijde",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "6.0", "difficulty": "4.0",
        "priority_index": "4.5", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick861 positive",
    },
    {
        "item_id": "lb_kx_fin_debt_78m_2025",
        "name": "Koksijde fin debt stock 77.8m YE2025 (new loans 24.5m; MJP26 +25m)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>debt",
        "annual_cost_eur": "2665475", "total_cost_eur": "77761004",
        "tco_notes": "Strong FOI-adjacent; rising 66.2to77.8m; large new loans vs invest 19.7m; dual Aarschot 43m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance invest", "measured_outcome": "T4 rising",
        "absurdity_score": "6.5", "cost_score": "6.5", "difficulty": "5.5",
        "priority_index": "6.5", "cut_proposal": "Lender FOI",
        "status": "active", "struck_reason": "", "notes": "tick861 stock FOI-adjacent",
    },
    {
        "item_id": "lb_kx_fiscal_58m_2025",
        "name": "Koksijde fiscal receipts 58.0m 2025 (coastal base)",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>fiscal",
        "annual_cost_eur": "0", "total_cost_eur": "57967199",
        "tco_notes": "Strong coastal fiscal base funds high AFM; dual inland peers lower",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Tax base second homes/tourism class",
        "stated_goal": "Local tax receipts", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.5", "cost_score": "6.5", "difficulty": "4.0",
        "priority_index": "5.0", "cut_proposal": "Rate transparency FOI",
        "status": "active", "struck_reason": "", "notes": "tick861 positive capacity",
    },
    {
        "item_id": "lb_kx_ocmw_aid_1m_2025",
        "name": "Koksijde OCMW individual aid 1.4m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde>OCMW",
        "annual_cost_eur": "1438974", "total_cost_eur": "1438974",
        "tco_notes": "Strong low vs peers; dual Aarschot 4.0m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "2.5", "cost_score": "3.0", "difficulty": "7.0",
        "priority_index": "2.75", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick861 safety-net",
    },
    {
        "item_id": "lb_dual_koksijde_aarschot_tick861",
        "name": "Dual Koksijde 330m vs Aarschot 172m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "330404427",
        "tco_notes": "Strong dual not TE-additive; coastal fiscal/AFM vs inland debt-invest path",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.5", "cost_score": "6.0", "difficulty": "5.0",
        "priority_index": "5.25", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick861",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Gemeente+OCMW Koksijde Jaarrekening 2025 (BBC consolidatie, 463p)",
        "url": URL,
        "publisher": "Gemeente Koksijde",
        "accessed_date": "2026-08-06",
        "source_class": "primary_jaarrekening",
        "notes": "Pub 2026-06-25 class; assets 330.4m equity 216.5m cash 16.5m expl 90.3/72.3m AFM +10.3m BBR 13.2m fiscal 58.0m fin debt 77.8m new loans 24.5m invest 19.7m personnel 41.3m toelagen 10.3m; tick861",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Koksijde JR2025 vs Aarschot JR2025 tick861",
        "url": URL,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-06",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Koksijde 330m vs Aarschot 172m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Gemeente Koksijde",
    "name_fr": "Commune de Coxyde",
    "name_en": "Municipality of Koksijde",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.koksijde.be",
    "foi_email": "info@koksijde.be",
    "foi_postal": "Zeelaan 303 8670 Koksijde",
    "notes": "JR2025 assets 330m equity 216m cash 17m expl 90/72m fiscal 58m personnel 41m fin debt 78m new loans 24.5m AFM +10.3m BBR 13m toelagen 10m; tick861",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_koksijde_debt_loans_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Koksijde_L5",
    "entity_id": EID,
    "what_is_missing": "Lender schedule for fin debt 77.761m and new loans 24.528m (invest 19.732m); MJP2026 planned new loans 25.057m + 2027 30m project map; named toelagen matrix for other 2.779m; AGB/VVV full JR2025 consol detail",
    "why_it_matters": "330m coastal municipality with very strong AFM +10.3m and fiscal 58m but debt jump 66to78m + large planned loans FOI-adjacent L5",
    "priority": "8",
    "recipient_body": "Gemeente Koksijde / financieel directeur / openbaarheid",
    "recipient_email": "info@koksijde.be",
    "recipient_postal": "https://www.koksijde.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_koksijde_debt_loans_l5.md",
    "status": "ready",
    "date_ready": "2026-08-06",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_kx_fin_debt_78m_2025",
    "linked_leaderboard_id": "lb_kx_fin_debt_78m_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick861 primary JR2025; ready draft; do not send; prio8 debt jump",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_861":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick861 Koksijde JR2025 dual Aarschot; assets 330m fin debt 78m new loans 24.5m AFM +10.3m"
        print("rq_861 done")
        break

if not any(r["task_id"] == "rq_862" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_862",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Koksijde JR2025 filled tick861; residual Roeselare portal/Lier portal/Poperinge/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick861 after Koksijde dual Aarschot",
    })
    print("spawned rq_862")

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
        r["last_unit_id"] = "rq_861"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick861 Koksijde JR2025 dual Aarschot; FOI gap_koksijde_debt_loans_l5; next rq_862 residual dual L5; progress@870 in 9; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

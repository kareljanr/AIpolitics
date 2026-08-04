import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-06T01:30:00Z"
TICK = 857
SRC = "src_heist_jr2025"
SRC_DUAL = "src_dual_heist_lommel_tick857"
EID = "city_heist_op_den_berg"
URL = "https://www.heist-op-den-berg.be/jaarrekening"


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
    ("bud_hb_assets_2025", 232831365, "Consol stad+OCMW total assets YE2025 232.831m; tick857"),
    ("bud_hb_equity_2025", 165023692, "Nettoactief YE2025 165.024m; tick857"),
    ("bud_hb_debt_total_2025", 67807673, "Total schulden YE2025 67.808m; tick857"),
    ("bud_hb_fin_debt_2025", 18267350, "T4 total financiele schulden YE2025 18.267m (LT 16.348 + ST due 1.919); tick857"),
    ("bud_hb_fin_debt_lt_2025", 16348174, "Financiele schulden LT YE2025 16.348m; tick857"),
    ("bud_hb_fin_debt_st_due_2025", 1919176, "Schulden LT vervallend binnen jaar YE2025 1.919m; tick857"),
    ("bud_hb_pension_prov_2025", 24848037, "Pensioenvoorzieningen LT YE2025 24.848m; tick857"),
    ("bud_hb_cash_2025", 19951972, "Liquide middelen YE2025 19.952m; tick857"),
    ("bud_hb_cap_subs_2025", 15037433, "Kapitaalsubsidies YE2025 15.037m; tick857"),
    ("bud_hb_fva_total_2025", 28057211, "Financiele vaste activa YE2025 28.057m; tick857"),
    ("bud_hb_fva_igs_2025", 23095516, "Fin VA IGS YE2025 23.096m; tick857"),
    ("bud_hb_mva_2025", 145707425, "Materiele vaste activa YE2025 145.707m; tick857"),
    ("bud_hb_onbeschikbaar_2025", 413333, "Onbeschikbare gelden J2 0.413m; tick857"),
    ("bud_hb_expl_rec_2025", 86109035, "Exploitatieontvangsten 86.109m; tick857"),
    ("bud_hb_expl_exp_2025", 74702888, "Exploitatieuitgaven 74.703m; tick857"),
    ("bud_hb_expl_saldo_2025", 11406147, "Exploitatiesaldo +11.406m; tick857"),
    ("bud_hb_invest_exp_2025", 13923038, "Investeringsuitgaven J2 13.923m; tick857"),
    ("bud_hb_invest_rec_2025", 1770515, "Investeringsontvangsten J2 1.771m; tick857"),
    ("bud_hb_invest_saldo_2025", -12152523, "Investeringssaldo -12.153m; tick857"),
    ("bud_hb_fin_rec_2025", 2490145, "Financieringsontvangsten 2.490m; tick857"),
    ("bud_hb_fin_exp_2025", 2914097, "Financieringsuitgaven 2.914m; tick857"),
    ("bud_hb_new_loans_2025", 573404, "Nieuwe leningen 0.573m; tick857"),
    ("bud_hb_aflossingen_2025", 1874354, "Periodieke aflossingen 1.874m; tick857"),
    ("bud_hb_afm_2025", 10773617, "AFM +10.774m (very strong); tick857"),
    ("bud_hb_afm_corr_2025", 11082508, "Gecorrigeerde AFM +11.083m; tick857"),
    ("bud_hb_bbr_2025", 12023250, "BBR 12.023m after onbeschikbaar 0.413m; tick857"),
    ("bud_hb_budget_result_2025", -1170328, "Budgettair resultaat boekjaar -1.170m; tick857"),
    ("bud_hb_cum_br_2025", 12436584, "Gecumuleerd budgettair resultaat 12.437m; tick857"),
    ("bud_hb_pnl_result_2025", 423708, "Vennootschapsresultaat J5 +0.424m; tick857"),
    ("bud_hb_personnel_2025", 38626174, "J5 bezoldigingen 38.626m (T2 38.639m; incl onderwijs other-gov 6.790m); tick857"),
    ("bud_hb_toelagen_2025", 13553791, "Toegestane werkingssubsidies 13.554m (politie 6.303 fire 2.104 AGB 2.649 welzijn 1.811 other 0.662); tick857"),
    ("bud_hb_invest_subs_granted_2025", 5204610, "Toegestane investeringssubsidies J5 5.205m (was 0.588m); tick857"),
    ("bud_hb_ocmw_aid_2025", 3633944, "OCMW individuele hulp 3.634m; tick857"),
    ("bud_hb_fiscal_2025", 43746285, "J5 fiscale opbrengsten en boetes 43.746m; tick857"),
    ("bud_hb_werk_subs_rec_2025", 33358686, "J5 werkingssubsidies ontvangen 33.359m; tick857"),
    ("bud_hb_gemeentefonds_2025", 12603279, "Gemeentefonds 12.603m; tick857"),
    ("bud_hb_fin_costs_2025", 439554, "J5 financiele kosten 0.440m; tick857"),
    ("bud_hb_police_toelage_2025", 6302531, "Toelage politiezone 6.303m; tick857"),
    ("bud_hb_fire_toelage_2025", 2104124, "Toelage hulpverleningszone 2.104m; tick857"),
]
budget_rows = [{
    "budget_id": bid, "entity_id": EID, "year": "2025",
    "amount_eur": str(amt), "amount_min_eur": "", "amount_max_eur": "",
    "basis": "outturn", "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, amt, notes in budgets]
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_hb_balance_233m_2025",
        "title": "Heist-op-den-Berg consol stad+OCMW balance YE2025 assets 232.8m",
        "entity_id": EID, "beneficiary": "Gemeente+OCMW Heist-op-den-Berg",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-06-30",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "232831365", "cash_by_year": "2025:232831365",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal balance sheet", "cut_option": "Invest subs FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg",
        "notes": "tick857 primary JR2025 GR 30.06.2026 pub 01-02.07.2026",
    },
    {
        "commitment_id": "cmt_hb_expl_86m_2025",
        "title": "Heist-op-den-Berg exploitation receipts 86.1m expenses 74.7m 2025",
        "entity_id": EID, "beneficiary": "Gemeente+OCMW Heist-op-den-Berg",
        "legal_basis": "BBC", "decision_date": "2026-06-30",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "86109035", "cash_by_year": "2025:86109035",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal operations", "cut_option": "Toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>exploitatie",
        "notes": "tick857",
    },
    {
        "commitment_id": "cmt_hb_fin_debt_18m_2025",
        "title": "Heist-op-den-Berg financial debt stock 18.3m YE2025 (declining)",
        "entity_id": EID, "beneficiary": "creditors",
        "legal_basis": "BBC debt", "decision_date": "2026-06-30",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "18267350", "cash_by_year": "2025stock:18267350",
        "remaining_eur": "18267350", "status": "stock", "evaluation_url": URL,
        "stated_goal": "Capital finance", "cut_option": "Lender schedule FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>debt",
        "notes": "tick857 declining from 19.6m YE2024; low vs AFM",
    },
    {
        "commitment_id": "cmt_hb_afm_bbr_2025",
        "title": "Heist-op-den-Berg AFM +10.8m BBR 12.0m invest-subs 5.2m 2025",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-06-30",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "12023250",
        "cash_by_year": "2025BBR:12023250;AFM:10773617;invest_subs:5204610",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Financial equilibrium", "cut_option": "Invest subs FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>AFM",
        "notes": "tick857 very strong AFM; invest subsidies granted jump FOI-adjacent",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_hb_personnel_39m_2025",
        "name": "Heist-op-den-Berg personnel/bezold 38.6m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>personeel",
        "annual_cost_eur": "38626174", "total_cost_eur": "38626174",
        "tco_notes": "Strong; dual Lommel 28.0m; incl other-gov onderwijs 6.8m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff gemeente+OCMW",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "5.5", "difficulty": "7.0",
        "priority_index": "4.5", "cut_proposal": "Headcount FOI",
        "status": "active", "struck_reason": "", "notes": "tick857",
    },
    {
        "item_id": "lb_hb_toelagen_14m_2025",
        "name": "Heist-op-den-Berg toelagen 13.6m 2025 (police 6.3 AGB 2.6 fire 2.1 welzijn 1.8)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>toelagen",
        "annual_cost_eur": "13553791", "total_cost_eur": "13553791",
        "tco_notes": "Strong; dual Lommel 17.9m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + AGB + welzijn + fire",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2 buckets",
        "absurdity_score": "4.0", "cost_score": "5.0", "difficulty": "5.5",
        "priority_index": "4.5", "cut_proposal": "Named matrix FOI",
        "status": "active", "struck_reason": "", "notes": "tick857",
    },
    {
        "item_id": "lb_hb_invest_subs_5m_2025",
        "name": "Heist-op-den-Berg granted invest subsidies 5.2m 2025 (was 0.6m)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>invest_subs",
        "annual_cost_eur": "5204610", "total_cost_eur": "5204610",
        "tco_notes": "Strong FOI-adjacent jump YoY; beneficiaries not fully named in J5",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Unknown L5 beneficiaries",
        "stated_goal": "Capital grants out", "measured_outcome": "J5 outturn",
        "absurdity_score": "6.5", "cost_score": "5.0", "difficulty": "5.0",
        "priority_index": "5.75", "cut_proposal": "Named invest grants FOI",
        "status": "active", "struck_reason": "", "notes": "tick857 FOI-adjacent jump",
    },
    {
        "item_id": "lb_hb_afm_11m_2025",
        "name": "Heist-op-den-Berg AFM +10.8m BBR 12.0m 2025 (very strong)",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "10773617",
        "tco_notes": "Strong top-tier AFM; dual Lommel +5.5m Waregem +11.1m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Heist",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "6.0", "difficulty": "4.0",
        "priority_index": "4.5", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick857 positive",
    },
    {
        "item_id": "lb_hb_fin_debt_18m_2025",
        "name": "Heist-op-den-Berg fin debt stock 18.3m YE2025 (declining)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>debt",
        "annual_cost_eur": "435134", "total_cost_eur": "18267350",
        "tco_notes": "Strong declining; dual Lommel 16.0m; low vs cash 20m and AFM 10.8m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance", "measured_outcome": "T4 declining",
        "absurdity_score": "3.5", "cost_score": "4.5", "difficulty": "5.5",
        "priority_index": "4.0", "cut_proposal": "Lender FOI",
        "status": "active", "struck_reason": "", "notes": "tick857 stock",
    },
    {
        "item_id": "lb_hb_ocmw_aid_4m_2025",
        "name": "Heist-op-den-Berg OCMW individual aid 3.6m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg>OCMW",
        "annual_cost_eur": "3633944", "total_cost_eur": "3633944",
        "tco_notes": "Strong; dual Lommel 2.4m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0", "cost_score": "3.5", "difficulty": "7.0",
        "priority_index": "3.25", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick857 safety-net",
    },
    {
        "item_id": "lb_dual_heist_lommel_tick857",
        "name": "Dual Heist-op-den-Berg 233m vs Lommel 432m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "232831365",
        "tco_notes": "Strong dual not TE-additive; Heist high AFM + invest-subs jump vs Lommel cash/IGS reval",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.0", "cost_score": "5.5", "difficulty": "5.0",
        "priority_index": "4.75", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick857",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Gemeente+OCMW Heist-op-den-Berg Jaarrekening 2025 (BBC consolidatie, 213p)",
        "url": URL,
        "publisher": "Gemeente Heist-op-den-Berg",
        "accessed_date": "2026-08-06",
        "source_class": "primary_jaarrekening",
        "notes": "GR 2026-06-30 pub 2026-07-01/02; assets 232.8m equity 165.0m cash 20.0m expl 86.1/74.7m AFM +10.8m BBR 12.0m fin debt 18.3m personnel 38.6m toelagen 13.6m invest-subs out 5.2m; tick857",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Heist-op-den-Berg JR2025 vs Lommel JR2025 tick857",
        "url": URL,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-06",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Heist 233m vs Lommel 432m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Gemeente Heist-op-den-Berg",
    "name_fr": "Commune de Heist-op-den-Berg",
    "name_en": "Municipality of Heist-op-den-Berg",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.heist-op-den-berg.be",
    "foi_email": "financien@heist-op-den-berg.be",
    "foi_postal": "Kerkplein 16 2220 Heist-op-den-Berg",
    "notes": "JR2025 assets 233m equity 165m cash 20m expl 86/75m personnel 39m fin debt 18m AFM +10.8m BBR 12m toelagen 14m invest-subs 5.2m; tick857",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_heist_invest_subs_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Heist-op-den-Berg_L5",
    "entity_id": EID,
    "what_is_missing": "Named beneficiaries for toegestane investeringssubsidies 5.205m (was 0.588m YE2024); residual named matrix other toelagen 0.662m; AGB full JR2025 detail beyond consol BBR 8.1m / AFM near-zero; lender schedule fin debt 18.3m",
    "why_it_matters": "233m city+OCMW with very strong AFM +10.8m but invest-grant out jump ~9x needs L5 transparency",
    "priority": "7",
    "recipient_body": "Gemeente Heist-op-den-Berg / financieel directeur / openbaarheid",
    "recipient_email": "financien@heist-op-den-berg.be",
    "recipient_postal": "https://www.heist-op-den-berg.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_heist_invest_subs_l5.md",
    "status": "ready",
    "date_ready": "2026-08-06",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_hb_afm_bbr_2025",
    "linked_leaderboard_id": "lb_hb_invest_subs_5m_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick857 primary JR2025; ready draft; do not send",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_847":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick857 Heist JR2025 dual Lommel; assets 233m AFM +10.8m invest-subs 5.2m"
        print("rq_847 done")
        break

if not any(r["task_id"] == "rq_848" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_848",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Heist JR2025 filled tick857; residual Roeselare portal/Lier portal/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick857 after Heist dual Lommel",
    })
    print("spawned rq_848")

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
        r["last_unit_id"] = "rq_847"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick857 Heist JR2025 dual Lommel; FOI gap_heist_invest_subs_l5; next rq_848 residual dual L5; progress@860 in 3; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

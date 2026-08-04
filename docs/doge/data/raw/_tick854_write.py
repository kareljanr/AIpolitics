import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-06T00:00:00Z"
TICK = 854
SRC = "src_waregem_jr2025"
SRC_DUAL = "src_dual_waregem_izegem_tick854"
EID = "city_waregem"
URL = "https://www.waregem.be/media/67401/download"
PAGE = "https://www.waregem.be/beleidsplan"


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
    ("bud_wg_assets_2025", 346006039, "Consol stad+OCMW total assets YE2025 346.006m; tick854"),
    ("bud_wg_equity_2025", 255785745, "Nettoactief YE2025 255.786m; tick854"),
    ("bud_wg_debt_total_2025", 90220294, "Total schulden YE2025 90.220m; tick854"),
    ("bud_wg_fin_debt_2025", 32734392, "T4 total financiele schulden YE2025 32.734m (LT 28.945 + ST due 3.758 + ST 0.031); tick854"),
    ("bud_wg_fin_debt_lt_2025", 28945254, "Financiele schulden LT YE2025 28.945m; tick854"),
    ("bud_wg_fin_debt_st_due_2025", 3757817, "Schulden LT vervallend binnen jaar YE2025 3.758m; tick854"),
    ("bud_wg_pension_prov_2025", 37051437, "Pensioenvoorzieningen LT YE2025 37.051m (~= fin debt); tick854"),
    ("bud_wg_cash_2025", 24727185, "Liquide middelen YE2025 24.727m; tick854"),
    ("bud_wg_cap_subs_2025", 22774098, "Kapitaalsubsidies YE2025 22.774m; tick854"),
    ("bud_wg_fva_total_2025", 61824103, "Financiele vaste activa YE2025 61.824m; tick854"),
    ("bud_wg_fva_igs_2025", 45979166, "Fin VA IGS YE2025 45.979m; tick854"),
    ("bud_wg_mva_2025", 242422202, "Materiele vaste activa YE2025 242.422m; tick854"),
    ("bud_wg_onbeschikbaar_2025", 4280970, "Onbeschikbare gelden J2 4.281m; tick854"),
    ("bud_wg_expl_rec_2025", 116856761, "Exploitatieontvangsten 116.857m; tick854"),
    ("bud_wg_expl_exp_2025", 101827770, "Exploitatieuitgaven 101.828m; tick854"),
    ("bud_wg_expl_saldo_2025", 15028992, "Exploitatiesaldo +15.029m; tick854"),
    ("bud_wg_invest_exp_2025", 15705151, "Investeringsuitgaven J2 15.705m; tick854"),
    ("bud_wg_invest_rec_2025", 5294189, "Investeringsontvangsten J2 5.294m; tick854"),
    ("bud_wg_invest_saldo_2025", -10410961, "Investeringssaldo -10.411m; tick854"),
    ("bud_wg_fin_rec_2025", 4161474, "Financieringsontvangsten 4.161m; tick854"),
    ("bud_wg_fin_exp_2025", 4102592, "Financieringsuitgaven 4.103m; tick854"),
    ("bud_wg_new_loans_2025", 2725682, "Nieuwe leningen 2.726m; tick854"),
    ("bud_wg_aflossingen_2025", 4102592, "Periodieke aflossingen 4.103m; tick854"),
    ("bud_wg_afm_2025", 11147053, "AFM +11.147m (very strong); tick854"),
    ("bud_wg_afm_corr_2025", 12523246, "Gecorrigeerde AFM +12.523m; tick854"),
    ("bud_wg_bbr_2025", 25098453, "BBR 25.098m after onbeschikbaar 4.281m; tick854"),
    ("bud_wg_budget_result_2025", 4676912, "Budgettair resultaat boekjaar +4.677m; tick854"),
    ("bud_wg_cum_br_2025", 29379423, "Gecumuleerd budgettair resultaat 29.379m; tick854"),
    ("bud_wg_pnl_result_2025", 2400895, "Vennootschapsresultaat J5 +2.401m; tick854"),
    ("bud_wg_personnel_2025", 56271433, "J5/T2 bezoldigingen 56.271m (incl onderwijs other-gov 13.126m); tick854"),
    ("bud_wg_toelagen_2025", 15034109, "Toegestane werkingssubsidies 15.034m (politie 4.682 fire 1.262 IGS 2.337 other 6.465); tick854"),
    ("bud_wg_ocmw_aid_2025", 4264137, "OCMW individuele hulp 4.264m; tick854"),
    ("bud_wg_fiscal_2025", 42401380, "J5 fiscale opbrengsten en boetes 42.401m; tick854"),
    ("bud_wg_werk_subs_rec_2025", 44060065, "J5 werkingssubsidies ontvangen 44.060m; tick854"),
    ("bud_wg_gemeentefonds_2025", 15839683, "Gemeentefonds 15.840m; tick854"),
    ("bud_wg_fin_costs_2025", 990691, "J5 financiele kosten 0.991m; tick854"),
    ("bud_wg_police_toelage_2025", 4682127, "Toelage politiezone 4.682m; tick854"),
    ("bud_wg_fire_toelage_2025", 1261695, "Toelage hulpverleningszone 1.262m; tick854"),
    ("bud_wg_other_toelagen_2025", 6464807, "Toelagen andere begunstigden 6.465m FOI-adjacent; tick854"),
]
budget_rows = [{
    "budget_id": bid, "entity_id": EID, "year": "2025",
    "amount_eur": str(amt), "amount_min_eur": "", "amount_max_eur": "",
    "basis": "outturn", "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, amt, notes in budgets]
nb = append_csv("docs/doge/data/budgets.csv", budget_rows)

commitments = [
    {
        "commitment_id": "cmt_wg_balance_346m_2025",
        "title": "Waregem consol stad+OCMW balance YE2025 assets 346.0m",
        "entity_id": EID, "beneficiary": "Stad+OCMW Waregem",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-07-07",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "346006039", "cash_by_year": "2025:346006039",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": PAGE,
        "stated_goal": "Municipal balance sheet", "cut_option": "Pension/toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem",
        "notes": "tick854 primary JR2025 GR 07.07.2026",
    },
    {
        "commitment_id": "cmt_wg_expl_117m_2025",
        "title": "Waregem exploitation receipts 116.9m expenses 101.8m 2025",
        "entity_id": EID, "beneficiary": "Stad+OCMW Waregem",
        "legal_basis": "BBC", "decision_date": "2026-07-07",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "116856761", "cash_by_year": "2025:116856761",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": PAGE,
        "stated_goal": "Municipal operations", "cut_option": "Other toelagen FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>exploitatie",
        "notes": "tick854",
    },
    {
        "commitment_id": "cmt_wg_fin_debt_33m_2025",
        "title": "Waregem financial debt stock 32.7m YE2025",
        "entity_id": EID, "beneficiary": "creditors",
        "legal_basis": "BBC debt", "decision_date": "2026-07-07",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "32734392", "cash_by_year": "2025stock:32734392",
        "remaining_eur": "32734392", "status": "stock", "evaluation_url": PAGE,
        "stated_goal": "Capital finance", "cut_option": "Lender schedule FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>debt",
        "notes": "tick854 declining from 34.1m YE2024; pension stock 37.1m larger",
    },
    {
        "commitment_id": "cmt_wg_afm_bbr_2025",
        "title": "Waregem AFM +11.1m and BBR 25.1m 2025 (onbeschikbaar 4.3m)",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-07-07",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "25098453",
        "cash_by_year": "2025BBR:25098453;AFM:11147053;onbeschikbaar:4280970;pension:37051437",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": PAGE,
        "stated_goal": "Financial equilibrium", "cut_option": "Pension+other grants FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>AFM",
        "notes": "tick854 very strong AFM; pension provisions ~fin debt class",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_wg_personnel_56m_2025",
        "name": "Waregem personnel/bezold 56.3m 2025 (incl other-gov onderwijs 13.1m)",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>personeel",
        "annual_cost_eur": "56271433", "total_cost_eur": "56271433",
        "tco_notes": "Strong; dual Izegem 27.7m; includes 13.1m teaching funded by other govs",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff Stad+OCMW Waregem",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "6.0", "difficulty": "7.0",
        "priority_index": "4.75", "cut_proposal": "Headcount FOI excl teaching",
        "status": "active", "struck_reason": "", "notes": "tick854",
    },
    {
        "item_id": "lb_wg_toelagen_15m_2025",
        "name": "Waregem toelagen 15.0m 2025 (police 4.7 other 6.5 IGS 2.3 fire 1.3)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>toelagen",
        "annual_cost_eur": "15034109", "total_cost_eur": "15034109",
        "tco_notes": "Strong; other 6.5m FOI-adjacent; dual Izegem 12.3m named DOC2",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + IGS + other",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2 buckets",
        "absurdity_score": "5.0", "cost_score": "5.5", "difficulty": "5.5",
        "priority_index": "5.25", "cut_proposal": "Named matrix FOI >=100k other",
        "status": "active", "struck_reason": "", "notes": "tick854 FOI-adjacent other",
    },
    {
        "item_id": "lb_wg_afm_11m_2025",
        "name": "Waregem AFM +11.1m BBR 25.1m 2025 (very strong)",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "11147053",
        "tco_notes": "Strong top-tier VL mid-city AFM; dual Izegem +3.1m Ieper +16.0m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Waregem",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "6.0", "difficulty": "4.0",
        "priority_index": "4.5", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick854 positive",
    },
    {
        "item_id": "lb_wg_pension_37m_2025",
        "name": "Waregem pension provisions stock 37.1m YE2025 (≈ fin debt 32.7m)",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>pension",
        "annual_cost_eur": "0", "total_cost_eur": "37051437",
        "tco_notes": "Strong FOI-adjacent; dual Geel pension≈debt pattern; stock not annual TE",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Former/current staff",
        "stated_goal": "Pension liability", "measured_outcome": "J4 provisions",
        "absurdity_score": "6.0", "cost_score": "6.0", "difficulty": "6.0",
        "priority_index": "6.0", "cut_proposal": "Composition FOI",
        "status": "active", "struck_reason": "", "notes": "tick854 stock FOI-adjacent",
    },
    {
        "item_id": "lb_wg_fin_debt_33m_2025",
        "name": "Waregem fin debt stock 32.7m YE2025 (declining)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>debt",
        "annual_cost_eur": "928677", "total_cost_eur": "32734392",
        "tco_notes": "Strong declining; dual Izegem 18.7m; pension stock larger than debt",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders",
        "stated_goal": "Capital finance", "measured_outcome": "T4 stock",
        "absurdity_score": "4.0", "cost_score": "5.0", "difficulty": "5.5",
        "priority_index": "4.5", "cut_proposal": "Lender FOI",
        "status": "active", "struck_reason": "", "notes": "tick854 stock",
    },
    {
        "item_id": "lb_wg_ocmw_aid_4m_2025",
        "name": "Waregem OCMW individual aid 4.3m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Waregem>OCMW",
        "annual_cost_eur": "4264137", "total_cost_eur": "4264137",
        "tco_notes": "Strong; dual Izegem 4.0m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0", "cost_score": "3.5", "difficulty": "7.0",
        "priority_index": "3.25", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick854 safety-net",
    },
    {
        "item_id": "lb_dual_waregem_izegem_tick854",
        "name": "Dual Waregem 346m vs Izegem 204m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "346006039",
        "tco_notes": "Strong dual not TE-additive; Waregem high AFM + pension stock vs Izegem named DOC2 toelagen",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.0", "cost_score": "6.0", "difficulty": "5.0",
        "priority_index": "5.0", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick854",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Stad+OCMW Waregem Jaarrekening 2025 (BBC consolidatie, 234p)",
        "url": PAGE,
        "publisher": "Stad Waregem",
        "accessed_date": "2026-08-06",
        "source_class": "primary_jaarrekening",
        "notes": "GR 2026-07-07; assets 346.0m equity 255.8m cash 24.7m expl 116.9/101.8m AFM +11.1m BBR 25.1m fin debt 32.7m pension 37.1m personnel 56.3m toelagen 15.0m other 6.5m; tick854",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Waregem JR2025 vs Izegem JR2025 tick854",
        "url": PAGE,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-06",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Waregem 346m vs Izegem 204m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Stad Waregem",
    "name_fr": "Ville de Waregem",
    "name_en": "City of Waregem",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.waregem.be",
    "foi_email": "info@waregem.be",
    "foi_postal": "Gemeenteplein 2 8790 Waregem",
    "notes": "JR2025 assets 346m equity 256m cash 25m expl 117/102m personnel 56m fin debt 33m pension 37m AFM +11m BBR 25m toelagen 15m other 6.5m; tick854",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_waregem_pension_subs_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Waregem_L5",
    "entity_id": EID,
    "what_is_missing": "Composition of pension provisions 37.1m vs fin debt 32.7m; named toelagen matrix for other beneficiaries 6.46m within 15.0m package; onbeschikbare gelden 4.28m composition; WAGSO full JR2025 consol detail beyond BBR 0.40m / AFM 1.26m",
    "why_it_matters": "346m city+OCMW with very strong AFM +11.1m but pension stock exceeds fin debt and other grants 6.5m lack named L5 list (unlike Izegem DOC2)",
    "priority": "7",
    "recipient_body": "Stad Waregem / financieel directeur / openbaarheid",
    "recipient_email": "info@waregem.be",
    "recipient_postal": "https://www.waregem.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_waregem_pension_subs_l5.md",
    "status": "ready",
    "date_ready": "2026-08-06",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_wg_afm_bbr_2025",
    "linked_leaderboard_id": "lb_wg_pension_37m_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick854 primary JR2025; ready draft; do not send",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_844":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick854 Waregem JR2025 dual Izegem; assets 346m AFM +11.1m pension 37m"
        print("rq_844 done")
        break

if not any(r["task_id"] == "rq_845" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_845",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Waregem JR2025 filled tick854; residual Roeselare portal/Lier portal/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick854 after Waregem dual Izegem",
    })
    print("spawned rq_845")

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
        r["last_unit_id"] = "rq_844"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick854 Waregem JR2025 dual Izegem; FOI gap_waregem_pension_subs_l5; next rq_845 residual dual L5; progress@860 in 6; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

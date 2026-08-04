# tick831 Kortrijk JR2025 CSV writer
import csv
csv.field_size_limit(10**7)

BASE = "docs/doge/data"
TS = "2026-08-05T12:30:00Z"
DATE = "2026-08-05"
SRC = "src_kortrijk_jr2025"
SRC_DUAL = "src_dual_kortrijk_mechelen_tick831"
ENT = "city_kortrijk"
GAP = "gap_kortrijk_debt_pension_subs_l5"


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write_csv(path, fields, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


# --- sources ---
sfields, srows = read_csv(f"{BASE}/sources.csv")
if not any(r.get("source_id") == SRC for r in srows):
    srows.append(
        {
            "source_id": SRC,
            "title": "Stad en OCMW Kortrijk Jaarrekening 2025 (BBC, volgnr 215589)",
            "url": "https://www.kortrijk.be/media/140406/download?inline",
            "publisher": "Stad Kortrijk / OCMW Kortrijk",
            "accessed_date": DATE,
            "source_class": "entity_accounts",
            "notes": "Strong tick831 primary 245p: consol stad+OCMW assets 720.4m equity 379.7m; expl ontvangsten 279.3m uitgaven 252.1m saldo +27.2m; AFM 7.2m BBR 20.2m; loonkost 135.6m (J5 bezold 102.5m); fin debt 258.0m; pension prov 34.5m; toelagen/subs 39.6m; invest 57.0m; raw kortrijk_jr2025.pdf",
        }
    )
if not any(r.get("source_id") == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Kortrijk JR2025 720m assets vs Mechelen JR2025 residual tick831",
            "url": "docs/doge/data/raw/kortrijk_jr2025.pdf",
            "publisher": "DOGE synthesis",
            "accessed_date": DATE,
            "source_class": "synthesis",
            "notes": "Strong dual not TE-additive: Kortrijk consol assets 720.4m expl 279m loon 135.6m AFM +7.2m vs Mechelen assets 610.8m expl 268m personnel 113m AFM +2.5m",
        }
    )
write_csv(f"{BASE}/sources.csv", sfields, srows)

# --- entities ---
efields, erows = read_csv(f"{BASE}/entities.csv")
if not any(r.get("entity_id") == ENT for r in erows):
    erows.append(
        {
            "entity_id": ENT,
            "name_nl": "Stad Kortrijk",
            "name_fr": "Ville de Courtrai",
            "name_en": "City of Kortrijk",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.kortrijk.be",
            "foi_email": "info@kortrijk.be",
            "foi_postal": "https://www.kortrijk.be",
            "notes": "JR2025 assets 720.4m consol stad+OCMW; tick831",
        }
    )
write_csv(f"{BASE}/entities.csv", efields, erows)

# --- budgets ---
bfields, brows = read_csv(f"{BASE}/budgets.csv")
budgets = [
    ("bud_kortrijk_assets_2025", 720408434, "stock", "Consol stad+OCMW total assets YE2025 720.408m; tick831"),
    ("bud_kortrijk_equity_2025", 379677266, "stock", "Nettoactief YE2025 379.677m; tick831"),
    ("bud_kortrijk_debt_total_2025", 340731169, "stock", "Total schulden YE2025 340.731m; tick831"),
    ("bud_kortrijk_fin_debt_2025", 258038673, "stock", "Financiele schulden YE2025 258.039m (+26.3m YoY); per capita 3194; tick831"),
    ("bud_kortrijk_fin_debt_lt_2025", 236615135, "stock", "Financiele schulden LT YE2025 236.615m; tick831"),
    ("bud_kortrijk_pension_prov_2025", 34450620, "stock", "Pensioenvoorzieningen YE2025 34.451m (was 45.630m 2024; Ethias path alignment); tick831"),
    ("bud_kortrijk_cash_2025", 25413209, "stock", "Liquide middelen YE2025 25.413m; tick831"),
    ("bud_kortrijk_cap_subs_2025", 83309693, "stock", "Kapitaalsubsidies YE2025 83.310m (+10.4m); tick831"),
    ("bud_kortrijk_fva_igs_2025", 106433987, "stock", "Fin VA intergemeentelijke samenwerkingsverbanden 106.434m; tick831"),
    ("bud_kortrijk_expl_rec_2025", 279296463, "cash", "Exploitatieontvangsten 279.296m; tick831"),
    ("bud_kortrijk_expl_exp_2025", 252134945, "cash", "Exploitatieuitgaven 252.135m; tick831"),
    ("bud_kortrijk_expl_saldo_2025", 27161518, "cash", "Exploitatiesaldo +27.162m; tick831"),
    ("bud_kortrijk_invest_exp_2025", 56997533, "cash", "Investeringsuitgaven 56.998m; tick831"),
    ("bud_kortrijk_invest_rec_2025", 17789798, "cash", "Investeringsontvangsten 17.790m; tick831"),
    ("bud_kortrijk_invest_saldo_2025", -39207735, "cash", "Investeringssaldo -39.208m; tick831"),
    ("bud_kortrijk_fin_rec_2025", 51112347, "cash", "Financieringsontvangsten 51.112m (loans ~48.8m); tick831"),
    ("bud_kortrijk_fin_exp_2025", 23933396, "cash", "Financieringsuitgaven 23.933m (aflossingen 22.5m); tick831"),
    ("bud_kortrijk_new_loans_2025", 48800000, "cash", "Nieuwe leningen/leasings 48.8m (45m eigen +1.3m doorgeef PZ +2.5m boekhoud Fluvius/VEA); tick831"),
    ("bud_kortrijk_afm_2025", 7198327, "cash", "Autofinancieringsmarge AFM 7.198m (interne 6.927m; gecorr 11.186m); tick831"),
    ("bud_kortrijk_bbr_2025", 20200945, "cash", "Beschikbaar budgettair resultaat BBR 20.201m; tick831"),
    ("bud_kortrijk_budget_result_2025", 15132734, "cash", "Budgettair resultaat boekjaar +15.133m; tick831"),
    ("bud_kortrijk_pnl_result_2025", 11032619, "cash", "Vennootschapsresultaat J5 +11.033m; tick831"),
    ("bud_kortrijk_loonkost_2025", 135554000, "cash", "Totale loonkost intern 135.554m (+2.8% YoY; 1591 VTE); tick831"),
    ("bud_kortrijk_bezold_pnl_2025", 102509298, "cash", "J5 bezoldigingen/sociale/pensioenen 102.509m; tick831"),
    ("bud_kortrijk_respo_2025", 8031000, "cash", "Responsabiliseringsbijdrage 8.031m (netto na VL sub ~3.9m); tick831"),
    ("bud_kortrijk_goederen_pnl_2025", 84625555, "cash", "J5 goederen en diensten 84.626m; tick831"),
    ("bud_kortrijk_toelagen_2025", 39631954, "cash", "J5 toegestane werkingssubsidies 39.632m (toelagen ~36.8m + regl 2.8m); tick831"),
    ("bud_kortrijk_inv_subs_granted_2025", 1064220, "cash", "J5 toegestane investeringssubsidies 1.064m; tick831"),
    ("bud_kortrijk_ocmw_aid_2025", 19257158, "cash", "J5 individuele hulpverlening OCMW 19.257m; tick831"),
    ("bud_kortrijk_fiscal_2025", 89094173, "cash", "J5 fiscale opbrengsten en boetes 89.094m; tick831"),
    ("bud_kortrijk_werk_subs_rec_2025", 112410290, "cash", "J5 werkingssubsidies ontvangen 112.410m; tick831"),
    ("bud_kortrijk_fin_costs_2025", 6931125, "cash", "J5 financiele kosten 6.931m; tick831"),
    ("bud_kortrijk_kerkfabriek_2025", 1400000, "cash", "Toelage kerkfabrieken 1.4m (-18.1% YoY); tick831"),
]
new_bud = 0
for bid, amt, basis, notes in budgets:
    if any(r.get("budget_id") == bid for r in brows):
        continue
    brows.append(
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": "2025",
            "amount_eur": str(int(amt)),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": SRC,
            "confidence": "strong",
            "notes": notes,
        }
    )
    new_bud += 1
write_csv(f"{BASE}/budgets.csv", bfields, brows)

# --- commitments ---
cfields, crows = read_csv(f"{BASE}/commitments.csv")
cmts = [
    {
        "commitment_id": "cmt_kortrijk_balance_720m_2025",
        "title": "Kortrijk stad+OCMW balance 720.4m YE2025 (equity 379.7m debt 340.7m fin debt 258m)",
        "entity_id": ENT,
        "beneficiary": "City of Kortrijk / OCMW residents",
        "legal_basis": "BBC Jaarrekening 2025 volgnr 215589",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "720408434",
        "cash_by_year": '{"assets_m": 720.4, "equity_m": 379.7, "debt_m": 340.7, "fin_debt_m": 258.0, "pension_prov_m": 34.5, "expl_m": 279.3}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kortrijk_jr2025.pdf",
        "stated_goal": "Deliver local public services",
        "cut_option": "",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk",
        "notes": "tick831 dual Mechelen",
    },
    {
        "commitment_id": "cmt_kortrijk_pension_prov_34m_2025",
        "title": "Kortrijk pension provisions stock 34.5m YE2025 (Ethias path; was 45.6m)",
        "entity_id": ENT,
        "beneficiary": "Statutory staff pension liabilities",
        "legal_basis": "BBC balance J4 YE2025; Ethias study for MJP2026-2031",
        "decision_date": "2025-12-31",
        "start_year": "2015",
        "end_year": "2050",
        "total_envelope_eur": "34450620",
        "cash_by_year": '{"stock_m": 34.45, "respo_m": 8.031, "respo_net_m": 3.9}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kortrijk_jr2025.pdf",
        "stated_goal": "Cover pension obligations via Ethias path vs FPD",
        "cut_option": "Funding ratio FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>pensions",
        "notes": "tick831 large write-back provision",
    },
    {
        "commitment_id": "cmt_kortrijk_afm_bbr_2025",
        "title": "Kortrijk AFM +7.2m and BBR +20.2m 2025",
        "entity_id": ENT,
        "beneficiary": "Fiscal sustainability indicators",
        "legal_basis": "BBC schema J2 2025",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "20200945",
        "cash_by_year": '{"afm_m": 7.198, "afm_int_m": 6.927, "afm_corr_m": 11.186, "bbr_m": 20.201}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kortrijk_jr2025.pdf",
        "stated_goal": "Positive autofinancing and BBR",
        "cut_option": "Sustain AFM path FOI MJP2026-2031",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>AFM",
        "notes": "tick831 AFM down from 11.5m 2024 but still solid",
    },
    {
        "commitment_id": "cmt_dual_kortrijk_mechelen_tick831",
        "title": "Dual Kortrijk JR2025 vs Mechelen JR2025 city residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "Kortrijk JR2025 dual Mechelen tick829",
        "decision_date": DATE,
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "720408434",
        "cash_by_year": '{"kortrijk_assets_m": 720.4, "mechelen_assets_m": 610.8, "kortrijk_expl_m": 279.3, "mechelen_expl_m": 267.9}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kortrijk_jr2025.pdf",
        "stated_goal": "Dual residual map tick831",
        "cut_option": "Cross FOI city L5",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "notes": "tick831 not TE-additive",
    },
]
new_cmt = 0
for c in cmts:
    if not any(r.get("commitment_id") == c["commitment_id"] for r in crows):
        crows.append(c)
        new_cmt += 1
write_csv(f"{BASE}/commitments.csv", cfields, crows)

# --- leaderboard ---
lfields, lrows = read_csv(f"{BASE}/leaderboard.csv")
lbs = [
    {
        "item_id": "lb_kortrijk_loonkost_136m_2025",
        "name": "Kortrijk total loonkost 135.6m 2025 (1591 VTE; +2.8pct)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>personnel",
        "annual_cost_eur": "135554000",
        "total_cost_eur": "135554000",
        "tco_notes": "Strong primary internal loonkost; J5 bezoldigingen alone 102.5m; respo 8.0m within",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "city/OCMW/vzw staff",
        "stated_goal": "Deliver local services",
        "measured_outcome": "135.6m / 1591 VTE",
        "absurdity_score": "5.0",
        "cost_score": "7.2",
        "difficulty": "5.0",
        "priority_index": "5.73",
        "cut_proposal": "ETP productivity FOI; dual Mechelen 113m",
        "status": "active",
        "struck_reason": "",
        "notes": "tick831",
    },
    {
        "item_id": "lb_kortrijk_fin_debt_258m",
        "name": "Kortrijk financial debt stock 258m YE2025 (+26.3m YoY; 3194/capita)",
        "level": "L5",
        "type": "stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>debt",
        "annual_cost_eur": "6931125",
        "total_cost_eur": "258038673",
        "tco_notes": "Strong primary; annual fin cost 6.9m; new loans 48.8m vs repay 22.5m; stock not pure annual waste",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "lenders / infrastructure users",
        "stated_goal": "Finance investment programme 57m 2025",
        "measured_outcome": "258m stock / +26.3m",
        "absurdity_score": "5.5",
        "cost_score": "7.5",
        "difficulty": "6.0",
        "priority_index": "6.33",
        "cut_proposal": "Debt schedule FOI; investment prioritisation",
        "status": "active",
        "struck_reason": "",
        "notes": "tick831 stock filtered from pure annual top10",
    },
    {
        "item_id": "lb_kortrijk_toelagen_40m_2025",
        "name": "Kortrijk granted operating subsidies/toelagen 39.6m 2025",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>toelagen",
        "annual_cost_eur": "39631954",
        "total_cost_eur": "39631954",
        "tco_notes": "Strong J5; ~36.8m toelagen +2.8m regl; big4 police/fire/IMOG/kerkfabrieken >80pct",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Police zone, Fluvia fire, IMOG, kerkfabrieken, culture/sport",
        "stated_goal": "Fund safety zones and local partners",
        "measured_outcome": "39.6m / +2m YoY mostly police +1.8m",
        "absurdity_score": "5.5",
        "cost_score": "6.5",
        "difficulty": "5.5",
        "priority_index": "5.83",
        "cut_proposal": "Named beneficiary matrix FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick831",
    },
    {
        "item_id": "lb_kortrijk_pension_prov_34m",
        "name": "Kortrijk pension provision stock 34.5m YE2025 (Ethias write-back from 45.6m)",
        "level": "L5",
        "type": "stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>pensions",
        "annual_cost_eur": "8031000",
        "total_cost_eur": "34450620",
        "tco_notes": "Strong; respo 8.0m cash; large provision reverse via Ethias vs FPD path for MJP2026-31",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Statutory pensioners",
        "stated_goal": "Fund municipal pensions",
        "measured_outcome": "34.5m stock / respo 8.0m",
        "absurdity_score": "5.0",
        "cost_score": "6.0",
        "difficulty": "6.5",
        "priority_index": "5.83",
        "cut_proposal": "Ethias study + funding ratio FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick831 stock",
    },
    {
        "item_id": "lb_kortrijk_invest_57m_2025",
        "name": "Kortrijk investment spend 57.0m 2025 (net -39.2m after 17.8m receipts)",
        "level": "L5",
        "type": "capex",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>invest",
        "annual_cost_eur": "56997533",
        "total_cost_eur": "56997533",
        "tco_notes": "Strong; down 13.3m YoY; 61.9pct of budget; dual Mechelen invest ~26m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "city infrastructure users",
        "stated_goal": "Maintain and expand city infrastructure",
        "measured_outcome": "57.0m / -13.3m YoY",
        "absurdity_score": "4.5",
        "cost_score": "6.5",
        "difficulty": "5.0",
        "priority_index": "5.33",
        "cut_proposal": "Project-level ROI FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick831",
    },
    {
        "item_id": "lb_kortrijk_ocmw_aid_19m_2025",
        "name": "Kortrijk OCMW individual aid 19.3m 2025",
        "level": "L5",
        "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk>OCMW",
        "annual_cost_eur": "19257158",
        "total_cost_eur": "19257158",
        "tco_notes": "Strong J5 individuele hulpverlening; recuperatie 1.1m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social assistance",
        "measured_outcome": "19.3m",
        "absurdity_score": "3.5",
        "cost_score": "5.5",
        "difficulty": "7.0",
        "priority_index": "5.33",
        "cut_proposal": "Outcomes FOI not cut crude",
        "status": "active",
        "struck_reason": "",
        "notes": "tick831 safety-net class",
    },
]
new_lb = 0
for lb in lbs:
    if not any(r.get("item_id") == lb["item_id"] for r in lrows):
        lrows.append(lb)
        new_lb += 1
write_csv(f"{BASE}/leaderboard.csv", lfields, lrows)

# --- foi_queue ---
ffields, frows = read_csv(f"{BASE}/foi_queue.csv")
if not any(r.get("gap_id") == GAP for r in frows):
    frows.append(
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Gemeenten>Kortrijk_L5",
            "entity_id": ENT,
            "what_is_missing": "Full debt schedule by lender for fin debt 258m; Ethias pension study + funding path vs 34.5m provision; named toelagen matrix within 39.6m (beyond big4 narrative); Fluvius lease and PZ VLAS doorgeef detail; MJP2026-2031 multi-year AFM path reconciliation",
            "why_it_matters": "720m city+OCMW book with 258m fin debt, 34.5m pension provisions and 39.6m toelagen blocks dual VL city waste ranking vs Mechelen/Gent/Antwerp",
            "priority": "7",
            "recipient_body": "Stad Kortrijk / financieel directeur / openbaarheid van bestuur",
            "recipient_email": "info@kortrijk.be",
            "recipient_postal": "https://www.kortrijk.be",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": DATE,
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_kortrijk_balance_720m_2025|cmt_kortrijk_pension_prov_34m_2025|cmt_kortrijk_afm_bbr_2025",
            "linked_leaderboard_id": "lb_kortrijk_loonkost_136m_2025|lb_kortrijk_fin_debt_258m|lb_kortrijk_toelagen_40m_2025|lb_kortrijk_pension_prov_34m",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "tick831 primary JR2025; ready draft; do not send",
        }
    )
write_csv(f"{BASE}/foi_queue.csv", ffields, frows)

# --- research_queue ---
rfields, rrows = read_csv(f"{BASE}/research_queue.csv")
for r in rrows:
    if r.get("task_id") == "rq_821":
        r["status"] = "done"
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = "tick831 Kortrijk JR2025 assets 720.4m expl 279.3m loon 135.6m AFM 7.2m fin debt 258m pension 34.5m toelagen 39.6m dual Mechelen; FOI ready"
if not any(r.get("task_id") == "rq_822" for r in rrows):
    rrows.append(
        {
            "task_id": "rq_822",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Kortrijk JR2025 filled tick831; residual Aalst/Genk/Roeselare/Hasselt city or BELNET AR2025 or skeyes residual",
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned tick831 after Kortrijk dual Mechelen",
        }
    )
write_csv(f"{BASE}/research_queue.csv", rfields, rrows)

# --- loop_state ---
lsfields, lsrows = read_csv(f"{BASE}/loop_state.csv")
lsrows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": TS,
    "last_unit_id": "rq_821",
    "ticks_completed": "831",
    "paused": "no",
    "notes": "tick831 Kortrijk JR2025 dual Mechelen; next rq_822 residual dual L5; progress@840 in 9; rq_116 deferred",
}
write_csv(f"{BASE}/loop_state.csv", lsfields, lsrows)

print("budgets added", new_bud)
print("commitments added", new_cmt)
print("leaderboard added", new_lb)
print("ticks", lsrows[0]["ticks_completed"])
print(
    "open",
    [r["task_id"] for r in rrows if r.get("status") in ("open", "in_progress")],
)

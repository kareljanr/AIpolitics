import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
NOW = "2026-08-05T23:30:00Z"
TICK = 853
SRC = "src_izegem_jr2025"
SRC_DUAL = "src_dual_izegem_landen_tick853"
EID = "city_izegem"
URL = "https://www.izegem.be/jaarrekening"


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
    ("bud_iz_assets_2025", 203558009, "Consol stad+OCMW total assets YE2025 203.558m; tick853"),
    ("bud_iz_equity_2025", 176389794, "Nettoactief YE2025 176.390m; tick853"),
    ("bud_iz_debt_total_2025", 27168215, "Total schulden YE2025 27.168m; tick853"),
    ("bud_iz_fin_debt_2025", 18665103, "T4 total financiele schulden YE2025 18.665m (LT 15.866 + ST due 2.799); tick853"),
    ("bud_iz_fin_debt_lt_2025", 15866338, "Financiele schulden LT YE2025 15.866m; tick853"),
    ("bud_iz_fin_debt_st_due_2025", 2798766, "Schulden LT vervallend binnen jaar YE2025 2.799m; tick853"),
    ("bud_iz_fin_debt_excl_farys_2025", 8828888, "Fin debt excl Farys share YE2025 8.829m; tick853"),
    ("bud_iz_farys_debt_share_2025", 9836216, "Farys aandeel in fin debt YE2025 9.836m; tick853"),
    ("bud_iz_pension_prov_2025", 5330433, "Pensioenvoorzieningen LT YE2025 5.330m; tick853"),
    ("bud_iz_cash_2025", 8670452, "Liquide middelen YE2025 8.670m; tick853"),
    ("bud_iz_cap_subs_2025", 12057982, "Kapitaalsubsidies YE2025 12.058m; tick853"),
    ("bud_iz_fva_total_2025", 76518817, "Financiele vaste activa YE2025 76.519m; tick853"),
    ("bud_iz_fva_igs_2025", 38172519, "Fin VA IGS YE2025 38.173m; tick853"),
    ("bud_iz_mva_2025", 103335798, "Materiele vaste activa YE2025 103.336m; tick853"),
    ("bud_iz_onbeschikbaar_2025", 0, "Onbeschikbare gelden J2 0; tick853"),
    ("bud_iz_expl_rec_2025", 57126433, "Exploitatieontvangsten 57.126m; tick853"),
    ("bud_iz_expl_exp_2025", 51432168, "Exploitatieuitgaven 51.432m; tick853"),
    ("bud_iz_expl_saldo_2025", 5694265, "Exploitatiesaldo +5.694m; tick853"),
    ("bud_iz_invest_exp_2025", 8428720, "Investeringsuitgaven J2 8.429m; tick853"),
    ("bud_iz_invest_rec_2025", 1763256, "Investeringsontvangsten J2 1.763m; tick853"),
    ("bud_iz_invest_saldo_2025", -6665464, "Investeringssaldo -6.665m; tick853"),
    ("bud_iz_fin_rec_2025", 764852, "Financieringsontvangsten 0.765m; tick853"),
    ("bud_iz_fin_exp_2025", 3407853, "Financieringsuitgaven 3.408m; tick853"),
    ("bud_iz_new_loans_2025", 279996, "Nieuwe leningen/leasings 0.280m; tick853"),
    ("bud_iz_aflossingen_2025", 3140046, "Periodieke aflossingen 3.140m; tick853"),
    ("bud_iz_afm_2025", 3051592, "AFM +3.052m; tick853"),
    ("bud_iz_afm_corr_2025", 4469625, "Gecorrigeerde AFM +4.470m; tick853"),
    ("bud_iz_bbr_2025", 14397337, "BBR stad+OCMW 14.397m (onbeschikbaar 0); tick853"),
    ("bud_iz_bbr_consol_agencies_2025", 10095125, "Consol BBR incl AGIZ/ETIZ 10.095m (ETIZ 2024 lag -4.525m); tick853"),
    ("bud_iz_budget_result_2025", -3614200, "Budgettair resultaat boekjaar -3.614m; tick853"),
    ("bud_iz_cum_br_2025", 14397337, "Gecumuleerd budgettair resultaat 14.397m; tick853"),
    ("bud_iz_pnl_result_2025", -131860, "Vennootschapsresultaat J5 -0.132m; tick853"),
    ("bud_iz_personnel_2025", 27705366, "J5/T2 bezoldigingen 27.705m; tick853"),
    ("bud_iz_toelagen_2025", 12348961, "Toegestane werkingssubsidies 12.349m (politie 4.854 fire 0.839 AGB 0.433 IVIO 2.423 Farys 0.761); tick853"),
    ("bud_iz_ocmw_aid_2025", 3962953, "OCMW individuele hulp 3.963m; tick853"),
    ("bud_iz_fiscal_2025", 26363804, "J5 fiscale opbrengsten en boetes 26.364m; tick853"),
    ("bud_iz_werk_subs_rec_2025", 22067993, "J5 werkingssubsidies ontvangen 22.068m; tick853"),
    ("bud_iz_gemeentefonds_2025", 9226635, "Gemeentefonds 9.227m; tick853"),
    ("bud_iz_fin_costs_2025", 551681, "J5 financiele kosten 0.552m; tick853"),
    ("bud_iz_police_toelage_2025", 4853786, "Toelage politiezone 4.854m; tick853"),
    ("bud_iz_fire_toelage_2025", 839382, "Toelage hulpverleningszone 0.839m; tick853"),
    ("bud_iz_ivio_toelage_2025", 2423256, "Toelage IVIO exploitatie 2.423m (DOC2); tick853"),
    ("bud_iz_mjp2026_new_loans_plan", 14988669, "MJP planned new loans 2026 14.989m (path jump); tick853"),
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
        "commitment_id": "cmt_iz_balance_204m_2025",
        "title": "Izegem consol stad+OCMW balance YE2025 assets 203.6m",
        "entity_id": EID, "beneficiary": "Stad+OCMW Izegem",
        "legal_basis": "BBC DLB jaarrekening", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "203558009", "cash_by_year": "2025:203558009",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal balance sheet", "cut_option": "Debt/agency FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem",
        "notes": "tick853 primary JR2025 GR 22.06.2026 pub 29.06.2026",
    },
    {
        "commitment_id": "cmt_iz_expl_57m_2025",
        "title": "Izegem exploitation receipts 57.1m expenses 51.4m 2025",
        "entity_id": EID, "beneficiary": "Stad+OCMW Izegem",
        "legal_basis": "BBC", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "57126433", "cash_by_year": "2025:57126433",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Municipal operations", "cut_option": "Named toelagen public DOC2",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>exploitatie",
        "notes": "tick853; strong public L5 subsidy annex",
    },
    {
        "commitment_id": "cmt_iz_fin_debt_19m_2025",
        "title": "Izegem financial debt stock 18.7m YE2025 (Farys 9.8m)",
        "entity_id": EID, "beneficiary": "creditors/Farys",
        "legal_basis": "BBC debt", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2035",
        "total_envelope_eur": "18665103", "cash_by_year": "2025stock:18665103;farys:9836216;excl:8828888",
        "remaining_eur": "18665103", "status": "stock", "evaluation_url": URL,
        "stated_goal": "Capital finance", "cut_option": "2026 loan path FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>debt",
        "notes": "tick853 declining stock; MJP2026 plan +15m jump FOI-adjacent",
    },
    {
        "commitment_id": "cmt_iz_afm_bbr_2025",
        "title": "Izegem AFM +3.1m and BBR 14.4m 2025 (ETIZ lag -4.5m consol)",
        "entity_id": EID, "beneficiary": "fiscal sustainability",
        "legal_basis": "BBC evenwicht", "decision_date": "2026-06-22",
        "start_year": "2025", "end_year": "2025",
        "total_envelope_eur": "14397337",
        "cash_by_year": "2025BBR:14397337;AFM:3051592;consolBBR:10095125;ETIZ2024:-4524571",
        "remaining_eur": "0", "status": "outturn", "evaluation_url": URL,
        "stated_goal": "Financial equilibrium", "cut_option": "ETIZ 2025 FOI",
        "source_id": SRC, "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>AFM",
        "notes": "tick853 solid AFM; ETIZ 2024 lag distorts consol BBR",
    },
]
nc = append_csv("docs/doge/data/commitments.csv", commitments)

lbs = [
    {
        "item_id": "lb_iz_personnel_28m_2025",
        "name": "Izegem personnel/bezold 27.7m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>personeel",
        "annual_cost_eur": "27705366", "total_cost_eur": "27705366",
        "tco_notes": "Strong; dual Landen 19.6m Ieper 35.6m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Staff Stad+OCMW Izegem",
        "stated_goal": "Local public services", "measured_outcome": "JR2025 outturn",
        "absurdity_score": "3.5", "cost_score": "5.0", "difficulty": "7.0",
        "priority_index": "4.25", "cut_proposal": "Headcount FOI",
        "status": "active", "struck_reason": "", "notes": "tick853",
    },
    {
        "item_id": "lb_iz_toelagen_12m_2025",
        "name": "Izegem toelagen 12.3m 2025 (police 4.9 IVIO 2.4 fire 0.8 Farys 0.8)",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>toelagen",
        "annual_cost_eur": "12348961", "total_cost_eur": "12348961",
        "tco_notes": "Strong named DOC2 public L5; dual Landen 5.0m Ieper 11.6m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "PZ + IVIO + Farys + AGB + other",
        "stated_goal": "Statutory transfers", "measured_outcome": "T2+DOC2 named",
        "absurdity_score": "4.0", "cost_score": "5.0", "difficulty": "4.0",
        "priority_index": "4.5", "cut_proposal": "Already public named list",
        "status": "active", "struck_reason": "", "notes": "tick853 high transparency",
    },
    {
        "item_id": "lb_iz_afm_3m_2025",
        "name": "Izegem AFM +3.1m BBR 14.4m 2025",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>AFM",
        "annual_cost_eur": "0", "total_cost_eur": "3051592",
        "tco_notes": "Strong positive AFM; dual Landen +2.8m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Taxpayers Izegem",
        "stated_goal": "Fiscal equilibrium", "measured_outcome": "J2 outturn",
        "absurdity_score": "3.0", "cost_score": "4.0", "difficulty": "4.0",
        "priority_index": "3.5", "cut_proposal": "Sustain FOI",
        "status": "active", "struck_reason": "", "notes": "tick853 positive",
    },
    {
        "item_id": "lb_iz_fin_debt_19m_2025",
        "name": "Izegem fin debt stock 18.7m YE2025 (Farys 9.8m; MJP26 plan +15m)",
        "level": "L5", "type": "debt_stock",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>debt",
        "annual_cost_eur": "548619", "total_cost_eur": "18665103",
        "tco_notes": "Strong declining stock; Farys half; 2026 planned 15m loan jump FOI-adjacent",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "Lenders/Farys",
        "stated_goal": "Capital finance", "measured_outcome": "T4 declining to 18.7m",
        "absurdity_score": "5.5", "cost_score": "5.0", "difficulty": "5.0",
        "priority_index": "5.25", "cut_proposal": "2026 loan path FOI",
        "status": "active", "struck_reason": "", "notes": "tick853 stock FOI-adjacent",
    },
    {
        "item_id": "lb_iz_etiz_bbr_lag_2025",
        "name": "Izegem consol ETIZ BBR lag -4.5m (JR2024) distorts 2025 consol",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>ETIZ",
        "annual_cost_eur": "0", "total_cost_eur": "4524571",
        "tco_notes": "Strong residual opacity; consol BBR 10.1m vs core 14.4m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "ETIZ agency",
        "stated_goal": "Agency consolidation", "measured_outcome": "J2 consol uses 2024 ETIZ",
        "absurdity_score": "6.5", "cost_score": "4.5", "difficulty": "5.0",
        "priority_index": "5.5", "cut_proposal": "ETIZ JR2025 FOI",
        "status": "active", "struck_reason": "", "notes": "tick853 FOI-adjacent lag",
    },
    {
        "item_id": "lb_iz_ocmw_aid_4m_2025",
        "name": "Izegem OCMW individual aid 4.0m 2025",
        "level": "L5", "type": "transfer",
        "hierarchy_path": "Vlaanderen>Gemeenten>Izegem>OCMW",
        "annual_cost_eur": "3962953", "total_cost_eur": "3962953",
        "tco_notes": "Strong; dual Landen 2.2m Ieper 6.5m",
        "confidence": "strong", "source_id": SRC,
        "beneficiaries": "OCMW clients",
        "stated_goal": "Social safety net", "measured_outcome": "J5 outturn",
        "absurdity_score": "3.0", "cost_score": "3.5", "difficulty": "7.0",
        "priority_index": "3.25", "cut_proposal": "Outcomes FOI",
        "status": "active", "struck_reason": "", "notes": "tick853 safety-net",
    },
    {
        "item_id": "lb_dual_izegem_landen_tick853",
        "name": "Dual Izegem 204m vs Landen 101m city residual",
        "level": "L5", "type": "ops",
        "hierarchy_path": "Belgium>dual>vl_cities",
        "annual_cost_eur": "0", "total_cost_eur": "203558009",
        "tco_notes": "Strong dual not TE-additive; Izegem named L5 subsidies + Farys debt split vs Landen debt intensity",
        "confidence": "strong", "source_id": SRC_DUAL,
        "beneficiaries": "VL mid cities",
        "stated_goal": "Residual dual hole-fill", "measured_outcome": "JR2025 dual",
        "absurdity_score": "4.0", "cost_score": "5.5", "difficulty": "5.0",
        "priority_index": "4.75", "cut_proposal": "Cross FOI",
        "status": "active", "struck_reason": "", "notes": "tick853",
    },
]
nl = append_csv("docs/doge/data/leaderboard.csv", lbs)

sources = [
    {
        "source_id": SRC,
        "title": "Stad+OCMW Izegem Jaarrekening 2025 (BBC consolidatie, 107p) + DOC2 toelagen",
        "url": URL,
        "publisher": "Stad Izegem",
        "accessed_date": "2026-08-05",
        "source_class": "primary_jaarrekening",
        "notes": "GR 2026-06-22 pub 2026-06-29; assets 203.6m equity 176.4m fin debt 18.7m (Farys 9.8m) expl 57.1/51.4m AFM +3.1m BBR 14.4m personnel 27.7m toelagen 12.3m named DOC2; tick853",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual residual Izegem JR2025 vs Landen JR2025 tick853",
        "url": URL,
        "publisher": "AIpolitics DOGE dual",
        "accessed_date": "2026-08-05",
        "source_class": "derived_dual",
        "notes": "Not TE-additive; Izegem 204m vs Landen 101m; dual residual hole-fill",
    },
]
ns = append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": EID,
    "name_nl": "Stad Izegem",
    "name_fr": "Ville d'Izegem",
    "name_en": "City of Izegem",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.izegem.be",
    "foi_email": "1780@izegem.be",
    "foi_postal": "Korenmarkt 10 8870 Izegem",
    "notes": "JR2025 assets 204m equity 176m cash 8.7m expl 57/51m personnel 28m fin debt 19m (Farys 9.8m) AFM +3.1m BBR 14.4m toelagen 12.3m named DOC2; tick853",
}]
ne = append_csv("docs/doge/data/entities.csv", entities)

foi = [{
    "gap_id": "gap_izegem_etiz_loans_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Izegem_L5",
    "entity_id": EID,
    "what_is_missing": "ETIZ JR2025 full accounts (consol BBR still uses 2024 lag -4.525m); MJP2026 planned new loans 14.989m lender schedule and project map; residual lender schedule for non-Farys fin debt 8.829m",
    "why_it_matters": "204m city+OCMW with solid AFM +3.1m and strong public toelagen DOC2, but agency lag + planned 15m 2026 debt jump is residual FOI-adjacent L5",
    "priority": "7",
    "recipient_body": "Stad Izegem / financieel directeur / openbaarheid",
    "recipient_email": "1780@izegem.be",
    "recipient_postal": "https://www.izegem.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_izegem_etiz_loans_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": "cmt_iz_fin_debt_19m_2025",
    "linked_leaderboard_id": "lb_iz_etiz_bbr_lag_2025",
    "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick853 primary JR2025; ready draft; do not send; subsidies largely public via DOC2",
}]
nf = append_csv("docs/doge/data/foi_queue.csv", foi)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rq_fields = reader.fieldnames
    rq_rows = list(reader)

for r in rq_rows:
    if r["task_id"] == "rq_843":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (r.get("notes") or "") + " | tick853 Izegem JR2025 dual Landen; assets 204m fin debt 19m AFM +3.1m named toelagen DOC2"
        print("rq_843 done")
        break

if not any(r["task_id"] == "rq_844" for r in rq_rows):
    rq_rows.append({
        "task_id": "rq_844",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Izegem JR2025 filled tick853; residual Roeselare portal/Lier portal/VUB machine-readable/skeyes residual",
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned tick853 after Izegem dual Landen",
    })
    print("spawned rq_844")

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
        r["last_unit_id"] = "rq_843"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = "tick853 Izegem JR2025 dual Landen; FOI gap_izegem_etiz_loans_l5; next rq_844 residual dual L5; progress@860 in 7; rq_116 deferred"
with ls_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ls_fields, lineterminator="\n")
    w.writeheader()
    for r in ls_rows:
        w.writerow({k: r.get(k, "") for k in ls_fields})
print("DONE budgets", nb, "cmt", nc, "lb", nl, "src", ns, "ent", ne, "foi", nf)

# tick 443: Alterfin AR 2025 (+2024 dual) Belgian cooperative impact finance L5
import csv
import json
import shutil
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
RAW = DATA / "raw"
NOW = "2026-08-02T12:15:00Z"
TICK = 443
UNIT = "rq_434"
SRC = "src_alterfin_ar_2025"
URL = "https://www.alterfin.be/publications"

# Copy PDFs
for src, dst in [
    (
        Path(r"C:\Users\karel\.grok\sessions\C%3A%5CUsers%5Ckarel%5Cdev%5CAIpolitics\019fa67c-d539-7cf3-991a-2a67c778c282\downloads\2.pdf"),
        RAW / "alterfin_ar_2025_en.pdf",
    ),
    (
        Path(r"C:\Users\karel\.grok\sessions\C%3A%5CUsers%5Ckarel%5Cdev%5CAIpolitics\019fa67c-d539-7cf3-991a-2a67c778c282\downloads\1.pdf"),
        RAW / "alterfin_ar_2024_en.pdf",
    ),
]:
    if src.exists() and not dst.exists():
        shutil.copy2(src, dst)

# 2025 key (EUR unless noted)
Y2025 = {
    "members": 5828,
    "members_indiv": 5644,
    "members_inst": 184,
    "capital": 69697875,
    "capital_indiv": 59800000,  # ~59.8m
    "capital_inst": 9900000,  # 9.9m
    "capital_delta": -1110000,  # -1.1m
    "new_members": 157,
    "portfolio_mgmt_adv_eur": 122100000,  # 122.1m under mgmt+advisory
    "portfolio_mgmt_adv_usd": 143600000,  # 143.6m USD +3.7% record
    "portfolio_mgmt_eur": 98500000,  # 98.5m under management
    "portfolio_mgmt_usd": 115800000,  # 115.8m USD record
    "disbursed_eur": 95000000,  # key figures 95m
    "disbursed_usd": 108000000,  # >108m USD record under mgmt
    "advisory_disbursed_usd": 26700000,
    "advisory_disbursed_eur": 23200000,
    "partners": 142,
    "countries": 32,
    "agri_orgs": 57,
    "mfis": 76,
    "funds": 9,
    "new_partners": 8,
    "left_partners": 12,
    "benef_mfi": 4117870,
    "benef_farmers": 199922,
    "benef_families": 4317792,
    "total_assets": 164304750,
    "net_loan_portfolio": 91988344,
    "investments_eur": 65345069,
    "financial_fa": 3153215,
    "equity": 73104599,
    "debt": 90273842,
    "debt_equity": 1.20,
    "income_total": 9782153,
    "income_portfolio": 7392491,
    "income_advisory": 366401,
    "income_ta": 36839,
    "income_eur_invest": 1986421,
    "fin_costs": -3653870,
    "fin_margin": 6128283,
    "op_costs": -3518188,
    "staff_costs": -2651835,
    "gross_op_margin": 2610095,
    "cost_of_risk": -1609124,
    "net_result": 733222,
    "taxes": -179689,
    "dividend_rate": 0.01,  # proposed 1%
    "aum_fsma": 226136743,  # FSMA definition >100m threshold
    "fx_hedge": 38028743,
    "irs_notional": 23803249,
    "other_funding": 52000000,  # key figures
    "fefisol_capacity": 27900000,
    "fefisol_invested": 23100000,
    "fefisol_partners": 40,
    "fefisol_dual_alterfin": 12900000,  # 19 partners also direct Alterfin
    "africa_portfolio": 38000000,
    "latam_portfolio": 46000000,
    "asia_portfolio": 28000000,
    "intl_portfolio": 10000000,
    "mgmt_share_pct": 0.80,  # ~80% under mgmt vs advisory ~20%
}

Y2024 = {
    "members": 5901,
    "capital": 70810938,
    "portfolio_mgmt_adv_eur": 133000000,
    "disbursed_eur": 96000000,
    "partners": 143,
    "countries": 31,
    "agri": 57,
    "mfis": 77,
    "benef_families": 4960790,
    "net_result": 839033,
    "total_assets": 168581348,
    "net_loan_portfolio": 99253363,
    "equity": 74181468,
    "debt_equity": 1.22,
    "gross_op_margin": 2258151,
    "cost_of_risk": -1239388,
}

# BIO dual loan USD 5m to Alterfin (public BIO site)
BIO_ALTERFIN_USD = 5000000

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Alterfin Annual Report 2025 cooperative capital portfolio P&L dual BIO",
            "url": URL,
            "publisher": "Alterfin CV",
            "accessed_date": "2026-08-02",
            "source_class": "official_annual_report",
            "notes": (
                f"capital 69.7m members 5828; portfolio mgmt+adv 122.1m EUR / 143.6m USD; "
                f"net result 0.73m; AUM FSMA 226m; tax break abolished; dual BIO/DGD; tick{TICK}"
            ),
        }
    )
if not any(r["source_id"] == "src_alterfin_ar_2024" for r in src):
    src.append(
        {
            "source_id": "src_alterfin_ar_2024",
            "title": "Alterfin Annual Report 2024 dual prior year",
            "url": URL,
            "publisher": "Alterfin CV",
            "accessed_date": "2026-08-02",
            "source_class": "official_annual_report",
            "notes": f"capital 70.8m portfolio 133m members 5901; dual tick{TICK}",
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "entities.csv", encoding="utf-8", newline="") as f:
    ent = list(csv.DictReader(f))
    ef = list(ent[0].keys())
if not any(r.get("entity_id") == "alterfin" for r in ent):
    row = {k: "" for k in ef}
    row.update(
        {
            "entity_id": "alterfin",
            "name_nl": "Alterfin CV",
            "name_fr": "Alterfin SC",
            "name_en": "Alterfin cooperative development finance",
            "level": "asbl",
            "parent_id": "sec_federal",
            "community_language": "bi",
            "website": "https://www.alterfin.be",
            "notes": "Belgian co-op 1994; private capital to MFI/agri Global South; dual BIO/Kampani/Enabel/DGD; tick443",
        }
    )
    ent.append(row)
with open(DATA / "entities.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ef, extrasaction="ignore")
    w.writeheader()
    w.writerows(ent)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add_bud(bid, entity, year, amount, basis, notes, conf="strong"):
    if any(r["budget_id"] == bid for r in bud):
        return False
    bud.append(
        {
            "budget_id": bid,
            "entity_id": entity,
            "year": str(year),
            "amount_eur": str(int(round(amount))),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": SRC if year == 2025 else "src_alterfin_ar_2024",
            "confidence": conf,
            "notes": notes,
        }
    )
    return True


n_bud = 0

# 2025 core
core_2025 = [
    ("bud_alterfin_capital_2025", Y2025["capital"], "stock", f"Alterfin co-op capital {Y2025['capital']/1e6:.2f}m from {Y2025['members']} members EOY2025 (-1.1m YoY first decline; tax break abolished); tick{TICK}"),
    ("bud_alterfin_capital_indiv_2025", Y2025["capital_indiv"], "stock", f"Individual members capital ~{Y2025['capital_indiv']/1e6:.1f}m (86pct; avg 10.6k); tick{TICK}"),
    ("bud_alterfin_capital_inst_2025", Y2025["capital_inst"], "stock", f"Institutional members capital {Y2025['capital_inst']/1e6:.1f}m (14pct; avg 54k); tick{TICK}"),
    ("bud_alterfin_port_mgmt_adv_eur_2025", Y2025["portfolio_mgmt_adv_eur"], "stock", f"Total investment portfolio under mgmt+advisory {Y2025['portfolio_mgmt_adv_eur']/1e6:.1f}m EUR (-8.2pct FX); dual USD 143.6m +3.7pct record; tick{TICK}"),
    ("bud_alterfin_port_mgmt_adv_usd_2025", Y2025["portfolio_mgmt_adv_usd"], "stock", f"Portfolio mgmt+advisory USD face {Y2025['portfolio_mgmt_adv_usd']/1e6:.1f}m (amount stores USD; no FX invent); tick{TICK}"),
    ("bud_alterfin_port_mgmt_eur_2025", Y2025["portfolio_mgmt_eur"], "stock", f"Portfolio under Alterfin management {Y2025['portfolio_mgmt_eur']/1e6:.1f}m EUR; tick{TICK}"),
    ("bud_alterfin_port_mgmt_usd_2025", Y2025["portfolio_mgmt_usd"], "stock", f"Portfolio under management USD {Y2025['portfolio_mgmt_usd']/1e6:.1f}m record; tick{TICK}"),
    ("bud_alterfin_disbursed_eur_2025", Y2025["disbursed_eur"], "outturn", f"Disbursed {Y2025['disbursed_eur']/1e6:.0f}m EUR 2025 key figures; tick{TICK}"),
    ("bud_alterfin_disbursed_usd_2025", Y2025["disbursed_usd"], "outturn", f"Disbursements under management >{Y2025['disbursed_usd']/1e6:.0f}m USD record; tick{TICK}"),
    ("bud_alterfin_advisory_disb_eur_2025", Y2025["advisory_disbursed_eur"], "outturn", f"Advisory portfolio disbursements {Y2025['advisory_disbursed_eur']/1e6:.1f}m EUR 2025; tick{TICK}"),
    ("bud_alterfin_assets_2025", Y2025["total_assets"], "stock", f"Total assets {Y2025['total_assets']/1e6:.1f}m EOY2025 (-3pct); tick{TICK}"),
    ("bud_alterfin_net_loan_2025", Y2025["net_loan_portfolio"], "stock", f"Net loan portfolio {Y2025['net_loan_portfolio']/1e6:.1f}m EUR (-7pct FX); tick{TICK}"),
    ("bud_alterfin_eur_investments_2025", Y2025["investments_eur"], "stock", f"Euro treasury investments {Y2025['investments_eur']/1e6:.1f}m (collateral for USD funding); tick{TICK}"),
    ("bud_alterfin_equity_2025", Y2025["equity"], "stock", f"Equity {Y2025['equity']/1e6:.1f}m EOY2025; tick{TICK}"),
    ("bud_alterfin_debt_2025", Y2025["debt"], "stock", f"Debt {Y2025['debt']/1e6:.1f}m (ratio debt/equity {Y2025['debt_equity']}); tick{TICK}"),
    ("bud_alterfin_income_2025", Y2025["income_total"], "outturn", f"Financial+operational income {Y2025['income_total']/1e6:.2f}m 2025; tick{TICK}"),
    ("bud_alterfin_portfolio_income_2025", Y2025["income_portfolio"], "outturn", f"Income from own portfolio {Y2025['income_portfolio']/1e6:.2f}m (-13pct); tick{TICK}"),
    ("bud_alterfin_fin_costs_2025", abs(Y2025["fin_costs"]), "outturn", f"Financial costs {abs(Y2025['fin_costs'])/1e6:.2f}m (-26pct); tick{TICK}"),
    ("bud_alterfin_op_costs_2025", abs(Y2025["op_costs"]), "outturn", f"Operational costs {abs(Y2025['op_costs'])/1e6:.2f}m (+8pct; FSMA licence prep); tick{TICK}"),
    ("bud_alterfin_staff_2025", abs(Y2025["staff_costs"]), "outturn", f"Staff costs {abs(Y2025['staff_costs'])/1e6:.2f}m 2025; tick{TICK}"),
    ("bud_alterfin_gross_margin_2025", Y2025["gross_op_margin"], "outturn", f"Gross operating margin {Y2025['gross_op_margin']/1e6:.2f}m (+16pct); tick{TICK}"),
    ("bud_alterfin_cost_of_risk_2025", abs(Y2025["cost_of_risk"]), "outturn", f"Cost of risk {abs(Y2025['cost_of_risk'])/1e6:.2f}m (+30pct lower recoveries); tick{TICK}"),
    ("bud_alterfin_net_result_2025", Y2025["net_result"], "outturn", f"Net result {Y2025['net_result']/1e6:.3f}m (-13pct); proposed dividend 1pct; tick{TICK}"),
    ("bud_alterfin_aum_fsma_2025", Y2025["aum_fsma"], "stock", f"FSMA AUM definition {Y2025['aum_fsma']/1e6:.1f}m (>100m threshold → full AIFM licence path H2-2026); tick{TICK}"),
    ("bud_alterfin_fefisol_invested_2025", Y2025["fefisol_invested"], "stock", f"Fefisol II invested {Y2025['fefisol_invested']/1e6:.1f}m / {Y2025['fefisol_partners']} partners (capacity ~27.9m; dual BIO co-founder class); tick{TICK}"),
    ("bud_alterfin_africa_port_2025", Y2025["africa_portfolio"], "stock", f"Africa portfolio ~{Y2025['africa_portfolio']/1e6:.0f}m EUR regional split; tick{TICK}"),
    ("bud_alterfin_latam_port_2025", Y2025["latam_portfolio"], "stock", f"Latin America portfolio ~{Y2025['latam_portfolio']/1e6:.0f}m EUR; tick{TICK}"),
    ("bud_alterfin_asia_port_2025", Y2025["asia_portfolio"], "stock", f"Asia portfolio ~{Y2025['asia_portfolio']/1e6:.0f}m EUR; tick{TICK}"),
    ("bud_bio_alterfin_loan_usd", BIO_ALTERFIN_USD, "commitment", f"BIO loan to Alterfin USD {BIO_ALTERFIN_USD/1e6:.0f}m face (BIO investment page; dual cooperative); tick{TICK}"),
]
for bid, amt, basis, notes in core_2025:
    conf = "medium" if "usd" in bid or "africa" in bid or "latam" in bid or "asia" in bid or "bio_alterfin" in bid else "strong"
    if add_bud(bid, "alterfin" if "bio_" not in bid else "bio_invest", 2025, amt, basis, notes, conf):
        n_bud += 1

# headcounts
for key, val, note in [
    ("bud_alterfin_members_2025", Y2025["members"], "co-op members headcount"),
    ("bud_alterfin_partners_2025", Y2025["partners"], "active partners"),
    ("bud_alterfin_mfis_2025", Y2025["mfis"], "MFI partners"),
    ("bud_alterfin_agri_2025", Y2025["agri_orgs"], "agri SME/coop partners"),
    ("bud_alterfin_benef_families_2025", Y2025["benef_families"], "end-beneficiary families class"),
]:
    if add_bud(key, "alterfin", 2025, val, "estimate", f"Alterfin {note} {val} 2025 (not EUR); tick{TICK}", "strong"):
        n_bud += 1

# 2024 dual
for bid, amt, basis, notes in [
    ("bud_alterfin_capital_2024", Y2024["capital"], "stock", f"Alterfin capital {Y2024['capital']/1e6:.2f}m / {Y2024['members']} members EOY2024; tick{TICK}"),
    ("bud_alterfin_port_mgmt_adv_eur_2024", Y2024["portfolio_mgmt_adv_eur"], "stock", f"Portfolio mgmt+advisory {Y2024['portfolio_mgmt_adv_eur']/1e6:.0f}m EUR 2024 record then; tick{TICK}"),
    ("bud_alterfin_disbursed_2024", Y2024["disbursed_eur"], "outturn", f"Disbursed {Y2024['disbursed_eur']/1e6:.0f}m 2024; tick{TICK}"),
    ("bud_alterfin_net_result_2024", Y2024["net_result"], "outturn", f"Net result {Y2024['net_result']/1e6:.3f}m 2024; tick{TICK}"),
    ("bud_alterfin_assets_2024", Y2024["total_assets"], "stock", f"Total assets {Y2024['total_assets']/1e6:.1f}m 2024; tick{TICK}"),
    ("bud_alterfin_net_loan_2024", Y2024["net_loan_portfolio"], "stock", f"Net loan portfolio {Y2024['net_loan_portfolio']/1e6:.1f}m 2024; tick{TICK}"),
]:
    if add_bud(bid, "alterfin", 2024, amt, basis, notes, "strong"):
        n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())

n_cmt = 0
if not any(r.get("commitment_id") == "cmt_alterfin_coop_2024_25" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_alterfin_coop_2024_25",
            "title": "Alterfin Belgian cooperative DFI capital+portfolio 2024-2025",
            "entity_id": "alterfin",
            "beneficiary": "MFI and agri SMEs Global South / Belgian co-op members",
            "legal_basis": "Cooperative under Belgian law; development fund status; AIFM transition 2025-26",
            "decision_date": "1994-01-01",
            "start_year": "2024",
            "end_year": "2025",
            "total_envelope_eur": str(Y2025["portfolio_mgmt_adv_eur"]),
            "cash_by_year": json.dumps(
                {
                    "2024": {
                        "capital": Y2024["capital"],
                        "portfolio_eur": Y2024["portfolio_mgmt_adv_eur"],
                        "net_result": Y2024["net_result"],
                        "members": Y2024["members"],
                    },
                    "2025": {
                        "capital": Y2025["capital"],
                        "portfolio_eur": Y2025["portfolio_mgmt_adv_eur"],
                        "portfolio_usd": Y2025["portfolio_mgmt_adv_usd"],
                        "net_result": Y2025["net_result"],
                        "members": Y2025["members"],
                        "aum_fsma": Y2025["aum_fsma"],
                        "tax_break": "abolished; capital first decline",
                        "fefisol_m": Y2025["fefisol_invested"],
                        "bio_loan_usd": BIO_ALTERFIN_USD,
                    },
                    "dual": "BIO Kampani Enabel DGD Belgian impact ecosystem",
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Rural financial inclusion and smallholder agriculture finance",
            "cut_option": "Not public budget cut target; private co-op capital; track tax-incentive policy dual",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "BE>private_coop>Alterfin",
            "notes": f"Private solidarity capital dual public DFI BIO; tick{TICK}",
        }
    )
    n_cmt += 1

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def add_lb(iid, name, annual, total, tco, conf, benef, goal, outcome, abs_s, cost_s, diff, prio, cut, notes, hpath, typ="ops"):
    if any(r.get("item_id") == iid for r in lb):
        return False
    lb.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": hpath,
            "annual_cost_eur": str(int(round(annual))),
            "total_cost_eur": str(int(round(total))),
            "tco_notes": tco,
            "confidence": conf,
            "source_id": SRC,
            "beneficiaries": benef,
            "stated_goal": goal,
            "measured_outcome": outcome,
            "absurdity_score": str(abs_s),
            "cost_score": str(cost_s),
            "difficulty": str(diff),
            "priority_index": str(prio),
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": notes,
        }
    )
    return True


n_lb = 0
rows = [
    (
        "lb_alterfin_portfolio_122m",
        "Alterfin portfolio under mgmt+advisory 122m EUR 2025",
        122.1e6,
        122.1e6,
        "Strong AR: 122.1m EUR (-8.2pct FX) vs USD 143.6m +3.7pct record; dual BIO/Kampani Belgian impact stack",
        "strong",
        "MFI and agri partners Global South",
        "Private cooperative development finance",
        "Not public TE; dual public DFI BIO",
        2.5,
        6.5,
        4,
        4.7,
        "Map public capital subsidies if any; dual Fefisol/BIO",
        f"tick{TICK}",
        "BE>Alterfin>portfolio",
    ),
    (
        "lb_alterfin_capital_70m",
        "Alterfin co-op capital 69.7m / 5828 members 2025",
        69.7e6,
        69.7e6,
        "Strong: first capital decline -1.1m after abolition of 5pct tax break for development-fund shares",
        "strong",
        "Belgian individual+institutional co-op members",
        "Mobilise private solidarity capital",
        "Policy incentive change material",
        4.5,
        5.5,
        5,
        5.0,
        "Score tax-break removal vs ODA cuts dual",
        f"tick{TICK}",
        "BE>Alterfin>capital",
    ),
    (
        "lb_alterfin_net_result_0_73m",
        "Alterfin net result 0.73m 2025 (dividend 1pct proposed)",
        0.733e6,
        0.733e6,
        "Strong P&L: gross margin +16pct; cost of risk +30pct; net -13pct YoY",
        "strong",
        "Co-op members",
        "Financial sustainability of impact model",
        "Positive result maintained",
        2.0,
        2.5,
        3,
        2.5,
        "Not waste; transparency of risk costs",
        f"tick{TICK}",
        "BE>Alterfin>result",
    ),
    (
        "lb_alterfin_tax_break_abolition",
        "Development-fund share tax break abolished (Alterfin capital impact)",
        1110000,
        1110000,
        "Strong AR: capital -1.1m first decline attributed partly to end of 5pct tax reduction; dual fiscal policy",
        "strong",
        "Belgian retail impact investors",
        "Fiscal incentive for approved development funds",
        "Co-op capital headwind class",
        5.5,
        3.5,
        4,
        4.5,
        "Publish fiscal cost of former TE if FPS inventory; dual ODA cuts",
        f"tick{TICK}",
        "Federal>taxex>dev_fund_shares",
    ),
    (
        "lb_alterfin_fsma_aum_226m",
        "Alterfin FSMA AUM 226m crosses full AIFM licence threshold",
        226.1e6,
        226.1e6,
        "Strong AR annex: assets+swaps AUM 226m >100m; full OPCA/AIFM licence path H2-2026; compliance cost up",
        "strong",
        "Regulated impact fund investors",
        "Investor protection / systemic risk rules",
        "Regulatory step-up not pure waste",
        3.5,
        6.5,
        5,
        5.1,
        "Track compliance cost vs member capital",
        f"tick{TICK}",
        "BE>Alterfin>FSMA_AIFM",
    ),
    (
        "lb_alterfin_fefisol_23m",
        "Fefisol II Africa fund 23.1m invested / 40 partners (Alterfin co-founder)",
        23.1e6,
        27.9e6,
        "Strong AR: capacity ~27.9m; dual BIO among funders; 12.9m also direct Alterfin partners",
        "strong",
        "African MFI and agri partners",
        "Europe solidarity fund Africa focus",
        "Multi-DFI Belgian ecosystem",
        3.0,
        4.5,
        4,
        3.9,
        "Publish partner L5 dual BIO",
        f"tick{TICK}",
        "BE>Alterfin>Fefisol",
    ),
    (
        "lb_bio_alterfin_5m_usd",
        "BIO loan to Alterfin 5m USD (Belgian dual stack)",
        5e6,
        5e6,
        "Medium BIO investment page USD face; dual cooperative DFI financing",
        "medium",
        "Alterfin co-op / end partners",
        "DFI support to Belgian impact cooperative",
        "Named public",
        3.0,
        3.5,
        3,
        3.4,
        "Reconcile in BIO portfolio L5",
        f"tick{TICK}",
        "Federal>BIO>Alterfin",
    ),
    (
        "lb_alterfin_cost_of_risk_1_6m",
        "Alterfin cost of risk 1.61m 2025",
        1.61e6,
        1.61e6,
        "Strong P&L: +30pct YoY on lower recoveries; still green risk indicators narrative",
        "strong",
        "Co-op capital buffer",
        "Credit risk on Global South loans",
        "Material vs 0.73m net",
        4.0,
        3.5,
        4,
        3.8,
        "Publish default by region L5",
        f"tick{TICK}",
        "BE>Alterfin>risk",
    ),
    (
        "lb_alterfin_staff_2_65m",
        "Alterfin staff costs 2.65m 2025",
        2.65e6,
        2.65e6,
        "Strong: +6pct; multi-country investment managers; dual op costs +8pct licence prep",
        "strong",
        "Alterfin employees",
        "Operate cooperative DFI",
        "Core overhead",
        2.5,
        3.5,
        3,
        3.2,
        "Benchmark vs BIO opex dual",
        f"tick{TICK}",
        "BE>Alterfin>staff",
    ),
    (
        "lb_alterfin_dual_bio_kampani",
        "Belgian private impact stack Alterfin+Kampani+BIO dual Enabel/DGD",
        122.1e6,
        122.1e6 + 2e6 + 1196e6,
        "Medium dual map: Alterfin 122m portfolio + Kampani BIO equity 2m + BIO assets 1.2bn; not additive TE",
        "medium",
        "Belgian impact ecosystem",
        "Complement public ODA with private co-op/DFI capital",
        "Structural dual architecture",
        3.5,
        7.0,
        6,
        5.4,
        "Publish joint capital flow diagram public-private",
        f"tick{TICK}",
        "BE>dual>impact_finance",
    ),
]
for args in rows:
    if add_lb(*args):
        n_lb += 1

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())
for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: Alterfin AR2025 capital 69.7m portfolio 122m EUR/144m USD net 0.73m "
            f"tax-break abolition dual BIO/Kampani; rq_116 deferred"
        )
if not any(r.get("task_id") == "rq_435" for r in rq):
    rq.append(
        {
            "task_id": "rq_435",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": "",
            "notes": f"Spawned tick{TICK} after Alterfin dual; rq_116 SWA deferred",
        }
    )
with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsf = list(ls[0].keys())
ls[-1]["last_tick_utc"] = NOW
ls[-1]["last_unit_id"] = UNIT
ls[-1]["ticks_completed"] = str(TICK)
ls[-1]["mode"] = "continuous"
ls[-1]["current_sprint"] = "hole_fill"
ls[-1]["paused"] = "no"
ls[-1]["notes"] = (
    f"Scheduler 60s. Next prio5 rq_435; rq_116 SWA deferred. "
    f"tick{TICK} Alterfin 70m capital + 122m portfolio dual BIO."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **Alterfin AR 2025 Belgian cooperative impact finance dual BIO/Kampani**)
- Found (strong primary Alterfin Annual Report 2025 + 2024 dual):
  - **Capital €69.70m** / **5,828** members (indiv 5,644 / inst 184); **first decline −€1.1m** after **abolition of 5% tax break** on development-fund shares
  - **Portfolio mgmt+advisory:** **€122.1m** (−8.2% FX) vs **USD 143.6m** (+3.7% record); under mgmt **€98.5m** / **USD 115.8m**
  - Disbursed key **€95m** · under-mgmt **>USD 108m** record · advisory **€23.2m** / **USD 26.7m**
  - Partners **142** in **32** countries (MFI **76** · agri **57** · funds **9**); families class **~4.32m**
  - BS assets **€164.3m** · net loans **€92.0m** · equity **€73.1m** · debt/equity **1.20**
  - P&L net **€733k** (−13%); gross margin **+16%**; cost of risk **€1.61m** (+30%); proposed dividend **1%**
  - FSMA AUM **€226.1m** → full AIFM/OPCA licence path H2-2026; Fefisol II **€23.1m**/40 partners; BIO loan **USD 5m** dual
- Wrote: sources +2; entity alterfin; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_434=done; spawn **rq_435**; ticks={TICK}
- FOI: none new (private co-op; partner L5 residual optional not material public euro opacity)
- Next: prio5 **rq_435**; deferred **rq_116** SWA
"""
with open(Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md"), "ab") as f:
    f.write(log.encode("utf-8"))

print(f"OK tick{TICK} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")

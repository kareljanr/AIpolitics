# tick 442: BIO AR 2025 named investment L5 + financials residual + dual Kampani
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T11:45:00Z"
TICK = 442
UNIT = "rq_433"
SRC = "src_bio_ar2025_l5_named"
URL = "https://report.bio-invest.be/approved-investments"

# Aggregates 2025 (EUR m unless noted)
AGG = {
    "approvals_m": 235.0,  # 30 projects; DGD AR said 240 — dual keep both
    "approvals_n": 30,
    "approvals_n_2024": 22,
    "signed_m": 166.0,
    "signed_n": 21,
    "committed_stock_m": 1200.0,  # 171 projects
    "committed_projects": 171,
    "signed_stock_m": 1033.0,
    "assets_m": 1196.0,
    "equity_up_m": 16.7,
    "income_m": 55.3,
    "gross_margin_m": 54.5,
    "net_margin_m": 40.2,
    "opex_delta_m": 2.8,
    "cost_of_risk_m": 20.1,
    "fx_result_m": -5.9,
    "op_result_m": 20.1,
    "net_profit_m": 9.0,
    "retained_earnings_m": 34.9,
    "dividend_m": 4.5,
    "africa_share_approvals": 0.55,
    "gender_share_2024_25": 0.57,
    "jobs_direct_eoy2024": 388000,
    "direct_enterprise_approvals_2025": 11,
    "direct_enterprise_approvals_2024": 2,
    "mgmt_contract_5y_m": 1200.0,  # capital recycle 2024-28 strategy
    "capital_subsidies_extra_m": 85.0,  # State capital subsidies higher risk/impact
}

# Named 2025 approvals/signs with published amounts (store EUR as EUR; USD separate with conf medium)
# amount_eur for USD: leave as USD face * note — DOGE: no invent FX; store face as amount with notes
NAMED_EUR = {
    "acep_group": (1.5e6, "loan", "EUR", "ACEP Group pan-African microfinance BF/Niger/MG/CM"),
    "coris_holding": (20e6, "equity", "EUR", "Coris Holding banking group Francophone West Africa"),
    "fefisol_ii": (2e6, "follow_on", "EUR", "FEFISOL 2 fund rural financial inclusion Africa"),
    "foodsco": (3e6, "loan", "EUR", "Foods'Co Ivorian food processing"),
    "glacier_products": (8e6, "loan", "EUR", "Glacier Products Kenya dairy"),
    "kampani": (2e6, "equity", "EUR", "Kampani Belgian impact fund smallholder farming"),
    "limbua_group": (2e6, "loan", "EUR", "Limbua Group Kenya macadamia mango avocado"),
    "orchidia": (10e6, "equity", "EUR", "Orchidia Pharmaceutical Industries Egypt ophthalmic generics"),
    "vital_finance": (3e6, "loan", "EUR", "Vital Finance Benin microfinance"),
}
NAMED_USD = {
    "adenia_ef_ii": (15e6, "equity", "USD", "Adenia Entrepreneurial Fund II Africa SME"),
    "amartha": (15e6, "loan", "USD", "Amartha Indonesia microfinance fintech"),
    "banco_atlantida_sv": (15e6, "loan", "USD", "Banco Atlantida El Salvador SME"),
    "banco_ademi": (15e6, "loan", "USD", "Banco Multiple ADEMI Dominican MSME"),
    "banco_popular_hn": (1.5e6, "equity", "USD", "Banco Popular Honduras microfinance additional"),
    "bandwidth_cloud": (15e6, "loan", "USD", "Bandwidth and Cloud Services optic fiber SSA 7 markets"),
    "ecom": (10e6, "loan", "USD", "ECOM Agroindustrial coffee cocoa cotton nuts"),
    "excelsior_vn_ii": (15e6, "equity", "USD", "Excelsior Capital Vietnam Partners II"),
    "helios_clear": (10e6, "equity", "USD", "Helios CLEAR Fund climate Africa"),
    "lendable_msme_2": (10e6, "equity", "USD", "Lendable MSME Fintech Credit Fund 2"),
    "super_silica": (3.7e6, "loan", "USD", "Super Silica Bangladesh green precipitated silica"),
    "ukraine_rebuild_fund": (6e6, "investment", "USD", "Rebuilding Ukraine Fund second Ukraine investment"),
}
# Sum EUR named for check
EUR_SUM = sum(v[0] for v in NAMED_EUR.values())
USD_SUM = sum(v[0] for v in NAMED_USD.values())

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "BIO Annual Report 2025 named approvals + financials + dual Kampani",
            "url": URL,
            "publisher": "BIO Belgian Investment Company",
            "accessed_date": "2026-08-02",
            "source_class": "official_annual_report",
            "notes": (
                f"approvals 235m/30 signed 166m/21 stock 1.2bn/171; named L5 EUR+USD; "
                f"Kampani 2m; dual DGD AR 240m; tick{TICK}"
            ),
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

# entity kampani if missing
with open(DATA / "entities.csv", encoding="utf-8", newline="") as f:
    ent = list(csv.DictReader(f))
    ef = list(ent[0].keys())
if not any(r.get("entity_id") == "kampani" for r in ent):
    ent.append(
        {
            "entity_id": "kampani",
            "name_nl": "Kampani",
            "name_fr": "Kampani",
            "name_en": "Kampani impact investment fund smallholder farming",
            "level": "asbl",
            "parent_id": "sec_federal",
            "community_language": "bi",
            "website": "https://www.kampani.org/",
            "notes": "Belgian impact-first agri fund; BIO equity 2m 2025; dual Enabel/BIO ecosystem; tick442",
        }
    )
    # fix if fieldnames differ
    row = ent[-1]
    for k in ef:
        if k not in row:
            row[k] = ""
    ent[-1] = {k: row.get(k, "") for k in ef}
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
            "source_id": SRC,
            "confidence": conf,
            "notes": notes,
        }
    )
    return True


n_bud = 0

# Aggregates (skip if prior identical IDs exist with same amount - use new l5 ids)
pairs = [
    ("bud_bio_approvals_2025_ar25", AGG["approvals_m"] * 1e6, "commitment", f"BIO approvals {AGG['approvals_m']}m / {AGG['approvals_n']} projects 2025 AR (dual DGD AR 240m); tick{TICK}"),
    ("bud_bio_signed_2025", AGG["signed_m"] * 1e6, "commitment", f"BIO signed investments {AGG['signed_m']}m / {AGG['signed_n']} projects 2025; tick{TICK}"),
    ("bud_bio_committed_stock_2025", AGG["committed_stock_m"] * 1e6, "stock", f"BIO committed portfolio stock {AGG['committed_stock_m']}m / {AGG['committed_projects']} projects EOY2025 class (+10pct YoY); tick{TICK}"),
    ("bud_bio_signed_stock_2025", AGG["signed_stock_m"] * 1e6, "stock", f"BIO signed investments stock {AGG['signed_stock_m']}m 2025; tick{TICK}"),
    ("bud_bio_income_2025_ar", AGG["income_m"] * 1e6, "outturn", f"BIO total income {AGG['income_m']}m 2025; tick{TICK}"),
    ("bud_bio_gross_margin_2025", AGG["gross_margin_m"] * 1e6, "outturn", f"BIO gross margin {AGG['gross_margin_m']}m 2025; tick{TICK}"),
    ("bud_bio_net_margin_2025", AGG["net_margin_m"] * 1e6, "outturn", f"BIO net margin {AGG['net_margin_m']}m 2025; tick{TICK}"),
    ("bud_bio_cost_of_risk_2025_ar", AGG["cost_of_risk_m"] * 1e6, "outturn", f"BIO cost of risk {AGG['cost_of_risk_m']}m 2025; tick{TICK}"),
    ("bud_bio_fx_result_2025", AGG["fx_result_m"] * 1e6, "outturn", f"BIO FX result {AGG['fx_result_m']}m 2025 (EUR appreciation); tick{TICK}"),
    ("bud_bio_op_result_2025", AGG["op_result_m"] * 1e6, "outturn", f"BIO operating result {AGG['op_result_m']}m 2025; tick{TICK}"),
    ("bud_bio_net_profit_2025_ar", AGG["net_profit_m"] * 1e6, "outturn", f"BIO net profit {AGG['net_profit_m']}m 2025; dual prior; tick{TICK}"),
    ("bud_bio_dividend_2025_ar", AGG["dividend_m"] * 1e6, "budgeted", f"BIO proposed dividend to Belgian State {AGG['dividend_m']}m 2025 (2nd consecutive year); tick{TICK}"),
    ("bud_bio_retained_earnings_2025", AGG["retained_earnings_m"] * 1e6, "stock", f"BIO retained earnings {AGG['retained_earnings_m']}m 2025; tick{TICK}"),
    ("bud_bio_equity_increase_2025", AGG["equity_up_m"] * 1e6, "outturn", f"BIO equity increase {AGG['equity_up_m']}m 2025 (capital grants + subsidy results + RE); tick{TICK}"),
    ("bud_bio_jobs_direct_2024", AGG["jobs_direct_eoy2024"], "estimate", f"BIO portfolio direct jobs ~{AGG['jobs_direct_eoy2024']} EOY2024 (headcount not EUR); tick{TICK}"),
    ("bud_bio_mgmt_contract_5y", AGG["mgmt_contract_5y_m"] * 1e6, "commitment", f"BIO investment strategy 2024-28 expected ~{AGG['mgmt_contract_5y_m']}m capital approvals ~150 projects class; tick{TICK}"),
    ("bud_bio_capital_subsidies_85m", AGG["capital_subsidies_extra_m"] * 1e6, "commitment", f"Belgian State capital subsidies extra {AGG['capital_subsidies_extra_m']}m for higher risk/impact under mgmt contract 2024-28; tick{TICK}"),
]
for bid, amt, basis, notes in pairs:
    conf = "strong"
    if "jobs" in bid:
        conf = "medium"
    if "mgmt_contract" in bid or "capital_subsidies" in bid:
        conf = "medium"
    if add_bud(bid, "bio_invest", 2025 if "2024" not in bid or "jobs" in bid else 2024, amt, basis, notes, conf):
        n_bud += 1

for key, (amt, instr, ccy, desc) in NAMED_EUR.items():
    if add_bud(
        f"bud_bio_l5_{key}_2025",
        "bio_invest" if key != "kampani" else "kampani",
        2025,
        amt,
        "commitment",
        f"BIO named {instr} {desc}: {amt/1e6:.1f}m {ccy} 2025 AR approved/signed list; tick{TICK}",
        "strong",
    ):
        n_bud += 1

for key, (amt, instr, ccy, desc) in NAMED_USD.items():
    # Store USD face in amount_eur field with clear note — no invent FX
    if add_bud(
        f"bud_bio_l5_{key}_2025_usd",
        "bio_invest",
        2025,
        amt,
        "commitment",
        (
            f"BIO named {instr} {desc}: {amt/1e6:.1f}m {ccy} face 2025 AR "
            f"(amount_eur stores USD face; no FX convert); tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1

if add_bud(
    "bud_bio_named_eur_sum_sample_2025",
    "bio_invest",
    2025,
    EUR_SUM,
    "derived",
    f"Sum of named EUR-denominated sample L5 {EUR_SUM/1e6:.1f}m of approvals 235m (partial list not full 30); tick{TICK}",
    "strong",
):
    n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

# commitments
with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())

n_cmt = 0
if not any(r.get("commitment_id") == "cmt_bio_l5_named_2025" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_bio_l5_named_2025",
            "title": "BIO 2025 named investment L5 sample + portfolio stocks",
            "entity_id": "bio_invest",
            "beneficiary": "Developing-country private sector / Belgian State (dividend)",
            "legal_basis": "BIO law + management contract 2024-2028; sole State shareholder",
            "decision_date": "2025-01-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(int(AGG["approvals_m"] * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "approvals_m": AGG["approvals_m"],
                    "signed_m": AGG["signed_m"],
                    "committed_stock_m": AGG["committed_stock_m"],
                    "signed_stock_m": AGG["signed_stock_m"],
                    "named_eur": {k: v[0] for k, v in NAMED_EUR.items()},
                    "named_usd_face": {k: v[0] for k, v in NAMED_USD.items()},
                    "africa_share": AGG["africa_share_approvals"],
                    "gender_share_2024_25": AGG["gender_share_2024_25"],
                    "kampani_eur_m": 2.0,
                    "capital_subsidies_extra_m": AGG["capital_subsidies_extra_m"],
                    "note": "Named list partial of 30 approvals; residual investees FOI gap_bio_l5_portfolio",
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Patient capital private sector developing countries dual Enabel/DGD",
            "cut_option": "Publish full outstanding by investee; dual capital subsidy cash path",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Federal>BIO>named_L5_2025",
            "notes": f"AR 2025 public named sample; dual cmt_bio_portfolio; tick{TICK}",
        }
    )
    n_cmt += 1

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

# FOI update
with open(DATA / "foi_queue.csv", encoding="utf-8", newline="") as f:
    foi = list(csv.DictReader(f))
    ff = list(foi[0].keys())
for r in foi:
    if r.get("gap_id") == "gap_bio_l5_portfolio":
        r["updated_utc"] = NOW
        r["notes"] = (
            (r.get("notes") or "")
            + f" | tick{TICK}: named 2025 approvals sample public (EUR+USD); residual full outstanding matrix + impairments still ready"
        )
        r["what_is_missing"] = (
            "Full outstanding investees EUR top50 multi-year; impairments by project; "
            "State/DGD capital grants cash path; residual names beyond 2025 approvals sample"
        )
with open(DATA / "foi_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ff, extrasaction="ignore")
    w.writeheader()
    w.writerows(foi)

# leaderboard
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
        "lb_bio_approvals_235m_2025",
        "BIO approvals 235m / 30 projects 2025 (record net since 2019)",
        235e6,
        235e6,
        "Strong AR: 235m/30 (+25pct projects vs 22); signed 166m/21; dual DGD AR 240m; stock 1.2bn/171",
        "strong",
        "Developing-country private sector",
        "DFI patient capital dual Enabel",
        "Africa 55pct; gender 57pct 2024-25; LDC/FCAS focus",
        3.5,
        7.0,
        5,
        5.4,
        "Publish full outstanding L5; dual capital subsidies 85m",
        f"tick{TICK}",
        "Federal>BIO>approvals",
    ),
    (
        "lb_bio_signed_166m_2025",
        "BIO signed investments 166m / 21 projects 2025",
        166e6,
        166e6,
        "Strong AR signed vs approved gap (execution lag); signed stock 1.033bn",
        "strong",
        "Investees / funds",
        "Close commitments to cash",
        "Pipeline conversion residual",
        3.5,
        6.5,
        4,
        5.1,
        "Track approval-to-sign lag",
        f"tick{TICK}",
        "Federal>BIO>signed",
    ),
    (
        "lb_bio_coris_20m",
        "BIO equity Coris Holding 20m EUR 2025",
        20e6,
        20e6,
        "Strong named AR: largest EUR sample line; West Africa banking group",
        "strong",
        "Coris Holding / Francophone West Africa",
        "Scale regional banking MSME access",
        "Named L5 public",
        3.0,
        4.5,
        4,
        3.9,
        "Monitor concentration/governance",
        f"tick{TICK}",
        "Federal>BIO>Coris",
    ),
    (
        "lb_bio_kampani_2m",
        "BIO equity Kampani 2m EUR 2025 (Belgian dual ecosystem)",
        2e6,
        2e6,
        "Strong: Belgian impact fund; dual Enabel early-stage + BIO scale; DGD AR Biophyto narrative",
        "strong",
        "Smallholder farmers via Kampani investees",
        "Missing-middle agri finance Belgium ecosystem",
        "Dual structure Enabel-Kampani-BIO",
        3.5,
        3.0,
        3,
        3.4,
        "Publish Kampani portfolio dual public",
        f"tick{TICK}",
        "Federal>BIO>Kampani",
    ),
    (
        "lb_bio_orchidia_10m",
        "BIO equity Orchidia Pharma Egypt 10m EUR 2025",
        10e6,
        10e6,
        "Strong named: first pharma direct investment class 2025",
        "strong",
        "Egyptian pharma / ophthalmic patients",
        "Local generics production dual health GPGs",
        "Named L5",
        3.0,
        4.0,
        4,
        3.7,
        "Track local production additionality",
        f"tick{TICK}",
        "Federal>BIO>Orchidia",
    ),
    (
        "lb_bio_usd_sample_face",
        f"BIO named USD sample face {USD_SUM/1e6:.1f}m 2025 (no FX convert)",
        USD_SUM,
        USD_SUM,
        f"Medium: USD face sum of published named lines {USD_SUM/1e6:.1f}m; amount stores USD; dual EUR sample {EUR_SUM/1e6:.1f}m",
        "medium",
        "Multi-region investees",
        "Diversified DFI portfolio",
        "Partial of 30 approvals",
        3.5,
        6.5,
        5,
        5.1,
        "Publish EUR equivalent series + full list",
        f"tick{TICK}",
        "Federal>BIO>usd_named_sample",
    ),
    (
        "lb_bio_cost_of_risk_20m",
        "BIO cost of risk 20.1m 2025",
        20.1e6,
        20.1e6,
        "Strong AR: elevated risk materialisation; dual net profit 9.0 after FX -5.9",
        "strong",
        "Belgian State shareholder / portfolio quality",
        "Credit risk on DFI portfolio",
        "Volatility watch vs dividend 4.5m",
        5.0,
        4.5,
        5,
        4.7,
        "Publish impairment by segment L5",
        f"tick{TICK}",
        "Federal>BIO>cost_of_risk",
    ),
    (
        "lb_bio_dividend_4_5m_state",
        "BIO dividend to Belgian State 4.5m 2025",
        4.5e6,
        4.5e6,
        "Strong: 2nd consecutive year dividend; dual nonfiscal State receipts",
        "strong",
        "Federal Treasury",
        "Return capital to sole shareholder",
        "Positive after prior thin years",
        2.5,
        3.0,
        2,
        2.9,
        "Keep transparent vs reinvestment tradeoff",
        f"tick{TICK}",
        "Federal>BIO>dividend",
    ),
    (
        "lb_bio_capital_subsidies_85m",
        "State capital subsidies extra 85m under BIO mgmt contract 2024-28",
        85e6,
        85e6,
        "Medium strategy doc: higher risk/impact capital subsidies; dual DGD code5 path FOI residual",
        "medium",
        "BIO higher-impact investments",
        "Fund riskier DFI tickets with State subsidy capital",
        "Not annual cash schedule public",
        4.5,
        5.5,
        6,
        5.1,
        "Publish cash-by-year capital grants; dual gap_bio",
        f"tick{TICK}",
        "Federal>BIO>capital_subsidies",
    ),
    (
        "lb_bio_ukraine_6m_usd",
        "BIO Ukraine Rebuilding Fund 6m USD 2025 (2nd Ukraine investment)",
        6e6,
        6e6,
        "Medium: USD face; FCAS milestone after Bank Lviv; dual FCAS strategy",
        "medium",
        "Ukraine reconstruction private sector",
        "Operate in fragile/conflict-affected states",
        "Named L5 public",
        3.5,
        3.5,
        5,
        3.6,
        "Track risk and additionality",
        f"tick{TICK}",
        "Federal>BIO>Ukraine",
    ),
]
for args in rows:
    if add_lb(*args):
        n_lb += 1

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

# research_queue
with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())
for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: BIO AR2025 named L5 (EUR sample Coris20 Kampani2 Orchidia10 + USD face) "
            f"approvals 235 signed 166 stock 1.2bn; gap_bio residual; rq_116 deferred"
        )
if not any(r.get("task_id") == "rq_434" for r in rq):
    rq.append(
        {
            "task_id": "rq_434",
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
            "notes": f"Spawned tick{TICK} after BIO named L5; rq_116 SWA deferred",
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
    f"Scheduler 60s. Next prio5 rq_434; rq_116 SWA deferred. "
    f"tick{TICK} BIO named L5 235m approvals + Kampani."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **BIO AR 2025 named investment L5 + dual Kampani**)
- Found (strong primary BIO Annual Report 2025 web):
  - **Approvals €235m / 30** projects (signed **€166m / 21**); committed stock **€1.2bn / 171**; signed stock **€1.033bn**
  - Financials: assets **€1.196bn** · income **55.3** · cost of risk **20.1** · FX **−5.9** · net **9.0** · dividend **4.5**
  - Africa **55%** approvals · gender **57%** of 2024-25 · direct enterprise **11** (vs 2) · jobs direct **~388k** EOY2024
  - **Named EUR L5:** Coris **20** · Orchidia **10** · Glacier **8** · FoodsCo **3** · Vital **3** · Kampani **2** · Limbua **2** · FEFISOL **2** · ACEP **1.5** (sample sum **€{EUR_SUM/1e6:.1f}m**)
  - **Named USD face L5:** multiple **15m** lines (Adenia/Amartha/Atlántida/ADEMI/Bandwidth/Excelsior) · ECOM **10** · Helios **10** · Lendable **10** · Super Silica **3.7** · Ukraine fund **6** (no FX invent)
  - Dual: DGD AR **240m** approvals class; State capital subsidies extra **€85m** strategy 2024-28
- Wrote: sources +1; entity kampani; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; foi gap_bio note; rq_433=done; spawn **rq_434**; ticks={TICK}
- FOI: gap_bio_l5_portfolio residual narrowed (named sample public; full outstanding+impairments still ready)
- Next: prio5 **rq_434**; deferred **rq_116** SWA
"""
with open(Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md"), "ab") as f:
    f.write(log.encode("utf-8"))

print(f"OK tick{TICK} bud+{n_bud} cmt+{n_cmt} lb+{n_lb} eur_sum={EUR_SUM/1e6:.1f} usd_sum={USD_SUM/1e6:.1f}")

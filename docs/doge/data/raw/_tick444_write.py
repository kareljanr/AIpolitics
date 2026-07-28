# tick 444: BRS Microfinance Coop AR 2025 L5 + dissolution dual Alterfin/Incofin/Cera
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T12:45:00Z"
TICK = 444
UNIT = "rq_435"
SRC = "src_brs_ar_2025"
URL = "https://magazines.cera.coop/JaarverslagBRS/FR/2026/4/index.html"
URL_DISSOLVE = "https://www.brs.coop/en/news/2026/20260513_brs_microfinance_coop"

# BRS Microfinance Coop EOY2025
COOP = {
    "assets": 22000000,
    "assets_2024": 22200000,
    "equity": 21400000,
    "capital_total": 21240000,
    "capital_A": 3743500,  # 1420 members
    "capital_C": 17500000,
    "members_A": 1420,
    "avg_A": 2636,
    "share_cera_pct": 45.58,
    "share_kbc_pct": 17.62,
    "share_brs_asbl_pct": 1.5,
    "share_indiv_pct": 35.3,
    "loans_mfi": 2000000,
    "loans_amc_sv": 1400000,
    "loans_el_ejido_ec": 300000,
    "loans_ebo_ug": 300000,
    "funds_total": 9000000,
    "fund_incofin_mf": 1600000,
    "fund_alterfin": 1000000,
    "fund_ecf": 1000000,
    "fund_fefisol_ii": 1500000,
    "fund_incofin_climate": 1000000,
    "fund_triodos": 3000000,
    "cash_deposits": 10800000,
    "profit": 219297,
    "profit_2024": 559063,
    "dividend_total": 533512,
    "dividend_rate": 0.025,
    "provision_dissolve": 50000,
    "triodos_impairment": 54054,
    "repaid_loans_2025": 500000,
    "debt_dividends": 533512,
    "fx_hedge_notional": 2000000,
    "borrowers_reach": 44000,
    "borrowers_via_loans": 1110,
    "mfi_portfolio_usd": 94500000,
    "dissolve_date": "2026-06-30",
    "repay_week": "2026-07-W1",
}

# BRS ASBL 2025
ASBL = {
    "assets": 2414181,
    "assets_2024": 2505229,
    "equity": 2397886,
    "fonds_assoc": 700000,
    "reserves": 500000,
    "result_carried": 1197886,
    "loss": 84837,
    "loss_2024": 84732,
    "income_ops": 503385,
    "donations": 389599,
    "tombola_cera": 108531,
    "training_income": 4755,
    "services_goods": 609254,
    "projects_services": 403154,
    "consultance": 102029,
    "formation": 47767,
    "communication": 39904,
    "functioning": 16401,
    "fin_income": 30963,
    "gross_margin": -105869,
    "project_intl": 293797,
    "coaching_formation_pack": 246217,
    "projects_n": 14,
    "countries_n": 7,
    "coaching_days": 594,
    "microfact_days": 108,
    "volunteers_kbc": 94,  # press 94; AR narrative 96
    "reach_farmers_class": 1000000,
    "hold_alterfin": 2500,
    "hold_incofin": 2604,
    "hold_brs_mfc": 318000,
    "commitments_open": 455000,
}

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "BRS ASBL + BRS Microfinance Coop Annual Report 2025 + dissolution press",
            "url": URL,
            "publisher": "BRS / Cera",
            "accessed_date": "2026-08-02",
            "source_class": "official_annual_report",
            "notes": (
                f"MFC assets 22m equity 21.4m loans 2m funds 9m; dissolve 2026-06-30 to Alterfin/Incofin via Cera; "
                f"ASBL assets 2.41m loss 85k; dual KBC volunteers; tick{TICK}"
            ),
        }
    )
if not any(r["source_id"] == "src_brs_dissolve_2026" for r in src):
    src.append(
        {
            "source_id": "src_brs_dissolve_2026",
            "title": "BRS Microfinance Coop voluntary dissolution 13 May 2026 press",
            "url": URL_DISSOLVE,
            "publisher": "BRS / Cera",
            "accessed_date": "2026-08-02",
            "source_class": "official_press",
            "notes": f"EGM dissolve midnight 30 Jun 2026; 1420 members full repay Jul; dividend 2.5% 2025; tick{TICK}",
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "entities.csv", encoding="utf-8", newline="") as f:
    ent = list(csv.DictReader(f))
    ef = list(ent[0].keys())
for eid, nl, fr, en, notes in [
    (
        "brs_asbl",
        "BRS vzw",
        "BRS ASBL",
        "Belgian Raiffeisen Foundation ASBL coaching microfinance",
        "Cera+KBC joint venture coaching; dual Microfinance Coop dissolved 2026; tick444",
    ),
    (
        "brs_mfc",
        "BRS Microfinance Coop",
        "BRS Microfinance Coop",
        "BRS Microfinance cooperative investment vehicle (dissolved 2026)",
        "Dissolve 2026-06-30; capital to Cera stakes Alterfin+Incofin; tick444",
    ),
    (
        "incofin_mf_fund",
        "Incofin Microfinance Fund",
        "Incofin Microfinance Fund",
        "Incofin Microfinance Fund Belgian cooperative",
        "Receives Cera increased stake post BRS MFC dissolve; dual Alterfin; tick444",
    ),
]:
    if not any(r.get("entity_id") == eid for r in ent):
        row = {k: "" for k in ef}
        row.update(
            {
                "entity_id": eid,
                "name_nl": nl,
                "name_fr": fr,
                "name_en": en,
                "level": "asbl",
                "parent_id": "sec_federal",
                "community_language": "bi",
                "website": "https://www.brs.coop" if "brs" in eid else "https://incofin.com",
                "notes": notes,
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
            "source_id": SRC,
            "confidence": conf,
            "notes": notes,
        }
    )
    return True


n_bud = 0

# Coop aggregates
coop_rows = [
    ("bud_brs_mfc_assets_2025", "brs_mfc", COOP["assets"], "stock", f"BRS MFC total assets {COOP['assets']/1e6:.1f}m EOY2025 (vs {COOP['assets_2024']/1e6:.1f}m); dissolve 2026-06-30; tick{TICK}"),
    ("bud_brs_mfc_equity_2025", "brs_mfc", COOP["equity"], "stock", f"BRS MFC equity {COOP['equity']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_capital_2025", "brs_mfc", COOP["capital_total"], "stock", f"BRS MFC capital contributions {COOP['capital_total']/1e6:.2f}m ({COOP['members_A']} A-members {COOP['capital_A']/1e6:.2f}m + C {COOP['capital_C']/1e6:.1f}m); tick{TICK}"),
    ("bud_brs_mfc_capital_A_2025", "brs_mfc", COOP["capital_A"], "stock", f"Individual A-shares {COOP['capital_A']/1e6:.3f}m / {COOP['members_A']} members avg {COOP['avg_A']}; tick{TICK}"),
    ("bud_brs_mfc_loans_2025", "brs_mfc", COOP["loans_mfi"], "stock", f"Direct MFI loans outstanding {COOP['loans_mfi']/1e6:.1f}m (AMC-SV 1.4 + El Ejido 0.3 + EBO-UG 0.3); tick{TICK}"),
    ("bud_brs_mfc_loan_amc_2025", "brs_mfc", COOP["loans_amc_sv"], "stock", f"Loan AMC El Salvador {COOP['loans_amc_sv']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_loan_ejido_2025", "brs_mfc", COOP["loans_el_ejido_ec"], "stock", f"Loan Union El Ejido Ecuador {COOP['loans_el_ejido_ec']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_loan_ebo_2025", "brs_mfc", COOP["loans_ebo_ug"], "stock", f"Loan EBO Sacco Uganda {COOP['loans_ebo_ug']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_funds_2025", "brs_mfc", COOP["funds_total"], "stock", f"Specialised MF fund holdings {COOP['funds_total']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_fund_incofin_2025", "brs_mfc", COOP["fund_incofin_mf"], "stock", f"Incofin Microfinance Fund stake {COOP['fund_incofin_mf']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_fund_alterfin_2025", "brs_mfc", COOP["fund_alterfin"], "stock", f"Alterfin stake {COOP['fund_alterfin']/1e6:.1f}m dual; tick{TICK}"),
    ("bud_brs_mfc_fund_fefisol_2025", "brs_mfc", COOP["fund_fefisol_ii"], "stock", f"Fefisol II stake {COOP['fund_fefisol_ii']/1e6:.1f}m dual Alterfin; tick{TICK}"),
    ("bud_brs_mfc_fund_triodos_2025", "brs_mfc", COOP["fund_triodos"], "stock", f"Triodos Microfinance Fund {COOP['fund_triodos']/1e6:.1f}m (impairment {COOP['triodos_impairment']}); tick{TICK}"),
    ("bud_brs_mfc_fund_ecf_2025", "brs_mfc", COOP["fund_ecf"], "stock", f"Emerging Credit Fund {COOP['fund_ecf']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_fund_incofin_climate_2025", "brs_mfc", COOP["fund_incofin_climate"], "stock", f"Incofin Climate Smart MF Fund {COOP['fund_incofin_climate']/1e6:.1f}m; tick{TICK}"),
    ("bud_brs_mfc_cash_2025", "brs_mfc", COOP["cash_deposits"], "stock", f"Cash+term deposits {COOP['cash_deposits']/1e6:.1f}m almost all EUR; tick{TICK}"),
    ("bud_brs_mfc_profit_2025", "brs_mfc", COOP["profit"], "outturn", f"Profit {COOP['profit']} (vs {COOP['profit_2024']} 2024); tick{TICK}"),
    ("bud_brs_mfc_dividend_2025", "brs_mfc", COOP["dividend_total"], "budgeted", f"Dividend 2.5pct = {COOP['dividend_total']} of capital; tick{TICK}"),
    ("bud_brs_mfc_provision_dissolve", "brs_mfc", COOP["provision_dissolve"], "budgeted", f"Dissolution provision {COOP['provision_dissolve']} EOY2025; tick{TICK}"),
    ("bud_brs_mfc_members_A_2025", "brs_mfc", COOP["members_A"], "estimate", f"Individual A-members headcount {COOP['members_A']} (not EUR); full repay Jul 2026; tick{TICK}"),
]
for bid, ent, amt, basis, notes in coop_rows:
    if add_bud(bid, ent, 2025, amt, basis, notes, "strong"):
        n_bud += 1

# ASBL
asbl_rows = [
    ("bud_brs_asbl_assets_2025", ASBL["assets"], "stock", f"BRS ASBL assets {ASBL['assets']/1e6:.3f}m EOY2025; tick{TICK}"),
    ("bud_brs_asbl_equity_2025", ASBL["equity"], "stock", f"BRS ASBL equity/fonds {ASBL['equity']/1e6:.3f}m; tick{TICK}"),
    ("bud_brs_asbl_loss_2025", ASBL["loss"], "outturn", f"BRS ASBL loss {ASBL['loss']} (similar {ASBL['loss_2024']} 2024); going concern via carried profit {ASBL['result_carried']/1e6:.2f}m; tick{TICK}"),
    ("bud_brs_asbl_income_2025", ASBL["income_ops"], "outturn", f"Operating income {ASBL['income_ops']} (donations {ASBL['donations']} + tombola Cera {ASBL['tombola_cera']}); tick{TICK}"),
    ("bud_brs_asbl_donations_2025", ASBL["donations"], "outturn", f"Donations {ASBL['donations']}; tick{TICK}"),
    ("bud_brs_asbl_projects_cost_2025", ASBL["projects_services"], "outturn", f"Projects+financial services cost {ASBL['projects_services']}; tick{TICK}"),
    ("bud_brs_asbl_project_intl_2025", ASBL["project_intl"], "outturn", f"International project financing {ASBL['project_intl']}; tick{TICK}"),
    ("bud_brs_asbl_coaching_pack_2025", ASBL["coaching_formation_pack"], "outturn", f"Coaching+training pack {ASBL['coaching_formation_pack']} incl Microfact; tick{TICK}"),
    ("bud_brs_asbl_consultance_2025", ASBL["consultance"], "outturn", f"Consultance cost line {ASBL['consultance']}; tick{TICK}"),
    ("bud_brs_asbl_hold_mfc_2025", ASBL["hold_brs_mfc"], "stock", f"BRS ASBL book value BRS MFC shares {ASBL['hold_brs_mfc']}; tick{TICK}"),
    ("bud_brs_asbl_commitments_2025", ASBL["commitments_open"], "estimate", f"Open project commitments off-balance {ASBL['commitments_open']}; tick{TICK}"),
    ("bud_brs_asbl_coaching_days_2025", ASBL["coaching_days"], "estimate", f"Coaching+training days {ASBL['coaching_days']} (headcount-days not EUR); tick{TICK}"),
    ("bud_brs_asbl_volunteers_2025", ASBL["volunteers_kbc"], "estimate", f"KBC/CBC/Cera volunteer experts ~{ASBL['volunteers_kbc']} (press 94 / AR ~96); tick{TICK}"),
]
for bid, amt, basis, notes in asbl_rows:
    if add_bud(bid, "brs_asbl", 2025, amt, basis, notes, "strong"):
        n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())

n_cmt = 0
if not any(r.get("commitment_id") == "cmt_brs_mfc_dissolve_2026" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_brs_mfc_dissolve_2026",
            "title": "BRS Microfinance Coop voluntary dissolution 2026 + Cera pivot to Alterfin/Incofin",
            "entity_id": "brs_mfc",
            "beneficiary": "1420 co-op members (full repay) / Cera stakes Alterfin+Incofin",
            "legal_basis": "EGM May 2026 voluntary dissolve; Belgian CSA cooperative; dissolve midnight 30 Jun 2026",
            "decision_date": "2026-05-13",
            "start_year": "2015",
            "end_year": "2026",
            "total_envelope_eur": str(COOP["capital_total"]),
            "cash_by_year": json.dumps(
                {
                    "2025_assets": COOP["assets"],
                    "2025_capital": COOP["capital_total"],
                    "2025_loans": COOP["loans_mfi"],
                    "2025_funds": COOP["funds_total"],
                    "fund_split": {
                        "incofin_mf": COOP["fund_incofin_mf"],
                        "alterfin": COOP["fund_alterfin"],
                        "fefisol_ii": COOP["fund_fefisol_ii"],
                        "triodos": COOP["fund_triodos"],
                        "ecf": COOP["fund_ecf"],
                        "incofin_climate": COOP["fund_incofin_climate"],
                    },
                    "dividend_2025": COOP["dividend_total"],
                    "dissolve": COOP["dissolve_date"],
                    "repay": COOP["repay_week"],
                    "ownership_pct": {
                        "cera": COOP["share_cera_pct"],
                        "kbc": COOP["share_kbc_pct"],
                        "brs_asbl": COOP["share_brs_asbl_pct"],
                        "individuals": COOP["share_indiv_pct"],
                    },
                    "note": "Post-dissolve Cera invests MF via increased Alterfin+Incofin stakes; BRS ASBL coaching continues",
                }
            ),
            "remaining_eur": "",
            "status": "cancelled",
            "evaluation_url": URL_DISSOLVE,
            "stated_goal": "Simplify Belgian microfinance co-op stack; raise impact via specialised partners",
            "cut_option": "Not public budget; private co-op consolidation; dual tax-break end Alterfin",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "BE>Cera_BRS>Microfinance_Coop",
            "notes": f"AR2025 + press dissolve; dual Alterfin tick443; tick{TICK}",
        }
    )
    n_cmt += 1

if not any(r.get("commitment_id") == "cmt_brs_asbl_2025" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_brs_asbl_2025",
            "title": "BRS ASBL coaching microfinance 2025 package",
            "entity_id": "brs_asbl",
            "beneficiary": "14 partner MFIs rural South + Belgian awareness",
            "legal_basis": "ASBL; Cera+KBC partnership",
            "decision_date": "2025-01-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(ASBL["income_ops"]),
            "cash_by_year": json.dumps(
                {
                    "income": ASBL["income_ops"],
                    "donations": ASBL["donations"],
                    "tombola_cera": ASBL["tombola_cera"],
                    "projects_cost": ASBL["projects_services"],
                    "project_intl": ASBL["project_intl"],
                    "coaching_days": ASBL["coaching_days"],
                    "volunteers": ASBL["volunteers_kbc"],
                    "partners": ASBL["projects_n"],
                    "loss": ASBL["loss"],
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Capacity building rural MFIs dual KBC volunteers",
            "cut_option": "Private ASBL; track Cera tombola+donations sustainability",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "BE>Cera_BRS>ASBL",
            "notes": f"AR2025; continues after MFC dissolve; tick{TICK}",
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
        "lb_brs_mfc_22m_dissolve",
        "BRS Microfinance Coop 22m assets dissolve Jun 2026 to Alterfin/Incofin via Cera",
        22e6,
        22e6,
        "Strong AR+press: equity 21.4m capital 21.2m; loans 2m + funds 9m + cash 10.8m; full member repay; dual Alterfin",
        "strong",
        "1420 co-op members / Cera",
        "Simplify Belgian MF co-op stack",
        "Not pure waste; consolidation of dual private impact vehicles",
        3.5,
        5.0,
        4,
        4.4,
        "Track Cera post-dissolve stakes public",
        f"tick{TICK}",
        "BE>BRS>MFC_dissolve",
    ),
    (
        "lb_brs_mfc_funds_9m",
        "BRS MFC specialised MF fund holdings 9m (Alterfin/Incofin/Triodos/Fefisol)",
        9e6,
        9e6,
        "Strong L5: Incofin 1.6 + Alterfin 1 + Fefisol 1.5 + Triodos 3 + ECF 1 + Incofin Climate 1",
        "strong",
        "MF funds dual Belgian stack",
        "Indirect microfinance exposure",
        "Named fund L5 public",
        3.0,
        4.0,
        3,
        3.6,
        "Publish fund NAV L5 after liquidate",
        f"tick{TICK}",
        "BE>BRS>fund_holdings",
    ),
    (
        "lb_brs_mfc_loans_2m",
        "BRS MFC direct MFI loans 2m (3 partners SV/EC/UG)",
        2e6,
        2e6,
        "Strong: AMC 1.4 + El Ejido 0.3 + EBO 0.3; also BRS ASBL coaching partners",
        "strong",
        "~1110 borrowers class via 3 MFIs",
        "Direct rural MFI lending",
        "Portfolio shrinking into dissolve",
        2.5,
        3.5,
        3,
        3.2,
        "Monitor repay path 1.5m maturing 2026",
        f"tick{TICK}",
        "BE>BRS>direct_loans",
    ),
    (
        "lb_brs_asbl_coaching_2025",
        "BRS ASBL 594 coaching days / 0.50m income / 14 partners 2025",
        503385,
        503385,
        "Strong: donations 0.39m + Cera tombola 0.11m; project costs 0.40m; loss 85k; KBC volunteers ~94",
        "strong",
        "14 partner MFIs rural South",
        "Capacity building dual KBC expertise",
        "Continues after MFC dissolve",
        2.0,
        3.0,
        3,
        2.8,
        "Core non-financial dual model",
        f"tick{TICK}",
        "BE>BRS>ASBL_coaching",
    ),
    (
        "lb_brs_cera_kbc_dual_stack",
        "Belgian private MF stack Cera-BRS-KBC-Alterfin-Incofin-BIO",
        22e6,
        22e6 + 122e6 + 1196e6,
        "Medium dual map: MFC 22m + Alterfin 122m + BIO 1.2bn; not additive TE; KBC volunteer channel unique",
        "medium",
        "Rural Global South + Belgian co-op members",
        "Private cooperative development finance ecosystem",
        "Structural dual with public DGD/Enabel",
        3.5,
        5.5,
        5,
        4.7,
        "Publish consolidated private MF capital map BE",
        f"tick{TICK}",
        "BE>dual>microfinance_coop_stack",
    ),
    (
        "lb_brs_mfc_dividend_2_5pct",
        "BRS MFC dividend 2.5pct / 0.53m 2025 final year",
        533512,
        533512,
        "Strong AR: profit 0.22m + reserve draw 0.31m to pay 2.5pct; dual Alterfin 1pct",
        "strong",
        "Co-op members A+C",
        "Member return on solidarity capital",
        "Final year before dissolve repay",
        2.5,
        2.5,
        2,
        2.6,
        "Not waste; transparency of dissolve economics",
        f"tick{TICK}",
        "BE>BRS>dividend",
    ),
    (
        "lb_brs_asbl_donations_0_39m",
        "BRS ASBL donations 0.39m + Cera tombola 0.11m 2025",
        389599 + 108531,
        389599 + 108531,
        "Strong: main ASBL funding; fiscal attestation >=40 EUR gifts",
        "strong",
        "BRS coaching operations",
        "Private fundraising for capacity building",
        "Sustains after MFC exit",
        2.0,
        3.5,
        3,
        3.1,
        "Track tombola dependency",
        f"tick{TICK}",
        "BE>BRS>fundraising",
    ),
    (
        "lb_brs_mfc_ownership_cera_46pct",
        "Cera 45.6pct of BRS MFC capital (KBC 17.6pct individuals 35.3pct)",
        COOP["capital_total"] * 0.4558,
        COOP["capital_total"] * 0.4558,
        "Strong AR ownership pie; Cera leads post-dissolve Alterfin/Incofin path",
        "strong",
        "Cera cooperative / KBC",
        "Institutional control of MF co-op vehicle",
        "Private not public budget",
        3.0,
        4.5,
        3,
        3.9,
        "Map Cera KBC dual financial group stakes",
        f"tick{TICK}",
        "BE>Cera>BRS_MFC",
    ),
    (
        "lb_brs_dissolve_provision_50k",
        "BRS MFC dissolution provision 50k EOY2025",
        50000,
        50000,
        "Strong: accounts on discontinuity basis; extra liquidate costs",
        "strong",
        "Liquidation process",
        "Cover dissolve costs",
        "Tiny vs 22m assets",
        2.0,
        1.5,
        2,
        1.9,
        "Routine dissolve accounting",
        f"tick{TICK}",
        "BE>BRS>dissolve_cost",
    ),
    (
        "lb_brs_kbc_volunteers_94",
        "BRS KBC volunteer experts ~94 / 594 coaching days 2025",
        94,
        594,
        "Strong: unique BE model bank staff pro-bono dual Cera; amount_eur=headcount not cash wage",
        "strong",
        "14 partner MFIs",
        "Knowledge transfer rural MFIs",
        "Non-cash public-interest private channel",
        2.0,
        2.0,
        3,
        2.3,
        "Value-in-kind residual optional",
        f"tick{TICK}",
        "BE>BRS>volunteers",
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
            f"tick{TICK}: BRS MFC 22m dissolve 2026-06-30 (loans 2 funds 9) + ASBL coaching 0.5m/594d; "
            f"dual Cera→Alterfin/Incofin; rq_116 deferred"
        )
if not any(r.get("task_id") == "rq_436" for r in rq):
    rq.append(
        {
            "task_id": "rq_436",
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
            "notes": f"Spawned tick{TICK} after BRS MFC dissolve dual; rq_116 SWA deferred",
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
    f"Scheduler 60s. Next prio5 rq_436; rq_116 SWA deferred. "
    f"tick{TICK} BRS MFC 22m dissolve dual Alterfin/Incofin."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **BRS Microfinance Coop dissolve + ASBL coaching dual Alterfin/Incofin**)
- Found (strong primary BRS AR 2025 magazine + dissolve press 13 May 2026):
  - **BRS MFC EOY2025:** assets **€22.0m** · equity **€21.4m** · capital **€21.24m** (**1,420** A-members **€3.74m** + C **€17.5m**)
  - Ownership: Cera **45.6%** · individuals **35.3%** · KBC **17.6%** · BRS ASBL **1.5%**
  - Loans **€2.0m** (AMC-SV **1.4** · El Ejido **0.3** · EBO-UG **0.3**) · MF funds **€9.0m** (Triodos **3** · Incofin **1.6** · Fefisol **1.5** · Alterfin **1** · ECF **1** · Incofin Climate **1**) · cash **€10.8m**
  - Profit **€219k** · dividend **2.5% / €534k** · dissolve provision **€50k**
  - **Dissolve:** midnight **2026-06-30**; full A-share repay early Jul; Cera continues MF via **increased Alterfin + Incofin** stakes
  - **BRS ASBL:** assets **€2.41m** · loss **€85k** · income **€503k** (donations **€390k** + Cera tombola **€109k**) · projects **€403k** · **594** coaching days · **~94** KBC volunteers · **14** partners / **7** countries
- Wrote: sources +2; entities +3; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_435=done; spawn **rq_436**; ticks={TICK}
- FOI: none new (private co-op dissolve; dual stack now mapped public)
- Next: prio5 **rq_436**; deferred **rq_116** SWA
"""
with open(Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md"), "ab") as f:
    f.write(log.encode("utf-8"))

print(f"OK tick{TICK} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")

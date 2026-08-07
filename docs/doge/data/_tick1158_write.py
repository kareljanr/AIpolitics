# -*- coding: utf-8 -*-
"""Tick 1158: AGB Patrimonium Lommel JR2025 Entity II dual residual (NEG equity / gecorr AFM)."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
UTC = "2026-08-07T20:30:00Z"
TICK = 1158
SRC = "src_agb_lommel_patrimonium_jr2025"
ENT = "agb_lommel_patrimonium"
CITY = "city_lommel"
SRC_URL = "https://www.lommel.be/jaarrekening-2025-agb-patrimonium"
GAP = "gap_agb_lommel_pat_equity_neg_gecorr_afm_deep_neg_fva_l5"


def load(path):
    for e in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            with open(path, encoding=e, newline="") as f:
                r = csv.DictReader(f)
                return r.fieldnames, list(r), e
        except UnicodeDecodeError:
            continue
    raise RuntimeError(path)


def save(path, fieldnames, rows, enc="utf-8"):
    with open(path, "w", encoding=enc, newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


sf, srcs, senc = load(DATA / "sources.csv")
if not any(s.get("source_id") == SRC for s in srcs):
    srcs.append(
        {
            "source_id": SRC,
            "title": "AGB Patrimonium Lommel BBC Jaarrekening 2025 (primary)",
            "url": SRC_URL,
            "publisher": "AGB Patrimonium Lommel / Stad Lommel",
            "accessed_date": "2026-08-07",
            "source_class": "primary_pdf",
            "notes": (
                "tick1158; Entity II dual residual patrimonium/FVA shell; KBO 0882.833.820; "
                "Hertog Janplein 1 3920; AD Ronny Vanhoof FD Carine Joos; Voorzitter Bob Nijs "
                "Secretaris Iris Mulkens; 42p bekendmaking 20.05.2026; assets 6.055m equity "
                "NEG -0.342m CRITICAL FVA other 5.990m fin debt T4 5.880m (LT 5.874 ST due "
                "0.006) total schulden 6.397m cash 0.064m BBR 0.049m AFM +0.005m gecorr AFM "
                "-0.460m DEEP NEG budget +0.005m PnL +0.011m city subsidy 0.020m interest 0.001m"
            ),
        }
    )
    save(DATA / "sources.csv", sf, srcs, senc)
    print("sources +1")

ef, ents, eenc = load(DATA / "entities.csv")
ek = ef[0]
found = False
for e in ents:
    eid = e.get(ek) or e.get("entity_id") or ""
    if eid == ENT:
        found = True
        e["notes"] = (
            "JR2025 Entity II dual residual tick1158; KBO 0882.833.820; assets 6.055m "
            f"equity NEG -0.342m fin debt 5.880m gecorr AFM -0.460m DEEP NEG; FOI {GAP}"
        )
        e["website"] = e.get("website") or "https://www.lommel.be"
        e["foi_email"] = e.get("foi_email") or "info@lommel.be"
        e["foi_postal"] = e.get("foi_postal") or "Hertog Janplein 1 3920 Lommel"
    if eid == CITY:
        n = e.get("notes") or ""
        if "tick1158" not in n:
            e["notes"] = (
                n + " | tick1158 AGB Patrimonium Entity II dual residual mined "
                "(equity NEG / gecorr AFM DEEP NEG)"
            )
if not found:
    ents.append(
        {
            ek: ENT,
            "name_nl": "AGB Patrimonium Lommel",
            "name_fr": "AGB Patrimoine Lommel",
            "name_en": "AGB Patrimonium Lommel",
            "level": "local_entity",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.lommel.be",
            "foi_email": "info@lommel.be",
            "foi_postal": "Hertog Janplein 1 3920 Lommel",
            "notes": f"JR2025 Entity II dual residual tick1158; KBO 0882.833.820; FOI {GAP}",
        }
    )
save(DATA / "entities.csv", ef, ents, eenc)
print("entities ok")

bf, buds, benc = load(DATA / "budgets.csv")
ex = {b.get("budget_id") for b in buds}
rows = [
    ("bud_agblommelp_assets_2025", 6054824, "Assets balanstotaal YE2025 6.055m"),
    ("bud_agblommelp_equity_2025", -341926, "Nettoactief YE2025 NEG -0.342m CRITICAL"),
    ("bud_agblommelp_cum_pnl_neg_2025", -341926, "Gecumuleerd tekort equity path YE2025 -0.342m"),
    ("bud_agblommelp_debt_total_2025", 6396749, "Schulden total YE2025 6.397m"),
    ("bud_agblommelp_fin_debt_2025", 5879864, "Fin schulden T4 total YE2025 5.880m (LT 5.874 + ST due 0.006)"),
    ("bud_agblommelp_fin_debt_lt_2025", 5873864, "Fin schulden LT YE2025 5.874m"),
    ("bud_agblommelp_fin_debt_st_due_2025", 6000, "Fin schulden LT binnen jaar YE2025 0.006m"),
    ("bud_agblommelp_lt_nonfin_ruil_2025", 500928, "LT niet-fin ruil schulden YE2025 0.501m FOI residual"),
    ("bud_agblommelp_cash_2025", 64034, "Liquide middelen YE2025 0.064m"),
    ("bud_agblommelp_fva_other_2025", 5990000, "Andere FVA YE2025 5.990m FOI residual CRITICAL shell"),
    ("bud_agblommelp_expl_ont_2025", 20000, "Exploitatieontvangsten 0.020m city subsidy 2025"),
    ("bud_agblommelp_expl_uit_2025", 9073, "Exploitatieuitgaven 0.009m 2025"),
    ("bud_agblommelp_expl_saldo_2025", 10927, "Exploitatiesaldo +0.011m 2025"),
    ("bud_agblommelp_invest_saldo_2025", 0, "Investeringssaldo 0 2025"),
    ("bud_agblommelp_fin_saldo_2025", -6000, "Financieringssaldo -0.006m 2025"),
    ("bud_agblommelp_loan_repay_2025", 6000, "Periodieke aflossingen 0.006m 2025"),
    ("bud_agblommelp_budget_2025", 4927, "Budgettair resultaat +0.005m 2025"),
    ("bud_agblommelp_cum_budget_2025", 48867, "Gecumuleerd budgettair YE2025 0.049m"),
    ("bud_agblommelp_bbr_2025", 48867, "Beschikbaar budgettair resultaat 0.049m thin"),
    ("bud_agblommelp_afm_2025", 4927, "Autofinancieringsmarge +0.005m 2025"),
    ("bud_agblommelp_afm_gecorr_2025", -459942, "Gecorrigeerde AFM -0.460m DEEP NEG CRITICAL"),
    ("bud_agblommelp_pnl_2025", 10927, "PnL overschot +0.011m 2025"),
    ("bud_agblommelp_interest_2025", 1470, "Financiele kosten/rente 0.001m 2025"),
    ("bud_agblommelp_city_subsidy_2025", 20000, "Algemene werkingssubsidie stad 0.020m 2025"),
]
add = 0
for bid, amt, note in rows:
    if bid in ex:
        continue
    buds.append(
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": "2025",
            "amount_eur": str(int(amt)),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "BBC JR2025 primary",
            "source_id": SRC,
            "confidence": "strong",
            "notes": f"{note}; tick{TICK}",
        }
    )
    add += 1
save(DATA / "budgets.csv", bf, buds, benc)
print(f"budgets +{add}")

cf, comms, cenc = load(DATA / "commitments.csv")
cex = {c.get("commitment_id") for c in comms}
crows = [
    (
        "comm_agblommelp_equity_neg_2025",
        "AGB Lommel Pat equity NEG -0.342m CRITICAL",
        "341926",
        "active",
        "Negative equity shell after FVA/debt stack",
        "Equity FOI residual CRITICAL",
    ),
    (
        "comm_agblommelp_gecorr_afm_deep_neg_2025",
        "AGB Lommel Pat gecorr AFM -0.460m DEEP NEG",
        "459942",
        "active",
        "Gecorr AFM deep NEG debt 5.88m vs amort 6k",
        "AFM FOI residual CRITICAL",
    ),
    (
        "comm_agblommelp_fva_other_5_99m_2025",
        "AGB Lommel Pat FVA other 5.990m FOI",
        "5990000",
        "stock",
        "Opaque andere FVA holdings shell",
        "FVA FOI residual CRITICAL",
    ),
    (
        "comm_agblommelp_fin_debt_5_88m_2025",
        "AGB Lommel Pat fin debt 5.880m",
        "5879864",
        "stock",
        "Debt stock amort only 6k/yr wall",
        "Debt FOI residual",
    ),
    (
        "comm_agblommelp_lt_nonfin_0_50m_2025",
        "AGB Lommel Pat LT non-fin ruil 0.501m",
        "500928",
        "stock",
        "LT non-financial exchange liabilities FOI",
        "FOI residual",
    ),
    (
        "comm_agblommelp_city_subsidy_20k_2025",
        "AGB Lommel Pat city subsidy 0.020m/yr",
        "20000",
        "active",
        "Structural city operating grant",
        "Monitor residual subsidy",
    ),
]
for cid, title, env, status, goal, cut in crows:
    if cid in cex:
        continue
    comms.append(
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AGB dual residual",
            "legal_basis": "BBC JR2025",
            "decision_date": "2026-05-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": f"{{2025:{env}}}",
            "remaining_eur": "0",
            "status": status,
            "evaluation_url": SRC_URL,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>AGB_Patrimonium",
            "notes": f"tick{TICK}",
        }
    )
save(DATA / "commitments.csv", cf, comms, cenc)
print("comms ok")

lf, lbs, lenc = load(DATA / "leaderboard.csv")
lex = {x.get("item_id") for x in lbs}
lrows = [
    (
        "lb_agblommelp_equity_neg_0_34m_2025",
        "AGB Lommel Pat equity NEG -0.34m CRITICAL",
        "341926",
        "9.0",
        "Equity FOI residual CRITICAL",
    ),
    (
        "lb_agblommelp_gecorr_afm_deep_neg_0_46m_2025",
        "AGB Lommel Pat gecorr AFM -0.46m DEEP NEG",
        "459942",
        "9.0",
        "AFM FOI residual CRITICAL",
    ),
    (
        "lb_agblommelp_fva_other_5_99m_2025",
        "AGB Lommel Pat FVA other 5.99m FOI shell",
        "5990000",
        "8.5",
        "FVA FOI residual CRITICAL",
    ),
    (
        "lb_agblommelp_fin_debt_5_88m_2025",
        "AGB Lommel Pat fin debt 5.88m amort 6k",
        "5879864",
        "8.0",
        "Debt FOI residual",
    ),
    (
        "lb_agblommelp_assets_6_05m_2025",
        "AGB Lommel Pat assets 6.05m Entity II",
        "6054824",
        "6.0",
        "Map residual shell",
    ),
    (
        "lb_agblommelp_lt_nonfin_0_50m_2025",
        "AGB Lommel Pat LT non-fin 0.50m FOI",
        "500928",
        "6.5",
        "FOI residual",
    ),
    (
        "lb_agblommelp_city_subsidy_20k_2025",
        "AGB Lommel Pat city subsidy 20k/yr",
        "20000",
        "4.0",
        "Monitor residual subsidy",
    ),
]
for iid, name, cost, absurd, cut in lrows:
    if iid in lex:
        continue
    c = abs(int(cost))
    cs = "7.0" if c > 5_000_000 else ("5.5" if c > 500_000 else "3.5")
    pi = round((float(absurd) + float(cs)) / 2.5, 1)
    lbs.append(
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": "Vlaanderen>Gemeenten>Lommel>AGB_Patrimonium_L5",
            "annual_cost_eur": str(abs(int(cost))),
            "total_cost_eur": str(abs(int(cost))),
            "tco_notes": (
                "JR2025 Entity II dual residual VL strong primary BBC NEG equity / "
                "gecorr AFM DEEP NEG patrimonium FVA shell"
            ),
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Lommel residents",
            "stated_goal": "Local dual residual map VL JR2025 AGB Patrimonium Lommel",
            "measured_outcome": "BBC J2/J4/J5 primary",
            "absurdity_score": absurd,
            "cost_score": cs,
            "difficulty": "3.0",
            "priority_index": str(pi),
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}",
        }
    )
save(DATA / "leaderboard.csv", lf, lbs, lenc)
print("lb ok")

ff, fois, fenc = load(DATA / "foi_queue.csv")
if not any(g.get("gap_id") == GAP for g in fois):
    fois.append(
        {
            "gap_id": GAP,
            "hierarchy_path": (
                "Vlaanderen>Gemeenten>Lommel>AGB_Patrimonium>"
                "equity_neg_gecorr_afm_fva_L5"
            ),
            "entity_id": ENT,
            "what_is_missing": (
                "Composition of andere FVA 5.990m (holdings counterparties valuation); "
                "loan schedule remaining fin debt 5.880m (amort only 6k/yr interest 1.47k "
                "lender/covenant); LT non-fin ruil debt 0.501m nature; negative equity "
                "-0.342m recovery/city support plan; gecorr AFM -0.460m path; city subsidy "
                "0.020m multi-year decision"
            ),
            "why_it_matters": (
                "Entity II dual residual: patrimonium shell with 5.99m opaque FVA stacked "
                "against 5.88m debt and NEG equity; thin BBR/AFM masking deep NEG gecorr AFM"
            ),
            "priority": "9",
            "recipient_body": "Stad / AGB Patrimonium Lommel",
            "recipient_email": "info@lommel.be",
            "recipient_postal": "Hertog Janplein 1 3920 Lommel",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-07",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agblommelp_equity_neg_2025",
            "linked_leaderboard_id": "lb_agblommelp_equity_neg_0_34m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    )
    save(DATA / "foi_queue.csv", ff, fois, "utf-8")
    print("foi +1")

rf, rqs, renc = load(DATA / "research_queue.csv")
for row in rqs:
    if row.get("task_id") == "rq_1158":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["entity_id"] = ENT
        row["blocked_gap_id"] = GAP
        row["notes"] = (
            f"tick{TICK}: AGB Lommel Pat assets 6.05m equity NEG -0.34m FVA 5.99m "
            "fin debt 5.88m gecorr AFM -0.46m FOI; spawn rq_1159 residual dual L5"
        )
if not any(r.get("task_id") == "rq_1159" for r in rqs):
    rqs.append(
        {
            "task_id": "rq_1159",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "PROGRESS residual dual L5 (Oosterzele / Nijlen login / Bornem JR2024 / "
                "Schelle GE+OCMW / Lievegem / Roeselare / Wommelgem / AGB Stabroek / "
                "AGB Genk / AGB Veurne / other); skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned tick{TICK} after AGB Lommel Pat; continuous hole_fill",
        }
    )
save(DATA / "research_queue.csv", rf, rqs, renc)

lsf, lss, lsenc = load(DATA / "loop_state.csv")
for row in lss:
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = UTC
    row["last_unit_id"] = "rq_1158"
    row["ticks_completed"] = str(TICK)
    row["paused"] = "no"
    row["notes"] = (
        f"tick{TICK} AGB Lommel Pat equity NEG / gecorr AFM DEEP NEG dual residual; "
        "next rq_1159 residual dual L5; rq_116 deferred; continuous hole_fill"
    )
save(DATA / "loop_state.csv", lsf, lss, lsenc)
print("OK ticks=1158")

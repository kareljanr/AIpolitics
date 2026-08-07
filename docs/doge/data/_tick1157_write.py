# -*- coding: utf-8 -*-
"""Tick 1157: AGB Schoten JR2025 Entity II dual residual (sport AGB after city GE)."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
UTC = "2026-08-07T20:00:00Z"
TICK = 1157
SRC = "src_agb_schoten_jr2025"
ENT = "agb_schoten"
CITY = "city_schoten"
SRC_URL = (
    "https://www.schoten.be/sites/default/files/public/documenten/"
    "Reglementen/2025_jaarrekening_AGBS.pdf"
)
GAP = "gap_agb_schoten_nonruil_recv_2m_city_loan_debt_l5"


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
            "title": "AGB Schoten BBC Jaarrekening 2025 (primary)",
            "url": SRC_URL,
            "publisher": "AGB Schoten / Gemeente Schoten",
            "accessed_date": "2026-08-07",
            "source_class": "primary_pdf",
            "notes": (
                "tick1157; Entity II dual residual sport AGB (Vordensteyn/De Zeurt); "
                "KBO 0819.981.481; Verbertstraat 3 2900; Voorzitter Paul De Swaef "
                "Secretaris An Adriaenssens; NIS 11040; 77p afdruk 13.03.2026; "
                "assets 4.438m equity 3.710m fin debt T4 0.573m (LT 0.475 + ST due 0.098) "
                "total schulden 0.728m cash 0.089m BBR 2.133m AFM +0.120m budget +0.120m "
                "PnL +0.071m dividend city 0.065m; city-only loan no bank debt; "
                "ST non-ruil recv 2.061m FOI; kerncijfers MVA 2.192m mislabeled as invest uitg"
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
            "JR2025 Entity II dual residual tick1157; KBO 0819.981.481; assets 4.438m "
            f"fin debt 0.573m BBR 2.133m AFM +0.120m; FOI {GAP}"
        )
        e["website"] = e.get("website") or "https://www.schoten.be"
        e["foi_email"] = e.get("foi_email") or "info@schoten.be"
        e["foi_postal"] = e.get("foi_postal") or "Verbertstraat 3 2900 Schoten"
    if eid == CITY:
        n = e.get("notes") or ""
        if "tick1157" not in n:
            e["notes"] = n + " | tick1157 AGB Schoten Entity II dual residual mined (healthy BBR/AFM)"
if not found:
    ents.append(
        {
            ek: ENT,
            "name_nl": "AGB Schoten",
            "name_fr": "AGB Schoten",
            "name_en": "AGB Schoten",
            "level": "local_entity",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.schoten.be",
            "foi_email": "info@schoten.be",
            "foi_postal": "Verbertstraat 3 2900 Schoten",
            "notes": f"JR2025 Entity II dual residual tick1157; KBO 0819.981.481; FOI {GAP}",
        }
    )
save(DATA / "entities.csv", ef, ents, eenc)
print("entities ok")

bf, buds, benc = load(DATA / "budgets.csv")
ex = {b.get("budget_id") for b in buds}
rows = [
    ("bud_agbschoten_assets_2025", 4438056, "Assets balanstotaal YE2025 4.438m"),
    ("bud_agbschoten_equity_2025", 3710411, "Nettoactief YE2025 3.710m"),
    ("bud_agbschoten_cum_pnl_2025", 480425, "Gecumuleerd overschot equity path YE2025 0.480m"),
    ("bud_agbschoten_cap_subs_2025", 13869, "Kapitaalsubsidies YE2025 0.014m"),
    ("bud_agbschoten_debt_total_2025", 727645, "Schulden total YE2025 0.728m"),
    ("bud_agbschoten_fin_debt_2025", 573119, "Fin schulden T4 total YE2025 0.573m (LT 0.475 + ST due 0.098)"),
    ("bud_agbschoten_fin_debt_lt_2025", 475047, "Fin schulden LT YE2025 0.475m city loan"),
    ("bud_agbschoten_fin_debt_st_due_2025", 98072, "Fin schulden LT binnen jaar YE2025 0.098m"),
    ("bud_agbschoten_cash_2025", 89463, "Liquide middelen YE2025 0.089m"),
    ("bud_agbschoten_fva_2025", 1250, "Fin VA IGS YE2025 1.250"),
    ("bud_agbschoten_mva_2025", 2192069, "MVA bedrijfsmatig YE2025 2.192m (kerncijfers mislabeled as invest uitg)"),
    ("bud_agbschoten_st_nonruil_recv_2025", 2060662, "ST vorderingen niet-ruil YE2025 2.061m FOI residual"),
    ("bud_agbschoten_st_nonruil_debt_2025", 12792, "ST schulden niet-ruil YE2025 0.013m"),
    ("bud_agbschoten_expl_ont_2025", 518230, "Exploitatieontvangsten 0.518m 2025"),
    ("bud_agbschoten_expl_uit_2025", 266628, "Exploitatieuitgaven 0.267m 2025"),
    ("bud_agbschoten_expl_saldo_2025", 251602, "Exploitatiesaldo +0.252m 2025"),
    ("bud_agbschoten_invest_uit_2025", 58307, "Investeringsuitgaven 0.058m 2025 (J2 not kerncijfers MVA stock)"),
    ("bud_agbschoten_invest_saldo_2025", -58307, "Investeringssaldo -0.058m 2025"),
    ("bud_agbschoten_fin_saldo_2025", -73694, "Financieringssaldo -0.074m 2025"),
    ("bud_agbschoten_new_loans_2025", 58307, "Nieuwe leningen city investment financing 0.058m 2025"),
    ("bud_agbschoten_loan_repay_2025", 132001, "Periodieke aflossingen 0.132m 2025"),
    ("bud_agbschoten_budget_2025", 119601, "Budgettair resultaat +0.120m 2025"),
    ("bud_agbschoten_cum_budget_2025", 2133070, "Gecumuleerd budgettair YE2025 2.133m"),
    ("bud_agbschoten_bbr_2025", 2133070, "Beschikbaar budgettair resultaat 2.133m healthy"),
    ("bud_agbschoten_afm_2025", 119601, "Autofinancieringsmarge +0.120m 2025"),
    ("bud_agbschoten_afm_gecorr_2025", 199857, "Gecorrigeerde AFM +0.200m 2025"),
    ("bud_agbschoten_pnl_2025", 70548, "PnL overschot +0.071m 2025"),
    ("bud_agbschoten_dividend_city_2025", 65000, "Rechthebbenden/dividend to city 0.065m 2025"),
    ("bud_agbschoten_interest_2025", 0, "Financiele kosten 0 2025 (city loan no bank interest)"),
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
        "comm_agbschoten_st_nonruil_recv_2_06m_2025",
        "AGB Schoten ST non-ruil recv 2.061m FOI",
        "2060662",
        "stock",
        "Composition of non-exchange ST receivables",
        "FOI residual non-ruil recv",
    ),
    (
        "comm_agbschoten_fin_debt_city_0_57m_2025",
        "AGB Schoten city loan fin debt 0.573m",
        "573119",
        "stock",
        "City-only investment loan no bank debt",
        "Map residual city loan schedule",
    ),
    (
        "comm_agbschoten_dividend_city_65k_2025",
        "AGB Schoten dividend to city 0.065m 2025",
        "65000",
        "active",
        "Surplus transfer to parent municipality",
        "Monitor residual dividend policy",
    ),
    (
        "comm_agbschoten_mva_2_19m_2025",
        "AGB Schoten MVA sport plant 2.192m",
        "2192069",
        "stock",
        "Sport facilities Vordensteyn/De Zeurt MVA",
        "Map residual MVA util",
    ),
    (
        "comm_agbschoten_bbr_healthy_2_13m_2025",
        "AGB Schoten BBR 2.133m healthy AFM +0.12m",
        "2133070",
        "stock",
        "Healthy dual residual Entity II sport AGB",
        "Monitor residual dual closed",
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
            "decision_date": "2026-03-13",
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
            "hierarchy_path": "Vlaanderen>Gemeenten>Schoten>AGB_Schoten",
            "notes": f"tick{TICK}",
        }
    )
save(DATA / "commitments.csv", cf, comms, cenc)
print("comms ok")

lf, lbs, lenc = load(DATA / "leaderboard.csv")
lex = {x.get("item_id") for x in lbs}
lrows = [
    (
        "lb_agbschoten_st_nonruil_recv_2_06m_2025",
        "AGB Schoten ST non-ruil recv 2.06m FOI",
        "2060662",
        "7.0",
        "FOI residual non-ruil recv composition",
    ),
    (
        "lb_agbschoten_mva_2_19m_2025",
        "AGB Schoten MVA sport plant 2.19m",
        "2192069",
        "5.5",
        "Map residual MVA util",
    ),
    (
        "lb_agbschoten_fin_debt_0_57m_2025",
        "AGB Schoten city loan fin debt 0.57m",
        "573119",
        "5.0",
        "City loan schedule residual",
    ),
    (
        "lb_agbschoten_bbr_healthy_2_13m_2025",
        "AGB Schoten BBR 2.13m healthy dual",
        "2133070",
        "4.0",
        "Monitor residual dual closed healthy",
    ),
    (
        "lb_agbschoten_assets_4_44m_2025",
        "AGB Schoten assets 4.44m Entity II sport",
        "4438056",
        "5.0",
        "Map residual Entity II",
    ),
    (
        "lb_agbschoten_dividend_city_65k_2025",
        "AGB Schoten dividend city 65k 2025",
        "65000",
        "4.5",
        "Monitor residual dividend",
    ),
    (
        "lb_agbschoten_afm_pos_0_12m_2025",
        "AGB Schoten AFM +0.12m / budget +0.12m",
        "119601",
        "3.5",
        "Healthy residual AFM",
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
            "hierarchy_path": "Vlaanderen>Gemeenten>Schoten>AGB_Schoten_L5",
            "annual_cost_eur": str(abs(int(cost))),
            "total_cost_eur": str(abs(int(cost))),
            "tco_notes": "JR2025 Entity II dual residual VL strong primary BBC healthy sport AGB",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Schoten residents",
            "stated_goal": "Local dual residual map VL JR2025 AGB Schoten",
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
            "hierarchy_path": "Vlaanderen>Gemeenten>Schoten>AGB_Schoten>nonruil_recv_city_loan_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "Composition of ST non-ruil receivables 2.061m (counterparties maturity "
                "nature); city loan schedule remaining fin debt 0.573m (LT 0.475 ST due "
                "0.098 amort 0.132m/yr); terms of city investment financing 0.058m new in "
                "2025; dividend/surplus transfer policy 0.065m to city; MVA sport plant "
                "utilisation 2.192m Vordensteyn/De Zeurt"
            ),
            "why_it_matters": (
                "Entity II dual residual: healthy BBR/AFM sport AGB but opaque 2.06m "
                "non-exchange ST receivables and parent-city loan dependency; dual after "
                "city GE already mined"
            ),
            "priority": "7",
            "recipient_body": "Gemeente / AGB Schoten",
            "recipient_email": "info@schoten.be",
            "recipient_postal": "Verbertstraat 3 2900 Schoten",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-07",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbschoten_st_nonruil_recv_2_06m_2025",
            "linked_leaderboard_id": "lb_agbschoten_st_nonruil_recv_2_06m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    )
    save(DATA / "foi_queue.csv", ff, fois, "utf-8")
    print("foi +1")

rf, rqs, renc = load(DATA / "research_queue.csv")
for row in rqs:
    if row.get("task_id") == "rq_1157":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["entity_id"] = ENT
        row["blocked_gap_id"] = GAP
        row["notes"] = (
            f"tick{TICK}: AGB Schoten assets 4.44m BBR 2.13m AFM +0.12m fin debt 0.57m "
            "ST non-ruil recv 2.06m FOI; spawn rq_1158 residual dual L5"
        )
if not any(r.get("task_id") == "rq_1158" for r in rqs):
    rqs.append(
        {
            "task_id": "rq_1158",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "PROGRESS residual dual L5 (Oosterzele / Nijlen login / Bornem JR2024 / "
                "Schelle GE+OCMW / Lievegem / Roeselare / Wommelgem / AGB Stabroek / other); "
                "skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned tick{TICK} after AGB Schoten; continuous hole_fill",
        }
    )
save(DATA / "research_queue.csv", rf, rqs, renc)

lsf, lss, lsenc = load(DATA / "loop_state.csv")
for row in lss:
    row["mode"] = "continuous"
    row["current_sprint"] = "hole_fill"
    row["last_tick_utc"] = UTC
    row["last_unit_id"] = "rq_1157"
    row["ticks_completed"] = str(TICK)
    row["paused"] = "no"
    row["notes"] = (
        f"tick{TICK} AGB Schoten healthy BBR/AFM dual residual ST non-ruil 2.06m FOI; "
        "next rq_1158 residual dual L5; rq_116 deferred; continuous hole_fill"
    )
save(DATA / "loop_state.csv", lsf, lss, lsenc)
print("OK ticks=1157")

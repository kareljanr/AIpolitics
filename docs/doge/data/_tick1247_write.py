# -*- coding: utf-8 -*-
"""Tick 1247: Zorgbedrijf Rivierenland JR2025 Entity II dual residual (AFM NEG / gecorr DEEP NEG)."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T05:56:00Z"
TICK = 1247
SRC = "src_zorgbedrijf_rivierenland_jr2025"
ENT = "zorgbedrijf_rivierenland"
CITY = "city_mechelen"
CITY2 = "city_sint_katelijne_waver"
SRC_URL = (
    "https://rivierenland.mechelen-prod.hosted-temp.com/sites/"
    "zorgbedrijfrivierenland/files/algemeen/files/2026-07/"
    "zb-rivierenland-jr2025-av-28052026-.pdf"
)
GAP = "gap_zbr_afm_neg_1_50m_gecorr_3_52m_fin_debt_69_1m_ocmw_cut_4m_pnl_neg_1_20m_l5"
HIER = "Vlaanderen>Gemeenten>Mechelen>Zorgbedrijf_Rivierenland"


def append_rows(path, new_rows):
    """Append dict rows using existing header; do not rewrite the file."""
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing_ids = set()
        id_key = fields[0]
        for row in reader:
            existing_ids.add(row.get(id_key))
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(id_key) in existing_ids:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added


# --- sources ---
n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Zorgbedrijf Rivierenland WV JR2025 BBC (71p text) dual residual",
            "url": SRC_URL,
            "publisher": "Zorgbedrijf Rivierenland / OCMW Mechelen / OCMW Sint-Katelijne-Waver",
            "accessed_date": "2026-08-17",
            "source_class": "primary_pdf",
            "notes": (
                "tick1247; KBO 0680.439.360 Wilsonstraat 28 2860 Sint-Katelijne-Waver; "
                "AD Geert Debbaut FD Brigitte Verstrepen; AV 28.05.2026; 71p text primary; "
                "assets 96.212m fin debt 69.051m AFM -1.500m gecorr -3.521m OCMW toelage "
                "5.513m (Mechelen cut 4.000m) PnL -1.200m personnel 36.072m"
            ),
        }
    ],
)
print("sources", n)

# --- entities ---
n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "Zorgbedrijf Rivierenland Welzijnsvereniging",
            "name_fr": "Zorgbedrijf Rivierenland (soins)",
            "name_en": "Zorgbedrijf Rivierenland care association (WZC dual Mechelen/SKW)",
            "level": "ocmw_association",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.zorgbedrijfrivierenland.be",
            "foi_email": "info@zbrivierenland.be",
            "foi_postal": "Wilsonstraat 28 2860 Sint-Katelijne-Waver",
            "notes": (
                "tick1247; dual residual OCMW Mechelen + OCMW SKW; KBO 0680.439.360; "
                f"FOI {GAP}"
            ),
        }
    ],
)
print("entities", n)

# --- budgets ---
bud_rows = [
    ("bud_zbr_assets_2025", 96211788, "Assets balanstotaal YE2025 96.212m"),
    ("bud_zbr_equity_2025", 14123740, "Nettoactief YE2025 14.124m"),
    ("bud_zbr_debt_total_2025", 82088048, "Schulden total YE2025 82.088m"),
    ("bud_zbr_fin_debt_2025", 69050596, "Fin schulden total YE2025 69.051m (LT 65.381 + ST due 3.670)"),
    ("bud_zbr_fin_debt_lt_2025", 65381084, "Fin schulden LT YE2025 65.381m"),
    ("bud_zbr_fin_debt_st_due_2025", 3669512, "Fin schulden LT vervallend YE2025 3.670m"),
    ("bud_zbr_cash_2025", 6438461, "Liquide middelen YE2025 6.438m JUMP (was 4.562m)"),
    ("bud_zbr_st_recv_2025", 6066700, "Vorderingen KT total YE2025 6.067m"),
    ("bud_zbr_mva_2025", 80622134, "Materiele VA YE2025 80.622m"),
    ("bud_zbr_cap_subs_2025", 11027362, "Kapitaalssubsidies YE2025 11.027m"),
    ("bud_zbr_cum_pnl_2025", 1536507, "Gecumuleerd overschot YE2025 1.537m DROP (was 2.737m)"),
    ("bud_zbr_expl_rec_2025", 55531602, "Exploitatieontvangsten 55.532m"),
    ("bud_zbr_expl_exp_2025", 53828620, "Exploitatieuitgaven 53.829m"),
    ("bud_zbr_expl_saldo_2025", 1702982, "Exploitatiesaldo +1.703m"),
    ("bud_zbr_invest_exp_2025", 1653494, "Investeringsuitgaven 1.653m"),
    ("bud_zbr_invest_rec_2025", 2280968, "Investeringsontvangsten 2.281m"),
    ("bud_zbr_invest_saldo_2025", 627474, "Investeringssaldo +0.627m"),
    ("bud_zbr_fin_saldo_2025", -3807456, "Financieringssaldo -3.807m"),
    ("bud_zbr_budget_result_2025", -1477000, "Budgettair resultaat boekjaar -1.477m NEG"),
    ("bud_zbr_cumul_budget_2025", 3402003, "Gecumuleerd budgettair resultaat +3.402m"),
    ("bud_zbr_bbr_2025", 3402003, "BBR +3.402m"),
    ("bud_zbr_afm_2025", -1500007, "AFM -1.500m NEG"),
    ("bud_zbr_gecorr_afm_2025", -3521195, "Gecorrigeerde AFM -3.521m DEEP NEG"),
    ("bud_zbr_pnl_2025", -1200281, "PnL tekort -1.200m flip (was +2.297m)"),
    ("bud_zbr_personnel_2025", 36071832, "Bezoldigingen J5 36.072m"),
    ("bud_zbr_personnel_incl_interim_2025", 43800999, "Personeel incl interim toelichting 43.801m"),
    ("bud_zbr_goederen_2025", 17053323, "Goederen en diensten 17.053m"),
    ("bud_zbr_sub_total_2025", 17063095, "Werkingssubsidies total J5 17.063m"),
    ("bud_zbr_ocmw_sub_alg_2025", 5513025, "OCMW dual algemene werkingssub 5.513m"),
    ("bud_zbr_ocmw_mechelen_sub_2025", 3131494, "OCMW Mechelen toelage 3.131m (cut 4.000m vs budget 7.131m)"),
    ("bud_zbr_ocmw_skw_sub_2025", 2381531, "OCMW SKW toelage 2.382m"),
    ("bud_zbr_sub_spec_2025", 11550070, "Specifieke werkingssubsidies 11.550m"),
    ("bud_zbr_mechelen_invest_sub_2025", 1676501, "Invest-sub Mechelen Hof van Egmont 1.677m"),
    ("bud_zbr_vipa_lisdodde_2025", 604467, "VIPA invest-sub wzc De Lisdodde 0.604m"),
    ("bud_zbr_werking_ontv_2025", 37644920, "Opbrengsten uit de werking 37.645m"),
    ("bud_zbr_new_loans_2025", 0, "Nieuwe leningen 2025 EUR0"),
    ("bud_zbr_repayments_2025", 3807456, "Periodieke aflossingen 3.807m"),
    ("bud_zbr_interest_2025", 691670, "Financiele kosten J5 0.692m"),
    ("bud_zbr_costs_2025", 57323145, "J5 costs total 57.323m"),
    ("bud_zbr_provisions_vg_2025", 3722003, "Voorziening vakantiegeld YE2025 3.722m"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": "2025",
            "amount_eur": str(int(amt)),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "bbc_jr_realized",
            "source_id": SRC,
            "confidence": "strong",
            "notes": f"{note}; tick{TICK}",
        }
        for bid, amt, note in bud_rows
    ],
)
print("budgets", n)

# --- commitments ---
crows = [
    (
        "comm_zbr_afm_neg_1_50m_2025",
        "Zorgbedrijf Rivierenland AFM -1.500m NEG",
        "1500007",
        "OCMW Mechelen 4m toelage cut drives AFM NEG",
        "OCMW package + amort FOI",
    ),
    (
        "comm_zbr_gecorr_afm_neg_3_52m_2025",
        "Zorgbedrijf Rivierenland gecorr AFM -3.521m DEEP NEG",
        "3521195",
        "Corrected amort 5.829m vs contractual 3.807m",
        "OCMW package + amort FOI",
    ),
    (
        "comm_zbr_fin_debt_69_1m_2025",
        "Zorgbedrijf Rivierenland fin debt 69.051m",
        "69050596",
        "Care campus debt stock no new 2025 loans",
        "Lender/guarantee FOI",
    ),
    (
        "comm_zbr_ocmw_sub_5_51m_2025",
        "Zorgbedrijf Rivierenland OCMW dual toelage 5.513m",
        "5513025",
        "Mechelen 3.131m after 4.000m cut + SKW 2.382m",
        "OCMW multi-year matrix FOI",
    ),
    (
        "comm_zbr_pnl_neg_1_20m_2025",
        "Zorgbedrijf Rivierenland PnL -1.200m",
        "1200281",
        "PnL flip from +2.297m after toelage cut",
        "OCMW package + P&L FOI",
    ),
    (
        "comm_zbr_personnel_36_1m_2025",
        "Zorgbedrijf Rivierenland personnel 36.072m",
        "36071832",
        "Care payroll dual residual",
        "FTE recon FOI",
    ),
    (
        "comm_zbr_budget_neg_1_48m_2025",
        "Zorgbedrijf Rivierenland budget result -1.477m",
        "1477000",
        "Cash-year deficit after zero new loans",
        "OCMW package + amort FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Zorgbedrijf Rivierenland / OCMW Mechelen / OCMW SKW",
            "legal_basis": "BBC JR2025 multi-muni dual care",
            "decision_date": "2026-05-28",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary Zorgbedrijf Rivierenland JR2025",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

# --- leaderboard ---
lrows = [
    ("lb_zbr_afm_neg_1_50m_2025", "Zorgbedrijf Rivierenland AFM -1.50m", "1500007", "8.0", "7.0", "3.5"),
    ("lb_zbr_gecorr_afm_neg_3_52m_2025", "Zorgbedrijf Rivierenland gecorr AFM -3.52m", "3521195", "8.5", "7.2", "3.5"),
    ("lb_zbr_fin_debt_69_1m_2025", "Zorgbedrijf Rivierenland fin debt 69.1m", "69050596", "7.5", "8.5", "4.0"),
    ("lb_zbr_ocmw_sub_5_51m_2025", "Zorgbedrijf Rivierenland OCMW dual toelage 5.51m after 4m cut", "5513025", "8.0", "7.0", "3.0"),
    ("lb_zbr_pnl_neg_1_20m_2025", "Zorgbedrijf Rivierenland PnL -1.20m", "1200281", "7.5", "6.0", "3.5"),
    ("lb_zbr_personnel_36_1m_2025", "Zorgbedrijf Rivierenland personnel 36.1m dual residual", "36071832", "6.0", "8.0", "4.0"),
    ("lb_zbr_budget_neg_1_48m_2025", "Zorgbedrijf Rivierenland budget result -1.48m", "1477000", "7.5", "6.0", "3.5"),
]
n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + "_L5",
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": "Multi-muni dual care residual Zorgbedrijf Rivierenland JR2025",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Mechelen / Sint-Katelijne-Waver residents / seniors / WZC users",
            "stated_goal": "Local dual residual care map VL JR2025",
            "measured_outcome": "AFM -1.50m; gecorr -3.52m; fin debt 69.1m; OCMW toelage 5.51m after Mechelen -4m; PnL -1.20m",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "OCMW package + amort/lender FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary Zorgbedrijf Rivierenland JR2025; not TE-additive without care",
        }
        for iid, name, cost, absurd, cscore, diff in lrows
    ],
)
print("leaderboard", n)

# --- foi_queue ---
n = append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": HIER + ">jr2025_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "OCMW dual toelage multi-year matrix Mechelen 3.131m after 4.000m cut + SKW 2.382m; "
                "AFM -1.500m / gecorr -3.521m recovery vs corrected amort 5.829m; fin debt 69.051m "
                "lender/rate/guarantee split; PnL -1.200m drivers; personnel 36.072m vs 43.801m FTE; "
                "invest-sub Mechelen 1.677m + VIPA 0.604m remaining; 2026 planned loans 16.895m"
            ),
            "why_it_matters": (
                "Dual care residual: AFM -1.50m gecorr -3.52m fin debt 69.1m after Mechelen "
                "toelage cut 4m; PnL flip -1.20m"
            ),
            "priority": "9",
            "recipient_body": "Zorgbedrijf Rivierenland / OCMW Mechelen / OCMW Sint-Katelijne-Waver",
            "recipient_email": "info@zbrivierenland.be",
            "recipient_postal": "Wilsonstraat 28 2860 Sint-Katelijne-Waver",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_zbr_afm_neg_1_50m_2025",
            "linked_leaderboard_id": "lb_zbr_afm_neg_1_50m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

# --- research_queue: stream replace rq_1247 + append rq_1248 ---
rq_path = DATA / "research_queue.csv"
tmp = rq_path.with_suffix(".csv.tmp")
found_1247 = False
has_1248 = False
with rq_path.open(encoding="utf-8", newline="") as fin, tmp.open("w", encoding="utf-8", newline="") as fout:
    r = csv.DictReader(fin)
    fields = r.fieldnames
    w = csv.DictWriter(fout, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for row in r:
        if row.get("task_id") == "rq_1247":
            found_1247 = True
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["entity_id"] = ENT
            row["title"] = "Zorgbedrijf Rivierenland dual residual JR2025 multi-muni care Entity II"
            row["instructions"] = (
                "Completed: Zorgbedrijf Rivierenland JR2025 full BBC text primary dual care"
            )
            row["blocked_gap_id"] = GAP
            row["notes"] = (
                "tick1247; KBO 0680.439.360 assets 96.2m fin debt 69.1m AFM -1.50m "
                "gecorr -3.52m OCMW toelage 5.51m Mechelen cut 4m PnL -1.20m; FOI ready; spawn rq_1248"
            )
        if row.get("task_id") == "rq_1248":
            has_1248 = True
        w.writerow(row)
    if not has_1248:
        w.writerow(
            {
                "task_id": "rq_1248",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "hole_fill",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg not yet mined",
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned tick1247 after Zorgbedrijf Rivierenland dual residual; next residual dual L5 VL",
            }
        )
tmp.replace(rq_path)
print("research_queue 1247", found_1247, "spawned_1248", not has_1248)

# --- loop_state ---
with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_1247",
            "ticks_completed": "1247",
            "paused": "no",
            "notes": (
                "tick1247 Zorgbedrijf Rivierenland dual residual AFM -1.50m gecorr -3.52m "
                "fin debt 69.1m OCMW toelage 5.51m Mechelen cut 4m PnL -1.20m FOI ready; "
                "next rq_1248 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

# --- loop_log append ---
log = ROOT / "loop_log.md"
entry = """
### Tick 1247 - 2026-08-17 - rq_1247 Zorgbedrijf Rivierenland dual residual
- Unit: Zorgbedrijf Rivierenland WV JR2025 multi-muni dual care Entity II (KBO 0680.439.360; 71p text primary; members OCMW Mechelen + OCMW Sint-Katelijne-Waver).
- EUR strong: assets **96.2m**; fin debt **69.1m**; AFM **-1.500m** NEG; gecorr AFM **-3.521m** DEEP NEG; budget **-1.477m**; BBR **+3.402m**; OCMW dual toelage **5.513m** (Mechelen **3.131m** after **4.000m** cut + SKW **2.382m**); PnL **-1.200m** flip; personnel **36.072m**; cash JUMP **6.44m**; new loans **0**.
- CSVs: sources/entities/budgets+40/commitments+7/leaderboard+7 + FOI ready `gap_zbr_afm_neg_1_50m_gecorr_3_52m_fin_debt_69_1m_ocmw_cut_4m_pnl_neg_1_20m_l5` (not sent); rq_1247=done; spawn rq_1248.
- Next: rq_1248 residual dual L5 VL JR2025 hole_fill.

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
print("OK ticks=1247")

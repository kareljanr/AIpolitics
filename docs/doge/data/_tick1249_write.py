# -*- coding: utf-8 -*-
"""Tick 1249 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 Zorgbedrijf Sakura JR2025 Entity II dual residual (OCMW toelage JUMP / PnL NEG)."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T06:08:00Z"
TICK = 1249
SRC = "src_zorgbedrijf_sakura_jr2025"
ENT = "zorgbedrijf_sakura"
CITY = "city_lokeren"
SRC_URL = "https://lokeren.be/assets/6a44d9246929a1b43919919f/Sakura%20jaarrekening%202025.pdf"
GAP = "gap_sakura_ocmw_toelage_1_43m_pnl_neg_0_21m_fin_debt_5_66m_l5"
HIER = "Vlaanderen>Gemeenten>Lokeren>Zorgbedrijf_Sakura"


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


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Zorgbedrijf Sakura WV JR2025 BBC (251p text) dual residual",
            "url": SRC_URL,
            "publisher": "Zorgbedrijf Sakura / Stad Lokeren / OCMW Lokeren / OCMW Moerbeke-Waas",
            "accessed_date": "2026-08-17",
            "source_class": "primary_pdf",
            "notes": (
                "tick1249; KBO 0684.613.726 Polderstraat 2 9160 Lokeren NIS 44034; "
                "AD Bart D'Hanis FD Beatrice Sergeant; AV 24.06.2026; 251p text primary; "
                "assets 25.121m fin debt 5.656m AFM +0.427m gecorr +0.638m OCMW toelage 1.432m "
                "JUMP PnL -0.206m cash 3.397m BBR 4.242m personnel 18.694m"
            ),
        }
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "Zorgbedrijf Sakura Welzijnsvereniging",
            "name_fr": "Zorgbedrijf Sakura (soins)",
            "name_en": "Zorgbedrijf Sakura care association (WZC dual Lokeren/Moerbeke)",
            "level": "ocmw_association",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://zorgbedrijf-sakura.lokeren.be",
            "foi_email": "info@zorgbedrijfsakura.be",
            "foi_postal": "Polderstraat 2 9160 Lokeren",
            "notes": (
                "tick1249; dual residual OCMW Lokeren + OCMW Moerbeke-Waas; "
                f"KBO 0684.613.726; FOI {GAP}"
            ),
        }
    ],
)
print("entities", n)

bud_rows = [
    ("bud_sak_assets_2025", 25121424, "Assets balanstotaal YE2025 25.121m DROP (was 26.129m)"),
    ("bud_sak_equity_2025", 16044758, "Nettoactief YE2025 16.045m"),
    ("bud_sak_debt_total_2025", 9076666, "Schulden total YE2025 9.077m"),
    ("bud_sak_fin_debt_2025", 5655658, "Fin schulden total YE2025 5.656m (LT 4.975 + ST due 0.681)"),
    ("bud_sak_fin_debt_lt_2025", 4974876, "Fin schulden LT YE2025 4.975m"),
    ("bud_sak_fin_debt_st_due_2025", 680781, "Fin schulden LT vervallend YE2025 0.681m"),
    ("bud_sak_cash_2025", 3396586, "Liquide middelen YE2025 3.397m JUMP (was 3.107m)"),
    ("bud_sak_st_recv_2025", 2931974, "Vorderingen KT total YE2025 2.932m"),
    ("bud_sak_st_recv_nonruil_2025", 641899, "Vorderingen KT niet-ruil YE2025 0.642m"),
    ("bud_sak_mva_2025", 18606812, "Materiele VA YE2025 18.607m"),
    ("bud_sak_leasing_mva_2025", 0, "Leasing MVA YE2025 EUR0"),
    ("bud_sak_cap_subs_2025", 5223121, "Kapitaalssubsidies YE2025 5.223m"),
    ("bud_sak_cum_pnl_2025", 1729412, "Gecumuleerd overschot YE2025 1.729m (was 1.935m)"),
    ("bud_sak_expl_rec_2025", 24766709, "Exploitatieontvangsten 24.767m"),
    ("bud_sak_expl_exp_2025", 23618332, "Exploitatieuitgaven 23.618m"),
    ("bud_sak_expl_saldo_2025", 1148377, "Exploitatiesaldo +1.148m"),
    ("bud_sak_invest_exp_2025", 462985, "Investeringsuitgaven 0.463m"),
    ("bud_sak_invest_rec_2025", 44573, "Investeringsontvangsten 0.045m"),
    ("bud_sak_invest_saldo_2025", -418412, "Investeringssaldo -0.418m"),
    ("bud_sak_fin_saldo_2025", -721802, "Financieringssaldo -0.722m"),
    ("bud_sak_budget_result_2025", 8163, "Budgettair resultaat boekjaar +8.163"),
    ("bud_sak_bbr_2025", 4241640, "BBR +4.242m"),
    ("bud_sak_afm_2025", 426575, "AFM +0.427m declining (2018 +0.919m; 2023 was -25k)"),
    ("bud_sak_gecorr_afm_2025", 638180, "Gecorrigeerde AFM +0.638m"),
    ("bud_sak_pnl_2025", -206028, "PnL tekort -0.206m"),
    ("bud_sak_op_pnl_2025", -478911, "Operationeel PnL -0.479m NEG"),
    ("bud_sak_personnel_2025", 18694306, "Bezoldigingen J5 18.694m / 226.48 VTE"),
    ("bud_sak_goederen_2025", 4704543, "Goederen en diensten 4.705m"),
    ("bud_sak_sub_total_2025", 4875123, "Werkingssubsidies total J5 4.875m"),
    ("bud_sak_ocmw_sub_alg_2025", 1432100, "OCMW dual algemene werkingssub 1.432m JUMP (was 1.172m)"),
    ("bud_sak_ocmw_lokeren_alg_2025", 1108300, "OCMW Lokeren algemene werkingssub 1.108m JUMP +270.8k"),
    ("bud_sak_ocmw_moerbeke_alg_2025", 323800, "OCMW Moerbeke algemene werkingssub 0.324m flat"),
    ("bud_sak_vl_sub_alg_2025", 183132, "VL algemene werkingssub 0.183m"),
    ("bud_sak_sub_spec_2025", 3259891, "Specifieke werkingssub 3.260m"),
    ("bud_sak_vl_sub_spec_2025", 2010181, "VL specifieke werkingssub 2.010m"),
    ("bud_sak_fed_sub_spec_2025", -28333, "FED specifieke werkingssub -28k (clawback/reclass)"),
    ("bud_sak_other_sub_spec_2025", 1278044, "Andere entiteiten specifieke werkingssub 1.278m"),
    ("bud_sak_vl_invest_sub_2025", 44573, "Invest-sub VL 0.045m"),
    ("bud_sak_werking_ontv_2025", 19447744, "Opbrengsten uit de werking 19.448m"),
    ("bud_sak_new_loans_2025", 0, "Nieuwe leningen 2025 EUR0 (2024 3.000m)"),
    ("bud_sak_repayments_2025", 721802, "Periodieke aflossingen 0.722m"),
    ("bud_sak_interest_2025", 154063, "Financiele kosten J5 0.154m"),
    ("bud_sak_costs_2025", 25383003, "J5 costs total 25.383m"),
    ("bud_sak_provisions_2025", 1323866, "Voorzieningen KT YE2025 1.324m"),
    ("bud_sak_pnl_ex_toelage_2025", -1638128, "PnL zonder OCMW toelage -1.638m (entity note p.92)"),
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

crows = [
    (
        "comm_sak_ocmw_toelage_1_43m_2025",
        "Zorgbedrijf Sakura OCMW algemene werkingssub 1.432m JUMP",
        "1432100",
        "OCMW dual toelage restored to 2018 level; Lokeren +270.8k",
        "OCMW multi-year matrix FOI",
    ),
    (
        "comm_sak_pnl_neg_0_21m_2025",
        "Zorgbedrijf Sakura PnL -0.206m / op -0.479m",
        "206028",
        "Book loss vs AFM +0.427m / BBR +4.24m; without toelage -1.638m",
        "PnL vs AFM recon FOI",
    ),
    (
        "comm_sak_fin_debt_5_66m_2025",
        "Zorgbedrijf Sakura fin debt 5.656m declining",
        "5655658",
        "2024 new loan 3.000m; 2025 new loans 0; repay 0.722m",
        "Lender/guarantee FOI",
    ),
    (
        "comm_sak_personnel_18_7m_2025",
        "Zorgbedrijf Sakura personnel 18.694m / 226.48 VTE",
        "18694306",
        "Care payroll 226.48 VTE (was 230.73)",
        "FTE recon FOI",
    ),
    (
        "comm_sak_afm_0_43m_declining_2025",
        "Zorgbedrijf Sakura AFM +0.427m declining",
        "426575",
        "AFM down from 2018 +0.919m; 2023 was -25k",
        "AFM path / indexation FOI",
    ),
    (
        "comm_sak_bbr_4_24m_cash_3_40m_2025",
        "Zorgbedrijf Sakura BBR 4.242m cash 3.397m JUMP",
        "4241640",
        "Healthy BBR vs book loss; cash jump 3.107 to 3.397m",
        "Working-capital / OCMW recv FOI",
    ),
    (
        "comm_sak_pnl_ex_toelage_1_64m_2025",
        "Zorgbedrijf Sakura PnL without OCMW toelage -1.638m",
        "1638128",
        "Entity note: dual toelage is the solvency plug",
        "OCMW clawback / indexation FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Zorgbedrijf Sakura / OCMW Lokeren / OCMW Moerbeke-Waas",
            "legal_basis": "BBC JR2025 multi-muni dual care",
            "decision_date": "2026-06-24",
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
            "notes": f"tick{TICK}; primary Zorgbedrijf Sakura JR2025",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_sak_ocmw_toelage_1_43m_2025", "Zorgbedrijf Sakura OCMW toelage JUMP 1.43m", "1432100", "8.0", "6.5", "3.0"),
    ("lb_sak_pnl_neg_0_21m_2025", "Zorgbedrijf Sakura PnL -0.21m / op -0.48m", "206028", "7.5", "5.5", "3.5"),
    ("lb_sak_fin_debt_5_66m_2025", "Zorgbedrijf Sakura fin debt 5.66m declining", "5655658", "7.0", "6.5", "4.0"),
    ("lb_sak_personnel_18_7m_2025", "Zorgbedrijf Sakura personnel 18.7m dual residual", "18694306", "6.0", "7.5", "4.0"),
    ("lb_sak_afm_0_43m_declining_2025", "Zorgbedrijf Sakura AFM +0.43m declining vs 2018", "426575", "7.0", "5.5", "3.0"),
    ("lb_sak_bbr_4_24m_cash_3_40m_2025", "Zorgbedrijf Sakura BBR 4.24m cash 3.40m JUMP", "4241640", "6.5", "6.0", "3.0"),
    ("lb_sak_pnl_ex_toelage_1_64m_2025", "Zorgbedrijf Sakura PnL without OCMW toelage -1.64m", "1638128", "8.0", "6.5", "3.0"),
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
            "tco_notes": "Multi-muni dual care residual Zorgbedrijf Sakura JR2025",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Lokeren / Moerbeke-Waas residents / seniors / WZC users",
            "stated_goal": "Local dual residual care map VL JR2025",
            "measured_outcome": "OCMW toelage JUMP 1.43m; PnL -0.21m; fin debt 5.66m; AFM +0.43m declining; BBR 4.24m cash 3.40m",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "OCMW package + AFM/PnL/debt FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary Zorgbedrijf Sakura JR2025; not TE-additive without care",
        }
        for iid, name, cost, absurd, cscore, diff in lrows
    ],
)
print("leaderboard", n)

n = append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": HIER + ">jr2025_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "OCMW dual toelage multi-year matrix algemene 1.432m JUMP (Lokeren 1.108m +270.8k "
                "+ Moerbeke 0.324m flat) + 2026 indexation decision; AFM +0.427m declining vs 2018 "
                "+0.919m (2023 was -25k) vs PnL -0.206m / op -0.479m; without toelage PnL -1.638m; "
                "fin debt 5.656m lender/guarantee 2024 new loan 3.000m; T2 FED specific -28k vs "
                "other 1.278m reclass; FTE 226.48"
            ),
            "why_it_matters": (
                "Dual care residual: OCMW toelage JUMP 1.43m; PnL -0.21m / op -0.48m; "
                "without toelage -1.64m; fin debt 5.66m; AFM +0.43m declining; BBR 4.24m"
            ),
            "priority": "9",
            "recipient_body": "Zorgbedrijf Sakura / OCMW Lokeren / OCMW Moerbeke-Waas",
            "recipient_email": "info@zorgbedrijfsakura.be",
            "recipient_postal": "Polderstraat 2 9160 Lokeren",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_sak_ocmw_toelage_1_43m_2025",
            "linked_leaderboard_id": "lb_sak_ocmw_toelage_1_43m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

# Surgical research_queue: rewrite only target rows via line-preserving copy
rq_path = DATA / "research_queue.csv"
tmp = rq_path.with_suffix(".csv.tmp")
found_1249 = False
has_1250 = False
with rq_path.open(encoding="utf-8", newline="") as fin, tmp.open("w", encoding="utf-8", newline="") as fout:
    r = csv.DictReader(fin)
    fields = r.fieldnames
    w = csv.DictWriter(fout, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for row in r:
        if row.get("task_id") == "rq_1249":
            found_1249 = True
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["entity_id"] = ENT
            row["title"] = "Zorgbedrijf Sakura dual residual JR2025 multi-muni care Entity II"
            row["instructions"] = (
                "Completed: Zorgbedrijf Sakura JR2025 full BBC text primary dual care"
            )
            row["blocked_gap_id"] = GAP
            row["notes"] = (
                "tick1249; KBO 0684.613.726 assets 25.1m fin debt 5.66m AFM +0.43m "
                "gecorr +0.64m OCMW toelage JUMP 1.43m PnL -0.21m cash 3.40m BBR 4.24m; "
                "FOI ready; spawn rq_1250"
            )
        if row.get("task_id") == "rq_1250":
            has_1250 = True
        w.writerow(row)
    if not has_1250:
        w.writerow(
            {
                "task_id": "rq_1250",
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
                "notes": "spawned tick1249 after Zorgbedrijf Sakura dual residual; next residual dual L5 VL",
            }
        )
tmp.replace(rq_path)
print("research_queue 1249", found_1249, "spawned_1250", not has_1250)

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
            "last_unit_id": "rq_1249",
            "ticks_completed": "1249",
            "paused": "no",
            "notes": (
                "tick1249 Zorgbedrijf Sakura dual residual OCMW toelage JUMP 1.43m "
                "PnL -0.21m fin debt 5.66m AFM +0.43m declining BBR 4.24m cash 3.40m "
                "FOI ready; next rq_1250 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1249 - 2026-08-17 - rq_1249 Zorgbedrijf Sakura dual residual
- Unit: Zorgbedrijf Sakura WV JR2025 multi-muni dual care Entity II (KBO 0684.613.726; 251p text primary; members OCMW Lokeren + OCMW Moerbeke-Waas).
- EUR strong: assets **25.1m** DROP; fin debt **5.66m** declining; AFM **+0.427m** declining (2018 +0.919m); gecorr AFM **+0.638m**; BBR **+4.242m**; OCMW algemene werkingssub **1.432m** JUMP (Lokeren **1.108m** +270.8k + Moerbeke **0.324m**); PnL **-0.206m**; op PnL **-0.479m**; without toelage PnL **-1.638m**; cash JUMP **3.397m**; personnel **18.694m** / 226.48 VTE; new loans **0**.
- CSVs: sources/entities/budgets+45/commitments+7/leaderboard+7 + FOI ready `gap_sakura_ocmw_toelage_1_43m_pnl_neg_0_21m_fin_debt_5_66m_l5` (not sent); rq_1249=done; spawn rq_1250.
- Next: rq_1250 residual dual L5 VL JR2025 hole_fill.

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
print("OK ticks=1249")

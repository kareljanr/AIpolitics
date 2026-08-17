# -*- coding: utf-8 -*-
"""Tick 1248 (research_queue patched surgically after run — do not DictWriter-rewrite the whole file):
 Zorgbedrijf Meetjesland JR2025 Entity II dual residual (AFM thin NEG / OCMW sub jump)."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T06:02:00Z"
TICK = 1248
SRC = "src_zorgbedrijf_meetjesland_jr2025"
ENT = "zorgbedrijf_meetjesland"
CITY = "city_evergem"
SRC_URL = "https://www.zorgbedrijfmeetjesland.be/wp-content/uploads/2026/06/Jaarrekening-2025.pdf"
GAP = "gap_zbm_afm_thin_neg_4k_ocmw_sub_jump_4_81m_fin_debt_9_32m_liq_0_71_l5"
HIER = "Vlaanderen>Gemeenten>Evergem>Zorgbedrijf_Meetjesland"


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
            "title": "Zorgbedrijf Meetjesland WV JR2025 BBC (298p text) dual residual",
            "url": SRC_URL,
            "publisher": "Zorgbedrijf Meetjesland / OCMW Evergem / Maldegem / Deinze / Lievegem",
            "accessed_date": "2026-08-17",
            "source_class": "primary_pdf",
            "notes": (
                "tick1248; KBO 0666.615.870 Sleidinge-Dorp 43 9940 Evergem NIS 44019; "
                "AD Piet Vanwambeke Voorzitter Joeri De Maertelaere; AV 17.06.2026; 298p text primary; "
                "assets 42.477m fin debt 9.319m AFM -4.370 gecorr +1.177m OCMW werkingssub 4.805m "
                "JUMP cash 0.925m DROP liq 0.706 personnel 33.208m"
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
            "name_nl": "Zorgbedrijf Meetjesland Welzijnsvereniging",
            "name_fr": "Zorgbedrijf Meetjesland (soins)",
            "name_en": "Zorgbedrijf Meetjesland care association (WZC dual Evergem/Maldegem/Deinze/Lievegem)",
            "level": "ocmw_association",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.zorgbedrijfmeetjesland.be",
            "foi_email": "info@zorgbedrijfmeetjesland.be",
            "foi_postal": "Sleidinge-Dorp 43 9940 Evergem",
            "notes": (
                "tick1248; dual residual OCMW Evergem + Maldegem + Deinze + Lievegem; "
                f"KBO 0666.615.870; FOI {GAP}"
            ),
        }
    ],
)
print("entities", n)

bud_rows = [
    ("bud_zbm_assets_2025", 42477419, "Assets balanstotaal YE2025 42.477m"),
    ("bud_zbm_equity_2025", 25063405, "Nettoactief YE2025 25.063m"),
    ("bud_zbm_debt_total_2025", 17414014, "Schulden total YE2025 17.414m"),
    ("bud_zbm_fin_debt_2025", 9318968, "Fin schulden total YE2025 9.319m (LT 7.159 + ST due 2.160)"),
    ("bud_zbm_fin_debt_lt_2025", 7159457, "Fin schulden LT YE2025 7.159m"),
    ("bud_zbm_fin_debt_st_due_2025", 2159511, "Fin schulden LT vervallend YE2025 2.160m"),
    ("bud_zbm_cash_2025", 925331, "Liquide middelen YE2025 0.925m DROP (was 1.505m)"),
    ("bud_zbm_st_recv_2025", 5675228, "Vorderingen KT total YE2025 5.675m"),
    ("bud_zbm_st_recv_nonruil_2025", 3084665, "Vorderingen KT niet-ruil YE2025 3.085m"),
    ("bud_zbm_mva_2025", 33851534, "Materiele VA YE2025 33.852m"),
    ("bud_zbm_leasing_mva_2025", 28729799, "Leasing MVA YE2025 28.730m"),
    ("bud_zbm_cap_subs_2025", 12442513, "Kapitaalssubsidies YE2025 12.443m"),
    ("bud_zbm_cum_pnl_2025", 458723, "Gecumuleerd overschot YE2025 0.459m (was 971)"),
    ("bud_zbm_expl_rec_2025", 48781952, "Exploitatieontvangsten 48.782m"),
    ("bud_zbm_expl_exp_2025", 47344160, "Exploitatieuitgaven 47.344m"),
    ("bud_zbm_expl_saldo_2025", 1437792, "Exploitatiesaldo +1.438m"),
    ("bud_zbm_invest_exp_2025", 745128, "Investeringsuitgaven 0.745m"),
    ("bud_zbm_invest_rec_2025", 1329758, "Investeringsontvangsten 1.330m"),
    ("bud_zbm_invest_saldo_2025", 584629, "Investeringssaldo +0.585m"),
    ("bud_zbm_fin_saldo_2025", -2022421, "Financieringssaldo -2.022m"),
    ("bud_zbm_budget_result_2025", 0, "Budgettair resultaat boekjaar EUR0 designed-to-zero"),
    ("bud_zbm_bbr_2025", 0, "BBR EUR0 designed-to-zero"),
    ("bud_zbm_afm_2025", -4370, "AFM -4.370 thin NEG designed-to-zero"),
    ("bud_zbm_gecorr_afm_2025", 1176740, "Gecorrigeerde AFM +1.177m"),
    ("bud_zbm_pnl_2025", 457752, "PnL overschot +0.458m"),
    ("bud_zbm_op_pnl_2025", -337769, "Operationeel PnL -0.338m NEG"),
    ("bud_zbm_personnel_2025", 33208276, "Bezoldigingen J5 33.208m"),
    ("bud_zbm_goederen_2025", 13726221, "Goederen en diensten 13.726m"),
    ("bud_zbm_sub_total_2025", 15565579, "Werkingssubsidies total J5 15.566m all specific"),
    ("bud_zbm_ocmw_sub_spec_2025", 4805443, "OCMW dual specifieke werkingssub 4.805m JUMP (was 2.308m)"),
    ("bud_zbm_vl_sub_spec_2025", 6432865, "VL specifieke werkingssub 6.433m"),
    ("bud_zbm_fed_sub_spec_2025", 3504681, "FED specifieke werkingssub 3.505m"),
    ("bud_zbm_ocmw_dots_indep_2025", 1386265, "Resultaatsonafhankelijke OCMW exploitatiedotaties 1.386m"),
    ("bud_zbm_ocmw_evergem_dot_2025", 700528, "OCMW Evergem result-indep dot 0.701m"),
    ("bud_zbm_ocmw_maldegem_dot_2025", 447196, "OCMW Maldegem result-indep dot 0.447m"),
    ("bud_zbm_ocmw_deinze_dot_2025", 219015, "OCMW Deinze result-indep dot 0.219m"),
    ("bud_zbm_ocmw_lievegem_dot_2025", 19526, "OCMW Lievegem result-indep dot 0.020m"),
    ("bud_zbm_ocmw_invest_sub_2025", 652517, "Invest-sub OCMW 0.653m"),
    ("bud_zbm_vl_invest_sub_2025", 677240, "Invest-sub VL 0.677m"),
    ("bud_zbm_werking_ontv_2025", 32824627, "Opbrengsten uit de werking 32.825m"),
    ("bud_zbm_new_loans_2025", 66000, "Nieuwe leningen 2025 EUR66k"),
    ("bud_zbm_repayments_2025", 2088421, "Periodieke aflossingen 2.088m"),
    ("bud_zbm_interest_2025", 369522, "Financiele kosten J5 0.370m"),
    ("bud_zbm_costs_2025", 49484748, "J5 costs total 49.485m"),
    ("bud_zbm_provisions_2025", 1489572, "Voorzieningen KT YE2025 1.490m"),
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
        "comm_zbm_afm_thin_neg_4k_2025",
        "Zorgbedrijf Meetjesland AFM -4.370 thin NEG",
        "4370",
        "Designed-to-zero AFM via OCMW clawback",
        "OCMW package + AFM formula FOI",
    ),
    (
        "comm_zbm_ocmw_sub_jump_4_81m_2025",
        "Zorgbedrijf Meetjesland OCMW specific werkingssub 4.805m JUMP",
        "4805443",
        "OCMW dual specific sub doubled vs 2024 2.308m",
        "OCMW multi-year matrix FOI",
    ),
    (
        "comm_zbm_fin_debt_9_32m_2025",
        "Zorgbedrijf Meetjesland fin debt 9.319m",
        "9318968",
        "Care campus debt vs leasing MVA 28.730m",
        "Lender/guarantee/leasing FOI",
    ),
    (
        "comm_zbm_personnel_33_2m_2025",
        "Zorgbedrijf Meetjesland personnel 33.208m",
        "33208276",
        "Care payroll 747 heads / 523.89 VTE",
        "FTE recon FOI",
    ),
    (
        "comm_zbm_ocmw_dots_1_39m_2025",
        "Zorgbedrijf Meetjesland result-indep OCMW dots 1.386m",
        "1386265",
        "Evergem 0.701 + Maldegem 0.447 + Deinze 0.219 + Lievegem 0.020",
        "OCMW multi-year matrix FOI",
    ),
    (
        "comm_zbm_op_pnl_neg_0_34m_2025",
        "Zorgbedrijf Meetjesland operational PnL -0.338m",
        "337769",
        "Op loss vs total PnL +0.458m; Ter Leenen -0.179m Ter Caele -0.113m",
        "WZC result FOI",
    ),
    (
        "comm_zbm_cash_drop_0_93m_2025",
        "Zorgbedrijf Meetjesland cash 0.925m DROP liquidity 0.71",
        "925331",
        "Cash drop 1.505 to 0.925m; payables 118 days; OCMW as WC bank",
        "Working-capital / OCMW recv FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Zorgbedrijf Meetjesland / OCMW Evergem / Maldegem / Deinze / Lievegem",
            "legal_basis": "BBC JR2025 multi-muni dual care",
            "decision_date": "2026-06-17",
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
            "notes": f"tick{TICK}; primary Zorgbedrijf Meetjesland JR2025",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_zbm_afm_thin_neg_4k_2025", "Zorgbedrijf Meetjesland AFM -4.4k designed-to-zero", "4370", "7.5", "4.0", "3.0"),
    ("lb_zbm_ocmw_sub_jump_4_81m_2025", "Zorgbedrijf Meetjesland OCMW werkingssub JUMP 4.81m", "4805443", "8.0", "7.0", "3.0"),
    ("lb_zbm_fin_debt_9_32m_2025", "Zorgbedrijf Meetjesland fin debt 9.32m vs leasing MVA 28.7m", "9318968", "7.0", "7.5", "4.0"),
    ("lb_zbm_personnel_33_2m_2025", "Zorgbedrijf Meetjesland personnel 33.2m dual residual", "33208276", "6.0", "8.0", "4.0"),
    ("lb_zbm_ocmw_dots_1_39m_2025", "Zorgbedrijf Meetjesland result-indep OCMW dots 1.39m", "1386265", "7.5", "6.0", "3.0"),
    ("lb_zbm_op_pnl_neg_0_34m_2025", "Zorgbedrijf Meetjesland operational PnL -0.34m", "337769", "7.0", "5.5", "3.5"),
    ("lb_zbm_cash_drop_liq_0_71_2025", "Zorgbedrijf Meetjesland cash 0.93m DROP liquidity 0.71", "925331", "7.5", "5.5", "3.0"),
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
            "tco_notes": "Multi-muni dual care residual Zorgbedrijf Meetjesland JR2025",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Evergem / Maldegem / Deinze / Lievegem residents / seniors / WZC users",
            "stated_goal": "Local dual residual care map VL JR2025",
            "measured_outcome": "AFM -4.4k; OCMW sub JUMP 4.81m; fin debt 9.32m; cash 0.93m liq 0.71; op PnL -0.34m",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "OCMW package + AFM/liquidity/leasing FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary Zorgbedrijf Meetjesland JR2025; not TE-additive without care",
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
                "OCMW dual toelage multi-year matrix result-indep 1.386m + result-dep T2 4.805m JUMP "
                "(was 2.308m) per Evergem/Maldegem/Deinze/Lievegem; p.149/152/153 tables are images; "
                "AFM -4.370 designed-to-zero vs gecorr +1.177m; fin debt 9.319m vs leasing MVA 28.730m "
                "lender/guarantee; cash DROP 0.925m liquidity 0.706 payables 118d OCMW WC; "
                "op PnL -0.338m Ter Leenen/Ter Caele; 2027 planned loans 6.940m"
            ),
            "why_it_matters": (
                "Dual care residual: AFM -4.4k designed-to-zero; OCMW werkingssub JUMP 4.81m; "
                "fin debt 9.32m; cash 0.93m / liq 0.71; op PnL -0.34m"
            ),
            "priority": "9",
            "recipient_body": "Zorgbedrijf Meetjesland / OCMW Evergem / Maldegem / Deinze / Lievegem",
            "recipient_email": "info@zorgbedrijfmeetjesland.be",
            "recipient_postal": "Sleidinge-Dorp 43 9940 Evergem",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_zbm_ocmw_sub_jump_4_81m_2025",
            "linked_leaderboard_id": "lb_zbm_ocmw_sub_jump_4_81m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_path = DATA / "research_queue.csv"
tmp = rq_path.with_suffix(".csv.tmp")
found_1248 = False
has_1249 = False
with rq_path.open(encoding="utf-8", newline="") as fin, tmp.open("w", encoding="utf-8", newline="") as fout:
    r = csv.DictReader(fin)
    fields = r.fieldnames
    w = csv.DictWriter(fout, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for row in r:
        if row.get("task_id") == "rq_1248":
            found_1248 = True
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["entity_id"] = ENT
            row["title"] = "Zorgbedrijf Meetjesland dual residual JR2025 multi-muni care Entity II"
            row["instructions"] = (
                "Completed: Zorgbedrijf Meetjesland JR2025 full BBC text primary dual care"
            )
            row["blocked_gap_id"] = GAP
            row["notes"] = (
                "tick1248; KBO 0666.615.870 assets 42.5m fin debt 9.32m AFM -4.4k "
                "gecorr +1.18m OCMW sub JUMP 4.81m cash 0.93m liq 0.71; FOI ready; spawn rq_1249"
            )
        if row.get("task_id") == "rq_1249":
            has_1249 = True
        w.writerow(row)
    if not has_1249:
        w.writerow(
            {
                "task_id": "rq_1249",
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
                "notes": "spawned tick1248 after Zorgbedrijf Meetjesland dual residual; next residual dual L5 VL",
            }
        )
tmp.replace(rq_path)
print("research_queue 1248", found_1248, "spawned_1249", not has_1249)

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
            "last_unit_id": "rq_1248",
            "ticks_completed": "1248",
            "paused": "no",
            "notes": (
                "tick1248 Zorgbedrijf Meetjesland dual residual AFM -4.4k gecorr +1.18m "
                "fin debt 9.32m OCMW sub JUMP 4.81m cash 0.93m liq 0.71 op PnL -0.34m FOI ready; "
                "next rq_1249 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1248 - 2026-08-17 - rq_1248 Zorgbedrijf Meetjesland dual residual
- Unit: Zorgbedrijf Meetjesland WV JR2025 multi-muni dual care Entity II (KBO 0666.615.870; 298p text primary; members OCMW Evergem + Maldegem + Deinze + Lievegem).
- EUR strong: assets **42.5m**; fin debt **9.32m**; AFM **-4.370** thin NEG designed-to-zero; gecorr AFM **+1.177m**; budget/BBR **0**; OCMW specific werkingssub **4.805m** JUMP (was 2.308m); result-indep OCMW dots **1.386m**; cash DROP **0.925m**; liquidity **0.706**; op PnL **-0.338m**; personnel **33.208m**; new loans **66k**.
- CSVs: sources/entities/budgets+45/commitments+7/leaderboard+7 + FOI ready `gap_zbm_afm_thin_neg_4k_ocmw_sub_jump_4_81m_fin_debt_9_32m_liq_0_71_l5` (not sent); rq_1248=done; spawn rq_1249.
- Next: rq_1249 residual dual L5 VL JR2025 hole_fill.

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
print("OK ticks=1248")

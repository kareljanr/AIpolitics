# -*- coding: utf-8 -*-
"""Tick 1251 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 Welzijnszorg Kempen JR2025 Entity II dual residual (PnL NEG / OCMW 1.69m / 2026 fee hike)."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T06:30:00Z"
TICK = 1251
SRC = "src_welzijnszorg_kempen_jr2025"
ENT = "welzijnszorg_kempen"
CITY = "city_geel"
SRC_URL = "https://welzijnszorgkempen.be/wp-content/uploads/2026/07/Jaarrekening-WZK-2025.pdf"
GAP = "gap_wzk_pnl_neg_0_25m_cum_flip_0_10m_ocmw_sub_1_69m_fee_hike_2026_l5"
HIER = "Vlaanderen>Gemeenten>Geel>Welzijnszorg_Kempen"


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
            "title": "Welzijnszorg Kempen WV JR2025 BBC (99p text) dual residual",
            "url": SRC_URL,
            "publisher": "Welzijnszorg Kempen / 27 OCMW arr. Turnhout / IOK",
            "accessed_date": "2026-08-17",
            "source_class": "primary_pdf",
            "notes": (
                "tick1251; KBO 0222.947.570 Antwerpseweg 1A bus 1 2440 Geel; "
                "AD Eric Nysmans Voorzitter Michel Meeus; pub 22.07.2026; 99p text primary; "
                "assets 6.346m fin debt 0 AFM +82.031 gecorr +82.031 OCMW dual 1.693m "
                "PnL -0.251m cash 3.984m BBR 2.460m personnel 12.922m"
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
            "name_nl": "Welzijnszorg Kempen Welzijnsvereniging",
            "name_fr": "Welzijnszorg Kempen (soins/bien-etre)",
            "name_en": "Welzijnszorg Kempen welfare association (27-muni OCMW Turnhout arr.)",
            "level": "ocmw_association",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://welzijnszorgkempen.be",
            "foi_email": "wzk.communicatie@iok.be",
            "foi_postal": "Antwerpseweg 1A bus 1 2440 Geel",
            "notes": (
                "tick1251; dual residual 27 OCMW arr. Turnhout + IOK; "
                f"KBO 0222.947.570; FOI {GAP}"
            ),
        }
    ],
)
print("entities", n)

bud_rows = [
    ("bud_wzk_assets_2025", 6345745, "Assets balanstotaal YE2025 6.346m (was 6.304m)"),
    ("bud_wzk_equity_2025", 887680, "Nettoactief YE2025 0.888m DROP (was 1.139m)"),
    ("bud_wzk_debt_total_2025", 5458066, "Schulden total YE2025 5.458m all ST"),
    ("bud_wzk_fin_debt_2025", 0, "Fin schulden YE2025 EUR0 (T4 empty)"),
    ("bud_wzk_cash_2025", 3983550, "Liquide middelen YE2025 3.984m JUMP (was 3.425m)"),
    ("bud_wzk_st_recv_2025", 2040104, "Vorderingen KT total YE2025 2.040m"),
    ("bud_wzk_st_recv_nonruil_2025", 1074708, "Vorderingen KT niet-ruil YE2025 1.075m"),
    ("bud_wzk_mva_2025", 200469, "Materiele VA YE2025 0.200m"),
    ("bud_wzk_provisions_2025", 1454823, "Voorzieningen risico/kosten YE2025 1.455m"),
    ("bud_wzk_cum_pnl_2025", -102888, "Gecumuleerd tekort YE2025 -0.103m FLIP (was +0.148m)"),
    ("bud_wzk_expl_rec_2025", 17764859, "Exploitatieontvangsten 17.765m"),
    ("bud_wzk_expl_exp_2025", 17687827, "Exploitatieuitgaven 17.688m"),
    ("bud_wzk_expl_saldo_2025", 77031, "Exploitatiesaldo +77.031"),
    ("bud_wzk_invest_exp_2025", 18898, "Investeringsuitgaven 18.898"),
    ("bud_wzk_invest_saldo_2025", -18898, "Investeringssaldo -18.898"),
    ("bud_wzk_fin_saldo_2025", 5000, "Financieringssaldo +5.000 (terugvordering toegestane leningen)"),
    ("bud_wzk_budget_result_2025", 63133, "Budgettair resultaat boekjaar +63.133"),
    ("bud_wzk_bbr_2025", 2460251, "BBR +2.460m"),
    ("bud_wzk_afm_2025", 82031, "AFM +82.031 (MJP was -442.539)"),
    ("bud_wzk_gecorr_afm_2025", 82031, "Gecorrigeerde AFM +82.031"),
    ("bud_wzk_pnl_2025", -250946, "PnL tekort -0.251m FLIP (was +0.126m)"),
    ("bud_wzk_op_pnl_2025", -314638, "Operationeel PnL -0.315m NEG"),
    ("bud_wzk_personnel_2025", 12921782, "Bezoldigingen J5 12.922m / 184.02 VTE"),
    ("bud_wzk_goederen_2025", 4755502, "Goederen en diensten 4.756m"),
    ("bud_wzk_sub_total_2025", 13437112, "Werkingssubsidies total J5 13.437m"),
    ("bud_wzk_ocmw_sub_alg_2025", 1019640, "OCMW dual algemene werkingssub 1.020m DROP (was 1.232m)"),
    ("bud_wzk_ocmw_sub_spec_2025", 673305, "OCMW dual specifieke werkingssub 0.673m JUMP (was 0.205m)"),
    ("bud_wzk_ocmw_sub_total_2025", 1692945, "OCMW dual total alg+spec 1.693m"),
    ("bud_wzk_vl_sub_spec_2025", 11301623, "VL specifieke werkingssub T2 11.302m"),
    ("bud_wzk_fed_sub_spec_2025", 397017, "FED specifieke werkingssub T2 0.397m (12 VTE sociale maribel)"),
    ("bud_wzk_city_sub_spec_2025", 50006, "Gemeente specifieke werkingssub T2 50.006"),
    ("bud_wzk_other_sub_spec_2025", 28646, "Andere entiteiten specifieke werkingssub T2 28.646"),
    ("bud_wzk_werking_ontv_2025", 3360174, "Opbrengsten uit de werking 3.360m"),
    ("bud_wzk_costs_2025", 17914647, "J5 costs total 17.915m"),
    ("bud_wzk_fin_income_2025", 64345, "Financiele opbrengsten J5 64.345"),
    ("bud_wzk_t2_sub_total_2025", 13470238, "T2 werkingssubsidies cash 13.470m"),
    ("bud_wzk_new_loans_2025", 0, "Nieuwe leningen 2025 EUR0"),
    ("bud_wzk_loans_granted_open_2025", 23248, "Toegestane leningen open YE2025 23.248"),
    ("bud_wzk_overig_netto_2025", 990567, "Overig nettoactief YE2025 0.991m"),
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
        "comm_wzk_pnl_neg_0_25m_2025",
        "Welzijnszorg Kempen PnL -0.251m / op -0.315m FLIP",
        "250946",
        "Structural book loss after only 2024 profit; 2019-2023 also negative",
        "PnL vs AFM recon + 2026 fee FOI",
    ),
    (
        "comm_wzk_ocmw_sub_1_69m_2025",
        "Welzijnszorg Kempen OCMW dual alg+spec 1.693m",
        "1692945",
        "Alg 1.020m DROP (2024 extra 0.50/inh 238k not repeated) + spec 0.673m JUMP",
        "OCMW multi-year matrix FOI",
    ),
    (
        "comm_wzk_personnel_12_9m_2025",
        "Welzijnszorg Kempen personnel 12.922m / 184.02 VTE",
        "12921782",
        "Payroll +9.6% vs 11.795m; VIA eco-cheques +100/VTE; 12 VTE maribel",
        "FTE recon FOI",
    ),
    (
        "comm_wzk_afm_0_08m_vs_mjp_neg_2025",
        "Welzijnszorg Kempen AFM +82k vs MJP -443k",
        "82031",
        "AFM/gecorr +82.031 vs planned -442.539; BBR 2.460m",
        "AFM path / MJP recon FOI",
    ),
    (
        "comm_wzk_cum_flip_0_10m_2025",
        "Welzijnszorg Kempen cum P&L flip to -0.103m",
        "102888",
        "Equity drop 1.139 to 0.888m; cum +148k to -103k",
        "Solvency / member recap FOI",
    ),
    (
        "comm_wzk_fee_hike_2026",
        "Welzijnszorg Kempen 2026 member fee 1.09 to 2.08/inh",
        "1019640",
        "AV 24.09.2025 doubles general fee from 2026; 2025 without extra 0.50/inh",
        "2026 envelope + indexation FOI",
    ),
    (
        "comm_wzk_bbr_2_46m_cash_3_98m_2025",
        "Welzijnszorg Kempen BBR 2.460m cash 3.984m JUMP",
        "2460251",
        "Healthy BBR/cash vs book loss; fin debt 0; loans granted open 23k",
        "Working-capital / granted-loan FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Welzijnszorg Kempen / 27 OCMW arr. Turnhout / IOK",
            "legal_basis": "BBC JR2025 multi-muni dual welfare",
            "decision_date": "2026-07-22",
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
            "notes": f"tick{TICK}; primary Welzijnszorg Kempen JR2025",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_wzk_pnl_neg_0_25m_2025", "Welzijnszorg Kempen PnL -0.25m / op -0.31m FLIP", "250946", "8.0", "5.5", "3.0"),
    ("lb_wzk_ocmw_sub_1_69m_2025", "Welzijnszorg Kempen OCMW dual 1.69m (alg drop + spec JUMP)", "1692945", "8.0", "6.5", "3.0"),
    ("lb_wzk_personnel_12_9m_2025", "Welzijnszorg Kempen personnel 12.9m / 184 VTE dual residual", "12921782", "6.0", "7.5", "4.0"),
    ("lb_wzk_afm_0_08m_vs_mjp_neg_2025", "Welzijnszorg Kempen AFM +82k vs MJP -443k", "82031", "7.5", "5.0", "3.0"),
    ("lb_wzk_cum_flip_0_10m_2025", "Welzijnszorg Kempen cum P&L flip to -0.10m", "102888", "7.5", "5.0", "3.0"),
    ("lb_wzk_fee_hike_2026", "Welzijnszorg Kempen 2026 fee hike 1.09 to 2.08/inh", "1019640", "8.0", "6.0", "3.0"),
    ("lb_wzk_bbr_2_46m_cash_3_98m_2025", "Welzijnszorg Kempen BBR 2.46m cash 3.98m JUMP vs book loss", "2460251", "6.5", "6.0", "3.0"),
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
            "tco_notes": "Multi-muni dual welfare residual Welzijnszorg Kempen JR2025",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "27-muni Turnhout arr. residents / RolMobiel / Thuiszorg Kempen users",
            "stated_goal": "Local dual residual welfare map VL JR2025",
            "measured_outcome": "PnL -0.25m flip; cum -0.10m; OCMW 1.69m; AFM +82k vs MJP -443k; 2026 fee 1.09 to 2.08/inh; BBR 2.46m cash 3.98m",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "OCMW package + AFM/PnL/2026 fee FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary Welzijnszorg Kempen JR2025; not TE-additive without care",
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
                "OCMW dual toelage multi-year matrix alg 1.020m DROP (2024 extra 0.50/inh 238.284 not "
                "repeated) + spec 0.673m JUMP = 1.693m per 27 OCMW + IOK; AV 24.09.2025 fee hike "
                "1.09 to 2.08 EUR/inh from 2026 + indexation envelope; AFM +82.031 vs MJP -442.539 "
                "vs PnL -250.946 / op -314.638 / cum flip -102.888; T2 VL 11.302m FED 0.397m "
                "city 50k other 29k split per dienst; FTE 184.02 vs 188.10; loans granted open 23.248"
            ),
            "why_it_matters": (
                "Dual welfare residual 27-muni: PnL -0.25m flip; cum -0.10m; OCMW 1.69m; "
                "AFM +82k vs MJP -443k; 2026 fee almost doubles; BBR 2.46m cash 3.98m"
            ),
            "priority": "9",
            "recipient_body": "Welzijnszorg Kempen / 27 OCMW arr. Turnhout / IOK",
            "recipient_email": "wzk.communicatie@iok.be",
            "recipient_postal": "Antwerpseweg 1A bus 1 2440 Geel",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_wzk_pnl_neg_0_25m_2025",
            "linked_leaderboard_id": "lb_wzk_pnl_neg_0_25m_2025",
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
found_1251 = False
has_1252 = False
with rq_path.open(encoding="utf-8", newline="") as fin, tmp.open("w", encoding="utf-8", newline="") as fout:
    r = csv.DictReader(fin)
    fields = r.fieldnames
    w = csv.DictWriter(fout, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for row in r:
        if row.get("task_id") == "rq_1251":
            found_1251 = True
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["entity_id"] = ENT
            row["title"] = "Welzijnszorg Kempen dual residual JR2025 27-muni OCMW association"
            row["instructions"] = (
                "Completed: Welzijnszorg Kempen JR2025 full BBC text primary dual welfare"
            )
            row["blocked_gap_id"] = GAP
            row["notes"] = (
                "tick1251; KBO 0222.947.570 assets 6.35m fin debt 0 AFM +82k "
                "gecorr +82k OCMW dual 1.69m PnL -0.25m cash 3.98m BBR 2.46m; "
                "FOI ready; spawn rq_1252"
            )
        if row.get("task_id") == "rq_1252":
            has_1252 = True
        w.writerow(row)
    if not has_1252:
        w.writerow(
            {
                "task_id": "rq_1252",
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
                "notes": "spawned tick1251 after Welzijnszorg Kempen dual residual; next residual dual L5 VL",
            }
        )
tmp.replace(rq_path)
print("research_queue 1251", found_1251, "spawned_1252", not has_1252)

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
            "last_unit_id": "rq_1251",
            "ticks_completed": "1251",
            "paused": "no",
            "notes": (
                "tick1251 Welzijnszorg Kempen dual residual 27-muni PnL -0.25m "
                "cum flip -0.10m OCMW 1.69m AFM +82k vs MJP -443k fee hike 2026 "
                "1.09 to 2.08/inh personnel 12.92m cash 3.98m BBR 2.46m FOI ready; "
                "next rq_1252 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1251 - 2026-08-17 - rq_1251 Welzijnszorg Kempen dual residual
- Unit: Welzijnszorg Kempen WV JR2025 27-muni OCMW-vereniging Entity II (KBO 0222.947.570; 99p text primary; members 27 OCMW arr. Turnhout + IOK). Distinct from Zorggroep Orion (tick 1244, Turnhout seat care).
- EUR strong: assets **6.35m**; fin debt **0**; AFM **+82.031** (MJP **-442.539**); gecorr AFM **+82.031**; BBR **+2.460m**; OCMW dual **1.693m** (alg **1.020m** DROP + spec **0.673m** JUMP); PnL flip **-0.251m**; op PnL **-0.315m**; cum P&L flip **-0.103m**; cash JUMP **3.984m**; personnel **12.922m** / 184.02 VTE; 2026 fee hike **1.09 → 2.08/inh**.
- CSVs: sources/entities/budgets+39/commitments+7/leaderboard+7 + FOI ready `gap_wzk_pnl_neg_0_25m_cum_flip_0_10m_ocmw_sub_1_69m_fee_hike_2026_l5` (not sent); rq_1251=done; spawn rq_1252.
- Next: rq_1252 residual dual L5 VL JR2025 hole_fill.

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
print("OK ticks=1251")

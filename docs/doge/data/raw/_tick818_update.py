# -*- coding: utf-8 -*-
"""Tick 818 — KU Leuven jaarrekening 2025 residual dual FWB higher-ed."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T06:00:00Z"
ROOT = Path(__file__).resolve().parents[1]


def load_csv(name):
    p = ROOT / name
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames, p


def save_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def prio(a, c, d):
    return round((float(a) + float(c) + float(d)) / 3, 2)


# ensure entity
ent_rows, ent_fields, ent_path = load_csv("entities.csv")
if not any(e.get("entity_id") == "kuleuven" for e in ent_rows):
    ent_rows.append(
        {
            "entity_id": "kuleuven",
            "name_nl": "KU Leuven",
            "name_fr": "KU Leuven",
            "name_en": "KU Leuven",
            "level": "L2",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.kuleuven.be",
            "foi_email": "openbaarheid@vlaanderen.be",
            "foi_postal": "https://www.vlaanderen.be/openbaarheid-van-bestuur",
            "notes": "Flemish university; public funding heavy; tick818",
        }
    )
    save_csv(ent_path, ent_fields, ent_rows)
    print("entity kuleuven added")
else:
    print("entity kuleuven exists")

src_rows, src_fields, src_path = load_csv("sources.csv")
new_sources = [
    {
        "source_id": "src_kuleuven_jv2025",
        "title": "KU Leuven Jaarverslag 2025 statutory/finance narrative",
        "url": "docs/doge/data/raw/kuleuven_jv2025.pdf",
        "publisher": "KU Leuven",
        "accessed_date": "2026-08-05",
        "source_class": "entity_accounts",
        "notes": "Strong tick818 primary 167p: balance YE2025 3.4bn (+178.6m +5.6pct); equity 2.520bn; provisions 254.3m; debt 532.1m; fixed assets 856.2m current 2.530bn; destined funds 2.518bn; research spend 781.88m (749.2m 2024); LRD op revenues 419m; valorisatie 4th stream after matching 247.2m; VL gov savings net impact -31.4m 2025; mecenat 26.522m; Stuvo budget 43.780m result -10.086m costs 53.867m; Horizon Europe HES 334.2m/562 projects KU lead pillar2 139.5m/219; dual FWB higher-ed residual",
    },
    {
        "source_id": "src_dual_kuleuven_fwb_he_tick818",
        "title": "Dual KU Leuven 3.4bn balance / 782m research vs FWB higher-ed residual",
        "url": "docs/doge/data/raw/kuleuven_jv2025.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: KU Leuven public uni book dual prior FWB education personnel ~7.1bn class Entity II",
    },
]
existing = {s["source_id"] for s in src_rows}
for s in new_sources:
    if s["source_id"] not in existing:
        src_rows.append(s)
save_csv(src_path, src_fields, src_rows)
print("sources ok")

bud_rows, bud_fields, bud_path = load_csv("budgets.csv")
new_buds = [
    ("bud_kuleuven_balance_2025", "kuleuven", 2025, 3400000000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Balance total YE2025 3.4bn (+178.6m +5.6pct); tick818"),
    ("bud_kuleuven_balance_delta_2025", "kuleuven", 2025, 178600000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Balance increase 178.6m 2025; tick818"),
    ("bud_kuleuven_equity_2025", "kuleuven", 2025, 2520000000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Eigen vermogen 2.520bn YE2025 (from 2.321bn); tick818"),
    ("bud_kuleuven_destined_funds_2025", "kuleuven", 2025, 2518000000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Bestemde fondsen 2.518bn YE2025 (from 2.319bn); tick818"),
    ("bud_kuleuven_provisions_2025", "kuleuven", 2025, 254300000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Provisions 254.3m (7.5pct) YE2025 -8.2m YoY; tick818"),
    ("bud_kuleuven_debt_2025", "kuleuven", 2025, 532100000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Schulden 532.1m (15.7pct) YE2025 -4.5m; tick818"),
    ("bud_kuleuven_fixed_assets_2025", "kuleuven", 2025, 856200000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Vaste activa 856.2m +60.9m; tick818"),
    ("bud_kuleuven_current_assets_2025", "kuleuven", 2025, 2530000000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Vlottende activa 2.530bn +117.7m (geldbeleggingen); tick818"),
    ("bud_kuleuven_research_spend_2025", "kuleuven", 2025, 781880000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Onderzoeksuitgaven 781.88m 2025 (incl LRD FWO mandates); tick818"),
    ("bud_kuleuven_research_spend_2024", "kuleuven", 2024, 749200000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Research spend 749.2m 2024; tick818"),
    ("bud_kuleuven_lrd_op_rev_2025", "kuleuven", 2025, 419000000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "LRD bedrijfsopbrengsten 419m 2025 (+4m); tick818"),
    ("bud_kuleuven_valorisatie_4th_stream_2025", "kuleuven", 2025, 247200000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "4th stream valorisatie after matching 247.2m (private contract 76.8+12.6 etc); tick818"),
    ("bud_kuleuven_vl_gov_cut_impact_2025", "kuleuven", 2025, -31400000, "", "", "estimate", "src_kuleuven_jv2025", "strong", "VL government savings net impact KU Leuven 2025 -31.4m; tick818"),
    ("bud_kuleuven_mecenat_2025", "kuleuven", 2025, 26522498, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Mecenat total 26.522m (projects 7.203 funds 3.599 chairs 6.489 legacies 9.232); tick818"),
    ("bud_kuleuven_stuvo_budget_2025", "kuleuven", 2025, 43780489, "", "", "budgeted", "src_kuleuven_jv2025", "strong", "Stuvo budget 43.780m (toelagen 18.376 + other 25.404); tick818"),
    ("bud_kuleuven_stuvo_result_2025", "kuleuven", 2025, -10086323, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Stuvo result -10.086m; costs 53.867m (+60.2pct) rev 43.780m; tick818"),
    ("bud_kuleuven_stuvo_costs_2025", "kuleuven", 2025, 53866811, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Stuvo total costs 53.867m; tick818"),
    ("bud_kuleuven_horizon_pillar2_cum", "kuleuven", 2025, 139500000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "Horizon Europe pillar2 Global challenges 139.5m 219 projects KU lead HES; tick818"),
    ("bud_kuleuven_hes_horizon_total_rank", "kuleuven", 2025, 334200000, "", "", "outturn", "src_kuleuven_jv2025", "medium", "HES Horizon Europe ranking total 334.2m 562 projects (system class not all KU); tick818"),
    ("bud_kuleuven_basiskoten_new_loans_2025", "kuleuven", 2025, 11000000, "", "", "outturn", "src_kuleuven_jv2025", "strong", "New loans basiskoten +11.0m in debt mutations; tick818"),
    ("bud_dual_kuleuven_fwb_he_tick818", "gg_belgium", 2025, 3400000000, "", "", "synthesis", "src_dual_kuleuven_fwb_he_tick818", "strong", "Dual KU Leuven 3.4bn balance vs FWB HE residual; not TE-additive; tick818"),
]
existing_b = {b["budget_id"] for b in bud_rows}
for row in new_buds:
    d = dict(
        zip(
            [
                "budget_id",
                "entity_id",
                "year",
                "amount_eur",
                "amount_min_eur",
                "amount_max_eur",
                "basis",
                "source_id",
                "confidence",
                "notes",
            ],
            row,
        )
    )
    for k in ["year", "amount_eur", "amount_min_eur", "amount_max_eur"]:
        if d[k] != "" and d[k] is not None:
            d[k] = str(d[k])
    if d["budget_id"] not in existing_b:
        bud_rows.append(d)
save_csv(bud_path, bud_fields, bud_rows)
print("budgets", len(new_buds))

cmt_rows, cmt_fields, cmt_path = load_csv("commitments.csv")
new_cmts = [
    {
        "commitment_id": "cmt_kuleuven_research_782m_2025",
        "title": "KU Leuven research expenditure 781.88m 2025",
        "entity_id": "kuleuven",
        "beneficiary": "Research units / LRD / FWO mandates",
        "legal_basis": "KU Leuven jaarrekening 2025",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "781880000",
        "cash_by_year": '{"2025_m": 781.88, "2024_m": 749.2, "lrd_op_rev_m": 419, "valorisatie_m": 247.2}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kuleuven_jv2025.pdf",
        "stated_goal": "Scientific research excellence",
        "cut_option": "Publish public vs private stream split FOI; dual UGent",
        "source_id": "src_kuleuven_jv2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven>research",
        "notes": "tick818 +4.4pct YoY",
    },
    {
        "commitment_id": "cmt_kuleuven_balance_3_4bn_2025",
        "title": "KU Leuven balance sheet 3.4bn YE2025",
        "entity_id": "kuleuven",
        "beneficiary": "University operations / destined funds",
        "legal_basis": "KU Leuven jaarrekening 2025",
        "decision_date": "2025-12-31",
        "start_year": "2024",
        "end_year": "2025",
        "total_envelope_eur": "3400000000",
        "cash_by_year": '{"balance_bn": 3.4, "equity_bn": 2.52, "debt_m": 532.1, "provisions_m": 254.3, "destined_bn": 2.518}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kuleuven_jv2025.pdf",
        "stated_goal": "Solvent public research university",
        "cut_option": "Destined-fund transparency; public grant share FOI",
        "source_id": "src_kuleuven_jv2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven",
        "notes": "tick818 stock class",
    },
    {
        "commitment_id": "cmt_kuleuven_vl_cut_31_4m_2025",
        "title": "VL government savings net impact KU Leuven -31.4m 2025",
        "entity_id": "kuleuven",
        "beneficiary": "VL fiscal consolidation path",
        "legal_basis": "JV2025 narrative middelenbegroting 2024-2027",
        "decision_date": "2025-01-01",
        "start_year": "2025",
        "end_year": "2027",
        "total_envelope_eur": "31400000",
        "cash_by_year": '{"net_impact_m": -31.4}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kuleuven_jv2025.pdf",
        "stated_goal": "Absorb VL higher-ed savings",
        "cut_option": "Publish line-level cut vs workingsubsidy FOI",
        "source_id": "src_kuleuven_jv2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven>cuts",
        "notes": "tick818 negative amount is impact not spend",
    },
    {
        "commitment_id": "cmt_dual_kuleuven_fwb_he_tick818",
        "title": "Dual KU Leuven mega-book vs FWB higher-ed residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "KU Leuven JV dual prior FWB edu personnel",
        "decision_date": "2026-08-05",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "3400000000",
        "cash_by_year": '{"kul_balance_bn": 3.4, "kul_research_m": 781.88, "vl_cut_m": -31.4}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/kuleuven_jv2025.pdf",
        "stated_goal": "Dual residual map tick818",
        "cut_option": "Cross FOI public grant matrices",
        "source_id": "src_dual_kuleuven_fwb_he_tick818",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>kuleuven_fwb_he",
        "notes": "tick818 not TE-additive",
    },
]
existing_c = {c["commitment_id"] for c in cmt_rows}
for c in new_cmts:
    if c["commitment_id"] not in existing_c:
        cmt_rows.append(c)
save_csv(cmt_path, cmt_fields, cmt_rows)
print("cmt", len(new_cmts))

lb_rows, lb_fields, lb_path = load_csv("leaderboard.csv")
new_lbs = [
    {
        "item_id": "lb_kuleuven_research_782m_2025",
        "name": "KU Leuven research spend 781.88m 2025",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven>research",
        "annual_cost_eur": "781880000",
        "total_cost_eur": "0",
        "tco_notes": "Strong JV2025; mixed public/private streams; LRD 419m; climate steelman research excellence real; FOI public share",
        "confidence": "strong",
        "source_id": "src_kuleuven_jv2025",
        "beneficiaries": "research community / industry via LRD",
        "stated_goal": "Research excellence",
        "measured_outcome": "+4.4pct YoY to 781.88m",
        "absurdity_score": "3.5",
        "cost_score": "8.5",
        "difficulty": "6.0",
        "priority_index": str(prio(3.5, 8.5, 6.0)),
        "cut_proposal": "Transparent public vs private stream; no pure cut without quality metric",
        "status": "active",
        "struck_reason": "",
        "notes": "tick818 not pure waste — transparency FOI",
    },
    {
        "item_id": "lb_kuleuven_balance_3_4bn",
        "name": "KU Leuven balance sheet 3.4bn YE2025",
        "level": "L2",
        "type": "finance",
        "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven",
        "annual_cost_eur": "0",
        "total_cost_eur": "3400000000",
        "tco_notes": "Strong stock; equity 2.52bn destined funds 2.52bn; FILTER pure annual top10 stock",
        "confidence": "strong",
        "source_id": "src_kuleuven_jv2025",
        "beneficiaries": "university system",
        "stated_goal": "Solvent public research university",
        "measured_outcome": "+5.6pct balance YoY",
        "absurdity_score": "3.0",
        "cost_score": "9.0",
        "difficulty": "7.0",
        "priority_index": str(prio(3.0, 9.0, 7.0)),
        "cut_proposal": "Destined-fund public report; grant efficiency FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick818 stock",
    },
    {
        "item_id": "lb_kuleuven_stuvo_deficit_10m",
        "name": "KU Leuven Stuvo deficit 10.09m 2025 (costs +60pct)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven>stuvo",
        "annual_cost_eur": "10086323",
        "total_cost_eur": "53866811",
        "tco_notes": "Strong: costs 53.87m (+60.2pct) rev 43.78m; toelagen 18.38m; student services stress",
        "confidence": "strong",
        "source_id": "src_kuleuven_jv2025",
        "beneficiaries": "students (housing meals welfare)",
        "stated_goal": "Student services",
        "measured_outcome": "10m deficit 2025",
        "absurdity_score": "6.5",
        "cost_score": "6.0",
        "difficulty": "4.5",
        "priority_index": str(prio(6.5, 6.0, 4.5)),
        "cut_proposal": "Cost driver FOI (+60pct); housing unit economics",
        "status": "active",
        "struck_reason": "",
        "notes": "tick818 student services blowout",
    },
    {
        "item_id": "lb_kuleuven_vl_cut_31_4m",
        "name": "VL gov savings net hit KU Leuven 31.4m 2025",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven>cuts",
        "annual_cost_eur": "31400000",
        "total_cost_eur": "0",
        "tco_notes": "Strong narrative net impact -31.4m from VL savings package; dual workingsubsidy path FOI",
        "confidence": "strong",
        "source_id": "src_kuleuven_jv2025",
        "beneficiaries": "VL fiscal path",
        "stated_goal": "Contribute to VL consolidation",
        "measured_outcome": "31.4m net negative impact stated",
        "absurdity_score": "4.0",
        "cost_score": "5.5",
        "difficulty": "5.0",
        "priority_index": str(prio(4.0, 5.5, 5.0)),
        "cut_proposal": "Publish line-level allocation of cut",
        "status": "active",
        "struck_reason": "",
        "notes": "tick818 amount is cut impact not waste stock",
    },
    {
        "item_id": "lb_dual_kuleuven_fwb_he_tick818",
        "name": "Dual KU Leuven 3.4bn vs FWB higher-ed residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>kuleuven_fwb_he",
        "annual_cost_eur": "0",
        "total_cost_eur": "3400000000",
        "tco_notes": "Strong dual not TE-additive",
        "confidence": "strong",
        "source_id": "src_dual_kuleuven_fwb_he_tick818",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "4.0",
        "cost_score": "8.5",
        "difficulty": "5.5",
        "priority_index": str(prio(4.0, 8.5, 5.5)),
        "cut_proposal": "Cross FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick818",
    },
]
existing_l = {x["item_id"] for x in lb_rows}
for lb in new_lbs:
    if lb["item_id"] not in existing_l:
        lb_rows.append(lb)
save_csv(lb_path, lb_fields, lb_rows)
print("lb", [x["priority_index"] for x in new_lbs])

foi_rows, foi_fields, foi_path = load_csv("foi_queue.csv")
new_gap = {
    "gap_id": "gap_kuleuven_public_grant_matrix_l5",
    "hierarchy_path": "Vlaanderen>Onderwijs>KU_Leuven_L5",
    "entity_id": "kuleuven",
    "what_is_missing": (
        "Full statutory P&L 2025: werkingsuitkering / first-stream public grant EUR; "
        "split research spend 781.88m by public (VL/federal/EU) vs private LRD; "
        "line-level VL savings package -31.4m; Stuvo cost drivers +60.2pct; "
        "destined funds 2.518bn composition; basiskoten loan schedule +11m"
    ),
    "why_it_matters": (
        "3.4bn public university balance and 782m research without clear public-euro matrix "
        "blocks dual Entity II HE compare and waste ranking"
    ),
    "priority": "7",
    "recipient_body": "KU Leuven / Departement Onderwijs en Vorming / Vlaams Parlement",
    "recipient_email": "openbaarheid@vlaanderen.be",
    "recipient_postal": "https://www.vlaanderen.be/openbaarheid-van-bestuur",
    "draft_letter_path": "docs/doge/foi/drafts/gap_kuleuven_public_grant_matrix_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_kuleuven_research_782m_2025|cmt_kuleuven_balance_3_4bn_2025|cmt_kuleuven_vl_cut_31_4m_2025",
    "linked_leaderboard_id": "lb_kuleuven_research_782m_2025|lb_kuleuven_stuvo_deficit_10m|lb_kuleuven_balance_3_4bn",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick818 primary JV2025; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_kuleuven_public_grant_matrix_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi ok")

rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_809":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick818 KU Leuven JV2025 balance 3.4bn research 781.88m LRD 419m VL cut -31.4m "
            "Stuvo -10.1m dual FWB HE; FOI gap_kuleuven_public_grant_matrix_l5 ready"
        )
if not any(x.get("task_id") == "rq_810" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_810",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, "
                "UGent dual if public); prefer FOI-adjacent L5; skip rq_116; KU Leuven JV filled tick818; "
                "progress@820 due in 2 ticks — prepare for coverage refresh"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick818 after KU Leuven JV dual; progress@820 soon",
        }
    )
save_csv(rq_path, rq_fields, rq_rows)
print("rq ok")

ls_rows, ls_fields, ls_path = load_csv("loop_state.csv")
ls_rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": utc,
    "last_unit_id": "rq_809",
    "ticks_completed": "818",
    "paused": "no",
    "notes": (
        "tick818 KU Leuven 3.4bn/782m research VL cut-31.4 Stuvo-10 dual FWB FOI; "
        "next rq_810 residual dual L5; progress@820 in 2; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 818 OK")

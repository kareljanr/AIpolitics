# -*- coding: utf-8 -*-
"""Tick 817 — WAL ExpGen BI2026 Table II/III/IV L5 residual dual FWB cabinets."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T05:30:00Z"
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


# amounts in ExpGen tables are kEUR -> convert to EUR
src_rows, src_fields, src_path = load_csv("sources.csv")
new_sources = [
    {
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "title": "Wallonie ExpGen BI2026 Table II CE / III CL / IV encours L5 residual",
        "url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "publisher": "SPW Finances",
        "accessed_date": "2026-08-05",
        "source_class": "budget",
        "notes": "Strong tick817 residual: TableII CE 2026ini cabinets 28043k tourisme 65632k commerce ext 76843k CWaPE 9259k DO09 211195k DO01 87404k; CE total 21176400k CL 21335748k diff -159348k; encours eng 6832697k at 11.11.2025 (7075721k YE2024); debt-garanties prog ~1317m CE; spending review postal ~7.5m TVAC/yr SOWAER SPAQuE SOFICO AVIQ; dual FWB cabinets prior 16.8m",
    },
    {
        "source_id": "src_dual_wal_fwb_cabinets_tick817",
        "title": "Dual WAL cabinets 28.043m vs FWB cabinets residual tick817",
        "url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: WAL DO02 cabinets 28.043m CE BI2026 dual prior FWB cabinets ~16.8m CoA aju",
    },
]
existing = {s["source_id"] for s in src_rows}
for s in new_sources:
    if s["source_id"] not in existing:
        src_rows.append(s)
save_csv(src_path, src_fields, src_rows)
print("sources ok")

bud_rows, bud_fields, bud_path = load_csv("budgets.csv")
# values already in EUR after *1000
new_buds = [
    ("bud_wal_ce_total_bi2026", "wallonie_gov", 2026, 21176400000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "TableII/III note CE total 21176400 kEUR BI2026; tick817"),
    ("bud_wal_cl_total_bi2026", "wallonie_gov", 2026, 21335748000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "CL total 21335748 kEUR matches depenses BI2026; tick817"),
    ("bud_wal_ce_cl_diff_bi2026", "wallonie_gov", 2026, -159348000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "CE-CL differential -159.348m (liquidations honor past eng); tick817"),
    ("bud_wal_cabinets_ce_bi2026", "wallonie_gov", 2026, 28043000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "DO02 cabinets subsistence CE BI2026ini 28043 kEUR; tick817"),
    ("bud_wal_parlement_ce_bi2026", "wallonie_gov", 2026, 76254000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "Parlement wallon dotation CE 76254 kEUR; tick817"),
    ("bud_wal_mediateur_ce_bi2026", "wallonie_gov", 2026, 1891000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "Mediateur RW CE 1891 kEUR; tick817"),
    ("bud_wal_cwape_ce_bi2026", "wallonie_gov", 2026, 9259000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "NEW CWaPE dotation CE 9259 kEUR 2026; tick817"),
    ("bud_wal_do01_ce_bi2026", "wallonie_gov", 2026, 87404000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "DO01 total CE 87404 kEUR (parlement+mediateur+CWaPE); tick817"),
    ("bud_wal_tourisme_ce_bi2026", "wallonie_gov", 2026, 65632000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "Programme 09.018 Tourisme CE 65632 kEUR BI2026ini; tick817"),
    ("bud_wal_commerce_ext_ce_bi2026", "wallonie_gov", 2026, 76843000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "09.020 Commerce exterieur et investisseurs CE 76843 kEUR; tick817"),
    ("bud_wal_relations_ext_ce_bi2026", "wallonie_gov", 2026, 30098000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "09.019 Relations exterieures CE 30098 kEUR; tick817"),
    ("bud_wal_do09_ce_bi2026", "wallonie_gov", 2026, 211195000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "DO09 total CE 211195 kEUR (gov services non-DO); tick817"),
    ("bud_wal_cese_ce_bi2026", "wallonie_gov", 2026, 7858000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "CESE Wallonie CE 7858 kEUR; tick817"),
    ("bud_wal_iweps_ce_bi2026", "wallonie_gov", 2026, 7727000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "IWEPS CE 7727 kEUR; tick817"),
    ("bud_wal_ceseffb_ce_bi2026", "wallonie_gov", 2026, 8889000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "CeSEFFB new/modified CE 8889 kEUR; tick817"),
    ("bud_wal_e_wbs_ce_bi2026", "wallonie_gov", 2026, 1250000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "e-Wallonie-Bruxelles-Simplification CE 1250 kEUR (down from ~4.5m 2025); tick817"),
    ("bud_wal_presidence_chanc_ce_bi2026", "wallonie_gov", 2026, 11833000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "10.023 Presidence et Chancellerie CE 11833 kEUR; tick817"),
    ("bud_wal_dev_durable_ce_bi2026", "wallonie_gov", 2026, 13255000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "10.085 Developpement durable CE 13255 kEUR; tick817"),
    ("bud_wal_prw_frr_ce_bi2026", "wallonie_gov", 2026, 41000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "10.122 PRW+FRR CE collapsed to 41 kEUR 2026ini (from 713.5m 2025ini); tick817"),
    ("bud_wal_debt_garanties_ce_bi2026", "wallonie_debt", 2026, 1317296000, "", "", "budgeted", "src_wal_expgen_bi2026_l5_tables", "strong", "19.036 Dettes et garanties CE ~1317.296m class (TableII); dual interest 1102m; tick817"),
    ("bud_wal_encours_eng_20251111", "wallonie_gov", 2025, 6832697000, "", "", "outturn", "src_wal_expgen_bi2026_l5_tables", "strong", "Encours engagements 6832.697m at 11.11.2025 TableIV; tick817"),
    ("bud_wal_encours_eng_2024", "wallonie_gov", 2024, 7075721000, "", "", "outturn", "src_wal_expgen_bi2026_l5_tables", "strong", "Encours engagements YE2024 7075.721m; tick817"),
    ("bud_wal_encours_eng_2023", "wallonie_gov", 2023, 6839625000, "", "", "outturn", "src_wal_expgen_bi2026_l5_tables", "strong", "Encours engagements YE2023 6839.625m; tick817"),
    ("bud_wal_postal_market_review_class", "wallonie_gov", 2026, 7500000, "", "", "estimate", "src_wal_expgen_bi2026_l5_tables", "medium", "Spending review: SPW postal market ~7.5m TVAC/yr; tick817"),
    ("bud_wal_tourisme_encours_202511", "wallonie_gov", 2025, 18828000, "", "", "outturn", "src_wal_expgen_bi2026_l5_tables", "strong", "Tourisme encours eng 18828 kEUR at 11.11.2025; tick817"),
    ("bud_dual_wal_cabinets_tick817", "gg_belgium", 2026, 28043000, "", "", "synthesis", "src_dual_wal_fwb_cabinets_tick817", "strong", "Dual WAL cabinets 28.043m vs FWB residual; not TE-additive; tick817"),
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
        "commitment_id": "cmt_wal_cabinets_28m_bi2026",
        "title": "WAL ministerial cabinets CE 28.043m BI2026",
        "entity_id": "wallonie_gov",
        "beneficiary": "Ministerial cabinets",
        "legal_basis": "ExpGen Table II DO02 BI2026",
        "decision_date": "2025-10-20",
        "start_year": "2026",
        "end_year": "2026",
        "total_envelope_eur": "28043000",
        "cash_by_year": '{"ce_k": 28043, "cl_k": 28043}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "stated_goal": "Cabinet subsistence",
        "cut_option": "Publish FTE+grade; dual FWB cabinets compare",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Cabinets",
        "notes": "tick817 dual FWB ~16.8m prior",
    },
    {
        "commitment_id": "cmt_wal_tourisme_65_6m_bi2026",
        "title": "WAL Tourisme programme CE 65.632m BI2026",
        "entity_id": "wallonie_gov",
        "beneficiary": "Tourism sector / VisitWallonia class",
        "legal_basis": "Programme 09.018 ExpGen",
        "decision_date": "2025-10-20",
        "start_year": "2026",
        "end_year": "2026",
        "total_envelope_eur": "65632000",
        "cash_by_year": '{"ce_k": 65632, "encours_202511_k": 18828}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "stated_goal": "Tourism policy and subsidies",
        "cut_option": "Named L5 beneficiaries FOI",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Tourisme",
        "notes": "tick817 discretionary L5 class",
    },
    {
        "commitment_id": "cmt_wal_encours_eng_6_83bn_202511",
        "title": "WAL encours engagements 6.833bn at 11 Nov 2025",
        "entity_id": "wallonie_gov",
        "beneficiary": "Contractors and subsidy recipients",
        "legal_basis": "ExpGen Table IV",
        "decision_date": "2025-11-11",
        "start_year": "2023",
        "end_year": "2030",
        "total_envelope_eur": "6832697000",
        "cash_by_year": '{"ye2023_m": 6839.6, "ye2024_m": 7075.7, "202511_m": 6832.7}',
        "remaining_eur": "6832697000",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "stated_goal": "Honor contracted markets and subsidies",
        "cut_option": "Publish aging of encours by DO; stop new eng if CL>CE structural",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Budget>encours",
        "notes": "tick817 potential debt off-balance class",
    },
    {
        "commitment_id": "cmt_dual_wal_fwb_cabinets_tick817",
        "title": "Dual WAL cabinets 28m vs FWB cabinets residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "ExpGen dual prior FWB CoA aju cabinets",
        "decision_date": "2026-08-05",
        "start_year": "2026",
        "end_year": "2026",
        "total_envelope_eur": "28043000",
        "cash_by_year": '{"wal_m": 28.043, "fwb_class_m": 16.8}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "stated_goal": "Dual residual map tick817",
        "cut_option": "Cross FOI cabinet FTE",
        "source_id": "src_dual_wal_fwb_cabinets_tick817",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>wal_fwb_cabinets",
        "notes": "tick817 not TE-additive",
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
        "item_id": "lb_wal_cabinets_28m_bi2026",
        "name": "WAL ministerial cabinets 28.043m CE BI2026",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Wallonie>Cabinets",
        "annual_cost_eur": "28043000",
        "total_cost_eur": "0",
        "tco_notes": "Strong TableII; dual FWB cabinets ~16.8m; pure annual discretionary overhead",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "beneficiaries": "ministerial staff",
        "stated_goal": "Cabinet support",
        "measured_outcome": "Flat vs 2025 ~28m",
        "absurdity_score": "6.0",
        "cost_score": "6.0",
        "difficulty": "4.0",
        "priority_index": str(prio(6.0, 6.0, 4.0)),
        "cut_proposal": "Publish FTE matrix; cap dual Entity II total",
        "status": "active",
        "struck_reason": "",
        "notes": "tick817",
    },
    {
        "item_id": "lb_wal_tourisme_65_6m_bi2026",
        "name": "WAL Tourisme programme 65.632m CE BI2026",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Wallonie>Tourisme",
        "annual_cost_eur": "65632000",
        "total_cost_eur": "0",
        "tco_notes": "Strong 09.018; encours 18.8m Nov2025; L5 beneficiaries FOI",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "beneficiaries": "tourism operators / VisitWallonia class",
        "stated_goal": "Tourism promotion",
        "measured_outcome": "Programme total only",
        "absurdity_score": "5.5",
        "cost_score": "7.0",
        "difficulty": "4.5",
        "priority_index": str(prio(5.5, 7.0, 4.5)),
        "cut_proposal": "Named top20 FOI; outcome KPI or cut",
        "status": "active",
        "struck_reason": "",
        "notes": "tick817",
    },
    {
        "item_id": "lb_wal_commerce_ext_76_8m_bi2026",
        "name": "WAL commerce exterieur / investisseurs 76.843m CE BI2026",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Wallonie>Economie>commerce_ext",
        "annual_cost_eur": "76843000",
        "total_cost_eur": "0",
        "tco_notes": "Strong 09.020; dual AWEX/export residual; FOI named grants",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "beneficiaries": "export promotion / investors",
        "stated_goal": "Attract investment and exports",
        "measured_outcome": "Programme total only",
        "absurdity_score": "5.5",
        "cost_score": "7.5",
        "difficulty": "5.0",
        "priority_index": str(prio(5.5, 7.5, 5.0)),
        "cut_proposal": "Publish firm-level awards FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick817",
    },
    {
        "item_id": "lb_wal_encours_eng_6_83bn",
        "name": "WAL encours engagements stock 6.83bn (Nov2025)",
        "level": "L2",
        "type": "finance",
        "hierarchy_path": "Wallonie>Budget>encours",
        "annual_cost_eur": "0",
        "total_cost_eur": "6832697000",
        "tco_notes": "Strong TableIV; potential future cash; CE-CL negative means liquidating past; FILTER pure annual stock",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "beneficiaries": "past contractors/subsidy recipients",
        "stated_goal": "Honor commitments",
        "measured_outcome": "Stock down slightly vs YE2024 7.08bn",
        "absurdity_score": "5.0",
        "cost_score": "9.0",
        "difficulty": "6.5",
        "priority_index": str(prio(5.0, 9.0, 6.5)),
        "cut_proposal": "Aging report public; no new eng without CL capacity",
        "status": "active",
        "struck_reason": "",
        "notes": "tick817 stock class",
    },
    {
        "item_id": "lb_wal_prw_frr_collapse_2026",
        "name": "WAL PRW/FRR CE collapse to 41k in BI2026 (from 713.5m 2025)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Wallonie>Relance>PRW_FRR",
        "annual_cost_eur": "41000",
        "total_cost_eur": "0",
        "tco_notes": "Strong TableII path: 2025ini 713.5m -> 2026ini 41k; residual cash via CL/encours FOI; not savings claim without CL path",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026_l5_tables",
        "beneficiaries": "RRF/PRW projects residual",
        "stated_goal": "Phase out new PRW/FRR eng",
        "measured_outcome": "Near-zero new CE",
        "absurdity_score": "4.0",
        "cost_score": "3.0",
        "difficulty": "3.0",
        "priority_index": str(prio(4.0, 3.0, 3.0)),
        "cut_proposal": "Publish residual CL for open RRF projects",
        "status": "active",
        "struck_reason": "",
        "notes": "tick817 path note",
    },
    {
        "item_id": "lb_dual_wal_fwb_cabinets_tick817",
        "name": "Dual WAL cabinets 28m vs FWB cabinets residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>wal_fwb_cabinets",
        "annual_cost_eur": "28043000",
        "total_cost_eur": "0",
        "tco_notes": "Strong dual not TE-additive",
        "confidence": "strong",
        "source_id": "src_dual_wal_fwb_cabinets_tick817",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "5.5",
        "cost_score": "6.0",
        "difficulty": "4.0",
        "priority_index": str(prio(5.5, 6.0, 4.0)),
        "cut_proposal": "Cross FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick817",
    },
]
existing_l = {x["item_id"] for x in lb_rows}
for lb in new_lbs:
    if lb["item_id"] not in existing_l:
        lb_rows.append(lb)
save_csv(lb_path, lb_fields, lb_rows)
print("lb", [x["priority_index"] for x in new_lbs])

foi_rows, foi_fields, foi_path = load_csv("foi_queue.csv")
# update existing gap with L5 table fills
for row in foi_rows:
    if row.get("gap_id") == "gap_wal_bi2026_l5_matrix":
        row["notes"] = (row.get("notes") or "") + (
            " | tick817 TableII filled cabinets 28.043m tourisme 65.6m commerce 76.8m encours 6.83bn; "
            "residual still FOREM split AVIQ SOFICO named L5 + DO matrix full"
        )
        row["updated_utc"] = utc
        row["linked_commitment_id"] = (row.get("linked_commitment_id") or "") + (
            "|cmt_wal_cabinets_28m_bi2026|cmt_wal_tourisme_65_6m_bi2026|cmt_wal_encours_eng_6_83bn_202511"
        )
        row["linked_leaderboard_id"] = (row.get("linked_leaderboard_id") or "") + (
            "|lb_wal_cabinets_28m_bi2026|lb_wal_tourisme_65_6m_bi2026|lb_wal_encours_eng_6_83bn"
        )

new_gap = {
    "gap_id": "gap_wal_forem_aviq_sofico_l5",
    "hierarchy_path": "Wallonie>Emploi_Sante_Infra>L5",
    "entity_id": "wallonie_gov",
    "what_is_missing": (
        "BI2026 CE/CL split for FOREM programmes 18.102-18.130 titres-services reductions formation; "
        "AVIQ financing model review outputs and EUR; SOFICO SPAQuE SOWAER procurement review baselines; "
        "postal market 7.5m contract detail; full DO17 socio-sante CE totals; "
        "named tourism and commerce-exterieur top beneficiaries under 65.6m/76.8m"
    ),
    "why_it_matters": "Largest residual L5 opacity after tick817 DO01/02/09 fill; employment and health mega-programmes",
    "priority": "8",
    "recipient_body": "SPW Finances / FOREm / AViQ / SOFICO / ministre Emploi et Sante",
    "recipient_email": "",
    "recipient_postal": "https://www.wallonie.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_wal_forem_aviq_sofico_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_wal_tourisme_65_6m_bi2026|cmt_wal_encours_eng_6_83bn_202511",
    "linked_leaderboard_id": "lb_wal_tourisme_65_6m_bi2026|lb_wal_commerce_ext_76_8m_bi2026",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick817 residual after TableII DO01-10 sample; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_wal_forem_aviq_sofico_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi ok")

rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_808":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick817 WAL ExpGen L5: cabinets 28.043m tourisme 65.6m commerce 76.8m encours 6.83bn "
            "CE-CL -159m dual FWB cabinets; FOI gap_wal_forem_aviq_sofico_l5 ready"
        )
if not any(x.get("task_id") == "rq_809" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_809",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, "
                "WAL FOREM/AVIQ if public PDF); prefer FOI-adjacent L5; skip rq_116; "
                "WAL ExpGen DO01-10 L5 filled tick817"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick817 after WAL ExpGen L5 tables dual",
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
    "last_unit_id": "rq_808",
    "ticks_completed": "817",
    "paused": "no",
    "notes": (
        "tick817 WAL L5 cabinets28 tourisme66 commerce77 encours6.83bn dual FWB FOI; "
        "next rq_809 residual dual L5/local; progress@820 in 3; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 817 OK")

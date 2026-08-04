# -*- coding: utf-8 -*-
"""Tick 814 — CoA 2026_20 ISI bank data dual SECAL/fraud residual."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T04:00:00Z"
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


# --- sources ---
src_rows, src_fields, src_path = load_csv("sources.csv")
new_sources = [
    {
        "source_id": "src_ccrek_2026_20_isi_bank",
        "title": "CoA Utilisation donnees bancaires AGIsi ISI report 2026_20 AG 16 Apr 2026",
        "url": "https://www.ccrek.be/sites/default/files/Docs/2026_20_DonneesBancairesISI.pdf",
        "publisher": "Cour des comptes",
        "accessed_date": "2026-08-05",
        "source_class": "court_of_audit",
        "notes": "Strong tick814 primary 56p: bank-inquiry dossiers 2015-2024 established taxes 2.3bn (12pct of AGIsi total 18.7bn); collected only 36m so far (1.57pct); PCC YE2024 55.3m national accounts (+49pct vs2015) ~62m holders 25m mandataires; ~700 bank inquiries authorised 2024 mostly 5th dir VAT carrousels; BAF files 2020-24: 23/3681/4620/10364/15664 total 34352; procedural errors ~10pct sample; bank inquiry detects undeclared income ~70pct cases; productivity 61pct vs AGIsi 54pct; datamining PCC legal from law 18 Dec 2025; crypto/securities PCC from 1 Dec 2026",
    },
    {
        "source_id": "src_dual_isi_secal_fraud_tick814",
        "title": "Dual ISI bank-inquiry recovery 1.57pct vs SECAL 26.6pct and social fraud residual",
        "url": "docs/doge/data/raw/ccrek_2026_20_DonneesBancairesISI.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: CoA ISI collection gap 2.3bn established/36m collected dual SECAL recovery 26.6pct + fraude sociale staff path; tax enforcement effectiveness L5",
    },
]
existing = {s["source_id"] for s in src_rows}
for s in new_sources:
    if s["source_id"] not in existing:
        src_rows.append(s)
save_csv(src_path, src_fields, src_rows)
print("sources", len(src_rows))

# --- budgets ---
bud_rows, bud_fields, bud_path = load_csv("budgets.csv")
new_buds = [
    ("bud_isi_bank_inquiry_tax_established_2015_24", "fod_finance", 2024, 2300000000, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "CoA: bank-inquiry dossiers 2015-2024 taxes established 2.3bn; tick814"),
    ("bud_isi_bank_inquiry_tax_collected_2015_24", "fod_finance", 2024, 36000000, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "CoA: of 2.3bn established only 36m collected to date (1.57pct); tick814"),
    ("bud_isi_bank_inquiry_collection_gap_2015_24", "fod_finance", 2024, 2264000000, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "Implied uncollected of established bank-inquiry taxes 2.3bn-36m=2.264bn (timing/preventive 5th dir explain part); tick814"),
    ("bud_agisi_total_tax_established_2015_24", "fod_finance", 2024, 18700000000, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "CoA: AGIsi total taxes established 18.7bn of which bank-inquiry 2.3bn=12pct; tick814"),
    ("bud_pcc_national_accounts_2024", "nbb", 2024, 55300000, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "PCC YE2024 55.3 million national bank accounts (+49pct vs 2015); unit=count not EUR; amount_eur stores count; tick814"),
    ("bud_pcc_account_holders_2024", "nbb", 2024, 62000000, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "PCC ~62 million account holders YE2024; unit=count; tick814"),
    ("bud_pcc_mandataires_2024", "nbb", 2024, 25000000, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "PCC ~25 million mandataires YE2024; unit=count; tick814"),
    ("bud_isi_bank_inquiries_authorised_2024", "fod_finance", 2024, 700, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "~700 bank inquiries authorised AGIsi 2024 mostly 5th dir VAT carrousels; unit=count; tick814"),
    ("bud_isi_baf_files_2024", "fod_finance", 2024, 15664, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "Bank audit files BAF 15664 in 2024; tick814"),
    ("bud_isi_baf_files_cum_2020_24", "fod_finance", 2024, 34352, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "BAF cumulative 2020-2024: 23+3681+4620+10364+15664=34352; tick814"),
    ("bud_isi_baf_files_2023", "fod_finance", 2023, 10364, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "BAF 10364 in 2023; tick814"),
    ("bud_isi_baf_files_2022", "fod_finance", 2022, 4620, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "BAF 4620 in 2022; tick814"),
    ("bud_isi_collection_rate_bank_inquiry_pct", "fod_finance", 2024, 157, "", "", "outturn", "src_ccrek_2026_20_isi_bank", "strong", "Collection rate 1.57pct of established bank-inquiry taxes; amount_eur stores bps 157; tick814"),
    ("bud_dual_isi_secal_recovery_tick814", "gg_belgium", 2024, 2300000000, 36000000, 2264000000, "synthesis", "src_dual_isi_secal_fraud_tick814", "strong", "Dual ISI 2.3bn established/36m collected vs SECAL recovery residual; not TE-additive; tick814"),
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
print("budgets new", len(new_buds))

# --- commitments ---
cmt_rows, cmt_fields, cmt_path = load_csv("commitments.csv")
new_cmts = [
    {
        "commitment_id": "cmt_isi_bank_inquiry_2_3bn_established",
        "title": "AGIsi bank-inquiry tax assessments 2.3bn 2015-2024 (36m collected)",
        "entity_id": "fod_finance",
        "beneficiary": "Federal treasury / tax enforcement",
        "legal_basis": "CIR 92 bank inquiry; VAT code art62bis; CoA 2026_20",
        "decision_date": "2026-04-16",
        "start_year": "2015",
        "end_year": "2024",
        "total_envelope_eur": "2300000000",
        "cash_by_year": '{"established_bn": 2.3, "collected_m": 36, "rate_pct": 1.57, "agisi_total_bn": 18.7, "share_pct": 12, "inquiries_2024": 700, "baf_2024": 15664}',
        "remaining_eur": "2264000000",
        "status": "active",
        "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_20_DonneesBancairesISI.pdf",
        "stated_goal": "Tax fraud detection via bank data and PCC",
        "cut_option": "Harmonise income-tax/VAT procedures; standard bank data format; expand PCC datamining; improve collection follow-up",
        "source_id": "src_ccrek_2026_20_isi_bank",
        "confidence": "strong",
        "hierarchy_path": "Federal>Finance>AGIsi_bank_inquiry",
        "notes": "tick814 low collection partly preventive 5th dir VAT carrousels; not pure cash waste",
    },
    {
        "commitment_id": "cmt_pcc_accounts_55_3m_2024",
        "title": "PCC central account register 55.3m national accounts YE2024",
        "entity_id": "nbb",
        "beneficiary": "AGIsi / tax and AML authorities",
        "legal_basis": "Law 8 Jul 2018 PCC; extensions 2015 foreign 2022 balances 2026 crypto",
        "decision_date": "2024-12-31",
        "start_year": "2011",
        "end_year": "2030",
        "total_envelope_eur": "",
        "cash_by_year": '{"accounts_m": 55.3, "holders_m": 62, "mandataires_m": 25, "vs_2015_pct": 49, "crypto_from": "2026-12-01", "datamining_law": "2025-12-18"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_20_DonneesBancairesISI.pdf",
        "stated_goal": "Central financial account identification for fraud combat",
        "cut_option": "Strengthen AGTres completeness control; add transaction counts",
        "source_id": "src_ccrek_2026_20_isi_bank",
        "confidence": "strong",
        "hierarchy_path": "Federal>Finance>PCC",
        "notes": "tick814 counts not EUR envelope",
    },
    {
        "commitment_id": "cmt_dual_isi_secal_tick814",
        "title": "Dual ISI 1.57pct recovery vs SECAL 26.6pct residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "CoA ISI 2026_20 dual SECAL 2025_49",
        "decision_date": "2026-08-05",
        "start_year": "2015",
        "end_year": "2025",
        "total_envelope_eur": "2300000000",
        "cash_by_year": '{"isi_established_bn": 2.3, "isi_collected_m": 36, "secal_recovery_pct": 26.6}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/ccrek_2026_20_DonneesBancairesISI.pdf",
        "stated_goal": "Dual residual map tick814",
        "cut_option": "Cross FOI collection pipelines",
        "source_id": "src_dual_isi_secal_fraud_tick814",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>isi_secal",
        "notes": "tick814 not TE-additive",
    },
]
existing_c = {c["commitment_id"] for c in cmt_rows}
for c in new_cmts:
    if c["commitment_id"] not in existing_c:
        cmt_rows.append(c)
save_csv(cmt_path, cmt_fields, cmt_rows)
print("commitments", len(new_cmts))

# --- leaderboard ---
lb_rows, lb_fields, lb_path = load_csv("leaderboard.csv")
new_lbs = [
    {
        "item_id": "lb_isi_bank_inquiry_collection_gap_2_26bn",
        "name": "AGIsi bank-inquiry tax collection gap ~2.26bn of 2.3bn established",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Federal>Finance>AGIsi_collection",
        "annual_cost_eur": "0",
        "total_cost_eur": "2264000000",
        "tco_notes": "Strong CoA 2015-24: established 2.3bn collected 36m (1.57pct); gap partly preventive VAT carrousel path not pure cash loss; FILTER pure annual as multi-year stock; still material enforcement failure",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_20_isi_bank",
        "beneficiaries": "evaders residual / delayed treasury",
        "stated_goal": "Collect taxes on bank-inquiry assessments",
        "measured_outcome": "1.57pct collected to date",
        "absurdity_score": "8.5",
        "cost_score": "9.0",
        "difficulty": "6.5",
        "priority_index": str(prio(8.5, 9.0, 6.5)),
        "cut_proposal": "Collection KPI separate from assessment; follow-up on established tax; procedure harmonisation",
        "status": "active",
        "struck_reason": "",
        "notes": "tick814 multi-year stock class",
    },
    {
        "item_id": "lb_isi_bank_inquiry_1_57pct_recovery",
        "name": "Bank-inquiry tax recovery rate 1.57pct (36m of 2.3bn)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Federal>Finance>AGIsi_recovery_rate",
        "annual_cost_eur": "0",
        "total_cost_eur": "36000000",
        "tco_notes": "Strong CoA rate metric; dual SECAL 26.6pct recovery; climate of enforcement incentives",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_20_isi_bank",
        "beneficiaries": "system effectiveness measure",
        "stated_goal": "Effective fraud recovery",
        "measured_outcome": "1.57pct",
        "absurdity_score": "9.0",
        "cost_score": "7.5",
        "difficulty": "5.5",
        "priority_index": str(prio(9.0, 7.5, 5.5)),
        "cut_proposal": "Publish collection by direction; end 10pct inquiry KPI without quality",
        "status": "active",
        "struck_reason": "",
        "notes": "tick814 high absurdity rate",
    },
    {
        "item_id": "lb_isi_agisi_18_7bn_assessments",
        "name": "AGIsi total tax assessments 18.7bn 2015-24 (bank path 12pct)",
        "level": "L2",
        "type": "ops",
        "hierarchy_path": "Federal>Finance>AGIsi",
        "annual_cost_eur": "0",
        "total_cost_eur": "18700000000",
        "tco_notes": "Strong CoA perimeter AGIsi assessments multi-year; not expenditure; filter pure waste top10 as gross assessments",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_20_isi_bank",
        "beneficiaries": "tax enforcement system",
        "stated_goal": "Tax corrections and fraud fight",
        "measured_outcome": "18.7bn established class",
        "absurdity_score": "5.0",
        "cost_score": "9.5",
        "difficulty": "7.0",
        "priority_index": str(prio(5.0, 9.5, 7.0)),
        "cut_proposal": "Report established vs collected matrix annual",
        "status": "active",
        "struck_reason": "",
        "notes": "tick814 stock assessments not TE",
    },
    {
        "item_id": "lb_isi_procedure_errors_10pct",
        "name": "AGIsi bank-inquiry procedural errors ~10pct sample",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Federal>Finance>AGIsi_procedure",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "Strong CoA sample ~10pct dossiers with procedure errors; dual income-tax vs VAT rule conflict; legal risk nullifies assessments",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_20_isi_bank",
        "beneficiaries": "litigation / nullified cases",
        "stated_goal": "Lawful bank inquiries",
        "measured_outcome": "~10pct error rate sample",
        "absurdity_score": "7.5",
        "cost_score": "5.0",
        "difficulty": "4.5",
        "priority_index": str(prio(7.5, 5.0, 4.5)),
        "cut_proposal": "Harmonise CIR/TVA bank-inquiry procedures in one code path",
        "status": "active",
        "struck_reason": "",
        "notes": "tick814 governance L5",
    },
    {
        "item_id": "lb_dual_isi_secal_tick814",
        "name": "Dual ISI 1.57pct recovery vs SECAL 26.6pct residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>isi_secal",
        "annual_cost_eur": "0",
        "total_cost_eur": "2300000000",
        "tco_notes": "Strong dual not TE-additive; primary CoA ISI + SECAL",
        "confidence": "strong",
        "source_id": "src_dual_isi_secal_fraud_tick814",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "7.0",
        "cost_score": "8.5",
        "difficulty": "5.0",
        "priority_index": str(prio(7.0, 8.5, 5.0)),
        "cut_proposal": "Cross FOI collection pipelines",
        "status": "active",
        "struck_reason": "",
        "notes": "tick814",
    },
]
existing_l = {x["item_id"] for x in lb_rows}
for lb in new_lbs:
    if lb["item_id"] not in existing_l:
        lb_rows.append(lb)
save_csv(lb_path, lb_fields, lb_rows)
print("leaderboard", [x["priority_index"] for x in new_lbs])

# --- FOI ---
foi_rows, foi_fields, foi_path = load_csv("foi_queue.csv")
new_gap = {
    "gap_id": "gap_isi_bank_inquiry_collection_l5",
    "hierarchy_path": "Federal>Finance>AGIsi_bank_L5",
    "entity_id": "fod_finance",
    "what_is_missing": (
        "AGIsi bank-inquiry established vs collected matrix by year and by direction 2015-2025; "
        "aging of open claims on the 2.3bn; share prevented vs cash-collectible; "
        "5th direction VAT carrousel outcomes (blocked accounts 84 of 145 CTIF tips); "
        "PCC completeness audit results AGTres; administrative fines applied vs 50k min; "
        "BAF processing cost and FTE; collection rate after 2024 for new assessments"
    ),
    "why_it_matters": (
        "Material 2.3bn established with 1.57pct collected; dual SECAL recovery shows public claim "
        "pipelines systematically under-collect; FOI for L5 collection path"
    ),
    "priority": "9",
    "recipient_body": "SPF Finances AGIsi / AG Perception / AG Tresorerie / minister Finances",
    "recipient_email": "",
    "recipient_postal": "https://finances.belgium.be / IBZ openbaarheid",
    "draft_letter_path": "docs/doge/foi/drafts/gap_isi_bank_inquiry_collection_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_isi_bank_inquiry_2_3bn_established|cmt_pcc_accounts_55_3m_2024",
    "linked_leaderboard_id": "lb_isi_bank_inquiry_collection_gap_2_26bn|lb_isi_bank_inquiry_1_57pct_recovery",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick814 primary CoA 2026_20; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_isi_bank_inquiry_collection_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi ok")

# --- research_queue ---
rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_805":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick814 CoA 2026_20 ISI bank data: 2.3bn established 36m collected 1.57pct; "
            "AGIsi 18.7bn; PCC 55.3m accounts; dual SECAL; FOI gap_isi_bank_inquiry_collection_l5 ready"
        )
if not any(x.get("task_id") == "rq_806" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_806",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual); "
                "prefer FOI-adjacent L5; skip rq_116; ISI bank largely filled tick814"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick814 after CoA ISI bank dual",
        }
    )
save_csv(rq_path, rq_fields, rq_rows)
print("rq ok")

# --- loop_state ---
ls_rows, ls_fields, ls_path = load_csv("loop_state.csv")
ls_rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": utc,
    "last_unit_id": "rq_805",
    "ticks_completed": "814",
    "paused": "no",
    "notes": (
        "tick814 CoA ISI bank 2.3bn/36m 1.57pct dual SECAL FOI; "
        "next rq_806 residual dual L5/local; progress@820 in 6; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 814 OK")

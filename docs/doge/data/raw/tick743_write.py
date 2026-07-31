# tick743 — CoA Rekenhof NL Activiteitenverslag 2025 residual recs/certification (rq_734)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T08:45:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_37_Activiteitenverslag_2025.pdf"
# local copy if online path differs
URL_LOCAL = "docs/doge/data/raw/ccrek_2026_37_activiteitenverslag_2025.pdf"

SRC = "src_ccrek_2026_37_av2025_residual"
SRC_DUAL = "src_dual_coa_recs_implement_tick743"

# --- entity rekenhof note if exists ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)
has_rh = any(e.get("entity_id") in ("rekenhof", "ccrek", "cour_des_comptes") for e in ents)
if not any(e.get("entity_id") == "rekenhof_nl" for e in ents):
    with open(ent_path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow([
            "rekenhof_nl",
            "Rekenhof Nederlandse kamer (Vlaanderen)",
            "Cour des comptes chambre neerlandaise",
            "Belgian Court of Audit Dutch chamber",
            "oversight",
            "gg_belgium",
            "nl",
            "https://www.ccrek.be",
            "",
            "",
            "tick743 AV2025 residual: 453 recs 2018-25 only 15.8pct fully implemented; disclaimer on VG 2024 commercial accounts; 58.5 FTE VL",
        ])
    print("entity rekenhof_nl +")
else:
    print("entity rekenhof_nl exists")

# counts from primary percentages
# 379 assessed: 15.8% full, 45.6% started, 19% intention, 14.2% none, 5.4% not assessed
FULL = round(379 * 0.158)  # 60
STARTED = round(379 * 0.456)  # 173
INTENTION = round(379 * 0.19)  # 72
NONE = round(379 * 0.142)  # 54
NOT_ASSESSED = round(379 * 0.054)  # 20
# 60+173+72+54+20 = 379 OK

budgets = [
    # Recommendation monitor residual (counts)
    ("bud_ccrek_vl_thematic_audits_n_42_2018_25", "rekenhof_nl", 2025, 42, "", "", "outturn", SRC, "strong", "VL thematic audit reports COUNT 42 in 2018-2025 monitor; tick743"),
    ("bud_ccrek_vl_recs_total_453_2018_25", "rekenhof_nl", 2025, 453, "", "", "outturn", SRC, "strong", "Recommendations in VL thematic audits 453 COUNT 2018-2025; tick743"),
    ("bud_ccrek_vl_recs_not_yet_followed_16_3pct", "rekenhof_nl", 2025, 163, "", "", "outturn", SRC, "strong", "Share recs not yet followed up 16.3pct (too recent for first assessment); tick743"),
    ("bud_ccrek_vl_recs_assessed_379", "rekenhof_nl", 2025, 379, "", "", "outturn", SRC, "strong", "Recommendations assessed COUNT 379 of 453 2018-2025; tick743"),
    ("bud_ccrek_vl_recs_full_impl_15_8pct", "rekenhof_nl", 2025, 158, "", "", "outturn", SRC, "strong", "Fully implemented share of assessed recs 15.8pct 2018-2025; tick743"),
    ("bud_ccrek_vl_recs_full_impl_n_60", "rekenhof_nl", 2025, 60, "", "", "outturn", SRC, "medium", "Fully implemented COUNT ~60 (=15.8pct of 379 assessed) calculated; tick743"),
    ("bud_ccrek_vl_recs_started_45_6pct", "rekenhof_nl", 2025, 456, "", "", "outturn", SRC, "strong", "Actions planned+started share 45.6pct of assessed; tick743"),
    ("bud_ccrek_vl_recs_intention_only_19pct", "rekenhof_nl", 2025, 190, "", "", "outturn", SRC, "strong", "Intention only (not started) share 19pct of assessed; tick743"),
    ("bud_ccrek_vl_recs_no_action_14_2pct", "rekenhof_nl", 2025, 142, "", "", "outturn", SRC, "strong", "No action and no intention share 14.2pct of assessed; tick743"),
    ("bud_ccrek_vl_recs_no_action_n_54", "rekenhof_nl", 2025, 54, "", "", "outturn", SRC, "medium", "No-action COUNT ~54 (=14.2pct of 379) calculated; tick743"),
    ("bud_ccrek_vl_recs_not_assessed_5_4pct", "rekenhof_nl", 2025, 54, "", "", "outturn", SRC, "strong", "Not assessed (insufficient BBT info) share 5.4pct of assessed; tick743"),
    ("bud_ccrek_vl_recs_weak_followup_class_38_6pct", "rekenhof_nl", 2025, 386, "", "", "outturn", SRC, "medium", "Weak follow-up class intention+none+not_assessed 19+14.2+5.4=38.6pct of assessed; tick743"),
    # Certification residual 2024 accounts
    ("bud_ccrek_vl_cert_disclaimer_commercial_2024", "rekenhof_nl", 2024, 1, "", "", "outturn", SRC, "strong", "Certification disclaimer (onthouding) on VL commercial annual accounts 2024; tick743"),
    ("bud_ccrek_vl_cert_qualified_budget_exec_2024", "rekenhof_nl", 2024, 1, "", "", "outturn", SRC, "strong", "Qualified opinion (met voorbehoud) on VL budget execution 2024; tick743"),
    ("bud_ccrek_vl_cert_clean_esr_2024", "rekenhof_nl", 2024, 1, "", "", "outturn", SRC, "strong", "Unqualified opinion on ESR reporting and consolidated ESR 2024; tick743"),
    ("bud_ccrek_vl_entities_rekeningen_180", "rekenhof_nl", 2024, 180, "", "", "outturn", SRC, "strong", "VL legal entities/DABs in rekeningen overview ~180 (footnote 185 of which 5 no accounts 2024); tick743"),
    ("bud_ccrek_vl_entities_no_accounts_5_2024", "rekenhof_nl", 2024, 5, "", "", "outturn", SRC, "strong", "Entities that did not submit 2024 accounts COUNT 5; tick743"),
    # Capacity residual
    ("bud_ccrek_vl_staff_fte_67_5_2026", "rekenhof_nl", 2026, 675, "", "", "outturn", SRC, "strong", "Rekenhof VL sector FTE 67.5 of which 58.5 for VG level 1Jan2026; tick743"),
    ("bud_ccrek_vl_staff_vg_fte_58_5_2026", "rekenhof_nl", 2026, 585, "", "", "outturn", SRC, "strong", "VG-level FTE 58.5 in Rekenhof VL sector 1Jan2026; tick743"),
    # Verantwoordingsdag residual
    ("bud_ccrek_verantwoordingsdag_first_2027", "rekenhof_nl", 2027, 1, "", "", "budgeted", SRC, "strong", "First Verantwoordingsdag planned plenary 28 Jun 2027 (Dutch model accountability day); tick743"),
    ("bud_ccrek_verantwoordingsdag_werven_7", "rekenhof_nl", 2026, 7, "", "", "outturn", SRC, "strong", "Technical working group 7 workstreams for Verantwoordingsdag (charter); tick743"),
    # 2025 published thematic audits inventory COUNT
    ("bud_ccrek_vl_audits_published_class_2025", "rekenhof_nl", 2025, 8, "", "", "outturn", SRC, "medium", "Thematic audits reported to VL parliament class ~8 in 2025 wave (TV, coast, renewables, schakel, combined permit, performance budget, digisprong, buitengewoon edu); tick743"),
    ("bud_ccrek_impact_notes_6_2025", "rekenhof_nl", 2025, 6, "", "", "outturn", SRC, "strong", "Impact-evaluation notes produced COUNT 6 in 2025; tick743"),
    ("bud_ccrek_followup_notes_5_2025", "rekenhof_nl", 2025, 5, "", "", "outturn", SRC, "strong", "Follow-up notes COUNT 5 in 2025; VDAB outsourcing needs further follow-up; tick743"),
    ("bud_ccrek_buitengewoon_edu_pupils_plus_13pct", "rekenhof_nl", 2024, 13, "", "", "outturn", SRC, "strong", "Special education pupils +nearly 13pct in 4 years (no path to inclusive education); tick743"),
    # Dual residual governance
    ("bud_dual_coa_recs_full_impl_only_15_8pct", "gg_belgium", 2025, 158, "", "", "outturn", SRC_DUAL, "strong", "VL CoA recs fully implemented only 15.8pct of assessed dual federal/BCR CoA follow-up residual; tick743"),
    ("bud_dual_coa_disclaimer_accounts_vs_esr_clean", "gg_belgium", 2024, 1, "", "", "outturn", SRC_DUAL, "strong", "VL commercial accounts disclaimer vs clean ESR dual reporting quality residual; tick743"),
    ("bud_dual_verantwoordingsdag_2027_vs_bbt_quality", "gg_belgium", 2027, 1, "", "", "budgeted", SRC_DUAL, "strong", "Verantwoordingsdag 2027 depends on earlier BBT delivery dual performance-budget residual; tick743"),
]

bud_path = DATA / "budgets.csv"
with open(bud_path, encoding="utf-8", newline="") as f:
    br = csv.DictReader(f)
    bfields = br.fieldnames
    existing = {r["budget_id"] for r in br}
added_b = 0
with open(bud_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bfields, lineterminator="\n")
    for row in budgets:
        if row[0] in existing:
            continue
        w.writerow({
            "budget_id": row[0], "entity_id": row[1], "year": row[2],
            "amount_eur": row[3], "amount_min_eur": row[4], "amount_max_eur": row[5],
            "basis": row[6], "source_id": row[7], "confidence": row[8], "notes": row[9],
        })
        added_b += 1
print(f"budgets +{added_b}")

commitments = [
    {
        "commitment_id": "cmt_ccrek_recs_monitor_453_2018_25",
        "title": "CoA VL recommendation monitor 453 recs / only 15.8pct fully implemented",
        "entity_id": "rekenhof_nl",
        "beneficiary": "VL Parliament oversight / citizen accountability",
        "legal_basis": "Rekenhof Activiteitenverslag 2025 ch4.3.6 monitor.ccrek.be",
        "decision_date": "2026-06-23",
        "start_year": "2018",
        "end_year": "2025",
        "total_envelope_eur": "453",
        "cash_by_year": '{"audits_n":42,"recs_n":453,"assessed_n":379,"full_impl_pct":15.8,"started_pct":45.6,"intention_pct":19.0,"no_action_pct":14.2,"not_assessed_pct":5.4,"not_yet_followed_pct":16.3}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://monitor.ccrek.be",
        "stated_goal": "Ensure CoA recommendations are implemented",
        "cut_option": "Publish cash-impact of open recs FOI + force BBT disclosure",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Rekenhof>recs_monitor",
        "notes": "tick743 amount_eur is COUNT recs",
    },
    {
        "commitment_id": "cmt_ccrek_cert_disclaimer_2024",
        "title": "VL 2024 accounts: commercial disclaimer + qualified budget execution",
        "entity_id": "rekenhof_nl",
        "beneficiary": "Vlaams Parlement / fiscal transparency",
        "legal_basis": "Rekeningenrapport 2024 via AV2025 residual",
        "decision_date": "2025-06-30",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "",
        "cash_by_year": '{"commercial":"disclaimer_onthouding","budget_exec":"qualified_voorbehoud","esr":"unqualified","consol_esr":"unqualified","entities_no_accounts_n":5}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "True and fair view of VL public accounts",
        "cut_option": "Remediate commercial accounts for clean opinion FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Rekenhof>certification",
        "notes": "tick743",
    },
    {
        "commitment_id": "cmt_ccrek_verantwoordingsdag_2027",
        "title": "First Verantwoordingsdag planned 28 Jun 2027 with CoA accountability research",
        "entity_id": "rekenhof_nl",
        "beneficiary": "Vlaams Parlement / performance budget path",
        "legal_basis": "Regeerakkoord 2024-29 + technical WG under CoA lead",
        "decision_date": "2026-04-01",
        "start_year": "2025",
        "end_year": "2027",
        "total_envelope_eur": "",
        "cash_by_year": '{"first_date":"2027-06-28","werven_n":7,"bbt_reform":"web platform detail","depends_on":"earlier document delivery before 21 May"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Dutch-model accountability day linking money to results",
        "cut_option": "Advance BBT deadlines FOI dual performance budget",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Rekenhof>verantwoordingsdag",
        "notes": "tick743",
    },
    {
        "commitment_id": "cmt_ccrek_audits_2025_wave",
        "title": "2025 thematic audit wave: TV, coast, renewables, combined permit, schakel",
        "entity_id": "rekenhof_nl",
        "beneficiary": "VL policy domains MOW/Omgeving/Onderwijs",
        "legal_basis": "Rekenhof AV2025 ch4.3",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "",
        "cash_by_year": '{"tv_5th_progress":"2025-03-11","kust":"2026-01-27","renewables":"2025-10-14","schakel":"2025-06-11","combined_permit":"2025-07-10","performance_budget":"2024-09-30","buitengewoon_edu":"+13pct pupils 4y","vdab_outsourcing":"further_followup"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Performance audit of high-impact VL policies",
        "cut_option": "Link open recs to € programmes FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Rekenhof>audits_2025",
        "notes": "tick743",
    },
    {
        "commitment_id": "cmt_ccrek_vl_staff_58_5_fte",
        "title": "Rekenhof VL chamber capacity 58.5 FTE for entire VG oversight",
        "entity_id": "rekenhof_nl",
        "beneficiary": "Oversight of VL GG spend",
        "legal_basis": "Rekenhof AV2025 ch2 organigram",
        "decision_date": "2026-01-01",
        "start_year": "2026",
        "end_year": "2026",
        "total_envelope_eur": "58.5",
        "cash_by_year": '{"sector_fte":67.5,"vg_fte":58.5,"dirs":"9 financial + 10 thematic"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Adequate audit capacity for VL government",
        "cut_option": "Capacity vs TE coverage ratio FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Rekenhof>capacity",
        "notes": "tick743 amount is FTE",
    },
    {
        "commitment_id": "cmt_dual_coa_recs_implement_tick743",
        "title": "Dual CoA rec implementation gap VL 15.8% full vs performance-budget path",
        "entity_id": "gg_belgium",
        "beneficiary": "BE accountability dual map",
        "legal_basis": "Rekenhof AV2025 + prior CoA dual residual",
        "decision_date": "2026-06-23",
        "start_year": "2018",
        "end_year": "2025",
        "total_envelope_eur": "453",
        "cash_by_year": '{"vl_full_impl_pct":15.8,"vl_no_action_pct":14.2,"vl_intention_pct":19.0,"verantwoordingsdag":2027,"disclaimer_accounts":2024,"note":"not TE euros — governance residual"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Comparable audit follow-through across BE levels",
        "cut_option": "Publish open-rec cash map FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>CoA_recs",
        "notes": "tick743",
    },
]

cmt_path = DATA / "commitments.csv"
with open(cmt_path, encoding="utf-8", newline="") as f:
    cr = csv.DictReader(f)
    cfields = cr.fieldnames
    cexist = {r["commitment_id"] for r in cr}
added_c = 0
with open(cmt_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cfields, lineterminator="\n")
    for row in commitments:
        if row["commitment_id"] in cexist:
            continue
        w.writerow(row)
        added_c += 1
print(f"commitments +{added_c}")

leaderboard = [
    {
        "item_id": "lb_ccrek_recs_full_impl_only_15_8pct",
        "name": "CoA VL recs fully implemented only 15.8% of 379 assessed (2018-25)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Vlaanderen>Rekenhof>recs_impl",
        "annual_cost_eur": "453",
        "total_cost_eur": "453",
        "tco_notes": "42 audits / 453 recs; 14.2% no action; 19% intention only; not pure TE but oversight failure",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "VL taxpayers via unfixed audit findings",
        "stated_goal": "Implement Court of Audit recommendations",
        "measured_outcome": "15.8% full; 45.6% started; 38.6% weak class",
        "absurdity_score": "8.5",
        "cost_score": "4.0",
        "difficulty": "3",
        "priority_index": "6.50",
        "cut_proposal": "Force open-rec cash map + BBT mandatory response FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick743 high-absurdity governance residual",
    },
    {
        "item_id": "lb_ccrek_disclaimer_commercial_accounts_2024",
        "name": "VL 2024 commercial accounts certification disclaimer (onthouding)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Vlaanderen>Rekenhof>certification",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "Disclaimer vs clean ESR; qualified budget execution; 5 entities no accounts",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Fiscal transparency users",
        "stated_goal": "True and fair commercial accounts",
        "measured_outcome": "Disclaimer commercial; qualified budget exec; clean ESR",
        "absurdity_score": "8.0",
        "cost_score": "3.5",
        "difficulty": "3",
        "priority_index": "5.95",
        "cut_proposal": "Remediation plan for clean commercial opinion FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick743",
    },
    {
        "item_id": "lb_ccrek_recs_no_action_14_2pct",
        "name": "CoA VL recs 14.2% no action/no intention (dead recommendations)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Vlaanderen>Rekenhof>dead_recs",
        "annual_cost_eur": "54",
        "total_cost_eur": "54",
        "tco_notes": "~54 of 379 assessed; plus 19% intention-only not started",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Unfixed policy failures",
        "stated_goal": "Ministerial follow-through on audits",
        "measured_outcome": "14.2% none + 19% intention-only",
        "absurdity_score": "8.0",
        "cost_score": "3.5",
        "difficulty": "2",
        "priority_index": "6.10",
        "cut_proposal": "Name-and-shame dead recs in BBT FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick743",
    },
    {
        "item_id": "lb_ccrek_verantwoordingsdag_2027_lag",
        "name": "Verantwoordingsdag only from 2027; docs still late after 21 May",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Vlaanderen>Rekenhof>verantwoordingsdag",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "First day 28 Jun 2027; CoA needs earlier docs for deep review; dual performance budget",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Parliament performance oversight",
        "stated_goal": "Link money to results annually",
        "measured_outcome": "Framework set Apr2026; first day 2027; BBT reform multi-year",
        "absurdity_score": "6.5",
        "cost_score": "3.0",
        "difficulty": "3",
        "priority_index": "5.15",
        "cut_proposal": "Advance document deadlines FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick743",
    },
    {
        "item_id": "lb_ccrek_buitengewoon_edu_plus_13pct",
        "name": "Special education pupils +13% in 4 years (no path to inclusion)",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Vlaanderen>Onderwijs>buitengewoon",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "CoA AV residual summary; capacity shortage size unknown to gov",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Special-education pupils",
        "stated_goal": "Inclusive education path",
        "measured_outcome": "+nearly 13% pupils 4y; capacity gap unknown",
        "absurdity_score": "7.0",
        "cost_score": "5.5",
        "difficulty": "4",
        "priority_index": "6.00",
        "cut_proposal": "Capacity map + CLB inclusion FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick743 euro Unknown — FOI",
    },
    {
        "item_id": "lb_ccrek_vdab_outsourcing_followup_open",
        "name": "VDAB outsourcing audit still needs further CoA follow-up (2025)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Vlaanderen>VDAB>outsourcing_recs",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "Of 5 follow-up notes 2025 only VDAB flagged for further follow-up",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "VDAB procurement oversight",
        "stated_goal": "Close outsourcing audit recommendations",
        "measured_outcome": "Further follow-up necessary Dec2025",
        "absurdity_score": "6.5",
        "cost_score": "5.0",
        "difficulty": "3",
        "priority_index": "5.70",
        "cut_proposal": "Parliament follow-up debate + open recs FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick743",
    },
    {
        "item_id": "lb_dual_coa_recs_implement_gap",
        "name": "Dual CoA rec implementation gap: VL only 15.8% full vs clean ESR fiction",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>CoA_recs",
        "annual_cost_eur": "453",
        "total_cost_eur": "453",
        "tco_notes": "Not TE; governance dual across chambers; Verantwoordingsdag 2027 path",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE accountability dual map",
        "stated_goal": "Comparable audit follow-through",
        "measured_outcome": "VL 15.8% full impl; commercial accounts disclaimer",
        "absurdity_score": "8.0",
        "cost_score": "4.5",
        "difficulty": "3",
        "priority_index": "6.30",
        "cut_proposal": "Cross-chamber open-rec cash dashboard FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick743",
    },
]

lb_path = DATA / "leaderboard.csv"
with open(lb_path, encoding="utf-8", newline="") as f:
    lr = csv.DictReader(f)
    lfields = lr.fieldnames
    lexist = {r["item_id"] for r in lr}
added_l = 0
with open(lb_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lfields, lineterminator="\n")
    for row in leaderboard:
        if row["item_id"] in lexist:
            continue
        w.writerow(row)
        added_l += 1
print(f"leaderboard +{added_l}")

sources = [
    {
        "source_id": SRC,
        "title": "Rekenhof NL Activiteitenverslag 2025 residual recs/certification dual",
        "url": "https://www.ccrek.be/sites/default/files/Docs/2026_37_Activiteitenverslag_2025.pdf",
        "publisher": "Rekenhof Nederlandse kamer",
        "accessed_date": "2026-08-02",
        "source_class": "court_of_audit",
        "notes": (
            "Strong tick743: 42 VL thematic audits 2018-25 / 453 recs; assessed 379: full 15.8 started 45.6 "
            "intention 19 no_action 14.2 not_assessed 5.4; commercial accounts disclaimer 2024; qualified budget exec; "
            "clean ESR; Verantwoordingsdag 28Jun2027; 58.5 FTE VG; 5 entities no 2024 accounts; raw ccrek_2026_37"
        ),
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual CoA rec implementation gap VL residual tick743",
        "url": "https://www.ccrek.be/sites/default/files/Docs/2026_37_Activiteitenverslag_2025.pdf",
        "publisher": "DOGE synthesis Rekenhof AV2025",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": (
            "Strong dual governance: VL rec full impl only 15.8pct + commercial disclaimer vs ESR clean; "
            "Verantwoordingsdag 2027 lag dual performance-budget residual; not TE euros; tick743"
        ),
    },
]

src_path = DATA / "sources.csv"
with open(src_path, encoding="utf-8", newline="") as f:
    sr = csv.DictReader(f)
    sfields = sr.fieldnames
    sexist = {r["source_id"] for r in sr}
added_s = 0
with open(src_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, lineterminator="\n")
    for row in sources:
        if row["source_id"] in sexist:
            continue
        w.writerow(row)
        added_s += 1
print(f"sources +{added_s}")

foi_row = {
    "gap_id": "gap_ccrek_av2025_recs_impl_l5",
    "hierarchy_path": "Vlaanderen>Rekenhof>AV2025_recs_impl_L5",
    "entity_id": "rekenhof_nl",
    "what_is_missing": (
        "Machine-readable L5: (1) full list of 453 recs with status and linked € programmes; "
        "(2) cash impact estimate of the 14.2% no-action and 19% intention-only recs; "
        "(3) remediation plan and timeline for commercial accounts certification disclaimer 2024; "
        "(4) names of 5 entities without 2024 accounts; (5) Verantwoordingsdag BBT delivery calendar "
        "and early-document milestones 2026-27; (6) open recs for GIP/TV/VDAB/housing duals"
    ),
    "why_it_matters": (
        "AV2025 shows only 15.8% full implementation of assessed CoA recs and a commercial-accounts "
        "disclaimer — governance residual that blocks waste cut follow-through"
    ),
    "priority": "8",
    "recipient_body": "Rekenhof / Vlaams Parlement / FB",
    "recipient_email": "info@ccrek.be",
    "recipient_postal": "https://www.ccrek.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_ccrek_av2025_recs_impl_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_ccrek_recs_monitor_453_2018_25|cmt_ccrek_cert_disclaimer_2024|cmt_ccrek_verantwoordingsdag_2027",
    "linked_leaderboard_id": "lb_ccrek_recs_full_impl_only_15_8pct|lb_ccrek_disclaimer_commercial_accounts_2024|lb_dual_coa_recs_implement_gap",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick743 CoA AV2025 residual; ready not sent; monitor.ccrek.be partial public",
}

foi_path = DATA / "foi_queue.csv"
with open(foi_path, encoding="utf-8", newline="") as f:
    fr = csv.DictReader(f)
    ffields = fr.fieldnames
    fexist = {r["gap_id"] for r in fr}
if foi_row["gap_id"] not in fexist:
    with open(foi_path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ffields, lineterminator="\n")
        w.writerow(foi_row)
    print("foi +gap_ccrek_av2025_recs_impl_l5")
else:
    print("foi already exists")

rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_734":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick743 CoA AV2025 residual: recs 453 full impl 15.8pct; commercial disclaimer 2024; "
            "Verantwoordingsdag 2027; FOI gap_ccrek_av2025_recs_impl_l5 ready"
        )
if not any(r.get("task_id") == "rq_735" for r in rqs):
    rqs.append({
        "task_id": "rq_735",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined (prefer CoA 2026_31 IT carrieres or "
            "hernieuwbare energie full if not mined) or Entity II dual residual or fed Pillar2/VVPR recheck"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick743 after rq_734",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("research_queue rq_734=done rq_735=open")

ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys())
if ls:
    ls[0]["mode"] = "continuous"
    ls[0]["current_sprint"] = "hole_fill"
    ls[0]["last_tick_utc"] = UTC
    ls[0]["last_unit_id"] = "rq_734"
    ls[0]["ticks_completed"] = "743"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        "tick743 CoA AV2025 recs/cert residual; next rq_735; "
        "progress@750 in 7; rq_116 deferred"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=743")
print("DONE tick743")

# tick 439: CoA Budget 2026 federal personnel austerity L5 multi-year + specialty breaches residual
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T10:15:00Z"
TICK = 439
UNIT = "rq_430"
SRC = "src_ccrek_budget2026_personnel_austerity"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf"

# Partial replacement of departures (personnel+ops credits) m EUR
# 100m 2026 growing to 175m 2030; linear intermediate if not published — use only stated ends + note
# CoA: progressive; only endpoints explicit
REPLACE = {
    2026: 100.0,
    2030: 175.0,
}
# 2 hires per 5 departures if target missed; excl regalian (Justice Defence Police AE Interior OE)

# Statutory employer cotis on NEW statutaires after 31 May 2026
# Rate path 9.5% 2026 → 38% 2030 (covers pension cost of new statutaires per exposé)
STAT_COTIS = {
    2026: 10.0,
    2029: 284.0,
    2030: 365.0,
}
# Combined Entity I financing balance influence 459m in 2029 (gov claim)

# Defence department estimate of cotis cost on new statutaires (m EUR)
DEF_COTIS = {
    2026: 3.7,
    2027: 22.7,
    2028: 59.4,
    2029: 113.3,
    2034: 297.3,
}
# Defence recruitment path (headcount, not EUR)
DEF_RECRUIT = {
    "active_2026": 2800,
    "active_2034": 3600,
    "reserve_2026": 1050,
    "reserve_2034": 1500,
    "civil_annual": 960,
    "target_active_2034": 34500,
    "target_reserve_2034": 12800,
    "target_civil_2034": 8500,
    "annual_recruits_2034_lo": 4810,
    "annual_recruits_2034_hi": 6060,
}

# Justice impact
JUSTICE = {
    2026: {"cost_m": 3.3, "fte": 61},
    2029: {"cost_m": 101.0, "fte": 1859, "fte_judiciary": 622},
}

# Federal police
POLICE = {
    2026: {"fte_cut": 26},
    2029: {"fte_cut_lo": 700, "fte_cut_hi": 821},
}

# Specialty / transfer derogations
SPECIALTY = {
    "transfers_2024_eng_m": 454.0,  # between programmes 2024
    "defence_eng_transferable_m": 20100.0,  # s16 full eng transferable
    "justice_section_m": 2500.0,  # personnel/ops/invest redistributable
    "police_section_m": 1600.0,
    "provisions_interdept_eng_m": 2125.8,
    "provisions_interdept_liq_m": 2128.0,
}

# Droits d'auteur forfait removal +30m (dual IPP -142 reopen IT)
DROITS_FORFAIT_SAVE = 30.0

# VVPR historical path (context for 18% measure)
VVPR_HIST = {2022: 344.0, 2024: 760.4}  # doubled in 3 years

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 personnel austerity L5 + specialty breaches",
            "url": URL,
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": (
                f"p53-57 partial replace 100→175; statutaire cotis 10/284/365; "
                f"Defence/Justice/Police impacts; specialty transfers; tick{TICK}"
            ),
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add_bud(bid, entity, year, amount, basis, notes, conf="medium"):
    if any(r["budget_id"] == bid for r in bud):
        return False
    bud.append(
        {
            "budget_id": bid,
            "entity_id": entity,
            "year": str(year),
            "amount_eur": str(int(round(amount))),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": SRC,
            "confidence": conf,
            "notes": notes,
        }
    )
    return True


n_bud = 0

# Partial replacement multi-year (only stated years)
for y, v in REPLACE.items():
    if add_bud(
        f"bud_personnel_partial_replace_save_{y}",
        "sec_federal",
        y,
        v * 1e6,
        "budgeted",
        (
            f"Partial staff/ops replacement save target {v}m {y} CoA p53 "
            f"(100→175 path 2026-30; excl regalian; 2/5 hire rule if miss); tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1

# Intermediate path unknown — store CoA note only via 2027-29 optional linear? Prefer NOT invent.
# Document gap as Unknown intermediate in commitment.

for y, v in STAT_COTIS.items():
    if add_bud(
        f"bud_statutaire_employer_cotis_{y}",
        "sec_federal",
        y,
        v * 1e6,
        "budgeted",
        (
            f"Employer cotis on new Entity I statutaires after 31 May 2026: yield {v}m {y} "
            f"(rate 9.5pct 2026 → 38pct 2030; CoA: flat hire-volume hyp contradicts contract-prefer policy); tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1

if add_bud(
    "bud_personnel_austerity_entity1_2029",
    "sec_federal",
    2029,
    459e6,
    "budgeted",
    (
        "Combined personnel austerity influence on Entity I financing balance 459m 2029 "
        "(partial replace + statutaire cotis gov claim CoA p53); tick{TICK}"
    ),
    "medium",
):
    n_bud += 1

# Defence cotis path
for y, v in DEF_COTIS.items():
    if add_bud(
        f"bud_def_statutaire_cotis_cost_{y}",
        "mod_defensie",
        y,
        v * 1e6,
        "estimate",
        (
            f"Defence est employer cotis cost on new statutaires {v}m {y} CoA p55 "
            f"(not in military programming law; compensates from other section credits); tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1

# Defence recruitment headcounts
for key, v in DEF_RECRUIT.items():
    y = 2034 if "2034" in key else 2026
    if add_bud(
        f"bud_def_recruit_{key}",
        "mod_defensie",
        y,
        v,
        "estimate",
        f"Defence recruitment/target {key}={v} (headcount; loi programmation militaire 2026-34); tick{TICK}",
        "strong",
    ):
        n_bud += 1

# Justice impact
for y, d in JUSTICE.items():
    if add_bud(
        f"bud_justice_statutaire_cotis_cost_{y}",
        "fod_justice",
        y,
        d["cost_m"] * 1e6,
        "estimate",
        (
            f"Justice est statutaire cotis cost {d['cost_m']}m / {d['fte']} FTE {y} CoA p54 "
            f"(2029 of which judiciary {d.get('fte_judiciary', '')} FTE); compensate other s12 credits; tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_justice_statutaire_cotis_fte_{y}",
        "fod_justice",
        y,
        d["fte"],
        "estimate",
        f"Justice FTE equivalent of statutaire cotis {d['fte']} {y}; headcount; tick{TICK}",
        "medium",
    ):
        n_bud += 1

# Police
if add_bud(
    "bud_police_statutaire_fte_cut_2026",
    "police_federale",
    2026,
    POLICE[2026]["fte_cut"],
    "estimate",
    f"Federal police recruitment capacity cut {POLICE[2026]['fte_cut']} FTE 2026 from statutaire cotis CoA p55; tick{TICK}",
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_police_statutaire_fte_cut_2029_lo",
    "police_federale",
    2029,
    POLICE[2029]["fte_cut_lo"],
    "estimate",
    f"Federal police FTE capacity cut low {POLICE[2029]['fte_cut_lo']} by 2029 CoA; tick{TICK}",
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_police_statutaire_fte_cut_2029_hi",
    "police_federale",
    2029,
    POLICE[2029]["fte_cut_hi"],
    "estimate",
    f"Federal police FTE capacity cut high {POLICE[2029]['fte_cut_hi']} by 2029 CoA; tick{TICK}",
    "medium",
):
    n_bud += 1

# Specialty
for key, v in SPECIALTY.items():
    conf = "strong"
    if add_bud(
        f"bud_specialty_{key}",
        "sec_federal",
        2026 if "2024" not in key else 2024,
        v * 1e6 if "fte" not in key else v,
        "budgeted" if "2024" not in key else "outturn",
        (
            f"Budget specialty breach/transfer L5 {key} {v}{'m EUR' if True else ''} CoA p56-57 "
            f"(Defence full eng transferable; Justice+Police personnel/ops/invest free; "
            f"provisions 2.13bn CM transfer); tick{TICK}"
        ),
        conf,
    ):
        n_bud += 1

if add_bud(
    "bud_droits_auteur_forfait_remove_2026",
    "fod_finance",
    2026,
    DROITS_FORFAIT_SAVE * 1e6,
    "budgeted",
    (
        f"Remove forfait expense deduction on copyright regime +{DROITS_FORFAIT_SAVE}m 2026 "
        f"(artists with arts-work attestation keep forfait; dual IPP reopen IT -142m); tick{TICK}"
    ),
    "medium",
):
    n_bud += 1

for y, v in VVPR_HIST.items():
    if add_bud(
        f"bud_vvpr_pm_hist_{y}",
        "fod_finance",
        y,
        v * 1e6,
        "outturn",
        f"VVPR/liquidation-class PM receipts {v}m {y} CoA p48 (doubled 2022-24); dual 18pct measure; tick{TICK}",
        "strong",
    ):
        n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

# --- commitments ---
with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())

n_cmt = 0
if not any(r.get("commitment_id") == "cmt_personnel_austerity_2026_30" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_personnel_austerity_2026_30",
            "title": "Entity I personnel austerity: partial replace + statutaire employer cotis 2026-30",
            "entity_id": "sec_federal",
            "beneficiary": "Federal administrations (excl partial regalian carve-outs)",
            "legal_basis": "Coalition 31 Jan 2025; CM budget conclave; draft law statutaire cotis",
            "decision_date": "2025-12-12",
            "start_year": "2026",
            "end_year": "2030",
            "total_envelope_eur": str(int(459e6)),
            "cash_by_year": json.dumps(
                {
                    "partial_replace_m": REPLACE,
                    "statutaire_cotis_m": STAT_COTIS,
                    "entity1_combined_2029_m": 459,
                    "rate_path_pct": {"2026": 9.5, "2030": 38},
                    "defence_cost_m": DEF_COTIS,
                    "justice_cost_m": {str(y): JUSTICE[y]["cost_m"] for y in JUSTICE},
                    "justice_fte": {str(y): JUSTICE[y]["fte"] for y in JUSTICE},
                    "police_fte_cut": POLICE,
                    "coa_flags": [
                        "statutaire cotis flat hire volume contradicts contract-prefer policy",
                        "regalian depts still hit by cotis (no exception)",
                        "costs compensated from ops/invest within sections",
                        "partial replace intermediate years 2027-29 not published",
                    ],
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Cut federal admin headcount cost; prefer contractual; fund new-statutaire pensions",
            "cut_option": "Publish intermediate replace path; exempt true regalian or fund cotis; dual antifraud FTE",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": "Federal>personnel>austerity_2026_30",
            "notes": f"CoA p53-55 full L5; tick{TICK}",
        }
    )
    n_cmt += 1

if not any(r.get("commitment_id") == "cmt_budget_specialty_breaches_2026" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_budget_specialty_breaches_2026",
            "title": "Federal budget specialty principle breaches 2024-26 (transfers + provisions)",
            "entity_id": "sec_federal",
            "beneficiary": "Executive flexibility vs parliamentary control",
            "legal_basis": "Budget general des depenses derogations; art 48/52 law 22 May 2003",
            "decision_date": "2026-01-28",
            "start_year": "2024",
            "end_year": "2026",
            "total_envelope_eur": str(int(SPECIALTY["provisions_interdept_liq_m"] * 1e6)),
            "cash_by_year": json.dumps(SPECIALTY),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Management flexibility via transfers and interdept provisions",
            "cut_option": "Restore specialty; inscribe known uses in sections; limit eng transfer powers",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Federal>budget>specialty_breaches",
            "notes": f"CoA p56-57; dual provisions prior ticks; tick{TICK}",
        }
    )
    n_cmt += 1

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

# --- leaderboard ---
with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def add_lb(iid, name, annual, total, tco, conf, benef, goal, outcome, abs_s, cost_s, diff, prio, cut, notes, hpath, typ="policy"):
    if any(r.get("item_id") == iid for r in lb):
        return False
    lb.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": hpath,
            "annual_cost_eur": str(int(round(annual))),
            "total_cost_eur": str(int(round(total))),
            "tco_notes": tco,
            "confidence": conf,
            "source_id": SRC,
            "beneficiaries": benef,
            "stated_goal": goal,
            "measured_outcome": outcome,
            "absurdity_score": str(abs_s),
            "cost_score": str(cost_s),
            "difficulty": str(diff),
            "priority_index": str(prio),
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": notes,
        }
    )
    return True


n_lb = 0
rows = [
    (
        "lb_personnel_austerity_459m_2029",
        "Entity I personnel austerity package influence 459m 2029",
        459e6,
        459e6,
        "Medium CoA: partial replace 100→175 + statutaire cotis 10/284/365; method flags; regalian still hit by cotis",
        "medium",
        "Federal admin / new statutaires",
        "Cut admin cost; prefer contractual hiring",
        "CoA cannot verify hire-volume hyp vs contract preference",
        5.5,
        7.5,
        6,
        6.5,
        "Publish intermediate path; fund regalian cotis or exempt",
        f"tick{TICK}",
        "Federal>personnel>austerity",
    ),
    (
        "lb_statutaire_cotis_365m_2030",
        "New-statutaire employer cotis path to 365m 2030",
        365e6,
        (10 + 284 + 365) * 1e6,
        "Medium: 9.5pct→38pct of new statutaire wage bill; Defence alone 3.7→113m 2026-29 / 297m 2034",
        "medium",
        "Entity I employers of new statutaires",
        "Pre-fund pensions of new statutaires; push contractual",
        "Flat volume hyp; no section credit uplift",
        6.0,
        7.0,
        6,
        6.4,
        "Reconcile with military/police/justice staffing laws",
        f"tick{TICK}",
        "Federal>personnel>statutaire_cotis",
    ),
    (
        "lb_partial_replace_175m_2030",
        "Partial departure replacement save 100m→175m 2030",
        100e6,
        (100 + 175) * 1e6,
        "Medium CoA: personnel+ops; excl regalian; 2-for-5 hire penalty if miss; intermediate years unpublished",
        "medium",
        "Non-regalian Entity I institutions",
        "Shrink federal headcount via attrition",
        "Delivery depends on turnover and section discipline",
        4.5,
        6.0,
        5,
        5.2,
        "Publish annual target by SPF; dual admin reorg 300m",
        f"tick{TICK}",
        "Federal>personnel>partial_replace",
    ),
    (
        "lb_def_statutaire_cotis_113m_2029",
        "Defence statutaire cotis cost 113m 2029 path 297m 2034",
        113.3e6,
        sum(DEF_COTIS.values()) * 1e6,
        "Medium Defence est: 3.7/22.7/59.4/113.3/297.3; military programming law ignores cost; no contractual military",
        "medium",
        "Defence new recruits (statutaire only for active)",
        "Pension prefunding for military growth path",
        "Conflicts with 34500 active target by 2034",
        6.5,
        7.5,
        7,
        7.0,
        "Amend LPM envelope; dual NATO 2pct path",
        f"tick{TICK}",
        "Federal>Defence>statutaire_cotis",
    ),
    (
        "lb_justice_statutaire_cotis_101m",
        "Justice statutaire cotis cost 101m / 1859 FTE by 2029",
        101e6,
        (3.3 + 101) * 1e6,
        "Medium CoA: 3.3m/61 FTE 2026 → 101m/1859 FTE 2029 (622 judiciary); compensate s12 other credits",
        "medium",
        "Justice / judiciary recruitment",
        "Pension prefund new statutaires",
        "Stacks with surpop and security provisions pressure",
        6.0,
        6.5,
        6,
        6.2,
        "Clarify regalian carve-out for judiciary; dual prison package",
        f"tick{TICK}",
        "Federal>Justice>statutaire_cotis",
    ),
    (
        "lb_police_fte_cut_cotis_821",
        "Federal police recruitment cut up to 821 FTE by 2029 from cotis",
        821,
        821,
        "Medium CoA: 26 FTE 2026 → 700-821 by 2029; statute blocks full contractual substitution",
        "medium",
        "Federal police staffing",
        "Pension prefund vs headcount capacity",
        "Conflicts with security reinforcement narrative",
        7.0,
        6.0,
        6,
        6.4,
        "Legislate contractual path or fund cotis; dual security prov 367m",
        f"tick{TICK}",
        "Federal>Police>statutaire_cotis_fte",
    ),
    (
        "lb_specialty_defence_transfer_20bn",
        "Defence full engagement credits transferable without parliament 20.1bn",
        20100e6,
        20100e6,
        "Strong CoA p57: s16 eng fully redistributable; Justice 2.5bn + Police 1.6bn personnel/ops/invest free; dual provisions 2.13bn",
        "strong",
        "Executive vs parliament budget control",
        "Management flexibility",
        "Programmes become indicative only CoA",
        8.0,
        9.0,
        7,
        8.0,
        "Restore specialty; annual transfer report L5",
        f"tick{TICK}",
        "Federal>budget>specialty_defence",
    ),
    (
        "lb_specialty_transfers_454m_2024",
        "Inter-programme credit transfers 454m eng 2024",
        454e6,
        454e6,
        "Strong CoA: 454m engagement redistributed across programmes 2024 under soft specialty rules",
        "strong",
        "Federal programmes",
        "Flexible reallocation within/between programmes",
        "Cumulative erosion of programme budget model since 1986",
        6.5,
        7.0,
        5,
        6.3,
        "Cap transfers; publish real-time programme dashboard",
        f"tick{TICK}",
        "Federal>budget>programme_transfers",
    ),
    (
        "lb_droits_auteur_forfait_30m",
        "Copyright forfait deduction removal +30m 2026",
        30e6,
        30e6,
        "Medium: only arts-work attestation keeps forfait; dual IPP reopen IT sector -142m net package",
        "medium",
        "Copyright regime users (non-attested)",
        "Narrow forfait abuse after IT reopening",
        "Complex regime history confounds estimate CoA",
        5.0,
        4.0,
        4,
        4.4,
        "Publish IT vs artist split outturn",
        f"tick{TICK}",
        "Federal>tax>droits_auteur_forfait",
    ),
    (
        "lb_vvpr_anticipation_spike",
        "VVPR PM anticipation spike to 1.21bn 2025 before 18pct rate",
        1209.6e6,
        1209.6e6,
        "Strong CoA: 1209.6m 2025 (+449.2; Dec +404.6); base doubled 344→760 2022-24; 2026 +90m uncertain",
        "strong",
        "SME shareholders VVPRbis/liquidation reserves",
        "Discourage passage-en-société distributions",
        "Front-loading risks hollow 2026+ yields",
        6.0,
        7.5,
        5,
        6.4,
        "Track multi-year PM after rate change; dual CGT interaction",
        f"tick{TICK}",
        "Federal>tax>VVPR_anticipation",
    ),
]
for args in rows:
    if add_lb(*args):
        n_lb += 1

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

# --- research_queue ---
with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())

for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: personnel austerity L5 (replace 100→175; cotis 10/284/365; EntityI 459m 2029; "
            f"Defence/Justice/Police impacts) + specialty breaches 20.1bn/454m; rq_116 deferred"
        )

if not any(r.get("task_id") == "rq_431" for r in rq):
    rq.append(
        {
            "task_id": "rq_431",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": "",
            "notes": f"Spawned tick{TICK} after personnel austerity L5; rq_116 SWA deferred",
        }
    )

with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

# --- loop_state ---
with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsf = list(ls[0].keys())
ls[-1]["last_tick_utc"] = NOW
ls[-1]["last_unit_id"] = UNIT
ls[-1]["ticks_completed"] = str(TICK)
ls[-1]["mode"] = "continuous"
ls[-1]["current_sprint"] = "hole_fill"
ls[-1]["paused"] = "no"
ls[-1]["notes"] = (
    f"Scheduler 60s. Next prio5 rq_431; rq_116 SWA deferred. "
    f"tick{TICK} personnel austerity 459m + specialty."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **personnel austerity L5 multi-year + specialty breaches**)
- Found (medium-strong primary Cour des comptes Budget Etat 2026 p53-57):
  - **Partial replace:** **100m 2026 → 175m 2030** (personnel+ops; excl regalian; 2/5 hire if miss; intermediate years unpublished)
  - **Statutaire employer cotis** (new hires after 31 May 2026): **10m 2026 / 284m 2029 / 365m 2030** (rate **9.5%→38%**); CoA: flat hire-volume hyp contradicts contract-prefer policy
  - **Combined Entity I influence 459m 2029** (gov claim)
  - **Departmental hit:** Justice **3.3m/61 FTE → 101m/1859 FTE** (622 judiciary); Defence **3.7→113.3m 2029 / 297m 2034**; Police **26 FTE → 700-821 FTE** capacity cut
  - **Specialty breaches:** Defence eng fully transferable **20.1bn**; Justice **2.5bn** + Police **1.6bn** free redistribute; inter-programme transfers **454m eng 2024**; provisions **2.13bn** CM transfer
  - Dual: droits d'auteur forfait remove **+30m**; VVPR hist **344→760m 2022-24**
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_430=done; spawn **rq_431**; ticks={TICK}
- FOI: none new (intermediate replace path optional later if annex absent; method residual not opacity)
- Next: prio5 **rq_431**; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log_entry.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")

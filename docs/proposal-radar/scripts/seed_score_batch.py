#!/usr/bin/env python3
"""Seed + score first calibration batch of 10 live Belgian proposals.

Run after research; writes proposals.csv, sources, analyses/*.md, history, state.
"""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RADAR = ROOT / "docs" / "proposal-radar"
DATA = RADAR / "data"
ANALYSES = RADAR / "analyses"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW[:10]

PROPOSAL_FIELDS = [
    "proposal_id", "title", "title_nl", "summary_one_line", "actor_name", "actor_role",
    "party_or_coalition", "jurisdiction", "competence_notes", "instrument_type", "status",
    "first_seen_date", "decision_date", "stated_goal", "mechanism_tag",
    "fiscal_static_min_eur", "fiscal_static_max_eur", "fiscal_basis", "fiscal_confidence",
    "clownpoints", "genius_score", "policy_index", "truth_problem", "mechanism_fit",
    "abundance_ev", "fiscal_honesty", "incentive_quality", "competence_fit",
    "evidence_quality", "capture_risk", "score_confidence", "analysis_version",
    "analysis_path", "primary_source_id", "doge_item_ids", "parent_proposal_id",
    "recommendation", "falsifier", "publish_ok", "created_utc", "updated_utc", "notes",
]

SOURCE_FIELDS = [
    "source_id", "title", "url", "publisher", "accessed_date", "source_class",
    "language", "proposal_ids", "notes",
]

HISTORY_FIELDS = [
    "history_id", "proposal_id", "analysis_version", "clownpoints", "genius_score",
    "policy_index", "score_confidence", "changed_reason", "recorded_utc",
]


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def memo(p: dict, body: str) -> str:
    return f"""# Analysis: {p['proposal_id']}

| Field | Value |
|-------|-------|
| **Title** | {p['title']} |
| **Actor** | {p['actor_name']} ({p['actor_role']}) |
| **Party / body** | {p['party_or_coalition']} |
| **Jurisdiction** | {p['jurisdiction']} |
| **Instrument** | {p['instrument_type']} |
| **Status** | {p['status']} |
| **First seen** | {p['first_seen_date']} |
| **Analysis version** | {p['analysis_version']} |
| **Primary source** | {p['primary_source_id']} |

---

## Steelman (proponent’s best case)

{body}

---

## Scores

| Public | Score |
|--------|-------|
| **Clownpoints** | {p['clownpoints']} |
| **Genius score** | {p['genius_score']} |
| **policy_index** | {p['policy_index']} |

| Subscore | Score |
|----------|-------|
| truth_problem | {p['truth_problem']} |
| mechanism_fit | {p['mechanism_fit']} |
| abundance_ev | {p['abundance_ev']} |
| fiscal_honesty | {p['fiscal_honesty']} |
| incentive_quality | {p['incentive_quality']} |
| competence_fit | {p['competence_fit']} |
| evidence_quality | {p['evidence_quality']} |
| capture_risk | {p['capture_risk']} |

**score_confidence:** {p['score_confidence']}

## Recommendation

`{p['recommendation']}`

## Falsifier

> {p['falsifier']}

## Fiscal

€{p['fiscal_static_min_eur']}–{p['fiscal_static_max_eur']} ({p['fiscal_basis']}, confidence {p['fiscal_confidence']})

## Notes

{p['notes']}

---
*Auto-scored calibration batch {TODAY}. Review welcome.*
"""


# fmt: off
BATCH = [
  {
    "proposal_id": "prop_2025_unemp_time_limit",
    "title": "Time-limit unemployment benefits (Arizona)",
    "title_nl": "Werkloosheidsuitkering in de tijd beperken",
    "summary_one_line": "Cap duration of UI to raise job search intensity and cut structural non-employment cost.",
    "actor_name": "Federal government De Wever I",
    "actor_role": "government",
    "party_or_coalition": "Arizona (N-VA, CD&V, Vooruit, MR, Les Engagés)",
    "jurisdiction": "federal",
    "competence_notes": "Social security / labour market federal",
    "instrument_type": "law",
    "status": "implemented",
    "first_seen_date": "2025-01-31",
    "decision_date": "2025-02-01",
    "stated_goal": "Raise employment rate; curb open-ended UI cost",
    "mechanism_tag": "incentive_duration|activation",
    "fiscal_static_min_eur": "",
    "fiscal_static_max_eur": "",
    "fiscal_basis": "unknown",
    "fiscal_confidence": "weak",
    "clownpoints": "2.0",
    "genius_score": "7.5",
    "policy_index": "5.5",
    "truth_problem": "8.5",
    "mechanism_fit": "8.0",
    "abundance_ev": "7.5",
    "fiscal_honesty": "5.5",
    "incentive_quality": "8.5",
    "competence_fit": "9.0",
    "evidence_quality": "7.0",
    "capture_risk": "3.0",
    "score_confidence": "medium",
    "analysis_version": "1",
    "primary_source_id": "src_ing_consol_2026",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "support",
    "falsifier": "We reverse if employment exit rates of long-term unemployed do not rise within 3 years while OCMW/CPAS caseloads absorb savings 1:1 without activation gain.",
    "publish_ok": "yes",
    "notes": "ING/CoA: gov assumes ~1/3 find work at end of entitlement; short-run may shift to other assistance. Structural direction correct; book static savings cautiously.",
    "memo_body": """Long-term open-ended UI in a high tax-wedge economy selects for non-work and burdens the productive base. A time limit (order of two years class, with activation) aligns private search incentives with social insurance purpose.

### 1 Problem
Belgium combines high labour tax wedge with large inactivity/UI stocks. **Strong/Medium** problem claim (OECD wedge + BE employment gap vs peers).

### 2 Mechanism
Duration elasticity of job search is a standard labour result. **mechanism_fit high**.

### 3 Options
A status quo unlimited · B time limit + activation (this) · C cut replacement rates · D wage subsidy · E public jobs · F pilot by region.

### 4–6 Evidence & fiscal
ING (2026-02) notes CoA scepticism on *speed* of savings and leakage to other schemes. Dynamic employment gains **Medium**; static year-1 savings **Weak** if booked fully.

### 7 Competence
Federal SS — correct level.

### 8 Rec
**Support** with honest dynamic accounting and OCMW monitoring. Not clown theatre: real incentive reform.""",
  },
  {
    "proposal_id": "prop_2025_cgt_capital_gains",
    "title": "Introduce capital gains tax (Arizona)",
    "title_nl": "Invoering meerwaardebelasting",
    "summary_one_line": "Tax capital gains to raise revenue and rebalance tax mix away from labour.",
    "actor_name": "Federal government De Wever I",
    "actor_role": "government",
    "party_or_coalition": "Arizona",
    "jurisdiction": "federal",
    "competence_notes": "Federal personal/corporate tax",
    "instrument_type": "tax",
    "status": "adopted",
    "first_seen_date": "2025-01-31",
    "decision_date": "2025-02-01",
    "stated_goal": "Fiscal consolidation + fairness vs labour taxation",
    "mechanism_tag": "tax_base|incidence",
    "fiscal_static_min_eur": "",
    "fiscal_static_max_eur": "",
    "fiscal_basis": "annual",
    "fiscal_confidence": "weak",
    "clownpoints": "4.5",
    "genius_score": "4.0",
    "policy_index": "-0.5",
    "truth_problem": "7.0",
    "mechanism_fit": "5.0",
    "abundance_ev": "4.0",
    "fiscal_honesty": "3.5",
    "incentive_quality": "4.0",
    "competence_fit": "8.0",
    "evidence_quality": "5.5",
    "capture_risk": "5.0",
    "score_confidence": "medium",
    "analysis_version": "1",
    "primary_source_id": "src_ing_consol_2026",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "amend",
    "falsifier": "We reverse toward support if a simple broad CGT with low rate and few exemptions raises predicted revenue within 10% for 2 consecutive years without measurable exit of mobile capital (Medium evidence bar).",
    "publish_ok": "yes",
    "notes": "ING: complex 'camel' design; CoA doubts yield. Principle of taxing capital income can be right; execution risk is the score drag.",
    "memo_body": """Steelman: labour is over-taxed; capital gains often lightly taxed; a clean CGT can fund labour tax cuts and consolidation.

### Reality check
Problem of labour-biased tax mix is **Strong**. But Arizona design described as complex coalition camel; Court of Audit / ING flag revenue shortfall vs forecasts. Without published simple rate+base, **fiscal_honesty low**.

### Mechanism
CGT can work if broad base, moderate rate, limited lock-in/exit. High exemptions + mobility → paper revenue, real distortion.

### Options
A status quo · B simple broad CGT + cut labour wedge · C this complex package · D wealth tax (worse) · E consumption tax shift · F pilot reporting only.

### Rec
**Amend** toward simplicity; do not celebrate revenue until realised. Mixed index: not pure clown, not genius.""",
  },
  {
    "proposal_id": "prop_2026_centenindex",
    "title": "Centenindex: temporary limit on automatic wage/pension indexation",
    "title_nl": "Centenindex — tijdelijke indexbeperking",
    "summary_one_line": "Temporarily cap automatic indexation (2026/2028 phases) to slow wage-price spiral and cut public wage bill.",
    "actor_name": "Federal programme law + Flemish implementation",
    "actor_role": "government",
    "party_or_coalition": "Arizona + Flanders execution",
    "jurisdiction": "multi",
    "competence_notes": "Federal law; regions implement for own staff",
    "instrument_type": "law",
    "status": "adopted",
    "first_seen_date": "2026-05-30",
    "decision_date": "2026-06-01",
    "stated_goal": "Wage moderation; public finance consolidation",
    "mechanism_tag": "indexation|nominal_anchor",
    "fiscal_static_min_eur": "",
    "fiscal_static_max_eur": "",
    "fiscal_basis": "annual",
    "fiscal_confidence": "medium",
    "clownpoints": "3.0",
    "genius_score": "6.0",
    "policy_index": "3.0",
    "truth_problem": "7.5",
    "mechanism_fit": "7.0",
    "abundance_ev": "6.0",
    "fiscal_honesty": "6.0",
    "incentive_quality": "5.5",
    "competence_fit": "8.0",
    "evidence_quality": "6.5",
    "capture_risk": "4.0",
    "score_confidence": "medium",
    "analysis_version": "1",
    "primary_source_id": "src_vl_mr_20260717",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "amend",
    "falsifier": "Reverse if real wage collapse for low earners exceeds inflation-protection goal without deficit improvement vs counterfactual within 2 years.",
    "publish_ok": "yes",
    "notes": "Programmawet 30 May 2026; Flanders VPS alignment on agenda 17 Jul 2026. Temporary partial freeze is more honest than fake dynamic growth assumptions; distributional design matters.",
    "memo_body": """Steelman: automatic full indexation of wages/pensions in a high-debt open economy amplifies cost-push inflation and public wage bills; temporary brake buys consolidation space.

### Problem
Structural deficit + indexation feedback — **Medium/Strong**.

### Mechanism
Nominal anchor / public wage moderation — **fit good**. Risk: if only public sector, dual market; if high earners only, fairness optics vs efficiency.

### Options
A full index · B temporary high-end freeze (this class) · C permanent reform of index basket · D VAT/excise only · E spending cuts without wage brake.

### Rec
**Amend** toward transparent temporary rule + protect bottom deciles; better than denying arithmetic. Solid not genius.""",
  },
  {
    "proposal_id": "prop_2021_company_car_ice_2026",
    "title": "Phase-out tax deductibility of fossil company cars from 2026",
    "title_nl": "Einde aftrek fossiele bedrijfswagens vanaf 2026",
    "summary_one_line": "Remove corporate tax deductibility for new ICE/hybrid company cars; keep path for zero-emission fleet greening.",
    "actor_name": "Federal legislator (2021 greening law)",
    "actor_role": "government",
    "party_or_coalition": "prior federal majority; still binding 2026",
    "jurisdiction": "federal",
    "competence_notes": "Federal corporate tax + mobility fiscality",
    "instrument_type": "tax",
    "status": "implemented",
    "first_seen_date": "2021-11-25",
    "decision_date": "2021-11-25",
    "stated_goal": "Electrify fleet; cut CO2 and large company-car tax expenditure",
    "mechanism_tag": "tax_expenditure|externality",
    "fiscal_static_min_eur": "500000000",
    "fiscal_static_max_eur": "1200000000",
    "fiscal_basis": "annual",
    "fiscal_confidence": "medium",
    "clownpoints": "1.5",
    "genius_score": "7.0",
    "policy_index": "5.5",
    "truth_problem": "9.0",
    "mechanism_fit": "8.0",
    "abundance_ev": "6.5",
    "fiscal_honesty": "7.0",
    "incentive_quality": "7.5",
    "competence_fit": "9.0",
    "evidence_quality": "8.0",
    "capture_risk": "4.0",
    "score_confidence": "strong",
    "analysis_version": "1",
    "primary_source_id": "src_fpb_company_cars",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "support",
    "falsifier": "Reverse if net fiscal + second-hand EV access effects are negative and congestion/externalities worsen vs counterfactual by 2029 (FPB-style evaluation).",
    "publish_ok": "yes",
    "notes": "Law 25 Nov 2021; FPB ex-ante ~€1bn class net revenue improvement from 2026. Still live policy surface in 2026. Residual clown risk: EV deductibility still a soft subsidy for high earners.",
    "memo_body": """Steelman: company cars are a massive Belgian tax expenditure that subsidises car ownership for higher earners; greening + phase-out of ICE deductibility attacks both climate externality and fiscal leak.

### Problem
**Strong** — large TE, known BE anomaly.

### Mechanism
Price signal on employer fleet choice — **high fit**. Side effects: wage packaging shift, EV grid/charging, used market flood (can be good).

### Evidence
FPB and tax literature document trajectory; revenue order-of-magnitude **Medium/Strong**.

### Rec
**Support** direction. Pair with labour tax cut if political space — convert TE kill into wage competitiveness.""",
  },
  {
    "proposal_id": "prop_2025_hybrid_car_rehab",
    "title": "Arizona soft rehab of hybrid company-car deductibility",
    "title_nl": "Gedeeltelijk herstel hybride-aftrek bedrijfswagens",
    "summary_one_line": "Extend/soften hybrid deductibility path (75% then step-down) vs pure 2026 ICE cliff.",
    "actor_name": "Federal government De Wever I",
    "actor_role": "government",
    "party_or_coalition": "Arizona",
    "jurisdiction": "federal",
    "competence_notes": "Federal tax",
    "instrument_type": "tax",
    "status": "announced",
    "first_seen_date": "2025-02-01",
    "decision_date": "2025-02-01",
    "stated_goal": "Practical transition; industry/employee bridge to EV",
    "mechanism_tag": "tax_expenditure|lobby_soften",
    "fiscal_static_min_eur": "",
    "fiscal_static_max_eur": "",
    "fiscal_basis": "annual",
    "fiscal_confidence": "weak",
    "clownpoints": "6.5",
    "genius_score": "3.0",
    "policy_index": "-3.5",
    "truth_problem": "5.0",
    "mechanism_fit": "3.5",
    "abundance_ev": "3.0",
    "fiscal_honesty": "4.0",
    "incentive_quality": "2.5",
    "competence_fit": "8.0",
    "evidence_quality": "5.0",
    "capture_risk": "7.5",
    "score_confidence": "medium",
    "analysis_version": "1",
    "primary_source_id": "src_vialto_arizona_hybrid",
    "doge_item_ids": "",
    "parent_proposal_id": "prop_2021_company_car_ice_2026",
    "recommendation": "reject",
    "falsifier": "Support if independent evaluation shows hybrid path cuts TE cost and emissions faster than pure EV cliff without rebound ICE-like use (unlikely bar).",
    "publish_ok": "yes",
    "notes": "Undoes part of a rare good TE reform under lobby/transition rhetoric. Classic capture risk.",
    "memo_body": """Steelman: pure 2026 cliff may strand fleets, hurt SMEs, and over-rely on EV supply; hybrids are a bridge.

### Critique
Bridge rhetoric often reopens the TE hole that made BE company cars infamous. Mechanism fights the greening law's price signal. **Capture risk high**.

### Options
A hold cliff · B temporary SME-only lease grandfather · C this broad hybrid soft path · D cash-out company car into higher net wage.

### Rec
**Reject** broad rehab. Prefer transparent short grandfather over multi-year hybrid subsidy path.""",
  },
  {
    "proposal_id": "prop_2026_vl_syntra_49m",
    "title": "Flanders Syntrum/Syntra funding €49.7m (2026-27 transition year)",
    "title_nl": "Syntrum/Syntra financiering 49,7 mio",
    "summary_one_line": "Continue entrepreneurship training network funding while reforming governance/central steering.",
    "actor_name": "Matthias Diependaele / Vlaamse Regering",
    "actor_role": "minister",
    "party_or_coalition": "Flemish government",
    "jurisdiction": "flanders",
    "competence_notes": "Education/training regional",
    "instrument_type": "subsidy",
    "status": "adopted",
    "first_seen_date": "2026-07-17",
    "decision_date": "2026-07-17",
    "stated_goal": "Quality entrepreneurship training; network reform",
    "mechanism_tag": "training_subsidy|agency",
    "fiscal_static_min_eur": "49700000",
    "fiscal_static_max_eur": "49700000",
    "fiscal_basis": "one_off",
    "fiscal_confidence": "strong",
    "clownpoints": "4.0",
    "genius_score": "4.5",
    "policy_index": "0.5",
    "truth_problem": "5.5",
    "mechanism_fit": "5.0",
    "abundance_ev": "4.5",
    "fiscal_honesty": "7.5",
    "incentive_quality": "4.5",
    "competence_fit": "8.0",
    "evidence_quality": "6.0",
    "capture_risk": "6.0",
    "score_confidence": "medium",
    "analysis_version": "1",
    "primary_source_id": "src_vl_mr_20260717",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "watch",
    "falsifier": "Support more strongly if reform publishes unit-cost + placement outcomes and cuts permanent overhead 15%+ by 2028.",
    "publish_ok": "yes",
    "notes": "Primary: Belga Share VL ministerraad 17 Jul 2026. Transition year with reform narrative — score neutral until outcomes published.",
    "memo_body": """Steelman: SME entrepreneurship training has positive externalities; a transition year avoids service collapse while centralising governance for efficiency.

### Problem
Training quality/fragmentation — **Weak/Medium** without published outcome KPIs.

### Mechanism
Block grant to network — weak unless tied to placement/skill metrics. Reform promise is the only genius-adjacent part.

### Rec
**Watch**. Fiscal honesty good (clear €49.7m). Not circus; not transformative until KPIs.""",
  },
  {
    "proposal_id": "prop_2026_wk_veldrijden_ostend",
    "title": "Project subsidy max €350k for 2027 CX World Championships Ostend",
    "title_nl": "Projectsubsidie WK veldrijden Oostende 2027",
    "summary_one_line": "Qualify UCI CX Worlds as Flemish top event; grant ≤€350k to Flanders Classics.",
    "actor_name": "Diependaele / Depraetere / De Ridder",
    "actor_role": "minister",
    "party_or_coalition": "Flemish government",
    "jurisdiction": "flanders",
    "competence_notes": "Tourism/sport regional",
    "instrument_type": "subsidy",
    "status": "adopted",
    "first_seen_date": "2026-07-17",
    "decision_date": "2026-07-17",
    "stated_goal": "Top sporting event; tourism/image",
    "mechanism_tag": "event_subsidy|prestige",
    "fiscal_static_min_eur": "350000",
    "fiscal_static_max_eur": "350000",
    "fiscal_basis": "one_off",
    "fiscal_confidence": "strong",
    "clownpoints": "7.0",
    "genius_score": "2.0",
    "policy_index": "-5.0",
    "truth_problem": "3.0",
    "mechanism_fit": "2.5",
    "abundance_ev": "2.0",
    "fiscal_honesty": "8.0",
    "incentive_quality": "2.0",
    "competence_fit": "7.0",
    "evidence_quality": "6.5",
    "capture_risk": "7.0",
    "score_confidence": "strong",
    "analysis_version": "1",
    "primary_source_id": "src_vl_mr_20260717",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "reject",
    "falsifier": "Support if independent ex-post shows net tax revenue > grant + congestion costs with additionality (event would not occur privately).",
    "publish_ok": "yes",
    "notes": "Classic prestige sports subsidy. Amount small vs budget; principle and capture matter for clownpoints.",
    "memo_body": """Steelman: Flanders is CX heartland; Worlds bring visitors, soft power, and private co-spend.

### Critique
Event subsidies routinely fail additionality tests; organisers capture grant; locals bear congestion. €350k is small enough that **fiscal harm is limited** but **incentive quality is poor** — public cash for a private sports product with ticket/TV value.

### Rec
**Reject** as default. Prefer zero subsidy + municipal facilitation only. High clownpoints for mechanism, not for size.""",
  },
  {
    "proposal_id": "prop_2022_smaakhaven_38m",
    "title": "Smaakhaven (Vlaams Culinair Centrum) — €38m relance subsidy trail",
    "title_nl": "Smaakhaven Antwerpen — 38 mio relance",
    "summary_one_line": "Large tourism/gastronomy experience centre funded from relance; 2026 erfpacht continuation.",
    "actor_name": "Flemish government / Toerisme Vlaanderen / City of Antwerp",
    "actor_role": "government",
    "party_or_coalition": "Flanders multi-legislature",
    "jurisdiction": "flanders",
    "competence_notes": "Tourism / local partnership",
    "instrument_type": "subsidy",
    "status": "implemented",
    "first_seen_date": "2022-12-01",
    "decision_date": "2026-07-17",
    "stated_goal": "Culinary innovation hub; international food brand",
    "mechanism_tag": "prestige_infra|tourism_subsidy",
    "fiscal_static_min_eur": "38000000",
    "fiscal_static_max_eur": "38000000",
    "fiscal_basis": "multi_year_envelope",
    "fiscal_confidence": "strong",
    "clownpoints": "8.0",
    "genius_score": "1.5",
    "policy_index": "-6.5",
    "truth_problem": "2.5",
    "mechanism_fit": "2.0",
    "abundance_ev": "1.5",
    "fiscal_honesty": "6.5",
    "incentive_quality": "1.5",
    "competence_fit": "6.0",
    "evidence_quality": "7.0",
    "capture_risk": "8.0",
    "score_confidence": "strong",
    "analysis_version": "1",
    "primary_source_id": "src_vl_mr_20260717",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "reject",
    "falsifier": "Reverse if audited visitor TCO and private ROIC beat alternative uses of €38m (housing/tax cut) by 2029.",
    "publish_ok": "yes",
    "notes": "Relance 2022 envelope still live via 40y erfpacht approval Jul 2026. Top clown candidate this batch.",
    "memo_body": """Steelman: food sector is a Flanders strength; a flagship centre could cluster training, tourism, and exports.

### Critique
€38m public relance into a culinary experience centre is textbook **prestige infrastructure**. Opportunity cost vs housing supply, labour tax wedge, or null. Capture by city/sector coalitions high. 2026 still spends political/admin capital on erfpacht — sunk cost fallacy risk.

### Rec
**Reject** further public top-ups; sunset evaluation mandatory. High clownpoints.""",
  },
  {
    "proposal_id": "prop_2026_dolphin_ban_2036",
    "title": "Ban keeping cetaceans in captivity by end-2036 (Flanders)",
    "title_nl": "Verbod walvisachtigen in gevangenschap tegen 2036",
    "summary_one_line": "Phase out dolphinaria (Boudewijn Seapark class) with rehab exception for wild injured animals.",
    "actor_name": "Ben Weyts / Vlaamse Regering",
    "actor_role": "minister",
    "party_or_coalition": "Flemish government",
    "jurisdiction": "flanders",
    "competence_notes": "Animal welfare community/region",
    "instrument_type": "ban",
    "status": "tabled",
    "first_seen_date": "2026-07-17",
    "decision_date": "2026-07-17",
    "stated_goal": "Animal welfare; end captivity stress",
    "mechanism_tag": "ban|preference",
    "fiscal_static_min_eur": "0",
    "fiscal_static_max_eur": "5000000",
    "fiscal_basis": "unknown",
    "fiscal_confidence": "speculative",
    "clownpoints": "3.5",
    "genius_score": "3.5",
    "policy_index": "0.0",
    "truth_problem": "6.0",
    "mechanism_fit": "7.0",
    "abundance_ev": "2.5",
    "fiscal_honesty": "5.0",
    "incentive_quality": "5.0",
    "competence_fit": "8.5",
    "evidence_quality": "5.5",
    "capture_risk": "3.0",
    "score_confidence": "medium",
    "analysis_version": "1",
    "primary_source_id": "src_vl_mr_20260717",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "watch",
    "falsifier": "Reject if welfare science shows managed captivity superior for existing animals and ban causes worse outcomes (export/kill).",
    "publish_ok": "yes",
    "notes": "Preference/values policy more than abundance engine. Long phase-out (to 2036) reduces transition cruelty. Not fiscal core.",
    "memo_body": """Steelman: cetaceans suffer in tanks; public values shifted; long sunset respects operators' capital while ending the practice.

### Framing
This is largely a **preference / ethics** policy, not a growth reform. Abundance impact near-zero. Mechanism (ban with sunset) fits the stated welfare goal better than sudden confiscation.

### Rec
**Watch** — acceptable if no large compensation circus; don't pretend it's an economic strategy. Mid scores.""",
  },
  {
    "proposal_id": "prop_2026_fwb_budget_cuts_255m",
    "title": "FWB 2026 budget: ~€255m savings package",
    "title_nl": "FWB begroting 2026: ~255 mio besparingen",
    "summary_one_line": "Community budget consolidation touching education, culture, school meals; higher tuition signals in package debate.",
    "actor_name": "Gouvernement Fédération Wallonie-Bruxelles",
    "actor_role": "government",
    "party_or_coalition": "FWB government",
    "jurisdiction": "fwb",
    "competence_notes": "Community education/culture",
    "instrument_type": "envelope",
    "status": "adopted",
    "first_seen_date": "2025-12-17",
    "decision_date": "2025-12-17",
    "stated_goal": "Control FWB deficit; multi-year path",
    "mechanism_tag": "spending_cut|package",
    "fiscal_static_min_eur": "255000000",
    "fiscal_static_max_eur": "255000000",
    "fiscal_basis": "annual",
    "fiscal_confidence": "medium",
    "clownpoints": "3.5",
    "genius_score": "5.0",
    "policy_index": "1.5",
    "truth_problem": "8.0",
    "mechanism_fit": "5.5",
    "abundance_ev": "5.0",
    "fiscal_honesty": "6.0",
    "incentive_quality": "5.0",
    "competence_fit": "8.0",
    "evidence_quality": "5.5",
    "capture_risk": "5.0",
    "score_confidence": "medium",
    "analysis_version": "1",
    "primary_source_id": "src_fwb_budget_2026_press",
    "doge_item_ids": "",
    "parent_proposal_id": "",
    "recommendation": "amend",
    "falsifier": "Support more if cuts hit low-ROI admin/culture middlemen first and protect high-ROI skills/STEM while deficit path hits published targets 2026-27.",
    "publish_ok": "yes",
    "notes": "Press: €255m economies adopted Dec 2025. Package score — child measures differ; prefer cutting bureaucracy over pure human-capital thinning.",
    "memo_body": """Steelman: FWB faces structural deficit; without consolidation, debt service crowds education quality later. Early package is responsible.

### Critique
Consolidation **direction right** (**truth_problem high**). Quality depends on *what* is cut: free meal optics vs admin dual structures vs tuition. Package opacity → mid genius. Raising minerval can be good price signal if paired with targeted grants; blunt culture cuts may be low ROI or high signal.

### Rec
**Amend** toward transparent L5 cut list and protect measurable learning outcomes.""",
  },
]
# fmt: on


SOURCES = [
    {
        "source_id": "src_ing_consol_2026",
        "title": "Fiscal consolidation in Belgium: you can't have it both ways",
        "url": "https://think.ing.com/articles/fiscal-consolidation-in-belgium-you-cant-have-it-both-ways/",
        "publisher": "ING THINK",
        "accessed_date": TODAY,
        "source_class": "think_tank",
        "language": "en",
        "proposal_ids": "prop_2025_unemp_time_limit|prop_2025_cgt_capital_gains|prop_2026_centenindex",
        "notes": "CoA critique + lists Arizona measures",
    },
    {
        "source_id": "src_vl_mr_20260717",
        "title": "Beslissingen van de ministerraad van 17 juli 2026",
        "url": "https://www.belgashare.be/nl/newsrooms/126/press-releases/34899/",
        "publisher": "Vlaamse Overheid / Belga Share",
        "accessed_date": TODAY,
        "source_class": "gov_press",
        "language": "nl",
        "proposal_ids": "prop_2026_vl_syntra_49m|prop_2026_wk_veldrijden_ostend|prop_2022_smaakhaven_38m|prop_2026_dolphin_ban_2036|prop_2026_centenindex",
        "notes": "Primary-adjacent official decision list",
    },
    {
        "source_id": "src_fpb_company_cars",
        "title": "Ex ante evaluation of the reform of company car taxation in Belgium",
        "url": "https://www.plan.be/en/publications/ex-ante-evaluation-reform-company-car-taxation",
        "publisher": "Federal Planning Bureau",
        "accessed_date": TODAY,
        "source_class": "audit",
        "language": "en",
        "proposal_ids": "prop_2021_company_car_ice_2026",
        "notes": "~€1bn class net revenue path",
    },
    {
        "source_id": "src_vialto_arizona_hybrid",
        "title": "Birth of the Arizona Coalition & De Wever I — hybrid car deductibility path",
        "url": "https://vialtopartners.com/regional-alerts/belgium-global-mobility-tax-birth-of-the-arizona-coalition-de-wever-i-federal-government-agreement-2025-2029",
        "publisher": "Vialto Partners",
        "accessed_date": TODAY,
        "source_class": "press",
        "language": "en",
        "proposal_ids": "prop_2025_hybrid_car_rehab",
        "notes": "Secondary legal briefing on hybrid path",
    },
    {
        "source_id": "src_fwb_budget_2026_press",
        "title": "FWB budget 2026 adopted — ~€255m savings",
        "url": "https://www.rtl.be/actu/belgique/politique/quelque-255-millions-deuros-deconomies-le-budget-2026-de-la-fwb-adopte-apres-une/2025-12-17/article/773836",
        "publisher": "RTL Info",
        "accessed_date": TODAY,
        "source_class": "press",
        "language": "fr",
        "proposal_ids": "prop_2026_fwb_budget_cuts_255m",
        "notes": "Press secondary; amount class medium",
    },
    {
        "source_id": "src_politico_budget_deal",
        "title": "Belgium avoids government collapse as Bart De Wever strikes budget deal",
        "url": "https://www.politico.eu/article/bart-de-wever-belgium-budget-deal-avoids-government-collapse/",
        "publisher": "Politico",
        "accessed_date": TODAY,
        "source_class": "press",
        "language": "en",
        "proposal_ids": "prop_2025_unemp_time_limit|prop_2025_cgt_capital_gains",
        "notes": "€9.2bn path by 2029 context",
    },
]


def main() -> int:
    ANALYSES.mkdir(parents=True, exist_ok=True)
    rows = []
    history = []
    for p in BATCH:
        p = dict(p)
        body = p.pop("memo_body")
        p["analysis_path"] = f"analyses/{p['proposal_id']}.md"
        p["created_utc"] = NOW
        p["updated_utc"] = NOW
        (ANALYSES / f"{p['proposal_id']}.md").write_text(memo(p, body), encoding="utf-8")
        rows.append(p)
        history.append(
            {
                "history_id": f"hist_{p['proposal_id']}_v1",
                "proposal_id": p["proposal_id"],
                "analysis_version": "1",
                "clownpoints": p["clownpoints"],
                "genius_score": p["genius_score"],
                "policy_index": p["policy_index"],
                "score_confidence": p["score_confidence"],
                "changed_reason": "initial_calibration_batch",
                "recorded_utc": NOW,
            }
        )

    write_csv(DATA / "proposals.csv", PROPOSAL_FIELDS, rows)
    # merge sources with any existing rss sources
    existing_src = []
    sp = DATA / "sources.csv"
    if sp.exists():
        with sp.open(encoding="utf-8", newline="") as f:
            existing_src = list(csv.DictReader(f))
    by_id = {s.get("source_id"): s for s in existing_src if s.get("source_id")}
    for s in SOURCES:
        by_id[s["source_id"]] = s
    write_csv(DATA / "sources.csv", SOURCE_FIELDS, list(by_id.values()))
    write_csv(DATA / "score_history.csv", HISTORY_FIELDS, history)

    write_csv(
        DATA / "loop_state.csv",
        ["state_id", "mode", "last_tick_utc", "last_unit_id", "ticks_completed", "proposals_scored", "paused", "notes"],
        [{
            "state_id": "main",
            "mode": "analyse",
            "last_tick_utc": NOW,
            "last_unit_id": "calibration_batch_10",
            "ticks_completed": "1",
            "proposals_scored": str(len(rows)),
            "paused": "no",
            "notes": "First auto batch: 10 live BE proposals scored for human review",
        }],
    )

    # mark RSS noise as rejected where non-BE
    ingest_path = DATA / "ingest_queue.csv"
    if ingest_path.exists():
        with ingest_path.open(encoding="utf-8", newline="") as f:
            ingest = list(csv.DictReader(f))
        fields = list(ingest[0].keys()) if ingest else []
        for r in ingest:
            title = (r.get("title_hint") or "").lower()
            if any(x in title for x in ("trump", "netanyahu", "mallorca", "shein", "frankfurt", "onyedika", "new york", "iran", "smithsonian")):
                r["status"] = "rejected_noise"
                r["updated_utc"] = NOW
                r["notes"] = (r.get("notes") or "") + "; auto_reject_non_be"
        if fields:
            write_csv(ingest_path, fields, ingest)

    print(f"Wrote {len(rows)} proposals + memos")
    for r in sorted(rows, key=lambda x: -float(x["clownpoints"])):
        print(f"  clown {r['clownpoints']:>4} genius {r['genius_score']:>4} idx {r['policy_index']:>5}  {r['proposal_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

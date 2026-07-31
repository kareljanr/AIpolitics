# tick392: Federal police I-Police cancel + section17 + NATO defence 2pct path
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T10:45:00Z"
TICK = 392
UNIT = "rq_383"
GAP = "gap_ipolice_claim_l5"


def append_rows(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as f:
        fields = csv.DictReader(f).fieldnames
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def rewrite(path: Path, rows: list[dict], fields: list[str]):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


# entity for federal police if missing
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    efields = list(r.fieldnames)
    ents = list(r)
if not any(e.get("entity_id") == "police_federale" for e in ents):
    ents.append(
        {
            "entity_id": "police_federale",
            "name_nl": "Federale Politie",
            "name_fr": "Police federale",
            "name_en": "Federal Police",
            "level": "agency",
            "parent_id": "sec_federal",
            "community_language": "bi",
            "website": "https://www.police.be",
            "foi_email": "",
            "foi_postal": "",
            "notes": "Section 17; FTE 13980 end-2025; I-Police cancelled; tick392",
        }
    )
    rewrite(DATA / "entities.csv", ents, efields)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_ccrek_budget2026_police_defence",
            "title": "Cour des comptes budget Etat 2026 — Police federale I-Police + NATO 2pct defence path",
            "url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-01",
            "source_class": "primary_audit",
            "notes": "I-Police liquidated 76.7 of 299m cancelled; claim 228.1m; NATO 13.1bn 2026; defence liq 10.77bn; FTE 13980",
        },
    ],
)

budgets = []


def add(y, bid, amt, note, ent="police_federale", conf="strong", basis="budgeted"):
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ent,
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": "src_ccrek_budget2026_police_defence",
            "confidence": conf,
            "notes": note,
        }
    )


# Police personnel / FTE
add(2021, "bud_police_fed_fte_2021", 13962, "Federal police FTE 13962 end-2021 (COUNT)", basis="outturn")
add(2025, "bud_police_fed_fte_2025", 13980, "Federal police FTE 13980 end-2025 (COUNT; +18 vs 2021 despite +600 ETP votes)", basis="outturn")
add(2026, "bud_police_fed_fte_target_2026", 14280, "Strategic FTE target 14280 2026 (+300 net; 115 fraud+federal prosecutor finance)", basis="budgeted", conf="medium")
add(2026, "bud_police_fed_napap_2026", 15600000, "Napap early-career police federal 15.6m 2026 (underfund >3m non-indexed since 2022)", conf="medium")
add(2026, "bud_police_fed_napap_under_2026", 3000000, "Napap underfunding >3m 2026 class", conf="medium")
add(2026, "bud_police_fed_ops_from_prov_2026", 87500000, "Ops credits +87.5m from security provision 2026 (structural underfunding ops)")
add(2025, "bud_police_fed_ops_prov_engaged_2025", 60700000, "Engaged from security provision ops 60.7m 2025 (IT vehicles grandes villes)", basis="outturn")
add(2025, "bud_police_fed_ops_prov_residual_2025", 26800000, "Unspent security provision ops residual 26.8m 2025 carryable", basis="outturn")
add(2026, "bud_police_grandes_villes_cumul_2025_29", 43600000, "Plan Grandes Villes federal police needs 43.6m cumul 2025-2029 (11 need types)")
add(2026, "bud_police_grandes_villes_eng_2026", 9900000, "Grandes Villes engagement 9.9m 2026")
add(2026, "bud_police_grandes_villes_liq_2026", 13200000, "Grandes Villes liquidation 13.2m 2026")

# I-Police
add(2026, "bud_ipolice_initial_envelope", 299000000, "I-Police initial planned envelope 299m (cancelled end-2025)", basis="budgeted", conf="strong")
add(2026, "bud_ipolice_liquidated_202601", 76700000, "I-Police liquidated 76.7m of 299m as of Fedcom 26 Jan 2026 (outturn)", basis="outturn")
add(2026, "bud_ipolice_claim_total_2026", 228100000, "Police claim on vendor 228.1m 2026 (49.9 invoices + 178.5 damages) — claim not cash", conf="medium", basis="estimate")
add(2026, "bud_ipolice_claim_invoices_2026", 49900000, "Claim: resolution paid invoices 49.9m", conf="medium", basis="estimate")
add(2026, "bud_ipolice_claim_damages_2026", 178500000, "Claim: additional damages severe failings 178.5m", conf="medium", basis="estimate")
add(2026, "bud_ipolice_claim_consultants_2026", 20600000, "Damages breakdown: external consultants 20.6m", conf="medium", basis="estimate")
add(2026, "bud_ipolice_claim_infra_2026", 7900000, "Damages: infrastructure 7.9m", conf="medium", basis="estimate")
add(2026, "bud_ipolice_claim_staff_2026", 1000000, "Damages: judicial police staff treatments 1.0m", conf="medium", basis="estimate")
add(2026, "bud_ipolice_claim_lost_gain_2026", 149000000, "Damages: lost expected programme gain 149m (largest; soft)", conf="weak", basis="estimate")
add(2026, "bud_ipolice_prog_eng_2026", 7800000, "Prog 17.80.4 residual eng 7.8m 2026 (other digitalisation Focus etc after cancel)")
add(2026, "bud_ipolice_prog_liq_2026", 15100000, "Prog 17.80.4 residual liq 15.1m 2026")

# Defence NATO
add(2025, "bud_nato_effort_2025", 12725700000, "NATO defence effort total 12725.7m 2025 (~2.0pct GDP)", ent="mod_defensie", basis="outturn")
add(2026, "bud_nato_effort_2026", 13095800000, "NATO defence effort total 13095.8m 2026 (99.9pct of 2pct)", ent="mod_defensie")
add(2027, "bud_nato_effort_2027", 13573100000, "NATO effort 13573.1m 2027", ent="mod_defensie", conf="medium")
add(2028, "bud_nato_effort_2028", 13950000000, "NATO effort 13950.0m 2028", ent="mod_defensie", conf="medium")
add(2029, "bud_nato_effort_2029", 14289700000, "NATO effort 14289.7m 2029", ent="mod_defensie", conf="medium")
add(2025, "bud_defence_s16_liq_2025", 10485800000, "Defence section 16 liquidations 10485.8m 2025", ent="mod_defensie", basis="outturn")
add(2026, "bud_defence_s16_liq_2026", 10769600000, "Defence section 16 liquidations 10769.6m 2026", ent="mod_defensie")
add(2025, "bud_nato_external_2025", 2239900000, "External defence effort 2239.9m 2025 (pensions+other depts+std)", ent="mod_defensie", basis="outturn")
add(2026, "bud_nato_external_2026", 2326200000, "External defence effort 2326.2m 2026", ent="mod_defensie")
add(2026, "bud_nato_pens_military_2026", 1688000000, "Military pensions in NATO effort 1688m 2026", ent="fpd")
add(2026, "bud_nato_pens_civil_2026", 73000000, "Civil defence pensions 73m 2026", ent="fpd")
add(2026, "bud_nato_pens_survivor_2026", 267000000, "Survivor defence pensions 267m 2026", ent="fpd")
add(2026, "bud_nato_other_depts_2026", 130700000, "Other departments military spend 130.7m 2026", ent="mod_defensie")
add(2026, "bud_nato_standardisation_2026", 167500000, "Standardisation (incl conscript pensions 167.5m) 2026", ent="mod_defensie")
add(2025, "bud_nato_norm_2pct_2025", 12726400000, "NATO 2pct of GDP target 12726.4m 2025", ent="mod_defensie", basis="outturn")
add(2026, "bud_nato_norm_2pct_2026", 13107100000, "NATO 2pct target 13107.1m 2026", ent="mod_defensie")
add(2026, "bud_nato_extra_spend_2026", 3522000000, "Additional defence spend plan 3522m 2026 (of 16783 total 2025-29)", ent="mod_defensie")
add(2025, "bud_nato_extra_spend_2025_29", 16783000000, "Additional defence spend package 16783m 2025-2029", ent="mod_defensie")
add(2026, "bud_nato_temp_fin_2026", 1663000000, "Temporary financing 1663m 2026 (CIT Russian assets 1163 + Belfius div 500)", ent="mod_defensie")
add(2026, "bud_nato_cit_russian_2026", 1163000000, "CIT on frozen Russian assets financing 1163m 2026", ent="sec_federal")
add(2026, "bud_nato_belfius_div_2026", 500000000, "Belfius exceptional dividend 500m 2026 defence financing", ent="sec_federal")
add(2026, "bud_nato_struct_fin_2026", 400000000, "Structural financing defence 400m 2026 (of path to 1750 in 2029)", ent="mod_defensie")
add(2026, "bud_nato_deficit_temp_2026", 1459000000, "Temporarily higher deficit for defence 1459m 2026", ent="mod_defensie", conf="medium")

# DGD development coop
add(2025, "bud_dgd_liq_2025", 1129300000, "Development coop liquidation credits 1129.3m 2025", ent="sec_federal", basis="budgeted")
add(2026, "bud_dgd_liq_2026", 1040300000, "Development coop liq 1040.3m 2026 (-89m)", ent="sec_federal")
add(2027, "bud_dgd_liq_2027", 957000000, "Development coop liq path 957m 2027", ent="sec_federal", conf="medium")
add(2026, "bud_dgd_fad17_2026", 64200000, "African Development Fund 17th replenishment voluntary 64.2m engage 2026 pay over 10y", ent="sec_federal")

# FPS Finance
add(2026, "bud_finance_credits_2026", 2400000000, "SPF Finances credits 2.4bn 2026 (-2.8bn vs prior; IMF quota one-off ends)", ent="fod_finance")
add(2026, "bud_finance_personnel_2026", 1561500000, "SPF Finances personnel 1561.5m 2026", ent="fod_finance")
add(2026, "bud_finance_it_delta_2026", 68800000, "SPF Finances IT increase +68.8m 2026 (compliance 20.8 + e-com/customs 42.5)", ent="fod_finance")
add(2026, "bud_finance_ccei_scanners_2026", 22600000, "CCEI new-gen scanners 22.6m 2026 (EU cofinance; 9m prepay 2025)", ent="fod_finance")
add(2026, "bud_esm_capital_2026", 216200000, "ESM capital key adjustment extra 216.2m 2026 (underestimation risk CoA)", ent="fod_finance", conf="medium")
add(2026, "bud_antifraud_fiscal_target_2026", 300000000, "Fiscal fraud fight revenue target 300m 2026 (to 600m 2029; plan not yet finalised)", ent="fod_finance", conf="weak")
add(2026, "bud_admin_reform_save_path", 300000000, "Federal admin reorganisation savings path 300m by end legislature (not objectified CoA)", ent="sec_federal", conf="weak")

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets))

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "cmt_ipolice_cancelled_2025",
            "title": "I-Police IT modernisation cancelled after 76.7m spent of 299m",
            "entity_id": "police_federale",
            "beneficiary": "Federal police IT vendor (contract suspended)",
            "legal_basis": "Section 17.80.4; Interior minister decision end-2025",
            "decision_date": "2025-12-01",
            "start_year": 2020,
            "end_year": 2025,
            "total_envelope_eur": 299000000,
            "cash_by_year": '{"liq_to_2026_01":76700000}',
            "remaining_eur": 0,
            "status": "cancelled",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "stated_goal": "Modernise police IT applications (replaced multiple legacy systems)",
            "cut_option": "Recover claim; publish post-mortem; residual digitalisation 7.8/15.1m 2026",
            "source_id": "src_ccrek_budget2026_police_defence",
            "confidence": "strong",
            "hierarchy_path": "Federal>Police>I-Police",
            "notes": "tick392: 76.7m liquidated; claim 228.1m (lost gain 149m soft); FOI claim status",
        },
        {
            "commitment_id": "cmt_nato_2pct_2025_2029",
            "title": "NATO 2pct GDP defence effort path 2025-2029",
            "entity_id": "mod_defensie",
            "beneficiary": "Belgian defence + dual pensions/other depts",
            "legal_basis": "CM 11 Apr 2025 Easter accord Plan de defense; NATO 2pct",
            "decision_date": "2025-04-11",
            "start_year": 2025,
            "end_year": 2029,
            "total_envelope_eur": 67634300000,
            "cash_by_year": '{"2025":12725700000,"2026":13095800000,"2027":13573100000,"2028":13950000000,"2029":14289700000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "stated_goal": "Meet NATO 2pct GDP defence spending",
            "cut_option": "Track standardisation growth; dual capacity contracts FOI residual",
            "source_id": "src_ccrek_budget2026_police_defence",
            "confidence": "strong",
            "hierarchy_path": "Federal>Defence>NATO_2pct",
            "notes": "tick392: s16 10.77bn of 13.10bn 2026; std 167.5m miliciens; extra 16.8bn package 25-29",
        },
    ],
)

lbs = [
    (
        "lb_ipolice_spent_77m_cancelled",
        "I-Police IT project 76.7m spent then cancelled",
        76700000,
        "Strong CoA: 76.7m of 299m liquidated; contract suspended end-2025; residual digital 15.1m liq 2026",
        9.0,
        5.5,
        4,
        6.85,
        "Recover claim; public post-mortem; stop soft lost-gain accounting",
        "ops",
    ),
    (
        "lb_ipolice_claim_228m",
        "I-Police vendor claim 228.1m (49.9+178.5 damages)",
        228100000,
        "Medium: police demand 228.1m incl lost gain 149m soft; consultants 20.6 infra 7.9 staff 1.0",
        8.5,
        7.0,
        6,
        6.70,
        "Litigate hard costs only; FOI claim status and settlement",
        "ops",
    ),
    (
        "lb_nato_effort_13_1bn_2026",
        "NATO defence effort 13.10bn 2026 (~2pct GDP)",
        13095800000,
        "Strong: total effort 13095.8m; s16 liq 10769.6; external 2326 (pens+std)",
        2,
        9.5,
        3,
        6.55,
        "Core alliance spend; dual capacity cash FOI residual",
        "ops",
    ),
    (
        "lb_defence_s16_10_77bn_2026",
        "Defence section 16 liquidations 10.77bn 2026",
        10769600000,
        "Strong: 10769.6m; 82.2pct of NATO effort; path from 10486 2025",
        2,
        9.5,
        3,
        6.55,
        "Publish major contract cash-by-year",
        "ops",
    ),
    (
        "lb_nato_extra_16_8bn_2025_29",
        "Additional defence spend package 16.78bn 2025-2029",
        3522000000,
        "Strong plan: 16783m extra; 2026 slice 3522m; temp fin CIT+Belfius + structural + deficit",
        3,
        8.5,
        4,
        6.13,
        "Track temporary vs structural financing mix",
        "ops",
    ),
    (
        "lb_police_fte_flat_14k",
        "Federal police FTE flat ~14k despite +600 ETP votes",
        13980,
        "Strong: 13980 end-2025 vs 13962 2021; recruitment lag; target 14280 2026",
        6,
        3.0,
        5,
        4.75,
        "Publish recruitment unit cost vs attrition",
        "ops",
    ),
    (
        "lb_police_ops_prov_87_5m_2026",
        "Police ops top-up from security provision 87.5m 2026",
        87500000,
        "Strong: structural ops underfunding via provision (CoA: provision unjustified if amount preset)",
        5,
        5.5,
        4,
        5.55,
        "Move to structural section 17 line",
        "ops",
    ),
    (
        "lb_dgd_cut_path_1_04bn_2026",
        "Development cooperation liq 1.04bn 2026 (cut path)",
        1040300000,
        "Strong: 1040.3m vs monitoring 1252.6; gap 212m; FAD17 64.2m over 10y",
        4,
        8.0,
        4,
        6.00,
        "Publish new-commitment freeze list L5",
        "transfer",
    ),
]
lb_rows = []
for iid, name, cost, tco, ab, cs, df, pi, cut, typ in lbs:
    # annual for FTE count is weird - use 0 annual cost for FTE or keep as ops opacity
    ann = cost if iid != "lb_police_fte_flat_14k" else 0
    lb_rows.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": "Federal>Police>" + iid if "police" in iid or "ipolice" in iid else "Federal>Defence>" + iid,
            "annual_cost_eur": ann if ann else "",
            "total_cost_eur": cost if "fte" not in iid else "",
            "tco_notes": tco + ("; FTE count not EUR" if "fte" in iid else ""),
            "confidence": "strong" if "Weak" not in tco and "weak" not in tco and "Medium" not in tco[:10] else ("medium" if "Medium" in tco or "medium" in tco else "strong"),
            "source_id": "src_ccrek_budget2026_police_defence",
            "beneficiaries": "Police / defence / development partners",
            "stated_goal": "Public security defence development",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick392",
        }
    )
# fix confidences manually
for r in lb_rows:
    if "claim" in r["item_id"] or "Medium" in r["tco_notes"]:
        r["confidence"] = "medium"
    if r["item_id"] == "lb_ipolice_spent_77m_cancelled":
        r["confidence"] = "strong"
append_rows(DATA / "leaderboard.csv", lb_rows)
print("lb +", len(lb_rows))

draft = REPO / "docs/doge/foi/drafts" / f"{GAP}.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — {GAP}

Status: **ready** (human send only). Not legal advice.

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: Federale Politie / FOD Binnenlandse Zaken
t.a.v. dienst openbaarheid van bestuur

Betreft: Openbaarmaking — I-Police beeindiging, liquidaties 76,7 miljoen, claim 228,1 miljoen

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. **Beslissing tot beeindiging** I-Police (eind 2025) en opgeschort contract met leverancier.
2. **Liquidatiehistoriek** per jaar tot Fedcom 26 jan 2026 (totaal 76,7 miljoen van 299 miljoen).
3. **Status van de vordering** 228,1 miljoen (49,9 facturen + 178,5 schade), eventuele
   procedure/schikking, en onderbouw van de post 149 miljoen "verdwenen verwachte winst".
4. **Bestemming** residuale kredieten prog 17.80.4 (eng 7,8 / liq 15,1 miljoen 2026).

Periode: 2020-01-01 tot 2026-12-31.
Intern pad: Federal > Police > I-Police. Ref: {GAP}

Context (publiek CoA budget 2026):
- 76,7 miljoen geliquideerd; contract opgeschort;
- claim 228,1 miljoen waarvan 149 miljoen soft lost gain.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instelling Federale Politie / IBZ
- [x] Concrete I-Police cash + claim
- [x] Periode
- [ ] Contact verzoeker (mens)
- [x] ready draft complete
""",
    encoding="utf-8",
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Federal>Police>I-Police",
            "entity_id": "police_federale",
            "what_is_missing": "I-Police cancel decision + full cash liquidations by year + status of 228.1m vendor claim (esp. 149m lost-gain) + residual 17.80.4 projects 2026",
            "why_it_matters": "76.7m spent of 299m cancelled IT mega-project; large soft damages claim; classic DOGE opacity",
            "priority": 8,
            "recipient_body": "Federale Politie / FOD Binnenlandse Zaken",
            "recipient_email": "",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_ipolice_cancelled_2025",
            "linked_leaderboard_id": "lb_ipolice_spent_77m_cancelled",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick392 CoA public fill; claim litigation human send FOI",
        }
    ],
)

# update entity notes
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    efields = list(r.fieldnames)
    ents = list(r)
for row in ents:
    if row.get("entity_id") == "police_federale":
        row["notes"] = (
            "Section 17; FTE 13980 end-2025 (~flat since 2021); ops +87.5m from provision; "
            "I-Police cancelled 76.7/299m spent claim 228.1m; FOI gap_ipolice_claim_l5; tick392"
        )
    if row.get("entity_id") == "mod_defensie":
        row["notes"] = (
            "NATO 2pct path; s16 liq 10.77bn 2026 of effort 13.10bn; "
            "extra package 16.78bn 2025-29; capacity 33.8bn commit prior; tick392"
        )
rewrite(DATA / "entities.csv", ents, efields)

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = list(r.fieldnames)
    rq = list(r)
for row in rq:
    if row["task_id"] == UNIT:
        row["status"] = "done"
        row["updated_utc"] = NOW
        row["blocked_gap_id"] = GAP
        row["notes"] = (
            "tick392: I-Police 76.7/299m cancelled claim 228m; police FTE 14k; "
            "NATO 13.1bn s16 10.77; DGD 1.04bn; FOI claim; spawn rq_384"
        )
        break
if not any(x["task_id"] == "rq_384" for x in rq):
    rq.append(
        {
            "task_id": "rq_384",
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
            "notes": "Spawned tick392 after police I-Police + NATO defence; rq_116 SWA deferred",
        }
    )
rewrite(DATA / "research_queue.csv", rq, rq_fields)

with (DATA / "loop_state.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    stf = list(r.fieldnames)
    st = list(r)
st[0].update(
    {
        "last_tick_utc": NOW,
        "last_unit_id": UNIT,
        "ticks_completed": str(TICK),
        "paused": "no",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "notes": "Scheduler 60s. Next prio5 rq_384; rq_116 SWA deferred. FOI ready. tick392 I-Police 77m NATO 13.1bn.",
    }
)
rewrite(DATA / "loop_state.csv", st, stf)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **Federal police I-Police cancel + NATO 2pct defence path**)
- Found (strong primary CoA Budget 2026):
  - **I-Police cancelled:** liquidated **EUR 76.7m** of **299m**; claim **228.1m** (49.9 invoices + 178.5 damages of which lost-gain **149m** soft)
  - Residual prog 17.80.4 eng **7.8** / liq **15.1m** 2026 (Focus/digitalisation)
  - Police FTE **13,980** end-2025 (~flat vs 13,962 2021); target **14,280**; ops +**87.5m** from security provision
  - Grandes Villes police **43.6m** 2025-29; eng **9.9** / liq **13.2m** 2026
  - **NATO effort 2026 EUR 13,095.8m** (s16 liq **10,769.6**; external **2,326**; mil pens **1,688**)
  - Extra defence package **16,783m** 2025-29; temp fin CIT Russia **1,163** + Belfius **500**
  - DGD liq **1,040.3m** 2026; SPF Finance **2.4bn** (personnel 1.56)
- Wrote: sources +1; budgets +{len(budgets)}; cmt +2; lb +{len(lb_rows)}; entity police_federale; FOI **{GAP}** ready prio8; rq_383=done; spawn **rq_384**; ticks={TICK}
- FOI: I-Police claim/settlement human send only
- Next: prio5 **rq_384**; deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)

# tick389: Federal social assistance L5 — IGO/GRAPA 1bn + handicap 3.3bn + RIS 2.2bn (CoA Budget2026)
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T09:15:00Z"
TICK = 389
UNIT = "rq_380"
GAP = "gap_igo_handicap_ris_cash_codes"


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


append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_ccrek_budget2026_social_assist",
            "title": "Cour des comptes commentaires budget Etat 2026 — depenses sociales Entite I + aide handicap/ages/CPAS",
            "url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-01",
            "source_class": "primary_audit",
            "notes": "Entity I dep 268.7bn social 155.5bn SS prest 135.5bn; handicap 3.3bn ages(IGO) 1.0bn RIS 2.2bn + Ukraine 299m; chomage 3.9bn 2026",
        },
        {
            "source_id": "src_pensionstat_grapa_2025",
            "title": "PensionStat GRAPA stock Jan 2025 beneficiaries + monthly averages",
            "url": "https://www.pensionstat.be/fr/chiffres-cles/pension-legale/grapa",
            "publisher": "Service federal des Pensions / PensionStat",
            "accessed_date": "2026-08-01",
            "source_class": "primary_official",
            "notes": "119651 beneficiaries Jan2025 wavg ~719 EUR official page; monthly mass ~86.0m annualized ~1.03bn medium dual CoA 1.0bn 2026",
        },
    ],
)

budgets = []


def add(y, bid, amt, note, ent="sec_federal", conf="strong"):
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ent,
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "budgeted" if y >= 2026 else "outturn",
            "source_id": "src_ccrek_budget2026_social_assist",
            "confidence": conf,
            "notes": note,
        }
    )


# Entity I macro 2026
add(2026, "bud_entity1_dep_sec_2026", 268700000000, "Entity I depenses SEC consolidees 268.7bn 2026")
add(2026, "bud_entity1_deficit_2026", 24600000000, "Entity I deficit financement 24.6bn 2026")
add(2026, "bud_entity1_social_dep_2026", 155500000000, "Entity I politique sociale large 155.5bn 2026 (57.9pct dep; hors fiscal 18.6bn 2023 class)")
add(2026, "bud_entity1_ss_prest_2026", 135500000000, "Prestations regimes SS 135.5bn 2026 (+2pct)")
add(2026, "bud_entity1_cotis_2026", 86100000000, "Cotisations sociales Entity I 86.1bn 2026 (apres reductions)")
add(2026, "bud_entity1_red_cotis_2026", 5500000000, "Reductions cotisations 5.5bn 2026 (hors Maribel social)")
add(2026, "bud_entity1_chomage_2026", 3900000000, "Allocations chomage 3.9bn 2026 (vs 5.7bn annee prec; -1.8bn -31.5pct)")
add(2025, "bud_entity1_chomage_2025", 5700000000, "Allocations chomage 5.7bn 2025 class (prior year vs 2026)")
add(2026, "bud_entity1_indemnites_2026", 15900000000, "Indemnites incapacity 15.9bn 2026 (+4.8pct)")
add(2026, "bud_entity1_soins_sante_2026", 41300000000, "Soins de sante 41.3bn 2026 (+3.7pct)")
add(2026, "bud_entity1_pensions_2026", 72000000000, "Pensions 72bn 2026 (+3.3pct)")
add(2026, "bud_entity1_interest_2026", 12200000000, "Charges interet 12.2bn 2026 (1.84pct PIB)")
add(2026, "bud_entity1_transfers_other_2026", 66500000000, "Transfers autres pouvoirs 66.5bn 2026 (hors RIS CPAS)")
add(2026, "bud_entity1_transfers_federated_2026", 59100000000, "Transfers entites federees 59.1bn 2026")
add(2026, "bud_entity1_ue_rnb_2026", 5000000000, "Contribution UE RNB ~5bn 2026 (+30pct)")
add(2026, "bud_entity1_defense_sec_2026", 9500000000, "Defense SEC 9.5bn 2026 (40.6pct fonctions autorite)")
add(2026, "bud_entity1_defense_liq_2026", 10700000000, "Defense liquidations 10.7bn 2026")
add(2026, "bud_entity1_rail_2026", 3400000000, "Promotion service ferroviaire 3.4bn 2026")
add(2026, "bud_entity1_energie_2026", 1500000000, "Politique energetique 1.5bn 2026")
add(2026, "bud_entity1_bpost_pso_2026", 155000000, "bpost missions service public 155m 2026")
add(2026, "bud_entity1_esa_2026", 410000000, "Agence spatiale europeenne 410m 2026")

# Social assistance trilogy (core unit)
add(2026, "bud_handicap_federal_2026", 3300000000, "Aide federale personnes handicapees 3.3bn 2026 (budget general; hors SS regimes)")
add(2026, "bud_igo_grapa_federal_2026", 1000000000, "Aide personnes agees IGO/GRAPA 1.0bn 2026 (Tresor; hors cotisations)")
add(2026, "bud_ris_cpas_federal_2026", 2200000000, "Revenu d integration federal aux CPAS 2.2bn 2026")
add(2026, "bud_ris_ukraine_2026", 299000000, "RIS/refugies ukrainiens 299m 2026 (non compris dans 2.2bn)")
add(2026, "bud_social_assist_package_2026", 6500000000, "Package assistance sociale directe budget 6.5bn = 3.3+1.0+2.2 (excl Ukraine 0.3)")
add(2026, "bud_cpas_compensation_extra_2026", 300000000, "Compensation supplementaire CPAS +300m 2026 (SPP IS notifications)")

# GRAPA PensionStat dual
budgets.append(
    {
        "budget_id": "bud_grapa_benef_2025",
        "entity_id": "fpd",
        "year": 2025,
        "amount_eur": 119651,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_pensionstat_grapa_2025",
        "confidence": "strong",
        "notes": "GRAPA beneficiaries 119651 Jan2025 stock (COUNT unit; ~2/3 women)",
    }
)
budgets.append(
    {
        "budget_id": "bud_grapa_avg_monthly_2025",
        "entity_id": "fpd",
        "year": 2025,
        "amount_eur": 719,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_pensionstat_grapa_2025",
        "confidence": "strong",
        "notes": "GRAPA montant moyen brut 719 EUR/mois Jan2025 (official page)",
    }
)
budgets.append(
    {
        "budget_id": "bud_grapa_monthly_mass_2025",
        "entity_id": "fpd",
        "year": 2025,
        "amount_eur": 86042000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_pensionstat_grapa_2025",
        "confidence": "strong",
        "notes": "GRAPA monthly payment mass Jan2025 ~86.042m (sum n*avg by type from XLSX)",
    }
)
budgets.append(
    {
        "budget_id": "bud_grapa_annualized_2025",
        "entity_id": "fpd",
        "year": 2025,
        "amount_eur": 1032504000,
        "amount_min_eur": 1000000000,
        "amount_max_eur": 1100000000,
        "basis": "estimate",
        "source_id": "src_pensionstat_grapa_2025",
        "confidence": "medium",
        "notes": "Annualized Jan mass*12 ~1032.5m; dual CoA budget ages 1.0bn 2026 strong; method medium",
    }
)
# type splits count
for bid, n, note in [
    ("bud_grapa_pure_2025", 22135, "GRAPA alone 22135 Jan2025 COUNT"),
    ("bud_grapa_pr_2025", 56565, "PR+GRAPA 56565 COUNT"),
    ("bud_grapa_pr_pd_2025", 29792, "PR+PD+GRAPA 29792 COUNT"),
]:
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": "fpd",
            "year": 2025,
            "amount_eur": n,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "outturn",
            "source_id": "src_pensionstat_grapa_2025",
            "confidence": "strong",
            "notes": note,
        }
    )

# SPP IS reform savings (budgeted yields - speculative delivery)
add(2026, "bud_ris_reform_integration_save_2026", 33500000, "Economie reforme RIS parcours integration 33.5m 2026 budgeted (CoA: delivery risk high)", conf="medium")
add(2026, "bud_ris_attente_5ans_save_2026", 6700000, "Economie delai attente 5 ans aide sociale 6.7m 2026 budgeted", conf="medium")

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets))

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "cmt_social_assist_federal_2026",
            "title": "Federal social assistance package handicap+IGO+RIS 2026",
            "entity_id": "sec_federal",
            "beneficiary": "Disabled persons, elderly poor (GRAPA), CPAS RIS clients",
            "legal_basis": "Budget general des depenses; lois IGO/GRAPA; loi integration sociale; allocations handicap",
            "decision_date": "2026-01-01",
            "start_year": 2026,
            "end_year": 2026,
            "total_envelope_eur": 6500000000,
            "cash_by_year": '{"2026":6500000000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "stated_goal": "Means-tested safety net outside contribution-financed SS",
            "cut_option": "Keep floors; open cash codes L5; dual reform path CoA flags overstated savings",
            "source_id": "src_ccrek_budget2026_social_assist",
            "confidence": "strong",
            "hierarchy_path": "Federal>social_assistance>package_2026",
            "notes": "tick389: 3.3+1.0+2.2=6.5bn; Ukraine 0.3 separate; FOI AB codes",
        }
    ],
)

lbs = [
    (
        "lb_entity1_social_155bn_2026",
        "Entity I social policy spend 155.5bn 2026",
        155500000000,
        "Strong CoA Budget2026: 155.5bn 57.9pct Entity I dep; SS prest 135.5 + direct assist + other",
        2,
        10.0,
        2,
        6.90,
        "Map residual sections 23-25; dual SS already deep",
        "transfer",
        "strong",
    ),
    (
        "lb_ss_prest_135_5bn_2026",
        "SS regime prestations 135.5bn 2026",
        135500000000,
        "Strong: 135.5bn (+2pct); chomage cut -1.8bn; pens 72 health 41.3 indemn 15.9",
        2,
        10.0,
        2,
        6.90,
        "Track unemployment time-limit delivery vs 3.9bn",
        "transfer",
        "strong",
    ),
    (
        "lb_handicap_federal_3_3bn_2026",
        "Federal disability assistance 3.3bn 2026",
        3300000000,
        "Strong CoA: aide personnes handicapees 3.3bn budget general; dual regional VAPH/AVIQ",
        3,
        8.5,
        4,
        6.13,
        "Open ARR/AI cash codes L5 dual regions",
        "transfer",
        "strong",
    ),
    (
        "lb_igo_grapa_1bn_2026",
        "IGO/GRAPA elderly assistance 1.0bn 2026",
        1000000000,
        "Strong CoA 1.0bn ages; dual PensionStat ~1.03bn annualized medium 119651 benef Jan2025",
        3,
        8.0,
        3,
        6.05,
        "Publish official outturn series; dual gap_fpd residual narrowed",
        "transfer",
        "strong",
    ),
    (
        "lb_ris_cpas_2_2bn_2026",
        "Federal RIS to CPAS 2.2bn 2026",
        2200000000,
        "Strong CoA: 2.2bn + Ukraine 299m + compensation 300m path; SPP IS dual local CPAS",
        4,
        8.0,
        4,
        6.10,
        "Open per-commune top transfers; reform savings CoA overstate risk",
        "transfer",
        "strong",
    ),
    (
        "lb_chomage_3_9bn_2026",
        "Unemployment benefits budgeted 3.9bn 2026",
        3900000000,
        "Strong CoA: 3.9bn vs 5.7bn prior (-31.5pct) time-limit reform; delivery risk",
        5,
        8.0,
        5,
        6.20,
        "Track RVA outturn vs 3.9; dual local RIS spillover",
        "transfer",
        "strong",
    ),
    (
        "lb_social_assist_package_6_5bn_2026",
        "Federal means-tested assistance package 6.5bn 2026",
        6500000000,
        "Strong sum handicap 3.3 + IGO 1.0 + RIS 2.2; safety-net outside SS cotis pie",
        3,
        8.5,
        3,
        6.20,
        "Full AB codes FOI; protect floors",
        "transfer",
        "strong",
    ),
]
lb_rows = []
for iid, name, cost, tco, ab, cs, df, pi, cut, typ, conf in lbs:
    lb_rows.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": "Federal>social>" + iid.replace("lb_", ""),
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": tco,
            "confidence": conf,
            "source_id": "src_ccrek_budget2026_social_assist",
            "beneficiaries": "Social assistance / SS beneficiaries",
            "stated_goal": "Social protection and means-tested floors",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick389",
        }
    )
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

Aan: FOD Sociale Zekerheid / SPP Integratie Sociale / Federale Pensioendienst
t.a.v. dienst openbaarheid van bestuur

Betreft: Openbaarmaking — basisallocaties IGO/GRAPA, handicap, leefloon 2023-2026

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. **Budgetcodes / basisallocaties** en kasuitgaven 2023-2026 voor:
   - IGO / GRAPA (garantie de revenus aux personnes agees);
   - federale tegemoetkomingen personen met handicap (ARR/AI e.a.);
   - federale tussenkomst leefloon / revenu d integration aan OCMW/CPAS.
2. **Splitsing** per jaar: kredieten vs realisaties; eventuele Ukraine-envelope.
3. Eventuele **begunstigden-statistieken** cash (niet enkel headcount) per jaar.

Periode: 2023-01-01 tot 2026-12-31.
Intern pad: Federal > social_assistance > cash_codes. Ref: {GAP}

Context (publiek CoA budget 2026):
- handicap 3,3 miljard; leeftijd/IGO 1,0 miljard; leefloon 2,2 miljard (+299m Oekraine);
- PensionStat GRAPA ~119.651 begunstigden jan 2025.
Ontbreekt: officiële kasreeks per AB-code.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instellingen FOD SZ / SPP IS / FPD
- [x] Concrete AB-codes + cash
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
            "hierarchy_path": "Federal>social_assistance>cash_codes",
            "entity_id": "sec_federal",
            "what_is_missing": "Official AB codes + cash-by-year 2023-26 for IGO/GRAPA, federal disability ARR/AI, RIS to CPAS; Ukraine envelope split",
            "why_it_matters": "6.5bn means-tested package mapped at L2; residual end-receiver cash codes for L5",
            "priority": 6,
            "recipient_body": "FOD Sociale Zekerheid / SPP Integratie / FPD",
            "recipient_email": "",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_social_assist_federal_2026",
            "linked_leaderboard_id": "lb_social_assist_package_6_5bn_2026",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick389 CoA+PensionStat; residual AB codes human send; narrows gap_fpd_beheer_igo",
        }
    ],
)

# entities - update fpd note
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("entity_id") == "fpd":
        row["notes"] = (
            "Worker public IGO pensions payment; PensionStat legal 69.05bn 2025; "
            "GRAPA ~120k benef / ~1.0bn 2026 CoA; package 69.4bn 2024; "
            "FOI gap_fpd_beheer_igo_l5 + gap_igo_handicap_ris_cash_codes; tick389"
        )
        break
# add entity spp_is if missing
if not any(r.get("entity_id") == "spp_is" for r in rows):
    rows.append(
        {
            "entity_id": "spp_is",
            "name_nl": "POD Maatschappelijke Integratie",
            "name_fr": "SPP Integration sociale",
            "name_en": "PPS Social Integration",
            "level": "agency",
            "parent_id": "sec_federal",
            "community_language": "bi",
            "website": "https://www.mi-is.be",
            "foi_email": "",
            "foi_postal": "",
            "notes": "Federal RIS to CPAS 2.2bn 2026 + Ukraine 299m + compensation 300m; tick389",
        }
    )
rewrite(DATA / "entities.csv", rows, list(fields))

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq = list(r)
for row in rq:
    if row["task_id"] == UNIT:
        row["status"] = "done"
        row["updated_utc"] = NOW
        row["blocked_gap_id"] = GAP
        row["notes"] = (
            "tick389: Entity I social 155.5bn SS prest 135.5; handicap 3.3 IGO 1.0 RIS 2.2; "
            "GRAPA 120k; FOI cash codes; spawn rq_381 progress@390"
        )
        break
if not any(x["task_id"] == "rq_381" for x in rq):
    rq.append(
        {
            "task_id": "rq_381",
            "title": "Progress coverage % + waste top10 @tick390",
            "sprint": "continuous",
            "priority": "6",
            "status": "open",
            "hierarchy_target": "meta",
            "entity_id": "gg_belgium",
            "instructions": "Mandatory every-10-ticks: refresh progress_every_10_ticks.md + doge_waste_top10_current.md; no invent euros.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": "",
            "notes": "Spawned tick389 for mandatory progress@390",
        }
    )
rewrite(DATA / "research_queue.csv", rq, list(rq_fields))

with (DATA / "loop_state.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    stf = r.fieldnames
    st = list(r)
st[0].update(
    {
        "last_tick_utc": NOW,
        "last_unit_id": UNIT,
        "ticks_completed": str(TICK),
        "paused": "no",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "notes": "Scheduler 60s. Next **mandatory progress@390 rq_381**; rq_116 SWA deferred. tick389 social assist 6.5bn.",
    }
)
rewrite(DATA / "loop_state.csv", st, list(stf))

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **federal social assistance L5 IGO+handicap+RIS + Entity I social macro**)
- Found (strong primary CoA Budget 2026 + PensionStat GRAPA):
  - Entity I dep **268.7bn** · social **155.5bn** · SS prest **135.5bn** · cotis **86.1bn**
  - **Handicap 3.3bn** · **IGO/ages 1.0bn** · **RIS CPAS 2.2bn** (+Ukraine **299m**) = package **6.5bn**
  - Chomage **3.9bn** 2026 (vs 5.7bn; -31.5pct) · pens **72bn** · health **41.3bn** · indemn **15.9bn**
  - GRAPA stock **119,651** Jan2025 · avg **719 EUR/mo** · annualized **~1.03bn** medium dual 1.0bn
- Wrote: sources +2; budgets +{len(budgets)}; cmt +1; lb +{len(lb_rows)}; entity spp_is; FOI **{GAP}** ready; rq_380=done; spawn **rq_381** progress@390; ticks={TICK}
- FOI: AB cash codes handicap/IGO/RIS human send only
- Next: **mandatory progress@390** (rq_381); deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)

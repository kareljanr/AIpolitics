# tick391: SPF Justice 2026 credits+provisions + prison overcrowding envelope + Fedasil cut path
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T10:15:00Z"
TICK = 391
UNIT = "rq_382"
GAP = "gap_justice_provisions_l5_2026"


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
            "source_id": "src_ccrek_budget2026_justice_fedasil",
            "title": "Cour des comptes budget Etat 2026 — SPF Justice provisions + Fedasil dotation + BE-Watt Phoenix",
            "url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-01",
            "source_class": "primary_audit",
            "notes": "Justice section 2843m + provisions 465.5m; prison envelope 840m 2026-29; Fedasil dot 702.2+prov 100; BE-Watt 487.6; energy norm 249",
        },
    ],
)

budgets = []


def add(y, bid, amt, note, ent="fod_justice", conf="strong", basis="budgeted"):
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ent,
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": "src_ccrek_budget2026_justice_fedasil",
            "confidence": conf,
            "notes": note,
        }
    )


# Justice section
add(2026, "bud_justice_section_2026", 2843000000, "SPF Justice section 12 engagement+liquidation credits 2843m 2026 (+82m vs prior year)")
add(2026, "bud_justice_prov_securite_2026", 112500000, "Provision securite for Justice 112.5m 2026 (of 250m structural security/return policy)")
add(2026, "bud_justice_prov_surpop_struct_2026", 50000000, "Provision structural prison overcrowding Justice 50m/yr 2026 (of 240m 2026-29 package)")
add(2026, "bud_justice_prov_infra_surpop_2026", 259000000, "Provision infra+exploit overcrowding 259m 2026 (of 600m 2026-29; Justice+Regie des batiments)")
add(2026, "bud_justice_prov_efficiency_2026", 44000000, "Provision gains d efficacite Justice 44m 2026 (of 50.7m Justice+Interior add-on)")
add(2026, "bud_justice_provisions_sum_2026", 465500000, "Sum dedicated provisions for Justice projects 465.5m 2026 (CoA: specialty principle breach)")
add(2026, "bud_justice_package_class_2026", 3308500000, "Justice class section+provisions 2843+465.5=3308.5m 2026 (not pure additive outturn)")
add(2026, "bud_prison_envelope_2026_2029", 840000000, "Prison overcrowding envelope 840m engagement+liq 2026-2029 (CM Dec 2025)")
add(2026, "bud_prison_infra_package_600m", 600000000, "Prison infra+exploit package 600m 2026-29 (Regie+Justice; 259m in 2026)")
add(2026, "bud_prison_struct_package_240m", 240000000, "Prison structural package 240m 2026-29 (Justice 50/yr + Sante 5 + Migration 5)")
add(2026, "bud_prison_tf_needs_1_1bn", 1100000000, "Task-force estimated needs 1.1bn hors index (capacity+health+migration+foreign)", conf="medium", basis="estimate")
add(2026, "bud_prison_places_2026", 1052, "Task force capacity: 1052 new detention places 2026 plan incl Antwerp (COUNT)", conf="medium", basis="estimate")
add(2026, "bud_prison_capacity_budget_2026", 303800000, "Task force capacity budget example 303.8m for 1052 places 2026", conf="medium", basis="estimate")
add(2025, "bud_prison_surpop_credit_2025", 55000000, "Prison overcrowding one-off credit 55m 2025 (made structural +5m to 60m path 2026)")
add(2026, "bud_prison_food_detainees_2026", 25200000, "Frais nourriture et entretien detenus 25.2m 2026 (prog 11 DG EPI)")
add(2025, "bud_prison_food_detainees_2025", 24400000, "Frais nourriture detenus engagement 24.4m 2025 class")
add(2026, "bud_prison_food_underfund_2026", 10180000, "Estimated underfunding food/maintenance detainees 10.18m 2026 (to pull from provision)", conf="medium")

# Security provision aggregate
add(2026, "bud_prov_securite_total_2026", 366900000, "Provision securite+return policy total 366.9m 2026 (250+60+6.2+50.7)", ent="sec_federal")
add(2026, "bud_prov_securite_struct_2026", 250000000, "Structural security/return policy 250m 2026 (Justice 112.5 Police fed 87.5 Migration 50)", ent="sec_federal")
add(2026, "bud_prov_securite_police_2026", 87500000, "Police federale share of security provision 87.5m 2026", ent="sec_federal")
add(2026, "bud_prov_securite_migration_2026", 50000000, "Migration services share of security provision 50m 2026", ent="fod_ibz")
add(2026, "bud_prov_securite_report_justice_2026", 6200000, "Report unused 2025 justice surpop 6.2m into 2026 provision", ent="fod_justice")
add(2026, "bud_prov_securite_addon_2026", 50700000, "Addon provision Justice+Interior 50.7m 2026 (Justice 44 Interior 6; purpose opaque CoA)", ent="sec_federal")

# Fedasil
add(2025, "bud_fedasil_dot_adj_2025", 828900000, "Fedasil dotation adjusted budget 828.9m 2025", ent="fedasil")
add(2026, "bud_fedasil_dot_2026", 702200000, "Fedasil dotation initial 702.2m 2026 (-126.7m vs adj 2025)", ent="fedasil")
add(2025, "bud_fedasil_prov_2025", 126600000, "Fedasil interdept provision 126.6m 2025", ent="fedasil")
add(2026, "bud_fedasil_prov_2026", 100000000, "Fedasil interdept provision unavoidable reception costs 100m 2026", ent="fedasil")
add(2025, "bud_fedasil_package_2025", 955600000, "Fedasil package dot+prov 955.6m 2025", ent="fedasil")
add(2026, "bud_fedasil_package_2026", 802200000, "Fedasil package 802.2m 2026 (-153.4m)", ent="fedasil")
add(2026, "bud_fedasil_economy_2026", 247000000, "Fedasil savings path 247m 2026 (part of 688m by 2029 asylum tightening)", ent="fedasil", conf="medium")
add(2029, "bud_fedasil_economy_2029", 688000000, "Asylum policy savings target 688m 2029 (of which reception network 538m class)", ent="fedasil", conf="medium")

# BE-Watt / energy (same CoA chapter residual high value)
add(2026, "bud_bewatt_dot_2026", 487600000, "BE-Watt dotation 487.6m 2026 (federal shareholder BE-NUC Phoenix Doel4/Tihange3)", ent="sec_federal")
add(2026, "bud_bewatt_prov_q1_2026", 146000000, "BE-Watt provisional credits Q1 2026 obligations 146m", ent="sec_federal")
add(2026, "bud_energy_norm_prov_2026", 249000000, "Provision norme energetique 249m 2026 (industry electricity cost competitiveness)", ent="sec_federal")
add(2026, "bud_fluxys_energy_receipt_2026", 100000000, "Fluxys receipt earmarked to energy norm 100m 2026 (CoA: universality principle issue)", ent="sec_federal")

# SPP IS DIS detail table
add(2026, "bud_ris_dis_2026", 2084500000, "DIS federal to CPAS 2084.5m 2026 (base 1841.7 -index +300 comp -reforms)", ent="spp_is")
add(2026, "bud_ris_loi1965_2026", 156400000, "Loi 1965 aide indigence CPAS 156.4m 2026", ent="spp_is")
add(2026, "bud_ris_dis_base_2026", 1841700000, "DIS base before corrections 1841.7m 2026 (CM Jul 2025)", ent="spp_is")
add(2026, "bud_ris_comp_chomage_2026", 300000000, "CPAS compensation unemployment spillover +300m 2026", ent="spp_is")

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets))

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "cmt_prison_overcrowding_2026_2029",
            "title": "Prison overcrowding envelope 840m 2026-2029 + Justice provisions",
            "entity_id": "fod_justice",
            "beneficiary": "DG EPI prisons + Regie des batiments + detainees",
            "legal_basis": "CM 18 Jul 2025 + conclave 12 Dec 2025; BOSA provisions 06.90",
            "decision_date": "2025-12-12",
            "start_year": 2026,
            "end_year": 2029,
            "total_envelope_eur": 840000000,
            "cash_by_year": '{"2026":259000000}',
            "remaining_eur": 581000000,
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "stated_goal": "Reduce prison overcrowding via capacity and structural ops",
            "cut_option": "Publish named projects L5; end multi-year carry of unused provision credits",
            "source_id": "src_ccrek_budget2026_justice_fedasil",
            "confidence": "strong",
            "hierarchy_path": "Federal>Justice>prison_overcrowding",
            "notes": "tick391: 600m infra+240m structural; TF needs 1.1bn medium; FOI project list",
        },
        {
            "commitment_id": "cmt_fedasil_dot_2026",
            "title": "Fedasil reception package 2026 (dot+provision)",
            "entity_id": "fedasil",
            "beneficiary": "Asylum seekers reception network",
            "legal_basis": "Budget general section 13.40.4 + interdept provision",
            "decision_date": "2025-12-12",
            "start_year": 2026,
            "end_year": 2026,
            "total_envelope_eur": 802200000,
            "cash_by_year": '{"2026":802200000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "stated_goal": "Asylum reception network with tightened policy savings path",
            "cut_option": "Track 247m 2026 / 688m 2029 delivery vs reception quality",
            "source_id": "src_ccrek_budget2026_justice_fedasil",
            "confidence": "strong",
            "hierarchy_path": "Federal>Interior>Fedasil",
            "notes": "tick391: 702.2+100 vs 955.6 2025; dual partners FOI residual",
        },
    ],
)

lbs = [
    (
        "lb_justice_section_2_84bn_2026",
        "SPF Justice section credits 2.84bn 2026",
        2843000000,
        "Strong CoA: 2843m engagement+liq (+82m); dual 465.5m provisions off-section",
        3,
        8.5,
        4,
        6.13,
        "Integrate provisions into section; publish project L5",
        "ops",
    ),
    (
        "lb_justice_provisions_466m_2026",
        "Justice off-section provisions 465.5m 2026",
        465500000,
        "Strong: securite 112.5 + surpop 50 + infra 259 + efficacite 44; CoA specialty breach",
        6,
        7.5,
        5,
        6.35,
        "Open named project list; annuality of unused credits",
        "ops",
    ),
    (
        "lb_prison_envelope_840m_2026_29",
        "Prison overcrowding envelope 840m 2026-2029",
        210000000,
        "Strong: 840m multi-year; 259m infra 2026; structural 60m/yr path; TF needs 1.1bn medium",
        5,
        7.5,
        5,
        6.20,
        "Publish places/cost unit; dual Regie L5",
        "ops",
    ),
    (
        "lb_fedasil_package_802m_2026",
        "Fedasil reception package 802.2m 2026",
        802200000,
        "Strong: dot 702.2 + prov 100; -153m vs 2025 package; savings 247m 2026 / 688m 2029 path",
        4,
        7.5,
        5,
        6.00,
        "Track place network cuts vs FOI partners L5",
        "transfer",
    ),
    (
        "lb_bewatt_phoenix_488m_2026",
        "BE-Watt Phoenix nuclear extension 487.6m 2026",
        487600000,
        "Strong: federal shareholder BE-NUC Doel4/Tihange3; +146m Q1 provisional",
        5,
        7.5,
        6,
        5.95,
        "Dual Hedera waste stock; publish cash vs Engie deal",
        "ops",
    ),
    (
        "lb_energy_norm_249m_2026",
        "Energy norm provision industry 249m 2026",
        249000000,
        "Strong: norme energetique 249m; Fluxys 100m earmark universality issue CoA",
        6,
        7.0,
        5,
        6.05,
        "Publish firm eligibility L5 dual gas reduced rate FOI",
        "tax_expenditure",
    ),
    (
        "lb_prov_securite_367m_2026",
        "Security+return policy provision 366.9m 2026",
        366900000,
        "Strong: 250 structural (J 112.5 P 87.5 M 50) +60 surpop +6.2 report +50.7 opaque addon",
        5,
        7.5,
        5,
        6.20,
        "Split named uses; dual police/migration outturn",
        "ops",
    ),
    (
        "lb_prison_food_underfund_10m_2026",
        "Prison food/maintenance underfunding 10.2m 2026",
        10180000,
        "Strong estimate admin: food line 25.2m vs need underfund 10.18m from provision",
        7,
        4.5,
        3,
        5.65,
        "Fund structural line not provision pull",
        "ops",
    ),
]
lb_rows = []
for iid, name, cost, tco, ab, cs, df, pi, cut, typ in lbs:
    lb_rows.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": "Federal>Justice>" + iid.replace("lb_", ""),
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": tco,
            "confidence": "strong" if "medium" not in tco.lower() or "Strong" in tco[:6] else "medium",
            "source_id": "src_ccrek_budget2026_justice_fedasil",
            "beneficiaries": "Justice system / asylum / energy industry",
            "stated_goal": "Public security justice asylum energy policy",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick391",
        }
    )
# fix confidence for medium items
for r in lb_rows:
    if "medium" in r["tco_notes"] and "Strong" in r["tco_notes"]:
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

Aan: FOD Justitie / SPF Justice en FOD BOSA
t.a.v. dienst openbaarheid van bestuur

Betreft: Openbaarmaking — projecten provisions Justitie 2026 + overbevolking gevangenissen

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. **Lijst van projecten/bestemmingen** die in 2026 worden gefinancierd uit:
   - provision Securite (112,5 miljoen Justitie);
   - provision structurele overbevolking (50 miljoen/jaar Justitie);
   - provision infrastructuur/exploitatie overbevolking (259 miljoen 2026);
   - provision gains d efficacite Justitie (44 miljoen).
2. **Cash-by-year** 2026-2029 binnen de enveloppe 840 miljoen overbevolking
   (600+240), met splitsing Regie der Gebouwen vs Justitie.
3. Eventuele **evaluaties** unit-cost per nieuwe plaats / per detenu.

Periode: 2025-01-01 tot 2029-12-31.
Intern pad: Federal > Justice > provisions_L5. Ref: {GAP}

Context (publiek CoA budget 2026):
- sectie Justitie 2.843 miljoen + provisions 465,5 miljoen;
- task force raming 1,1 miljard; enveloppe 840 miljoen 2026-2029;
- projectlijst niet aan Rekenhof meegedeeld.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instelling Justitie + BOSA
- [x] Concrete provisions + project list
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
            "hierarchy_path": "Federal>Justice>provisions_L5_2026",
            "entity_id": "fod_justice",
            "what_is_missing": "Named 2026 projects financed from Justice provisions (securite 112.5, surpop 50, infra 259, efficacite 44) and 840m 2026-29 prison envelope split Regie vs Justice",
            "why_it_matters": "465.5m off-section + multi-year prison package opacity; CoA specialty/annuality critique",
            "priority": 6,
            "recipient_body": "FOD Justitie / FOD BOSA",
            "recipient_email": "",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_prison_overcrowding_2026_2029",
            "linked_leaderboard_id": "lb_justice_provisions_466m_2026",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick391 CoA public fill; project L5 FOI human send",
        }
    ],
)

# entities
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = list(r.fieldnames)
    rows = list(r)
for row in rows:
    if row.get("entity_id") in ("fod_justice", "fod_justitie"):
        row["notes"] = (
            "Annual budget section ~2.84bn 2026 + provisions 465.5m; "
            "prisons overcrowding envelope 840m 2026-29; courts/prisons dual; "
            f"FOI {GAP}; tick391"
        )
    if row.get("entity_id") == "fedasil":
        row["notes"] = (
            "Dotatie 702.2m + prov 100m = 802.2m 2026 (vs 955.6 2025); "
            "savings path 247m 2026 / 688m 2029; third-party residual FOI; tick391"
        )
    if row.get("entity_id") == "dg_epi":
        row["notes"] = (
            "Prison admin; food line 25.2m 2026 underfund 10.2m; "
            "overcrowding envelope dual Justice; tick391"
        )
rewrite(DATA / "entities.csv", rows, fields)

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
            "tick391: Justice 2.84bn+prov 465.5; prison 840m 26-29; Fedasil 802.2; "
            "BE-Watt 487.6; energy norm 249; FOI provisions L5; spawn rq_383"
        )
        break
if not any(x["task_id"] == "rq_383" for x in rq):
    rq.append(
        {
            "task_id": "rq_383",
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
            "notes": "Spawned tick391 after Justice/Fedasil L5; rq_116 SWA deferred",
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
        "notes": "Scheduler 60s. Next prio5 rq_383; rq_116 SWA deferred. FOI ready. tick391 Justice 2.84bn Fedasil 802m.",
    }
)
rewrite(DATA / "loop_state.csv", st, stf)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **SPF Justice 2026 + prison envelope + Fedasil cut + BE-Watt**)
- Found (strong primary CoA Budget 2026):
  - Justice section **EUR 2,843m** (+82) + dedicated provisions **465.5m** (sec 112.5 · surpop 50 · infra 259 · effic 44)
  - Prison overcrowding envelope **840m 2026-2029** (600 infra + 240 structural); TF needs **1.1bn** medium
  - Food detainees **25.2m** underfund **10.18m**; security provision total **366.9m**
  - Fedasil package **802.2m** 2026 (dot 702.2 + prov 100; -153 vs 2025); savings **247m** / **688m by 2029**
  - BE-Watt Phoenix **487.6m** + Q1 prov **146m**; energy norm **249m**; Fluxys earmark **100m**
  - RIS DIS detail **2,084.5** + loi1965 **156.4** = **2,240.9m**
- Wrote: sources +1; budgets +{len(budgets)}; cmt +2; lb +{len(lb_rows)}; entities; FOI **{GAP}** ready; rq_382=done; spawn **rq_383**; ticks={TICK}
- FOI: Justice provision project list human send only
- Next: prio5 **rq_383**; deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)

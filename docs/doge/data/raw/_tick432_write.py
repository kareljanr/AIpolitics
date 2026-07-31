# tick 432: CoA Budget 2026 Entity I social transfers triple + provision generale L5
import csv, json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T06:45:00Z"
TICK = 432
UNIT = "rq_423"
SRC = "src_ccrek_budget2026_entity1_social_prov"

# Entity I direct social transfers (CoA p18) — milliards
handicap = 3.3e9  # aide personnes handicapees
ages_igo = 1.0e9  # personnes agees (IGO)
ris_cpas = 2.2e9  # CPAS revenu integration (excl Ukraine)
ukraine = 299e6  # not included in 2.2bn
social_triple = handicap + ages_igo + ris_cpas  # 6.5bn
social_plus_ua = social_triple + ukraine

# Dual recon with prior ticks
# DG HAN 2.93bn was 2025 outturn; CoA 3.3bn is 2026 budget class (broader?)
# SPP IS 2.241bn tick431 vs CoA 2.2bn class (rounding / perimeter)

# Provision generale interdepartementale 2026 (p58 table)
prov_total_2026 = 829.8e6
prov_total_2025_adj = 599.7e6
prov_total_2025_init = 607.3e6
prov_justice_divers = 618.3e6  # 2026
prov_fedasil = 100.0e6
prov_bpost = 78.0e6
prov_bienetre = 33.5e6
# 2025 lines for path
prov_justice_2025_adj = 131.7e6
prov_fedasil_2025_adj = 126.6e6
prov_bpost_2025_adj = 85.4e6
prov_pecule_2025_adj = 66.0e6
prov_decom_2025_adj = 190.0e6

# Named uses inside justice/divers 618.3m (from CoA list — sum of named)
named_surpop = 259e6
named_esa = 176e6  # ESA space agency
named_eco_soc = 50e6
named_reorg = 36e6
named_tria = 5.3e6
named_cpl = 2.7e6
named_sum = named_surpop + named_esa + named_eco_soc + named_reorg + named_tria + named_cpl  # 529m
# residual in 618.3 - 529 = ~89.3m other decisions

# Transfers to other governments Entity I (p18)
transfers_other = 66.5e9  # after neutralizing third-party
transfers_federated = 59.1e9

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 Entity I social transfers + provision generale L5",
            "url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": f"Handicap 3.3bn ages 1.0bn RIS 2.2bn (+UA 299m); prov gen 829.8m; tick{TICK}",
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add(bid, entity, year, amount, basis, notes, conf="strong"):
    if any(r["budget_id"] == bid for r in bud):
        return
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


# Social triple
add(
    "bud_entity1_handicap_3_3bn_2026",
    "sec_federal",
    2026,
    handicap,
    "budgeted",
    f"Entity I aide personnes handicapees 3.3bn 2026 CoA p18; dual DG HAN 2.93bn 2025 outturn; tick{TICK}",
)
add(
    "bud_entity1_ages_igo_1bn_2026",
    "fpd",
    2026,
    ages_igo,
    "budgeted",
    f"Entity I aide personnes agees (IGO/GRAPA class) 1.0bn 2026 CoA; dual PensionStat GRAPA; tick{TICK}",
)
add(
    "bud_entity1_ris_cpas_2_2bn_2026",
    "spp_is",
    2026,
    ris_cpas,
    "budgeted",
    f"Entity I CPAS revenu integration 2.2bn 2026 CoA excl Ukraine; dual tick431 table 2.241bn; tick{TICK}",
)
add(
    "bud_entity1_ukraine_refugees_299m_2026",
    "spp_is",
    2026,
    ukraine,
    "budgeted",
    f"Ukraine refugee support 299m 2026 not in 2.2bn RIS line CoA; tick{TICK}",
)
add(
    "bud_entity1_social_triple_6_5bn_2026",
    "sec_federal",
    2026,
    social_triple,
    "budgeted",
    f"Entity I social transfer triple handicap+ages+RIS 6.5bn 2026 (+UA 299m = 6.8bn); tick{TICK}",
)
add(
    "bud_entity1_transfers_other_66_5bn_2026",
    "sec_federal",
    2026,
    transfers_other,
    "budgeted",
    f"Entity I transfers to other govts 66.5bn 2026 (excl third-party; excl RIS CPAS); federated 59.1bn class; tick{TICK}",
)
add(
    "bud_entity1_transfers_federated_59_1bn_2026",
    "sec_federal",
    2026,
    transfers_federated,
    "budgeted",
    f"Transfers to federated entities 59.1bn 2026 (LSF class); tick{TICK}",
)

# Provision generale
add(
    "bud_prov_gen_829_8m_2026",
    "sec_federal",
    2026,
    prov_total_2026,
    "budgeted",
    f"Provision interdepartementale generale 829.8m 2026 (+230m vs 599.7 adj 2025); tick{TICK}",
)
add(
    "bud_prov_gen_justice_divers_618m_2026",
    "sec_federal",
    2026,
    prov_justice_divers,
    "budgeted",
    f"Prov gen line frais de justice et divers 618.3m 2026 (was 131.7 adj 2025); tick{TICK}",
)
add(
    "bud_prov_gen_fedasil_100m_2026",
    "fedasil",
    2026,
    prov_fedasil,
    "budgeted",
    f"Prov gen Fedasil unavoidable reception 100m 2026 (dual package 702.2+100); tick{TICK}",
)
add(
    "bud_prov_gen_bpost_78m_2026",
    "sec_federal",
    2026,
    prov_bpost,
    "budgeted",
    f"Prov gen nouveaux contrats bpost 78m 2026 (was 85.4); tick{TICK}",
)
add(
    "bud_prov_gen_bienetre_33_5m_2026",
    "sec_federal",
    2026,
    prov_bienetre,
    "budgeted",
    f"Prov gen bien-etre groupes vulnerables et cohesion sociale 33.5m 2026; tick{TICK}",
)
add(
    "bud_prov_named_surpop_259m_2026",
    "fod_justice",
    2026,
    named_surpop,
    "budgeted",
    f"Inside justice/divers: prison surpopulation infra 259m 2026; tick{TICK}",
)
add(
    "bud_prov_named_esa_176m_2026",
    "sec_federal",
    2026,
    named_esa,
    "budgeted",
    f"Inside justice/divers: ESA (Agence spatiale europeenne) 176m 2026; tick{TICK}",
)
add(
    "bud_prov_named_eco_soc_50m_2026",
    "sec_federal",
    2026,
    named_eco_soc,
    "budgeted",
    f"Inside justice/divers: economie sociale 50m 2026; tick{TICK}",
)
add(
    "bud_prov_named_reorg_36m_2026",
    "sec_federal",
    2026,
    named_reorg,
    "budgeted",
    f"Inside justice/divers: reorg admin federale + centralisation support 36m 2026; tick{TICK}",
)
add(
    "bud_prov_named_tria_5_3m_2026",
    "sec_ss",
    2026,
    named_tria,
    "budgeted",
    f"Inside justice/divers: Tria IT programme SPF SS 5.3m 2026; tick{TICK}",
)
add(
    "bud_prov_named_cpl_2_7m_2026",
    "fod_justice",
    2026,
    named_cpl,
    "budgeted",
    f"Inside justice/divers: modular units CPL forensic psych 2.7m 2026; tick{TICK}",
)
add(
    "bud_prov_named_sum_529m_2026",
    "sec_federal",
    2026,
    named_sum,
    "budgeted",
    f"Sum of named uses in justice/divers list ~529m of 618.3m (residual ~89m other); tick{TICK}",
)

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())


def addc(cid, **kw):
    if any(r["commitment_id"] == cid for r in cmt):
        return
    row = {k: "" for k in cf}
    row.update(kw)
    cmt.append(row)


addc(
    "cmt_entity1_social_triple_2026",
    title="Entity I direct social transfers handicap+ages+RIS 6.5bn 2026",
    entity_id="sec_federal",
    beneficiary="Persons with disabilities, elderly (IGO), CPAS RIS recipients",
    legal_basis="Federal budget general des depenses social policy lines",
    decision_date="2025-12-01",
    start_year="2026",
    end_year="2026",
    total_envelope_eur=str(int(social_triple)),
    cash_by_year=json.dumps(
        {
            "handicap": int(handicap),
            "ages_igo": int(ages_igo),
            "ris_cpas": int(ris_cpas),
            "ukraine_excl": int(ukraine),
            "triple": int(social_triple),
            "dual_dghan_2025": 2930000000,
            "dual_spp_is_table_2026": 2240900000,
            "note": "CoA p18 class figures; dual prior deep-dives",
        },
        separators=(",", ":"),
    ),
    remaining_eur="",
    status="active",
    evaluation_url="https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
    stated_goal="Federal social assistance outside SS institutions perimeter",
    cut_option="Core safety nets; dual SS 146.8bn separate; reform RIS/unemp spillover",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="EntityI>social_transfers>triple_2026",
    notes=f"6.5bn +UA 299m; not pure waste; dual tick429/431; tick{TICK}",
)

addc(
    "cmt_prov_gen_2026_l5",
    title="Interdepartmental general provision 829.8m 2026 L5 breakdown",
    entity_id="sec_federal",
    beneficiary="Multiple federal programmes via BOSA provision",
    legal_basis="Budget provision interdepartementale generale AB 06.90.10.01.00.01",
    decision_date="2025-12-12",
    start_year="2026",
    end_year="2026",
    total_envelope_eur=str(int(prov_total_2026)),
    cash_by_year=json.dumps(
        {
            "total": int(prov_total_2026),
            "justice_divers": int(prov_justice_divers),
            "fedasil": int(prov_fedasil),
            "bpost": int(prov_bpost),
            "bienetre": int(prov_bienetre),
            "named_surpop": int(named_surpop),
            "named_esa": int(named_esa),
            "named_eco_soc": int(named_eco_soc),
            "named_reorg": int(named_reorg),
            "named_tria": int(named_tria),
            "named_cpl": int(named_cpl),
            "named_sum": int(named_sum),
            "path_2025_adj": int(prov_total_2025_adj),
            "coa_flag": "prefer section credits over provision when beneficiary known",
        },
        separators=(",", ":"),
    ),
    remaining_eur="",
    status="active",
    evaluation_url="https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
    stated_goal="Cross-department contingency and policy packages",
    cut_option="Move known uses to sections (CoA); dual prison/ESA/Fedasil tracking",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="Federal>BOSA>provision_generale_2026",
    notes=f"829.8m; justice/divers 618m holds ESA 176 + surpop 259; tick{TICK}",
)

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def addl(iid, **kw):
    if any(r["item_id"] == iid for r in lb):
        return
    row = {k: "" for k in lf}
    row.update(kw)
    lb.append(row)


addl(
    "lb_entity1_social_triple_6_5bn_2026",
    name="Entity I social transfers triple 6.5bn 2026",
    level="federal",
    type="social_transfer",
    hierarchy_path="EntityI>social_triple_2026",
    annual_cost_eur=str(int(social_triple)),
    total_cost_eur=str(int(social_triple)),
    tco_notes="Strong CoA: handicap 3.3 + ages 1.0 + RIS 2.2 (+UA 299m excl); dual DG HAN/SPP IS deep-dives",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Disabled, elderly IGO, RIS via CPAS",
    stated_goal="Federal social assistance direct budget lines",
    measured_outcome="Core safety nets outside SS institutions; dual unemp reform RIS pressure",
    absurdity_score="2",
    cost_score="9.0",
    difficulty="5",
    priority_index="5.9",
    cut_proposal="Core; reconcile 3.3 vs DG HAN 2.93 perimeter; dual full RIS cash",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_entity1_handicap_3_3bn_2026",
    name="Entity I disability aid 3.3bn 2026 budget",
    level="federal",
    type="social_transfer",
    hierarchy_path="EntityI>handicap_2026",
    annual_cost_eur=str(int(handicap)),
    total_cost_eur=str(int(handicap)),
    tco_notes="Strong CoA class 3.3bn 2026; dual DG HAN ARR/AI 2.93bn 2025 outturn (year/perimeter delta)",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Persons with disabilities",
    stated_goal="Federal disability income support",
    measured_outcome="Dual tick429; reform 1987 law ongoing",
    absurdity_score="2",
    cost_score="9.0",
    difficulty="6",
    priority_index="5.7",
    cut_proposal="Publish ARR/AI cash split in budget docs",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_entity1_igo_1bn_2026",
    name="Entity I elderly aid IGO 1.0bn 2026",
    level="federal",
    type="social_transfer",
    hierarchy_path="EntityI>ages_igo_2026",
    annual_cost_eur=str(int(ages_igo)),
    total_cost_eur=str(int(ages_igo)),
    tco_notes="Strong CoA 1.0bn; dual PensionStat GRAPA stock ~120k / ~1.0bn class",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Elderly GRAPA/IGO recipients",
    stated_goal="Income guarantee for elderly",
    measured_outcome="Core floor; dual FPD payment",
    absurdity_score="2",
    cost_score="8.5",
    difficulty="5",
    priority_index="5.6",
    cut_proposal="Track take-up vs legal pensions path",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_prov_gen_830m_2026",
    name="Interdepartmental general provision 830m 2026",
    level="federal",
    type="ops",
    hierarchy_path="Federal>BOSA>prov_gen_2026",
    annual_cost_eur=str(int(prov_total_2026)),
    total_cost_eur=str(int(prov_total_2026)),
    tco_notes="Strong: 829.8m (+230m YoY); justice/divers 618 holds ESA 176 + prison 259; CoA prefers section credits",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Multi-programme federal packages",
    stated_goal="Cross-cutting provision",
    measured_outcome="Opacity risk when uses known but parked in provision",
    absurdity_score="6",
    cost_score="7.5",
    difficulty="4",
    priority_index="6.3",
    cut_proposal="Book known uses on section lines; dual prison envelope",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_prov_esa_176m_2026",
    name="ESA Belgium contribution via provision 176m 2026",
    level="federal",
    type="ops",
    hierarchy_path="Federal>ESA>prov_2026",
    annual_cost_eur=str(int(named_esa)),
    total_cost_eur=str(int(named_esa)),
    tco_notes="Strong CoA list inside justice/divers provision 176m ESA 2026",
    confidence="strong",
    source_id=SRC,
    beneficiaries="European Space Agency programmes",
    stated_goal="Belgium ESA membership contribution",
    measured_outcome="Parked in justice/divers provision not space section",
    absurdity_score="5",
    cost_score="6.5",
    difficulty="3",
    priority_index="5.5",
    cut_proposal="Move to proper section for transparency",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_prov_bpost_78m_2026",
    name="bpost new contracts provision 78m 2026",
    level="federal",
    type="ops",
    hierarchy_path="Federal>bpost>prov_contracts_2026",
    annual_cost_eur=str(int(prov_bpost)),
    total_cost_eur=str(int(prov_bpost)),
    tco_notes="Strong: 78m 2026 (85.4 prior); dual NBB bpost subsidy path / USO FOI residual",
    confidence="strong",
    source_id=SRC,
    beneficiaries="bpost contracts",
    stated_goal="New postal service contracts provision",
    measured_outcome="Dual PSO/USO transparency residual",
    absurdity_score="5",
    cost_score="5.5",
    difficulty="5",
    priority_index="5.0",
    cut_proposal="Publish contract L5 dual gap_bpost_uso",
    status="seed",
    notes=f"tick{TICK}",
)

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())
for r in rq:
    if r["task_id"] == "rq_423":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = f"tick{TICK}: Entity I social triple 6.5bn + prov gen 830m L5; spawn rq_424"
if not any(r["task_id"] == "rq_424" for r in rq):
    rq.append(
        {
            "task_id": "rq_424",
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
            "notes": f"Spawned tick{TICK} after Entity I social+prov; rq_116 SWA deferred",
        }
    )
with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    st = list(csv.DictReader(f))
    sfields = list(st[0].keys())
st[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": NOW,
        "last_unit_id": UNIT,
        "ticks_completed": str(TICK),
        "paused": "no",
        "notes": f"Scheduler 60s. Next prio5 rq_424; rq_116 SWA deferred. tick{TICK} Entity I social 6.5bn + prov 830m.",
    }
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, extrasaction="ignore")
    w.writeheader()
    w.writerows(st)

print("OK", TICK, "triple", int(social_triple), "prov", int(prov_total_2026), "named", int(named_sum))
print("bud", len(bud), "cmt", len(cmt), "lb", len(lb))

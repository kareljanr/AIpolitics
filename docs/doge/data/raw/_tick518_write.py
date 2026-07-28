# tick518 — CoA consultancy residual 101-contract procurement compliance L5 dual
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_consultancy_101_compliance_2025,CoA consultancy 2025 Ch6 101-contract procurement compliance,"
        "docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Rekenhof AG 22 Oct 2025,2026-07-29,court_of_audit,"
        "Strong tick518: 101 contracts 2.2bn sample; incomplete docs 63pct/1.5bn; no cost-benefit 78pct/1.8bn; "
        "exclusion 67pct/1.7bn; named overruns org 1.8->47 SAP 10->22 data 72->110; dual tick514; tick518\n"
    )
    f.write(
        "src_dual_consultancy_compliance_tick518,Dual consultancy spend opacity + procurement non-compliance,"
        "docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "DOGE synthesis CoA 101-contract findings + 2.5bn stack,2026-07-29,synthesis,"
        "Strong dual: 2.2bn sample compliance failures under 2.5bn consultancy stack; tick518\n"
    )

buds = [
    "bud_cons_sample_101_2_2bn_2020_22,sec_federal,2022,2200000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,101 consultancy contracts sample spend 2.2bn incl VAT 2020-22 legality review; tick518",
    "bud_cons_incomplete_docs_15bn,sec_federal,2022,1500000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,63.37pct dossiers incomplete documentation = 1.5bn of which 1.3bn still used; tick518",
    "bud_cons_no_costbenefit_18bn,sec_federal,2022,1800000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,78.22pct missing cost-benefit vs internal = 1.8bn spend class; tick518",
    "bud_cons_need_not_justified_1bn,sec_federal,2022,1000000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,20.79pct need not correctly justified = 1.0bn; half dossiers prep phase weak = 1.3bn; tick518",
    "bud_cons_no_realistic_estimate_14bn,sec_federal,2022,1400000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,44.55pct no realistic value estimate = 1.4bn; tick518",
    "bud_cons_exclusion_not_checked_17bn,sec_federal,2022,1700000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,67.47pct no proof exclusion grounds checked = 1.7bn; tick518",
    "bud_cons_selection_criteria_fail_11bn,sec_federal,2022,1100000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,39.19pct selection criteria deficiencies = 1.1bn; 60.81pct criteria unrelated 1.4bn; tick518",
    "bud_cons_abnormal_prices_14bn,sec_federal,2022,1400000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,60.24pct abnormal price analysis issues = 1.4bn; tick518",
    "bud_cons_award_decision_fail_15bn,sec_federal,2022,1500000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,40.45pct motivated award decision missing/deficient = 1.5bn; tick518",
    "bud_cons_delegation_fail_586m,sec_federal,2022,586100000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,12.87pct internal delegation/ordonnateur fail = 586.1m; tick518",
    "bud_cons_negotiation_fail_280m,sec_federal,2022,280000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,10.34pct negotiation documentation fail = 280m; tick518",
    "bud_cons_forfait_fail_78m,sec_federal,2022,77900000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,8.14pct forfait principle not respected = 77.9m; tick518",
    "bud_cons_no_competition_98m,sec_federal,2022,9800000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,11.76pct no competition call without justification = 9.8m; tick518",
    "bud_cons_overrun_org_47m,sec_federal,2022,47000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,Named: org consultancy est 1.8m executed >47m; tick518",
    "bud_cons_overrun_sap_22m,sec_federal,2022,22000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,Named: SAP app est 10m awarded >22m (offers 30-49m); tick518",
    "bud_cons_overrun_datamine_110m,sec_federal,2022,110000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,Named: datamining licenses est 72m awarded 110m; tick518",
    "bud_cons_overrun_400k_to_10m,sec_federal,2022,10000000,,,outturn,src_ccrek_consultancy_101_compliance_2025,strong,Named: est 400k became actual 10m class; tick518",
    "bud_cons_tactical_ra_150m,sec_federal,2022,150300000,,,budgeted,src_ccrek_consultancy_101_compliance_2025,medium,Tactical/operational consultancy RA max from participant needs 150.3m; tick518",
    "bud_dual_cons_compliance_2022,gg_belgium,2022,2200000000,,,derived,src_dual_consultancy_compliance_tick518,strong,Dual 2.2bn sample compliance failures; tick518",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_cons_101_compliance_matrix,Consultancy 101-contract procurement non-compliance matrix CoA,"
        "sec_federal,Federal buyers consultants,"
        "CoA consultancy 2025 Ch6,"
        "2025-10-22,2020,2022,2200000000,"
        '"{""sample_m"":2200,""incomplete_docs_pct"":63.37,""incomplete_docs_m"":1500,'
        '""no_costbenefit_pct"":78.22,""no_costbenefit_m"":1800,'
        '""need_not_justified_pct"":20.79,""need_not_justified_m"":1000,'
        '""no_estimate_pct"":44.55,""no_estimate_m"":1400,'
        '""exclusion_pct"":67.47,""exclusion_m"":1700,'
        '""selection_fail_pct"":39.19,""selection_fail_m"":1100,'
        '""abnormal_price_pct"":60.24,""abnormal_price_m"":1400,'
        '""award_decision_pct"":40.45,""award_decision_m"":1500,'
        '""delegation_pct"":12.87,""delegation_m"":586.1,'
        '""negotiation_pct"":10.34,""negotiation_m"":280,'
        '""forfait_pct"":8.14,""forfait_m"":77.9,'
        '""note"":""Strong CoA sample not full population; percentages of applicable contracts""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Enforce procurement compliance,Publish named L5 FOI,"
        "src_ccrek_consultancy_101_compliance_2025,strong,Federal>Consultancy>compliance_101,tick518"
    ),
    (
        "cmt_cons_named_overruns,Named consultancy estimate-to-award overruns CoA sample,"
        "sec_federal,Federal buyers,"
        "CoA consultancy 2025 §6 estimate examples,"
        "2025-10-22,2020,2022,189000000,"
        '"{""org_consult_est_m"":1.8,""org_consult_actual_m"":47,'
        '""sap_est_m"":10,""sap_award_m"":22,""datamine_est_m"":72,""datamine_award_m"":110,'
        '""micro_est_k"":400,""micro_actual_m"":10,'
        '""note"":""Strong CoA named examples; entities not always named publicly""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Stop estimate fraud,Named FOI awards,"
        "src_ccrek_consultancy_101_compliance_2025,strong,Federal>Consultancy>overruns,tick518"
    ),
    (
        "cmt_dual_cons_compliance,Dual consultancy mega-spend + procurement non-compliance,"
        "gg_belgium,Taxpayers,"
        "CoA consultancy dual,"
        "2025-10-22,2020,2022,2200000000,"
        '"{""sample_m"":2200,""stack_3y_m"":2524.7,""no_costbenefit_m"":1800,'
        '""note"":""not additive pure TE; dual governance failure""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Fix dual IT procurement governance,Inventory+compliance FOI,"
        "src_dual_consultancy_compliance_tick518,strong,BE>dual>consultancy_compliance,tick518"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_cons_101_sample_2_2bn,Consultancy 101-contract sample 2.2bn non-compliance,federal,ops,Federal>Consultancy>sample_101,733000000,2200000000,Strong CoA: 2.2bn sample systemic procurement failures; dual 2.5bn stack,strong,src_ccrek_consultancy_101_compliance_2025,Federal buyers,Procurement legality,Governance failure mega,8.0,9.0,5,8.15,Enforce rules FOI,seed,,tick518",
    "lb_cons_no_costbenefit_18bn,No cost-benefit 78pct of consultancy 1.8bn sample,federal,ops,Federal>Consultancy>no_costbenefit,600000000,1800000000,Strong CoA: 78.22pct missing make-or-buy = 1.8bn class,strong,src_ccrek_consultancy_101_compliance_2025,Taxpayers,Outsourcing without analysis,Core absurdity,8.5,9.0,4,8.35,Mandatory CBA FOI,seed,,tick518",
    "lb_cons_exclusion_17bn,Exclusion grounds unchecked 67pct 1.7bn,federal,ops,Federal>Consultancy>exclusion_fail,567000000,1700000000,Strong CoA: 67.47pct no exclusion proof = 1.7bn,strong,src_ccrek_consultancy_101_compliance_2025,Integrity,Contractor integrity checks,Compliance failure,8.0,9.0,3,8.15,Strict checks FOI,seed,,tick518",
    "lb_cons_org_overrun_47m,Org consultancy est 1.8m actual >47m,federal,ops,Federal>Consultancy>overrun_org,47000000,47000000,Strong CoA named overrun 26x estimate,strong,src_ccrek_consultancy_101_compliance_2025,Consultancies,Organisation advisory,Classic overrun,8.5,5.5,4,7.15,Name entity FOI,seed,,tick518",
    "lb_cons_datamine_110m,Datamining licenses est 72m award 110m,federal,ops,Federal>Consultancy>overrun_datamine,110000000,110000000,Strong CoA: est 72 awarded 110m,strong,src_ccrek_consultancy_101_compliance_2025,Software vendors,Data mining licences,Estimate failure,6.5,7.5,4,6.75,Benchmark FOI,seed,,tick518",
    "lb_cons_incomplete_docs_15bn,Incomplete procurement files 63pct 1.5bn,federal,ops,Federal>Consultancy>incomplete_docs,500000000,1500000000,Strong CoA: 63.37pct incomplete files 1.5bn (1.3bn still spent),strong,src_ccrek_consultancy_101_compliance_2025,Auditors,Document retention,Traceability failure,7.5,9.0,3,7.95,Archive FOI,seed,,tick518",
    "lb_dual_cons_compliance,Dual consultancy 2.2bn sample compliance failure,multi,ops,BE>dual>consultancy_compliance,733000000,2200000000,Strong dual CoA residual,strong,src_dual_consultancy_compliance_tick518,Taxpayers,Dual procurement map,Scale dual,7.5,9.0,5,7.85,Inventory+compliance FOI,seed,,tick518",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_cons_101_named_overruns_l5,Federal>Consultancy>101_named_overruns_L5,sec_federal,"
    "Named entities and contract IDs for sample overruns (org 1.8->47m; SAP 10->22m; datamine 72->110m; "
    "400k->10m); list of 101 contracts with award amounts and deficiency flags; remediation status "
    "on exclusion-ground checks and cost-benefit for recurrent IT;"
    "CoA 2025: systemic non-compliance on 2.2bn sample; named overruns without public IDs,8,"
    "FOD BOSA / Inspectie van Financiën,info@bosa.fgov.be,"
    ",docs/doge/foi/drafts/gap_cons_101_named_overruns_l5.md,"
    "ready,2026-07-29,,,,,cmt_cons_named_overruns,"
    "lb_cons_101_sample_2_2bn|lb_cons_org_overrun_47m|lb_cons_no_costbenefit_18bn,"
    "2026-07-29T02:40:00Z,2026-07-29T02:40:00Z,"
    "tick518: CoA consultancy 101 compliance residual; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_509,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T02:20:00Z,,Spawned tick517 after CoA Smals broker; progress@520 next ticks; rq_116 deferred"
)
new = (
    "rq_509,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_cons_101_named_overruns_l5,"
    "2026-07-29T02:20:00Z,2026-07-29T02:40:00Z,"
    "tick518: CoA consultancy 101 contracts 2.2bn compliance dual; FOI; progress@520 next; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_509 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_510,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T02:40:00Z,,Spawned tick518 after CoA consultancy 101 compliance; progress@520 next tick; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T02:40:00Z,rq_509,518,no,"
    "Tick518 CoA consultancy 101 contracts 2.2bn compliance dual; next prio5 rq_510; progress@520 next; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick518 OK")

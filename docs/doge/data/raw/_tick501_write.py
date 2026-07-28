# tick501 — CoA 2026_19 DWV study contracts overrun dual Lantis/GIP
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_dwv_studies_2026,Rekenhof De Werkvennootschap uitvoering studieopdrachten 2026_19,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf,"
        "Rekenhof NL chamber 31 Mar 2026,2026-07-28,court_of_audit,"
        "Strong: 4 study contracts R0 Noord/Oost Brabantnet R4; R0N award 36m spent 85.4m est 103.6m; "
        "Brabantnet 5.9->11m+8.75 extra; R4 +40pct; dual GIP/Lantis; tick501\n"
    )
    f.write(
        "src_ccrek_dwv_studies_press_2026,CoA press DWV studieopdrachten Apr 2026,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap_Persbericht.pdf,"
        "Rekenhof,2026-07-28,court_of_audit_press,"
        "Strong headlines: 3/4 overruns; all 4 delayed; OP-posten; dependency risk; tick501\n"
    )
    f.write(
        "src_dual_dwv_lantis_gip_tick501,Dual DWV study overruns vs Lantis Toekomstverbond + GIP,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf,"
        "DOGE synthesis CoA DWV+RR2025 Lantis/GIP,2026-07-28,synthesis,"
        "Strong dual: DWV study cash >120m class 4 dossiers vs Lantis cum 3.85bn Toekomstverbond; same mobility stack; tick501\n"
    )

buds = [
    "bud_dwv_r0_noord_award_2016,de_werkvennootschap,2016,36000000,,,budgeted,src_ccrek_dwv_studies_2026,strong,R0 Noord study award 36m Dec2016 (AWV prep then DWV); tick501",
    "bud_dwv_r0_noord_spent_2025_03,de_werkvennootschap,2025,85400000,,,outturn,src_ccrek_dwv_studies_2026,strong,R0 Noord study spent 85.4m to Mar2025 (>2x award); tick501",
    "bud_dwv_r0_noord_est_2023,de_werkvennootschap,2023,103600000,,,estimated,src_ccrek_dwv_studies_2026,strong,R0 Noord revised total study budget estimate 103.6m 2023 (uncertain if enough); tick501",
    "bud_dwv_r0_noord_op_posten_2025,de_werkvennootschap,2025,9400000,,,outturn,src_ccrek_dwv_studies_2026,strong,R0 Noord OP-posten unforeseen expertise almost 9.4m Mar2025 without competition; tick501",
    "bud_dwv_r0_oost_annual_award,de_werkvennootschap,2018,3500000,,,budgeted,src_ccrek_dwv_studies_2026,strong,R0 Oost study award 3.5m per year 2018; tick501",
    "bud_dwv_r0_oost_spent_2025_03,de_werkvennootschap,2025,11100000,,,outturn,src_ccrek_dwv_studies_2026,strong,R0 Oost study spent 11.1m to Mar2025; tick501",
    "bud_dwv_r0_oost_quickwins_2023,de_werkvennootschap,2023,3700000,,,outturn,src_ccrek_dwv_studies_2026,strong,R0 Oost extra 3.7m same provider 2023 three quick wins unpublished change; tick501",
    "bud_dwv_brabantnet_award_2014,de_werkvennootschap,2014,5900000,,,budgeted,src_ccrek_dwv_studies_2026,strong,Brabantnet study award 5.9m 2014 De Lijn then DWV; tick501",
    "bud_dwv_brabantnet_spent_2025_03,de_werkvennootschap,2025,11000000,,,outturn,src_ccrek_dwv_studies_2026,strong,Brabantnet original study spent 11.0m Mar2025; tick501",
    "bud_dwv_brabantnet_extra_studies,de_werkvennootschap,2025,8750000,,,outturn,src_ccrek_dwv_studies_2026,strong,Brabantnet additional/new studies total 8.75m (ringtrambus 0.1 luchthaven 5.1 sneltram 3.6); tick501",
    "bud_dwv_brabantnet_lost_0_2m,de_werkvennootschap,2025,200000,,,outturn,src_ccrek_dwv_studies_2026,strong,Brabantnet lost study costs from policy rework ~0.2m (DWV claim after suspension); tick501",
    "bud_dwv_r4_award,de_werkvennootschap,2017,12100000,,,budgeted,src_ccrek_dwv_studies_2026,strong,R4 West/Oost study award 12.1m (DWV re-tender after AWV first); tick501",
    "bud_dwv_r4_spent_class_2025_03,de_werkvennootschap,2025,16940000,,,outturn,src_ccrek_dwv_studies_2026,strong,R4 spent class ~17m Mar2025 (award 12.1 +>40pct CoA); tick501",
    "bud_dwv_r4_deel4_raise_2023,de_werkvennootschap,2023,9200000,,,budgeted,src_ccrek_dwv_studies_2026,strong,R4 deelopdracht4 studiebudget raised 4.3->9.2m 2023; undermines plafond; tick501",
    "bud_dwv_studies4_spent_class_2025,de_werkvennootschap,2025,124900000,,,outturn,src_ccrek_dwv_studies_2026,strong,Four audited studies spent class ~124.9m Mar2025 (85.4+11.1+11.0+17.4); still running; tick501",
    "bud_dual_dwv_studies_vs_lantis,gg_belgium,2025,124900000,,,derived,src_dual_dwv_lantis_gip_tick501,strong,Dual DWV study cash 125m class vs Lantis Toekomstverbond 3.85bn same mobility stack; tick501",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_dwv_studies_four_audit,DWV four long study contracts CoA overrun audit,"
        "de_werkvennootschap,WADR R0 Brabantnet R4 infrastructure studies,"
        "CoA 2026_19 + awards 2014-2018,"
        "2014-04-01,2014,2027,124900000,"
        '"{""r0n_award_m"":36,""r0n_spent_m"":85.4,""r0n_est_m"":103.6,""r0n_op_m"":9.4,'
        '""r0o_annual_m"":3.5,""r0o_spent_m"":11.1,""r0o_quick_m"":3.7,'
        '""brab_award_m"":5.9,""brab_spent_m"":11.0,""brab_extra_m"":8.75,'
        '""r4_award_m"":12.1,""r4_overrun_pct_gt"":40,""all_delayed"":true,'
        '""note"":""Strong CoA: 3/4 major overruns; competition/transparency risks; dual GIP""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf,"
        "Prepare complex mobility infrastructure,Strict procurement+plafond; FOI contractor L5,"
        "src_ccrek_dwv_studies_2026,strong,Vlaanderen>DWV>studieopdrachten,tick501 dual Lantis"
    ),
    (
        "cmt_dwv_r0_noord_study,R0 Noord ring study contract path 36 to 104m,"
        "de_werkvennootschap,Brussels ring north redesign studies,"
        "Award Dec2016 + CoA 2026_19,"
        "2016-12-01,2016,2027,103600000,"
        '"{""award_m"":36,""spent_mar2025_m"":85.4,""est_2023_m"":103.6,""op_posten_m"":9.4,'
        '""note"":""Strong CoA: >2x award; OP without competition""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf,"
        "R0 North multimodal redesign studies,Cap OP-posten; recompete material changes,"
        "src_ccrek_dwv_studies_2026,strong,Vlaanderen>DWV>R0_Noord,tick501"
    ),
    (
        "cmt_dwv_brabantnet_study,Brabantnet tram studies split three projects,"
        "de_werkvennootschap,Ringtrambus Luchthaventram Sneltram,"
        "De Lijn 2014 award + CoA 2026_19,"
        "2014-04-01,2014,2027,19750000,"
        '"{""award_m"":5.9,""spent_m"":11.0,""extra_m"":8.75,""ringtrambus_m"":0.1,'
        '""luchthaven_m"":5.1,""sneltram_m"":3.6,""lost_policy_m"":0.2,'
        '""sneltram_in_gip_2025_27"":false,'
        '""note"":""Strong CoA: monopoly re-award risk; policy churn""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf,"
        "Three tram corridors north of Brussels,Recompete material changes; GIP alignment,"
        "src_ccrek_dwv_studies_2026,strong,Vlaanderen>DWV>Brabantnet,tick501"
    ),
    (
        "cmt_dual_dwv_lantis_mobility,Dual DWV study overruns + Lantis Toekomstverbond stock,"
        "gg_belgium,Flanders mobility mega-projects,"
        "CoA DWV 2026_19 + RR2025 Lantis Table23,"
        "2014-01-01,2014,2027,3976500000,"
        '"{""dwv_studies4_spent_m"":124.9,""lantis_toekomst_cum_m"":3851.6,'
        '""note"":""not additive TE; study cash vs project financing stock dual WADR/Oosterweel stack""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf,"
        "Map dual VL mobility delivery vehicles,Comparable L5 contractor governance,"
        "src_dual_dwv_lantis_gip_tick501,strong,BE>dual>Mobility>DWV_Lantis,tick501"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_dwv_r0_noord_study_104m,DWV R0 Noord study path 85-104m vs 36m award,regional,consultancy,Vlaanderen>DWV>R0_Noord_study,85400000,103600000,Strong CoA: spent 85.4m Mar2025 est 103.6m award 36m; OP 9.4m no competition; dual WADR,strong,src_ccrek_dwv_studies_2026,Ring north users,R0 North redesign studies,Classic study-scope creep mega-contract,7.5,7.5,5,7.25,Recompete material change; cap OP; FOI names,seed,,tick501",
    "lb_dwv_studies4_125m,DWV four audited study contracts ~125m spent Mar2025,regional,consultancy,Vlaanderen>DWV>studieopdrachten_4,124900000,124900000,Strong CoA sample: R0N 85.4 R0O 11.1 Brabantnet 11.0 R4 ~17 class still running; 3/4 overruns,strong,src_ccrek_dwv_studies_2026,Mobility projects,Complex infra preparation,Procurement transparency risks CoA,7.0,7.5,5,7.0,Strict plafond+publication; dual Lantis,seed,,tick501",
    "lb_dwv_brabantnet_study_20m,Brabantnet studies 11m+8.75m extras vs 5.9m award,regional,consultancy,Vlaanderen>DWV>Brabantnet_study,19750000,19750000,Strong CoA: original 11m + extras 8.75; monopoly re-award risk; sneltram off GIP 2025-27,strong,src_ccrek_dwv_studies_2026,North-rand transit users,Three tram corridors studies,Policy churn drives study cost,6.5,6.5,5,6.25,Recompete; GIP inclusion decision,seed,,tick501",
    "lb_dwv_r0_oost_study_11m,R0 Oost study 11.1m spent +3.7m quick wins,regional,consultancy,Vlaanderen>DWV>R0_Oost_study,11100000,14800000,Strong CoA: 3.5m/yr award; 11.1 spent; 3.7m same provider unpublished; stop risk,strong,src_ccrek_dwv_studies_2026,R0 east nodes users,Four junctions redesign studies,Extension without transparency,6.5,5.5,4,6.05,Publish changes; dual R0 Noord,seed,,tick501",
    "lb_dwv_r4_study_overrun,R4 West/Oost study >40pct over 12.1m award,regional,consultancy,Vlaanderen>DWV>R4_study,16940000,16940000,Strong CoA: award 12.1m +>40pct; deel4 4.3->9.2m undermines plafond,strong,src_ccrek_dwv_studies_2026,Ghent R4 users,Primary road conversion studies,Plafond control failure,6.5,5.5,4,6.05,Enforce plafond; FOI L5,seed,,tick501",
    "lb_dual_dwv_lantis_mobility,Dual DWV studies 125m + Lantis Toekomstverbond 3.85bn,multi,programme,BE>dual>Mobility_DWV_Lantis,124900000,3976500000,Strong dual CoA: study cash vs project finance stock same VL mobility mega-stack,strong,src_dual_dwv_lantis_gip_tick501,Flanders mobility users,Multi-vehicle delivery,Governance dual FOI L5 contractors,5.5,8.0,5,6.45,Comparable contractor L5 both vehicles,seed,,tick501",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_dwv_studies_contractor_l5,Vlaanderen>DWV>studieopdrachten>contractors_L5,de_werkvennootschap,"
    "Named contractors/consortia + cash-by-year 2014-2026 for R0 Noord R0 Oost Brabantnet R4 studies "
    "incl OP-posten 9.4m R0N and Brabantnet extras 8.75m and all bijakten/verrekeningen,"
    "CoA 2026_19 aggregates strong; end-provider L5 and full cash schedule opaque public,8,"
    "De Werkvennootschap / Team Openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_dwv_studies_contractor_l5.md,"
    "ready,2026-07-28,,,,,cmt_dwv_studies_four_audit,"
    "lb_dwv_studies4_125m|lb_dwv_r0_noord_study_104m,"
    "2026-07-28T21:10:00Z,2026-07-28T21:10:00Z,"
    "tick501: CoA 2026_19 primary fill; residual contractor L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_492,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T20:50:00Z,,Spawned tick500 after progress@500; rq_116 deferred"
)
new = (
    "rq_492,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_dwv_studies_contractor_l5,"
    "2026-07-28T20:50:00Z,2026-07-28T21:10:00Z,"
    "tick501: CoA 2026_19 DWV studies R0N 85-104m Brabantnet dual Lantis; FOI L5; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_492 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_493,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T21:10:00Z,,Spawned tick501 after CoA DWV studieopdrachten; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T21:10:00Z,rq_492,501,no,"
    "Tick501 CoA DWV studies R0N 85-104m +4-pack ~125m dual Lantis; next prio5 rq_493; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick501 OK")

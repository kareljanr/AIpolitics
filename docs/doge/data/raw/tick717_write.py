# tick717 — VL GIP monitoring/eval/governance residual dual WAL
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]

budgets = [
    ("bud_vl_gip_monitor_volume_2503m", "vlaanderen_gov", 2026, 2503000000, "", "", "budgeted", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "GIP avg ~2503m/yr under failed monitoring/eval instrument CoA ch6-8; tick717"),
    ("bud_vl_gip_horizon_fail_3y_not_5y", "vlaanderen_gov", 2025, 2501000000, "", "", "budgeted", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Ambition 5y GIP collapsed to 3y 2025-27 then 1y actu2026 only CoA ch8; tick717"),
    ("bud_vl_gip_actu_1y_only_3685m", "vlaanderen_gov", 2026, 3685000000, "", "", "budgeted", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Actualisatie 2026 one-year GIP 3685m; multi-year 2027-29 not validated CoA; tick717"),
    ("bud_vl_gip_ic_fte_capacity_3", "mow_investeringscel", 2025, 3, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Investeringscel ~3 FTE insufficient for modusneutral regie CoA s7.2; tick717"),
    ("bud_vl_gip_vek_reporting_not_live_2026", "vlaanderen_gov", 2026, 0, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "VEK reporting pilot since 2021; promised begin 2026 still not operational CoA s6.1; tick717"),
    ("bud_vl_gip_encours_program_not_live", "vlaanderen_gov", 2026, 0, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Openstaande verbintenissen program-level reporting not delivered CoA s6.1; tick717"),
    ("bud_vl_gip_public_exec_report_missing", "vlaanderen_gov", 2026, 0, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "RA promised annual public GIP execution report not published CoA s6.1; tick717"),
    ("bud_vl_gip_tool_dec2025_gradual", "mow_investeringscel", 2025, 1, "", "", "budgeted", "src_ccrek_vl_gip_monitor_eval_2026", "medium", "GIP-tool gradual ops from Dec 2025; CoA/IC: no guarantee internal data quality fix; tick717"),
    ("bud_vl_gip_pps_beschik_horizon_y", "vlaanderen_gov", 2026, 25, "", "", "projected", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "PPS availability 20-25-30y not matched in GIP look-through CoA s6.1; tick717"),
    ("bud_vl_gip_lcca_goal_2030_flag", "vlaanderen_gov", 2030, 1, "", "", "projected", "src_ccrek_vl_gip_monitor_eval_2026", "medium", "Dept goal know full MOW patrimony lifecycle cost by 2030; GIP lacks project LCCA CoA s6.2; tick717"),
    ("bud_vl_gip_recs_count_16", "vlaanderen_gov", 2026, 16, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "CoA 16 formal recommendations ch9; monitor.ccrek.be follow-up earliest +1y; tick717"),
    ("bud_vl_gip_minister_reply_2026_06_09", "vlaanderen_gov", 2026, 1, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Minister De Ridder reply 9 Jun 2026: GIP tool + BA2027 separate basisallocaties GIP link; soft vs CoA hard fail; tick717"),
    ("bud_vl_gip_score_flip_am_1_to_5", "vlaanderen_gov", 2026, 5, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Annex1: AM score GIP001723 tram track Gent 1->5 between GIP2025-27 and 2026-29; tick717"),
    ("bud_vl_gip_score_flip_fiets_4_to_1", "vlaanderen_gov", 2026, 1, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Annex1: fiets score Waasmunsterbrug GIP000354/01 4->1; tick717"),
    ("bud_vl_gip_id_collision_n44_aalter", "vlaanderen_gov", 2025, 1, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Same GIP00465664 used for both Uitvoering and Onteigening N44 Aalter; tick717"),
    ("bud_vl_gip_no_output_km_indicators", "vlaanderen_gov", 2026, 0, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "GIP does not state km tunnels/roads renovated for budget; blocks ex-post eval CoA s6.2; tick717"),
    ("bud_vl_gip_no_total_project_cost_field", "vlaanderen_gov", 2026, 0, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "Project lines lack total invest cost past/future study expropriation finance O&M CoA s6.2; tick717"),
    ("bud_vl_gip_internal_reports_unpublished", "mow_investeringscel", 2026, 1, "", "", "outturn", "src_ccrek_vl_gip_monitor_eval_2026", "strong", "IC holds basis/fiets/AM reports and GIS map unpublished externally CoA s6.1; tick717"),
    ("bud_vl_gip_ba2027_basisalloc_promise", "vlaanderen_gov", 2027, 1, "", "", "budgeted", "src_ccrek_vl_gip_monitor_eval_2026", "medium", "Minister: BO2027 separate basisallocaties to 1-to-1 link GIP spend; not yet outturn; tick717"),
    ("bud_dual_gip_monitor_sofico_2026", "gg_belgium", 2026, 2503000000, "", "", "budgeted", "src_dual_gip_monitor_wal_tick717", "strong", "Dual VL GIP monitor fail on 2.5bn vs WAL SOFICO RA transparency residual; not TE-additive; tick717"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_vl_gip_monitor_eval_fail_2026",
        "VL GIP monitoring reporting evaluation fail dual residual",
        "vlaanderen_gov",
        "MOW entities parliament public",
        "CoA 2026_27 ch6-8 + RA 2024-2029 GIP 2.0 promises",
        "2025-07-14",
        2025,
        2030,
        2503000000,
        '{"avg_gip_m":2503,"actu_2026_m":3685,"horizon":"3y_then_1y","vek_live":false,"encours_live":false,"public_exec_report":false,"gip_tool":"dec2025_gradual","lcca_goal":2030,"recs":16,"minister_reply":"2026-06-09"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Turn GIP into reliable multi-year steering and accountability instrument",
        "Publish VEK+encours+output km; legal frame; IC mandate+FTE",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "strong",
        "Vlaanderen>MOW>GIP_monitor",
        "tick717 CoA ch6-8",
    ),
    (
        "cmt_vl_gip_vek_encours_gap",
        "GIP VEK and open commitments reporting gap since 2021",
        "vlaanderen_gov",
        "MOW invest cash timing",
        "Omzendbrief GIP 2019 + CoA s6.1",
        "2021-01-01",
        2021,
        2026,
        0,
        '{"vek_pilot_since":2021,"global_vek_draft":2023,"promised":"begin_2026","status_coa":"not_operational","encours_program":"no_breakthrough"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Payment schedules and multi-year cash visibility",
        "Go-live VEK+encours public dashboards FOI",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "strong",
        "Vlaanderen>GIP>VEK_encours",
        "tick717",
    ),
    (
        "cmt_vl_gip_data_id_score_instability",
        "GIP data ID collisions and score flips dual residual",
        "vlaanderen_gov",
        "Investeringscel entities",
        "CoA Bijlage1 datakwaliteit en projectbeoordeling",
        "2025-01-01",
        2025,
        2026,
        0,
        '{"unique_id":false,"example_id_collision":"GIP00465664_uitvoering_and_onteigening","am_flip_GIP001723":"1_to_5","fiets_flip_GIP000354":"4_to_1","name_drift":true}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Reliable project tracking and prioritisation",
        "Immutable GIP IDs; freeze scores with change log FOI",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "strong",
        "Vlaanderen>GIP>data_quality",
        "tick717",
    ),
    (
        "cmt_vl_gip_governance_legal_gap",
        "GIP weak legal frame internal notes only dual residual",
        "vlaanderen_gov",
        "Parliament MOW entities",
        "Decreet basisbereikbaarheid 2019 + omzendbrief 2019 only CoA s7.1",
        "2019-04-26",
        2019,
        2026,
        0,
        '{"legal_anchor":"basisbereikbaarheid_mention_only","omzendbrief":2019,"enforceable_rules":false,"political_agenda_VR":true,"ic_mandate_weak":true,"fte_approx":3,"recs_legal":"rec3_rec4"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Enforceable multi-year invest governance",
        "Adopt binding GIP decree + IC mandate",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "strong",
        "Vlaanderen>GIP>governance",
        "tick717",
    ),
    (
        "cmt_vl_gip_minister_ba2027_link",
        "Minister promise BA2027 basisallocaties + GIP tool dual",
        "vlaanderen_gov",
        "Budget-GIP reconciliation",
        "Minister reply 9 Jun 2026 Bijlage2",
        "2026-06-09",
        2026,
        2027,
        0,
        '{"basisalloc_BO2027":true,"gip_tool":true,"coa_view":"tool_unproven_need_broad_data_quality","flex_annual_snapshot":true}',
        0,
        "planned",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "1-to-1 GIP to budget articles",
        "Track BO2027 delivery; dual Sofico RA model",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "medium",
        "Vlaanderen>GIP>BA2027_link",
        "tick717",
    ),
    (
        "cmt_dual_gip_monitor_sofico_tick717",
        "Dual VL GIP monitor opacity vs WAL SOFICO residual",
        "gg_belgium",
        "Entity II infrastructure users",
        "CoA GIP ch6 + prior SOFICO RA",
        "2025-01-01",
        2025,
        2026,
        2503000000,
        '{"vl_gip_avg_m":2503,"vl_public_vek":false,"wal_sofico_ra":"published_prior","note":"not TE-additive"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Comparable regional invest transparency",
        "Publish dual VEK/encours dashboards FOI",
        "src_dual_gip_monitor_wal_tick717",
        "strong",
        "Belgium>dual>GIP_monitor",
        "tick717",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_vl_gip_monitor_fail_2_5bn",
        "GIP steers ~2.5bn without VEK encours public report",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>monitor_fail",
        2503000000,
        3685000000,
        "Strong CoA ch6-8: no public exec report; VEK not live since 2021 pilots; no encours; no output km; tool unproven",
        "strong",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "Taxpayers contractors parliament",
        "Reliable multi-year invest accountability",
        "Instrument claims control while cash/outcome opaque",
        9.0,
        9.0,
        5,
        8.7,
        "Go-live public VEK+encours+output indicators FOI",
        "seed",
        "",
        "tick717",
    ),
    (
        "lb_vl_gip_horizon_collapse_5_to_1y",
        "GIP horizon collapse 5y ambition to 1y actu2026",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>horizon_collapse",
        3685000000,
        0,
        "Strong CoA: RA 5y/10y large; delivered 3y then single-year 3685m actu; entities lack predictability",
        "strong",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "Entities contractors municipalities",
        "Stable multi-year invest calendar",
        "Opposite of legislatuur-overschrijdend promise",
        8.5,
        8.5,
        4,
        8.35,
        "Lock multi-year GIP at BO not only BA; dual Sofico",
        "seed",
        "",
        "tick717",
    ),
    (
        "lb_vl_gip_data_id_score_chaos",
        "GIP ID collisions and score flips undermine ranking",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>data_chaos",
        2503000000,
        0,
        "Strong CoA annex1: non-unique IDs; same number uitvoer+onteigen; AM 1->5; fiets 4->1; name drift",
        "strong",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "Project portfolio managers",
        "Objective prioritisation",
        "Cannot track or rank if keys and scores drift",
        8.5,
        7.5,
        4,
        7.85,
        "Immutable IDs + published score change log",
        "seed",
        "",
        "tick717",
    ),
    (
        "lb_vl_gip_legal_governance_void",
        "GIP legal frame almost void IC weak mandate ~3 FTE",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>governance_void",
        2503000000,
        0,
        "Strong CoA ch7: only basisbereikbaarheid mention + 2019 circular; internal notes; IC no hard mandate; entities compete",
        "strong",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "All MOW entities",
        "Enforceable integrated invest governance",
        "Political VR agenda without binding admin rules",
        8.0,
        8.0,
        5,
        7.8,
        "Binding GIP decree + IC FTE/mandate reform",
        "seed",
        "",
        "tick717",
    ),
    (
        "lb_vl_gip_no_lcca_no_mkba",
        "GIP lacks LCCA total cost and systematic MKBA",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>no_lcca",
        2503000000,
        0,
        "Strong CoA s6.2 s7.4: no total project cost fields; no systematic MKBA/risk/scenario; PPS pre-choice risks art3 report hollow",
        "strong",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "Taxpayers future O&M",
        "Lifecycle-aware invest choice",
        "2030 LCCA goal blocked by missing GIP fields",
        8.0,
        8.0,
        5,
        7.8,
        "Mandatory total cost + MKBA for large projects",
        "seed",
        "",
        "tick717",
    ),
    (
        "lb_vl_gip_unpublished_internal_intel",
        "IC holds unpublished fiets AM GIS reports on 2.5bn",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>unpublished_intel",
        2503000000,
        0,
        "Strong CoA s6.1: thematic reports and GIS internal only; website descriptive no dashboard",
        "strong",
        "src_ccrek_vl_gip_monitor_eval_2026",
        "Public parliament researchers",
        "External controllability",
        "Transparency claim without published data products",
        7.5,
        7.5,
        3,
        7.45,
        "Publish reports GIS dashboard FOI",
        "seed",
        "",
        "tick717",
    ),
    (
        "lb_dual_gip_monitor_sofico_2026",
        "Dual VL GIP monitor fail vs WAL SOFICO RA",
        "Belgium",
        "ops",
        "Belgium>dual>GIP_monitor",
        2503000000,
        0,
        "Strong dual: VL GIP no public VEK/encours; WAL SOFICO published RA invest residual; not TE-additive",
        "strong",
        "src_dual_gip_monitor_wal_tick717",
        "Entity II citizens",
        "Comparable invest transparency",
        "Asymmetric regional accountability",
        7.5,
        8.0,
        6,
        7.4,
        "Dual public invest dashboards FOI",
        "seed",
        "",
        "tick717",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_ccrek_vl_gip_monitor_eval_2026",
        "CoA VL GIP 2026_27 monitoring evaluation governance dual residual",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Rekenhof / Cour des comptes",
        "2026-08-01",
        "audit",
        "Strong primary ch6-10 + Bijlage1-2 residual tick717",
    ),
    (
        "src_dual_gip_monitor_wal_tick717",
        "Dual VL GIP monitor opacity vs WAL SOFICO residual",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "DOGE synthesis CoA dual",
        "2026-08-01",
        "synthesis",
        "Strong dual Entity II invest transparency residual tick717",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

foi = (
    "gap_vl_gip_monitor_eval_gov_2026",
    "Vlaanderen>MOW>GIP_monitor_eval_gov",
    "vlaanderen_gov",
    "Public VEK and openstaande-verbintenissen series by programme/entity; annual GIP execution report archive; unpublished basis/fiets/AM reports and GIS export; immutable project-ID schema and score change-log (incl AM 1->5 and fiets 4->1 examples); output/effect indicators (km renovated) mapping to GIP lines; IC organigram FTE and mandate decision; BA2027 basisallocatie design docs; dual unit-cost vs SOFICO",
    "GIP claims to steer ~EUR 2.5bn+/yr but CoA finds no live VEK/encours public report and weak legal/IC governance; dual WAL Sofico residual",
    "5",
    "Departement MOW / Investeringscel / Team Openbaarheid",
    "openbaarheid@vlaanderen.be",
    "Havenlaan 88 bus 20 1000 Brussel",
    "docs/doge/foi/drafts/gap_vl_gip_monitor_eval_gov_2026.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_vl_gip_monitor_eval_fail_2026",
    "lb_vl_gip_monitor_fail_2_5bn",
    "2026-08-01T21:00:00Z",
    "2026-08-01T21:00:00Z",
    "tick717 CoA GIP monitor/eval/gov residual; not sent",
)
with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi)
print("foi +1")

rq_path = DATA / "research_queue.csv"
with open(rq_path, "r", encoding="utf-8", newline="") as f:
    r = csv.reader(f)
    header = next(r)
    rows = [header]
    for row in r:
        if row and row[0] == "rq_708":
            row[4] = "done"
            row[10] = "2026-08-01T21:00:00Z"
            row[11] = "tick717 GIP monitor/eval/gov VEK gap horizon 1y data chaos dual Sofico; FOI gap_vl_gip_monitor_eval_gov_2026 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_709" not in ids:
    rows.append(
        [
            "rq_709",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: WAL residual CoA deepen preferred (Sofico/OTW/UAP L5 new PDF) or fed Pillar2/VVPR recheck or new CoA VL kunstbeleid 2026",
            "",
            "2026-08-01T21:00:00Z",
            "",
            "spawned tick717 after rq_708",
        ]
    )
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T21:00:00Z,rq_708,717,no,tick717 VL GIP monitor/eval/gov dual Sofico; next rq_709; progress@720 in 3; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

# tick718 — fed flexi-jobs CoA 2026_34 residual HERMES/fiscal dual VL
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]

budgets = [
    ("bud_flexi_workers_q4_2024", "onss", 2024, 184360, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Flexi workers Q4 2024 184360 CoA 2026_34 ch2; tick718"),
    ("bud_flexi_hours_q4_2024", "onss", 2024, 13995721, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Flexi hours nearly 14m Q4 2024 (13995721) CoA; tick718"),
    ("bud_flexi_wage_mass_q4_2024", "onss", 2024, 220071000, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Flexi wage mass 220.071m Q4 2024 CoA Graph4; tick718"),
    ("bud_flexi_vte_q4_2024", "onss", 2024, 29500, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Flexi VTE ~29500 vs total employee VTE 3.4m Q4 2024 <1pct CoA; tick718"),
    ("bud_flexi_workers_q1_2016", "onss", 2016, 10548, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Flexi workers Q1 2016 10548 horeca only start; tick718"),
    ("bud_flexi_hours_q1_2016", "onss", 2016, 418466, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Flexi hours Q1 2016 418466; tick718"),
    ("bud_flexi_wage_mass_q1_2016", "onss", 2016, 4769300, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Flexi wage mass 4.769m Q1 2016; tick718"),
    ("bud_flexi_hourly_men_2024", "onss", 2024, 16.38, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Avg flexi hourly men 16.38 EUR end-2024 CoA; tick718"),
    ("bud_flexi_hourly_women_2024", "onss", 2024, 15.0, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Avg flexi hourly women 15.00 EUR end-2024 CoA; tick718"),
    ("bud_flexi_share_vl_85pct", "onss", 2024, 85, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "~85pct flexi jobs performed in Flanders CoA s2.6; tick718"),
    ("bud_flexi_jobs_vl_class_157525", "onss", 2024, 157525, "", "", "outturn", "src_ccrek_flexijob_2026_34", "medium", "Graph8 class VL 157525 flexi jobs path 2016-24 end class CoA p22; tick718"),
    ("bud_flexi_jobs_wal_class_21118", "onss", 2024, 21118, "", "", "outturn", "src_ccrek_flexijob_2026_34", "medium", "Graph8 class WAL 21118; tick718"),
    ("bud_flexi_jobs_bru_class_5023", "onss", 2024, 5023, "", "", "outturn", "src_ccrek_flexijob_2026_34", "medium", "Graph8 class BRU 5023; tick718"),
    ("bud_flexi_age65plus_share_18pct", "onss", 2024, 18, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "65+ share of flexi workers 18pct end-2024 (near 0 in 2016); tick718"),
    ("bud_flexi_dimona_incomplete_q4_2024", "onss", 2024, 4628, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Dimona incomplete/not declared flexi 4628 of 184360 places 2.51pct Q4 2024 T4; tick718"),
    ("bud_flexi_improper_cumul_q4_2024", "onss", 2024, 512, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Improper cumul no 4/5 or pensioner 512 places 0.28pct Q4 2024; tick718"),
    ("bud_flexi_rsz_investigations_2024", "onss", 2024, 270, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "RSZ flexi investigations 270 in 2024 (189 2023; 160 2022) T5; tick718"),
    ("bud_flexi_rsz_findings_2024", "onss", 2024, 154, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "RSZ findings flexi law 154 of 270 (57pct) 2024; tick718"),
    ("bud_flexi_rsz_regularised_high_ss_2024", "onss", 2024, 5, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Only 5 of 154 findings regularised with higher SS 2024; 24 dossiers to parquet; tick718"),
    ("bud_flexi_event_inspections_2022_24", "onss", 2024, 1, "", "", "outturn", "src_ccrek_flexijob_2026_34", "strong", "Only 1 RSZ control in event sector 2022-24 despite statutory focus; tick718"),
    ("bud_flexi_hermes_exante_vte_2026", "fod_finance", 2026, 10836, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "HERMES ex ante abolish horeca flexi: -10836 flexi VTE +10836 regular T8; tick718"),
    ("bud_flexi_hermes_exante_wage_flexi_m", "fod_finance", 2026, 294000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "Ex ante flexi wage mass shock -294m 2026 T8; tick718"),
    ("bud_flexi_hermes_exante_wage_reg_m", "fod_finance", 2026, 386000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "Ex ante regular wage mass +386m; net +92m; tick718"),
    ("bud_flexi_hermes_exante_net_wage_m", "fod_finance", 2026, 92000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "Net wage mass +92m when flexi->regular ex ante; tick718"),
    ("bud_flexi_hermes_exante_er_ss_net_m", "fod_finance", 2026, 43000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "Ex ante employer SS net -43m (flexi -82 regular +39) rate 28pct flexi; tick718"),
    ("bud_flexi_hermes_exante_ee_ss_m", "fod_finance", 2026, 38000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "Ex ante employee SS +38m; tick718"),
    ("bud_flexi_hermes_exante_suppl_er_m", "fod_finance", 2026, 28000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "Ex ante supplemental employer SS +28m; tick718"),
    ("bud_flexi_hermes_heads_shock_9199", "fod_finance", 2026, 9199, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "Labour force heads shock +/-9199 V1/V2 T8; tick718"),
    ("bud_flexi_hermes_v1_balance_2030", "fod_finance", 2030, 106000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "HERMES V1 abolish horeca flexi 2030 gov balance +106m (0.01pp GDP) T9; tick718"),
    ("bud_flexi_hermes_v2_balance_2030", "fod_finance", 2030, 213000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "HERMES V2 gov balance +213m (0.03pp GDP) 2030; tick718"),
    ("bud_flexi_hermes_v1_receipts_2030", "fod_finance", 2030, 116000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V1 receipts +116m (PIT +163m dominates) 2030; tick718"),
    ("bud_flexi_hermes_v2_receipts_2030", "fod_finance", 2030, 179000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V2 receipts +179m (PIT +179m) 2030; tick718"),
    ("bud_flexi_hermes_v1_er_ss_2030", "fod_finance", 2030, 77000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V1 employer SS -77m 2030; tick718"),
    ("bud_flexi_hermes_v2_er_ss_2030", "fod_finance", 2030, 48000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V2 employer SS -48m 2030; tick718"),
    ("bud_flexi_hermes_v1_ee_ss_2030", "fod_finance", 2030, 50000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V1 employee SS +50m 2030; tick718"),
    ("bud_flexi_hermes_v2_ee_ss_2030", "fod_finance", 2030, 66000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V2 employee SS +66m 2030; tick718"),
    ("bud_flexi_hermes_v2_ui_save_2030", "fod_finance", 2030, 108000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V2 UI expenditure -108m 2030 (pull from unemployed reserve); tick718"),
    ("bud_flexi_hermes_v1_ui_cost_2030", "fod_finance", 2030, 6000000, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V1 UI +6m 2030; tick718"),
    ("bud_flexi_hermes_v1_heads_2030", "fod_finance", 2030, 600, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V1 headcount employment -600 2030; tick718"),
    ("bud_flexi_hermes_v2_heads_2030", "fod_finance", 2030, 2600, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "V2 headcount +2600 2030 duration tradeoff; tick718"),
    ("bud_flexi_implicit_tax_wedge_2026", "fod_finance", 2026, 32.11, "", "", "projected", "src_ccrek_flexijob_2026_34", "strong", "HERMES implicit ee SS 10.13 + PIT 23.15 = 32.11pct on regular wages 2026 Kader6; tick718"),
    ("bud_dual_flexi_vl_share_2024", "gg_belgium", 2024, 157525, "", "", "outturn", "src_dual_flexi_vl_tick718", "strong", "Dual: ~85pct flexi in VL vs WAL/BRU residual; not TE-additive; tick718"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_flexi_coa_2026_34_volume",
        "Flexi-jobs volume path 2016-2024 CoA ONSS dual residual",
        "onss",
        "Flexi workers employers horeca retail",
        "Programme law 22 Dec 2023 art.192 CoA+BFP 2026_34",
        "2015-12-01",
        2016,
        2024,
        220071000,
        '{"workers_q4_2024":184360,"hours_q4_2024":13995721,"wage_mass_q4_m":220.071,"vte_q4":29500,"share_total_vte_pct":"<1","vl_share_pct":85,"age65_pct":18,"hourly_m":16.38,"hourly_f":15.0}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "Flexible peak labour + formalise black work",
        "Publish open ONSS series; dual regional incidence",
        "src_ccrek_flexijob_2026_34",
        "strong",
        "Federal>ONSS>flexi_volume",
        "tick718 residual vs tick407",
    ),
    (
        "cmt_flexi_hermes_abolish_horeca_2030",
        "HERMES abolish horeca flexi from 2026 fiscal path to 2030",
        "fod_finance",
        "Federal budget SS PIT horeca employers workers",
        "CoA+BFP HERMES ch4.2.3 Tables 8-9",
        "2026-01-01",
        2026,
        2030,
        213000000,
        '{"exante_vte":10836,"exante_wage_flexi_m":-294,"exante_wage_reg_m":386,"exante_net_wage_m":92,"v1_balance_m":106,"v2_balance_m":213,"v1_gdp_pct":-0.01,"v2_gdp_pct":-0.02,"v1_labour_pct":-0.02,"v2_labour_pct":-0.08,"scope":"horeca_only_not_all_sectors"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "Counterfactual fiscal cost of flexi tax privilege horeca",
        "Policy choice: keep vs reform; full-sector FOI residual",
        "src_ccrek_flexijob_2026_34",
        "strong",
        "Federal>flexi>HERMES",
        "tick718",
    ),
    (
        "cmt_flexi_enforcement_gap_2024",
        "Flexi enforcement Dimona anomalies + thin RSZ regularisation",
        "onss",
        "Flexi employers workers",
        "CoA 2026_34 T4-T5 + event sector note",
        "2024-01-01",
        2022,
        2024,
        0,
        '{"dimona_incomplete_q4_2024":4628,"improper_cumul_q4":512,"investigations_2024":270,"findings_2024":154,"regularised_high_ss":5,"event_controls_2022_24":1}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "Detect misuse and protect SS base",
        "Publish offence typology; event-sector control plan FOI",
        "src_ccrek_flexijob_2026_34",
        "strong",
        "Federal>ONSS>flexi_enforcement",
        "tick718",
    ),
    (
        "cmt_dual_flexi_vl_concentration",
        "Dual flexi concentration VL 85pct vs WAL BRU residual",
        "gg_belgium",
        "Regional labour markets horeca retail",
        "CoA 2026_34 s2.5-2.6 Graph8",
        "2016-01-01",
        2016,
        2024,
        220071000,
        '{"vl_share_pct":85,"class_vl":157525,"class_wal":21118,"class_bru":5023,"note":"not TE-additive"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "Map dual regional flexi incidence",
        "Region-level wage mass and SS FOI",
        "src_dual_flexi_vl_tick718",
        "strong",
        "Belgium>dual>flexi",
        "tick718",
    ),
    (
        "cmt_flexi_tax_privilege_implicit",
        "Flexi tax privilege vs regular wedge 32.11pct dual residual",
        "fod_finance",
        "Flexi workers employers federal budget",
        "CoA Kader6 HERMES implicit rates 2026",
        "2024-01-01",
        2024,
        2026,
        220071000,
        '{"flexi_ee_ss":0,"flexi_pit":0,"regular_ee_ss_pct":10.13,"regular_pit_pct":23.15,"wedge_pct":32.11,"employer_flexi_ss_pct":28,"q4_wage_mass_m":220.071}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "Price flexible peak labour with reduced wedge",
        "Score as tax expenditure class; dual FPS inventory link",
        "src_ccrek_flexijob_2026_34",
        "strong",
        "Federal>taxex>flexi",
        "tick718",
    ),
    (
        "cmt_flexi_event_sector_control_fail",
        "Event-sector flexi statutory review without controls dual",
        "onss",
        "Event organisers flexi workers",
        "Programme law Dec 2023 + CoA s3.4",
        "2024-01-01",
        2022,
        2024,
        0,
        '{"event_controls":1,"coa":"definition_too_vague_for_targeted_control","observation_period":"too_short"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "Prevent misuse in event sector",
        "Define event function list + control plan FOI",
        "src_ccrek_flexijob_2026_34",
        "strong",
        "Federal>flexi>events",
        "tick718",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_flexi_tax_privilege_220m_q4",
        "Flexi wage mass 220m Q4 under zero PIT/ee-SS privilege",
        "federal",
        "tax_expenditure",
        "Federal>SS>flexi_privilege",
        220071000,
        220071000,
        "Strong CoA: Q4 2024 wage mass 220.071m; workers pay no PIT/ee SS; employer fixed rate; dual VL 85pct",
        "strong",
        "src_ccrek_flexijob_2026_34",
        "Flexi workers employers",
        "Flexible peak labour cheaper formal alternative",
        "Tax privilege on growing mass; full-year TCO residual",
        7.5,
        7.5,
        4,
        7.25,
        "Publish annual TE estimate; link FPS inventory",
        "seed",
        "",
        "tick718",
    ),
    (
        "lb_flexi_hermes_v2_balance_213m",
        "Abolish horeca flexi HERMES V2 +213m budget 2030",
        "federal",
        "tax_expenditure",
        "Federal>flexi>HERMES_V2",
        213000000,
        213000000,
        "Strong CoA T9: V2 supply-gone +213m balance (0.03pp GDP); V1 +106m; horeca-only counterfactual",
        "strong",
        "src_ccrek_flexijob_2026_34",
        "Federal budget SS",
        "Counterfactual fiscal cost of horeca flexi privilege",
        "Macro effects small vs GDP but absolute mEUR material; not pure waste",
        7.0,
        7.5,
        5,
        6.95,
        "Use as reform upper bound; full-sector FOI",
        "seed",
        "",
        "tick718",
    ),
    (
        "lb_flexi_enforcement_thin_5of154",
        "RSZ flexi findings 154 but only 5 high-SS regularisations 2024",
        "federal",
        "ops",
        "Federal>ONSS>flexi_enforcement",
        154,
        270,
        "Strong CoA T5: 270 investigations 154 findings; only 5 high SS regularisations; event sector 1 control 2022-24",
        "strong",
        "src_ccrek_flexijob_2026_34",
        "SS base taxpayers",
        "Detect and sanction misuse",
        "Enforcement scale lags expansion 2024",
        7.5,
        6.0,
        4,
        6.75,
        "Publish offence typology + event control plan",
        "seed",
        "",
        "tick718",
    ),
    (
        "lb_flexi_dimona_anomaly_2_5pct",
        "Dimona incomplete flexi 2.51pct Q4 2024 dual residual",
        "federal",
        "ops",
        "Federal>ONSS>flexi_dimona",
        4628,
        184360,
        "Strong CoA T4: 4628 incomplete Dimona + 512 improper cumul on 184360 places Q4 2024",
        "strong",
        "src_ccrek_flexijob_2026_34",
        "SS inspectors employers",
        "Data integrity of flexi status",
        "Automated flags exist but residual non-compliance",
        6.5,
        5.5,
        3,
        6.15,
        "Auto-block non-compliant Dimona before pay",
        "seed",
        "",
        "tick718",
    ),
    (
        "lb_flexi_vl_concentration_85pct",
        "85pct flexi jobs in Flanders dual residual",
        "Belgium",
        "ops",
        "Belgium>dual>flexi_VL",
        157525,
        184360,
        "Strong CoA: ~85pct flexi in VL; Graph8 class VL 157k WAL 21k BRU 5k; dual labour incidence",
        "strong",
        "src_dual_flexi_vl_tick718",
        "Regional labour markets",
        "Flexible peak labour access dual",
        "Federal privilege with highly asymmetric regional uptake",
        6.5,
        7.0,
        5,
        6.45,
        "Publish regional wage-mass and SS maps",
        "seed",
        "",
        "tick718",
    ),
    (
        "lb_flexi_under_1pct_vte_scale",
        "Flexi still under 1pct of employee VTE despite growth",
        "federal",
        "ops",
        "Federal>flexi>scale",
        29500,
        3400000,
        "Strong CoA: 29.5k flexi VTE vs 3.4m employee VTE Q4 2024; growth huge from 2016 but still small share",
        "strong",
        "src_ccrek_flexijob_2026_34",
        "Labour market",
        "Peak labour flexibility",
        "Scale bounds waste claims; focus privilege rate not mass",
        4.0,
        5.0,
        3,
        4.5,
        "Keep scale context in waste ranking",
        "seed",
        "",
        "tick718",
    ),
    (
        "lb_flexi_event_control_void",
        "Statutory event-sector flexi review without RSZ targeting",
        "federal",
        "ops",
        "Federal>flexi>events_void",
        1,
        0,
        "Strong CoA: law requires event misuse focus; RSZ only 1 control 2022-24; definition too vague",
        "strong",
        "src_ccrek_flexijob_2026_34",
        "Event workers SS",
        "Prevent event-sector misuse",
        "Legislative mandate without operational control",
        7.0,
        5.5,
        3,
        6.35,
        "Define event functions + targeted campaign FOI",
        "seed",
        "",
        "tick718",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_ccrek_flexijob_2026_34",
        "CoA+BFP Analyse flexi-jobs 2026_34 art.192 residual HERMES dual",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "Rekenhof / Cour des comptes + Federaal Planbureau",
        "2026-08-01",
        "audit",
        "Strong primary Jan 2026 report ch2-4 HERMES T8-9 residual tick718",
    ),
    (
        "src_dual_flexi_vl_tick718",
        "Dual flexi VL 85pct concentration residual vs WAL BRU",
        "https://www.ccrek.be/sites/default/files/Docs/2026_34_FlexiJob.pdf",
        "DOGE synthesis CoA dual",
        "2026-08-01",
        "synthesis",
        "Strong dual regional incidence tick718",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

foi = (
    "gap_flexi_hermes_full_sector_l5",
    "Federal>SS>flexi_HERMES_full_sector",
    "fod_finance",
    "Full-sector HERMES/FPS annual tax-expenditure estimate of flexi privilege beyond horeca-only counterfactual; Q1-Q4 wage mass series 2022-2025 by region and PC; RSZ offence typology for 154 findings 2024; event-sector function list and control plan; dual VL/WAL/BRU SS incidence",
    "Horeca-only HERMES V2 +213m is lower bound; 85pct VL concentration; enforcement thin; TE inventory residual",
    "6",
    "FPS Finance / ONSS / NAR greffe",
    "",
    "",
    "docs/doge/foi/drafts/gap_flexi_hermes_full_sector_l5.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_flexi_hermes_abolish_horeca_2030",
    "lb_flexi_hermes_v2_balance_213m",
    "2026-08-01T21:15:00Z",
    "2026-08-01T21:15:00Z",
    "tick718 CoA 2026_34 residual; not sent; recipient contacts TBD",
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
        if row and row[0] == "rq_709":
            row[4] = "done"
            row[10] = "2026-08-01T21:15:00Z"
            row[11] = "tick718 flexi CoA 2026_34 HERMES V2 +213m wage mass 220m dual VL85; FOI gap_flexi_hermes_full_sector_l5 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_710" not in ids:
    rows.append(
        [
            "rq_710",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: WAL Sofico/OTW/UAP L5 preferred or fed VVPR/Pillar2 recheck or VL kunst residual L5 names",
            "",
            "2026-08-01T21:15:00Z",
            "",
            "spawned tick718 after rq_709",
        ]
    )
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T21:15:00Z,rq_709,718,no,tick718 flexi HERMES residual dual VL; next rq_710; progress@720 in 2; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

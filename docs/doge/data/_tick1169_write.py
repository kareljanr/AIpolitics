# tick1169: AGB Genk JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_genk_jr2025"
ENT = "agb_genk"
TICK = "tick1169"
UTC = "2026-08-08T02:00:00Z"
GAP = "gap_agb_genk_gecorr_afm_neg_bbr_neg_leasing_11m_treasury_l5"
URL = "https://www.genk.be/jaarrekening-2025"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Genk Jaarrekening BBC 2025 (276p) RVB 21.04.2026 pub 28.04.2026",
            URL,
            "AGB Genk / Stad Genk",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0872.093.742; assets 88.974m fin debt 12.897m "
            "leasing MVA 11.191m gecorr AFM -0.419m BBR -1.452m treasury 1.75m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Genk",
            "AGB Genk",
            "AGB Genk",
            "local_entity",
            "city_genk",
            "nl",
            URL,
            "openbaarheid@genk.be",
            "Stadsplein 1 3600 Genk",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0872.093.742; assets 88.974m equity/netto 73.740m (cum P&L -2.705m) "
            "cash 0.235m fin debt 12.897m (LT 10.903 + ST due 0.244 + treasury 1.750) "
            "leasing MVA 11.191m FVA ThorPark/T2 15.075m BBR -1.452m AFM +0.335m "
            "gecorr AFM -0.419m NEG city werkingsub 0.861m investsub 4.626m; "
            "Wnd AD Stijn Ooms FD Rudi Van Gurp; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbgenk_assets_2025", 88973961, "Assets balanstotaal YE2025 88.974m"),
    ("bud_agbgenk_equity_2025", 73740132, "Nettoactief YE2025 73.740m"),
    ("bud_agbgenk_cum_pnl_2025", -2704627, "Gecumuleerd tekort YE2025 -2.705m"),
    ("bud_agbgenk_cap_subs_2025", 40362725, "Kapitaalssubsidies YE2025 40.363m"),
    ("bud_agbgenk_other_netto_2025", 36082034, "Overig nettoactief YE2025 36.082m"),
    ("bud_agbgenk_debt_total_2025", 15233829, "Schulden total YE2025 15.234m"),
    ("bud_agbgenk_fin_debt_2025", 12896770, "Fin schulden T4 total YE2025 12.897m"),
    ("bud_agbgenk_fin_debt_lt_2025", 10902645, "Fin schulden LT YE2025 10.903m"),
    ("bud_agbgenk_fin_debt_st_due_2025", 244125, "Fin schulden LT vervallend YE2025 0.244m"),
    ("bud_agbgenk_treasury_st_2025", 1750000, "Thesauriebewijzen ST YE2025 1.750m JUMP from 1.0m"),
    ("bud_agbgenk_cash_2025", 235276, "Liquide middelen YE2025 0.235m"),
    ("bud_agbgenk_mva_2025", 71214982, "MVA YE2025 71.215m"),
    ("bud_agbgenk_mva_buildings_2025", 56226841, "MVA terreinen/gebouwen bedrijfsmatig YE2025 56.227m"),
    ("bud_agbgenk_leasing_mva_2025", 11191175, "Leasing MVA YE2025 11.191m MASSIVE"),
    ("bud_agbgenk_fva_2025", 15074814, "FVA YE2025 15.075m (Thor Park 13.955 + T2 CV 1.120)"),
    ("bud_agbgenk_st_recv_2025", 2269538, "ST vorderingen YE2025 2.270m"),
    ("bud_agbgenk_expl_rec_2025", 5778030, "Exploitatieontvangsten 5.778m"),
    ("bud_agbgenk_expl_exp_2025", 5206274, "Exploitatieuitgaven 5.206m"),
    ("bud_agbgenk_expl_saldo_2025", 571755, "Exploitatiesaldo +0.572m"),
    ("bud_agbgenk_werkingssub_city_2025", 860952, "Algemene werkingssubsidie gemeente 0.861m DROP from 1.150m"),
    ("bud_agbgenk_werkingssub_total_2025", 891532, "Werkingssubsidies total T2 0.892m"),
    ("bud_agbgenk_invest_exp_2025", 6059606, "Investeringsuitgaven 6.060m (SportinGenk 5.254m)"),
    ("bud_agbgenk_invest_rec_2025", 5401220, "Investeringsontvangsten 5.401m"),
    ("bud_agbgenk_invest_sub_city_2025", 4626169, "Investeringssubsidies van gemeente 4.626m"),
    ("bud_agbgenk_invest_saldo_2025", -658386, "Investeringssaldo -0.658m"),
    ("bud_agbgenk_fin_exp_2025", 237055, "Financieringsuitgaven/aflossingen 0.237m"),
    ("bud_agbgenk_fin_rec_2025", 0, "Financieringsontvangsten/new loans 0"),
    ("bud_agbgenk_fin_saldo_2025", -237055, "Financieringssaldo -0.237m"),
    ("bud_agbgenk_budget_result_2025", -323685, "Budgettair resultaat boekjaar -0.324m"),
    ("bud_agbgenk_bbr_2025", -1451970, "Beschikbaar BBR YE2025 -1.452m NEG (treasury booking)"),
    ("bud_agbgenk_afm_2025", 334701, "AFM +0.335m"),
    ("bud_agbgenk_afm_gecorr_2025", -418951, "Gecorr AFM -0.419m NEG CRITICAL (aangewezen 0.991m)"),
    ("bud_agbgenk_aangewezen_amort_2025", 990706, "Gecorrigeerde aflossingen o.b.v. fin schulden 0.991m"),
    ("bud_agbgenk_pnl_2025", 256175, "P&L +0.256m (carryforward; no dividend)"),
    ("bud_agbgenk_interest_2025", 424852, "Financiele kosten 0.425m"),
    ("bud_agbgenk_depr_2025", 2167969, "Afschrijvingen 2.168m"),
    ("bud_agbgenk_sportingenk_invest_2025", 5254381, "SportinGenk investeringswerken 5.254m"),
    ("bud_agbgenk_thor_invest_2025", 470377, "Thor Park werkzaamheden 0.470m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbgenk_gecorr_afm_neg_0_42m_2025",
        "AGB Genk gecorr AFM -0.42m NEG",
        "Indicated amort 0.991m >> contractual 0.237m; healthy AFM masks NEG gecorr",
        418951,
    ),
    (
        "comm_agbgenk_bbr_neg_1_45m_2025",
        "AGB Genk beschikbaar BBR -1.45m NEG",
        "Treasury certificates not booked as budget receipt; BBC 2015 ABB rule",
        1451970,
    ),
    (
        "comm_agbgenk_leasing_mva_11_2m_2025",
        "AGB Genk leasing MVA 11.2m",
        "City-AGB onroerende leasing stock on balance",
        11191175,
    ),
    (
        "comm_agbgenk_fin_debt_12_9m_2025",
        "AGB Genk fin debt 12.9m + treasury 1.75m",
        "LT bank+lease 10.9m + ST due 0.24m + thesaurie 1.75m",
        12896770,
    ),
    (
        "comm_agbgenk_city_invest_sub_4_63m_2025",
        "AGB Genk city invest subsidy 4.63m 2025",
        "Investeringssubsidies van gemeente dual residual",
        4626169,
    ),
    (
        "comm_agbgenk_fva_thor_t2_15_1m_2025",
        "AGB Genk FVA Thor Park + T2 15.1m",
        "Participaties Thor Park NV 13.955m + T2 CV 1.120m",
        15074814,
    ),
]
with open(ROOT / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for cid, title, goal, env in cmts:
        w.writerow(
            [
                cid,
                title,
                ENT,
                "AGB dual residual",
                "BBC JR2025",
                "2026-04-21",
                2025,
                2025,
                env,
                f"{{2025:{env}}}",
                0,
                "active",
                URL,
                goal,
                "Entity II FOI residual",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Genk>AGB",
                TICK,
            ]
        )

lbs = [
    (
        "lb_agbgenk_assets_89m_2025",
        "AGB Genk assets 89m Entity II",
        88973961,
        5.5,
        8.0,
        3.0,
        "Map residual",
    ),
    (
        "lb_agbgenk_gecorr_afm_neg_0_42m_2025",
        "AGB Genk gecorr AFM -0.42m NEG",
        418951,
        8.5,
        5.0,
        3.0,
        "AFM path FOI residual",
    ),
    (
        "lb_agbgenk_bbr_neg_1_45m_2025",
        "AGB Genk BBR -1.45m NEG treasury",
        1451970,
        8.0,
        6.0,
        3.0,
        "Treasury FOI residual",
    ),
    (
        "lb_agbgenk_leasing_11_2m_2025",
        "AGB Genk leasing MVA 11.2m",
        11191175,
        7.5,
        7.5,
        3.0,
        "Lease FOI residual",
    ),
    (
        "lb_agbgenk_fin_debt_12_9m_2025",
        "AGB Genk fin debt 12.9m",
        12896770,
        7.0,
        7.5,
        3.0,
        "Debt FOI residual",
    ),
    (
        "lb_agbgenk_city_invest_sub_4_63m_2025",
        "AGB Genk city invest sub 4.63m",
        4626169,
        7.0,
        6.5,
        3.0,
        "Dual city path FOI",
    ),
    (
        "lb_agbgenk_fva_15_1m_2025",
        "AGB Genk FVA Thor/T2 15.1m",
        15074814,
        6.5,
        7.5,
        3.0,
        "Participatie FOI residual",
    ),
    (
        "lb_agbgenk_sportingenk_invest_5_25m_2025",
        "AGB Genk SportinGenk invest 5.25m",
        5254381,
        6.5,
        6.5,
        3.0,
        "Project FOI residual",
    ),
]
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for lid, name, cost, abs_s, cost_s, diff, cut in lbs:
        prio = round((abs_s * cost_s * (10 - diff)) / 10.0, 1)
        w.writerow(
            [
                lid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Genk>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC leasing FVA treasury",
                "strong",
                SRC,
                "Genk residents / SportinGenk users",
                "Local dual residual map VL JR2025 AGB Genk",
                "BBC J2/J4/J5/T2/T4 primary",
                abs_s,
                cost_s,
                diff,
                prio,
                cut,
                "active",
                "",
                TICK,
            ]
        )

with open(ROOT / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            GAP,
            "Vlaanderen>Gemeenten>Genk>AGB>gecorr_afm_bbr_leasing_treasury_L5",
            ENT,
            "Gecorr AFM -0.419m multi-year path vs indicated amort 0.991m; BBR -1.452m treasury "
            "certificate programme schedule and BBC booking recon; leasing 11.191m city-AGB contracts; "
            "fin debt 12.897m lender schedule (ING 1m / KBC 5m / lease); city werkingsub 0.861m + "
            "investsub 4.626m multi-year; SportinGenk 5.254m project list; Thor Park / T2 FVA governance; "
            "interest 0.425m split city lease vs banks",
            "Entity II 89m book dual after city GE: NEG gecorr AFM and NEG BBR via treasury, "
            "massive leasing+FVA shell for sport/park investments",
            9,
            "Stad / AGB Genk openbaarheid",
            "openbaarheid@genk.be",
            "Stadsplein 1 3600 Genk",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbgenk_gecorr_afm_neg_0_42m_2025|comm_agbgenk_bbr_neg_1_45m_2025",
            "lb_agbgenk_gecorr_afm_neg_0_42m_2025|lb_agbgenk_bbr_neg_1_45m_2025|lb_agbgenk_leasing_11_2m_2025",
            UTC,
            UTC,
            TICK + "; ready not sent; do not send without human OK",
        ]
    )

# research_queue: mark 1169 done, spawn 1170
rows = []
with open(ROOT / "research_queue.csv", "r", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_1169":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1169 AGB Genk JR2025 Entity II dual residual; gecorr AFM NEG BBR NEG "
                "leasing 11.2m treasury 1.75m; FOI " + GAP
            )
        rows.append(row)
rows.append(
    {
        "task_id": "rq_1170",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "Vlaanderen>Gemeenten>residual_dual_L5",
        "entity_id": "",
        "instructions": "Residual dual L5 VL JR2025 (GE/OCMW + AGB). Prefer unmined AGB after city GE. Primary BBC only.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned by tick1169; next residual dual L5 after AGB Genk",
    }
)
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1169 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

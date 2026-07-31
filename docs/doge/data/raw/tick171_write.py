# -*- coding: utf-8 -*-
"""Tick 171: Sibelga Brussels DSO 2024 financials + Fluvius EG deepen L5."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T07:05:00Z"
TICK = 171
UNIT = "rq_166"


def append_lines(path: Path, lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def replace_line_startswith(path: Path, prefix: str, new_line: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    found = False
    for line in lines:
        if line.startswith(prefix):
            out.append(new_line if new_line.endswith("\n") else new_line + "\n")
            found = True
        else:
            out.append(line)
    if not found:
        raise SystemExit(f"prefix not found: {prefix}")
    path.write_text("".join(out), encoding="utf-8", newline="\n")


append_lines(
    DATA / "sources.csv",
    [
        "src_sibelga_fin_2024,Sibelga Board report and annual accounts 2024 EN,"
        "https://2024.sibelga.be/wp-content/uploads/2025/06/SIBELGA-RAPPORT-FINANCIER-2024-EN.pdf,"
        "Sibelga,2026-07-28,official_annual_report,"
        '"Turnover 415.4m op profit 74.7m profit 49.1m distributed 49.1m; assets 1.511bn equity 861m; '
        'tariff total income proposal 347.5m fair margin 47.9m; RAB init 1.198bn end-2018; tick171"',
        "src_fluvius_investor_2025_deep,Fluvius EG investor update 2025 deepen L5,"
        "https://over.fluvius.be/sites/fluvius/files/2026-03/update-investors-annual-report-2025.pdf,"
        "Fluvius,2026-07-28,official_investor,"
        '"WACC 5.2pct 2025 (3.5 2024); network tariff rev 2931m; GEC/CHP cost +149m; staff +23m; '
        'dividend policy 60pct ELED/GASD; EQ/RAB 33pct; employees 5997; tick171"',
    ],
)

append_lines(
    DATA / "entities.csv",
    [
        "sibelga,Sibelga,Sibelga,Brussels electricity and gas DSO intercommunale,"
        "intercommunale,brussels_gov,bi,https://www.sibelga.be,,"
        "Brussels,"
        "BCR DSO 100pct public; turnover 415m profit 49m 2024; dual Fluvius Flanders + Elia TSO; tick171",
    ],
)

append_lines(
    DATA / "budgets.csv",
    [
        # Sibelga
        "bud_sibelga_turnover_2024,sibelga,2024,415398290,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga turnover 415.398m 2024",
        "bud_sibelga_turnover_2023,sibelga,2023,379624511,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga turnover 379.625m 2023",
        "bud_sibelga_op_income_2024,sibelga,2024,441189629,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga operating income 441.190m 2024",
        "bud_sibelga_op_profit_2024,sibelga,2024,74749119,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga operating profit 74.749m 2024",
        "bud_sibelga_op_profit_2023,sibelga,2023,77639256,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga operating profit 77.639m 2023",
        "bud_sibelga_profit_2024,sibelga,2024,49067501,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga profit for period 49.068m 2024",
        "bud_sibelga_profit_2023,sibelga,2023,52565320,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga profit for period 52.565m 2023",
        "bud_sibelga_dividend_2024,sibelga,2024,49124845,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga profit distributed remuneration of contribution 49.125m 2024 (to municipalities)",
        "bud_sibelga_dividend_2023,sibelga,2023,52027706,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga distributed 52.028m 2023",
        "bud_sibelga_assets_2024,sibelga,2024,1511461285,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga total assets 1.511bn EOY 2024",
        "bud_sibelga_equity_2024,sibelga,2024,861150642,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga equity 861.151m EOY 2024",
        "bud_sibelga_tangible_fa_2024,sibelga,2024,1326437624,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga tangible fixed assets 1.326bn EOY 2024",
        "bud_sibelga_fin_debt_lt_2024,sibelga,2024,357016855,,,outturn,src_sibelga_fin_2024,strong,"
        "Sibelga LT financial debts 357.017m EOY 2024",
        "bud_sibelga_tariff_income_2024,sibelga,2024,347500000,,,budgeted,src_sibelga_fin_2024,strong,"
        "Tariff proposal total income electricity+gas 347.5m 2024",
        "bud_sibelga_fair_margin_2024,sibelga,2024,47900000,,,budgeted,src_sibelga_fin_2024,strong,"
        "Fair margin tariff proposal 47.9m 2024",
        "bud_sibelga_manageable_costs_2024,sibelga,2024,131400000,,,budgeted,src_sibelga_fin_2024,strong,"
        "Manageable costs tariff proposal 131.4m 2024 before index recalculation",
        "bud_sibelga_nonmanageable_costs_2024,sibelga,2024,216100000,,,budgeted,src_sibelga_fin_2024,strong,"
        "Non-manageable costs tariff proposal 216.1m 2024",
        "bud_sibelga_rab_init_2018,sibelga,2018,1197600000,,,outturn,src_sibelga_fin_2024,strong,"
        "Initial RAB approved Brugel end-2018 1.1976bn",
        # Fluvius deepen
        "bud_fluvius_ops_result_2025,fluvius,2025,482000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Fluvius EG result from operations 482m 2025 (313m 2024)",
        "bud_fluvius_ops_result_2024,fluvius,2024,313000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Fluvius EG result from operations 313m 2024",
        "bud_fluvius_net_finance_2025,fluvius,2025,-207000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Fluvius EG net finance costs -207m 2025",
        "bud_fluvius_network_tariff_rev_2025,fluvius,2025,2931000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Distribution+transmission network tariff revenue 2.931bn 2025 (2.222bn 2024)",
        "bud_fluvius_network_tariff_rev_2024,fluvius,2024,2222000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Network tariff revenue 2.222bn 2024",
        "bud_fluvius_gec_chp_cost_delta_2025,fluvius,2025,149000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "GEC+CHP certificate purchase cost increase +149m y/y 2025 (exogenous)",
        "bud_fluvius_staff_delta_2025,fluvius,2025,23000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Staff costs +23m y/y 2025",
        "bud_fluvius_employees_2025,fluvius,2025,5997,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Employees headcount 5997 EOY 2025 (5863 2024)",
        "bud_fluvius_eq_rab_2025,fluvius,2025,33,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "EQ/RAB ELED+GASD 33pct 2025 (35pct 2024); target 40pct",
        "bud_fluvius_wacc_2025,fluvius,2025,5.2,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Allowed WACC 5.2pct 2025-28 tariff period (was 3.5pct 2024)",
        "bud_fluvius_dividend_payout_policy,fluvius,2025,60,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Dividend policy 60pct expected profit ELED/GASD 2025-28 (avg payout est 66pct)",
        "bud_fluvius_assets_total_2025,fluvius,2025,19799000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Fluvius EG balance sheet total 19.799bn EOY 2025",
        "bud_fluvius_noncurrent_assets_2025,fluvius,2025,18055000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Non-current assets 18.055bn EOY 2025",
        "bud_fluvius_ops_cashflow_2025,fluvius,2025,1019000000,,,outturn,src_fluvius_investor_2025_deep,strong,"
        "Net cash flow from operating activities 1.019bn 2025",
    ],
)

append_lines(
    DATA / "commitments.csv",
    [
        'cmt_sibelga_dso_2023_24,Sibelga Brussels DSO regulated outturn multi-year,sibelga,'
        "BCR electricity gas consumers municipalities,Brugel tariff methodology 2020-24 / 2025-29,"
        "2023-01-01,2023,2024,415398290,"
        '"{""2024_turnover"":415398290,""2023_turnover"":379624511,""2024_op_profit"":74749119,'
        '""2024_profit"":49067501,""2024_dividend"":49124845,""2024_assets"":1511461285,'
        '""2024_equity"":861150642,""2024_tariff_income"":347500000,""2024_fair_margin"":47900000,'
        '""rab_init_2018"":1197600000,""ownership"":""100pct_public_municipal"",'
        '""note"":""Dual regional DSO with Fluvius Flanders; Elia federal TSO above""}",'
        "0,active,https://2024.sibelga.be/wp-content/uploads/2025/06/SIBELGA-RAPPORT-FINANCIER-2024-EN.pdf,"
        "Operate Brussels electricity and gas distribution grids,"
        "Publish RAB path annual; municipal dividend transparency; dual VL-BCR unit costs,"
        "src_sibelga_fin_2024,strong,Bruxelles>Energie>Sibelga,"
        "tick171 dual Fluvius/Elia stack",
        'cmt_fluvius_eg_2025_deepen,Fluvius EG 2025 deepen tariff WACC GEC dividend,fluvius,'
        "Flemish DSOs municipalities consumers,VNR tariff methodology 2025-28,"
        "2025-01-01,2025,2028,4597000000,"
        '"{""ops_rev"":4597000000,""ops_result"":482000000,""ebitda"":1107000000,""result"":182000000,'
        '""capex"":1780000000,""network_tariff_rev"":2931000000,""gec_chp_cost_delta"":149000000,'
        '""wacc_pct"":5.2,""eq_rab_pct"":33,""dividend_policy_pct"":60,""employees"":5997,'
        '""equity_strengthen_vl_max"":1560000000,""assets"":19799000000,'
        '""note"":""Deepen tick150; dual Elia TSO above and Sibelga BCR DSO""}",'
        "0,active,https://over.fluvius.be/sites/fluvius/files/2026-03/update-investors-annual-report-2025.pdf,"
        "Enable Flanders energy transition distribution,"
        "Deliver EQ/RAB 40pct without over-dividend; open municipal dividend L5,"
        "src_fluvius_investor_2025_deep,strong,Vlaanderen>Fluvius,"
        "tick171 deepen",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_sibelga_dso_415m,Sibelga Brussels DSO turnover 415m profit 49m 2024,Brussels,ops,"
        "Bruxelles>Energie>Sibelga,415398290,415398290,"
        "Strong accounts: turnover 415m dividend 49m to municipalities; dual Fluvius 4.6bn EG Flanders,"
        "strong,src_sibelga_fin_2024,BCR households businesses municipalities,"
        "Electricity gas distribution BCR,"
        "Core infra monopoly; regulated fair margin; dual regional DSO stack,"
        "4,8.5,6,6.2,"
        "Publish annual RAB; dual VL-BCR unit cost benchmarks,"
        "seed,,tick171",
        "lb_grid_dual_fluvius_elia_sibelga,BE grid dual Fluvius+Elia+Sibelga stack,multi,ops,"
        "BE>Energy>grids_dual,4597000000,1667400000,"
        "Strong: Fluvius EG 4.6bn ops 1.78bn CAPEX; Elia ETB 1.67bn rev 1.47bn CAPEX; Sibelga 0.42bn turnover; triple layer,"
        "strong,src_fluvius_investor_2025_deep,All BE electricity consumers,"
        "Transmission+distribution energy transition,"
        "Core infra not waste; dual/triple institutional layers VL-BCR-federal; municipal equity claims,"
        "5,9.5,7,7.5,"
        "Open municipal dividend matrix; simplify dual DSO where efficient,"
        "seed,,tick171",
    ],
)

replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_166,",
    "rq_166,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ",2026-07-28T06:45:00Z,2026-07-28T07:05:00Z,"
    '"tick171: Sibelga 2024 turnover 415m profit 49m dividend 49m + Fluvius deepen WACC 5.2 GEC+149m dual Elia; Mons/Antwerp register still FOI; spawn rq_167"\n',
)

rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_167," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_167,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T07:05:00Z,,"
            '"Spawned tick171 after Sibelga+Fluvius deepen; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_167 hole-fill Antwerp/Mons/taxex/other; rq_116 SWA deferred. FOI ready human send. tick171 Sibelga+Fluvius."\n',
    encoding="utf-8",
    newline="\n",
)

log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **Sibelga BCR DSO 2024 + Fluvius EG deepen**)
- Found (strong primary Sibelga accounts + Fluvius investor update):
  - **Sibelga 2024:** turnover **EUR 415.4m** (379.6m 2023) · op. profit **74.7m** · profit **49.1m** · distributed to municipalities **49.1m**.
  - Assets **1.511bn** · equity **861m** · LT fin. debt **357m** · tangible FA **1.326bn**.
  - Tariff proposal: total income **347.5m** · fair margin **47.9m** · manageable **131.4m** · non-manageable **216.1m** · RAB init **1.198bn** (end-2018).
  - **Fluvius deepen:** ops result **482m** · network tariff rev **2.931bn** · GEC/CHP cost **+149m** · WACC **5.2%** · EQ/RAB **33%** · staff **5 997** · dividend policy **60%** · assets **19.8bn**.
  - Dual/triple grid stack: **Fluvius VL DSO** + **Elia federal TSO** + **Sibelga BCR DSO**.
- Mons BI2026 / Antwerp bulk register still not newly filled.
- Wrote: sources 2; entity 1; budgets 33; cmt 2; lb 2; rq_166=done; seeded **rq_167**.
- FOI: residual municipal dividend L5 + local FOIs human send.
- Next: prio5 **rq_167**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")
print("tick171 OK")

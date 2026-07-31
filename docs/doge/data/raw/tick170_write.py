# -*- coding: utf-8 -*-
"""Tick 170: Elia Transmission Belgium IAR2025 regulated TSO financials."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T06:45:00Z"
TICK = 170
UNIT = "rq_165"


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
        "src_elia_etb_iar2025,Elia Transmission Belgium Integrated Annual Report 2025 ENG,"
        "https://investor.eliagroup.eu/-/media/project/elia/shared/documents/investor-relations/reports-and-results/reports-for-elia-transmission-belgium/2026/en_2025_elia-transmission-belgium.pdf,"
        "Elia Transmission Belgium,2026-07-28,official_annual_report,"
        '"Revenue 1667.4m profit 300.7m CAPEX ~1.47bn RAB 7.8bn equity 4.43bn assets 11.68bn; '
        'settlement mech -160.9m; personnel 264m; CAPEX plan 7.5bn 2025-28; equity inject 1.057bn; tick170"'
    ],
)

# update elia entity if present
ent_path = DATA / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
if "elia,Elia Transmission Belgium" in ent:
    # refresh notes via replace if simple line exists
    pass
else:
    append_lines(
        DATA / "entities.csv",
        [
            "elia,Elia Transmission Belgium,Elia Transmission Belgium,Elia Belgian electricity TSO,"
            "parastatal,sec_federal,bi,https://www.elia.be,,"
            "Brussels,"
            "Federal HV TSO 8851km; revenue 1.67bn profit 301m 2025; RAB 7.8bn CAPEX 1.47bn; CRM host; tick170",
        ],
    )

append_lines(
    DATA / "budgets.csv",
    [
        "bud_elia_revenue_2025,elia,2025,1667400000,,,outturn,src_elia_etb_iar2025,strong,"
        "ETB consolidated revenue 1.6674bn 2025",
        "bud_elia_revenue_2024,elia,2024,1257700000,,,outturn,src_elia_etb_iar2025,strong,"
        "ETB consolidated revenue 1.2577bn 2024",
        "bud_elia_settlement_mech_2025,elia,2025,-160900000,,,outturn,src_elia_etb_iar2025,strong,"
        "Net income/expense from settlement mechanism -160.9m 2025 (was +247.8m 2024)",
        "bud_elia_settlement_mech_2024,elia,2024,247800000,,,outturn,src_elia_etb_iar2025,strong,"
        "Settlement mechanism net +247.8m 2024",
        "bud_elia_services_goods_2025,elia,2025,646000000,,,outturn,src_elia_etb_iar2025,strong,"
        "Services and other goods 646.0m 2025 (831.9m 2024)",
        "bud_elia_personnel_2025,elia,2025,264000000,,,outturn,src_elia_etb_iar2025,strong,"
        "Personnel expenses 264.0m 2025 (225.8m 2024)",
        "bud_elia_personnel_2024,elia,2024,225800000,,,outturn,src_elia_etb_iar2025,strong,"
        "Personnel expenses 225.8m 2024",
        "bud_elia_da_2025,elia,2025,266900000,,,outturn,src_elia_etb_iar2025,strong,"
        "Depreciation amortisation impairment 266.9m 2025",
        "bud_elia_ebit_2025,elia,2025,448700000,,,outturn,src_elia_etb_iar2025,strong,"
        "EBIT 448.7m 2025 (385.8m 2024)",
        "bud_elia_ebit_2024,elia,2024,385800000,,,outturn,src_elia_etb_iar2025,strong,"
        "EBIT 385.8m 2024",
        "bud_elia_profit_2025,elia,2025,300700000,,,outturn,src_elia_etb_iar2025,strong,"
        "Net profit 300.7m 2025 (245.0m 2024)",
        "bud_elia_profit_2024,elia,2024,245000000,,,outturn,src_elia_etb_iar2025,strong,"
        "Net profit 245.0m 2024",
        "bud_elia_capex_2025,elia,2025,1469500000,,,outturn,src_elia_etb_iar2025,strong,"
        "Total CAPEX/investments class 1.4695bn 2025 (taxonomy table; key figures 1.4bn)",
        "bud_elia_rab_2025,elia,2025,7800000000,,,outturn,src_elia_etb_iar2025,strong,"
        "Regulated Asset Base RAB 7.8bn 2025",
        "bud_elia_total_assets_2025,elia,2025,11683000000,,,outturn,src_elia_etb_iar2025,strong,"
        "Total assets 11.683bn EOY 2025",
        "bud_elia_total_assets_2024,elia,2024,9704200000,,,outturn,src_elia_etb_iar2025,strong,"
        "Total assets 9.704bn EOY 2024",
        "bud_elia_equity_2025,elia,2025,4430200000,,,outturn,src_elia_etb_iar2025,strong,"
        "Equity 4.430bn EOY 2025 (3.179bn 2024)",
        "bud_elia_equity_2024,elia,2024,3179100000,,,outturn,src_elia_etb_iar2025,strong,"
        "Equity 3.179bn EOY 2024",
        "bud_elia_equity_inject_2025,elia,2025,1057000000,,,outturn,src_elia_etb_iar2025,strong,"
        "Shares issued equity injection ~1.057bn 2025 from Elia Group capital raise",
        "bud_elia_loans_lt_2025,elia,2025,4864400000,,,outturn,src_elia_etb_iar2025,strong,"
        "Non-current loans and borrowings 4.864bn EOY 2025",
        "bud_elia_loans_st_2025,elia,2025,628100000,,,outturn,src_elia_etb_iar2025,strong,"
        "Current loans and borrowings 628.1m EOY 2025",
        "bud_elia_cash_2025,elia,2025,1503900000,,,outturn,src_elia_etb_iar2025,strong,"
        "Cash and cash equivalents 1.504bn EOY 2025",
        "bud_elia_ppe_2025,elia,2025,7139000000,,,outturn,src_elia_etb_iar2025,strong,"
        "Property plant equipment 7.139bn EOY 2025",
        "bud_elia_dividends_2025,elia,2025,99700000,,,outturn,src_elia_etb_iar2025,strong,"
        "Dividends paid 99.7m 2025 (40.8m 2024)",
        "bud_elia_capex_plan_2025_28,elia,2025,7500000000,,,commitment,src_elia_etb_iar2025,strong,"
        "CAPEX plan 2025-2028 EUR 7.5bn",
        "bud_elia_invest_plan_2026,elia,2026,1700000000,,,budgeted,src_elia_etb_iar2025,strong,"
        "Planned investment 1.7bn in 2026 (management interview)",
        "bud_elia_baekeland_invest,elia,2026,400000000,,,commitment,src_elia_etb_iar2025,medium,"
        "Baekeland 380/150kV substation Ghent port investment 400m class",
        "bud_elia_green_bond_2025,elia,2025,500000000,,,outturn,src_elia_etb_iar2025,strong,"
        "EU Green Bond placement 500m 2025",
    ],
)

append_lines(
    DATA / "commitments.csv",
    [
        'cmt_elia_etb_results_2024_25,Elia Transmission Belgium regulated TSO outturn multi-year,elia,'
        "Electricity consumers Belgium grid users,CREG tariff methodology + federal TSO mandate,"
        "2024-01-01,2024,2028,7500000000,"
        '"{""2025_revenue"":1667400000,""2024_revenue"":1257700000,""2025_profit"":300700000,""2024_profit"":245000000,'
        '""2025_ebit"":448700000,""2025_personnel"":264000000,""2025_settlement"":-160900000,""2024_settlement"":247800000,'
        '""2025_capex"":1469500000,""2025_rab"":7800000000,""2025_equity"":4430200000,""2025_assets"":11683000000,'
        '""2025_equity_inject"":1057000000,""2025_dividends"":99700000,""capex_plan_2025_28"":7500000000,'
        '""invest_plan_2026"":1700000000,""grid_km"":8851,""reliability_pct"":99.99,'
        '""projects"":""Princess Elisabeth Island Ventilus Boucle du Hainaut Brabo Baekeland"",'
        '""note"":""Regulated monopoly TSO; tariffs recover allowed return on RAB; hosts CRM and federal GC OSP cash""}",'
        "0,active,https://investor.eliagroup.eu/-/media/project/elia/shared/documents/investor-relations/reports-and-results/reports-for-elia-transmission-belgium/2026/en_2025_elia-transmission-belgium.pdf,"
        "Operate Belgian HV electricity transmission grid,"
        "Track CAPEX delivery vs plan; tariff methodology 2028-31; MOG II cost control,"
        "src_elia_etb_iar2025,strong,Federal>Energy>Elia_TSO,"
        "tick170; dual with Fluvius DSO and CRM/GC OSP",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_elia_etb_capex_1_5bn,Elia ETB CAPEX ~1.47bn 2025 plan 7.5bn 2025-28,federal,ops,"
        "Federal>Energy>Elia>CAPEX,1469500000,7500000000,"
        "IAR strong: CAPEX 1.47bn 2025 RAB 7.8bn; plan 7.5bn 4y; 2026 invest 1.7bn; dual Fluvius DSO,"
        "strong,src_elia_etb_iar2025,Electricity consumers Belgium,"
        "HV grid energy transition investment,"
        "Core infra not pure waste; regulated return; MOG II cost risk; congestion bottleneck,"
        "4,9.5,7,7.2,"
        "Publish project L5 CAPEX calendar; control Princess Elisabeth/HVDC costs,"
        "seed,,tick170",
        "lb_elia_etb_revenue_1_7bn,Elia ETB revenue 1.67bn profit 301m 2025,federal,ops,"
        "Federal>Energy>Elia>ops,1667400000,1667400000,"
        "IAR strong: rev 1.667bn (+32pct) profit 300.7m; settlement mech volatile -161m; personnel 264m,"
        "strong,src_elia_etb_iar2025,Grid users,"
        "Regulated TSO operations,"
        "Core monopoly; tariff-funded; equity inject 1.06bn public-linked holding,"
        "3,9.0,6,6.3,"
        "Open settlement mechanism L5; dividend vs CAPEX balance,"
        "seed,,tick170",
    ],
)

replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_165,",
    "rq_165,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ",2026-07-28T06:25:00Z,2026-07-28T06:45:00Z,"
    '"tick170: Elia ETB IAR2025 rev 1.667bn profit 301m CAPEX 1.47bn RAB 7.8bn equity 4.43bn plan 7.5bn; Mons/Antwerp still FOI; spawn rq_166"\n',
)

rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_166," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_166,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T06:45:00Z,,"
            '"Spawned tick170 after Elia ETB; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_166 hole-fill Antwerp/Mons/taxex/other; rq_116 SWA deferred. FOI ready human send. tick170 Elia ETB 1.67bn."\n',
    encoding="utf-8",
    newline="\n",
)

log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **Elia Transmission Belgium IAR 2025**)
- Found (strong primary integrated annual report, consol FS €m):
  - **Revenue 1.667bn 2025** (1.258bn 2024) · **profit 300.7m** (245.0m) · **EBIT 448.7m**.
  - Settlement mechanism **−160.9m** 2025 (was **+247.8m** 2024) — OSP/GC volatility link.
  - Personnel **264.0m** · services **646.0m** · D&A **266.9m**.
  - **CAPEX ~1.47bn** · **RAB 7.8bn** · PPE **7.14bn** · assets **11.68bn** · equity **4.43bn** (inject **+1.057bn**).
  - Loans LT **4.86bn** + ST **0.63bn** · cash **1.50bn** · dividends **99.7m**.
  - CAPEX plan **7.5bn 2025–28** · 2026 invest plan **1.7bn** · Baekeland **~400m** · Green Bond **500m**.
  - Grid **8 851 km** · reliability **99.99%** · dual with Fluvius DSO + CRM host.
- Mons BI2026 / Antwerp full register still not newly filled.
- Wrote: sources 1; budgets 28; cmt 1; lb 2; entity note; rq_165=done; seeded **rq_166**.
- FOI: no new gap (regulated monopoly well disclosed); residual local FOIs human send.
- Next: prio5 **rq_166**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")
print("tick170 OK")

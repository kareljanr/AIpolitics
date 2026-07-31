# -*- coding: utf-8 -*-
"""Tick 168: CREG AR2025 offshore wind support cost 538.5m + nuclear redistribution."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T06:05:00Z"
TICK = 168
UNIT = "rq_163"


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
        "src_creg_ar2025,CREG Rapport annuel 2025 FR official PDF,"
        "https://www.creg.be/sites/default/files/assets/Publications/AnnualReports/CREG-AR2025-FR.pdf,"
        "CREG,2026-07-28,official_annual_report,"
        '"Offshore support total 538.5m 2025 (GC purchase 456.24m + advances 82.26m); production 6780 GWh inject / 6912 GWh net; '
        'advances regime ended 2025; nuclear contribution Electrabel 152.5m Luminus 8.8m 2025; tick168"'
    ],
)

append_lines(
    DATA / "budgets.csv",
    [
        "bud_offshore_support_total_2025,sec_federal,2025,538500000,,,outturn,src_creg_ar2025,strong,"
        "CREG total offshore wind support cost 538.5m 2025 (GC+advances)",
        "bud_offshore_gc_cost_2025,sec_federal,2025,456240000,,,outturn,src_creg_ar2025,strong,"
        "Federal green certificates granted offshore parks 456.24m 2025 (7 parks listed)",
        "bud_offshore_advances_2025,sec_federal,2025,82260000,,,outturn,src_creg_ar2025,strong,"
        "Offshore advances system 82.26m 2025 (Northwester2 Mermaid Seastar); regime ended 2025",
        "bud_offshore_prod_gwh_inject_2025,sec_federal,2025,6780,,,outturn,src_creg_ar2025,strong,"
        "Offshore net injection to grid 6780 GWh 2025 (7054 GWh 2024)",
        "bud_offshore_prod_gwh_inject_2024,sec_federal,2024,7054,,,outturn,src_creg_ar2025,strong,"
        "Offshore net injection 7054 GWh 2024",
        "bud_offshore_prod_gwh_net_cert_2025,sec_federal,2025,6912,,,outturn,src_creg_ar2025,strong,"
        "Offshore certified net production before transform 6912 GWh 2025",
        "bud_offshore_support_per_mwh_2025,sec_federal,2025,77.9,,,outturn,src_creg_ar2025,medium,"
        "Implied support EUR/MWh 538.5m/6912 GWh ~77.9 (order of magnitude)",
        "bud_nuclear_contrib_electrabel_2025,sec_federal,2025,152517984.5,,,budgeted,src_creg_ar2025,strong,"
        "Contribution de repartition Electrabel 152.518m 2025 (AR 12 Oct 2025 after CREG avis)",
        "bud_nuclear_contrib_luminus_2025,sec_federal,2025,8821247.28,,,budgeted,src_creg_ar2025,strong,"
        "Contribution de repartition Luminus 8.821m 2025",
        "bud_nuclear_contrib_total_2025,sec_federal,2025,161339231.78,,,budgeted,src_creg_ar2025,strong,"
        "Nuclear redistribution contribution sum Electrabel+Luminus 161.3m 2025",
    ],
)

append_lines(
    DATA / "commitments.csv",
    [
        'cmt_offshore_support_creg_2025,Federal offshore wind support cost CREG multi-year path,sec_federal,'
        "9 North Sea wind parks (domain concessions),AR 16 Jul 2002 RES support + CREG annual,"
        "2009-04-01,2023,2025,538500000,"
        '"{""2025_total"":538500000,""2025_gc"":456240000,""2025_advances"":82260000,'
        '""2025_gwh_inject"":6780,""2024_gwh_inject"":7054,""2025_gwh_net_cert"":6912,'
        '""parks_gc"":""C-Power Belwind Northwind Nobelwind Norther Rentel Northwester2"",'
        '""parks_advances"":""Northwester2 Mermaid Seastar"",""advances_ended"":2025,'
        '""prior_creg_2023_class"":179400000,""nbb_esa_2024"":592000000,'
        '""note"":""CREG total=GC purchase+advances; prior 179.4m 2023 may be different perimeter/net; NBB ESA D.31 592m 2024 still dual series""}",'
        "0,active,https://www.creg.be/sites/default/files/assets/Publications/AnnualReports/CREG-AR2025-FR.pdf,"
        "Promote offshore RES generation Belgium,"
        "Publish annual cash series 2020-2026 same method; reconcile NBB ESA; advance phase-out done,"
        "src_creg_ar2025,strong,Federal>Energy>offshore_wind,"
        "tick168; partial close gap_offshore; residual multi-year same-method series+NBB reconcile FOI",
        'cmt_nuclear_repartition_2025,Nuclear contribution de repartition Electrabel+Luminus 2025,sec_federal,'
        "Electrabel Luminus nuclear operators,Loi contribution repartition + AR 12 Oct 2025,"
        "2025-01-01,2025,2025,161339232,"
        '"{""electrabel"":152517984.5,""luminus"":8821247.28,""total"":161339231.78,'
        '""source"":""CREG avis then AR 12 Oct 2025"",""plants"":""Doel4 Tihange3 class""}",'
        "0,active,https://www.creg.be/sites/default/files/assets/Publications/AnnualReports/CREG-AR2025-FR.pdf,"
        "Redistribute nuclear infra-marginal rents,"
        "Publish multi-year series; track LTO budgets separately,"
        "src_creg_ar2025,strong,Federal>Energy>nuclear_repartition,"
        "tick168 bonus L5 from same CREG AR",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_offshore_support_538m,Offshore wind federal support 538.5m 2025,federal,subsidy,"
        "Federal>Energy>offshore_wind,538500000,538500000,"
        "CREG AR strong: 538.5m 2025 (GC 456.2m + advances 82.3m); dual NBB ESA 592m 2024 residual,"
        "strong,src_creg_ar2025,Electricity consumers taxpayers,"
        "Offshore wind green certificate support,"
        "Not pure waste (climate/RES); high annual cost; advances ended 2025; dual accounting opacity,"
        "5,9.5,7,7.3,"
        "Open multi-year same-method series; reconcile ESA; track new tender zero-subsidy path,"
        "seed,,tick168",
        "lb_nuclear_repartition_161m,Nuclear contribution de repartition 161m 2025,federal,tax,"
        "Federal>Energy>nuclear_repartition,161339232,161339232,"
        "Strong CREG/AR: Electrabel 152.5m + Luminus 8.8m 2025,"
        "strong,src_creg_ar2025,Taxpayers nuclear operators,"
        "Infra-marginal rent redistribution,"
        "Revenue not spending; dual with LTO state contracts,"
        "3,8.5,5,5.3,"
        "Publish multi-year; separate LTO budgets,"
        "seed,,tick168",
    ],
)

# FOI gap_offshore update
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_offshore_annual_cash,",
    "gap_offshore_annual_cash,Federal>Energy>offshore_wind>annual,sec_federal,"
    "Reconcile CREG total support method (GC+advances: 538.5m 2025 strong) vs NBB ESA D.31 offshore series 2022-2026 "
    "(NBB 592m 2024; prior CREG 179.4m 2023 different perimeter); publish same-method annual series 2020-2024,"
    "2025 CREG total filled strong; multi-year same-method pre-2025 and ESA dual still opaque,"
    "6,FOD Economie AD Energie / CREG / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_offshore_annual_cash.md,ready,2026-07-20,,,,,"
    "cmt_offshore_support_creg_2025,lb_offshore_support_538m,"
    "2026-07-20T02:40:00Z,2026-07-28T06:05:00Z,"
    "rq_032 |tick168: CREG 538.5m 2025 filled; residual multi-year+NBB reconcile human send\n",
)

replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_163,",
    "rq_163,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV if unblocked other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_offshore_annual_cash,2026-07-28T05:45:00Z,2026-07-28T06:05:00Z,"
    '"tick168: CREG AR2025 offshore support 538.5m (GC 456.2m + advances 82.3m) nuclear repartition 161m; Mons BI2026 still missing; spawn rq_164"\n',
)

rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_164," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_164,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex updates large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T06:05:00Z,,"
            '"Spawned tick168 after CREG offshore; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_164 hole-fill Antwerp/Mons/taxex/other; rq_116 SWA deferred. FOI ready human send. tick168 CREG offshore 538.5m."\n',
    encoding="utf-8",
    newline="\n",
)

log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **CREG AR2025 offshore support + nuclear repartition**)
- Found (strong primary CREG Rapport annuel 2025 FR, 92 pp):
  - **Offshore total support 2025: EUR 538.5m** = GC purchase **456.24m** + advances **82.26m**.
  - Production: inject **6 780 GWh** (vs 7 054 in 2024); net certified **6 912 GWh**.
  - Parks GC: C-Power Belwind Northwind Nobelwind Norther Rentel Northwester2; advances: Northwester2 Mermaid Seastar (**regime ended 2025**).
  - Dual series residual: prior CREG 179.4m 2023 different perimeter; NBB ESA **592m 2024**.
  - Bonus L5: nuclear contribution de répartition **Electrabel 152.5m + Luminus 8.8m = 161.3m 2025**.
- Mons BI2026 still not online (only 2025 ord/extra PDFs); Antwerp full register still FOI.
- Wrote: sources 1; budgets 10; cmt 2; lb 2; gap_offshore notes partial; rq_163=done; seeded **rq_164**.
- FOI: gap_offshore residual multi-year same-method + NBB reconcile still **ready** human send.
- Next: prio5 **rq_164**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")
print("tick168 OK")

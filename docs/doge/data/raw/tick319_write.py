# tick 319 — Rail Facilities dual HR Rail/NMBS staff procurement vehicle
from pathlib import Path

base = Path("docs/doge/data")

def append(name: str, text: str) -> None:
    path = base / name
    with open(path, "a", encoding="utf-8", newline="") as f:
        if not text.endswith("\n"):
            text += "\n"
        f.write(text)

append(
    "sources.csv",
    "src_rail_facilities_companyweb_nbb,Rail Facilities NV NBB-derived multi-year jaarrekening Companyweb KBO 0403.265.325,"
    "https://www.companyweb.be/nl/0403265325/rail-facilities; https://consult.cbso.nbb.be/consult-enterprise/0403265325,"
    "Companyweb (NBB CBSO),2026-07-30,nbb,"
    '"Strong statutory: omzet 11.279/13.830/13.874/14.839m 2022-25; net 0.069/0.192/0.149/0.112m; '
    'equity ~11.0m 2025; FTE 0 (staff via HR Rail); dual Infrabel 49pct stake path"',
)

append(
    "entities.csv",
    "rail_facilities,Rail Facilities NV,Rail Facilities SA,"
    "Rail staff social procurement vehicle NMBS Infrabel HR Rail families,parastatal,hr_rail,bi,,,,"
    "Frankrijkstraat 58 1060 Sint-Gillis,"
    "Procurement for serving/retired rail staff; omzet ~14.8m 2025; FTE 0 dual HR; Infrabel 49pct via HR; tick319",
)

append(
    "budgets.csv",
    "bud_rail_fac_omzet_2022,rail_facilities,2022,11278774,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Rail Facilities statutory omzet 11278774 EUR 2022\n"
    "bud_rail_fac_omzet_2023,rail_facilities,2023,13829791,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Rail Facilities statutory omzet 13829791 EUR 2023\n"
    "bud_rail_fac_omzet_2024,rail_facilities,2024,13874085,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Rail Facilities statutory omzet 13874085 EUR 2024\n"
    "bud_rail_fac_omzet_2025,rail_facilities,2025,14839471,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Rail Facilities statutory omzet 14839471 EUR 2025\n"
    "bud_rail_fac_net_2024,rail_facilities,2024,149041,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Net result 149041 EUR 2024\n"
    "bud_rail_fac_net_2025,rail_facilities,2025,111719,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Net result 111719 EUR 2025\n"
    "bud_rail_fac_equity_2025,rail_facilities,2025,11008963,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Equity 11008963 EUR YE2025\n"
    "bud_rail_fac_fte_2025,rail_facilities,2025,0,,,outturn,src_rail_facilities_companyweb_nbb,strong,"
    "Statutory FTE 0 2025 (legal employment via HR Rail dual; same pattern as NMBS)",
)

cash = (
    '"{""omzet_2022"":11278774,""omzet_2023"":13829791,'
    '""omzet_2024"":13874085,""omzet_2025"":14839471,'
    '""net_2025"":111719,""equity_2025"":11008963,""fte"":0,'
    '""infrabel_stake_pct"":49}"'
)

append(
    "commitments.csv",
    "cmt_rail_facilities_omzet_2022_25,Rail Facilities procurement vehicle omzet path dual HR Rail,"
    "rail_facilities,Serving and retired NMBS Infrabel HR Rail staff and families,"
    "NV procurement + Infrabel AR subsidiaries 49pct via HR Rail,"
    f"1930-05-11,2022,2025,53822121,{cash},,active,,"
    "Staff social/procurement services for rail public employers,"
    "Publish activity split and client recharge L5; dual stack map,"
    "src_rail_facilities_companyweb_nbb,strong,Federal>Mobiliteit>HR_Rail>Rail_Facilities,"
    "tick319: omzet 14.8m 2025; FTE 0 dual HR; small vs HR 2.37bn but completes dual structure map",
)

append(
    "leaderboard.csv",
    "lb_rail_facilities_omzet_15m,Rail Facilities omzet ~14.8m 2025 dual HR Rail,federal,ops,"
    "Federal>Mobiliteit>HR_Rail>Rail_Facilities>omzet,14839471,14839471,"
    "Strong NBB: 14.84m 2025 (13.87m 2024); FTE 0; Infrabel 49pct; dual NMBS statutory FTE 0 pattern,"
    "strong,src_rail_facilities_companyweb_nbb,Rail staff families taxpayers,"
    "Procurement/social services for rail staff,"
    "Core staff welfare vehicle; dual employer opacity pattern; small vs HR payroll 2.4bn,"
    "3,4.5,3,3.7,Open L5 product mix and markups,seed,,tick319 dual rail stack\n"
    "lb_rail_dual_stack_map,Rail public dual stack HR+NMBS+Infrabel+daughters,federal,ops,"
    "Federal>Mobiliteit>rail>dual_full_stack,2368227721,322236232,"
    "Strong multi-tick map: HR 2.37bn payroll; NMBS ops 17k FTE0 statutory; Infrabel 9.4k+810m; Ypto 140m TUC 182m RailFac 15m,"
    "strong,src_rail_facilities_companyweb_nbb,Passengers taxpayers,"
    "Full dual public rail employer and daughter map,"
    "Core sector structure; not additive TE; L5 charge matrix FOI residual,"
    "5,9.0,5,6.8,Joint annual dual disclosure table,seed,,tick319 closes dual map note",
)

append(
    "foi_queue.csv",
    "gap_rail_facilities_l5,Federal>HR_Rail>Rail_Facilities>L5_activity,rail_facilities,"
    "Activity/product mix L5 2023-2025 (canteen shops insurance other) with EUR; recharge rules to NMBS Infrabel HR; "
    "ownership cash dividends 2022-2025; reconcile 0 FTE with any seconded staff,"
    "Entity omzet ~15m strong; activity opacity dual staff-welfare vehicle,"
    "3,Rail Facilities / HR Rail / FOD Mobiliteit openbaarheid,,"
    "https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_rail_facilities_l5.md,ready,2026-07-30,,,,,"
    "cmt_rail_facilities_omzet_2022_25,lb_rail_facilities_omzet_15m,"
    "2026-07-30T22:15:00Z,2026-07-30T22:15:00Z,tick319 draft ready human send low-medium prio",
)

# FOI draft will be written separately as markdown file

rq = (base / "research_queue.csv").read_text(encoding="utf-8")
old = (
    "rq_311,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after or with progress@320. Prefer before idle.,,"
    "2026-07-30T21:45:00Z,,Spawned tick318; after progress@320"
)
new = (
    "rq_311,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills after or with progress@320. Prefer before idle.,"
    "gap_rail_facilities_l5,2026-07-30T21:45:00Z,2026-07-30T22:15:00Z,"
    "tick319: Rail Facilities omzet 14.8m FTE0 dual HR; FOI L5; spawn continue; progress@320 next\n"
    "rq_312,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after progress@320. Prefer before idle.,,"
    "2026-07-30T22:15:00Z,,Spawned tick319; do after rq_310 progress@320"
)
if old not in rq:
    raise SystemExit("rq_311 not found")
(base / "research_queue.csv").write_text(rq.replace(old, new), encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T22:15:00Z,rq_311,319,no,"
    "Scheduler 60s. NEXT MANDATORY rq_310 progress@320; then rq_312; rq_116 SWA deferred. "
    "tick319 Rail Facilities 14.8m dual HR.\n",
    encoding="utf-8",
)

print("tick319 CSV writes OK")

# tick 321 — Egov Select omzet ~112m dual Smals (closes gap_egov_select institutional)
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
    "src_egov_select_companyweb_nbb,Egov Select VZW NBB-derived multi-year jaarrekening Companyweb KBO 0475.479.251,"
    "https://www.companyweb.be/nl/0475479251/egov-select; https://consult.cbso.nbb.be/consult-enterprise/0475479251,"
    "Companyweb (NBB CBSO),2026-07-30,nbb,"
    '"Strong: omzet 73.0/71.4/92.0/111.9m 2021-24; FTE 544.6/660.8/772.4/907.7; net 2.81m 2023 / 1.28m 2024; '
    'equity 8.37m 2024; dual Smals federal IT detachment"',
)

# update entity egov_select
ents = (base / "entities.csv").read_text(encoding="utf-8")
old_ent = (
    "egov_select,Egov Select vzw,Egov Select asbl,"
    "Egov Select federal IT recruitment and detachment VZW,asbl,sec_federal,bi,,,,"
    "IT detachments to FODs police defence cultural/scientific; private-sector pay scales; dual Smals SS-focused; CoA 2025; tick311"
)
new_ent = (
    "egov_select,Egov Select vzw,Egov Select asbl,"
    "Egov Select federal IT recruitment and detachment VZW,asbl,sec_federal,bi,"
    "https://egovselect.be,,,,"
    "Omzet 111.9m 2024 FTE 907.7; growth 73m 2021 to 112m 2024; dual Smals 579m; tick311+321"
)
if old_ent not in ents:
    raise SystemExit("egov_select entity not found")
(base / "entities.csv").write_text(ents.replace(old_ent, new_ent), encoding="utf-8")

append(
    "budgets.csv",
    "bud_egov_omzet_2021,egov_select,2021,73022796,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "Egov Select omzet 73022796 EUR 2021 NBB-derived\n"
    "bud_egov_omzet_2022,egov_select,2022,71435229,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "Egov Select omzet 71435229 EUR 2022\n"
    "bud_egov_omzet_2023,egov_select,2023,92016018,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "Egov Select omzet 92016018 EUR 2023 (+28.8pct)\n"
    "bud_egov_omzet_2024,egov_select,2024,111943142,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "Egov Select omzet 111943142 EUR 2024 (+21.7pct)\n"
    "bud_egov_net_2023,egov_select,2023,2813217,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "Net result 2813217 EUR 2023\n"
    "bud_egov_net_2024,egov_select,2024,1275859,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "Net result 1275859 EUR 2024\n"
    "bud_egov_equity_2024,egov_select,2024,8368095,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "Equity 8368095 EUR YE2024\n"
    "bud_egov_fte_2021,egov_select,2021,545,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "FTE 544.6 2021\n"
    "bud_egov_fte_2022,egov_select,2022,661,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "FTE 660.8 2022\n"
    "bud_egov_fte_2023,egov_select,2023,772,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "FTE 772.4 2023\n"
    "bud_egov_fte_2024,egov_select,2024,908,,,outturn,src_egov_select_companyweb_nbb,strong,"
    "FTE 907.7 2024 (rapid growth dual Smals headcount path)\n"
    "bud_egov_unit_omzet_fte_2024,egov_select,2024,123300,,,estimate,src_egov_select_companyweb_nbb,medium,"
    "Implied omzet/FTE ~123k 2024 (111.9m/907.7); recharge/billing class not pure wage",
)

cash = (
    '"{""omzet_2021"":73022796,""omzet_2022"":71435229,'
    '""omzet_2023"":92016018,""omzet_2024"":111943142,'
    '""fte_2021"":544.6,""fte_2022"":660.8,""fte_2023"":772.4,""fte_2024"":907.7,'
    '""net_2024"":1275859,""equity_2024"":8368095,'
    '""smals_omzet_2025"":578900000}"'
)

append(
    "commitments.csv",
    "cmt_egov_select_omzet_2021_24,Egov Select federal IT detachment omzet path dual Smals,"
    "egov_select,Federal FODs police defence cultural scientific ICT,"
    "VZW federal IT recruitment and employment + NBB filings,"
    f"2001-07-17,2021,2024,348417185,{cash},,active,,"
    "Recruit select and employ ICT professionals for federal public sector,"
    "Publish top client FOD recharges L5; dual unit-cost Smals; free NBB PDF,"
    "src_egov_select_companyweb_nbb,strong,Federal>IT>Egov_Select>omzet,"
    "tick321: omzet 111.9m FTE 908 2024; closes institutional EUR FOI residual client L5",
)

append(
    "leaderboard.csv",
    "lb_egov_select_omzet_112m,Egov Select federal IT detachment omzet 111.9m 2024,federal,ops,"
    "Federal>IT>Egov_Select>omzet,111943142,111943142,"
    "Strong NBB: 111.9m 2024 (+22pct); FTE 907.7; dual Smals 579m SS-focused; private-sector pay scales,"
    "strong,src_egov_select_companyweb_nbb,Federal digital services taxpayers,"
    "Federal IT staff capacity vehicle,"
    "Core IT capacity; dual middleman with Smals; rapid FTE growth 545->908 2021-24,"
    "5,7.5,3,5.9,Open client FOD matrix; dual unit-cost Smals,seed,,tick321 dual Smals\n"
    "lb_egov_smals_dual_ict,Federal dual ICT middlemen Egov Select 112m + Smals 579m,federal,ops,"
    "Federal>IT>Egov_Smals_dual,111943142,578900000,"
    "Strong dual map: Egov Select federal detachments 112m vs Smals multi-sector 579m; not additive TE; external IT 206m under Smals separate,"
    "strong,src_egov_select_companyweb_nbb,Taxpayers multi-level digital,"
    "Fragmented federal/SS public ICT capacity,"
    "Dual structures; L5 clients residual both; CoA consultancy context,"
    "6,8.5,4,6.9,Common transparency L5 recharges both VZW,seed,,tick321 dual structure\n"
    "lb_egov_fte_growth_908,Egov Select FTE growth 545 to 908 2021-24,federal,ops,"
    "Federal>IT>Egov_Select>FTE,908,908,"
    "Strong NBB FTE series 544.6/660.8/772.4/907.7; ~+67pct in 3y; omzet/FTE ~123k class,"
    "strong,src_egov_select_companyweb_nbb,Federal IT workforce,"
    "Staffing capacity expansion,"
    "Growth not pure waste; track unit cost and client value,"
    "4,5.5,3,4.5,Publish productivity KPIs with FODs,seed,,tick321",
)

# update FOI gap_egov_select_budget to partial/answered-style residual
foi = (base / "foi_queue.csv").read_text(encoding="utf-8")
old_gap = (
    "gap_egov_select_budget,Federal>IT>Egov_Select>recharges_FTE,egov_select,"
    "Annual recharge total and FTE detached 2023-2026; top client FODs by EUR; wage bill; reconcile any FPS budget lines,"
    "CoA model strong; absolute EUR missing; dual Smals external 206m material,"
    "5,Egov Select / FOD BOSA openbaarheid,,https://bosa.belgium.be,"
    "docs/doge/foi/drafts/gap_egov_select_budget.md,ready,2026-07-30,,,,,,"
    "cmt_egov_select_model,lb_smals_external_it_206m,"
    "2026-07-30T18:15:00Z,2026-07-30T18:15:00Z,tick311 draft ready human send"
)
new_gap = (
    "gap_egov_select_budget,Federal>IT>Egov_Select>recharges_FTE,egov_select,"
    "Top client FODs by EUR recharge 2023-2025; wage bill vs omzet recon; 2025-26 multi-year; free NBB PDF confirmation,"
    "Institutional omzet 111.9m and FTE 907.7 2024 filled strong tick321; residual L5 client matrix,"
    "4,Egov Select / FOD BOSA openbaarheid,,https://bosa.belgium.be,"
    "docs/doge/foi/drafts/gap_egov_select_budget.md,ready,2026-07-30,,,,,,"
    "cmt_egov_select_omzet_2021_24,lb_egov_select_omzet_112m,"
    "2026-07-30T18:15:00Z,2026-07-30T23:15:00Z,"
    "tick311 draft | tick321: omzet+FTE filled public; residual top FOD recharges human send"
)
if old_gap not in foi:
    raise SystemExit("gap_egov_select_budget not found exact")
(base / "foi_queue.csv").write_text(foi.replace(old_gap, new_gap), encoding="utf-8")

rq = (base / "research_queue.csv").read_text(encoding="utf-8")
old = (
    "rq_312,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after progress@320. Prefer before idle.,,"
    "2026-07-30T22:15:00Z,,Spawned tick319; do after rq_310 progress@320"
)
new = (
    "rq_312,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills after progress@320. Prefer before idle.,"
    "gap_egov_select_budget,2026-07-30T22:15:00Z,2026-07-30T23:15:00Z,"
    "tick321: Egov Select omzet 111.9m FTE 908 dual Smals; FOI L5 clients residual; spawn rq_313\n"
    "rq_313,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-30T23:15:00Z,,Spawned tick321 after Egov Select; rq_116 SWA deferred"
)
if old not in rq:
    raise SystemExit("rq_312 not found")
(base / "research_queue.csv").write_text(rq.replace(old, new), encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T23:15:00Z,rq_312,321,no,"
    "Scheduler 60s. Next prio5 rq_313; rq_116 SWA deferred. FOI ready. "
    "tick321 Egov Select ~112m dual Smals.\n",
    encoding="utf-8",
)

print("tick321 CSV writes OK")

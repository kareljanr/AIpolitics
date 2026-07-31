# tick 322 — ASTRID statutory omzet/net/equity deepen dual IBZ toelage wedge
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
    "src_astrid_companyweb_nbb,ASTRID NV PR NBB-derived multi-year jaarrekening Companyweb KBO 0263.893.151,"
    "https://www.companyweb.be/nl/0263893151/a-s-t-r-i-d-; https://consult.cbso.nbb.be/consult-enterprise/0263893151,"
    "Companyweb (NBB CBSO),2026-07-30,nbb,"
    '"Strong: omzet 23.57/25.93/26.20/27.16m 2022-25; net 11.83/14.90/14.04/14.65m; equity 123/139/152/167m; '
    'FTE 121/126/132/136; negative brutomarge; dual IBZ toelage 76.5m 2025 residual recon"',
)

# entity update
ents = (base / "entities.csv").read_text(encoding="utf-8")
old_ent = (
    "astrid,ASTRID NV radiocommunicatie,ASTRID SA radiocommunications,"
    "ASTRID emergency radio network company,soe,sec_federal,bi,https://www.astrid.be,,,"
    "Federal SOE TETRA radio emergency services; contract 46.5m/yr ops; IBZ toelage 76.5m 2025; invest 117m subscriptions; tick284-285"
)
new_ent = (
    "astrid,ASTRID NV radiocommunicatie,ASTRID SA radiocommunications,"
    "ASTRID emergency radio network company,soe,sec_federal,bi,https://www.astrid.be,,,"
    "Omzet 27.2m 2025 net 14.6m equity 167m FTE 136; IBZ toelage 76.5m vs contract 46.5m vs omzet wedge; tick284-285+322"
)
if old_ent not in ents:
    raise SystemExit("astrid entity not found")
(base / "entities.csv").write_text(ents.replace(old_ent, new_ent), encoding="utf-8")

append(
    "budgets.csv",
    "bud_astrid_omzet_2022,astrid,2022,23568911,,,outturn,src_astrid_companyweb_nbb,strong,"
    "ASTRID statutory omzet 23568911 EUR 2022\n"
    "bud_astrid_omzet_2023,astrid,2023,25931259,,,outturn,src_astrid_companyweb_nbb,strong,"
    "ASTRID statutory omzet 25931259 EUR 2023\n"
    "bud_astrid_omzet_2024,astrid,2024,26204037,,,outturn,src_astrid_companyweb_nbb,strong,"
    "ASTRID statutory omzet 26204037 EUR 2024\n"
    "bud_astrid_omzet_2025,astrid,2025,27159629,,,outturn,src_astrid_companyweb_nbb,strong,"
    "ASTRID statutory omzet 27159629 EUR 2025\n"
    "bud_astrid_net_2022,astrid,2022,11834459,,,outturn,src_astrid_companyweb_nbb,strong,"
    "Net result 11834459 EUR 2022\n"
    "bud_astrid_net_2023,astrid,2023,14900284,,,outturn,src_astrid_companyweb_nbb,strong,"
    "Net result 14900284 EUR 2023\n"
    "bud_astrid_net_2024,astrid,2024,14044235,,,outturn,src_astrid_companyweb_nbb,strong,"
    "Net result 14044235 EUR 2024\n"
    "bud_astrid_net_2025,astrid,2025,14647241,,,outturn,src_astrid_companyweb_nbb,strong,"
    "Net result 14647241 EUR 2025\n"
    "bud_astrid_equity_2025,astrid,2025,166640503,,,outturn,src_astrid_companyweb_nbb,strong,"
    "Equity 166640503 EUR YE2025 (152.1m YE2024)\n"
    "bud_astrid_fte_2025,astrid,2025,136,,,outturn,src_astrid_companyweb_nbb,strong,"
    "FTE 136.2 2025 (132 2024; 126.2 2023; 121.3 2022)\n"
    "bud_astrid_brutomarge_2025,astrid,2025,-25735122,,,outturn,src_astrid_companyweb_nbb,strong,"
    "Negative brutomarge -25.7m 2025 (omzet below COGS/services class; other income/subsidies residual)\n"
    "bud_astrid_wedge_ibz_vs_omzet_2025,astrid,2025,49357371,,,estimate,src_astrid_companyweb_nbb,medium,"
    "IBZ toelage 76.517m - statutory omzet 27.160m = residual 49.4m class not hitting omzet line; recon FOI",
)

cash = (
    '"{""omzet_2022"":23568911,""omzet_2023"":25931259,'
    '""omzet_2024"":26204037,""omzet_2025"":27159629,'
    '""net_2025"":14647241,""equity_2025"":166640503,""fte_2025"":136.2,'
    '""ops_contract_m"":46500000,""ibz_toelage_2025_m"":76517000,'
    '""wedge_ibz_vs_omzet_2025"":49357371,'
    '""invest_subscriptions_m"":117000000}"'
)

append(
    "commitments.csv",
    "cmt_astrid_statutory_path_2022_25,ASTRID statutory P&L path dual IBZ toelage recon,"
    "astrid,Police fire emergency services Belgium,"
    "NV PR emergency radio + NBB filings + 4th management contract 2023-27,"
    f"1998-07-31,2022,2025,166640503,{cash},,active,,"
    "National TETRA digital radio for emergency services,"
    "FOI full P&L other income vs IBZ 76.5m; reconcile omzet 27m vs contract 46.5m,"
    "src_astrid_companyweb_nbb,strong,Federal>IBZ>ASTRID>statutory,"
    "tick322: omzet 27m net 14.6m equity 167m; triple wedge IBZ 76.5 / contract 46.5 / omzet 27",
)

append(
    "leaderboard.csv",
    "lb_astrid_omzet_27m,ASTRID statutory omzet ~27m 2025 dual IBZ 76.5m,federal,ops,"
    "Federal>IBZ>ASTRID>omzet,27159629,27159629,"
    "Strong NBB: omzet 27.16m 2025; net 14.65m; equity 167m FTE 136; triple wedge vs IBZ 76.5m and contract 46.5m,"
    "strong,src_astrid_companyweb_nbb,Emergency services police fire,"
    "National emergency radio SOE operations,"
    "Core public safety; financing opacity: toelage>>omzet; high net on thin omzet; negative brutomarge,"
    "6,6.0,4,5.7,Publish full P&L other income and IBZ cash split,seed,,tick322 dual opacity\n"
    "lb_astrid_triple_wedge,ASTRID triple financing wedge IBZ 76.5 / contract 46.5 / omzet 27,federal,ops,"
    "Federal>IBZ>ASTRID>financing_wedge,27159629,76517000,"
    "Strong multi-source: IBZ budget 76.517m 2025; contract ops 46.5m/yr; statutory omzet 27.2m; residual ~30m and ~49m class,"
    "strong,src_astrid_companyweb_nbb,Taxpayers emergency services,"
    "Reconcile three public financing perimeters,"
    "Material opacity on emergency radio SOE cash path; invest 117m subscriptions separate,"
    "7,7.5,4,6.8,FOI cash-by-year recon all three series,seed,,tick322 high mechanism\n"
    "lb_astrid_equity_167m,ASTRID equity stock 167m YE2025,federal,ops,"
    "Federal>IBZ>ASTRID>equity,166640503,166640503,"
    "Strong NBB: equity 123.4/139.0/152.1/166.6m 2022-25; net retained ~14m/yr class,"
    "strong,src_astrid_companyweb_nbb,State as shareholder taxpayers,"
    "SOE balance sheet accumulation,"
    "Not pure waste; dividend/reinvestment policy residual,"
    "3,7.0,4,5.2,Publish dividend path and CAPEX vs equity build,seed,,tick322",
)

# update FOI gap
foi = (base / "foi_queue.csv").read_text(encoding="utf-8")
old_gap = (
    "gap_astrid_toelage_reconcile,Federal>IBZ>ASTRID>toelage_vs_contract,astrid,"
    "Reconcile IBZ toelage line 76.517m 2025 vs management contract ops 46.5m/yr 2023-27: cash-by-year split ops vs invest vs other; "
    "full ASTRID annual accounts 2023-2025; subscription revenue series; ownership SFPIM/state,"
    "Contract 46.5m public strong; IBZ 76.5m higher — material ~30m opacity on emergency radio SOE,"
    "6,FOD Binnenlandse Zaken / ASTRID NV openbaarheid,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_astrid_toelage_reconcile.md,ready,2026-07-30,,,,,,"
    "cmt_astrid_financing_2023_27,lb_astrid_76m_vs_46m,"
    "2026-07-30T05:15:00Z,2026-07-30T05:15:00Z,tick285 draft ready human send"
)
new_gap = (
    "gap_astrid_toelage_reconcile,Federal>IBZ>ASTRID>toelage_vs_contract,astrid,"
    "Reconcile triple: IBZ 76.517m 2025 vs contract ops 46.5m vs statutory omzet 27.2m — other operating income cash path; "
    "subscription revenue series; ownership SFPIM/state dividends; free NBB full PDF,"
    "Statutory omzet/net/equity multi-year filled strong tick322; residual cash recon of three perimeters,"
    "6,FOD Binnenlandse Zaken / ASTRID NV openbaarheid,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_astrid_toelage_reconcile.md,ready,2026-07-30,,,,,,"
    "cmt_astrid_statutory_path_2022_25,lb_astrid_triple_wedge,"
    "2026-07-30T05:15:00Z,2026-07-30T23:45:00Z,"
    "tick285 draft | tick322: statutory omzet 27m net 14.6m equity 167m filled; residual triple recon human send"
)
if old_gap not in foi:
    raise SystemExit("gap_astrid not found")
(base / "foi_queue.csv").write_text(foi.replace(old_gap, new_gap), encoding="utf-8")

rq = (base / "research_queue.csv").read_text(encoding="utf-8")
old = (
    "rq_313,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-30T23:15:00Z,,Spawned tick321 after Egov Select; rq_116 SWA deferred"
)
new = (
    "rq_313,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_astrid_toelage_reconcile,2026-07-30T23:15:00Z,2026-07-30T23:45:00Z,"
    "tick322: ASTRID omzet 27m net 14.6m equity 167m triple wedge IBZ 76.5; FOI recon; spawn rq_314\n"
    "rq_314,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-30T23:45:00Z,,Spawned tick322 after ASTRID; rq_116 SWA deferred"
)
if old not in rq:
    raise SystemExit("rq_313 not found")
(base / "research_queue.csv").write_text(rq.replace(old, new), encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T23:45:00Z,rq_313,322,no,"
    "Scheduler 60s. Next prio5 rq_314; rq_116 SWA deferred. FOI ready. "
    "tick322 ASTRID omzet 27m triple wedge IBZ 76.5.\n",
    encoding="utf-8",
)

print("tick322 CSV writes OK")

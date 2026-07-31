# tick 323 — skeyes 2025 statutory omzet 353m dual airports (closes BS residual class)
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
    "src_skeyes_companyweb_nbb_2025,skeyes OI NBB-derived multi-year jaarrekening Companyweb KBO 0206.048.091,"
    "https://www.companyweb.be/nl/0206048091/skeyes; https://consult.cbso.nbb.be/consult-enterprise/0206048091,"
    "Companyweb (NBB CBSO),2026-07-30,nbb,"
    '"Strong: omzet 306.1/309.6/335.2/352.9m 2022-25; net 18.8/9.1/15.8/18.6m; equity 281/290/309/328m; '
    'FTE 894.5/934.2/950.9/966.3; dual BAC/BSCA airports; tick323"',
)

# entity update
ents = (base / "entities.csv").read_text(encoding="utf-8")
old_ent = (
    "skeyes,skeyes (ex-Belgocontrol),skeyes (ex-Belgocontrol),"
    "Belgian air navigation service provider ANS,parastatal,sec_federal,bi,https://www.skeyes.be,,"
    "Steenokkerzeel,State-owned ANS; omzet 335.2m profit 15.4m equity ~308m 2024; COVID loan 110m; dual airports BAC/BSCA; tick189"
)
new_ent = (
    "skeyes,skeyes (ex-Belgocontrol),skeyes (ex-Belgocontrol),"
    "Belgian air navigation service provider ANS,parastatal,sec_federal,bi,https://www.skeyes.be,,"
    "Steenokkerzeel,Omzet 352.9m net 18.6m equity 328m FTE 966 2025; dual BAC/BSCA; COVID path prior; tick189+323"
)
if old_ent not in ents:
    raise SystemExit("skeyes entity not found")
(base / "entities.csv").write_text(ents.replace(old_ent, new_ent), encoding="utf-8")

append(
    "budgets.csv",
    "bud_skeyes_omzet_2022,skeyes,2022,306060923,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "skeyes statutory omzet 306060923 EUR 2022\n"
    "bud_skeyes_omzet_2023,skeyes,2023,309568223,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "skeyes statutory omzet 309568223 EUR 2023\n"
    "bud_skeyes_omzet_2024_nbb,skeyes,2024,335191054,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "skeyes statutory omzet 335191054 EUR 2024 NBB (matches JV 335.2m)\n"
    "bud_skeyes_omzet_2025,skeyes,2025,352850957,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "skeyes statutory omzet 352850957 EUR 2025 (+5.3pct)\n"
    "bud_skeyes_net_2022,skeyes,2022,18840905,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "Net 18840905 EUR 2022\n"
    "bud_skeyes_net_2023,skeyes,2023,9068544,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "Net 9068544 EUR 2023\n"
    "bud_skeyes_net_2024_nbb,skeyes,2024,15832485,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "Net 15832485 EUR 2024 NBB (JV profit 15.4m class)\n"
    "bud_skeyes_net_2025,skeyes,2025,18600526,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "Net 18600526 EUR 2025 (+17.5pct)\n"
    "bud_skeyes_equity_2024_nbb,skeyes,2024,308819414,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "Equity 308819414 EUR YE2024 NBB (matches prior est 308.4m)\n"
    "bud_skeyes_equity_2025,skeyes,2025,327517497,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "Equity 327517497 EUR YE2025\n"
    "bud_skeyes_fte_2024,skeyes,2024,951,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "FTE 950.9 2024 statutory\n"
    "bud_skeyes_fte_2025,skeyes,2025,966,,,outturn,src_skeyes_companyweb_nbb_2025,strong,"
    "FTE 966.3 2025 (media headcount 1006 class different metric)",
)

cash = (
    '"{""omzet_2022"":306060923,""omzet_2023"":309568223,'
    '""omzet_2024"":335191054,""omzet_2025"":352850957,'
    '""net_2024"":15832485,""net_2025"":18600526,'
    '""equity_2024"":308819414,""equity_2025"":327517497,'
    '""fte_2024"":950.9,""fte_2025"":966.3,'
    '""covid_loan_prior"":110000000,""correction_asset_2024"":195392000}"'
)

append(
    "commitments.csv",
    "cmt_skeyes_statutory_path_2022_25,skeyes multi-year statutory P&L dual airports,"
    "skeyes,Airlines airports Belgian State SES,"
    "OI air navigation + NBB filings + management contract,"
    f"1946-11-20,2022,2025,327517497,{cash},,active,,"
    "En-route and terminal ANS Belgium Luxembourg,"
    "Publish unit-rate multi-year and RP3 recovery cash; dual BAC terminal L5,"
    "src_skeyes_companyweb_nbb_2025,strong,Federal>skeyes>statutory,"
    "tick323: omzet 352.9m net 18.6m equity 328m 2025; closes multi-year BS residual class",
)

append(
    "leaderboard.csv",
    "lb_skeyes_omzet_353m,skeyes ANS omzet 353m 2025 dual airports,federal,ops,"
    "Federal>skeyes>omzet,352850957,352850957,"
    "Strong NBB: 352.9m 2025 (+5.3pct); net 18.6m equity 328m FTE 966; dual BAC/BSCA terminal,"
    "strong,src_skeyes_companyweb_nbb_2025,Airlines passengers airports,"
    "Air navigation service monopoly SES,"
    "Core aviation safety ops; unit-rate recovery and COVID correction residual FOI,"
    "3,8.0,4,5.7,Open multi-year unit rates and correction cash,seed,,tick323 dual airports\n"
    "lb_skeyes_net_path_19m,skeyes net result path 9-19m 2022-25,federal,ops,"
    "Federal>skeyes>net,18600526,18600526,"
    "Strong NBB: net 18.8/9.1/15.8/18.6m 2022-25; equity build 281->328m,"
    "strong,src_skeyes_companyweb_nbb_2025,State shareholder taxpayers,"
    "ANS financial sustainability,"
    "Not pure waste; track RP3 performance vs profit,"
    "3,5.5,3,4.3,Publish SES performance outturn,seed,,tick323",
)

# update FOI gap_skeyes
foi = (base / "foi_queue.csv").read_text(encoding="utf-8")
old_gap = (
    "gap_skeyes_bs_2025,Federal>skeyes>financials_L5,skeyes,"
    "Full statutory accounts 2025; RP3 correction recovery schedule cash-by-year 2024-2030; "
    "COVID state loan residual calendar; unit rates En-route Terminal 2024-26; digital tower CAPEX multi-year,"
    "2024 P&L strong public; 2025 full BS and multi-year tariff path thin on AR2025 web,"
    "5,skeyes openbaarheid / FOD Mobiliteit / IBZ FOI,,"
    "https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_skeyes_bs_2025.md,ready,2026-07-30,,,,,,"
    "cmt_skeyes_ans_2023_25,lb_skeyes_covid_correction_195m,"
    "2026-07-30T13:05:00Z,2026-07-30T13:05:00Z,tick189 draft ready human send"
)
new_gap = (
    "gap_skeyes_bs_2025,Federal>skeyes>financials_L5,skeyes,"
    "RP3 correction recovery schedule cash-by-year 2024-2030; COVID state loan residual calendar; "
    "unit rates En-route Terminal 2024-26; digital tower CAPEX multi-year; free NBB full PDF 2025,"
    "2025 statutory omzet 352.9m net 18.6m equity 328m FTE 966 filled strong tick323; residual multi-year tariff/CAPEX,"
    "4,skeyes openbaarheid / FOD Mobiliteit / IBZ FOI,,"
    "https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_skeyes_bs_2025.md,ready,2026-07-30,,,,,,"
    "cmt_skeyes_statutory_path_2022_25,lb_skeyes_omzet_353m,"
    "2026-07-30T13:05:00Z,2026-07-31T00:15:00Z,"
    "tick189 draft | tick323: 2025 statutory filled; residual RP3/unit rates/CAPEX human send"
)
if old_gap not in foi:
    raise SystemExit("gap_skeyes not found")
(base / "foi_queue.csv").write_text(foi.replace(old_gap, new_gap), encoding="utf-8")

rq = (base / "research_queue.csv").read_text(encoding="utf-8")
old = (
    "rq_314,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-30T23:45:00Z,,Spawned tick322 after ASTRID; rq_116 SWA deferred"
)
new = (
    "rq_314,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_skeyes_bs_2025,2026-07-30T23:45:00Z,2026-07-31T00:15:00Z,"
    "tick323: skeyes omzet 352.9m net 18.6m equity 328m 2025; FOI RP3 residual; spawn rq_315\n"
    "rq_315,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-31T00:15:00Z,,Spawned tick323 after skeyes; rq_116 SWA deferred"
)
if old not in rq:
    raise SystemExit("rq_314 not found")
(base / "research_queue.csv").write_text(rq.replace(old, new), encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T00:15:00Z,rq_314,323,no,"
    "Scheduler 60s. Next prio5 rq_315; rq_116 SWA deferred. FOI ready. "
    "tick323 skeyes omzet 353m 2025 dual airports.\n",
    encoding="utf-8",
)

print("tick323 CSV writes OK")

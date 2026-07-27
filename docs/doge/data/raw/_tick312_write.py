# tick 312 — rq_303 Ypto NMBS IT dual Smals
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T18:45:00Z"
unit = "rq_303"

src_lines = [
    (
        "src_ypto_companyweb_nbb,"
        "Ypto NV NBB-derived multi-year jaarrekening Companyweb KBO 0821.220.410,"
        "https://www.companyweb.be/nl/0821220410/ypto; https://consult.cbso.nbb.be/consult-enterprise/0821220410,"
        "Companyweb (NBB CBSO),2026-07-30,nbb_aggregator,"
        "Omzet 86.5/99.5/117.0/140.2m 2022-25; net -1.72/0.42/1.85/4.01m; FTE 291/342/391/445; "
        "equity 12.73m 2025; filed 2026-05-21; medium-strong NBB-derived; tick312\n"
    ),
    (
        "src_ccrek_ypto_nmbs_ih,"
        "Rekenhof consultancy 2025 NMBS Ypto in-house classification 296.7m vs staff 104.2m,"
        "docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Rekenhof / Cour des comptes,2026-07-30,court_audit,"
        "NMBS: all Ypto services 296.7m classed IH; CoA counts only Ypto internal staff 104.2m as IH; "
        "residual ~192m external via Ypto still claimed exempt; dual Smals; tick312\n"
    ),
]
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for line in src_lines:
        f.write(line)

ent_path = ROOT / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
if "ypto," not in ent:
    ent = ent.rstrip("\n") + "\n"
    ent += (
        "ypto,Ypto NV,Ypto SA,"
        "Ypto NMBS IT subsidiary computer consultancy,"
        "parastatal,nmbs,bi,https://www.ypto.be,,,,"
        "NMBS daughter IT; omzet 140.2m 2025 FTE 445; dual Smals/Egov IT middleman stack; "
        "CoA NMBS-Ypto path 296.7m class; tick312\n"
    )
    ent_path.write_text(ent, encoding="utf-8")

bud_rows = [
    "bud_ypto_omzet_2022,ypto,2022,86485941,,,outturn,src_ypto_companyweb_nbb,strong,"
    "NBB-derived omzet 86.485941m 2022",
    "bud_ypto_omzet_2023,ypto,2023,99477663,,,outturn,src_ypto_companyweb_nbb,strong,"
    "NBB-derived omzet 99.477663m 2023",
    "bud_ypto_omzet_2024,ypto,2024,116980076,,,outturn,src_ypto_companyweb_nbb,strong,"
    "NBB-derived omzet 116.980076m 2024",
    "bud_ypto_omzet_2025,ypto,2025,140170919,,,outturn,src_ypto_companyweb_nbb,strong,"
    "NBB-derived omzet 140.170919m 2025 (+19.8pct)",
    "bud_ypto_net_2024,ypto,2024,1852648,,,outturn,src_ypto_companyweb_nbb,strong,"
    "Net result 1.852648m 2024",
    "bud_ypto_net_2025,ypto,2025,4011212,,,outturn,src_ypto_companyweb_nbb,strong,"
    "Net result 4.011212m 2025",
    "bud_ypto_equity_2025,ypto,2025,12729967,,,outturn,src_ypto_companyweb_nbb,strong,"
    "Equity 12.729967m eoy2025",
    "bud_ypto_gross_margin_2025,ypto,2025,64107057,,,outturn,src_ypto_companyweb_nbb,strong,"
    "Gross margin 64.107057m 2025",
    "bud_ypto_fte_2025,ypto,2025,445,,,outturn,src_ypto_companyweb_nbb,strong,"
    "FTE 445 2025 (391.3 2024; 341.7 2023; 291.2 2022); not EUR",
    "bud_ypto_nmbs_ih_staff_coa,ypto,2022,104200000,,,estimate,src_ccrek_ypto_nmbs_ih,strong,"
    "CoA 2020-22 survey: Ypto internal staff performances 104.2m counted as in-house",
    "bud_ypto_nmbs_total_claim_coa,ypto,2022,296700000,,,estimate,src_ccrek_ypto_nmbs_ih,medium,"
    "NMBS classification: all Ypto services to NMBS 296.7m as IH (includes Ypto-procured external); CoA disputes full IH label",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

cmt_rows = [
    (
        "cmt_ypto_omzet_path_2022_25,Ypto NMBS IT subsidiary omzet path dual Smals,"
        "ypto,NMBS group rail digital ops,NV subsidiary of NMBS KBO 0821.220.410,"
        "2009-12-07,2022,2025,443114599,"
        '"{""omzet_2022"":86485941,""omzet_2023"":99477663,""omzet_2024"":116980076,'
        '""omzet_2025"":140170919,""net_2025"":4011212,""fte_2025"":445,'
        '""equity_2025"":12729967,""gross_margin_2025"":64107057,'
        '""note"":""Entity omzet is statutory; NMBS group consolidations may differ""}",'
        "0,active,https://www.companyweb.be/nl/0821220410/ypto,"
        "Rail IT services for NMBS,"
        "FOI NMBS-Ypto recharge matrix; dual Smals external 206m,"
        "src_ypto_companyweb_nbb,strong,Federal>NMBS>Ypto,tick312"
    ),
    (
        "cmt_ypto_nmbs_coa_ih_dispute,NMBS-Ypto in-house classification dispute CoA 296.7 vs 104.2m,"
        "ypto,NMBS as buyer of Ypto services,"
        "Special sectors public procurement + CoA audit definition,2020-01-01,2020,2022,296700000,"
        '"{""nmbs_claim_total_m"":296.7,""coa_staff_ih_only_m"":104.2,'
        '""implied_external_via_ypto_m"":192.5,'
        '""nmbs_consultancy_total_m"":465.1,'
        '""note"":""CoA counts only direct Ypto staff as IH; NMBS claims full Ypto envelope exempt from procurement law""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Clarify true external IT vs in-house rail IT,"
        "Publish Ypto external contractor top20; dual Smals broker,"
        "src_ccrek_ypto_nmbs_ih,strong,Federal>NMBS>Ypto>IH_dispute,tick312"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

lb_rows = [
    (
        "lb_ypto_omzet_140m,Ypto NMBS IT subsidiary omzet 140.2m 2025,federal,ops,"
        "Federal>NMBS>Ypto>omzet,140170919,140170919,"
        "Strong NBB-derived: omzet 140.2m 2025 (+20pct); FTE 445; dual Smals 574m SS IT,"
        "strong,src_ypto_companyweb_nbb,NMBS passengers taxpayers,Rail digital IT services,"
        "Core rail IT vehicle; dual middleman stack with Smals,"
        "4,7.5,3,5.7,Publish L5 external contractors; dual unit cost Smals,"
        "seed,,tick312"
    ),
    (
        "lb_ypto_nmbs_ih_wedge_193m,NMBS-Ypto IH claim wedge ~193m external via Ypto,federal,ops,"
        "Federal>NMBS>Ypto>IH_wedge,192500000,296700000,"
        "Strong CoA: NMBS 296.7m claim vs staff-only IH 104.2m; residual ~192.5m external procurement via Ypto,"
        "strong,src_ccrek_ypto_nmbs_ih,Taxpayers rail,True external IT spend transparency,"
        "Classification opacity dual Smals external 206m,"
        "7,8.0,4,7.1,Open Ypto contractor top20 + procurement compliance,"
        "seed,,tick312 high mechanism"
    ),
    (
        "lb_rail_it_middleman_dual,Rail IT middleman dual Ypto+Smals+TUC,federal,ops,"
        "Federal>IT>rail_ss_dual,0,0,"
        "Strong dual map: Ypto 140m omzet + Smals ext IT >206m + TUC Rail on CoA IT vendor list; NMBS consultancy 465m 2020-22,"
        "strong,src_ccrek_ypto_nmbs_ih,Rail and SS digital users,Shared public IT capacity models,"
        "Multi-body IT middleman stack,"
        "5,8.0,4,6.3,Comparative TCO table three vehicles,"
        "seed,,tick312 dual structure"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

foi_line = (
    "gap_ypto_external_l5,Federal>NMBS>Ypto>external_contractors_L5,ypto,"
    "Top-20 external IT contractors via Ypto 2022-2025 with EUR; cash-by-year NMBS recharge to Ypto; "
    "reconcile CoA 296.7m claim vs statutory omzet ~117-140m path; preferred-supplier list residual,"
    "Entity omzet strong; NMBS IH classification wedge ~193m opacity; dual Smals external 206m,"
    "7,Ypto NV / NMBS openbaarheid / FOD Mobiliteit,,https://www.belgiantrain.be,"
    "docs/doge/foi/drafts/gap_ypto_external_l5.md,ready,2026-07-30,,,,,,"
    "cmt_ypto_omzet_path_2022_25|cmt_ypto_nmbs_coa_ih_dispute,"
    "lb_ypto_nmbs_ih_wedge_193m|lb_ypto_omzet_140m,"
    "2026-07-30T18:45:00Z,2026-07-30T18:45:00Z,tick312 draft ready human send\n"
)
with (ROOT / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_303,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; Ypto NMBS IT dual Smals; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T18:15:00Z,,Spawned tick311 after Smals CoA deepen; rq_116 SWA deferred"
)
new = (
    "rq_303,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; Ypto NMBS IT dual Smals; other FOI-adjacent). Prefer before idle.,"
    "gap_ypto_external_l5,2026-07-30T18:15:00Z,2026-07-30T18:45:00Z,"
    "tick312: Ypto omzet 140.2m 2025 FTE 445; CoA NMBS path 296.7 vs staff IH 104.2m; FOI L5; spawn rq_304"
)
if old not in text:
    raise SystemExit("rq_303 not found")
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_304,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; TUC Rail dual; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T18:45:00Z,,Spawned tick312 after Ypto; rq_116 SWA deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},312,no,"
    "Scheduler 60s. Next prio5 rq_304; rq_116 SWA deferred. FOI ready. "
    "tick312 Ypto 140m omzet + CoA IH wedge ~193m.\n",
    encoding="utf-8",
)
print("OK")

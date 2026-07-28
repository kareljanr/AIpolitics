# tick516 — CoA FAM medical accidents fund follow-up 2025 dual RIZIV
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

# entity
with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "fam,Fonds des accidents medicaux FAM,Fonds des accidents medicaux,"
        "Medical Accidents Fund (INAMI autonomous service),"
        "agency,riziv,bi,https://www.fam.be,,,INAMI autonomous service law 31 Mar 2010; indemnifies medical accidents; "
        "ops 12.5m 2024 indemnities cumul 101.1m eoy2024; tick516\n"
    )

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fam_suivi_2025,CoA Fonds des accidents medicaux suivi 2025 recommandations,"
        "docs/doge/data/raw/ccrek_fam_2025.pdf,"
        "Rekenhof AG 19 Nov 2025,2026-07-29,court_of_audit,"
        "Strong tick516: 11/24 rec done 12 in progress 1 not; backlog 2445->989; indemn cumul 101.1m; "
        "ops 12.5m 2024 ~16500/dossier; dual RIZIV; tick516\n"
    )
    f.write(
        "src_dual_fam_riziv_tick516,Dual FAM medical accident fund + RIZIV healthcare stack,"
        "docs/doge/data/raw/ccrek_fam_2025.pdf,"
        "DOGE synthesis CoA FAM + prior RIZIV,2026-07-29,synthesis,"
        "Strong dual: FAM ops 12.5m + indemn cumul 101m under RIZIV vs healthcare 43.9bn; tick516\n"
    )

buds = [
    "bud_fam_indemn_cumul_101m_2024,fam,2024,101100000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM cumulative indemnities paid eoy2024 101.1m (was 16.3m eoy2018); tick516",
    "bud_fam_indemn_cumul_16m_2018,fam,2018,16300000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM cumulative indemnities eoy2018 16.3m; tick516",
    "bud_fam_indemn_annual_12_4m_2023,fam,2023,12400000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM annual indemnities 12.4m 2023 (was 6.4m 2018 class); tick516",
    "bud_fam_indemn_annual_6_4m_2018,fam,2018,6400000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM annual indemnities 6.4m 2018 class; tick516",
    "bud_fam_ops_cost_12_5m_2024,fam,2024,12500000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM operating costs excl indemnities 12.5m 2024 (590 opinions 681 closed); tick516",
    "bud_fam_cost_per_dossier_16500_2024,fam,2024,16500,,,derived,src_ccrek_fam_suivi_2025,medium,CoA crude cost/dossier ~16500 (12.5m / avg 760 closed 2021-24); no cost accounting; amount is EUR not m; tick516",
    "bud_fam_backlog_open_989_2024,fam,2024,989,,,outturn,src_ccrek_fam_suivi_2025,strong,Open dossiers eoy2024 989 (was 2445 eoy2019 1066 eoy2023); amount stores count; FIX remove",
]
# Fix: don't store counts as euros - use separate note budgets carefully
# For backlog use amount_eur as count is wrong practice - better only commitments JSON
buds = [b for b in buds if "bud_fam_backlog" not in b and "bud_fam_cost_per_dossier" not in b]
buds += [
    "bud_fam_taskforce_closed_1249_2023,fam,2023,0,,,outturn,src_ccrek_fam_suivi_2025,strong,Task force treated 1249 dossiers by Oct2023 of which 83pct closed with opinion; amount 0 count in notes; tick516",
    "bud_fam_new_dossiers_632_2024,fam,2024,0,,,outturn,src_ccrek_fam_suivi_2025,strong,New dossier openings 632 in 2024; amount 0 count in cmt; tick516",
    "bud_fam_opinions_590_2024,fam,2024,0,,,outturn,src_ccrek_fam_suivi_2025,strong,Opinions issued 590 in 2024 (651 in 2023 517 in 2018); tick516",
    "bud_fam_closed_681_2024,fam,2024,0,,,outturn,src_ccrek_fam_suivi_2025,strong,Dossiers closed 681 in 2024 (735 in 2023 616 in 2018); tick516",
    "bud_fam_staff_cadre_62,fam,2024,0,,,outturn,src_ccrek_fam_suivi_2025,strong,Staff cadre 62 persons after reintegration task force into base team; tick516",
    "bud_dual_fam_riziv_2024,gg_belgium,2024,12500000,,,derived,src_dual_fam_riziv_tick516,strong,Dual FAM ops 12.5m under RIZIV healthcare stack; tick516",
]
# Clean zero-count noise rows - keep only real euro rows + one dual
buds = [
    "bud_fam_indemn_cumul_101m_2024,fam,2024,101100000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM cumulative indemnities paid eoy2024 101.1m (was 16.3m eoy2018); tick516",
    "bud_fam_indemn_cumul_16m_2018,fam,2018,16300000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM cumulative indemnities eoy2018 16.3m; tick516",
    "bud_fam_indemn_annual_12_4m_2023,fam,2023,12400000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM annual indemnities 12.4m 2023 (was 6.4m 2018 class); tick516",
    "bud_fam_indemn_annual_6_4m_2018,fam,2018,6400000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM annual indemnities 6.4m 2018 class; tick516",
    "bud_fam_ops_cost_12_5m_2024,fam,2024,12500000,,,outturn,src_ccrek_fam_suivi_2025,strong,FAM operating costs excl indemnities 12.5m 2024 (590 opinions 681 closed; ~16500/dossier crude); tick516",
    "bud_fam_ops_plus_indemn_class_2024,fam,2024,24900000,,,derived,src_ccrek_fam_suivi_2025,medium,Illustrative 2024 stack ops 12.5 + annual indemn class ~12.4 prior year path; not exact 2024 annual indemn; tick516",
    "bud_dual_fam_riziv_2024,gg_belgium,2024,12500000,,,derived,src_dual_fam_riziv_tick516,strong,Dual FAM ops 12.5m under RIZIV healthcare stack; tick516",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_fam_indemn_ops_2024,FAM medical accidents indemnities + ops CoA follow-up 2025,"
        "fam,Victims care providers insurers,"
        "CoA FAM suivi AG 19 Nov 2025 + law 31 Mar 2010,"
        "2010-03-31,2018,2024,101100000,"
        '"{""indemn_cumul_2018_m"":16.3,""indemn_cumul_2024_m"":101.1,'
        '""indemn_annual_2018_m"":6.4,""indemn_annual_2023_m"":12.4,'
        '""ops_2024_m"":12.5,""cost_per_dossier_eur"":16500,'
        '""open_2019"":2445,""open_2023"":1066,""open_2024"":989,'
        '""taskforce_treated"":1249,""taskforce_closed_pct"":83,'
        '""new_2024"":632,""opinions_2024"":590,""closed_2024"":681,'
        '""p80_months_2019"":31.6,""p80_months_2022"":13.2,'
        '""staff_n"":62,""rec_done"":11,""rec_progress"":12,""rec_not"":1,'
        '""note"":""Strong CoA; 9/10 victims still avoid procedure historically; prevention weak""}",'
        "0,active,docs/doge/data/raw/ccrek_fam_2025.pdf,"
        "Timely victim indemnification,Law reform + cost accounting FOI,"
        "src_ccrek_fam_suivi_2025,strong,Federal>RIZIV>FAM,tick516"
    ),
    (
        "cmt_fam_reco_status_2025,FAM 24 CoA recommendations implementation status 2025,"
        "fam,FAM INAMI minister,"
        "CoA FAM suivi 2025,"
        "2025-11-19,2020,2025,0,"
        '"{""total_rec"":24,""done"":11,""in_progress"":12,""not_done"":1,'
        '""law_wg_list_due"":""2026-12-31"",""law_wg_results_due"":""2027-02-28"",'
        '""coalition_optim"":true,'
        '""note"":""Strong CoA declaration-based follow-up; no full re-audit""}",'
        "0,active,docs/doge/data/raw/ccrek_fam_2025.pdf,"
        "Complete reform of fund role,Prevention mission FOI,"
        "src_ccrek_fam_suivi_2025,strong,Federal>FAM>recommendations,tick516"
    ),
    (
        "cmt_dual_fam_riziv,Dual FAM fund under RIZIV healthcare mega-stack,"
        "gg_belgium,Patients victims,"
        "CoA FAM + prior RIZIV dual,"
        "2025-11-19,2024,2024,12500000,"
        '"{""fam_ops_m"":12.5,""fam_indemn_cumul_m"":101.1,""riziv_healthcare_bn"":43.9,'
        '""note"":""not additive pure TE; dual health governance""}",'
        "0,active,docs/doge/data/raw/ccrek_fam_2025.pdf,"
        "Map residual health L5 funds,Role reform FOI,"
        "src_dual_fam_riziv_tick516,strong,BE>dual>FAM_RIZIV,tick516"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_fam_indemn_cumul_101m,FAM cumulative indemnities 101.1m eoy2024,federal,ops,Federal>RIZIV>FAM>indemnities,12400000,101100000,Strong CoA: cumul 101.1m eoy2024 from 16.3m eoy2018; annual path 6.4->12.4m,strong,src_ccrek_fam_suivi_2025,Victims,Medical accident compensation,Core victim payments,3.0,5.5,4,4.45,Keep tracking FOI,seed,,tick516",
    "lb_fam_ops_12_5m_2024,FAM operating costs 12.5m 2024 excl indemnities,federal,ops,Federal>RIZIV>FAM>ops,12500000,12500000,Strong CoA: 12.5m ops for 590 opinions 681 closed; ~16500/dossier crude; was 12k/open 2020 audit,strong,src_ccrek_fam_suivi_2025,Taxpayers victims,Fund administration,High unit cost vs throughput,6.5,5.5,4,5.95,Cost accounting FOI,seed,,tick516",
    "lb_fam_backlog_cleared,FAM backlog 2445 to 989 open dossiers,federal,ops,Federal>RIZIV>FAM>backlog,0,0,Strong CoA: open 2445 eoy2019 -> 989 eoy2024 via task force; p80 months 31.6->13.2,strong,src_ccrek_fam_suivi_2025,Victims,Case backlog reduction,Partial success,4.0,4.0,3,4.1,Watch phase3 delays FOI,seed,,tick516",
    "lb_fam_reco_half_done,FAM CoA recs 11 done 12 progress 1 not,federal,ops,Federal>RIZIV>FAM>recommendations,0,0,Strong CoA follow-up: 11/24 done; prevention and role reform incomplete; law WG 2026-27,strong,src_ccrek_fam_suivi_2025,Parliament,Reform follow-through,Governance incomplete,6.0,4.0,4,5.0,Finish recs FOI,seed,,tick516",
    "lb_fam_low_uptake,FAM historically ~9/10 victims avoid procedure,federal,ops,Federal>RIZIV>FAM>uptake,0,101100000,Strong CoA 2020 baseline still relevant: slow process low indemn probability; raison d'etre questioned,strong,src_ccrek_fam_suivi_2025,Victims,Access to medical accident remedy,Design failure risk,7.5,5.5,6,6.45,Role reform FOI,seed,,tick516",
    "lb_dual_fam_riziv,Dual FAM 12.5m ops under RIZIV 43.9bn healthcare,multi,ops,BE>dual>FAM_RIZIV,12500000,12500000,Strong dual CoA FAM + prior RIZIV,strong,src_dual_fam_riziv_tick516,Patients,Dual residual health L5,Micro vs mega,4.0,5.5,4,4.85,Map residual funds FOI,seed,,tick516",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_fam_cost_role_l5,Federal>RIZIV>FAM>cost_role_L5,fam,"
    "Cost accounting by dossier phase 2023-2025; annual indemnity cash series 2019-2025; "
    "legal recovery costs series; prevention budget and outputs; working group law reform list "
    "due 31 Dec 2026; evaluation of opinions below gravity threshold where FAM does not pay,"
    "CoA FAM 2025: ops 12.5m ~16500/dossier crude; 9/10 uptake problem; role reform open,6,"
    "FAM / INAMI / SPF Santé,info@fam.be,"
    ",docs/doge/foi/drafts/gap_fam_cost_role_l5.md,"
    "ready,2026-07-29,,,,,cmt_fam_indemn_ops_2024,"
    "lb_fam_ops_12_5m_2024|lb_fam_low_uptake,"
    "2026-07-29T02:00:00Z,2026-07-29T02:00:00Z,"
    "tick516: CoA FAM suivi 2025; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_507,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T01:40:00Z,,Spawned tick515 after CoA BRU budget; rq_116 deferred"
)
new = (
    "rq_507,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_fam_cost_role_l5,"
    "2026-07-29T01:40:00Z,2026-07-29T02:00:00Z,"
    "tick516: CoA FAM medical accidents ops 12.5m indemn 101m dual RIZIV; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_507 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_508,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T02:00:00Z,,Spawned tick516 after CoA FAM; progress@520 soon; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T02:00:00Z,rq_507,516,no,"
    "Tick516 CoA FAM ops 12.5m indemn cumul 101m dual RIZIV; next prio5 rq_508; progress@520; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick516 OK")

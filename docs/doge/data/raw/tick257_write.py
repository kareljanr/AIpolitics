# tick 257 — rq_248 FIT dual AWEX package BO2026 + JR2025 outturn
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T15:30:00Z"
tick = 257
unit = "rq_248"

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_bbt_fit_sp_2026,DKBUZA FIT BBT presentation 2026 Programma SP Internationaal Ondernemen,"
        "docs/doge/data/raw/vl_bbt_dkbuza_fit_2026.pdf,Vlaams Parlement pfile 2240989 Diependaele,"
        "2026-07-29,budget,"
        "FIT werkingsdotatie 52.713m VAK/VEK + subsidiedotatie 10.642m VAK / 10.429m VEK; "
        "Expo Osaka -800k; dual AWEX 76.8m hub 46.2m; tick257\n"
    )
    f.write(
        "src_fit_jaarrekening_2025,FIT Vlaams Agentschap Internationaal Ondernemen jaarrekening 2025,"
        "docs/doge/data/raw/fit_jaarrekening_2025.pdf,Vlaams Parlement pfile 2321600 / DFB repertorium,"
        "2026-07-29,agency,"
        "Bedrijfsopbrengsten 71.867m 2025 (70.314m 2024); bedrijfskosten 70.948m; "
        "bezoldigingen 37.800m; andere opbrengsten 67.214m; dual AWEX; tick257\n"
    )
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
lines = [L for L in ent_path.read_text(encoding="utf-8").splitlines() if L.strip()]
out = []
for L in lines:
    if L.startswith("fit_flanders,"):
        L = (
            "fit_flanders,Flanders Investment and Trade FIT,Flanders Investment and Trade,"
            "Flemish export and FDI agency,parastatal,vlaanderen_gov,nl,"
            "https://www.flandersinvestmentandtrade.com,,,"
            "BO2026 werkings 52.713m + subsidie ~10.4m; JR2025 opbrengsten 71.867m bezold 37.8m; "
            "dual AWEX 76.8m hub 46.2m; tick257"
        )
    if L.startswith("awex,") and "tick257" not in L:
        L = L.replace("tick254", "tick254; dual FIT 52.7+10.4m BO2026 filled tick257")
    if L.startswith("hub_brussels,") and "tick257" not in L:
        L = L.rstrip() + "; dual FIT filled tick257"
    out.append(L)
with open(ent_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out) + "\n")
print("entities ok")

# --- budgets ---
bud = root / "docs/doge/data/budgets.csv"
rows = [
    "bud_fit_werkingsdotatie_bo2026,fit_flanders,2026,52713000,,,budgeted,src_vl_bbt_fit_sp_2026,strong,BBT SP: werkingsdotatie FIT 52.713m VAK=VEK 2026; -800k Expo Osaka vs prior",
    "bud_fit_subsidiedotatie_vak_bo2026,fit_flanders,2026,10642000,,,budgeted,src_vl_bbt_fit_sp_2026,strong,BBT SP: subsidiedotatie VAK 10.642m 2026 (bedrijven + partner org)",
    "bud_fit_subsidiedotatie_vek_bo2026,fit_flanders,2026,10429000,,,budgeted,src_vl_bbt_fit_sp_2026,strong,BBT SP: subsidiedotatie VEK 10.429m 2026; -1.089m uitrustingsgoederen schrapping",
    "bud_fit_package_vak_bo2026,fit_flanders,2026,63355000,,,budgeted,src_vl_bbt_fit_sp_2026,strong,Derived: werkings 52.713 + subsidie VAK 10.642 = 63.355m package VAK",
    "bud_fit_package_vek_bo2026,fit_flanders,2026,63142000,,,budgeted,src_vl_bbt_fit_sp_2026,strong,Derived: werkings 52.713 + subsidie VEK 10.429 = 63.142m package VEK; dual AWEX 76.8m",
    "bud_fit_opbrengsten_2025,fit_flanders,2025,71867000,,,outturn,src_fit_jaarrekening_2025,strong,JR2025: bedrijfsopbrengsten 71.867m (kEUR table x1000); was 70.314m 2024",
    "bud_fit_opbrengsten_2024,fit_flanders,2024,70314000,,,outturn,src_fit_jaarrekening_2025,strong,JR2025 prior year bedrijfsopbrengsten 70.314m",
    "bud_fit_andere_opbrengsten_2025,fit_flanders,2025,67214000,,,outturn,src_fit_jaarrekening_2025,strong,Andere bedrijfsopbrengsten 67.214m (mainly VL toelage class)",
    "bud_fit_omzet_2025,fit_flanders,2025,4401000,,,outturn,src_fit_jaarrekening_2025,strong,Omzet 4.401m 2025",
    "bud_fit_bedrijfskosten_2025,fit_flanders,2025,70948000,,,outturn,src_fit_jaarrekening_2025,strong,Bedrijfskosten 70.948m 2025 (was 76.070m 2024)",
    "bud_fit_bedrijfskosten_2024,fit_flanders,2024,76070000,,,outturn,src_fit_jaarrekening_2025,strong,Bedrijfskosten 76.070m 2024",
    "bud_fit_bezoldigingen_2025,fit_flanders,2025,37800000,,,outturn,src_fit_jaarrekening_2025,strong,Bezoldigingen sociale lasten pensioenen 37.800m 2025 (~53pct of costs)",
    "bud_fit_bezoldigingen_2024,fit_flanders,2024,37113000,,,outturn,src_fit_jaarrekening_2025,strong,Bezoldigingen 37.113m 2024",
    "bud_fit_diensten_2025,fit_flanders,2025,20695000,,,outturn,src_fit_jaarrekening_2025,strong,Diensten en diverse goederen 20.695m 2025",
    "bud_fit_andere_kosten_2025,fit_flanders,2025,11733000,,,outturn,src_fit_jaarrekening_2025,strong,Andere bedrijfskosten 11.733m 2025",
]
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(r + "\n")
print("budgets", len(rows))

# --- commitments ---
cmt = root / "docs/doge/data/commitments.csv"
cash = (
    '{"werkings_bo2026": 52713000, "subsidie_vak_2026": 10642000, "subsidie_vek_2026": 10429000, '
    '"package_vak_2026": 63355000, "package_vek_2026": 63142000, '
    '"opbrengsten_2025": 71867000, "opbrengsten_2024": 70314000, '
    '"kosten_2025": 70948000, "kosten_2024": 76070000, '
    '"bezold_2025": 37800000, "omzet_2025": 4401000, '
    '"note": "Dual AWEX package 76.843m 2026 vs FIT package VEK 63.142m; institutional outturn ~72m > VL toelage"}'
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_fit_budget_2025_26,FIT Flanders dual AWEX export-investment agency package,"
        "fit_flanders,Flemish exporters FDI attraction network abroad,"
        "Oprichtingsdecreet 7 May 2004; BBT SP 2026; JR2025,"
        f"2025-01-01,2025,2026,63142000,\"{cash}\",0,active,"
        "docs/doge/data/raw/vl_bbt_dkbuza_fit_2026.pdf,"
        "Export promotion and foreign investment attraction Flanders,"
        "L5 subsidy beneficiary list residual; dual unit-cost vs AWEX/hub,"
        "src_vl_bbt_fit_sp_2026,strong,Vlaanderen>Buitenland>FIT,"
        "tick257 closes gap_fit totals; L5 residual optional\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_fit_package_63_1m,FIT package VEK 63.1m BO2026 dual AWEX export,Flanders,ops,Vlaanderen>FIT>package,63142000,63142000,Strong BBT SP: werkings 52.713 + subsidie VEK 10.429 = 63.142m; dual AWEX 76.8m hub 46.2m,strong,src_vl_bbt_fit_sp_2026,Flemish exporters investors,Export and FDI agency,Core dual export stack; not pure waste,3,7.0,4,5.75,Publish triple matrix AWEX+FIT+hub unit-cost,seed,,tick257",
    "lb_fit_jr_opbrengsten_71_9m,FIT institutional opbrengsten 71.9m 2025,Flanders,ops,Vlaanderen>FIT>opbrengsten,71867000,71867000,Strong JR2025: bedrijfsopbrengsten 71.867m (andere 67.214 + omzet 4.401); kosten 70.948; dual AWEX,strong,src_fit_jaarrekening_2025,Flemish exporters investors,Agency full institutional revenue,Outturn > BO toelage package; dual scale vs AWEX 76.8m,3,7.0,4,5.75,Open L5 subsidy awards register,seed,,tick257",
    "lb_fit_bezold_37_8m,FIT bezoldigingen 37.8m 2025,Flanders,ops,Vlaanderen>FIT>personnel,37800000,37800000,Strong JR: bezold 37.800m of kosten 70.948m (~53pct); dual hub remun 31.9m,strong,src_fit_jaarrekening_2025,Agency staff,Wage bill export agency,High wage share dual agencies,3,6.5,4,5.35,Publish FTE dual unit-cost,seed,,tick257",
    "lb_export_triple_awex_fit_hub_filled,Export triple AWEX 76.8 FIT 63.1 hub 46.2,Belgium,ops,BE>Export>triple_AWEX_FIT_hub_filled,0,0,Strong triple filled: AWEX 76.843m 2026 + FIT package VEK 63.142m BO2026 + hub.brussels 46.166m 2024; years differ not additive; ACE 0.438m WAL,strong,src_vl_bbt_fit_sp_2026,Exporters BE regional,Regional triple export promotion post-federalisation,Three regional export agencies + federal ACE,4,8.5,4,6.55,L5 mission grants residual FOI optional,seed,,tick257 triple not additive",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb", len(lb_rows))

# --- foi_queue update gap_fit ---
foi = root / "docs/doge/data/foi_queue.csv"
text = foi.read_text(encoding="utf-8")
lines = text.splitlines()
out_foi = []
for L in lines:
    if L.startswith("gap_fit_budget_2026,"):
        # mark answered for totals; note L5 residual optional
        parts = L.split(",")
        # status is field index - better replace known substrings
        L = L.replace(",ready,2026-07-29,,,,,", ",answered,2026-07-29,,2026-07-29,tick257 BBT SP werkings 52.713m + subsidie VAK/VEK 10.642/10.429; JR2025 opbrengsten 71.867m; L5 beneficiary residual optional,")
        if "tick257" not in L:
            L = L.rstrip() + " | tick257 totals filled public; L5 optional"
        # fix if double notes
    out_foi.append(L)
with open(foi, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out_foi) + "\n")
print("foi updated")

# optional residual FOI for L5 only - light priority
with open(foi, "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_fit_l5_subsidies,Vlaanderen>FIT>L5_subsidie_begunstigden,fit_flanders,"
        "Top L5 FIT subsidiedotatie awards/begunstigden 2024-2026 with amounts "
        "(package totals now public: werkings 52.713 + subsidie ~10.4m),"
        "Totals filled tick257; dual unit-cost needs end-receiver transparency under 10.4m subsidy envelope,4,"
        "Vlaamse overheid Team Openbaarheid / FIT,openbaarheid@vlaanderen.be,"
        "Havenlaan 88 bus 20 1000 Brussel,"
        "docs/doge/foi/drafts/gap_fit_l5_subsidies.md,ready,2026-07-29,,,,,"
        "cmt_fit_budget_2025_26,lb_fit_package_63_1m,"
        f"{now},{now},tick257 residual L5 after totals filled; human send optional\n"
    )
print("foi l5 residual")

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_248,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "other FOI-adjacent after tourism triple).,,2026-07-29T15:00:00Z,,"
    "Spawned tick256 after VISITWallonia 15.4m dual tourism; rq_116 SWA deferred"
)
new = (
    "rq_248,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "other FOI-adjacent after tourism triple).,gap_fit_l5_subsidies,"
    "2026-07-29T15:00:00Z,2026-07-29T15:30:00Z,"
    "tick257: FIT BO2026 package VEK 63.142m (werk 52.713+sub 10.429); JR2025 opbrengsten 71.867m; dual AWEX; spawn rq_249"
)
if old not in rq:
    raise SystemExit("rq_248 not found")
rq = rq.replace(old, new)
if "rq_249," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_249,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent after FIT fill).,,"
        "2026-07-29T15:30:00Z,,"
        "Spawned tick257 after FIT 63.1m dual AWEX; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
(root / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next prio5 rq_249; rq_116 SWA deferred. FOI ready human send. "
    "tick257 FIT package 63.1m dual AWEX hub export triple filled.\n",
    encoding="utf-8",
)
print("DONE", tick)

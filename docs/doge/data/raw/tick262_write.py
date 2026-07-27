# tick 262 — rq_253 PMV jaarrekening 2025 dual WE holding
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T18:00:00Z"
tick = 262
unit = "rq_253"

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_pmv_jr_2025,PMV jaarrekening 2025 statutory balance P&L kEUR,"
        "docs/doge/data/raw/pmv_jaarrekening_2025.pdf,Vlaams Parlement pfile 2321639 / DFB repertorium,"
        "2026-07-29,agency,"
        "Assets 4.236bn (was 1.626bn); equity 4.180bn; geplaatst kap 4.329bn; fin FA 4.031bn; "
        "bezold 21.101m; result 17.234m; dual WE ~4.98bn equity; BAC stake path; tick262\n"
    )
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
lines = [L for L in ent_path.read_text(encoding="utf-8").splitlines() if L.strip()]
out = []
for L in lines:
    if L.startswith("pmv,"):
        L = (
            "pmv,Participatiemaatschappij Vlaanderen PMV,Participatiemaatschappij Vlaanderen,"
            "Flanders Participation Company PMV,parastatal,vlaanderen_gov,nl,https://www.pmv.eu,,,"
            "JR2025 statutory assets 4.236bn equity 4.180bn; dual WE 4.98bn; BAC stake jump; tick262"
        )
    out.append(L)
with open(ent_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out) + "\n")
print("entities ok")

# --- budgets (kEUR * 1000) ---
bud = root / "docs/doge/data/budgets.csv"
rows = [
    "bud_pmv_assets_2025,pmv,2025,4236105000,,,outturn,src_pmv_jr_2025,strong,JR2025 statutory total assets 4.236105bn (kEUR table x1000); was 1.626bn 2024",
    "bud_pmv_assets_2024_stat,pmv,2024,1626097000,,,outturn,src_pmv_jr_2025,strong,JR2025 prior year statutory assets 1.626097bn",
    "bud_pmv_equity_2025,pmv,2025,4180096000,,,outturn,src_pmv_jr_2025,strong,Eigen vermogen 4.180096bn end-2025 (was 1.613bn)",
    "bud_pmv_equity_2024_stat,pmv,2024,1613027000,,,outturn,src_pmv_jr_2025,strong,Eigen vermogen 1.613027bn end-2024 statutory",
    "bud_pmv_geplaatst_kap_2025,pmv,2025,4329462000,,,outturn,src_pmv_jr_2025,strong,Geplaatst kapitaal 4.329462bn (niet-opgevraagd 716.042m)",
    "bud_pmv_fin_fa_2025,pmv,2025,4031083000,,,outturn,src_pmv_jr_2025,strong,Financiele vaste activa 4.031083bn (was 1.436bn); BAC/deelnemingen jump",
    "bud_pmv_deelnemingen_verbonden_2025,pmv,2025,3190997000,,,outturn,src_pmv_jr_2025,strong,Deelnemingen verbonden ondernemingen 3.190997bn (was 637.108m)",
    "bud_pmv_opbrengsten_2025,pmv,2025,18758000,,,outturn,src_pmv_jr_2025,strong,Bedrijfsopbrengsten 18.758m 2025 statutory",
    "bud_pmv_opbrengsten_2024_stat,pmv,2024,13271000,,,outturn,src_pmv_jr_2025,strong,Bedrijfsopbrengsten 13.271m 2024 statutory",
    "bud_pmv_kosten_2025,pmv,2025,35332000,,,outturn,src_pmv_jr_2025,strong,Bedrijfskosten 35.332m 2025",
    "bud_pmv_bezold_2025,pmv,2025,21101000,,,outturn,src_pmv_jr_2025,strong,Bezoldigingen 21.101m 2025 (was 19.460m)",
    "bud_pmv_bezold_2024_stat,pmv,2024,19460000,,,outturn,src_pmv_jr_2025,strong,Bezoldigingen 19.460m 2024 statutory",
    "bud_pmv_result_2025,pmv,2025,17234000,,,outturn,src_pmv_jr_2025,strong,Resultaat boekjaar 17.234m 2025 (was 27.151m)",
    "bud_pmv_result_2024_stat,pmv,2024,27151000,,,outturn,src_pmv_jr_2025,strong,Resultaat 27.151m 2024 statutory",
    "bud_pmv_dividend_2025,pmv,2025,3800000,,,outturn,src_pmv_jr_2025,strong,Dividend/vergoeding kapitaal 3.8m 2025 (flat vs 2024)",
    "bud_pmv_fin_opbrengsten_2025,pmv,2025,88336000,,,outturn,src_pmv_jr_2025,strong,Financiele opbrengsten 88.336m 2025 (incl non-recurrent 36.704m)",
]
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(r + "\n")
print("budgets", len(rows))

# --- commitments ---
cmt = root / "docs/doge/data/commitments.csv"
cash = (
    '{"assets_2025": 4236105000, "assets_2024": 1626097000, "equity_2025": 4180096000, '
    '"geplaatst_kap_2025": 4329462000, "fin_fa_2025": 4031083000, '
    '"deelnemingen_verbonden_2025": 3190997000, "bezold_2025": 21101000, '
    '"result_2025": 17234000, "dividend_2025": 3800000, '
    '"note": "Statutory PMV not full group consol; BAC stake drives jump; dual WE equity ~4.98bn 2025; '
    "SFPIM federal 11.7bn class\"}"
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_pmv_jr_2025,PMV Flanders holding statutory 2025 dual WE SFPIM,"
        "pmv,Flemish companies SMEs biotech infra BAC Aquafin,PMV decree + VL capital; JR2025,"
        f"2025-01-01,2024,2025,4236105000,\"{cash}\",0,active,"
        "docs/doge/data/raw/pmv_jaarrekening_2025.pdf,"
        "Strategic equity loans guarantees Flanders economy,"
        "Publish L5 top portfolio EUR; dual WE unit-cost; open BAC stake cost path,"
        "src_pmv_jr_2025,strong,Vlaanderen>PMV,"
        "tick262 dual WE holdings comparable scale\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_pmv_assets_4_24bn,PMV statutory assets 4.24bn 2025 dual WE,Flanders,ops,Vlaanderen>PMV>assets,4236105000,4236105000,Strong JR2025: assets 4.236bn (was 1.626bn); BAC/deelnemingen jump; dual WE equity ~4.98bn,strong,src_pmv_jr_2025,Flemish economy investees,Regional investment holding stock,Stock not annual waste; dual holding opacity L5,3,9.5,5,6.95,Open L5 top stakes EUR matrix dual WE SFPIM,seed,,tick262 stock not flow",
    "lb_pmv_bezold_21_1m,PMV bezoldigingen 21.1m 2025,Flanders,ops,Vlaanderen>PMV>personnel,21101000,21101000,Strong JR: bezold 21.101m 2025 (19.460m 2024); dual WE FTE 178 class,strong,src_pmv_jr_2025,PMV staff,Wage bill investment holding,Agency opex dual,3,5.5,3,4.7,Compare dual WE staff costs,seed,,tick262",
    "lb_holding_dual_pmv_we,Regional holdings dual PMV 4.24bn vs WE 4.98bn equity,Belgium,ops,BE>Holdings>dual_PMV_WE,0,0,Strong dual: PMV statutory assets 4.236bn 2025 + WE equity ~4.981bn 2025; SFPIM federal 11.7bn third layer; L5 stakes residual,strong,src_pmv_jr_2025,Regional SMEs strategic stakes,Post-federalisation regional investment holdings,Institutional dual equity tools + federal SFPIM,4,9.0,5,6.75,L5 portfolio transparency both regions,seed,,tick262 dual not additive",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb ok")

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_253,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; APEFE budget if public; "
    "other FOI-adjacent after Enabel).,,2026-07-29T17:30:00Z,,"
    "Spawned tick261 after Enabel 435.6m dual APEFE; rq_116 SWA deferred"
)
new = (
    "rq_253,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; APEFE budget if public; "
    "other FOI-adjacent after Enabel).,,"
    "2026-07-29T17:30:00Z,2026-07-29T18:00:00Z,"
    "tick262: PMV JR2025 assets 4.236bn equity 4.180bn dual WE; spawn rq_254"
)
if old not in rq:
    raise SystemExit("rq_253 not found")
rq = rq.replace(old, new)
if "rq_254," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_254,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; APEFE budget if public; "
        "other FOI-adjacent after PMV).,,2026-07-29T18:00:00Z,,"
        "Spawned tick262 after PMV 4.24bn dual WE; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
(root / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next prio5 rq_254; rq_116 SWA deferred. FOI ready human send. "
    "tick262 PMV 4.24bn dual WE holdings.\n",
    encoding="utf-8",
)
print("DONE", tick)

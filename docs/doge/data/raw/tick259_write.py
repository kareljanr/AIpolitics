# tick 259 — rq_250 WAL WBI dotation 30.098m closes gap_wbi_wal_contribution
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T16:30:00Z"
tick = 259
unit = "rq_250"

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_wal_bud27_wbi_dot_2026,Parlement wallon bud27 Dolimont DF019.003 WBI dotation 30.098m 2026,"
        "docs/doge/data/raw/wal_bud27_2026.pdf,Parlement wallon BUDGET bud27 2025-2026,"
        "2026-07-29,parliament,"
        "DF 019.003 dotation WBI 30.098m 2026 (-0.600m vs 2025 = 30.698m); building EIWB1 option; dual FWB 42.945m; tick259\n"
    )
    f.write(
        "src_ccrek_rw_2025a1_wbi,Cour des comptes RW budget 2025A1 WBI -19.6m emphyteose,"
        "docs/doge/data/raw/ccrek_budget_rw_2025a1.pdf,Cour des comptes,"
        "2026-07-29,audit,"
        "WBI consolidated impact -19.6m 2025A1 mainly emphyteotic option 12.1m Sainctelette; tick259\n"
    )
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
lines = [L for L in ent_path.read_text(encoding="utf-8").splitlines() if L.strip()]
out = []
for L in lines:
    if L.startswith("wbi,"):
        L = (
            "wbi,Wallonie-Bruxelles International WBI,"
            "Wallonie-Bruxelles International,"
            "Wallonia-Brussels International (joint FWB-WAL-COCOF external relations),"
            "agency,fwb_gov,fr,https://wbi.be,,,"
            "Liq 104.2/96.4m 2024-25; FWB dot 42.945m + WAL 30.098m 2026; dual VL; tick259"
        )
    out.append(L)
with open(ent_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out) + "\n")
print("entities ok")

# --- budgets ---
bud = root / "docs/doge/data/budgets.csv"
rows = [
    "bud_wbi_wal_dot_2026,wbi,2026,30098000,,,budgeted,src_wal_bud27_wbi_dot_2026,strong,DF 019.003 Relations exterieures: WAL dotation WBI 30.098m 2026",
    "bud_wbi_wal_dot_2025,wbi,2025,30698000,,,budgeted,src_wal_bud27_wbi_dot_2026,strong,Implied: 2026 30.098 + 0.600 cut = 30.698m 2025 base (Dolimont -600k vs 2025)",
    "bud_wbi_fwb_wal_dots_sum_2026,wbi,2026,73043000,,,budgeted,src_wal_bud27_wbi_dot_2026,strong,Derived: FWB 42.945 + WAL 30.098 = 73.043m dual dots 2026; residual to total liq class own/EU/COCOF",
]
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(r + "\n")
print("budgets", len(rows))

# --- update commitment ---
cmt = root / "docs/doge/data/commitments.csv"
# append update row rather than rewrite
cash = (
    '{"liq_2024": 104237000, "liq_2025": 96448000, '
    '"fwb_dot_2026": 42945000, "wal_dot_2026": 30098000, "wal_dot_2025": 30698000, '
    '"fwb_wal_sum_2026": 73043000, '
    '"note": "WAL DF019.003 filled tick259; residual COCOF/own/EU vs total 96m; dual VL SN+FIT"}'
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_wbi_wal_fwb_dots_2026,WBI dual FWB+WAL financing matrix 2026,"
        "wbi,WBI network FWB-WAL-COCOF,bud27 Dolimont + CdC RD26,"
        f"2025-10-01,2025,2026,73043000,\"{cash}\",0,active,"
        "docs/doge/data/raw/wal_bud27_2026.pdf,"
        "Joint external relations financing,"
        "COCOF residual; dual unit-cost vs Flanders,"
        "src_wal_bud27_wbi_dot_2026,strong,BE>WBI>FWB_WAL_dots,"
        "tick259 closes WAL FOI gap\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_wbi_wal_dot_30_1m,WAL WBI dotation 30.1m 2026 dual FWB,Wallonia,ops,Wallonie>WBI>dotation,30098000,30098000,Strong bud27 Dolimont DF019.003: 30.098m 2026 (-0.6m vs 30.698m 2025); dual FWB 42.945m sum 73.0m,strong,src_wal_bud27_wbi_dot_2026,WBI network,Regional co-finance of joint international agency,Dual FWB-WAL financing filled; not pure waste,3,6.0,3,5.1,Publish annual trilogy FWB+WAL+COCOF,seed,,tick259",
    "lb_wbi_fwb_wal_sum_73m,WBI FWB+WAL dots sum 73.0m 2026,Belgium,ops,BE>WBI>FWB_WAL_sum,73043000,73043000,Strong derived: FWB 42.945 + WAL 30.098 = 73.043m; total agency liq 96.4m 2025 residual own/COCOF/EU,strong,src_wal_bud27_wbi_dot_2026,WBI operators,Dual financing of international agency,Institutional dual FR community-region stack,4,7.0,4,5.9,Map COCOF share; dual Flanders TCO,seed,,tick259",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb ok")

# --- foi mark answered ---
foi = root / "docs/doge/data/foi_queue.csv"
text = foi.read_text(encoding="utf-8")
out_f = []
for L in text.splitlines():
    if L.startswith("gap_wbi_wal_contribution,"):
        L = L.replace(
            ",ready,2026-07-29,,,,,",
            ",answered,2026-07-29,,2026-07-29,tick259 Dolimont bud27 DF019.003 WAL 30.098m 2026 (30.698m 2025); -600k building option,",
        )
        if "tick259" not in L.split(",")[-1]:
            L = L.rstrip() + " | tick259 answered public"
    out_f.append(L)
with open(foi, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out_f) + "\n")
print("foi answered")

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_250,Continuous FOI-adjacent public hole-fill batch + progress@260 prep,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent). "
    "Note tick 260 is mandatory progress coverage % + waste top10.,,"
    "2026-07-29T16:00:00Z,,"
    "Spawned tick258 after WBI 96.4m dual intl; progress@260 in 2 ticks; rq_116 SWA deferred"
)
new = (
    "rq_250,Continuous FOI-adjacent public hole-fill batch + progress@260 prep,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent). "
    "Note tick 260 is mandatory progress coverage % + waste top10.,gap_wbi_wal_contribution,"
    "2026-07-29T16:00:00Z,2026-07-29T16:30:00Z,"
    "tick259: WAL WBI dot 30.098m 2026 FWB+WAL sum 73.0m; gap answered; spawn rq_251 progress@260 next"
)
if old not in rq:
    raise SystemExit("rq_250 not found")
rq = rq.replace(old, new)
if "rq_251," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_251,Mandatory progress@260 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
        "When ticks_completed hits 260: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
        "and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
        "2026-07-29T16:30:00Z,,"
        "Spawned tick259; progress@260 next tick mandatory\n"
    )
# also spawn continuous hole-fill after progress
if "rq_252," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_252,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills after progress@260 (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent).,,"
        "2026-07-29T16:30:00Z,,"
        "Spawned tick259 for post-progress@260; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
(root / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next **rq_251 progress@260 mandatory**; then rq_252. "
    "rq_116 SWA deferred. FOI ready human send. tick259 WAL WBI 30.1m dual filled.\n",
    encoding="utf-8",
)
print("DONE", tick)

# tick 261 — rq_252 Enabel dual APEFE development cooperation
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T17:30:00Z"
tick = 261
unit = "rq_252"

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_enabel_ar_2025_26,Enabel Activity Report 2025-26 finances volume staff,"
        "docs/doge/data/raw/enabel_activity_report_2025_26.pdf,Enabel Belgian development agency,"
        "2026-07-29,agency,"
        "Op rev 435.600m 2025 (357.090m 2024); staff costs 91.022m; staff 2369; volume path 303-435m 2021-25; "
        "dual APEFE regional; tick261\n"
    )
    f.write(
        "src_apefe_ra_2024,APEFE Rapport activites 2024 dual Enabel structure,"
        "docs/doge/data/raw/apefe_ra_2024.pdf,APEFE ASBL,"
        "2026-07-29,agency,"
        "Regional cooperation FWB-WAL-fed tutelle; staff ~20 HQ +52 abroad +6 expats; linked WBI; "
        "budget total residual FOI; tick261\n"
    )
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
lines = [L for L in ent_path.read_text(encoding="utf-8").splitlines() if L.strip()]
has_en = has_ap = False
out = []
for L in lines:
    if L.startswith("enabel,"):
        has_en = True
        L = (
            "enabel,Enabel Belgische Ontwikkelingsagentschap,Enabel Agence belge de developpement,"
            "Enabel Belgian development agency,parastatal,sec_federal,bi,https://www.enabel.be,,,"
            "Op rev 435.6m 2025 staff 2369; dual APEFE regional; EU ~40pct class partners; tick261"
        )
    if L.startswith("apefe,"):
        has_ap = True
        L = (
            "apefe,APEFE Association pour la Promotion de l Education et de la Formation a l Etranger,"
            "APEFE,APEFE Wallonia-Brussels technical cooperation ASBL,"
            "asbl,fwb_gov,fr,https://www.apefe.org,,,"
            "Dual Enabel; shared WBI AG; staff ~78; full budget FOI; tick261"
        )
    out.append(L)
if not has_en:
    out.append(
        "enabel,Enabel Belgische Ontwikkelingsagentschap,Enabel Agence belge de developpement,"
        "Enabel Belgian development agency,parastatal,sec_federal,bi,https://www.enabel.be,,,"
        "Op rev 435.6m 2025 staff 2369; dual APEFE regional; EU ~40pct class partners; tick261"
    )
if not has_ap:
    out.append(
        "apefe,APEFE Association pour la Promotion de l Education et de la Formation a l Etranger,"
        "APEFE,APEFE Wallonia-Brussels technical cooperation ASBL,"
        "asbl,fwb_gov,fr,https://www.apefe.org,,,"
        "Dual Enabel; shared WBI AG; staff ~78; full budget FOI; tick261"
    )
with open(ent_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out) + "\n")
print("entities", len(out))

# --- budgets ---
bud = root / "docs/doge/data/budgets.csv"
rows = [
    "bud_enabel_op_rev_2025,enabel,2025,435600343,,,outturn,src_enabel_ar_2025_26,strong,AR: operating revenue 435.600m 2025",
    "bud_enabel_op_rev_2024,enabel,2024,357089576,,,outturn,src_enabel_ar_2025_26,strong,AR: operating revenue 357.090m 2024",
    "bud_enabel_turnover_2025,enabel,2025,407097008,,,outturn,src_enabel_ar_2025_26,strong,Turnover 407.097m 2025",
    "bud_enabel_turnover_2024,enabel,2024,329159608,,,outturn,src_enabel_ar_2025_26,strong,Turnover 329.160m 2024",
    "bud_enabel_op_costs_2025,enabel,2025,438055645,,,outturn,src_enabel_ar_2025_26,strong,Operating costs 438.056m 2025",
    "bud_enabel_op_costs_2024,enabel,2024,363720256,,,outturn,src_enabel_ar_2025_26,strong,Operating costs 363.720m 2024",
    "bud_enabel_staff_costs_2025,enabel,2025,91021649,,,outturn,src_enabel_ar_2025_26,strong,Staff costs 91.022m 2025 (~21pct of op costs)",
    "bud_enabel_staff_costs_2024,enabel,2024,80167734,,,outturn,src_enabel_ar_2025_26,strong,Staff costs 80.168m 2024",
    "bud_enabel_volume_2021,enabel,2021,303000000,,,outturn,src_enabel_ar_2025_26,strong,Volume chart 303m 2021",
    "bud_enabel_volume_2022,enabel,2022,340000000,,,outturn,src_enabel_ar_2025_26,strong,Volume chart 340m 2022",
    "bud_enabel_volume_2023,enabel,2023,335000000,,,outturn,src_enabel_ar_2025_26,strong,Volume chart 335m 2023",
    "bud_enabel_volume_2024_chart,enabel,2024,357000000,,,outturn,src_enabel_ar_2025_26,strong,Volume chart 357m 2024 (matches op rev class)",
    "bud_enabel_volume_2025_chart,enabel,2025,435000000,,,outturn,src_enabel_ar_2025_26,strong,Volume chart +435m 2025",
    "bud_enabel_staff_headcount_2026,enabel,2026,2369,,,outturn,src_enabel_ar_2025_26,strong,Staff 2369 at 1/1/2026 path (2385 peak 2025)",
    "bud_enabel_assets_2025,enabel,2025,217367384,,,outturn,src_enabel_ar_2025_26,strong,Total assets 217.367m end-2025",
    "bud_enabel_assets_2024,enabel,2024,221899107,,,outturn,src_enabel_ar_2025_26,strong,Total assets 221.899m end-2024",
]
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(r + "\n")
print("budgets", len(rows))

# --- commitments ---
cmt = root / "docs/doge/data/commitments.csv"
cash = (
    '{"op_rev_2025": 435600343, "op_rev_2024": 357089576, "turnover_2025": 407097008, '
    '"op_costs_2025": 438055645, "staff_costs_2025": 91021649, "staff_2026": 2369, '
    '"projects_ongoing": 200, "volume_2021_25": [303,340,335,357,435], '
    '"note": "Federal development agency dual APEFE regional + WBI network; EU partner share growing; '
    'Flanders/BCR/WAL listed among financial partners"}'
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_enabel_portfolio_2024_25,Enabel federal development dual APEFE regional stack,"
        "enabel,Partner countries governments civil society private,Law 16 Nov 2017 Enabel; AR 2025-26,"
        f"2024-01-01,2024,2026,435600343,\"{cash}\",0,active,"
        "docs/doge/data/raw/enabel_activity_report_2025_26.pdf,"
        "Belgian international development cooperation implementation,"
        "FOI APEFE full budget dual unit-cost; open BE vs EU funding split annual,"
        "src_enabel_ar_2025_26,strong,Federal>Cooperation>Enabel,"
        "tick261 dual APEFE FOI residual\n"
    )
    f.write(
        "cmt_apefe_structure_2024,APEFE regional technical cooperation dual Enabel,"
        "apefe,Partner countries education training climate health,ASBL statutes; RA2024,"
        "2024-01-01,2024,2026,0,"
        "\"{\"\"hq_staff\"\": 20, \"\"abroad_staff\"\": 52, \"\"expats\"\": 6, \"\"bureaux\"\": 7, "
        "\"\"programme\"\": \"2022-2026 pluriannual\", \"\"note\"\": \"Budget total residual FOI; dual Enabel 435m\"}\","
        "0,active,docs/doge/data/raw/apefe_ra_2024.pdf,"
        "Regional technical cooperation education climate,"
        "FOI full budget multi-year FWB/WAL/DGD split,"
        "src_apefe_ra_2024,medium,FWB>Cooperation>APEFE,"
        "tick261 structure strong euros FOI\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_enabel_435_6m,Enabel operating revenue 435.6m 2025 dual APEFE,federal,ops,Federal>Cooperation>Enabel,435600343,435600343,Strong AR: op rev 435.600m 2025 (+22pct vs 357m 2024); staff costs 91.0m; dual APEFE regional smaller,strong,src_enabel_ar_2025_26,Partner countries BE diplomacy,Belgian development agency,Core ODA implementation dual regional; not pure waste,3,7.5,5,5.85,Publish BE vs EU funding split; dual APEFE TCO,seed,,tick261",
    "lb_enabel_staff_91m,Enabel staff costs 91.0m 2025,federal,ops,Federal>Enabel>personnel,91021649,91021649,Strong AR: staff costs 91.022m of op costs 438m (~21pct); headcount 2369,strong,src_enabel_ar_2025_26,Enabel staff 50 nationalities,Wage bill development agency,High headcount dual APEFE ~78,3,7.0,4,5.75,Dual unit-cost per project vs APEFE,seed,,tick261",
    "lb_devcoop_dual_enabel_apefe,Development cooperation dual Enabel 436m vs APEFE residual,Belgium,ops,BE>Development>dual_Enabel_APEFE,0,0,Strong dual: federal Enabel 435.6m 2025 vs regional APEFE structure public budget FOI; shared WBI leadership; partners include Flanders BCR WAL,strong,src_enabel_ar_2025_26,ODA beneficiaries,Federal-regional dual technical cooperation,Institutional dual ODA stack post-federalisation,4,8.0,5,6.2,FOI APEFE full budget; unit-cost dual,seed,,tick261 dual not additive",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb ok")

# --- foi APEFE budget ---
foi = root / "docs/doge/data/foi_queue.csv"
with open(foi, "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_apefe_budget_total,FWB_WAL>APEFE>budget_total,apefe,"
        "APEFE full budget recettes/depenses 2024-2026 with FWB/WAL/DGD/EU split "
        "(structure public; Enabel dual 435.6m strong),"
        "Dual development stack needs regional agency total for unit-cost vs Enabel,5,"
        "APEFE / WBI publicite administration / FWB openbaarheid,,"
        "APEFE Brussels,"
        "docs/doge/foi/drafts/gap_apefe_budget_total.md,ready,2026-07-29,,,,,"
        "cmt_apefe_structure_2024|cmt_enabel_portfolio_2024_25,lb_devcoop_dual_enabel_apefe,"
        f"{now},{now},tick261 draft ready human send; Enabel side filled\n"
    )
print("foi ok")

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_252,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after progress@260 (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent).,,"
    "2026-07-29T16:30:00Z,,"
    "Spawned tick259 for post-progress@260; rq_116 SWA deferred"
)
new = (
    "rq_252,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills after progress@260 (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent)."
    ",gap_apefe_budget_total,"
    "2026-07-29T16:30:00Z,2026-07-29T17:30:00Z,"
    "tick261: Enabel op rev 435.6m 2025 staff 91m dual APEFE FOI; spawn rq_253"
)
if old not in rq:
    raise SystemExit("rq_252 not found")
rq = rq.replace(old, new)
if "rq_253," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_253,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; APEFE budget if public; "
        "other FOI-adjacent after Enabel).,,2026-07-29T17:30:00Z,,"
        "Spawned tick261 after Enabel 435.6m dual APEFE; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
(root / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next prio5 rq_253; rq_116 SWA deferred. FOI ready human send. "
    "tick261 Enabel 435.6m dual APEFE.\n",
    encoding="utf-8",
)
print("DONE", tick)

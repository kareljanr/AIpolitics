# tick 256 — rq_247 VISITWallonia dual tourism + Tourisme Wallonie package
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T15:00:00Z"
tick = 256
unit = "rq_247"

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_wal_ep_lescrenier_tourisme_2026,Wallonie EP Lescrenier BI2026 programme 09.018 Tourisme + VISITWallonia,"
        "docs/doge/data/raw/wal_ep_lescrenier_2026.pdf,SPW Finances / Parlement wallon EP Lescrenier,"
        "2026-07-29,budget,"
        "Prog 09.018 total CE=CL 65.632m 2026 (69.868m 2025); Tourisme Wallonie 48.578m; "
        "VISITWallonia subvention 13.054m; CRAC tourisme 4.000m; dual TV/Visit.brussels; tick256\n"
    )
    f.write(
        "src_wal_bud37_visitwallonia_2026,Wallonie bud37 BA2026 OIP type3 VISITWallonia global 15.4m,"
        "docs/doge/data/raw/wal_bud37_2026.pdf,Parlement wallon BUDGET bud37 2025-2026,"
        "2026-07-29,budget,"
        "VISITWallonia depenses globales 15.4m initial 2026 no adjustment; dual TV+Visit; tick256\n"
    )
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
lines = [L for L in ent_path.read_text(encoding="utf-8").splitlines() if L.strip()]
has_vw = has_tw = False
out = []
for L in lines:
    if L.startswith("visitwallonia,") or L.startswith("wbt_visitwallonia,"):
        has_vw = True
        L = (
            "visitwallonia,VISITWallonia (ex Wallonie Belgique Tourisme WBT),"
            "VISITWallonia asbl ex-WBT,Wallonia tourism promotion agency,"
            "asbl,wallonie_gov,fr,https://visitwallonia.be,,,"
            "Subvention 13.054m + global dep 15.4m 2026; dual TV 74.8m Visit 14.9m; tick256"
        )
    if L.startswith("tourisme_wallonie,") or L.startswith("cgt_wallonie,"):
        has_tw = True
        L = (
            "tourisme_wallonie,Tourisme Wallonie (ex CGT),"
            "Tourisme Wallonie ex-Commissariat general au Tourisme,"
            "Wallonia tourism administration / development agency,"
            "agency,wallonie_gov,fr,https://www.tourismewallonie.be,,,"
            "Fonctionnement subvention 48.578m 2026; dual admin vs promo VISITWallonia; tick256"
        )
    out.append(L)
if not has_vw:
    out.append(
        "visitwallonia,VISITWallonia (ex Wallonie Belgique Tourisme WBT),"
        "VISITWallonia asbl ex-WBT,Wallonia tourism promotion agency,"
        "asbl,wallonie_gov,fr,https://visitwallonia.be,,,"
        "Subvention 13.054m + global dep 15.4m 2026; dual TV 74.8m Visit 14.9m; tick256"
    )
if not has_tw:
    out.append(
        "tourisme_wallonie,Tourisme Wallonie (ex CGT),"
        "Tourisme Wallonie ex-Commissariat general au Tourisme,"
        "Wallonia tourism administration / development agency,"
        "agency,wallonie_gov,fr,https://www.tourismewallonie.be,,,"
        "Fonctionnement subvention 48.578m 2026; dual admin vs promo VISITWallonia; tick256"
    )
# light note on toerisme_vlaanderen dual
out2 = []
for L in out:
    if L.startswith("toerisme_vlaanderen,") and "tick256" not in L:
        L = L.rstrip() + "; dual VISITWallonia 15.4m + Visit.brussels; tick256"
    if L.startswith("visit_brussels,") and "tick256" not in L:
        L = L.rstrip() + "; dual VISITWallonia 15.4m WAL; tick256"
    out2.append(L)
with open(ent_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out2) + "\n")
print("entities", len(out2))

# --- budgets ---
bud = root / "docs/doge/data/budgets.csv"
rows = [
    "bud_wal_prog_09018_tourisme_2026,wallonie_gov,2026,65632000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,EP Lescrenier prog 09.018 Tourisme CE=CL 65.632m 2026 (was 69.868m 2025)",
    "bud_wal_prog_09018_tourisme_2025,wallonie_gov,2025,69868000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,EP: prog 09.018 2025 ini CE=CL 69.868m",
    "bud_tourisme_wallonie_dot_2026,tourisme_wallonie,2026,48578000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,DF 018.003 subvention fonctionnement Tourisme Wallonie ex-CGT 48.578m CE=CL",
    "bud_tourisme_wallonie_dot_2025,tourisme_wallonie,2025,49080000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,DF 018.003 2025 ini 49.080m",
    "bud_visitwallonia_subvention_2026,visitwallonia,2026,13054000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,DF 018.007 subvention WBT-VISITWallonia fonctionnement 13.054m CE=CL",
    "bud_visitwallonia_subvention_2025,visitwallonia,2025,12934000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,DF 018.007 2025 ini 12.934m",
    "bud_visitwallonia_global_dep_2026,visitwallonia,2026,15400000,,,budgeted,src_wal_bud37_visitwallonia_2026,strong,bud37 OIP: depenses globales 15.4m initial 2026 no BA adjustment; > regional subvention 13.054m",
    "bud_wal_crac_tourisme_2026,wallonie_gov,2026,4000000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,DF 018.002 CRAC tourisme financement alternatif 4.000m (was 7.854m 2025)",
    "bud_wal_crac_tourisme_2025,wallonie_gov,2025,7854000,,,budgeted,src_wal_ep_lescrenier_tourisme_2026,strong,CRAC tourisme 2025 ini 7.854m",
]
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(r + "\n")
print("budgets", len(rows))

# --- commitments ---
cmt = root / "docs/doge/data/commitments.csv"
cash_vw = (
    '{"subvention_2026": 13054000, "subvention_2025": 12934000, "global_dep_2026": 15400000, '
    '"espace_bxl_120k": 120000, '
    '"note": "Global 15.4m > regional subvention 13.054m (own income/partners); dual TV+Visit.brussels"}'
).replace('"', '""')
cash_tw = (
    '{"dot_2026": 48578000, "dot_2025": 49080000, '
    '"note": "Admin/dev agency ex-CGT; not pure promotion; dual VISITWallonia promo 15.4m"}'
).replace('"', '""')
cash_prog = (
    '{"prog_2026": 65632000, "prog_2025": 69868000, "tw": 48578000, "vw_sub": 13054000, '
    '"crac": 4000000, "eu_ini": 0, '
    '"note": "Sum lines = 65.632m; BA reventil EU +3.037m CE not in initial"}'
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_visitwallonia_budget_2026,VISITWallonia dual tourism promo package vs Toerisme VL + visit.brussels,"
        "visitwallonia,Walloon tourism operators members MICE,Decret 27 May 2004 Code wallon Tourisme; EP Lescrenier,"
        f"2025-10-01,2025,2026,15400000,\"{cash_vw}\",0,active,"
        "docs/doge/data/raw/wal_bud37_2026.pdf,"
        "Destination promotion marketing MICE,"
        "Publish dual unit-cost exports/overnight stays vs TV and Visit.brussels full,"
        "src_wal_bud37_visitwallonia_2026,strong,Wallonie>Tourisme>VISITWallonia,"
        "tick256 triple tourism promo map\n"
    )
    f.write(
        "cmt_tourisme_wallonie_dot_2026,Tourisme Wallonie ex-CGT functioning subvention dual VISITWallonia,"
        "tourisme_wallonie,TW staff infrastructure PRW operators,Code wallon du Tourisme; EP Lescrenier,"
        f"2025-10-01,2025,2026,48578000,\"{cash_tw}\",0,active,"
        "docs/doge/data/raw/wal_ep_lescrenier_2026.pdf,"
        "Tourism admin development infrastructure,"
        "Separate promo agency VISITWallonia; dual overhead stack,"
        "src_wal_ep_lescrenier_tourisme_2026,strong,Wallonie>Tourisme>Tourisme_Wallonie,"
        "tick256 dual admin+promo\n"
    )
    f.write(
        "cmt_wal_prog_09018_tourisme_2026,Wallonie programme 09.018 Tourisme package BI2026,"
        "wallonie_gov,TW VISITWallonia CRAC EU tourism,EP Lescrenier BI2026,"
        f"2025-10-01,2025,2026,65632000,\"{cash_prog}\",0,active,"
        "docs/doge/data/raw/wal_ep_lescrenier_2026.pdf,"
        "Regional tourism policy financing,"
        "Track BA EU reventil; dual VL SQ 74.8m,"
        "src_wal_ep_lescrenier_tourisme_2026,strong,Wallonie>Tourisme>prog_09_018,"
        "tick256\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_visitwallonia_15_4m,VISITWallonia global 15.4m 2026 dual tourism promo,Wallonia,ops,Wallonie>Tourisme>VISITWallonia,15400000,15400000,Strong bud37: depenses globales 15.4m; regional subvention 13.054m EP; dual TV 74.8m Visit 14.9m partial,strong,src_wal_bud37_visitwallonia_2026,Walloon tourism SMEs visitors,Destination promotion marketing,Core dual tourism promo agency; not pure waste,3,5.5,4,4.95,Publish triple matrix TV+Visit+VW unit-cost,seed,,tick256",
    "lb_tourisme_wallonie_48_6m,Tourisme Wallonie functioning 48.6m dual promo stack,Wallonia,ops,Wallonie>Tourisme>Tourisme_Wallonie,48578000,48578000,Strong EP: DF 018.003 48.578m 2026 (49.080m 2025); admin/dev not pure promo; dual VISITWallonia 15.4m,strong,src_wal_ep_lescrenier_tourisme_2026,TW staff infrastructure operators,Tourism administration and development,Dual admin+promo institutional stack,3,6.5,4,5.35,Clarify TCO TW+VW vs Toerisme VL single agency,seed,,tick256",
    "lb_wal_prog_tourisme_65_6m,Wallonie prog 09.018 Tourisme 65.6m 2026,Wallonia,ops,Wallonie>Tourisme>prog_09_018,65632000,65632000,Strong EP: total 65.632m = TW 48.578 + VW 13.054 + CRAC 4.000; was 69.868m 2025,strong,src_wal_ep_lescrenier_tourisme_2026,Tourism sector Wallonia,Regional tourism programme,Programme envelope dual VL SQ 74.8m,3,7.0,4,5.75,Dual regional tourism programme compare,seed,,tick256",
    "lb_tourism_triple_tv_visit_vw,Tourism triple TV 74.8 Visit 14.9 VW 15.4,Belgium,ops,BE>Tourism>triple_TV_Visit_VW,0,0,Strong triple promo: Toerisme VL SQ VEK 74.8m BO2024 + Visit prog302 14.9m partial + VISITWallonia global 15.4m 2026; scopes/years differ not additive; WAL also TW admin 48.6m,strong,src_wal_bud37_visitwallonia_2026,Tourism BE regional,Regional triple tourism promotion post-federalisation,Three regional promo layers + WAL admin dual,4,8.0,5,6.2,FOI Visit full package; unit-cost overnight stays,seed,,tick256 triple not additive",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb", len(lb_rows))

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_247,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "WBT Wallonia tourism dual residual; other FOI-adjacent).,,2026-07-29T14:30:00Z,,"
    "Spawned tick255 after dual tourism TV+Visit; rq_116 SWA deferred"
)
new = (
    "rq_247,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "WBT Wallonia tourism dual residual; other FOI-adjacent).,,"
    "2026-07-29T14:30:00Z,2026-07-29T15:00:00Z,"
    "tick256: VISITWallonia global 15.4m sub 13.054m; TW 48.578m; prog 09.018 65.632m dual TV; spawn rq_248"
)
if old not in rq:
    raise SystemExit("rq_247 not found")
rq = rq.replace(old, new)
if "rq_248," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_248,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
        "other FOI-adjacent after tourism triple).,,2026-07-29T15:00:00Z,,"
        "Spawned tick256 after VISITWallonia 15.4m dual tourism; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
(root / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next prio5 rq_248; rq_116 SWA deferred. FOI ready human send. "
    "tick256 VISITWallonia 15.4m TW 48.6m dual tourism triple.\n",
    encoding="utf-8",
)
print("DONE", tick)

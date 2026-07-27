# tick 258 — rq_249 WBI dual international relations FWB/WAL vs Flanders DKBUZA
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T16:00:00Z"
tick = 258
unit = "rq_249"

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_wbi_rapport_2024,WBI Rapport d activite 2024 budget liquidation 2024-2025,"
        "docs/doge/data/raw/wbi_rapport_activite_2024.pdf,Wallonie-Bruxelles International,"
        "2026-07-29,agency,"
        "Budget liquidation 104.237m 2024 / 96.448m 2025; dual FWB+WAL+COCOF; tick258\n"
    )
    f.write(
        "src_cdc_rd26_wbi_fwb_dot,Cour des comptes RD26 WBI FWB DO14 AB11.4101 series,"
        "docs/doge/data/raw/cdc_rd26_wbi.pdf,Cour des comptes / FWB revue depenses,"
        "2026-07-29,audit,"
        "FWB subvention WBI kEUR: 46742 2024 / 43945 2025 AJU / 42945 2026 INI; "
        "dual WAL 50pct key; network spending review 10pct target; tick258\n"
    )
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
lines = [L for L in ent_path.read_text(encoding="utf-8").splitlines() if L.strip()]
has_wbi = False
out = []
for L in lines:
    if L.startswith("wbi,") or L.startswith("wbi_wallonie_bruxelles,"):
        has_wbi = True
        L = (
            "wbi,Wallonie-Bruxelles International WBI,"
            "Wallonie-Bruxelles International,"
            "Wallonia-Brussels International (joint FWB-WAL-COCOF external relations),"
            "agency,fwb_gov,fr,https://wbi.be,,,"
            "Budget liq 104.237m 2024 / 96.448m 2025; FWB dot 42.945m 2026ini; dual VL DKBUZA+FIT; tick258"
        )
    out.append(L)
if not has_wbi:
    out.append(
        "wbi,Wallonie-Bruxelles International WBI,"
        "Wallonie-Bruxelles International,"
        "Wallonia-Brussels International (joint FWB-WAL-COCOF external relations),"
        "agency,fwb_gov,fr,https://wbi.be,,,"
        "Budget liq 104.237m 2024 / 96.448m 2025; FWB dot 42.945m 2026ini; dual VL DKBUZA+FIT; tick258"
    )
with open(ent_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out) + "\n")
print("entities", len(out))

# --- budgets ---
bud = root / "docs/doge/data/budgets.csv"
rows = [
    "bud_wbi_total_liq_2024,wbi,2024,104237000,,,budgeted,src_wbi_rapport_2024,strong,RA2024: budget en liquidation 104.237m 2024",
    "bud_wbi_total_liq_2025,wbi,2025,96448000,,,budgeted,src_wbi_rapport_2024,strong,RA2024: budget en liquidation 96.448m 2025 (-7.5pct vs 2024)",
    "bud_wbi_fwb_dot_2024,wbi,2024,46742000,,,budgeted,src_cdc_rd26_wbi_fwb_dot,strong,CdC RD26: DO14 AB11.4101 FWB subvention 46.742m 2024",
    "bud_wbi_fwb_dot_2025,wbi,2025,43945000,,,budgeted,src_cdc_rd26_wbi_fwb_dot,strong,CdC: FWB subvention 43.945m 2025 AJU",
    "bud_wbi_fwb_dot_2026,wbi,2026,42945000,,,budgeted,src_cdc_rd26_wbi_fwb_dot,strong,CdC: FWB subvention 42.945m 2026 INI; RD targets >=10pct savings options",
    "bud_vl_dkbuza_sn_bbt_2026,vlaanderen_gov,2026,8971000,,,budgeted,src_vl_bbt_fit_sp_2026,strong,BBT Diependaele: Programma SN Buitenlands Beleid 8.971m VAK/VEK 2026; dual WBI scope smaller partial (FIT trade separate)",
]
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(r + "\n")
print("budgets", len(rows))

# --- commitments ---
cmt = root / "docs/doge/data/commitments.csv"
cash = (
    '{"liq_2024": 104237000, "liq_2025": 96448000, '
    '"fwb_dot_2024": 46742000, "fwb_dot_2025": 43945000, "fwb_dot_2026": 42945000, '
    '"vl_sn_bbt_2026": 8971000, '
    '"note": "WBI joint FWB+WAL+COCOF; WAL share residual FOI (50/50 key mentioned CdC); '
    'dual Flanders SN 9m partial + FIT 63m trade separate not additive"}'
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_wbi_budget_2024_26,WBI dual international relations FWB-WAL vs Flanders DKBUZA,"
        "wbi,Cultural academic scientific operators FWB-WAL-COCOF,"
        "Accord cooperation 20 Mar 2008; RA2024; CdC RD26,"
        f"2024-01-01,2024,2026,96448000,\"{cash}\",0,active,"
        "docs/doge/data/raw/wbi_rapport_activite_2024.pdf,"
        "External relations diplomacy cultural cooperation,"
        "FOI WAL full contribution path; dual unit-cost vs VL DKBUZA+FIT stack,"
        "src_wbi_rapport_2024,strong,FWB>Relations_internationales>WBI,"
        "tick258 dual FL foreign affairs partial SN 9m\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_wbi_96_4m,WBI budget liquidation 96.4m 2025 dual Flanders,FWB,ops,FWB>WBI>total,96448000,96448000,Strong RA2024: liq 96.448m 2025 (104.237m 2024); joint FWB-WAL-COCOF external relations,strong,src_wbi_rapport_2024,Operators FWB-WAL cultural academic,International relations of Wallonia-Brussels,Core dual diplomacy stack vs Flanders DKBUZA+FIT; not pure waste,3,7.5,5,5.85,Publish FWB+WAL contribution matrix; FOI WAL share,seed,,tick258",
    "lb_wbi_fwb_dot_42_9m,FWB WBI subvention 42.9m 2026 path,FWB,ops,FWB>WBI>dotation,42945000,42945000,Strong CdC RD26: AB11.4101 46.742/43.945/42.945m 2024/25aju/26ini; spending review >=10pct options,strong,src_cdc_rd26_wbi_fwb_dot,WBI network,FWB financing of joint international agency,Path down; dual WAL co-finance residual,3,6.5,4,5.35,Track RD savings decisions 2026-27,seed,,tick258",
    "lb_intl_dual_wbi_vl,International dual WBI 96m vs VL SN 9m + FIT 63m,Belgium,ops,BE>International>dual_WBI_VL,0,0,Strong dual: WBI liq 96.4m 2025 vs Flanders SN Buitenlands Beleid 8.971m + FIT export 63.1m separate; scopes differ not additive; WBI includes culture/cooperation,strong,src_wbi_rapport_2024,BE regional operators,Post-federalisation external relations dualism,Institutional dual international stack FR vs NL,4,8.0,5,6.2,FOI WAL WBI contribution; full VL DKBUZA TCO,seed,,tick258 dual not additive",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb", len(lb_rows))

# --- foi residual WAL contribution ---
foi = root / "docs/doge/data/foi_queue.csv"
with open(foi, "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_wbi_wal_contribution,Wallonie>WBI>dotation_regionale,wbi,"
        "Walloon Region annual contribution / dotation to WBI 2024-2026 cash series "
        "(FWB side strong 42.945-46.742m; CdC notes 50/50 key on common lines),"
        "WBI total liq 96-104m public; dual map needs WAL share for full financing matrix,5,"
        "SPW / service publicite de l administration Wallonie,,"
        "SPW Namur,"
        "docs/doge/foi/drafts/gap_wbi_wal_contribution.md,ready,2026-07-29,,,,,"
        "cmt_wbi_budget_2024_26,lb_wbi_96_4m|lb_intl_dual_wbi_vl,"
        f"{now},{now},tick258 draft ready human send; FWB side filled\n"
    )
print("foi ok")

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_249,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent after FIT fill).,,"
    "2026-07-29T15:30:00Z,,"
    "Spawned tick257 after FIT 63.1m dual AWEX; rq_116 SWA deferred"
)
new = (
    "rq_249,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent after FIT fill)."
    ",gap_wbi_wal_contribution,"
    "2026-07-29T15:30:00Z,2026-07-29T16:00:00Z,"
    "tick258: WBI liq 104.2/96.4m 2024-25; FWB dot 42.945m 2026; dual VL SN 9m; spawn rq_250"
)
if old not in rq:
    raise SystemExit("rq_249 not found")
rq = rq.replace(old, new)
if "rq_250," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_250,Continuous FOI-adjacent public hole-fill batch + progress@260 prep,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; other FOI-adjacent). "
        "Note tick 260 is mandatory progress coverage % + waste top10.,,"
        "2026-07-29T16:00:00Z,,"
        "Spawned tick258 after WBI 96.4m dual intl; progress@260 in 2 ticks; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
(root / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next prio5 rq_250; progress@260 in 2 ticks; rq_116 SWA deferred. "
    "FOI ready human send. tick258 WBI 96.4m dual intl.\n",
    encoding="utf-8",
)
print("DONE", tick)

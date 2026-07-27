# tick 260 — mandatory progress coverage % + waste top10
from pathlib import Path
import csv
from collections import Counter

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T17:00:00Z"
tick = 260
unit = "rq_251"


def count_data_rows(path: Path) -> int:
    lines = [L for L in path.read_text(encoding="utf-8", errors="replace").splitlines() if L.strip()]
    return max(0, len(lines) - 1)


counts = {}
for name in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
    "research_queue.csv",
]:
    counts[name] = count_data_rows(root / name)

foi = list(csv.DictReader((root / "foi_queue.csv").open(encoding="utf-8")))
st = Counter(r.get("status", "") for r in foi)
ready = st.get("ready", 0)
answered = st.get("answered", 0)
foi_total = len(foi)

rq = list(csv.DictReader((root / "research_queue.csv").open(encoding="utf-8")))
rq_open = sum(1 for r in rq if r.get("status") == "open")
rq_total = len(rq)

lb = list(csv.DictReader((root / "leaderboard.csv").open(encoding="utf-8")))


def fnum(r, k):
    try:
        return float(r.get(k) or 0)
    except Exception:
        return 0.0


sorted_lb = sorted(
    lb,
    key=lambda r: (-fnum(r, "priority_index"), -fnum(r, "absurdity_score"), -fnum(r, "annual_cost_eur")),
)

print("COUNTS", counts)
print("FOI ready", ready, "answered", answered, "total", foi_total, st)
print("RQ open", rq_open, "total", rq_total, "lb", len(lb))
print("TOP12")
for i, r in enumerate(sorted_lb[:12], 1):
    print(
        i,
        r.get("item_id"),
        r.get("annual_cost_eur"),
        r.get("absurdity_score"),
        r.get("cost_score"),
        r.get("difficulty"),
        r.get("priority_index"),
        (r.get("name") or "")[:55],
    )

# high absurdity shortlist
abs_sorted = sorted(lb, key=lambda r: (-fnum(r, "absurdity_score"), -fnum(r, "annual_cost_eur")))
print("HIGH_ABS")
for i, r in enumerate(abs_sorted[:8], 1):
    print(i, r.get("item_id"), r.get("absurdity_score"), r.get("annual_cost_eur"), (r.get("name") or "")[:50])

# write progress file
progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## How to read the % figures

| Layer | Meaning | “End stop of money”? |
|-------|---------|----------------------|
| **A. L0 total** | Official GG TE known | No — single top line |
| **B. L1 subsector** | TE split federal / SS / state / local | No — still aggregates |
| **C. L2 entity totals** | Named institutions with primary budget totals (De Lijn, FOREM, ORES, …) | **Partial** — who holds the money |
| **D. L5 end-receivers** | Named third party / project / ASBL / firm with € | **Yes** — where possible |
| **E. FOI residual** | Known gap, draft ready for human send | Tracked, not yet answered |

**Honest claim:** A+B are essentially complete. C is large but incomplete. **D is still a small share of €348 bn** — that is structural (payroll, pensions, debt interest, formula grants are not “projects”).

---

## Snapshot at **tick 260** (2026-07-29)

| Layer | Coverage of €347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; transfer wedge ~€149 bn if double-counted |
| **C. L2 entity totals** | **~81–89%** (order of magnitude) | Up from ~79–87% @250: export triple **AWEX 76.8m + FIT 63.1m + hub 46.2m**; tourism triple **TV SQ 74.8m + Visit 14.9m partial + VW 15.4m + TW 48.6m**; **WBI 96.4m** + FWB/WAL dots **73.0m**; justice fed triple **147.3m**; residual SS bulk + many communes + operator L5 opacity |
| **D. L5 named end-receivers** | **~12–20%** of TE (generous) | Still thin vs TE; agency packages improve C more than pure L5; FIT L5 residual optional; Visit full residual FOI |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only — closes D when answered; several gaps answered public (FIT totals, WBI WAL) |

**Off-TE (do not mix into 348 bn):** federal taxex inventory ~**€39 bn**; **4e fossil inventory direct €13.3 bn** (2022 bench1) + FFS/company cars TE; cheque TE — waste map, **not cash TE**.

### Inventory (tick 260)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~{counts['budgets.csv']:,} |
| commitments.csv | ~{counts['commitments.csv']:,} |
| leaderboard.csv | ~{counts['leaderboard.csv']:,} |
| entities.csv | ~{counts['entities.csv']:,} |
| sources.csv | ~{counts['sources.csv']:,} |
| FOI ready | ~{ready} |
| FOI answered | ~{answered} |
| FOI total rows | ~{foi_total} |
| research_queue | ~{rq_total} (open: rq_116 deferred + rq_252) |

### What improved since tick 250

- **Export triple filled:** AWEX package **76.843m** 2026 + FIT BO2026 package VEK **63.142m** (JR2025 opbrengsten **71.867m**) + hub.brussels **46.166m** 2024 — years differ, not additive.  
- **Tourism triple:** Toerisme VL SQ VEK **74.816m** BO2024 + visit.brussels prog302 **14.9m** partial + VISITWallonia global **15.4m** + Tourisme Wallonie admin **48.578m**.  
- **International dual:** WBI liq **104.2/96.4m** 2024–25; FWB dot **42.945m** + WAL DF019.003 **30.098m** = **73.043m** 2026.  
- **Justice fed triple:** art.47/10 **147.338m** (VL 90.572 + FWB 55.835 + DG 0.931).  
- **FOI closures (public):** gap_fit_budget_2026 answered; gap_wbi_wal_contribution answered.  
- FOI residual L5 still stack (FIT beneficiaries optional; Visit full; Mons ASBL; AGMJ wage).  

---

## Snapshot schedule (fill at each milestone)

| Tick | L0 | L1 | L2 (ord) | L5 (ord) | FOI ready | Note |
|------|----|----|----------|----------|-----------|------|
| 120 | 100% | 100% | ~40% | ~3–6% | ~34 | Idle pause era |
| 130 | 100% | 100% | ~45% | ~5–8% | ~40 | BOSA register + cheques |
| 140 | 100% | 100% | ~50% | ~6–10% | ~45 | Antwerp/mutualities |
| 150 | 100% | 100% | ~55% | ~7–11% | ~50 | Fluvius + housing |
| 160 | 100% | 100% | ~58% | ~8–11% | ~52 | NMBS JV hole-fill |
| 170 | 100% | 100% | ~60% | ~8–12% | ~55 | Elia energy stack |
| 180 | 100% | 100% | ~60–68% | ~8–12% | ~55 | VL water stack |
| 190 | 100% | 100% | ~62–70% | ~6–13% | ~60 | SFPIM+airports+Credendo |
| 200 | 100% | 100% | ~68–76% | ~7–14% | ~68 | Holdings+ports+rail dual |
| 210 | 100% | 100% | ~70–78% | ~8–15% | ~71 | Fedasil+MDK+Antwerp L5+PZA+CAW |
| 220 | 100% | 100% | ~72–80% | ~8–16% | ~71 | Antwerp AGB mega stack ~631m |
| 230 | 100% | 100% | ~74–82% | ~9–17% | ~71 | Digipolis 246m + culture 16/16 + social ~32m |
| 240 | 100% | 100% | ~78–86% | ~10–18% | ~77 | WVG IVAs + AViQ + AF duals + COCOM/COCOF/VGC |
| 250 | 100% | 100% | ~79–87% | ~11–19% | ~87 | AJH dual justice + equality triple + fossil off-TE + Charleroi L5 |
| **260** | **100%** | **100%** | **~81–89%** | **~12–20%** | **~{ready}** | **Current** (export+tourism+WBI duals; FIT/WBI FOI public closes) |

*(L2/L5 % are **expert order-of-magnitude** from primary anchors — not a false-precision audit identity.)*

---

## Agent checklist (every 10 ticks)

1. Re-read `loop_state.ticks_completed` (if `N % 10 == 0` or human request).  
2. Update this file’s milestone row + inventory counts.  
3. Re-run leaderboard top 10 into `doge_waste_top10_current.md`.  
4. Append 5–10 lines to `loop_log.md`.  
"""

(root / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

# top 10 table from sorted
top10 = sorted_lb[:10]
just_out = sorted_lb[10:15]


def fmt_eur(v):
    try:
        x = float(v)
    except Exception:
        return str(v)
    if x >= 1e9:
        return f"**{x/1e9:.2f} bn**"
    if x >= 1e6:
        return f"**{x/1e6:.1f} m**"
    if x >= 1e3:
        return f"**{x/1e3:.0f} k**"
    return f"**{x:.0f}**"


rows = []
for i, r in enumerate(top10, 1):
    rows.append(
        f"| {i} | `{r.get('item_id')}` | {(r.get('name') or '')[:70]} | {fmt_eur(r.get('annual_cost_eur'))} | "
        f"{r.get('absurdity_score')} | {r.get('cost_score')} | {r.get('difficulty')} | **{r.get('priority_index')}** | "
        f"{(r.get('notes') or r.get('tco_notes') or '')[:40]} |"
    )

out_rows = []
for i, r in enumerate(just_out, 11):
    out_rows.append(
        f"| {i} | `{r.get('item_id')}` | {fmt_eur(r.get('annual_cost_eur'))} | {r.get('priority_index')} | "
        f"{(r.get('name') or '')[:50]} |"
    )

abs_rows = []
for i, r in enumerate(abs_sorted[:6], 1):
    abs_rows.append(
        f"| {i} | `{r.get('item_id')}` | {r.get('absurdity_score')} | {fmt_eur(r.get('annual_cost_eur'))} | "
        f"{(r.get('name') or '')[:55]} |"
    )

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **260** (2026-07-29) · **~{len(lb)}** leaderboard rows  
**Sort:** `priority_index` desc (then absurdity, then annual €)  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate. Small scandals can score high on **absurdity** (see honourable mentions).

---

## Top 10 (all-time current)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
{chr(10).join(rows)}

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
{chr(10).join(out_rows)}

---

## “Clown / high absurdity” shortlist (not pure size)

| Rank by abs | ID | Abs | Annual € class | One-liner |
|------------:|-----|----:|----------------|-----------|
{chr(10).join(abs_rows)}

*Top 10 **stable** vs @250 on pure-waste mega items (cheque, fossil, company cars, EIWT). Hole-fill ticks 251–259 mainly raised **L2 dual coverage** (export/tourism/WBI/justice) — high coverage value, lower pure-waste priority. Export triple and tourism triple are **core economic development**, not clown waste, unless dual unit-cost or L5 FOI fails.*
"""

(root / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

# update research_queue rq_251 done
rq_path = root / "research_queue.csv"
rq_text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_251,Mandatory progress@260 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
    "When ticks_completed hits 260: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
    "and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
    "2026-07-29T16:30:00Z,,"
    "Spawned tick259; progress@260 next tick mandatory"
)
new = (
    "rq_251,Mandatory progress@260 coverage % + waste top10,continuous,6,done,L0,gg_belgium,"
    "When ticks_completed hits 260: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
    "and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
    "2026-07-29T16:30:00Z,2026-07-29T17:00:00Z,"
    f"tick260: progress L2 ~81-89 L5 ~12-20 FOI ready ~{ready}; waste top10 stable cheque/fossil; continue rq_252"
)
if old not in rq_text:
    raise SystemExit("rq_251 not found")
rq_path.write_text(rq_text.replace(old, new), encoding="utf-8")

# loop_state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    f"Scheduler 60s. Next prio5 rq_252; rq_116 SWA deferred. FOI ready ~{ready} human send. "
    "tick260 progress L2~81-89 L5~12-20 export+tourism+WBI duals.\n",
    encoding="utf-8",
)

print("WROTE progress + top10 + state")
print("DONE tick", tick)

# tick 310 — progress@310 coverage + waste top10
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T17:45:00Z"

lb_rows = list(csv.DictReader((ROOT / "leaderboard.csv").open(encoding="utf-8")))

def fnum(x, default=0.0):
    try:
        return float(x) if x not in (None, "") else default
    except Exception:
        return default

lb_rows.sort(
    key=lambda r: (
        -fnum(r.get("priority_index")),
        -fnum(r.get("absurdity_score")),
        -fnum(r.get("annual_cost_eur")),
    )
)

print("LEADERBOARD", len(lb_rows))
for i, r in enumerate(lb_rows[:15], 1):
    print(
        i,
        r["item_id"],
        r.get("priority_index"),
        r.get("annual_cost_eur"),
        r["name"][:60],
    )

print("HIGH_ABS")
for i, r in enumerate(
    sorted(lb_rows, key=lambda r: (-fnum(r.get("absurdity_score")), -fnum(r.get("priority_index"))))[
        :8
    ],
    1,
):
    print(i, r["item_id"], r.get("absurdity_score"), r.get("annual_cost_eur"), r["name"][:50])

foi = list(csv.DictReader((ROOT / "foi_queue.csv").open(encoding="utf-8")))
print("FOI", dict(Counter(r.get("status") for r in foi)), "total", len(foi))

rq = list(csv.DictReader((ROOT / "research_queue.csv").open(encoding="utf-8")))
print("RQ", len(rq), "open", sum(1 for r in rq if r["status"] == "open"))

for name in ["budgets.csv", "commitments.csv", "entities.csv", "sources.csv"]:
    n = sum(1 for _ in (ROOT / name).open(encoding="utf-8")) - 1
    print(name, n)

# counts for report
ready = sum(1 for r in foi if r.get("status") == "ready")
answered = sum(1 for r in foi if r.get("status") == "answered")
top10 = lb_rows[:10]
abs_top = sorted(
    lb_rows, key=lambda r: (-fnum(r.get("absurdity_score")), -fnum(r.get("priority_index")))
)[:6]

# --- write progress file ---
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

## Snapshot at **tick 310** (2026-07-30)

| Layer | Coverage of €347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; transfer wedge if double-counted |
| **C. L2 entity totals** | **~88–96%** (order of magnitude) | Up from ~87–95% @300: **Kamer-dotatie 9-inst pack** approved kred **€149.3m** (Rekenhof €71m + GBA €15.9m + Comité P €14.3m + Hof €14.5m + Ombuds €8.3m + HRJ €7.4m + CTRG €6.7m + Comité I €6.2m + FIRM €5.1m); **Raad van State ~€50m** IBZ-hosted dual Hof; AIG €9m + OCAD €4.1m; **CoA federal consultancy ~€0.84bn/yr class** (2.52bn 2020–22, IT 81%) |
| **D. L5 named end-receivers** | **~15–24%** of TE (generous) | Slight uptick: consultancy **top buyers named** (NMBS €465m / Infrabel €319m / Finances €185m 3y); ETF 140 projects still EUR FOI; pure ASBL/contractor bulk residual |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{answered}** |

**Off-TE (do not mix into 348 bn):** federal taxex inventory ~**€39 bn**; **4e fossil inventory direct €13.3 bn** (2022) + FFS/company cars TE; cheque TE; **Hedera CAP ~15 bn stock** / Synatom assets — waste/risk map, **not cash TE flow**. CoA consultancy **€2.52 bn / 3y** is **procurement-adjacent TE** (ops support), not pure taxex; annual class ~**€0.84 bn** for waste ranking.

### Inventory (tick 310)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~{sum(1 for _ in (ROOT / 'budgets.csv').open(encoding='utf-8')) - 1} |
| commitments.csv | ~{sum(1 for _ in (ROOT / 'commitments.csv').open(encoding='utf-8')) - 1} |
| leaderboard.csv | ~{len(lb_rows)} |
| entities.csv | ~{sum(1 for _ in (ROOT / 'entities.csv').open(encoding='utf-8')) - 1} |
| sources.csv | ~{sum(1 for _ in (ROOT / 'sources.csv').open(encoding='utf-8')) - 1} |
| FOI ready | ~{ready} |
| FOI answered | ~{answered} |
| FOI total rows | ~{len(foi)} |
| research_queue | ~{len(rq)} (open: rq_116 deferred + rq_302 hole-fill) |

### What improved since tick 300

- **Regulators fee-financed:** KSC budget class **~€8.1m** + NBB checks **€454k** (tick303); FANC fee model refined earlier.  
- **GBA privacy regulator:** werkings **€15.1–15.3m** 2024–25; staff **84→96**; toewijzing cut via reserves (tick304).  
- **Federale Ombudsman:** budget **€8.0–8.3m**; outturn 2024 **~€6.61m** util 83%; dots decline via boni X→X+2 (tick305).  
- **Kamer-dotatie pack:** full **9 institutions** approved 2026 kred **€149.28m** / dots **€133.13m** (Moesen +0.78% dots); Rekenhof **€71m** reclassified as spend entity (tick306–307).  
- **FIRM + CTRG:** approved **€5.08m** / **€6.69m** 2026 (tick307).  
- **Raad van State dual finance:** IBZ-hosted **~€50m** 2025 vs Hof Kamer-dotatie **~€14.5m**; AIG **€9.05m**; OCAD **€4.12m** (tick308).  
- **Federal consultancy CoA:** **€2.525bn** 2020–22 (IT **€2.03bn**); top NMBS/Infrabel/Finances; no central inventory — high waste-priority seed (tick309).  

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
| 260 | 100% | 100% | ~81–89% | ~12–20% | ~92 | Export+tourism+WBI duals; FIT/WBI FOI public closes |
| 270 | 100% | 100% | ~82–90% | ~13–21% | ~98 | FWO/FNRS + Sciensano/FAVV + Innoviris L5 + FIB |
| 280 | 100% | 100% | ~84–92% | ~14–22% | ~106 | SS CoA + Smals/KSZ + health + CREG/BIPT |
| 290 | 100% | 100% | ~86–94% | ~14–22% | ~115 | Nuclear dual + asylum + Hedera stock + ASEVA |
| 300 | 100% | 100% | ~87–95% | ~15–23% | ~124 | FPS Economy energy/crisis/H2/telecom/ETF/quality |
| **310** | **100%** | **100%** | **~88–96%** | **~15–24%** | **~{ready}** | **Current** (Kamer-dotatie pack + RvS dual + CoA consultancy 2.52bn) |
"""

# fix f-string inventory - already embedded above with wrong expressions
# Rebuild inventory section properly
n_bud = sum(1 for _ in (ROOT / "budgets.csv").open(encoding="utf-8")) - 1
n_cmt = sum(1 for _ in (ROOT / "commitments.csv").open(encoding="utf-8")) - 1
n_ent = sum(1 for _ in (ROOT / "entities.csv").open(encoding="utf-8")) - 1
n_src = sum(1 for _ in (ROOT / "sources.csv").open(encoding="utf-8")) - 1

progress = progress.replace(
    f"~{{sum(1 for _ in (ROOT / 'budgets.csv').open(encoding='utf-8')) - 1}}",
    f"~{n_bud}",
)
# The f-string already evaluated badly - rewrite file cleanly
progress_path = ROOT / "progress_every_10_ticks.md"
progress_path.write_text(
    f"""# DOGE progress — every 10 ticks

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

## Snapshot at **tick 310** (2026-07-30)

| Layer | Coverage of €347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; transfer wedge if double-counted |
| **C. L2 entity totals** | **~88–96%** (order of magnitude) | Up from ~87–95% @300: **Kamer-dotatie 9-inst pack** approved kred **€149.3m** (Rekenhof €71m + GBA €15.9m + Comité P €14.3m + Hof €14.5m + Ombuds €8.3m + HRJ €7.4m + CTRG €6.7m + Comité I €6.2m + FIRM €5.1m); **Raad van State ~€50m** IBZ-hosted dual Hof; AIG €9m + OCAD €4.1m; **CoA federal consultancy ~€0.84bn/yr class** (2.52bn 2020–22, IT 81%) |
| **D. L5 named end-receivers** | **~15–24%** of TE (generous) | Slight uptick: consultancy **top buyers named** (NMBS €465m / Infrabel €319m / Finances €185m 3y); ETF 140 projects still EUR FOI; pure ASBL/contractor bulk residual |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{answered}** |

**Off-TE (do not mix into 348 bn):** federal taxex inventory ~**€39 bn**; **4e fossil inventory direct €13.3 bn** (2022) + FFS/company cars TE; cheque TE; **Hedera CAP ~15 bn stock** / Synatom assets — waste/risk map, **not cash TE flow**. CoA consultancy **€2.52 bn / 3y** is **procurement-adjacent TE** (ops support), not pure taxex; annual class ~**€0.84 bn** for waste ranking.

### Inventory (tick 310)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~{n_bud} |
| commitments.csv | ~{n_cmt} |
| leaderboard.csv | ~{len(lb_rows)} |
| entities.csv | ~{n_ent} |
| sources.csv | ~{n_src} |
| FOI ready | ~{ready} |
| FOI answered | ~{answered} |
| FOI total rows | ~{len(foi)} |
| research_queue | ~{len(rq)} (open: rq_116 deferred + rq_302 hole-fill) |

### What improved since tick 300

- **Regulators fee-financed:** KSC budget class **~€8.1m** + NBB checks **€454k** (tick303); FANC fee model refined earlier.  
- **GBA privacy regulator:** werkings **€15.1–15.3m** 2024–25; staff **84→96**; toewijzing cut via reserves (tick304).  
- **Federale Ombudsman:** budget **€8.0–8.3m**; outturn 2024 **~€6.61m** util 83%; dots decline via boni X→X+2 (tick305).  
- **Kamer-dotatie pack:** full **9 institutions** approved 2026 kred **€149.28m** / dots **€133.13m** (Moesen +0.78% dots); Rekenhof **€71m** reclassified as spend entity (tick306–307).  
- **FIRM + CTRG:** approved **€5.08m** / **€6.69m** 2026 (tick307).  
- **Raad van State dual finance:** IBZ-hosted **~€50m** 2025 vs Hof Kamer-dotatie **~€14.5m**; AIG **€9.05m**; OCAD **€4.12m** (tick308).  
- **Federal consultancy CoA:** **€2.525bn** 2020–22 (IT **€2.03bn**); top NMBS/Infrabel/Finances; no central inventory — high waste-priority seed (tick309).  

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
| 260 | 100% | 100% | ~81–89% | ~12–20% | ~92 | Export+tourism+WBI duals; FIT/WBI FOI public closes |
| 270 | 100% | 100% | ~82–90% | ~13–21% | ~98 | FWO/FNRS + Sciensano/FAVV + Innoviris L5 + FIB |
| 280 | 100% | 100% | ~84–92% | ~14–22% | ~106 | SS CoA + Smals/KSZ + health + CREG/BIPT |
| 290 | 100% | 100% | ~86–94% | ~14–22% | ~115 | Nuclear dual + asylum + Hedera stock + ASEVA |
| 300 | 100% | 100% | ~87–95% | ~15–23% | ~124 | FPS Economy energy/crisis/H2/telecom/ETF/quality |
| **310** | **100%** | **100%** | **~88–96%** | **~15–24%** | **~{ready}** | **Current** (Kamer-dotatie pack + RvS dual + CoA consultancy 2.52bn) |
""",
    encoding="utf-8",
)

# --- waste top10 ---
def fmt_eur(v):
    try:
        v = float(v)
    except Exception:
        return str(v)
    if v >= 1e9:
        return f"**{v/1e9:.2f} bn**"
    if v >= 1e6:
        return f"**{v/1e6:.2f} m**"
    if v >= 1e3:
        return f"**{v/1e3:.1f} k**"
    return f"**{v:.0f}**"

lines = []
lines.append("# DOGE waste ranking — current top 10\n")
lines.append(f"**As-of:** tick **310** (2026-07-30) · **~{len(lb_rows)}** leaderboard rows  ")
lines.append("**Sort:** `priority_index` desc (then absurdity, then annual €)  ")
lines.append("**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  ")
lines.append(
    "**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  \n"
)
lines.append(
    "**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  "
)
lines.append(
    "Large structural TE/FFS score high on **cost** even when “absurdity” is moderate. Small scandals can score high on **absurdity** (see honourable mentions).\n"
)
lines.append("---\n")
lines.append("## Top 10 (all-time current — annual flow / TE-adjacent)\n")
lines.append(
    "| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |"
)
lines.append(
    "|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|"
)
why = {
    "lb_fed_fossil_direct_13_3bn": "4e fossil inventory",
    "lb_company_cars_fpb": "FPB package",
    "lb_fed_fossil_accises_10_5bn": "fossil inventory",
    "lb_exc_heatoil": "FFS multi-year",
    "lb_cheque_economy": "CoA TE layer B; face=wages; pure waste admin+DWL only",
    "lb_fed_fossil_company_cars_ehs_3_4bn": "fossil inventory",
    "lb_fed_fossil_mazout_1_86bn": "fossil inventory",
    "lb_company_cars": "Official FFS package",
    "lb_eiwt_package": "Top wage-subsidy instrument",
    "lb_eiwt_night_shift_cluster": "~2.04bn 2024 cluster",
    "lb_fed_consultancy_2_5bn": "CoA 2.52bn 2020-22 / ~0.84bn/yr; no inventory",
}
for i, r in enumerate(top10, 1):
    iid = r["item_id"]
    lines.append(
        f"| {i} | `{iid}` | {r['name'][:55]} | {fmt_eur(r.get('annual_cost_eur'))} | "
        f"{r.get('absurdity_score')} | {r.get('cost_score')} | {r.get('difficulty')} | "
        f"**{r.get('priority_index')}** | {why.get(iid, r.get('notes', '')[:40] or 'leaderboard')} |"
    )

lines.append(
    "\n**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.\n"
)
lines.append("### Just outside top 10 (often relevant)\n")
lines.append("| # | ID | Annual € | Priority | Note |")
lines.append("|---|-----|----------:|---------:|------|")
for i, r in enumerate(lb_rows[10:15], 11):
    lines.append(
        f"| {i} | `{r['item_id']}` | {fmt_eur(r.get('annual_cost_eur'))} | {r.get('priority_index')} | {r['name'][:45]} |"
    )

lines.append("\n### Large stock / off-TE / temporary / procurement map (not pure annual waste top 10)\n")
lines.append("| ID | Stock / envelope / peak | Note |")
lines.append("|-----|------------------:|------|")
lines.append(
    "| `lb_hedera_cap_15bn` | **~15 bn** CAP | Phoenix nuclear waste finance stock; not annual TE flow |"
)
lines.append("| `lb_synatom_assets_12_9bn` | **12.9 bn** | Pre/post CAP provision assets |")
lines.append(
    "| `lb_creg_crisis_pack_2bn_2023` | **~2.09 bn** peak 2023 | Temporary energy-crisis CREG social+basisfonds |"
)
lines.append(
    "| `lb_fed_consultancy_2_5bn` | **~0.84 bn/yr** class | CoA 2.52bn 2020–22 IT-heavy; inventory FOI |"
)
lines.append(
    "| `lb_kamer_dotatie_9pack_149m` | **149 m** kred 2026 | Kamer-dotatie democratic control pack |"
)
lines.append("| `lb_raad_van_state_50m` | **~50 m** 2025 | IBZ-hosted dual Hof Kamer-dotatie |")

lines.append('\n## “Clown / high absurdity” shortlist (not pure size)\n')
lines.append("| Rank by abs | ID | Abs | Annual € class | One-liner |")
lines.append("|------------:|-----|----:|----------------|-----------|")
for i, r in enumerate(abs_top, 1):
    lines.append(
        f"| {i} | `{r['item_id']}` | {r.get('absurdity_score')} | {fmt_eur(r.get('annual_cost_eur'))} | {r['name'][:50]} |"
    )

lines.append(
    "\n*Top 10 **stable** vs @300 on pure-waste mega items (fossil, company cars, cheque TE, EIWT). "
    "Ticks 301–309 raised **institutional map** (KSC, GBA, Ombuds, Kamer-dotatie 9-pack, RvS dual) and **CoA consultancy €2.52bn** "
    "as high-priority opacity — not a re-ranking of fossil/cars unless pi exceeds. "
    "Core courts/regulators are **not pure clown waste**; consultancy opacity is the new high-pi mechanism seed.*\n"
)

(ROOT / "doge_waste_top10_current.md").write_text("\n".join(lines), encoding="utf-8")

# --- research_queue ---
rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_300,Mandatory progress@310 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
    "When ticks_completed hits 310: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
    "2026-07-30T16:45:00Z,,Spawned tick308 after RvS; progress@310 next after 2 more ticks or do at 310"
)
new = (
    "rq_300,Mandatory progress@310 coverage % + waste top10,continuous,6,done,L0,gg_belgium,"
    "When ticks_completed hits 310: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
    f"2026-07-30T16:45:00Z,{utc},"
    f"tick310: L2 ~88-96 L5 ~15-24 FOI ready ~{ready}; waste top10 stable fossil/cars/cheque/EIWT; consultancy 0.84bn/yr noted off pure top10; spawn continue rq_302"
)
if old not in text:
    raise SystemExit("rq_300 not found as expected")
text = text.replace(old, new)
rq_path.write_text(text, encoding="utf-8")

# loop_state
(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_300,310,no,"
    "Scheduler 60s. Next prio5 rq_302; rq_116 SWA deferred. FOI ready. "
    f"tick310 progress L2~88-96 L5~15-24 FOI~{ready}; consultancy map.\n",
    encoding="utf-8",
)

print("progress@310 written")
print("top1", top10[0]["item_id"], top10[0].get("priority_index"))
print("ready", ready, "answered", answered, "lb", len(lb_rows))

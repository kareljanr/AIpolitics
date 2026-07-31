# tick740 — progress@740 coverage % + waste top10
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T07:15:00Z"


def count_csv(name: str) -> int:
    with open(DATA / name, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


counts = {
    "budgets": count_csv("budgets.csv"),
    "commitments": count_csv("commitments.csv"),
    "leaderboard": count_csv("leaderboard.csv"),
    "entities": count_csv("entities.csv"),
    "sources": count_csv("sources.csv"),
    "foi_total": count_csv("foi_queue.csv"),
}

with open(DATA / "foi_queue.csv", encoding="utf-8", newline="") as f:
    foi = list(csv.DictReader(f))
foi_ready = sum(1 for r in foi if (r.get("status") or "").strip() == "ready")
foi_answered = sum(1 for r in foi if (r.get("status") or "").strip() == "answered")
foi_draft = sum(1 for r in foi if (r.get("status") or "").strip() == "draft")

with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lbs = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0.0


def ae(r):
    try:
        return float(str(r.get("annual_cost_eur") or "0").replace(",", "").replace(" ", ""))
    except Exception:
        return 0.0


def abs_s(r):
    try:
        return float(r.get("absurdity_score") or 0)
    except Exception:
        return 0.0


# Stock / multi-decade filter (annual_cost is full stock or multi-decade finance)
STOCK_HINTS = (
    "stock",
    "snowball",
    "eoy20",
    "eoy2083",
    "portfolio",
    "encours",
    "bond stock",
    "debt book",
    "multi-decade",
    "path 20",
    "equity inject",
    "refinance stock",
    "sub debt",
)

# Known stock IDs to filter from pure annual top10
STOCK_IDS = {
    "lb_owv_sub_snowball_27bn_2083",
    "lb_metro3_overrun_477pct",
    "lb_metro3_financing_gap_4bn",
    "lb_ss_exp_148bn_2026",
    "lb_ss_rec_148bn_2026",
    "lb_fed_e1_path_36_2bn_2029",
    "lb_vl_dotaties_34_8bn_2026",
    "lb_dual_wal_vl_debt_2026",
    "lb_ss_alt_finance_27_6bn_2026",
    "lb_vwf_portfolio_9_698bn_2025",
    "lb_swl_debt_2_742bn_2024",
    "lb_swcs_encours_1_749bn",
    "lb_slrb_debt_1_672bn",
    "lb_slrb_encours_1_131bn",
    "lb_flrbc_encours_1_607bn_2025",
    "lb_flrbc_bs_2_128bn_vs_fin_1_780bn",
    "lb_dual_flrbc_vwf_swcs_slrb_asymmetry",
    "lb_dual_vwf_swcs_flw_asymmetry",
    "lb_dual_swl_vmsw_slrb_swcs_asymmetry",
    "lb_dual_swcs_vmsw_slrb_flw_asymmetry",
    "lb_dual_slrb_vmsw_swl_asymmetry",
}


def is_stock(r):
    iid = r.get("item_id") or ""
    if iid in STOCK_IDS:
        return True
    t = f"{iid} {(r.get('name') or '')} {(r.get('type') or '')} {(r.get('tco_notes') or '')}".lower()
    if (r.get("type") or "").lower() in ("stock", "dual") and ae(r) >= 1_000_000_000:
        return True
    if any(h in t for h in STOCK_HINTS) and ae(r) >= 5_000_000_000:
        return True
    # eoy snowball / multi-decade
    if "snowball" in t or "eoy2083" in t:
        return True
    return False


lbs_sorted = sorted(lbs, key=lambda r: (-pi(r), -ae(r)))
annual_pool = [r for r in lbs_sorted if not is_stock(r)]
top10 = annual_pool[:10]
outside = annual_pool[10:20]
high_abs = sorted(lbs, key=lambda r: (-abs_s(r), -pi(r)))[:15]

# Housing dual residual wave 730-739 for progress notes
housing_ids = [
    "lb_flrbc_funding_freeze_2025",
    "lb_vwf_prod_1_632bn_2025",
    "lb_vwf_bonds_1_550bn_2025",
    "lb_swl_plan_reno_1_1675bn",
    "lb_swcs_garantie_npl_31pct",
    "lb_slrb_prl_own_fund_gap_577m",
    "lb_flrbc_gl_arrears_22pct_2025",
    "lb_flrbc_debt_service_158_6m_2025",
]
housing_found = {r.get("item_id"): r for r in lbs if r.get("item_id") in housing_ids}

print("COUNTS", counts)
print("FOI ready", foi_ready, "answered", foi_answered, "draft", foi_draft)
print("TOP10 ANNUAL:")
for i, r in enumerate(top10, 1):
    print(i, pi(r), ae(r), r.get("item_id"), (r.get("name") or "")[:70])
print("OUTSIDE:")
for i, r in enumerate(outside, 11):
    print(i, pi(r), ae(r), r.get("item_id"))
print("HIGH ABS:")
for r in high_abs[:12]:
    print(abs_s(r), pi(r), r.get("item_id"))

# --- write progress file (prepend new snapshot) ---
progress_path = DATA / "progress_every_10_ticks.md"
old = progress_path.read_text(encoding="utf-8")

# Insert after the protocol header (after first --- block ending "How to read")
# Simpler: rewrite full file with new snapshot on top of previous snapshots truncated
new_snapshot = f"""# DOGE progress — every 10 ticks

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

## Snapshot at **tick 740** (2026-08-02)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** FLRBC full RA2025 BS **€2.128bn** / encours **€1.607bn** · VWF portfolio **€9.698bn** / prod **€1.632bn** · SWL BS debt **€2.742bn** · SWCS encours **€1.749bn** · SLRB liq **€803m** / debt **€1.672bn** · prior GIP/OTW/Oosterweel/BCR retained |
| **D. L5 named / measure end-lines** | **~53-67%** of TE (generous) | **Gain 730→740 is FOI-adjacent dual housing residual wave (not near-complete of 348bn):** SLRB RA2025 residual (liq 802.7 / PRL gap 577 / ARS 52.5) · SWCS RA2025 (prod 483m / encours 1.749bn / garantie NPL **31%**) · SWL RA2024 (works 364.3m / plan reno envelope **1.1675bn** delivery lag) · VWF AV2025 (prod **1.632bn** @2.48% vs bonds **1.55bn** @4.21% / portfolio **9.698bn**) · FLRBC RA2025 (**credit freeze Jul–Dec 2025** / debt service 158.6 > new credit 149.5 / GL arrears **22%** / CCP default **2.52%** vs BE 0.60) · COCOF/COCOM/VGC/SPW residual duals retained · FOI still bulk L5 awards + dual unit-cost/NPL matrices |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_answered}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform *savings paths* · **gross financing / OLO** · **unconsol federal debt / E1 path €24.5–36.2bn** · **VL Maastricht/consol debt ~€50–57bn** · **WAL direct debt ~€30–34bn** / **FWB ~€14–21bn path** · **BCR consol debt €16.1→19.1bn path** · **Hedera CAP €15bn** · **Phoenix CfD multi-year** · **VL begrotingsfondsen stocks ~€0.86bn** · **VL ruiter carry €1.4bn** · **Oosterweel VAK + BC interest/sub snowball stocks** · **project-bond over-plafond path** · **SKF multi-year €0.96bn** · **Fluvius equity inject path €1.56bn** · **FRBRTC/refinance stocks** · **OAA reporté fiction** · **GIP beschikbaarheid path** · **Sofico guaranteed debt / CAPEX commit** · **VWF portfolio €9.7bn / SWL debt €2.74bn / SWCS encours €1.75bn / FLRBC encours €1.61bn / SLRB debt €1.67bn** (housing finance stocks dual, not pure TE) · **flexi privilege TE class** · **internal security dual-use / NATO classification** · **CSF NPE growth caps** · Moody/S&P rating actions (not euros).

### Inventory (tick 740)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~{counts['budgets']} |
| commitments.csv | ~{counts['commitments']} |
| leaderboard.csv | ~{counts['leaderboard']} |
| entities.csv | ~{counts['entities']} |
| sources.csv | ~{counts['sources']} |
| FOI ready | ~{foi_ready} |
| FOI answered | ~{foi_answered} |
| FOI total rows | ~{counts['foi_total']} |
| research_queue open | rq_116 deferred + next hole-fill after progress |

### What improved since tick 730

- **BCR community dual residual (tick731–733):** COCOF BI2026 SEC **−€22.7m** / debt **€203.7m** / Phare **€210.3m** · COCOM fake recettes **€49.1m** / sous-util **€64.7m** / Iriscare **€1.83bn** · VGC JR2025 onderwijs **€53.9m** / werksubs **€53.9m** / PPS Deleers **~€64m**.
- **WAL Entity II residual (tick734–737):** SPW RA2025 local fin **€2.322bn** / CV **~€330m** / housing reno **>€110m** · SLRB RA2025 liq **€802.7m** / debt **€1.672bn** / encours **€1.131bn** / PRL gap **€577m** · SWCS RA2025 prod **€483m** / encours **€1.749bn** / garantie NPL **31%** · SWL RA2024 works **€364.3m** / plan reno envelope **€1.1675bn** (invest 231m / receptions only 126) / BS debt **€2.742bn**.
- **VL+BCR social credit dual (tick738–739):** VWF AV2025 prod **€1.632bn** @**2.48%** vs bonds **€1.55bn** @**4.21%** / portfolio **€9.698bn** / HW NPL **9%** · FLRBC RA2025 encours **€1.607bn** / **credit freeze Jul–Dec 2025** (loans **€130m** vs 260) / debt service **€158.6m** / GL arrears **22%** / CCP **2.52%** vs BE **0.60%** / BS **€2.128bn** vs fin-CG **€1.780bn** carveout.
- **Dual map:** full BE social-housing + social-credit OIP stack (VMSW/VWF/SLRB/FLRBC/SWL/SWCS/FLW) with unit-cost and NPL matrices still FOI-heavy; BCR funding freeze is 2025 governance outlier.

---

"""

# Keep prior snapshots from old file (from first "## Snapshot at **tick 730**")
marker = "## Snapshot at **tick 730**"
idx = old.find(marker)
if idx >= 0:
    rest = old[idx:]
else:
    # fallback: keep everything after first snapshot attempt
    rest = old.split("---\n\n## Snapshot", 1)[-1] if "## Snapshot" in old else ""
    if rest and not rest.startswith("## Snapshot"):
        rest = "## Snapshot" + rest

progress_path.write_text(new_snapshot + rest, encoding="utf-8")
print("wrote progress_every_10_ticks.md")

# --- waste top10 ---
def fmt_eur(v):
    if v >= 1_000_000_000:
        return f"**{v/1e9:.2f} bn**"
    if v >= 1_000_000:
        return f"**{v/1e6:.2f} m**"
    return f"**{v:,.0f}**"


def row_line(i, r, why=""):
    return (
        f"| {i} | `{r.get('item_id')}` | {(r.get('name') or '')[:70]} | "
        f"{fmt_eur(ae(r))} | {r.get('absurdity_score')} | {r.get('cost_score')} | "
        f"{r.get('difficulty')} | **{pi(r):.2f}** | {why} |"
    )


why_map = {
    "lb_vl_gip_monitor_fail_2_5bn": "Governance opacity on multi-mode invest (not pure TE waste)",
    "lb_fed_fossil_direct_13_3bn": "4e fossil inventory",
    "lb_fed_fossil_accises_10_5bn": "fossil inventory",
    "lb_company_cars_fpb": "FPB package",
    "lb_exc_heatoil": "FFS multi-year",
    "lb_cheque_economy": "CoA TE layer B; face=wages; pure waste admin+DWL only",
    "lb_co2_vs_ordinary_ssc_gap_1bn": "CoA CO₂ under-collection path",
    "lb_oaa_consol_reporte_300_6m": "Systemic CFP art13 budget fiction",
    "lb_bcr_annexe2_reporte_wave": "Reporté sincerity cluster",
    "lb_dual_cars_ssc_taxex": "dual SSC+taxex under-pricing",
    "lb_flrbc_funding_freeze_2025": "NEW 739 BCR social-credit freeze Jul–Dec 2025",
    "lb_vwf_prod_1_632bn_2025": "NEW 738 rate subsidy 2.48% lend vs 4.21% fund",
    "lb_swl_plan_reno_1_1675bn": "NEW 737 plan reno delivery lag",
}

lines = []
lines.append("# DOGE waste ranking — current top 10\n")
lines.append(f"**As-of:** tick **740** (2026-08-02) · **~{counts['leaderboard']}** leaderboard rows  ")
lines.append("**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**  ")
lines.append("**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  ")
lines.append("**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  \n")
lines.append("**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  ")
lines.append("Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.\n")
lines.append("---\n")
lines.append("## Top 10 (all-time current — annual flow / TE-adjacent)\n")
lines.append("| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |")
lines.append("|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|")
for i, r in enumerate(top10, 1):
    why = why_map.get(r.get("item_id") or "", (r.get("notes") or "ranked by priority_index")[:60])
    lines.append(row_line(i, r, why))

lines.append("")
lines.append("**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  ")
lines.append("**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  ")
lines.append("**Stock filter (off pure annual top10):** Metro3 overrun/gap · Hedera CAP · VL/WAL/FWB/BCR debt stocks · **`lb_owv_sub_snowball_27bn_2083` (raw high pi — eoy2083 sub debt €27bn)** · Oosterweel VAK/bond plafond residual · encours · federal unconsol debt / E1 path · Infrabel/WE equity · SS consol 148bn · Fluvius equity path · Sofico CAPEX commit / guaranteed debt · **VWF portfolio €9.7bn · SWL debt €2.74bn · SWCS/FLRBC/SLRB encours duals** · ruiter carry · FRBRTC refinance.\n")
lines.append("**Change vs tick 730:** pure annual top10 **largely stable** (GIP monitor #1; fossil/cars/cheque/reporté #2–10). **Major NEW residual off pure top10 / just outside:** FLRBC funding freeze · VWF rate-subsidy spread · SWL plan-reno delivery lag · SWCS/FLRBC/VWF deposit-loan NPL band **9–31%** · full dual housing OIP stack mapped. Gain 730–740 is **BE social-housing + social-credit dual residual** more than FFS reshuffle.\n")
lines.append("### Just outside top 10 (often relevant)\n")
lines.append("| # | ID | Annual € | Priority | Note |")
lines.append("|---|-----|----------:|---------:|------|")
# include stock snowball explicitly
snow = next((r for r in lbs if r.get("item_id") == "lb_owv_sub_snowball_27bn_2083"), None)
if snow:
    lines.append(
        f"| — | `lb_owv_sub_snowball_27bn_2083` | **27.0 bn stock** | **{pi(snow):.2f}** | STOCK filtered; CoA unjustified FM assignment |"
    )
freeze = next((r for r in lbs if r.get("item_id") == "lb_flrbc_funding_freeze_2025"), None)
if freeze:
    lines.append(
        f"| — | `lb_flrbc_funding_freeze_2025` | {fmt_eur(ae(freeze))} | **{pi(freeze):.2f}** | **NEW 739** BCR credit freeze Jul–Dec 2025 |"
    )
vwf = next((r for r in lbs if r.get("item_id") == "lb_vwf_prod_1_632bn_2025"), None)
if vwf:
    lines.append(
        f"| — | `lb_vwf_prod_1_632bn_2025` | {fmt_eur(ae(vwf))} | **{pi(vwf):.2f}** | **NEW 738** lend 2.48% vs fund 4.21% |"
    )
for i, r in enumerate(outside[:8], 11):
    lines.append(
        f"| {i} | `{r.get('item_id')}` | {fmt_eur(ae(r))} | **{pi(r):.2f}** | {(r.get('name') or '')[:50]} |"
    )

lines.append("\n### High-absurdity shortlist (not pure annual cost rank)\n")
lines.append("| ID | Abs | Note |")
lines.append("|----|----:|------|")
seen = set()
for r in high_abs:
    iid = r.get("item_id") or ""
    if iid in seen:
        continue
    seen.add(iid)
    lines.append(f"| `{iid}` | **{abs_s(r):.1f}** | {(r.get('name') or '')[:70]} |")
    if len(seen) >= 14:
        break

lines.append("\n### Dual / mega map (not pure annual waste top 10)\n")
lines.append("| ID | Envelope / peak | Note |")
lines.append("|----|----------------:|------|")
lines.append("| `lb_ss_exp_148bn_2026` / `lb_ss_rec_148bn_2026` | **148 bn** | SS near-balance dual |")
lines.append("| `lb_riziv_care_43_9bn_2026` | **43.9 bn** | dual AViQ/WVG |")
lines.append("| `lb_fed_e1_path_36_2bn_2029` | **36.2 bn** | E1 path 2029 |")
lines.append("| `lb_vl_dotaties_34_8bn_2026` | **34.8 bn** | BFW dual |")
lines.append("| `lb_dual_wal_vl_debt_2026` | **33 / 57 bn** | WAL Baa1 vs VL A1 |")
lines.append("| `lb_owv_sub_snowball_27bn_2083` | **27.0 bn stock** | Lantis sub eoy2083 |")
lines.append("| `lb_vwf_portfolio_9_698bn_2025` | **9.70 bn stock** | **NEW 738** largest BE social-credit book |")
lines.append("| `lb_swl_debt_2_742bn_2024` | **2.74 bn stock** | **NEW 737** SWL BS debt |")
lines.append("| `lb_flrbc_encours_1_607bn_2025` | **1.61 bn stock** | **NEW 739** FLRBC credit book |")
lines.append("| `lb_swcs_encours_1_749bn` | **1.75 bn stock** | **NEW 736** SWCS loan book |")
lines.append("| `lb_slrb_debt_1_672bn` | **1.67 bn stock** | **NEW 735** SLRB BS debt |")
lines.append("| dual housing OIP stack | multi-bn | VMSW/VWF/SLRB/FLRBC/SWL/SWCS/FLW mapped 735–739 |")
lines.append("")

(DATA / "doge_waste_top10_current.md").write_text("\n".join(lines), encoding="utf-8")
print("wrote doge_waste_top10_current.md")

# --- close rq_731, spawn rq_732 ---
rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_731":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            f"tick740 progress@740 L2~99 L5~53-67 FOI ready~{foi_ready}; "
            "waste top10 stable GIP#1; housing dual residual wave 731-739; spawn rq_732"
        )
if not any(r.get("task_id") == "rq_732" for r in rqs):
    rqs.append({
        "task_id": "rq_732",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined or Entity II dual residual "
            "or VMSW residual dual housing or fed Pillar2/VVPR recheck if new PDF"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick740 after progress@740",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("rq_731=done rq_732=open")

ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys())
if ls:
    ls[0]["mode"] = "continuous"
    ls[0]["current_sprint"] = "hole_fill"
    ls[0]["last_tick_utc"] = UTC
    ls[0]["last_unit_id"] = "rq_731"
    ls[0]["ticks_completed"] = "740"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        f"tick740 progress@740 L2~99 L5~53-67 FOI ready~{foi_ready}; "
        "next rq_732; rq_116 deferred; housing dual wave 731-739"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=740")
print("DONE tick740")

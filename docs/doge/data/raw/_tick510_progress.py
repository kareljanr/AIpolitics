# tick510 — progress milestone @510 + waste top10; no invent euros
from pathlib import Path
from datetime import datetime, timezone

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
docs = root.parent

# Inventory (line counts incl header; class ≈ n-1)
def nlines(p):
    return sum(1 for _ in open(p, encoding="utf-8", errors="replace"))

inv = {
    "budgets": nlines(root / "budgets.csv") - 1,
    "cmt": nlines(root / "commitments.csv") - 1,
    "lb": nlines(root / "leaderboard.csv") - 1,
    "entities": nlines(root / "entities.csv") - 1,
    "sources": nlines(root / "sources.csv") - 1,
    "foi": nlines(root / "foi_queue.csv") - 1,
    "rq": nlines(root / "research_queue.csv") - 1,
}
# FOI ready approx from prior parse
ready, answered = 257, 9

progress_path = root / "progress_every_10_ticks.md"
old = progress_path.read_text(encoding="utf-8")

# Insert new snapshot after the intro block (before "## Snapshot at **tick 500**")
marker = "## Snapshot at **tick 500**"
if marker not in old:
    raise SystemExit("tick 500 marker missing")

new_snap = f"""## Snapshot at **tick 510** (2026-07-28)

| Layer | Coverage of €347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE €347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** Entity I aju deficit **24.5bn** · SS BC **148.0bn** near balance · Fedasil **848m** · Justice **2.9bn** · unemp **4.84bn** · dual E1/E2 residual |
| **D. L5 named / measure end-lines** | **~31–44%** of TE (generous) | **Gain 500→510 is CoA mobility + federal aju residual wave:** DWV studies **~125m** four-pack overruns · Oosterweel exec **10.1bn** / interest **24.5bn** 2026-83 · E1 energy **~2.6bn** · MPKV coast **466m** / Kustvisie **21m** / century **2–5bn** · KMO VenB control uplift **>5.6bn** · BBI bank assess **2.3bn** / collect **36m** · Fedasil save path gap · POD MI soft save **13m** undeliverable · RIZIV miss **183m** · unemp reform path **1.69→2.45bn** / exclusion **194k** / leefloon shift **32%** · invalidity cumul miss **334m** · FOI still bulk ASBL/firm + dual cash |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{answered}**; total FOI rows **~{inv['foi']}** (+ DWV · Oosterweel · energy funds · MPKV · KMO · BBI · Fedasil · POD MI · RVA/leefloon, …) |

**Off-TE (do not mix into 348 bn):** federal taxex **€29.7bn** · company cars/cheque/EIWT · lottery player stakes · FPB *options* · Tax Shelter · private PPP · equity injections (Zaventem) are debt/finance not TE flow · reform *savings paths* are budget deltas not TE flow.

### Inventory (tick 510)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~{inv['budgets']} |
| commitments.csv | ~{inv['cmt']} |
| leaderboard.csv | ~{inv['lb']} |
| entities.csv | ~{inv['entities']} |
| sources.csv | ~{inv['sources']} |
| FOI ready | ~{ready} |
| FOI answered | ~{answered} |
| FOI total rows | ~{inv['foi']} |
| research_queue | ~{inv['rq']} (open: rq_116 deferred + hole-fill after progress) |

### What improved since tick 500

- **Mobility dual (tick501–502):** DWV study four-pack spent class **~€125m** (R0N **36→104m** est) · Toekomstverbond Oosterweel exec **€10.055bn** · BC interest **€24.495bn** 2026–2083 · dual Lantis/GIP.
- **Federal aju macro (tick503):** Entity I deficit **€24.5bn** · primary **12.2→18.7** · interest **12.3→17.5** · defence multi-year **17.3bn** · energy **~2.6bn** · dual E2.
- **Coast + tax control (tick504–506):** MPKV **€321+144m** / Kustvisie **€21m** / century **€2–5bn** · KMO VenB **>€5.6bn** control uplifts · BBI bank **€2.3bn** assess / **€36m** collect (~1.6%).
- **Social residual (tick507–509):** Justice **€2.9bn** + prison provis **€259m** · Fedasil **€848m** · SS **€148.0bn** · POD MI OCMW **€2.31bn** soft save slip · unemp reform **€1.69bn** path dual leefloon **31.9%** Q1 · invalidity multi-year miss **€334m**.

---

"""

progress_path.write_text(old.replace(marker, new_snap + marker, 1), encoding="utf-8")

# Waste top10
waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **510** (2026-07-28) · **~{inv['lb']}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks with annual € = 0 filtered off pure top10**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | 4e fossil inventory |
| 2 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | fossil inventory (tie-break annual vs cars) |
| 3 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB package |
| 4 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS multi-year |
| 5 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted  | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA TE layer B; face=wages; pure waste admin+DWL only |
| 6 | `lb_fed_fossil_company_cars_ehs_3_4bn` | Company cars EHS fossil inventory 3.43bn 2022 | **3.43 bn** | 8 | 9.0 | 7 | **8.35** | fossil inventory |
| 7 | `lb_fed_fossil_mazout_1_86bn` | Heating oil accise gap 1.86bn 2022 fossil inv | **1.86 bn** | 8 | 9.0 | 6 | **8.3** | fossil inventory |
| 8 | `lb_company_cars` | Company cars tax expenditure package | **3.14 bn** | 8 | 9.5 | 8 | **8.22** | Official FFS package |
| 9 | `lb_eiwt_package` | EIWT partial remittance bedrijfsvoorheffing package | **4.36 bn** | 7 | 9.5 | 6 | **8.08** | Top wage-subsidy instrument |
| 10 | `lb_eiwt_night_shift_cluster` | EIWT night+shift+continuous+construction cluster | **2.04 bn** | 7 | 9.5 | 6 | **8.08** | ~2.04bn 2024 cluster |

**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter:** Hedera CAP / ETS blocked / VL Maastricht debt **€50.2bn** annual=0 stay **off** pure annual top10.  
**Stable vs tick 500:** fossil/company-cars/cheque/EIWT mega items still dominate; **#2/#3** may flip on equal pi=8.5 (annual tie-break). Ticks 501–509 filled **CoA mobility + federal aju residual + tax control + social dual** — transparency/governance gains, not waste-first reordering of taxex giants.

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| 11 | `lb_taxex_fed_29_7bn` | **29.7 bn** | 8.05 | Federal TE inventory 2023 (off-TE pie) |
| 12 | `lb_specialty_defence_transfer_20bn` | **20.1 bn** | **8.0** | Specialty breach (control) |
| 13 | `lb_vl_gsc_support` | **822.0 m** | 8.0 | Flanders GSC |
| 14 | `lb_wage_subsidies_block` | **16.70 bn** | 7.98 | Wage subsidies block |
| 15 | `lb_cm_e1_control_gap_7_7bn` / dual map | **7.7 bn** residual | high cost | Entity I control-account residual 2029 |
| 16 | `lb_rva_reform_save_1_69bn` / dual leefloon | **1.69 bn** path | mid-high | **NEW 509** unemp reform save path dual 32% leefloon |
| 17 | `lb_bbi_bank_assess_2_3bn` class | **2.3 bn** assess / **36 m** collect | abs-heavy | **NEW 506** collection gap ~1.6% |
| 18 | `lb_kmo_venb_uplift_5_6bn` class | **>5.6 bn** control | high cost | **NEW 505** VenB control uplifts vs fraud claims |
| 19 | `lb_tv_oosterweel_10bn` / interest **24.5bn** | mega envelope | stock | **NEW 502** Toekomstverbond finance path |
| 20 | `lb_ss_exp_148bn_bc2026` | **148.0 bn** | core mass | **NEW 508** SS BC near balance |

### Large stock / off-TE / dual-structure / reform map (not pure annual waste top 10)

| ID | Stock / envelope / peak | Note |
|-----|------------------:|------|
| `lb_hedera_cap_15bn` | **~15 bn** CAP | Phoenix nuclear waste finance stock |
| `lb_ets_blocked_1_8bn` | **1.8 bn** | ETS auction proceeds blocked SPF Santé |
| `lb_lpm_invest_33_8bn_2026_34` | **33.8 bn** eng | Military programming 2026–34 |
| `lb_edp_gg_debt_692_5bn_2025` | **692.5 bn** | GG Maastricht debt 107.9% GDP |
| `lb_vl_debt_50_2bn_2025` | **50.2 bn** | VL Maastricht eoy2025 CoA RR |
| `lb_ss_exp_148bn_bc2026` | **148.0 bn** | SS BC2026 macro |
| `lb_tv_oosterweel` / interest path | **10.1 / 24.5 bn** | Lantis Oosterweel + lifetime interest |
| `lb_gip` class / CoA 2026_27 | **~3.7 bn** | VL GIP actualisatie dual SOFICO |
| `lb_mpkv_coast_466m` / century | **0.47 / 2–5 bn** | Coast defence near-term vs century |
| `lb_e1_deficit_24_5bn_aju` | **24.5 bn** | Entity I aju deficit 2026 |

### High-absurdity honourable mentions (not top-10 cost)

| ID | Note |
|----|------|
| `lb_vl_wassalon_podcast` | abs 9.5 — micro culture absurdity flag |
| `lb_ipolice_spent_77m_cancelled` | abs 9.0 — cancelled IT mega-project 76.7m spent |
| `lb_vl_persona_16m` / `lb_fwb_cepage_96m_est` | dual education payroll IT failures |
| `lb_bbi_bank_collect_36m` | **2.3bn assess / 36m collect** collection gap |
| `lb_podmi_save_slip_13m` | booked save not deliverable 2026 |
| `lb_leefloon_shift_32pct` | reform displacement not pure save |
| `lb_dwv_studies_125m` | study contract award→spend overruns |
| `lb_specialty_defence_transfer_20bn` | Full eng redistribution without parliament |

---

**Refresh rule:** recompute at each multiple of 10 ticks or when human asks “waste top / progress”.
"""
(root / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

# Update research queue
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old_rq = (
    "rq_501,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T23:45:00Z,,Spawned tick509 after CoA RVA unemp residual; progress@510 next tick; rq_116 deferred"
)
new_rq = (
    "rq_501,Progress milestone @510 coverage % + waste top10,continuous,5,done,L5,gg_belgium,"
    "Refresh progress_every_10_ticks.md + doge_waste_top10_current.md; no invent euros.,,"
    "2026-07-28T23:45:00Z,2026-07-29T00:05:00Z,"
    "tick510: progress A100 B100 C~99 D~31-44 E~257 ready; CoA wave 501-509 mobility+fed aju+tax control+social dual; waste top10 stable; rq_116 deferred"
)
if old_rq not in text:
    raise SystemExit("rq_501 open row not found")
text = text.replace(old_rq, new_rq)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_502,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T00:05:00Z,,Spawned tick510 after progress@510; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T00:05:00Z,rq_501,510,no,"
    "Tick510 progress@510 coverage+waste top10; next prio5 rq_502; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("tick510 progress OK", inv, "ready", ready)

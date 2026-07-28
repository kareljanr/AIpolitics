# tick 440: progress coverage % + waste top10 refresh (no new euro invent)
import csv
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T10:45:00Z"
TICK = 440
UNIT = "rq_431"

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
    with open(DATA / name, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    counts[name] = len(rows)
    if name == "foi_queue.csv":
        counts["foi_ready"] = sum(1 for r in rows if r.get("status") == "ready")
        counts["foi_answered"] = sum(1 for r in rows if r.get("status") == "answered")

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

## Snapshot at **tick 440** (2026-08-02)

| Layer | Coverage of €347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE €347.956bn; dual EDP/COM path) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS deficits dual EDP |
| **C. L2 entity totals** | **~98–99%** (order of magnitude) | **+** SS consol **€147.86bn** 2026 · Entity I social triple **€6.5bn** · SPP IS CPAS **€2.24bn** · NATO effort **€13.1bn** · Fedasil package **€802m** · coop **€1.04bn** · federal liq **€92bn** by cellule |
| **D. L5 named / measure end-lines** | **~24–37%** of TE (generous) | **Gain since 430 is reform/measure L5 not firm ASBL lists:** pens reform **0.81→2.23bn** path · RTW **0.20→1.93bn** · INAMI sante **764.5m** components · IPP annex **−0.42→−5.4bn** · chomage waves **193.9k** · Fedasil accueil/retours · personnel austerity · specialty breaches · residual FOI still dominates discretionary ASBL/firm end-receivers |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; total FOI rows **~{counts['foi_queue.csv']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **€29.7bn** · company cars/cheque/EIWT · IPP reform path · NATO extra **€16.8bn** package · ESSPROS social protection **€174–178bn** broader than TE pie.

### Inventory (tick 440)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~{counts['budgets.csv']} |
| commitments.csv | ~{counts['commitments.csv']} |
| leaderboard.csv | ~{counts['leaderboard.csv']} |
| entities.csv | ~{counts['entities.csv']} |
| sources.csv | ~{counts['sources.csv']} |
| FOI ready | ~{counts['foi_ready']} |
| FOI answered | ~{counts['foi_answered']} |
| FOI total rows | ~{counts['foi_queue.csv']} |
| research_queue | ~{counts['research_queue.csv']} (open: rq_116 deferred + hole-fill after progress) |

### What improved since tick 430

- **SPP IS / CPAS (tick431):** federal DIS+loi1965 **€2.241bn** · unemp compensation **€300m** path vs SPP IS understate.
- **Entity I social + provisions (tick432):** handicap+IGO+RIS **€6.5bn** · provision gen **€829.8m** L5.
- **SS consol 2026 (tick433):** dep **€147.86bn** prest L5 · demission cost **€33.6m** · credit familial **€40m**.
- **Pension reform L5 (tick434):** save **€807→2,229m** 2027-30 full measure matrix.
- **RTW + chomage waves (tick435):** RTW **€203→1,929m** · exits **90.2k** · UI exclusions **193.9k** regional.
- **Fedasil/coop/ONSS (tick436):** Fedasil **0→688m** · coop **1.13→0.96bn** · altfin multi-year **25→27.2bn**.
- **Sante/NATO/Justice (tick437):** INAMI save **€764.5m** L5 · NATO **12.7→14.3bn** · Justice provisions **€465.5m**.
- **IPP annex L5 (tick438):** full measure path **−421m→−5.4bn** · entity split · emp-rate gap **3.7pp**.
- **Personnel austerity (tick439):** replace **100→175m** · statutaire cotis **10/284/365m** · specialty **20.1bn** Defence transfer.

---

## Snapshot at **tick 430** (2026-08-02) — archived

| Layer | Coverage of €347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE €347.956bn; dual EDP/COM path) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS deficits dual EDP |
| **C. L2 entity totals** | **~98–99%** (order of magnitude) | **+** SPF SS macro **€146.8bn** 2025 · DG HAN **€2.93bn** · FPD **€69.05bn** + menage **€5.92bn** · INAMI inv **~€10.64bn** · primaire **€2.86bn** · mat/pat **€0.87bn** |
| **D. L5 named end-receivers** | **~23–36%** of TE (generous) | INAMI/FPD/DG HAN L5 fills; FOI ASBL/firm residual |
| **E. FOI-ready gaps** | **~215** drafts ready | answered **~9**; total FOI rows **~226** |

### Inventory (tick 430)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~6982 |
| commitments.csv | ~775 |
| leaderboard.csv | ~1229 |
| entities.csv | ~358 |
| sources.csv | ~749 |
| FOI ready | ~215 |
| FOI answered | ~9 |
| FOI total rows | ~226 |

---

## Method notes (unchanged)

- Coverage % for C/D is **order-of-magnitude judgment**, not a SQL sum of budgets.csv.
- Reform save/cost paths (pension, RTW, IPP, Fedasil) improve **transparency of policy euro claims** even when they are not TE end-receivers.
- FOI queue: humans send; agent drafts only.
"""

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **440** (2026-08-02) · **~{counts['leaderboard.csv']}** leaderboard rows  
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
| 2 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB package |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | fossil inventory |
| 4 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS multi-year |
| 5 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted  | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA TE layer B; face=wages; pure waste admin+DWL only |
| 6 | `lb_fed_fossil_company_cars_ehs_3_4bn` | Company cars EHS fossil inventory 3.43bn 2022 | **3.43 bn** | 8 | 9.0 | 7 | **8.35** | fossil inventory |
| 7 | `lb_fed_fossil_mazout_1_86bn` | Heating oil accise gap 1.86bn 2022 fossil inv | **1.86 bn** | 8 | 9.0 | 6 | **8.3** | fossil inventory |
| 8 | `lb_company_cars` | Company cars tax expenditure package | **3.14 bn** | 8 | 9.5 | 8 | **8.22** | Official FFS package |
| 9 | `lb_eiwt_package` | EIWT partial remittance bedrijfsvoorheffing package | **4.36 bn** | 7 | 9.5 | 6 | **8.08** | Top wage-subsidy instrument |
| 10 | `lb_eiwt_night_shift_cluster` | EIWT night+shift+continuous+construction cluster | **2.04 bn** | 7 | 9.5 | 6 | **8.08** | ~2.04bn 2024 cluster |

**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter:** Hedera CAP (~15bn) / ETS blocked (€1.8bn) stay **off** pure annual top10 when annual=0.  
**Stable vs tick 430:** fossil/company-cars/cheque/EIWT mega items still dominate top10; **no reorder**. Ticks 431–439 filled **reform paths** (pens/RTW/IPP/sante/Fedasil/NATO/personnel) and **SS/Entity I maps** — core entitlement and policy transparency, not waste-first reordering.

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| 11 | `lb_taxex_fed_29_7bn` | **29.7 bn** | 8.05 | Federal TE inventory 2023 (off-TE pie) |
| 12 | `lb_vl_gsc_support` | **822.0 m** | 8.0 | Flanders GSC |
| 13 | `lb_wage_subsidies_block` | **16.70 bn** | 7.98 | Wage subsidies block |
| 14 | `lb_specialty_defence_transfer_20bn` | **20.1 bn** | **8.0** | **NEW tick439** specialty breach (control) |
| 15 | `lb_nato_asset_optim_3_17bn` | **3.17 bn** | **7.8** | **NEW tick437** opaque asset optim |
| 16 | `lb_nato_cit_russian_path` | **1.16 bn** | **7.1** | **NEW tick437** frozen-asset CIT path |
| 17 | `lb_rtw_recontrol_1_07bn_2029` | **1.07 bn** | **7.4** | **NEW tick435** RTW recontrol path |
| 18 | `lb_emp_rate_gap_78_vs_74` | gap **3.7pp** | **7.2** | **NEW tick438** return-effect credibility |
| 19 | `lb_fpd_legal_pensions_69bn_2025` | **69.05 bn** | **6.9** | Legal pensions (core entitlement) |
| 20 | `lb_ss_total_146_8bn_2025` | **146.8 bn** | **6.5** | SS macro |

### Large stock / off-TE / dual-structure / reform map (not pure annual waste top 10)

| ID | Stock / envelope / peak | Note |
|-----|------------------:|------|
| `lb_hedera_cap_15bn` | **~15 bn** CAP | Phoenix nuclear waste finance stock |
| `lb_ets_blocked_1_8bn` | **1.8 bn** | ETS auction proceeds blocked SPF Santé |
| `lb_lpm_invest_33_8bn_2026_34` | **33.8 bn** eng | Military programming 2026–34 |
| `lb_edp_gg_debt_692_5bn_2025` | **692.5 bn** | GG Maastricht debt 107.9% GDP |
| `lb_ss_total_146_8bn_2025` / consol 2026 | **146.8 / 147.9 bn** | SS macro |
| `lb_fpd_legal_pensions_69bn_2025` | **69.05 bn** | Legal pensions three regimes |
| `lb_pens_reform_total_path_2_23bn` | **0.81→2.23 bn** | Pension reform save path 2027-30 |
| `lb_rtw_total_1_93bn_2029_l5` | **0.20→1.93 bn** | RTW invalidity plan |
| `lb_ipp_reform_path_5_5bn_l5` | **−0.42→−5.4 bn** | IPP reform cost path |
| `lb_nato_extra_16_8bn_path` | **16.78 bn** | Defence extra 2025-29 |
| `lb_fedasil_save_path_688m` | **0→688 m** | Asylum tightening path |
| `lb_chom_wave_exclusions_193k` | **193.9 k** persons | UI exclusion waves 2026-27 |

### High-absurdity honourable mentions (not top-10 cost)

| ID | Note |
|----|------|
| `lb_specialty_defence_transfer_20bn` | Full eng redistribution without parliament |
| `lb_rtw_psycho_roi_fragile` | ROI study not on invalid population |
| `lb_prison_food_underfund_10m` | Structural under-budgeting to provisions |
| `lb_vvpr_anticipation_spike` | 1.21bn front-load before 18% rate |

---

**Refresh rule:** recompute at each multiple of 10 ticks or when human asks “waste top / progress”.
"""

(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

# research_queue
with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())
for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: progress coverage % + waste top10 refresh; no new euro invent; "
            f"rq_116 SWA deferred"
        )
if not any(r.get("task_id") == "rq_432" for r in rq):
    rq.append(
        {
            "task_id": "rq_432",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": "",
            "notes": f"Spawned tick{TICK} after progress @440; rq_116 SWA deferred",
        }
    )
with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsf = list(ls[0].keys())
ls[-1]["last_tick_utc"] = NOW
ls[-1]["last_unit_id"] = UNIT
ls[-1]["ticks_completed"] = str(TICK)
ls[-1]["mode"] = "continuous"
ls[-1]["current_sprint"] = "hole_fill"
ls[-1]["paused"] = "no"
ls[-1]["notes"] = (
    f"Scheduler 60s. Next prio5 rq_432; rq_116 SWA deferred. "
    f"tick{TICK} progress coverage + top10."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (**progress milestone @440** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~98-99%** - SS consol 147.86 · Entity I social 6.5 · SPP IS 2.24 · NATO 13.1 · Fedasil 0.80 · coop 1.04 · liq 92
  - **D L5:** **~24-37%** generous (reform-measure L5: pens 0.8-2.2 · RTW 0.2-1.9 · sante 0.76 · IPP path · chom waves 194k; FOI ASBL/firm residual)
  - **E FOI ready:** **~{counts['foi_ready']}** (answered **~{counts['foi_answered']}**; total FOI rows **~{counts['foi_queue.csv']}**)
- Inventory: budgets ~{counts['budgets.csv']} · cmt ~{counts['commitments.csv']} · lb ~{counts['leaderboard.csv']} · entities ~{counts['entities.csv']} · sources ~{counts['sources.csv']}
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; reform maps off pure waste top10
- Dual/off-TE: SS 147.9bn; IPP -5.4bn path; NATO extra 16.8bn; taxex 29.7bn
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_431=done; spawn **rq_432**; ticks={TICK}
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_432** hole-fill; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} inventory={counts}")

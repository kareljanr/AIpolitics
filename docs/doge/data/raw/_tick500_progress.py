# tick500 — progress coverage % + waste top10 refresh (no invent euros)
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
prog_path = root / "progress_every_10_ticks.md"
old = prog_path.read_text(encoding="utf-8")
marker = "## Snapshot at **tick 490**"
idx = old.find(marker)
if idx < 0:
    raise SystemExit("tick 490 marker missing")
header = old[:idx]
rest = old[idx:].replace(
    "## Snapshot at **tick 490** (2026-07-28)",
    "## Snapshot at **tick 490** (2026-07-28) — archived",
    1,
)

new_snap = """## Snapshot at **tick 500** (2026-07-28)

| Layer | Coverage of €347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE €347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** CoA Entity II aju quartet complete (FWB/WAL/DG) · VL Onderwijs **17.25bn** · VL certified RR2025 outturn/debt · GIP **3.685bn** class · prison DBFM follow-up |
| **D. L5 named / measure end-lines** | **~30–43%** of TE (generous) | **Gain 490→500 is CoA dual education + Entity II aju + VL certified accounts:** prison DBFM Antwerp fees · GIP actualisatie **3.685bn** / bike **220m** · FWB SEC aju **−1.753bn** economies **254→733m** · WAL SEC aju **−2.015bn** debt **30.7→33.0bn** · DG ESVG **−0.11bn** debt path **1.47bn** · FWB Cepage IT **35–96m** unsubstantiated + Etnic **~118m** · VL Persona **16m** cancelled dual · VL OV savings **~322m** · AVB **52.2m** + inductie **48.7m** + bonus **24.7m** · VL RR ESR **−3.98bn** / Maastricht **50.2bn** (+**8.4bn**) / Zaventem PMV **2.55bn** / nonbudget debt **1.07bn** / Toekomstverbond **3.85bn** · FOI still bulk named ASBL/firm + debt bridge L5 |
| **E. FOI-ready gaps** | **~248** drafts ready | Human send only; answered **~9**; total FOI rows **~259** (+ debt bridge, Persona, AVB, Cepage, WAL fiches, DG infra, FWB economies programme, …) |

**Off-TE (do not mix into 348 bn):** federal taxex **€29.7bn** · company cars/cheque/EIWT · lottery player stakes · FPB *options* (not adopted budget) · Tax Shelter · private PPP · equity injections (Zaventem) are debt/finance not TE flow.

### Inventory (tick 500)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~8685 |
| commitments.csv | ~914 |
| leaderboard.csv | ~1697 |
| entities.csv | ~411 |
| sources.csv | ~936 |
| FOI ready | ~248 |
| FOI answered | ~9 |
| FOI total rows | ~259 |
| research_queue | ~486 (open: rq_116 deferred + hole-fill after progress) |

### What improved since tick 490

- **CoA prison DBFM + GIP (tick491–492):** Antwerp DBFM fees/VFM dual VL PPP · GIP actualisatie **€3.685bn** class + bike **€220m** dual SOFICO.
- **Entity II aju complete (tick493–495):** FWB SEC **−1.753bn** economies **254→733m** · WAL SEC **−2.015bn** debt **30.7bn** eoy25 path **33.0** · DG ESVG **−0.11bn** debt path **1.47bn** · dual quartet residual map closed with DG.
- **Dual education IT + OV (tick496–498):** FWB Cepage **35–96m** uncosted under personnel **€7.1bn** · VL Persona **€16m** stop · VL OV **€17.25bn** + savings **~€322m** · AVB+inductie **>€100m** + bonus **€24.7m**.
- **VL certified accounts (tick499):** ESR **−€3.98bn** · Maastricht **€50.2bn** (+**€8.4bn**) · Zaventem/PMV **€2.55bn** · nonbudget debt build **€1.07bn** FOI · Toekomstverbond cum **€3.85bn**.

---

"""

prog_path.write_text(header + new_snap + rest, encoding="utf-8")
print("progress OK")

waste_path = root / "doge_waste_top10_current.md"
waste_path.write_text(
    """# DOGE waste ranking — current top 10

**As-of:** tick **500** (2026-07-28) · **~1697** leaderboard rows  
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
**Stock filter:** Hedera CAP (~15bn, pi 8.25 annual=0) / ETS blocked (€1.8bn) / VL Maastricht debt stock (€50.2bn annual=0) stay **off** pure annual top10.  
**Stable vs tick 490:** fossil/company-cars/cheque/EIWT mega items still dominate top10; **no reorder**. Ticks 491–499 filled **CoA dual Entity II aju + education IT/OV + VL certified RR2025** (Zaventem **2.55bn** equity · debt **+8.4bn** · Cepage/Persona IT · starter **>100m**) — transparency/governance gains, not waste-first reordering of taxex giants.

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| 11 | `lb_taxex_fed_29_7bn` | **29.7 bn** | 8.05 | Federal TE inventory 2023 (off-TE pie) |
| 12 | `lb_specialty_defence_transfer_20bn` | **20.1 bn** | **8.0** | Specialty breach (control) |
| 13 | `lb_vl_gsc_support` | **822.0 m** | 8.0 | Flanders GSC |
| 14 | `lb_wage_subsidies_block` | **16.70 bn** | 7.98 | Wage subsidies block |
| 15 | `lb_cm_e1_control_gap_7_7bn` / dual map | **7.7 bn** residual | high cost | Entity I control-account residual 2029 |
| 16 | `lb_vl_debt_50_2bn_2025` | stock **50.2 bn** | high stock | **NEW 499** VL Maastricht debt eoy2025 (+8.4bn) |
| 17 | `lb_vl_zaventem_pmv_2_55bn` | **2.55 bn** | mid-high | **NEW 499** PMV BAC capital injection |
| 18 | `lb_vl_nonbudget_debt_1_07bn` | **1.07 bn** | **7.25** abs-heavy | **NEW 499** debt-saldo opacity FOI |
| 19 | `lb_fwb_cepage_96m_est` / `lb_vl_persona_16m` | **35–96m / 16m** | **7.25 / 7.35** | **NEW 496–497** dual education IT mega-failures |
| 20 | `lb_vl_ov_17_25bn_2026` | **17.25 bn** | mid (core) | **NEW 497** VL Onderwijs VAK (entitlement mass) |

### Large stock / off-TE / dual-structure / reform map (not pure annual waste top 10)

| ID | Stock / envelope / peak | Note |
|-----|------------------:|------|
| `lb_hedera_cap_15bn` | **~15 bn** CAP | Phoenix nuclear waste finance stock (pi 8.25; annual 0) |
| `lb_ets_blocked_1_8bn` | **1.8 bn** | ETS auction proceeds blocked SPF Santé |
| `lb_lpm_invest_33_8bn_2026_34` | **33.8 bn** eng | Military programming 2026–34 |
| `lb_edp_gg_debt_692_5bn_2025` | **692.5 bn** | GG Maastricht debt 107.9% GDP |
| `lb_vl_debt_50_2bn_2025` | **50.2 bn** | VL Maastricht eoy2025 CoA RR |
| `lb_ss_total_146_8bn_2025` / consol 2026 | **146.8 / 147.9 bn** | SS macro |
| `lb_cm_e1_path_def_38bn_2029` | **38.3 bn** def | Entity I deficit path CM Jul 2026 |
| `lb_vl_toekomstverbond_3_85bn` | **3.85 bn** cum | Lantis/Oosterweel financing stock |
| `lb_gip` class / CoA 2026_27 | **~3.7 bn** | VL GIP actualisatie dual SOFICO |
| `lb_nl_society_385m_2025` | **385 m** | Lottery society dual (doelen+rent) |

### High-absurdity honourable mentions (not top-10 cost)

| ID | Note |
|----|------|
| `lb_vl_wassalon_podcast` | abs 9.5 — micro culture absurdity flag |
| `lb_ipolice_spent_77m_cancelled` | abs 9.0 — cancelled IT mega-project 76.7m spent |
| `lb_vl_persona_16m` / `lb_fwb_cepage_96m_est` | dual education payroll IT failures |
| `lb_vl_kunsten_neg_advice_9` | expert reject then minister fund (CoA 2026_36) |
| `lb_vl_nonbudget_debt_1_07bn` | Parliament under-informed on debt bridge |
| `lb_specialty_defence_transfer_20bn` | Full eng redistribution without parliament |
| `lb_prison_food_underfund_10m` | Structural under-budgeting to provisions |
| `lb_vvpr_anticipation_spike` | 1.21bn front-load before 18% rate |

---

**Refresh rule:** recompute at each multiple of 10 ticks or when human asks “waste top / progress”.
""",
    encoding="utf-8",
)
print("waste OK")

# research_queue: close rq_491, spawn rq_492
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old_rq = (
    "rq_491,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T20:30:00Z,,Spawned tick499 after CoA VL Rekeningenrapport 2025; progress@500 next tick; rq_116 deferred"
)
new_rq = (
    "rq_491,Progress milestone @500 coverage % + waste top10,continuous,5,done,L5,gg_belgium,"
    "Refresh progress_every_10_ticks.md + doge_waste_top10_current.md; no invent euros.,,"
    "2026-07-28T20:30:00Z,2026-07-28T20:50:00Z,"
    "tick500: progress A100 B100 C~99 D~30-43 E~248 ready; CoA dual wave 491-499; waste top10 stable; rq_116 deferred"
)
if old_rq not in text:
    raise SystemExit("rq_491 row not found")
text = text.replace(old_rq, new_rq)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_492,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T20:50:00Z,,Spawned tick500 after progress@500; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T20:50:00Z,rq_491,500,no,"
    "Tick500 progress@500 coverage+waste top10; next prio5 rq_492; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("queue+state OK")

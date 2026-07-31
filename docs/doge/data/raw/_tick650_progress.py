# -*- coding: utf-8 -*-
"""Tick 650 PROGRESS MILESTONE: coverage % + waste top10 + dual wave 641-649 — rq_641."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
PROGRESS = ROOT / "progress_every_10_ticks.md"
WASTE = ROOT / "doge_waste_top10_current.md"
NOW = "2026-08-01T04:15:00Z"
TICK = 650
RQ = "rq_641"
NEXT_RQ = "rq_642"
GAP = "gap_dual_coa_wave_641_650_l5_2025"


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


def append_rows(path: Path, rows: list[str]) -> int:
    text = read_text(path)
    existing = text
    added = 0
    for row in rows:
        key = row.split(",", 1)[0]
        if key and any(
            L.startswith(key + ",") or L.startswith("\ufeff" + key + ",")
            for L in existing.splitlines()
        ):
            print(f"SKIP exists {key}")
            continue
        if not text.endswith("\n"):
            text += "\n"
        text += row + "\n"
        existing = text
        added += 1
        print(f"ADD {key}")
    path.write_bytes(text.encode("utf-8"))
    return added


def update_rq_done(path: Path, rq_id: str, notes: str) -> None:
    text = read_text(path)
    lines = text.splitlines()
    out = []
    for L in lines:
        if L.startswith(rq_id + ",") or L.startswith("\ufeff" + rq_id + ","):
            parts = L.split(",")
            if len(parts) >= 5:
                parts[4] = "done"
            if len(parts) >= 11:
                parts[10] = NOW
            if len(parts) >= 12:
                parts[11] = notes.replace(",", ";")
            else:
                parts.append(notes.replace(",", ";"))
            L = ",".join(parts)
            print(f"RQ done {rq_id}")
        out.append(L)
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


def spawn_rq(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    if any(L.startswith(key + ",") for L in text.splitlines()):
        print(f"SKIP spawn {key}")
        return
    if not text.endswith("\n"):
        text += "\n"
    text += row + "\n"
    path.write_bytes(text.encode("utf-8"))
    print(f"SPAWN {key}")


def set_loop_state(path: Path) -> None:
    header = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes"
    notes = (
        f"tick{TICK} progress coverage + waste top10; dual CoA wave 641-649; "
        f"next {NEXT_RQ}; progress@660 in 10; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


PROGRESS_SNAPSHOT = """
## Snapshot at **tick 650** (2026-08-01)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** CoA finance/recovery/UAP wave: DO10 PRW CL **2.274bn** · DO19 debt **2.146bn** · Ste-Émilie **4.671bn** + LSF **3.304bn** · UAP unites **-755m** · Encours **7.565bn** · OCPP after-corr **435m** · prior DO11–18 mega retained |
| **D. L5 named / measure end-lines** | **~45-58%** of TE (generous) | **Gain 640→650 is WAL CoA finance + recovery + UAP dual hole-fill:** DO19 direct debt **€30.0bn**/interest **€605m** dual VL · Ste-Émilie **€4.67bn** dual FWB · PRW/FRR CL **€2.255bn** dual VV · UAP type3 **-€207m** (OTW **-€139m**) · Encours incomplete **+€2.08bn** · OCPP requalif **€125m** · FA+MD **+€75m** · circulation **€779m** · FOI still bulk L5 awards + dual unit-cost matrices |
| **E. FOI-ready gaps** | **~392** drafts ready | Human send only; answered **~9**; total FOI rows **~402** (+ DO15 agri · DO11 personnel · DO18 ZAE · DO19 debt · Ste-Émilie · DO10 PRW · UAP SEC · encours/SP · FA/OCPP · dual wave matrix · …) |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform *savings paths* · **gross financing / OLO** · **unconsol federal debt** · **WAL direct debt stock ~€30bn** / VL Maastricht **€50.2bn** · **encours stock €7.57bn** (+ incomplete **€2.08bn**) · **fonds stocks** (env **495m** · Kyoto **445m** · déchets **221m** · RDI **171m**) · UAP treasury remonte **€576m** · WE equity **~5bn** · SPAQuE/Sowaer BS · FRR/RePower receipts conditional.

### Inventory (tick 650)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~11878 |
| commitments.csv | ~1345 |
| leaderboard.csv | ~2612 |
| entities.csv | ~471 |
| sources.csv | ~1278 |
| FOI ready | ~392 |
| FOI answered | ~9 |
| FOI total rows | ~402 |
| research_queue open | rq_116 deferred + rq_642 hole-fill after progress |

### What improved since tick 640

- **Debt + financing (tick644–645):** DO19 CL **€2.146bn** / direct debt eoy2025est **€29.95bn** / interest **€605m** dual VL Maastricht · Recettes **€21.80bn** / Ste-Émilie **€4.67bn** / LSF competences **€3.30bn** dual FWB/fed.
- **Recovery + admin (tick641–643, 646):** DO15 agri CL **€605m** dual Landbouw/ANB · DO11 personnel CL **€888m** / SPW remun **€669m** · DO18 ZAE path **-€109m** + emploi pack **€3.14bn** dual VLAIO/VDAB · DO10 PRW+FRR CL **€2.255bn** dual VV (FRR rec **€920m** + RePower **€110m**).
- **UAP + stocks + financial ops (tick647–649):** UAP unites impact **-€755m** (type3 **-€207m** / AViQ **-€331m**) · Encours **€7.57bn** incomplete **+€2.08bn** + section part EU rec **€389m** dual EFRO · FA+MD **+€75m** / OCPP after-corr **€435m** / **requalif margin €125m** dual PMV · circulation **€779m**.

---

"""

WASTE_MD = """# DOGE waste ranking — current top 10

**As-of:** tick **650** (2026-08-01) · **~2612** leaderboard rows  
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
| 6 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO₂ vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | CoA CO₂ under-collection path |
| 7 | `lb_dual_cars_ssc_taxex` | Dual company car CO₂ SSC under-collection vs taxex | **0.28 bn** receipts class | 8.5 | 9.5 | 6 | **8.4** | dual SSC+taxex under-pricing |
| 8 | `lb_fed_fossil_company_cars_ehs_3_4bn` | Company cars EHS fossil inventory 3.43bn 2022 | **3.43 bn** | 8 | 9.0 | 7 | **8.35** | fossil inventory |
| 9 | `lb_cons_no_costbenefit_18bn` | No cost-benefit 78pct of consultancy 1.8bn sample | **0.60 bn** ann / **1.8 bn** class | 8.5 | 9.0 | 4 | **8.35** | CoA 101-contract compliance |
| 10 | `lb_fed_fossil_mazout_1_86bn` | Heating oil accise gap 1.86bn 2022 fossil inv | **1.86 bn** | 8 | 9.0 | 6 | **8.3** | fossil inventory |

**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter:** Metro3 overrun/gap · Hedera CAP · VL Maastricht debt · WAL direct debt **~€30bn** · encours **€7.57bn** · federal unconsol debt / gross financing · **Infrabel equity 20.5bn** · **WE equity ~5bn** · **fonds stocks** stay **off** pure annual top10 when annual=0 or finance-not-TE.  
**Change vs tick 640:** pure annual **top10 unchanged** (fossil/cars/cheque/consultancy). Gain 640-650 adds **WAL CoA finance/recovery/UAP dual wave** (PRW **€2.25bn**; debt **€30bn**/interest **€605m**; Ste-Émilie **€4.67bn**; UAP **-€755m**; encours **€7.57bn**; OCPP requalif **€125m**) that raise **L2 dual financing/recovery/UAP map** more than FFS ranking (see high-absurdity + dual tables).

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| 11 | `lb_company_cars` | **3.14 bn** | 8.22 | Official FFS package |
| 12 | `lb_cons_101_sample_2_2bn` | **0.73 / 2.2 bn** class | 8.15 | Systemic procurement failure |
| 13 | `lb_cons_exclusion_17bn` | **0.57 / 1.7 bn** class | 8.15 | Exclusion grounds unchecked 67% |
| 14 | `lb_eiwt_package` | **4.36 bn** | 8.08 | Top wage-subsidy instrument |
| 15 | `lb_eiwt_night_shift_cluster` | **2.04 bn** | 8.08 | ~2.04bn 2024 cluster |
| 16 | `lb_taxex_fed_29_7bn` | **29.7 bn** | 8.05 | Federal TE inventory 2023 (off-TE pie) |
| 17 | `lb_specialty_defence_transfer_20bn` | **20.1 bn** | **8.0** | Specialty breach (control) |
| 18 | `lb_vl_gsc_support` | **~0.8–1.1 bn** | 8.0 | Flanders GSC bill-side |
| 19 | `lb_wage_subsidies_block` | **16.7 bn** | 7.98 | Enterprise package ~2/3 |
| 20 | `lb_e1_nopol_financing_39bn` | **39.1 bn** counterfactual | **7.85** | no-policy financing 2029 |

### High-absurdity shortlist (not pure annual cost rank)

| ID | Abs | Note |
|----|----:|------|
| `lb_metro3_overrun_477pct` | **9.5** | +477% 0.82→4.76bn stock (prio **9.05** #1 raw) |
| `lb_vl_wassalon_podcast` | **9.5** | Small € high absurdity |
| `lb_metro3_financing_gap_4bn` | **9.0** | ~€4.3bn BCR residual stock |
| `lb_kenteken_sole_bidder_bpost` | **9.0** | sole bidder concession |
| `lb_ypto_proc_law_fail` | **9.0** | rail IT procurement |
| `lb_vlaio_prescription_16_4m` | **8.5** | eco write-offs solvent debtors |
| `lb_ocpp_requalif_125m_2025` | **7.5** | **NEW 649** OCPP requalif margin €125m |
| `lb_encours_incomplete_2_08bn_2023` | **7.5** | **NEW 648** CRAC/Sowafinal+déchets off-book |
| `lb_encours_7_57bn_2024` | **7.5** | **NEW 648** commitment stock €7.57bn |
| `lb_fwcn_obj_gap_165m_2025` | **6.5** | **NEW 647** FWCN obj −165 vs budget −63 |
| `lb_sowafinal3_specialty_breach_2025` | **7.0** | specialty breach DO16 residual |
| `lb_prw_122_cl_2_25bn_2025` | **7.0** | **NEW 646** PRW sticky CL vs eng collapse |

### Dual / DO mega map (not pure annual waste top 10)

| ID | Envelope / peak | Note |
|----|----------------:|------|
| `lb_do17_cl_9_52bn_2025` | **9.52 bn** | DO17 local social dual VAPH (prior 639) |
| `lb_ste_emilie_4_67bn_2025` | **4.67 bn** | **NEW 645** Ste-Émilie dual FWB |
| `lb_competences_lsf_3_30bn_2025` | **3.30 bn** | **NEW 645** LSF competences dual fed |
| `lb_do10_cl_2_27bn_2025` | **2.27 bn** | **NEW 646** DO10 Secretariat PRW-heavy |
| `lb_prw_122_cl_2_25bn_2025` | **2.25 bn** | **NEW 646** PRW+FRR dual VV |
| `lb_do19_dette` / interets class | **2.15 / 0.61 bn** | **NEW 644** DO19 debt dual VL |
| `lb_do14_cl_1_65bn_2025` | **1.65 bn** | DO14 mobility dual De Lijn |
| `lb_uap_unites_impact_755m_2025` | **0.76 bn** impact | **NEW 647** UAP SEC consol |
| `lb_ocpp_after_corr_435m_2025` | **0.44 bn** | **NEW 649** OCPP after GW corr |
| `lb_fiscal_circulation_779m_2025` | **0.78 bn** | **NEW 649** vehicle tax dual VL |
| `lb_dual_financing_wal_fwb_fed_2025` | dual | **NEW 645** Ste-Émilie/LSF dual |
| `lb_dual_prw_vv_recovery_2025` | dual | **NEW 646** PRW vs VV |
| `lb_dual_debt_wal_vl_2025` | dual | **NEW 644** debt dual |
| `lb_dual_uap_sec_wal_vl_2025` | dual | **NEW 647** UAP SEC dual |
| `lb_dual_encours_eu_wal_vl_2025` | dual | **NEW 648** encours/EU dual |
| `lb_dual_fa_ocpp_wal_vl_2025` | dual | **NEW 649** FA/OCPP dual |

### Large stock / off-TE / dual-structure / reform map (not pure annual waste top 10)

| ID | Stock / envelope / peak | Note |
|-----|------------------:|------|
| `lb_dual_pension_72bn` | **72.0 bn** benefits | emp+self+public pension stacks |
| `lb_vl_debt_50_2bn_2025` | **50.2 bn** Maastricht | VL debt eoy2025 |
| `lb_wal_dette_directe_30bn_2025` | **~30.0 bn** | **NEW 644** WAL direct debt eoy2025est |
| `lb_encours_7_57bn_2024` | **7.57 bn** stock | **NEW 648** unliquidated commitments |
| `lb_encours_incomplete_2_08bn_2023` | **2.08 bn** stock | **NEW 648** off-book CRAC/Sowafinal/déchets |
| `lb_e1_nopol_financing_39bn` / post 31bn | **39.1 / 31.2 bn** | nopol vs measures 2029 |
| `lb_fonds_prot_env_stock_495m_2025` | **0.50 bn** stock | largest WAL fonds stock |
| `lb_kyoto_wal_stock_445m_2025` | **0.45 bn** stock | Kyoto under-spend |
| `lb_we_group` equity class | **~5.0 bn** | WE holding dual PMV |
| `lb_infrabel_assets_25_7bn` / equity 20.5 | **25.7 / 20.5 bn** | infra SOE balance |
| `lb_riziv_care_39_7bn_2025` | **39.7 bn** | care authorized outturn |
"""


def write_progress() -> None:
    text = read_text(PROGRESS)
    marker = "## Snapshot at **tick 650**"
    if marker in text:
        print("SKIP progress already has tick 650")
        return
    insert_after = "**Honest claim:** A+B are essentially complete. C is large but incomplete. **D is still a small share of €348 bn** — that is structural (payroll, pensions, debt interest, formula grants are not “projects”).\n\n---\n"
    # try ascii-safe variants
    if insert_after not in text:
        # find first snapshot and insert before it
        idx = text.find("## Snapshot at **tick 640**")
        if idx < 0:
            idx = text.find("## Snapshot at")
        if idx < 0:
            raise SystemExit("cannot find insert point in progress file")
        new_text = text[:idx] + PROGRESS_SNAPSHOT.lstrip("\n") + text[idx:]
    else:
        idx = text.find(insert_after) + len(insert_after)
        new_text = text[:idx] + "\n" + PROGRESS_SNAPSHOT.lstrip("\n") + text[idx:]
    PROGRESS.write_bytes(new_text.encode("utf-8"))
    print("WROTE progress_every_10_ticks.md tick650 snapshot")


def write_waste() -> None:
    WASTE.write_bytes(WASTE_MD.encode("utf-8"))
    print("WROTE doge_waste_top10_current.md")


src_rows = [
    "src_progress_tick650_coa_wave,DOGE progress tick650 WAL CoA finance recovery UAP dual wave 641-649,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE progress synthesis CoA wave,2026-08-01,synthesis,Strong tick650: DO19 debt 30bn interest 605m; Ste Emilie 4.67bn LSF 3.30bn; DO10 PRW CL 2.255bn FRR 920m; UAP unites -755m type3 -207m; encours 7.57bn incomplete +2.08bn; OCPP requalif 125m FA+MD 75m; DO15/11/18 residual duals; not TE-additive inventory budgets~11878 cmt~1345 lb~2612 src~1278 ent~471 FOI ready~392",
]

cmt_rows = [
    'cmt_dual_coa_wave_641_650,Dual WAL CoA finance recovery UAP wave ticks641-649,wallonie_gov,WAL DO finance recovery UAP dual VL FWB,CoA Budget RW 2024_63 multi-chapter,2024-11-15,2025,2025,0,"{""do19_debt_bn"":29.95,""interest_m"":605.2,""ste_emilie_bn"":4.671,""lsf_bn"":3.304,""prw_cl_bn"":2.255,""frr_rec_m"":920,""uap_unites_m"":-755.157,""encours_bn"":7.565,""ocpp_requalif_m"":125.37,""fa_md_m"":74.767,""note"":""Strong multi-tick synthesis primary CoA; not TE-additive""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,CoA dual finance recovery UAP map,FOI residual L5 matrix human send,src_progress_tick650_coa_wave,strong,Wallonie>CoA>wave_641_650,tick650 progress',
]

lb_rows = [
    "lb_dual_coa_wave_641_650,Dual WAL CoA finance recovery UAP wave 641-650,Belgium,ops,Belgium>CoA>dual_wave_641_650,0,0,Strong synthesis: debt 30bn PRW 2.25bn Ste-Emilie 4.67bn UAP -755m encours 7.57bn OCPP requalif 125m dual VL/FWB/VV/PMV; not TE-additive,strong,src_progress_tick650_coa_wave,BE regional taxpayers,CoA dual wave map progress@650,L2 map gain not FFS top10 shift,6.5,8.5,4,6.95,FOI residual L5 matrix,seed,,tick650",
]

foi_row = (
    f"{GAP},Wallonie>CoA>wave_641_650>L5_matrix,wallonie_gov,"
    "Residual L5 matrix across DO15/11/18/19/10 UAP encours OCPP FA: project lists "
    "debt sensitivity PRW milestones FWCN gap OTW invest SEC requalif map dual VL,"
    "Progress@650 synthesis strong totals; L5 residual dual,"
    "5,SPW Budget / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_dual_coa_wave_641_650,lb_dual_coa_wave_641_650,"
    f"{NOW},{NOW},tick650 progress synthesis; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** CoA Budget RW dual wave ticks 641–649 synthesis (progress@650)

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — matrice L5 résiduelle vague CoA 2025
        (dette / PRW / UAP / encours / OCPP)

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om une matrice
L5 consolidée (CSV/XLSX) couvrant:

1. DO19: sensibilité taux dette + plan emprunts vs Coret 3,3 mrd.
2. PRW/FRR prog 122: projets + jalons Commission (recettes FRR 920 mEUR).
3. UAP: objectifs SEC 146 institutions vs exécution (écart FWCN −165/−63).
4. Encours: inclusion CRAC/Sowafinal 2,0 mrd + promesses déchets 77 mEUR.
5. OCPP: marge de requalification 125,4 mEUR ligne par ligne.
6. Dual: tables de comparaison avec équivalents flamands (dette,
   Veerkracht, PMV, EFRO) si disponibles côté SPW.

Période: 2023-01-01 à 2026-12-31.

Cordialement,
[Naam]
```

## Notes (internal)

- Progress@650 synthesis; individual FOI drafts already ready per DO.
- Do **not** send as agent.
"""

log_entry = f"""
### {NOW} -- tick {TICK} (PROGRESS MILESTONE)
- Unit: {RQ} (progress@650 + dual CoA DO/finance/recovery/UAP wave synthesis ticks641-649)
- Found (synthesis strong, primary-sourced no invent euros):
  - **Debt + financing:** DO19 direct **EUR29.95bn** / interest **EUR605m** dual VL; Ste-Emilie **EUR4.67bn** + LSF **EUR3.30bn** dual FWB
  - **Recovery + admin:** DO10 PRW CL **EUR2.255bn** / FRR **EUR920m** dual VV; DO18 emploi pack **EUR3.14bn** / ZAE path **-EUR109m**; DO11 remun **EUR669m**; DO15 agri CL **EUR605m**
  - **UAP + stocks + financial ops:** UAP unites **-EUR755m** (type3 **-EUR207m** OTW **-EUR139m**); Encours **EUR7.57bn** incomplete **+EUR2.08bn**; OCPP requalif **EUR125m** / after-corr **EUR435m**; FA+MD **+EUR75m**
- Progress coverage:
  - **A/B:** 100% (L0 TE + L1 subsectors)
  - **C L2:** ~**99%** (+ PRW 2.27bn + debt 2.15bn + Ste-Emilie/LSF + UAP/encours/OCPP mega-fills)
  - **D L5:** ~**45-58%** generous (not near-complete of 348bn)
  - **E FOI ready:** ~**392** · answered ~**9** · total FOI rows ~**402**
- Inventory: budgets ~**11878** · cmt ~**1345** · lb ~**2612** · sources ~**1278** · entities ~**471**
- Waste top10: **unchanged** fossil/cars/cheque/consultancy (priority 8.55-8.30)
- High-abs + dual NEW: OCPP requalif 125m · encours incomplete 2.08bn · FWCN gap 165/63 · PRW 2.25bn · debt 30bn · Ste-Emilie 4.67bn
- Gain 640-650: WAL CoA finance/recovery/UAP dual wave (largest stock add = encours 7.57bn; largest transfer = Ste-Emilie 4.67bn)
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; cmt+lb+src dual wave; FOI {GAP} ready+draft; {RQ}=done spawn {NEXT_RQ}; ticks={TICK}
- FOI opened: {GAP} (ready, human send) - not sent
- Next: prio5 **{NEXT_RQ}**; deferred **rq_116**; progress@660 in 10 ticks
"""


def main() -> None:
    write_progress()
    write_waste()

    n_src = append_rows(ROOT / "sources.csv", src_rows)
    n_cmt = append_rows(ROOT / "commitments.csv", cmt_rows)
    n_lb = append_rows(ROOT / "leaderboard.csv", lb_rows)
    n_foi = append_rows(ROOT / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft_path = FOI_DRAFTS / f"{GAP}.md"
    if not draft_path.exists():
        draft_path.write_text(foi_draft, encoding="utf-8")
        print(f"WROTE draft {draft_path.name}")
    else:
        print(f"SKIP draft exists {draft_path.name}")

    update_rq_done(
        ROOT / "research_queue.csv",
        RQ,
        f"tick{TICK} progress@650 dual CoA wave 641-649; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after progress@650; rq_116 deferred; progress@660 in 10",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log_text = read_text(LOG)
    if f"-- tick {TICK}" not in log_text[-4000:]:
        if not log_text.endswith("\n"):
            log_text += "\n"
        log_text += log_entry
        LOG.write_bytes(log_text.encode("utf-8"))
        print("LOG appended")
    else:
        print("SKIP log already has tick")

    print(f"DONE tick{TICK}: src+{n_src} cmt+{n_cmt} lb+{n_lb} foi+{n_foi}")


if __name__ == "__main__":
    main()

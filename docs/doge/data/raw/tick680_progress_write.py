from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 680
utc = "2026-08-01T11:45:00Z"
src = "src_progress_tick680"
src_dual = "src_dual_wave_671_680_tick680"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

# Inventory (line counts include header)
inv = {
    "budgets": 13216,
    "commitments": 1506,
    "leaderboard": 2777,
    "entities": 528,
    "sources": 1341,
    "foi_ready": 423,  # +1 synthesis this tick
    "foi_answered": 9,
    "foi_total": 434,  # +1 this tick → was 433 rows data + header 434 file lines before; after +1 = 434 data? 
}
# file lines were: budgets 13217 incl header → 13216 data
# foi 434 lines incl header → 433 data; ready 422; after +1 FOI → 434 data, ready 423

# --- sources ---
src_rows = [
    f'{src},DOGE progress@680 coverage layers + waste top10 refresh,docs/doge/data/progress_every_10_ticks.md,DOGE loop,2026-08-01,synthesis,"Tick680: A/B 100%; C L2 ~99%; D L5 ~48-61% generous; E FOI ready ~423 answered ~9 total ~434; inventory budgets~13216 cmt~1506 lb~2777 ent~528 src~1341; wave671-679 dual fed+VL CoA residual"',
    f'{src_dual},Dual residual wave ticks671-679 VL BA + fed SS/energy/nonfiscal,{url},DOGE synthesis CoA dual,2026-08-01,synthesis,"Strong dual: VL debt 57bn Moody A1 + fonds 856m + WZC/Lantis; fed E1 path 24.5-36.2 + SS 148bn dual + energy 2.6bn + nonfiscal 7.83bn; not TE-additive; tick680"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

# light commitment + leaderboard synthesis rows
cmt_rows = [
    f'cmt_progress_tick680,Progress@680 dual fed/VL residual wave synthesis,gg_belgium,DOGE coverage,LOOP.md every 10 ticks,2026-08-01,2026,2026,0,"{{""tick"":680}}",,active,,Coverage milestone,Continue hole-fill,{src},strong,Belgium>progress>680,tick680',
    f'cmt_dual_wave_671_680,Dual VL BA + fed SS energy nonfiscal wave 671-679,gg_belgium,Fed+VL dual,CoA 2026_28+2026_22,2026-08-01,2026,2026,148026600000,"{{""ss_exp"":148026600000,""energy"":2600000000,""nonfiscal"":7829000000}}",,active,,Dual residual map,Not TE-additive,{src_dual},strong,Belgium>dual>wave680,tick680',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_progress_tick680_coverage,Progress@680 coverage snapshot,Belgium,ops,Belgium>progress>680,0,0,Synthesis: A/B 100 C~99 D~48-61 generous E FOI~423; top10 waste unchanged fossil/cars,strong,{src},researchers,Coverage dual,Primary synthesis,5.0,5.0,1,5.00,Continue L5 FOI,open,,tick680",
    f"lb_dual_wave_671_680_2026,Dual residual wave 671-679 fed+VL,Belgium,ops,Belgium>dual>wave680,148026600000,0,Strong dual: SS 148bn + energy 2.6bn + nonfiscal 7.83bn + VL debt 57bn fonds 856m; not TE-additive,strong,{src_dual},all entities,Wave dual residual,Primary dual,6.0,9.0,3,7.05,Cross FOI,open,,tick680",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

gap_id = "gap_dual_wave_671_680_l5_2026"
foi_row = (
    f"{gap_id},Belgium>dual>wave_671_680_L5,gg_belgium,"
    "Cross-entity L5 still opaque after wave: VL fonds per-fund cash + Klimaat eng table; Energiefonds desaffect 46/56; Phoenix CfD strike; energy assign 1.4bn L5; SS reductions beneficiary; SFPIM dividend budget correction; Finocas capital calendar; Lantis loan herijk; RIZIV save miss 183,"
    "Progress@680 dual wave synthesis; FOI batch residual,"
    "5,FOD BOSA / openbaarheid Vlaanderen / FOD Economie / FOD SZ,"
    "openbaarheid@bosa.be,https://bosa.belgium.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_dual_wave_671_680|cmt_progress_tick680,"
    "lb_dual_wave_671_680_2026|lb_energy_assign_opacity_1_4bn|lb_phoenix_cfd_583_6m_strike_gap,"
    f"{utc},{utc},tick680 progress synthesis; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

# research_queue
rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_671,"):
        out.append(
            "rq_671,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,sec_federal,"
            "PROGRESS@680: refresh progress_every_10_ticks.md + doge_waste_top10_current.md; synthesize residual wave ticks671-679 dual fed/VL; spawn next hole-fill.,,"
            f"2026-08-01T11:30:00Z,{utc},"
            "tick680 progress@680 coverage + waste top10; dual wave 671-679 synthesis; FOI gap_dual_wave_671_680_l5_2026 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_672,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Next residual after progress@680: SS other receipts L5 CoA or fed primary exp cells residual or VL GIP/Lantis FOI-adjacent deepen.,,"
    f"{utc},,spawned tick680 after rq_671 progress"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_671,680,no,"
    "tick680 PROGRESS coverage C~99 D~48-61 FOI~423; dual wave 671-679; next rq_672; progress@690 in 10; rq_116 deferred\n",
    encoding="utf-8",
)

# FOI draft
draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** DOGE progress@680 synthesis; CoA 2026_22 + 2026_28 primary wave ticks 671–679

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: FOD BOSA / openbaarheid Vlaanderen / FOD Economie / FOD Sociale Zekerheid
openbaarheid@bosa.be

Betreft: Openbaarheid — residual L5 na duale CoA-golf 2026 (fed+VL)

Geachte,

Op grond van de toepasselijke openbaarheidsregels verzoek ik om de nog
ontbrekende L5-documenten die na de openbare CoA-publicaties 2026_22 en
2026_28 residual blijven:

1. **Vlaanderen begrotingsfondsen**: cash per fonds 2024–2026 +
   historische engagemententabel Klimaatfonds (cum. tekort ~54 mEUR) +
   reconciliatie Energiefonds-desaffectatie 46,2 vs 56,2 mEUR.
2. **Federale energie**: toewijzingsfondsen CREG/Elia/NIRAS/Hedera L5 +
   Phoenix CfD-uitoefenprijs en sensitiviteit t.o.v. 583,6 mEUR.
3. **Sociale zekerheid**: top begunstigden bijdrageverminderingen
   (5,14 mld) en RIZIV-besparingsrest 183 mEUR (geneesmiddelen 145,7).
4. **SFPIM**: dividendakte 78,4 mEUR vs begroting 55,8 mEUR.
5. **Finocas / Lantis**: kapitaalkalender 177,5 mEUR en herijking
   lening 1,65 mld / overnamepad 2,82 mld.

Publieke steun: Rekenhof 2026_22 en 2026_28; DOGE progress tick 680.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Batch residual after progress@680; individual gap drafts remain authoritative for detail.
- Tick 680.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

# --- progress_every_10_ticks.md: prepend snapshot after header block ---
progress_path = data / "progress_every_10_ticks.md"
old = progress_path.read_text(encoding="utf-8")
marker = "## Snapshot at **tick 670**"
snap680 = """## Snapshot at **tick 680** (2026-08-01)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** dual fed+VL CoA residual: SS consol **€148.0bn** rec/exp · RIZIV care **€43.9bn** · energy stack **€2.6bn** · nonfiscal **€7.83bn** · VL debt **€57.0bn** · VL dotaties **€34.8bn** · WZC **€2.74bn** · Lantis VAK **€2.48bn** · begrotingsfondsen end **€856.5m** · prior Entity II aju DO matrices retained |
| **D. L5 named / measure end-lines** | **~48-61%** of TE (generous) | **Gain 670→680 is dual VL BA2026 + fed SS/energy/nonfiscal residual:** VL Moody **A1**/Fitch **AA-** debt path **+€6.8bn** · GIP shortfall **€82.4m** · Digisprong raid **€24m** · MVP **€88m** · Lantis loan **€1.65bn**/herijk **€2.82bn** · E1 deficit path **€24.5→36.2bn** · interest **€12.3→17.5bn** · RIZIV save miss **€183m** · AO slip **−€129m** · Elia GSC **€552m**+CRM **€170m** · Phoenix CfD strike unknown **€584m** · energy assign opacity **€1.4bn** · SS alt fin **€27.6bn** · RSZ-GB deficit settle **€547.5m** · Klimaat cum deficit **~€54m** · Energiefonds desaffect **46.2 vs 56.2** · SFPIM dividend underbook **€22.6m** · FOI still bulk L5 awards + dual unit-cost matrices |
| **E. FOI-ready gaps** | **~423** drafts ready | Human send only; answered **~9**; total FOI rows **~434** (+ VL residual · receipts/Omgeving · WVG/Lantis · E1 path/pension · SS RIZIV/AO · energy ch4 · SS receipts · begrotingsfondsen · nonfiscal/SFPIM · dual wave 671–680 · …) |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform *savings paths* · **gross financing / OLO** · **unconsol federal debt / E1 path €24.5–36.2bn** · **VL Maastricht/consol debt ~€50–57bn** · **WAL direct debt ~€30–34bn** / **FWB ~€14–21bn path** · **Hedera CAP €15bn** · **Phoenix CfD multi-year** · **VL begrotingsfondsen stocks ~€0.86bn** · **fonds stocks WAL** · UAP treasury remonte · WE equity **~5bn** · FRR/RePower conditional · **CSF NPE growth caps** · Moody rating actions (not euros).

### Inventory (tick 680)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~13216 |
| commitments.csv | ~1506 |
| leaderboard.csv | ~2777 |
| entities.csv | ~528 |
| sources.csv | ~1341 |
| FOI ready | ~423 |
| FOI answered | ~9 |
| FOI total rows | ~434 |
| research_queue open | rq_116 deferred + rq_672 hole-fill after progress |

### What improved since tick 670

- **VL BA2026 residual (tick671–673, 678):** debt consol **€56.97bn** / ratings Fitch **AA-** Moody **A1** S&P **AA-** dual WAL **Baa1** FWB **A3** · Finocas **€177.5m** unclear · Viapass **€99.3m** · Digisprong raid **€24m** · GIP shortfall **€82.4m** · dotaties **€34.82bn** · opcentiemen **€10.79bn** · MVP+EPC **€88.2m** · WZC **€2.74bn** CoA gap **€35.9m** · Lantis VAK **€2.48bn** / loan **€1.65bn** herijk **€2.82bn** · **begrotingsfondsen** end **€856.5m** (Klimaat cum deficit **~€54m**; Energie desaffect **46.2 vs 56.2**; buffer **+€58.5m**; index under **€48.3+7.0m**).
- **Federal E1 + SS (tick674–675, 677):** E1 deficit aju **€24.5bn** path **€36.2bn 2029** · interest **€12.3→17.5bn** · BE vs MTFSP gap **−2.5pp** · SS exp **€148.027bn** / rec **€148.002bn** near-balance · RIZIV care **€43.857bn** save miss **€183m**/€801m · AO slip **−€129m** path **−€323m 2029** · alt finance **€27.583bn** (BTW **€19.6bn** + RV **€7.9bn**) · RSZ-GB dots **€8.66bn** / evenwicht settle **−€547.5m** · contribution reductions **€5.14bn**.
- **Energy + nonfiscal (tick676, 679):** energy stack **~€2.6bn** (DG **1.2** + assign **1.4**) · Elia GSC **€552m** + CRM **€169.9m** · Phoenix CfD **€583.6m** strike unknown · nonfiscal **€7.83–7.85bn** · customs retention **€1.014bn** · SFPIM dividend **€78.4m** underbooked **€22.6m** · CREG refund **€285m** path **€412m**.
- **Dual map:** Entity II ratings **A1 / Baa1 / A3** · SS care dual AViQ/WVG · energy dual VEKA/GSC · SFPIM vs Finocas holdings · near-balance SS rec/exp.

---

"""

if marker in old:
    new_progress = old.replace(marker, snap680 + marker, 1)
else:
    # insert after first --- following how-to-read
    new_progress = old
    # fallback: after line with Honest claim
    key = "**Honest claim:**"
    idx = old.find(key)
    if idx >= 0:
        # find next --- after honest claim section
        rest = old[idx:]
        dash = rest.find("\n---\n")
        if dash >= 0:
            pos = idx + dash + len("\n---\n")
            new_progress = old[:pos] + "\n" + snap680 + old[pos:]
progress_path.write_text(new_progress, encoding="utf-8")

# --- waste top10 ---
waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **680** (2026-08-01) · **~2777** leaderboard rows  
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
**Stock filter:** Metro3 overrun/gap · Hedera CAP · VL Maastricht/consol debt **~€50–57bn** · WAL direct debt **~€30–34bn** · FWB direct debt **~€14–21bn path** · encours stocks · federal unconsol debt / E1 path / gross financing · **Infrabel equity 20.5bn** · **WE equity ~5bn** · **SACA report / fonds stocks** · **SS consol 148bn** stay **off** pure annual top10 when annual=0, finance-not-TE, or structural entitlement mega without waste framing.  
**Change vs tick 670:** pure annual **top10 unchanged** (fossil/cars/cheque/consultancy). Gain 670–680 adds **dual VL BA + fed SS/energy/nonfiscal residual** (VL debt **€57bn** Moody **A1**; SS **€148bn** near-balance; energy assign **€1.4bn** opacity prio **7.85**; Phoenix CfD strike gap; Klimaat cum deficit **~€54m**; SFPIM underbook **€22.6m**) that raise **L2 dual map** more than FFS ranking (see high-absurdity + dual tables).

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
| 20 | `lb_energy_assign_opacity_1_4bn` | **1.4 bn** | **7.85** | **NEW 676** CoA assign opacity |

### High-absurdity shortlist (not pure annual cost rank)

| ID | Abs | Note |
|----|----:|------|
| `lb_metro3_overrun_477pct` | **9.5** | +477% 0.82→4.76bn stock (prio **9.05** #1 raw) |
| `lb_vl_wassalon_podcast` | **9.5** | Small € high absurdity |
| `lb_metro3_financing_gap_4bn` | **9.0** | ~€4.3bn BCR residual stock |
| `lb_kenteken_sole_bidder_bpost` | **9.0** | sole bidder concession |
| `lb_ypto_proc_law_fail` | **9.0** | rail IT procurement |
| `lb_employer_km_credit_opaque_2026` | **8.5** | **NEW 676** 20m/mo no FOD data |
| `lb_phoenix_cfd_583_6m_strike_gap` | **8.0** | **NEW 676** strike price unknown |
| `lb_energy_assign_opacity_1_4bn` | **8.0** | **NEW 676** toewijzingsfondsen opacity |
| `lb_vl_klimaat_cum_deficit_54m` | **8.0** | **NEW 678** surplus masks deficit |
| `lb_vl_digisprong_raid_24m_2026` | **8.0** | **NEW 671** provisie raided |
| `lb_bac_interest_79m_specialty_2026` | **8.0** | **NEW 672** via O&O provisie |
| `lb_lantis_loan_1650_herijk_2822` | **8.0** | **NEW 673** herijk takeover |
| `lb_riziv_save_miss_183m_2026` | **8.0** | **NEW 675** pharma 145.7 of miss |
| `lb_fwb_ecureuil_sec_85m_2026` | **8.0** | reserve misbooked (prior 669) |
| `lb_be_mtfsp_gap_2_5pp_2029` | **8.0** | **NEW 674** path vs plan |

### Dual / mega map (not pure annual waste top 10)

| ID | Envelope / peak | Note |
|----|----------------:|------|
| `lb_ss_exp_148bn_2026` / `lb_ss_rec_148bn_2026` | **148 bn** | **NEW 675/677** SS near-balance dual |
| `lb_riziv_care_43_9bn_2026` | **43.9 bn** | **NEW 675** dual AViQ/WVG |
| `lb_fed_e1_path_36_2bn_2029` | **36.2 bn** | **NEW 674** E1 path 2029 |
| `lb_vl_dotaties_34_8bn_2026` | **34.8 bn** | **NEW 672** BFW dual |
| `lb_dual_e1_e2_path_2026` | **~32 bn** class | **NEW 674** E1+E2 saldo class |
| `lb_ss_alt_finance_27_6bn_2026` | **27.6 bn** | **NEW 677** BTW+RV assign |
| `lb_fed_interest_17_5bn_2029` | **17.5 bn** | **NEW 674** interest path |
| `lb_vl_opcentiemen_10_79bn_2026` | **10.8 bn** | **NEW 672** dual WAL IPP |
| `lb_fed_nonfiscal_7_83bn_2026` | **7.83 bn** | **NEW 679** nonfiscal dual |
| `lb_vl_debt_57bn_moody_a1_2026` | **57 bn** stock | **NEW 671** dual ratings |
| `lb_dual_energy_2_6bn_2026` | **2.6 bn** | **NEW 676** energy dual E2 |
| `lb_lantis_vak_2_48bn_2026` | **2.48 bn** | **NEW 673** dual Oosterweel |
| `lb_vl_begrotingsfondsen_856m_2026` | **0.86 bn** | **NEW 678** dual WAL fonds |
| `lb_do17_social_sante_9_89bn_2026` | **9.89 bn** | prior 666 WAL DO17 dual |

"""
(data / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

# loop log
entry = f"""
### {utc} — tick {tick} (PROGRESS MILESTONE)
- Unit: **rq_671** (progress@680 + dual residual wave synthesis ticks671–679)
- Found (synthesis strong, primary-sourced no invent euros):
  - **VL BA:** debt **€56.97bn** Moody **A1**/Fitch **AA-** · dotaties **€34.82bn** · opcentiemen **€10.79bn** · WZC **€2.74bn** · Lantis VAK **€2.48bn**/loan **€1.65bn** · fonds end **€856.5m** · Klimaat cum deficit **~€54m** · Energie desaffect **46.2 vs 56.2**
  - **Fed E1/SS:** deficit path **€24.5→36.2bn** · interest **€12.3→17.5bn** · SS rec/exp **€148.0bn** near-balance · RIZIV **€43.86bn** · alt fin **€27.58bn** · AO slip **−€129m** · save miss **€183m**
  - **Energy/nonfiscal:** stack **~€2.6bn** · Elia GSC **€552m**+CRM **€170m** · CfD **€584m** strike unknown · nonfiscal **€7.83bn** · customs retention **€1.01bn** · SFPIM div under **€22.6m**
  - **Dual:** ratings **A1/Baa1/A3** · SS care dual · energy dual · SFPIM/Finocas · Entity II aju retained
- Progress coverage:
  - **A/B:** 100% (L0 TE + L1 subsectors)
  - **C L2:** ~**99%** (+ SS 148bn + energy 2.6bn + nonfiscal 7.83bn + VL debt/fonds/WZC/Lantis)
  - **D L5:** ~**48-61%** generous (not near-complete of 348bn)
  - **E FOI ready:** ~**423** / answered ~**9** / total FOI rows ~**434**
- Inventory: budgets ~**13216** / cmt ~**1506** / lb ~**2777** / sources ~**1341** / entities ~**528**
- Waste top10: **unchanged** fossil/cars/cheque/consultancy (priority 8.55–8.30)
- High-abs + dual NEW: employer km opaque · Phoenix strike · energy assign 1.4bn · Klimaat deficit 54 · Digisprong raid · Lantis herijk · RIZIV save miss · E1 path 36.2 · SS 148bn · nonfiscal 7.83
- Gain 670–680: largest flow dual = SS **148bn** + energy **2.6bn** + nonfiscal **7.83bn** + VL dots **34.8bn**; largest stock = VL debt **57bn** + E1 path **36bn** + Lantis/Hedera off-TE
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; cmt+lb+src dual wave; FOI **gap_dual_wave_671_680_l5_2026** ready+draft; rq_671=done spawn **rq_672**; ticks=680
- FOI opened: gap_dual_wave_671_680_l5_2026 (ready, human send) — not sent
- Next: prio5 **rq_672**; deferred **rq_116**; progress@690 in 10 ticks
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick680 progress")
print("progress has 680:", "tick 680" in progress_path.read_text(encoding="utf-8"))
print("waste as-of:", [l for l in (data/"doge_waste_top10_current.md").read_text(encoding="utf-8").splitlines() if "As-of" in l][0])

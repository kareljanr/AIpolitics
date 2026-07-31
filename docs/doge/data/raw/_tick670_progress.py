# -*- coding: utf-8 -*-
"""Tick 670 PROGRESS MILESTONE: coverage % + waste top10 + dual aju WAL/FWB wave 661-669 — rq_661."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
PROGRESS = ROOT / "progress_every_10_ticks.md"
WASTE = ROOT / "doge_waste_top10_current.md"
NOW = "2026-08-01T09:15:00Z"
TICK = 670
RQ = "rq_661"
NEXT_RQ = "rq_662"
GAP = "gap_dual_aju_wave_661_670_l5_2026"
SRC = "src_dual_aju_wave_661_670_tick670"


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
        f"tick{TICK} progress coverage + waste top10; dual aju WAL/FWB wave 661-669; "
        f"next {NEXT_RQ}; progress@680 in 10; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


def update_foi(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    lines = text.splitlines()
    out = []
    found = False
    for L in lines:
        if L.startswith(key + ",") or L.startswith("\ufeff" + key + ","):
            out.append(row)
            found = True
            print(f"FOI update {key}")
        else:
            out.append(L)
    if not found:
        out.append(row)
        print(f"FOI add {key}")
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


PROGRESS_SNAPSHOT = """
## Snapshot at **tick 670** (2026-08-01)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** dual Entity II aju wave: WAL DO CL **21.94bn** · FWB DO CL **16.50bn** · WAL DO17 **9.89bn** / AViQ channel **7.05bn** · FWB DO52 **3.65bn** · FWB SACA CL **714m** · ONE **822m** · WAL SPW remun **741m** · PRW/FRR CL **1.73bn** · prior AViQ/CAF/CSF retained |
| **D. L5 named / measure end-lines** | **~47-60%** of TE (generous) | **Gain 660→670 is dual WAL+FWB CoA aju2026 residual:** WAL Moody **Baa1** debt path **€33.0bn**/interest **€754m** · FWB Moody **A3** debt **€16.2bn**/interest **€357m** · dual cabinets **€16.8m+€28.0m** · dual SEC aju **−€1.753bn/−€2.015bn** · Piebs eng **€400m** · CUR **€267m** · annex programmes · Job+/APE/CISP · digital no-plan **€10m** · Ecureuil reserve bookkeeping · FOI still bulk L5 awards + dual unit-cost matrices |
| **E. FOI-ready gaps** | **~408** drafts ready | Human send only; answered **~9**; total FOI rows **~422** (+ aju recettes/OTW · DO matrix · annex prog · FWB debt/DO · SACA/OAP · dual aju wave 661–670 · …) |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform *savings paths* · **gross financing / OLO** · **unconsol federal debt** · **WAL direct debt ~€30–34bn** / **FWB direct debt ~€14–21bn path** / VL Maastricht **€50.2bn** · **WAL encours €5.94bn** incomplete **+€1.94bn** / **FWB encours €863m** · **SACA report stocks €1.10→€0.73bn** · **fonds stocks** · UAP treasury remonte · WE equity **~5bn** · SPAQuE/Sowaer BS · FRR/RePower conditional · **CSF NPE growth caps** · Moody rating actions (not euros).

### Inventory (tick 670)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~12815 |
| commitments.csv | ~1447 |
| leaderboard.csv | ~2721 |
| entities.csv | ~517 |
| sources.csv | ~1318 |
| FOI ready | ~408 |
| FOI answered | ~9 |
| FOI total rows | ~422 |
| research_queue open | rq_116 deferred + rq_662 hole-fill after progress |

### What improved since tick 660

- **WAL aju2026 residual (tick663–667):** AViQ billing shock **+€198m** / Job+ **€32m** · provisions specialty **€1.22bn liq** · debt eoy2025 **€30.7bn** path **€33.0bn** / Moody **Baa1** / interest **€754m** · primes stock **€262m** · recettes **€22.09bn** / Ste-Émilie gap **€146m** / OTW capital **−€75m** · full **DO CE/CL matrix** (DO17 **€9.89bn** DO18 **€3.76bn**) · SPW remun **€740.8m** · Emploi Table13 **€3.13bn** · Annex cabinets **€28.0m** / PRW+FRR CL **€1.73bn** / DO17 sante **€7.05bn** / AWEX **€76.8m**.
- **FWB aju2026 dual (tick668–669):** full **DO matrix CL €16.50bn** (DO52 **€3.65bn** DO51 **€2.96bn** DO54 **€1.17bn**) · debt **€14.42→€16.20bn** / path **€20.6bn 2029** / Moody **A3** / interest **€357m** path **€561m** · cabinets **€16.8m** dual WAL **€28.0m** · dual SEC **−€3.77bn** · **SACA** solde **−€215m** report **€1.10→€0.73bn** · Piebs eng **€400m** · CUR CL **€267m** · ONE **€822m** · Etnic **€143m** · Ecureuil SEC **+€85m** reserve bookkeeping · encours **€863→€769m**.
- **Dual Entity II map:** Moody **Baa1 (WAL) vs A3 (FWB)** · cabinets dual · PRW/FRR vs FWB PRR/CUR · education dual (WAL emploi pack vs FWB DO51–55) · SACA/OAP vs WAL Type3.

---

"""

WASTE_MD = """# DOGE waste ranking — current top 10

**As-of:** tick **670** (2026-08-01) · **~2721** leaderboard rows  
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
**Stock filter:** Metro3 overrun/gap · Hedera CAP · VL Maastricht debt · WAL direct debt **~€30–34bn** · FWB direct debt **~€14–21bn path** · encours stocks · federal unconsol debt / gross financing · **Infrabel equity 20.5bn** · **WE equity ~5bn** · **SACA report / fonds stocks** stay **off** pure annual top10 when annual=0 or finance-not-TE.  
**Change vs tick 660:** pure annual **top10 unchanged** (fossil/cars/cheque/consultancy). Gain 660-670 adds **dual WAL+FWB CoA aju2026 residual wave** (WAL Moody **Baa1** / FWB Moody **A3**; dual SEC **−€3.77bn**; DO matrices **€21.9bn+€16.5bn**; SACA **−€215m**; Piebs **€400m**; ONE **€822m**) that raise **L2 dual map** more than FFS ranking (see high-absurdity + dual tables).

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
| `lb_fwb_ecureuil_sec_85m_2026` | **8.0** | **NEW 669** reserve misbooked as rec |
| `lb_digital_prov_no_plan_10m_2026` | **8.0** | **NEW 666** IT provision no master plan |
| `lb_provisions_liq_1_22bn_2026` | **8.0** | **NEW 663** specialty provisions liq |
| `lb_wal_revent_2_36bn_2023` | **8.0** | specialty revent eng €2.36bn (prior) |
| `lb_fwb_piebs_eng_400m_2026` | **7.5** | **NEW 669** Piebs report drawdown |
| `lb_fwb_debt_16_2bn_moody_a3_2026` | **7.5** | **NEW 668** FWB Moody A3 dual WAL Baa1 |
| `lb_prw_frr_cl_1_73bn_2026` | **7.5** | **NEW 667** PRW+FRR exec 4.4% May |
| `lb_ocpp_sousutil_524m_2026` | **7.5** | **NEW 666** sous-util vs inexec gap |
| `lb_moody_baa1_wal_2026` | **7.0** | **NEW 664** WAL Moody Baa1 |
| `lb_factures_shift_248m_2023_24` | **8.0** | year-end invoice shift (prior) |

### Dual / mega map (not pure annual waste top 10)

| ID | Envelope / peak | Note |
|----|----------------:|------|
| `lb_do17_social_sante_9_89bn_2026` | **9.89 bn** | **NEW 666** WAL DO17 aju dual VAPH |
| `lb_do17_dot_sante_7_05bn_2026` | **7.05 bn** | **NEW 667** prog093 sante dual |
| `lb_fwb_do52_secondaire_3_65bn_2026` | **3.65 bn** | **NEW 668** FWB secondary dual GO! |
| `lb_dual_fwb_wal_aju_sec_2026` | **3.77 bn** | **NEW 668** dual SEC aju FWB+WAL |
| `lb_prw_frr_cl_1_73bn_2026` | **1.73 bn** | **NEW 667** WAL PRW/FRR dual VV |
| `lb_fwb_do25_av_458m_2026` | **0.46 bn** | **NEW 668** AV dual VRT |
| `lb_fwb_one_822m_2026` | **0.82 bn** | **NEW 669** ONE dual KO |
| `lb_fwb_saca_solde_215m_2026` | **0.22 / 1.10 bn** stock | **NEW 669** SACA perimeter dual |
| `lb_spw_remun_740m_2026` | **0.74 bn** | **NEW 666** SPW wage bill dual VL |
| `lb_cabinets_wal_28m_2026` / `lb_fwb_cabinets_16_8m_2026` | **0.045 bn** dual | **NEW 667–668** cabinets dual |
| `lb_do_encours_8_93bn_may2026` | **8.93 bn** stock | WAL DO encours (prior wave) |
| `lb_aviq_dep_7_26bn_table34_2025` | **7.26 bn** | AViQ branch (prior) |
"""

src_rows = [
    f"{SRC},Dual aju WAL+FWB residual wave ticks661-669 progress@670 synthesis,https://www.ccrek.be/sites/default/files/Docs/2026_26_BudgetRW_2026_AJU.pdf,DOGE synthesis CoA WAL aju 2026_26 + FWB aju 2026_33,2026-08-01,synthesis,"
    "Strong primary-sourced: WAL DO CL 21.94bn Moody Baa1 debt 33.0bn interest 754m cabinets 28m PRW/FRR 1.73bn SPW remun 741m DO17 9.89bn; FWB DO CL 16.50bn Moody A3 debt 16.2bn interest 357m cabinets 16.8m SACA -215m ONE 822m Piebs 400m; dual SEC -3.77bn; progress@670; not TE-additive",
]

cmt_rows = [
    f"cmt_dual_aju_wave_661_670,Dual WAL+FWB aju2026 residual wave 661-670,gg_belgium,Entity II dual aju,CoA 2026_26+2026_33,2026-06-11,2026,2026,3768200000,\"{{\"\"2026\"\":3768200000}}\",,active,,Dual Entity II aju map,Not TE-additive,{SRC},strong,Belgium>dual>aju_wave_661_670,SEC dual -3.77bn DO 21.9+16.5bn Moody Baa1/A3; tick670",
]

lb_rows = [
    f"lb_dual_aju_wave_661_670_2026,Dual WAL+FWB aju residual wave 661-670,Belgium,ops,Belgium>dual>aju_wave_661_670,3768200000,0,Strong dual synthesis: WAL SEC -2.015 FWB -1.753 DO 21.9+16.5bn Moody Baa1/A3 SACA/ONE/Piebs; not TE-additive,strong,{SRC},Entity II dual,Aju dual map progress@670,Primary dual,6.5,8.5,3,6.85,Cross-entity L5 FOI,open,,tick670 progress",
]

foi_row = (
    f"{GAP},Belgium>dual>aju_wave_661_670_L5,gg_belgium,"
    "Cross-entity L5 residual from aju wave: WAL DO17/PRW/FRR/SPW remun/Job+; FWB DO51-55 economies/Piebs/CUR/ONE/Etnic/Ecureuil; dual cabinets FTE; dual Moody drivers; interest paid-accrued both entities,"
    "Progress@670 dual aju wave synthesis strong; L5 residual dual,"
    f"5,SPW Budget / MFWB Budget / Wallonie+FWB transparence,transparence@spw.wallonie.be;transparence@cfwb.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_dual_aju_wave_661_670,"
    f"lb_dual_aju_wave_661_670_2026,"
    f"{NOW},{NOW},tick670 progress dual aju wave; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** CoA WAL aju 2026_26 + FWB aju 2026_33 (ticks 661–669 synthesis @670)

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / MFWB Budget / services transparence
transparence@spw.wallonie.be
transparence@cfwb.be

Betreft: Openbaarheid — dual aju 2026 residual L5 (WAL DO/PRW + FWB SACA/OAP)

Geachte,

Op grond van de toepasselijke openbaarheidsregels verzoek ik om (machine-leesbaar):

WAL (CoA 2026_26):
1. DO17 CL 9.89 bn / prog093 sante 7.05 bn — top 30 beneficiaires.
2. PRW+FRR CL 1.73 bn — projecten >5 mEUR + exec per 30/06/2026.
3. SPW remun DF031.005 740.8 mEUR — FTE + 2e pilier status.
4. Job+/APE/CISP outturn vs aju 32/2.1/2.8 mEUR.

FWB (CoA 2026_33):
5. Piebs engagements 400 mEUR — projectlijst + report stock.
6. CUR PRR envelope 401 mEUR — liquidaties per project.
7. ONE CL 821.6 mEUR — top 30 + reserve repay 29.5 mEUR.
8. Economies Table3 253.6 mEUR — cash path per sector 2026.

Dual:
9. Cabinets FWB 16.8 + WAL 28.0 mEUR — FTE/comms per cabinet.
10. Interest paid vs accrued correction 2026 (beide entiteiten).

Période: 2025-01-01 à 2027-12-31.
Forme: CSV/XLSX bij voorkeur.

Cordialement,
[Naam]
```

## Notes agent
- Synthesis FOI for dual aju wave @ tick670; component FOIs already ready.
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK} (PROGRESS MILESTONE)
- Unit: {RQ} (progress@670 + dual aju WAL/FWB residual wave synthesis ticks661-669)
- Found (synthesis strong, primary-sourced no invent euros):
  - **WAL aju:** DO CL **EUR21.94bn** · DO17 **9.89bn** · Moody **Baa1** debt **33.0bn** interest **754m** · cabinets **28.0m** · PRW/FRR **1.73bn** · SPW remun **740.8m** · Ste-Emilie gap **146m** · OTW capital **-75m**
  - **FWB aju:** DO CL **EUR16.50bn** · DO52 **3.65bn** · Moody **A3** debt **16.2bn** interest **357m** path **561m 2029** · cabinets **16.8m** · SACA **-215m** report **1.10->0.73bn** · ONE **822m** · Piebs eng **400m** · CUR **267m**
  - **Dual:** SEC aju **FWB -1.753 + WAL -2.015 = -3.768bn** · Moody **A3/Baa1** · cabinets **44.8m** · education/emploi dual packs
- Progress coverage:
  - **A/B:** 100% (L0 TE + L1 subsectors)
  - **C L2:** ~**99%** (+ dual Entity II aju DO matrices + SACA/OAP + debt ratings)
  - **D L5:** ~**47-60%** generous (not near-complete of 348bn)
  - **E FOI ready:** ~**408** / answered ~**9** / total FOI rows ~**422**
- Inventory: budgets ~**12815** / cmt ~**1447** / lb ~**2721** / sources ~**1318** / entities ~**517**
- Waste top10: **unchanged** fossil/cars/cheque/consultancy (priority 8.55-8.30)
- High-abs + dual NEW: Ecureuil bookkeeping · digital no-plan · Piebs 400m · FWB Moody A3 · PRW/FRR 1.73bn · dual SEC 3.77bn · DO17 9.89bn · ONE 822m · SPW remun 741m
- Gain 660-670: largest flow dual = DO matrices **21.9+16.5bn**; largest stock path = WAL debt **33bn** + FWB debt **16.2bn** + SACA report **1.1bn**
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; cmt+lb+src dual wave; FOI {GAP} ready+draft; {RQ}=done spawn {NEXT_RQ}; ticks={TICK}
- FOI opened: {GAP} (ready, human send) - not sent
- Next: prio5 **{NEXT_RQ}**; deferred **rq_116**; progress@680 in 10 ticks
"""


def main() -> None:
    # prepend snapshot after header block (after first --- following How to read)
    prog = read_text(PROGRESS)
    marker = "## Snapshot at **tick 660**"
    if "## Snapshot at **tick 670**" in prog:
        print("PROGRESS already has 670")
    else:
        if marker in prog:
            prog = prog.replace(marker, PROGRESS_SNAPSHOT.strip() + "\n\n" + marker, 1)
        else:
            # insert after first methodology section
            insert_at = prog.find("\n---\n\n## Snapshot")
            if insert_at == -1:
                prog = PROGRESS_SNAPSHOT + "\n" + prog
            else:
                # find second ---
                pass
            prog = prog.replace(
                "## Snapshot at **tick",
                PROGRESS_SNAPSHOT.strip() + "\n\n## Snapshot at **tick",
                1,
            ) if "## Snapshot at **tick 670**" not in prog else prog
            if "## Snapshot at **tick 670**" not in prog and marker in prog:
                prog = read_text(PROGRESS)
                prog = prog.replace(marker, PROGRESS_SNAPSHOT.strip() + "\n\n" + marker, 1)
        PROGRESS.write_bytes(prog.encode("utf-8"))
        print("PROGRESS updated")

    # re-read and force if needed
    prog = read_text(PROGRESS)
    if "## Snapshot at **tick 670**" not in prog:
        # insert after line containing "Honest claim" block end ---
        parts = prog.split("\n---\n", 2)
        if len(parts) >= 3:
            # structure: header, howto, rest
            new = parts[0] + "\n---\n" + parts[1] + "\n---\n" + PROGRESS_SNAPSHOT.strip() + "\n\n---\n" + parts[2]
            # actually simpler: after second ---
            pass
        idx = prog.find("## Snapshot at **tick 660**")
        if idx > 0:
            prog = prog[:idx] + PROGRESS_SNAPSHOT.strip() + "\n\n" + prog[idx:]
            PROGRESS.write_bytes(prog.encode("utf-8"))
            print("PROGRESS force-inserted")
        else:
            print("PROGRESS WARN no insert point")

    WASTE.write_bytes(WASTE_MD.encode("utf-8"))
    print("WASTE updated")

    n_src = append_rows(ROOT / "sources.csv", src_rows)
    n_cmt = append_rows(ROOT / "commitments.csv", cmt_rows)
    n_lb = append_rows(ROOT / "leaderboard.csv", lb_rows)
    update_foi(ROOT / "foi_queue.csv", foi_row)
    draft_path = FOI_DRAFTS / f"{GAP}.md"
    draft_path.write_bytes(foi_draft.encode("utf-8"))
    print(f"DRAFT {draft_path}")

    update_rq_done(
        ROOT / "research_queue.csv",
        RQ,
        f"tick{TICK} progress@670 dual aju WAL/FWB wave 661-669; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Next residual after progress@670: Flanders CoA BA2026 dual cabinets/PRW or FWB recettes ch4 residual or new CoA PDF.,,"
        f"{NOW},,spawned tick{TICK} after {RQ}",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log = read_text(LOG)
    if f"tick {TICK}" not in log[-3000:]:
        if not log.endswith("\n"):
            log += "\n"
        log += log_entry
        LOG.write_bytes(log.encode("utf-8"))
        print("LOG appended")
    else:
        print("LOG skip duplicate")

    print(f"DONE tick{TICK}: src={n_src} cmt={n_cmt} lb={n_lb}")


if __name__ == "__main__":
    main()

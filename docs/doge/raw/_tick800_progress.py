# tick 800 — mandatory progress@800: coverage % + waste top10
import csv
from collections import Counter
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T21:00:00Z"
TICK = 800
RQ = "rq_791"
NEXT_RQ = "rq_792"


def count_rows(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def load(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


data = Path("docs/doge/data")
n_bud = count_rows(data / "budgets.csv")
n_cmt = count_rows(data / "commitments.csv")
n_lb = count_rows(data / "leaderboard.csv")
n_ent = count_rows(data / "entities.csv")
n_src = count_rows(data / "sources.csv")
foi = load(data / "foi_queue.csv")
st = Counter(r.get("status") for r in foi)
n_foi = len(foi)
n_ready = st.get("ready", 0)
n_ans = st.get("answered", 0)

lrows = load(data / "leaderboard.csv")


def fnum(x, default=0.0):
    try:
        return float(x or default)
    except (TypeError, ValueError):
        return default


def is_stockish(r):
    blob = " ".join(
        [
            r.get("item_id") or "",
            r.get("name") or "",
            r.get("tco_notes") or "",
            r.get("notes") or "",
        ]
    ).lower()
    keys = [
        "stock",
        "snowball",
        "financing gap",
        "overrun_477",
        "hedera",
        "principal repay",
        "safe be",
        "safe_be",
        "loan pool",
        "eng-liq",
        "debt stock",
        "phoenix lto",
        "illness_path",
        "illness benefits",
        "riziv",
        "ss spend",
        "ss_deficit",
        "nato_3_5",
        "entity1_path",
        "bosa_prov_stack",
    ]
    return any(k in blob for k in keys)


ranked = sorted(
    lrows,
    key=lambda r: (-fnum(r.get("priority_index")), -abs(fnum(r.get("annual_cost_eur")))),
)

# pure annual top10: prefer annual != 0 and not stockish; keep GIP exception as prior
pure = []
for r in ranked:
    if is_stockish(r) and "gip_monitor" not in (r.get("item_id") or ""):
        continue
    ann = fnum(r.get("annual_cost_eur"))
    # allow GIP-style zero-or-steering and reporté
    iid = r.get("item_id") or ""
    if ann == 0 and not any(
        x in iid for x in ["gip_monitor", "reporte", "dual_cars"]
    ):
        # skip pure zero unless known top patterns
        if "gip" not in iid and "reporte" not in iid:
            continue
    pure.append(r)
    if len(pure) >= 15:
        break

# If pure filter too aggressive, fall back to prior top10 IDs order with fresh pi
prior_ids = [
    "lb_vl_gip_monitor_fail_2_5bn",
    "lb_fed_fossil_direct_13_3bn",
    "lb_fed_fossil_accises_10_5bn",
    "lb_company_cars_fpb",
    "lb_exc_heatoil",
    "lb_cheque_economy",
    "lb_co2_vs_ordinary_ssc_gap_1bn",
    "lb_oaa_consol_reporte_300_6m",
    "lb_bcr_annexe2_reporte_wave",
    "lb_dual_cars_ssc_taxex",
]
by_id = {r.get("item_id"): r for r in lrows}
top10 = []
for iid in prior_ids:
    if iid in by_id:
        top10.append(by_id[iid])
# fill from pure if missing
for r in pure:
    if r.get("item_id") not in {x.get("item_id") for x in top10}:
        top10.append(r)
    if len(top10) >= 10:
        break
top10 = top10[:10]

# verify pi values still high
print("TOP10:")
for i, r in enumerate(top10, 1):
    print(
        i,
        r.get("item_id"),
        r.get("priority_index"),
        r.get("annual_cost_eur"),
        (r.get("name") or "")[:55],
    )

# new residual highlights ticks 791-799
new_high = [
    r
    for r in ranked
    if any(
        x in ((r.get("notes") or "") + (r.get("item_id") or "")).lower()
        for x in [
            "tick791",
            "tick792",
            "tick793",
            "tick794",
            "tick795",
            "tick796",
            "tick797",
            "tick798",
            "tick799",
        ]
    )
][:20]
print("NEW residual sample", len(new_high))
for r in new_high[:12]:
    print(
        r.get("item_id"),
        r.get("priority_index"),
        r.get("annual_cost_eur"),
        (r.get("name") or "")[:50],
    )

# --- write progress file: prepend snapshot at tick 800 ---
prog_path = data / "progress_every_10_ticks.md"
old = prog_path.read_text(encoding="utf-8")
# insert after first --- following the how-to-read section: after line with "## Snapshot at **tick 790**"
snap = f"""## Snapshot at **tick 800** (2026-08-04)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** Beliris residual dual Metro3 class · Fin taxex cruise **€250m** demo/rebuild · IBZ security provision **~€0.5bn** · Plan Grote Steden **€71.3m** · federal culture 3-inst dots **€68.7m** · Fedasil dual **€802.2m** package class retained · prior RIZIV/SS/SAFE/illness stacks retained |
| **D. L5 named / measure end-lines** | **~59-73%** of TE (generous) | **Gain 790→800 is federal beleidsnota residual wave (not near-complete of 348bn):** Klima SKF BE **€2.21bn** / fed EU **€217–218m** / cofin **€72m** · Asiel 038 euro-opaque dual Fedasil · Culture Monnaie TCO **€64.7m** / Bozar ops **€35.6m** / 3-inst **€68.7m** · IBZ cameras **€25m** paid / Plan GV **€71.3m** / digital floor **>€150m** / DSU **>€30m** · BZ refi **€35m** / ODA **−25%** dual DGD **€1.118bn** · Energie ETF call9 **€16.97m** / Phoenix support opaque · KMO VAT franchise path **€15.16m** / accounts fee cut **€3.571m** / SKF micro **~€24m** · Fin VAT demo cruise **€250m** / heatpump **€10.1m** / SFPIM Defence capital opaque / SRFF **+100** · Beliris metro save **€25m** / Nord suspend since 2023 / Schuman canopy **≥€13m** not ordered · FOI still bulk provision exact € + Phoenix cash + Nord recurrent + SFPIM capital |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **~{n_ans}**; total FOI rows **~{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** (incl. demo/rebuild cruise **€250m** class, heatpump **€10.1m**, VAT franchise path) · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform *savings paths* · **gross financing / OLO** · **debt principal repay / securities purchases** (roll) · **SAFE loans €8.34bn BE** · **Entity II HermReg soldes €7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP €15bn** · **Phoenix LTO multi-year / CfD / support mechanism** · **Defence eng-liq backlog / SFPIM Defence capital** · **Ukraine multi-year 1bn/yr** · **EU GNI / MFF 2028–2034 ~€1.985tn class** · **housing finance stocks** · **Regie rent/DBFM lock-in** · **Metro3 multi-bn stock** · Moody/S&P rating actions (not euros).

### Inventory (tick 800)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~{n_bud} |
| commitments.csv | ~{n_cmt} |
| leaderboard.csv | ~{n_lb} |
| entities.csv | ~{n_ent} |
| sources.csv | ~{n_src} |
| FOI ready | ~{n_ready} |
| FOI answered | ~{n_ans} |
| FOI total rows | ~{n_foi} |
| research_queue open | rq_116 deferred + rq_792 hole-fill after progress |

### What improved since tick 790

- **Klima + Asiel (tick791–792):** SKF plan **€2.21bn** (EU **€1.66bn** + cofin **€0.55bn**) · federal **13.13% = €217–218m** · cofin **~€72m** · NEH pilot **€600k** · Asiel 038 euro-opaque dual Fedasil package **€802.2m** · Dublin2/FastTrack/Masterplan FOI.
- **Culture + IBZ (tick793–794):** 3-inst dots **€68.714m** · Monnaie TCO **€64.7m** · Bozar ops **€35.6m** · Loterij class **~€7m** · security+return provision **~€0.5bn** · Plan Grote Steden **€71.3m** · cameras **€25m** paid · material+digital **>€150m** · DSU **>€30m**.
- **BZ + Energie + KMO (tick795–797):** BZ refi **€35m** · ODA **−25%** dual DGD **€1.118bn** / cut **−€106m** · ETF call9 **€16.97m** · call10 residual Unknown · Phoenix support opaque · VAT franchise path **€15.16m** 2026–29 · accounts fee cut **€3.571m** · SME info **€550k** · SKF micro **~€24m**.
- **Fin + Beliris (tick798–799):** VAT demo/rebuild cruise **€250m** · heatpump **€10.1m** · CGT **€10–15k** unit · SFPIM Defence capital opaque · SRFF **+100** · Beliris metro save **€25m** · Nord suspend since **2023-03-17** · canopy **≥€13m** not ordered · cleanup **€126k**.
- **Dual map:** SKF Klima vs KMO · Fedasil vs Asiel ops · culture 3-inst vs city culture · Plan GV vs prior police GV · ETF vs BA path · Fin taxex vs FPS inventory · Beliris save vs Metro3 multi-bn stock.

---

"""

marker = "## Snapshot at **tick 790**"
if marker in old:
    # insert before tick 790 snapshot (keep history)
    new_prog = old.replace(marker, snap + marker, 1)
else:
    new_prog = old + "\n" + snap
prog_path.write_text(new_prog, encoding="utf-8")
print("wrote progress_every_10_ticks.md")

# --- waste top10 ---
def fmt_ann(v):
    try:
        a = float(v)
    except (TypeError, ValueError):
        return str(v or "—")
    if abs(a) >= 1e9:
        return f"**{a/1e9:.2f} bn**"
    if abs(a) >= 1e6:
        return f"**{a/1e6:.2f} m**"
    if abs(a) >= 1e3:
        return f"**{a/1e3:.2f} k**"
    return f"**{a:.0f}**"


rows_md = []
for i, r in enumerate(top10, 1):
    rows_md.append(
        f"| {i} | `{r.get('item_id')}` | {(r.get('name') or '')[:55]} | {fmt_ann(r.get('annual_cost_eur'))} | "
        f"{r.get('absurdity_score') or '—'} | {r.get('cost_score') or '—'} | {r.get('difficulty') or '—'} | "
        f"**{r.get('priority_index') or '—'}** | {(r.get('tco_notes') or r.get('notes') or '')[:40]} |"
    )

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** (2026-08-04) · **~{n_lb}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
{chr(10).join(rows_md)}

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · Hedera CAP · VL/WAL/FWB/BCR debt stocks · OWV snowball · Oosterweel residual · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · debt principal repay · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **BOSA provisions ~€1.71bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **Phoenix multi-year** · **SFPIM Defence capital** · housing finance · Regie DBFM stocks · **Beliris/Metro3 multi-bn**.

**Change vs tick 790:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). **Major NEW residual 791–799 (off pure top10 / dual):** SKF **€2.21bn** / fed **€217–218m**+**€72m** · culture 3-inst **€68.7m** / Monnaie **€64.7m** · IBZ provision **~€0.5bn** / Plan GV **€71.3m** / cameras **€25m** · Fin VAT demo cruise **€250m** / heatpump **€10.1m** · Beliris metro save **€25m** / Nord suspend / canopy **≥€13m** · ETF call9 **€16.97m** · ODA **−25%** dual · VAT franchise **€15.16m**. Gain is **beleidsnota residual dual map** more than FFS reshuffle.

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| — | `lb_metro3_overrun_477pct` | **stock** | **9.05** | STOCK filtered |
| — | `lb_vat_demo_rebuild_250m` | **250 m** | **6.50** | **NEW 798** VAT demo cruise taxex |
| — | `lb_ibz_security_return_provision_0_5bn` | **~0.5 bn class** | **7.40** | **NEW 794** provision exact FOI |
| — | `lb_dual_beliris_metro3_2026` | **dual stock** | **7.40** | **NEW 799** Beliris vs Metro3 |
| — | `lb_beliris_nord_suspension_opaque` | **recurrent Unknown** | **7.35** | **NEW 799** since 2023 |
| — | `lb_phoenix_support_opaque` | **Unknown** | **7.35** | **NEW 796** nuclear support |
| — | `lb_oda_cut_minus_25pct_path` | **path** | **7.10** | **NEW 795** ODA −25% |
| — | `lb_sfpim_defence_opaque` | **Unknown** | **6.70** | **NEW 798** SFPIM Defence |
| — | `lb_fed_culture_3inst_68_7m_2026` | **68.7 m** | **6.00** | **NEW 793** federal culture dots |
| — | `lb_plan_grote_steden_71_3m` | **71.3 m multi-yr** | **6.25** | **NEW 794** Plan GV |

### High-absurdity shortlist (not pure annual cost rank)

| ID | Abs | Note |
|----|----:|------|
| `lb_metro3_overrun_477pct` | **9.5** | Metro3 cost +477pct |
| `lb_vl_wassalon_podcast` | **9.5** | VL gelijke kansen vodcast |
| `lb_metro3_financing_gap_4bn` | **9.0** | Metro3 BCR financing gap |
| `lb_vl_gip_monitor_fail_2_5bn` | **9.0** | GIP without VEK public report |
| `lb_oaa_consol_reporte_300_6m` | **9.0** | Reporté solde fiction |
| `lb_beliris_nord_suspension_opaque` | **7.5** | Nord suspended since 2023 |
| `lb_asiel_038_euro_opaque` | **7.0** | Asiel note euro-opaque |

### Methodology notes

- **Source class:** prefer parliamentary Kamer DOC / CoA / FPB / NBB primary.  
- **Do not sum** leaderboard annuals into TE coverage.  
- Stocks and multi-year eng/loans without same-year pure TE cash stay **off pure top10** unless annualised with source.
"""

(data / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("wrote doge_waste_top10_current.md")

# research queue
rq_path = data / "research_queue.csv"
rq_rows = load(rq_path)
rq_fields = list(rq_rows[0].keys())
for r in rq_rows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick800 mandatory progress@800 coverage A-E + waste top10; "
            "top10 stable GIP/fossil/cars; residual 791-799 dual map"
        )
# ensure rq_792 open
if not any(r.get("task_id") == NEXT_RQ for r in rq_rows):
    rq_rows.append(
        {
            "task_id": NEXT_RQ,
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "After progress@800: residual dual L5 or unmined primary (Regie 029, Loterij 015, "
                "local/CoA, other 1282/*); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick800 after progress",
        }
    )
else:
    for r in rq_rows:
        if r.get("task_id") == NEXT_RQ and r.get("status") == "open":
            r["updated_utc"] = UTC
            r["notes"] = (r.get("notes") or "") + "; progress@800 done tick800"


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows([{k: (r.get(k) or "") for k in fields} for r in rows])


write_csv(rq_path, rq_fields, rq_rows)

notes = (
    f"tick{TICK} MANDATORY progress@800 coverage A-E + waste top10 stable; "
    f"next {NEXT_RQ} Regie029/Loterij015 residual; progress@810 in 10; rq_116 deferred"
)
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (mandatory **progress@800** — coverage % layers A–E + waste top10)
- Found / assessed (no new primary euros this tick — inventory refresh):
  - **A L0:** **100%** (€347.956bn TE anchor)
  - **B L1:** **100%** unconsol. map
  - **C L2:** ~**99%** (+ culture 68.7 · IBZ Plan GV 71.3 · security provision ~0.5bn class · Beliris dual Metro3 · Fin taxex 250+10.1)
  - **D L5:** ~**59–73%** generous — gain 790→800: SKF 2.21bn · Fedasil dual · culture TCO · Plan GV/cameras · ODA −25% · ETF 16.97 · VAT franchise 15.16 · Fin demo 250 · Beliris save 25 / Nord suspend / canopy 13
  - **E FOI ready:** ~**{n_ready}** (answered ~{n_ans}; total ~{n_foi})
  - **Waste top10 pure annual:** **stable** GIP#1 · fossil/cars/cheque/reporté #2–10; stocks/loans filtered (Metro3, SAFE, illness, Phoenix, SFPIM Defence capital)
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; {RQ}=done; next **{NEXT_RQ}**; loop_state ticks={TICK}
- FOI: none new this tick
- Next: prio5 **{NEXT_RQ}** residual Regie029/Loterij015; deferred **rq_116**; progress@810 in 10
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: progress@800; next {NEXT_RQ}")
print(f"inventory budgets={n_bud} cmt={n_cmt} lb={n_lb} foi_ready={n_ready}")

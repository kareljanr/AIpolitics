# tick 263 — rq_254 Mons ASBL L5 sample from budget 2025 primary
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T18:30:00Z"
tick = 263
unit = "rq_254"

# load mons L5
mons = json.loads((root / "docs/doge/data/raw/mons_l5_top_tick103.json").read_text(encoding="utf-8"))
lines = mons["top_subsidy_lines_2025"]

# pick named third-party / ASBL / association / sports club L5 (not pure personnel)
named = [
    ("rca_piscine", "RCA piscine exploitation", 1900000.0),
    ("rca_subside", "Regie Communale Autonome RCA", 1156470.97),
    ("rca_fonct", "RCA frais de fonctionnement", 815000.0),
    ("fonds_impulsion", "Fonds impulsion nouveaux commerces", 650000.0),
    ("mars_fonct", "MARS fonctionnement associations", 400000.0),
    ("rca_76422", "RCA line 76422", 380000.0),
    ("ot_personnel", "Office du Tourisme personnel", 289204.0),
    ("escale", "TFT Escale Plan Cohesion Sociale", 275630.02),
    ("ot_fonct", "Office du Tourisme fonctionnement", 273750.0),
    ("basket_umh", "Basket Union Mons Hainaut", 220000.0),
    ("asbl_garance", "ASBL Garance Enfant-Phare", 170000.0),
    ("mars_anim", "MARS animations", 150000.0),
    ("mars_musical", "MARS volet musical", 124000.0),
    ("fondation_mons2025", "Fondation Mons 2025", 110000.0),
    ("grandes_manif", "Grandes manifestations conventionnees", 108000.0),
    ("charte_activites", "Charte vie associative activites", 100000.0),
    ("regie_quartiers", "Regie des quartiers", 90000.0),
    ("monsports", "ASBL Monsports", 66000.0),
    ("asbl_saint_georges", "ASBL Saint Georges", 55000.0),
    ("charte_fonct", "Charte vie associative fonctionnement", 50000.0),
    ("orchestre_rcw", "Orchestre Royal de Chambre de Wallonie", 50000.0),
    ("film_festival", "Festival International du Film de Mons", 45000.0),
]

sample_sum = sum(x[2] for x in named)

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_mons_budget_ord_2025_l5,Mons budget ordinaire 2025 top subsidy lines L5 extract,"
        "docs/doge/data/raw/mons_budget_ord_2025.pdf,Ville de Mons eComptes budget 2025,"
        "2026-07-29,budget,"
        f"Top ASBL/RCA/assoc sample sum {sample_sum:.0f}; MARS 400k Garance 170k Basket 220k Film 45k; "
        "full top50 in mons_l5_top_tick103.json; tick263\n"
    )
print("sources ok", sample_sum)

# --- budgets ---
bud = root / "docs/doge/data/budgets.csv"
# only add lines not already present
existing = (root / "docs/doge/data/budgets.csv").read_text(encoding="utf-8")
new_rows = []
for key, label, eur in named:
    bid = f"bud_mons_{key}_2025"
    if bid in existing:
        continue
    new_rows.append(
        f"{bid},city_mons,2025,{eur:.2f},,,budgeted,src_mons_budget_ord_2025_l5,strong,"
        f"{label} {eur:.0f} EUR BI2025"
    )
# aggregate
if "bud_mons_l5_asbl_sample_2025" not in existing:
    new_rows.append(
        f"bud_mons_l5_asbl_sample_2025,city_mons,2025,{sample_sum:.2f},,,budgeted,src_mons_budget_ord_2025_l5,strong,"
        f"Named ASBL/RCA/assoc/sport sample n={len(named)} sum {sample_sum:.0f} from top50 extract"
    )
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in new_rows:
        f.write(r + "\n")
print("budgets", len(new_rows))

# --- commitments ---
cmt = root / "docs/doge/data/commitments.csv"
cash = (
    f'{{"sample_sum": {sample_sum:.2f}, "n_lines": {len(named)}, '
    '"mars_package": 674000, "rca_cluster": 4251470.97, '
    '"note": "BI2025 primary extract; BI2026 named matrix residual FOI gap_mons_budget_l5"}'
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_mons_l5_asbl_sample_2025,Mons city L5 ASBL RCA association subsidy sample 2025,"
        "city_mons,Local ASBL RCA sports culture tourism operators,Budget ordinaire 2025 Conseil,"
        f"2025-01-01,2025,2025,{sample_sum:.2f},\"{cash}\",0,active,"
        "docs/doge/data/raw/mons_budget_ord_2025.pdf,"
        "Municipal third-party subsidies culture sport tourism,"
        "FOI BI2026 full named top20; open data register,"
        "src_mons_budget_ord_2025_l5,strong,Mons>subsidies>L5_sample,"
        "tick263 closes deferred Mons L5 sample\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    f"lb_mons_l5_sample_{sample_sum/1e6:.1f}m,Mons L5 ASBL/RCA/assoc sample {sample_sum/1e6:.1f}m 2025,local,ops,Mons>subsidies>L5_sample,{sample_sum:.2f},{sample_sum:.2f},"
    f"Strong budget 2025 extract n={len(named)} named lines incl RCA cluster ~4.25m MARS 0.67m Garance 0.17m Basket 0.22m,strong,src_mons_budget_ord_2025_l5,"
    "Local associations sports tourism,Municipal discretionary third-party grants,Core local culture/sport dual Charleroi sample,3,5.5,4,4.85,"
    "FOI BI2026 named top20; publish open register,seed,,tick263",
    "lb_mons_mars_package,Mons MARS culture package ~0.67m 2025,local,ops,Mons>culture>MARS,674000,674000,"
    "Strong: MARS fonct 400k + animations 150k + musical 124k = 674k BI2025,strong,src_mons_budget_ord_2025_l5,"
    "MARS association,Culture venue municipal support,Named L5 culture dual Charleroi PBA,3,3.5,3,3.55,"
    "Track multi-year path,seed,,tick263",
    "lb_mons_rca_cluster,Mons RCA municipal regie cluster ~4.25m 2025,local,ops,Mons>RCA>subsidies,4251470.97,4251470.97,"
    "Strong: piscine 1.9m + RCA 1.156m + fonct 0.815m + 0.38m lines class,strong,src_mons_budget_ord_2025_l5,"
    "Regie Communale Autonome,Municipal autonomous regie operations,Quasi-internal transfer not pure third-party ASBL,3,5.5,4,4.85,"
    "Separate from pure ASBL L5,seed,,tick263",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb ok")

# --- foi update gap_mons if exists ---
foi = root / "docs/doge/data/foi_queue.csv"
text = foi.read_text(encoding="utf-8")
out_f = []
for L in text.splitlines():
    if L.startswith("gap_mons_budget_l5,"):
        if "tick263" not in L:
            L = L.rstrip() + " | tick263: BI2025 L5 sample filled public; residual BI2026 named top20"
    out_f.append(L)
# if no gap, add residual for BI2026
if "gap_mons_budget_l5," not in text and "gap_mons_bi2026_named," not in text:
    out_f.append(
        "gap_mons_bi2026_named,Mons>subsidies>BI2026_named_top20,city_mons,"
        "BI2026 named third-party ASBL top20 with amounts (BI2025 L5 sample public tick263),"
        "BI2025 sample filled; dual year path and BI2026 opacity,5,"
        "Ville de Mons publicite de l administration,,"
        "Hotel de Ville Mons,"
        "docs/doge/foi/drafts/gap_mons_bi2026_named.md,ready,2026-07-29,,,,,"
        "cmt_mons_l5_asbl_sample_2025,lb_mons_l5_sample_,"
        f"{now},{now},tick263 draft ready residual BI2026"
    )
with open(foi, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out_f) + "\n")
print("foi ok")

# FOI draft
draft = root / "docs/doge/foi/drafts/gap_mons_bi2026_named.md"
if not draft.exists():
    draft.write_text(
        f"""# FOI draft — gap_mons_bi2026_named

Status: **ready** (human send only)  
Internal ref: `gap_mons_bi2026_named`  
Tick: 263

### Public side filled (BI2025)

Named L5 sample sum **€{sample_sum:,.0f}** from budget ordinaire 2025 (RCA cluster, MARS, Garance, Basket UMH, Film festival, Charte associative, etc.).

### Residual

BI2026 named third-party top20 amounts not in public Mag-level aggregates.

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon / datum]

Aan: Ville de Mons
     service publicité de l'administration
     Hôtel de Ville, Mons

Betreft: Demande de publicité — top 20 subventions ASBL BI2026
         (dossierref: gap_mons_bi2026_named)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration,
je sollicite :

1. Liste des 20 principales subventions de fonctionnement/facultatives
   aux ASBL et tiers (hors RCA purement interne si distinct) pour le
   budget initial 2026, avec montants.

2. Comparaison éventuelle avec le budget 2025 (extrait public disponible).

Forme: PDF/CSV à [e-mail].

Réf.: gap_mons_bi2026_named
```
""",
        encoding="utf-8",
    )

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_254,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; APEFE budget if public; "
    "other FOI-adjacent after PMV).,,2026-07-29T18:00:00Z,,"
    "Spawned tick262 after PMV 4.24bn dual WE; rq_116 SWA deferred"
)
new = (
    "rq_254,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; APEFE budget if public; "
    "other FOI-adjacent after PMV).,gap_mons_bi2026_named,"
    "2026-07-29T18:00:00Z,2026-07-29T18:30:00Z,"
    f"tick263: Mons L5 sample {sample_sum/1e6:.1f}m BI2025 n={len(named)}; spawn rq_255"
)
if old not in rq:
    raise SystemExit("rq_254 not found")
rq = rq.replace(old, new)
if "rq_255," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_255,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; APEFE budget if public; "
        "finance.brussels dual PMV/WE; other FOI-adjacent after Mons L5).,,2026-07-29T18:30:00Z,,"
        "Spawned tick263 after Mons L5 sample; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
(root / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    f"Scheduler 60s. Next prio5 rq_255; rq_116 SWA deferred. FOI ready human send. "
    f"tick263 Mons L5 sample {sample_sum/1e6:.1f}m.\n",
    encoding="utf-8",
)
print("DONE", tick, "sum", sample_sum)

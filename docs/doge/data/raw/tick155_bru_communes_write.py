# -*- coding: utf-8 -*-
"""Tick 155 — rq_145 Brussels communes Ixelles / Schaerbeek / Anderlecht L5 sample."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 155
UNIT = "rq_145"
UTC = "2026-07-28T01:15:00Z"
GAP = "gap_bru_communes_subsidies_top20"


def read_text(p: Path) -> str:
    raw = p.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def write_text(p: Path, text: str) -> None:
    p.write_bytes(text.encode("utf-8", errors="replace"))


def append_if_missing(p: Path, rows: list[str]) -> None:
    text = read_text(p)
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        if row.split(",", 1)[0] not in text:
            text += row + "\n"
    write_text(p, text)


def replace_line_startswith(p: Path, prefix: str, new_line: str) -> bool:
    text = read_text(p)
    lines = text.splitlines()
    found = False
    out = []
    for L in lines:
        if L.startswith(prefix):
            out.append(new_line)
            found = True
        else:
            out.append(L)
    write_text(p, "\n".join(out) + "\n")
    return found


# --- sources ---
srcs = [
    'src_ixelles_budget_2026_dh,Ixelles budget 2026 figures quoted from echevine Finances Gilson via DH,https://www.dhnet.be/regions/bruxelles/2026/05/21/pas-de-hausse-dimpots-a-ixelles-en-2026-mais-la-commune-doit-puiser-dans-ses-reserves-pour-rester-a-lequilibre-2QSTB77ERRETJM5Y4BXJ77T4VU/,DH / Commune Ixelles quotes,2026-07-28,press_official_quote,"Ord rec ~253m dep ~258m+; provisions 5.5m+; invest 46.2m of which emprunt 26.9m; transfers +9.4m CPAS +6.07m iris 4.75m police +0.3m; debt path 119->210m; tick155"',
    'src_ixelles_budget_participatif_2026,Ixelles budget participatif 170k 2026,https://www.ixelles.be/site/790-Budget-participatif,Commune d Ixelles,2026-07-28,official_web,"Citizen participatory budget envelope 170000 EUR 2026; tick155"',
    'src_schaerbeek_note_budget_2026,Schaerbeek Note politique budget 2026 official PDF,https://www.1030.be/data/media/document/1.-note-politique-budget-2026.pdf,Commune de Schaerbeek,2026-07-28,official_budget,"Named invest: Brichaut creche 6.5m (commune 20pct); Hoogvorst ~6m (commune 2m); RenovaS Dupont 5m; Plantes 3m; sport >2m; CPAS AS hire 945853; tick155"',
    'src_schaerbeek_budget_2026_rtbf,Schaerbeek budget 2026 60m invest RTBF quotes echevin Vanhalewyn,https://www.rtbf.be/article/60-millions-d-investissements-dans-le-budget-de-schaerbeek-en-2026-11638560,RTBF / Commune Schaerbeek,2026-07-28,press_official_quote,"Invest 60m; creche 6.5m; trottoirs 1.5m; athletics Terdelt 1.2m; CPAS +~17m federal means; tick155"',
    'src_anderlecht_cp_budget_2026,Anderlecht communique budget 2026 a l equilibre,https://www.anderlecht.be/sites/default/files/medias/Files/CP/260302%20Communiqu%C3%A9%20Budget.pdf,Commune d Anderlecht,2026-07-28,official_press,"Equilibre 2026 plan 2025-27; voirie asphalt 1.2m sidewalks 0.85m; maintain associative/sport/jeunesse; full opex totals not in CP; tick155"',
]
append_if_missing(DATA / "sources.csv", srcs)

# --- entities ---
ents = [
    "city_ixelles,Commune d Ixelles,Gemeente Elsene,Municipality of Ixelles,local,brussels_gov,bi,https://www.ixelles.be,,1050 Brussels,Ord rec ~253m dep ~258m+ 2026 medium; invest 46.2m; debt ~210m; tick155",
    "city_schaerbeek,Commune de Schaerbeek,Gemeente Schaarbeek,Municipality of Schaerbeek,local,brussels_gov,bi,https://www.1030.be,,1030 Brussels,Invest 60m 2026; balance path 2027; CPAS +17m class federal; tick155",
    "city_anderlecht,Commune d Anderlecht,Gemeente Anderlecht,Municipality of Anderlecht,local,brussels_gov,bi,https://www.anderlecht.be,,1070 Brussels,Budget 2026 equilibrium claimed; voirie 2.05m named invest; full opex FOI; tick155",
]
append_if_missing(DATA / "entities.csv", ents)

# --- budgets ---
bud = [
    # Ixelles
    "bud_ixelles_ord_rec_2026,city_ixelles,2026,253000000,,,budgeted,src_ixelles_budget_2026_dh,medium,Ordinary receipts nearly 253m EUR quoted echevine Gilson DH May 2026",
    "bud_ixelles_ord_dep_2026,city_ixelles,2026,258000000,,,budgeted,src_ixelles_budget_2026_dh,medium,Ordinary dep functioning+personnel+transfers a bit over 258m EUR quoted",
    "bud_ixelles_provisions_2026,city_ixelles,2026,5500000,,,budgeted,src_ixelles_budget_2026_dh,medium,Provisions/prelevements >5.5m to balance ordinary; not sustainable indefinitely per quote",
    "bud_ixelles_invest_2026,city_ixelles,2026,46200000,,,budgeted,src_ixelles_budget_2026_dh,medium,Investment ambition 46.2m of which 26.9m emprunt",
    "bud_ixelles_invest_emprunt_2026,city_ixelles,2026,26900000,,,budgeted,src_ixelles_budget_2026_dh,medium,Borrowing share of invest 26.9m",
    "bud_ixelles_debt_2025,city_ixelles,2025,210000000,,,outturn_class,src_ixelles_budget_2026_dh,medium,Debt path previous legislature 119m to 210m (2018-2025 class)",
    "bud_ixelles_ord_delta_2026,city_ixelles,2026,11000000,,,budgeted,src_ixelles_budget_2026_dh,medium,Ordinary spending +11m vs prior of which transfers +9.4m",
    "bud_ixelles_cpas_delta_2026,city_ixelles,2026,6070000,,,budgeted,src_ixelles_budget_2026_dh,medium,CPAS transfer +6.07m 2026",
    "bud_ixelles_iris_deficit_2026,city_ixelles,2026,4750000,,,budgeted,src_ixelles_budget_2026_dh,medium,Iris hospital network deficit catch-up 4.75m for 2024-2025 exercises",
    "bud_ixelles_police_delta_2026,city_ixelles,2026,300000,,,budgeted,src_ixelles_budget_2026_dh,medium,Police zone +300k",
    "bud_ixelles_participatif_2026,city_ixelles,2026,170000,,,budgeted,src_ixelles_budget_participatif_2026,strong,Citizen participatory budget 170k official site",
    # Schaerbeek
    "bud_schaerbeek_invest_2026,city_schaerbeek,2026,60000000,,,budgeted,src_schaerbeek_budget_2026_rtbf,medium,Total investments 60m 2026 per echevin Vanhalewyn RTBF",
    "bud_schaerbeek_creche_brichaut_2026,city_schaerbeek,2026,6500000,,,budgeted,src_schaerbeek_note_budget_2026,strong,Creche Brichaut total invest 6.5m; commune cofinance 20pct ~1.3m",
    "bud_schaerbeek_creche_brichaut_commune_2026,city_schaerbeek,2026,1300000,,,budgeted,src_schaerbeek_note_budget_2026,strong,Commune 20pct of Brichaut 6.5m = 1.3m",
    "bud_schaerbeek_hoogvorst_2026,city_schaerbeek,2026,6000000,,,budgeted,src_schaerbeek_note_budget_2026,strong,Creche rue d Hoogvorst almost 6m 2026; commune cofinance 2m",
    "bud_schaerbeek_hoogvorst_commune_2026,city_schaerbeek,2026,2000000,,,budgeted,src_schaerbeek_note_budget_2026,strong,Commune cofinance Hoogvorst 2m",
    "bud_schaerbeek_trottoirs_2026,city_schaerbeek,2026,1500000,,,budgeted,src_schaerbeek_budget_2026_rtbf,medium,Plan trottoirs 1.5m RTBF quote",
    "bud_schaerbeek_terdelt_2026,city_schaerbeek,2026,1200000,,,budgeted,src_schaerbeek_budget_2026_rtbf,medium,Athletics track Terdelt 1.2m",
    "bud_schaerbeek_renovas_dupont_2026,city_schaerbeek,2026,5000000,,,budgeted,src_schaerbeek_note_budget_2026,strong,RenovaS health-youth equipment Dupont 5m",
    "bud_schaerbeek_plantes_2026,city_schaerbeek,2026,3000000,,,budgeted,src_schaerbeek_note_budget_2026,strong,Rue des Plantes renovation 3m of which 60pct commune",
    "bud_schaerbeek_sport_2026,city_schaerbeek,2026,2000000,,,budgeted,src_schaerbeek_note_budget_2026,strong,Sport renovations more than 2m 2026",
    "bud_schaerbeek_cpas_federal_2026,city_schaerbeek,2026,17000000,,,budgeted,src_schaerbeek_budget_2026_rtbf,medium,CPAS envelope +~17m federal means integrated (not all new communal cash)",
    "bud_schaerbeek_cpas_as_2026,city_schaerbeek,2026,945853,,,budgeted,src_schaerbeek_note_budget_2026,strong,CPAS personnel line 945853 EUR for social workers",
    # Anderlecht
    "bud_anderlecht_voirie_asphalt_2026,city_anderlecht,2026,1200000,,,budgeted,src_anderlecht_cp_budget_2026,strong,Communal road asphalt 1.2m official CP",
    "bud_anderlecht_trottoirs_2026,city_anderlecht,2026,850000,,,budgeted,src_anderlecht_cp_budget_2026,strong,Sidewalks 850k official CP",
    "bud_anderlecht_voirie_sum_2026,city_anderlecht,2026,2050000,,,budgeted,src_anderlecht_cp_budget_2026,strong,Named public-space invest sum 1.2+0.85=2.05m",
]
append_if_missing(DATA / "budgets.csv", bud)

# --- commitments ---
cmts = [
    (
        'cmt_ixelles_budget_2026,Ixelles ordinary + invest envelope 2026,city_ixelles,Commune d Ixelles + CPAS Iris police,'
        'Conseil communal budget 2026 (quoted echevine Finances),2026-05-21,2026,2026,258000000,'
        '"{""2026_ord_rec"":253000000,""2026_ord_dep"":258000000,""2026_provisions"":5500000,""2026_invest"":46200000,'
        '""2026_emprunt"":26900000,""2026_cpas_delta"":6070000,""2026_iris"":4750000,""2026_police_delta"":300000,'
        '""2026_participatif"":170000,""debt_path"":""119m_to_210m_prior_legislature""}",0,active,'
        'https://www.ixelles.be,Local public services transfer operators,'
        'Publish full BI PDF + top20 ASBL subsidies; reduce debt; stop recurrent provision draw,'
        'src_ixelles_budget_2026_dh,medium,Bruxelles>Ixelles>budget2026,'
        'tick155; medium because press quotes official; residual FOI full PDF+ASBL'
    ),
    (
        'cmt_schaerbeek_invest_2026,Schaerbeek investment programme named L5 2026,city_schaerbeek,Commune Schaerbeek / RenovaS / creches,'
        'Note politique budget 2026 + Conseil 26 Nov 2025,2025-11-26,2026,2026,60000000,'
        '"{""2026_invest_total"":60000000,""creche_brichaut"":6500000,""creche_brichaut_commune"":1300000,'
        '""hoogvorst"":6000000,""hoogvorst_commune"":2000000,""trottoirs"":1500000,""terdelt"":1200000,'
        '""renovas_dupont"":5000000,""plantes"":3000000,""sport"":2000000,""cpas_federal_class"":17000000}",0,active,'
        'https://www.1030.be/data/media/document/1.-note-politique-budget-2026.pdf,Local infrastructure social care culture,'
        'Publish ordinary totals + top20 ASBL; track balance path 2027,'
        'src_schaerbeek_note_budget_2026,strong,Bruxelles>Schaerbeek>invest2026,'
        'tick155; invest total medium via RTBF; named project lines strong from official note'
    ),
    (
        'cmt_anderlecht_invest_space_2026,Anderlecht public-space invest sample 2026,city_anderlecht,Commune Anderlecht,'
        'Communique budget 2026 conseil 5 mars 2026,2026-03-02,2026,2026,2050000,'
        '"{""2026_asphalt"":1200000,""2026_sidewalks"":850000,""note"":""equilibrium claimed; full opex and ASBL list not in CP""}",0,active,'
        'https://www.anderlecht.be/sites/default/files/medias/Files/CP/260302%20Communiqu%C3%A9%20Budget.pdf,'
        'Public space renovation proximity services,Publish full BI2026 + associative credits L5,'
        'src_anderlecht_cp_budget_2026,strong,Bruxelles>Anderlecht>invest_space,'
        'tick155; only partial public L5; FOI residual'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

# --- leaderboard ---
lbs = [
    "lb_ixelles_ord_gap,Ixelles ordinary gap covered by provisions ~5.5m 2026,local,ops,Bruxelles>Ixelles>provisions,5500000,5500000,Ord rec 253m vs dep 258m+; balance via past provisions; debt 210m class; transfers +9.4m,medium,src_ixelles_budget_2026_dh,Ixelles residents,Local equilibrium,Structural if transfers keep rising; not pure waste but fiscal risk,5,5.0,4,5.0,Stop provision draw; open full BI PDF; cut non-core transfers,seed,,tick155",
    "lb_ixelles_iris_catchup,Ixelles Iris hospital deficit catch-up 4.75m,local,transfer,Bruxelles>Ixelles>Iris,4750000,4750000,Transfer to apurer Iris 2024-25 deficits quoted; dual hospital governance opacity,medium,src_ixelles_budget_2026_dh,Hospital users,Hospital network catch-up,Inter-level cost shift to commune,5,5.0,5,5.0,FOI Iris multi-year path; regional hospital funding review,seed,,tick155",
    "lb_schaerbeek_invest_60m,Schaerbeek invest package 60m 2026,local,programme,Bruxelles>Schaerbeek>invest,60000000,60000000,RTBF medium total 60m; named creches 6.5+6m RenovaS 5m sport 2m trottoirs 1.5m strong sample,medium,src_schaerbeek_budget_2026_rtbf,Schaerbeek residents,Public space social infrastructure,Core mandate if unit costs controlled; ASBL L5 missing,3,6.5,4,5.0,Publish ordinary totals; open ASBL top20; unit-cost creches,seed,,tick155",
    "lb_anderlecht_voirie_2m,Anderlecht voirie package 2.05m 2026,local,invest,Bruxelles>Anderlecht>voirie,2050000,2050000,Official CP asphalt 1.2m + sidewalks 0.85m; associative envelope maintained without EUR,strong,src_anderlecht_cp_budget_2026,Anderlecht residents,Public space,Core maintenance; full budget opacity,2,4.0,3,3.3,Publish full BI + associative L5,seed,,tick155",
]
append_if_missing(DATA / "leaderboard.csv", lbs)

# --- FOI ---
foi_row = (
    f"{GAP},Bruxelles>communes>Ixelles_Schaerbeek_Anderlecht>subsidies_top20,brussels_gov,"
    "Full BI2026 ordinary+extra PDFs; ranked top20 third-party ASBL/subsidies with EUR 2025-2026 for Ixelles Schaerbeek Anderlecht; reconcile Ixelles transfers and Schaerbeek ordinary totals,"
    "Named invest L5 partial public; associative top20 and full opex still opaque especially Anderlecht,"
    "6,Communes Ixelles Schaerbeek Anderlecht publicite administration,,,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-07-28,,,,,"
    "cmt_ixelles_budget_2026|cmt_schaerbeek_invest_2026|cmt_anderlecht_invest_space_2026,"
    "lb_ixelles_ord_gap|lb_schaerbeek_invest_60m,"
    f"{UTC},{UTC},tick155 partial public fill; residual human send"
)
text_f = read_text(DATA / "foi_queue.csv")
if GAP not in text_f:
    if not text_f.endswith("\n"):
        text_f += "\n"
    write_text(DATA / "foi_queue.csv", text_f + foi_row + "\n")

FOI.mkdir(parents=True, exist_ok=True)
draft = f"""# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `{GAP}`  
**Status:** ready (human send only)  
**Linked:** {UNIT}

---

## Brief (FR — tri-commune)

```text
[Nom]
[Adresse]
[E-mail]
[Date]

A: Service publicite de l'administration
   - Commune d'Ixelles
   - Commune de Schaerbeek (1030.be)
   - Commune d'Anderlecht

Objet: Demande de publicite — budgets initiaux 2026 et top 20 subventions tierces 2025-2026

Madame, Monsieur,

Sur la base du decret bruxellois relatif a la publicite de l'administration,
je sollicite pour chacune des trois communes:

1. Le budget initial 2026 complet (service ordinaire + extraordinaire + annexes)
   en PDF machine-lisible, avec totaux recettes/depenses ordinaires et d'investissement.
2. La liste classee (CSV) des 20 plus importantes subventions / interventions
   a des tiers (ASBL, ASBL culture, sport, cohesion sociale, etc.) pour 2025 et 2026,
   avec nom du beneficiaire, montant, base legale ou deliberation, et objet.
3. Pour Ixelles: detail des transferts 2026 vers CPAS, reseau Iris et zone de police
   (reconciliation des montants cites publiquement: CPAS +6,07 m; Iris 4,75 m; police +0,3 m).
4. Pour Schaerbeek: totaux ordinaires 2026 (recettes/depenses) et dotation CPAS communale
   hors moyens federaux cites (~17 m).
5. Pour Anderlecht: totaux ordinaires 2026 et enveloppe associative/sport/jeunesse
   maintenue (montants absents du communique).

Periode: 2025-01-01 a 2026-12-31.

Reference interne: {GAP}

Cordialement,
[Nom]
```

---

## Checklist

- [x] Trois communes
- [x] Documents concrets
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
"""
(FOI / f"{GAP}.md").write_text(draft, encoding="utf-8")

# --- research_queue ---
rq_new = (
    f"rq_145,Brussels communes top 3 L5 sample,continuous,5,done,L5,brussels_gov,"
    f'"Ixelles/Schaerbeek/Anderlecht named subsidies sample.",{GAP},2026-07-27T14:00:00Z,{UTC},'
    "tick155: Ixelles ord ~253/258m invest 46.2m; Schaerbeek invest 60m named creches/RenovaS; "
    "Anderlecht voirie 2.05m; residual ASBL top20 FOI ready"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_145,", rq_new):
    raise SystemExit("rq_145 not found")

# --- loop_state ---
state = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio5 DGD defence justice; FOI ready human send. rq_145 Brussels communes L5 sample done."\n'
)
write_text(DATA / "loop_state.csv", state)

# --- loop_log ---
log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Brussels communes Ixelles / Schaerbeek / Anderlecht L5 sample)
- Found:
  - **Ixelles (medium — DH quotes echevine Gilson):** ord rec **~EUR 253m** · ord dep **~EUR 258m+** · provisions **>5.5m** · invest **46.2m** (emprunt **26.9m**) · transfers **+9.4m** (CPAS **+6.07m** · Iris catch-up **4.75m** · police **+0.3m**) · debt path **119→210m** · participatif **0.17m strong**.
  - **Schaerbeek (strong note + medium RTBF total):** invest **EUR 60m** · Brichaut creche **6.5m** (commune **1.3m**) · Hoogvorst **~6m** (commune **2m**) · RenovaS Dupont **5m** · Plantes **3m** · sport **>2m** · trottoirs **1.5m** · Terdelt **1.2m** · CPAS federal class **~17m** · AS hire **0.95m**.
  - **Anderlecht (strong CP):** equilibrium claimed · asphalt **1.2m** · sidewalks **0.85m** · associative/sport maintained without EUR totals.
- Wrote: sources 5; entities 3; budgets ~27; cmt 3; lb 4; rq_145=done; FOI residual ready.
- FOI: {GAP} (full BI PDFs + ASBL top20 ×3) human send only.
- Next: prio5 **rq_146 DGD** / **rq_147 defence** / **rq_150 justice** / **rq_121 hole-fill**.
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)

print("OK tick", TICK, UNIT)

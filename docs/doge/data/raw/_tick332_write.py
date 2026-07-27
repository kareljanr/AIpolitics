# tick 332: RV Belgica II capital dual Belspo marine research
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge/data/raw -> repo root? 
# Path: docs/doge/data/raw/_tick332_write.py -> parents[0]=raw, [1]=data, [2]=doge, [3]=docs, [4]=repo
ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

def append(path: Path, text: str):
    with path.open("a", encoding="utf-8", newline="\n") as f:
        if not text.startswith("\n") and path.stat().st_size > 0:
            # ensure leading newline if file doesn't end with one
            with path.open("rb") as rb:
                rb.seek(-1, 2)
                last = rb.read(1)
            if last != b"\n":
                f.write("\n")
        f.write(text if text.endswith("\n") else text + "\n")

# --- sources ---
append(DATA / "sources.csv", """src_belspo_belgica_timeline,BELSPO RV Belgica NewRV official timeline CM budget award and launch,https://www.belspo.be/belspo/NewRV/timeline_en.stm,BELSPO,2026-07-31,official_portal,"Strong: CM 28Oct2016 budget 54.45 MEURO; financing study 4Apr2014 54.45 MEURO incl VAT; CM 22Dec2017 Freire award 53.7 MEURO; launch 11Feb2020 cost ~54m VAT incl; Genavir ops Nov2021; arrival Zeebrugge Dec2021; baptism Jun2022; dual BELSPO RBINS Defence; tick332"
src_belgica_vliz_financing_study,Naudts et al VLIZ/RBINS financing study RV Belgica II build and ops cost,https://www.vliz.be/imisdocs/publications/264118.pdf,RBINS OD Nature + BELSPO (via VLIZ),2026-07-31,primary_study,"Strong-medium: expected build 54.45 MEURO incl VAT; exploitation 4.3 MEURO/yr for 300 days 2 crews; dual Simon Stevin VLIZ; financing study 2013-14; tick332"
src_navalnews_belgica_launch_2020,Naval News Freire launch Belgica research vessel Feb 2020,https://www.navalnews.com/naval-news/2020/02/freire-shipyard-launched-belgian-navys-future-belgica-research-vessel/,Naval News,2026-07-31,press,"Medium: project Oct2016 total cost 54m; Defence staff Zeebrugge; 300 days/yr; 28 scientists+12 crew; dual MoD RBINS BELSPO; tick332"
""")

# --- entity ---
append(DATA / "entities.csv", """rv_belgica,Onderzoeksschip RV Belgica,Navire de recherche RV Belgica,Belgian federal oceanographic research vessel,asset,belspo,bi,https://www.belspo.be/belspo/NewRV/index_en.stm,,,Owned Belgian State via BELSPO; Freire build award 53.7m CM budget 54.45m; ops Genavir; dual VLIZ Simon Stevin + Defence; tick332
""")

# --- budgets ---
append(DATA / "budgets.csv", """bud_belgica_cm_budget_2016,rv_belgica,2016,54450000,,,budgeted,src_belspo_belgica_timeline,strong,CM 28Oct2016 budget 54.45 MEURO replace RV Belgica (incl VAT financing study)
bud_belgica_award_freire_2017,rv_belgica,2017,53700000,,,budgeted,src_belspo_belgica_timeline,strong,CM 22Dec2017 award Freire Shipyard Vigo 53.7 MEURO design+build
bud_belgica_project_cost_launch_2020,rv_belgica,2020,54000000,,,budgeted,src_belspo_belgica_timeline,strong,BELSPO launch press 11Feb2020 project cost approx 54m VAT included
bud_belgica_ops_class_annual,rv_belgica,2014,4300000,,,budgeted,src_belgica_vliz_financing_study,medium,Financing study class: exploitation 4.3 MEURO/yr for 300 days at sea (2 crews) — not confirmed outturn
""")

# --- commitments ---
append(DATA / "commitments.csv", """cmt_belgica_ii_capital_ops,RV Belgica II federal marine research capital and ops dual Belspo,rv_belgica,Marine scientists RBINS universities Defence North Sea Europe,CM Oct2016 + CM Dec2017 Freire + BELSPO ownership Genavir ops,2016-10-28,2016,2046,54450000,"{""cm_budget_2016_m"":54.45,""award_freire_2017_m"":53.7,""launch_press_cost_m"":54,""ops_class_annual_m"":4.3,""ops_days_class"":300,""crews_class"":2,""operator"":""Genavir_FR"",""delivery"":""2021-12 Zeebrugge"",""baptism"":""2022-06-25"",""partners"":""BELSPO RBINS Defence"",""dual_vliz"":""Simon_Stevin_Flanders"",""note"":""Capital strong primary BELSPO timeline; annual ops class from 2013-14 financing study residual FOI outturn Genavir contract""}",0,active,https://www.belspo.be/belspo/NewRV/timeline_en.stm,Federal multipurpose oceanographic research infrastructure,Publish multi-year CAPEX cash path and annual Genavir ops cost; dual unit-cost vs VLIZ Stevin,src_belspo_belgica_timeline,strong,Federal>BELSPO>RV_Belgica,tick332: 54.45m capital dual marine research
""")

# --- leaderboard ---
append(DATA / "leaderboard.csv", """lb_belgica_capital_54m,RV Belgica federal research vessel capital ~54m dual Belspo marine,federal,ops,Federal>BELSPO>RV_Belgica,4300000,54450000,Strong BELSPO timeline: CM budget 54.45m award Freire 53.7m; ops class 4.3m/yr financing study medium; dual VLIZ Simon Stevin Genavir ops,strong,src_belspo_belgica_timeline,Marine scientists public,Federal oceanographic research infrastructure,Core research infrastructure not pure waste; CAPEX sunk; ops FOI residual dual Flanders vessel,2,6.5,3,4.15,Publish annual ops cash Genavir; dual unit-cost Simon Stevin,seed,,tick332
""")

# --- foi_queue ---
append(DATA / "foi_queue.csv", """gap_belgica_ops_l5,Federal>BELSPO>RV_Belgica>ops_and_cash,rv_belgica,Cash-by-year CAPEX outturn 2016-2022 vs 54.45m budget and 53.7m award; annual ops cost Genavir management contract 2022-2026 with EUR; BA codes; dual Defence base support Zeebrugge cash; days-at-sea outturn vs 300 class,Capital envelope strong BELSPO timeline; annual ops and Genavir L5 residual,4,BELSPO / RBINS OD Nature / Defence / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,docs/doge/foi/drafts/gap_belgica_ops_l5.md,ready,2026-07-31,,,,,cmt_belgica_ii_capital_ops,lb_belgica_capital_54m,2026-07-31T04:45:00Z,2026-07-31T04:45:00Z,tick332 draft ready human send
""")

# --- research_queue update ---
rq_path = DATA / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = "rq_323,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T04:15:00Z,,Spawned tick331 after ESA BE; rq_116 SWA deferred"
new = "rq_323,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_belgica_ops_l5,2026-07-31T04:15:00Z,2026-07-31T04:45:00Z,tick332: RV Belgica capital 54.45m award 53.7m ops class 4.3m/yr dual Belspo marine; FOI ops L5; spawn rq_324"
if old not in rq:
    raise SystemExit("rq_323 open row not found")
rq = rq.replace(old, new)
if "rq_324," not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += "rq_324,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T04:45:00Z,,Spawned tick332 after Belgica II; rq_116 SWA deferred\n"
rq_path.write_text(rq, encoding="utf-8")

# --- belspo entity note ---
ent_path = DATA / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
ent_old = "Managed budget ~570-630m; ESA contrib 284m 2025 strong MERI; FWI ~25pct; cut 93m; dual community research; tick329+331"
ent_new = "Managed budget ~570-630m; ESA 284m 2025; RV Belgica capital 54.45m; FWI ~25pct; cut 93m; dual community research; tick329-332"
if ent_old in ent:
    ent = ent.replace(ent_old, ent_new)
    ent_path.write_text(ent, encoding="utf-8")
else:
    print("WARN: belspo note not updated")

# --- loop_state ---
(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T04:45:00Z,rq_323,332,no,Scheduler 60s. Next prio5 rq_324; rq_116 SWA deferred. FOI ready. tick332 RV Belgica 54.45m capital dual Belspo marine.\n",
    encoding="utf-8",
)

# --- FOI draft ---
FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_belgica_ops_l5.md").write_text("""# FOI draft — gap_belgica_ops_l5

Status: **ready** (human send only).  
Not legal advice — verify procedure with counsel if needed.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO)
t.a.v. de dienst openbaarheid van bestuur
cc: Koninklijk Belgisch Instituut voor Natuurwetenschappen (KBIN/RBINS) — OD Nature
cc: Ministerie van Defensie — Marinecomponent Zeebrugge
cc: IBZ openbaarheid
https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — RV Belgica
kapitaal-kaspad en Genavir-exploitatiekosten 2016-2026

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
en aanvullende federale bepalingen dien ik hierbij een verzoek in tot
openbaarmaking / afschrift van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. Het **kaspad (cash-by-year) 2016-2022** van de aankoop/bouw van het
   onderzoeksschip **RV Belgica** (opvolger A962), met:
   - reconciliatie met de **CM-beslissing van 28 oktober 2016**
     (budget **54,45 MEURO**);
   - reconciliatie met de **toewijzing Freire Shipyard (CM 22 december 2017)**
     van **53,7 MEURO**;
   - begrotingsartikelcodes (BA) en eventuele bijkomende uitrustings-
     of wisselkoerskosten.
2. Het **beheers- en operatiecontract met Genavir** (sinds november 2021):
   - jaarlijkse kost in EUR 2022-2026 (bemanning, maintenance, brandstof-
     forfait of werkelijke, verzekering, havengelden indien via Genavir);
   - looptijd, indexering, herzieningsclausules.
3. **Dagen op zee (days-at-sea)** outturn 2022-2025 vs de klasse van
   **~300 dagen/jaar** uit de financieringsstudie.
4. Eventuele **Defensie-bijdrage** (Zeebrugge-basisondersteuning, personeel,
   logistiek) cash-by-year of in natura met EUR-waardering indien beschikbaar.
5. Eventuele **vergelijking / afstemming** met het Vlaamse onderzoeksschip
   **RV Simon Stevin** (VLIZ) — gedeelde campagnes of cost-sharing.

Periode: 2016 tot en met 2026 (en nog lopende verbintenissen).

### 2. Context (waarom)

Dit verzoek kadert in onderzoek naar overheidsuitgaven en federale
onderzoeks-infrastructuur (transparantie van publieke middelen).
Hiërarchisch pad (intern): Federal > BELSPO > RV_Belgica > ops_L5.

Publiek is reeds bekend (BELSPO NewRV timeline): CM-budget **€54,45 m**
(2016); Freire-toewijzing **€53,7 m** (2017); projectkost bij tewaterlating
**~€54 m** BTW incl. (2020); aankomst Zeebrugge december 2021; doop juni
2022; operator Genavir. Residual is kaspad CAPEX-outturn en jaarlijkse
exploitatie.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail].
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: gap_belgica_ops_l5

Met vriendelijke groet,

[Naam]
```

---
""", encoding="utf-8")

# --- loop_log ---
log_entry = """
### 2026-07-31T04:45:00Z - tick 332
- Unit: **rq_323** (FOI-adjacent hole-fill - **RV Belgica II federal marine research dual Belspo**)
- Found (strong BELSPO NewRV timeline + financing study class):
  - CM **28 Oct 2016** budget **€54.45m** (incl VAT) for replacement vessel.
  - CM **22 Dec 2017** award Freire Shipyard (Vigo) **€53.7m**.
  - Launch press **11 Feb 2020**: project cost **~€54m** VAT included.
  - Delivery Zeebrugge **Dec 2021**; baptism **25 Jun 2022** (Princess Elisabeth).
  - Operator **Genavir** (FR oceanographic fleet) from **Nov 2021**.
  - Financing study class ops **€4.3m/yr** for **300 days** (2 crews) — medium, not outturn.
  - Dual: BELSPO ownership + RBINS science + Defence base; complementary **VLIZ Simon Stevin**.
- Wrote: sources +3; entity rv_belgica (+belspo note); budgets +4; cmt +1; lb +1; FOI gap_belgica_ops_l5 ready; draft; rq_323=done; spawn rq_324; ticks=332
- FOI: CAPEX cash path + Genavir ops L5 ready human send
- Next: prio5 **rq_324**; deferred **rq_116** SWA
"""
append(LOG, log_entry)

print("tick332 write OK")
print("ROOT", ROOT)

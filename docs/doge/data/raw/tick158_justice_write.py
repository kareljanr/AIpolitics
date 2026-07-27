# -*- coding: utf-8 -*-
"""Tick 158 — rq_150 Justice prisons courts operating overhead dual NL/FR."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 158
UNIT = "rq_150"
UTC = "2026-07-28T02:30:00Z"
GAP = "gap_justice_dual_lang_tolk"


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
    out, found = [], False
    for L in lines:
        if L.startswith(prefix):
            out.append(new_line)
            found = True
        else:
            out.append(L)
    write_text(p, "\n".join(out) + "\n")
    return found


srcs = [
    'src_fod_justitie_psp_2026_29,FOD Justitie Strategisch plan 2026-2029 budget context,https://justitie.belgium.be/sites/default/files/news/PSP-NL-DEF.pdf,FOD Justitie,2026-07-28,official_strategy,"Annual Justice budget ~2.7bn; courts 1431m prisons 799m ops 496.7m invest 74.7m personnel 67pct; tick158"',
    'src_coa_prisons_dbfm_2023,Rekenhof 2023 Nieuwe gevangenissen via PPS DBFM,https://www.ccrek.be/sites/default/files/Docs/2023_27_NieuweGevangenissen.pdf,Rekenhof Cour des comptes,2026-07-28,official_audit,"9 DBFM prisons 3874 places; annual fees >=153.1m when all open; 25y cost 3.828bn; Haren 48.4m/yr; tick158"',
    'src_justice_prison_cost_2022,Justice ministry annual prison figures cost per detainee 2022,https://justice.belgium.be/sites/default/files/Chiffres%20annuels%202022%20Etablissements%20p%C3%A9nitentiaires%20.pdf,FOD Justitie DG EPI,2026-07-28,official_stats,"Average cost per prisoner EUR 55624.24 in 2022; tick158"',
    'src_prisonstudies_be_2025,World Prison Brief Belgium population Nov 2025,https://www.prisonstudies.org/country/belgium,Institute for Crime and Justice Policy Research / MoJ,2026-07-28,secondary_official,"Population 13483 capacity 11098 occupancy 121.5pct Nov 2025; tick158"',
]
append_if_missing(DATA / "sources.csv", srcs)

ents = [
    "fod_justice,FOD Justitie / SPF Justice,Service public federal Justice,Federal Public Service Justice,ministry,sec_federal,bi,https://justitie.belgium.be,,Brussels,Annual budget ~2.7bn; courts 1.43bn prisons 0.80bn; bilingual federal justice; tick158",
    "dg_epi,DG Penitentiaire Inrichtingen / DG Etablissements penitentiaires,DG EPI,Directorate-General Penitentiary Institutions,agency,fod_justice,bi,https://justitie.belgium.be,,Belgium,Prison administration; 799m 2025 line; overcrowding 121pct; tick158",
]
append_if_missing(DATA / "entities.csv", ents)

bud = [
    # FOD totals PSP
    "bud_justice_total_class_2025,fod_justice,2025,2700000000,,,budgeted,src_fod_justitie_psp_2026_29,medium,FOD strategic plan: annual Justice budget estimated about 2.7bn this legislature",
    "bud_justice_courts_ro_2025,fod_justice,2025,1431000000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Ordinary courts rechterlijke orde afdeling 56: 1431m (2023 was 1313m)",
    "bud_justice_prisons_2025,dg_epi,2025,799000000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Prison system afdeling 51: 799m 2025",
    "bud_justice_legislation_dg_2025,fod_justice,2025,41300000,,,budgeted,src_fod_justitie_psp_2026_29,strong,DG Legislation and fundamental rights 41.3m",
    "bud_justice_cults_2025,fod_justice,2025,136200000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Erediensten and vrijzinnigheid 136.2m",
    "bud_justice_central_support_2025,fod_justice,2025,184100000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Support and central services 184.1m (2023 169.0m)",
    "bud_justice_special_services_2025,fod_justice,2025,55300000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Special services e.g. Kansspelcommissie afdeling 62: 55.3m (2023 39.4m)",
    "bud_justice_grants_dotations_2025,fod_justice,2025,303000000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Toelagen and dotaties 303m of annual budget",
    "bud_justice_operating_2025,fod_justice,2025,496736000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Werkingskredieten 496.736m (food detainees court costs legal aid victim aid)",
    "bud_justice_invest_2025,fod_justice,2025,74731000,,,budgeted,src_fod_justitie_psp_2026_29,strong,Investeringskredieten only 74.731m of regular credits",
    # unit costs / population
    "bud_justice_cost_per_prisoner_2022,dg_epi,2022,55624.24,,,outturn,src_justice_prison_cost_2022,strong,Official average cost per prisoner EUR 55624.24 in 2022",
    "bud_justice_prison_pop_2025,dg_epi,2025,13483,,,outturn,src_prisonstudies_be_2025,medium,Prison population 13483 Nov 2025 MoJ via WPB",
    "bud_justice_prison_capacity_2025,dg_epi,2025,11098,,,outturn,src_prisonstudies_be_2025,medium,Official capacity 11098 Nov 2025 occupancy 121.5pct",
    # DBFM CoA named L5
    "bud_justice_dbfm_annual_all9,dg_epi,2029,153100000,,,budgeted,src_coa_prisons_dbfm_2023,strong,CoA: annual DBFM fees >=153.1m once all 9 prisons operational",
    "bud_justice_dbfm_25y_total,dg_epi,2023,3827900000,,,commitment,src_coa_prisons_dbfm_2023,strong,CoA: 9 DBFM prisons total cost over 25 years 3827.9m",
    "bud_justice_dbfm_mp1_annual,dg_epi,2023,53000000,,,outturn,src_coa_prisons_dbfm_2023,strong,MP1 four prisons annual fees sum 53.0m (Beveren 13.6 Marche 12.3 Leuze 12.1 Dendermonde 15.0)",
    "bud_justice_dbfm_haren_annual,dg_epi,2023,48400000,,,outturn,src_coa_prisons_dbfm_2023,strong,Haren annual fee 48.4m capacity 1190 places",
    "bud_justice_dbfm_haren_25y,dg_epi,2023,1210900000,,,commitment,src_coa_prisons_dbfm_2023,strong,Haren total cost over 25y 1210.9m",
    "bud_justice_dbfm_beveren_annual,dg_epi,2023,13600000,,,outturn,src_coa_prisons_dbfm_2023,strong,Beveren annual 13.6m capacity 312",
    "bud_justice_dbfm_dendermonde_annual,dg_epi,2023,15000000,,,outturn,src_coa_prisons_dbfm_2023,strong,Dendermonde annual 15.0m capacity 444",
    "bud_justice_dbfm_antwerpen_annual,dg_epi,2026,17700000,,,budgeted,src_coa_prisons_dbfm_2023,medium,Antwerpen annual 17.7m at award capacity 440 (may change before financial close)",
    "bud_justice_dbfm_offbalance_2022,dg_epi,2022,2600000000,,,commitment,src_coa_prisons_dbfm_2023,strong,Legal commitment off-balance sheet DBFM 2.6bn end-2022",
    "bud_justice_dbfm_places_total,dg_epi,2029,3874,,,budgeted,src_coa_prisons_dbfm_2023,strong,9 DBFM prisons planned capacity addition 3874 places (5 open ~2570 in 2023 audit)",
]
append_if_missing(DATA / "budgets.csv", bud)

cmts = [
    (
        'cmt_justice_budget_split_2025,FOD Justice annual budget split courts prisons cults,fod_justice,Rechterlijke orde DG EPI FOD services,'
        'FOD Justitie Strategisch plan 2026-2029 Financieel beheer,2025-01-01,2025,2029,2700000000,'
        '"{""total_class"":2700000000,""courts_ro"":1431000000,""prisons"":799000000,""legislation"":41300000,'
        '""cults"":136200000,""central"":184100000,""special"":55300000,""grants"":303000000,'
        '""operating"":496736000,""invest"":74731000,""personnel_share"":""67pct_regular_credits""}",0,active,'
        'https://justitie.belgium.be/sites/default/files/news/PSP-NL-DEF.pdf,Federal justice courts detention legislation,'
        'Publish Kamer sectie 12 line codes cash; dual language tolk/vertaling L5; court backlog KPIs,'
        'src_fod_justitie_psp_2026_29,strong,Federal>Justitie>budget,'
        'tick158; bilingual structure constitutional; residual FOI interpreter dual-pub costs'
    ),
    (
        'cmt_justice_dbfm_prisons_25y,Prison DBFM PPP nine facilities multi-year,dg_epi,Regie der Gebouwen private consortia,'
        'Rekenhof 2023 DBFM prisons audit + masterplans 1-3,2008-04-18,2013,2050,3827900000,'
        '"{""prisons"":9,""places"":3874,""annual_fees_all9_min"":153100000,""cost_25y"":3827900000,'
        '""haren_annual"":48400000,""haren_places"":1190,""mp1_annual"":53000000,'
        '""offbalance_eoy2022"":2600000000,""note"":""private finance premium vs state borrowing CoA; annual fees index-linked""}",0,active,'
        'https://www.ccrek.be/sites/default/files/Docs/2023_27_NieuweGevangenissen.pdf,'
        'Humane prison infrastructure capacity overcrowding,'
        'Annual parliament multi-year fee table; VFM vs classic build; CoA 2026 follow-up,'
        'src_coa_prisons_dbfm_2023,strong,Federal>Justitie>DBFM_prisons,'
        'tick158; off-balance long-term lock-in; dual NL/FR prison ops separate residual'
    ),
    (
        'cmt_justice_unit_cost_detention,Detention unit cost and overcrowding 2022-2025,dg_epi,Detainees prison system,'
        'Justice annual prison stats 2022 + WPB Nov 2025,2022-12-31,2022,2025,55624,'
        '"{""cost_per_prisoner_2022"":55624.24,""pop_2025_11"":13483,""capacity_2025_11"":11098,'
        '""occupancy_pct"":121.5,""implied_ops_class"":""pop*unit_cost ~750m vs budget line 799m medium reconcile""}",0,active,'
        'https://justice.belgium.be,Detention capacity overcrowding,'
        'Update unit cost series annually; reduce pre-trial share; alternatives to custody,'
        'src_justice_prison_cost_2022,strong,Federal>Justitie>detention_unit_cost,'
        'tick158; overcrowding drives cost and rights risk'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

lbs = [
    "lb_justice_total_2_7bn,FOD Justice package ~2.7bn annual,federal,ops,Federal>Justitie>budget,2700000000,2700000000,PSP strong split: courts 1.43bn prisons 0.80bn ops 0.50bn invest only 0.07bn; personnel 67pct,strong,src_fod_justitie_psp_2026_29,Citizens detainees litigants,Rule of law courts detention,Core state function; under-investment invest line thin; dual language structural,3,8.5,4,6.2,Publish sectie12 codes; backlog KPIs; dual-lang cost FOI,seed,,tick158",
    "lb_justice_prisons_799m,Prison system budget 799m 2025 + overcrowding,federal,ops,Federal>Justitie>prisons,799000000,799000000,PSP 799m afd51; pop 13483 vs capacity 11098 (121.5pct); unit cost 55.6k 2022,strong,src_fod_justitie_psp_2026_29,Detainees staff public safety,Detention and reintegration,Overcrowding rights risk; DBFM fees layer on top,5,7.5,5,6.5,Reduce pre-trial; unit cost path; DBFM fee transparency,seed,,tick158",
    "lb_justice_dbfm_153m,Prison DBFM annual fees path >=153m,federal,procurement,Federal>Justitie>DBFM_fees,153100000,3827900000,CoA strong: 9 prisons 25y 3.83bn; annual >=153.1m full; Haren alone 48.4m/yr; off-balance 2.6bn eoy2022,strong,src_coa_prisons_dbfm_2023,Detainees Regie Gebouwen,Prison infrastructure PPP,Private finance premium vs state debt; lock-in 25y; parliament multi-year opacity CoA,6,7.5,5,6.8,Annual multi-year fee table in budget; VFM recheck; 2026 CoA follow-up,seed,,tick158",
    "lb_justice_courts_1_43bn,Ordinary courts rechterlijke orde 1.43bn,federal,ops,Federal>Justitie>courts,1431000000,1431000000,PSP: afd56 1431m up from 1313m 2023; bilingual judicial organisation constitutional,strong,src_fod_justitie_psp_2026_29,Litigants accused victims,Judicial adjudication,Core; dual NL/FR structure not optional waste but cost opaque without tolk FOI,3,8.0,5,6.0,FOI interpreter translation dual-publication costs; backlog,seed,,tick158",
]
append_if_missing(DATA / "leaderboard.csv", lbs)

# update multi_parliaments gap note optionally - new FOI for tolk
foi_row = (
    f"{GAP},Federal>Justitie>dual_language_tolk_courts,fod_justice,"
    "Cash-by-year 2022-2026 for court interpreters sworn translators dual-language publications bilingual court admin; split NL/FR caseload costs; DG EPI dual prison language staffing if material,"
    "Bilingual justice is constitutional; euro cost of dual ops not published separately from 1.43bn courts / 0.80bn prisons,"
    "6,FOD Justitie openbaarheid / College hoven en rechtbanken,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-07-28,,,,,"
    "cmt_justice_budget_split_2025,lb_justice_courts_1_43bn,"
    f"{UTC},{UTC},tick158 partial budget+DBFM; residual dual-lang FOI; also gap_multi_parliaments related"
)
text_f = read_text(DATA / "foi_queue.csv")
if GAP not in text_f:
    if not text_f.endswith("\n"):
        text_f += "\n"
    write_text(DATA / "foi_queue.csv", text_f + foi_row + "\n")

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(f"""# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `{GAP}`  
**Status:** ready (human send only)  
**Linked:** {UNIT} · gap_multi_parliaments (related)

---

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: FOD Justitie — dienst openbaarheid van bestuur
     en/of College van de hoven en rechtbanken / College OM
     (federaal: https://www.ibz.be/nl/openbaarheid-van-bestuur)

Betreft: Verzoek om openbaarmaking — kosten tweetaligheid Justitie (tolken/vertalingen) 2022-2026

Geachte,

Op grond van de wet 11 april 1994 inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Cash-by-year 2022-2026 van uitgaven voor:
   - beedigde tolken en vertalers in straf- en burgerlijke zaken;
   - tweetalige publicaties en vertaling van rechterlijke documenten;
   - eventuele aparte NL/FR administratieve ondersteuning bij hoven/rechtbanken
     (indien in de boekhouding onderscheiden).
2. Begrotingscodes (sectie 12 FOD Justitie / afdeling 56) waarop die uitgaven
   worden aangerekend, met goedgekeurde en vereffende bedragen.
3. Indien beschikbaar: caseload-split NL/FR per arrondissement of taalrol
   (zonder persoonsgegevens).
4. Optioneel DG EPI: materiële meerkosten tweetalige detentielabels/communicatie
   indien afzonderlijk geboekt.

Periode: 2022-01-01 tot meest recente stand.

### 2. Context

FOD Justitie PSP 2026-2029 raamt Justitie op ca. EUR 2,7 miljard (rechterlijke orde
EUR 1,431 miljard; gevangenissen EUR 799 miljoen). De tweetalige organisatie is
grondwettelijk; de euro-kost is niet als L5 openbaar. DBFM-gevangenissen (Rekenhof 2023)
zijn apart in kaart gebracht.

Hierarchie intern: Federal > Justitie > dual_language / courts.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {GAP}

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling (FOD Justitie / Colleges)
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
""", encoding="utf-8")

rq_new = (
    f"rq_150,Justice prisons courts operating overhead dual NL/FR,continuous,5,done,L5,sec_federal,"
    f'"Court/prison dual language cost samples.",{GAP},2026-07-27T14:00:00Z,{UTC},'
    "tick158: Justice ~2.7bn courts 1.43bn prisons 799m; DBFM annual >=153m 25y 3.83bn; "
    "unit cost 55.6k 2022; residual dual-lang FOI"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_150,", rq_new):
    raise SystemExit("rq_150 not found")

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio4 police zones; prio5 hole-fill FOI-adjacent; FOI ready human send. rq_150 justice done."\n',
)

log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Justice prisons courts dual NL/FR overhead sample)
- Found (strong primary FOD PSP + Rekenhof DBFM 2023):
  - **Justitie ~EUR 2.7bn/yr:** courts **1.431bn** · prisons **799m** · cults **136.2m** · central **184.1m** · grants **303m** · ops **496.7m** · invest **74.7m** · personnel **67%**.
  - **Detention:** unit cost **EUR 55,624** (2022) · pop **13,483** / capacity **11,098** (121.5% Nov 2025).
  - **DBFM prisons (CoA):** 9 sites **3,874** places · annual fees **≥153.1m** full · **25y EUR 3.828bn** · Haren **48.4m/yr** (1,190 places) · MP1 **53.0m/yr** · off-balance **2.6bn** eoy2022.
  - Dual NL/FR: constitutional; euro L5 (tolk/vertaling) **not** published → FOI.
- Wrote: sources 4; entities 2; budgets ~23; cmt 3; lb 4; rq_150=done; FOI residual ready.
- FOI: {GAP} (interpreter/dual-lang cash) human send only.
- Next: prio4 **rq_151 police zones** / prio5 **rq_121 hole-fill** / deferred **rq_116 SWA**.
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)
print("OK tick", TICK, UNIT)

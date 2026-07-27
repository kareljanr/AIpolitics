# tick 335 — FED-tWIN dual FSI-university + DIGIT-04
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T06:15:00Z"

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_belspo_fedtwin_page,BELSPO FED-tWIN programme official page profiles batches dual FSI universities,"
        "https://www.belspo.be/belspo/research/FEDtWIN_en.stm,BELSPO,2026-07-31,official_portal,"
        "Strong: 125 profiles 5 batches of 25 2019-2024; funded 100pct 5y then 50pct next 5y; "
        "law 21Jul2017 RD 14Oct2018; dual FSI-universities linguistic communities; tick335\n"
    )
    f.write(
        "src_rmah_research_strategy_2023,RMAH Research Strategy Digital 2023 FED-tWIN rates DIGIT-04 envelope,"
        "https://www.artandhistory.museum/sites/default/files/2023-12/Research-strategy-RMAH-Digital-corr.pdf,"
        "Royal Museums of Art and History KMKG-MRAH,2026-07-31,official_strategy,"
        "Strong-medium: FED-tWIN annual 125k first 5y then 75k next 5y per profile; "
        "DIGIT-04 37.63m 2019-24 all 10 FSI+Cinematek ca 380k/yr RMAH; P4S/S4P successor note; tick335\n"
    )
    f.write(
        "src_climat_be_belspo_climate_funds,climat.be BELSPO climate-related projects and funds 2019-2027,"
        "https://climat.be/doc/belspo-climate-related-projects-and-funds-2021-2026-docx.pdf,"
        "climat.be / BELSPO,2026-07-31,official_inventory,"
        "Strong: climate portfolio total 39.2m 2019-27 / 32.9m 2022-26; FedTwin postdocs climate "
        "13 projects 9.25m 2020-26; Polar call 1.667m; BELGICA call 1.997m; BRAIN-P1 11.681m; tick335\n"
    )

# --- entities ---
with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "fedtwin_belspo,FED-tWIN BELSPO FSI-university research profiles,"
        "FED-tWIN programme BELSPO,"
        "Federal dual research profiles postdocs half FSI half university,"
        "programme,belspo,bi,https://www.belspo.be/belspo/FED-tWIN/,,,"
        "125 profiles 5x25 2019-24; 125k/yr then 75k/yr class; dual community unis; tick335\n"
    )
    f.write(
        "digit04_belspo,DIGIT-04 BELSPO federal heritage digitisation,"
        "DIGIT-04 programme BELSPO,"
        "Digitisation long-term preservation access federal FSI collections + Cinematek,"
        "programme,belspo,bi,https://www.belspo.be/,,,,"
        "Envelope 37.63m 2019-2024 10 FSI+Cinematek; dual community heritage; tick335\n"
    )

# --- budgets ---
bud = [
    "bud_fedtwin_rate_yr1_5,fedtwin_belspo,2024,125000,,,budgeted,src_rmah_research_strategy_2023,strong,FED-tWIN annual budget per profile first five years 125k (RMAH strategy cites BELSPO rates)",
    "bud_fedtwin_rate_yr6_10,fedtwin_belspo,2026,75000,,,budgeted,src_rmah_research_strategy_2023,strong,FED-tWIN annual budget per profile years 6-10 75k (after 50pct step-down vs full; RMAH)",
    "bud_fedtwin_profile_count,fedtwin_belspo,2024,125,,,budgeted,src_belspo_fedtwin_page,strong,Total 125 research profiles via 5 batches of 25 selected 2019-2024",
    "bud_fedtwin_profile_10y_class,fedtwin_belspo,2024,1000000,,,budgeted,src_rmah_research_strategy_2023,medium,Illustrative TCO per profile 5*125k+5*75k=1.0m if full 10y path; not outturn",
    "bud_fedtwin_programme_10y_class,fedtwin_belspo,2024,125000000,,,budgeted,src_rmah_research_strategy_2023,medium,Illustrative if 125 profiles full 10y path ~125m; batches staggered not concurrent; FOI cash path",
    "bud_fedtwin_climate_13_2020_26,fedtwin_belspo,2026,9250000,,,budgeted,src_climat_be_belspo_climate_funds,strong,Climate-related FedTwin postdocs 13 projects total 9.25m 2020-2026 (climat.be inventory)",
    "bud_digit04_total_2019_24,digit04_belspo,2024,37630000,,,budgeted,src_rmah_research_strategy_2023,strong,DIGIT-04 programme 2019-2024 envelope 37.63m for 10 FSI + Cinematek",
    "bud_digit04_rmah_annual_class,digit04_belspo,2024,380000,,,budgeted,src_rmah_research_strategy_2023,medium,RMAH share ca 380k annually within DIGIT-04",
    "bud_belspo_climate_total_2019_27,belspo,2027,39200000,,,budgeted,src_climat_be_belspo_climate_funds,strong,BELSPO climate-related projects total 39.2m between 2019-2027 (inventory sum)",
    "bud_belspo_climate_2022_26,belspo,2026,32900000,,,budgeted,src_climat_be_belspo_climate_funds,strong,BELSPO climate-related 32.9m between 2022-2026",
    "bud_belspo_polar_call_2022_25,belspo,2025,1667100,,,budgeted,src_climat_be_belspo_climate_funds,strong,Polar call 5 climate projects total 1.6671m 2022-2025",
    "bud_belspo_belgica_call_2022_25,belspo,2025,1997100,,,budgeted,src_climat_be_belspo_climate_funds,strong,BELGICA call 2 climate projects total 1.9971m 2022-2025",
    "bud_belspo_brain_p1_climate_2019_26,belspo,2026,11681000,,,budgeted,src_climat_be_belspo_climate_funds,strong,BRAIN-be2.0 Pillar1 climate 16 projects total 11.681m 2019-2026",
    "bud_belspo_stereo_climate_2023_29,belspo,2029,7000000,,,budgeted,src_climat_be_belspo_climate_funds,strong,STEREO EO climate 10 projects total 7.0m 2023-2029",
    "bud_belspo_esa_climate_space_dte_2023_27,belspo,2027,9000000,,,budgeted,src_climat_be_belspo_climate_funds,strong,ESA Climate Space 6.5m + Digital Twin Earth 2.5m = 9.0m 2023-2027",
]
with open(root / "budgets.csv", "a", encoding="utf-8") as f:
    f.write("\n".join(bud) + "\n")

# --- commitments ---
def cmt_row(cid, title, eid, ben, legal, ddate, sy, ey, tot, cash, rem, url, goal, cut, src, conf, path, notes):
    cash_field = json.dumps(cash, separators=(",", ":")).replace('"', '""')
    rem_s = "" if rem is None else str(rem)
    return (
        f'{cid},{title},{eid},{ben},{legal},{ddate},{sy},{ey},{tot},'
        f'"{cash_field}",{rem_s},active,{url},{goal},{cut},{src},{conf},{path},{notes}\n'
    )

with open(root / "commitments.csv", "a", encoding="utf-8") as f:
    f.write(
        cmt_row(
            "cmt_fedtwin_profiles_2019_29",
            "FED-tWIN dual FSI-university research profiles multi-year",
            "fedtwin_belspo",
            "Postdocs FSI and 11 Belgian universities NL/FR",
            "Law 21 Jul 2017 + RD 14 Oct 2018 / 14 Feb 2022",
            "2017-07-21",
            2019,
            2029,
            125000000,
            {
                "profiles": 125,
                "batches": 5,
                "per_batch": 25,
                "rate_yr1_5_eur": 125000,
                "rate_yr6_10_eur": 75000,
                "profile_10y_class_eur": 1000000,
                "programme_10y_class_eur": 125000000,
                "funding_first5_pct": 1.0,
                "funding_next5_pct": 0.5,
                "climate_subset_13_m": 9.25,
                "note": "Programme TCO 125m is illustrative full-path class; cash outturn staggered FOI; dual linguistic unis",
            },
            None,
            "https://www.belspo.be/belspo/research/FEDtWIN_en.stm",
            "Sustainable joint research FSI and universities scientific excellence",
            "Publish cash-by-year and named profiles; dual unit-cost vs community PhD schemes",
            "src_belspo_fedtwin_page",
            "medium",
            "Federal>BELSPO>FED-tWIN",
            "tick335: 125 profiles 125k/75k rates dual FSI-uni; climate 9.25m strong subset",
        )
    )
    f.write(
        cmt_row(
            "cmt_digit04_2019_24",
            "DIGIT-04 federal FSI+Cinematek digitisation 2019-2024",
            "digit04_belspo",
            "10 FSI + Royal Belgian Film Archives Cinematek",
            "BELSPO Digitization Programme DIGIT-04",
            "2019-01-01",
            2019,
            2024,
            37630000,
            {
                "total_m": 37.63,
                "rmah_annual_class_k": 380,
                "institutions": "10 FSI + Cinematek",
                "priorities": "digitization long-term preservation access reuse",
                "note": "RMAH strategy primary extract; dual community heritage digitisation programmes",
            },
            0,
            "https://www.artandhistory.museum/sites/default/files/2023-12/Research-strategy-RMAH-Digital-corr.pdf",
            "Digitize preserve and open federal heritage collections",
            "Publish L5 cash by FSI and successor DIGIT path post-2024",
            "src_rmah_research_strategy_2023",
            "strong",
            "Federal>BELSPO>DIGIT-04",
            "tick335: 37.63m 2019-24 dual heritage digitisation",
        )
    )
    f.write(
        cmt_row(
            "cmt_belspo_climate_portfolio_2019_27",
            "BELSPO climate-related project portfolio 2019-2027",
            "belspo",
            "FSI universities polar marine climate researchers",
            "BRAIN-be2.0 STEREO Polar BELGICA FedTwin ESA Climate inventories",
            "2019-01-01",
            2019,
            2027,
            39200000,
            {
                "total_2019_27_m": 39.2,
                "total_2022_26_m": 32.9,
                "brain_p1_climate_m": 11.681,
                "fedtwin_climate_m": 9.25,
                "stereo_m": 7.0,
                "esa_climate_dte_m": 9.0,
                "polar_call_m": 1.667,
                "belgica_call_m": 1.997,
                "note": "climat.be inventory primary; subset of Belspo RDI not full Belspo budget",
            },
            None,
            "https://climat.be/doc/belspo-climate-related-projects-and-funds-2021-2026-docx.pdf",
            "Federal climate research knowledge for policy and FSI capacity",
            "Track project outturns vs awards; dual regional climate research",
            "src_climat_be_belspo_climate_funds",
            "strong",
            "Federal>BELSPO>climate_RDI",
            "tick335: 39.2m climate portfolio dual polar marine space",
        )
    )

# --- leaderboard ---
with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_fedtwin_125_profiles,FED-tWIN 125 dual FSI-university profiles class ~125m 10y,federal,ops,"
        "Federal>BELSPO>FED-tWIN,9250000,125000000,"
        "Strong structure 125 profiles BELSPO; rates 125k/75k RMAH; climate subset 9.25m strong; full TCO medium class,"
        "medium,src_belspo_fedtwin_page,Postdocs FSI universities,"
        "Sustainable FSI-university research bridge,"
        "Core capacity not pure waste; dual linguistic unis vs single federal research; cash path FOI,"
        "3,7.0,5,5.5,FOI cash-by-year + named profiles matrix; dual unit-cost,seed,,tick335 dual research\n"
    )
    f.write(
        "lb_digit04_37_6m,DIGIT-04 federal digitisation 37.63m 2019-24 dual heritage,federal,ops,"
        "Federal>BELSPO>DIGIT-04,6260000,37630000,"
        "Strong RMAH strategy: 37.63m envelope 10 FSI+Cinematek 2019-24; ~6.27m/yr class; dual community heritage,"
        "strong,src_rmah_research_strategy_2023,Museums libraries archives film,"
        "Digitize federal heritage for access and preservation,"
        "Core heritage not pure waste; L5 by FSI residual; successor path unknown,"
        "2,6.5,4,4.6,Publish L5 cash by FSI and post-2024 DIGIT path,seed,,tick335 dual heritage\n"
    )
    f.write(
        "lb_belspo_climate_39m,BELSPO climate project portfolio 39.2m 2019-27,federal,ops,"
        "Federal>BELSPO>climate_RDI,32900000,39200000,"
        "Strong climat.be: 39.2m 2019-27 / 32.9m 2022-26; FedTwin 9.25 polar 1.67 BELGICA 2.0 BRAIN 11.7 ESA 9,"
        "strong,src_climat_be_belspo_climate_funds,Climate researchers polar marine,"
        "Federal climate knowledge and FSI capacity,"
        "Core research not pure waste; dual regional programmes; project L5 partial public,"
        "2,7.0,4,4.9,Track awards vs outturn; polar ops FOI residual,seed,,tick335 climate dual\n"
    )

# --- FOI gap new ---
gap_id = "gap_fedtwin_cash_profiles_l5"
draft_path = f"docs/doge/foi/drafts/{gap_id}.md"
with open(root / "foi_queue.csv", "a", encoding="utf-8") as f:
    f.write(
        f"{gap_id},Federal>BELSPO>FED-tWIN>cash_and_profiles_L5,fedtwin_belspo,"
        "Cash-by-year FED-tWIN programme 2019-2026 total and by batch; named list 125 profiles with FSI university EUR start date; "
        "reconcile RMAH 125k/75k rates with Belspo budget codes; climate 13-project subset names if separate,"
        "Structure and rates public; full cash path and end-receiver L5 opaque; dual linguistic distribution check,5,"
        "BELSPO / POD Wetenschapsbeleid / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        f"{draft_path},ready,2026-07-31,,,,,"
        "cmt_fedtwin_profiles_2019_29,lb_fedtwin_125_profiles,"
        f"{now},{now},tick335 draft ready human send; dual FSI-university\n"
    )
    # also digit residual optional lower prio - combine note into same or separate
    f.write(
        "gap_digit04_fsi_l5,Federal>BELSPO>DIGIT-04>FSI_L5,digit04_belspo,"
        "Cash-by-year DIGIT-04 2019-2024 by each of 10 FSI + Cinematek; successor DIGIT path 2025+ envelopes; "
        "objects digitized and access KPIs if held,"
        "Programme total 37.63m strong; L5 by institution residual,4,"
        "BELSPO / POD Wetenschapsbeleid / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_digit04_fsi_l5.md,ready,2026-07-31,,,,,"
        "cmt_digit04_2019_24,lb_digit04_37_6m,"
        f"{now},{now},tick335 draft ready human send\n"
    )

# FOI drafts
draft_dir = root.parent / "foi" / "drafts"
draft_dir.mkdir(parents=True, exist_ok=True)
(draft_dir / f"{gap_id}.md").write_text(
    f"""# FOI draft — {gap_id}

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO)
t.a.v. de dienst openbaarheid van bestuur
WTC III Simon Bolivarlaan 30 bus 7
1000 Brussel
via IBZ openbaarheid: https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — FED-tWIN kasstromen en L5-profielen

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van de hieronder omschreven
bestuursdocumenten.

### 1. Voorwerp van het verzoek

1. Meerjarige kasuitgaven (cash-by-year) 2019-2026 van het programma **FED-tWIN**,
   met begrotingsartikelcodes waar beschikbaar.
2. Lijst van de **125 onderzoeksprofielen** (batches 2019-2024) met: naam/thema,
   FWI, universiteit, startdatum, toegekend jaarbudget, status (actief/afgerond).
3. Bevestiging van de tarieven **€125.000/jaar** (eerste 5 jaar) en **€75.000/jaar**
   (volgende 5 jaar) per profiel, of de actuele geldende schalen.
4. Aggregaat per taalrol/universiteit en per FWI over de volledige looptijd.
5. Eventuele evaluatie- of voortgangsrapporten over het programma.

Periode: 2019-01-01 tot heden (en lopende verbintenissen).

### 2. Context

Onderzoek naar federale wetenschapsuitgaven en duale structuren FWI/universiteiten.
Hiërarchisch pad (intern): Federal > BELSPO > FED-tWIN > cash_and_profiles_L5.

Publiek bekend: 125 profielen in 5 batches van 25; 100% financiering 5 jaar daarna 50%;
klimaat-subset 13 projecten €9,25 m (2020-2026) via climat.be.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail.
Indien weigering: gemotiveerde beslissing met rechtsgrond en beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: burger / onderzoek AIpolitics DOGE
Dossierreferentie intern: {gap_id}

Met vriendelijke groet,

[Naam]
```

## Checklist

- [x] Juiste instelling (BELSPO / IBZ)
- [x] Concrete documenten (cash path + named profiles)
- [x] Periode en bedragen gevraagd
- [x] Meerjarigheid expliciet
- [ ] Contactgegevens verzoeker (human)
- [x] foi_queue ready

## Notes tick335

Strong public structure BELSPO; rates RMAH strategy; climate subset climat.be.
Residual: programme cash outturn and full L5 names.
""",
    encoding="utf-8",
)

(draft_dir / "gap_digit04_fsi_l5.md").write_text(
    """# FOI draft — gap_digit04_fsi_l5

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO)
t.a.v. de dienst openbaarheid van bestuur
WTC III Simon Bolivarlaan 30 bus 7
1000 Brussel
via IBZ openbaarheid: https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — DIGIT-04 kasstromen per FWI/Cinematek

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking.

### 1. Voorwerp

1. Cash-by-year 2019-2024 van programma **DIGIT-04** per van de 10 FWI en
   Koninklijk Belgisch Filmarchief (Cinematek), met begrotingscodes.
2. Eventueel opvolgingsprogramma DIGIT/digitalisering 2025+ met enveloppe.
3. KPI's of tussentijdse rapporten: aantal gedigitaliseerde objecten / toegang.

Periode: 2019-01-01 tot heden.

### 2. Context

Federal > BELSPO > DIGIT-04 > FSI_L5.
Publiek: totale enveloppe **€37,63 m** (2019-2024) voor 10 FWI + Cinematek
(RMAH research strategy).

### 3. Vorm

Digitale kopie (PDF/CSV) bij voorkeur.

### 4. Identiteit

Dossierreferentie intern: gap_digit04_fsi_l5

Met vriendelijke groet,
[Naam]
```

## Checklist

- [x] Instelling BELSPO
- [x] Concrete L5 per FWI
- [x] foi_queue ready
- [ ] Human contact fill + send
""",
    encoding="utf-8",
)

# --- research_queue: seed rq_326 done + rq_327 ---
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
if "rq_326" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_326,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_fedtwin_cash_profiles_l5,"
        f"2026-07-31T05:45:00Z,{now},"
        "tick335: FED-tWIN 125 profiles 125k/75k + DIGIT-04 37.63m dual; climate 39.2m; FOI L5; spawn rq_327\n"
    )
else:
    rq = re.sub(
        r"rq_326,[^\n]+",
        "rq_326,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_fedtwin_cash_profiles_l5,"
        f"2026-07-31T05:45:00Z,{now},"
        "tick335: FED-tWIN 125 profiles 125k/75k + DIGIT-04 37.63m dual; climate 39.2m; FOI L5; spawn rq_327",
        rq,
        count=1,
    )
if "rq_327" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_327,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        f"{now},,Spawned tick335 after FED-tWIN DIGIT climate; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")

# --- loop_state ---
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_326,335,no,"
    "Scheduler 60s. Next prio5 rq_327; rq_116 SWA deferred. FOI ready. tick335 FED-tWIN DIGIT climate.\n",
    encoding="utf-8",
)

# belspo entity note
ent = (root / "entities.csv").read_text(encoding="utf-8")
ent2 = re.sub(
    r"belspo,POD Wetenschapsbeleid BELSPO,[^\n]+",
    "belspo,POD Wetenschapsbeleid BELSPO,SPP Politique scientifique BELSPO,"
    "Federal Science Policy Office,agency,sec_federal,bi,https://www.belspo.be,,,"
    "Budget 2024 582.4m; FED-tWIN 125 profiles; DIGIT-04 37.63m; climate RDI 39.2m; dual; tick329-335",
    ent,
    count=1,
)
(root / "entities.csv").write_text(ent2, encoding="utf-8")

print("OK tick335")

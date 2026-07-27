# -*- coding: utf-8 -*-
"""Tick 154 — rq_149 Housing regional subsidies VL + WAL named envelopes."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 154
UNIT = "rq_149"
UTC = "2026-07-28T00:50:00Z"
GAP = "gap_housing_l5_slsp_wm"


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


def append_if_missing(p: Path, rows: list[str], key_prefix: str | None = None) -> None:
    text = read_text(p)
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        key = row.split(",", 1)[0] if key_prefix is None else key_prefix
        if key_prefix is None:
            if row.split(",", 1)[0] in text:
                continue
        else:
            if key in text and row.split(",", 1)[0] in text:
                continue
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
    'src_vl_bbt_wonen_bo2026,BBT Wonen BO2026 Vlaams Parlement 13-G (2025-2026) Nr.1,https://docs.vlaamsparlement.be/pfile?id=2226288,Vlaams Parlement / minister Wonen,2026-07-28,official_budget,"Programme QD WONEN VAK 3290.673m VEK 348.020m; demand ISE huursub+premie 140.968m; VWF loan auth 1.72bn; VMSW FS3 1bn + QDB5QK 1228.9m; tick154"',
    'src_wal_do16_budget2026,Wallonie Budget general depenses 2026 DO16 Amenagement logement patrimoine energie,https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do16.pdf,SPW Finances / Gouvernement wallon,2026-07-28,official_budget,"Prog 16.081 SWL PEI 55.282m Impulsion 5m PRW 31.146m PIVERT 22.419m; SWCS 23.3m; Renopack 88.632m primes; tick154"',
    'src_eib_flanders_housing_2026,EIB Flanders social housing 1.7bn financing agreement first tranche 700m,https://www.eib.org/en/press/all/2026-019-eib-and-belgian-region-of-flanders-agree-landmark-eur1-7-billion-financing-agreement-to-boost-social-housing,EIB,2026-07-28,official_press,"Largest EIB BE op; preferential loans; Bonte cites 2pct interest subsidy for housing associations; financing not pure grant; tick154"',
]
append_if_missing(DATA / "sources.csv", srcs)

# --- entities ---
ents = [
    "vmsw,Vlaamse Maatschappij voor Sociaal Wonen (VMSW),Societe flamande de logement social,Flemish Social Housing Company,agency,vlaanderen_gov,nl,https://www.vlaanderen.be,,Brussels/Flanders,Financial intermediary inside Wonen in Vlaanderen; FS3 loan auth 1bn 2026; SSI GSC budgethuren channels; tick154",
    "vwf,Vlaams Woningfonds,Fonds flamand du logement,Flemish Housing Fund,agency,vlaanderen_gov,nl,https://www.vlaamswoningfonds.be,,Flanders,BSL/Woonlening auth 1.7bn + HWL 20m 2026; werkings toelage 41.763m; tick154",
    "swl,Societe wallonne du Logement (SWL),Societe wallonne du Logement,Walloon Housing Company,agency,wallonie_gov,fr,https://www.swl.be,,Charleroi/Wallonia,UAP financing SLSP; DO16 2026 PEI+Impulsion+PRW+PIVERT ~114m eng; Agence Habitation reform pending; tick154",
    "swcs,Societe wallonne du Credit social (SWCS),Societe wallonne du Credit social,Walloon Social Credit Company,agency,wallonie_gov,fr,https://www.swcs.be,,Wallonia,Social loans + Renopack channel; DO16 23.3m social loans + Renopack ops/primes; tick154",
]
append_if_missing(DATA / "entities.csv", ents)

# --- budgets (EUR) ---
bud = [
    # VL programme totals
    "bud_vl_wonen_qd_vak_2026,vlaanderen_gov,2026,3290673000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Programme QD WONEN BO2026 VAK 3290673 kEUR BBT p7",
    "bud_vl_wonen_qd_vek_2026,vlaanderen_gov,2026,348020000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Programme QD WONEN BO2026 VEK 348020 kEUR (cash-like); BA2025 VEK was 377775k",
    "bud_vl_wonen_qd_vak_2025,vlaanderen_gov,2025,3321435000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,BA2025 VAK 3321435 kEUR",
    "bud_vl_wonen_qd_vek_2025,vlaanderen_gov,2025,377775000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,BA2025 VEK 377775 kEUR",
    # VL demand-side
    "bud_vl_huurtoelage_2026,vlaanderen_gov,2026,140968000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Joint huursubsidie+huurpremie 140968 kEUR BO2026 demand ISE; article QF0-1QDB2PA-WT",
    "bud_vl_qdb2pa_2026,vlaanderen_gov,2026,152085000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,QF0-1QDB2PA-WT full 152085 kEUR incl huurtoelagen + VGW 8357k + mediation",
    "bud_vl_vgw_2026,vlaanderen_gov,2026,8357000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Verzekering Gewaarborgd Wonen premiums 8357 kEUR after -850k tax cut",
    "bud_vl_vwf_werking_2026,vwf,2026,41763000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,VWF werkings/financieringstoelage QF0-1QDB2PJ-IS 41763 kEUR",
    "bud_vl_vwf_lening_auth_2026,vwf,2026,1720000000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,QF0-1QDB5PJ-IS loan authorization 1720m = 1.7bn Woonlening + 20m huurwaarborg; not cash grant",
    "bud_vl_fbuh_2026,vlaanderen_gov,2026,1741000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Fonds bestrijding uithuiszettingen toelage 1741 kEUR",
    # VL supply / VMSW
    "bud_vl_vmsw_is_vak_2026,vmsw,2026,68056000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,QF0-1QDB2QK-IS VMSW IS VAK 68056 kEUR (SSI GSC budgethuren etc)",
    "bud_vl_vmsw_is_vek_2026,vmsw,2026,71812000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,QF0-1QDB2QK-IS VMSW IS VEK 71812 kEUR",
    "bud_vl_vmsw_loan_auth_2026,vmsw,2026,1228907000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,QF0-1QDB5QK-IS VMSW loan authorizations VAK 1228907 kEUR; FS3 max 1bn + market 220m + student 100m class",
    "bud_vl_vmsw_fs3_auth_2026,vmsw,2026,1000000000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,FS3 programme loan auth max 1bn EUR 2026 (+ unused 2025); -1pct path shifting to -2pct financing reform",
    "bud_vl_gsc_2026,vmsw,2026,13500000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Gewestelijke Sociale Correctie GSC 13500 kEUR constant in VMSW table",
    "bud_vl_budgethuren_cap_2026,vmsw,2026,12800000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Budgethuren/SVKpro annual intervention cap 12.8m at cruise; VMSW table also notes 6m 2026 line",
    "bud_vl_ssi_assign_2026,vmsw,2026,54599000,,,budgeted,src_vl_bbt_wonen_bo2026,medium,SSI infrastructure assignment volume 54599 kEUR class (BO26 40301 + rider 15301 + shifts)",
    "bud_vl_mvp_cut_2026,vlaanderen_gov,2026,-70549000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Mijn VerbouwPremie new credits zero from 2026; saving 70549 kEUR vs BA2025 quality ISE",
    "bud_vl_expertisepool_2026,vlaanderen_gov,2026,500000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,Expertisepool woonmaatschappijen 500 kEUR QF0-1QDB2QA-WT",
    "bud_vl_igs_2026,vlaanderen_gov,2026,9300000,,,budgeted,src_vl_bbt_wonen_bo2026,strong,IGS local housing cooperation subsidy ~9.3m VAK on QDB2TA",
    "bud_eib_fl_housing_facility,vlaanderen_gov,2026,1700000000,,,commitment,src_eib_flanders_housing_2026,strong,EIB facility total 1.7bn multi-year; first tranche 700m signed Jan 2026; preferential loans not cash grant",
    # WAL SWL / SWCS / Renopack
    "bud_wal_swl_pei_2026,swl,2026,55282000,,,budgeted,src_wal_do16_budget2026,strong,DO16 081.016 PEI engagement=liquidation 55282 kEUR",
    "bud_wal_swl_impulsion_2026,swl,2026,5000000,,,budgeted,src_wal_do16_budget2026,strong,DO16 081.020 Plan Impulsion Logement 5000 kEUR",
    "bud_wal_swl_prw_eng_2026,swl,2026,31146000,,,budgeted,src_wal_do16_budget2026,strong,DO16 081.038 PRW renovation plan eng 31146 kEUR liq 25529k",
    "bud_wal_swl_prw_liq_2026,swl,2026,25529000,,,budgeted,src_wal_do16_budget2026,strong,DO16 081.038 PRW liquidation 25529 kEUR",
    "bud_wal_swl_pivert_2026,swl,2026,22419000,,,budgeted,src_wal_do16_budget2026,strong,DO16 081.059 PIVERT 22419 kEUR eng=liq",
    "bud_wal_swl_ancrage_liq_2026,swl,2026,9784000,,,budgeted,src_wal_do16_budget2026,strong,DO16 081.021 Ancrage communal eng 0 liq 9784 kEUR",
    "bud_wal_swl_named_eng_sum_2026,swl,2026,113847000,,,budgeted,src_wal_do16_budget2026,strong,Sum named SWL capital dots eng PEI+Impulsion+PRW+PIVERT 113847 kEUR (excl ancrage eng0)",
    "bud_wal_swl_named_liq_sum_2026,swl,2026,118014000,,,budgeted,src_wal_do16_budget2026,strong,Sum named SWL liq PEI+Impulsion+Ancrage+PRW+PIVERT 118014 kEUR",
    "bud_wal_prog_16081_2026,wallonie_gov,2026,116179000,,,budgeted,src_wal_do16_budget2026,strong,Programme 16.081 investment plans eng 116179 / liq 120346 kEUR",
    "bud_wal_swcs_prets_2026,swcs,2026,23300000,,,budgeted,src_wal_do16_budget2026,strong,DO16 080.036 SWCS social loans dotation 23300 kEUR",
    "bud_wal_swcs_deficit_2026,swcs,2026,6048000,,,budgeted,src_wal_do16_budget2026,strong,DO16 080.062 SWCS special cash deficit capital 6048 kEUR",
    "bud_wal_flw_2026,wallonie_gov,2026,4332000,,,budgeted,src_wal_do16_budget2026,strong,DO16 080.037 Fonds du Logement renove/gestion eng 4332 liq 5632 kEUR",
    "bud_wal_renopack_primes_2026,swcs,2026,88632000,,,budgeted,src_wal_do16_budget2026,strong,DO16 084.014 Renopack primes SWCS/FLW 88632 kEUR",
    "bud_wal_renopack_ops_2026,swcs,2026,11712000,,,budgeted,src_wal_do16_budget2026,strong,DO16 084.013 Renopack functioning SWCS/FLW 11712 kEUR",
    "bud_wal_prog_16080_2026,wallonie_gov,2026,331634000,,,budgeted,src_wal_do16_budget2026,strong,Programme 16.080 Logement eng 331634 / liq 330319 kEUR broader housing",
]
append_if_missing(DATA / "budgets.csv", bud)

# --- commitments ---
cmts = [
    (
        'cmt_vl_wonen_qd_2026,Flanders programme QD Wonen BO2026 envelope,vlaanderen_gov,Wonen in Vlaanderen / VMSW / VWF,'
        'BBT Wonen BO2026 + Vlaamse Codex Wonen,2025-10-24,2026,2026,3290673000,'
        '"{""2026_vak"":3290673000,""2026_vek"":348020000,""2025_vak"":3321435000,""2025_vek"":377775000,'
        '""huurtoelage"":140968000,""vwf_loan_auth"":1720000000,""vmsw_loan_auth"":1228907000,""vmsw_fs3"":1000000000,'
        '""vmsw_is_vek"":71812000,""vgw"":8357000,""mvp_cut"":-70549000,""social_stock_2024"":177461}",0,active,'
        'https://docs.vlaamsparlement.be/pfile?id=2226288,Social + private housing affordability quality access,'
        'Publish L5 per woonmaatschappij; track FS3 vs outcomes BSO 45-56k units,'
        'src_vl_bbt_wonen_bo2026,strong,Vlaanderen>Wonen>QD,'
        'tick154; VAK dominated by loan authorizations not pure grants; VEK ~348m is cash-like programme total'
    ),
    (
        'cmt_wal_swl_invest_plans_2026,Wallonia SWL named investment-plan dots 2026,swl,SWL / SLSP network,'
        'Budget general depenses Wallonie 2026 DO16 prog 16.081,2025-10-20,2026,2026,118014000,'
        '"{""2026_pei"":55282000,""2026_impulsion"":5000000,""2026_prw_eng"":31146000,""2026_prw_liq"":25529000,'
        '""2026_pivert"":22419000,""2026_ancrage_liq"":9784000,""2026_named_eng_sum"":113847000,""2026_named_liq_sum"":118014000,'
        '""prog_16081_eng"":116179000,""prog_16081_liq"":120346000}",0,active,'
        'https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do16.pdf,Public social housing investment/renovation SLSP,'
        'Open per-SLSP cash table; audit SWL+SWCS+FLW for Agence Habitation reform,'
        'src_wal_do16_budget2026,strong,Wallonie>Logement>SWL>plans,'
        'tick154; residual L5 SLSP FOI; dual SWL/SWCS/FLW stack pending merger'
    ),
    (
        'cmt_wal_renopack_2026,Wallonia Renopack primes + ops via SWCS/FLW 2026,swcs,SWCS/FLW households,'
        'Budget Wallonie 2026 DO16 prog 16.084,2025-10-20,2026,2026,100344000,'
        '"{""2026_primes"":88632000,""2026_ops"":11712000,""2026_avances"":19413000,""prog_total_eng"":119757000}",0,active,'
        'https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do16.pdf,Private renovation energy social loans channel,'
        'Publish beneficiary volumes and deadweight; reform conditions Oct 2026,'
        'src_wal_do16_budget2026,strong,Wallonie>Logement>Renopack,'
        'tick154; primes 88.6m + ops 11.7m; avances separate repayable'
    ),
    (
        'cmt_eib_fl_social_housing_17bn,EIB Flanders social housing facility 1.7bn,vlaanderen_gov,Woonmaatschappijen / Flanders,'
        'EIB board approval + first tranche signature,2026-01-22,2026,2035,1700000000,'
        '"{""facility_total"":1700000000,""first_tranche"":700000000,""note"":""preferential loans; interest subsidy path 2pct claimed by minister press; not pure grant cash""}",1700000000,active,'
        'https://www.eib.org/en/press/all/2026-019-eib-and-belgian-region-of-flanders-agree-landmark-eur1-7-billion-financing-agreement-to-boost-social-housing,'
        'Social housing newbuild/renovation energy bills,Track annual draw and budgeted interest-subsidy cost vs FS3,'
        'src_eib_flanders_housing_2026,strong,Vlaanderen>Wonen>EIB_facility,'
        'tick154; financing instrument; residual interest-subsidy cash FOI'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

# --- leaderboard ---
lbs = [
    "lb_vl_wonen_programme,Flanders QD Wonen VEK ~348m 2026 (VAK 3.29bn),regional,programme,Vlaanderen>Wonen>QD,348020000,3290673000,BBT strong: VEK 348m cash-like; VAK 3.29bn mostly loan auths VWF 1.72bn + VMSW 1.23bn; huurtoelage 141m; MVP cut -70.5m,strong,src_vl_bbt_wonen_bo2026,Social tenants private low-income buyers,Affordable quality housing BSO growth,Loan auth inflation can mask cash cost; dual VMSW+VWF stack,4,7.5,4,5.8,Publish cash TCO of interest subsidies; L5 per WM; BSO unit cost,seed,,tick154",
    "lb_vl_huurtoelage,Flanders joint rent subsidy+premium ~141m 2026,regional,subsidy,Vlaanderen>Wonen>huurtoelage,140968000,140968000,BBT: joint huursubsidie+huurpremie 140.968m on QDB2PA; merge to single scheme planned; non-take-up noted,strong,src_vl_bbt_wonen_bo2026,Private tenants waiting list / low income,Affordable private rent,Core safety-net not pure waste; admin dual schemes until merge,3,6.0,3,4.5,Complete merge; track take-up KPIs; open monthly caseload,seed,,tick154",
    "lb_wal_swl_plans,Wallonia SWL named investment dots ~118m liq 2026,regional,programme,Wallonie>SWL>plans,118014000,118014000,DO16 strong PEI 55.3 + PRW 25.5 liq + PIVERT 22.4 + Impulsion 5 + Ancrage 9.8 liq; SLSP L5 opaque,strong,src_wal_do16_budget2026,Social housing tenants SLSP,Public housing invest renovate,Core mandate; multi-UAP SWL/SWCS/FLW overhead pending Agence Habitation,4,6.5,4,5.3,FOI per-SLSP top20; complete external audit; merger cost-neutral,seed,,tick154",
    "lb_wal_renopack,Wallonia Renopack primes ~88.6m 2026,regional,subsidy,Wallonie>Renopack>primes,88632000,100344000,DO16 primes 88.632m + ops 11.712m via SWCS/FLW; reform conditions 2026,strong,src_wal_do16_budget2026,Households renovating,Energy renovation social credit,Deadweight risk on energy renos; dual channel with VL MVP cut contrast,4,6.0,4,5.0,Publish L5 measure mix and additionality; align SWCS/FLW,seed,,tick154",
]
append_if_missing(DATA / "leaderboard.csv", lbs)

# --- FOI ---
foi_row = (
    f"{GAP},BE>Housing>VL_WM_WAL_SLSP>L5_cash,gg_belgium,"
    "Per-woonmaatschappij Flanders cash from VMSW/GSC/SSI/budgethuren 2023-2026; per-SLSP Wallonia cash from SWL PEI/PRW/PIVERT/Impulsion; EIB facility interest-subsidy budgeted cost series,"
    "Programme envelopes now public; end-receiver L5 still opaque for both regions,"
    "6,Wonen in Vlaanderen / VMSW + SWL / SPW Logement + openbaarheid,"
    "openbaarheid@vlaanderen.be,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-07-28,,,,,"
    "cmt_vl_wonen_qd_2026|cmt_wal_swl_invest_plans_2026,lb_vl_wonen_programme|lb_wal_swl_plans,"
    f"{UTC},{UTC},tick154 partial programme fill; residual L5 human send"
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
**Linked:** {UNIT} · cmt_vl_wonen_qd_2026 · cmt_wal_swl_invest_plans_2026

---

## Brief (NL — Vlaanderen)

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Agentschap Wonen in Vlaanderen / VMSW
     Team Openbaarheid Vlaanderen
     openbaarheid@vlaanderen.be
     Havenlaan 88 bus 20, 1000 Brussel

Betreft: Verzoek om openbaarmaking — L5 cash per woonmaatschappij en interestsubsidie EIB/FS3 2023-2026

Geachte,

Op grond van het Bestuursdecreet (openbaarheid van bestuur)
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Machine-readable lijst (CSV) van alle bedragen 2023-2026 per woonmaatschappij voor:
   - GSC (Gewestelijke Sociale Correctie);
   - SSI-infrastructuursubsidies;
   - budgethuren / geconventioneerde verhuur;
   - overige VMSW-doorgestorte subsidies ≥50.000 EUR/jaar.
2. Jaarlijkse begrote en gerealiseerde kost van interesttussenkomsten
   (FS3 -1%/-2% path en eventuele EIB-preferentiele leningen / 2%-claim)
   2023-2026, met BBT-artikelcodes.
3. Top 20 grootste projecttoewijzingen FS3 2024-2026 (naam initiatiefnemer, gemeente, EUR).

Periode: 2023-01-01 tot meest recente stand.

### 2. Context

BBT Wonen BO2026 publiceert programmatotalen (QD VAK 3,29 mrd / VEK 348 m;
huurtoelage 141 m; VMSW-machtiging 1,23 mrd). Ontbrekend: L5 per woonmaatschappij
en cash-TCO van rentesubsidies.

Hierarchie intern: Vlaanderen > Wonen > QD / VMSW > L5.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {GAP}

Met vriendelijke groet,
[Naam]
```

---

## Brief (FR — Wallonie)

```text
[Nom]
[Adresse]
[E-mail]
[Date]

A: Societe wallonne du Logement (SWL)
   et/ou SPW Logement — publicite de l'administration

Objet: Demande de publicite — flux L5 par SLSP (plans PEI/PRW/PIVERT/Impulsion) 2023-2026

Madame, Monsieur,

Sur la base du decret wallon relatif a la publicite de l'administration,
je sollicite la communication des documents suivants:

1. Liste machine-readable (CSV) des montants verses 2023-2026 par SLSP au titre des
   lignes budgetaires 081.016 (PEI), 081.020 (Impulsion), 081.021 (Ancrage),
   081.038 (PRW), 081.059 (PIVERT), avec engagement et liquidation.
2. Top 20 des plus gros beneficiaires SLSP par annee.
3. Etat d'avancement de l'audit externe SWL/SWCS/FLW et calendrier Agence de l'Habitation
   si document administratifs disponibles.

Periode: 2023-01-01 a la date la plus recente.

Reference interne: {GAP}

Cordialement,
[Nom]
```

---

## Checklist

- [x] Instellingen (VL + WAL)
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
"""
(FOI / f"{GAP}.md").write_text(draft, encoding="utf-8")

# --- research_queue ---
rq_new = (
    f"rq_149,Housing regional subsidies top named programmes,continuous,5,done,L5,gg_belgium,"
    f'"VL social housing + WAL SWL named envelopes.",{GAP},2026-07-27T14:00:00Z,{UTC},'
    "tick154: VL BBT QD VAK 3.29bn VEK 348m huurtoelage 141m VWF 1.72bn VMSW FS3 1bn; "
    "WAL SWL named ~118m liq + Renopack 88.6m; residual L5 FOI ready"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_149,", rq_new):
    raise SystemExit("rq_149 not found")

# --- loop_state ---
state = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio5 Brussels communes DGD defence; FOI ready human send. rq_149 housing VL+WAL envelopes done."\n'
)
write_text(DATA / "loop_state.csv", state)

# --- loop_log ---
log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Housing regional subsidies — VL social housing + WAL SWL)
- Found (strong primary BBT Wonen BO2026 + WAL DO16):
  - **VL programme QD WONEN BO2026:** VAK **EUR 3.291bn** · VEK **EUR 348.0m** (BA2025 VEK 377.8m).
  - **Huurtoelage joint** (huursubsidie+huurpremie): **EUR 141.0m**; full QDB2PA **152.1m** (incl VGW **8.36m**).
  - **VWF loan auth:** **EUR 1.72bn** (1.7bn Woonlening + 20m HWL); werkings **41.8m**.
  - **VMSW:** loan auth **EUR 1.229bn** (FS3 max **1.0bn** + market 220m + student 100m class); IS VEK **71.8m**; GSC **13.5m**; budgethuren cap **12.8m**.
  - **MVP cut:** **-EUR 70.5m** new credits from 2026.
  - **Social stock 31/12/2024:** **177.461** units; BSO path 45k+ voluntary to max **56k**.
  - **EIB facility:** **EUR 1.7bn** (first tranche **700m**) preferential loans — not pure grant.
  - **WAL SWL named liq sum ~EUR 118.0m:** PEI **55.3** · PRW liq **25.5** · PIVERT **22.4** · Ancrage **9.8** · Impulsion **5.0**.
  - **WAL Renopack primes EUR 88.6m** + ops **11.7m**; SWCS social loans **23.3m**.
- Wrote: sources 3; entities 4; budgets ~35; cmt 4; lb 4; rq_149=done; FOI residual ready.
- FOI: {GAP} (per-WM / per-SLSP L5 + interest-subsidy cash) human send only.
- Next: prio5 **rq_145 Brussels communes** / **rq_146 DGD** / **rq_147 defence** / **rq_121 hole-fill**.
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)

print("OK tick", TICK, UNIT)
print("VL VEK", 348020000, "huurtoelage", 140968000)
print("WAL SWL named liq", 118014000, "Renopack primes", 88632000)

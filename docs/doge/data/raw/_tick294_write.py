# tick294 write: CREG crisis pack + CCE + INR from Kamer 55K2933/016
from pathlib import Path
import json

SRC = "src_kamer_55k2933_creg_crisis_cce"
PDF = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"


def q(s: str) -> str:
    s = str(s)
    if any(c in s for c in [",", '"', "\n"]):
        return '"' + s.replace('"', '""') + '"'
    return s


def append_if_missing(path: Path, needle: str, lines: list[str]) -> int:
    text = path.read_text(encoding="utf-8")
    added = 0
    with path.open("a", encoding="utf-8", newline="") as f:
        for line in lines:
            key = line.split(",", 1)[0]
            if key in text or needle in line and key in text:
                # also check key specifically
                pass
            if key not in text:
                f.write(line if line.endswith("\n") else line + "\n")
                text += line
                added += 1
    return added


# --- sources ---
src_path = Path("docs/doge/data/sources.csv")
src_line = (
    f"{SRC},Kamer 55K2933/016 FOD Economie prog 21/4 CREG social tariff basisfonds CCE INR,"
    f"{PDF},Belgische Kamer van volksvertegenwoordigers,2026-07-30,official_budget,"
    "BA 21.40.414001 CREG social tariff enlargement 276/733.3/642.4/3.4m 2021-24; "
    "BA 21.40.414003 basisfonds 517.2m 2022 1444.5m 2023 (elec 620.7 gas 823.8 Q1-23); "
    "BA 21.40.414002 CCE ~5.3-5.4m; BA 21.40.414006 INR ~1.3m; tick294\n"
)
print("sources", append_if_missing(src_path, SRC, [src_line]))

# --- entities ---
ent_path = Path("docs/doge/data/entities.csv")
ents = [
    "cce_crb,Centrale Raad voor het Bedrijfsleven CRB,Conseil Central de l Economie CCE,"
    "Central Economic Council,agency,fod_economy,bi,https://www.ccecrb.fgov.be,,,,"
    "Paritary socio-economic advisory; FPS Economy BA 21.40.414002 ~5.4m/yr path; law 20 Sep 1948; tick294\n",
    "icn_inr,Instituut voor de Nationale Rekeningen INR,Institut des comptes nationaux ICN,"
    "Institute for National Accounts,agency,fod_economy,bi,https://www.nbb.be,,,,"
    "Public body under Economy minister law 21 Dec 1994; BA 21.40.414006 ~1.3m/yr; NBB/Statbel/FPB partners; tick294\n",
]
print("entities", append_if_missing(ent_path, "cce_crb", ents))

# --- budgets ---
bud_path = Path("docs/doge/data/budgets.csv")
brows = []
st = {
    2021: 276000000,
    2022: 733340000,
    2023: 642400000,
    2024: 3400000,
    2025: 3400000,
    2026: 3400000,
    2027: 3400000,
}
for y, a in st.items():
    brows.append(
        f"bud_creg_social_tariff_enlarged_{y},creg,{y},{a},,,budgeted,{SRC},strong,"
        "BA 21.40.414001 CREG compensation enlargement social tariff gas+elec eng=liq; "
        "residual 3.4m 2024-27 after end Mar2023 extension\n"
    )
for y, a in {2022: 517204000, 2023: 1444500000}.items():
    brows.append(
        f"bud_creg_basisfonds_heating_{y},creg,{y},{a},,,budgeted,{SRC},strong,"
        "BA 21.40.414003 CREG basisfonds/forfait base heating premium; "
        "2023=elec 620.7m+gas 823.8m Q1 prolongation\n"
    )
brows.append(
    f"bud_creg_basisfonds_elec_q1_2023,creg,2023,620700000,,,budgeted,{SRC},strong,"
    "BA 21.40.414003 text: electricity forfait base prolongation Jan-Mar 2023 620.7m\n"
)
brows.append(
    f"bud_creg_basisfonds_gas_q1_2023,creg,2023,823800000,,,budgeted,{SRC},strong,"
    "BA 21.40.414003 text: gas forfait base prolongation Jan-Mar 2023 823.8m\n"
)
brows.append(
    f"bud_creg_crisis_pack_2022,creg,2022,1250544000,,,budgeted,{SRC},strong,"
    "Sum BA 414001 733.34m + 414003 517.204m = 1.251bn class 2022 energy crisis CREG channel\n"
)
brows.append(
    f"bud_creg_crisis_pack_2023,creg,2023,2086900000,,,budgeted,{SRC},strong,"
    "Sum BA 414001 642.4m + 414003 1444.5m = 2.087bn class 2023 energy crisis CREG channel\n"
)
cce = {
    2021: 4929000,
    2022: 5290000,
    2023: 5409000,
    2024: 5359000,
    2025: 5375000,
    2026: 5390000,
    2027: 5405000,
}
for y, a in cce.items():
    brows.append(
        f"bud_cce_crb_dotatie_{y},cce_crb,{y},{a},,,budgeted,{SRC},strong,"
        "BA 21.40.414002 CCE/CRB annual subsidy eng=liq path\n"
    )
inr_liq = {
    2021: 1255000,
    2022: 1329000,
    2023: 1320000,
    2024: 1291000,
    2025: 1291000,
    2026: 1291000,
    2027: 1291000,
}
for y, a in inr_liq.items():
    brows.append(
        f"bud_icn_inr_dotatie_{y},icn_inr,{y},{a},,,budgeted,{SRC},strong,"
        "BA 21.40.414006 ICN/INR liquidations; eng near-identical\n"
    )
print("budgets", append_if_missing(bud_path, "bud_creg_social_tariff_enlarged", brows))


def cmt_row(cid, title, eid, ben, legal, dd, sy, ey, env, cash, goal, cut, hpath, notes):
    cj = json.dumps(cash, separators=(",", ":"))
    return ",".join(
        [
            cid,
            q(title),
            eid,
            q(ben),
            q(legal),
            dd,
            str(sy),
            str(ey),
            str(env),
            q(cj),
            "0",
            "active",
            PDF,
            q(goal),
            q(cut),
            SRC,
            "strong",
            hpath,
            q(notes),
        ]
    )


cmt_path = Path("docs/doge/data/commitments.csv")
cmts = [
    cmt_row(
        "cmt_creg_social_tariff_enlarged",
        "CREG channel enlargement social tariff gas+electricity crisis path",
        "creg",
        "Protected energy customers enlarged social tariff categories",
        "Energy crisis CM packages + BA 21.40.414001 FPS Economy",
        "2022-01-01",
        2021,
        2027,
        1667340000,
        {
            "2021": 276000000,
            "2022": 733340000,
            "2023": 642400000,
            "2024": 3400000,
            "2025": 3400000,
            "2026": 3400000,
            "2027": 3400000,
            "note": "BA 21.40.414001 eng=liq; extended tariff end Mar2023; residual 3.4m; dual FFS permanent+RVT",
        },
        "Compensate suppliers for enlarged social tariff gas and electricity",
        "Sunset residual 3.4m; reconcile FFS permanent+RVT series; dual mazout cheque",
        "Federal>Energy>CREG>social_tariff_enlarged",
        "tick294 dual FFS social tariff and collective 113m",
    ),
    cmt_row(
        "cmt_creg_basisfonds_heating",
        "CREG basisfonds heating forfait base energy crisis",
        "creg",
        "Households electricity gas heating forfait",
        "CM energy packages + BA 21.40.414003",
        "2022-01-01",
        2022,
        2023,
        1961704000,
        {
            "2022": 517204000,
            "2023": 1444500000,
            "q1_2023_elec_m": 620.7,
            "q1_2023_gas_m": 823.8,
            "note": "BA 21.40.414003; 2023 table equals Q1 prolongation split",
        },
        "Crisis basic package heating premium via CREG",
        "Temporary; dual mazout cheque and social heating fund",
        "Federal>Energy>CREG>basisfonds",
        "tick294 one-off crisis channel",
    ),
    cmt_row(
        "cmt_cce_crb_dotatie",
        "Central Economic Council CCE/CRB annual federal subsidy",
        "cce_crb",
        "Social partners employers workers",
        "Law 20 Sep 1948 art4 + BA 21.40.414002",
        "1948-09-20",
        2021,
        2027,
        37157000,
        {
            "2021": 4929000,
            "2022": 5290000,
            "2023": 5409000,
            "2024": 5359000,
            "2025": 5375000,
            "2026": 5390000,
            "2027": 5405000,
        },
        "Paritary socio-economic advice and technical wage margin report",
        "Core social dialogue infrastructure; dual NAR CNT",
        "Federal>Economy>CCE_CRB",
        "tick294 structural advisory ~5.4m",
    ),
    cmt_row(
        "cmt_icn_inr_dotatie",
        "Institute for National Accounts ICN/INR federal dotation",
        "icn_inr",
        "National accounts statistical production",
        "Law 21 Dec 1994 + BA 21.40.414006",
        "1994-12-21",
        2021,
        2027,
        9068000,
        {
            "2021": 1255000,
            "2022": 1329000,
            "2023": 1320000,
            "2024": 1291000,
            "2025": 1291000,
            "2026": 1291000,
            "2027": 1291000,
            "note": "liq series",
        },
        "Produce national accounts under Economy minister",
        "Core statistics; dual NBB Statbel FPB",
        "Federal>Economy>ICN_INR",
        "tick294 ~1.3m/yr",
    ),
    cmt_row(
        "cmt_creg_energy_crisis_pack_2022_23",
        "FPS Economy CREG energy crisis pack social tariff+basisfonds",
        "creg",
        "Households energy crisis",
        "Energy crisis packages 2022-23 BA 21.40.414001+414003",
        "2022-01-01",
        2022,
        2023,
        3337444000,
        {
            "2022_m": 1250.544,
            "2023_m": 2086.9,
            "components": "414001+414003",
            "dual": "mazout 208/144m + collective 113m + heating fund ~21m BA 42.40",
        },
        "Mitigate household energy price shock via CREG",
        "Temporary; dual ASEVA oil levy and FFS social tariff inventory",
        "Federal>Energy>crisis_CREG_pack",
        "tick294 dual tick291 mazout pack",
    ),
]
print("commitments", append_if_missing(cmt_path, "cmt_creg_social_tariff_enlarged", cmts))


def lb_row(
    iid, name, level, typ, hpath, ann, tot, tco, conf, src, ben, goal, out, absu, cost, diff, pi, cut, notes
):
    return ",".join(
        [
            iid,
            q(name),
            level,
            typ,
            hpath,
            str(ann),
            str(tot),
            q(tco),
            conf,
            src,
            q(ben),
            q(goal),
            q(out),
            str(absu),
            str(cost),
            str(diff),
            str(pi),
            q(cut),
            "seed",
            "",
            q(notes),
        ]
    )


lb_path = Path("docs/doge/data/leaderboard.csv")
lbs = [
    lb_row(
        "lb_creg_social_tariff_enlarged_733m",
        "CREG social tariff enlargement peak 733m 2022",
        "federal",
        "ops",
        "Federal>Energy>CREG>social_tariff_enlarged",
        733340000,
        1667340000,
        "Strong BA 21.40.414001: 276/733/642/3.4m 2021-24; crisis peak then residual; dual FFS permanent+RVT inventory",
        "strong",
        SRC,
        "Protected customers enlarged categories",
        "Supplier compensation enlarged social tariff",
        "Budget path; outturn residual FOI",
        5,
        9.0,
        4,
        6.5,
        "Keep targeted; sunset residual; publish outturn vs FFS",
        "tick294 dual FFS social tariff gas",
    ),
    lb_row(
        "lb_creg_basisfonds_1445m",
        "CREG basisfonds heating forfait 1.445bn 2023",
        "federal",
        "ops",
        "Federal>Energy>CREG>basisfonds",
        1444500000,
        1961704000,
        "Strong BA 21.40.414003: 517.2m 2022 + 1444.5m 2023 (elec 620.7+gas 823.8 Q1-23 prolongation)",
        "strong",
        SRC,
        "Households electricity and gas",
        "Crisis basic package heating premium",
        "Temporary crisis measure",
        6,
        9.5,
        3,
        6.8,
        "One-off; dual mazout cheque; avoid permanentisation",
        "tick294 energy crisis peak",
    ),
    lb_row(
        "lb_creg_crisis_pack_2bn_2023",
        "CREG crisis pack social+basisfonds ~2.09bn 2023",
        "federal",
        "ops",
        "Federal>Energy>crisis_CREG_pack",
        2086900000,
        3337444000,
        "Strong sum 2023: 642.4m social enlargement + 1444.5m basisfonds; 2022 pack 1.25bn; dual mazout/heating fund BA 42.40",
        "strong",
        SRC,
        "Households energy crisis",
        "Mitigate energy price shock via CREG channel",
        "BA tables 2022-23",
        6,
        9.5,
        4,
        7.0,
        "Temporary pack closed; reconcile FFS+CREG outturn",
        "tick294 dual ASEVA structural",
    ),
    lb_row(
        "lb_cce_crb_5_4m",
        "Central Economic Council CCE/CRB ~5.4m/yr",
        "federal",
        "ops",
        "Federal>Economy>CCE_CRB",
        5409000,
        37157000,
        "Strong BA 21.40.414002 path ~4.9-5.4m 2021-27; law 1948 paritary advisory",
        "strong",
        SRC,
        "Social partners",
        "Socio-economic advice wage margin report",
        "Structural body",
        2,
        3.5,
        2,
        2.8,
        "Keep; dual NAR efficiency review only",
        "tick294 not waste core",
    ),
    lb_row(
        "lb_icn_inr_1_3m",
        "Institute National Accounts ICN/INR ~1.3m/yr",
        "federal",
        "ops",
        "Federal>Economy>ICN_INR",
        1320000,
        9068000,
        "Strong BA 21.40.414006 liq ~1.26-1.33m path; law 1994",
        "strong",
        SRC,
        "Public statistics users",
        "National accounts production",
        "Core stats infrastructure",
        1,
        2.0,
        1,
        1.5,
        "Keep; dual NBB Statbel map only",
        "tick294 not waste",
    ),
]
print("leaderboard", append_if_missing(lb_path, "lb_creg_social_tariff_enlarged", lbs))

# --- FOI queue ---
foi_path = Path("docs/doge/data/foi_queue.csv")
foi_line = (
    "gap_creg_crisis_outturn_2022_24,Federal>Energy>CREG>crisis_BA_outturn,creg,"
    "Cash outturn 2021-2025 BA 21.40.414001 social tariff enlargement and BA 21.40.414003 basisfonds vs Kamer budget tables; "
    "beneficiary counts households; reconcile FFS social tariff permanent+RVT inventory and CREG annual accounts,"
    "Peak ~2.09bn 2023 class energy-crisis channel; budget tables strong outturn and FFS dual perimeter residual,"
    "5,FOD Economie / CREG openbaarheid,,https://www.creg.be,"
    "docs/doge/foi/drafts/gap_creg_crisis_outturn_2022_24.md,ready,2026-07-30,,,,,,"
    "cmt_creg_social_tariff_enlarged|cmt_creg_basisfonds_heating|cmt_creg_energy_crisis_pack_2022_23,"
    "lb_creg_crisis_pack_2bn_2023|lb_creg_basisfonds_1445m,"
    "2026-07-30T09:45:00Z,2026-07-30T09:45:00Z,tick294 draft ready human send\n"
)
print("foi", append_if_missing(foi_path, "gap_creg_crisis_outturn_2022_24", [foi_line]))

# --- research_queue ---
rq_path = Path("docs/doge/data/research_queue.csv")
text = rq_path.read_text(encoding="utf-8")
# mark rq_285 done
lines = text.splitlines(keepends=True)
out = []
for line in lines:
    if line.startswith("rq_285,"):
        # rebuild row with done status
        parts = line.rstrip("\n").split(",")
        # status is index 4
        if len(parts) > 4:
            parts[4] = "done"
            # blocked_gap_id index 8
            if len(parts) > 8:
                parts[8] = "gap_creg_crisis_outturn_2022_24"
            # updated_utc index 10
            if len(parts) > 10:
                parts[10] = "2026-07-30T09:45:00Z"
            # notes last field - careful with commas in notes
            # Safer: replace open with done and append notes via string replace
        line = (
            "rq_285,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CERN/DK RES). "
            "Prefer before idle; do not idle while public work remains.,"
            "gap_creg_crisis_outturn_2022_24,2026-07-30T09:15:00Z,2026-07-30T09:45:00Z,"
            "tick294: CREG social tariff enlargement 276/733/642m + basisfonds 517/1445m pack ~2.09bn 2023; "
            "CCE 5.4m INR 1.3m; FOI ready; spawn rq_286\n"
        )
    out.append(line)
if "rq_286," not in text:
    out.append(
        "rq_286,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CREG crisis pack). "
        "Prefer before idle; do not idle while public work remains.,,"
        "2026-07-30T09:45:00Z,,Spawned tick294 after CREG crisis pack CCE INR; rq_116 SWA deferred\n"
    )
rq_path.write_text("".join(out), encoding="utf-8")
print("research_queue updated")

# --- loop_state ---
ls_path = Path("docs/doge/data/loop_state.csv")
ls_path.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T09:45:00Z,rq_285,294,no,"
    "Scheduler 60s. Next prio5 rq_286; rq_116 SWA deferred. FOI ready. "
    "tick294 CREG crisis pack ~2.09bn 2023 + CCE/INR.\n",
    encoding="utf-8",
)
print("loop_state ok")

# FOI draft
draft = Path("docs/doge/foi/drafts/gap_creg_crisis_outturn_2022_24.md")
draft.write_text(
    """# FOI draft — gap_creg_crisis_outturn_2022_24

**Status:** ready (not sent)  
**Gap ID:** `gap_creg_crisis_outturn_2022_24`  
**Linked:** `cmt_creg_social_tariff_enlarged`, `cmt_creg_basisfonds_heating`, `cmt_creg_energy_crisis_pack_2022_23`  
**Tick:** 294  

Public fill (Kamer 55K2933/016 FOD Economie programme 21/4):

| Line | Role | Amounts (eng=liq unless noted) |
|------|------|--------------------------------|
| BA 21.40.414001 | CREG social tariff enlargement gas+elec | **276 / 733.34 / 642.4 / 3.4m** 2021–24 then 3.4m path |
| BA 21.40.414003 | CREG basisfonds / forfait base (heating premium) | **517.2m** 2022 / **1 444.5m** 2023 |
| Text Q1-2023 | Basisfonds prolongation | Elec **620.7m** + gas **823.8m** |
| Pack class | 414001+414003 | **~1.25bn** 2022 / **~2.09bn** 2023 |
| Dual | Mazout cheque + collective + heating fund | BA 42.40 (tick291) separate |
| Dual | FFS social tariff permanent+RVT | Inventory perimeter differs |

Also mapped structural: CCE/CRB BA 21.40.414002 **~5.4m/yr**; ICN/INR BA 21.40.414006 **~1.3m/yr**.

Residual: cash outturn vs budget; household beneficiary counts; FFS dual reconcile.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie, K.M.O., Middenstand en Energie
en/of CREG — dienst openbaarheid van bestuur
https://economie.fgov.be / https://www.creg.be

Betreft: Verzoek om openbaarmaking — CREG-kanalen sociaal tarief en basispakket 2021–2025 (gap_creg_crisis_outturn_2022_24)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking / afschrift van de hieronder
omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. Cash-by-year vastleggingen en vereffeningen 2021–2025 voor basisallocatie
   32.21.40.414001 (CREG — uitbreiding sociaal tarief gas en elektriciteit),
   met eventuele uitsplitsing gas vs elektriciteit en vs structureel sociaal tarief.
2. Cash-by-year vastleggingen en vereffeningen 2021–2025 voor basisallocatie
   32.21.40.414003 (CREG — basispakket / forfait de base / verwarmingspremie),
   met uitsplitsing elektriciteit vs gas en per periode (incl. verlenging Q1 2023).
3. Aantal begunstigde huishoudens / leverancierscompensaties per jaar voor beide
   kanalen (geaggregeerd; geen persoonsgegevens nodig).
4. Eventuele reconciliatietabel met de inventaris fossiele subsidies / FFS-sociale-
   tarieflijnen (permanent + RVT) voor zover bij FOD Economie of CREG berustend.

Periode: 1 januari 2021 tot 31 december 2025.

### 2. Context (waarom)

Onderzoek naar overheidsuitgaven (transparantie). Intern pad:
Federal > Energy > CREG crisis channels. Publieke Kamer-tabellen (DOC 55 2933/016)
geven budgetpaden tot ~2,09 mrd EUR in 2023-class; ontbrekend is de effectieve
cash-outturn en de duale perimeter t.o.v. FFS-inventaris.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail].
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: gap_creg_crisis_outturn_2022_24

Met vriendelijke groet,

[…]
```

**Do not send as agent.** Human send only.
""",
    encoding="utf-8",
)
print("draft", draft)
print("tick294 write complete")

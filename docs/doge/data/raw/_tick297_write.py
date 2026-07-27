# tick297: Energy Transition Fund deepen — call awards, financing, L5 sample
from pathlib import Path
import json

SRC = "src_kamer_etf_deepen_2023_26"
PDF_K = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"
PDF_O = "docs/doge/data/raw/etf_overzicht_projecten.pdf"
TICK = "tick297"
URL_O = "https://economie.fgov.be/sites/default/files/Files/Energy/Overzicht-gesubsidieerde-projecten-energietransitiefonds.pdf"


def q(s: str) -> str:
    s = str(s)
    if any(c in s for c in [",", '"', "\n"]):
        return '"' + s.replace('"', '""') + '"'
    return s


def append_if_missing(path: Path, lines: list[str]) -> int:
    text = path.read_text(encoding="utf-8")
    added = 0
    with path.open("a", encoding="utf-8", newline="") as f:
        for line in lines:
            key = line.split(",", 1)[0]
            if key not in text:
                f.write(line if line.endswith("\n") else line + "\n")
                text += line
                added += 1
    return added


print(
    "sources",
    append_if_missing(
        Path("docs/doge/data/sources.csv"),
        [
            f"{SRC},Kamer 55K2933/016 ETF call awards I-VI + financing + overzicht 140 projects July 2026,"
            f"{PDF_K}; {URL_O},Belgische Kamer + FOD Economie AD Energie,2026-07-30,official_budget,"
            "Calls I-VI awards sum 129.146m / 84 projects; BA 24.75m/yr + ops 0.25m; Doel1-2 LTO fee 20m/yr 2016-25; "
            "overview 140 projects calls I-X July2026; per-project EUR residual FOI; tick297\n"
        ],
    ),
)

print(
    "entities",
    append_if_missing(
        Path("docs/doge/data/entities.csv"),
        [
            "etf_energy_transition_fund,Energietransitiefonds ETF,Fonds de transition energetique FTE,"
            "Federal Energy Transition Fund,programme,fod_economy,bi,"
            "https://economie.fgov.be/nl/themas/energie/energietransitie/energietransitiefonds,,,,"
            "BA 42.90.313201 ~24.75m/yr; financed by nuclear LTO fee Doel1-2 20m/yr class; 140 projects July2026; tick297\n"
        ],
    ),
)

# budgets
brows = []
# annual BA already partial; ensure multi-year + ops + financing
for y in range(2021, 2028):
    rid = f"bud_etf_ba_{y}"
    brows.append(
        f"{rid},etf_energy_transition_fund,{y},24750000,,,budgeted,{SRC},strong,"
        "BA 42.90.313201 eng=liq flat 24.75m path Kamer 2023 multi-year\n"
    )
for y in range(2022, 2028):
    brows.append(
        f"bud_etf_ops_{y},etf_energy_transition_fund,{y},250000,,,budgeted,{SRC},strong,"
        "BA 42.90.121101 ETF operating costs external auditor+technical experts path 250k\n"
    )
brows.append(
    f"bud_etf_ops_2021,etf_energy_transition_fund,2021,155000,,,budgeted,{SRC},strong,"
    "BA 42.90.121101 liq 155k 2021 (eng 224k)\n"
)
# call awards
calls = [
    (1, 2017, 1, 221827, "Jun2017 award 2017"),
    (2, 2017, 17, 27912262, "Dec2017 award Jul2018"),
    (3, 2018, 17, 29112383, "Aug2018 award Sep2019"),
    (4, 2019, 15, 23006075, "Oct2019 award Jun2020"),
    (5, 2020, 14, 24357268, "Nov2020 award Jun2021"),
    (6, 2021, 20, 24536176, "Nov2021 award Jun2022"),
]
for n, y, np, eur, note in calls:
    brows.append(
        f"bud_etf_call{n}_award,etf_energy_transition_fund,{y},{eur},,,outturn,{SRC},strong,"
        f"Call {n} total subsidy awarded to {np} projects; {note}; Kamer 55K2933/016\n"
    )
brows.append(
    f"bud_etf_calls_I_VI_sum,etf_energy_transition_fund,2022,129145991,,,outturn,{SRC},strong,"
    "Sum awards calls I-VI 129.145991m across 84 projects (Kamer tables)\n"
)
brows.append(
    f"bud_etf_call7_budget_2023,etf_energy_transition_fund,2023,25000000,,,budgeted,{SRC},strong,"
    "Call VII Nov2022 planned budget 25m 2023 (Kamer text)\n"
)
# Doel LTO financing inflow
for y in range(2016, 2026):
    brows.append(
        f"bud_etf_doel12_lto_fee_{y},etf_energy_transition_fund,{y},20000000,,,outturn,{SRC},strong,"
        "Doel1&2 LTO convention fee 20m/yr to federal state 15 Apr 2016-2025 feeds ETF (art4/2 nuclear exit law)\n"
    )
print("budgets", append_if_missing(Path("docs/doge/data/budgets.csv"), brows))


def cmt_row(cid, title, eid, ben, legal, dd, sy, ey, env, cash, goal, cut, hpath, notes):
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
            str(env if env is not None else ""),
            q(json.dumps(cash, separators=(",", ":"))),
            "0",
            "active",
            PDF_K,
            q(goal),
            q(cut),
            SRC,
            "strong",
            hpath,
            q(notes),
        ]
    )


cmts = [
    cmt_row(
        "cmt_etf_calls_I_VI_awards",
        "Energy Transition Fund competitive call awards I-VI",
        "etf_energy_transition_fund",
        "Selected energy R&I consortia (84 projects)",
        "Law 28 Jun 2015 + RD 9 May 2017 + annual calls BA 42.90.313201",
        "2017-06-30",
        2017,
        2022,
        129145991,
        {
            "call1_m": 0.222,
            "call1_n": 1,
            "call2_m": 27.912,
            "call2_n": 17,
            "call3_m": 29.112,
            "call3_n": 17,
            "call4_m": 23.006,
            "call4_n": 15,
            "call5_m": 24.357,
            "call5_n": 14,
            "call6_m": 24.536,
            "call6_n": 20,
            "sum_m": 129.146,
            "projects": 84,
            "call7_budget_2023_m": 25,
            "overview_projects_jul2026": 140,
            "calls_I_X": True,
        },
        "Fund energy R&I and supply-security projects under federal competence",
        "Publish machine-readable EUR per project; dual regional climate funds screen",
        "Federal>Energy>ETF>calls",
        f"{TICK} Kamer awards + FOD overzicht 140 projects Jul2026",
    ),
    cmt_row(
        "cmt_etf_doel12_financing",
        "ETF financing via Doel1-2 LTO nuclear fee 20m/yr",
        "etf_energy_transition_fund",
        "Federal ETF budget",
        "Nuclear exit law 31 Jan 2003 art4/2 + Doel1-2 LTO convention + CM 1 Dec 2017 ceiling",
        "2016-04-15",
        2016,
        2025,
        200000000,
        {
            "annual_fee_m": 20,
            "first_payment": "2016-04-15",
            "last_payment": "2025-04-15",
            "cm_2017_ceiling": "30m 2018-19 then +5m above 20m until reserves exhausted",
            "ba_path_2021_27_m": 24.75,
            "ops_k": 250,
            "note": "Fund fed by nuclear LTO fee not pure TE appropriation; BA ~24.75m spend path",
        },
        "Ring-fence nuclear LTO fee into energy transition R&I",
        "Track reserve exhaustion post-2025 LTO fee end; dual Hedera CAP separate",
        "Federal>Energy>ETF>financing",
        f"{TICK} dual nuclear stack Hedera CAP",
    ),
    cmt_row(
        "cmt_etf_l5_sample_public",
        "ETF public named project sample dual nuclear-grid-H2-SMR",
        "etf_energy_transition_fund",
        "Elia TECNUBEL SCK UGent Fluxys BASF INOVYN KMS VITO consortia class",
        "FOD Economie ETF overzicht July 2026 140 projects",
        "2026-07-01",
        2018,
        2026,
        0,
        {
            "sample": [
                "Elia Local Inertia call1",
                "TECNUBEL ARCHER robotics decommissioning call2",
                "SCK CEN ASOF spent fuel call2",
                "UGent/UMons BEOWIND offshore call2",
                "UGent/Fluxys BE-HyStore H2 storage call7",
                "KULeuven/BASF/Elia HARMONIC call7",
                "KULeuven/INOVYN FLEX-SMR call10",
                "VITO/UGent/Engie SMART-C-HUB SMR heat call10",
            ],
            "projects_total_jul2026": 140,
            "per_project_eur": "Unknown residual FOI",
            "url": URL_O,
        },
        "Document public L5 beneficiaries without inventing project EUR",
        "FOI cash-by-project matrix only residual",
        "Federal>Energy>ETF>L5_sample",
        f"{TICK} names strong EUR residual",
    ),
]
print("commitments", append_if_missing(Path("docs/doge/data/commitments.csv"), cmts))


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


lbs = [
    lb_row(
        "lb_etf_awards_129m_I_VI",
        "ETF call awards I-VI sum 129.1m (84 projects)",
        "federal",
        "ops",
        "Federal>Energy>ETF>awards_I_VI",
        24536176,
        129145991,
        "Strong Kamer: call awards 0.22+27.9+29.1+23.0+24.4+24.5m; 84 projects; BA path 24.75m/yr; 140 projects Jul2026 overzicht",
        "strong",
        SRC,
        "Selected R&I consortia",
        "Energy transition innovation competitive grants",
        "Call totals strong; per-project EUR residual",
        4,
        7.5,
        3,
        5.5,
        "Publish EUR matrix L5; dual regional funds",
        f"{TICK} upgrades lb_etf_24_75m",
    ),
    lb_row(
        "lb_etf_doel_fee_20m",
        "ETF financed by Doel1-2 LTO fee 20m/yr",
        "federal",
        "ops",
        "Federal>Energy>ETF>financing_Doel",
        20000000,
        200000000,
        "Strong Kamer: convention fee 20m/yr 2016-2025 feeds ETF; CM 2017 raised spend ceiling; dual nuclear LTO revenue not TE taxex",
        "strong",
        SRC,
        "Electrabel/operator fee to state",
        "Ring-fence LTO fee into energy R&I",
        "Financing path strong",
        3,
        6.0,
        2,
        4.2,
        "Track post-2025 funding when LTO fee ends",
        f"{TICK} dual Hedera CAP separate",
    ),
    lb_row(
        "lb_etf_140_projects_opacity",
        "ETF 140 named projects public EUR matrix opaque",
        "federal",
        "ops",
        "Federal>Energy>ETF>L5_opacity",
        24750000,
        129145991,
        "Strong FOD overzicht Jul2026: 140 projects named with beneficiaries; per-project EUR not in public PDF — residual FOI",
        "strong",
        SRC,
        "140 project consortia",
        "Transparency of competitive energy R&I aid",
        "Names public amounts missing",
        5,
        6.5,
        3,
        5.2,
        "FOI machine-readable award table by project",
        f"{TICK}",
    ),
    lb_row(
        "lb_etf_ops_250k",
        "ETF operating costs external audit 250k/yr",
        "federal",
        "ops",
        "Federal>Energy>ETF>ops",
        250000,
        250000,
        "Strong BA 42.90.121101 path 250k for external auditor + technical experts from call VI",
        "strong",
        SRC,
        "Fund administration",
        "Financial and technical evaluation of proposals",
        "Small overhead",
        1,
        1.5,
        1,
        1.2,
        "Keep; publish audit cost KPIs",
        f"{TICK}",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

# Update FOI: refine gap if exists or new residual for EUR matrix
foi_line = (
    "gap_etf_project_eur_matrix,Federal>Energy>ETF>project_EUR_L5,etf_energy_transition_fund,"
    "Machine-readable table of all ETF awards 2017-2026: project name beneficiary KBO call-year "
    "awarded EUR cash-by-year paid remaining; reconcile calls I-X with BA 42.90.313201 outturn and 140-project overzicht,"
    "Names of 140 projects public July2026; call I-VI totals 129.1m strong; per-project EUR still opaque for waste ranking,"
    "5,FOD Economie AD Energie ETF cell,ETF.FTE@economie.fgov.be,https://economie.fgov.be,"
    "docs/doge/foi/drafts/gap_etf_project_eur_matrix.md,ready,2026-07-30,,,,,,"
    "cmt_etf_calls_I_VI_awards|cmt_etf_l5_sample_public,"
    "lb_etf_awards_129m_I_VI|lb_etf_140_projects_opacity,"
    "2026-07-30T11:15:00Z,2026-07-30T11:15:00Z,tick297 draft ready; partial public name fill\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

# research queue
rq = Path("docs/doge/data/research_queue.csv")
text = rq.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_288,"):
        line = (
            "rq_288,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after telecom/Airbus fill). "
            "Prefer before idle; do not idle while public work remains.,"
            "gap_etf_project_eur_matrix,2026-07-30T10:45:00Z,2026-07-30T11:15:00Z,"
            "tick297: ETF calls I-VI awards 129.1m/84 projects; Doel LTO fee 20m; 140 projects named Jul2026; "
            "EUR matrix FOI; spawn rq_289\n"
        )
    out.append(line)
if "rq_289," not in text:
    out.append(
        "rq_289,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after ETF deepen). "
        "Prefer before idle; do not idle while public work remains. Note progress@300 soon.,,"
        "2026-07-30T11:15:00Z,,Spawned tick297 after ETF deepen; rq_116 SWA deferred; progress@300 in 3 ticks\n"
    )
rq.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T11:15:00Z,rq_288,297,no,"
    "Scheduler 60s. Next prio5 rq_289; progress@300 in 3 ticks; rq_116 SWA deferred. "
    "tick297 ETF awards 129.1m + 140 projects named.\n",
    encoding="utf-8",
)
print("loop_state ok")

Path("docs/doge/foi/drafts/gap_etf_project_eur_matrix.md").write_text(
    f"""# FOI draft — gap_etf_project_eur_matrix

**Status:** ready (not sent)  
**Gap ID:** `gap_etf_project_eur_matrix`  
**Linked:** `cmt_etf_calls_I_VI_awards`, `cmt_etf_l5_sample_public`  
**Tick:** 297  

Public fill:

| Item | Value | Source |
|------|-------|--------|
| BA 42.90.313201 | **24.75m/yr** eng=liq 2021–27 | Kamer 55K2933/016 |
| Ops BA 42.90.121101 | **250k/yr** | Kamer |
| Calls I–VI awards | **€129.146m** / **84** projects | Kamer |
| Call VII budget class | **25m** 2023 | Kamer |
| Financing | Doel1&2 LTO fee **20m/yr** 2016–2025 | Kamer |
| Project overzicht | **140** named projects calls I–X (Jul 2026) | [FOD PDF]({URL_O}) |
| L5 sample names | Elia, TECNUBEL, SCK ASOF, BE-HyStore, HARMONIC, FLEX-SMR… | FOD PDF |

**Missing:** awarded EUR and cash paid per project.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie — Algemene Directie Energie
Cel Energietransitiefonds
ETF.FTE@economie.fgov.be
Koning Albert II-laan 16, 1000 Brussel

Betreft: Verzoek om openbaarmaking — Energietransitiefonds project-EUR-matrix 2017–2026 (gap_etf_project_eur_matrix)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking / afschrift van de hieronder
omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. Een machineleesbare tabel (CSV/Excel) van alle steuntoekenningen van het
   Energietransitiefonds (oproepen I tot en met X, of recentste stand), met per
   project: projectnaam, begunstigde(n), KBO-nummer, oproepnummer, toekenningsdatum,
   toegekend bedrag (EUR), cumulatief uitbetaald bedrag, openstaand saldo, en
   status (lopend/afgesloten).
2. Cash-by-year vastleggingen en vereffeningen op basisallocatie 32.42.90.313201
   2017–2026, te reconcilieren met de som van de projecttoekenningen.
3. Eventuele koninklijke besluiten / toekenningslijsten per oproep met bedragen
   (publieke samenvatting volstaat indien volledige dossiers bedrijfsgeheimen bevatten).

Periode: 1 januari 2017 tot 31 december 2026.

### 2. Context (waarom)

Onderzoek naar overheidsuitgaven (transparantie). Intern pad:
Federal > Energy > ETF. Publiek beschikbaar: oproeptotalen I–VI (~129 mEUR) en
namen van 140 projecten (overzicht juli 2026). Ontbrekend is de EUR per project.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail].
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: gap_etf_project_eur_matrix

Met vriendelijke groet,

[…]
```

**Do not send as agent.** Human send only.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick297 write complete")

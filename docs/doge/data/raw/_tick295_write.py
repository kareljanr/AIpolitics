# tick295: hydrogen RRF pack + press concession BA path (Kamer 55K2933/016)
from pathlib import Path
import json

SRC = "src_kamer_55k2933_h2_press"
PDF = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"
TICK = "tick295"


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


# --- sources ---
src_path = Path("docs/doge/data/sources.csv")
print(
    "sources",
    append_if_missing(
        src_path,
        [
            f"{SRC},Kamer 55K2933/016 FOD Economie hydrogen RRF pack + press concession BA,"
            f"{PDF},Belgische Kamer van volksvertegenwoordigers,2026-07-30,official_budget,"
            "BA 42.50.313203/31.32.03 H2 eng 300m 2022-23 liq path 4/4/24/86m; "
            "BA 313204 H2 import 10m eng; BA 313205 green steel electrolyser 6m; "
            "BA 43.40.31.22.01 press concession eng 170-178.6m then 129-138m path; tick295\n"
        ],
    ),
)

# --- entities (light) ---
ent_path = Path("docs/doge/data/entities.csv")
print(
    "entities",
    append_if_missing(
        ent_path,
        [
            "fed_h2_rrf,Federaal waterstof RRF-pakket FOD Economie,Paquet hydrogene federal RRF SPF Economie,"
            "Federal hydrogen RRF package FPS Economy,programme,fod_economy,bi,https://economie.fgov.be,,,,"
            "RRF axis climate/H2: BA 42.50.313203 eng 300m class + import 10m + green steel electrolyser 6m; tick295\n"
        ],
    ),
)

# --- budgets ---
brows = []
# H2 call / backbone 313203 eng (kEUR*1000)
for y, a in {2022: 300000000, 2023: 300000000}.items():
    brows.append(
        f"bud_h2_call_eng_{y},fed_h2_rrf,{y},{a},,,budgeted,{SRC},strong,"
        "BA 42.50.313203 (=31.32.03 compact) engagement H2 innovation call/backbone; "
        "text: 2022 credits blocked postponed to 2023 same amount — not additive double cash\n"
    )
# H2 liq path
for y, a in {2024: 4000000, 2025: 4000000, 2026: 24000000, 2027: 86000000}.items():
    brows.append(
        f"bud_h2_call_liq_{y},fed_h2_rrf,{y},{a},,,budgeted,{SRC},strong,"
        "BA 42.50.313203 liquidations path; RRF demo projects target -50kt CO2/yr from 2026\n"
    )
# H2 import infra
brows.append(
    f"bud_h2_import_infra_eng_2023,fed_h2_rrf,2023,10000000,,,budgeted,{SRC},strong,"
    "BA 42.50.313204 eng 10m CM 20Oct2021 axis5 H2 import infrastructure call\n"
)
for y, a in {2023: 2000000, 2024: 3000000, 2025: 3000000, 2026: 2000000}.items():
    brows.append(
        f"bud_h2_import_infra_liq_{y},fed_h2_rrf,{y},{a},,,budgeted,{SRC},strong,"
        "BA 42.50.313204 liquidations H2 import infrastructure\n"
    )
# green steel electrolyser
brows.append(
    f"bud_h2_green_steel_electrolyser_eng_2023,fed_h2_rrf,2023,6000000,,,budgeted,{SRC},strong,"
    "BA 42.50.313205 eng 6m CM 20Oct2021 flexible electrolyser for green steel axis5\n"
)
for y, a in {2023: 1000000, 2024: 2000000, 2025: 2000000, 2026: 1000000}.items():
    brows.append(
        f"bud_h2_green_steel_electrolyser_liq_{y},fed_h2_rrf,{y},{a},,,budgeted,{SRC},strong,"
        "BA 42.50.313205 liquidations flexible electrolyser green steel\n"
    )
# pack class eng 2023
brows.append(
    f"bud_h2_rrf_pack_eng_2023,fed_h2_rrf,2023,316000000,,,budgeted,{SRC},strong,"
    "Sum eng class 2023: 300m H2 call/backbone + 10m import + 6m electrolyser = 316m "
    "(300m may be re-inscription of 2022 blocked credits)\n"
)
# press concession multi-year BA 43.40.31.22.01
press_eng = {
    2021: 170000000,
    2022: 178593000,
    2023: 178593000,
    2024: 129000000,
    2025: 132000000,
    2026: 135000000,
    2027: 138000000,
}
press_liq = {
    2021: 167993000,
    2022: 175700000,
    2023: 175700000,
    2024: 129000000,
    2025: 132000000,
    2026: 135000000,
    2027: 138000000,
}
for y, a in press_liq.items():
    brows.append(
        f"bud_press_concession_ba_{y},bpost,{y},{a},,,budgeted,{SRC},strong,"
        f"BA 43.40.31.22.01 press distribution concession compensation liq; eng {press_eng[y]}; "
        "CM 25Mar2021; amounts still provisional in 2023 doc\n"
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
            PDF,
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
        "cmt_h2_rrf_call_backbone",
        "Federal RRF hydrogen innovation call / backbone engagement 300m class",
        "fed_h2_rrf",
        "Selected H2 demo firms (L5 residual FOI)",
        "RRF reg 2021/241 + BE PHV axis1 + BA 42.50.313203 (=31.32.03)",
        "2022-01-01",
        2022,
        2027,
        300000000,
        {
            "eng_2022_m": 300,
            "eng_2023_m": 300,
            "note_double": "2022 eng blocked postponed 2023 same amount — envelope class 300m not 600m",
            "liq_m": {"2024": 4, "2025": 4, "2026": 24, "2027": 86},
            "co2_target_t_from_2026": 50000,
            "selection_deadline_class": "2022-06-30",
            "impl_deadline_class": "2026-Q2",
        },
        "Accelerate H2 demo technologies via RRF innovation call / backbone",
        "Publish named winners L5; track CO2 KPI; dual regional H2 funds",
        "Federal>Energy>H2_RRF>call_backbone",
        f"{TICK} RRF not pure TE waste; L5 end-receivers FOI",
    ),
    cmt_row(
        "cmt_h2_import_infra_10m",
        "Federal H2 import infrastructure project call 10m",
        "fed_h2_rrf",
        "Selected H2 import infra promoters",
        "CM 20 Oct 2021 axis5 + BA 42.50.313204",
        "2021-10-20",
        2023,
        2026,
        10000000,
        {"eng_2023_m": 10, "liq_m": {"2023": 2, "2024": 3, "2025": 3, "2026": 2}},
        "Support hydrogen import infrastructure development",
        "L5 winners FOI; dual regional import corridors",
        "Federal>Energy>H2_RRF>import_infra",
        f"{TICK}",
    ),
    cmt_row(
        "cmt_h2_green_steel_electrolyser_6m",
        "Federal flexible electrolyser for green steel 6m",
        "fed_h2_rrf",
        "Green steel electrolyser project promoter",
        "CM 20 Oct 2021 axis5 + BA 42.50.313205",
        "2021-10-20",
        2023,
        2026,
        6000000,
        {"eng_2023_m": 6, "liq_m": {"2023": 1, "2024": 2, "2025": 2, "2026": 1}},
        "Flexible electrolyser for green steel industrial transition",
        "L5 beneficiary FOI; additionality vs EU IPCEI",
        "Federal>Energy>H2_RRF>green_steel",
        f"{TICK}",
    ),
    cmt_row(
        "cmt_h2_rrf_pack_316m_eng",
        "Federal hydrogen RRF pack eng class 316m 2023",
        "fed_h2_rrf",
        "H2 demo import green-steel promoters",
        "RRF PHV + CM 2021 axis5 + BA 42.50.313203-05",
        "2021-10-20",
        2022,
        2027,
        316000000,
        {
            "call_backbone_eng_class_m": 300,
            "import_m": 10,
            "electrolyser_m": 6,
            "sum_eng_2023_class_m": 316,
            "dual_smr": "SMR BA 31.32.01 separate 100m package tick287",
        },
        "Federal H2 transition package under RRF and investment axis",
        "FOI L5 winners full matrix; dual regional H2",
        "Federal>Energy>H2_RRF>pack",
        f"{TICK} dual SMR nuclear H2 path",
    ),
    cmt_row(
        "cmt_press_concession_ba_path",
        "Press distribution concession FPS Economy BA multi-year path",
        "bpost",
        "Press concessionaire (bpost class) + recognized newspapers periodicals",
        "CM 25 Mar 2021 service concession + BA 43.40.31.22.01 FPS Economy control",
        "2021-03-25",
        2021,
        2027,
        1053986000,
        {
            "eng_m": {
                "2021": 170,
                "2022": 178.593,
                "2023": 178.593,
                "2024": 129,
                "2025": 132,
                "2026": 135,
                "2027": 138,
            },
            "liq_m": {
                "2021": 167.993,
                "2022": 175.7,
                "2023": 175.7,
                "2024": 129,
                "2025": 132,
                "2026": 135,
                "2027": 138,
            },
            "note": "2023 Kamer amounts provisional procedure ongoing; dual press 125m save path secondary; reconcile AR SGEI press end mid-2024",
        },
        "Compensation for recognized newspaper and periodical distribution concession",
        "Complete phase-out; no soft replacement; FOI actual outturn vs BA",
        "Federal>bpost>press_concession_BA",
        f"{TICK} upgrades secondary 125m class with strong FPS BA path",
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
        "lb_h2_rrf_300m_eng",
        "Federal RRF hydrogen call/backbone eng 300m class",
        "federal",
        "ops",
        "Federal>Energy>H2_RRF>call_backbone",
        300000000,
        300000000,
        "Strong BA 42.50.313203: eng 300m 2022+2023 (re-inscription class not additive); liq path 4/4/24/86m 2024-27; RRF demo -50kt CO2 target",
        "strong",
        SRC,
        "Selected H2 demo firms L5 residual",
        "Accelerate H2 demonstration technologies",
        "Budget eng strong; spend lag; winners FOI",
        5,
        8.5,
        5,
        6.5,
        "Publish L5 winners; audit additionality vs EU H2 funds",
        f"{TICK} not pure waste RRF transition",
    ),
    lb_row(
        "lb_h2_import_10m",
        "Federal H2 import infrastructure call 10m",
        "federal",
        "ops",
        "Federal>Energy>H2_RRF>import_infra",
        10000000,
        10000000,
        "Strong BA 42.50.313204 eng 10m 2023 CM Oct2021; liq 2/3/3/2m 2023-26",
        "strong",
        SRC,
        "Import infra promoters",
        "H2 import infrastructure",
        "BA path only L5 FOI",
        3,
        5.0,
        4,
        4.0,
        "FOI named projects; dual regional corridors",
        f"{TICK}",
    ),
    lb_row(
        "lb_h2_green_steel_6m",
        "Flexible electrolyser green steel 6m",
        "federal",
        "ops",
        "Federal>Energy>H2_RRF>green_steel",
        6000000,
        6000000,
        "Strong BA 42.50.313205 eng 6m CM Oct2021; liq 1/2/2/1m 2023-26",
        "strong",
        SRC,
        "Green steel project",
        "Industrial H2 steel transition",
        "BA path; single project class",
        3,
        4.0,
        3,
        3.5,
        "FOI beneficiary; additionality IPCEI",
        f"{TICK}",
    ),
    lb_row(
        "lb_press_concession_ba_176m",
        "Press distribution concession BA ~176m peak then 129m path",
        "federal",
        "ops",
        "Federal>bpost>press_concession_BA",
        175700000,
        1053986000,
        "Strong BA 43.40.31.22.01 liq 168/175.7/175.7 then 129-138m 2021-27; CM Mar2021; dual secondary 125m save narrative and SGEI press end mid-2024",
        "strong",
        SRC,
        "Publishers readers concessionaire",
        "Recognized press distribution compensation",
        "Budget path provisional 2023; outturn FOI",
        7,
        8.5,
        4,
        7.0,
        "Complete phase-out; reconcile AR SGEI vs BA residual",
        f"{TICK} dual gap_bpost_uso_split",
    ),
    lb_row(
        "lb_h2_rrf_pack_316m",
        "Federal H2 RRF pack eng ~316m class 2023",
        "federal",
        "ops",
        "Federal>Energy>H2_RRF>pack",
        316000000,
        316000000,
        "Strong sum eng class: 300+10+6m; dual SMR nuclear H2 research 100m separate",
        "strong",
        SRC,
        "H2 industrial transition actors",
        "RRF climate axis H2 package",
        "Engagement class; cash lag",
        5,
        8.5,
        5,
        6.5,
        "L5 matrix FOI; dual regional H2",
        f"{TICK}",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

# FOI
foi_line = (
    "gap_h2_rrf_l5_winners,Federal>Energy>H2_RRF>L5_winners,fed_h2_rrf,"
    "Named L5 winners amounts and cash-by-year 2022-2027 for BA 42.50.313203 hydrogen call/backbone "
    "plus 313204 import infra and 313205 green steel electrolyser; outturn vs 300m eng class; "
    "project selection decisions and CO2 KPI progress,"
    "Eng class ~300m+16m material RRF industrial aid; budget tables strong end-receiver L5 opaque,"
    "6,FOD Economie AD Energie / RRF coordination,,https://economie.fgov.be,"
    "docs/doge/foi/drafts/gap_h2_rrf_l5_winners.md,ready,2026-07-30,,,,,,"
    "cmt_h2_rrf_call_backbone|cmt_h2_import_infra_10m|cmt_h2_green_steel_electrolyser_6m,"
    "lb_h2_rrf_300m_eng|lb_h2_rrf_pack_316m,"
    "2026-07-30T10:15:00Z,2026-07-30T10:15:00Z,tick295 draft ready human send\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

# Also update press FOI note? gap_bpost_uso_split already ready — leave it; optional note in log only.

# research_queue
rq_path = Path("docs/doge/data/research_queue.csv")
text = rq_path.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_286,"):
        line = (
            "rq_286,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CREG crisis pack). "
            "Prefer before idle; do not idle while public work remains.,"
            "gap_h2_rrf_l5_winners,2026-07-30T09:45:00Z,2026-07-30T10:15:00Z,"
            "tick295: H2 RRF eng 300m class + import 10m + green steel 6m; press concession BA 168-176m path; "
            "FOI L5 ready; spawn rq_287\n"
        )
    out.append(line)
if "rq_287," not in text:
    out.append(
        "rq_287,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after H2 RRF pack). "
        "Prefer before idle; do not idle while public work remains.,,"
        "2026-07-30T10:15:00Z,,Spawned tick295 after H2 RRF + press concession BA; rq_116 SWA deferred\n"
    )
rq_path.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T10:15:00Z,rq_286,295,no,"
    "Scheduler 60s. Next prio5 rq_287; rq_116 SWA deferred. FOI ready. "
    "tick295 H2 RRF 300m eng + press concession BA path.\n",
    encoding="utf-8",
)
print("loop_state ok")

# FOI draft
Path("docs/doge/foi/drafts/gap_h2_rrf_l5_winners.md").write_text(
    """# FOI draft — gap_h2_rrf_l5_winners

**Status:** ready (not sent)  
**Gap ID:** `gap_h2_rrf_l5_winners`  
**Linked:** `cmt_h2_rrf_call_backbone`, `cmt_h2_import_infra_10m`, `cmt_h2_green_steel_electrolyser_6m`  
**Tick:** 295  

Public fill (Kamer 55K2933/016 FOD Economie):

| BA | Role | Engagement | Liquidation path |
|----|------|------------|------------------|
| **42.50.313203** (=31.32.03) | H2 innovation call / backbone | **300m** 2022 + **300m** 2023 (re-inscription class) | 4 / 4 / 24 / 86m 2024–27 |
| **42.50.313204** | H2 import infrastructure | **10m** 2023 | 2 / 3 / 3 / 2m 2023–26 |
| **42.50.313205** | Flexible electrolyser green steel | **6m** 2023 | 1 / 2 / 2 / 1m 2023–26 |
| Pack class | Sum eng 2023 | **~316m** | spend lag |
| Dual | SMR BA 31.32.01 | separate ~100m package | tick287 |

Also same tick: press concession **BA 43.40.31.22.01** liq ~168–176m then 129–138m path (dual bpost FOI already ready).

Residual: named L5 winners + cash outturn + CO2 KPI.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie, K.M.O., Middenstand en Energie — AD Energie / RRF-coördinatie
t.a.v. de dienst openbaarheid van bestuur
https://economie.fgov.be

Betreft: Verzoek om openbaarmaking — federale waterstof RRF-projecten L5 2022–2027 (gap_h2_rrf_l5_winners)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking / afschrift van de hieronder
omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. Lijst van geselecteerde projecten (naam promotor, KBO, projecttitel, toegekend bedrag,
   vastleggings- en vereffeningsjaren) voor basisallocaties:
   - 32.42.50.313203 / 32.42.50.31.32.03 (projectoproep waterstof / backbone)
   - 32.42.50.313204 (waterstof-importinfrastructuur)
   - 32.42.50.313205 (flexibele electrolyser groen staal)
2. Cash-by-year vastleggingen en vereffeningen 2022–2027 per project en per BA,
   met toelichting of de 300 mEUR vastlegging 2022 en 2023 een herschrijving
   (geblokkeerde kredieten) dan wel cumulatieve enveloppe betreft.
3. Selectiebeslissingen / toekenningsbesluiten (of geanonimiseerde samenvatting)
   en eventuele voortgangsrapportage t.a.v. de beoogde CO2-reductie
   (50 000 t/jaar vanaf 2026 in DOC 55 2933/016).

Periode: 1 januari 2022 tot 31 december 2027.

### 2. Context (waarom)

Onderzoek naar overheidsuitgaven (transparantie). Intern pad:
Federal > Energy > H2_RRF. Publieke Kamer-tabellen geven enveloppes tot ~300 mEUR
engagement-class; ontbrekend is de L5-eindbegunstigdenmatrix en effectieve cash-outturn.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail].
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: gap_h2_rrf_l5_winners

Met vriendelijke groet,

[…]
```

**Do not send as agent.** Human send only.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick295 write complete")

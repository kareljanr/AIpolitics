# tick303: Kansspelcommissie KSC 2024 AR — fee-financed gambling regulator
from pathlib import Path
import json

SRC = "src_ksc_jaarverslag_2024"
PDF = "docs/doge/data/raw/ksc_jaarverslag_2024.pdf"
URL = "https://gamingcommission.be/sites/default/files/2025-10/2024-KSC_Jaarverslag-NL_0.pdf"
TICK = "tick303"


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
            f"{SRC},Kansspelcommissie Jaarverslag 2024 budget NBB FTE fee model,"
            f"{URL},Kansspelcommissie / Gaming Commission,2026-07-30,agency,"
            "NBB checks paid 453877.60 EUR 2024; 2025 est 700k = 8.6pct total budget => budget class ~8.14m; "
            "FTE 38.3 eoy2024 vs plan 57; fee-financed by licensees; tick303\n"
        ],
    ),
)

print(
    "entities",
    append_if_missing(
        Path("docs/doge/data/entities.csv"),
        [
            "kansspelcommissie,Kansspelcommissie KSC,Commission des jeux de hasard,"
            "Belgian Gaming Commission gambling regulator,agency,fod_justice,bi,https://www.gamingcommission.be,,,,"
            "Fee-financed by licensees; under Justice tutelage HR; budget class ~8.14m 2025; FTE 38.3 eoy2024 vs plan 57; tick303\n"
        ],
    ),
)

# 700000/0.086
budget_2025 = round(700000 / 0.086)

brows = [
    f"bud_ksc_nbb_checks_2024,kansspelcommissie,2024,453878,,,outturn,{SRC},strong,"
    "NBB credit-register consultation fees paid by KSC 453877.60 EUR 2024 (play-limit uplift system)\n",
    f"bud_ksc_nbb_checks_2025_est,kansspelcommissie,2025,700000,,,estimate,{SRC},strong,"
    "KSC estimate ~700k NBB fees 2025 stated as 8.6pct of total KSC budget\n",
    f"bud_ksc_total_budget_2025_class,kansspelcommissie,2025,{budget_2025},,,estimate,{SRC},medium,"
    "Derived: 700k / 0.086 = total budget class ~8.14m 2025; not a published single table line\n",
    f"bud_ksc_fte_2023,kansspelcommissie,2023,39.3,,,outturn,{SRC},strong,"
    "Secretariat FTE eoy2023 39.3 (AR2024)\n",
    f"bud_ksc_fte_2024,kansspelcommissie,2024,38.3,,,outturn,{SRC},strong,"
    "Secretariat FTE eoy2024 38.3 vs personnel plan 57 VTE 2021-25; later 32.8 at publication\n",
    f"bud_ksc_fte_plan_target,kansspelcommissie,2025,57,,,budgeted,{SRC},strong,"
    "Personnel plan 2021-2025 target 57 FTE not achieved\n",
    f"bud_ksc_play_limit_uplifts_2024,kansspelcommissie,2024,285783,,,outturn,{SRC},strong,"
    "Persons who raised online play limit eoy2024 285783 monthly NBB rechecks required\n",
]
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
        "cmt_ksc_package_2024_25",
        "Kansspelcommissie fee-financed gambling regulator package",
        "kansspelcommissie",
        "Gambling licensees and players (EPIS protection)",
        "Wet 7 mei 1999 kansspelen + Fonds KSC + Justice tutelage HR",
        "1999-05-07",
        2024,
        2025,
        budget_2025,
        {
            "nbb_paid_2024": 453877.6,
            "nbb_est_2025": 700000,
            "nbb_pct_budget_2025": 8.6,
            "total_budget_2025_class_m": round(budget_2025 / 1e6, 2),
            "fte_eoy2023": 39.3,
            "fte_eoy2024": 38.3,
            "fte_plan": 57,
            "fte_publication_later": 32.8,
            "play_limit_uplifts_2024": 285783,
            "financing": "100% license holder retributions (not pure TE appropriation)",
            "note": "Justice PSP afd62 special services 55.3m 2025 is wider perimeter not KSC alone",
            "confidence_budget_total": "medium derived from 8.6pct statement",
        },
        "Safe controlled gambling environment player protection EPIS",
        "Fix NBB check design or charge fund; grant HR autonomy; FOI full P&L",
        "Federal>Justitie>Kansspelcommissie",
        f"{TICK} dual FANC fee-financed regulator model",
    ),
    cmt_row(
        "cmt_ksc_nbb_play_limit_cost",
        "KSC NBB credit-check cost for online play-limit uplifts",
        "kansspelcommissie",
        "Online gamblers requesting limit uplift",
        "KB 19 Jun 2022 NBB Centrale kredieten consultation",
        "2022-06-19",
        2024,
        2025,
        700000,
        {
            "2024_eur": 453877.6,
            "2025_est_eur": 700000,
            "persons_eoy2024": 285783,
            "ksc_critique": "limited protective effect vs cost; prefers EPIS auto-inclusion of defaulters",
            "dual_surendettement": "CSR already in EPIS; debt mediators federal 6.2m separate",
        },
        "Prevent over-indebted players from raising online spend limits",
        "Reform to EPIS or player-borne attest; stop open-ended monthly recheck cost growth",
        "Federal>Justitie>KSC>NBB_checks",
        f"{TICK} dual EPIS and surendettement",
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
        "lb_ksc_budget_8m",
        "Kansspelcommissie total budget class ~8.1m 2025",
        "federal",
        "ops",
        "Federal>Justitie>Kansspelcommissie",
        budget_2025,
        budget_2025,
        "Medium derived: NBB est 700k = 8.6pct total budget => ~8.14m; fee-financed; FTE understaffed 38 vs plan 57",
        "medium",
        SRC,
        "Licensees players",
        "Gambling regulation player protection",
        "Regulator understaffed; NBB cost bite",
        4,
        5.0,
        4,
        4.5,
        "Publish full jaarrekening; reform NBB checks; HR autonomy",
        f"{TICK} dual FANC fee model; Justice afd62 55.3m wider",
    ),
    lb_row(
        "lb_ksc_nbb_454k",
        "KSC NBB play-limit checks 454k 2024 rising to ~700k",
        "federal",
        "ops",
        "Federal>Justitie>KSC>NBB_checks",
        453878,
        700000,
        "Strong AR: 453878 paid 2024; 700k est 2025 = 8.6pct budget; 285783 persons monthly recheck; limited protection critique",
        "strong",
        SRC,
        "Online players raising limits",
        "Block limit uplift for NBB-registered defaulters",
        "Cost grows open-ended; weak vs multi-account",
        6,
        4.0,
        3,
        5.0,
        "EPIS auto-include defaulters or player-borne free attest; fund charge",
        f"{TICK} high absurdity mechanism not size",
    ),
    lb_row(
        "lb_ksc_fte_understaff",
        "KSC secretariat understaffed 38 FTE vs plan 57",
        "federal",
        "ops",
        "Federal>Justitie>KSC>FTE",
        0,
        0,
        "Strong AR: plan 57 VTE; eoy2024 38.3; later 32.8; HR locked to FOD Justice recruitment",
        "strong",
        SRC,
        "Gambling market supervision",
        "Adequate regulatory capacity",
        "Mission-staff gap; sector finance data not published 2024",
        5,
        3.5,
        4,
        4.2,
        "HR autonomy or BOSA selection capacity; fill plan",
        f"{TICK}",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

foi_line = (
    "gap_ksc_accounts_2023_25,Federal>Justitie>Kansspelcommissie>jaarrekening,kansspelcommissie,"
    "Full institutional budget/outturn 2023-2025: personnel ops invest fund balance retributions collected; "
    "reconcile derived ~8.14m 2025 with Justice afdeling 62 special services 55.3m perimeter; NBB fee series,"
    "AR gives NBB cost and FTE strong but not full P&L; fee-financed regulator material dual FANC,"
    "4,Kansspelcommissie / FOD Justitie openbaarheid,,https://www.gamingcommission.be,"
    "docs/doge/foi/drafts/gap_ksc_accounts_2023_25.md,ready,2026-07-30,,,,,,"
    "cmt_ksc_package_2024_25|cmt_ksc_nbb_play_limit_cost,lb_ksc_budget_8m|lb_ksc_nbb_454k,"
    "2026-07-30T14:15:00Z,2026-07-30T14:15:00Z,tick303 draft ready human send\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

rq = Path("docs/doge/data/research_queue.csv")
text = rq.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_294,"):
        line = (
            "rq_294,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after consumer pack). Prefer before idle. "
            "FPS Economy Kamer 55K2933 largely mined — prefer new primary PDFs or FOI-adjacent public fills.,"
            "gap_ksc_accounts_2023_25,2026-07-30T13:45:00Z,2026-07-30T14:15:00Z,"
            "tick303: KSC NBB 454k 2024 / budget class ~8.14m 2025 (8.6pct); FTE 38 vs plan 57; fee-financed; spawn rq_295\n"
        )
    out.append(line)
if "rq_295," not in text:
    out.append(
        "rq_295,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (new agency ARs / Kamer 56 PDFs; AGMJ if extractable). Prefer before idle.,,"
        "2026-07-30T14:15:00Z,,Spawned tick303 after KSC AR2024; rq_116 SWA deferred\n"
    )
rq.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T14:15:00Z,rq_294,303,no,"
    "Scheduler 60s. Next prio5 rq_295; rq_116 SWA deferred. FOI ready. "
    "tick303 KSC fee-financed ~8.1m class + NBB 454k.\n",
    encoding="utf-8",
)
print("loop_state ok")

Path("docs/doge/foi/drafts/gap_ksc_accounts_2023_25.md").write_text(
    f"""# FOI draft — gap_ksc_accounts_2023_25

**Status:** ready (not sent)  
**Gap ID:** `gap_ksc_accounts_2023_25`  
**Linked:** `cmt_ksc_package_2024_25`  
**Tick:** 303  

Public fill (KSC Jaarverslag 2024):

| Item | Value | Confidence |
|------|-------|------------|
| NBB consultation fees paid 2024 | **€453,877.60** | strong |
| NBB estimate 2025 | **~€700,000** | strong (KSC text) |
| Share of total budget 2025 | **8.6%** | strong (KSC text) |
| Implied total budget 2025 | **~€8.14m** | medium (derived) |
| FTE eoy2024 / plan | **38.3 / 57** | strong |
| Financing | License retributions (fee-financed) | strong |
| Play-limit uplifts eoy2024 | **285,783** persons | strong |

Justice PSP afdeling 62 special services **€55.3m** 2025 is a **wider** perimeter — not equal to KSC alone.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Kansspelcommissie / FOD Justitie
t.a.v. de dienst openbaarheid van bestuur
https://www.gamingcommission.be

Betreft: Verzoek om openbaarmaking — KSC begroting en jaarrekening 2023–2025 (gap_ksc_accounts_2023_25)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

1. Volledige begroting en jaarrekening/uitvoering 2023–2025 van de Kansspelcommissie
   (personeel, werking, investeringen, fondsstand, geïnde retributies).
2. Cash-by-year betalingen aan de NBB voor raadpleging Centrale voor kredieten 2022–2025.
3. Reconciliatie met begrotingsafdeling 62 / bijzondere diensten Justitie indien van toepassing.

Periode: 1 januari 2023 tot 31 december 2025.

Dossierreferentie intern: gap_ksc_accounts_2023_25

Met vriendelijke groet,
[…]
```

**Do not send as agent.** Human send only.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick303 write complete", "budget_2025", budget_2025)

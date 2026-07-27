# tick299: surendettement debt mediation + telecom DG admin (Kamer 55K2933/016)
from pathlib import Path
import json

SRC = "src_kamer_55k2933_surendettement_telecom_admin"
PDF = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"
TICK = "tick299"


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
            f"{SRC},Kamer 55K2933/016 FOD Economie surendettement debt mediators + telecom DG BCO admin,"
            f"{PDF},Belgische Kamer van volksvertegenwoordigers,2026-07-30,official_budget,"
            "BA 49.40.12.11.58 debt mediator fees ~6.2m path; staff cells ~0.31m; "
            "BA 59 telecom DG personnel ~1.05m + ops path; dual connectivity 66.2m; tick299\n"
        ],
    ),
)

print(
    "entities",
    append_if_missing(
        Path("docs/doge/data/entities.csv"),
        [
            "fed_surendettement,Federale bestrijding overmatige schuldenlast,Traitement federal du surendettement,"
            "Federal over-indebtedness debt mediation support,programme,fod_economy,bi,https://economie.fgov.be,,,,"
            "Subsidiarity payment of debt mediator fees law 5 Jul 1998; BA ~6.2m/yr + admin cell; fund abolished 2015; tick299\n",
            "dg_telecom,AD Telecom FOD Economie,DG Telecom SPF Economie,"
            "FPS Economy Telecom DG incl Broadband Competence Office,directorate,fod_economy,bi,https://economie.fgov.be,,,,"
            "National broadband plan admin + social telecom tariff automation; dual connectivity subsidies 66.2m; tick299\n",
        ],
    ),
)

brows = []
# debt mediator legal expenses
legal = {
    2021: 6930000,
    2022: 5993000,
    2023: 6193000,
    2024: 6193000,
    2025: 6193000,
    2026: 6193000,
    2027: 6193000,
}
for y, a in legal.items():
    brows.append(
        f"bud_surendettement_mediator_fees_{y},fed_surendettement,{y},{a},,,budgeted,{SRC},strong,"
        "BA 49.40.12.11.58 legal expenses honoraria fees debt mediators eng=liq\n"
    )
# staff cell 11.00.03
for y, a in {2021: 66000, 2022: 186000, 2023: 186000, 2024: 186000, 2025: 186000, 2026: 186000, 2027: 186000}.items():
    brows.append(
        f"bud_surendettement_staff_a_{y},fed_surendettement,{y},{a},,,budgeted,{SRC},strong,"
        "BA 49.40.11.00.03 personnel administrative cell surendettement\n"
    )
# staff cell 11.00.04 (from 2022)
for y, a in {2022: 128000, 2023: 128000, 2024: 128000, 2025: 128000, 2026: 128000, 2027: 128000}.items():
    brows.append(
        f"bud_surendettement_staff_b_{y},fed_surendettement,{y},{a},,,budgeted,{SRC},strong,"
        "BA 49.40.11.00.04 personnel administrative cell surendettement\n"
    )
brows.append(
    f"bud_surendettement_pack_2023,fed_surendettement,2023,6507000,,,budgeted,{SRC},strong,"
    "Sum 2023: mediator fees 6.193 + staff 0.186+0.128 = 6.507m\n"
)
# telecom DG personnel
for y, a in {2022: 738000, 2023: 1048000, 2024: 1048000, 2025: 1048000, 2026: 1048000, 2027: 1048000}.items():
    brows.append(
        f"bud_dg_telecom_personnel_{y},dg_telecom,{y},{a},,,budgeted,{SRC},strong,"
        "BA 59.01.11.00.03 statutory personnel DG Telecom / BCO broadband plan\n"
    )
# telecom ops
telecom_ops = {2022: 1669000, 2023: 1386000, 2024: 886000, 2025: 886000, 2026: 886000, 2027: 886000}
for y, a in telecom_ops.items():
    brows.append(
        f"bud_dg_telecom_ops_{y},dg_telecom,{y},{a},,,budgeted,{SRC},strong,"
        "BA 59.02.12.11.01 functioning DG Telecom broadband plan + social tariff automation class\n"
    )
brows.append(
    f"bud_dg_telecom_admin_pack_2023,dg_telecom,2023,2434000,,,budgeted,{SRC},strong,"
    "Sum 2023 admin: personnel 1.048 + ops 1.386 = 2.434m (excl connectivity subsidies 66.2m)\n"
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
        "cmt_surendettement_mediator_fees",
        "Federal subsidiary payment of debt mediator fees",
        "fed_surendettement",
        "Debt mediators and over-indebted households collective debt settlement",
        "Law 5 Jul 1998 art20 + BA 49.40.12.11.58; fund abolished programme law 20 Dec 2015",
        "1998-07-05",
        2021,
        2027,
        6193000,
        {
            "fees_m": {
                "2021": 6.93,
                "2022": 5.993,
                "2023": 6.193,
                "2024": 6.193,
                "2025": 6.193,
                "2026": 6.193,
                "2027": 6.193,
            },
            "staff_2023_m": 0.314,
            "pack_2023_m": 6.507,
            "note": "Subsidiary intervention in mediator honoraria; dual regional CPAS debt mediation not additive",
        },
        "Ensure access to collective debt settlement via mediator fee support",
        "Core social safety access; FOI case counts unit cost only",
        "Federal>Consumer>surendettement",
        f"{TICK} not pure waste; dual VL/WAL mediation",
    ),
    cmt_row(
        "cmt_dg_telecom_admin_bco",
        "DG Telecom broadband plan admin BCO + social tariff automation",
        "dg_telecom",
        "National Broadband Competence Office and telecom social tariff automation",
        "CM 30 Apr 2021 broadband plan + CM 20 Oct 2021 + BA 59.01.11.00.03 + 59.02.12.11.01",
        "2021-04-30",
        2022,
        2027,
        2434000,
        {
            "personnel_2023_m": 1.048,
            "ops_2023_m": 1.386,
            "ops_path_m": {"2022": 1.669, "2023": 1.386, "2024_27": 0.886},
            "dual_subsidies_eng_2023_m": 66.2,
            "missions": "BCO facilitate broadband deployment; automate social telecom tariff rights",
        },
        "Implement national fixed+mobile broadband plan and automate social tariff rights",
        "Admin overhead on top of 66.2m connectivity subsidies; dual BIPT",
        "Federal>Telecom>DG_admin",
        f"{TICK} dual cmt_telecom_connectivity_66m",
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
        "lb_surendettement_6_2m",
        "Federal debt mediator fees ~6.2m/yr",
        "federal",
        "ops",
        "Federal>Consumer>surendettement",
        6193000,
        6193000,
        "Strong BA 49.40.12.11.58 path 6.93/5.99/6.19m 2021-23 then flat 6.19m; staff +0.31m; dual regional mediation",
        "strong",
        SRC,
        "Debt mediators and over-indebted households",
        "Subsidiary payment mediator fees collective debt settlement",
        "Access to debt procedure; unit cost residual FOI",
        2,
        5.0,
        2,
        3.2,
        "Publish case counts unit cost; dual CPAS map",
        f"{TICK} social access not pure waste",
    ),
    lb_row(
        "lb_dg_telecom_admin_2_4m",
        "DG Telecom admin BCO ~2.4m 2023",
        "federal",
        "ops",
        "Federal>Telecom>DG_admin",
        2434000,
        2434000,
        "Strong personnel 1.05m + ops 1.39m 2023; dual connectivity subsidies 66.2m separate",
        "strong",
        SRC,
        "Broadband plan implementation",
        "BCO + social tariff automation admin",
        "Admin layer on connectivity pack",
        2,
        4.0,
        2,
        2.8,
        "Keep lean; dual BIPT avoid overlap",
        f"{TICK}",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

# light FOI for unit costs / case counts
foi_line = (
    "gap_surendettement_unit_cost,Federal>Consumer>surendettement>unit_cost,fed_surendettement,"
    "Cash outturn 2021-2025 BA 49.40.12.11.58 and number of collective debt files / mediators paid; "
    "average fee per file; dual map with regional CPAS mediation budgets if held,"
    "Annual ~6.2m material access programme; aggregates public unit economics opaque,"
    "3,FOD Economie openbaarheid,,https://economie.fgov.be,"
    "docs/doge/foi/drafts/gap_surendettement_unit_cost.md,ready,2026-07-30,,,,,,"
    "cmt_surendettement_mediator_fees,lb_surendettement_6_2m,"
    "2026-07-30T12:15:00Z,2026-07-30T12:15:00Z,tick299 draft ready low-medium prio\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

# research queue: complete rq_291 early (hole-fill before progress) or use continuous
rq = Path("docs/doge/data/research_queue.csv")
text = rq.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_291,"):
        line = (
            "rq_291,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills after progress@300 (AGMJ wage if public PDF extractable; other FOI-adjacent). "
            "Prefer before idle.,"
            "gap_surendettement_unit_cost,2026-07-30T11:45:00Z,2026-07-30T12:15:00Z,"
            "tick299: surendettement mediator fees ~6.2m + staff 0.31m; DG Telecom admin ~2.4m dual connectivity 66.2m; "
            "progress@300 next; spawn rq_292 after progress\n"
        )
    out.append(line)
if "rq_292," not in text:
    out.append(
        "rq_292,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills after progress@300 (AGMJ wage if public; other FOI-adjacent). Prefer before idle.,,"
        "2026-07-30T12:15:00Z,,Spawned tick299; run after rq_290 progress@300\n"
    )
rq.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T12:15:00Z,rq_291,299,no,"
    "Scheduler 60s. NEXT MANDATORY rq_290 progress@300. Then rq_292. rq_116 SWA deferred. "
    "tick299 surendettement 6.2m + telecom admin 2.4m.\n",
    encoding="utf-8",
)
print("loop_state ok")

Path("docs/doge/foi/drafts/gap_surendettement_unit_cost.md").write_text(
    """# FOI draft — gap_surendettement_unit_cost

**Status:** ready (not sent)  
**Gap ID:** `gap_surendettement_unit_cost`  
**Linked:** `cmt_surendettement_mediator_fees`  
**Tick:** 299  

Public fill (Kamer 55K2933/016):

| BA | Role | Path |
|----|------|------|
| **49.40.12.11.58** | Honoraria/fees debt mediators | **6.93 / 5.99 / 6.19m** then flat **6.19m** |
| **49.40.11.00.03/04** | Admin cell personnel | **~0.31m** path |
| Pack 2023 | Fees + staff | **~6.51m** |

Law 5 Jul 1998; fund abolished 2015; residual federal subsidy of mediator costs.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie
t.a.v. de dienst openbaarheid van bestuur
https://economie.fgov.be

Betreft: Verzoek om openbaarmaking — overmatige schuldenlast unit costs 2021–2025 (gap_surendettement_unit_cost)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking / afschrift van:

1. Cash-outturn 2021–2025 BA 32.49.40.12.11.58 (erelonen schuldbemiddelaars).
2. Aantal dossiers / bemiddelaars per jaar en gemiddelde tussenkomst per dossier.
3. Eventuele splitsing erelonen vs onkosten.

Periode: 1 januari 2021 tot 31 december 2025.

Dossierreferentie intern: gap_surendettement_unit_cost

Met vriendelijke groet,
[…]
```

**Do not send as agent.** Human send only.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick299 write complete")

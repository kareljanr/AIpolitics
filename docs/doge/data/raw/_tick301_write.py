# tick301: Statbel national statistics + FANC financing model note
from pathlib import Path
import json
import csv

SRC = "src_kamer_55k2933_statbel"
SRC_F = "src_fanc_irrs_2023_financing"
PDF = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"
PDF_F = "docs/doge/data/raw/fanc_irrs_2023.pdf"
TICK = "tick301"


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
            f"{SRC},Kamer 55K2933/016 FOD Economie Statbel programme 48 FTE and ops BA,"
            f"{PDF},Belgische Kamer van volksvertegenwoordigers,2026-07-30,official_budget,"
            "Statbel FTE 275.6 01jul2022; functioning ~0.99m; fund contractual 0.84m; "
            "enqueteurs diverse ~1.48m+SSC; statutaire personnel pour memoire FOI; tick301\n",
            f"{SRC_F},IAEA IRRS Belgium 2023 FANC financing model fee-based category C,"
            f"{PDF_F},IAEA IRRS mission Belgium 2023,2026-07-30,agency,"
            "FANC balances annual budget; income taxes+fees+fines; NPP taxes ~75pct income; "
            "phase-out funding risk; dual Bel V hourly billing; no absolute EUR total; tick301\n",
        ],
    ),
)

print(
    "entities",
    append_if_missing(
        Path("docs/doge/data/entities.csv"),
        [
            "statbel,Statbel Algemene Directie Statistiek,Statbel Direction generale Statistique,"
            "Statbel Belgian statistical office,agency,fod_economy,bi,https://statbel.fgov.be,,,,"
            "FPS Economy DG Statistics; FTE 275.6 01jul2022; ops+fund+enqueteurs ~4.4m class 2023 excl statutaire payroll memo; tick301\n",
        ],
    ),
)

# update fanc entity notes if present
ent = Path("docs/doge/data/entities.csv")
et = ent.read_text(encoding="utf-8")
if "fanc," in et and "fee-financed" not in et:
    lines = []
    for line in et.splitlines(keepends=True):
        if line.startswith("fanc,"):
            line = line.rstrip("\n")
            if line.endswith(","):
                line = line + "Category C; 100% fee/tax financed (NPP taxes ~75% income per IRRS 2023); balances budget; dual Bel V; absolute EUR residual FOI; tick301\n"
            else:
                # append to notes field - last field
                parts = line.rsplit(",", 1)
                notes = parts[-1] if len(parts) > 1 else ""
                line = (
                    line.rstrip()
                    + "; Category C fee/tax financed NPP taxes ~75pct IRRS2023; EUR residual FOI; tick301\n"
                )
        lines.append(line)
    ent.write_text("".join(lines), encoding="utf-8")
    print("fanc entity note updated")

brows = []
# functioning
for y, a in {
    2021: 623000,
    2022: 1002000,
    2023: 991000,
    2024: 977000,
    2025: 977000,
    2026: 977000,
    2027: 977000,
}.items():
    brows.append(
        f"bud_statbel_functioning_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.02.12.11.01 permanent non-IT goods/services liq (surveys postage EU-SILC etc)\n"
    )
# indemnities 12.11.99
for y, a in {
    2021: 138000,
    2022: 295000,
    2023: 303000,
    2024: 300000,
    2025: 300000,
    2026: 300000,
    2027: 300000,
}.items():
    brows.append(
        f"bud_statbel_indemnities_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.02.12.11.99 indemnities forfaitaires path\n"
    )
# durable
for y, a in {2021: 30000, 2022: 87000, 2023: 87000, 2024: 87000, 2025: 87000, 2026: 87000, 2027: 87000}.items():
    brows.append(
        f"bud_statbel_durable_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.02.74.22.01 durable movable goods non-IT\n"
    )
# fund contractual
for y, a in {2021: 547000, 2022: 840000, 2023: 840000, 2024: 840000, 2025: 840000, 2026: 840000, 2027: 840000}.items():
    brows.append(
        f"bud_statbel_fund_contractual_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.10.11.00.04 Fonds NIS contractual personnel\n"
    )
# fund enqueteurs + ssc
for y, a in {2022: 182000, 2023: 304000, 2024: 139000, 2025: 139000, 2026: 139000, 2027: 139000}.items():
    brows.append(
        f"bud_statbel_fund_enqueteurs_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.10.11.12.06 Fonds NIS enqueteurs\n"
    )
for y, a in {2022: 28000, 2023: 46000, 2024: 21000, 2025: 21000, 2026: 21000, 2027: 21000}.items():
    brows.append(
        f"bud_statbel_fund_enqueteurs_ssc_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.10.11.20.06 Fonds NIS employer SSC enqueteurs\n"
    )
# diverse enqueteurs main
for y, a in {
    2021: 1382000,
    2022: 1443000,
    2023: 1483000,
    2024: 1435000,
    2025: 1435000,
    2026: 1435000,
    2027: 1435000,
}.items():
    brows.append(
        f"bud_statbel_enqueteurs_diverse_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.12.11.12.06 diverse surveys enqueteurs (LFS EU-SILC HBS etc)\n"
    )
for y, a in {
    2021: 210000,
    2022: 218000,
    2023: 224000,
    2024: 254000,
    2025: 254000,
    2026: 254000,
    2027: 254000,
}.items():
    brows.append(
        f"bud_statbel_enqueteurs_ssc_{y},statbel,{y},{a},,,budgeted,{SRC},strong,"
        "BA 48.12.11.20.06 employer SSC diverse enqueteurs\n"
    )
# pack 2023 without statutaire
brows.append(
    f"bud_statbel_ops_fund_pack_2023,statbel,2023,4366000,,,budgeted,{SRC},strong,"
    "Sum 2023 class excl statutaire payroll memo: functioning 0.991 + indemn 0.303 + durable 0.087 + "
    "fund contract 0.84 + fund enqu 0.35 + diverse enqu+ssc 1.707 + tiny ASBL ~0.01 = ~4.37m\n"
)
brows.append(
    f"bud_statbel_fte_2022,statbel,2022,0,,,outturn,{SRC},strong,"
    "FTE headcount 275.6 as of 01 Jul 2022 (Kamer effectifs table); wage bill residual FOI\n"
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
        "cmt_statbel_package_2022_23",
        "Statbel national statistics office ops+fund+enqueteurs package",
        "statbel",
        "Public statistics users Eurostat government researchers",
        "Public statistics law + FPS Economy DG Statbel programme 48",
        "2022-07-01",
        2021,
        2027,
        4366000,
        {
            "fte_2022_07_01": 275.6,
            "functioning_2023_m": 0.991,
            "indemnities_2023_m": 0.303,
            "fund_contractual_2023_m": 0.84,
            "enqueteurs_pack_2023_m": 1.707,
            "ops_fund_pack_2023_m": 4.37,
            "statutaire_payroll": "pour memoire FOI residual",
            "note": "Core public good; dual regional IIS partners; statutaire wage bill not in BA tables",
        },
        "Produce official statistics for policy Eurostat SDG monitoring",
        "Keep; FOI only statutaire wage bill multi-year",
        "Federal>Statbel>package",
        f"{TICK} dual INR FPB Sciensano surveys",
    ),
    cmt_row(
        "cmt_fanc_fee_financing_model",
        "FANC nuclear regulator fee-financed category C model dual Bel V",
        "fanc",
        "Nuclear licensees Class I primarily NPPs",
        "FANC law + law 16 Mar 1954 category C + IRRS 2023",
        "2001-09-01",
        2023,
        2025,
        0,
        {
            "financing": "100% taxes fees fines allowances (no TE appropriation class)",
            "npp_tax_share_pct": 75,
            "budget_rule": "must balance annual budget",
            "phase_out_risk": "NPP phase-out reduces revenue vs continuing regulatory duties",
            "dual_bel_v": "Bel V TSO hourly billing licensees; turnover 16.0m 2024 mapped tick285",
            "absolute_eur": "Unknown residual FOI gap_fanc_budget_2024_26",
        },
        "Independent nuclear safety regulation self-financed by sector",
        "FOI absolute budget/outturn still; dual Bel V already public",
        "Federal>Nuclear>FANC>financing",
        f"{TICK} strong model no invent euros",
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
        "lb_statbel_ops_4_4m",
        "Statbel ops+fund+enqueteurs ~4.4m 2023 excl statutaire",
        "federal",
        "ops",
        "Federal>Statbel>ops_pack",
        4366000,
        4366000,
        "Strong Kamer: functioning~1.0m + fund contract 0.84m + enqueteurs~1.7m + other; FTE 275.6; statutaire payroll FOI",
        "strong",
        SRC,
        "Public statistics users",
        "Official statistics production",
        "Core public good; wage bill residual",
        1,
        4.0,
        1,
        2.0,
        "Keep; FOI statutaire payroll only",
        f"{TICK} not waste",
    ),
    lb_row(
        "lb_fanc_fee_financed_dual_belv",
        "FANC fee-financed regulator dual Bel V (EUR residual)",
        "federal",
        "ops",
        "Federal>Nuclear>FANC>fee_model",
        0,
        0,
        "Strong IRRS: 100% fee/tax financed; NPP taxes ~75% income; balances budget; dual Bel V 16m; absolute FANC EUR still FOI",
        "strong",
        SRC_F,
        "Nuclear licensees public safety",
        "Independent nuclear safety regulation",
        "Funding model strong; cash total residual",
        3,
        5.0,
        4,
        4.0,
        "FOI jaarrekening budget still gap_fanc_budget; dual Bel V filled",
        f"{TICK} not TE appropriation class",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

# update FOI gap_fanc note if exists
foi = Path("docs/doge/data/foi_queue.csv")
ft = foi.read_text(encoding="utf-8")
if "gap_fanc_budget_2024_26" in ft:
    lines = []
    for line in ft.splitlines(keepends=True):
        if line.startswith("gap_fanc_budget_2024_26,"):
            # update notes at end
            if "tick301" not in line:
                line = line.rstrip("\n") + " | tick301: IRRS fee model 75pct NPP taxes strong; absolute EUR still ready human send\n"
        lines.append(line)
    foi.write_text("".join(lines), encoding="utf-8")
    print("foi fanc note updated")

# Statbel FOI for statutaire payroll
foi_line = (
    "gap_statbel_statutaire_payroll,Federal>Statbel>statutaire_payroll,statbel,"
    "Cash-by-year 2021-2026 BA 48.01.11.00.03/04 statutaire and non-statutaire personnel "
    "and reconcile total institutional budget vs ops+fund+enqueteurs ~4.4m path; FTE series,"
    "FTE 275.6 public; statutaire lines pour memoire in Kamer so full TCO incomplete,"
    "4,FOD Economie / Statbel openbaarheid,,https://statbel.fgov.be,"
    "docs/doge/foi/drafts/gap_statbel_statutaire_payroll.md,ready,2026-07-30,,,,,,"
    "cmt_statbel_package_2022_23,lb_statbel_ops_4_4m,"
    "2026-07-30T13:15:00Z,2026-07-30T13:15:00Z,tick301 draft ready\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

rq = Path("docs/doge/data/research_queue.csv")
text = rq.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_292,"):
        line = (
            "rq_292,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills after progress@300 (AGMJ wage if public; other FOI-adjacent). Prefer before idle.,"
            "gap_statbel_statutaire_payroll,2026-07-30T12:15:00Z,2026-07-30T13:15:00Z,"
            "tick301: Statbel FTE 275.6 + ops/fund/enqueteurs ~4.4m 2023 excl statutaire; FANC fee model 75pct NPP taxes IRRS; "
            "spawn rq_293\n"
        )
    out.append(line)
if "rq_293," not in text:
    out.append(
        "rq_293,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after Statbel/FANC). Prefer before idle.,,"
        "2026-07-30T13:15:00Z,,Spawned tick301 after Statbel FANC financing; rq_116 SWA deferred\n"
    )
rq.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T13:15:00Z,rq_292,301,no,"
    "Scheduler 60s. Next prio5 rq_293; rq_116 SWA deferred. FOI ready. "
    "tick301 Statbel ~4.4m ops pack + FANC fee model.\n",
    encoding="utf-8",
)
print("loop_state ok")

Path("docs/doge/foi/drafts/gap_statbel_statutaire_payroll.md").write_text(
    """# FOI draft — gap_statbel_statutaire_payroll

**Status:** ready (not sent)  
**Gap ID:** `gap_statbel_statutaire_payroll`  
**Linked:** `cmt_statbel_package_2022_23`  
**Tick:** 301  

Public fill (Kamer 55K2933/016 programme 48):

| Item | Value |
|------|-------|
| FTE 01 Jul 2022 | **275.6** |
| Functioning BA 48.02.12.11.01 | **~0.99m** 2023 path |
| Fonds contractual | **0.84m** |
| Enqueteurs diverse + SSC | **~1.71m** 2023 |
| Ops+fund pack class 2023 | **~4.4m** |
| Statutaire BA 48.01.11.00.03/04 | **pour mémoire** — amounts missing |

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie — Statbel / AD Statistiek
t.a.v. de dienst openbaarheid van bestuur
https://statbel.fgov.be

Betreft: Verzoek om openbaarmaking — Statbel statutaire loonmassa 2021–2026 (gap_statbel_statutaire_payroll)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

1. Cash-by-year vastleggingen en vereffeningen 2021–2026 voor BA
   32.48.01.11.00.03 en 32.48.01.11.00.04 (statutair en niet-statutair personeel Statbel).
2. FTE-reeks en totale personeelskost (loonmassa) Statbel 2021–2026.
3. Eventuele reconcilatie met werkings- en enquêteursbudgetten.

Periode: 1 januari 2021 tot 31 december 2026.

Dossierreferentie intern: gap_statbel_statutaire_payroll

Met vriendelijke groet,
[…]
```

**Do not send as agent.** Human send only.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick301 write complete")

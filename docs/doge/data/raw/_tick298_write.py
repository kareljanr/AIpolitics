# tick298: quality infrastructure BELAC + NBN + EMPIR/EPM (Kamer 55K2933/016)
from pathlib import Path
import json

SRC = "src_kamer_55k2933_belac_nbn_metrology"
PDF = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"
TICK = "tick298"


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
            f"{SRC},Kamer 55K2933/016 FOD Economie BELAC NBN normalisation EMPIR EPM,"
            f"{PDF},Belgische Kamer van volksvertegenwoordigers,2026-07-30,official_budget,"
            "BELAC pers 0.88m + ops 2.72m; NBN subside ~2.07m; Antennes-Normes 4.46m; "
            "octrooicellen 0.54m; EMPIR 0.12m EPM 0.20m; pack ~11m class; tick298\n"
        ],
    ),
)

print(
    "entities",
    append_if_missing(
        Path("docs/doge/data/entities.csv"),
        [
            "belac,BELAC Belgische Accreditatie-instelling,BELAC Systeme belge d accreditation,"
            "BELAC Belgian Accreditation Body,agency,fod_economy,bi,https://economie.fgov.be/nl/themas/kwaliteit-veiligheid/accreditatie-belac,,,,"
            "National accreditation; BA personnel ~0.88m + functioning ~2.72m; fee-funded staff expansion; tick298\n",
            "nbn,NBN Bureau voor Normalisatie,NBN Bureau de Normalisation,"
            "NBN Belgian Bureau for Standardisation,agency,fod_economy,bi,https://www.nbn.be,,,,"
            "National standards body; federal subside ~2.07m + prenorm 4.46m via collective centres; tick298\n",
        ],
    ),
)

brows = []
# BELAC statutory personnel
for y, a in {2021: 738000, 2022: 880000, 2023: 880000, 2024: 880000, 2025: 880000, 2026: 880000, 2027: 880000}.items():
    brows.append(
        f"bud_belac_personnel_statut_{y},belac,{y},{a},,,budgeted,{SRC},strong,"
        "BA 46.10.11.00.03 BELAC statutory personnel 13 FTE class eng=liq\n"
    )
# BELAC functioning (auditors IT etc)
for y, a in {
    2021: 2388000,
    2022: 2495000,
    2023: 2723000,
    2024: 2723000,
    2025: 2723000,
    2026: 2723000,
    2027: 2723000,
}.items():
    brows.append(
        f"bud_belac_functioning_{y},belac,{y},{a},,,budgeted,{SRC},strong,"
        "BA 46.10.12.11.50 BELAC functioning external auditors interlab IT e-gov\n"
    )
# pack BELAC 2023
brows.append(
    f"bud_belac_pack_2023,belac,2023,3603000,,,budgeted,{SRC},strong,"
    "Sum 2023: personnel 0.88 + functioning 2.723 = 3.603m (excludes fee-funded fund staff)\n"
)
# Antennes-Normes / prenorm
for y, a in {
    2021: 4432000,  # liq
    2022: 4462000,
    2023: 4462000,
    2024: 4462000,
    2025: 4462000,
    2026: 4462000,
    2027: 4462000,
}.items():
    brows.append(
        f"bud_nbn_antennes_prenorm_{y},nbn,{y},{a},,,budgeted,{SRC},strong,"
        "BA 46.50.41.40.30 Normalisation prenorm studies Antennes-Normes via collective centres; eng 3.964m 2021 then 4.462m\n"
    )
# patent cells
for y in range(2021, 2028):
    a = 494000 if y == 2021 else 541000
    brows.append(
        f"bud_patent_cells_{y},fod_economy,{y},{a},,,budgeted,{SRC},strong,"
        "BA 46.50.31.32.32 Normalisation cellules brevets/octrooicellen SME innovation\n"
    )
# NBN subside
nbn_sub = {
    2021: 1915000,
    2022: 2027000,
    2023: 2074000,
    2024: 2049000,
    2025: 2050000,
    2026: 2051000,
    2027: 2052000,
}
for y, a in nbn_sub.items():
    brows.append(
        f"bud_nbn_subside_{y},nbn,{y},{a},,,budgeted,{SRC},strong,"
        "BA 46.50.41.40.31 Subside NBN general-interest missions functioning\n"
    )
# EMPIR EPM
for y in range(2021, 2028):
    brows.append(
        f"bud_empir_contrib_{y},fod_economy,{y},120000,,,budgeted,{SRC},strong,"
        "Belgian annual EMPIR metrology programme contribution 120k\n"
    )
    brows.append(
        f"bud_epm_contrib_{y},fod_economy,{y},200000,,,budgeted,{SRC},strong,"
        "Belgian annual EPM European Partnership on Metrology contribution 200k\n"
    )
# pack 2023 quality infra
brows.append(
    f"bud_quality_infra_pack_2023,fod_economy,2023,10780000,,,budgeted,{SRC},strong,"
    "Sum class 2023: BELAC 3.603 + Antennes 4.462 + patent 0.541 + NBN 2.074 + EMPIR 0.12 + EPM 0.20 = ~11.0m\n"
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
        "cmt_belac_package",
        "BELAC accreditation body federal budget package",
        "belac",
        "Accredited labs inspection certification bodies export market access",
        "Belgian accreditation system + BA 46.10.11.00.03 + 46.10.12.11.50",
        "2021-01-01",
        2021,
        2027,
        3603000,
        {
            "personnel_statut_2023_m": 0.88,
            "functioning_2023_m": 2.723,
            "pack_2023_m": 3.603,
            "fte_statut_class": 13,
            "fee_fund_staff": "additional staff financed by accreditation fees not in BA table",
            "note": "Core market infrastructure; fee-funded expansion separate",
        },
        "National accreditation for product/service reliability and export acceptance",
        "Keep; dual EU EA recognition; publish fee vs budget split",
        "Federal>Quality>BELAC",
        f"{TICK} structural not pure waste",
    ),
    cmt_row(
        "cmt_nbn_normalisation_pack",
        "NBN standardisation federal subsidy + prenorm antennas pack",
        "nbn",
        "NBN collective centres SMEs prenorm patent cells",
        "BA 46.50.41.40.30 Antennes-Normes + 46.50.41.40.31 NBN subside + 46.50.31.32.32 patent cells",
        "2020-01-01",
        2021,
        2027,
        7077000,
        {
            "antennes_2023_m": 4.462,
            "nbn_subside_2023_m": 2.074,
            "patent_cells_2023_m": 0.541,
            "pack_2023_m": 7.077,
            "transfer_note": "NBN subside -49k for seconded staff control at FPS Economy",
        },
        "National standardisation general-interest missions and SME prenorm support",
        "Keep core; L5 collective centre grants FOI if needed",
        "Federal>Quality>NBN_normalisation",
        f"{TICK}",
    ),
    cmt_row(
        "cmt_empir_epm_metrology",
        "Belgian EMPIR + EPM European metrology contributions",
        "fod_economy",
        "European metrology research network",
        "Art 185 TFEU EMPIR + European Partnership on Metrology EPM",
        "2009-09-16",
        2021,
        2027,
        320000,
        {"empir_k": 120, "epm_k": 200, "annual_m": 0.32},
        "Belgian participation in EU metrology research programmes",
        "Keep membership minimums",
        "Federal>Quality>metrology_EU",
        f"{TICK}",
    ),
    cmt_row(
        "cmt_quality_infra_pack_11m",
        "Federal quality infrastructure pack BELAC+NBN+metrology ~11m 2023",
        "fod_economy",
        "Accreditation standardisation metrology stack",
        "FPS Economy quality programmes 46/10 + 46/50 + EMPIR/EPM",
        "2021-01-01",
        2023,
        2023,
        11000000,
        {
            "belac_m": 3.603,
            "nbn_pack_m": 7.077,
            "empir_epm_m": 0.32,
            "sum_m": 11.0,
            "note": "Order-of-magnitude pack class; not double-count fee-funded BELAC staff",
        },
        "Market quality infrastructure dual accreditation and standards",
        "Core institutions; FOI only L5 NBN collective grants if material",
        "Federal>Quality>infra_pack",
        f"{TICK} dual BMA competition authority separate",
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
        "lb_belac_3_6m",
        "BELAC accreditation budget ~3.6m 2023",
        "federal",
        "ops",
        "Federal>Quality>BELAC",
        3603000,
        3603000,
        "Strong BA: personnel 0.88m + functioning 2.72m; fee-funded staff expansion off-table; core market infra",
        "strong",
        SRC,
        "Accredited operators exporters",
        "National accreditation system",
        "Structural institution",
        1,
        4.0,
        1,
        2.0,
        "Keep; publish fee vs budget dual",
        f"{TICK} not waste",
    ),
    lb_row(
        "lb_nbn_pack_7m",
        "NBN + prenorm antennas + patent cells ~7.1m 2023",
        "federal",
        "ops",
        "Federal>Quality>NBN_pack",
        7077000,
        7077000,
        "Strong: Antennes-Normes 4.46m + NBN subside 2.07m + patent cells 0.54m",
        "strong",
        SRC,
        "SMEs collective centres NBN",
        "Standardisation and prenorm SME support",
        "Structural; L5 centres residual",
        2,
        5.0,
        2,
        3.2,
        "Optional FOI collective centre L5",
        f"{TICK}",
    ),
    lb_row(
        "lb_quality_infra_11m",
        "Federal quality infra pack ~11m 2023",
        "federal",
        "ops",
        "Federal>Quality>infra_pack",
        11000000,
        11000000,
        "Strong sum BELAC 3.6 + NBN pack 7.1 + EMPIR/EPM 0.32 ≈ 11.0m class",
        "strong",
        SRC,
        "Market quality stack",
        "Accreditation standards metrology",
        "Core infrastructure dual BMA",
        2,
        5.5,
        2,
        3.5,
        "Keep; dual competition authority separate",
        f"{TICK}",
    ),
    lb_row(
        "lb_empir_epm_0_32m",
        "EMPIR+EPM metrology contributions 0.32m/yr",
        "federal",
        "ops",
        "Federal>Quality>metrology_EU",
        320000,
        320000,
        "Strong: EMPIR 120k + EPM 200k annual Belgian participation",
        "strong",
        SRC,
        "EU metrology network",
        "European metrology research participation",
        "Small membership",
        1,
        1.5,
        1,
        1.2,
        "Keep minimums",
        f"{TICK}",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

# Optional light FOI for NBN collective L5 only if material - prenorm 4.46m has L5 opacity
foi_line = (
    "gap_nbn_antennes_l5,Federal>Quality>NBN>antennes_prenorm_L5,nbn,"
    "Named collective centres / Antennes-Normes recipients with EUR 2022-2026 under BA 46.50.41.40.30 "
    "and patent-cell beneficiaries under 46.50.31.32.32; reconcile NBN subside 46.50.41.40.31 outturn,"
    "Prenorm+antenna pack ~4.5m + patent 0.54m + NBN 2.07m; end-receiver L5 not in Kamer tables,"
    "3,FOD Economie / NBN openbaarheid,,https://www.nbn.be,"
    "docs/doge/foi/drafts/gap_nbn_antennes_l5.md,ready,2026-07-30,,,,,,"
    "cmt_nbn_normalisation_pack,lb_nbn_pack_7m,"
    "2026-07-30T11:45:00Z,2026-07-30T11:45:00Z,tick298 draft ready low prio\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

# Note AGMJ: chiffres clés portal has interactive budget dashboard — no machine-readable EUR extracted this tick
# FOI gap_fwb_mdj_personnel_total already ready

rq = Path("docs/doge/data/research_queue.csv")
text = rq.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_289,"):
        line = (
            "rq_289,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after ETF deepen). "
            "Prefer before idle; do not idle while public work remains. Note progress@300 soon.,"
            "gap_nbn_antennes_l5,2026-07-30T11:15:00Z,2026-07-30T11:45:00Z,"
            "tick298: quality infra pack ~11m BELAC 3.6 NBN pack 7.1 EMPIR/EPM 0.32; AGMJ chiffres cles portal no extractable EUR; "
            "spawn rq_290 progress@300; FOI NBN L5 low prio\n"
        )
    out.append(line)
if "rq_290," not in text:
    out.append(
        "rq_290,Mandatory progress@300 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
        "When ticks_completed hits 300: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
        "and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
        "2026-07-30T11:45:00Z,,Spawned tick298; do at tick 300\n"
    )
if "rq_291," not in text:
    out.append(
        "rq_291,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills after progress@300 (AGMJ wage if public PDF extractable; other FOI-adjacent). "
        "Prefer before idle.,,"
        "2026-07-30T11:45:00Z,,Spawned tick298 after quality infra; after rq_290\n"
    )
rq.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T11:45:00Z,rq_289,298,no,"
    "Scheduler 60s. Next: progress rq_290 @300 then rq_291. rq_116 SWA deferred. "
    "tick298 quality infra ~11m BELAC+NBN+metrology.\n",
    encoding="utf-8",
)
print("loop_state ok")

Path("docs/doge/foi/drafts/gap_nbn_antennes_l5.md").write_text(
    """# FOI draft — gap_nbn_antennes_l5

**Status:** ready (not sent) — **low priority**  
**Gap ID:** `gap_nbn_antennes_l5`  
**Linked:** `cmt_nbn_normalisation_pack`  
**Tick:** 298  

Public fill (Kamer 55K2933/016):

| BA | Role | ~2023 |
|----|------|-------|
| 46.50.41.40.30 | Antennes-Normes / prenorm studies | **4.462m** |
| 46.50.31.32.32 | Cellules brevets / octrooicellen | **0.541m** |
| 46.50.41.40.31 | Subside NBN missions d'intérêt général | **2.074m** |
| Dual | BELAC pack | **~3.6m** (separate) |

Residual: named collective centres and patent-cell amounts.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie / NBN
t.a.v. de dienst openbaarheid van bestuur
https://economie.fgov.be / https://www.nbn.be

Betreft: Verzoek om openbaarmaking — Antennes-Normes en NBN-subsidie L5 (gap_nbn_antennes_l5)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking / afschrift van de hieronder
omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

1. Lijst van begunstigde collectieve centra / Antennes-Normes met bedragen
   2022–2026 op basisallocatie 32.46.50.41.40.30.
2. Begunstigden en bedragen octrooicellen (BA 32.46.50.31.32.32) 2022–2026.
3. Cash-outturn van de NBN-werkingssubsidie (BA 32.46.50.41.40.31) 2022–2026.

Periode: 1 januari 2022 tot 31 december 2026.

### 2. Context

Transparantie overheidsuitgaven. Publieke Kamer-tabellen geven enveloppes;
ontbrekend is de L5-eindbegunstigdenmatrix.

### 3. Vorm

Bij voorkeur CSV/PDF per e-mail naar [e-mail].

### 4. Identiteit

Dossierreferentie intern: gap_nbn_antennes_l5

Met vriendelijke groet,
[…]
```

**Do not send as agent.** Human send only. Low priority vs larger FOI stack.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick298 write complete")

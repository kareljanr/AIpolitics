# tick302: FPS Economy consumer protection external subsidies pack
from pathlib import Path
import json

SRC = "src_kamer_55k2933_consumer_protection"
PDF = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"
TICK = "tick302"


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
            f"{SRC},Kamer 55K2933/016 FOD Economie consumer protection programme 49 external subsidies,"
            f"{PDF},Belgische Kamer van volksvertegenwoordigers,2026-07-30,official_budget,"
            "AB-REOC 506k; CEC 162k; Ombudsdienst Consument ~395k; patient orgs 38k; ECC ODR 50k; "
            "CLV travel 15k; pack ~1.17m 2023; dual surendettement 6.2m; tick302\n"
        ],
    ),
)

print(
    "entities",
    append_if_missing(
        Path("docs/doge/data/entities.csv"),
        [
            "ab_reoc,BV-OECO Vereniging Onderzoek Expertise Consumentenorganisaties,AB-REOC Association belge recherche expertise organisations consommateurs,"
            "AB-REOC Belgian consumer organisations research body,asbl,fod_economy,bi,,,,,"
            "Technical legal support to consumer orgs; federal subsidy flat 506k; founded Jun2015; tick302\n",
            "cec_belgium,Europees Centrum voor de Consument Belgie,Centre Europeen des Consommateurs Belgique,"
            "European Consumer Centre Belgium ECC,asbl,fod_economy,bi,https://www.eccbelgie.be,,,,"
            "Cross-border consumer advice ECC-Net; federal 162k + EC 50pct co-finance; ODR contact point separate ~50k; tick302\n",
            "ombuds_consumer,Ombudsdienst voor de Consument,Service de mediation pour le Consommateur,"
            "Consumer Mediation Service residual ADR,agency,fod_economy,bi,https://www.consumerombudsman.be,,,,"
            "Single desk residual consumer ADR; federal subside ~388-395k; dual sector ombuds post telecom energy rail bank; tick302\n",
        ],
    ),
)

brows = []
# AB-REOC 506k flat
for y in range(2021, 2028):
    brows.append(
        f"bud_ab_reoc_{y},ab_reoc,{y},506000,,,budgeted,{SRC},strong,"
        "BA 49.10.33.00.02 AB-REOC/BV-OECO consumer orgs technical legal support flat 506k eng=liq\n"
    )
# CEC main 162k
for y in range(2021, 2028):
    brows.append(
        f"bud_cec_belgium_{y},cec_belgium,{y},162000,,,budgeted,{SRC},strong,"
        "BA 49.30.33.00.30 European Consumer Centre Belgium; 50pct EC co-finance class\n"
    )
# Ombuds consumer
for y, a in {
    2021: 368000,
    2022: 386000,
    2023: 395000,
    2024: 388000,
    2025: 388000,
    2026: 388000,
    2027: 388000,
}.items():
    brows.append(
        f"bud_ombuds_consumer_{y},ombuds_consumer,{y},{a},,,budgeted,{SRC},strong,"
        "BA 49.10.41.40.01 Service mediation / Ombudsdienst voor de Consument residual ADR\n"
    )
# patient orgs insurance bureau
for y in range(2021, 2028):
    brows.append(
        f"bud_patient_orgs_insurance_bureau_{y},fod_economy,{y},38000,,,budgeted,{SRC},strong,"
        "BA 49.02.33.00.01 LUSS+Vlaams Patiëntenplatform doctors in insurance tariff follow-up bureau\n"
    )
# ECC ODR point
for y, a in {
    2021: 52000,
    2022: 51000,
    2023: 50000,
    2024: 49000,
    2025: 49000,
    2026: 49000,
    2027: 49000,
}.items():
    brows.append(
        f"bud_ecc_odr_contact_{y},cec_belgium,{y},{a},,,budgeted,{SRC},strong,"
        "BA 49.02.33.00.02 ECC ODR online dispute resolution contact point (OIPC host)\n"
    )
# travel disputes
for y in range(2021, 2028):
    brows.append(
        f"bud_clv_travel_disputes_{y},fod_economy,{y},15000,,,budgeted,{SRC},strong,"
        "BA 49.10.33.00.03 Commission Litiges Voyages / Geschillencommissie Reizen 15k\n"
    )
# pack 2023
brows.append(
    f"bud_consumer_protection_external_pack_2023,fod_economy,2023,1166000,,,budgeted,{SRC},strong,"
    "Sum 2023: AB-REOC 506 + CEC 162 + ombuds 395 + patients 38 + ODR 50 + CLV 15 = 1.166m; dual surendettement 6.2m separate\n"
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
        "cmt_consumer_protection_external_pack",
        "FPS Economy consumer protection external subsidies pack",
        "fod_economy",
        "AB-REOC CEC Ombudsdienst patient orgs CLV",
        "Consumer ADR directives + insurance residual balance law + BA programme 49",
        "2015-01-01",
        2021,
        2027,
        1166000,
        {
            "ab_reoc_k": 506,
            "cec_k": 162,
            "ombuds_2023_k": 395,
            "patients_k": 38,
            "odr_2023_k": 50,
            "clv_k": 15,
            "pack_2023_m": 1.166,
            "dual_surendettement_m": 6.2,
            "note": "Named L5 orgs strong; dual debt mediation separate programme 49/4",
        },
        "Consumer information ADR support and residual dispute mediation",
        "Keep core ADR; dual sector ombuds avoid overlap; low FOI priority",
        "Federal>Consumer>external_pack",
        f"{TICK} dual surendettement",
    ),
    cmt_row(
        "cmt_ab_reoc_506k",
        "AB-REOC BV-OECO consumer organisations research support",
        "ab_reoc",
        "Belgian consumer organisations technical legal aid",
        "ASBL Jun2015 + BA 49.10.33.00.02",
        "2015-06-01",
        2021,
        2027,
        506000,
        {"annual_k": 506, "flat": True},
        "Technical legal support to consumer organisations",
        "Publish annual activity KPIs",
        "Federal>Consumer>AB_REOC",
        f"{TICK}",
    ),
    cmt_row(
        "cmt_ombuds_consumer_path",
        "Consumer Mediation Service residual ADR federal subsidy",
        "ombuds_consumer",
        "Consumers residual disputes without sector ombuds",
        "EU ADR/ODR rules + BA 49.10.41.40.01",
        "2015-01-01",
        2021,
        2027,
        395000,
        {
            "2021_k": 368,
            "2022_k": 386,
            "2023_k": 395,
            "2024_27_k": 388,
            "role": "single desk + residual ADR; board of sector mediators",
        },
        "Residual consumer dispute mediation and information desk",
        "Dual sector ombuds post telecom energy rail bank insurance",
        "Federal>Consumer>Ombuds",
        f"{TICK}",
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
        "lb_consumer_external_pack_1_2m",
        "Consumer protection external pack ~1.17m 2023",
        "federal",
        "ops",
        "Federal>Consumer>external_pack",
        1166000,
        1166000,
        "Strong sum AB-REOC 506k + CEC 162k + ombuds 395k + patients 38k + ODR 50k + CLV 15k; dual surendettement 6.2m",
        "strong",
        SRC,
        "Consumers ADR orgs",
        "Consumer information and ADR infrastructure",
        "Named L5 strong",
        2,
        3.5,
        2,
        2.7,
        "Keep ADR core; dual sector ombuds",
        f"{TICK}",
    ),
    lb_row(
        "lb_ab_reoc_506k",
        "AB-REOC consumer orgs support 506k/yr",
        "federal",
        "ops",
        "Federal>Consumer>AB_REOC",
        506000,
        506000,
        "Strong flat BA 506k to AB-REOC/BV-OECO technical legal support consumer orgs",
        "strong",
        SRC,
        "Consumer organisations",
        "Technical legal aid consumer movement",
        "Flat multi-year",
        2,
        2.5,
        2,
        2.3,
        "Publish activity report KPIs",
        f"{TICK}",
    ),
    lb_row(
        "lb_ombuds_consumer_395k",
        "Ombudsdienst Consument ~395k 2023",
        "federal",
        "ops",
        "Federal>Consumer>Ombuds",
        395000,
        395000,
        "Strong BA residual ADR single desk ~368-395k path; dual sector ombuds",
        "strong",
        SRC,
        "Consumers residual disputes",
        "Residual consumer mediation",
        "Core ADR infrastructure",
        1,
        2.5,
        1,
        1.9,
        "Keep; dual sector map",
        f"{TICK}",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

# low FOI if needed - mostly complete; optional CEC EC co-finance outturn
foi_line = (
    "gap_consumer_adr_outturn,Federal>Consumer>ADR>cash_outturn,fod_economy,"
    "Cash outturn 2021-2025 for BA programme 49 external lines (AB-REOC CEC ombuds ODR CLV patients) "
    "vs budget tables; CEC EC co-finance amount; Ombudsdienst case volumes,"
    "Budget tables strong ~1.17m; outturn and performance residual low material,"
    "2,FOD Economie consumentenbescherming,,https://economie.fgov.be,"
    "docs/doge/foi/drafts/gap_consumer_adr_outturn.md,ready,2026-07-30,,,,,,"
    "cmt_consumer_protection_external_pack,lb_consumer_external_pack_1_2m,"
    "2026-07-30T13:45:00Z,2026-07-30T13:45:00Z,tick302 draft ready low prio\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

rq = Path("docs/doge/data/research_queue.csv")
text = rq.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_293,"):
        line = (
            "rq_293,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after Statbel/FANC). Prefer before idle.,"
            "gap_consumer_adr_outturn,2026-07-30T13:15:00Z,2026-07-30T13:45:00Z,"
            "tick302: consumer protection external pack ~1.17m (AB-REOC 506k CEC 162k ombuds 395k); dual surendettement; "
            "spawn rq_294\n"
        )
    out.append(line)
if "rq_294," not in text:
    out.append(
        "rq_294,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after consumer pack). Prefer before idle. "
        "FPS Economy Kamer 55K2933 largely mined — prefer new primary PDFs or FOI-adjacent public fills.,,"
        "2026-07-30T13:45:00Z,,Spawned tick302; rq_116 SWA deferred; Economy stream thinning\n"
    )
rq.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T13:45:00Z,rq_293,302,no,"
    "Scheduler 60s. Next prio5 rq_294; rq_116 SWA deferred. FOI ready. "
    "tick302 consumer external pack ~1.17m. Economy stream thinning.\n",
    encoding="utf-8",
)
print("loop_state ok")

Path("docs/doge/foi/drafts/gap_consumer_adr_outturn.md").write_text(
    """# FOI draft — gap_consumer_adr_outturn

**Status:** ready (not sent) — **low priority**  
**Gap ID:** `gap_consumer_adr_outturn`  
**Linked:** `cmt_consumer_protection_external_pack`  
**Tick:** 302  

Public fill (Kamer 55K2933/016 programme 49):

| Recipient | BA | ~2023 |
|-----------|-----|------:|
| AB-REOC / BV-OECO | 49.10.33.00.02 | **506k** |
| CEC Belgium | 49.30.33.00.30 | **162k** (+ EC 50%) |
| Ombudsdienst Consument | 49.10.41.40.01 | **395k** |
| Patients LUSS+VPP | 49.02.33.00.01 | **38k** |
| ECC ODR contact | 49.02.33.00.02 | **50k** |
| CLV travel disputes | 49.10.33.00.03 | **15k** |
| **Pack** | | **~1.17m** |

Dual: surendettement mediator fees **~6.2m** (tick299).

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie — consumentenbescherming
t.a.v. de dienst openbaarheid van bestuur
https://economie.fgov.be

Betreft: Verzoek om openbaarmaking — consumenten ADR-subsidies outturn 2021–2025 (gap_consumer_adr_outturn)

Geachte,

Op grond van de wet van 11 april 1994 dien ik een verzoek in tot openbaarmaking van:

1. Cash-outturn 2021–2025 voor de basisallocaties van programma 49 externe toelagen
   (o.a. 32.49.10.33.00.02, 32.49.30.33.00.30, 32.49.10.41.40.01, 32.49.02.33.00.01/02, 32.49.10.33.00.03).
2. Voor CEC: bedrag EU-cofinanciering naast de federale 162k.
3. Voor Ombudsdienst Consument: aantal dossiers per jaar indien beschikbaar.

Dossierreferentie intern: gap_consumer_adr_outturn

Met vriendelijke groet,
[…]
```

**Do not send as agent.** Low priority.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick302 write complete")

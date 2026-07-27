# tick 336 — S4Policy 34.26m + PROBA-3 BE 63.4m dual Belspo
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T06:45:00Z"

with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_belspo_s4policy_call_2024_25,BELSPO S4Policy call 2024-2025 Information File Policy Driven budget,"
        "https://www.belspo.be/belspo/P4Science-S4Policy/call/S4Policy_2024/S4Policy_InfoFile_v6.pdf,"
        "BELSPO,2026-07-31,official_call,"
        "Strong: Policy Driven 4-call total 34.25616m; call1 6.15511 call2 7.9517 call3 8.79127 call4 11.35808; "
        "BELSPO max 90pct dept min 10pct cofund; dual federal depts+unis; tick336\n"
    )
    f.write(
        "src_belspo_proba3_ar2024,BELSPO Jaarverslag 2024 PROBA-3 space formation flying BE contribution,"
        "https://www.belspo.be/belspo/organisation/report-2024/doc/research/space_PROBA-3.pdf,"
        "BELSPO,2026-07-31,official_annual_report,"
        "Strong: PROBA-3 total cost 166m of which Belgium 63.4m via BELSPO GSTP+PRODEX; launch 4Dec2024; "
        "dual ESA industrial ROB CSL; tick336\n"
    )

with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "s4policy_belspo,S4Policy Science for Policy BELSPO,S4Policy programme BELSPO,"
        "Federal policy-driven research co-funded by BELSPO and federal departments,"
        "programme,belspo,bi,https://www.belspo.be/belspo/P4Science-S4Policy/,,,,"
        "Policy Driven 34.26m over 4 calls 2024-31; dual P4Science FSI; tick336\n"
    )
    f.write(
        "proba3_be,PROBA-3 Belgian ESA formation-flying mission,PROBA-3 mission BELSPO,"
        "ESA dual-satellite solar coronagraph formation flying with major Belgian contribution,"
        "programme,esa_be_contrib,bi,https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Proba_Missions,,,,"
        "Total 166m BE 63.4m BELSPO GSTP+PRODEX; launch Dec2024; dual industry science; tick336\n"
    )

bud = [
    "bud_s4policy_total_4calls,s4policy_belspo,2031,34256160,,,budgeted,src_belspo_s4policy_call_2024_25,strong,S4Policy Policy Driven indicative total 4 calls 34.25616m 2024-2031",
    "bud_s4policy_call1_2024_25,s4policy_belspo,2025,6155110,,,budgeted,src_belspo_s4policy_call_2024_25,strong,S4Policy Call1 Policy Driven 2024-2025 6.15511m",
    "bud_s4policy_call2_2026_27,s4policy_belspo,2027,7951700,,,budgeted,src_belspo_s4policy_call_2024_25,strong,S4Policy Call2 Policy Driven 2026-2027 7.9517m",
    "bud_s4policy_call3_2028_29,s4policy_belspo,2029,8791270,,,budgeted,src_belspo_s4policy_call_2024_25,strong,S4Policy Call3 Policy Driven 2028-2029 8.79127m",
    "bud_s4policy_call4_2030_31,s4policy_belspo,2031,11358080,,,budgeted,src_belspo_s4policy_call_2024_25,strong,S4Policy Call4 Policy Driven 2030-2031 11.35808m",
    "bud_proba3_total_mission,proba3_be,2024,166000000,,,budgeted,src_belspo_proba3_ar2024,strong,PROBA-3 total mission cost 166m euro ESA/partners",
    "bud_proba3_be_contrib,proba3_be,2024,63400000,,,budgeted,src_belspo_proba3_ar2024,strong,Belgium contribution 63.4m via BELSPO GSTP+PRODEX programmes",
]
with open(root / "budgets.csv", "a", encoding="utf-8") as f:
    f.write("\n".join(bud) + "\n")


def cmt(cid, title, eid, ben, legal, ddate, sy, ey, tot, cash, rem, url, goal, cut, src, conf, path, notes):
    cf = json.dumps(cash, separators=(",", ":")).replace('"', '""')
    rem_s = "" if rem is None else str(rem)
    return (
        f'{cid},{title},{eid},{ben},{legal},{ddate},{sy},{ey},{tot},'
        f'"{cf}",{rem_s},active,{url},{goal},{cut},{src},{conf},{path},{notes}\n'
    )


with open(root / "commitments.csv", "a", encoding="utf-8") as f:
    f.write(
        cmt(
            "cmt_s4policy_policy_driven_2024_31",
            "S4Policy Policy Driven research multi-call envelope 2024-2031",
            "s4policy_belspo",
            "Belgian research community universities FSI public centres + federal departments",
            "CM programme Science for Policy successor BRAIN-be policy pillar",
            "2024-06-25",
            2024,
            2031,
            34256160,
            {
                "total_4calls_m": 34.25616,
                "call1_m": 6.15511,
                "call2_m": 7.9517,
                "call3_m": 8.79127,
                "call4_m": 11.35808,
                "belspo_max_share_pct": 0.90,
                "dept_min_cofund_pct": 0.10,
                "themes": "Digital StrategicAutonomy InclusionHealth GreenSocietal",
                "note": "Indicative programme budget; dual P4Science FSI capacity; L5 awards residual FOI",
            },
            34256160,
            "https://www.belspo.be/belspo/P4Science-S4Policy/call/S4Policy_2024/S4Policy_InfoFile_v6.pdf",
            "Scientific evidence for federal policies co-created with departments",
            "Publish awarded project list EUR per call; dual unit-cost vs P4Science",
            "src_belspo_s4policy_call_2024_25",
            "strong",
            "Federal>BELSPO>S4Policy",
            "tick336: 34.26m Policy Driven dual depts+research",
        )
    )
    f.write(
        cmt(
            "cmt_proba3_be_63_4m",
            "PROBA-3 Belgian ESA contribution dual space industry science",
            "proba3_be",
            "Redwire SPACEBEL CSL ROB industry consortium ESA",
            "ESA GSTP + PRODEX via BELSPO federal space",
            "2024-12-04",
            2003,
            2028,
            63400000,
            {
                "mission_total_m": 166,
                "be_contrib_m": 63.4,
                "be_share_pct": 0.382,
                "launch": "2024-12-04 India",
                "channels": "GSTP+PRODEX",
                "science_ops": "ROB Royal Observatory",
                "payload": "ASPIICS CSL",
                "note": "Multi-year development; dual ESA geo-return; subset of Belspo space 283.4m 2024 class",
            },
            0,
            "https://www.belspo.be/belspo/organisation/report-2024/doc/research/space_PROBA-3.pdf",
            "Formation flying tech demo + solar corona science Space Weather",
            "Track GSTP/PRODEX cash path vs ESA optional; dual industrial concentration",
            "src_belspo_proba3_ar2024",
            "strong",
            "Federal>BELSPO>ESA>PROBA-3",
            "tick336: 63.4m BE of 166m mission dual space",
        )
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_s4policy_34m,S4Policy Policy Driven 34.26m 2024-31 dual federal research,federal,ops,"
        "Federal>BELSPO>S4Policy,6155110,34256160,"
        "Strong S4P InfoFile: 4-call total 34.26m; call1 6.16m; BELSPO 90pct + dept 10pct; dual P4Science FSI,"
        "strong,src_belspo_s4policy_call_2024_25,Researchers federal departments,"
        "Evidence for federal policy Digital Autonomy Inclusion Green,"
        "Core policy research not pure waste; L5 awards residual; dual with community research,"
        "2,6.5,4,4.6,Publish awarded L5 list per call; track cofund delivery,seed,,tick336 dual policy RDI\n"
    )
    f.write(
        "lb_proba3_be_63m,PROBA-3 Belgium contribution 63.4m of 166m dual ESA space,federal,ops,"
        "Federal>BELSPO>ESA>PROBA-3,63400000,166000000,"
        "Strong BELSPO AR2024: BE 63.4m of mission 166m via GSTP+PRODEX; launch Dec2024; dual industry ROB CSL,"
        "strong,src_belspo_proba3_ar2024,Space industry solar science,"
        "Formation flying demo and solar corona Space Weather,"
        "Core space industrial policy not pure waste; multi-year sunk; dual ESA return,"
        "2,8.0,5,5.5,Reconcile multi-year GSTP/PRODEX cash with ESA optional L5,seed,,tick336 dual space\n"
    )

# FOI residuals
with open(root / "foi_queue.csv", "a", encoding="utf-8") as f:
    f.write(
        "gap_s4policy_awards_l5,Federal>BELSPO>S4Policy>awards_L5,s4policy_belspo,"
        "Named awarded projects Call1 2024-25 with EUR BELSPO vs department cofund; cash-by-year 2025-2028; "
        "full programme actual vs indicative 34.26m multi-call,"
        "Indicative envelopes strong; award L5 and outturn residual,5,"
        "BELSPO / POD Wetenschapsbeleid / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_s4policy_awards_l5.md,ready,2026-07-31,,,,,"
        f"cmt_s4policy_policy_driven_2024_31,lb_s4policy_34m,{now},{now},tick336 draft ready human send\n"
    )
    f.write(
        "gap_proba3_gstp_prodex_cash,Federal>BELSPO>PROBA-3>GSTP_PRODEX_cash,proba3_be,"
        "Cash-by-year Belgium PROBA-3 contribution via GSTP and PRODEX 2015-2026; contractor top10 EUR; "
        "reconcile 63.4m total with Belspo space annual lines,"
        "Mission total and BE share strong; multi-year cash path and end-contractor L5 residual,5,"
        "BELSPO Space / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_proba3_gstp_prodex_cash.md,ready,2026-07-31,,,,,"
        f"cmt_proba3_be_63_4m,lb_proba3_be_63m,{now},{now},tick336 draft ready human send; dual ESA optional\n"
    )

draft_dir = root.parent / "foi" / "drafts"
draft_dir.mkdir(parents=True, exist_ok=True)
(draft_dir / "gap_s4policy_awards_l5.md").write_text(
    """# FOI draft — gap_s4policy_awards_l5

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO)
t.a.v. openbaarheid van bestuur
WTC III Simon Bolivarlaan 30 bus 7 — 1000 Brussel
via https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — S4Policy toegekende projecten L5

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik:

1. Lijst toegekende projecten **S4Policy Call 1 (2024-2025) Policy Driven** met:
   acroniem, titel, coördinator, partners, totaalbudget, aandeel BELSPO, aandeel
   federale departement(en), looptijd.
2. Cash-by-year (of begrotingsuitputting) 2025-2028 per project of geaggregeerd.
3. Eventuele actualisatie van de programmatotaal **€34.256.160** (4 calls) vs realisatie.

Periode: 2024-06-01 tot heden.

Context: Federal > BELSPO > S4Policy > awards_L5.
Publiek: InfoFile v6 — Call1 €6.155.110; programma 4 calls €34.256.160;
cofinanciering BELSPO max 90% / departement min 10%.

Dossierreferentie intern: gap_s4policy_awards_l5

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] BELSPO / IBZ
- [x] Concrete L5 awards
- [x] foi_queue ready
- [ ] Human contact + send
""",
    encoding="utf-8",
)

(draft_dir / "gap_proba3_gstp_prodex_cash.md").write_text(
    """# FOI draft — gap_proba3_gstp_prodex_cash

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO) — Space Research and Applications
t.a.v. openbaarheid van bestuur
via https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — PROBA-3 Belgische kasstromen GSTP/PRODEX

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik:

1. Cash-by-year van de Belgische bijdrage aan **PROBA-3** via **GSTP** en **PRODEX**
   (en eventuele andere kanalen) 2015-2026, met begrotingscodes.
2. Top-10 Belgische contractanten/onderaannemers met cumulatief EUR indien beschikbaar.
3. Aansluiting op de publieke totalen: missie **€166 m** waarvan België **€63,4 m**
   (BELSPO Jaarverslag 2024).

Periode: 2015-01-01 tot heden.

Context: Federal > BELSPO > ESA > PROBA-3.
Dossierreferentie intern: gap_proba3_gstp_prodex_cash

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] BELSPO Space / IBZ
- [x] Cash path + contractor L5
- [x] foi_queue ready
- [ ] Human send
""",
    encoding="utf-8",
)

# research queue
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_327,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-31T06:15:00Z,,Spawned tick335 after FED-tWIN DIGIT climate; rq_116 SWA deferred"
)
new = (
    "rq_327,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_s4policy_awards_l5|gap_proba3_gstp_prodex_cash,"
    f"2026-07-31T06:15:00Z,{now},"
    "tick336: S4Policy 34.26m Policy Driven + PROBA-3 BE 63.4m dual; FOI awards/cash; spawn rq_328"
)
if old not in rq:
    raise SystemExit("rq_327 not found")
rq = rq.replace(old, new)
if "rq_328" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_328,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        f"{now},,Spawned tick336 after S4Policy PROBA-3; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_327,336,no,"
    "Scheduler 60s. Next prio5 rq_328; rq_116 SWA deferred. FOI ready. tick336 S4Policy PROBA-3.\n",
    encoding="utf-8",
)

# belspo note
ent = (root / "entities.csv").read_text(encoding="utf-8")
ent2 = re.sub(
    r"belspo,POD Wetenschapsbeleid BELSPO,[^\n]+",
    "belspo,POD Wetenschapsbeleid BELSPO,SPP Politique scientifique BELSPO,"
    "Federal Science Policy Office,agency,sec_federal,bi,https://www.belspo.be,,,"
    "Budget 2024 582.4m; S4Policy 34.26m; PROBA-3 BE 63.4m; FED-tWIN DIGIT P4S; dual; tick329-336",
    ent,
    count=1,
)
(root / "entities.csv").write_text(ent2, encoding="utf-8")

print("OK tick336")

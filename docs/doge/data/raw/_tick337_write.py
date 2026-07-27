# tick 337 — STEREO IV EO programme 28.15m dual community RS
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T07:15:00Z"

with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_belspo_stereo_iv_call2025,BELSPO STEREO IV Earth observation programme InfoFile call 2025,"
        "https://eo.belspo.be/sites/default/files/pdf/project-management/STEREO-IV-infofile_call2025.pdf,"
        "BELSPO,2026-07-31,official_call,"
        "Strong: CM 22Nov2019 STEREO IV 2022-2029 budget 28.15m EUR; call2025 thematic networks ~7.4m tentative; "
        "dual FL/FR teams recommended; foreign max 20pct; tick337\n"
    )
    f.write(
        "src_belspo_stereo_iv_portal,BELSPO STEREO IV programme official EO portal,"
        "https://eo.belspo.be/en/stereo-iv-programme,BELSPO,2026-07-31,official_portal,"
        "Strong structure: 2022-2029 eighth EO phase since 1985; thematic priorities climate hazards biodiversity cities; "
        "CM approved multi-annual; tick337\n"
    )

with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "stereo_iv_belspo,STEREO IV Earth observation research BELSPO,"
        "STEREO IV programme BELSPO,"
        "Multi-annual federal Earth observation remote sensing research 2022-2029,"
        "programme,belspo,bi,https://eo.belspo.be/en/stereo-iv-programme,,,,"
        "Envelope 28.15m CM2019; call2025 ~7.4m; dual community RS; tick337\n"
    )

bud = [
    "bud_stereo_iv_total_2022_29,stereo_iv_belspo,2029,28150000,,,budgeted,src_belspo_stereo_iv_call2025,strong,STEREO IV programme 2022-2029 allocated budget 28.15m EUR (CM 22 Nov 2019)",
    "bud_stereo_iv_call2025_class,stereo_iv_belspo,2025,7400000,,,budgeted,src_belspo_stereo_iv_call2025,medium,Call 2025 thematic network projects tentatively ~7.4 MEURO subject to final budget approval",
    "bud_stereo_iv_annual_class,stereo_iv_belspo,2025,3518750,,,budgeted,src_belspo_stereo_iv_call2025,medium,Illustrative annual class 28.15m/8y ~3.52m if flat; not cash outturn",
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
            "cmt_stereo_iv_2022_29",
            "STEREO IV Earth observation multi-annual dual community RS",
            "stereo_iv_belspo",
            "Belgian RS research teams universities FSI + international partners",
            "CM 22 Nov 2019 Belgian space strategy multi-annual EO research",
            "2019-11-22",
            2022,
            2029,
            28150000,
            {
                "programme_m": 28.15,
                "period": "2022-2029",
                "call2025_class_m": 7.4,
                "foreign_max_share_pct": 0.20,
                "dual_community_recommended": True,
                "themes": "climate_EO hazards biodiversity green_cities",
                "prior_phases": "TELSAT+STEREO_I-III since 1985",
                "note": "Programme envelope strong primary; call2025 tentative; L5 project awards FOI; dual FL/FR teams",
            },
            None,
            "https://eo.belspo.be/sites/default/files/pdf/project-management/STEREO-IV-infofile_call2025.pdf",
            "Maintain top remote sensing community support Belgian space strategy",
            "Publish multi-year cash and named project L5; dual unit-cost vs regional EO",
            "src_belspo_stereo_iv_call2025",
            "strong",
            "Federal>BELSPO>STEREO_IV",
            "tick337: 28.15m 2022-29 dual EO research",
        )
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_stereo_iv_28m,STEREO IV Earth observation 28.15m 2022-29 dual community RS,federal,ops,"
        "Federal>BELSPO>STEREO_IV,3518750,28150000,"
        "Strong BELSPO: CM2019 envelope 28.15m 2022-29; call2025 ~7.4m class; dual FL/FR teams; climate EO subset prior,"
        "strong,src_belspo_stereo_iv_call2025,Remote sensing researchers universities,"
        "Quality EO research climate hazards biodiversity green cities,"
        "Core space/EO capacity not pure waste; L5 awards residual; dual community encouraged,"
        "2,6.5,4,4.6,Publish awarded project list EUR multi-year cash path,seed,,tick337 dual EO\n"
    )

with open(root / "foi_queue.csv", "a", encoding="utf-8") as f:
    f.write(
        "gap_stereo_iv_awards_cash_l5,Federal>BELSPO>STEREO_IV>awards_cash_L5,stereo_iv_belspo,"
        "Cash-by-year STEREO IV 2022-2026 outturn vs 28.15m envelope; named thematic network and open-call awards with EUR; "
        "share Flemish vs French-speaking partners; foreign partner spend within 20pct cap,"
        "Programme envelope and call2025 class public; end-project L5 and cash path residual,5,"
        "BELSPO Earth Observation / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_stereo_iv_awards_cash_l5.md,ready,2026-07-31,,,,,"
        f"cmt_stereo_iv_2022_29,lb_stereo_iv_28m,{now},{now},tick337 draft ready human send\n"
    )

draft = root.parent / "foi" / "drafts" / "gap_stereo_iv_awards_cash_l5.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    """# FOI draft — gap_stereo_iv_awards_cash_l5

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO) — Earth Observation / STEREO
t.a.v. openbaarheid van bestuur
WTC III Simon Bolivarlaan 30 bus 7 — 1000 Brussel
via https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — STEREO IV kasstromen en L5-projecten

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik:

1. Cash-by-year (of begrotingsuitputting) **STEREO IV** 2022-2026 vs programmatotaal
   **€28,15 m** (2022-2029).
2. Lijst toegekende projecten (thematic network + open call types) met: acroniem, titel,
   partners (FWI/universiteit), bedrag, looptijd, taalgemeenschap coördinator.
3. Aandeel buitenlandse partners binnen de 20%-cap, geaggregeerd.
4. Eventuele actualisatie call 2025 (~€7,4 m class) na begrotingsgoedkeuring.

Periode: 2022-01-01 tot heden.

Context: Federal > BELSPO > STEREO_IV > awards_cash_L5.
Publiek: CM 22 nov 2019; InfoFile call 2025; duale aanbeveling NL/FR teams.

Dossierreferentie intern: gap_stereo_iv_awards_cash_l5

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] BELSPO EO / IBZ
- [x] Concrete cash + L5 projects
- [x] foi_queue ready
- [ ] Human contact + send
""",
    encoding="utf-8",
)

# research queue: seed rq_328 done + rq_329
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
# ensure rq_328 exists as done
if "rq_328" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_328,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_stereo_iv_awards_cash_l5,"
        f"2026-07-31T06:45:00Z,{now},"
        "tick337: STEREO IV 28.15m EO dual community; call2025 ~7.4m; FOI awards L5; spawn rq_329\n"
    )
else:
    rq = re.sub(
        r"rq_328,[^\n]+",
        "rq_328,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_stereo_iv_awards_cash_l5,"
        f"2026-07-31T06:45:00Z,{now},"
        "tick337: STEREO IV 28.15m EO dual community; call2025 ~7.4m; FOI awards L5; spawn rq_329",
        rq,
        count=1,
    )
if "rq_329" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_329,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        f"{now},,Spawned tick337 after STEREO IV; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_328,337,no,"
    "Scheduler 60s. Next prio5 rq_329; rq_116 SWA deferred. FOI ready. tick337 STEREO IV 28.15m.\n",
    encoding="utf-8",
)

ent = (root / "entities.csv").read_text(encoding="utf-8")
ent2 = re.sub(
    r"belspo,POD Wetenschapsbeleid BELSPO,[^\n]+",
    "belspo,POD Wetenschapsbeleid BELSPO,SPP Politique scientifique BELSPO,"
    "Federal Science Policy Office,agency,sec_federal,bi,https://www.belspo.be,,,"
    "Budget 2024 582.4m; STEREO IV 28.15m; S4Policy PROBA-3 FED-tWIN DIGIT; dual; tick329-337",
    ent,
    count=1,
)
(root / "entities.csv").write_text(ent2, encoding="utf-8")

print("OK tick337")

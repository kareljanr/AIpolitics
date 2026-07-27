# tick 339 — EUMETSAT BE 13.48m 2024 dual intergov meteo space
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T08:15:00Z"

with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_eumetsat_ar2024,EUMETSAT Annual Report 2024 Member State contributions,"
        "https://www-cdn.eumetsat.int/files/2025-07/PDF_AR2025_EN%20%281%29.pdf,"
        "EUMETSAT,2026-07-31,official_annual_report,"
        "Strong: BE contribution 13480 kEUR = 13.480m of MS total 506.037m 2024; expenditure budgets total 763.2m; "
        "dual KMI IRM + Belspo intergov path CM25 ~25m/y class; tick339\n"
    )

with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "eumetsat_be,EUMETSAT Belgian membership contribution,"
        "EUMETSAT contribution belge,"
        "Belgium member state contribution to European Organisation for the Exploitation of Meteorological Satellites,"
        "programme,belspo,bi,https://www.eumetsat.int,,,,"
        "BE 13.480m 2024 of 506.037m MS; dual KMI meteo Belspo space; tick339\n"
    )

# belspo note
ent = (root / "entities.csv").read_text(encoding="utf-8")
ent = re.sub(
    r"belspo,POD Wetenschapsbeleid BELSPO,[^\n]+",
    "belspo,POD Wetenschapsbeleid BELSPO,SPP Politique scientifique BELSPO,"
    "Federal Science Policy Office,agency,sec_federal,bi,https://www.belspo.be,,,"
    "Budget 2024 582.4m; ESA CM25 path; EUMETSAT 13.48m 2024 dual intergov; tick329-339",
    ent,
    count=1,
)
(root / "entities.csv").write_text(ent, encoding="utf-8")

bud = [
    "bud_eumetsat_be_2024,eumetsat_be,2024,13480000,,,outturn,src_eumetsat_ar2024,strong,Belgium Member State contribution to EUMETSAT 13.480m EUR 2024 (table KEUR 13480)",
    "bud_eumetsat_ms_total_2024,eumetsat_be,2024,506037000,,,outturn,src_eumetsat_ar2024,strong,Total EUMETSAT Member State contributions 506.037m EUR 2024",
    "bud_eumetsat_exp_total_2024,eumetsat_be,2024,763200000,,,budgeted,src_eumetsat_ar2024,strong,EUMETSAT total expenditure budgets 2024 763.2m (GB 91 EPS-SG 254.3 MTG 219.1 Copernicus 111.4 etc)",
    "bud_eumetsat_be_share_pct_2024,eumetsat_be,2024,2.66,,,outturn,src_eumetsat_ar2024,strong,BE share of MS contributions 13.480/506.037 ~2.66pct 2024",
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
            "cmt_eumetsat_be_2024",
            "Belgium EUMETSAT membership contribution dual meteo space",
            "eumetsat_be",
            "KMI/IRM weather service Belgium + European meteo users",
            "EUMETSAT Convention GNI-scale Member State contributions",
            "1985-10-01",
            2024,
            2024,
            13480000,
            {
                "be_2024_m": 13.48,
                "ms_total_2024_m": 506.037,
                "be_share_pct": 0.0266,
                "eumetsat_exp_2024_m": 763.2,
                "exp_split_m": {
                    "GB": 91,
                    "EPS_SG": 254.3,
                    "MTG": 219.1,
                    "Copernicus_2": 111.4,
                    "EPS": 37.4,
                    "MSG": 23.3,
                    "DestinE": 24.3,
                    "Jason_CS": 2.4,
                },
                "note": "Part of CM25 intergov class ~25m/y with ECMWF+ESO residual FOI; dual KMI Belspo space path",
            },
            0,
            "https://www-cdn.eumetsat.int/files/2025-07/PDF_AR2025_EN%20%281%29.pdf",
            "Operational meteorological satellites for European weather climate services",
            "Publish multi-year BE cash series; FOI ECMWF ESO residual of intergov 25m class",
            "src_eumetsat_ar2024",
            "strong",
            "Federal>BELSPO>intergov>EUMETSAT",
            "tick339: 13.48m 2024 dual meteo space",
        )
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_eumetsat_be_13_5m,Belgium EUMETSAT contribution 13.48m 2024 dual meteo space,federal,ops,"
        "Federal>BELSPO>intergov>EUMETSAT,13480000,13480000,"
        "Strong EUMETSAT AR2024: BE 13.480m of 506.037m MS; ~2.66pct; dual KMI + Belspo CM25 intergov class,"
        "strong,src_eumetsat_ar2024,Weather services public safety,"
        "European operational meteorological satellites,"
        "Core weather infrastructure not pure waste; treaty membership; dual ESA space package,"
        "2,5.5,3,3.9,Multi-year series + ECMWF ESO residual FOI,seed,,tick339 dual intergov\n"
    )

with open(root / "foi_queue.csv", "a", encoding="utf-8") as f:
    f.write(
        "gap_be_intergov_meteo_space_l5,Federal>BELSPO>intergov>EUMETSAT_ECMWF_ESO,belspo,"
        "Cash-by-year 2022-2026 Belgium contributions to EUMETSAT ECMWF and ESO separately; budget article codes; "
        "reconcile CM25 intergov class ~25m/y with EUMETSAT 13.48m 2024 primary,"
        "EUMETSAT 2024 strong; ECMWF+ESO residual; dual KMI Belspo path,5,"
        "BELSPO / KMI-IRM / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_be_intergov_meteo_space_l5.md,ready,2026-07-31,,,,,"
        f"cmt_eumetsat_be_2024|cmt_be_space_path_2025_30,lb_eumetsat_be_13_5m,{now},{now},"
        "tick339 EUMETSAT filled; residual ECMWF ESO human send\n"
    )

draft = root.parent / "foi" / "drafts" / "gap_be_intergov_meteo_space_l5.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    """# FOI draft — gap_be_intergov_meteo_space_l5

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO)
cc: KMI/IRM waar van toepassing
via https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — Belgische bijdragen EUMETSAT / ECMWF / ESO

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik:

1. Cash-by-year 2022-2026 van de Belgische lidmaatschapsbijdragen aan:
   - **EUMETSAT**
   - **ECMWF**
   - **ESO** (European Southern Observatory)
   met begrotingsartikelcodes.
2. Aansluiting op de BELSPO CM-ESA Bremen-classificatie “intergovernmental
   ~€25 m/jaar” (Eumetsat + ECMWF + ESO).
3. Bevestiging van de EUMETSAT-bijdrage **€13,480 m (2024)** vs Belgische
   begrotingsuitputting.

Publiek: EUMETSAT AR2024 Member State contributions — Belgium 13.480 m€;
totaal MS 506.037 m€.

Dossierreferentie intern: gap_be_intergov_meteo_space_l5

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] BELSPO / KMI / IBZ
- [x] Concrete multi-year L5
- [x] foi_queue ready
- [ ] Human send
""",
    encoding="utf-8",
)

# research queue
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
if "rq_330" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_330,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Note progress@340 next tick.,"
        "gap_be_intergov_meteo_space_l5,"
        f"2026-07-31T07:45:00Z,{now},"
        "tick339: EUMETSAT BE 13.48m 2024 dual intergov; FOI ECMWF ESO residual; spawn rq_331 progress@340\n"
    )
else:
    rq = re.sub(
        r"rq_330,[^\n]+",
        "rq_330,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Note progress@340 next tick.,"
        "gap_be_intergov_meteo_space_l5,"
        f"2026-07-31T07:45:00Z,{now},"
        "tick339: EUMETSAT BE 13.48m 2024 dual intergov; FOI ECMWF ESO residual; spawn rq_331 progress@340",
        rq,
        count=1,
    )
if "rq_331" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_331,Mandatory progress@340 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
        "When ticks_completed hits 340: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
        "and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
        f"{now},,Spawned tick339; MANDATORY at tick 340\n"
    )
rq_path.write_text(rq, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_330,339,no,"
    "Scheduler 60s. Next MANDATORY rq_331 progress@340; rq_116 SWA deferred. tick339 EUMETSAT 13.48m.\n",
    encoding="utf-8",
)

print("OK tick339")

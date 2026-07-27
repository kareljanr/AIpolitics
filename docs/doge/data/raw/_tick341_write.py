# tick 341 — VAF Flanders dual AV fund ~30.7m VL dots
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T09:15:00Z"

with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_vaf_jv_2024,VAF Jaarverslag 2024 Film Media Game fonds dotaties en bestedingen,"
        "https://www.vaf.be/files/Jaarverslagen/VAF_2024_jaarverslag.pdf,VAF,2026-07-31,official_annual_report,"
        "Strong: Filmfonds VL Culture dot 20.490m total budget 20.535m creatie 11.753m; Mediafonds 7.450m; "
        "Gamefonds 2.768m; dual community AV; tick341\n"
    )
    f.write(
        "src_vaf_jv_2025,VAF Jaarverslag 2025 Film Media Game fonds dotaties,"
        "https://www.vaf.be/files/Jaarverslagen/Jaarverslag-2025.pdf,VAF,2026-07-31,official_annual_report,"
        "Strong: Filmfonds Culture 20.820m creatie 11.900m; Mediafonds 7.173m; Gamefonds 2.800m; tick341\n"
    )

with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "vaf,Vlaams Audiovisueel Fonds VAF,Fonds audiovisuel flamand VAF,"
        "Flanders audiovisual support agency Film Media Game Screen Flanders,"
        "agency,vlaanderen_gov,nl,https://www.vaf.be,,,,"
        "VL dots ~30.7m 2024-25 Film+Media+Game; dual CCA Wallonie + Cinematek federal; tick341\n"
    )

bud = [
    "bud_vaf_film_dot_culture_2024,vaf,2024,20490000,,,budgeted,src_vaf_jv_2024,strong,VAF/Filmfonds VL Culture dotatie excl Screen Flanders promo 20.490m 2024",
    "bud_vaf_film_total_budget_2024,vaf,2024,20535000,,,budgeted,src_vaf_jv_2024,strong,VAF/Filmfonds available total budget 20.535m (creatie 11.753 promo 0.825 talent 0.6 publiek 5.176 werk 2.136 SF promo 0.045)",
    "bud_vaf_film_creatie_2024,vaf,2024,11753000,,,budgeted,src_vaf_jv_2024,strong,Filmfonds steun creatie envelope 11.753m (fictie 7.753 doc 1.575 anim 1.575 filmlab 0.45 innov 0.4)",
    "bud_vaf_film_spend_2024,vaf,2024,21575521,,,outturn,src_vaf_jv_2024,strong,Filmfonds total spend 21.575521m 2024 (creatie approvals 12.82m)",
    "bud_vaf_media_dot_2024,vaf,2024,7449720,,,budgeted,src_vaf_jv_2024,strong,VAF/Mediafonds VL Media dotatie incl excedent 7.44972m 2024",
    "bud_vaf_media_total_budget_2024,vaf,2024,8894175,,,budgeted,src_vaf_jv_2024,strong,Mediafonds available total 8.894m incl dienstenverdelers/OTT 0.781m",
    "bud_vaf_media_spend_2024,vaf,2024,8554066,,,outturn,src_vaf_jv_2024,strong,Mediafonds total spend 8.554m 2024",
    "bud_vaf_game_dot_2024,vaf,2024,2768280,,,budgeted,src_vaf_jv_2024,strong,VAF/Gamefonds VL Media+Onderwijs dotatie 2.76828m 2024",
    "bud_vaf_vl_dots_sum_2024,vaf,2024,30707999.999,,,budgeted,src_vaf_jv_2024,strong,Sum VL government dots Film+Media+Game 20.490+7.450+2.768=30.708m 2024",
    "bud_vaf_film_dot_culture_2025,vaf,2025,20820000,,,budgeted,src_vaf_jv_2025,strong,VAF/Filmfonds VL Culture dotatie excl Screen Flanders promo 20.820m 2025",
    "bud_vaf_film_creatie_2025,vaf,2025,11900000,,,budgeted,src_vaf_jv_2025,strong,Filmfonds steun creatie total 11.900m 2025",
    "bud_vaf_media_dot_2025,vaf,2025,7173000,,,budgeted,src_vaf_jv_2025,strong,VAF/Mediafonds VL Media dotatie 7.173m 2025",
    "bud_vaf_game_dot_2025,vaf,2025,2800000,,,budgeted,src_vaf_jv_2025,strong,VAF/Gamefonds VL Media+Onderwijs 2.800m 2025",
    "bud_vaf_vl_dots_sum_2025,vaf,2025,30793000,,,budgeted,src_vaf_jv_2025,strong,Sum VL government dots Film+Media+Game 20.820+7.173+2.800=30.793m 2025",
]
# fix float row - use integer
bud[8] = "bud_vaf_vl_dots_sum_2024,vaf,2024,30708000,,,budgeted,src_vaf_jv_2024,strong,Sum VL government dots Film+Media+Game 20.490+7.450+2.768=30.708m 2024"
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
            "cmt_vaf_package_2024_25",
            "VAF Flanders audiovisual triple fund VL dots dual community culture",
            "vaf",
            "Flemish film series game producers festivals arthouse",
            "Beheersovereenkomsten VAF Film Media Game 2022-2025 / 2026-2030 path",
            "2022-01-01",
            2024,
            2025,
            61501000,
            {
                "vl_dots_2024_m": 30.708,
                "vl_dots_2025_m": 30.793,
                "film_culture_2024_m": 20.49,
                "film_culture_2025_m": 20.82,
                "media_2024_m": 7.45,
                "media_2025_m": 7.173,
                "game_2024_m": 2.768,
                "game_2025_m": 2.8,
                "film_creatie_2024_m": 11.753,
                "film_spend_2024_m": 21.576,
                "media_spend_2024_m": 8.554,
                "media_ott_contrib_2024_m": 0.781,
                "dual": "CCA Wallonie + federal Cinematek Belspo + tax-shelter Screen Flanders class",
                "note": "Strong VAF JV primary; CCA L5 residual FOI; dual community AV policy",
            },
            None,
            "https://www.vaf.be/files/Jaarverslagen/VAF_2024_jaarverslag.pdf",
            "Support Flemish audiovisual creation talent public game sector",
            "Publish L5 top awards; dual unit-cost vs CCA; Screen Flanders taxex map",
            "src_vaf_jv_2024",
            "strong",
            "Vlaanderen>CJSM>Media>VAF",
            "tick341: ~30.7m VL dots dual AV culture",
        )
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_vaf_vl_dots_31m,VAF Flanders AV triple fund VL dots ~30.7m dual community culture,regional,ops,"
        "Vlaanderen>CJSM>Media>VAF,30708000,61501000,"
        "Strong VAF JV: VL dots Film 20.5+Media 7.5+Game 2.8=30.7m 2024 / 30.8m 2025; dual CCA+Cinematek,"
        "strong,src_vaf_jv_2024,Flemish AV creators festivals,"
        "Audiovisual creation talent public games,"
        "Core culture policy not pure waste; dual community film funds; L5 award opacity residual,"
        "3,6.5,4,5.0,FOI CCA dual map; L5 top VAF awards multi-year,seed,,tick341 dual culture AV\n"
    )

with open(root / "foi_queue.csv", "a", encoding="utf-8") as f:
    f.write(
        "gap_vaf_cca_dual_l5,BE>culture>AV_funds>VAF_CCA_L5,vaf,"
        "Named top20 VAF Film+Media+Game awards EUR 2023-2025; CCA Wallonie annual package same structure; "
        "Screen Flanders tax-shelter cash path if public; federal Cinematek structural Belspo dot series,"
        "VAF VL dots strong primary; dual CCA and Cinematek base L5 residual,5,"
        "VAF / CCA / BELSPO / Team Openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,"
        "Havenlaan 88 bus 20 1000 Brussel,"
        "docs/doge/foi/drafts/gap_vaf_cca_dual_l5.md,ready,2026-07-31,,,,,"
        f"cmt_vaf_package_2024_25,lb_vaf_vl_dots_31m,{now},{now},"
        "tick341 VAF filled; residual CCA+Cinematek+L5 human send\n"
    )

draft = root.parent / "foi" / "drafts" / "gap_vaf_cca_dual_l5.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    """# FOI draft — gap_vaf_cca_dual_l5

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: Vlaams Audiovisueel Fonds / Team Openbaarheid Vlaanderen
cc: Centre du Cinéma et de l'Audiovisuel (FWB/Wallonie) waar van toepassing;
    POD Wetenschapsbeleid (CINEMATEK-dotatie)
openbaarheid@vlaanderen.be

Betreft: Verzoek om openbaarmaking — VAF/CCA audiovisuele steun L5 dual

Geachte,

Op grond van de toepasselijke openbaarheidsregels vraag ik:

1. **VAF**: machineleesbare top-20 toegekende steunen (Film/Media/Game)
   2023-2025 met bedrag, project/titel, begunstigde, fonds.
2. **CCA (of equivalent FWB/Wallonië)**: parallel jaarbudget/dotatie
   2023-2025 en top-20 toegekende steunen indien publiek gehouden.
3. **CINEMATEK**: structurele Belspo-dotatie cash-by-year 2022-2026.
4. Eventuele Screen Flanders / tax-shelter kasstromen die VAF beheert
   (indien aparte openbare rekeningen).

Publiek (VAF JV 2024-2025): VL-dotaties Film ~€20,5–20,8 m + Media ~€7,2–7,5 m
+ Game ~€2,8 m ≈ **€30,7 m/jaar**.

Dossierreferentie intern: gap_vaf_cca_dual_l5

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] VAF / VL openbaarheid / CCA / Belspo
- [x] Concrete L5 dual map
- [x] foi_queue ready
- [ ] Human send
""",
    encoding="utf-8",
)

# research queue
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
if "rq_332" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_332,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills after progress@340 (FOI-adjacent dual/L5). Prefer before idle.,"
        "gap_vaf_cca_dual_l5,"
        f"2026-07-31T08:45:00Z,{now},"
        "tick341: VAF VL dots ~30.7m Film/Media/Game dual culture AV; FOI CCA L5; spawn rq_333\n"
    )
else:
    rq = re.sub(
        r"rq_332,[^\n]+",
        "rq_332,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
        "Prefer public primary fills after progress@340 (FOI-adjacent dual/L5). Prefer before idle.,"
        "gap_vaf_cca_dual_l5,"
        f"2026-07-31T08:45:00Z,{now},"
        "tick341: VAF VL dots ~30.7m Film/Media/Game dual culture AV; FOI CCA L5; spawn rq_333",
        rq,
        count=1,
    )
if "rq_333" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_333,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        f"{now},,Spawned tick341 after VAF dual culture; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_332,341,no,"
    "Scheduler 60s. Next prio5 rq_333; rq_116 SWA deferred. FOI ready. tick341 VAF ~30.7m dual AV.\n",
    encoding="utf-8",
)

print("OK tick341")

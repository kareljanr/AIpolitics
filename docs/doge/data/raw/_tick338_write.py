# tick 338 — BE ESA CM25 multi-year space dual Belspo+Defence
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T07:45:00Z"

with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_belspo_cm25_esa_bremen_debrief,BELSPO CM-ESA Bremen 2025 Belgian subscription debrief presentation,"
        "https://www.belspo.be/belspo/space/doc/Presentations/20251205_CM-ESA-Bremen-2025_BELSPO-Debriefing-presentation.pdf,"
        "BELSPO,2026-07-31,official_presentation,"
        "Strong: BE space 2025-30 total 1845m (1277+168 MoD+400 one-off) ~369m/y; ESA CM25 BE 1109m incl MoD; "
        "PRODEX 99m GSTP 103.9m Science 106.4m; dual Defence DIRS; tick338\n"
    )

with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "esa_cm25_be,ESA CM25 Belgian multi-year subscription dual Defence,"
        "ESA Ministerial Council 2025 Belgium package,"
        "Belgian civil+defence ESA programme subscriptions 2025-2030 path,"
        "programme,esa_be_contrib,bi,https://www.esa.int/,,,,"
        "BE ESA 1109m CM25; total space BE 1845m 2025-30; dual MoD 168m ESA; tick338\n"
    )
    # update esa_be_contrib note
ent = (root / "entities.csv").read_text(encoding="utf-8")
ent = re.sub(
    r"esa_be_contrib,[^\n]+",
    "esa_be_contrib,ESA Belgian contribution,Contribution belge ESA,"
    "Belgian membership and optional programme contributions to European Space Agency,"
    "programme,belspo,bi,https://www.esa.int,,,,"
    "CM25 BE 1109m package; annual ~335m ESA class 2025-30; dual MoD; prior MERI 284m 2025; tick331+338",
    ent,
    count=1,
)
ent = re.sub(
    r"belspo,POD Wetenschapsbeleid BELSPO,[^\n]+",
    "belspo,POD Wetenschapsbeleid BELSPO,SPP Politique scientifique BELSPO,"
    "Federal Science Policy Office,agency,sec_federal,bi,https://www.belspo.be,,,"
    "Budget 2024 582.4m; ESA CM25 path ~335m/y space; dual MoD; STEREO S4P; tick329-338",
    ent,
    count=1,
)
(root / "entities.csv").write_text(ent, encoding="utf-8")
with open(root / "entities.csv", "a", encoding="utf-8") as f:
    pass  # already updated

bud = [
    "bud_be_space_total_2025_30,esa_cm25_be,2030,1845000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,BE total space 2025-2030 e.c.2025: 1277+168 MoD+400 one-off = 1845m (~369m/y)",
    "bud_be_space_base_path_2025_30,esa_cm25_be,2030,1277000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,Base BE space path 1277m 2025-30 before MoD ESA and one-off",
    "bud_be_space_mod_esa_168m,esa_cm25_be,2030,168000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,Belgian Defence participation ESA optional programmes 168m (CM25 package)",
    "bud_be_space_oneoff_400m,esa_cm25_be,2028,400000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,One-off budget increase 2026 and 2028 total 400m (CM 24 Nov 2025 class)",
    "bud_be_esa_cm25_total_1109m,esa_cm25_be,2030,1109000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,BE total ESA CM25 subscription 1109m incl MoD (5.06pct of ESA 22.07bn)",
    "bud_be_esa_cm25_annual_class,esa_cm25_be,2026,335000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,medium,ESA share of BE space ~335m/y average 2025-30 class incl defence",
    "bud_be_esa_ineluctables_1050m,esa_cm25_be,2030,1050000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,Previous ESA commitments Ineluctables 1050m",
    "bud_be_esa_new_commit_934m,esa_cm25_be,2030,934000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,New ESA programme commitments 934m of which 836m period 2026-2030",
    "bud_be_prodex_cm25_99m,esa_cm25_be,2029,99000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,PRODEX BE covered 99m (24 unconditional + 75 conditional) till 2029",
    "bud_be_gstp_cm25_103_9m,esa_cm25_be,2030,103900000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,medium,GSTP BE total 103.9m of which 79.9m TBA/conditional class",
    "bud_be_science_prog_cm25_106_4m,esa_cm25_be,2030,106400000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,ESA Science Programme BE 106.4m (GNP1)",
    "bud_be_basic_act_cm25_52_2m,esa_cm25_be,2030,52200000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,ESA Basic Activities BE 52.2m (GNP1)",
    "bud_be_mod_space_invest_2026_34,esa_cm25_be,2034,617000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,strong,Belgian Defence important investment programmes space 2026-2034 617m",
    "bud_be_intergov_space_class_25m,esa_cm25_be,2026,25000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,medium,Intergovernmental Eumetsat ECMWF ESO class ~25m/y of BE space path",
    "bud_be_eu_bilat_nat_space_class_10m,esa_cm25_be,2026,10000000,,,budgeted,src_belspo_cm25_esa_bremen_debrief,medium,EU bilateral national space activities class ~10m/y",
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
            "cmt_be_space_path_2025_30",
            "Belgium multi-year space package CM25 dual Belspo Defence",
            "esa_cm25_be",
            "Belgian space industry research universities Defence ESA",
            "ESA CM Bremen Nov2025 + BE resource decision May2025 + one-off 24Nov2025",
            "2025-11-26",
            2025,
            2030,
            1845000000,
            {
                "total_2025_30_m": 1845,
                "base_path_m": 1277,
                "mod_esa_m": 168,
                "oneoff_400_m": 400,
                "annual_class_m": 369,
                "esa_annual_class_m": 335,
                "intergov_annual_class_m": 25,
                "eu_bilat_nat_annual_class_m": 10,
                "esa_cm25_be_m": 1109,
                "ineluctables_m": 1050,
                "new_esa_commit_m": 934,
                "prodex_m": 99,
                "gstp_m": 103.9,
                "science_m": 106.4,
                "basic_m": 52.2,
                "mod_invest_2026_34_m": 617,
                "note": "e.c.2025 prices; some TBA/conditional need BE CM by 31Jan2026; dual civil Belspo + MoD DIRS",
            },
            None,
            "https://www.belspo.be/belspo/space/doc/Presentations/20251205_CM-ESA-Bremen-2025_BELSPO-Debriefing-presentation.pdf",
            "Belgian industrial return ESA membership dual civil-military space capacity",
            "Publish cash-by-year confirmed vs TBA; dual unit-cost civil vs MoD lines",
            "src_belspo_cm25_esa_bremen_debrief",
            "strong",
            "Federal>BELSPO>ESA>CM25",
            "tick338: 1845m 2025-30 dual Belspo Defence space",
        )
    )
    f.write(
        cmt(
            "cmt_be_mod_esa_dirs_2025_34",
            "Belgian Defence ESA+DIRS space investment dual Belspo",
            "esa_cm25_be",
            "Belgian Defence space capabilities industry",
            "MoD DIRS + ESA optional subscription CM25",
            "2025-10-01",
            2025,
            2034,
            785000000,
            {
                "mod_esa_subscription_m": 168,
                "mod_invest_2026_34_m": 617,
                "pack_class_m": 785,
                "gstp_make_mod_m": 50,
                "gstp_rsc_mod_m": 69,
                "navisp_e2_mod_m": 20,
                "scylight_mod_m": 15,
                "s2p_cosmic_mod_m": 11,
                "gstp_eee_mod_m": 3,
                "note": "MoD ESA lines sum 168m presentation; invest programmes 617m separate DIRS path; dual NATO accounting constraint",
            },
            None,
            "https://www.belspo.be/belspo/space/doc/Presentations/20251205_CM-ESA-Bremen-2025_BELSPO-Debriefing-presentation.pdf",
            "Military space capability dual-use industrial base NATO-accountable spend",
            "FOI cash-by-year DIRS space vs ESA optional L5 contractors",
            "src_belspo_cm25_esa_bremen_debrief",
            "strong",
            "Federal>Defence>Space>ESA_DIRS",
            "tick338: MoD 168m ESA + 617m invest dual",
        )
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_be_space_1845m_cm25,Belgium space multi-year 1.845bn 2025-30 dual Belspo Defence,federal,ops,"
        "Federal>BELSPO>ESA>CM25,369000000,1845000000,"
        "Strong BELSPO CM25 debrief: 1845m = 1277+168 MoD+400 one-off; ESA 1109m; ~369m/y dual civil-military,"
        "strong,src_belspo_cm25_esa_bremen_debrief,Space industry Defence research,"
        "ESA membership industrial return dual Defence space,"
        "Core industrial/security policy not pure waste; large multi-year; TBA/conditional residual; dual MoD,"
        "3,9.0,6,6.9,Confirm TBA by CM Jan2026; publish cash-by-year civil vs MoD,seed,,tick338 dual space\n"
    )
    f.write(
        "lb_be_esa_cm25_1109m,Belgium ESA CM25 subscription 1.109bn incl MoD,federal,ops,"
        "Federal>BELSPO>ESA>CM25_subscription,221800000,1109000000,"
        "Strong: BE 1109m of ESA 22.07bn (5.06pct) incl MoD; prior CM22 946.86m; dual civil optional,"
        "strong,src_belspo_cm25_esa_bremen_debrief,Belgian ESA actors industry,"
        "ESA optional+mandatory subscriptions multi-year,"
        "Core membership not pure waste; L5 programme split public presentation; residual cash FOI,"
        "2,8.5,5,5.9,FOI cash outturn by programme GSTP PRODEX ARTES,seed,,tick338\n"
    )
    f.write(
        "lb_be_mod_space_785m_class,Belgian Defence space ESA+DIRS class ~785m dual,federal,ops,"
        "Federal>Defence>Space,168000000,785000000,"
        "Strong BELSPO: MoD ESA 168m + invest 617m 2026-34; GSTP MAKE 50 RSC 69 NAVISP 20; dual NATO,"
        "strong,src_belspo_cm25_esa_bremen_debrief,Defence space industry,"
        "Military space capability and dual-use industrial base,"
        "Security core not pure waste; dual Belspo civil; L5 contractors residual,"
        "3,8.0,6,6.3,FOI DIRS cash path and contractor L5,seed,,tick338 dual MoD\n"
    )

with open(root / "foi_queue.csv", "a", encoding="utf-8") as f:
    f.write(
        "gap_be_space_cm25_cash_l5,Federal>BELSPO>ESA>CM25_cash_L5,esa_cm25_be,"
        "Cash-by-year 2025-2030 civil Belspo vs MoD for ESA programmes; confirmation of TBA/conditional 79.9m GSTP and 75m PRODEX conditional; "
        "one-off 400m 2026/2028 schedule; top contractors by programme if public,"
        "Package totals strong CM25 debrief; multi-year cash and TBA confirmation residual,6,"
        "BELSPO Space / Defence / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_be_space_cm25_cash_l5.md,ready,2026-07-31,,,,,"
        f"cmt_be_space_path_2025_30|cmt_be_mod_esa_dirs_2025_34,lb_be_space_1845m_cm25,{now},{now},"
        "tick338 draft ready human send; dual civil-military space\n"
    )

draft = root.parent / "foi" / "drafts" / "gap_be_space_cm25_cash_l5.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    """# FOI draft — gap_be_space_cm25_cash_l5

Status: **ready** (human send only)

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: POD Wetenschapsbeleid (BELSPO) — Space Research and Applications
cc: Ministerie van Defensie (DIRS) waar van toepassing
via https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — Belgische ESA/ruimte kasstromen CM25

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik:

1. Cash-by-year 2025-2030 van de Belgische ESA-inschrijvingen, gesplitst
   **civiel (BELSPO)** vs **Defensie (MoD)**, per programma-cluster
   (Basic, Science, PRODEX, GSTP, EO, ARTES, navigatie, transport, …).
2. Status en bevestiging van **TBA/conditionele** bedragen (o.a. GSTP ~79,9 m
   TBA-class; PRODEX 75 m conditioneel) na Ministerraad uiterlijk 31/01/2026.
3. Planning van de **one-off 400 m€** (2026 en 2028) per jaar.
4. Indien beschikbaar: top contractanten per programma (aggregaat).

Publiek (BELSPO debrief CM-ESA Bremen 5 dec 2025):
- Totaal BE space 2025-30: **1.845 m€** (1.277 + 168 MoD + 400 one-off)
- ESA CM25 BE: **1.109 m€** incl. MoD
- MoD invest space 2026-34: **617 m€**

Dossierreferentie intern: gap_be_space_cm25_cash_l5

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] BELSPO Space / Defensie / IBZ
- [x] Concrete cash split + TBA
- [x] foi_queue ready
- [ ] Human send
""",
    encoding="utf-8",
)

# also refresh gap_esa_be_optional if exists
foi = (root / "foi_queue.csv").read_text(encoding="utf-8")
if "gap_esa_be_optional_l5" in foi:
    foi2 = re.sub(
        r"(gap_esa_be_optional_l5,[^\n]+)",
        lambda m: m.group(1)
        if "tick338" in m.group(1)
        else m.group(1).rstrip()
        + " | tick338: CM25 multi-year 1109m/1845m filled package; residual cash L5 still ready",
        foi,
        count=1,
    )
    # simpler append note via replace last part of notes field - skip if fragile
    (root / "foi_queue.csv").write_text(foi, encoding="utf-8")

# research queue
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_329,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-31T07:15:00Z,,Spawned tick337 after STEREO IV; rq_116 SWA deferred"
)
new = (
    "rq_329,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_be_space_cm25_cash_l5,"
    f"2026-07-31T07:15:00Z,{now},"
    "tick338: BE space CM25 1845m dual Belspo+MoD ESA 1109m; FOI cash L5; spawn rq_330 progress@340 soon"
)
if old not in rq:
    raise SystemExit("rq_329 not found")
rq = rq.replace(old, new)
if "rq_330" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_330,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Note progress@340 in 2 ticks.,,"
        f"{now},,Spawned tick338 after BE ESA CM25 package; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_329,338,no,"
    "Scheduler 60s. Next prio5 rq_330; progress@340 in 2 ticks; rq_116 SWA deferred. tick338 CM25 space 1845m.\n",
    encoding="utf-8",
)

print("OK tick338")

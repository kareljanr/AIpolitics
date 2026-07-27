# -*- coding: utf-8 -*-
"""Tick 157 — rq_147 Defence major contracts L5 named."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 157
UNIT = "rq_147"
UTC = "2026-07-28T02:05:00Z"
GAP = "gap_defence_contract_cash"


def read_text(p: Path) -> str:
    raw = p.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def write_text(p: Path, text: str) -> None:
    p.write_bytes(text.encode("utf-8", errors="replace"))


def append_if_missing(p: Path, rows: list[str]) -> None:
    text = read_text(p)
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        if row.split(",", 1)[0] not in text:
            text += row + "\n"
    write_text(p, text)


def replace_line_startswith(p: Path, prefix: str, new_line: str) -> bool:
    text = read_text(p)
    lines = text.splitlines()
    out, found = [], False
    for L in lines:
        if L.startswith(prefix):
            out.append(new_line)
            found = True
        else:
            out.append(L)
    write_text(p, "\n".join(out) + "\n")
    return found


srcs = [
    'src_defensie_sv_2025,Strategische Visie Defensie 2025 integraal mil.be,https://www.mil.be/media/ulunodln/strategische-visie-2025-integraal.pdf,Defensie / Belgische regering,2026-07-28,official_strategy,"Capacity portfolio 2026-34 commit 33.784bn pay 24.661bn Cst26; F-35 +11 1.672bn; 3rd ASWF 1.270bn; NASAMS 2.032bn; tick157"',
    'src_coa_wederuitrusting_2025,Rekenhof 2025_16 Wederuitrusting gemotoriseerde capaciteit Defensie,https://www.ccrek.be/sites/default/files/Docs/2025_16_WederuitrustingDefensie.pdf,Rekenhof Cour des comptes,2026-07-28,official_audit,"Camo Griffon/Jaguar 1.575bn; lifecycle >=14.7bn 25y; STAR +11.2bn; draft budget 2025 12.9bn commit 10.5bn pay; tick157"',
]
append_if_missing(DATA / "sources.csv", srcs)

ents = [
    "mod_defensie,Ministerie van Landsverdediging / Defensie,Ministere de la Defense,Belgian Ministry of Defence,ministry,sec_federal,bi,https://www.mil.be,,Brussels,SV2025 capacity 33.8bn commit 2026-34; 2pct GDP path; tick157",
]
# may already exist - append_if_missing checks id
append_if_missing(DATA / "entities.csv", ents)

bud = [
    # Portfolio totals SV
    "bud_def_capacity_commit_2026_34,mod_defensie,2026,33784153531,,,commitment,src_defensie_sv_2025,strong,SV2025 annex C total vastlegging 2026-2034 EUR 33.784bn constant 2026",
    "bud_def_capacity_pay_2026_34,mod_defensie,2026,24661004760,,,budgeted,src_defensie_sv_2025,strong,SV2025 total vereffening 2026-2034 EUR 24.661bn Cst26",
    "bud_def_air_commit_2026_34,mod_defensie,2026,10280805049,,,commitment,src_defensie_sv_2025,strong,Air dimension commit 10.281bn 2026-34",
    "bud_def_land_commit_2026_34,mod_defensie,2026,13862344826,,,commitment,src_defensie_sv_2025,strong,Land dimension commit 13.862bn",
    "bud_def_maritime_commit_2026_34,mod_defensie,2026,3429737355,,,commitment,src_defensie_sv_2025,strong,Maritime commit 3.430bn",
    "bud_def_ici_commit_2026_34,mod_defensie,2026,3527691311,,,commitment,src_defensie_sv_2025,strong,ICI cyber-intel commit 3.528bn",
    "bud_def_comdo_commit_2026_34,mod_defensie,2026,2683574990,,,commitment,src_defensie_sv_2025,strong,Command and ops support commit 2.684bn",
    # Named L5 Air
    "bud_def_f35_extra11_2026,mod_defensie,2026,1672258720,,,commitment,src_defensie_sv_2025,strong,Air combat multirole 11EA F-35 incl mission equipment 1.672bn Cst26 first year 2026",
    "bud_def_f35_support_2026,mod_defensie,2026,445104480,,,commitment,src_defensie_sv_2025,strong,F-35 support equipment spare parts config updates 445.1m",
    "bud_def_nasams_10fu_2026,mod_defensie,2026,2032400000,,,commitment,src_defensie_sv_2025,strong,SBAMD short/medium NASAMS 10 firing units 2.032bn",
    "bud_def_sbamd_long_3fu_2029,mod_defensie,2029,1981590000,,,commitment,src_defensie_sv_2025,strong,SBAMD long-range 3 firing units 1.982bn first year 2029",
    "bud_def_sar_heli4_2026,mod_defensie,2026,193071489,,,commitment,src_defensie_sv_2025,strong,SAR helicopters 4EA 193.1m",
    "bud_def_afsc_awacs_2026,mod_defensie,2026,580443033,,,commitment,src_defensie_sv_2025,strong,Alliance Future Surveillance Control incl AWACS update 580.4m",
    # Named L5 Maritime
    "bud_def_aswf3_2026,mod_defensie,2026,1270250000,,,commitment,src_defensie_sv_2025,strong,3rd Anti-Submarine Warfare Frigate ASWF 1.270bn commit / 1.223bn pay",
    "bud_def_aswf_updates_2029,mod_defensie,2029,545213400,,,commitment,src_defensie_sv_2025,strong,ASWF updates upgrades support 545.2m",
    "bud_def_mcm_toolboxes_2026,mod_defensie,2026,656987876,,,commitment,src_defensie_sv_2025,strong,MCM Toolboxes 657.0m",
    "bud_def_mcmv_updates_2026,mod_defensie,2026,211877700,,,commitment,src_defensie_sv_2025,strong,MCMV updates upgrades additional material 211.9m",
    "bud_def_logistics_ship_2033,mod_defensie,2033,274374000,,,commitment,src_defensie_sv_2025,strong,Logistic Support Ship 274.4m first year 2033",
    # CoA Camo / STAR
    "bud_def_camo_griffon_jaguar_2018,mod_defensie,2018,1575000000,,,commitment,src_coa_wederuitrusting_2025,strong,Camo contract 18LP100 382 Griffon + 60 Jaguar 1.575bn current EUR investment",
    "bud_def_motorized_lifecycle_25y,mod_defensie,2024,14700000000,,,estimate,src_coa_wederuitrusting_2025,strong,Lifecycle cost motorized capacity investments 2018+2022 min 14.7bn over 25y 2024 prices incl ops munition infra",
    "bud_def_star_extra_2023_30,mod_defensie,2023,11176070000,,,commitment,src_coa_wederuitrusting_2025,strong,STAR military programming law +11.176bn constant 2022 for investments 2023-2030",
    "bud_def_star_motorized_extra,mod_defensie,2023,4780000000,,,commitment,src_coa_wederuitrusting_2025,strong,STAR extra motorized capacity envelope 4.78bn",
    "bud_def_sv2016_weapons_9_2bn,mod_defensie,2016,9200000000,,,commitment,src_coa_wederuitrusting_2025,strong,SV2016 weapons systems envelope 9.2bn class",
    "bud_def_budget_2025_commit,mod_defensie,2025,12900000000,,,budgeted,src_coa_wederuitrusting_2025,strong,Draft budget 2025 Defensie 12.9bn vastleggingen / 10.5bn vereffeningen (CoA)",
    "bud_def_budget_2025_pay,mod_defensie,2025,10500000000,,,budgeted,src_coa_wederuitrusting_2025,strong,Draft budget 2025 liquidation credits 10.5bn",
    "bud_def_knds_maint_to_2055,mod_defensie,2025,1488000000,,,commitment,src_coa_wederuitrusting_2025,medium,KNDS maintenance related path class 1.488bn to 2055 incl 248m spare stock 2025-28",
]
append_if_missing(DATA / "budgets.csv", bud)

cmts = [
    (
        'cmt_def_capacity_portfolio_2026_34,Defence capacity investment portfolio SV2025 2026-2034,mod_defensie,Belgian Armed Forces / industry partners,'
        'Strategische Visie Defensie 2025 annex C + military programming,2025-07-18,2026,2034,33784153531,'
        '"{""commit_total"":33784153531,""pay_total"":24661004760,""air"":10280805049,""land"":13862344826,'
        '""maritime"":3429737355,""ici"":3527691311,""comdo"":2683574990,""currency"":""EUR_constant_2026"",'
        '""f35_extra11"":1672258720,""aswf3"":1270250000,""nasams10"":2032400000,""sbamd_long3"":1981590000,'
        '""mcm_toolboxes"":656987876,""gdp_path"":""2pct_to_2033_then_2.5pct_2034""}",0,active,'
        'https://www.mil.be/media/ulunodln/strategische-visie-2025-integraal.pdf,NATO collective defence readiness,'
        'Publish signed contract cash-by-year; track industrial return; unit cost deliverables,'
        'src_defensie_sv_2025,strong,Federal>Defensie>SV2025_capacity,'
        'tick157; programming commitments not all signed contracts yet'
    ),
    (
        'cmt_def_camo_griffon_jaguar,Camo Griffon Jaguar motorized rearmament,mod_defensie,KNDS France partnership,'
        'Intergovernmental agreement France Nov 2018 + CoA 2025_16,2018-11-07,2018,2030,1575000000,'
        '"{""vehicles"":""382_Griffon_60_Jaguar"",""invest_commitment"":1575000000,""lifecycle_25y_min"":14700000000,'
        '""star_motorized_extra"":4780000000,""caesar_batch_2018_path"":""9_systems_May2022_in_partnership"",'
        '""maint_annual_class"":60000000}",0,active,'
        'https://www.ccrek.be/sites/default/files/Docs/2025_16_WederuitrustingDefensie.pdf,'
        'Motorized brigade interoperability France NATO,Open lifecycle cash; industrial return evaluation CoA critical,'
        'src_coa_wederuitrusting_2025,strong,Federal>Defensie>Camo,'
        'tick157; CoA flags incomplete lifecycle at decision; TCO 14.7bn strong'
    ),
    (
        'cmt_def_f35_extra11,F-35A additional 11 aircraft package SV2025,mod_defensie,Lockheed Martin / European production path,'
        'SV2025 Air Combat Multirole line,2025-07-18,2026,2034,1672258720,'
        '"{""aircraft"":11,""mission_equipment_package"":1672258720,""support_spares"":445104480,'
        '""prior_order"":34,""total_fleet_target"":45,""note"":""contract signing targeted 2026 per minister statements medium""}",0,active,'
        'https://www.mil.be/media/ulunodln/strategische-visie-2025-integraal.pdf,Air combat multirole NATO QRA,'
        'Publish signed contract vs SV line; industrial return; operating cost series,'
        'src_defensie_sv_2025,strong,Federal>Defensie>F35,'
        'tick157; SV programming amount strong; signed price residual FOI'
    ),
    (
        'cmt_def_aswf3_frigate,Third ASWF anti-submarine frigate,mod_defensie,BENESAM Netherlands shipbuilding,'
        'SV2025 Maritime Surface Combatant,2025-07-18,2026,2034,1270250000,'
        '"{""commit"":1270250000,""pay"":1223250000,""updates_support"":545213400,""note"":""unit cost press cites escalation to >1.3bn; RFI alternatives Jul 2026 medium""}",0,active,'
        'https://www.mil.be/media/ulunodln/strategische-visie-2025-integraal.pdf,Naval ASW permanent frigate presence,'
        'Confirm signed price path; delay risk; dual NL programme governance,'
        'src_defensie_sv_2025,strong,Federal>Defensie>ASWF,'
        'tick157'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

lbs = [
    "lb_def_capacity_33bn,Defence capacity portfolio ~33.8bn commit 2026-34,federal,programme,Federal>Defensie>SV2025,33784153531,24661004760,SV strong: commit 33.784bn pay 24.661bn Cst26; Land 13.9 Air 10.3 Maritime 3.4; 2pct GDP path,strong,src_defensie_sv_2025,NATO collective defence Belgian public,Force modernization readiness,Core security mandate; TCO and delivery risk not pure waste,3,9.5,5,6.8,Publish cash delivery vs plan; industrial return; unit readiness KPIs,seed,,tick157",
    "lb_def_f35_extra11,F-35 +11 package ~1.67bn SV2025,federal,procurement,Federal>Defensie>F35_extra,1672258720,2117363200,SV: aircraft+mission eq 1.672bn + support 0.445bn; prior 34 aircraft; total fleet 45 target,strong,src_defensie_sv_2025,Air force NATO QRA,Air combat multirole,Large single platform concentration; signed price residual,4,8.0,5,6.3,FOI signed contract cash series; O&M path; industrial return audit,seed,,tick157",
    "lb_def_camo_lifecycle,Camo motorized lifecycle TCO >=14.7bn,federal,procurement,Federal>Defensie>Camo_TCO,14700000000,14700000000,CoA strong: invest 1.575bn vehicles + lifecycle ops munition infra min 14.7bn/25y 2024 prices; STAR motorized +4.78bn,strong,src_coa_wederuitrusting_2025,Land component brigade,Motorized capability France partnership,CoA: lifecycle not estimated at decision; maintenance price risk,5,9.0,5,7.0,Full lifecycle cash table; dual France dependency clauses; return evaluation,seed,,tick157",
    "lb_def_nasams_sbamd,NASAMS SBAMD short/medium 10 FU ~2.03bn,federal,procurement,Federal>Defensie>NASAMS,2032400000,4013990000,SV: 10 short/medium FU 2.032bn + long-range 3 FU 1.982bn = SBAMD 4.014bn commit,strong,src_defensie_sv_2025,National territory critical infra,Ground-based air missile defence,New capability gap fill; dual with NL Benelux,3,8.0,5,6.0,FOI tender award values; munition stock path,seed,,tick157",
    "lb_def_aswf3,3rd ASWF frigate ~1.27bn,federal,procurement,Federal>Defensie>ASWF3,1270250000,1815463400,SV: frigate 1.270bn + updates 0.545bn; BENESAM NL; delay/cost risk press class,strong,src_defensie_sv_2025,Navy permanent sea presence,Anti-submarine surface combatant,Programme delay risk; dual NL build,4,7.5,5,6.0,Confirm signed price; RFI alternatives path; schedule risk,seed,,tick157",
]
append_if_missing(DATA / "leaderboard.csv", lbs)

foi_row = (
    f"{GAP},Federal>Defensie>contracts>cash_by_year_L5,mod_defensie,"
    "Signed contract values and cash-by-year 2018-2034 for F-35 original 34 + extra 11; Camo 18LP100; CAESAR batches; rMCM Belgium share; ASWF 1-3; NASAMS/SBAMD awards; industrial return EUR realized,"
    "SV2025 and CoA give strong programming and Camo invest totals; many lines still planned not signed cash series,"
    "7,Defensie openbaarheid / Kamer Defensiecommissie / Rekenhof,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-07-28,,,,,"
    "cmt_def_capacity_portfolio_2026_34|cmt_def_camo_griffon_jaguar|cmt_def_f35_extra11,lb_def_capacity_33bn,"
    f"{UTC},{UTC},tick157 partial SV+CoA fill; residual signed cash FOI"
)
text_f = read_text(DATA / "foi_queue.csv")
if GAP not in text_f:
    if not text_f.endswith("\n"):
        text_f += "\n"
    write_text(DATA / "foi_queue.csv", text_f + foi_row + "\n")

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(f"""# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `{GAP}`  
**Status:** ready (human send only)  
**Linked:** {UNIT}

---

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Ministerie van Landsverdediging — dienst openbaarheid van bestuur
     en/of Kamercommissie Landsverdediging
     (federaal ook: https://www.ibz.be/nl/openbaarheid-van-bestuur)

Betreft: Verzoek om openbaarmaking — cash-by-year grote Defensiecontracten 2018-2034

Geachte,

Op grond van de wet 11 april 1994 inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Getekende contractbedragen en cash-by-year (vastlegging/vereffening) 2018-2034 voor:
   - F-35A oorspronkelijke 34 toestellen + geplande 11 extra (inclusief mission equipment);
   - Camo / 18LP100 (Griffon/Jaguar) en onderhoudscontracten KNDS;
   - CAESAR-batches (9 + latere uitbreidingen / NG);
   - rMCM / City-class (Belgisch aandeel van het binational programma);
   - ASWF-fregatten (1-3) en updates;
   - NASAMS (10 FU) en long-range SBAMD (3 FU) indien gegund.
2. Gerealiseerde industriële return (EUR) per groot programma 2018-2025.
3. Reconciliatie van de SV2025-programmeringslijnen (Cst26) met effectief getekende
   contracten voor de 11 F-35 en het 3e ASWF-fregat.

Periode: 2018-01-01 tot meest recente stand.

### 2. Context

Strategische Visie 2025 en Rekenhof 2025_16 publiceren sterke programmerings- en
Camo-totalen (portfolio 33,8 mrd vastlegging 2026-34; Camo 1,575 mrd; F-35 +11 1,672 mrd;
3e ASWF 1,270 mrd). Ontbrekend: getekende cash-series per contract.

Hierarchie intern: Federal > Defensie > contracts L5.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {GAP}

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling (Defensie)
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends. Classified annexes may be redacted.
""", encoding="utf-8")

rq_new = (
    f"rq_147,Defence major contracts L5 named if public,continuous,5,done,L5,mod_defensie,"
    f'"Named large defence contracts public tender.",{GAP},2026-07-27T14:00:00Z,{UTC},'
    "tick157: SV2025 portfolio 33.8bn commit; F-35+11 1.67bn; ASWF3 1.27bn; NASAMS 2.03bn; "
    "Camo 1.575bn TCO>=14.7bn CoA; residual signed cash FOI"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_147,", rq_new):
    raise SystemExit("rq_147 not found")

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio5 justice police hole-fill; FOI ready human send. rq_147 defence L5 contracts done."\n',
)

log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Defence major contracts L5 named)
- Found (strong primary SV2025 + Rekenhof 2025_16):
  - **Portfolio 2026-34 (Cst26):** commit **EUR 33.784bn** · pay **24.661bn** (Land 13.9 · Air 10.3 · Maritime 3.4 · ICI 3.5 · Comdo 2.7).
  - **Named L5 (SV):** F-35 **+11** **1.672bn** (+ support **445m**) · 3rd **ASWF** **1.270bn** · **NASAMS** 10 FU **2.032bn** · SBAMD long 3 FU **1.982bn** · MCM toolboxes **657m** · SAR heli 4 **193m**.
  - **Camo (CoA):** 382 Griffon + 60 Jaguar **1.575bn** invest · lifecycle TCO **≥14.7bn**/25y · STAR motorized extra **4.78bn** · STAR law **+11.176bn** 2023-30.
  - **Budget 2025 draft (CoA):** commit **12.9bn** / pay **10.5bn**; 2% GDP path from 2025.
- Wrote: sources 2; budgets ~25; cmt 4; lb 5; rq_147=done; FOI residual ready.
- FOI: {GAP} (signed cash-by-year major contracts) human send only.
- Next: prio5 **rq_150 justice** / **rq_151 police** / **rq_121 hole-fill**.
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)
print("OK tick", TICK, UNIT)

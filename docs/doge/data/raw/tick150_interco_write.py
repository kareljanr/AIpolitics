# -*- coding: utf-8 -*-
"""Tick 150: rq_142 Intercommunales top public transfers BE sample."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T23:35:00Z"
TICK = 150
UNIT = "rq_142"


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1"), "latin-1"


def write_text(path: Path, text: str, enc: str) -> None:
    path.write_bytes(text.encode(enc, errors="replace"))


def append_lines(path: Path, lines: list[str]) -> None:
    text, enc = read_text(path)
    if not text.endswith("\n"):
        text += "\n"
    write_text(path, text + "\n".join(lines) + "\n", enc)


append_lines(DATA / "sources.csv", [
    'src_fluvius_investor_2025,Fluvius Economic Group investor update financial results 2025,https://over.fluvius.be/sites/fluvius/files/2026-03/update-investors-annual-report-2025.pdf,Fluvius,2026-07-27,annual_report,"EG ops rev 4597m 2025 / 3797m 2024; EBITDA 1107/900; CAPEX 1780/1557; result 182/113; equity 7270; debt interest-bearing 10361; VL equity strengthen up to 1.56bn PMV path; invest plan ~11bn/10y"',
    'src_spge_rapport_2024,SPGE rapport annuel en bref 2024,https://rapportannuelspge.be/en-bref/,SPGE,2026-07-27,annual_report,"CA 418m 2024; invest >200m 2024; cum invest 5.221bn; debt 1.581bn end-2024; equipment rate 92.3pct"',
    'src_aquafin_jv_esg_2024,Aquafin jaarverslag 2024 project volumes,https://esgdistrict.tijd.be/media/Jaarverslag-2024_DEFNL.pdf,Aquafin,2026-07-27,annual_report,"Project delivery 174m 2024; target 180m 2025; asset mgmt 54.3m 2024; infra replacement value ~10bn; new projects market 334m 2024"',
    'src_vl_aquafin_lokaal_pact_500m,VR Aquafin Lokaal Pact extension municipal sewers 500m 2026-2030,https://www.vlaanderen.be/vlaamse-regering/beslissingen-van-de-vlaamse-regering/verlenging-overname-investeringskosten-door-vlaams-gewest-voor-heraanleg-gemeentelijke-rioleringen,Vlaamse Regering,2026-07-27,government,"500m over 5y 2026-2030 Aquafin takeover municipal sewer invest costs"',
    'src_bru_vivaqua_180m,Brussels Times BCR 180m Vivaqua capital stake 49pct,https://www.brusselstimes.com/2187372/brussels-buys-half-of-vivaqua-to-gain-greater-control-over-water-policy,Brussels Times,2026-07-27,news,"BCR invest 180m for 49pct Vivaqua; aligns with CoA finops Vivaqua 180m path"',
])

append_lines(DATA / "budgets.csv", [
    # Fluvius Economic Group
    "bud_fluvius_ops_rev_2024,fluvius,2024,3797000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG operating revenue 2024",
    "bud_fluvius_ops_rev_2025,fluvius,2025,4597000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG operating revenue 2025 (+799m tariffs)",
    "bud_fluvius_ebitda_2025,fluvius,2025,1107000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG EBITDA 2025",
    "bud_fluvius_capex_2024,fluvius,2024,1557000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG CAPEX 2024",
    "bud_fluvius_capex_2025,fluvius,2025,1780000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG CAPEX 2025",
    "bud_fluvius_result_2025,fluvius,2025,182000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG net result 2025",
    "bud_fluvius_equity_2025,fluvius,2025,7270000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG equity end-2025",
    "bud_fluvius_debt_2025,fluvius,2025,10361000000,,,outturn,src_fluvius_investor_2025,strong,Fluvius EG interest-bearing loans end-2025",
    "bud_fluvius_equity_strengthen_vl,fluvius,2026,1560000000,,,budgeted,src_fluvius_investor_2025,strong,VL Gov commit equity strengthen DSOs up to 1.56bn (PMV/municipal path; BA2026 VEK 1.1bn related)",
    # SPGE
    "bud_spge_ca_2024,spge,2024,418000000,,,outturn,src_spge_rapport_2024,strong,SPGE chiffre d affaires 2024",
    "bud_spge_invest_2024,spge,2024,200000000,,,outturn,src_spge_rapport_2024,strong,SPGE investments >200m 2024",
    "bud_spge_debt_2024,spge,2024,1581000000,,,outturn,src_spge_rapport_2024,strong,SPGE endettement end-2024 Moody A3",
    "bud_spge_cum_invest,spge,2024,5221000000,,,outturn,src_spge_rapport_2024,strong,SPGE cumulative invest since creation 5.221bn",
    # Aquafin
    "bud_aquafin_project_delivery_2024,aquafin,2024,174000000,,,outturn,src_aquafin_jv_esg_2024,strong,Aquafin investment+optimisation project delivery budget realized 174m 2024",
    "bud_aquafin_project_target_2025,aquafin,2025,180000000,,,budgeted,src_aquafin_jv_esg_2024,strong,Aquafin project delivery target 180m 2025",
    "bud_aquafin_asset_mgmt_2024,aquafin,2024,54300000,,,outturn,src_aquafin_jv_esg_2024,strong,Aquafin asset management projects delivered 54.3m 2024",
    "bud_aquafin_lokaal_pact_2026_30,aquafin,2026,500000000,,,commitment,src_vl_aquafin_lokaal_pact_500m,strong,Lokaal Pact municipal sewers Aquafin takeover 500m 2026-2030",
    # Brussels Vivaqua
    "bud_vivaqua_capital_bru_path,vivaqua,2026,180000000,,,budgeted,src_bru_vivaqua_180m,medium,BCR capital injection/stake Vivaqua 180m path (finops + press 49pct)",
    # NBB Flanders wastewater (from prior NBB table)
    "bud_fl_wastewater_d92_2024,vlaanderen_gov,2024,82000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,Flanders D.92 wastewater investment grants non-public 82m 2024 (NBB A4)",
])

append_lines(DATA / "commitments.csv", [
    'cmt_fluvius_eg_public_utility,Fluvius Economic Group multi-utility intercommunale path Flanders,fluvius,Flemish DSOs municipalities,Mission entrusted associations + tariff regulation VNR,2024-01-01,2024,2035,11000000000,"{""2024_ops_rev"":3797000000,""2025_ops_rev"":4597000000,""2024_capex"":1557000000,""2025_capex"":1780000000,""2025_ebitda"":1107000000,""2025_result"":182000000,""2025_equity"":7270000000,""2025_debt"":10361000000,""equity_strengthen_max"":1560000000,""invest_plan_10y"":11000000000,""dividend_payout_eled_gasd_pct"":60,""employees_2025"":5997,""note"":""tariff-financed public service DSO not pure subsidy; VL equity injection is public transfer""}",0,active,https://over.fluvius.be/sites/fluvius/files/2026-03/update-investors-annual-report-2025.pdf,Energy transition distribution grids Flanders,Track PMV equity stake cash; open municipal dividend path,src_fluvius_investor_2025,strong,Vlaanderen>Intercommunale>Fluvius,tick150 largest BE intercommunale class',
    'cmt_spge_assainissement,SPGE Walloon wastewater public financing,spge,Walloon municipalities OAA,SPGE public water management company,1999-01-01,2024,2024,5221000000,"{""2024_ca"":418000000,""2024_invest"":200000000,""cum_invest"":5221000000,""debt_2024"":1581000000,""equipment_rate_pct"":92.3}",0,active,https://rapportannuelspge.be/en-bref/,Wastewater sanitation Wallonia,Publish annual OAA L5 transfers; tariff path transparency,src_spge_rapport_2024,strong,Wallonie>Intercommunale>SPGE,tick150',
    'cmt_aquafin_infra_path,Aquafin Flanders wastewater infrastructure path,aquafin,Flemish Region municipalities,Aquafin NV tasks of general interest + Lokaal Pact,2008-01-01,2024,2030,500000000,"{""2024_project_delivery"":174000000,""2025_target"":180000000,""2024_asset_mgmt"":54300000,""lokaal_pact_2026_30"":500000000,""infra_replacement_value_class"":10000000000,""note"":""user tariffs + Minafonds via water companies; VL co-debtor""}",0,active,https://www.aquafin.be/nl/investor-relations/jaarverslagen,Wastewater treatment Flanders,Open annual public vs tariff cost split,src_aquafin_jv_esg_2024,strong,Vlaanderen>Intercommunale>Aquafin,tick150',
    'cmt_vivaqua_bru_capital,Vivaqua Brussels water capital injection path,vivaqua,Vivaqua / BCR communes,BCR finops + capital stake decision,2026-01-01,2026,2029,180000000,"{""finops_envelope"":180000000,""stake_49pct_claim"":true}",0,active,https://www.brusselstimes.com/2187372/brussels-buys-half-of-vivaqua-to-gain-greater-control-over-water-policy,Public control water distribution Brussels,Confirm cash-by-year and governance,src_bru_vivaqua_180m,medium,Bruxelles>Intercommunale>Vivaqua,tick150; medium until official decree PDF',
])

append_lines(DATA / "leaderboard.csv", [
    "lb_fluvius_public_utility,Fluvius EG ops rev ~4.6bn CAPEX 1.8bn 2025 + VL equity up to 1.56bn,Flanders,ops,Vlaanderen>Fluvius,4597000000,11000000000,Investor update strong: tariff-financed DSO; VL equity strengthen 1.56bn is public transfer; CAPEX path energy transition,strong,src_fluvius_investor_2025,Flemish households municipalities,Electricity gas multi-utility grids,Core infrastructure not pure waste; municipal dividends + PMV stake governance risk,4,9.0,6,6.0,Open dividend cash-by-municipality; deliver EQ/RAB 40pct without over-equity,seed,,tick150",
    "lb_spge_aquafin_water,SPGE+Aquafin wastewater public infrastructure ~0.4-0.6bn/yr class,multi,ops,BE>Water>intercommunales,418000000,5221000000,SPGE CA 418m invest 200m 2024 strong; Aquafin project 174m + Lokaal Pact 500m 2026-30; dual regional water utilities,strong,src_spge_rapport_2024,Households businesses BE,Wastewater sanitation,Core environmental infrastructure; tariff+public co-finance,3,8.0,6,5.3,Publish dual VL-WAL unit cost benchmarks; open L5 OAA lists,seed,,tick150",
])

etext, _ = read_text(DATA / "entities.csv")
for line in [
    "fluvius,Fluvius Economic Group / System Operator,Fluvius,Flemish multi-utility DSO intercommunale group,intercommunale,sec_flanders,nl,https://over.fluvius.be,,,Ops rev 4.6bn 2025; CAPEX 1.78bn; equity strengthen path 1.56bn",
    "spge,Societe Publique de Gestion de l Eau,Societe Publique de Gestion de l Eau,Walloon public wastewater company,intercommunale,sec_wallonia,fr,https://www.spge.be,,,CA 418m 2024; cum invest 5.22bn; debt 1.58bn",
    "aquafin,Aquafin NV,Aquafin NV,Flemish wastewater treatment company,parastatal,sec_flanders,nl,https://www.aquafin.be,,,Project delivery 174m 2024; Lokaal Pact 500m 2026-30; infra ~10bn replacement",
    "vivaqua,Vivaqua,Vivaqua,Brussels water distribution intercommunale,intercommunale,sec_brussels,bi,https://www.vivaqua.be,,,BCR capital path 180m; 49pct stake claim",
]:
    eid = line.split(",")[0]
    if not any(l.startswith(eid + ",") for l in etext.splitlines()):
        append_lines(DATA / "entities.csv", [line])
        etext, _ = read_text(DATA / "entities.csv")

rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_142,Intercommunales top 20 public transfers BE,continuous,6,open,L5,gg_belgium,'
    '"Largest intercommunale subsidies or dividends path.",'
    ",2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,"
)
new = (
    'rq_142,Intercommunales top 20 public transfers BE,continuous,6,done,L5,gg_belgium,'
    '"Largest intercommunale subsidies or dividends path.",'
    "gap_interco_dividends_l5,2026-07-27T14:00:00Z,2026-07-27T23:35:00Z,"
    '"tick150: Fluvius 4.6bn rev CAPEX 1.8bn; SPGE 418m; Aquafin 174m+500m pact; Vivaqua 180m; FOI dividends"'
)
if old not in rtext:
    raise SystemExit("rq_142 OLD NOT FOUND:\n" + "\n".join(l for l in rtext.splitlines() if "rq_142" in l))
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_interco_dividends_l5.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_interco_dividends_l5`  
**Status:** ready (human send only)  
**Linked:** rq_142 · cmt_fluvius_eg_public_utility · lb_fluvius_public_utility

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Fluvius System Operator / PMV
     Team Openbaarheid Vlaanderen openbaarheid@vlaanderen.be
     et/ou SPGE / Aquafin / SPRB Bruxelles

Betreft: Verzoek om openbaarmaking — intercommunale transfers en dividenden 2023-2026

Geachte,

Op grond van het Bestuursdecreet / publicite de l administration
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Dividenden uitgekeerd door Fluvius DSOs / Fluvius EG aan gemeenten 2023-2026
   (cash-by-year per gemeente of per DSO).
2. Cash-by-year van de Vlaamse equity-versterking Fluvius/PMV (envelope max 1,56 bn):
   bedragen, aandeelhouders, timing.
3. Aquafin: splitsing publieke Minafonds/Gewest-bijdrage vs drinkwaterfactuur 2023-2026.
4. SPGE: transfers naar OAA / communes 2023-2026 top-20.
5. Vivaqua: officiële BCR-kapitaalinjectie beslissing + cash kalender.

Periode: 2023-01-01 tot meest recente stand.

### 2. Context

Primair: Fluvius EG ops 4,6 bn / CAPEX 1,8 bn 2025; SPGE CA 418m; Aquafin projecten
174m + Lokaal Pact 500m. Ontbrekend: gemeentelijke dividend-L5 en volledige public-
transfer matrix.

Hierarchie: BE > Intercommunales > public transfers.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: gap_interco_dividends_l5

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
""",
    encoding="utf-8",
    newline="\n",
)

append_lines(DATA / "foi_queue.csv", [
    "gap_interco_dividends_l5,BE>Intercommunales>dividends_public_transfers,fluvius,Municipal dividends Fluvius DSOs 2023-2026; VL PMV equity cash schedule max 1.56bn; Aquafin public vs tariff split; SPGE OAA top-20; Vivaqua BCR capital calendar,Entity totals strong; L5 municipal cash opaque,6,Fluvius PMV / Team Openbaarheid + SPGE Aquafin SPRB,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_interco_dividends_l5.md,ready,2026-07-27,,,,,cmt_fluvius_eg_public_utility,lb_fluvius_public_utility,2026-07-27T23:35:00Z,2026-07-27T23:35:00Z,tick150 partial; human send",
])

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 climate Charleroi Myria; FOI ready human send. rq_142 intercommunales done."\n',
    "utf-8",
)

log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Intercommunales top public transfers sample)
- Found (strong Fluvius investor + SPGE + Aquafin + BCR path):
  - **Fluvius EG:** ops rev **EUR 3.80bn 2024 / 4.60bn 2025**; CAPEX **1.56 / 1.78bn**; EBITDA **1.11bn**; result **182m**; debt **10.4bn**; equity strengthen path **up to 1.56bn** VL/PMV; 10y invest plan **~11bn**.
  - **SPGE (WAL water):** CA **EUR 418m 2024**; invest **>200m**; cum invest **5.22bn**; debt **1.58bn**.
  - **Aquafin (VL water):** project delivery **174m 2024 / target 180m 2025**; asset mgmt **54.3m**; **Lokaal Pact 500m 2026-30**.
  - **Vivaqua (BRU):** capital path **EUR 180m** (finops + 49pct stake claim medium).
  - NBB FL wastewater D.92 **82m 2024**.
- Wrote: sources 5; budgets 19; cmt 4; lb 2; entities 4; rq_142=done; FOI residual ready.
- FOI: gap_interco_dividends_l5 (municipal dividends + equity cash) human send.
- Next: prio6 **rq_148 climate** / **rq_144 Charleroi** / **rq_120 Myria**.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick150 write OK")

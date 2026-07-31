# -*- coding: utf-8 -*-
"""Tick 151: rq_148 Climate/energy named subsidies beyond offshore."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T23:55:00Z"
TICK = 151
UNIT = "rq_148"


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
    'src_ccrek_hernieuwbare_vl_2025,Rekenhof Hernieuwbare energie in Vlaanderen 2025 Table10 support 2014-2023,https://www.ccrek.be/sites/default/files/Docs/2025_34_HernieuwbareEnergieVL.pdf,Rekenhof,2026-07-27,court_of_audit,"Total support 12.97bn 2014-23; GSC 10.508bn; WKC 1.785bn; netbeheerder heat premiums 112m; call groene warmte 109m; PV premie 158m; retro 159m; call groene stroom 37m; only ~1.8bn on VL budget rest on bill"',
    'src_vnr_odv_horch_2025,VNR answer Horch VI6 ODV REG GSC WKC costs Fluvius Nov 2025,https://docs.vlaamsparlement.be/pfile?id=2250200,Vlaamse Nutsregulator,2026-07-27,regulator,"VL Gewest vergoeding GSC: 91.5m 2021 148m 2022 148m 2023 67m 2024 0 2025; WKC 0 until 25m 2024 60m 2025; REG/GSC net cost charts (digit FOI)"',
    'src_fluvius_gsc_inventory_2025,Fluvius investor update GEC CHP inventory + certificate costs,https://over.fluvius.be/sites/fluvius/files/2026-03/update-investors-annual-report-2025.pdf,Fluvius,2026-07-27,annual_report,"GEC+CHP inventory 602m end-2025 (521m CHP); certificate costs +149m y/y 2025"',
])

append_lines(DATA / "budgets.csv", [
    # CoA GSC multi-year
    "bud_vl_gsc_2021,vlaanderen_gov,2021,996000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders GSC support 996m 2021 CoA T10",
    "bud_vl_gsc_2022,vlaanderen_gov,2022,1030000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders GSC support 1030m 2022",
    "bud_vl_gsc_2023,vlaanderen_gov,2023,822000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders GSC support 822m 2023 CoA (NBB green cert 956m broader)",
    "bud_vl_gsc_cum_2014_23,vlaanderen_gov,2023,10508000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders GSC cumulative 10.508bn 2014-2023",
    # WKC
    "bud_vl_wkc_2021,vlaanderen_gov,2021,236000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders WKC CHP certificates 236m 2021",
    "bud_vl_wkc_2022,vlaanderen_gov,2022,185000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders WKC 185m 2022",
    "bud_vl_wkc_2023,vlaanderen_gov,2023,174000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders WKC 174m 2023",
    "bud_vl_wkc_cum_2014_23,vlaanderen_gov,2023,1785000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Flanders WKC cum 1.785bn 2014-2023",
    # Heat pump / netbeheerder premiums
    "bud_vl_heat_premiums_2023,vlaanderen_gov,2023,22000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Netbeheerder heat pump solar boiler boiler premiums 22m 2023",
    "bud_vl_heat_premiums_cum_2014_23,vlaanderen_gov,2023,112000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Netbeheerder heat premiums cum 112m 2014-2023 (incl warmtepomp)",
    # Other named instruments
    "bud_vl_call_groene_warmte_cum,vlaanderen_gov,2023,109000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Call groene warmte cum 109m 2014-2023 (70.4m in 2021-23)",
    "bud_vl_call_groene_stroom_cum,vlaanderen_gov,2023,37000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Call groene stroom project support 37.1m 2018-2023",
    "bud_vl_pv_premie_cum,vlaanderen_gov,2023,158000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,PV premie cum 158m (spike 126m 2023 class)",
    "bud_vl_retro_invest_premie_cum,vlaanderen_gov,2023,159000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Retroactieve investeringspremie cum 159m",
    "bud_vl_warmtenet_adhoc_cum,vlaanderen_gov,2023,53500000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Ad hoc warmtenetten subsidies 53.5m 2017-2022",
    "bud_vl_res_support_total_2023,vlaanderen_gov,2023,1174000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Total Flanders renewable support 1.174bn 2023 CoA T10",
    "bud_vl_res_support_cum_2014_23,vlaanderen_gov,2023,12970000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,Total Flanders renewable support 12.97bn 2014-2023 (~1.8bn on budget rest on electricity bill)",
    # VL Gewest compensation to DSO for certificates
    "bud_vl_gsc_vergoeding_dso_2021,vlaanderen_gov,2021,91512000,,,outturn,src_vnr_odv_horch_2025,strong,VL Gewest vergoeding GSC to electricity DSOs art 6.4.14",
    "bud_vl_gsc_vergoeding_dso_2022,vlaanderen_gov,2022,148000050,,,outturn,src_vnr_odv_horch_2025,strong,VL GSC vergoeding DSO 148.0m 2022",
    "bud_vl_gsc_vergoeding_dso_2023,vlaanderen_gov,2023,148000000,,,outturn,src_vnr_odv_horch_2025,strong,VL GSC vergoeding DSO 148.0m 2023",
    "bud_vl_gsc_vergoeding_dso_2024,vlaanderen_gov,2024,67000000,,,outturn,src_vnr_odv_horch_2025,strong,VL GSC vergoeding DSO 67.0m 2024 (then 0 2025 announced)",
    "bud_vl_wkc_vergoeding_dso_2024,vlaanderen_gov,2024,25000000,,,outturn,src_vnr_odv_horch_2025,strong,VL WKC vergoeding DSO 25.0m 2024",
    "bud_vl_wkc_vergoeding_dso_2025,vlaanderen_gov,2025,60000000,,,budgeted,src_vnr_odv_horch_2025,medium,VL WKC vergoeding DSO 60.0m 2025 announced",
    # Fluvius inventory
    "bud_fluvius_gec_chp_inventory_2025,fluvius,2025,602000000,,,outturn,src_fluvius_gsc_inventory_2025,strong,Fluvius GEC+CHP certificates inventory 602m EOY2025 (521m CHP)",
    # NBB residual (already partial) - green cert FL confirmed
    "bud_fl_green_cert_nbb_2023,vlaanderen_gov,2023,956000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,NBB FL D.31 green certificates 956m 2023 (broader than CoA GSC 822m)",
    "bud_fl_green_cert_nbb_2024,vlaanderen_gov,2024,858000000,,,outturn,src_nbb_subsidies_ent_2025_vipa,strong,NBB FL D.31 green certificates 858m 2024",
])

append_lines(DATA / "commitments.csv", [
    'cmt_vl_res_support_2014_23,Flanders renewable energy support multi-instrument 2014-2023,vlaanderen_gov,RES producers households DSOs,GSC WKC premiums calls VEKA Energiebesluit,2014-01-01,2014,2023,12970000000,"{""total_2014_23"":12970000000,""gsc_cum"":10508000000,""wkc_cum"":1785000000,""heat_premiums_cum"":112000000,""call_warmte_cum"":109000000,""pv_premie_cum"":158000000,""retro_cum"":159000000,""call_stroom_cum"":37000000,""warmtenet_adhoc"":53500000,""2023_total"":1174000000,""2023_gsc"":822000000,""2023_wkc"":174000000,""2023_heat_prem"":22000000,""budget_share_class"":1800000000,""bill_share_note"":""~95pct via electricity bill ODV not VL budget""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2025_34_HernieuwbareEnergieVL.pdf,Renewable electricity and heat deployment Flanders,Phase GSC/WKC; target heat pumps low-income; open annual cash table,src_ccrek_hernieuwbare_vl_2025,strong,Vlaanderen>Energie>hernieuwbaar,tick151 beyond offshore; dual WAL green cert 288-323m',
    'cmt_vl_gsc_wkc_dso_vergoeding,VL government certificate compensation to Fluvius DSOs,vlaanderen_gov,Fluvius electricity DSOs,Energiebesluit art 6.4.14/2 and /3,2021-01-01,2021,2025,479512050,"{""gsc_2021"":91512000,""gsc_2022"":148000050,""gsc_2023"":148000000,""gsc_2024"":67000000,""gsc_2025"":0,""wkc_2024"":25000000,""wkc_2025"":60000000,""sum_gsc_2021_24"":454512050}",0,active,https://docs.vlaamsparlement.be/pfile?id=2250200,Compensate DSO certificate purchase ODV,Publish multi-year net ODV GSC/WKC in tariffs open data,src_vnr_odv_horch_2025,strong,Vlaanderen>Energie>ODV_certificaten,tick151',
])

append_lines(DATA / "leaderboard.csv", [
    "lb_vl_gsc_support,Flanders green electricity certificates GSC ~0.8-1.1bn/yr,Flanders,subsidy,Vlaanderen>Energie>GSC,822000000,10508000000,CoA strong: 822m 2023 / 10.5bn cum 2014-23; mostly on electricity bill not budget; oversubsidy PV legacy,strong,src_ccrek_hernieuwbare_vl_2025,Electricity consumers RES producers,Renewable electricity support,Legacy oversubsidy; phase-out except wind; dual NBB 858-956m,8,9.0,6,8.0,Continue phase-out; open annual VEKA cash table; no new PV GSC,seed,,tick151",
    "lb_vl_wkc_chp,Flanders CHP certificates WKC ~174-236m/yr,Flanders,subsidy,Vlaanderen>Energie>WKC,174000000,1785000000,CoA strong: 174m 2023 / 1.785bn cum; sunset path to 2032; Fluvius CHP inventory 521m stock risk,strong,src_ccrek_hernieuwbare_vl_2025,CHP producers electricity consumers,CHP support,Certificate oversupply inventory risk,7,7.5,5,7.0,Accelerate sunset; clear inventory policy,seed,,tick151",
    "lb_vl_heat_pump_premiums,Flanders netbeheerder heat pump/boiler premiums ~22m 2023,Flanders,subsidy,Vlaanderen>Energie>warmtepomp_premies,22000000,112000000,CoA strong: 22m 2023 / 112m cum 2014-23; part of MVP reform; income-targeted from 2026,strong,src_ccrek_hernieuwbare_vl_2025,Household renovators,Electrify heating,Core climate; deadweight for high income; MVP reform ongoing,5,5.5,4,5.2,Keep income-targeted only; publish MVP heat-pump cash L5,seed,,tick151",
])

rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_148,Climate/energy named subsidies beyond offshore,continuous,6,open,L5,sec_federal,'
    '"Heat pumps premiums green cert residual named.",'
    ",2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,"
)
new = (
    'rq_148,Climate/energy named subsidies beyond offshore,continuous,6,done,L5,sec_federal,'
    '"Heat pumps premiums green cert residual named.",'
    "gap_vl_odv_mvp_cash,2026-07-27T14:00:00Z,2026-07-27T23:55:00Z,"
    '"tick151: CoA GSC 10.5bn/WKC 1.8bn cum; heat prem 112m; FOI REG digit + MVP total"'
)
if old not in rtext:
    raise SystemExit("rq_148 OLD NOT FOUND:\n" + "\n".join(l for l in rtext.splitlines() if "rq_148" in l))
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_vl_odv_mvp_cash.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_vl_odv_mvp_cash`  
**Status:** ready (human send only)  
**Linked:** rq_148 · cmt_vl_res_support_2014_23 · lb_vl_gsc_support

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: VEKA / Vlaamse Nutsregulator / Fluvius
     Team Openbaarheid Vlaanderen
     openbaarheid@vlaanderen.be
     Havenlaan 88 bus 20 1000 Brussel

Betreft: Verzoek om openbaarmaking — ODV REG/GSC/WKC en Mijn VerbouwPremie cash 2021-2026

Geachte,

Op grond van het Bestuursdecreet dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Digitale tijdreeks (niet alleen grafiek) van Fluvius REG-premiekosten en recuperaties
   uit algemene middelen/Energiefonds 2021-2026 (VNR-antwoord Horch VI6 figuur 2).
2. Digitale tijdreeks nettokosten ODV GSC en ODV WKC in nettarieven 2021-2026
   (VNR-figuren 5 en 7).
3. Mijn VerbouwPremie: totale uitbetaalde premies 2023-2026, met split warmtepomp /
   isolatie / overige, en aandeel begroting vs Energiefonds vs nettarief.
4. VEKA jaarlijkse steuntabel 2024-2025 in dezelfde structuur als Rekenhof T10 (2014-2023).

Periode: 2021-01-01 tot meest recente stand.

### 2. Context

Rekenhof 2025 en VNR 2025 geven sterke totalen/cumuls; grafieken zonder exacte
cijfers en MVP-totaalbudget blijven deels ondoorzichtig (CoA: ~95% steun via factuur).

Hierarchie: Vlaanderen > Energie > ODV / MVP.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: gap_vl_odv_mvp_cash

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
    "gap_vl_odv_mvp_cash,Vlaanderen>Energie>ODV_MVP_cash_series,vlaanderen_gov,Digit REG GSC WKC net cost series 2021-2026 and Mijn VerbouwPremie total paid by measure; VEKA support table 2024-25 parallel CoA T10,CoA 2014-23 + VNR partial strong; chart digits and MVP total FOI,7,VEKA / VNR / Fluvius / Team Openbaarheid,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vl_odv_mvp_cash.md,ready,2026-07-27,,,,,cmt_vl_res_support_2014_23,lb_vl_gsc_support,2026-07-27T23:55:00Z,2026-07-27T23:55:00Z,tick151 partial; human send",
])

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 Charleroi Myria housing; FOI ready human send. rq_148 climate energy done."\n',
    "utf-8",
)

log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Climate/energy named subsidies beyond offshore)
- Found (strong Rekenhof 2025 + VNR + Fluvius + NBB):
  - **Flanders RES support 2014-23: EUR 12.97bn** (~1.8bn on budget; rest on electricity bill).
  - **GSC:** 2023 **EUR 822m** · cum **10.51bn**; NBB broader green cert **956/858m 2023-24**.
  - **WKC CHP:** 2023 **EUR 174m** · cum **1.79bn**; Fluvius cert inventory **EUR 602m** EOY2025 (CHP 521m).
  - **Heat premiums (warmtepomp etc):** 2023 **EUR 22m** · cum **112m** 2014-23 (netbeheerder).
  - **Calls/ad hoc:** groene warmte **109m** · PV premie **158m** · retro **159m** · warmtenet **53.5m** · call stroom **37m**.
  - **VL DSO vergoedingen:** GSC 91.5→148→148→**67m** 2021-24; WKC **25m 2024 / 60m 2025**.
  - WAL green cert already mapped **323/288m**; offshore already mapped separately.
- Wrote: sources 3; budgets 26; cmt 2; lb 3; rq_148=done; FOI residual ready.
- FOI: gap_vl_odv_mvp_cash (REG digit series + MVP total) human send.
- Next: prio6 **rq_144 Charleroi** / **rq_120 Myria** / **rq_149 housing**.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick151 write OK")

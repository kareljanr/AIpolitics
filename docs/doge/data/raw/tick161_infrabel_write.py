# -*- coding: utf-8 -*-
"""Tick 161 — continuous hole-fill: Infrabel geconsolideerd jaarverslag 2024 primary (rail dual NMBS)."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 161
UNIT = "rq_156"
UTC = "2026-07-28T03:45:00Z"


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
        key = row.split(",", 1)[0]
        if key not in text:
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


# --- sources ---
srcs = [
    'src_infrabel_jv2024,Infrabel geconsolideerd jaarverslag 2024 NL PDF,https://infrabel.be/sites/default/files/generated/files/report/INFRABEL_Geconsolideerd%20jaarverslag%202024_NL.pdf,Infrabel,2026-07-28,official_annual_report,"Omzet 843.2m; exploitatiesubsidies 560.9m; kapitaalsubsidies P&L 794.9m; resultaat 33.6m; balanstotaal 25.231bn; kapitaalsubsidies stock 18.589bn; Liefkenshoek PPS 50.61m/y 2008; tick161"',
    'src_infrabel_facts_page,Infrabel facts figures jaarverslagen hub,https://infrabel.be/nl/facts-figures,Infrabel,2026-07-28,agency,"Hub for consolidated annual reports; tick161"',
]
append_if_missing(DATA / "sources.csv", srcs)

# --- budgets ---
bud = [
    "bud_infrabel_omzet_2024,infrabel,2024,843157343,,,outturn,src_infrabel_jv2024,strong,Consolidated omzet 843.157m 2024 (875.187m 2023)",
    "bud_infrabel_omzet_2023,infrabel,2023,875187323,,,outturn,src_infrabel_jv2024,strong,Consolidated omzet 875.187m 2023 restated base",
    "bud_infrabel_exploitatiesubsidies_2024,infrabel,2024,560883870,,,outturn,src_infrabel_jv2024,strong,Exploitatiesubsidies 560.884m 2024 (-23.0m y/y)",
    "bud_infrabel_exploitatiesubsidies_2023,infrabel,2023,583890503,,,outturn,src_infrabel_jv2024,strong,Exploitatiesubsidies 583.891m 2023",
    "bud_infrabel_kapitaalsubsidies_pl_2024,infrabel,2024,794869024,,,outturn,src_infrabel_jv2024,strong,Kapitaalsubsidies taken to P&L 794.869m 2024 (amortisation matching)",
    "bud_infrabel_kapitaalsubsidies_pl_2023,infrabel,2023,774723608,,,outturn,src_infrabel_jv2024,strong,Kapitaalsubsidies P&L 774.724m 2023",
    "bud_infrabel_bedrijfsopbr_pre_kap_2024,infrabel,2024,1966752090,,,outturn,src_infrabel_jv2024,strong,Bedrijfsopbrengsten voor kapitaalsubsidies 1.966752bn 2024",
    "bud_infrabel_ebitda_like_2024,infrabel,2024,114402842,,,outturn,src_infrabel_jv2024,strong,Bedrijfsresultaat voor kapitaalsubsidies afschrijvingen en impairments 114.403m 2024 (132.0m 2023)",
    "bud_infrabel_bedrijfsresultaat_2024,infrabel,2024,82037562,,,outturn,src_infrabel_jv2024,strong,Bedrijfsresultaat 82.038m 2024 (99.964m 2023)",
    "bud_infrabel_resultaat_2024,infrabel,2024,33562813,,,outturn,src_infrabel_jv2024,strong,Resultaat van het boekjaar 33.563m 2024 (44.260m 2023)",
    "bud_infrabel_afschrijvingen_2024,infrabel,2024,827234304,,,outturn,src_infrabel_jv2024,strong,Afschrijvingen en impairments 827.234m 2024",
    "bud_infrabel_diensten_2024,infrabel,2024,1507648300,,,outturn,src_infrabel_jv2024,strong,Diensten en diverse goederen 1.507648bn 2024 (includes HR Rail staff charge)",
    "bud_infrabel_personeelskosten_pl_2024,infrabel,2024,75746666,,,outturn,src_infrabel_jv2024,strong,Personeelskosten on Infrabel P&L only 75.747m (most staff via HR Rail in services)",
    "bud_infrabel_balans_totaal_2024,infrabel,2024,25230729323,,,outturn,src_infrabel_jv2024,strong,Balanstotaal 25.230729bn eoy2024",
    "bud_infrabel_materiele_va_2024,infrabel,2024,20322718064,,,outturn,src_infrabel_jv2024,strong,Materiele vaste activa 20.322718bn eoy2024 (+452.7m invest effect)",
    "bud_infrabel_kapitaalsubsidies_stock_2024,infrabel,2024,18589038347,,,outturn,src_infrabel_jv2024,strong,Kapitaalsubsidies LT 17.829bn + ST 0.760bn = 18.589bn stock eoy2024",
    "bud_infrabel_fin_schulden_2024,infrabel,2024,3241530827,,,outturn,src_infrabel_jv2024,strong,Financiele schulden incl derivatives ~3.2415bn eoy2024 (LT 3.166 + ST 0.049 + derivatives 0.027)",
    "bud_infrabel_cash_2024,infrabel,2024,625160520,,,outturn,src_infrabel_jv2024,strong,Geldmiddelen en kasequivalenten 625.161m eoy2024",
    "bud_infrabel_liefkenshoek_pps_annual,infrabel,2024,50610000,,,budgeted,src_infrabel_jv2024,strong,PPS Liefkenshoek Rail Link specific annual State subsidy 50.61m in 2008 euros through 2032 performance contract",
    "bud_infrabel_creditline_invest_2025_29,infrabel,2025,1000000000,,,commitment,src_infrabel_jv2024,strong,Government credit line up to 1bn current for investments 2025-2029 (performantiecontract note)",
    "bud_infrabel_alstom_switches_80m,infrabel,2024,80000000,,,commitment,src_infrabel_jv2024,medium,Alstom contract ~80m for ~10000 ultralight switches (editorial markante gebeurtenissen)",
    "bud_infrabel_thales_cyber_20m,infrabel,2024,20000000,,,commitment,src_infrabel_jv2024,medium,Thales cybersecurity 5y contract 20m (editorial)",
]
append_if_missing(DATA / "budgets.csv", bud)

# --- commitments ---
cmts = [
    (
        'cmt_infrabel_results_2024,Infrabel consolidated financial outturn 2024,infrabel,Rail infrastructure users State PSO,'
        'Infrabel geconsolideerd jaarverslag 2024,2025-04-22,2023,2024,560883870,'
        '"{""omzet_2024"":843157343,""omzet_2023"":875187323,""exploitatiesubsidies_2024"":560883870,'
        '""exploitatiesubsidies_2023"":583890503,""kapitaalsubsidies_pl_2024"":794869024,'
        '""kapitaalsubsidies_pl_2023"":774723608,""bedrijfsopbr_pre_kap_2024"":1966752090,'
        '""ebitda_like_2024"":114402842,""bedrijfsresultaat_2024"":82037562,""resultaat_2024"":33562813,'
        '""afschrijvingen_2024"":827234304,""diensten_2024"":1507648300,""personeel_pl_2024"":75746666,'
        '""balans_totaal"":25230729323,""materiele_va"":20322718064,""kapitaalsubsidies_stock"":18589038347,'
        '""fin_schulden"":3241530827,""cash"":625160520,""liefkenshoek_pps_m2008"":50610000,'
        '""creditline_2025_29"":1000000000,""note"":""In GG ESA unlike NMBS; staff mainly via HR Rail in services line; FPS cash codes residual FOI""}",0,active,'
        'https://infrabel.be/sites/default/files/generated/files/report/INFRABEL_Geconsolideerd%20jaarverslag%202024_NL.pdf,'
        'Public service rail infrastructure,Publish FPS cash codes vs JV; multi-year invest L5; HR Rail passthrough,'
        'src_infrabel_jv2024,strong,Federal>Mobiliteit>Infrabel>jv2024,'
        'tick161 hole-fill rail dual NMBS'
    ),
    (
        'cmt_infrabel_liefkenshoek_pps,Infrabel PPS Liefkenshoek availability fee State subsidy path,infrabel,Private partner Liefkenshoek Rail Link,'
        'Performance contract State-Infrabel + KB 26 Dec 2022,2022-12-26,2024,2032,50610000,'
        '"{""annual_m2008"":50610000,""lt_receivable_restated"":416624084,""kapitaalsubsidies_component"":95638980,'
        '""over_te_dragen_opbrengsten"":320985104,""note"":""Restatement 2023 balance; no P&L impact stated""}",0,active,'
        'https://infrabel.be/sites/default/files/generated/files/report/INFRABEL_Geconsolideerd%20jaarverslag%202024_NL.pdf,'
        'PPP rail link financing,Publish indexed cash-by-year paid vs booked,'
        'src_infrabel_jv2024,strong,Federal>Mobiliteit>Infrabel>Liefkenshoek,'
        'tick161'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

# --- leaderboard ---
lbs = [
    (
        'lb_infrabel_exploitatiesubsidies,Infrabel exploitatiesubsidies 561m 2024,federal,ops,'
        'Federal>Mobiliteit>Infrabel>exploitatiesubsidies,560883870,560883870,'
        'JV strong: 560.9m 2024 / 583.9m 2023; plus kapitaalsubsidies P&L 794.9m; dual with NMBS invest>820m 2025,'
        'strong,src_infrabel_jv2024,Rail users taxpayers,Rail infrastructure PSO,'
        'Core infra not pure waste; GG ESA entity; dual NMBS+HR Rail opacity,4,9.5,7,7.0,'
        'Open FPS cash codes; invest L5 multi-year; HR Rail staff cost matrix,seed,,tick161'
    ),
    (
        'lb_infrabel_kapitaalsubsidies_stock,Infrabel kapitaalsubsidies stock 18.6bn,federal,ops,'
        'Federal>Mobiliteit>Infrabel>kapitaalsubsidies_stock,18589038347,18589038347,'
        'JV eoy2024 kapitaalsubsidies LT+ST 18.589bn; annual P&L recognition 794.9m; assets 25.2bn,'
        'strong,src_infrabel_jv2024,Taxpayers,Capital grants rail network,'
        'Stock of historical State capital support amortised; not annual cash,3,9.5,5,5.8,'
        'Reconcile annual cash capital grants FPS vs stock movement,seed,,tick161'
    ),
    (
        'lb_infrabel_liefkenshoek_pps,Infrabel Liefkenshoek PPS State subsidy ~50.6m/y,federal,ops,'
        'Federal>Mobiliteit>Infrabel>Liefkenshoek_PPS,50610000,50610000,'
        'Annual specific subsidy 50.61m (2008 euros) for availability fee to private partner through 2032,'
        'strong,src_infrabel_jv2024,Taxpayers rail freight Antwerp,PPP availability payment,'
        'Long PPP tail; indexed; restatement 416.6m LT receivable,4,7.0,6,5.6,'
        'Publish indexed cash series and private-partner margin if public,seed,,tick161'
    ),
]
append_if_missing(DATA / "leaderboard.csv", lbs)

# --- FOI queue + draft ---
foi_row = (
    "gap_infrabel_dotatie_cash,Federal>Mobiliteit>Infrabel>subsidies_cash,infrabel,"
    "FPS/BOSA cash-by-year article codes for exploitatiesubsidies and kapitaalsubsidies 2022-2026 reconcile to JV 560.9m/794.9m; "
    "HR Rail personnel charge matrix; multi-year investment project L5 top20; Liefkenshoek indexed cash series,"
    "JV 2024 fills strong accounting outturn; absolute federal cash codes and project L5 still opaque like NMBS gap,"
    "6,FOD Mobiliteit / BOSA / Infrabel / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_infrabel_dotatie_cash.md,ready,2026-07-28,,,,,cmt_infrabel_results_2024,lb_infrabel_exploitatiesubsidies,"
    f"{UTC},{UTC},tick161 JV2024 partial fill; residual FPS cash+L5 human send"
)
append_if_missing(DATA / "foi_queue.csv", [foi_row])

draft = """# FOI draft — gap_infrabel_dotatie_cash

**Status:** ready (human send only — do not mark sent without confirmation)  
**Gap id:** gap_infrabel_dotatie_cash  
**Linked:** cmt_infrabel_results_2024 · lb_infrabel_exploitatiesubsidies · dual gap_nmbs_annual_toelage  
**Tick:** 161 (2026-07-28)

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Mobiliteit en Vervoer / FOD BOSA
t.a.v. de dienst openbaarheid van bestuur
en: Infrabel NV van publiek recht — openbaarheid / communicatie
via: https://www.ibz.be/nl/openbaarheid-van-bestuur (federaal loket indien van toepassing)

Betreft: Verzoek om openbaarmaking — Infrabel exploitatie- en kapitaalsubsidies cash-by-year en investerings-L5

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
(en aanvullende federale bepalingen waar van toepassing) dien ik hierbij een
verzoek in tot openbaarmaking / afschrift van de hieronder omschreven
bestuursdocumenten.

### 1. Voorwerp van het verzoek

1. Kasuitgaven van de Federale Staat aan Infrabel (of via HR Rail waar relevant)
   per begrotingsjaar 2022 t.e.m. 2026, met basisallocatie-/artikelcodes:
   a) exploitatiesubsidies / werkingsdotatie;
   b) kapitaalsubsidies / investeringsdotaties;
   c) specifieke subsidies (waaronder PPS Liefkenshoek Rail Link
      beschikbaarheidsvergoeding / jaarlijkse specifieke subsidie).

2. Aansluitingstabel die de kasuitgaven onder (1) afstemt op de bedragen in het
   geconsolideerd jaarverslag Infrabel 2024:
   - exploitatiesubsidies 560.883.869,57 EUR (2024) en 583.890.502,76 EUR (2023);
   - kapitaalsubsidies in resultaat 794.869.024,09 EUR (2024);
   - en de mutatie van de voorraad kapitaalsubsidies op de balans
     (circa 18,589 miljard EUR eoy 2024).

3. Overzicht van de doorberekening personeelskosten via HR Rail NV naar Infrabel
   (totaal en indien beschikbaar FTE) 2023-2025, ter duiding van de post
   "Diensten en diverse goederen" (1.507.648.300,39 EUR in 2024).

4. Top 20 investeringsprojecten 2024-2026 met gecommitteerd en kasbedrag
   (naam, bedrag, status), inclusief de kredietlijn tot 1 miljard EUR voor
   investeringen 2025-2029 zoals vermeld in het performantiecontract-kader.

5. Geïndexeerde kasreeks van de jaarlijkse specifieke Staatssubsidie voor
   Liefkenshoek Rail Link (basis 50,61 miljoen EUR 2008) voor 2022-2032.

### 2. Motivering

Publieke controle op de spoorinfrastructuurfinanciering (Infrabel zit in de
overheidsconsolidatie ESA, in tegenstelling tot NMBS) vereist aansluiting tussen
begrotingskas en jaarrekening. Aggregaten uit het jaarverslag 2024 zijn publiek;
kas-codes en project-L5 ontbreken parallel aan de NMBS-gap.

### 3. Vorm

Bij voorkeur machineleesbaar (CSV/XLSX) of doorzoekbare PDF.
Elektronische toezending volstaat.

### 4. Termijn en kosten

Gelieve te antwoorden binnen de wettelijke termijn. Ik vraag vrijstelling of
beperking van retributies als burger / journalistiek-onderzoeksverzoek.

Met vriendelijke groeten,

[Naam]
```

## Agent notes

- Primary fill tick161: official consolidated JV 2024 PDF downloaded to
  `docs/doge/data/raw/infrabel_jv2024.pdf`.
- Do **not** invent FPS cash totals; only JV accounting figures are strong.
- Human must send; agent never marks `sent` without confirmation.
"""
write_text(FOI / "gap_infrabel_dotatie_cash.md", draft)

# --- research queue: seed rq_156 done this tick; seed rq_157 next hole-fill ---
rq_156 = (
    f"rq_156,Infrabel 2024 JV public hole-fill rail dual NMBS,continuous,5,done,L2,infrabel,"
    f"\"Source Infrabel consolidated annual report 2024: exploitatie+kapitaal subsidies result balance; dual NMBS.\","
    f"gap_infrabel_dotatie_cash,{UTC},{UTC},"
    f"\"tick161: omzet 843m exp-sub 561m kap-sub P&L 795m result 33.6m balance 25.2bn stock kap 18.6bn; FOI residual FPS cash\""
)
rq_157 = (
    f"rq_157,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    f"\"Prefer public primary fills for ready FOI topics (FOREM 2024-26 RA De Lijn full 2025-26 perimeter Antwerp register "
    f"univ per-institution VIPA named Mons BI2026) if new PDFs appear; else next highest open rq; do not idle while public work remains.\","
    f",{UTC},,"
    f"\"Spawned tick161 after Infrabel fill; rq_116 SWA deferred Oct-Dec 2026\""
)
# fix seed of wrong rq_152 note from tick160 if present - ensure rq_156/157
append_if_missing(DATA / "research_queue.csv", [rq_156, rq_157])

# Update gap_de_lijn note: JV PDF still 403 this tick
gap_dl_new = (
    "gap_de_lijn_dotatie,Vlaanderen>MOW>De_Lijn>dotatie,de_lijn,"
    "Full 2025-2026 exploitatie+investering toelage comparable to 2019-2024 Vervoersautoriteit table "
    "(PQ955 filled 2019-24 and 2025 KN/AN/VoM+GIP slices; press surplus 20k passengers 372.9m; JV PDF still 403),"
    "2019-24 series strong; 2025-26 full total exp+inv still partial (minister pointed to BBT; ctfassets PDF blocked),"
    "6,Vlaamse overheid Team Openbaarheid / De Lijn,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
    "docs/doge/foi/drafts/gap_de_lijn_dotatie.md,ready,2026-07-20,,,,,2026-07-20T01:00:00Z,2026-07-28T03:45:00Z,"
    "tick126: 2019-24 filled; residual 2025-26 full perimeter |tick161: press metrics reconfirmed; JV PDF 403"
)
replace_line_startswith(DATA / "foi_queue.csv", "gap_de_lijn_dotatie,", gap_dl_new)

# --- loop_state ---
write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{UNIT},161,no,"
    "\"Scheduler 60s. Next prio5 rq_157 hole-fill FOREM/De Lijn/Antwerp/univ; rq_116 SWA deferred. "
    "FOI ready human send. tick161 Infrabel JV2024 fill.\"\n",
)

# --- loop_log append ---
log_path = ROOT / "docs" / "doge" / "loop_log.md"
log = read_text(log_path)
entry = f"""
### {UTC} — tick 161
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **Infrabel geconsolideerd JV 2024** rail dual NMBS)
- Found (strong primary PDF 4.4 MB, 53 pp):
  - **Omzet** EUR **843.2m** 2024 (875.2m 2023).
  - **Exploitatiesubsidies** **560.9m** (583.9m) — −23.0m y/y.
  - **Kapitaalsubsidies** P&L recognition **794.9m** (774.7m); **stock** LT+ST **18.589bn**.
  - Bedrijfsopbrengsten vóór kap. **1.967bn**; EBITDA-like **114.4m**; bedrijfsresultaat **82.0m**; **resultaat 33.6m**.
  - Balanstotaal **25.231bn**; materiële VA **20.323bn** (+452.7m invest effect); fin. debt **~3.24bn**; cash **625m**.
  - **Liefkenshoek PPS:** annual specific State subsidy **50.61m (2008 €)** through 2032; LT receivable restatement **416.6m**.
  - Credit line up to **1bn** invest 2025-29; Alstom switches **~80m**; Thales cyber **20m/5y** (editorial medium).
  - Note: P&L personnel only **75.7m** — bulk staff via **HR Rail** inside **diensten 1.508bn**.
- De Lijn 2025 JV PDF still **403** on ctfassets; press metrics already in DB (surplus 20k; pax 372.9m; −27.5m dotatie).
- Wrote: sources 2; budgets ~22; cmt 2; lb 3; FOI **gap_infrabel_dotatie_cash** ready; rq_156=done; seeded **rq_157**.
- FOI: gap_infrabel (FPS cash codes + invest L5 + Liefkenshoek series) human send only; gap_de_lijn residual note.
- Next: prio5 **rq_157** FOREM/De Lijn perimeter/Antwerp/univ; deferred **rq_116** SWA.
"""
if "tick 161" not in log[-2000:]:
    write_text(log_path, log.rstrip() + "\n" + entry)

print("tick161 write OK")

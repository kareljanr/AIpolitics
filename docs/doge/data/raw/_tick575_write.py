# -*- coding: utf-8 -*-
"""Tick 575 / rq_566: POAB factsheet 2025 L5 cargo dual + Pidpa JV2025 ops dual DWG."""
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]  # docs/doge/data/raw -> repo? 
# Path: docs/doge/data/raw/_tick575_write.py -> parents[0]=raw, [1]=data, [2]=doge, [3]=docs, [4]=repo
ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
NOW = "2026-07-31T11:00:00Z"
TICK = 575
UNIT = "rq_566"


def detect_enc(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            raw.decode(enc)
            return enc
        except UnicodeDecodeError:
            continue
    return "latin-1"


def append_rows(path: Path, rows: list[str]) -> None:
    enc = detect_enc(path)
    text = path.read_text(encoding=enc)
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        row = row.rstrip("\n")
        text += row + "\n"
    path.write_text(text, encoding=enc, newline="\n")


def replace_line_prefix(path: Path, prefix: str, new_line: str) -> bool:
    enc = detect_enc(path)
    lines = path.read_text(encoding=enc).splitlines()
    found = False
    out = []
    for l in lines:
        if l.startswith(prefix):
            out.append(new_line.rstrip("\n"))
            found = True
        else:
            out.append(l)
    path.write_text("\n".join(out) + "\n", encoding=enc, newline="\n")
    return found


def main() -> None:
    # --- sources ---
    sources = [
        "src_poab_factsheet_2025,Port of Antwerp-Bruges Factsheet Throughput Figures 2025,https://newsroom.portofantwerpbruges.com/en/press-releases/port-of-antwerp-bruges-ends-2025-with-resilience-in-a-turbulent-trading-climate,Port of Antwerp-Bruges,2026-07-31,primary_agency,Strong tick575: containers 149.4 Mt / 13.6m TEU; dry bulk 13.1 Mt -12.1pct; RoRo cars 3.186m; LNG US 3.7 Mt; Russia LNG 4.3 Mt; cruise 466k pax; vessels 20236 GT 642m; market share HLH 29.3pct; raw poab_factsheet_2025.pdf",
        "src_pidpa_jv_2025,Pidpa geintegreerd jaarverslag 2025 ops KPIs,https://www.pidpa.be/sites/default/files/2026-06/Pidpa_Jaarverslag_2025.pdf,Pidpa,2026-07-31,primary_agency,Strong tick575: production 62.4 Mm3 pure / 64.1 Mm3; users 1.5m; connections 603k; pipes 13k+ km; digital meters 200k 34.1pct; sewer 5768 km 48 munis; NRW 8.6pct ILI 0.45; replace 158 km 1.18pct; dual DWG; raw pidpa_jv_2025.pdf",
        "src_dual_ports_poab_nsp_tick575,Dual Belgian ports POAB throughput 2025 vs North Sea Port class,docs/doge/data/raw/poab_factsheet_2025.pdf,DOGE synthesis POAB factsheet + prior NSP 67 Mt class,2026-07-31,synthesis,Strong dual: POAB 266.5 Mt vs NSP ~67 Mt seaborne class; POAB omzet ~507m vs NSP 115m 2023; different scale; tick575",
        "src_dual_water_dwg_pidpa_tick575,Dual VL drinking De Watergroep + Pidpa 2025 ops,docs/doge/data/raw/pidpa_jv_2025.pdf,DOGE synthesis Pidpa JV2025 + DWG 2025,2026-07-31,synthesis,Strong dual: DWG omzet 974m prod 125.4 Mm3 cust 3.4m vs Pidpa omzet 403m prod 62.4 Mm3 users 1.5m; digital meters joint Farys; tick575",
    ]
    append_rows(DATA / "sources.csv", sources)

    # --- budgets (COUNT volumes: amount_eur stores count in native unit; notes clarify) ---
    budgets = [
        # POAB L5 cargo (tonnes where applicable; TEU/cars/pax as counts)
        "bud_poab_containers_mt_2025,port_antwerp_bruges,2025,149400000,,,outturn,src_poab_factsheet_2025,strong,COUNT container tonnage 149.4 Mt (+0.4pct); tick575",
        "bud_poab_containers_teu_2025,port_antwerp_bruges,2025,13600000,,,outturn,src_poab_factsheet_2025,strong,COUNT containers 13.6m TEU (+0.7pct); tick575",
        "bud_poab_dry_bulk_mt_2025,port_antwerp_bruges,2025,13100000,,,outturn,src_poab_factsheet_2025,strong,COUNT dry bulk 13.1 Mt (-12.1pct); fertilizers main; coal -61.6pct; tick575",
        "bud_poab_roro_cars_new_2025,port_antwerp_bruges,2025,3186000,,,outturn,src_poab_factsheet_2025,strong,COUNT new cars RoRo handled 3.186m (-1.2pct); China origin +11pct; tick575",
        "bud_poab_lng_us_mt_2025,port_antwerp_bruges,2025,3700000,,,outturn,src_poab_factsheet_2025,strong,COUNT US LNG throughput 3.7 Mt (>4x YoY); tick575",
        "bud_poab_lng_russia_mt_2025,port_antwerp_bruges,2025,4300000,,,outturn,src_poab_factsheet_2025,strong,COUNT Russia LNG origin 4.3 Mt (-16.6pct); EU ban path 2027; tick575",
        "bud_poab_lng_qatar_mt_2025,port_antwerp_bruges,2025,1500000,,,outturn,src_poab_factsheet_2025,strong,COUNT Qatar LNG 1.5 Mt (-21.7pct); tick575",
        "bud_poab_us_inbound_mt_2025,port_antwerp_bruges,2025,19700000,,,outturn,src_poab_factsheet_2025,strong,COUNT US inbound 19.7 Mt of 31.3 Mt total partner; tick575",
        "bud_poab_us_outbound_mt_2025,port_antwerp_bruges,2025,11700000,,,outturn,src_poab_factsheet_2025,strong,COUNT US outbound 11.7 Mt; tick575",
        "bud_poab_hlh_share_pct_2025,port_antwerp_bruges,2025,29.3,,,outturn,src_poab_factsheet_2025,strong,PCT Hamburg-Le Havre range container market share 29.3 first 9m (-1.2pp); tick575",
        "bud_poab_cruise_pax_2025,port_antwerp_bruges,2025,466089,,,outturn,src_poab_factsheet_2025,strong,COUNT Zeebrugge cruise passengers 466089 (-16.4pct); 166 ships; tick575",
        "bud_poab_vessels_2025,port_antwerp_bruges,2025,20236,,,outturn,src_poab_factsheet_2025,strong,COUNT seagoing vessel calls 20236 (+0.2pct); tick575",
        "bud_poab_gt_m_2025,port_antwerp_bruges,2025,642000000,,,outturn,src_poab_factsheet_2025,strong,COUNT combined gross tonnage 642m GT (+1.5pct); tick575",
        "bud_poab_conv_gc_yoy_pct_2025,port_antwerp_bruges,2025,1.6,,,outturn,src_poab_factsheet_2025,strong,PCT conventional general cargo +1.6 yoy 2025; steel import +6.7 export -13.9; tick575",
        "bud_poab_roro_yoy_pct_2025,port_antwerp_bruges,2025,3.0,,,outturn,src_poab_factsheet_2025,strong,PCT RoRo throughput +3 yoy 2025; used cars +37pct; tick575",
        "bud_poab_petrol_prod_yoy_pct_2025,port_antwerp_bruges,2025,-19.0,,,outturn,src_poab_factsheet_2025,strong,PCT liquid bulk petroleum products -19 yoy (about 60pct of liquid bulk); gasoline -40.8; tick575",
        # Pidpa ops dual DWG
        "bud_pidpa_prod_pure_mm3_2025,pidpa,2025,62400000,,,outturn,src_pidpa_jv_2025,strong,COUNT pure water produced 62.4 Mm3 2025; tick575",
        "bud_pidpa_prod_total_mm3_2025,pidpa,2025,64100000,,,outturn,src_pidpa_jv_2025,strong,COUNT total production volume class 64.1 Mm3 (incl rest flows); tick575",
        "bud_pidpa_users_2025,pidpa,2025,1500000,,,outturn,src_pidpa_jv_2025,strong,COUNT users ~1.5m 2025; tick575",
        "bud_pidpa_connections_2025,pidpa,2025,603000,,,outturn,src_pidpa_jv_2025,strong,COUNT water connections 603000; tick575",
        "bud_pidpa_daily_ml_2025,pidpa,2025,178,,,outturn,src_pidpa_jv_2025,strong,COUNT drinkwater per day million liters 178; tick575",
        "bud_pidpa_digital_meters_cum_2025,pidpa,2025,200000,,,outturn,src_pidpa_jv_2025,strong,COUNT digital meters cum >200000 = 34.1pct of meters eoy2025 joint Farys/DWG/Fluvius; tick575",
        "bud_pidpa_sewer_km_2025,pidpa,2025,5768,,,outturn,src_pidpa_jv_2025,strong,COUNT sewer network 5768 km; 48 munis after Kapellen Kalmthout Kasterlee join Dec2025; tick575",
        "bud_pidpa_drink_pipes_km_2025,pidpa,2025,13000,,,outturn,src_pidpa_jv_2025,strong,COUNT drinkwater pipes +13000 km class; tick575",
        "bud_pidpa_nrw_pct_2025,pidpa,2025,8.6,,,outturn,src_pidpa_jv_2025,strong,PCT NRW estimated 8.60 2025 (ILI 0.45); 2024 final NRW 8.46 ILI 0.42; Blue Deal leader; tick575",
        "bud_pidpa_pipe_replace_km_2025,pidpa,2025,158,,,outturn,src_pidpa_jv_2025,strong,COUNT replaced 158 km drink pipes 2025 rate 1.18pct; tick575",
        "bud_pidpa_alt_water_mm3_2025,pidpa,2025,2000000,,,outturn,src_pidpa_jv_2025,strong,COUNT alternative water supply circular/rain/reuse 2.0 Mm3 2025; tick575",
        "bud_pidpa_energy_primary_kwh_2025,pidpa,2025,81294556,,,outturn,src_pidpa_jv_2025,strong,COUNT primary energy use est 81.294m kWh 2025; on-site renewable ~7.99pct; tick575",
        "bud_pidpa_co2_total_t_2025,pidpa,2025,14149,,,outturn,src_pidpa_jv_2025,strong,COUNT total fossil GHG 14149 tCO2e 2025 (+1.02pct YoY; -20.75 vs 2016); tick575",
        "bud_pidpa_wpc_count_2025,pidpa,2025,11,,,outturn,src_pidpa_jv_2025,strong,COUNT water production centres 11 (new Oud-Turnhout 2025); tick575",
        "bud_pidpa_sewer_munis_2025,pidpa,2025,48,,,outturn,src_pidpa_jv_2025,strong,COUNT sewer municipalities 48 eoy2025; tick575",
    ]
    append_rows(DATA / "budgets.csv", budgets)

    # --- commitments ---
    commitments = [
        'cmt_poab_factsheet_cargo_2025,POAB maritime cargo L5 segments 2025 dual NSP,port_antwerp_bruges,Port users logistics industry energy,Port Authority public factsheet 2025,2025-01-01,2025,2025,0,"{""throughput_Mt"":266.5,""containers_Mt"":149.4,""containers_teu_m"":13.6,""dry_bulk_Mt"":13.1,""new_cars"":3186000,""lng_us_Mt"":3.7,""lng_ru_Mt"":4.3,""us_partner_Mt"":31.3,""cruise_pax"":466089,""vessels"":20236,""gt_m"":642,""hlh_share_pct"":29.3,""note"":""Strong primary factsheet volumes; Authority euro budget residual FOI; dual NSP ~67 Mt class""}",0,active,https://newsroom.portofantwerpbruges.com/en/press-releases/port-of-antwerp-bruges-ends-2025-with-resilience-in-a-turbulent-trading-climate,Handle maritime cargo energy and logistics Flanders,Publish Authority P&L L5 + municipal dividend; dual NSP unit,src_poab_factsheet_2025,strong,Vlaanderen>Haven>POAB>cargo_L5_2025,tick575 deepen tick574 volumes',
        'cmt_pidpa_ops_2025,Pidpa drinking+sewer ops 2025 dual DWG Farys,pidpa,Antwerp province households municipalities,Pidpa mandate + Ambitie 2030 + joint digital meters,2025-01-01,2025,2030,0,"{""prod_Mm3"":62.4,""users_m"":1.5,""connections"":603000,""digital_meters"":200000,""digital_pct"":34.1,""sewer_km"":5768,""sewer_munis"":48,""nrw_pct"":8.6,""ili"":0.45,""pipe_replace_km"":158,""omzet_m_prior"":402.7,""invest_m_prior"":183,""note"":""Strong JV2025 ops; fin already tick179; dual DWG 125.4 Mm3 / 3.4m cust""}",0,active,docs/doge/data/raw/pidpa_jv_2025.pdf,Produce distribute drink water and municipal sewer Antwerp,Publish unit cost vs DWG Farys; keep ILI leadership; FOI tariff split residual,src_pidpa_jv_2025,strong,Vlaanderen>Drinkwater>Pidpa>ops_2025,tick575',
        'cmt_dual_ports_poab_nsp_2025,Dual Belgian seaports POAB vs North Sea Port scale,gg_belgium,Port users BE logistics,Public port authorities POAB + NSP,2023-01-01,2023,2025,0,"{""poab_Mt_2025"":266.5,""poab_omzet_m_2025"":507.0,""nsp_Mt_class"":67,""nsp_omzet_m_2023"":115.0,""note"":""Not TE-additive; dual port authority scale comparison""}",0,active,docs/doge/data/raw/poab_factsheet_2025.pdf,Comparable dual port efficiency,NSP 2024-25 full accounts + POAB Authority euro FOI,src_dual_ports_poab_nsp_tick575,strong,BE>dual>Ports_POAB_NSP,tick575',
        'cmt_dual_water_dwg_pidpa_2025,Dual VL drinking De Watergroep + Pidpa 2025,gg_belgium,Flanders households municipalities,DWG 2025 + Pidpa JV/fin 2025,2025-01-01,2025,2025,0,"{""dwg_omzet_m"":974,""dwg_prod_Mm3"":125.4,""dwg_cust_m"":3.4,""pidpa_omzet_m"":402.7,""pidpa_prod_Mm3"":62.4,""pidpa_users_m"":1.5,""joint_digital_meters"":true,""note"":""Not TE-additive; dual VL drinking stack + Farys Water-link prior""}",0,active,docs/doge/data/raw/pidpa_jv_2025.pdf,Comparable dual VL drinking water,Unit-cost FOI both + Farys,src_dual_water_dwg_pidpa_tick575,strong,BE>dual>VL_drink_DWG_Pidpa,tick575',
    ]
    append_rows(DATA / "commitments.csv", commitments)

    # --- leaderboard ---
    leaderboard = [
        "lb_poab_containers_149mt,POAB containers 149.4 Mt / 13.6m TEU 2025,Flanders,ops,Vlaanderen>Haven>POAB>containers,0,149400000,Strong factsheet: containers 149.4 Mt +0.4pct / 13.6m TEU +0.7pct; HLH share 29.3pct -1.2pp; not Authority euro spend,strong,src_poab_factsheet_2025,Port users shipping lines,Container hub Flanders,Core logistics infra; industrial action + congestion risk; dual NSP smaller scale,3,8.5,7,5.85,Publish Authority CAPEX/dividend L5; track congestion cost,seed,,tick575",
        "lb_poab_lng_us_ru_2025,POAB LNG US 3.7 Mt + Russia 4.3 Mt 2025,Flanders,ops,Vlaanderen>Haven>POAB>LNG,0,8000000,Strong factsheet: US LNG 3.7 Mt 4x; Russia 4.3 Mt -16.6pct; Qatar 1.5 Mt; EU Russian LNG ban path 2027; volumes not public spend,strong,src_poab_factsheet_2025,Energy importers BE/EU,Energy security liquid bulk,Strategic energy flow not waste; transition risk residual FOI on public CAPEX,4,7.5,6,5.95,Track public LNG terminal support cash; dual energy policy,seed,,tick575",
        "lb_poab_dry_bulk_13mt,POAB dry bulk 13.1 Mt -12.1pct 2025,Flanders,ops,Vlaanderen>Haven>POAB>dry_bulk,0,13100000,Strong: dry bulk 13.1 Mt; coal -61.6pct fertilizers main; dual energy transition signal,strong,src_poab_factsheet_2025,Industry agriculture,Bulk commodities,Volume decline not euro waste; coal collapse dual climate,3,6.5,7,4.85,Monitor coal residual public supports,seed,,tick575",
        "lb_poab_roro_cars_3_2m,POAB RoRo new cars 3.186m 2025,Flanders,ops,Vlaanderen>Haven>POAB>RoRo_cars,0,3186000,Strong: 3.186m new cars -1.2pct; China +11pct overtook Japan; used cars +37pct; dual auto industrial policy,strong,src_poab_factsheet_2025,Auto industry logistics,Vehicle logistics hub,Core trade infra; China EV import pressure dual,3,7.0,7,5.1,Track public auto support vs port volumes,seed,,tick575",
        "lb_pidpa_ops_62mm3,Pidpa production 62.4 Mm3 users 1.5m dual DWG,Flanders,ops,Vlaanderen>Drinkwater>Pidpa>2025,402730385,1594848019,Strong JV+fin: omzet 403m prod 62.4 Mm3 users 1.5m NRW 8.6 ILI 0.45 invest 183m assets 1.59bn; dual DWG 974m/125 Mm3,strong,src_pidpa_jv_2025,Antwerp province households,Essential drinking water sewer,Core utility tariff-financed; dual DWG Farys scale; digital meter joint,3,8.5,6,5.85,Publish unit cost vs DWG; keep leak leadership,seed,,tick575",
        "lb_dual_ports_poab_nsp,Dual ports POAB 266.5 Mt vs NSP ~67 Mt,multi,ops,BE>dual>Ports_POAB_NSP,506962443,115017000,Strong dual: POAB 266.5 Mt omzet ~507m vs NSP class 67 Mt omzet 115m 2023; institutional dual BE seaports,strong,src_dual_ports_poab_nsp_tick575,BE logistics,Seaport authorities,Core infra dual ports; not waste; FOI Authority euro both,4,8.0,6,6.0,Open Authority accounts + municipal dividends both ports,seed,,tick575",
        "lb_dual_drink_dwg_pidpa,Dual VL drink DWG 974m + Pidpa 403m,Flanders,ops,BE>dual>VL_drink_DWG_Pidpa,974000000,402730385,Strong dual: DWG omzet 974m prod 125.4 vs Pidpa 403m/62.4; joint digital meters Farys; not TE-additive,strong,src_dual_water_dwg_pidpa_tick575,Flanders households,Drinking water dual intercommunales,Core utility; multi-entity overhead risk dual Farys Water-link,4,8.5,6,6.1,Unit-cost matrix four VL water companies,seed,,tick575",
    ]
    append_rows(DATA / "leaderboard.csv", leaderboard)

    # --- entities update ---
    replace_line_prefix(
        DATA / "entities.csv",
        "pidpa,",
        "pidpa,Pidpa,Pidpa,Antwerp province public drinking water and sewerage,parastatal,sec_flanders,nl,https://www.pidpa.be,,,Omzet 403m prod 62.4 Mm3 users 1.5m connections 603k NRW 8.6 ILI 0.45 sewer 5768km 48 munis digital meters 200k 2025; dual DWG; tick575",
    )
    replace_line_prefix(
        DATA / "entities.csv",
        "port_antwerp_bruges,",
        "port_antwerp_bruges,Port of Antwerp-Bruges,Haven Antwerpen-Brugge,Antwerp-Bruges port authority public law,parastatal,sec_flanders,bi,https://www.portofantwerpbruges.com,,,Throughput 266.5 Mt 2025; containers 149.4 Mt/13.6m TEU; dry bulk 13.1 Mt; LNG US 3.7 Ru 4.3; cars 3.186m; dual NSP; tick575",
    )

    # --- FOI: deepen residual authority budget already open; add Pidpa tariff L5 if useful ---
    foi_path = DATA / "foi_queue.csv"
    # update existing gap_poab_authority note
    enc = detect_enc(foi_path)
    lines = foi_path.read_text(encoding=enc).splitlines()
    out = []
    for l in lines:
        if l.startswith("gap_poab_authority_budget_l5,"):
            # bump updated note
            parts = l.split(",")
            # safer: append note via full rewrite of line
            l = (
                "gap_poab_authority_budget_l5,Vlaanderen>Haven>POAB>authority_budget_L5,port_antwerp_bruges,"
                "Port Authority annual accounts 2024-26; investment path ECA; public vs commercial cash; dual municipal dividends Antwerp Bruges; recon NBB omzet 507m vs factsheet volumes,"
                "Throughput L5 strong factsheet tick575; Authority euro budget residual,"
                "4,Port of Antwerp-Bruges / cities Antwerp Bruges,,https://www.portofantwerpbruges.com,"
                "docs/doge/foi/drafts/gap_poab_authority_budget_l5.md,ready,2026-07-31,,,,"
                "cmt_poab_throughput_2025|cmt_poab_factsheet_cargo_2025,lb_poab_throughput_267mt|lb_poab_containers_149mt,"
                "2026-07-31T10:55:00Z,2026-07-31T11:00:00Z,tick574 volumes + tick575 factsheet L5; residual Authority euro human send"
            )
        out.append(l)
    # add Pidpa residual FOI if not present
    if not any(l.startswith("gap_pidpa_tariff_l5_2025,") for l in out):
        out.append(
            "gap_pidpa_tariff_l5_2025,Vlaanderen>Pidpa>tariff_public_L5_2025,pidpa,"
            "Tariff vs municipal/public cash split 2024-26; top20 munis sewer; digital meter CAPEX cash path joint Farys/DWG; dual unit-cost DWG,"
            "Ops+fin aggregates strong; tariff composition and public cash residual dual,"
            "5,Pidpa / Team Openbaarheid,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
            "docs/doge/foi/drafts/gap_pidpa_tariff_l5_2025.md,ready,2026-07-31,,,,"
            "cmt_pidpa_ops_2025|cmt_dual_water_dwg_pidpa_2025,lb_pidpa_ops_62mm3|lb_dual_drink_dwg_pidpa,"
            f"{NOW},{NOW},tick575 Pidpa JV ops; residual tariff L5 human send"
        )
    foi_path.write_text("\n".join(out) + "\n", encoding=enc, newline="\n")

    # FOI draft
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft = FOI_DRAFTS / "gap_pidpa_tariff_l5_2025.md"
    if not draft.exists():
        draft.write_text(
            """# Openbaarheidsverzoek — Pidpa tarief/public cash L5 2025

**Status:** ready (niet verzonden door agent)  
**Gap ID:** gap_pidpa_tariff_l5_2025  
**Bestemmeling:** Pidpa / Team Openbaarheid Vlaanderen  
**Datum klaar:** 2026-07-31

## Vraag (NL)

Geachte,

Op basis van het Bestuursdecreet verzoek ik om de volgende documenten/gegevens over Pidpa (boekjaren 2024-2026):

1. Opsplitsing omzet drinkwater vs bovengemeentelijke/gemeentelijke sanering vs werken: tariefcomponenten vs eventuele overheidsdotaties of kapitaalsubsidies (cash per jaar).
2. Top-20 gemeenten naar saneringsomzet / rioleringsbeheer-contractwaarde 2025.
3. Investeringskasstromen digitale watermeters 2023-2026 (aanschaf, installatie, IT), inclusief aandeel gezamenlijke aankoop met Farys/De Watergroep/Fluvius.
4. Eenheidskosten (EUR/m³ geproduceerd; EUR/aansluiting; EUR/km leiding vervangen) 2024-2025 indien intern beschikbaar.

Publiek al bekend (jaarverslag/financieel 2025): omzet ~403m; productie 62,4 Mm³; gebruikers ~1,5m; NRW ~8,6%; investeringen ~183m. Dit verzoek betreft de tarief- vs publieke cash-opsplitsing en unit-costs.

Gelieve digitaal te antwoorden. Alvast dank.

*(Concept — agent verzendt niet tenzij expliciet bevolen.)*
""",
            encoding="utf-8",
        )

    # --- research_queue: close rq_566, spawn rq_567 ---
    rq = DATA / "research_queue.csv"
    enc = detect_enc(rq)
    rlines = rq.read_text(encoding=enc).splitlines()
    out_r = []
    for l in rlines:
        if l.startswith("rq_566,"):
            l = (
                "rq_566,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
                "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
                f"2026-07-31T10:55:00Z,{NOW},"
                "tick575: POAB factsheet L5 cargo + Pidpa ops dual DWG; spawn rq_567; rq_116 deferred"
            )
        out_r.append(l)
    if not any(l.startswith("rq_567,") for l in out_r):
        out_r.append(
            "rq_567,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
            f"{NOW},,"
            "Spawned tick575 after POAB L5+Pidpa dual; rq_116 deferred; progress@580 in 5 ticks"
        )
    rq.write_text("\n".join(out_r) + "\n", encoding=enc, newline="\n")

    # --- loop_state ---
    state = DATA / "loop_state.csv"
    state.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{NOW},{UNIT},{TICK},no,"
        "tick575 POAB factsheet L5 cargo + Pidpa ops dual DWG; next rq_567; progress@580 in 5; rq_116 deferred\n",
        encoding="utf-8",
        newline="\n",
    )

    # --- loop_log append ---
    log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **POAB factsheet 2025 L5 cargo dual NSP + Pidpa JV2025 ops dual DWG**)
- Found (strong primary POAB factsheet PDF + Pidpa JV2025 62 pp):
  - **POAB containers 149.4 Mt / 13.6m TEU** (+0.4% / +0.7%); HLH share **29.3%** (−1.2pp)
  - **Dry bulk 13.1 Mt** (−12.1%); coal **−61.6%**; fertilizers main
  - **RoRo new cars 3.186m** (−1.2%); China origin **+11%**; used cars **+37%**; RoRo **+3%**
  - **LNG:** US **3.7 Mt** (>4×); Russia **4.3 Mt** (−16.6%); Qatar **1.5 Mt**; petroleum products **−19%**
  - US partner split in/out **19.7 / 11.7 Mt**; cruise Zeebrugge **466k pax** (−16.4%); vessels **20,236** / GT **642m**
  - **Pidpa:** prod **62.4 Mm³** pure; users **1.5m**; connections **603k**; digital meters **>200k (34.1%)**
  - Sewer **5,768 km** / **48** munis; NRW **8.60%** ILI **0.45**; replace **158 km** (1.18%); alt water **2 Mm³**
  - Energy primary **~81.3 GWh**; CO₂ **14,149 t**; 11 WPC (new Oud-Turnhout)
  - **Dual ports:** POAB **266.5 Mt** / omzet ~**507m** vs NSP class **~67 Mt** / **115m** (2023)
  - **Dual drink:** DWG **974m / 125.4 Mm³ / 3.4m** vs Pidpa **403m / 62.4 / 1.5m**
- Wrote: sources +4; budgets +31; cmt +4; lb +7; FOI **gap_pidpa_tariff_l5_2025** ready+draft; update gap_poab_authority; entities; raw PDFs; rq_566=done spawn **rq_567**; ticks={TICK}
- FOI opened: gap_pidpa_tariff_l5_2025 (ready, human send) — not sent; gap_poab_authority_budget_l5 updated
- Next: prio5 **rq_567**; deferred **rq_116**; progress@580 in 5 ticks
"""
    enc_log = detect_enc(LOG)
    log_text = LOG.read_text(encoding=enc_log)
    if not log_text.endswith("\n"):
        log_text += "\n"
    LOG.write_text(log_text + log_entry, encoding=enc_log, newline="\n")

    print(f"OK tick {TICK} unit {UNIT} — POAB L5 + Pidpa dual written")


if __name__ == "__main__":
    main()

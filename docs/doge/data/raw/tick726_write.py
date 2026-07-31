# tick726 — OTW/LETEC residual dual L5 CSP revision + missions transfer + reliability (rq_717)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-01T23:45:00Z"
URL_RA = "https://mobilite.wallonie.be/files/eDocsMobilite/bus%20tram%20metro/letec-rapport-annuel-2025.pdf"
URL_PRESS = "https://presse.groupe.letec.be/contrat-de-service-public-revise-et-resultats-2025-valides-letec-consolide-son-plan-de-transformation-jusque-2029"
URL_PDF_CDN = "https://cdn.assets.prezly.com/5c946eda-1738-448c-9523-747aa6acffaf/-/inline/no/LETEC%20Rapport%20annuel%202025.pdf"

SRC = "src_letec_ra_csp_residual_tick726"
SRC_PRESS = "src_letec_csp_revise_press_2026_06"
SRC_DUAL = "src_dual_otw_delijn_ebus_missions_tick726"

budgets = [
    # Coverage / reliability KPIs (pct stored as number; note PCT)
    ("bud_otw_coverage_rate_2024", "tec", 2024, 14.36, "", "", "outturn", SRC, "strong", "PCT coverage own op receipts / opex 14.36 2024 RA; tick726"),
    ("bud_otw_coverage_rate_2025", "tec", 2025, 14.21, "", "", "outturn", SRC, "strong", "PCT coverage 14.21 2025 (already near/above Desquesnes 10-to-14 by 2030 narrative); tick726"),
    ("bud_otw_service_rate_2024", "tec", 2024, 97.35, "", "", "outturn", SRC, "strong", "PCT service execution km 97.35 2024; tick726"),
    ("bud_otw_service_rate_2025", "tec", 2025, 95.74, "", "", "outturn", SRC, "strong", "PCT service execution 95.74 2025 (-1.61pp YoY tram year); CSP target 99.8; tick726"),
    ("bud_otw_service_gap_vs_target_2025", "tec", 2025, 4.06, "", "", "outturn", SRC, "strong", "PCT gap 99.8 target minus 95.74 actual ~4.06pp; tick726"),
    ("bud_otw_satisfaction_2025", "tec", 2025, 62, "", "", "outturn", SRC, "strong", "PCT client satisfaction 62 vs CSP target 70; tick726"),
    ("bud_otw_satisfaction_gap_2025", "tec", 2025, 8, "", "", "outturn", SRC, "strong", "PCT satisfaction gap 70-62=8pp; tick726"),
    ("bud_otw_fraud_rate_2025", "tec", 2025, 3.52, "", "", "outturn", SRC, "strong", "PCT fraud rate 3.52 2025 RA chiffres; tick726"),
    # CA press vs farebox prior
    ("bud_otw_ca_press_2025", "tec", 2025, 135700000, "", "", "outturn", SRC_PRESS, "strong", "Press AG 10Jun2026: chiffre affaires 135.7m (+~3pct vs 2024); broader than farebox 66.4m RF; tick726"),
    ("bud_otw_ca_vs_farebox_wedge_2025", "tec", 2025, 69273300, "", "", "estimate", SRC, "medium", "Derived wedge CA press 135.7m minus traffic CA 66.427m ~69.3m other commercial/perimeter; tick726"),
    # Voyages residual
    ("bud_otw_voyages_regular_2025", "tec", 2025, 150767081, "", "", "outturn", SRC, "strong", "COUNT regular line voyages 150767081; tick726 recon tick567"),
    ("bud_otw_voyages_total_all_modes_2025", "tec", 2025, 159434791, "", "", "outturn", SRC, "strong", "COUNT total voyages all modes 159434791 (regular+scolaire+TPMR+special+TaD+Flexi); tick726"),
    ("bud_otw_voyages_scolaire_2025", "tec", 2025, 7071005, "", "", "outturn", SRC, "strong", "COUNT scolaire voyages 7071005 (-3.5pct YoY); tick726"),
    ("bud_otw_voyages_tpmr_2025", "tec", 2025, 231202, "", "", "outturn", SRC, "strong", "COUNT TPMR voyages 231202 (+0.9pct); tick726"),
    ("bud_otw_voyages_special_2025", "tec", 2025, 1326467, "", "", "outturn", SRC, "strong", "COUNT special/other regular specialised voyages 1326467; tick726"),
    ("bud_otw_voyages_tad_2025", "tec", 2025, 33933, "", "", "outturn", SRC, "strong", "COUNT LETEC a la demande 33933; press ~650 pax/week on 6 lines; tick726"),
    ("bud_otw_voyages_flexi_taxi_2025", "tec", 2025, 5103, "", "", "outturn", SRC, "strong", "COUNT FlexiTEC+TaxiTEC 5103; tick726"),
    ("bud_otw_tram_liege_voyages_y1_press", "tec", 2025, 12000000, "", "", "outturn", SRC_PRESS, "strong", "Press: tram Liege >12m voyages first year of service from 28 Apr 2025; tick726"),
    # Scolaire mission residual
    ("bud_otw_scolaire_pupils_2025", "tec", 2025, 21589, "", "", "outturn", SRC, "strong", "COUNT pupils scolaire daily 21589 (2024:21856); tick726"),
    ("bud_otw_scolaire_circuits_2025", "tec", 2025, 915, "", "", "outturn", SRC, "strong", "COUNT scolaire circuits 915; reliability 100pct assigned; tick726"),
    ("bud_otw_scolaire_km_2025", "tec", 2025, 21991909, "", "", "outturn", SRC, "strong", "COUNT scolaire km en charge 21991909; tick726"),
    ("bud_otw_scolaire_used_recon_2025", "tec", 2025, 65335707, "", "", "outturn", SRC, "strong", "EUR scolaire used 65.336m recon RF tick567; transfer to SPW MI validated GW Mar2026; tick726"),
    ("bud_otw_tpmr_used_recon_2025", "tec", 2025, 4911036, "", "", "outturn", SRC, "strong", "EUR TPMR used 4.911m recon RF; CSP transfer to SPW MI planned; tick726"),
    ("bud_otw_delegated_missions_used_recon", "tec", 2025, 136220099, "", "", "outturn", SRC, "strong", "EUR delegated missions total used 136.2m recon RF; school+TPMR exit path reduces OTW perimeter; tick726"),
    # Fleet e-bus lag dual De Lijn
    ("bud_otw_fleet_regie_2025", "tec", 2025, 1945, "", "", "outturn", SRC, "strong", "COUNT regie vehicles 1945; tick726"),
    ("bud_otw_fleet_private_2025", "tec", 2025, 796, "", "", "outturn", SRC, "strong", "COUNT private operator vehicles 796; tick726"),
    ("bud_otw_fleet_total_2025", "tec", 2025, 2741, "", "", "outturn", SRC, "strong", "COUNT total fleet 2741; tick726"),
    ("bud_otw_hybrid_count_2025", "tec", 2025, 829, "", "", "outturn", SRC, "strong", "COUNT hybrid regie 829 (42.62pct); tick726"),
    ("bud_otw_ebus_count_2025", "tec", 2025, 14, "", "", "outturn", SRC, "strong", "COUNT electric regie only 14 (0.72pct) first BUSWAY B2; tick726"),
    ("bud_otw_ebus_path_170_to_2029", "tec", 2029, 170, "", "", "budgeted", SRC_PRESS, "strong", "COUNT 170 e-buses deliveries path to 2029 press; aju bus -43.5m delay; tick726"),
    ("bud_dual_delijn_ebus_ordered_652", "de_lijn", 2025, 652, "", "", "outturn", SRC_DUAL, "strong", "COUNT dual De Lijn 652 e-buses ordered 2025 vs OTW 14 in service; tick726"),
    ("bud_dual_delijn_ebus_extra_400m", "de_lijn", 2025, 400000000, "", "", "budgeted", SRC_DUAL, "strong", "EUR dual De Lijn e-bus extra 400m vs OTW greening PNRR +21.3m path aju; tick726"),
    # Staff
    ("bud_otw_staff_total_2025", "tec", 2025, 5818, "", "", "outturn", SRC, "strong", "COUNT staff 5818; tick726"),
    ("bud_otw_drivers_2025", "tec", 2025, 3500, "", "", "outturn", SRC, "strong", "COUNT drivers 3500; tick726"),
    ("bud_otw_employees_2025", "tec", 2025, 1440, "", "", "outturn", SRC, "strong", "COUNT employees 1440; tick726"),
    ("bud_otw_other_workers_2025", "tec", 2025, 878, "", "", "outturn", SRC, "strong", "COUNT other workers/ouvriers 878; tick726"),
    # Recalibrage / CSP orientation
    ("bud_otw_recalibrage_capacity_2pct", "tec", 2026, 2, "", "", "budgeted", SRC, "strong", "PCT Dec2025 GW orientation: recalibrage 2pct operational capacity while maintaining global offer level; tick726"),
    ("bud_otw_csp_service_target_99_8", "tec", 2025, 99.8, "", "", "budgeted", SRC, "strong", "PCT CSP key indicator target service execution 99.8; tick726"),
    ("bud_otw_csp_satisfaction_target_70", "tec", 2025, 70, "", "", "budgeted", SRC, "strong", "PCT CSP client satisfaction target 70; tick726"),
    # CO2 residual
    ("bud_otw_co2_kg_per_pax_2024", "tec", 2024, 0.8052, "", "", "outturn", SRC, "strong", "kgCO2 per voyageur 0.8052 2024; tick726"),
    ("bud_otw_co2_kg_per_pax_2025", "tec", 2025, 0.7758, "", "", "outturn", SRC, "strong", "kgCO2 per voyageur 0.7758 2025 (now includes metro/tram/e-bus electricity 181.7g/kWh); tick726"),
    # Accessibility
    ("bud_otw_stops_accessible_2025", "tec", 2025, 3924, "", "", "outturn", SRC, "strong", "COUNT audited accessible boarding points 3924 (2024:3672); tick726"),
    ("bud_otw_stops_total_2025", "tec", 2025, 31861, "", "", "outturn", SRC, "strong", "COUNT stops total 31861; tick726"),
    ("bud_otw_lines_regular_2025", "tec", 2025, 832, "", "", "outturn", SRC, "strong", "COUNT regular lines 832; tick726"),
    # Dual km
    ("bud_otw_km_regie_2025", "tec", 2025, 64096117, "", "", "outturn", SRC, "strong", "COUNT km regie regular 64096117; tick726"),
    ("bud_otw_km_private_2025", "tec", 2025, 31398292, "", "", "outturn", SRC, "strong", "COUNT km private operators 31398292; tick726"),
    ("bud_otw_km_total_regular_2025", "tec", 2025, 95494409, "", "", "outturn", SRC, "strong", "COUNT km total regular en charge 95494409; tick726"),
    # Aju recon capital lag (already partial) reinforce dual
    ("bud_otw_pnrr_greening_bus_21_3m", "tec", 2026, 21300000, "", "", "budgeted", "src_ccrek_wal_aju2026_recettes_otw", "strong", "PNRR greening bus fleet +21.3m aju path recon; dual De Lijn 400m; tick726"),
    ("bud_otw_pnrr_chatelet_10m", "tec", 2026, 10000000, "", "", "budgeted", "src_ccrek_wal_aju2026_recettes_otw", "strong", "PNRR Chatelet antenna reno/extension +10m; tick726"),
    ("bud_dual_otw_dep_aju_vs_delijn_class", "gg_belgium", 2026, 1196300000, "", "", "budgeted", SRC_DUAL, "strong", "OTW dep aju 1196.3m dual De Lijn multi-bn VEK class not additive; tick726"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_otw_csp_revise_2026_2029",
        "LETEC CSP revision signed Jun2026 extended to 2029 dual missions exit",
        "tec",
        "Walloon public transport users / RW taxpayers",
        "CSP 2024-2028 revise + GW orientation Dec2025 + sign 10 Jun 2026",
        "2026-06-10",
        2026,
        2029,
        0,
        '{"signed":"2026-06-10","extend_to":2029,"recalibrage_pct":2,"service_target_pct":99.8,"satisfaction_target_pct":70,"coverage_actual_2025_pct":14.21,"missions_exit":["scolaire","TPMR"],"transfer_to":"SPW_MI","scolaire_gw_mar2026":true,"internal_savings_20m_by":2029,"coverage_narrative_10_to_14_by":2030,"note":"coverage already 14.21 on RA metric"}',
        0,
        "active",
        URL_PRESS,
        "Clearer funded CSP more autonomy better reliability modal shift",
        "Publish CSP cash tables dual De Lijn + FOI transfer calendar euro path",
        SRC_PRESS,
        "strong",
        "Wallonie>OTW>CSP_2026_29",
        "tick726 residual CSP+missions",
    ),
    (
        "cmt_otw_reliability_gap_2025",
        "OTW service 95.74 vs target 99.8 and satisfaction 62 vs 70",
        "tec",
        "Walloon passengers",
        "CSP strategic indicators + RA 2025",
        "2024-01-18",
        2025,
        2026,
        0,
        '{"service_2024":97.35,"service_2025":95.74,"service_target":99.8,"gap_pp":4.06,"satisfaction":62,"sat_target":70,"sat_gap_pp":8,"fraud_pct":3.52,"recalibrage_2pct":true,"tram_year":true}',
        0,
        "active",
        URL_RA,
        "Reliable attractive public transport",
        "Close reliability gap before capacity cut narrative; FOI penalty/service fail euro",
        SRC,
        "strong",
        "Wallonie>OTW>reliability_KPIs",
        "tick726",
    ),
    (
        "cmt_otw_scolaire_tpmr_transfer_spw",
        "Scolaire+TPMR delegated missions transfer OTW to SPW MI",
        "tec",
        "21589 scolaire pupils + TPMR users + SPW MI",
        "CSP 2024-28 + GW Mar2026 scolaire + CSP TPMR clause",
        "2026-03-01",
        2026,
        2028,
        70246743,
        '{"scolaire_used_2025_m":65.336,"tpmr_used_2025_m":4.911,"pupils":21589,"circuits":915,"tpmr_voyages":231202,"scolaire_validated":"2026-03","tpmr_csp_planned":true,"transfer_year_press":2028,"delegated_total_used_m":136.2}',
        70246743,
        "active",
        URL_RA,
        "Core-business focus transfer specialised missions to AOT",
        "FOI transfer cash calendar staff FTE dual De Lijn school transport",
        SRC,
        "strong",
        "Wallonie>OTW>missions_deleguees_transfer",
        "tick726",
    ),
    (
        "cmt_otw_ebus_lag_dual_delijn",
        "OTW e-bus 14 of 1945 vs De Lijn 652 ordered +400m",
        "tec",
        "Walloon climate modal-shift path",
        "RA 2025 fleet + press 170 path + De Lijn dual",
        "2025-09-15",
        2025,
        2029,
        0,
        '{"otw_ebus_2025":14,"otw_hybrid":829,"otw_regie":1945,"otw_ebus_pct":0.72,"path_170_to_2029":true,"aju_bus_cut_m":-43.5,"pnrr_greening_m":21.3,"delijn_ordered":652,"delijn_extra_m":400,"note":"not TE-additive dual fleet decarbonisation pace"}',
        0,
        "active",
        URL_RA,
        "Decarbonise bus fleet dual Entity II PT",
        "Publish e-bus delivery cash calendar dual VL; close tender lag FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>PT_ebus_OTW_DeLijn",
        "tick726",
    ),
    (
        "cmt_otw_coverage_metric_vs_narrative",
        "Coverage rate already 14.21pct vs CSP 10-to-14 by 2030 narrative",
        "tec",
        "RW taxpayers farebox reform",
        "RA indicator definition own op receipts/opex + Desquesnes CSP press",
        "2025-12-01",
        2025,
        2030,
        0,
        '{"coverage_2024":14.36,"coverage_2025":14.21,"narrative_from":10,"narrative_to":14,"by":2030,"definition":"recettes_propres_op / charges_exploitation","ca_press_m":135.7,"farebox_rf_m":66.4,"note":"metric already at/above 14; check if narrative uses different base"}',
        0,
        "active",
        URL_RA,
        "Raise farebox coverage efficiency",
        "FOI reconcile coverage definition vs CSP KPI series",
        SRC,
        "strong",
        "Wallonie>OTW>coverage_KPI",
        "tick726",
    ),
    (
        "cmt_dual_otw_delijn_missions_tick726",
        "Dual OTW delegated missions exit vs De Lijn integrated school/ops",
        "gg_belgium",
        "Regional PT authorities dual",
        "OTW RA residual + De Lijn prior dual",
        "2026-03-01",
        2026,
        2028,
        0,
        '{"otw_scolaire_m":65.3,"otw_tpmr_m":4.9,"otw_dep_aju_m":1196.3,"delijn_ebus_extra_m":400,"note":"not TE-additive architecture dual"}',
        0,
        "active",
        URL_RA,
        "Comparable PT perimeter transparency Entity II",
        "Publish dual school-transport unit-cost FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>PT_missions_OTW_DeLijn",
        "tick726",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

# priority_index heuristic ~ (absurdity*0.4 + cost*0.35 + (10-difficulty)*0.25) style used prior
lbs = [
    (
        "lb_otw_service_gap_4pp_2025",
        "OTW service execution 95.74 vs CSP target 99.8 (~4pp gap)",
        "regional",
        "ops",
        "Wallonie>OTW>service_execution",
        0,
        0,
        "Strong RA: km execution 95.74 2025 (97.35 2024) vs CSP 99.8; tram year + recalibrage 2pct capacity",
        "strong",
        SRC,
        "Walloon passengers",
        "99.8pct reliable service",
        "Misses target by ~4pp while cutting capacity 2pct",
        7.5,
        5.5,
        4,
        6.55,
        "Restore reliability before capacity cut; publish fail euro",
        "seed",
        "",
        "tick726",
    ),
    (
        "lb_otw_satisfaction_gap_8pp",
        "OTW client satisfaction 62 vs CSP target 70",
        "regional",
        "ops",
        "Wallonie>OTW>satisfaction",
        0,
        0,
        "Strong RA/CSP: 62pct vs 70 target; fraud 3.52; dual service gap",
        "strong",
        SRC,
        "Passengers",
        "Attractive PT",
        "8pp below CSP KPI",
        6.5,
        4.5,
        4,
        5.65,
        "Focus on reliability info billettique",
        "seed",
        "",
        "tick726",
    ),
    (
        "lb_otw_coverage_already_14pct",
        "Coverage 14.21pct already vs 10-to-14 by 2030 CSP narrative",
        "regional",
        "tax_spend",
        "Wallonie>OTW>coverage_KPI",
        0,
        0,
        "Strong RA: coverage own receipts/opex 14.21 2025 (14.36 2024); Desquesnes press still cites path 10 to 14 by 2030 — metric mismatch risk",
        "strong",
        SRC,
        "Taxpayers",
        "Higher farebox share",
        "Narrative lag vs measured 14pct",
        7.0,
        5.0,
        3,
        6.35,
        "Publish official coverage definition series FOI",
        "seed",
        "",
        "tick726",
    ),
    (
        "lb_otw_ebus_14_of_1945",
        "OTW only 14 e-buses (0.72pct) of 1945 regie fleet 2025",
        "regional",
        "climate_ops",
        "Wallonie>OTW>ebus_lag",
        0,
        0,
        "Strong RA: 14 electric + 829 hybrid; path 170 to 2029; aju bus acq -43.5m delays; dual De Lijn 652 ordered +400m",
        "strong",
        SRC_DUAL,
        "Climate modal shift",
        "Decarbonised fleet",
        "0.72pct electric vs VL scale-up",
        7.0,
        6.5,
        5,
        6.55,
        "Accelerate tenders close delivery lag FOI calendar",
        "seed",
        "",
        "tick726",
    ),
    (
        "lb_otw_scolaire_tpmr_transfer_opacity",
        "Scolaire 65.3m + TPMR 4.9m transfer to SPW without full cash path",
        "regional",
        "governance",
        "Wallonie>OTW>missions_transfer",
        70246743,
        0,
        "Strong RA+RF: scolaire validated GW Mar2026; TPMR CSP exit; used 65.3+4.9m 2025; press transfer 2028; dual De Lijn architecture",
        "strong",
        SRC,
        "Pupils PRM users SPW",
        "Core-business focus",
        "70m+ annual missions exit without published multi-year euro path",
        6.5,
        7.0,
        4,
        6.55,
        "FOI transfer cash FTE dual unit-cost",
        "seed",
        "",
        "tick726",
    ),
    (
        "lb_otw_ca_perimeter_wedge_69m",
        "CA press 135.7m vs farebox RF 66.4m ~69m perimeter wedge",
        "regional",
        "transparency",
        "Wallonie>OTW>CA_perimeter",
        69273300,
        0,
        "Strong: press CA 135.7m; RF traffic CA 66.427m; other op products 773m dominate; dual STIB/De Lijn reporting",
        "strong",
        SRC_PRESS,
        "Parliament taxpayers",
        "Transparent operator finances",
        "Public CA figure not equal farebox",
        6.0,
        6.0,
        3,
        6.0,
        "Standardise CA vs compensation tables FOI",
        "seed",
        "",
        "tick726",
    ),
    (
        "lb_dual_otw_delijn_ebus_missions",
        "Dual OTW e-bus lag + missions exit vs De Lijn integrated scale",
        "Belgium",
        "ops",
        "Belgium>dual>PT_OTW_DeLijn",
        0,
        0,
        "Strong dual residual: OTW 14 e-bus + 70m mission transfer path vs De Lijn 652 e-bus +400m; not TE-additive",
        "strong",
        SRC_DUAL,
        "Entity II PT policy",
        "Comparable PT performance",
        "Architecture/pace asymmetry",
        6.5,
        6.0,
        5,
        6.05,
        "Publish dual KPIs unit-cost e-bus school",
        "seed",
        "",
        "tick726",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

sources = [
    (
        SRC,
        "LETEC / OTW Rapport annuel 2025 residual L5 (CSP KPIs fleet missions coverage)",
        URL_RA,
        "LETEC / OTW / mobilite.wallonie.be",
        "2026-08-01",
        "agency_annual_report",
        "Strong tick726: coverage 14.21; service 95.74 vs 99.8; sat 62 vs 70; fraud 3.52; e-bus 14/1945; hybrid 829; scolaire 21589/915/7.07m voy; TPMR 231202; total voyages 159.4m; recalibrage 2pct; staff 5818; raw letec_ra_2025.pdf also CDN",
    ),
    (
        SRC_PRESS,
        "LETEC press CSP revise + 2025 results validated 10 Jun 2026",
        URL_PRESS,
        "LETEC presse / Cabinet Desquesnes / SPW MI",
        "2026-08-01",
        "official_press",
        "Strong tick726: CSP signed extended 2029; CA 135.7m; tram 12m voyages y1; 170 e-buses to 2029; scolaire/TPMR transfer SPW 2028 path; coverage narrative 10-14 by 2030; PDF CDN attached",
    ),
    (
        SRC_DUAL,
        "Dual OTW residual vs De Lijn e-bus + school/ops architecture tick726",
        URL_RA,
        "DOGE synthesis LETEC RA + prior De Lijn sources",
        "2026-08-01",
        "synthesis",
        "Strong dual not TE-additive: OTW 14 e-bus + missions exit 70m class vs De Lijn 652 ordered +400m; tick726",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in sources:
        w.writerow(r)
print("sources +", len(sources))

# research_queue: mark rq_717 done, spawn rq_718
rq_path = DATA / "research_queue.csv"
rows = []
with open(rq_path, encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_717":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick726 OTW/LETEC residual CSP: coverage 14.21 already; service 95.74 vs 99.8; "
                "sat 62 vs 70; e-bus 14/1945 dual De Lijn 652; scolaire+TPMR transfer SPW; FOI gap_otw_csp_missions_transfer_l5 ready"
            )
        rows.append(row)

new_rq = {
    "task_id": "rq_718",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: internal security dual-use residual or new CoA/primary PDF not yet mined "
        "or OTW CSP full text cash tables if published or WAL UAP residual"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick726 after rq_717",
}
rows.append(new_rq)

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue: rq_717=done spawn rq_718")

# foi_queue append
foi_row = (
    "gap_otw_csp_missions_transfer_l5",
    "Wallonie>OTW>CSP_missions_transfer_L5",
    "tec",
    (
        "Full revised CSP 2026-2029 signed text with cash-by-year regional compensation tables; "
        "official coverage-rate definition series reconciling RA 14.21 vs Desquesnes 10-to-14 narrative; "
        "service-failure / penalty euro series behind 95.74 vs 99.8; "
        "scolaire+TPMR transfer calendar cash FTE vehicle stock 2026-2028 dual unit-cost; "
        "e-bus delivery schedule for 170 units cash CAPEX path reconciling aju -43.5m lag"
    ),
    (
        "OTW ~1.2bn company perimeter + 70m missions exit + e-bus lag material; "
        "public RA/press strong on KPIs but CSP cash and transfer euro residual"
    ),
    "7",
    "SPW Mobilité et Infrastructures / OTW publicité administration / Cabinet Desquesnes",
    "",
    "",
    "docs/doge/foi/drafts/gap_otw_csp_missions_transfer_l5.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_otw_csp_revise_2026_2029|cmt_otw_scolaire_tpmr_transfer_spw|cmt_otw_ebus_lag_dual_delijn",
    "lb_otw_service_gap_4pp_2025|lb_otw_ebus_14_of_1945|lb_otw_scolaire_tpmr_transfer_opacity",
    UTC,
    UTC,
    "tick726 OTW residual CSP; not sent; contacts TBD; prior gap_otw_dotatie_cash remains ready",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue +1 gap_otw_csp_missions_transfer_l5 ready")

# loop_state
state_path = DATA / "loop_state.csv"
with open(state_path, encoding="utf-8", newline="") as f:
    rows_s = list(csv.reader(f))
header, row = rows_s[0], rows_s[1]
# state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes
row[3] = UTC
row[4] = "rq_717"
row[5] = "726"
row[7] = (
    "tick726 OTW CSP residual dual De Lijn; coverage 14.21 service gap 4pp e-bus 14/1945 "
    "missions transfer; next rq_718; progress@730 in 4; rq_116 deferred"
)
with open(state_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(header)
    w.writerow(row)
print("loop_state ticks=726")
print("DONE tick726")

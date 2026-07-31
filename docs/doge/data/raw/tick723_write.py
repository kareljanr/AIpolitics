# tick723 — WAL SPAQuE UAP residual L5 dual OVAM
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]

budgets = [
    ("bud_spaque_fin_assets_related_12_125m", "spaque", 2024, 12125000, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Immobilisations financieres entreprises liees 12.125m (parts 125k + creances 12m); tick723"),
    ("bud_spaque_participations_link_886k", "spaque", 2024, 885687.33, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Participations lien de participation 885.7k eoy2024; tick723"),
    ("bud_spaque_stock_immeubles_vente_6_43m", "spaque", 2024, 6428981.44, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Immeubles destines a la vente stock 6.429m eoy2024; tick723"),
    ("bud_spaque_immob_en_cours_1_12m", "spaque", 2024, 1124327.3, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Immobilisations en cours et acomptes 1.124m eoy2024; tick723"),
    ("bud_spaque_corporeal_fixed_5_28m", "spaque", 2024, 5283035.71, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Immobilisations corporelles 5.283m eoy2024; tick723"),
    ("bud_spaque_sites_investigated_24", "spaque", 2024, 24, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "24 sites investigues 2024 = 580 prelevements; tick723"),
    ("bud_spaque_samples_580", "spaque", 2024, 580, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "580 prelevements investigations 2024; tick723"),
    ("bud_spaque_mech_borings_331", "spaque", 2024, 331, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "331 forages mecaniques 2024; tick723"),
    ("bud_spaque_piezometers_121", "spaque", 2024, 121, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "121 piezometres installes 2024; tick723"),
    ("bud_spaque_rehab_sites_7", "spaque", 2024, 7, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "7 chantiers rehabilitation 2024; tick723"),
    ("bud_spaque_materials_t_63810", "spaque", 2024, 63810, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "63810 t materials treated 2024; tick723"),
    ("bud_spaque_materials_recycled_t_29913", "spaque", 2024, 29913, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "29913 t valorisees 47pct recycling 2024; tick723"),
    ("bud_spaque_final_eval_6_sites_33ha", "spaque", 2024, 6, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "6 sites evaluation finale 33 ha 2024; tick723"),
    ("bud_spaque_pv_kwh_3904028", "spaque", 2024, 3904028, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "PV+biogaz production 3904028 kWh 2024 (~935 WAL households); tick723"),
    ("bud_spaque_pv_kwh_3473370", "spaque", 2024, 3473370, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Photovoltaic 3473370 kWh of total renewable; tick723"),
    ("bud_spaque_biogas_kwh_430658", "spaque", 2024, 430658, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Biogas 430658 kWh 2024; tick723"),
    ("bud_spaque_pv_units_service_3", "spaque", 2024, 3, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "3 centrales PV en service + 2 en projet + 3 unites on post-gestion landfills; tick723"),
    ("bud_spaque_maintenance_sites_49", "spaque", 2024, 49, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "49 sites en maintenance 2024 (34 owned SPAQuE + 5 for tiers); tick723"),
    ("bud_spaque_owned_maint_sites_34", "spaque", 2024, 34, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "34 sites propriete SPAQuE en maintenance; tick723"),
    ("bud_spaque_bdes_parcels_ha_14032", "spaque", 2024, 14032, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "14032 ha parcels versed in BDES inventory 2024; tick723"),
    ("bud_spaque_vtr_pollutants_10", "spaque", 2024, 10, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "10 non-normed pollutants with VTR/limit values determined 2024; tick723"),
    ("bud_spaque_stake_recyhoc_pct", "spaque", 2024, 25.1, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "RECYHOC stake 25.1pct delegated mission RW; tick723"),
    ("bud_spaque_stake_recylieges_pct", "spaque", 2024, 25.1, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "RECYLIEGE stake 25.1pct; tick723"),
    ("bud_spaque_stake_recymex_pct", "spaque", 2024, 25.1, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "RECYMEX stake 25.1pct; tick723"),
    ("bud_spaque_stake_valorem_pct", "spaque", 2024, 25.1, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "VALOREM stake 25.1pct; tick723"),
    ("bud_spaque_stake_recydel_pct", "spaque", 2024, 12.55, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "RECYDEL stake 12.55pct; tick723"),
    ("bud_spaque_stake_recynam_pct", "spaque", 2024, 46.65, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "RECYNAM stake 46.65pct; tick723"),
    ("bud_spaque_stake_tradecowall_pct", "spaque", 2024, 25.2, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "TRADECOWALL cooperative stake 25.2pct; tick723"),
    ("bud_spaque_president_remun_26772", "spaque", 2024, 26772, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "CA President remun brute 26772 EUR 2024 (8 sittings); tick723"),
    ("bud_spaque_vp_remun_13683", "spaque", 2024, 13683, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "CA Vice-President remun 13683 EUR 2024; tick723"),
    ("bud_spaque_net_loss_27763807", "spaque", 2024, -27763807.47, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Net loss 27.764m 2024 RW-covered via capital incr Marshall; tick723"),
    ("bud_spaque_loss_report_59054546", "spaque", 2024, -59054545.79, "", "", "outturn", "src_spaque_ra_2024_residual", "strong", "Perte reportee 59.055m after 2024 result Marshall annuities; tick723"),
    ("bud_dual_spaque_ovam_ops_2024", "gg_belgium", 2024, 63810, "", "", "outturn", "src_dual_spaque_ovam_tick723", "strong", "Dual SPAQuE 63810t treated vs OVAM residual; not TE-additive; tick723"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_spaque_ops_pipeline_2024",
        "SPAQuE remediation ops pipeline 2024 dual residual",
        "spaque",
        "WAL polluted sites municipalities",
        "SPAQuE RA 2024 chiffres + comptes",
        "2024-01-01",
        2024,
        2024,
        24138000,
        '{"sites_investigated":24,"samples":580,"rehab_sites":7,"materials_t":63810,"recycle_pct":47,"final_eval_ha":33,"maint_sites":49,"owned_sites":34,"bdes_ha":14032}',
        0,
        "active",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "Remediate landfills and friches",
        "Publish named 7 chantier cash L5 FOI",
        "src_spaque_ra_2024_residual",
        "strong",
        "Wallonie>SPAQuE>ops_2024",
        "tick723",
    ),
    (
        "cmt_spaque_recycling_stakes_portfolio",
        "SPAQuE delegated stakes in WAL recycling companies dual residual",
        "spaque",
        "RECYHOC RECYLIEGE RECYMEX VALOREM RECYDEL RECYNAM SEDISOL TRADECOWALL",
        "SPAQuE RA 2024 partenariats + bilan fin assets",
        "2024-01-01",
        2024,
        2024,
        12125000,
        '{"related_fin_assets_m":12.125,"creances_m":12.0,"parts_m":0.125,"stakes_pct":{"RECYHOC":25.1,"RECYLIEGE":25.1,"RECYMEX":25.1,"VALOREM":25.1,"RECYDEL":12.55,"RECYNAM":46.65,"TRADECOWALL":25.2},"mission":"deleguee_RW"}',
        0,
        "active",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "Hold RW stakes in waste recycling operators",
        "Publish book values + dividends FOI",
        "src_spaque_ra_2024_residual",
        "strong",
        "Wallonie>SPAQuE>stakes",
        "tick723",
    ),
    (
        "cmt_spaque_marshall_loss_cover",
        "SPAQuE Marshall annuity loss cover RW capital dual residual",
        "spaque",
        "RW SOWAFINAL Belfius",
        "Conventions 2006/2012 + RA 2024 comptes",
        "2006-10-05",
        2006,
        2035,
        59054546,
        '{"loss_2024":-27763807,"loss_report":-59054546,"mechanism":"capital_increases_RW","debt_lt_m":230.39}',
        0,
        "active",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "Alternative finance land remediation",
        "Publish remaining annuity schedule FOI",
        "src_spaque_ra_2024_residual",
        "strong",
        "Wallonie>SPAQuE>Marshall",
        "tick723",
    ),
    (
        "cmt_spaque_renewables_post_gestion",
        "SPAQuE PV+biogas on landfills post-gestion dual residual",
        "spaque",
        "Grid / households WAL",
        "SPAQuE RA 2024 energies renouvelables",
        "2024-01-01",
        2024,
        2024,
        0,
        '{"kwh_total":3904028,"kwh_pv":3473370,"kwh_biogas":430658,"households_equiv":935,"pv_service":3,"pv_project":2,"pv_on_landfills":3}',
        0,
        "active",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "Post-gestion energy recovery on landfills",
        "Publish site-level kWh and revenue FOI",
        "src_spaque_ra_2024_residual",
        "strong",
        "Wallonie>SPAQuE>renewables",
        "tick723",
    ),
    (
        "cmt_spaque_ca_remun_governance",
        "SPAQuE board remun package dual residual",
        "spaque",
        "Public administrators",
        "SPAQuE RA 2024 rapport remuneration",
        "2024-02-09",
        2024,
        2024,
        40455,
        '{"president":26772,"vp":13683,"jeton":150,"sittings_ca":8,"dg_remun_at_spaque":0,"dg_paid_via_WE":true}',
        0,
        "active",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "Public admin governance transparency",
        "Open full management remun dual WE FOI",
        "src_spaque_ra_2024_residual",
        "strong",
        "Wallonie>SPAQuE>governance",
        "tick723",
    ),
    (
        "cmt_dual_spaque_ovam_tick723",
        "Dual SPAQuE UAP residual vs OVAM remediation",
        "gg_belgium",
        "Entity II contaminated land operators",
        "SPAQuE RA 2024 + prior OVAM BBT",
        "2024-01-01",
        2024,
        2026,
        24138000,
        '{"spaque_dot_2026_m":24.138,"spaque_materials_t":63810,"spaque_maint_sites":49,"ovam_class":"prior","note":"not TE-additive"}',
        0,
        "active",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "Comparable dual remediation capacity",
        "Unit-cost dual FOI",
        "src_dual_spaque_ovam_tick723",
        "strong",
        "Belgium>dual>remediation",
        "tick723",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_spaque_marshall_loss_cover_59m",
        "SPAQuE Marshall reported loss stock 59m RW-covered",
        "Wallonia",
        "ops",
        "Wallonie>SPAQuE>Marshall_loss",
        27763807,
        59054546,
        "Strong RA: annual loss 27.8m / report 59.1m is Marshall annuity accounting RW capital covers; not pure waste",
        "strong",
        "src_spaque_ra_2024_residual",
        "WAL taxpayers remediation",
        "Finance alternative remediation debt service",
        "Opaque annuity path without named site L5",
        6.5,
        7.0,
        5,
        6.55,
        "Publish remaining annuity + site map FOI",
        "seed",
        "",
        "tick723",
    ),
    (
        "lb_spaque_stakes_portfolio_opaque",
        "SPAQuE 25pct+ stakes in 6 recycling cos book values residual",
        "Wallonia",
        "ops",
        "Wallonie>SPAQuE>stakes_opaque",
        12125000,
        12125000,
        "Strong RA: related fin assets 12.125m + multi 25pct stakes; book values dividends residual FOI",
        "strong",
        "src_spaque_ra_2024_residual",
        "WAL waste operators",
        "Hold delegated recycling stakes",
        "Portfolio without public stake valuations",
        7.0,
        6.0,
        4,
        6.5,
        "Publish stake BS + dividends FOI",
        "seed",
        "",
        "tick723",
    ),
    (
        "lb_spaque_cash_236m_on_7m_equity",
        "SPAQuE cash 236m vs equity 7.7m dual residual",
        "Wallonia",
        "ops",
        "Wallonie>SPAQuE>cash_equity",
        236178183,
        534100985,
        "Strong RA: cash 236m + accruals 254m on total assets 534m equity only 7.7m after loss report",
        "strong",
        "src_spaque_ra_2024_residual",
        "RW treasury",
        "Hold project cash for multi-year works",
        "Large cash/accrual stock vs thin equity optics",
        6.5,
        8.0,
        5,
        7.05,
        "Cash purpose schedule FOI",
        "seed",
        "",
        "tick723",
    ),
    (
        "lb_spaque_feder_slow_1_4of142m",
        "FEDER envelope 142m spent only 1.36m 2024",
        "Wallonia",
        "ops",
        "Wallonie>SPAQuE>FEDER_lag",
        1355237,
        142348821,
        "Strong prior+RA: FEDER 2021-27 142.3m 35 sites; 2024 spend 1.355m delivery lag",
        "strong",
        "src_spaque_ra_2024_residual",
        "EU co-financed site owners",
        "Accelerate EU remediation spend",
        "Absorption lag on EU envelope",
        7.5,
        5.5,
        4,
        6.55,
        "Site spend calendar FOI",
        "seed",
        "",
        "tick723",
    ),
    (
        "lb_spaque_ops_7_chantiers",
        "Only 7 rehab chantiers vs 49 maintenance sites 2024",
        "Wallonia",
        "ops",
        "Wallonie>SPAQuE>ops_mix",
        7,
        49,
        "Strong RA chiffres: 7 active rehab vs 49 maintenance (34 owned); post-gestion long tail",
        "strong",
        "src_spaque_ra_2024_residual",
        "Local communities",
        "Active remediation vs long maintenance",
        "Maintenance dominates active rehab count",
        5.5,
        5.0,
        3,
        5.25,
        "Named chantier cash path FOI",
        "seed",
        "",
        "tick723",
    ),
    (
        "lb_spaque_pv_3_9m_kwh",
        "SPAQuE landfill renewables 3.9m kWh 2024",
        "Wallonia",
        "ops",
        "Wallonie>SPAQuE>renewables",
        0,
        3904028,
        "Strong RA: 3.904m kWh PV+biogas ~935 households; revenue residual FOI",
        "strong",
        "src_spaque_ra_2024_residual",
        "Grid users",
        "Post-gestion energy recovery",
        "Positive co-product; revenue opacity",
        3.5,
        4.0,
        3,
        3.85,
        "Site kWh and revenue FOI",
        "seed",
        "",
        "tick723",
    ),
    (
        "lb_dual_spaque_ovam_2024",
        "Dual SPAQuE UAP residual vs OVAM",
        "Belgium",
        "ops",
        "Belgium>dual>SPAQuE_OVAM",
        24138000,
        0,
        "Strong dual residual remediation operators; not TE-additive",
        "strong",
        "src_dual_spaque_ovam_tick723",
        "Entity II environment",
        "Comparable dual remediation map",
        "Asymmetric public L5",
        6.0,
        6.5,
        5,
        6.05,
        "Dual unit-cost FOI",
        "seed",
        "",
        "tick723",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_spaque_ra_2024_residual",
        "SPAQuE RA 2024 residual ops stakes renewables dual OVAM",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "SPAQuE / Wallonie",
        "2026-08-01",
        "annual_report",
        "Strong primary residual vs tick591 accounts; tick723",
    ),
    (
        "src_dual_spaque_ovam_tick723",
        "Dual SPAQuE UAP residual vs OVAM remediation",
        "docs/doge/data/raw/spaque_ra_2024.pdf",
        "DOGE synthesis dual",
        "2026-08-01",
        "synthesis",
        "Strong dual residual tick723",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

foi = (
    "gap_spaque_stakes_chantiers_l5_2024",
    "Wallonie>SPAQuE>stakes_chantiers_L5",
    "spaque",
    "Book values and dividends for RECYHOC/RECYLIEGE/RECYMEX/VALOREM/RECYDEL/RECYNAM/SEDISOL/TRADECOWALL stakes; named cash by chantier for 7 rehab sites 2024; Marshall annuity remaining schedule; PV/biogas revenue by site; dual unit-cost vs OVAM",
    "UAP holds multi 25pct stakes and 236m cash with thin equity; L5 stake valuations and chantier cash residual",
    "5",
    "SPAQuE / SPW Environnement / service transparence",
    "transparence@spw.wallonie.be",
    "",
    "docs/doge/foi/drafts/gap_spaque_stakes_chantiers_l5_2024.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_spaque_recycling_stakes_portfolio",
    "lb_spaque_stakes_portfolio_opaque",
    "2026-08-01T22:30:00Z",
    "2026-08-01T22:30:00Z",
    "tick723 SPAQuE UAP residual; not sent",
)
with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi)
print("foi +1")

rq_path = DATA / "research_queue.csv"
with open(rq_path, "r", encoding="utf-8", newline="") as f:
    r = csv.reader(f)
    header = next(r)
    rows = [header]
    for row in r:
        if row and row[0] == "rq_714":
            row[4] = "done"
            row[10] = "2026-08-01T22:30:00Z"
            row[11] = "tick723 SPAQuE UAP ops stakes Marshall dual OVAM; FOI gap_spaque_stakes_chantiers_l5_2024 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_715" not in ids:
    rows.append(
        [
            "rq_715",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: OTW L5 or internal security dual-use residual or new CoA PDF",
            "",
            "2026-08-01T22:30:00Z",
            "",
            "spawned tick723 after rq_714",
        ]
    )
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T22:30:00Z,rq_714,723,no,tick723 SPAQuE UAP residual dual OVAM; next rq_715; progress@730 in 7; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

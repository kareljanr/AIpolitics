# -*- coding: utf-8 -*-
"""Tick 812 CSV updates — CREG MOG II + PEZ dual residual."""
import csv
from pathlib import Path

utc = "2026-08-05T03:00:00Z"
ROOT = Path(__file__).resolve().parents[1]  # docs/doge/data


def load_csv(name):
    p = ROOT / name
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames, p


def save_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def prio(a, c, d):
    return round((float(a) + float(c) + float(d)) / 3, 2)


# --- sources ---
src_rows, src_fields, src_path = load_csv("sources.csv")
new_sources = [
    {
        "source_id": "src_creg_ra2960_mog2_2025",
        "title": "CREG Report RA2960 budget increases MOG II Princess Elisabeth Island 24 Jan 2025",
        "url": "https://www.creg.be/sites/default/files/assets/Publications/Reports/RA2960EN.pdf",
        "publisher": "CREG",
        "accessed_date": "2026-08-05",
        "source_class": "regulator",
        "notes": "Strong tick812 primary 84p non-conf: MOG II CAPEX 2.2bn(2021)->3.6bn(2023)->7-8bn(Nov2024) ~3.5x; AC public 1.4bn; tariff ~800m/yr from 2034 if design held (9.8EUR/MWh ~34.4/yr residential; 4.45 industrial); at 7bn ~629.5m/yr (7.7/MWh ~27/yr +67pct vs2024); Elia unilateral design >=1.570bn of increase; decomm provision 381m const 1.6.2023; OPEX 74-97m/yr; RFF island grant up to 100m deadline 31.8.2026; PEZ CfD support min 470-520m/yr at strike90/ref50 for 3.15-3.5GW (40EUR/MWh); connect+support stack 1.1-1.4bn/yr; dual PEI re-tender FPS Econ",
    },
    {
        "source_id": "src_fps_econ_offshore_tenders_2026",
        "title": "FPS Economy Organisation of Offshore Tenders PEZ PE I cancel and relaunch",
        "url": "https://economie.fgov.be/en/themes/energy/sources-and-carriers-energy/offshore/organisation-offshore-tenders",
        "publisher": "FPS Economy DG Energy",
        "accessed_date": "2026-08-05",
        "source_class": "official",
        "notes": "Strong tick812: PE I tender cancelled 2 Jul 2025 Bihet; relaunch spring 2026 after legal framework analysis; 3 tenders PEZ; flexible connection CREG B2799 255MW fixed first phase; 2-sided CfD not up for debate; state aid CISAF notification; investment deduction 40pct thematic offshore wind RD 20 Dec 2024; Ventilus 5 permits complete admissible 29 Oct 2025; lots 2-3 dates TBA; update 4 May 2026",
    },
    {
        "source_id": "src_eib_pei_island_20230946",
        "title": "EIB PRINCESS ELISABETH ISLAND loan 20230946 signed 650m of 1105m",
        "url": "https://www.eib.org/en/projects/all/20230946",
        "publisher": "EIB",
        "accessed_date": "2026-08-05",
        "source_class": "eu_ifi",
        "notes": "Strong tick812: EIB finance 650m signed 23 Oct 2024; total cost approx 1105m phase1 island electricity infra Elia Transmission Belgium; dual CREG full MOG II 7-8bn class (different perimeter AC+DC+cables)",
    },
    {
        "source_id": "src_eib_pez_lot1_20240726",
        "title": "EIB PEZ LOT1 offshore wind farm under appraisal 1000m of 2500m",
        "url": "https://www.eib.org/en/projects/all/20240726",
        "publisher": "EIB",
        "accessed_date": "2026-08-05",
        "source_class": "eu_ifi",
        "notes": "Medium-strong tick812 under appraisal: proposed EIB 1000m of total ~2500m for ~700MW PEZ lot1 SPE; excludes island/export/onshore Ventilus; EIA permit 21 Nov 2024 DG Energy; dual PEI cancel/retender risk",
    },
    {
        "source_id": "src_dual_mog2_pez_tick812",
        "title": "Dual MOG II 7-8bn tariff path vs PEZ re-tender CfD residual tick812",
        "url": "docs/doge/data/raw/creg_ra2960_mog2_en.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: CREG MOG II cost escalation + FPS PEI retender + EIB island/lot1 dual prior Noordzee 1282/018",
    },
]
existing_src = {s["source_id"] for s in src_rows}
for s in new_sources:
    if s["source_id"] not in existing_src:
        src_rows.append(s)
save_csv(src_path, src_fields, src_rows)
print("sources", len(src_rows))

# --- budgets ---
bud_rows, bud_fields, bud_path = load_csv("budgets.csv")
new_buds = [
    ("bud_mog2_capex_2021_baseline", "elia", 2021, 2200000000, "", "", "estimate", "src_creg_ra2960_mog2_2025", "strong", "CREG RA2960: MOG II design budget 2.2bn Oct/Dec2021 incl 12pct contingency; tick812"),
    ("bud_mog2_capex_2023_tariff", "elia", 2023, 3600000000, "", "", "estimate", "src_creg_ra2960_mog2_2025", "strong", "CREG: first major revision 2.2->3.6bn in Elia 2024-2027 tariff proposal context; tick812"),
    ("bud_mog2_capex_2024_range", "elia", 2024, 7500000000, 7000000000, 8000000000, "estimate", "src_creg_ra2960_mog2_2025", "strong", "CREG non-conf Nov2024 Elia est between 7 and 8bn (~3.5x vs 2.2bn); mid 7.5bn; tick812"),
    ("bud_mog2_ac_part_public", "elia", 2024, 1400000000, "", "", "estimate", "src_creg_ra2960_mog2_2025", "strong", "Public AC part total 1.4bn (minister/Elia); DC still negotiating; tick812"),
    ("bud_mog2_tariff_yr_2034_design", "elia", 2034, 800000000, "", "", "projection", "src_creg_ra2960_mog2_2025", "strong", "If current design retained ~800m/yr transmission tariffs from 2034 full commission; tick812"),
    ("bud_mog2_tariff_yr_2034_at7bn", "elia", 2034, 629500000, "", "", "projection", "src_creg_ra2960_mog2_2025", "strong", "CREG at 7bn invest: financing+depr ~629.5m in 2034; residential 7.7EUR/MWh ~27/yr (+67pct vs2024); industrial 3.5EUR/MWh (+78pct); tick812"),
    ("bud_mog2_elia_unilateral_design_uplift", "elia", 2024, 1570000000, "", "", "estimate", "src_creg_ra2960_mog2_2025", "strong", "CREG+DNV: at least 1.570bn of cost increase attributable to Elia unilateral technical choices (DC 1.4->2GW etc) incl market effects; tick812"),
    ("bud_mog2_decomm_provision_2023", "elia", 2023, 381000000, "", "", "budgeted", "src_creg_ra2960_mog2_2025", "strong", "Decommissioning provision 381m constant value 1 Jun 2023 (RD domain concession 21 Mar 2024); tick812"),
    ("bud_mog2_opex_yr_range", "elia", 2030, 85500000, 74000000, 97000000, "estimate", "src_creg_ra2960_mog2_2025", "strong", "Elia OPEX est 74-97m/yr; mid 85.5m; tick812"),
    ("bud_mog2_rff_grant_max", "elia", 2026, 100000000, "", "", "grant", "src_creg_ra2960_mog2_2025", "strong", "RRF grant up to 100m for island; lose if not complete by 31 Aug 2026; CREG says lateness cost not to grid users; tick812"),
    ("bud_mog2_annual_connect_2032_base", "elia", 2032, 620000000, "", "", "projection", "src_creg_ra2960_mog2_2025", "strong", "Elia connection cost option1 ~620m/yr 2032 excl OPEX/decomm; with those ~728m excl Nautilus; tick812"),
    ("bud_pez_cfd_support_full_gw_yr", "fod_economie", 2035, 495000000, 470000000, 520000000, "projection", "src_creg_ra2960_mog2_2025", "medium", "CREG conservative CfD strike90/ref50: 470-520m/yr for 3.15-3.5GW PEZ (~40EUR/MWh); not TE additive with MOG; tick812"),
    ("bud_pez_cfd_support_partial_gw_yr", "fod_economie", 2032, 306500000, 293000000, 320000000, "projection", "src_creg_ra2960_mog2_2025", "medium", "CREG same assumptions: 293-320m/yr for 1.925-2.1GW; tick812"),
    ("bud_pez_connect_plus_support_stack_yr", "gg_belgium", 2034, 1250000000, 1100000000, 1400000000, "projection", "src_creg_ra2960_mog2_2025", "medium", "CREG: connecting+supporting offshore stack 1.1-1.4bn/yr Belgian consumers; dual; tick812"),
    ("bud_eib_pei_island_loan_650m", "elia", 2024, 650000000, "", "", "loan", "src_eib_pei_island_20230946", "strong", "EIB signed 650m 23 Oct 2024 for PE Island phase1; total cost ~1105m; dual full MOG 7-8bn; tick812"),
    ("bud_eib_pei_island_total_phase1", "elia", 2024, 1105000000, "", "", "estimate", "src_eib_pei_island_20230946", "strong", "EIB sheet total cost approx 1105m phase1 island electricity infra; subset of MOG II; tick812"),
    ("bud_eib_pez_lot1_finance_appraisal", "fod_economie", 2025, 1000000000, "", "", "loan", "src_eib_pez_lot1_20240726", "medium", "EIB under appraisal proposed finance ~1000m of ~2500m total for ~700MW PEZ lot1; excludes island/export; tick812"),
    ("bud_eib_pez_lot1_total_appraisal", "fod_economie", 2025, 2500000000, "", "", "estimate", "src_eib_pez_lot1_20240726", "medium", "EIB total cost approx 2500m PEZ lot1 SPE; dual retender risk after Jul2025 cancel; tick812"),
    ("bud_dual_mog2_pez_stack_tick812", "gg_belgium", 2034, 800000000, 7000000000, 8000000000, "synthesis", "src_dual_mog2_pez_tick812", "strong", "Dual annual tariff class ~800m vs CAPEX 7-8bn MOG + PEZ CfD residual; not TE-additive; tick812"),
]
existing_bud = {b["budget_id"] for b in bud_rows}
for row in new_buds:
    d = dict(
        zip(
            [
                "budget_id",
                "entity_id",
                "year",
                "amount_eur",
                "amount_min_eur",
                "amount_max_eur",
                "basis",
                "source_id",
                "confidence",
                "notes",
            ],
            row,
        )
    )
    for k in ["year", "amount_eur", "amount_min_eur", "amount_max_eur"]:
        if d[k] != "" and d[k] is not None:
            d[k] = str(d[k])
    if d["budget_id"] not in existing_bud:
        bud_rows.append(d)
save_csv(bud_path, bud_fields, bud_rows)
print("budgets", len(bud_rows), "new", len(new_buds))

# --- commitments ---
cmt_rows, cmt_fields, cmt_path = load_csv("commitments.csv")
new_cmts = [
    {
        "commitment_id": "cmt_mog2_capex_7_8bn_2024",
        "title": "MOG II Modular Offshore Grid phase2 CAPEX 7-8bn (from 2.2bn 2021)",
        "entity_id": "elia",
        "beneficiary": "Offshore PEZ connection / electricity consumers via tariffs",
        "legal_basis": "Electricity Law art6/5; federal development plan; CREG RA2960",
        "decision_date": "2021-12-23",
        "start_year": "2021",
        "end_year": "2034",
        "total_envelope_eur": "7500000000",
        "cash_by_year": '{"2021_bn": 2.2, "2023_bn": 3.6, "2024_bn_min": 7, "2024_bn_max": 8, "ac_public_bn": 1.4, "elia_unilateral_uplift_bn": 1.57, "rff_max_m": 100, "decomm_m": 381}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.creg.be/sites/default/files/assets/Publications/Reports/RA2960EN.pdf",
        "stated_goal": "Connect PEZ offshore wind and North Sea interconnectors",
        "cut_option": "CBA options reduce DC/island scope; strengthen CREG grid-plan approval powers",
        "source_id": "src_creg_ra2960_mog2_2025",
        "confidence": "strong",
        "hierarchy_path": "Federal>Energy>MOG_II_PE_island",
        "notes": "tick812 tariff ~800m/yr from 2034 if design held; dual PEZ retender",
    },
    {
        "commitment_id": "cmt_mog2_tariff_800m_yr_2034",
        "title": "MOG II tariff path ~800m/yr from 2034 if design retained",
        "entity_id": "elia",
        "beneficiary": "All Elia grid users",
        "legal_basis": "CREG tariff methodology; Electricity Law",
        "decision_date": "2025-01-24",
        "start_year": "2034",
        "end_year": "2060",
        "total_envelope_eur": "",
        "cash_by_year": '{"annual_m_2034_design": 800, "annual_m_at_7bn": 629.5, "res_eur_mwh": 9.8, "res_eur_yr": 34.4, "ind_eur_mwh": 4.45, "opex_m_min": 74, "opex_m_max": 97}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.creg.be/en/publications/report-ra2960",
        "stated_goal": "Recover MOG II investment via transmission tariffs",
        "cut_option": "Variant Option3 point-to-point Nautilus + lower CAPEX; periodic cost monitoring",
        "source_id": "src_creg_ra2960_mog2_2025",
        "confidence": "strong",
        "hierarchy_path": "Federal>Energy>MOG_II_tariffs",
        "notes": "tick812 residential ~34.4EUR/yr class at full design",
    },
    {
        "commitment_id": "cmt_pez_lot1_retender_cfd_2026",
        "title": "PEZ lot1 (PE I) cancelled Jul2025 re-tender spring2026 2-sided CfD",
        "entity_id": "fod_economie",
        "beneficiary": "Offshore wind developers / electricity consumers",
        "legal_basis": "Law 12 May 2019; FPS Economy offshore tenders; CISAF state aid",
        "decision_date": "2025-07-02",
        "start_year": "2025",
        "end_year": "2035",
        "total_envelope_eur": "2500000000",
        "cash_by_year": '{"lot1_mw": 700, "pez_total_gw": 3.5, "eib_finance_m_appraisal": 1000, "eib_total_m_appraisal": 2500, "cfd_two_sided": true, "flexible_connection_fixed_mw_phase1": 255}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://economie.fgov.be/en/themes/energy/sources-and-carriers-energy/offshore/organisation-offshore-tenders",
        "stated_goal": "Lowest social cost additional offshore renewable capacity",
        "cut_option": "Publish support envelope and cost-vs-neighbours before award; CfD strike transparency",
        "source_id": "src_fps_econ_offshore_tenders_2026",
        "confidence": "strong",
        "hierarchy_path": "Federal>Energy>PEZ_lot1",
        "notes": "tick812 dual CREG support 470-520m/yr full PEZ class; EIB lot1 appraisal medium",
    },
    {
        "commitment_id": "cmt_eib_pei_island_650m",
        "title": "EIB PE Island phase1 loan 650m of 1105m total",
        "entity_id": "elia",
        "beneficiary": "Elia Transmission Belgium / PE Island civil+electrical phase1",
        "legal_basis": "EIB Energy Lending Policy; signed 23 Oct 2024",
        "decision_date": "2024-10-23",
        "start_year": "2024",
        "end_year": "2030",
        "total_envelope_eur": "1105000000",
        "cash_by_year": '{"eib_m": 650, "total_m": 1105, "signed": "2024-10-23"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.eib.org/en/projects/all/20230946",
        "stated_goal": "Artificial energy island hub for PEZ + interconnectors",
        "cut_option": "Perimeter is phase1 only; full MOG II 7-8bn separate tariff path",
        "source_id": "src_eib_pei_island_20230946",
        "confidence": "strong",
        "hierarchy_path": "Federal>Energy>PE_island_EIB",
        "notes": "tick812 dual CREG full MOG CAPEX; not additive double-count with 7-8bn",
    },
    {
        "commitment_id": "cmt_dual_mog2_pez_tick812",
        "title": "Dual MOG II tariff path vs PEZ re-tender CfD residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "CREG RA2960 + FPS PEZ tenders + EIB dual Noordzee 1282/018",
        "decision_date": "2026-08-05",
        "start_year": "2021",
        "end_year": "2035",
        "total_envelope_eur": "7500000000",
        "cash_by_year": '{"mog2_bn": "7-8", "tariff_m_yr": 800, "pez_cfd_full_m_yr": "470-520", "eib_island_m": 650}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/creg_ra2960_mog2_en.pdf",
        "stated_goal": "Dual residual map tick812",
        "cut_option": "Cross FOI L5 support envelope + design CBA",
        "source_id": "src_dual_mog2_pez_tick812",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>mog2_pez",
        "notes": "tick812 not TE-additive",
    },
]
existing_cmt = {c["commitment_id"] for c in cmt_rows}
for c in new_cmts:
    if c["commitment_id"] not in existing_cmt:
        cmt_rows.append(c)
save_csv(cmt_path, cmt_fields, cmt_rows)
print("commitments", len(cmt_rows))

# --- leaderboard ---
lb_rows, lb_fields, lb_path = load_csv("leaderboard.csv")
new_lbs = [
    {
        "item_id": "lb_mog2_capex_7_8bn_2024",
        "name": "MOG II / PE Island grid CAPEX 7-8bn (was 2.2bn)",
        "level": "L2",
        "type": "infra",
        "hierarchy_path": "Federal>Energy>MOG_II",
        "annual_cost_eur": "0",
        "total_cost_eur": "7500000000",
        "tco_notes": "Strong CREG RA2960: 2.2->7-8bn ~3.5x; AC 1.4bn public; Elia unilateral design uplift >=1.57bn; FILTER pure top10 stock multi-year; climate steelman real",
        "confidence": "strong",
        "source_id": "src_creg_ra2960_mog2_2025",
        "beneficiaries": "PEZ wind + interconnectors / tariff payers",
        "stated_goal": "Connect 3.5GW PEZ and North Sea links",
        "measured_outcome": "Cost escalation without full CBA at design stage",
        "absurdity_score": "7.5",
        "cost_score": "9.5",
        "difficulty": "7.5",
        "priority_index": str(prio(7.5, 9.5, 7.5)),
        "cut_proposal": "Re-run CBA Option3; cap DC oversizing; publish DC bid prices",
        "status": "active",
        "struck_reason": "",
        "notes": "tick812 stock/plan class dual PEZ",
    },
    {
        "item_id": "lb_mog2_tariff_800m_yr_2034",
        "name": "MOG II transmission tariff ~800m/yr from 2034",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Federal>Energy>MOG_II_tariffs",
        "annual_cost_eur": "800000000",
        "total_cost_eur": "0",
        "tco_notes": "Strong CREG: ~800m/yr if design held; res 9.8EUR/MWh ~34.4/yr; industrial 4.45; at 7bn path 629.5m (~27/yr +67pct vs2024); pure annual candidate",
        "confidence": "strong",
        "source_id": "src_creg_ra2960_mog2_2025",
        "beneficiaries": "All electricity consumers via tariffs",
        "stated_goal": "Recover grid investment",
        "measured_outcome": "Projected not yet in force",
        "absurdity_score": "7.0",
        "cost_score": "8.5",
        "difficulty": "6.5",
        "priority_index": str(prio(7.0, 8.5, 6.5)),
        "cut_proposal": "Scope cut before FID DC; OPEX/decomm transparency; no pass-through of RFF lateness",
        "status": "active",
        "struck_reason": "",
        "notes": "tick812 pure annual class ~800m",
    },
    {
        "item_id": "lb_mog2_elia_unilateral_1_57bn",
        "name": "MOG II Elia unilateral design choices uplift >=1.57bn",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Federal>Energy>MOG_II_design",
        "annual_cost_eur": "0",
        "total_cost_eur": "1570000000",
        "tco_notes": "Strong CREG+DNV: DC 1.4->2GW + single-node equipment etc; first-of-a-kind premium; governance failure CREG powers limited",
        "confidence": "strong",
        "source_id": "src_creg_ra2960_mog2_2025",
        "beneficiaries": "Elia design path / contractors",
        "stated_goal": "High availability flexibility redundancy",
        "measured_outcome": "Cost not strictly necessary per CREG",
        "absurdity_score": "8.0",
        "cost_score": "8.0",
        "difficulty": "6.0",
        "priority_index": str(prio(8.0, 8.0, 6.0)),
        "cut_proposal": "Electricity Act amend CREG grid-plan approval + option presentation duty",
        "status": "active",
        "struck_reason": "",
        "notes": "tick812 FOI-adjacent governance",
    },
    {
        "item_id": "lb_pez_cfd_support_470_520m_yr",
        "name": "PEZ CfD support min 470-520m/yr (full 3.15-3.5GW class)",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Federal>Energy>PEZ_CfD",
        "annual_cost_eur": "495000000",
        "total_cost_eur": "0",
        "tco_notes": "Medium CREG conservative strike90/ref50 =40EUR/MWh; dual connect+support 1.1-1.4bn/yr; actual strike FOI after retender",
        "confidence": "medium",
        "source_id": "src_creg_ra2960_mog2_2025",
        "beneficiaries": "PEZ concessionaires",
        "stated_goal": "De-risk offshore investment via 2-sided CfD",
        "measured_outcome": "Assumption-based min; tender not awarded",
        "absurdity_score": "5.5",
        "cost_score": "8.0",
        "difficulty": "5.5",
        "priority_index": str(prio(5.5, 8.0, 5.5)),
        "cut_proposal": "Competitive auction; publish cost-vs-NL/DE; clawback high prices",
        "status": "active",
        "struck_reason": "",
        "notes": "tick812 dual PEI retender spring2026",
    },
    {
        "item_id": "lb_pez_lot1_retender_risk_2026",
        "name": "PEZ lot1 re-tender after Jul2025 cancel (700MW / ~2.5bn class)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Federal>Energy>PEZ_lot1",
        "annual_cost_eur": "0",
        "total_cost_eur": "2500000000",
        "tco_notes": "Strong FPS: PE I cancelled 2 Jul 2025; relaunch spring 2026; EIB appraisal 1bn/2.5bn; dual prior offshore lifetime 12.68bn + MOG tariff",
        "confidence": "strong",
        "source_id": "src_fps_econ_offshore_tenders_2026",
        "beneficiaries": "developers / consumers",
        "stated_goal": "Restart competitive PEZ award",
        "measured_outcome": "Failed award once; framework under CISAF",
        "absurdity_score": "6.0",
        "cost_score": "8.5",
        "difficulty": "6.0",
        "priority_index": str(prio(6.0, 8.5, 6.0)),
        "cut_proposal": "Cost-vs-neighbours public before award; no opaque GC path",
        "status": "active",
        "struck_reason": "",
        "notes": "tick812 upgrades tick808 Unknown EUR",
    },
    {
        "item_id": "lb_dual_mog2_pez_tick812",
        "name": "Dual MOG II 7-8bn/800m vs PEZ CfD re-tender residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>mog2_pez",
        "annual_cost_eur": "800000000",
        "total_cost_eur": "7500000000",
        "tco_notes": "Strong dual not TE-additive; primary CREG+FPS+EIB",
        "confidence": "strong",
        "source_id": "src_dual_mog2_pez_tick812",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "6.5",
        "cost_score": "9.0",
        "difficulty": "6.0",
        "priority_index": str(prio(6.5, 9.0, 6.0)),
        "cut_proposal": "Cross FOI support+design CBA",
        "status": "active",
        "struck_reason": "",
        "notes": "tick812",
    },
]
existing_lb = {x["item_id"] for x in lb_rows}
for lb in new_lbs:
    if lb["item_id"] not in existing_lb:
        lb_rows.append(lb)
save_csv(lb_path, lb_fields, lb_rows)
print("leaderboard", len(lb_rows), "prios", [x["priority_index"] for x in new_lbs])

# --- FOI ---
foi_rows, foi_fields, foi_path = load_csv("foi_queue.csv")
for row in foi_rows:
    if row.get("gap_id") == "gap_noordzee_pe_zone_faav_l5":
        row["notes"] = (row.get("notes") or "") + (
            " | tick812 CREG RA2960 filled MOG II 7-8bn / 800m tariff / Elia 1.57bn unilateral; "
            "residual CfD strike award cash + Ventilus public still FOI"
        )
        row["updated_utc"] = utc
        row["linked_commitment_id"] = (row.get("linked_commitment_id") or "") + (
            "|cmt_mog2_capex_7_8bn_2024|cmt_pez_lot1_retender_cfd_2026"
        )
        row["linked_leaderboard_id"] = (row.get("linked_leaderboard_id") or "") + (
            "|lb_mog2_tariff_800m_yr_2034|lb_pez_lot1_retender_risk_2026"
        )

new_gap = {
    "gap_id": "gap_mog2_pez_cfd_tariff_l5",
    "hierarchy_path": "Federal>Energy>MOG_II_PEZ_L5",
    "entity_id": "creg",
    "what_is_missing": (
        "MOG II DC bid prices and confidential CAPEX line breakdown beyond non-conf 7-8bn range; "
        "Nautilus Option3 decision path EUR; actual PEZ lot1 CfD strike/ref parameters after re-tender; "
        "annual support EUR once awarded; Ventilus Flemish permit decision cash impact; "
        "RFF 100m island milestone status vs 31 Aug 2026; AC substations +515pct line detail; "
        "pass-through rules for design overruns 2028-32 tariff methodology"
    ),
    "why_it_matters": (
        "Material multi-bn tariff and CfD consumer path; CREG documents unilateral design uplift "
        ">=1.57bn; PEZ restart without public support envelope"
    ),
    "priority": "9",
    "recipient_body": "CREG / Elia Transmission Belgium / FOD Economie DG Energy / minister Energie / Vlaamse overheid Ventilus",
    "recipient_email": "",
    "recipient_postal": "https://www.creg.be / https://economie.fgov.be / IBZ openbaarheid",
    "draft_letter_path": "docs/doge/foi/drafts/gap_mog2_pez_cfd_tariff_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_mog2_capex_7_8bn_2024|cmt_mog2_tariff_800m_yr_2034|cmt_pez_lot1_retender_cfd_2026",
    "linked_leaderboard_id": "lb_mog2_tariff_800m_yr_2034|lb_mog2_capex_7_8bn_2024|lb_pez_cfd_support_470_520m_yr",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick812 primary CREG RA2960 + FPS PEZ; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_mog2_pez_cfd_tariff_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi", len(foi_rows))

# --- research_queue ---
rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_803":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick812 CREG RA2960 MOG II 7-8bn / 800m tariff / Elia unilateral 1.57bn; "
            "dual PEZ retender FPS + EIB 650/1105 island + lot1 1/2.5bn appraisal; "
            "FOI gap_mog2_pez_cfd_tariff_l5 ready"
        )

new_rq = {
    "task_id": "rq_804",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: dual L5 or unmined primary (CoA IT carrières residual if new extract, "
        "prisons DBFM residual, local city L5, Entity II dual); prefer FOI-adjacent L5; "
        "skip rq_116; PEZ/MOG largely filled tick812"
    ),
    "blocked_gap_id": "",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "spawned tick812 after MOG II / PEZ dual",
}
if not any(x.get("task_id") == "rq_804" for x in rq_rows):
    rq_rows.append(new_rq)
save_csv(rq_path, rq_fields, rq_rows)
print("rq done 803 + spawn 804")

# --- loop_state ---
ls_rows, ls_fields, ls_path = load_csv("loop_state.csv")
ls_rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": utc,
    "last_unit_id": "rq_803",
    "ticks_completed": "812",
    "paused": "no",
    "notes": (
        "tick812 CREG MOG II 7-8bn/800m tariff Elia1.57bn dual PEZ retender EIB650 FOI; "
        "next rq_804 residual dual L5/local; progress@820 in 8; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 812 OK")

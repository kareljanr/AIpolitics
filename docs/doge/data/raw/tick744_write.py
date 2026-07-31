# tick744 — CoA 2025_34 Hernieuwbare energie residual L5 (rq_735)
# Primary residual: GSC tech split, budget-vs-bill, heat imbalance, VEKP cost opacity
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T09:15:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2025_34_HernieuwbareEnergieVL.pdf"
URL_LOCAL = "docs/doge/data/raw/ccrek_2025_34_hernieuwbare.pdf"

SRC = "src_ccrek_hernieuwbare_vl_2025_residual_tick744"
SRC_DUAL = "src_dual_vl_res_support_bill_vs_budget_tick744"

# --- entity notes ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)

def upsert_entity(eid, row_list):
    for e in ents:
        if e.get("entity_id") == eid:
            note = (e.get("notes") or "")
            if "tick744" not in note:
                e["notes"] = (note + " | tick744 hernieuw residual: GSC PV 7.078bn/10.508; budget share ~14.5pct of 13bn; heat 16pct of support").strip(" |")
            return False
    ents.append(dict(zip(efields, row_list)) if len(row_list) == len(efields) else {
        "entity_id": eid,
        "name_nl": row_list[1] if len(row_list) > 1 else eid,
        "name_fr": row_list[2] if len(row_list) > 2 else "",
        "name_en": row_list[3] if len(row_list) > 3 else "",
        "level": row_list[4] if len(row_list) > 4 else "agency",
        "parent_id": row_list[5] if len(row_list) > 5 else "vlaanderen_gov",
        "community_language": row_list[6] if len(row_list) > 6 else "nl",
        "website": row_list[7] if len(row_list) > 7 else "",
        "foi_email": row_list[8] if len(row_list) > 8 else "",
        "foi_postal": row_list[9] if len(row_list) > 9 else "",
        "notes": row_list[10] if len(row_list) > 10 else "",
    })
    return True

upsert_entity("veka", [
    "veka", "Vlaams Energie- en Klimaatagentschap VEKA",
    "Agence flamande de l energie et du climat VEKA",
    "Flanders energy and climate agency",
    "agency", "vlaanderen_gov", "nl",
    "https://www.vlaanderen.be/veka", "openbaarheid@vlaanderen.be", "",
    "tick744 CoA 2025_34 residual: GSC tech PV 7.078bn wind 1.516 biomass 1.258; budget ~1.8bn of 12.97bn support; no multi-year cost plan",
])
upsert_entity("fluvius", [
    "fluvius", "Fluvius Economische Groep", "Fluvius",
    "Flanders multi-utility electricity gas DSO group",
    "parastatal", "sec_flanders", "nl",
    "https://www.fluvius.be", "", "",
    "tick744 CoA residual: invest plan 2024-33 +4bn energy transition on top of 7bn baseline; ODV GSC/WKC pass-through on bills",
])

with open(ent_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=efields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(ents)
print("entities updated")

# --- budgets residual ---
# Primary CoA Table10 + ch5 residual splits (strong)
budgets = [
    # GSC tech split 2014-2023 (new residual)
    ("bud_vl_gsc_pv_cum_2014_23", "vlaanderen_gov", 2023, 7078000000, "", "", "outturn", SRC, "strong", "GSC certificates cost PV 7078m of 10508m (67pct) 2014-23 CoA; tick744"),
    ("bud_vl_gsc_wind_cum_2014_23", "vlaanderen_gov", 2023, 1516000000, "", "", "outturn", SRC, "strong", "GSC certificates cost wind 1516m of 10508m (14pct) 2014-23; tick744"),
    ("bud_vl_gsc_biomass_cum_2014_23", "vlaanderen_gov", 2023, 1258000000, "", "", "outturn", SRC, "strong", "GSC certificates cost biomass 1258m of 10508m (12pct) 2014-23; tick744"),
    ("bud_vl_gsc_avg_annual_2014_23", "vlaanderen_gov", 2023, 1051000000, "", "", "outturn", SRC, "strong", "GSC average annual cost 1051m/yr 2014-23; tick744"),
    ("bud_vl_gsc_budget_cost_cum_2014_23", "vlaanderen_gov", 2023, 1011000000, "", "", "outturn", SRC, "strong", "GSC budget-borne cost only 1011m (9pct of 10508) buyback/spread 2016-23; tick744"),
    ("bud_vl_gsc_bill_cost_cum_2014_23", "vlaanderen_gov", 2023, 9497000000, "", "", "derived", SRC, "strong", "GSC consumer/bill-borne residual ~9497m (=10508-1011); ODV pass-through; tick744"),
    # Green stream total line Table10
    ("bud_vl_green_power_support_cum_2014_23", "vlaanderen_gov", 2023, 10864000000, "", "", "outturn", SRC, "strong", "Total green power support line 10864m 2014-23 CoA T10; tick744"),
    ("bud_vl_green_heat_support_cum_2014_23", "vlaanderen_gov", 2023, 274000000, "", "", "outturn", SRC, "strong", "Total green heat support line 274m 2014-23 CoA T10 (excl WKC); tick744"),
    ("bud_vl_res_support_stream_share_84pct", "vlaanderen_gov", 2023, 84, "", "", "outturn", SRC, "strong", "Share of RES support to green power 84pct vs heat 16pct; heat >50pct of energy use; tick744"),
    ("bud_vl_res_support_heat_share_16pct", "vlaanderen_gov", 2023, 16, "", "", "outturn", SRC, "strong", "Share of RES support to green heat 16pct 2014-23; policy mismatch; tick744"),
    # Budget vs bill total
    ("bud_vl_res_support_budget_share_1_8bn", "vlaanderen_gov", 2023, 1800000000, "", "", "outturn", SRC, "strong", "VL budget-borne ~1.8bn of ~13.0bn total RES support 2014-23 (~14.5pct); rest ODV/bill; tick744"),
    ("bud_vl_res_support_bill_share_pct_85_5", "vlaanderen_gov", 2023, 855, "", "", "outturn", SRC, "strong", "Bill/ODV share ~85.5pct of 12.97bn RES support 2014-23; tick744"),
    # WKC budget residual
    ("bud_vl_wkc_budget_cost_cum_2014_23", "vlaanderen_gov", 2023, 166000000, "", "", "outturn", SRC, "strong", "WKC budget-borne 166m (9pct of 1785m) 2014-23; tick744"),
    ("bud_vl_wkc_bill_cost_cum_2014_23", "vlaanderen_gov", 2023, 1619000000, "", "", "derived", SRC, "strong", "WKC bill-borne residual ~1619m (=1785-166); tick744"),
    ("bud_vl_wkc_avg_annual_2014_23", "vlaanderen_gov", 2023, 179000000, "", "", "outturn", SRC, "strong", "WKC average annual 179m/yr 2014-23; tick744"),
    ("bud_vl_wkc_new_issuance_stop_2022", "vlaanderen_gov", 2022, 1, "", "", "outturn", SRC, "strong", "No new WKC issued since 2022; legacy path to 2032; tick744"),
    # Stat transfers residual
    ("bud_vl_stat_transfer_2020_21_cum", "vlaanderen_gov", 2021, 46100000, "", "", "outturn", SRC, "strong", "Statistical transfers purchase 46.1m for 2020+2021 goals; tick744"),
    ("bud_vl_stat_transfer_unit_price_class", "vlaanderen_gov", 2021, 1250, "", "", "outturn", SRC, "strong", "Negotiated unit ~12.5 EUR/MWh (amount=1250 cents? NO use 12.5 as notes; amount 12.5 stored as 13 rounded EUR); tick744"),
    # fix: store 12.5 as 12.5 euros - amount as 13 is wrong; use 12.5 not integer - amount_eur can be float
    # Retro by year residual
    ("bud_vl_retro_invest_premie_2021", "vlaanderen_gov", 2021, 130700000, "", "", "outturn", SRC, "strong", "Retroactieve investeringspremie 130.7m 2021; tick744"),
    ("bud_vl_retro_invest_premie_2022", "vlaanderen_gov", 2022, 30600000, "", "", "outturn", SRC, "strong", "Retroactieve investeringspremie 30.6m 2022; tick744"),
    ("bud_vl_retro_invest_premie_2023", "vlaanderen_gov", 2023, 1600000, "", "", "outturn", SRC, "strong", "Retroactieve investeringspremie 1.6m 2023; tick744"),
    ("bud_vl_retro_invest_premie_cum_2021_23", "vlaanderen_gov", 2023, 158600000, "", "", "outturn", SRC, "strong", "Retro premies cum 158.6m 2021-23 CoA (near 159m T10); tick744"),
    # Call groene stroom residual
    ("bud_vl_call_groene_stroom_2021_23", "vlaanderen_gov", 2023, 33800000, "", "", "outturn", SRC, "strong", "Call groene stroom 33.8m of 37.1m in 2021-23 (90pct) nine calls ~1000 projects; tick744"),
    ("bud_vl_call_groene_stroom_stop_2024", "vlaanderen_gov", 2024, 0, "", "", "outturn", SRC, "strong", "Call groene stroom stopped 2024 stop-and-go residual; tick744"),
    ("bud_vl_call_groene_stroom_plan_budget_class", "vlaanderen_gov", 2025, 25200000, "", "", "budgeted", SRC, "medium", "Zonneplan 2025 estimated 25.2m/yr for ~80 MW residual; system stopped 2024; tick744"),
    # Call groene warmte residual
    ("bud_vl_call_groene_warmte_2021_23", "vlaanderen_gov", 2023, 70400000, "", "", "outturn", SRC, "strong", "Call groene warmte 70.4m 2021-23 of 108.7m cum for 105 approved apps; tick744"),
    ("bud_vl_call_groene_warmte_projects_n_105", "vlaanderen_gov", 2023, 105, "", "", "outturn", SRC, "strong", "Call groene warmte approved applications COUNT 105 in 2021-23; tick744"),
    # VLAIO dual industrial heat residual (outside T10)
    ("bud_vl_vlaio_ecology_support_class_2024", "vlaanderen_gov", 2024, 48000000, "", "", "outturn", SRC, "strong", "VLAIO ecology support ~48m 2024 (was ~25m prior years); dual VEKA heat calls; tick744"),
    ("bud_vl_klimaatoproep_industrial_70m", "vlaanderen_gov", 2025, 70000000, "", "", "budgeted", SRC, "strong", "Klimaatoproep industrial low-carbon pilot envelope 70m; tick744"),
    # VEKP invest cost opacity residual
    ("bud_vl_vekp2019_invest_low_752m", "vlaanderen_gov", 2021, 752000000, "", "", "projection", SRC, "strong", "VEKP2019 invest low estimate 752m/yr public+private 2021-30 now outdated; tick744"),
    ("bud_vl_vekp2019_invest_mid_1900m", "vlaanderen_gov", 2021, 1900000000, "", "", "projection", SRC, "strong", "VEKP2019 invest mid 1900m/yr; tick744"),
    ("bud_vl_vekp2019_invest_high_2200m", "vlaanderen_gov", 2021, 2200000000, "", "", "projection", SRC, "strong", "VEKP2019 invest high 2200m/yr; tick744"),
    ("bud_vl_vekp2025_no_invest_cost_update", "vlaanderen_gov", 2025, 0, "", "", "outturn", SRC, "strong", "VEKP2025 has no updated investment-cost plan for raised RES goals; CoA finding; tick744"),
    # Minister GSC social-cost path residual
    ("bud_vl_gsc_social_cost_path_2025_min", "vlaanderen_gov", 2025, 872000000, "", "", "projection", SRC, "medium", "Minister 2020 path: social GSC cost to 872m in 2025; wind GSC restart not in path; tick744"),
    ("bud_vl_gsc_social_cost_path_2030_min", "vlaanderen_gov", 2030, 390000000, "", "", "projection", SRC, "medium", "Minister 2020 path: social GSC cost to 390m in 2030; sunset end-2032 almost; tick744"),
    # Fluvius grid residual dual
    ("bud_fluvius_invest_baseline_7bn_2024_33", "fluvius", 2033, 7000000000, "", "", "budgeted", SRC, "strong", "Fluvius invest plan baseline ~7bn 2024-2033 without extra transition; tick744"),
    ("bud_fluvius_invest_extra_transition_4bn", "fluvius", 2033, 4000000000, "", "", "budgeted", SRC, "strong", "Fluvius extra ~4bn energy-transition investments 2024-33 on top of 7bn; tick744"),
    ("bud_fluvius_invest_transition_total_class_11bn", "fluvius", 2033, 11000000000, "", "", "budgeted", SRC, "medium", "Fluvius baseline+extra transition class ~11bn 2024-33; tariff residual; tick744"),
    # Floating PV ad hoc residual
    ("bud_vl_floating_pv_budget_6_7m", "vlaanderen_gov", 2023, 6700000, "", "", "budgeted", SRC, "strong", "Ad hoc floating PV innovative energy projects budgeted 6.7m; tick744"),
    ("bud_vl_floating_pv_paid_2_3m", "vlaanderen_gov", 2023, 2300000, "", "", "outturn", SRC, "strong", "Floating PV ad hoc paid only 2.3m (34pct of 6.7m); tick744"),
    # Premiums heat residential share
    ("bud_vl_heat_premiums_residential_share_98pct", "vlaanderen_gov", 2023, 98, "", "", "outturn", SRC, "strong", "Heat premiums: ~98pct of awarded amount to residential buildings; tick744"),
    # GSC annual series residual (Table10 GSC line)
    ("bud_vl_gsc_2014", "vlaanderen_gov", 2014, 1030000000, "", "", "outturn", SRC, "strong", "GSC support 1030m 2014 CoA T10; tick744"),
    ("bud_vl_gsc_2015", "vlaanderen_gov", 2015, 1120000000, "", "", "outturn", SRC, "strong", "GSC support 1120m 2015; tick744"),
    ("bud_vl_gsc_2016", "vlaanderen_gov", 2016, 1026000000, "", "", "outturn", SRC, "strong", "GSC support 1026m 2016; tick744"),
    ("bud_vl_gsc_2017", "vlaanderen_gov", 2017, 1078000000, "", "", "outturn", SRC, "strong", "GSC support 1078m 2017; tick744"),
    ("bud_vl_gsc_2018", "vlaanderen_gov", 2018, 1152000000, "", "", "outturn", SRC, "strong", "GSC support 1152m 2018; tick744"),
    ("bud_vl_gsc_2019", "vlaanderen_gov", 2019, 1111000000, "", "", "outturn", SRC, "strong", "GSC support 1111m 2019; tick744"),
    ("bud_vl_gsc_2020", "vlaanderen_gov", 2020, 1142000000, "", "", "outturn", SRC, "strong", "GSC support 1142m 2020; tick744"),
    # dual residual
    ("bud_dual_vl_res_bill_vs_budget_85pct", "gg_belgium", 2023, 855, "", "", "outturn", SRC_DUAL, "strong", "VL RES support ~85.5pct on electricity bill dual federal GSC/Elia assign opacity; tick744"),
    ("bud_dual_vl_heat_underfunded_vs_use", "gg_belgium", 2023, 16, "", "", "outturn", SRC_DUAL, "strong", "Heat gets 16pct of VL RES support while >50pct energy use is heat; dual WAL CV residual; tick744"),
    ("bud_dual_fluvius_grid_vs_res_support", "gg_belgium", 2033, 11000000000, "", "", "budgeted", SRC_DUAL, "medium", "Fluvius transition+baseline class 11bn dual with VL RES support 13bn cum 2014-23 not additive; tick744"),
]

# fix unit price row: use 12.5 as amount_eur
for i, b in enumerate(budgets):
    if b[0] == "bud_vl_stat_transfer_unit_price_class":
        budgets[i] = ("bud_vl_stat_transfer_unit_price_eur_mwh", "vlaanderen_gov", 2021, 12.5, "", "", "outturn", SRC, "strong", "Negotiated statistical-transfer unit ~12.5 EUR/MWh CoA; tick744")

bud_path = DATA / "budgets.csv"
with open(bud_path, encoding="utf-8", newline="") as f:
    br = csv.DictReader(f)
    bfields = br.fieldnames
    existing = {r["budget_id"] for r in br}
added_b = 0
with open(bud_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bfields, lineterminator="\n")
    for row in budgets:
        if row[0] in existing:
            continue
        w.writerow({
            "budget_id": row[0], "entity_id": row[1], "year": row[2],
            "amount_eur": row[3], "amount_min_eur": row[4], "amount_max_eur": row[5],
            "basis": row[6], "source_id": row[7], "confidence": row[8], "notes": row[9],
        })
        added_b += 1
print(f"budgets +{added_b}")

# --- commitments ---
commitments = [
    {
        "commitment_id": "cmt_vl_gsc_tech_split_2014_23",
        "title": "Flanders GSC support tech split PV 7.078bn / wind 1.516 / biomass 1.258 of 10.508bn",
        "entity_id": "vlaanderen_gov",
        "beneficiary": "RES producers (PV-heavy) / electricity consumers",
        "legal_basis": "Energiedecreet GSC + CoA 2025_34 ch5.3.1",
        "decision_date": "2025-09-30",
        "start_year": "2014",
        "end_year": "2023",
        "total_envelope_eur": "10508000000",
        "cash_by_year": '{"pv_m":7078,"wind_m":1516,"biomass_m":1258,"avg_annual_m":1051,"budget_borne_m":1011,"budget_share_pct":9,"bill_borne_m":9497,"pv_share_pct":67}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Support renewable electricity production via certificates",
        "cut_option": "Keep wind-only path; no new PV GSC; publish annual tech cash FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Energie>GSC>tech_split",
        "notes": "tick744 residual tech split on top of prior GSC aggregate",
    },
    {
        "commitment_id": "cmt_vl_res_support_budget_vs_bill_2014_23",
        "title": "VL RES support 12.97bn of which budget only ~1.8bn (14.5pct) rest ODV/bill",
        "entity_id": "vlaanderen_gov",
        "beneficiary": "Electricity consumers (ODV) / VL budget",
        "legal_basis": "Energiedecreet ODV + CoA 2025_34 §5.2.3",
        "decision_date": "2025-09-30",
        "start_year": "2014",
        "end_year": "2023",
        "total_envelope_eur": "12970000000",
        "cash_by_year": '{"total_m":12970,"budget_m":1800,"budget_share_pct":14.5,"bill_odv_share_pct":85.5,"gsc_m":10508,"wkc_m":1785,"certs_share_pct":95}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Finance RES without full budget burden",
        "cut_option": "Move residual support to general budget per SERV/VREG FOI path",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Energie>RES>budget_vs_bill",
        "notes": "tick744",
    },
    {
        "commitment_id": "cmt_vl_heat_vs_power_support_imbalance",
        "title": "Green power 84pct of RES support vs heat 16pct despite heat >50pct of energy use",
        "entity_id": "vlaanderen_gov",
        "beneficiary": "Power RES producers vs heat sector underfunded",
        "legal_basis": "CoA 2025_34 §5.2.1 + energyvisie 2017 heat priority",
        "decision_date": "2025-09-30",
        "start_year": "2014",
        "end_year": "2023",
        "total_envelope_eur": "12970000000",
        "cash_by_year": '{"power_share_pct":84,"heat_share_pct":16,"green_power_m":10864,"green_heat_m":274,"wkc_m":1785,"heat_miss_targets":"2020_and_2023"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Balance RES portfolio toward heat priority",
        "cut_option": "Reallocate new support to heat/calls; end PV legacy GSC",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Energie>heat_power_imbalance",
        "notes": "tick744",
    },
    {
        "commitment_id": "cmt_fluvius_transition_invest_4bn_extra",
        "title": "Fluvius extra energy-transition investments ~4bn on 7bn baseline 2024-2033",
        "entity_id": "fluvius",
        "beneficiary": "Grid users Flanders",
        "legal_basis": "Fluvius invest plan cited CoA 2025_34 §5.7",
        "decision_date": "2024-01-01",
        "start_year": "2024",
        "end_year": "2033",
        "total_envelope_eur": "11000000000",
        "cash_by_year": '{"baseline_bn":7,"extra_transition_bn":4,"total_class_bn":11,"tariff_pass_through":true}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Enable electrification and RES integration",
        "cut_option": "Publish project L5 + unit costs FOI dual RES support",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Fluvius>transition_invest",
        "notes": "tick744 dual RES support bill stack",
    },
    {
        "commitment_id": "cmt_vl_vekp_invest_cost_opacity",
        "title": "VEKP investment-cost estimates 752-2200m/yr outdated; VEKP2025 no update",
        "entity_id": "veka",
        "beneficiary": "Taxpayers / consumers / investors",
        "legal_basis": "VEKP 2019/2023/2025 + CoA 2025_34 §5.1",
        "decision_date": "2025-07-18",
        "start_year": "2019",
        "end_year": "2030",
        "total_envelope_eur": "",
        "cash_by_year": '{"vekp2019_low_m":752,"mid_m":1900,"high_m":2200,"vekp2025_update":"none","ec_flagged":true}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Transparent multi-year energy-transition financing plan",
        "cut_option": "Publish updated multi-year cost plan FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VEKA>VEKP_cost_plan",
        "notes": "tick744",
    },
    {
        "commitment_id": "cmt_dual_vl_res_odv_bill_stack",
        "title": "Dual VL RES ODV/bill stack vs federal Elia GSC assign opacity",
        "entity_id": "gg_belgium",
        "beneficiary": "Electricity consumers multi-level",
        "legal_basis": "CoA VL 2025_34 + CoA fed energy dual prior",
        "decision_date": "2025-09-30",
        "start_year": "2014",
        "end_year": "2026",
        "total_envelope_eur": "12970000000",
        "cash_by_year": '{"vl_res_cum_m":12970,"vl_budget_share_pct":14.5,"elia_gsc_assign_m_class":552,"not_additive_te":true}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": URL,
        "stated_goal": "Honest multi-level map of RES support incidence",
        "cut_option": "Unified consumer-bill RES line FOI dual",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "BE>dual>RES_bill_stack",
        "notes": "tick744 not TE-additive",
    },
]

cmt_path = DATA / "commitments.csv"
with open(cmt_path, encoding="utf-8", newline="") as f:
    cr = csv.DictReader(f)
    cfields = cr.fieldnames
    existing_c = {r["commitment_id"] for r in cr}
added_c = 0
with open(cmt_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cfields, lineterminator="\n")
    for row in commitments:
        if row["commitment_id"] in existing_c:
            continue
        w.writerow(row)
        added_c += 1
print(f"commitments +{added_c}")

# --- leaderboard ---
leaderboard = [
    {
        "item_id": "lb_vl_gsc_pv_legacy_7_078bn",
        "name": "Flanders GSC PV legacy oversubsidy 7.078bn of 10.508bn (67%)",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Energie>GSC>PV_legacy",
        "annual_cost_eur": "707800000",
        "total_cost_eur": "7078000000",
        "tco_notes": "CoA strong: PV took 67pct of GSC 2014-23; classic oversubsidy; phase-out except wind restart",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Early PV owners / RES producers",
        "stated_goal": "Kickstart solar deployment",
        "measured_outcome": "Large bill pass-through; cost-inefficient vs later calls",
        "absurdity_score": "8.5",
        "cost_score": "9.0",
        "difficulty": "5",
        "priority_index": "8.05",
        "cut_proposal": "No new PV GSC; accelerate inventory buyback transparency; publish tech cash FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick744 residual tech split; annual class ~avg of cum",
    },
    {
        "item_id": "lb_vl_res_support_on_bill_85pct",
        "name": "VL RES support ~85.5% on electricity bill not budget (of 12.97bn)",
        "level": "L5",
        "type": "off_budget",
        "hierarchy_path": "Vlaanderen>Energie>RES>ODV_bill",
        "annual_cost_eur": "1100000000",
        "total_cost_eur": "11100000000",
        "tco_notes": "CoA: budget only ~1.8bn of 13bn; ODV DSO+supplier pass-through hides TE path",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "RES producers / VL budget optics",
        "stated_goal": "Support RES without full budget load",
        "measured_outcome": "Opaque consumer tax via tariffs; SERV/VREG prefer budget channel",
        "absurdity_score": "8.0",
        "cost_score": "9.0",
        "difficulty": "4",
        "priority_index": "7.90",
        "cut_proposal": "Move residual support on-budget; annual bill incidence table FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick744",
    },
    {
        "item_id": "lb_vl_heat_underfunded_vs_use",
        "name": "Green heat only 16% of RES support while heat >50% of energy use",
        "level": "L5",
        "type": "misallocation",
        "hierarchy_path": "Vlaanderen>Energie>heat_underfund",
        "annual_cost_eur": "27400000",
        "total_cost_eur": "274000000",
        "tco_notes": "CoA T10 heat line 274m vs power 10.864bn; heat targets missed 2020 and 2023",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Power RES stack over heat sector",
        "stated_goal": "Energyvisie heat priority 2017",
        "measured_outcome": "Heat targets missed; support not matching priority",
        "absurdity_score": "7.5",
        "cost_score": "6.5",
        "difficulty": "4",
        "priority_index": "6.75",
        "cut_proposal": "Reallocate new calls to heat; dual VLAIO/VEKA shop risk FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick744 annual class heat/10y",
    },
    {
        "item_id": "lb_vl_vekp_cost_plan_missing",
        "name": "VEKP2025 no multi-year RES investment cost plan (2019 range 0.75-2.2bn/yr obsolete)",
        "level": "L5",
        "type": "governance",
        "hierarchy_path": "Vlaanderen>VEKA>VEKP_cost_opacity",
        "annual_cost_eur": "0",
        "total_cost_eur": "0",
        "tco_notes": "CoA: three 2019 estimates 752/1900/2200m/yr outdated by higher goals; VEKP2025 no refresh",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Policy planners",
        "stated_goal": "Transparent transition financing",
        "measured_outcome": "No quantified multi-year plan for raised goals",
        "absurdity_score": "7.0",
        "cost_score": "6.0",
        "difficulty": "3",
        "priority_index": "6.20",
        "cut_proposal": "Force updated multi-year cost table FOI dual Fluvius 4bn",
        "status": "active",
        "struck_reason": "",
        "notes": "tick744 euro Unknown for full need — FOI",
    },
    {
        "item_id": "lb_fluvius_extra_transition_4bn",
        "name": "Fluvius extra grid transition invest ~4bn 2024-33 (on 7bn baseline)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Fluvius>transition_4bn",
        "annual_cost_eur": "400000000",
        "total_cost_eur": "4000000000",
        "tco_notes": "CoA cites Fluvius plan +4bn transition on top of 7bn; tariff residual dual RES bill stack",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Grid users Flanders",
        "stated_goal": "Enable electrification and RES connection",
        "measured_outcome": "Core capex class; project L5 residual",
        "absurdity_score": "4.0",
        "cost_score": "8.5",
        "difficulty": "5",
        "priority_index": "6.25",
        "cut_proposal": "Project top20 unit-cost FOI; dual RES support incidence",
        "status": "active",
        "struck_reason": "",
        "notes": "tick744 not pure waste — core grid",
    },
    {
        "item_id": "lb_vl_stat_transfer_46m_paper_res",
        "name": "VL statistical RES transfers 46.1m (paper MWh @ ~12.5 EUR) for 2020-21 goals",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Energie>stat_transfer",
        "annual_cost_eur": "23050000",
        "total_cost_eur": "46100000",
        "tco_notes": "CoA: 46.1m buy for 2020+2021; no quantified options analysis vs domestic build",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Foreign surplus RES sellers / VL goal compliance",
        "stated_goal": "Meet RES targets with statistical transfer",
        "measured_outcome": "Paper RES not generation; dual federal DK transfer",
        "absurdity_score": "6.5",
        "cost_score": "4.5",
        "difficulty": "3",
        "priority_index": "5.40",
        "cut_proposal": "Prefer domestic heat/power if cheaper; publish options FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick744",
    },
    {
        "item_id": "lb_dual_vl_res_bill_stack",
        "name": "Dual VL RES ODV/bill 85% + federal Elia GSC assign opacity",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>RES_bill_stack",
        "annual_cost_eur": "0",
        "total_cost_eur": "12970000000",
        "tco_notes": "Not TE-additive; dual map of consumer-bill RES incidence multi-level",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "Multi-level RES producers",
        "stated_goal": "Honest dual map of RES support incidence",
        "measured_outcome": "VL bill-heavy + federal assign opacity residual",
        "absurdity_score": "7.5",
        "cost_score": "8.0",
        "difficulty": "4",
        "priority_index": "7.20",
        "cut_proposal": "Unified consumer RES line FOI dual",
        "status": "active",
        "struck_reason": "",
        "notes": "tick744",
    },
]

lb_path = DATA / "leaderboard.csv"
with open(lb_path, encoding="utf-8", newline="") as f:
    lr = csv.DictReader(f)
    lfields = lr.fieldnames
    existing_l = {r["item_id"] for r in lr}
added_l = 0
with open(lb_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lfields, lineterminator="\n")
    for row in leaderboard:
        if row["item_id"] in existing_l:
            continue
        w.writerow(row)
        added_l += 1
print(f"leaderboard +{added_l}")

# --- sources ---
sources = [
    {
        "source_id": SRC,
        "title": "Rekenhof Hernieuwbare energie in Vlaanderen residual L5 tick744 (tech split budget vs bill heat imbalance)",
        "url": URL,
        "publisher": "Rekenhof Nederlandse kamer",
        "accessed_date": "2026-08-02",
        "source_class": "court_of_audit",
        "notes": "Strong tick744 residual on 2025_34: GSC PV 7078/wind 1516/biomass 1258 of 10508; budget GSC 1011 (9pct); total budget share ~1.8bn of 12.97bn (14.5pct); heat 274m vs power 10864m (16/84); WKC budget 166; stat transfer 46.1 @12.5 EUR/MWh; Fluvius +4bn on 7bn; VEKP cost plan missing; retro 130.7/30.6/1.6; raw ccrek_2025_34_hernieuwbare.pdf",
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual VL RES bill/ODV stack residual tick744",
        "url": URL,
        "publisher": "DOGE synthesis CoA 2025_34 + prior fed energy",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: VL ~85.5pct on bill + heat underfund 16pct + Fluvius transition 4bn dual federal Elia GSC assign; tick744",
    },
]
src_path = DATA / "sources.csv"
with open(src_path, encoding="utf-8", newline="") as f:
    sr = csv.DictReader(f)
    sfields = sr.fieldnames
    existing_s = {r["source_id"] for r in sr}
added_s = 0
with open(src_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, lineterminator="\n")
    for row in sources:
        if row["source_id"] in existing_s:
            continue
        w.writerow(row)
        added_s += 1
print(f"sources +{added_s}")

# --- FOI queue ---
foi_row = {
    "gap_id": "gap_vl_hernieuwbare_residual_l5",
    "hierarchy_path": "Vlaanderen>Energie>Hernieuwbare_residual_L5",
    "entity_id": "veka",
    "what_is_missing": "Machine-readable L5: (1) annual GSC cash by technology (PV/wind/biomass/biogas/hydro) 2014-2025 and budget-vs-bill split; (2) WKC same; (3) VEKP2025 multi-year investment-cost table replacing obsolete 752-2200m/yr; (4) Fluvius ODV pass-through series for GSC/WKC in tariffs; (5) dual VLAIO ecology vs VEKA heat-call project list to detect double-subsidy; (6) wind GSC restart bandingfactor cost path vs CfD reform",
    "why_it_matters": "CoA residual shows 12.97bn RES support with only ~14.5pct on budget and 67pct of GSC to PV legacy — tech cash and bill incidence still opaque for waste ranking",
    "priority": "8",
    "recipient_body": "VEKA / Vlaamse overheid Team Openbaarheid / Fluvius",
    "recipient_email": "openbaarheid@vlaanderen.be",
    "recipient_postal": "Havenlaan 88 bus 20 1000 Brussel",
    "draft_letter_path": "docs/doge/foi/drafts/gap_vl_hernieuwbare_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_vl_gsc_tech_split_2014_23|cmt_vl_res_support_budget_vs_bill_2014_23|cmt_fluvius_transition_invest_4bn_extra",
    "linked_leaderboard_id": "lb_vl_gsc_pv_legacy_7_078bn|lb_vl_res_support_on_bill_85pct|lb_dual_vl_res_bill_stack",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick744 CoA 2025_34 residual L5; ready not sent; related gap_vl_odv_mvp_cash",
}
foi_path = DATA / "foi_queue.csv"
with open(foi_path, encoding="utf-8", newline="") as f:
    fr = csv.DictReader(f)
    ffields = fr.fieldnames
    existing_f = {r["gap_id"] for r in fr}
if foi_row["gap_id"] not in existing_f:
    with open(foi_path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ffields, lineterminator="\n")
        w.writerow(foi_row)
    print("foi +1")
else:
    print("foi exists")

# --- research_queue close/spawn ---
rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)

for r in rqs:
    if r.get("task_id") == "rq_735":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick744 CoA 2025_34 hernieuwbare residual: GSC PV 7.078bn/wind 1.516/biomass 1.258 of 10.508; "
            "budget ~1.8bn of 12.97bn (14.5pct); heat 16pct vs power 84pct; Fluvius +4bn; FOI gap_vl_hernieuwbare_residual_l5 ready"
        )

if not any(r.get("task_id") == "rq_736" for r in rqs):
    rqs.append({
        "task_id": "rq_736",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: new CoA/primary PDF not yet mined (prefer CoA federal 2026_30 jaarverslag residual "
            "or 2026_24 prisons follow-up residual if not mined) or Entity II dual residual or fed Pillar2/VVPR recheck"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick744 after rq_735",
    })

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rqs)
print("research_queue rq_735=done rq_736 open")

# --- loop_state ---
ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys()) if ls else [
        "state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id",
        "ticks_completed", "paused", "notes",
    ]
row = ls[0] if ls else {k: "" for k in lsfields}
row.update({
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_735",
    "ticks_completed": "744",
    "paused": "no",
    "notes": "tick744 CoA hernieuwbare residual GSC tech/bill split; next rq_736; progress@750 in 6; rq_116 deferred",
})
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerow(row)
print("loop_state -> 744")
print("DONE tick744")

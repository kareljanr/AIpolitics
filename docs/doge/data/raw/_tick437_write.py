# tick 437: CoA Budget 2026 INAMI health save L5 + NATO multi-year residual + Justice/security provisions
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T09:15:00Z"
TICK = 437
UNIT = "rq_428"
SRC = "src_ccrek_budget2026_sante_nato_justice"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf"

YEARS = (2025, 2026, 2027, 2028, 2029)

# --- INAMI health savings L5 p84 (m EUR 2026) ---
SANTE = {
    "total": 764.5,
    "drugs": 401.9,
    "doctors": 213.2,
    "hospitals": 50.0,
    "other_sectors": 73.8,
    "tm_reserved": 25.6,
    # pharma L5
    "drugs_price_cuts": 80.3,
    "drugs_antiacids": 65.8,
    "drugs_lipid": 29.4,
    "drugs_partial_bill_hosp": 42.0,
    "drugs_tm_per_pack": 27.9,
    "drugs_proposed_inami": 252.9,
    "drugs_residual_design": 148.9,
    # doctors L5
    "doctors_lab": 70.8,
    "doctors_imaging": 68.5,
    "doctors_surgery": 63.7,
    "doctors_delay_risk": 41.5,  # not realized 2026 per INAMI
    # hospitals
    "hosp_day": 47.1,
    "hosp_other": 3.0,
}
# pharma proposed sum check: 80.3+65.8+29.4+42+27.9 = 245.4 (~252.9 residual design elsewhere)

# --- NATO multi-year p29-30 ---
NATO = {
    "gdp_m": (636320, 655357, 675594, 695626, 717335),
    "need_2pct_m": (12726.4, 13107.1, 13511.9, 13912.5, 14346.7),
    "s16_budget_m": (10485.8, 10769.6, 11058.4, 11239.3, 11395.8),
    "s16_liq_m": (10485.8, 10769.6, 11100.8, 11317.8, 11478.8),
    "gdp_corr_m": (0.0, 0.0, -42.4, -78.5, -83.0),
    "external_m": (2239.9, 2326.2, 2514.7, 2710.7, 2893.9),
    "pens_mil_m": (1597.0, 1688.0, 1695.0, 1684.0, 1685.0),
    "pens_civ_m": (71.0, 73.0, 75.0, 77.0, 79.0),
    "pens_surv_m": (264.0, 267.0, 270.0, 273.0, 276.0),
    "other_depts_m": (140.4, 130.7, 174.7, 176.7, 103.9),
    "std_total_m": (167.5, 167.5, 300.0, 500.0, 750.0),
    "std_miliciens_m": (167.5, 167.5, 167.5, 167.5, 167.5),
    "std_new_m": (0.0, 0.0, 132.5, 332.5, 582.5),
    "effort_total_m": (12725.7, 13095.8, 13573.1, 13950.0, 14289.7),
    "s16_share_pct": (82.4, 82.2, 81.5, 80.6, 79.7),
    "std_share_total_pct": (1.3, 1.3, 2.2, 3.6, 5.2),
}
FIN = {
    "extra_spend_m": (3866, 3522, 3222, 3099, 3074),  # total 16783
    "temp_fin_m": (1708, 1663, 1217, 1269, 1297),  # 7154
    "cit_russian_m": (1208, 1163, 1217, 1269, 1297),  # 6154
    "belfius_m": (500, 500, 0, 0, 0),  # 1000
    "struct_total_m": (125, 400, 1050, 1500, 1750),  # 4825
    "std_fin_m": (125, 150, 300, 500, 750),  # 1825 (plan std targets)
    "struct_net_m": (0, 250, 750, 1000, 1000),  # 3000
    "deficit_temp_m": (2033, 1459, 955, 330, 27),  # 4804
    "asset_optim_pack_m": 3170,
}

# --- Security provision p59 + Justice p59-60 ---
SEC_PROV_2026 = {
    "total": 366.9,
    "renforcement": 250.0,  # structural security+return
    "surpop_struct": 60.0,  # was 55 one-off then +5 structural
    "report_justice": 6.2,  # unused 2025 carry
    "justice_interior_extra": 50.7,  # purpose opaque CoA (J 44 + I 6)
}
# Of renforcement 250: Justice 112.5, Fed police 87.5, migration 50
# Of surpop 60: Justice 50, Health 5, migration 5
JUSTICE = {
    "section_credits_2026": 2843.0,
    "provisions_for_justice_2026": 465.5,
    "prov_securite_j": 112.5,
    "prov_surpop_ops_j": 50.0,
    "prov_surpop_infra": 259.0,  # with Regie
    "prov_efficience_j": 44.0,
    "surpop_envelope_2026_29": 840.0,  # 600 infra + 240 structural
    "surpop_infra_pack": 600.0,
    "surpop_struct_pack": 240.0,  # J 50/yr + Health 5 + Mig 5 = 60/yr * 4
    "tf_need_class": 1100.0,  # 1.1bn TF needs
    "tf_capacity_places_2026": 1052,
    "tf_capacity_budget_2026": 303.8,
}

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 INAMI sante L5 + NATO multi-year + Justice/security provisions",
            "url": URL,
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": (
                f"p84 health save 764.5 L5; p28-31 NATO 2pct path+financing; "
                f"p59-60 security prov 366.9 Justice 465.5; tick{TICK}"
            ),
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add_bud(bid, entity, year, amount, basis, notes, conf="strong"):
    if any(r["budget_id"] == bid for r in bud):
        return False
    bud.append(
        {
            "budget_id": bid,
            "entity_id": entity,
            "year": str(year),
            "amount_eur": str(int(round(amount))),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": SRC,
            "confidence": conf,
            "notes": notes,
        }
    )
    return True


n_bud = 0

# Health L5
for key, v in SANTE.items():
    conf = "medium" if key in (
        "drugs_residual_design",
        "doctors_delay_risk",
        "hosp_day",
        "hosp_other",
        "other_sectors",
        "tm_reserved",
    ) else "strong"
    note_extra = ""
    if key == "drugs_residual_design":
        note_extra = " still to design CoA;"
    if key == "doctors_delay_risk":
        note_extra = " INAMI says not realized 2026 late entry;"
    if key == "hosp_day":
        note_extra = " linear advance cut = cash shift not true 2026 dep cut CoA;"
    if add_bud(
        f"bud_inami_l5_{key}_2026",
        "riziv",
        2026,
        v * 1e6,
        "budgeted",
        f"INAMI health save L5 {key} {v}m 2026 CoA p84;{note_extra} dual total 764.5; tick{TICK}",
        conf,
    ):
        n_bud += 1

# NATO multi-year series
for i, y in enumerate(YEARS):
    series = [
        ("gdp", NATO["gdp_m"][i] * 1e6, "gg_belgium", "strong", f"BFP GDP used for NATO 2pct {NATO['gdp_m'][i]}m {y}"),
        ("need_2pct", NATO["need_2pct_m"][i] * 1e6, "mod_defensie", "strong", f"NATO 2pct need {NATO['need_2pct_m'][i]}m {y}"),
        ("s16_budget", NATO["s16_budget_m"][i] * 1e6, "mod_defensie", "strong" if y <= 2026 else "medium", f"Defence budget s16 {NATO['s16_budget_m'][i]}m {y}"),
        ("s16_liq", NATO["s16_liq_m"][i] * 1e6, "mod_defensie", "strong" if y <= 2026 else "medium", f"Defence s16 liquidations {NATO['s16_liq_m'][i]}m {y}"),
        ("external", NATO["external_m"][i] * 1e6, "mod_defensie", "strong" if y <= 2026 else "medium", f"External defence effort {NATO['external_m'][i]}m {y}"),
        ("pens_mil", NATO["pens_mil_m"][i] * 1e6, "fpd", "strong" if y <= 2026 else "medium", f"Military pensions NATO {NATO['pens_mil_m'][i]}m {y}"),
        ("pens_civ", NATO["pens_civ_m"][i] * 1e6, "fpd", "strong" if y <= 2026 else "medium", f"Civil defence pensions {NATO['pens_civ_m'][i]}m {y}"),
        ("pens_surv", NATO["pens_surv_m"][i] * 1e6, "fpd", "strong" if y <= 2026 else "medium", f"Survivor defence pensions {NATO['pens_surv_m'][i]}m {y}"),
        ("other_depts", NATO["other_depts_m"][i] * 1e6, "mod_defensie", "medium", f"Other depts military {NATO['other_depts_m'][i]}m {y}"),
        ("std_total", NATO["std_total_m"][i] * 1e6, "mod_defensie", "medium" if y >= 2027 else "strong", f"Standardisation total {NATO['std_total_m'][i]}m {y}"),
        ("std_miliciens", NATO["std_miliciens_m"][i] * 1e6, "fpd", "medium", f"Former conscript pensions std {NATO['std_miliciens_m'][i]}m {y}"),
        ("std_new", NATO["std_new_m"][i] * 1e6, "mod_defensie", "medium", f"New-to-standardise (circular pending) {NATO['std_new_m'][i]}m {y}"),
        ("effort_total", NATO["effort_total_m"][i] * 1e6, "mod_defensie", "strong" if y <= 2026 else "medium", f"NATO effort total {NATO['effort_total_m'][i]}m {y} ({NATO['effort_total_m'][i]/NATO['need_2pct_m'][i]*100:.1f}pct of need)"),
        ("extra_spend", FIN["extra_spend_m"][i] * 1e6, "mod_defensie", "strong", f"Additional defence spend plan {FIN['extra_spend_m'][i]}m {y}"),
        ("temp_fin", FIN["temp_fin_m"][i] * 1e6, "sec_federal", "strong", f"Temporary defence financing {FIN['temp_fin_m'][i]}m {y}"),
        ("cit_russian", FIN["cit_russian_m"][i] * 1e6, "sec_federal", "medium", f"CIT on frozen Russian asset interest {FIN['cit_russian_m'][i]}m {y}"),
        ("belfius", FIN["belfius_m"][i] * 1e6, "sec_federal", "strong", f"Belfius exceptional dividend defence {FIN['belfius_m'][i]}m {y}"),
        ("struct_total", FIN["struct_total_m"][i] * 1e6, "mod_defensie", "medium", f"Structural defence financing total {FIN['struct_total_m'][i]}m {y}"),
        ("struct_net", FIN["struct_net_m"][i] * 1e6, "mod_defensie", "medium", f"Structural net (ex-std) {FIN['struct_net_m'][i]}m {y}"),
        ("deficit_temp", FIN["deficit_temp_m"][i] * 1e6, "mod_defensie", "medium", f"Temporarily higher deficit for defence {FIN['deficit_temp_m'][i]}m {y}"),
    ]
    if NATO["gdp_corr_m"][i] != 0:
        series.append(
            (
                "gdp_corr",
                NATO["gdp_corr_m"][i] * 1e6,
                "mod_defensie",
                "medium",
                f"GDP correction on s16 CM 12Dec {NATO['gdp_corr_m'][i]}m {y}",
            )
        )
    for key, amt, ent, conf, note in series:
        if add_bud(
            f"bud_nato_l5_{key}_{y}",
            ent,
            y,
            amt,
            "budgeted" if y >= 2026 else "outturn",
            f"{note} CoA p29-30; tick{TICK}",
            conf,
        ):
            n_bud += 1

if add_bud(
    "bud_nato_asset_optim_pack",
    "sec_federal",
    2025,
    FIN["asset_optim_pack_m"] * 1e6,
    "budgeted",
    (
        f"Asset optimisation package to limit debt from defence deficit {FIN['asset_optim_pack_m']}m 2025-29 "
        f"(~2/3 of temp deficit 4804m); implementation still open CoA; tick{TICK}"
    ),
    "medium",
):
    n_bud += 1

# Security provision L5
for key, v in SEC_PROV_2026.items():
    conf = "medium" if key == "justice_interior_extra" else "strong"
    if add_bud(
        f"bud_sec_prov_{key}_2026",
        "sec_federal",
        2026,
        v * 1e6,
        "budgeted",
        (
            f"Security/return interdept provision L5 {key} {v}m 2026 CoA p59 "
            f"(total 366.9; renforcement split J112.5 police87.5 mig50; "
            f"surpop J50 health5 mig5; opaque +50.7 J44+I6); tick{TICK}"
        ),
        conf,
    ):
        n_bud += 1

# Justice package
for key, v in JUSTICE.items():
    if key in ("tf_capacity_places_2026",):
        # headcount
        if add_bud(
            f"bud_justice_{key}",
            "fod_justice",
            2026,
            v,
            "estimate",
            f"TF capacity proposal {v} new detention places 2026 (incl Antwerp) CoA p60; headcount; tick{TICK}",
            "medium",
        ):
            n_bud += 1
        continue
    conf = "medium" if "tf" in key else "strong"
    ent = "fod_justice" if key != "surpop_infra_pack" else "sec_federal"
    if add_bud(
        f"bud_justice_{key}",
        ent,
        2026 if "2026_29" not in key and "pack" not in key or "2026" in key else 2026,
        v * 1e6 if key != "tf_capacity_places_2026" else v,
        "budgeted",
        f"Justice/surpop L5 {key} {v}{'m EUR' if key != 'tf_capacity_places_2026' else ' places'} CoA p59-60; tick{TICK}",
        conf,
    ):
        n_bud += 1

# Explicit multi-year structural surpop 60/yr
for y in (2026, 2027, 2028, 2029):
    if add_bud(
        f"bud_surpop_struct_annual_{y}",
        "fod_justice",
        y,
        60e6,
        "budgeted",
        f"Structural surpopulation financing 60m/yr {y} (Justice 50 + Health 5 + Migration 5) of 240m pack; tick{TICK}",
        "strong",
    ):
        n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

# --- commitments ---
with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())

n_cmt = 0
if not any(r.get("commitment_id") == "cmt_inami_sante_save_l5_2026" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_inami_sante_save_l5_2026",
            "title": "INAMI health care savings package L5 764.5m 2026",
            "entity_id": "riziv",
            "beneficiary": "Public finances / patients / providers / pharma",
            "legal_basis": "INAMI Conseil general + pluriannual pharma frame 17.3pct + programme measures",
            "decision_date": "2025-10-20",
            "start_year": "2026",
            "end_year": "2026",
            "total_envelope_eur": str(int(SANTE["total"] * 1e6)),
            "cash_by_year": json.dumps({"2026_m": SANTE, "coa_flags": [
                "drugs residual 148.9m still to design",
                "doctors 41.5m delay risk",
                "hospital linear advance = cash shift not real 2026 cut",
            ]}),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Contain health objective growth via drugs/fees/hospitals",
            "cut_option": "Deliver residual pharma list; avoid advance-shift theatre; dual prior cmt_inami_sante_2026",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": "SS>INAMI>sante_savings_l5_2026",
            "notes": f"CoA p84 full component L5; tick{TICK}",
        }
    )
    n_cmt += 1

if not any(r.get("commitment_id") == "cmt_nato_path_l5_2025_29" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_nato_path_l5_2025_29",
            "title": "NATO 2pct defence effort + financing multi-year L5 2025-2029",
            "entity_id": "mod_defensie",
            "beneficiary": "Defence / NATO accounting / dual pensions",
            "legal_basis": "CM 11 Apr 2025 Easter defence plan notification 31",
            "decision_date": "2025-04-11",
            "start_year": "2025",
            "end_year": "2029",
            "total_envelope_eur": str(int(sum(FIN["extra_spend_m"]) * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "effort_total_m": {str(y): NATO["effort_total_m"][i] for i, y in enumerate(YEARS)},
                    "need_2pct_m": {str(y): NATO["need_2pct_m"][i] for i, y in enumerate(YEARS)},
                    "s16_m": {str(y): NATO["s16_budget_m"][i] for i, y in enumerate(YEARS)},
                    "external_m": {str(y): NATO["external_m"][i] for i, y in enumerate(YEARS)},
                    "std_m": {str(y): NATO["std_total_m"][i] for i, y in enumerate(YEARS)},
                    "extra_spend_m": {str(y): FIN["extra_spend_m"][i] for i, y in enumerate(YEARS)},
                    "temp_fin_m": {str(y): FIN["temp_fin_m"][i] for i, y in enumerate(YEARS)},
                    "cit_russian_m": {str(y): FIN["cit_russian_m"][i] for i, y in enumerate(YEARS)},
                    "belfius_m": {str(y): FIN["belfius_m"][i] for i, y in enumerate(YEARS)},
                    "struct_total_m": {str(y): FIN["struct_total_m"][i] for i, y in enumerate(YEARS)},
                    "deficit_temp_m": {str(y): FIN["deficit_temp_m"][i] for i, y in enumerate(YEARS)},
                    "asset_optim_m": FIN["asset_optim_pack_m"],
                    "s16_share_pct": list(NATO["s16_share_pct"]),
                    "coa_flags": [
                        "COFOG classification not verified by CoA",
                        "standardisation circular still pending for 2027+",
                        "asset optim 3170m not detailed",
                    ],
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Meet NATO 2pct with controlled debt path",
            "cut_option": "Publish standardisation circular L5; asset optim FOI; dual capacity contracts",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Federal>Defence>NATO_2pct_l5",
            "notes": f"CoA p28-31 full multi-year; dual prior cmt_nato_*; tick{TICK}",
        }
    )
    n_cmt += 1

if not any(r.get("commitment_id") == "cmt_justice_sec_prov_l5_2026" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_justice_sec_prov_l5_2026",
            "title": "Justice + security/surpop provisions L5 2026",
            "entity_id": "fod_justice",
            "beneficiary": "Prisons / police / migration / Regie des batiments",
            "legal_basis": "CM Apr/Jul/Dec 2025; BOSA provisions 06.90",
            "decision_date": "2025-12-12",
            "start_year": "2026",
            "end_year": "2029",
            "total_envelope_eur": str(int(JUSTICE["surpop_envelope_2026_29"] * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "justice_section_2026_m": JUSTICE["section_credits_2026"],
                    "provisions_for_justice_2026_m": JUSTICE["provisions_for_justice_2026"],
                    "sec_prov_2026": SEC_PROV_2026,
                    "surpop_envelope_m": JUSTICE["surpop_envelope_2026_29"],
                    "surpop_infra_m": JUSTICE["surpop_infra_pack"],
                    "surpop_struct_m": JUSTICE["surpop_struct_pack"],
                    "tf_need_m": JUSTICE["tf_need_class"],
                    "tf_places_2026": JUSTICE["tf_capacity_places_2026"],
                    "tf_capacity_budget_2026_m": JUSTICE["tf_capacity_budget_2026"],
                    "coa_flags": [
                        "project list for 2026 provisions not available",
                        "specialty principle breached by BOSA provisions",
                        "TF needs 1.1bn vs envelope 840m gap",
                    ],
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Security reinforcement + prison overcrowding capacity",
            "cut_option": "Move known amounts into Justice section; publish project L5; dual TF 1.1bn",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Federal>Justice>provisions_surpop_security",
            "notes": f"CoA p59-60; dual cmt_prison_overcrowding; tick{TICK}",
        }
    )
    n_cmt += 1

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

# --- leaderboard ---
with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def add_lb(iid, name, annual, total, tco, conf, benef, goal, outcome, abs_s, cost_s, diff, prio, cut, notes, hpath, typ="policy"):
    if any(r.get("item_id") == iid for r in lb):
        return False
    lb.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": hpath,
            "annual_cost_eur": str(int(round(annual))),
            "total_cost_eur": str(int(round(total))),
            "tco_notes": tco,
            "confidence": conf,
            "source_id": SRC,
            "beneficiaries": benef,
            "stated_goal": goal,
            "measured_outcome": outcome,
            "absurdity_score": str(abs_s),
            "cost_score": str(cost_s),
            "difficulty": str(diff),
            "priority_index": str(prio),
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": notes,
        }
    )
    return True


n_lb = 0
rows = [
    (
        "lb_inami_sante_save_765m_l5",
        "INAMI health savings package 764.5m 2026 L5",
        764.5e6,
        764.5e6,
        "Strong CoA: drugs 401.9 doctors 213.2 hosp 50 other 73.8 TM-res 25.6; residual design 148.9; hosp cash-shift flag",
        "medium",
        "Patients providers pharma hospitals",
        "Contain AMI health objective",
        "Delivery risk on residual pharma + doctor delay 41.5m",
        5.0,
        8.0,
        6,
        6.5,
        "Publish residual 148.9 measures; no advance-shift theatre",
        f"tick{TICK}",
        "SS>INAMI>sante_savings_l5",
    ),
    (
        "lb_inami_drugs_402m_l5",
        "INAMI pharma savings 401.9m L5 (residual 148.9 design)",
        401.9e6,
        401.9e6,
        "Strong: price 80.3 antiacid 65.8 lipid 29.4 partial-bill 42 TM 27.9 proposed 252.9 residual 148.9; 17.3pct frame",
        "medium",
        "Pharma industry / patients / hospitals",
        "Cap drugs at 17.3pct of health objective",
        "Most proposed measures still need regulation",
        5.5,
        7.5,
        6,
        6.5,
        "Legislate residual before booking full 401.9",
        f"tick{TICK}",
        "SS>INAMI>pharma_l5",
    ),
    (
        "lb_inami_doctors_213m_l5",
        "INAMI physician-fee savings 213.2m (lab/imaging/surgery)",
        213.2e6,
        213.2e6,
        "Strong CoA: lab 70.8 imaging 68.5 surgery 63.7; INAMI delay risk 41.5m not realized 2026",
        "medium",
        "Physicians labs imaging surgery",
        "Rationalise high-volume medical acts",
        "Late legal entry cuts delivery",
        4.5,
        7.0,
        6,
        6.0,
        "Pass fee rules early; publish act-volume baselines",
        f"tick{TICK}",
        "SS>INAMI>doctors_fees_l5",
    ),
    (
        "lb_nato_extra_16_8bn_path",
        "Defence extra spend package 16.78bn 2025-29 L5 path",
        3522e6,
        16783e6,
        "Strong CoA: 3866/3522/3222/3099/3074; temp 7.15 + struct 4.83 + deficit 4.80; asset optim 3.17 open",
        "strong",
        "Defence / taxpayers",
        "Reach and hold NATO 2pct",
        "S16 share falls 82.4→79.7pct as standardisation grows",
        3.0,
        9.5,
        7,
        6.8,
        "Publish capacity contracts; open asset optim; dual pensions",
        f"tick{TICK}",
        "Federal>Defence>extra_spend_path",
    ),
    (
        "lb_nato_std_path_750m",
        "Defence standardisation path to 750m 2029 (circular pending)",
        167.5e6,
        sum(NATO["std_total_m"]) * 1e6,
        "Medium: 167.5 flat miliciens 25-26 then 300/500/750; new-to-std 0/0/132.5/332.5/582.5; circular not ready",
        "medium",
        "Other depts reclassified as defence COFOG 02",
        "Count existing spend toward NATO without new cash",
        "CoA did not verify COFOG classification",
        7.0,
        7.0,
        6,
        6.7,
        "Publish circular named lines; independent COFOG audit",
        f"tick{TICK}",
        "Federal>Defence>standardisation",
    ),
    (
        "lb_nato_cit_russian_path",
        "CIT on frozen Russian asset interest path ~6.15bn 2025-29",
        1163e6,
        sum(FIN["cit_russian_m"]) * 1e6,
        "Medium: 1208/1163/1217/1269/1297 temp defence finance; legal/geopolitical risk if stream ends",
        "medium",
        "Defence budget via frozen-asset interest CIT",
        "Temporary non-debt defence financing",
        "Gov will raise structural if stream dies",
        5.5,
        8.5,
        7,
        7.1,
        "Stress-test structural backfill; dual Belfius 1bn",
        f"tick{TICK}",
        "Federal>Defence>cit_russian_fin",
    ),
    (
        "lb_nato_asset_optim_3_17bn",
        "Defence-linked asset optimisation package 3.17bn (opaque)",
        3170e6,
        3170e6,
        "Medium CoA: ~2/3 of temp deficit 4.8bn; public holdings ops still undefined; FOI residual",
        "medium",
        "Public holdings / debt path",
        "Limit debt impact of defence deficit",
        "Several tracks still under study per Budget cell",
        7.5,
        8.0,
        8,
        7.8,
        "Publish named asset plan; no silent equity sales",
        f"tick{TICK}",
        "Federal>Defence>asset_optimisation",
    ),
    (
        "lb_justice_provisions_466m",
        "Justice via BOSA provisions 465.5m 2026 (specialty breach)",
        465.5e6,
        465.5e6,
        "Strong CoA: security 112.5 + surpop ops 50 + infra 259 + efficiency 44; project list unknown; dual section 2843m",
        "strong",
        "Prisons justice system Regie",
        "Finance justice via flexible interdept provisions",
        "CoA: specialty principle violated; progressive reintegration planned",
        7.0,
        7.5,
        5,
        6.7,
        "Inscribe in Justice section; publish 2026 project L5",
        f"tick{TICK}",
        "Federal>Justice>bosa_provisions",
    ),
    (
        "lb_surpop_envelope_840m_gap",
        "Prison overcrowding envelope 840m vs TF need 1.1bn",
        259e6,
        840e6,
        "Strong: 600 infra + 240 struct 2026-29; TF need ~1.1bn; 1052 places/303.8m 2026 class; project list FOI",
        "strong",
        "Detainees / Regie / Justice",
        "Reduce prison overcrowding",
        "Envelope short vs TF; carry unused years",
        5.5,
        8.0,
        6,
        6.7,
        "Close TF gap; name projects; dual DBFM prisons",
        f"tick{TICK}",
        "Federal>Justice>surpop_envelope",
    ),
    (
        "lb_sec_prov_367m_2026",
        "Security/return interdept provision 366.9m 2026 L5",
        366.9e6,
        366.9e6,
        "Strong: 250 reinforce + 60 surpop + 6.2 carry + 50.7 opaque (J44+I6); annuality breach CoA",
        "strong",
        "Justice police migration",
        "Security reinforcement and returns policy",
        "Opaque 50.7m purpose; multi-year carry allowed",
        6.5,
        7.0,
        5,
        6.4,
        "Split known lines to sections; explain +50.7",
        f"tick{TICK}",
        "Federal>BOSA>provision_securite",
    ),
]
for args in rows:
    if add_lb(*args):
        n_lb += 1

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

# --- research_queue ---
with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())

for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: INAMI sante L5 764.5 (drugs 401.9 residual 148.9) + NATO multi-year "
            f"effort/financing L5 + Justice/security provisions 466/367; rq_116 deferred"
        )

if not any(r.get("task_id") == "rq_429" for r in rq):
    rq.append(
        {
            "task_id": "rq_429",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": "",
            "notes": f"Spawned tick{TICK} after sante/NATO/Justice L5; rq_116 SWA deferred",
        }
    )

with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

# --- loop_state ---
with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsf = list(ls[0].keys())
ls[-1]["last_tick_utc"] = NOW
ls[-1]["last_unit_id"] = UNIT
ls[-1]["ticks_completed"] = str(TICK)
ls[-1]["mode"] = "continuous"
ls[-1]["current_sprint"] = "hole_fill"
ls[-1]["paused"] = "no"
ls[-1]["notes"] = (
    f"Scheduler 60s. Next prio5 rq_429; rq_116 SWA deferred. "
    f"tick{TICK} sante 765 L5 + NATO path + Justice prov."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **INAMI sante L5 + NATO multi-year + Justice/security provisions**)
- Found (strong/medium primary Cour des comptes Budget Etat 2026 p28-31 + p59-60 + p84):
  - **INAMI health save 764.5m 2026 L5:** drugs **401.9** (price 80.3 · antiacid 65.8 · lipid 29.4 · partial-bill 42 · TM 27.9 · residual design **148.9**) · doctors **213.2** (lab 70.8 · imaging 68.5 · surgery 63.7 · delay risk **41.5**) · hosp **50** (day 47.1 cash-shift flag) · other **73.8** · TM-res **25.6**
  - **NATO multi-year 2025-29:** effort **12.73→14.29bn** (~100% of 2pct need); s16 share **82.4→79.7%**; std **167.5→750m**
    - Extra spend **3.87→3.07bn/yr** sum **16.78bn**; temp fin **7.15** (CIT Russian **6.15** + Belfius **1.0**); struct **4.83**; deficit temp **4.80**; asset optim **3.17** (opaque)
  - **Security provision 366.9m:** reinforce **250** (J112.5 police87.5 mig50) · surpop **60** · carry **6.2** · opaque **50.7** (J44+I6)
  - **Justice:** section **2.843bn** + BOSA provisions **465.5m** (specialty breach); surpop envelope **840m** (600 infra + 240 struct) vs TF need **~1.1bn**; TF capacity **1052 places / 303.8m** 2026 class
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_428=done; spawn **rq_429**; ticks={TICK}
- FOI: none new (asset optim + surpop project list already covered by prior gaps/design residual)
- Next: prio5 **rq_429**; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log_entry.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")

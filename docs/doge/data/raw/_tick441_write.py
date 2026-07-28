# tick 441: DGD AR 2025 ODA L5 deepen (channels + top20 + themes + named programmes)
import csv
import json
import shutil
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
RAW = DATA / "raw"
NOW = "2026-08-02T11:15:00Z"
TICK = 441
UNIT = "rq_432"
SRC = "src_dgd_ar_2025_l5_tick441"
URL = "https://openaid.be/sites/default/files/2026-06/Annual%20Report%20DGD%202025%20ENG.pdf"

# Copy PDF to raw if not present
src_pdf = Path(
    r"C:\Users\karel\.grok\sessions\C%3A%5CUsers%5Ckarel%5Cdev%5CAIpolitics"
    r"\019fa677-56cb-7a13-9419-1769b5970459\downloads\1.pdf"
)
dst = RAW / "dgd_ar_2025_en.pdf"
if src_pdf.exists() and not dst.exists():
    shutil.copy2(src_pdf, dst)

# Totals multi-year (m EUR) — AR table p50-51
TOTAL = {2023: 1285.90, 2024: 1440.92, 2025: 1117.97}
CUT_2025 = 106.0  # budget cut year1
CUT_FROM_UNDERUSE = 90.0  # of which under-utilisation/multilateral review >90m

# Theme split 2025 figure p6 (m EUR) — provisional
THEMES_2025 = {
    "climate": 365.3,  # 32.5%
    "stability": 301.8,  # 26.9%
    "other_skills_edu": 181.5,  # 16.2%
    "humanitarian": 175.0,  # 15.6% figure; dual table 170.00
    "health": 98.8,  # 8.8%
}
# sum = 1122.4 ~ total 1117.97 provisional

# Channel L5 2025 (m EUR) from p50-51 table
CHANNEL_2025 = {
    "enabel_agency": 212.02,
    "consolidation_society_governance": 7.20,
    "enabel_management": 25.57,
    "state_to_state_loans": 5.57,
    "gov_subtotal": 250.35,
    "ngo_federations": 207.78,  # program-based finance federations class
    "ngo_other": 8.58,
    "institutional_actors": 23.05,
    "scientific_institutions": 8.01,
    "nongov_subtotal": 247.41,
    "multilateral_mandatory": 199.97,
    "multilateral_voluntary": 26.85,
    "edf_eib": 24.40,
    "world_bank_group": 6.69,
    "multilateral_subtotal": 257.91,
    "humanitarian_programmes": 170.00,
    "climate_policy": 102.18,
    "awareness_belgium": 1.99,
    "admin_eval_other": 1.92,
}

# Top 20 recipients 2025 (m EUR) p49 exact table
TOP20 = {
    "DRC": 104.49,
    "Burkina_Faso": 28.02,
    "Uganda": 27.80,
    "Burundi": 27.18,
    "Niger": 26.29,
    "Palestine": 24.71,
    "Senegal": 20.06,
    "Ukraine": 18.16,
    "Benin": 17.82,
    "Mali": 14.59,
    "Tanzania": 10.73,
    "Guinea": 10.71,
    "Morocco": 10.65,
    "Mozambique": 6.95,
    "Peru": 4.07,
    "Ecuador": 3.92,
    "Rwanda": 3.62,
    "Cambodia": 3.48,
    "Bolivia": 3.43,
    "Philippines": 3.06,
}
TOP20_SUM = sum(TOP20.values())

# Named programme L5 2025
NAMED = {
    "ldcf_2025": 18.5,  # 2nd largest donor LDCF
    "cgiar_2025": 9.3,
    "sahel_climate_enabel": 50.0,  # multi-year programme invest via Enabel
    "mrna_htap_4y": 8.0,  # over four years; >60% mRNA/HTAP
    "bio_approvals_2025": 240.0,  # AR says 240m / 30 projects (dual prior 235m)
}

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "DGD Annual Report 2025 ODA L5 channels themes top20 named programmes",
            "url": URL,
            "publisher": "DGD FPS Foreign Affairs",
            "accessed_date": "2026-08-02",
            "source_class": "official_annual_report",
            "notes": (
                f"p6 themes; p49 top20; p50-51 channel matrix; LDCF 18.5 CGIAR 9.3 "
                f"Sahel Climate 50 mRNA 8/4y; cut 106 of which >90 underuse; tick{TICK}"
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

for y, v in TOTAL.items():
    if add_bud(
        f"bud_dgd_total_l5_{y}",
        "dgd",
        y,
        v * 1e6,
        "outturn",
        f"DGD total ODA {v}m {y} AR 2025 figures table (provisional); dual prior totals; tick{TICK}",
        "strong",
    ):
        n_bud += 1

if add_bud(
    "bud_dgd_cut_2025",
    "dgd",
    2025,
    CUT_2025 * 1e6,
    "outturn",
    (
        f"DGD budget cut {CUT_2025}m 2025 year1 of -25pct path to 2027; "
        f">={CUT_FROM_UNDERUSE}m from under-utilisation + multilateral review CoA dual; tick{TICK}"
    ),
    "strong",
):
    n_bud += 1

for key, v in THEMES_2025.items():
    conf = "medium" if key == "humanitarian" else "strong"
    note = f"DGD theme {key} {v}m 2025 AR figure p6 (provisional; sum~1122 vs total 1118); tick{TICK}"
    if key == "humanitarian":
        note += " dual table channel 170m"
    if add_bud(
        f"bud_dgd_theme_{key}_2025",
        "dgd",
        2025,
        v * 1e6,
        "outturn",
        note,
        conf,
    ):
        n_bud += 1

for key, v in CHANNEL_2025.items():
    if add_bud(
        f"bud_dgd_ch_{key}_2025",
        "dgd" if "enabel" not in key else "enabel",
        2025,
        v * 1e6,
        "outturn",
        f"DGD channel L5 {key} {v}m 2025 AR p50-51; dual prior enabel/hum lines; tick{TICK}",
        "strong",
    ):
        n_bud += 1

for ctry, v in TOP20.items():
    if add_bud(
        f"bud_dgd_recipient_{ctry}_2025",
        "dgd",
        2025,
        v * 1e6,
        "outturn",
        f"DGD top20 recipient {ctry} {v}m 2025 AR p49; country envelope not project L5; tick{TICK}",
        "strong",
    ):
        n_bud += 1

if add_bud(
    "bud_dgd_top20_sum_2025",
    "dgd",
    2025,
    TOP20_SUM * 1e6,
    "derived",
    f"DGD top20 recipients sum {TOP20_SUM:.2f}m of total 1117.97m (~{100*TOP20_SUM/1117.97:.1f}pct) 2025; tick{TICK}",
    "strong",
):
    n_bud += 1

if add_bud(
    "bud_dgd_ldcf_2025",
    "dgd",
    2025,
    NAMED["ldcf_2025"] * 1e6,
    "outturn",
    f"Belgium LDCF contribution {NAMED['ldcf_2025']}m 2025 (2nd largest donor) AR p8; tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_dgd_cgiar_2025",
    "dgd",
    2025,
    NAMED["cgiar_2025"] * 1e6,
    "outturn",
    f"CGIAR agricultural research support {NAMED['cgiar_2025']}m 2025 AR p10; tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_dgd_sahel_climate_enabel",
    "enabel",
    2025,
    NAMED["sahel_climate_enabel"] * 1e6,
    "commitment",
    (
        f"Sahel Climate programme via Enabel {NAMED['sahel_climate_enabel']}m envelope AR p11 "
        f"(agroecology women/youth; multi-year class); tick{TICK}"
    ),
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_dgd_mrna_htap_4y",
    "dgd",
    2025,
    NAMED["mrna_htap_4y"] * 1e6,
    "commitment",
    (
        f"mRNA tech transfer + HTAP Belgium commitment {NAMED['mrna_htap_4y']}m over 4 years "
        f"(>60pct mRNA/HTAP) AR p13; tick{TICK}"
    ),
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_bio_approvals_2025_ar",
    "bio_invest",
    2025,
    NAMED["bio_approvals_2025"] * 1e6,
    "commitment",
    (
        f"BIO approvals {NAMED['bio_approvals_2025']}m / 30 projects 2025 DGD AR p15 "
        f"(dual prior AR financials 235m); tick{TICK}"
    ),
    "strong",
):
    n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

# commitments
with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())

n_cmt = 0
if not any(r.get("commitment_id") == "cmt_dgd_l5_2025_deep" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_dgd_l5_2025_deep",
            "title": "DGD ODA 2025 L5 channels themes top20 + named programmes",
            "entity_id": "dgd",
            "beneficiary": "Partner countries / Enabel / NGOs / multilaterals / BIO",
            "legal_basis": "DGD annual report 2025; Arizona -25pct path; Openaid provisional",
            "decision_date": "2025-01-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(int(TOTAL[2025] * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "total_m": TOTAL,
                    "cut_2025_m": CUT_2025,
                    "cut_underuse_m": CUT_FROM_UNDERUSE,
                    "themes_2025_m": THEMES_2025,
                    "channels_2025_m": CHANNEL_2025,
                    "top20_2025_m": TOP20,
                    "top20_sum_m": TOP20_SUM,
                    "named_m": NAMED,
                    "note": "Country envelopes public; end-project L5 residual FOI gap_dgd_l5_projects",
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "ODA climate/health/stability focus under -25pct budget path",
            "cut_option": "Publish Openaid project CSV; protect humanitarian; track under-use vs outcome",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Federal>DGD>ODA_l5_2025",
            "notes": f"AR 2025 deep L5; dual cmt_dgd_oda_path; tick{TICK}",
        }
    )
    n_cmt += 1

# update FOI gap note
with open(DATA / "foi_queue.csv", encoding="utf-8", newline="") as f:
    foi = list(csv.DictReader(f))
    ff = list(foi[0].keys())
for r in foi:
    if r.get("gap_id") == "gap_dgd_l5_projects":
        r["updated_utc"] = NOW
        r["notes"] = (
            (r.get("notes") or "")
            + f" | tick{TICK}: channel+theme+top20+named (LDCF/CGIAR/Sahel/mRNA) public; residual project-level still ready"
        )
with open(DATA / "foi_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ff, extrasaction="ignore")
    w.writeheader()
    w.writerows(foi)

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

# leaderboard
with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def add_lb(iid, name, annual, total, tco, conf, benef, goal, outcome, abs_s, cost_s, diff, prio, cut, notes, hpath, typ="programme"):
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
        "lb_dgd_channel_gov_250m",
        "DGD governmental cooperation subtotal 250.4m 2025",
        250.35e6,
        250.35e6,
        "Strong AR: Enabel 212 + mgmt 25.6 + governance 7.2 + state loans 5.6 = 250.4; dual Enabel turnover 407m multi-donor",
        "strong",
        "Enabel partner institutions",
        "Governmental bilateral implementation",
        "Core channel under -25pct path",
        3.0,
        7.0,
        4,
        5.2,
        "Reconcile DGD line vs Enabel omzet; open project L5",
        f"tick{TICK}",
        "Federal>DGD>gov_channel",
    ),
    (
        "lb_dgd_channel_nongov_247m",
        "DGD non-governmental programme finance 247.4m 2025",
        247.41e6,
        247.41e6,
        "Strong AR: federations 207.8 + NGO 8.6 + institutional 23.1 + scientific 8.0",
        "strong",
        "Belgian NGO federations institutional actors",
        "Civil society programme-based finance",
        "Largest non-Enabel domestic implementer block",
        4.0,
        7.0,
        5,
        5.6,
        "Publish federation ranking EUR; dual dual APEFE",
        f"tick{TICK}",
        "Federal>DGD>nongov_channel",
    ),
    (
        "lb_dgd_channel_multi_258m",
        "DGD multilateral cooperation 257.9m 2025",
        257.91e6,
        257.91e6,
        "Strong AR: mandatory 200 + voluntary 26.9 + EDF/EIB 24.4 + WB 6.7; voluntary refocus OHCHR/WHO/UNFPA/UN Women/IOM/UNEP",
        "strong",
        "UN/EU/IFIs",
        "Multilateral core + voluntary contributions",
        "GFATM/UNICEF/UNDP/GPE etc adjusted or held",
        3.5,
        7.0,
        4,
        5.3,
        "Publish hold-list amounts; dual climate LDCF",
        f"tick{TICK}",
        "Federal>DGD>multilateral",
    ),
    (
        "lb_dgd_theme_climate_365m",
        "DGD climate theme 365.3m 32.5pct 2025",
        365.3e6,
        365.3e6,
        "Strong AR figure: largest theme; dual climate policy channel 102m + broader portfolio",
        "strong",
        "LDCs partner climate adaptation",
        "Climate as global public good priority",
        "LDCF 18.5m second-largest donor class",
        3.0,
        7.5,
        4,
        5.5,
        "Track adaptation vs mitigation split L5",
        f"tick{TICK}",
        "Federal>DGD>theme_climate",
    ),
    (
        "lb_dgd_ldcf_18_5m",
        "LDCF contribution 18.5m 2025 (2nd largest donor)",
        18.5e6,
        18.5e6,
        "Strong AR p8 named multilateral climate fund line",
        "strong",
        "Least developed countries climate adaptation",
        "LDC Fund UNFCCC adaptation",
        "437 projects / 83.9m people fund-level outcomes",
        2.5,
        4.5,
        3,
        3.8,
        "Keep core climate multilateral",
        f"tick{TICK}",
        "Federal>DGD>LDCF",
    ),
    (
        "lb_dgd_sahel_climate_50m",
        "Sahel Climate Enabel programme 50m envelope",
        50e6,
        50e6,
        "Medium AR: 50m via Enabel agroecology women/youth; multi-year class not single-year cash",
        "medium",
        "Sahel women youth farmers",
        "Agroecology and climate resilience Sahel",
        "600 women groups supported class (outcome narrative)",
        3.5,
        5.5,
        5,
        4.7,
        "Publish cash-by-year and KPI; dual Enabel portfolio",
        f"tick{TICK}",
        "Federal>Enabel>Sahel_Climate",
    ),
    (
        "lb_dgd_cgiar_9_3m",
        "CGIAR support 9.3m 2025",
        9.3e6,
        9.3e6,
        "Strong AR p10 agricultural research network",
        "strong",
        "Farmers via CGIAR innovations",
        "Sustainable food systems / climate-smart agriculture",
        "Fund-level 20m farmers 2022-24 narrative",
        2.5,
        3.5,
        3,
        3.3,
        "Outcome attribution residual",
        f"tick{TICK}",
        "Federal>DGD>CGIAR",
    ),
    (
        "lb_dgd_top20_concentration",
        f"DGD top20 recipients {TOP20_SUM:.0f}m (~{100*TOP20_SUM/1117.97:.0f}pct of total)",
        TOP20_SUM * 1e6,
        TOP20_SUM * 1e6,
        f"Strong AR p49: top20 sum {TOP20_SUM:.2f}m of 1117.97; DRC 104.5 alone ~9.3pct",
        "strong",
        "Top partner countries",
        "Geographic concentration of bilateral ODA",
        "DRC largest; Rwanda interruption residual class",
        4.0,
        8.0,
        5,
        6.1,
        "FOI project L5 inside country envelopes",
        f"tick{TICK}",
        "Federal>DGD>top20_concentration",
    ),
    (
        "lb_dgd_cut_underuse_90m",
        "DGD 2025 cut 106m of which >90m under-utilisation path",
        106e6,
        106e6,
        "Strong AR: cut from under-use of programmes + multilateral review >90m; first year -25pct path",
        "strong",
        "Federal budget / ODA partners",
        "Deliver Arizona -25pct structural cut by 2027",
        "Not pure waste; delivery/commitment timing",
        5.0,
        6.0,
        4,
        5.3,
        "Publish which multilaterals held; dual coop liq path",
        f"tick{TICK}",
        "Federal>DGD>cut_2025",
    ),
    (
        "lb_bio_approvals_240m_2025",
        "BIO approvals 240m / 30 projects 2025 (DGD AR)",
        240e6,
        240e6,
        "Strong DGD AR 240m dual financial AR 235m; Biophyto Benin example dual Enabel/Kampani",
        "strong",
        "Developing-country private sector",
        "DFI private-sector scale-up",
        "Ecosystem Enabel→Kampani→BIO narrative",
        3.5,
        7.0,
        5,
        5.4,
        "Publish L5 investees; dual gap_bio_l5_portfolio",
        f"tick{TICK}",
        "Federal>BIO>approvals_2025",
    ),
]
for args in rows:
    if add_lb(*args):
        n_lb += 1

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

# research_queue
with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())
for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: DGD AR2025 L5 deep (channels gov250/nongov247/multi258; themes climate365; "
            f"top20; LDCF18.5 CGIAR9.3 Sahel50); gap_dgd residual project; rq_116 deferred"
        )
if not any(r.get("task_id") == "rq_433" for r in rq):
    rq.append(
        {
            "task_id": "rq_433",
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
            "notes": f"Spawned tick{TICK} after DGD L5 deep; rq_116 SWA deferred",
        }
    )
with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

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
    f"Scheduler 60s. Next prio5 rq_433; rq_116 SWA deferred. "
    f"tick{TICK} DGD ODA L5 channels+top20+named."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **DGD AR 2025 ODA L5 channels/themes/top20/named**)
- Found (strong primary DGD Annual Report 2025 ENG, provisional):
  - **Total DGD:** **€1,117.97m 2025** (vs 1,440.92 2024 / 1,285.90 2023); cut **€106m** of which **≥€90m** under-use + multi review
  - **Themes 2025:** climate **365.3** (32.5%) · stability **301.8** · other **181.5** · humanitarian **175** (dual table **170**) · health **98.8**
  - **Channels 2025:** gov **250.4** (Enabel **212.0** + mgmt **25.6** + gov **7.2** + loans **5.6**) · nongov **247.4** · multi **257.9** · hum **170** · climate policy **102.2**
  - **Top20 sum €{TOP20_SUM:.1f}m** (~{100*TOP20_SUM/1117.97:.0f}%); DRC **104.49** largest
  - **Named:** LDCF **18.5m** (2nd donor) · CGIAR **9.3m** · Sahel Climate Enabel **50m** · mRNA/HTAP **8m/4y** · BIO approvals **240m**/30 projects
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; foi gap_dgd note; rq_432=done; spawn **rq_433**; ticks={TICK}
- FOI: gap_dgd_l5_projects residual narrowed (project-level still ready human send)
- Next: prio5 **rq_433**; deferred **rq_116** SWA
"""
with open(Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md"), "ab") as f:
    f.write(log.encode("utf-8"))

print(f"OK tick{TICK} bud+{n_bud} cmt+{n_cmt} lb+{n_lb} top20={TOP20_SUM:.2f}")

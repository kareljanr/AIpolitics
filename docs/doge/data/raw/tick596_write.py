# tick 596 — Flanders Make dual SOC hole-fill
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
tick = "tick596"
utc = "2026-07-31T14:45:00Z"

# --- entities ---
with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "flanders_make,Flanders Make,Flanders Make,"
        "Flanders strategic research centre manufacturing innovation dual imec VIB VITO,"
        "parastatal,sec_flanders,nl,https://www.flandersmake.be,,,"
        "SOC vzw BE0860.286.268 Lommel; rev 37.3m turnover 33.2m convenant 20.9m personnel 24.3m "
        "profit 1.55m assets 234.7m cash 131.4m equity 26.0m creditors 208.6m 2025; "
        "ecosystem rev 134m researchers 1100 members 210; dual imec VIB VITO SOC; tick596\n"
    )

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_flanders_make_ar_2025,Flanders Make Activity Report 2025 balance P and L,"
        "https://www.flandersmake.be/en/about-us/activity-report-2025,Flanders Make SOC vzw,"
        "2026-07-31,official_annual_report,"
        "Strong tick596: rev 37325k turnover 33220k (convenant 20876 non-conv 10980 membership 1364) "
        "other 4105; costs 37134k salaries 24319 op 12440; op result 191k fin 1710k tax 356k profit 1545k; "
        "assets 234739k equity 26028 cash 131396 creditors 208648; ecosystem rev 134m researchers 1100 "
        "members 210 projects 1200; dual imec VIB VITO; raw flanders_make_balans_2025.jpeg\n"
    )
    f.write(
        "src_dual_soc_fm_imec_vib_vito_tick596,"
        "Dual Flanders SOC quartet Flanders Make imec VIB VITO 2024-25,"
        "docs/doge/raw/flanders_make_balans_2025.jpeg,DOGE synthesis FM AR2025 + prior SOC,"
        "2026-07-31,synthesis,"
        "Strong dual: FM rev 37.3m convenant 20.9m personnel 24.3m assets 235m vs imec 1.22bn "
        "VIB 169m VITO 297m; manufacturing SOC smallest of quartet; tick596\n"
    )

# --- budgets ---
bud_rows = [
    ("bud_fm_revenues_2025", 37325000, "Flanders Make total revenues 37.325m 2025; tick596", "strong"),
    ("bud_fm_turnover_2025", 33220000, "Flanders Make turnover 33.220m 2025; tick596", "strong"),
    ("bud_fm_convenant_2025", 20876000, "Flanders Make FM convenant revenue 20.876m 2025 (VL structural path); tick596", "strong"),
    ("bud_fm_non_convenant_2025", 10980000, "Flanders Make FM non-convenant revenue 10.980m 2025; tick596", "strong"),
    ("bud_fm_membership_2025", 1364000, "Flanders Make membership fees and other revenues 1.364m 2025; tick596", "strong"),
    ("bud_fm_other_rev_2025", 4105000, "Flanders Make other revenue 4.105m 2025; tick596", "strong"),
    ("bud_fm_costs_2025", 37134000, "Flanders Make total costs 37.134m 2025; tick596", "strong"),
    ("bud_fm_personnel_2025", 24319000, "Flanders Make salaries and social security 24.319m 2025; tick596", "strong"),
    ("bud_fm_op_costs_2025", 12440000, "Flanders Make operating costs 12.440m 2025; tick596", "strong"),
    ("bud_fm_other_costs_2025", 375000, "Flanders Make other costs 0.375m 2025; tick596", "strong"),
    ("bud_fm_op_result_2025", 191000, "Flanders Make operating result 0.191m 2025; tick596", "strong"),
    ("bud_fm_fin_result_2025", 1710000, "Flanders Make financial and exceptional result 1.710m 2025; tick596", "strong"),
    ("bud_fm_profit_bt_2025", 1901000, "Flanders Make profit before tax 1.901m 2025; tick596", "strong"),
    ("bud_fm_tax_2025", 356000, "Flanders Make tax on result 0.356m 2025; tick596", "strong"),
    ("bud_fm_profit_2025", 1545000, "Flanders Make profit to appropriate 1.545m 2025; tick596", "strong"),
    ("bud_fm_assets_2025", 234739000, "Flanders Make total assets 234.739m 2025; tick596", "strong"),
    ("bud_fm_fixed_assets_2025", 31938000, "Flanders Make fixed assets 31.938m 2025; tick596", "strong"),
    ("bud_fm_tangible_2025", 28543000, "Flanders Make tangible assets 28.543m 2025; tick596", "strong"),
    ("bud_fm_current_assets_2025", 202801000, "Flanders Make current assets 202.801m 2025; tick596", "strong"),
    ("bud_fm_stocks_2025", 42818000, "Flanders Make stocks and orders 42.818m 2025; tick596", "strong"),
    ("bud_fm_receivables_2025", 27072000, "Flanders Make accounts receivable within 1y 27.072m 2025; tick596", "strong"),
    ("bud_fm_cash_2025", 131396000, "Flanders Make cash at bank and in hand 131.396m 2025; tick596", "strong"),
    ("bud_fm_equity_2025", 26028000, "Flanders Make capital and reserves 26.028m 2025; tick596", "strong"),
    ("bud_fm_creditors_2025", 208648000, "Flanders Make creditors total 208.648m 2025; tick596", "strong"),
    ("bud_fm_creditors_lt_2025", 16459000, "Flanders Make creditors after 1 year 16.459m 2025; tick596", "strong"),
    ("bud_fm_creditors_st_2025", 105621000, "Flanders Make creditors within 1 year 105.621m 2025; tick596", "strong"),
    ("bud_fm_reg_liab_2025", 86568000, "Flanders Make liabilities regularisation accounts 86.568m 2025; tick596", "strong"),
    (
        "bud_fm_ecosystem_rev_2025",
        134000000,
        "Flanders Make ecosystem revenue 134m 2025 (AR numbers graphic; not statutory perimeter); tick596",
        "medium",
    ),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, amt, note, conf in bud_rows:
        f.write(
            f"{bid},flanders_make,2025,{amt},,,outturn,src_flanders_make_ar_2025,{conf},{note}\n"
        )

# --- commitments ---
import json

cmt_fm = {
    "2025_revenues": 37325000,
    "2025_turnover": 33220000,
    "2025_convenant": 20876000,
    "2025_non_convenant": 10980000,
    "2025_personnel": 24319000,
    "2025_profit": 1545000,
    "2025_assets": 234739000,
    "2025_equity": 26028000,
    "2025_cash": 131396000,
    "2025_creditors": 208648000,
    "ecosystem_rev_m": 134,
    "researchers": 1100,
    "members": 210,
    "note": "VL convenant core; dual imec VIB VITO manufacturing SOC",
}
cmt_dual = {
    "fm_rev_m": 37.3,
    "fm_convenant_m": 20.9,
    "fm_personnel_m": 24.3,
    "fm_assets_m": 234.7,
    "imec_op_income_m": 1216.9,
    "vib_op_income_m": 168.8,
    "vito_inkomsten_m": 297.1,
    "note": "Quartet Flanders SOC dual map manufacturing nano life sciences sustainability",
}

def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')

with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_flanders_make_ar_2025,Flanders Make manufacturing dual imec VIB VITO SOC 2025,'
        f'flanders_make,Flanders industry universities members,'
        f'VL FM convenant + non-convenant project + membership,'
        f'2025-01-01,2025,2030,37325000,"{esc_json(cmt_fm)}",0,active,'
        f'https://www.flandersmake.be,Industrial innovation manufacturing RTO,'
        f'Publish multi-year convenant L5 + NBB full FOI residual,src_flanders_make_ar_2025,strong,'
        f'Vlaanderen>Science_Mfg>Flanders_Make,tick596 AR2025 primary new entity\n'
    )
    f.write(
        f'cmt_dual_soc_fm_imec_vib_vito_2025,Dual Flanders SOC quartet FM imec VIB VITO 2024-25,'
        f'gg_belgium,Flanders strategic research ecosystem,'
        f'FM AR2025 + imec FS2025 + VIB AR2024 + VITO Impact2024,'
        f'2024-01-01,2024,2025,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map quartet Flanders strategic research centres,'
        f'FOI VL grant L5 all four residual,src_dual_soc_fm_imec_vib_vito_tick596,strong,'
        f'BE>dual>SOC_FM_imec_VIB_VITO,tick596\n'
    )

# --- leaderboard ---
# cols: id,title,jurisdiction,category,hierarchy_path,annual_eur,stock_eur,absurdity_note,confidence,source_id,
# spenders,stated_purpose,mechanism_or_waste_angle,priority_score,scale_score,opacity_score,priority_index,
# reform_hook,status,notes,seed_tick
lb = [
    (
        "lb_fm_revenues_37m_2025",
        "Flanders Make revenues 37.3m turnover 33.2m 2025 dual SOC",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Mfg>FM>revenues_37m",
        37325000,
        234739000,
        "Strong AR2025: rev 37.3m turnover 33.2m convenant 20.9m personnel 24.3m profit 1.55m assets 235m dual imec VIB VITO",
        "src_flanders_make_ar_2025",
        "VL manufacturing SOC",
        "Public manufacturing RTO",
        "Core public science not pure waste; VL convenant heavy",
        3,
        7.5,
        4,
        5.50,
        "Publish convenant L5 FOI",
    ),
    (
        "lb_fm_convenant_21m_2025",
        "Flanders Make VL convenant 20.9m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Mfg>FM>convenant_21m",
        20876000,
        20876000,
        "Strong: FM convenant 20.876m 56pct of rev; VL structural core manufacturing SOC",
        "src_flanders_make_ar_2025",
        "VL taxpayers",
        "Fund manufacturing excellence",
        "Grant intensity dual SOCs",
        4,
        7.0,
        4,
        5.25,
        "Multi-year convenant FOI",
    ),
    (
        "lb_fm_personnel_24m_2025",
        "Flanders Make personnel 24.3m salaries SS 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Mfg>FM>personnel_24m",
        24319000,
        24319000,
        "Strong: salaries SS 24.319m of costs 37.1m; dual imec 426m VIB 93m VITO 129m",
        "src_flanders_make_ar_2025",
        "FM staff",
        "Operate research labs industry projects",
        "Core ops dual SOC FTE",
        3,
        7.0,
        3,
        5.05,
        "Benchmark dual SOC FTE",
    ),
    (
        "lb_fm_assets_235m_2025",
        "Flanders Make assets 234.7m cash 131.4m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Mfg>FM>assets_235m",
        0,
        234739000,
        "Strong: assets 234.7m cash 131.4m creditors 208.6m equity 26.0m stock orders 42.8m",
        "src_flanders_make_ar_2025",
        "FM",
        "Finance research projects deferred income",
        "Stock cash/creditors material",
        3,
        6.5,
        4,
        4.85,
        "Balance L5 FOI residual",
    ),
    (
        "lb_fm_ecosystem_134m_2025",
        "Flanders Make ecosystem revenue 134m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Mfg>FM>ecosystem_134m",
        134000000,
        134000000,
        "Strong AR numbers: ecosystem 134m vs statutory 37.3m; 1100 researchers 210 members 526 companies; perimeter dual",
        "src_flanders_make_ar_2025",
        "FM network",
        "Ecosystem R&D volume incl university nodes",
        "Perimeter opacity vs statutory",
        4,
        7.5,
        5,
        5.85,
        "FOI perimeter recon",
    ),
    (
        "lb_dual_soc_fm_imec_vib_vito_2025",
        "Dual Flanders SOC quartet FM 37m + imec 1.22bn + VIB 169m + VITO 297m",
        "multi",
        "ops",
        "BE>dual>SOC_FM_imec_VIB_VITO_2025",
        37325000,
        1216899528,
        "Strong dual quartet: FM mfg 37m/21m convenant; imec nano 1.22bn; VIB life 169m; VITO sust 297m",
        "src_dual_soc_fm_imec_vib_vito_tick596",
        "Flanders SOC ecosystem",
        "Map quartet strategic research centres",
        "VL grant L5 residual all four",
        4,
        8.5,
        5,
        6.35,
        "FOI dual grant matrix SOC",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        (
            lid,
            title,
            jur,
            cat,
            hpath,
            annual,
            stock,
            note,
            src,
            spenders,
            purpose,
            mech,
            prio,
            scale,
            opac,
            pidx,
            hook,
        ) = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"{spenders},{purpose},{mech},{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick596\n"
        )

# --- foi_queue ---
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_fm_vl_convenant_l5_2025,Vlaanderen>Flanders_Make>vl_convenant_L5_2025,flanders_make,"
        "Multi-year VL FM convenant recon to 20.876m 2025; ecosystem 134m vs statutory 37.3m perimeter; "
        "NBB full jaarrekening annex; dual unit-cost vs imec VIB VITO; stocks/orders 42.8m + regularisation 86.6m L5,"
        "AR2025 P and L BS strong tick596; convenant and perimeter residual,5,"
        "Flanders Make / Vlaanderen WEWIS / openbaarheid,,https://www.flandersmake.be,"
        "docs/doge/foi/drafts/gap_fm_vl_convenant_l5_2025.md,ready,2026-07-31,,,,"
        "cmt_flanders_make_ar_2025|cmt_dual_soc_fm_imec_vib_vito_2025,"
        "lb_fm_revenues_37m_2025|lb_dual_soc_fm_imec_vib_vito_2025,"
        f"{utc},{utc},tick596 Flanders Make AR2025 primary; residual VL convenant human send\n"
    )

# --- research_queue: close rq_587 spawn rq_588 ---
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_587,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T14:30:00Z,,Spawned tick595 after VIB dual SOC; rq_116 deferred; progress@600 in 5"
)
new = (
    "rq_587,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T14:30:00Z,2026-07-31T14:45:00Z,"
    "tick596: Flanders Make rev 37.3m convenant 21m dual imec VIB VITO SOC; spawn rq_588; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_587 row not found or already updated")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_588,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T14:45:00Z,,Spawned tick596 after Flanders Make dual SOC; rq_116 deferred; progress@600 in 4\n"
)
rq_path.write_text(text, encoding="utf-8")

# --- loop_state ---
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_587,596,no,"
    "tick596 Flanders Make rev 37.3m convenant 21m dual imec VIB VITO SOC; next rq_588; progress@600 in 4; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick596 CSV writes OK")

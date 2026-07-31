# tick 601 — Plantentuin Meise dual VL/FWB scientific institution hole-fill
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T16:00:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "plantentuin_meise,Plantentuin Meise,Jardin botanique de Meise,"
        "Meise Botanic Garden dual VL FWB scientific institution,agency,vlaanderen_gov,bi,"
        "https://www.plantentuinmeise.be,,,Meise; ontvangsten 33.291m uitgaven 30.004m 2025 prelim; "
        "VL dotatie 16.366m FFEU invest 8.105m eigen+project 8.820m; staff 217 (VL 101 FWB 25 own 91); "
        "dual VL/FWB funding single garden; tick601\n"
    )

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_meise_jv_2025,Plantentuin Meise Jaarverslag 2025 financien personeel,"
        "https://www.plantentuinmeise.be/cms_files/File/Jaarverslag_2025--ONLINE3.pdf,"
        "Plantentuin Meise,2026-07-31,official_annual_report,"
        "Strong tick601 prelim: ontvangsten 33291k (VL 16366 FFEU 8105 eigen/project 8820); "
        "uitgaven 30004k (loon 16056 invest 9022); saldo +3287k; staff 217 1Jan2026 VL101 FWB25 own91; "
        "dual VL/FWB; raw plantentuin_meise_jv_2025.pdf\n"
    )
    f.write(
        "src_dual_meise_vl_fwb_tick601,Dual Plantentuin Meise VL + FWB funding 2025,"
        "docs/doge/raw/plantentuin_meise_jv_2025.pdf,DOGE synthesis Meise JV2025 dual communities,"
        "2026-07-31,synthesis,"
        "Strong dual: single botanic garden funded VL dotatie 16.4m + FWB staff 25 + federal 0.85m; "
        "community dual overhead classic; tick601\n"
    )

bud_rows = [
    ("bud_meise_ontvangsten_2025", 33291000, "Plantentuin Meise total ontvangsten 33.291m 2025 prelim; tick601"),
    ("bud_meise_uitgaven_2025", 30004000, "Plantentuin Meise total uitgaven 30.004m 2025 prelim; tick601"),
    ("bud_meise_saldo_2025", 3287000, "Plantentuin Meise budget saldo +3.287m underspend invest 2025; tick601"),
    ("bud_meise_vl_dotatie_2025", 16366000, "Plantentuin Meise VL government endowment 16.366m 2025; tick601"),
    ("bud_meise_ffeu_invest_2025", 8105000, "Plantentuin Meise FFEU investment budget 8.105m 2025; tick601"),
    ("bud_meise_eigen_project_2025", 8820000, "Plantentuin Meise own+project income total 8.820m 2025; tick601"),
    ("bud_meise_entrance_2025", 1955000, "Plantentuin Meise entrance fees 1.955m 2025; tick601"),
    ("bud_meise_projects_2025", 4240000, "Plantentuin Meise projects consultancy 4.240m 2025; tick601"),
    ("bud_meise_federal_2025", 849000, "Plantentuin Meise federal authorities income 0.849m 2025; tick601"),
    ("bud_meise_rental_cater_2025", 1086000, "Plantentuin Meise rental catering sponsoring insurance 1.086m 2025; tick601"),
    ("bud_meise_shop_2025", 511000, "Plantentuin Meise garden shop 0.511m 2025; tick601"),
    ("bud_meise_parking_2025", 179000, "Plantentuin Meise parking 0.179m 2025; tick601"),
    ("bud_meise_salaries_2025", 16056000, "Plantentuin Meise salaries 16.056m 53.5pct of exp 2025; tick601"),
    ("bud_meise_invest_repairs_2025", 9022000, "Plantentuin Meise investments repairs 9.022m 30.1pct 2025; tick601"),
    ("bud_meise_energy_2025", 659000, "Plantentuin Meise energy 0.659m 2025; tick601"),
    ("bud_meise_collections_2025", 858000, "Plantentuin Meise collections 0.858m 2025; tick601"),
    ("bud_meise_research_exp_2025", 755000, "Plantentuin Meise research exp 0.755m 2025; tick601"),
    ("bud_meise_outreach_2025", 1091000, "Plantentuin Meise public outreach 1.091m 2025; tick601"),
    ("bud_meise_overhead_2025", 1258000, "Plantentuin Meise general overheads 1.258m 2025; tick601"),
    ("bud_meise_ict_2025", 306000, "Plantentuin Meise ICT 0.306m 2025; tick601"),
    ("bud_meise_staff_2026", 0, "Plantentuin Meise staff 217 on 1Jan2026 (not EUR); tick601"),
    ("bud_meise_staff_vl_2026", 0, "Plantentuin Meise staff funded VL 101 1Jan2026; tick601"),
    ("bud_meise_staff_fwb_2026", 0, "Plantentuin Meise staff funded FWB 25 1Jan2026 dual; tick601"),
    ("bud_meise_staff_own_2026", 0, "Plantentuin Meise staff funded own income 91 1Jan2026; tick601"),
    ("bud_meise_ontvangsten_2024", 28508000, "Plantentuin Meise ontvangsten 28.508m 2024 series; tick601"),
    ("bud_meise_uitgaven_2024", 29295000, "Plantentuin Meise uitgaven 29.295m 2024 series; tick601"),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, amt, note in bud_rows:
        year = 2026 if "2026" in bid else (2024 if "2024" in bid else 2025)
        f.write(
            f"{bid},plantentuin_meise,{year},{amt},,,outturn,src_meise_jv_2025,strong,{note}\n"
        )

cmt = {
    "2025_ontvangsten": 33291000,
    "2025_uitgaven": 30004000,
    "2025_saldo": 3287000,
    "2025_vl_dotatie": 16366000,
    "2025_ffeu": 8105000,
    "2025_salaries": 16056000,
    "staff_2026": 217,
    "staff_vl": 101,
    "staff_fwb": 25,
    "staff_own": 91,
    "note": "Dual VL+FWB funding single botanic garden; prelim 2025",
}
cmt_dual = {
    "meise_vl_dotatie_m": 16.366,
    "meise_total_m": 33.291,
    "meise_fwb_staff": 25,
    "meise_vl_staff": 101,
    "note": "Classic dual community funding of one scientific garden",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_meise_jv_2025,Plantentuin Meise dual VL FWB scientific 2025,plantentuin_meise,'
        f'Flanders FWB visitors science,VL dotatie + FFEU + own + federal + FWB staff,'
        f'2025-01-01,2025,2030,33291000,"{esc_json(cmt)}",0,active,'
        f'https://www.plantentuinmeise.be,Botanic garden research collections public,'
        f'Publish final audited accounts + multi-year VL/FWB FOI,'
        f'src_meise_jv_2025,strong,Vlaanderen>Science_Garden>Meise,tick601 JV2025 primary new entity\n'
    )
    f.write(
        f'cmt_dual_meise_vl_fwb_2025,Dual Plantentuin Meise VL + FWB 2025,gg_belgium,'
        f'Community dual scientific institution,Meise JV2025,'
        f'2025-01-01,2025,2025,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual community funding single garden,FOI dual staff cost recon,'
        f'src_dual_meise_vl_fwb_tick601,strong,BE>dual>Meise_VL_FWB,tick601\n'
    )

lb = [
    (
        "lb_meise_ontvangsten_33m_2025",
        "Plantentuin Meise ontvangsten 33.3m uitgaven 30.0m 2025 dual VL FWB",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Garden>Meise>ontvangsten_33m",
        33291000,
        33291000,
        "Strong JV2025 prelim: VL 16.4m FFEU 8.1m own/project 8.8m; exp 30.0m salaries 16.1m dual FWB staff",
        "src_meise_jv_2025",
        3,
        7.5,
        4,
        5.50,
        "Final audited FOI",
    ),
    (
        "lb_meise_vl_dotatie_16m_2025",
        "Plantentuin Meise VL dotatie 16.4m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Garden>Meise>vl_dotatie_16m",
        16366000,
        16366000,
        "Strong: VL endowment 16.366m 49pct of receipts; core structural",
        "src_meise_jv_2025",
        4,
        7.0,
        3,
        5.15,
        "Multi-year VL FOI",
    ),
    (
        "lb_meise_salaries_16m_2025",
        "Plantentuin Meise salaries 16.1m 53.5pct 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Garden>Meise>salaries_16m",
        16056000,
        16056000,
        "Strong: loonkost 16.056m of 30.0m exp; staff 217 dual VL/FWB/own",
        "src_meise_jv_2025",
        3,
        7.0,
        3,
        5.05,
        "Benchmark dual garden FTE",
    ),
    (
        "lb_meise_ffeu_8m_2025",
        "Plantentuin Meise FFEU investment 8.1m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Garden>Meise>ffeu_8m",
        8105000,
        8105000,
        "Strong: FFEU invest budget 8.105m; underspend drives +3.3m saldo",
        "src_meise_jv_2025",
        3,
        6.5,
        4,
        4.85,
        "Invest execution FOI",
    ),
    (
        "lb_meise_staff_217_2026",
        "Plantentuin Meise staff 217 VL101 FWB25 own91 dual",
        "Flanders",
        "ops",
        "Vlaanderen>Science_Garden>Meise>staff_217",
        0,
        0,
        "Strong: dual community staff funding VL 101 + FWB 25 + own 91 1Jan2026",
        "src_meise_jv_2025",
        4,
        6.5,
        4,
        5.05,
        "Dual staff cost FOI",
    ),
    (
        "lb_dual_meise_vl_fwb_2025",
        "Dual Plantentuin Meise VL + FWB funding one garden 2025",
        "multi",
        "ops",
        "BE>dual>Meise_VL_FWB_2025",
        16366000,
        33291000,
        "Strong dual: VL dotatie 16.4m + FWB 25 staff + federal 0.85m single botanic garden",
        "src_dual_meise_vl_fwb_tick601",
        4,
        8.0,
        5,
        6.15,
        "FOI dual community matrix",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        lid, title, jur, cat, hpath, annual, stock, note, src, prio, scale, opac, pidx, hook = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"VL FWB visitors,Botanic garden science public,Core public science dual communities,"
            f"{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick601\n"
        )

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_meise_final_accounts_l5_2025,Vlaanderen>Plantentuin_Meise>final_accounts_L5_2025,plantentuin_meise,"
        "Final audited 2025 accounts recon to prelim 33.3/30.0m; multi-year VL+FWB cash; FFEU invest L5; "
        "dual staff cost VL vs FWB EUR; federal 0.85m line,"
        "JV2025 prelim strong tick601; final audit residual,5,"
        "Plantentuin Meise / Vlaanderen / FWB / openbaarheid,,https://www.plantentuinmeise.be,"
        "docs/doge/foi/drafts/gap_meise_final_accounts_l5_2025.md,ready,2026-07-31,,,,"
        "cmt_meise_jv_2025|cmt_dual_meise_vl_fwb_2025,"
        "lb_meise_ontvangsten_33m_2025|lb_dual_meise_vl_fwb_2025,"
        f"{utc},{utc},tick601 Meise JV2025 primary; residual final accounts human send\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_592,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:45:00Z,,Spawned tick600 after progress dual research wave; rq_116 deferred; progress@610 in 10"
)
new = (
    "rq_592,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:45:00Z,2026-07-31T16:00:00Z,"
    "tick601: Plantentuin Meise 33.3/30.0m dual VL FWB staff 217; spawn rq_593; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_592 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_593,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:00:00Z,,Spawned tick601 after Meise dual VL/FWB; rq_116 deferred; progress@610 in 9\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_592,601,no,"
    "tick601 Plantentuin Meise 33.3/30.0m dual VL FWB; next rq_593; progress@610 in 9; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick601 CSV writes OK")

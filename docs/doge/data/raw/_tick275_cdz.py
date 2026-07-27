# tick 275 — Controledienst ziekenfondsen (CDZ) + HDA dual light
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T00:15:00Z"

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_cdz_jv_2025,Controledienst ziekenfondsen Jaarverslag 2025 begroting balans sector admin,"
        "docs/doge/data/raw/cdz_jaarverslag_2025.pdf,CDZ OCM,2026-07-30,agency,"
        "Uitvoering 2025 ontvangsten 8.259m uitgaven 8.043m (pers 6.029 werking 1.953 invest 0.061); "
        "begroting 2026 ont 8.679 uitg 9.863; staff 46+3 Smals; VI admin 1.377bn 2023; assets 4.753m; tick275\n"
    )
    f.write(
        "src_hda_jv_2025,Health Data Agency Jaarverslag 2025 staff RRF dual e-health,"
        "docs/doge/data/raw/hda_jaarverslag_2025.pdf,HDA Belgium,2026-07-30,agency,"
        "Staff 13 end-2025; +10 vacatures 2026; RRF 7m 2021 Health Data Ecosystem; "
        "no EUR outturn in JV; Healthdata.be merge Q2 2026; dual e-health/Smals; tick275\n"
    )

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cdz,Controledienst voor de ziekenfondsen CDZ,Office de controle des mutualites OCM,"
        "Control Office for mutual health funds,agency,sec_ss,bi,https://ocm-cdz.be,,,"
        "Sector-financed supervisor; outturn 8.04m exp 2025; dual mutual admin 1.38bn; Smals IT 3; tick275\n"
    )
    f.write(
        "hda,Gezondheidszorgdata-agentschap HDA,Agence des donnees de sante HDA,"
        "Belgian Health Data Agency,agency,sec_federal,bi,https://www.hda.belgium.be,,,"
        "ADBA; staff 13 2025; RRF 7m seed; annual EUR FOI; dual e-health fusion; tick275\n"
    )

# --- budgets ---
bud = [
    "bud_cdz_ontvangsten_2025,cdz,2025,8258971.69,,,outturn,src_cdz_jv_2025,strong,AV: ontvangsten uitvoering 8.258.97169",
    "bud_cdz_uitgaven_2025,cdz,2025,8042831.77,,,outturn,src_cdz_jv_2025,strong,AV: uitgaven 8.042.83177 (pers 6.028.66859 + werking 1.952.75014 + invest 61.41304)",
    "bud_cdz_personeel_2025,cdz,2025,6028668.59,,,outturn,src_cdz_jv_2025,strong,Personeelskosten 6.028.66859",
    "bud_cdz_werking_2025,cdz,2025,1952750.14,,,outturn,src_cdz_jv_2025,strong,Werkingskosten 1.952.75014",
    "bud_cdz_invest_2025,cdz,2025,61413.04,,,outturn,src_cdz_jv_2025,strong,Investeringen 61.41304",
    "bud_cdz_surplus_2025,cdz,2025,216139.92,,,outturn,src_cdz_jv_2025,strong,Overschot boekjaar 216.13992",
    "bud_cdz_ontvangsten_2026,cdz,2026,8678895,,,budgeted,src_cdz_jv_2025,strong,Begroting 2026 ontvangsten 8.678.895",
    "bud_cdz_uitgaven_2026,cdz,2026,9862930,,,budgeted,src_cdz_jv_2025,strong,Begroting 2026 uitgaven 9.862.930 (pers 7.086.141 werking 2.636.189 invest 122.600); tekort 1.184.035 from reserve",
    "bud_cdz_mut_tussenkomst_2025,cdz,2025,5139048.80,,,outturn,src_cdz_jv_2025,strong,Tussenkomst mutualistische entiteiten 5.139.04880",
    "bud_cdz_vmob_tussenkomst_2025,cdz,2025,2734169.20,,,outturn,src_cdz_jv_2025,strong,Tussenkomst VMOB 2.734.16920",
    "bud_cdz_assets_2025,cdz,2025,4753060.12,,,outturn,src_cdz_jv_2025,strong,Totaal actief balans 4.753.06012; admin reserve 3.474.81265",
    "bud_cdz_staff_2025,cdz,2025,46,,,outturn,src_cdz_jv_2025,strong,46 personeelsleden + 3 Smals; amount is headcount",
    "bud_vi_admin_kosten_2022,sec_ss,2022,1321633904.29,,,outturn,src_cdz_jv_2025,strong,CDZ sector table: VI administratiekosten 1.321.633.90429 2022",
    "bud_vi_admin_kosten_2023,sec_ss,2023,1376818451.20,,,outturn,src_cdz_jv_2025,strong,CDZ sector table: VI administratiekosten 1.376.818.45120 2023 (+4.18pct)",
    "bud_vi_geneesk_verz_2023,sec_ss,2023,37301635426.91,,,outturn,src_cdz_jv_2025,strong,CDZ: geneeskundige verzorging VI 37.301.635.42691 2023",
    "bud_vi_uitkeringen_2023,sec_ss,2023,13050464862.22,,,outturn,src_cdz_jv_2025,strong,CDZ: uitkeringen 13.050.464.86222 2023",
    "bud_hda_rrf_seed_2021,hda,2021,7000000,,,budgeted,src_hda_jv_2025,strong,EU-RRF Health Data Ecosystem programme 7m end-2021 (multi-year seed)",
    "bud_hda_staff_2025,hda,2025,13,,,outturn,src_hda_jv_2025,strong,13 medewerkers 2025; amount is headcount; +10 vacatures 2026",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

# --- commitments ---
cash_cdz = {
    "ontvangsten_2025": 8258971.69,
    "uitgaven_2025": 8042831.77,
    "personeel_2025": 6028668.59,
    "werking_2025": 1952750.14,
    "invest_2025": 61413.04,
    "surplus_2025": 216139.92,
    "ontvangsten_2026": 8678895,
    "uitgaven_2026": 9862930,
    "personeel_2026": 7086141,
    "werking_2026": 2636189,
    "tekort_2026_budget": 1184035,
    "mut_tussenkomst_2025": 5139048.80,
    "vmob_tussenkomst_2025": 2734169.20,
    "tussenpersonen_2025": 384790.47,
    "staff": 46,
    "smals_fte": 3,
    "assets_2025": 4753060.12,
    "admin_reserve_2025": 3474812.65,
    "vi_admin_2022": 1321633904.29,
    "vi_admin_2023": 1376818451.20,
    "financing": "sector recharges not federal TE; KB 19 Nov 2023 split model",
    "note": "Dual mutual admin 1.38bn 2023 CDZ vs INAMI OA 988m 2025 different perimeter/year; residual L5 landbond optional",
}
cash_hda = {
    "rrf_seed_2021_m": 7,
    "staff_2025": 13,
    "vacancies_2026": 10,
    "healthdata_be_merge": "Q2_2026",
    "dataproducts_2025": 484,
    "ehds_maturity_index_pct": 43,
    "note": "No EUR annual outturn in JV2025; structural budget FAQ 750k/4.5m outdated secondary; FOI residual",
}
for cmt_id, title, ent, ben, basis, start, end, env, cash, goal, cut, conf, path, notes in [
    (
        "cmt_cdz_budget_2025_26",
        "CDZ Controledienst ziekenfondsen sector-financed budget dual mutual admin",
        "cdz",
        "Mutualities VMOB RMOB sector entities controlled",
        "Wet 6 aug 1990 + KB 19 Nov 2023 financing model",
        "2025",
        "2026",
        9862930,
        cash_cdz,
        "Prudential and performance supervision of mutual health funds",
        "Publish multi-year outturn; dual unit-cost vs INAMI OA admin",
        "strong",
        "SS>CDZ>budget",
        "tick275 sector-financed not pure federal TE",
    ),
    (
        "cmt_hda_structure_2025",
        "HDA Health Data Agency structure dual e-health Smals",
        "hda",
        "Researchers policymakers data holders citizens",
        "Organic law 14 Mar 2023 ADBA + EU-RRF Health Data Programme",
        "2021",
        "2026",
        7000000,
        cash_hda,
        "FAIR secondary use of health data EHDS HDAB role",
        "FOI annual budget outturn; dual e-health fusion transparency",
        "medium",
        "Federal>HDA>structure",
        "tick275 euros thin FOI; staff+RRF strong",
    ),
]:
    cash_csv = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
    line = (
        f"{cmt_id},{title},{ent},{ben},{basis},2025-01-01,{start},{end},{env},"
        f"{cash_csv},0,active,docs/doge/data/raw/{'cdz_jaarverslag_2025.pdf' if ent=='cdz' else 'hda_jaarverslag_2025.pdf'},"
        f"{goal},{cut},{'src_cdz_jv_2025' if ent=='cdz' else 'src_hda_jv_2025'},{conf},{path},{notes}\n"
    )
    with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
        f.write(line)

# --- leaderboard ---
lb = [
    "lb_cdz_ops_8_0m,CDZ Controledienst ops 8.0m outturn 2025,federal,ops,SS>CDZ>ops,8042831.77,8042831.77,Strong AV2025: uitgaven 8.043m (pers 6.029 werking 1.953); sector-financed not federal TE; staff 46+3 Smals,strong,src_cdz_jv_2025,Mutualities taxpayers via sector charges,Supervise mutual health funds,Core prudential control dual 1.38bn VI admin not pure waste,3,5.5,3,4.7,Publish L5 if material; dual unit-cost,seed,,tick275",
    "lb_cdz_budget_9_9m_2026,CDZ budgeted spend 9.9m 2026,federal,ops,SS>CDZ>budget_2026,9862930,9862930,Strong AV: begroting uitgaven 9.863m 2026 (+22.6pct vs 2025 outturn) deficit 1.184m from admin reserve,strong,src_cdz_jv_2025,Sector entities,Expand supervision capacity,Jump needs justification; reserve draw,4,5.0,3,4.6,Track reserve path multi-year,seed,,tick275",
    "lb_vi_admin_1_38bn_2023,Mutual VI administratiekosten 1.377bn 2023 CDZ,federal,ops,SS>mutualities>admin_CDZ,1376818451.20,1376818451.20,Strong CDZ sector table 2023: admin 1.3768bn (+4.18pct vs 1.322bn 2022); dual INAMI OA 988m 2025 different perimeter/year,strong,src_cdz_jv_2025,Landsbonden members,Mutual admin of compulsory insurance,Core SS channel; L5 by landsbond residual FOI gap_mutual_admin_l5,4,9.0,6,6.5,FOI still landbond split; reconcile INAMI 988m vs CDZ 1.38bn,seed,,tick275 dual gap_mutual",
    "lb_hda_staff_13,HDA Health Data Agency 13 staff 2025 dual e-health,federal,ops,Federal>HDA>staff,0,0,Strong JV: 13 staff 2025 +10 vacancies 2026; RRF 7m seed; annual EUR budget residual FOI; dual e-health 132.5m Smals 579m,strong,src_hda_jv_2025,Researchers policymakers,Secondary health data access EHDS,Core digital health governance small; budget opacity,3,4.0,3,4.0,FOI annual budget outturn gap_hda_budget,seed,,tick275",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# --- foi_queue ---
foi_lines = [
    (
        "gap_hda_budget_2024_26",
        "Federal>HDA>budget_outturn",
        "hda",
        "Cash-by-year structural federal budget + RRF residual + EU project grants 2023-2026; personnel vs opex; Healthdata.be integration cost 2026; reconcile FAQ 0.75/4.5m claims",
        "JV2025 has staff 13 and RRF 7m seed but no EUR annual outturn; dual e-health financing map incomplete",
        "5",
        "Health Data Agency / FOD Volksgezondheid openbaarheid",
        "info@hda.belgium.be",
        "https://www.hda.belgium.be",
        "docs/doge/foi/drafts/gap_hda_budget_2024_26.md",
        "cmt_hda_structure_2025",
        "lb_hda_staff_13",
        "tick275 draft ready human send; staff+RRF filled",
    ),
]
foi_path = base / "foi_queue.csv"
text = foi_path.read_text(encoding="utf-8")
out = text.rstrip("\n").split("\n")
# update mutual admin gap note
out2 = []
for line in out:
    if line.startswith("gap_mutual_admin_l5,") and "tick275" not in line:
        line = line.rstrip() + " | tick275: CDZ VI admin 1.377bn 2023 strong; residual L5 landsbond still ready"
    out2.append(line)
for gap_id, hier, ent, miss, why, prio, body, email, postal, draft, cmt, lb, notes in foi_lines:
    if not any(l.startswith(gap_id + ",") for l in out2):
        out2.append(
            f"{gap_id},{hier},{ent},{miss},{why},{prio},{body},{email},{postal},{draft},"
            f"ready,2026-07-30,,,,,,{cmt},{lb},{now},{now},{notes}"
        )
foi_path.write_text("\n".join(out2) + "\n", encoding="utf-8")

# --- research_queue ---
rq_path = base / "research_queue.csv"
rq_lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq_lines:
    if line.startswith("rq_266,"):
        out.append(
            "rq_266,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; Controledienst ziekenfondsen; HDA; other FOI-adjacent after Smals).,"
            f"gap_hda_budget_2024_26,2026-07-29T23:45:00Z,{now},"
            "tick275: CDZ outturn 8.0m + VI admin 1.38bn; HDA staff 13 FOI budget; spawn rq_267"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_267,") for l in out):
    out.append(
        "rq_267,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CDZ/HDA).,,"
        f"{now},,Spawned tick275 after CDZ HDA; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

# --- loop_state ---
(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_266,275,no,"
    "Scheduler 60s. Next prio5 rq_267; rq_116 SWA deferred. FOI ready human send. tick275 CDZ 8.0m + VI admin 1.38bn.\n",
    encoding="utf-8",
)

print("OK tick275 CSV writes")

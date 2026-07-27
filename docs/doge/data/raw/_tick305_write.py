# tick 305 — rq_296 Federale Ombudsman AR2024 + Kamer 56K0983
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T15:15:00Z"
unit = "rq_296"

# --- sources ---
src_lines = [
    (
        "src_fed_ombuds_jaarverslag_2024,"
        "Federale Ombudsman Jaarverslag 2024 budget staff cases,"
        "docs/doge/data/raw/fed_ombuds_jaarverslag_2024.pdf; "
        "https://www.federaalombudsman.be/sites/default/files/2025-04/Jaarverslag_2024.pdf,"
        "Federale Ombudsman / Mediateur federal,"
        "2026-07-30,agency,"
        "AR table p95: uitgaven 6238257.12 2023 / budget 7955700 2024 / 8238400 2025; "
        "dotatie 6840000/7367000/6917000; boni 551k/589k/1321k; staff 52; tick305\n"
    ),
    (
        "src_kamer_56k0983_fed_ombuds,"
        "Kamer 56K0983/001 Comptabiliteit federale ombudsmannen rekeningen 2024 budget 2026,"
        "docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf; "
        "https://www.dekamer.be/FLWB/PDF/56/0983/56K0983001.pdf,"
        "Belgische Kamer van volksvertegenwoordigers commissie Comptabiliteit,"
        "2026-07-30,official_budget,"
        "2024 surplus exp 1346689.20 util 83.07pct; global result 1515477.14; "
        "2026 exp 8268000 dotatie 6753000 (-164k vs 2025) + boni 2024; 8 ETP hard fill; tick305\n"
    ),
]
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for line in src_lines:
        f.write(line)

# --- entities ---
ent_line = (
    "fed_ombudsman,Federale Ombudsman,Mediateurs federaux,"
    "Federal Ombudsman parliamentary mediation and whistleblowing,"
    "agency,sec_federal,bi,"
    "https://www.federaalombudsman.be,contact@federaalombudsman.be,,"
    "Kamer-dotatie institution; dual GBA FIRM CTRG; budget ~8.0-8.3m; staff 52; "
    "whistleblower private+public; tick305\n"
)
with (ROOT / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(ent_line)

# --- budgets ---
# 2024 actual spend derived: budget 7955700 - surplus 1346689.20 = 6609010.80
bud_rows = [
    "bud_fed_ombuds_exp_2023,fed_ombudsman,2023,6238257,,,outturn,src_fed_ombuds_jaarverslag_2024,strong,"
    "AR rekeningen 2023 uitgaven 6.238.25712 EUR",
    "bud_fed_ombuds_exp_budget_2024,fed_ombudsman,2024,7955700,,,budgeted,src_fed_ombuds_jaarverslag_2024,strong,"
    "AR budget 2024 uitgaven 7.955.700 EUR",
    "bud_fed_ombuds_exp_outturn_2024,fed_ombudsman,2024,6609011,,,outturn,src_kamer_56k0983_fed_ombuds,strong,"
    "Derived: budget 7.9557m - Kamer surplus 1.3466892m = 6.609011m; util 83.07pct confirmed",
    "bud_fed_ombuds_exp_budget_2025,fed_ombudsman,2025,8238400,,,budgeted,src_fed_ombuds_jaarverslag_2024,strong,"
    "AR budget 2025 uitgaven 8.238.400 EUR",
    "bud_fed_ombuds_exp_budget_2026,fed_ombudsman,2026,8268000,,,budgeted,src_kamer_56k0983_fed_ombuds,strong,"
    "Kamer ontwerp 2026 totale uitgaven 8.268.000 (+29.6k vs 2025)",
    "bud_fed_ombuds_dotatie_2023,fed_ombudsman,2023,6840000,,,outturn,src_fed_ombuds_jaarverslag_2024,strong,"
    "AR financing dotatie 6.840.000 2023",
    "bud_fed_ombuds_dotatie_2024,fed_ombudsman,2024,7367000,,,budgeted,src_fed_ombuds_jaarverslag_2024,strong,"
    "AR financing dotatie 7.367.000 2024",
    "bud_fed_ombuds_dotatie_2025,fed_ombudsman,2025,6917000,,,budgeted,src_fed_ombuds_jaarverslag_2024,strong,"
    "AR financing dotatie 6.917.000 2025 (-6.1pct vs 2024); gap filled by boni 1.321m",
    "bud_fed_ombuds_dotatie_2026,fed_ombudsman,2026,6753000,,,budgeted,src_kamer_56k0983_fed_ombuds,strong,"
    "Kamer 2026 requested dotatie 6.753.000 (-164k vs 2025); + boni 2024 1.515m",
    "bud_fed_ombuds_boni_2024,fed_ombudsman,2024,1515477,,,outturn,src_kamer_56k0983_fed_ombuds,strong,"
    "Kamer global result 2024 1.515.47714 (budget result 926736 + carried 588741)",
    "bud_fed_ombuds_staff_2024,fed_ombudsman,2024,52,,,outturn,src_fed_ombuds_jaarverslag_2024,strong,"
    "Headcount 52 (48 FT + 4 PT); 35 statutaire 17 contractueel; FR27 NL25; not EUR",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

# --- commitments ---
cmt_rows = [
    (
        "cmt_fed_ombuds_package_2023_26,Federale Ombudsman parliamentary-dotation package,fed_ombudsman,"
        "Citizens complainants whistleblowers federal admin,Wet 22 mrt 1995 federale ombudsmannen + klokkenluiders wetten,"
        "1995-03-22,2023,2026,31078357,"
        '"{""exp_2023"":6238257.12,""budget_2024"":7955700,""outturn_2024_class"":6609011,'
        '""budget_2025"":8238400,""budget_2026"":8268000,'
        '""dotatie_2023"":6840000,""dotatie_2024"":7367000,""dotatie_2025"":6917000,""dotatie_2026"":6753000,'
        '""boni_2024_global"":1515477.14,""util_2024_pct"":83.07,'
        '""staff_2024"":52,""etp_expansion_hard_fill"":8,'
        '""financing"":""Kamer dotatie + boni year X for year X+2 not returned to Treasury"",'
        '""note"":""Under-spend driven by recruitment lag forensic auditors bilingual; dual GBA FIRM""}",'
        "0,active,docs/doge/data/raw/fed_ombuds_jaarverslag_2024.pdf,"
        "Citizen mediation whistleblower protection admin accountability,"
        "Core democratic infrastructure; FOI multi-year P&L L5 optional,"
        "src_fed_ombuds_jaarverslag_2024,strong,Federal>Parlement>Federale_Ombudsman,"
        "tick305 dual GBA~15m Kamer-dotation peers"
    ),
    (
        "cmt_fed_ombuds_dotatie_path,Federale Ombudsman federal Kamer dotatie path declining via boni,fed_ombudsman,"
        "Federale Ombudsman ops,Kamer Comptabiliteit annual allocation,1995-03-22,2023,2026,27877000,"
        '"{""2023"":6840000,""2024"":7367000,""2025"":6917000,""2026"":6753000,'
        '""mechanism"":""boni year X cofinances year X+2 reduces requested dotatie"",'
        '""moesen_freeze"":""nominal freeze legislative institutions CM 14Feb2025""}",'
        "0,active,docs/doge/data/raw/kamer_56k0983_dotaties_2025.pdf,"
        "Fund independent parliamentary ombudsman,"
        "Publish multi-year boni stock; Moesen freeze compatibility,"
        "src_kamer_56k0983_fed_ombuds,strong,Federal>Parlement>Ombuds>dotatie,tick305"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

# --- leaderboard ---
lb_rows = [
    (
        "lb_fed_ombuds_budget_8m,Federale Ombudsman budget ~8.0-8.3m 2024-26,federal,ops,"
        "Federal>Parlement>Federale_Ombudsman,8238400,8268000,"
        "Strong AR+Kamer: budget 7.96m 2024 / 8.24m 2025 / 8.27m 2026; outturn 2024 ~6.61m util 83pct; staff 52,"
        "strong,src_fed_ombuds_jaarverslag_2024,Citizens whistleblowers,Independent mediation and integrity,"
        "Core democratic control; under-spend from recruitment lag not waste,"
        "2,5.0,2,3.3,Keep; dual map GBA FIRM CTRG dotatie peers,"
        "seed,,tick305 not pure waste"
    ),
    (
        "lb_fed_ombuds_underspend_1_3m,Federale Ombudsman 2024 under-spend surplus 1.35m util 83pct,federal,ops,"
        "Federal>Parlement>Ombuds>underspend,1346689,1515477,"
        "Strong Kamer: exp surplus 1.347m (pers 1.135 + ops 0.185 + cap 0.027); global result 1.515m; 8 ETP hard to fill,"
        "strong,src_kamer_56k0983_fed_ombuds,Taxpayers,Full staffing of mandated whistleblower capacity,"
        "Boni recycles to X+2 lowers future dotatie — opacity on permanent vs temporary capacity,"
        "5,4.5,3,4.5,Fill bilingual forensic posts or right-size kader; publish ETP plan,"
        "seed,,tick305 mechanism recruitment lag"
    ),
    (
        "lb_fed_ombuds_dotatie_decline,Federale Ombudsman dotatie 7.37m->6.75m 2024-26 via boni,federal,ops,"
        "Federal>Parlement>Ombuds>dotatie_path,6753000,27877000,"
        "Strong: dotatie 7.367/6.917/6.753m 2024-26; boni X for X+2; Moesen nominal freeze context,"
        "strong,src_kamer_56k0983_fed_ombuds,Taxpayers Kamer,Sustainable parliamentary control funding,"
        "Dotatie falls while budgeted exp rises — reserve-funded sustainability risk parallel GBA,"
        "4,5.0,3,4.3,Publish boni stock multi-year; dual GBA reserve model,"
        "seed,,tick305 parallel GBA financing mix"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

# --- foi_queue ---
foi_line = (
    "gap_fed_ombuds_l5_pnl,Federal>Parlement>Federale_Ombudsman>L5_P&L,fed_ombudsman,"
    "Full cash outturn table 2023-2025 by littera A/B personnel vs ops vs IT vs invest; multi-year FTE filled vs kader "
    "including whistleblower 4 ETP; boni stock begin/end each year; reconcile AR budget vs Kamer 2024 accounts,"
    "Totals and surplus strong; L5 cost structure and filled ETP path still thin; dual GBA reserve model material,"
    "3,Federale Ombudsman / Kamer openbaarheid,contact@federaalombudsman.be,"
    "https://www.federaalombudsman.be,"
    "docs/doge/foi/drafts/gap_fed_ombuds_l5_pnl.md,ready,2026-07-30,,,,,,"
    "cmt_fed_ombuds_package_2023_26|cmt_fed_ombuds_dotatie_path,"
    "lb_fed_ombuds_budget_8m|lb_fed_ombuds_underspend_1_3m,"
    "2026-07-30T15:15:00Z,2026-07-30T15:15:00Z,tick305 draft ready human send low-medium prio\n"
)
with (ROOT / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

# --- research_queue ---
rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_296,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (new agency ARs / Kamer 56 PDFs; Federale Ombudsman deepen; AGMJ if extractable). Prefer before idle.,,"
    "2026-07-30T14:45:00Z,,Spawned tick304 after GBA AR2024-25; rq_116 SWA deferred"
)
new = (
    "rq_296,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (new agency ARs / Kamer 56 PDFs; Federale Ombudsman deepen; AGMJ if extractable). Prefer before idle.,"
    "gap_fed_ombuds_l5_pnl,2026-07-30T14:45:00Z,2026-07-30T15:15:00Z,"
    "tick305: Fed Ombuds budget 8.0-8.3m; outturn 2024 ~6.61m util 83pct; dotatie 7.37->6.75m; staff 52; FOI L5; spawn rq_297"
)
if old not in text:
    raise SystemExit("rq_296 row not found:\n" + repr(text[-500:]))
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_297,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Kamer 56K0983 peer institutions: Grondwettelijk Hof Rekenhof FIRM CTRG HRJ; AGMJ if extractable). Prefer before idle.,,"
    "2026-07-30T15:15:00Z,,Spawned tick305 after Federale Ombudsman; rq_116 SWA deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

# --- loop_state ---
(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},305,no,"
    "Scheduler 60s. Next prio5 rq_297; rq_116 SWA deferred. FOI ready. "
    "tick305 Fed Ombuds ~8.0-8.3m budget + outturn 6.61m.\n",
    encoding="utf-8",
)

print("CSV updates OK")

# tick 304 — rq_295 GBA Gegevensbeschermingsautoriteit AR 2024-2025
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T14:45:00Z"
unit = "rq_295"

# --- sources ---
src_line = (
    "src_gba_jaarverslag_2024_25,"
    "GBA Gegevensbeschermingsautoriteit Jaarverslag 2024+2025 budget staff,"
    "docs/doge/data/raw/gba_jaarverslag_2024.pdf; docs/doge/data/raw/gba_jaarverslag_2025.pdf; "
    "https://www.gegevensbeschermingsautoriteit.be/publications/jaarverslag-2024.pdf; "
    "https://www.gegevensbeschermingsautoriteit.be/publications/jaarverslag-2025.pdf,"
    "Gegevensbeschermingsautoriteit GBA / Autorite protection donnees,"
    "2026-07-30,agency,"
    "AR2024: staff 84 eoy; werkingskredieten 15112565.38; 2023 13274000; dotatie 14002000 + reserves. "
    "AR2025: staff 96 eoy (+12pct); werkingskrediet 15299845.55; toewijzing 12669000 + reserves. "
    "tick304\n"
)
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_line)

# --- entities ---
ent_line = (
    "gba_apd,Gegevensbeschermingsautoriteit GBA,Autorite de protection des donnees APD,"
    "Belgian Data Protection Authority GDPR regulator,agency,sec_federal,bi,"
    "https://www.gegevensbeschermingsautoriteit.be,,,,"
    "Independent GDPR supervisor WOG; werkingskredieten ~15.1-15.3m; staff 84->96 2024-25; "
    "dotatie/toewijzing 14.0->12.7m + reserves; dual BMA BIPT CCB COC; tick304\n"
)
with (ROOT / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(ent_line)

# --- budgets ---
bud_rows = [
    "bud_gba_werkings_2023,gba_apd,2023,13274000,,,outturn,src_gba_jaarverslag_2024_25,strong,"
    "AR2024: werkingskredieten 13.274m 2023 (Belgian notation 13.274.00 = 13.274.000; +13.85pct to 2024 confirms)",
    "bud_gba_werkings_2024,gba_apd,2024,15112565,,,outturn,src_gba_jaarverslag_2024_25,strong,"
    "AR2024 exact: 15.112.56538 EUR werkingskredieten 2024",
    "bud_gba_werkings_2025,gba_apd,2025,15299846,,,outturn,src_gba_jaarverslag_2024_25,strong,"
    "AR2025 exact: 15.299.84555 EUR werkingskrediet 2025 (+1.24pct)",
    "bud_gba_dotatie_2024,gba_apd,2024,14002000,,,budgeted,src_gba_jaarverslag_2024_25,strong,"
    "AR2024: eigenlijke dotatie 14.002.000 EUR; remainder from carried boni/reserves",
    "bud_gba_toewijzing_2025,gba_apd,2025,12669000,,,budgeted,src_gba_jaarverslag_2024_25,strong,"
    "AR2025: eigenlijke toewijzing 12.669.000 EUR; rest from overgedragen reserves; -9.5pct vs 2024 dotatie",
    "bud_gba_staff_2024,gba_apd,2024,84,,,outturn,src_gba_jaarverslag_2024_25,strong,"
    "Headcount eoy2024 84 medewerkers vs 68 eoy2023 (+23.5pct); not EUR",
    "bud_gba_staff_2025,gba_apd,2025,96,,,outturn,src_gba_jaarverslag_2024_25,strong,"
    "Headcount eoy2025 96 medewerkers vs 84 (+12pct); not EUR",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

# --- commitments ---
cmt_rows = [
    (
        "cmt_gba_package_2023_25,GBA data protection authority werkingskredieten package,gba_apd,"
        "Data subjects controllers processors (GDPR),Wet 3 dec 2017 GBA (WOG) + AVG/GDPR,2018-05-25,2023,2025,43687000,"
        '"{""werkings_2023"":13274000,""werkings_2024"":15112565.38,""werkings_2025"":15299845.55,'
        '""dotatie_2024"":14002000,""toewijzing_2025"":12669000,'
        '""staff_eoy2023"":68,""staff_eoy2024"":84,""staff_eoy2025"":96,'
        '""financing"":""federal dotatie/toewijzing + carried reserves/boni"",'
        '""note"":""2025 toewijzing cut while staff+krediet up via reserves; dual digital package BMA BIPT CCB""}",'
        "0,active,docs/doge/data/raw/gba_jaarverslag_2024.pdf,"
        "Independent GDPR supervision enforcement advice first-line,"
        "Core privacy infrastructure; FOI personnel/ops L5 + Kamer BA codes,"
        "src_gba_jaarverslag_2024_25,strong,Federal>Justitie_Privacy>GBA,tick304 dual regulators BMA BIPT"
    ),
    (
        "cmt_gba_dotatie_path,GBA federal dotatie/toewijzing path 2024-2025,gba_apd,"
        "GBA operations,WOG annual parliamentary/federal allocation,2018-05-25,2024,2025,26671000,"
        '"{""dotatie_2024"":14002000,""toewijzing_2025"":12669000,""delta_pct"":-9.5,'
        '""werkings_gap_filled_by"":""carried reserves/boni"",'
        '""staff_path"":""68->84->96""}",'
        "0,active,docs/doge/data/raw/gba_jaarverslag_2025.pdf,"
        "Fund independent DPA operations,"
        "Publish reserve stock path + multi-year staff plan; avoid silent TE creep,"
        "src_gba_jaarverslag_2024_25,strong,Federal>GBA>dotatie,tick304"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

# --- leaderboard ---
lb_rows = [
    (
        "lb_gba_werkings_15m,GBA werkingskredieten ~15.1-15.3m 2024-25,federal,ops,"
        "Federal>Privacy>GBA>werkingskredieten,15112565,15299846,"
        "Strong AR: 15.11m 2024 / 15.30m 2025; staff 84->96; dotatie 14.0->12.7m + reserves,"
        "strong,src_gba_jaarverslag_2024_25,Data subjects controllers,Independent GDPR supervision,"
        "Core digital rights infrastructure; staff growth funded partly by reserves,"
        "2,5.5,2,3.6,Keep core; publish P&L personnel/ops split; reserve policy note,"
        "seed,,tick304 dual BMA~9m BIPT~80m FSMA~108m"
    ),
    (
        "lb_gba_dotatie_cut_reserves,GBA toewijzing cut 14.0m->12.7m while staff+12pct via reserves,federal,ops,"
        "Federal>Privacy>GBA>financing_mix,12669000,26671000,"
        "Strong AR path: 2024 dotatie 14.002m; 2025 toewijzing 12.669m (-9.5pct); werkings still +1.24pct via reserves; staff 84->96,"
        "strong,src_gba_jaarverslag_2024_25,Taxpayers GBA staff,Sustainable DPA financing,"
        "Permanent headcount rise vs temporary reserve draw — sustainability risk,"
        "5,5.0,3,4.7,Publish reserve stock path + multi-year staff plan; avoid silent TE creep,"
        "seed,,tick304 mechanism not pure waste"
    ),
    (
        "lb_gba_staff_96,GBA headcount 96 eoy2025 (+41pct vs 68 eoy2023),federal,ops,"
        "Federal>Privacy>GBA>FTE,0,0,"
        "Strong AR: 68 eoy2023 / 84 eoy2024 / 96 eoy2025; wage bill residual FOI,"
        "strong,src_gba_jaarverslag_2024_25,GDPR enforcement capacity,Adequate DPA staffing,"
        "Rapid growth post-AVG; dual digital package with BMA BIPT CCB,"
        "3,4.0,3,3.5,FOI wage bill; dual map digital regulators capacity,"
        "seed,,tick304"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

# --- foi_queue ---
foi_line = (
    "gap_gba_accounts_l5,Federal>Privacy>GBA>jaarrekening_L5,gba_apd,"
    "Full jaarrekening 2023-2025: personnel vs ops vs invest split; reserve/boni stock path; "
    "Kamer/BOSA BA or allocation codes for federal toewijzing; multi-year FTE by service,"
    "AR gives totals strong; L5 cost structure and permanent vs reserve financing opacity; material ~15m/yr regulator,"
    "4,Gegevensbeschermingsautoriteit / FOD Justitie openbaarheid,,"
    "https://www.gegevensbeschermingsautoriteit.be,"
    "docs/doge/foi/drafts/gap_gba_accounts_l5.md,ready,2026-07-30,,,,,,"
    "cmt_gba_package_2023_25|cmt_gba_dotatie_path,lb_gba_werkings_15m|lb_gba_dotatie_cut_reserves,"
    "2026-07-30T14:45:00Z,2026-07-30T14:45:00Z,tick304 draft ready human send\n"
)
with (ROOT / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

# --- research_queue ---
rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_295,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (new agency ARs / Kamer 56 PDFs; AGMJ if extractable). Prefer before idle.,,"
    "2026-07-30T14:15:00Z,,Spawned tick303 after KSC AR2024; rq_116 SWA deferred"
)
new = (
    "rq_295,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (new agency ARs / Kamer 56 PDFs; AGMJ if extractable). Prefer before idle.,"
    "gap_gba_accounts_l5,2026-07-30T14:15:00Z,2026-07-30T14:45:00Z,"
    "tick304: GBA werkings 15.11/15.30m 2024-25; staff 84->96; toewijzing 14.0->12.7m + reserves; FOI L5; spawn rq_296"
)
if old not in text:
    raise SystemExit("rq_295 row not found as expected:\n" + repr(text[-400:]))
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_296,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (new agency ARs / Kamer 56 PDFs; Federale Ombudsman deepen; AGMJ if extractable). Prefer before idle.,,"
    "2026-07-30T14:45:00Z,,Spawned tick304 after GBA AR2024-25; rq_116 SWA deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

# --- loop_state ---
(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},304,no,"
    "Scheduler 60s. Next prio5 rq_296; rq_116 SWA deferred. FOI ready. "
    "tick304 GBA privacy regulator ~15.1-15.3m + staff 96.\n",
    encoding="utf-8",
)

print("CSV updates OK")

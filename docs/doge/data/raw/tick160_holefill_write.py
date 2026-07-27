# -*- coding: utf-8 -*-
"""Tick 160 — rq_121 FOI-adjacent public hole-fill: NMBS 2025 results + VDAB 2024."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 160
UNIT = "rq_121"
UTC = "2026-07-28T03:20:00Z"


def read_text(p: Path) -> str:
    raw = p.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def write_text(p: Path, text: str) -> None:
    p.write_bytes(text.encode("utf-8", errors="replace"))


def append_if_missing(p: Path, rows: list[str]) -> None:
    text = read_text(p)
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        if row.split(",", 1)[0] not in text:
            text += row + "\n"
    write_text(p, text)


def replace_line_startswith(p: Path, prefix: str, new_line: str) -> bool:
    text = read_text(p)
    lines = text.splitlines()
    out, found = [], False
    for L in lines:
        if L.startswith(prefix):
            out.append(new_line)
            found = True
        else:
            out.append(L)
    write_text(p, "\n".join(out) + "\n")
    return found


def replace_containing(p: Path, match: str, new_line: str) -> bool:
    """Replace first CSV row starting with id before first comma if match is id."""
    return replace_line_startswith(p, match + ",", new_line)


srcs = [
    'src_nmbs_results_2025_page,NMBS Resultaten 2025 official corporate page,https://www.belgiantrain.be/nl/about-sncb/corporate/2026/financial-results-2025,NMBS/SNCB,2026-07-28,official_press,"EBITDA 54.2m 2025; debt 1.532bn; invest >820m; ODC op compensation hypothesis -100m vs 2025 path; rail savings 675m 2025-29; staff 16976; tick160"',
    'src_vdab_jv_2024,VDAB Jaarverslag 2024 PDF,https://www.vdab.be/sites/default/files/media/files/VDAB-jaarverslag-2024.pdf,VDAB,2026-07-28,official_annual_report,"Staff 4761 eoy2024 (-230); PMO managed ~160m projects since 2019; tick160"',
    'src_vl_pq_vdab_budget_52_2025,VP schriftelijke vraag 52 Ongena VDAB budget 962m/783m 2024,https://docs.vlaamsparlement.be/pfile?id=2236871,Vlaams Parlement / minister Demir,2026-07-28,official_parliament,"Question states 962m total 783m VL dots 2024; minister points to jaarrekening; medium for totals; tick160"',
]
append_if_missing(DATA / "sources.csv", srcs)

bud = [
    # NMBS 2025
    "bud_nmbs_ebitda_2025,nmbs,2025,54200000,,,outturn,src_nmbs_results_2025_page,strong,Recurrent EBITDA 54.2m 2025 (131.6m 2024) official results page",
    "bud_nmbs_ebitda_2024,nmbs,2024,131600000,,,outturn,src_nmbs_results_2025_page,strong,Recurrent EBITDA 131.6m 2024",
    "bud_nmbs_debt_econ_2025,nmbs,2025,1532000000,,,outturn,src_nmbs_results_2025_page,strong,Economic debt 1.532bn eoy2025 (2.146bn eoy2024)",
    "bud_nmbs_debt_econ_2024,nmbs,2024,2146000000,,,outturn,src_nmbs_results_2025_page,strong,Economic debt 2.146bn eoy2024",
    "bud_nmbs_invest_2025,nmbs,2025,820000000,,,outturn,src_nmbs_results_2025_page,strong,Investments more than 820m 2025 official",
    "bud_nmbs_invest_rolling_2025,nmbs,2025,350000000,,,outturn,src_nmbs_results_2025_page,strong,Rolling stock renewal invest >350m 2025 (M7 delivery ETCS 100pct fleet)",
    "bud_nmbs_invest_stations_2025,nmbs,2025,213000000,,,outturn,src_nmbs_results_2025_page,strong,Station reception infrastructure invest 213m 2025",
    "bud_nmbs_invest_workshops_2025,nmbs,2025,89000000,,,outturn,src_nmbs_results_2025_page,strong,Workshop renovation modernization 89m 2025",
    "bud_nmbs_invest_digital_2025,nmbs,2025,152000000,,,outturn,src_nmbs_results_2025_page,strong,Digitalization invest 152m 2025",
    "bud_nmbs_odc_hyp_delta_2025,nmbs,2025,-100000000,,,budgeted,src_nmbs_results_2025_page,medium,Revenue/cost path under ODC 2022 contractual exploitatievergoeding hypothesis for 2025 of -100m (not absolute cash toelage)",
    "bud_nmbs_staff_2026_01,nmbs,2026,16976,,,outturn,src_nmbs_results_2025_page,strong,Staff headcount 16976 on 2026-01-01 after 1100+ hires 2025",
    "bud_nmbs_passengers_2025,nmbs,2025,207800000,,,outturn,src_nmbs_results_2025_page,strong,Passengers 207.8m 2025 (+1pct vs 2024) despite 27 strike days",
    "bud_nmbs_punctuality_2025,nmbs,2025,91.7,,,ratio_pct,src_nmbs_results_2025_page,strong,Punctuality 91.7pct 2025 best in 20y excl COVID",
    "bud_nmbs_mr30_order_180,nmbs,2025,0,,,commitment,src_nmbs_results_2025_page,medium,Board awarded CAF MR30 order first batch 180 units Dec 2025 — cash envelope not in press page",
    # VDAB 2024
    "bud_vdab_staff_2024,vdab,2024,4761,,,outturn,src_vdab_jv_2024,strong,Staff 4761 eoy2024 (-230 vs 2023) meets savings norm",
    "bud_vdab_total_2024_class,vdab,2024,962000000,,,budgeted,src_vl_pq_vdab_budget_52_2025,medium,VP question premise 962m institutional total 2024; minister defers to jaarrekening",
    "bud_vdab_vl_dotatie_2024_class,vdab,2024,783000000,,,budgeted,src_vl_pq_vdab_budget_52_2025,medium,VP question 783m VL dotations of 962m 2024; residual jaarrekening FOI",
    "bud_vdab_pmo_portfolio_cum,vdab,2024,160000000,,,outturn,src_vdab_jv_2024,strong,PMO managed about 160m project means since 2019 (~382 projects)",
]
append_if_missing(DATA / "budgets.csv", bud)

cmts = [
    (
        'cmt_nmbs_results_2025,NMBS 2025 financial and investment outturn,nmbs,NMBS passengers State PSO,'
        'NMBS official Results 2025 page + ODC 2023-2032,2026-04-02,2025,2025,820000000,'
        '"{""ebitda"":54200000,""ebitda_2024"":131600000,""debt_econ"":1532000000,""debt_2024"":2146000000,'
        '""invest_total"":820000000,""invest_rolling"":350000000,""invest_stations"":213000000,'
        '""invest_workshops"":89000000,""invest_digital"":152000000,""odc_hyp_delta"":-100000000,'
        '""rail_sector_savings_2025_29"":675000000,""staff_2026_01"":16976,""passengers"":207800000,'
        '""punctuality_pct"":91.7,""strike_days"":27,""note"":""absolute State cash toelage still FOI; ODC path cmt separate""}",0,active,'
        'https://www.belgiantrain.be/nl/about-sncb/corporate/2026/financial-results-2025,'
        'Public service rail PSO delivery,Publish FPS cash codes vs ODC; track 675m sector savings split,'
        'src_nmbs_results_2025_page,strong,Federal>Mobiliteit>NMBS>results2025,'
        'tick160 hole-fill gap_nmbs partial'
    ),
    (
        'cmt_vdab_institutional_2024,VDAB institutional budget and staff 2024,vdab,Workseekers employers Flanders,'
        'VP PQ52 + VDAB Jaarverslag 2024,2025-10-02,2024,2024,962000000,'
        '"{""total_class"":962000000,""vl_dotatie_class"":783000000,""eu_own_class"":179000000,'
        '""staff_eoy"":4761,""staff_delta"":-230,""pmo_cum_160m"":true,'
        '""bbt_2026_vek"":750702000,""note"":""totals medium from PQ premise; staff strong from JV; FOI jaarrekening for full split""}",0,active,'
        'https://www.vdab.be/sites/default/files/media/files/VDAB-jaarverslag-2024.pdf,'
        'PES Flanders dual FOREM/Actiris,Publish jaarrekening tender L5; deliver savings path,'
        'src_vdab_jv_2024,medium,Vlaanderen>WEWIL>VDAB>2024,'
        'tick160; strengthens gap_vdab partial; residual FOI remains'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

lbs = [
    "lb_nmbs_invest_820m,NMBS investments ~820m 2025,federal,programme,Federal>NMBS>invest2025,820000000,820000000,Official: rolling 350m stations 213m digital 152m workshops 89m; debt down to 1.53bn; EBITDA 54.2m,strong,src_nmbs_results_2025_page,Rail passengers,PSO rolling stock stations digital,Core PSO; absolute toelage FOI; strike impact,3,7.5,4,5.5,FPS cash vs ODC path; 675m sector savings split,seed,,tick160",
    "lb_nmbs_debt_path,NMBS economic debt 1.53bn eoy2025,federal,ops,Federal>NMBS>debt,1532000000,1532000000,Debt 2.146bn->1.532bn 2024-25 partly delayed capex; improving since 2022 faster than plan,strong,src_nmbs_results_2025_page,Taxpayers passengers,PSO balance sheet,Capex deferral vs structural improvement split,3,7.0,4,5.2,Track when deferred MR30/stations hit cash,seed,,tick160",
    "lb_vdab_staff_budget,VDAB staff 4761 and budget class 962m 2024,regional,ops,Vlaanderen>VDAB>2024,962000000,962000000,JV strong staff -230; PQ medium 962m total 783m VL dots; BBT 2026 VEK 750.7m,medium,src_vdab_jv_2024,Jobseekers employers,PES Flanders,Dual PES stack; FOI jaarrekening L5,3,7.0,4,5.2,Open jaarrekening full; tender L5; dual FOREM compare,seed,,tick160",
]
append_if_missing(DATA / "leaderboard.csv", lbs)

# Update FOI gaps notes (partial fill)
def update_foi_notes(gap_id: str, note_suffix: str) -> None:
    text = read_text(DATA / "foi_queue.csv")
    lines = text.splitlines()
    out = []
    for L in lines:
        if L.startswith(gap_id + ","):
            # append note at end if not already
            if "tick160" not in L:
                L = L.rstrip() + " " + note_suffix
            out.append(L)
        else:
            out.append(L)
    write_text(DATA / "foi_queue.csv", "\n".join(out) + "\n")


update_foi_notes(
    "gap_nmbs_annual_toelage",
    "|tick160: 2025 results filled EBITDA/debt/invest; residual absolute FPS cash codes still ready human send",
)
update_foi_notes(
    "gap_vdab_full_budget",
    "|tick160: staff+PMO from JV2024; 962/783 medium PQ; residual jaarrekening L5 still ready human send",
)

# rq_121 done as batch tick (one unit of hole-fill batch)
rq_new = (
    f"rq_121,Fill high-value FOI-adjacent public holes batch,continuous,5,done,L5,gg_belgium,"
    f'"Prefer public primary fills for ready FOI topics if new PDFs appear (NMBS De Lijn VDAB FOREM); else pick next open rq by prio.",,'
    f"2026-07-27T12:00:00Z,{UTC},"
    "tick160: NMBS 2025 invest 820m EBITDA 54.2m debt 1.53bn; VDAB staff 4761 + 962/783 medium; "
    "gaps nmbs/vdab partial; FOREM/De Lijn 2025-26 still FOI; spawn next hole-fill if needed"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_121,", rq_new):
    raise SystemExit("rq_121 not found")

# Seed next continuous hole-fill so queue not empty except deferred SWA
seed = (
    f"rq_152,FOI-adjacent public hole-fill batch 2 (FOREM De Lijn Antwerp),continuous,5,open,L5,gg_belgium,"
    f'"Continue hole-fill: FOREM RA2024-26 if published; De Lijn full 2025-26 perimeter; Antwerp register if appears; else large FOI residual public slices.",,'
    f"{UTC},{UTC},Spawned tick160 after rq_121; keep continuous mode"
)
text_rq = read_text(DATA / "research_queue.csv")
if "rq_152," not in text_rq:
    if not text_rq.endswith("\n"):
        text_rq += "\n"
    write_text(DATA / "research_queue.csv", text_rq + seed + "\n")

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio5 rq_152 hole-fill FOREM/De Lijn/Antwerp; rq_116 SWA deferred. FOI ready human send. rq_121 NMBS+VDAB fill done."\n',
)

log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill batch — NMBS 2025 + VDAB 2024)
- Found:
  - **NMBS 2025 (strong official):** EBITDA **EUR 54.2m** (was 131.6m) · economic debt **1.532bn** (was 2.146bn) · invest **>820m** (rolling **350** · stations **213** · digital **152** · workshops **89**) · ODC path hyp **−100m** vs 2025 contractual assumptions · rail sector savings demand **675m 2025-29** · staff **16,976** · passengers **207.8m** · punctuality **91.7%**.
  - **VDAB 2024:** staff **4,761** (−230) strong JV · institutional total **962m** / VL dots **783m** medium (VP PQ premise; minister → jaarrekening) · PMO ~**160m** project means since 2019.
  - FOREM 2024-26 RA and De Lijn full 2025-26 perimeter still not newly filled this tick.
- Wrote: sources 3; budgets ~18; cmt 2; lb 3; FOI gaps nmbs/vdab notes partial; rq_121=done; seeded **rq_152**.
- FOI: gap_nmbs / gap_vdab still **ready** residual human send; FOREM/De Lijn ready.
- Next: prio5 **rq_152** · deferred **rq_116** SWA.
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)
print("OK tick", TICK, UNIT)

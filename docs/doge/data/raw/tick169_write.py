# -*- coding: utf-8 -*-
"""Tick 169: CREG OSP federal GC + CRM costs; Elia CRM auction package."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T06:25:00Z"
TICK = 169
UNIT = "rq_164"


def append_lines(path: Path, lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def replace_line_startswith(path: Path, prefix: str, new_line: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    found = False
    for line in lines:
        if line.startswith(prefix):
            out.append(new_line if new_line.endswith("\n") else new_line + "\n")
            found = True
        else:
            out.append(line)
    if not found:
        raise SystemExit(f"prefix not found: {prefix}")
    path.write_text("".join(out), encoding="utf-8", newline="\n")


append_lines(
    DATA / "sources.csv",
    [
        "src_creg_ar2025_osp,CREG AR2025 federal OSP GC and CRM cost evaluations,"
        "https://www.creg.be/sites/default/files/assets/Publications/AnnualReports/CREG-AR2025-FR.pdf,"
        "CREG,2026-07-28,official_annual_report,"
        '"GC OSP est 675.707m 2025 / 551.352m 2026; CRM OSP est 169.917m (B2893 for 2025 year); '
        'H2-2024 State to Elia 39.5m GC; H1-2025 Elia to State 110.4m; CRM surplus 2024 3.0m; tick169"',
        "src_elia_crm_auction_2025_10,Elia CRM auction results Oct 2025 press,"
        "https://www.elia.be/en/newsroom/2025/10/20251030_elia-publishes-crm-auction-results,"
        "Elia Transmission Belgium,2026-07-28,official_press,"
        '"Oct 2025 Y-1 Y-2 Y-4 simultaneous auctions total cost 125.4m (20.2k/MW) vs prior 182.9m; '
        'WAP 14.1k/MW/y; 4556 MW selected 171 MW new; tick169 medium pending full results PDF"',
    ],
)

append_lines(
    DATA / "budgets.csv",
    [
        "bud_fed_gc_osp_est_2025,sec_federal,2025,675707187,,,budgeted,src_creg_ar2025_osp,strong,"
        "CREG est OSP federal green certificates financing 675.707m for 2025",
        "bud_fed_gc_osp_est_2026,sec_federal,2026,551351856,,,budgeted,src_creg_ar2025_osp,strong,"
        "CREG est OSP federal GC financing 551.352m for 2026 (-125.355m vs 2025 est; higher ref power price)",
        "bud_fed_gc_osp_h2_2024_state_to_elia,sec_federal,2024,39527505,,,outturn,src_creg_ar2025_osp,strong,"
        "State paid Elia 39.528m for federal GC OSP balance H2-2024",
        "bud_fed_gc_osp_h1_2025_elia_to_state,sec_federal,2025,110411019,,,outturn,src_creg_ar2025_osp,strong,"
        "Elia repaid State 110.411m federal GC OSP balance H1-2025",
        "bud_crm_osp_est_2025,sec_federal,2025,169916607,,,budgeted,src_creg_ar2025_osp,strong,"
        "CREG est OSP CRM financing 169.917m (dec B2893; AR text cites with 2026 study line - year 2025 per footnote)",
        "bud_crm_adequacy_study_2026,sec_federal,2026,621668,,,budgeted,src_creg_ar2025_osp,strong,"
        "Biennial adequacy and flexibility study OSP cost 0.622m",
        "bud_crm_surplus_2024,sec_federal,2024,2991337.74,,,outturn,src_creg_ar2025_osp,strong,"
        "CRM OSP surplus 2024 Elia to repay State 2.991m",
        "bud_strategic_reserve_surplus_2024,sec_federal,2024,32953.67,,,outturn,src_creg_ar2025_osp,strong,"
        "Strategic reserve OSP surplus 2024 32.954k Elia to State",
        "bud_crm_auction_package_2025_10,sec_federal,2025,125400000,,,outturn,src_elia_crm_auction_2025_10,medium,"
        "Elia Oct 2025 CRM multi-auction (Y-1/Y-2/Y-4) total cost 125.4m (press)",
        "bud_crm_auction_package_prior_yr,sec_federal,2024,182900000,,,outturn,src_elia_crm_auction_2025_10,medium,"
        "Prior year CRM auction package cost 182.9m (Elia press compare)",
        "bud_crm_auction_mw_2025_10,sec_federal,2025,4556,,,outturn,src_elia_crm_auction_2025_10,medium,"
        "CRM Oct 2025 selected capacity 4556 MW of which 171 MW new",
        "bud_crm_auction_wap_2025_10,sec_federal,2025,14100,,,outturn,src_elia_crm_auction_2025_10,medium,"
        "CRM weighted avg price 14.1k EUR/MW/year Oct 2025 (IPC 22.7k)",
    ],
)

append_lines(
    DATA / "commitments.csv",
    [
        'cmt_fed_gc_osp_elia_path,Federal green certificates OSP financing via Elia multi-year,sec_federal,'
        "Offshore and federal GC system Elia consumers,Electricity law OSP + CREG annual cost eval,"
        "2024-01-01,2024,2026,675707187,"
        '"{""est_2025"":675707187,""est_2026"":551351856,""delta_2026_vs_2025"":-125355331,'
        '""ref_price_2025_eur_mwh"":58.02,""ref_price_2026_eur_mwh"":87.56,'
        '""h2_2024_state_to_elia"":39527505,""h1_2025_elia_to_state"":110411019,'
        '""related_offshore_support_2025"":538500000,'
        '""note"":""OSP tariff estimate for GC purchase financing; related but not identical to CREG support cost 538.5m 2025""}",'
        "0,active,https://www.creg.be/sites/default/files/assets/Publications/AnnualReports/CREG-AR2025-FR.pdf,"
        "Finance federal green certificate purchases,"
        "Publish multi-year outturn vs estimate; align with offshore support series,"
        "src_creg_ar2025_osp,strong,Federal>Energy>GC_OSP,"
        "tick169 dual with offshore support",
        'cmt_crm_belgium_package,Belgium Capacity Remuneration Mechanism multi-year,sec_federal,'
        "Capacity providers Elia consumers,Electricity law CRM + reliability options auctions,"
        "2021-10-01,2024,2030,169916607,"
        '"{""osp_est_2025"":169916607,""auction_package_2025_10"":125400000,""auction_package_prior"":182900000,'
        '""mw_selected_2025_10"":4556,""mw_new_2025_10"":171,""wap_eur_mw_y"":14100,""ipc_eur_mw_y"":22700,'
        '""surplus_2024"":2991337.74,""delivery_y1"":""2026-2027"",'
        '""note"":""OSP est is tariff financing cost; auction package is cleared multi-horizon cost from Elia press""}",'
        "0,active,https://www.creg.be/sites/default/files/assets/Publications/AnnualReports/CREG-AR2025-FR.pdf,"
        "Security of supply capacity after nuclear phase-out,"
        "Publish annual OSP outturn and auction L5 winners; track battery share,"
        "src_creg_ar2025_osp,strong,Federal>Energy>CRM,"
        "tick169; residual auction L5 FOI optional",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_fed_gc_osp_551m,Federal green certificate OSP via Elia ~551-676m/yr,federal,subsidy,"
        "Federal>Energy>GC_OSP,551351856,675707187,"
        "CREG strong: est 675.7m 2025 / 551.4m 2026; dual offshore support 538.5m 2025,"
        "strong,src_creg_ar2025_osp,Electricity consumers,"
        "Finance federal GC purchases (offshore class),"
        "Overlaps offshore support; not pure waste (RES); tariff recovery opacity,"
        "5,9.5,7,7.3,"
        "Reconcile OSP est vs CREG support cost; multi-year outturn,"
        "seed,,tick169",
        "lb_crm_osp_170m,Belgium CRM capacity mechanism ~126-183m auction / ~170m OSP,federal,subsidy,"
        "Federal>Energy>CRM,125400000,182900000,"
        "CREG OSP est 169.9m 2025 strong; Elia Oct2025 auction package 125.4m medium (was 182.9m),"
        "strong,src_creg_ar2025_osp,Electricity consumers capacity providers,"
        "Capacity remuneration security of supply,"
        "Not pure waste (adequacy); design cost debates; dual OSP vs auction metrics,"
        "5,9.0,7,7.0,"
        "Publish annual OSP outturn; auction winner L5; battery vs gas mix,"
        "seed,,tick169",
    ],
)

# entities elia if missing
ent = (DATA / "entities.csv").read_text(encoding="utf-8")
if "\nelia," not in ent and not ent.startswith("elia,"):
    append_lines(
        DATA / "entities.csv",
        [
            "elia,Elia Transmission Belgium,Elia Transmission Belgium,Elia Belgian TSO,"
            "parastatal,sec_federal,bi,https://www.elia.be,,"
            "Brussels,"
            "Federal electricity TSO; hosts CRM auctions and federal GC OSP cash; tick169",
        ],
    )

# FOI: optional residual for CRM multi-year OSP outturn series
foi = (DATA / "foi_queue.csv").read_text(encoding="utf-8")
if "gap_crm_osp_series" not in foi:
    append_lines(
        DATA / "foi_queue.csv",
        [
            "gap_crm_osp_series,Federal>Energy>CRM>OSP_cash_series,elia,"
            "Cash-by-year CRM OSP cost outturn vs estimate 2022-2026 with CREG decision refs; "
            "auction clearing cost by delivery year Y-1/Y-2/Y-4 2021-2025; winner list top capacities,"
            "2025 OSP est 169.9m and Oct2025 auction 125.4m public; multi-year matrix incomplete,"
            "5,CREG / Elia / FOD Economie / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
            "docs/doge/foi/drafts/gap_crm_osp_series.md,draft,,,,,,,"
            "cmt_crm_belgium_package,lb_crm_osp_170m,"
            f"{TS},{TS},tick169 draft pending",
        ],
    )

# draft letter
draft = ROOT / "foi" / "drafts" / "gap_crm_osp_series.md"
draft.write_text(
    f"""# FOI draft — gap_crm_osp_series

**Status:** draft (complete for human review)  
**Gap ID:** gap_crm_osp_series  
**Tick:** {TICK}  
**Do not send as agent** — human only.

---

**Betreft:** Openbaarheid — CRM en federale OSP-kosten Elia/CREG 2022-2026

Geachte,

In het kader van de openbaarheid van bestuur verzoek ik om:

1. **Cash-by-year** kost van de openbaredienstverplichting (OSP) voor de financiering van het **Capacity Remuneration Mechanism (CRM)** 2022–2026 (raming vs uitkomst), met verwijzing naar CREG-beslissingen (o.a. B2893 en opvolgers).

2. **Veilingresultaten** Y-1 / Y-2 / Y-4 2021–2025: totale kost per leveringsjaar, gewogen gemiddelde prijs EUR/MW/jaar, geselecteerd vermogen (MW), waarvan nieuwbouw.

3. **Top 20** geselecteerde capaciteiten (CMU) per veiling met vermogen en vergoeding (of bevestiging dat de openbare Elia-resultaten PDF alle L5 bevat).

Reeds publiek (CREG AR2025 / Elia pers): OSP-CRM-raming ca. **EUR 169,9m (2025)**; veilingpakket okt. 2025 ca. **125,4m** (vs 182,9m vorig jaar).

Gelieve digitaal te antwoorden binnen de wettelijke termijn.

Met vriendelijke groet,  
[Naam — menselijke afzender]  
[Contact]

---
## Agent notes
- Draft ready for human polish → set status ready when complete.
""",
    encoding="utf-8",
    newline="\n",
)

replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_crm_osp_series,",
    "gap_crm_osp_series,Federal>Energy>CRM>OSP_cash_series,elia,"
    "Cash-by-year CRM OSP cost outturn vs estimate 2022-2026 with CREG decision refs; "
    "auction clearing cost by delivery year Y-1/Y-2/Y-4 2021-2025; winner list top capacities,"
    "2025 OSP est 169.9m and Oct2025 auction 125.4m public; multi-year matrix incomplete,"
    "5,CREG / Elia / FOD Economie / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_crm_osp_series.md,ready,2026-07-28,,,,,"
    "cmt_crm_belgium_package,lb_crm_osp_170m,"
    f"{TS},{TS},tick169 draft ready human send\n",
)

# also update gap_offshore note that GC OSP is dual financing path
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_offshore_annual_cash,",
    "gap_offshore_annual_cash,Federal>Energy>offshore_wind>annual,sec_federal,"
    "Reconcile CREG support cost (538.5m 2025) vs federal GC OSP Elia financing est (675.7m 2025 / 551.4m 2026) vs NBB ESA D.31 "
    "(592m 2024); publish same-method annual series 2020-2024,"
    "2025 support+OSP est filled strong tick168-169; multi-year ESA dual still residual,"
    "6,FOD Economie AD Energie / CREG / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_offshore_annual_cash.md,ready,2026-07-20,,,,,"
    "cmt_offshore_support_creg_2025|cmt_fed_gc_osp_elia_path,lb_offshore_support_538m,"
    "2026-07-20T02:40:00Z,2026-07-28T06:25:00Z,"
    "tick168 support |tick169 GC OSP path; residual multi-year+NBB human send\n",
)

replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_164,",
    "rq_164,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex updates large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_crm_osp_series,2026-07-28T06:05:00Z,2026-07-28T06:25:00Z,"
    '"tick169: CREG GC OSP est 675.7/551.4m 2025-26 + CRM OSP 169.9m + Elia auction 125.4m; Mons/Antwerp still FOI; spawn rq_165"\n',
)

rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_165," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_165,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T06:25:00Z,,"
            '"Spawned tick169 after CRM/GC OSP; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_165 hole-fill Antwerp/Mons/taxex/other; rq_116 SWA deferred. FOI ready human send. tick169 CRM+GC OSP."\n',
    encoding="utf-8",
    newline="\n",
)

log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **CREG federal GC OSP + CRM costs**)
- Found (strong CREG AR2025 §3.1.3.5; medium Elia auction press):
  - **Federal GC OSP financing (Elia):** est **EUR 675.707m 2025** → **551.352m 2026** (−125.4m; higher power ref price 87.56 vs 58.02 €/MWh).
  - Settlements: State→Elia **39.5m** H2-2024; Elia→State **110.4m** H1-2025.
  - Dual with offshore support **538.5m 2025** (tick168): same family, different metric.
  - **CRM OSP est:** **169.917m** (B2893; 2025 year per footnote).
  - CRM 2024 surplus **2.991m** repaid to State; strategic reserve residual tiny.
  - **Elia Oct 2025 auctions** (Y-1/Y-2/Y-4): package cost **125.4m** (was **182.9m**); **4 556 MW** (171 new); WAP **14.1k €/MW/y**.
- Mons BI2026 / Antwerp full register still not newly filled.
- Wrote: sources 2; entity 1; budgets 12; cmt 2; lb 2; FOI **gap_crm_osp_series** ready; gap_offshore note; rq_164=done; seeded **rq_165**.
- FOI: CRM multi-year + residual Mons/Antwerp human send.
- Next: prio5 **rq_165**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")
print("tick169 OK")

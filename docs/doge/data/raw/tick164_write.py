# -*- coding: utf-8 -*-
"""Tick 164: bpost SGEI remuneration package from Consolidated AR 2024."""
from pathlib import Path
from datetime import datetime, timezone

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent  # docs/doge
TS = "2026-07-28T04:45:00Z"
TICK = 164
UNIT = "rq_159"


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


# --- sources ---
append_lines(
    DATA / "sources.csv",
    [
        "src_bpost_ar2024_consol,bpostgroup Consolidated annual accounts 2024 ENG,"
        "https://bpostgroup.com/sites/default/files/2025-04/9.%20Consolidated_annual_accounts_bpostgroup_2024_ENG.pdf,"
        "bpostgroup,2026-07-28,official_annual_report,"
        '"SGEI rem 227.8m 2024 / 311.9m 2023 (note 6.7); press SGEI until 2024-06-30; USO mgmt contract to 2028; '
        'overcomp provision 75m prior years; State 9.5pct op income incl SGEI; tick164"'
    ],
)

# --- budgets ---
append_lines(
    DATA / "budgets.csv",
    [
        "bud_bpost_sgei_rem_2024,bpost,2024,227800000,,,outturn,src_bpost_ar2024_consol,strong,"
        "SGEI remuneration State to bpost 227.8m 2024 (consol AR note 6.7)",
        "bud_bpost_sgei_rem_2023,bpost,2023,311900000,,,outturn,src_bpost_ar2024_consol,strong,"
        "SGEI remuneration State to bpost 311.9m 2023",
        "bud_bpost_sgei_delta_2024,bpost,2024,-84100000,,,outturn,src_bpost_ar2024_consol,strong,"
        "SGEI rem y/y delta -84.1m 2024 vs 2023 (press end + contract path)",
        "bud_bpost_op_income_2024,bpost,2024,4341300000,,,outturn,src_bpost_ar2024_consol,strong,"
        "Total operating income group 4.3413bn 2024",
        "bud_bpost_rev_ex_sgei_2024,bpost,2024,4100900000,,,outturn,src_bpost_ar2024_consol,strong,"
        "Revenue excluding SGEI remuneration 4.1009bn 2024",
        "bud_bpost_rev_ex_sgei_2023,bpost,2023,3945700000,,,outturn,src_bpost_ar2024_consol,strong,"
        "Revenue excluding SGEI remuneration 3.9457bn 2023",
        "bud_bpost_state_share_opinc_2024,bpost,2024,9.5,,,outturn,src_bpost_ar2024_consol,strong,"
        "Belgian State + related entities share of total operating income 9.5pct 2024 incl SGEI",
        "bud_bpost_overcomp_provision_2023,bpost,2023,75000000,,,outturn,src_bpost_ar2024_consol,strong,"
        "Provision 75.0m potential overcompensation years prior 2023 (repay commitment)",
        "bud_bpost_sgei_receivable_eoy2023,bpost,2023,74600000,,,outturn,src_bpost_ar2024_consol,strong,"
        "SGEI receivable outstanding end-2023 74.6m; fully settled end-2024",
        "bud_bpost_esa_d31_minus_sgei_2024,bpost,2024,101200000,,,outturn,src_bpost_ar2024_consol,medium,"
        "Implied residual: NBB ESA D.31 329m minus SGEI rem 227.8m = 101.2m perimeter gap 2024",
        "bud_bpost_esa_d31_minus_sgei_2023,bpost,2023,12100000,,,outturn,src_bpost_ar2024_consol,medium,"
        "Implied residual: NBB ESA D.31 324m minus SGEI rem 311.9m = 12.1m 2023",
    ],
)

# --- commitments ---
append_lines(
    DATA / "commitments.csv",
    [
        'cmt_bpost_sgei_package_2023_24,bpost federal SGEI remuneration package multi-year,bpost,bpost Belgian State,'
        "7th management contract SGEI + press concessions + USO management contract,"
        "2016-01-01,2023,2028,227800000,"
        '"{""2023_sgei"":311900000,""2024_sgei"":227800000,""delta_2024"":-84100000,'
        '""press_end"":""2024-06-30"",""uso_contract_end"":""2028-12-31"",""uso_contract_signed"":""2023-11-09"",'
        '""nac_method"":true,""overcomp_provision_2023"":75000000,'
        '""sgei_receivable_eoy2023"":74600000,""sgei_receivable_eoy2024"":0,'
        '""state_share_opinc_2024_pct"":9.5,""op_income_2024"":4341300000,'
        '""rev_ex_sgei_2024"":4100900000,""rev_ex_sgei_2023"":3945700000,'
        '""nbb_d31_2024"":329000000,""nbb_d31_2023"":324000000,'
        '""sgei_components"":""retail_network_1300pts+cash_counter+pensions+ad_hoc+press_until_2024-06"",'
        '""note"":""SGEI rem is cash compensation package; pure USO may be tariff-financed; NBB D.31 wider perimeter""}",'
        "0,active,https://bpostgroup.com/sites/default/files/2025-04/9.%20Consolidated_annual_accounts_bpostgroup_2024_ENG.pdf,"
        "Universal postal + retail network + residual press SGEI,"
        "Publish cash split USO vs retail/cash/pensions vs press residual; reconcile NBB ESA,"
        "src_bpost_ar2024_consol,strong,Federal>bpost>SGEI,"
        "tick164: primary consol AR; residual L5 split FOI",
    ],
)

# --- leaderboard ---
append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_bpost_sgei_rem,bpost SGEI remuneration 228-312m/yr,federal,subsidy,Federal>bpost>SGEI,"
        "227800000,311900000,"
        "AR strong: 227.8m 2024 / 311.9m 2023; press SGEI ended mid-2024; dual with NBB ESA D.31 329m,"
        "strong,src_bpost_ar2024_consol,Postal users retail network,"
        "SGEI public service compensation NAC,"
        "Not pure waste; opacity on USO vs retail/cash/press split; overcomp risk,"
        "6,9.0,7,7.2,"
        "Open annual L5 split by SGEI; finish press phase-out savings tracking,"
        "seed,,tick164",
        "lb_bpost_sgei_vs_esa_gap,bpost SGEI vs NBB ESA D.31 residual ~101m 2024,federal,subsidy,"
        "Federal>bpost>ESA_vs_SGEI,101200000,101200000,"
        "Medium: NBB D.31 329m - AR SGEI 227.8m; 2023 gap only 12m; dual accounting perimeter,"
        "medium,src_bpost_ar2024_consol,Taxpayers,"
        "Reconcile product subsidies vs management-contract cash,"
        "Opacity risk if residual is other contracts/press cash timing,"
        "7,8.0,6,6.8,"
        "FOI FPS cash codes by article; publish dual series,"
        "seed,,tick164",
    ],
)

# --- entities note touch for bpost if exists ---
# skip full rewrite; optional one-line via notes in commitments

# --- FOI gap_bpost_uso_split update ---
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_bpost_uso_split,",
    "gap_bpost_uso_split,Federal>bpost>USO_vs_press,bpost,"
    "Cash-by-year L5 split inside SGEI rem 227.8m/311.9m: pure USO net cost (if any cash) vs retail network vs cash-at-counter vs pensions/ad-hoc vs press residual 2020-2026; FPS budget article codes; reconcile NBB ESA D.31 329/324m residual ~101m/12m,"
    "SGEI package totals now public strong AR; press end mid-2024; component L5 and ESA residual still opaque,"
    "7,FOD Economie / BIPT / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_bpost_uso_split.md,ready,2026-07-20,,,,,"
    "cmt_bpost_sgei_package_2023_24,lb_bpost_sgei_rem,"
    "2026-07-20T02:20:00Z,2026-07-28T04:45:00Z,"
    "rq_028 |tick164: AR SGEI 227.8/311.9m filled; residual L5+ESA gap human send\n",
)

# --- research_queue ---
replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_159,",
    "rq_159,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026 bpost USO HR Rail FWB univ dots) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_bpost_uso_split,2026-07-28T04:25:00Z,2026-07-28T04:45:00Z,"
    '"tick164: bpost consol AR2024 SGEI rem 227.8m 2024 / 311.9m 2023; press SGEI to 2024-06-30; USO contract to 2028; overcomp 75m; NBB gap ~101m; residual L5 FOI; spawn rq_160"\n',
)

# append rq_160 if missing
rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_160," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_160,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026 HR Rail FWB univ dots) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T04:45:00Z,,"
            '"Spawned tick164 after bpost SGEI AR; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

# --- loop_state ---
(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_160 hole-fill De Lijn/Antwerp/VIPA/Mons/HR Rail/FWB univ; rq_116 SWA deferred. FOI ready human send. tick164 bpost SGEI AR."\n',
    encoding="utf-8",
    newline="\n",
)

# --- loop_log ---
log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **bpost Consolidated AR 2024 SGEI package**)
- Found (strong primary consol AR PDF, note 6.7 + related-party):
  - **SGEI remuneration:** **EUR 227.8m 2024** / **311.9m 2023** (−84.1m y/y).
  - Method: net avoided cost (NAC); 7th management contract SGEIs (retail network ≥1300 points, cash-at-counter, pensions, ad-hoc) + press newspapers/periodicals **until 2024-06-30**.
  - **USO:** dedicated management contract signed **2023-11-09**, USO provider to **2028-12-31** (tariff/regulatory; not equal to SGEI cash line).
  - Op. income **4.341bn**; rev ex-SGEI **4.101bn** / 3.946bn; State share **9.5%** of op. income incl SGEI.
  - Overcompensation provision **75.0m** (prior years, 3 services); SGEI receivable **74.6m** eoy2023 → **0** eoy2024.
  - Dual series: NBB ESA D.31 **329m** 2024 vs SGEI **227.8m** → residual **~101m** medium perimeter gap (2023 gap only ~12m).
- Wrote: sources 1; budgets 11; cmt 1; lb 2; gap_bpost notes partial prio7; rq_159=done; seeded **rq_160**.
- FOI: gap_bpost residual L5 SGEI components + ESA residual still **ready** human send.
- Next: prio5 **rq_160**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")

print("tick164 write OK")

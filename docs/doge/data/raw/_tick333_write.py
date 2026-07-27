# tick 333: BELSPO budget 2024 primary L2 split (AR figures)
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

def append(path: Path, text: str):
    with path.open("a", encoding="utf-8", newline="\n") as f:
        if path.stat().st_size > 0:
            with path.open("rb") as rb:
                rb.seek(-1, 2)
                if rb.read(1) != b"\n":
                    f.write("\n")
        f.write(text if text.endswith("\n") else text + "\n")

append(DATA / "sources.csv", """src_belspo_ar2024_figures,BELSPO Jaarverslag 2024 cijfers begroting realisaties L2 split,https://www.belspo.be/belspo/organisation/report-2024/figures-trends_nl.stm,BELSPO,2026-07-31,official_annual_report,"Strong: budget realisations 2024 582.4m; space 283.4m; ADBA+ION FWI Belnet Polar Cinematek 162.6m; mgmt organs 19.4m (pers 16.9m 3pct); nat+int RDI 56.5m; PRT 15.7m; EU fund prog5 26.9m; museums >1.5m visitors; tick333"
""")

append(DATA / "budgets.csv", """bud_belspo_total_2024,belspo,2024,582400000,,,outturn,src_belspo_ar2024_figures,strong,Budgettaire realisaties 2024 582.4m (AR figures primary)
bud_belspo_space_2024,belspo,2024,283400000,,,outturn,src_belspo_ar2024_figures,strong,Ruimtevaartbudget 283.4m nearly half of Belspo 2024; dual ESA 284m 2025 MERI
bud_belspo_adba_ion_2024,belspo,2024,162600000,,,outturn,src_belspo_ar2024_figures,strong,ADBA+ION envelope 162.6m: FWI Belnet Poolsecretariaat Koninklijk Belgisch Filmarchief
bud_belspo_mgmt_organs_2024,belspo,2024,19400000,,,outturn,src_belspo_ar2024_figures,strong,Beheersorganen 19.4m (3pct) of which personnel 16.9m
bud_belspo_mgmt_pers_2024,belspo,2024,16900000,,,outturn,src_belspo_ar2024_figures,strong,Personeelskosten beheersorganen 16.9m 2024
bud_belspo_rdi_nat_int_2024,belspo,2024,56500000,,,outturn,src_belspo_ar2024_figures,strong,Nationale en internationale R&D programma's en acties 56.5m ~10pct
bud_belspo_prt_2024,belspo,2024,15700000,,,outturn,src_belspo_ar2024_figures,strong,PRT Herstart- en Transitieplan projecten ending 31Dec2024 15.7m (subset RDI)
bud_belspo_eu_fund_prog5_2024,belspo,2024,26900000,,,outturn,src_belspo_ar2024_figures,strong,EU research programmes fund prog5 section 60 exp 26.9m 2024 (extra federal budget)
""")

append(DATA / "commitments.csv", """cmt_belspo_budget_2024_split,BELSPO budget 2024 primary L2 split dual space FWI,belspo,FWI Belnet Polar Cinematek ESA RDI SCK Myrrha VKI,BELSPO annual report figures + federal budget section 60,2024-01-01,2024,2024,582400000,"{""total_2024_m"":582.4,""space_m"":283.4,""adba_ion_m"":162.6,""mgmt_organs_m"":19.4,""mgmt_pers_m"":16.9,""mgmt_share_pct"":0.03,""rdi_nat_int_m"":56.5,""prt_m"":15.7,""rdi_ex_prt_class_pct"":0.07,""diverse_subs_ex_space_pct"":0.10,""eu_fund_prog5_m"":26.9,""museum_visitors_gt_m"":1.5,""note"":""Primary AR 2024 outturn tightens prior 570-630m class; space aligns ESA 284m 2025; diverse subs include SCK Myrrha VKI nuclear/hydrogen; L5 per FWI residual FOI""}",0,active,https://www.belspo.be/belspo/organisation/report-2024/figures-trends_nl.stm,Federal science policy space FWI museums research,Publish L5 cash per FWI and reconcile cut 93m path 2025-26,src_belspo_ar2024_figures,strong,Federal>BELSPO>budget_2024,tick333: 582.4m total space 283.4m FWI envelope 162.6m
""")

append(DATA / "leaderboard.csv", """lb_belspo_582m_2024,BELSPO budget realisations 582.4m 2024 dual space FWI,federal,ops,Federal>BELSPO>budget,582400000,582400000,Strong AR2024: total 582.4m; space 283.4m; ADBA+ION 162.6m; mgmt 19.4m; RDI 56.5m; EU fund 26.9m extra; dual ESA MERI 284m 2025,strong,src_belspo_ar2024_figures,Science ecosystem space industry museums,Federal science policy coordination,Core mandate not pure waste; cut 93m path risk; L5 FWI residual FOI,3,8.5,5,6.55,FOI per-FWI cash; track post-cut 2025; dual community research,seed,,tick333 replaces class 630m with strong outturn
""")

# Update prior belspo commitment note lightly via entity
ent_path = DATA / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
old_note = "Managed budget ~570-630m; ESA 284m 2025; RV Belgica capital 54.45m; FWI ~25pct; cut 93m; dual community research; tick329-332"
new_note = "Budget 2024 strong 582.4m (space 283.4 ADBA+ION 162.6 RDI 56.5); ESA 284m 2025; Belgica 54.45m; cut 93m; dual community; tick329-333"
if old_note in ent:
    ent_path.write_text(ent.replace(old_note, new_note), encoding="utf-8")
else:
    print("WARN belspo entity note")

# FOI: update gap_belspo_fwi with new totals, keep ready
foi_path = DATA / "foi_queue.csv"
foi = foi_path.read_text(encoding="utf-8")
old_foi = "Aggregates strong FRWB+Kamer; L5 per institute and cut implementation residual,6,BELSPO / POD Wetenschapsbeleid / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,docs/doge/foi/drafts/gap_belspo_fwi_l5_cut.md,ready,2026-07-31,,,,,cmt_belspo_science_path_2024_25,lb_belspo_630m,2026-07-31T03:15:00Z,2026-07-31T03:15:00Z,tick329 draft ready | tick331: ESA 284m 2025 filled public; residual FWI L5 + optional ESA still human send"
new_foi = "AR2024 total 582.4m space 283.4 ADBA+ION 162.6 strong; L5 per institute and cut 93m path residual,6,BELSPO / POD Wetenschapsbeleid / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,docs/doge/foi/drafts/gap_belspo_fwi_l5_cut.md,ready,2026-07-31,,,,,cmt_belspo_budget_2024_split|cmt_belspo_science_path_2024_25,lb_belspo_582m_2024|lb_belspo_630m,2026-07-31T03:15:00Z,2026-07-31T05:15:00Z,tick329 draft | tick331 ESA filled | tick333 AR2024 582.4m split; residual FWI L5 + cut path human send"
if old_foi in foi:
    foi_path.write_text(foi.replace(old_foi, new_foi), encoding="utf-8")
else:
    print("WARN foi update skipped")
    append(DATA / "foi_queue.csv", """gap_belspo_fwi_l5_cut_refresh,Federal>BELSPO>FWI_L5_and_cut_path,belspo,Cash-by-year 2024-2026 per 10 FWI + Belnet base vs ADBA+ION 162.6m 2024; post-cut after 93m-15pct; BA codes,AR2024 L2 split strong; L5 per institute residual,6,BELSPO / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,docs/doge/foi/drafts/gap_belspo_fwi_l5_cut.md,ready,2026-07-31,,,,,cmt_belspo_budget_2024_split,lb_belspo_582m_2024,2026-07-31T05:15:00Z,2026-07-31T05:15:00Z,tick333 note refresh if prior row mismatch
""")

# research queue
rq_path = DATA / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = "rq_324,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T04:45:00Z,,Spawned tick332 after Belgica II; rq_116 SWA deferred"
new = "rq_324,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_belspo_fwi_l5_cut,2026-07-31T04:45:00Z,2026-07-31T05:15:00Z,tick333: BELSPO AR2024 582.4m space 283.4m ADBA+ION 162.6m dual; FOI FWI L5 residual; spawn rq_325"
if old not in rq:
    raise SystemExit("rq_324 open not found")
rq = rq.replace(old, new)
if "rq_325," not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += "rq_325,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T05:15:00Z,,Spawned tick333 after Belspo AR2024 split; rq_116 SWA deferred\n"
rq_path.write_text(rq, encoding="utf-8")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T05:15:00Z,rq_324,333,no,Scheduler 60s. Next prio5 rq_325; rq_116 SWA deferred. FOI ready. tick333 BELSPO AR2024 582.4m L2 split.\n",
    encoding="utf-8",
)

# Refresh FOI draft context with 582.4m numbers (append note if exists)
draft = FOI / "gap_belspo_fwi_l5_cut.md"
if draft.exists():
    text = draft.read_text(encoding="utf-8")
    if "582,4" not in text and "582.4" not in text:
        text += """
---

## Update tick 333

BELSPO Jaarverslag 2024 (figures) primary:
- **Budgettaire realisaties 2024: €582,4 m**
- Ruimtevaart: **€283,4 m**
- ADBA + ION (FWI, Belnet, Poolsecretariaat, Filmarchief): **€162,6 m**
- Beheersorganen: **€19,4 m** (personeel €16,9 m; 3%)
- Nat./int. R&D: **€56,5 m** (PRT €15,7 m aflopend 2024)
- EU-fonds prog.5: **€26,9 m** (extra)
- Residual FOI: L5 per FWI + cut path €93 m (−15%)
"""
        draft.write_text(text, encoding="utf-8")
else:
    print("WARN draft missing")

append(LOG, """
### 2026-07-31T05:15:00Z - tick 333
- Unit: **rq_324** (FOI-adjacent hole-fill - **BELSPO AR2024 budget L2 primary split**)
- Found (strong BELSPO Jaarverslag 2024 figures page):
  - Budgettaire realisaties **€582.4m** 2024 (tightens prior 570-630m class).
  - Space **€283.4m** (~half; dual ESA MERI €284m 2025).
  - ADBA+ION (FWI Belnet Polar Cinematek) **€162.6m** (>25%).
  - Mgmt organs **€19.4m** (3%; personnel **€16.9m**).
  - Nat+int RDI **€56.5m** (~10%); PRT ending 2024 **€15.7m**.
  - Diverse subsidies ex-space ~10% (SCK Myrrha VKI nuclear/H2 class).
  - EU research fund prog5 **€26.9m** exp 2024 (extra federal budget).
  - Museums **>1.5m** visitors 2024.
- Wrote: sources +1; budgets +8; cmt +1; lb +1; entity belspo note; FOI gap_belspo refresh; draft note; rq_324=done; spawn rq_325; ticks=333
- FOI: FWI L5 per institute + cut path still ready human send
- Next: prio5 **rq_325**; deferred **rq_116** SWA
""")

print("tick333 write OK")

# tick 334 — P4Science FSI L5 envelopes
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T05:45:00Z"

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_belspo_p4science_call_2024_25,"
        "BELSPO P4Science call 2024-2025 Information File FSI L5 envelopes,"
        "https://www.belspo.be/belspo/P4Science-S4Policy/call/P4Science_2025/P4S_call2024-25-Info-File_v2.pdf,"
        "BELSPO,2026-07-31,official_call,"
        "Strong: CM 9Feb2024 P4Science; call 15.26189m over 2 budget years; "
        "20pct competitive 2.85238m all FSI; 80pct non-competitive by FSI key; "
        "10 BELSPO FSI + Sciensano NICC WHI; dual community research; tick334\n"
    )

# --- entities ---
with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "p4science_belspo,P4Science BELSPO FSI research programme,"
        "P4Science programme BELSPO,"
        "Multi-year competitive+allocated research projects for Federal Scientific Institutions,"
        "programme,belspo,bi,https://www.belspo.be/belspo/P4Science-S4Policy/,,,"
        "CM 9Feb2024; call 2024-25 envelope 15.26m; dual FWO/FNRS; tick334\n"
    )

# --- budgets ---
fsi = [
    ("kbin_irsnb", 1883060, "KBIN-IRSNB non-competitive P4Science 2024-25 envelope"),
    ("kmma_mrac", 1220590, "KMMA-MRAC AfricaMuseum non-competitive P4Science envelope"),
    ("kmi_irm", 959290, "KMI-IRM non-competitive P4Science envelope"),
    ("kbs_orb", 1097500, "KBS-ORB non-competitive P4Science envelope"),
    ("bira_iasb", 1151720, "BIRA-IASB non-competitive P4Science envelope"),
    ("kmkg_mrah", 962520, "KMKG-MRAH non-competitive P4Science envelope"),
    ("kmskb_mrbab", 594530, "KMSKB-MRBAB non-competitive P4Science envelope"),
    ("kik_irpa", 1185650, "KIK-IRPA non-competitive P4Science envelope"),
    ("ara_agr", 1696340, "ARA-AGR State Archives non-competitive P4Science envelope"),
    ("kbr", 555110, "KBR Royal Library non-competitive P4Science envelope"),
    ("sciensano", 563760, "Sciensano non-competitive P4Science envelope (non-BELSPO FSI)"),
    ("nicc_incc", 393260, "NICC-INCC non-competitive P4Science envelope"),
    ("whi", 131180, "WHI non-competitive P4Science envelope"),
]
noncomp = sum(a for _, a, _ in fsi)
bud_lines = [
    "bud_p4science_call_total_2024_25,p4science_belspo,2025,15261890,,,budgeted,src_belspo_p4science_call_2024_25,strong,P4Science call 2024-25 indicative total 15.26189m covers two budget years",
    "bud_p4science_competitive_2024_25,p4science_belspo,2025,2852380,,,budgeted,src_belspo_p4science_call_2024_25,strong,Competitive 20pct all FSI 2.85238m (+250k already committed international)",
    "bud_p4science_intl_committed_2024_25,p4science_belspo,2025,250000,,,budgeted,src_belspo_p4science_call_2024_25,strong,Competitive budget already committed to international calls 250k",
]
for eid, amt, note in fsi:
    bud_lines.append(
        f"bud_p4science_{eid}_2024_25,p4science_belspo,2025,{amt},,,budgeted,"
        f"src_belspo_p4science_call_2024_25,strong,{note}"
    )
bud_lines.append(
    f"bud_p4science_noncomp_sum_2024_25,p4science_belspo,2025,{noncomp},,,budgeted,"
    "src_belspo_p4science_call_2024_25,strong,"
    "Sum non-competitive FSI envelopes 12.39451m (~80pct of 15.26m)"
)
with open(root / "budgets.csv", "a", encoding="utf-8") as f:
    f.write("\n".join(bud_lines) + "\n")

# --- commitment ---
cash_json = (
    '{"call_total_m":15.26189,"competitive_m":2.85238,"competitive_pct":0.20,'
    '"noncomp_m":12.39451,"noncomp_pct":0.80,"intl_committed_m":0.25,'
    '"kbin_m":1.88306,"kmma_m":1.22059,"ara_m":1.69634,"kik_m":1.18565,'
    '"bira_m":1.15172,"kbs_m":1.0975,"kmkg_m":0.96252,"kmi_m":0.95929,'
    '"kmskb_m":0.59453,"sciensano_m":0.56376,"kbr_m":0.55511,"nicc_m":0.39326,'
    '"whi_m":0.13118,'
    '"note":"Project R&D NOT base FWI financing; dual community FWO/FNRS; biennial calls; residual FOI base L5"}'
)
cmt = (
    "cmt_p4science_call_2024_25,"
    "P4Science BELSPO FSI project research call 2024-25 L5,"
    "p4science_belspo,"
    "10 BELSPO FSI + Sciensano NICC WHI + university partners,"
    "CM 9 Feb 2024 P4Science programme,"
    "2024-02-09,2024,2026,15261890,"
    f'"{cash_json.replace(chr(34), chr(34)+chr(34))}",'
    "15261890,active,"
    "https://www.belspo.be/belspo/P4Science-S4Policy/call/P4Science_2025/P4S_call2024-25-Info-File_v2.pdf,"
    "Reinforce FSI scientific excellence research capacity federal priorities,"
    "Publish base financing per FWI cash-by-year separate from project envelopes,"
    "src_belspo_p4science_call_2024_25,strong,Federal>BELSPO>P4Science,"
    "tick334: 15.26m call L5 by FSI dual research\n"
)
# CSV standard: double quotes inside field
# Simpler: use single-quoted JSON without nested quote issues via json.dumps style doubled
import json

cash = {
    "call_total_m": 15.26189,
    "competitive_m": 2.85238,
    "competitive_pct": 0.20,
    "noncomp_m": 12.39451,
    "noncomp_pct": 0.80,
    "intl_committed_m": 0.25,
    "kbin_m": 1.88306,
    "kmma_m": 1.22059,
    "ara_m": 1.69634,
    "kik_m": 1.18565,
    "bira_m": 1.15172,
    "kbs_m": 1.0975,
    "kmkg_m": 0.96252,
    "kmi_m": 0.95929,
    "kmskb_m": 0.59453,
    "sciensano_m": 0.56376,
    "kbr_m": 0.55511,
    "nicc_m": 0.39326,
    "whi_m": 0.13118,
    "note": "Project R&D NOT base FWI financing; dual community FWO/FNRS; residual FOI base L5",
}
cash_field = json.dumps(cash, separators=(",", ":")).replace('"', '""')
cmt = (
    "cmt_p4science_call_2024_25,"
    "P4Science BELSPO FSI project research call 2024-25 L5,"
    "p4science_belspo,"
    "10 BELSPO FSI + Sciensano NICC WHI + university partners,"
    "CM 9 Feb 2024 P4Science programme,"
    f'2024-02-09,2024,2026,15261890,"{cash_field}",15261890,active,'
    "https://www.belspo.be/belspo/P4Science-S4Policy/call/P4Science_2025/P4S_call2024-25-Info-File_v2.pdf,"
    "Reinforce FSI scientific excellence research capacity federal priorities,"
    "Publish base financing per FWI cash-by-year separate from project envelopes,"
    "src_belspo_p4science_call_2024_25,strong,Federal>BELSPO>P4Science,"
    "tick334: 15.26m call L5 by FSI dual research\n"
)
with open(root / "commitments.csv", "a", encoding="utf-8") as f:
    f.write(cmt)

# --- leaderboard ---
with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_p4science_15m,"
        "P4Science FSI project call 15.26m 2024-25 dual federal research,"
        "federal,ops,Federal>BELSPO>P4Science,15261890,15261890,"
        "Strong BELSPO call: 15.26m over 2 years; 20/80 competitive vs FSI-allocated; "
        "largest KBIN 1.88m ARA 1.70m KMMA 1.22m; dual FWO/FNRS,"
        "strong,src_belspo_p4science_call_2024_25,FSI researchers universities,"
        "Federal FSI excellence and capacity,"
        "Core research project funding not pure waste; opacity is base financing residual; track awards L5,"
        "2,5.5,3,3.9,Publish awarded project list EUR; FOI base FWI L5 separate,seed,,tick334 partial FWI L5 fill\n"
    )

# --- foi_queue ---
foi_path = root / "foi_queue.csv"
text = foi_path.read_text(encoding="utf-8")
m = re.search(r"gap_belspo_fwi_l5_cut,[^\n]+", text)
if not m:
    raise SystemExit("gap_belspo row not found")
new_row = (
    "gap_belspo_fwi_l5_cut,Federal>BELSPO>FWI_L5_and_cut_path,belspo,"
    "Cash-by-year 2024-2026 base financing per 10 FWI + Belnet; post-cut outturn after 93m-15pct; "
    "free budget article codes; reconcile P4Science project envelopes vs base ADBA+ION 162.6m,"
    "AR2024 582.4m + P4Science 15.26m project L5 by FSI strong; residual base financing L5 and cut path,6,"
    "BELSPO / POD Wetenschapsbeleid / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_belspo_fwi_l5_cut.md,ready,2026-07-31,,,,,"
    "cmt_belspo_budget_2024_split|cmt_belspo_science_path_2024_25|cmt_p4science_call_2024_25,"
    "lb_belspo_582m_2024|lb_p4science_15m,2026-07-31T03:15:00Z,2026-07-31T05:45:00Z,"
    "tick329 draft | tick331 ESA | tick333 AR | tick334 P4Science project L5 partial; residual base FWI L5 + cut path human send"
)
text = text[: m.start()] + new_row + text[m.end() :]
foi_path.write_text(text, encoding="utf-8")

# --- research_queue ---
rq_path = root / "research_queue.csv"
rq_text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_325,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-31T05:15:00Z,,Spawned tick333 after Belspo AR2024 split; rq_116 SWA deferred"
)
new = (
    "rq_325,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_belspo_fwi_l5_cut,"
    "2026-07-31T05:15:00Z,2026-07-31T05:45:00Z,"
    "tick334: P4Science 15.26m FSI L5 project envelopes dual; FOI base residual; spawn rq_326"
)
if old not in rq_text:
    raise SystemExit("rq_325 row not found or already updated")
rq_text = rq_text.replace(old, new)
if "rq_326" not in rq_text:
    if not rq_text.endswith("\n"):
        rq_text += "\n"
    rq_text += (
        "rq_326,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-07-31T05:45:00Z,,Spawned tick334 after P4Science FSI L5; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq_text, encoding="utf-8")

# --- loop_state ---
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_325,334,no,"
    "Scheduler 60s. Next prio5 rq_326; rq_116 SWA deferred. FOI ready. tick334 P4Science 15.26m FSI L5.\n",
    encoding="utf-8",
)

# --- FOI draft note ---
draft = root.parent / "foi" / "drafts" / "gap_belspo_fwi_l5_cut.md"
if draft.exists():
    with open(draft, "a", encoding="utf-8") as f:
        f.write(
            """

## Update tick334 — P4Science project L5 partial public fill

Source: BELSPO P4Science Information File call 2024-2025 (primary PDF).

- Call total **€15.261.890** (covers two budget years).
- Competitive **20%**: **€2.852.380** all FSI (+€250k already committed international).
- Non-competitive **80%** allocated by FSI (repartition key for 10 BELSPO-FSI; flat rate Sciensano/NICC/WHI):
  - KBIN-IRSNB **€1.883.060** · ARA-AGR **€1.696.340** · KMMA-MRAC **€1.220.590**
  - KIK-IRPA **€1.185.650** · BIRA-IASB **€1.151.720** · KBS-ORB **€1.097.500**
  - KMKG-MRAH **€962.520** · KMI-IRM **€959.290** · KMSKB-MRBAB **€594.530**
  - Sciensano **€563.760** · KBR **€555.110** · NICC **€393.260** · WHI **€131.180**
- **Not** base financing (ADBA+ION €162.6m residual FOI). Project R&D only.
- CM approved programme **9 Feb 2024**.

Residual FOI unchanged: base cash-by-year per FWI + cut €93m path.
"""
        )

# --- entity belspo note refresh ---
ent_text = (root / "entities.csv").read_text(encoding="utf-8")
ent_text2 = re.sub(
    r"(belspo,POD Wetenschapsbeleid BELSPO,[^\n]+)",
    "belspo,POD Wetenschapsbeleid BELSPO,SPP Politique scientifique BELSPO,"
    "Federal Science Policy Office,agency,sec_federal,bi,https://www.belspo.be,,,"
    "Budget 2024 strong 582.4m; P4Science 15.26m FSI project L5; ESA 284m 2025; cut 93m; dual community; tick329-334",
    ent_text,
    count=1,
)
if ent_text2 == ent_text:
    print("WARN: belspo entity not updated")
else:
    (root / "entities.csv").write_text(ent_text2, encoding="utf-8")

print("OK tick334 data writes; noncomp", noncomp)

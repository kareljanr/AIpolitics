# tick 281 — FSMA dual CREG/BIPT financial regulator
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T03:15:00Z"

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fsma_jv_2024,FSMA Jaarverslag 2024 jaarrekening werkingskosten personeel,"
        "docs/doge/data/raw/fsma_jv_2024.pdf,FSMA,2026-07-30,agency,"
        "Budget werkings 112.373m 2024 (+zetel 3.122m=115.495m contrib); P&L opbr 115.405m kosten 107.469m "
        "bezold 79.831m surplus return 7.907m; staff 375/353 VTE; assets 80.226m; tick281\n"
    )

with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "fsma,Autoriteit voor Financiele Diensten en Markten FSMA,"
        "Autorite des services et marches financiers FSMA,"
        "Financial Services and Markets Authority,agency,sec_federal,bi,https://www.fsma.be,,,"
        "Conduct supervisor dual NBB prudential; werkings 107.5m 2024 sector-financed; staff 375; tick281\n"
    )

# P&L figures in kEUR -> EUR
bud = [
    "bud_fsma_budget_werkings_2024,fsma,2024,112373000,,,budgeted,src_fsma_jv_2024,strong,Budget werkingskosten 112.373m 2024 excl zetel 3.122m",
    "bud_fsma_budget_contrib_2024,fsma,2024,115495000,,,budgeted,src_fsma_jv_2024,strong,Gebudgetteerde bijdragen 115.495m = werkings 112.373 + zetel 3.122",
    "bud_fsma_opbrengsten_2024,fsma,2024,115405000,,,outturn,src_fsma_jv_2024,strong,P&L opbrengsten 115.405 kEUR (bijdragen 115.078 + andere 0.327)",
    "bud_fsma_opbrengsten_2023,fsma,2023,107396000,,,outturn,src_fsma_jv_2024,strong,P&L opbrengsten 107.396 kEUR 2023",
    "bud_fsma_werkingskosten_2024,fsma,2024,107469000,,,outturn,src_fsma_jv_2024,strong,Werkingskosten 107.469 kEUR 2024",
    "bud_fsma_werkingskosten_2023,fsma,2023,101473000,,,outturn,src_fsma_jv_2024,strong,Werkingskosten 101.473 kEUR 2023",
    "bud_fsma_bezoldigingen_2024,fsma,2024,79831000,,,outturn,src_fsma_jv_2024,strong,Bezoldigingen sociale lasten pensioenen 79.831 kEUR (~74pct of costs)",
    "bud_fsma_bezoldigingen_2023,fsma,2023,76038000,,,outturn,src_fsma_jv_2024,strong,Bezoldigingen 76.038 kEUR 2023",
    "bud_fsma_diensten_2024,fsma,2024,21249000,,,outturn,src_fsma_jv_2024,strong,Diensten en diverse goederen 21.249 kEUR",
    "bud_fsma_afschrijvingen_2024,fsma,2024,6886000,,,outturn,src_fsma_jv_2024,strong,Afschrijvingen 6.886 kEUR",
    "bud_fsma_surplus_return_2024,fsma,2024,7907000,,,outturn,src_fsma_jv_2024,strong,Werkingsoverschot returned to supervised entities 7.907 kEUR (art23 KB)",
    "bud_fsma_assets_2024,fsma,2024,80226000,,,outturn,src_fsma_jv_2024,strong,Balanstotaal 80.226 kEUR end-2024",
    "bud_fsma_staff_2024,fsma,2024,375,,,outturn,src_fsma_jv_2024,strong,Headcount 375 end-2024 (353 VTE register; 350.5 operational VTE); amount is count",
    "bud_fsma_staff_max_vte,fsma,2024,399,,,outturn,src_fsma_jv_2024,strong,Max operational VTE ceiling 399 (KB financing)",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

cash = {
    "budget_werkings_2024": 112373000,
    "budget_zetel_2024": 3122000,
    "budget_contrib_2024": 115495000,
    "opbrengsten_2024": 115405000,
    "opbrengsten_2023": 107396000,
    "werkingskosten_2024": 107469000,
    "werkingskosten_2023": 101473000,
    "bezoldigingen_2024": 79831000,
    "diensten_2024": 21249000,
    "surplus_return_2024": 7907000,
    "assets_2024": 80226000,
    "staff_headcount": 375,
    "staff_vte": 353,
    "staff_max_vte": 399,
    "finance": "sector contributions under KB 17 May 2012; surplus returned",
    "note": "Conduct supervisor dual NBB prudential; dual CREG 22.4m BIPT 79.8m regulators; not TE",
}
j = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
cmt = (
    "cmt_fsma_budget_2023_24,FSMA financial markets conduct supervisor package dual NBB CREG BIPT,"
    "fsma,Supervised financial firms intermediaries consumers,"
    "Wet 2 aug 2002 + KB 17 mei 2012 werkingskosten,2023-01-01,2023,2025,115405000,"
    + j
    + ",0,active,docs/doge/data/raw/fsma_jv_2024.pdf,"
    "Conduct supervision of financial markets and consumer protection,"
    "FOI 2025 budget detail; dual unit-cost NBB; L5 externe optional,"
    "src_fsma_jv_2024,strong,Federal>Finance>FSMA,tick281 dual CREG BIPT NBB\n"
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt)

lb = [
    "lb_fsma_werkings_107m,FSMA werkingskosten 107.5m 2024 dual regulators,federal,ops,Federal>Finance>FSMA,107469000,107469000,Strong JV: werkingskosten 107.469m 2024 (101.473m 2023); sector-contrib financed surplus return 7.9m; core conduct supervisor not pure waste,strong,src_fsma_jv_2024,Supervised entities consumers,Financial markets conduct supervision,Core dual NBB prudential CREG BIPT,3,7.5,3,5.55,Publish multi-year; dual unit-cost NBB,seed,,tick281",
    "lb_fsma_bezold_80m,FSMA personnel 79.8m 2024,federal,ops,Federal>Finance>FSMA>personnel,79831000,79831000,Strong JV: bezoldigingen 79.831m ~74pct of werkings; staff 375 (353 VTE) vs max 399,strong,src_fsma_jv_2024,FSMA staff,Conduct supervision capacity,Core capacity dual BIPT 27.4m CREG 14.7m,3,7.0,3,5.35,Track FTE vs ceiling,seed,,tick281",
    "lb_fsma_contrib_115m,FSMA sector contributions 115.4m 2024,federal,ops,Federal>Finance>FSMA>contrib,115405000,115405000,Strong JV: opbrengsten 115.405m (bijdragen 115.078m); budget contrib 115.495m; surplus 7.9m returned,strong,src_fsma_jv_2024,Financial sector firms,Industry-funded supervision,Fee-funded regulator dual CREG accijns BIPT licences,3,7.5,3,5.55,Open contribution matrix by sector if public,seed,,tick281",
    "lb_regulators_triple_creg_bipt_fsma,Federal regulators triple CREG+BIPT+FSMA,federal,ops,BE>Regulators>triple,0,0,Strong triple: CREG 22.4m 2023 + BIPT 79.8m 2024 + FSMA 107.5m 2024; all sector-fee financed not TE; not additive; dual NBB prudential separate,strong,src_fsma_jv_2024,Markets consumers,Independent economic financial regulation stack,Institutional multi-regulator map,4,8.5,4,6.05,Joint fee transparency; dual NBB unit-cost,seed,,tick281 dual not additive",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# FOI light residual 2025
foi_path = base / "foi_queue.csv"
lines = foi_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
out = lines[:]
# update creg_bipt gap note
out2 = []
for line in out:
    if line.startswith("gap_creg_bipt_2024_26,") and "tick281" not in line:
        line = line.rstrip() + " | tick281: FSMA 107.5m dual filled public"
    out2.append(line)
gap = "gap_fsma_budget_2025_26"
if not any(l.startswith(gap + ",") for l in out2):
    out2.append(
        f"{gap},Federal>FSMA>budget_2025_26,fsma,"
        "Approved budget 2025 (Raad Dec 2024) line detail vs 112.373m 2024 path; "
        "contribution matrix by supervised sector 2023-2025; L5 top external experts under diensten 21.2m,"
        "2023-24 P&L strong JV; 2025 budget approved but figures not in JV body; dual NBB residual,"
        "4,FSMA openbaarheid / Raad van toezicht,,"
        "https://www.fsma.be,"
        f"docs/doge/foi/drafts/{gap}.md,ready,2026-07-30,,,,,,"
        f"cmt_fsma_budget_2023_24,lb_fsma_werkings_107m,{now},{now},"
        "tick281 draft ready human send; 2024 filled"
    )
foi_path.write_text("\n".join(out2) + "\n", encoding="utf-8")

rq_path = base / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq:
    if line.startswith("rq_272,"):
        out.append(
            "rq_272,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills after progress@280 (AGMJ wage if public; Fedasil; FSMA; other FOI-adjacent).,"
            f"gap_fsma_budget_2025_26,2026-07-30T02:15:00Z,{now},"
            "tick281: FSMA werkings 107.5m dual CREG BIPT; spawn rq_273"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_273,") for l in out):
    out.append(
        "rq_273,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; NBB dual FSMA; Fedasil L5 residual; other FOI-adjacent after FSMA).,,"
        f"{now},,Spawned tick281 after FSMA; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_272,281,no,"
    "Scheduler 60s. Next prio5 rq_273; rq_116 SWA deferred. FOI ready human send. tick281 FSMA 107.5m dual CREG BIPT.\n",
    encoding="utf-8",
)
print("OK tick281")

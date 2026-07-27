# tick 282 — NBB ops dual FSMA prudential supervision
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T03:45:00Z"

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_nbb_ondernemingsverslag_2024,NBB Ondernemingsverslag 2024 jaarrekening personeel beheers prudentieel,"
        "docs/doge/data/raw/nbb_ondernemingsverslag_2024.pdf,Nationale Bank van Belgie,2026-07-30,agency,"
        "Personeel 335.7m 2024 (451.3m 2023); beheers 131.3m; loss 3.679bn monetary; "
        "prudential recovery 134.1m (banks 85.8 ins 46.8 other 1.5); dual FSMA; tick282\n"
    )

with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "nbb,Nationale Bank van Belgie NBB,Banque nationale de Belgique BNB,"
        "National Bank of Belgium,parastatal,sec_federal,bi,https://www.nbb.be,,,"
        "Central bank + prudential supervision dual FSMA; personeel 335.7m 2024; "
        "prudential recovery 134.1m; loss 3.679bn monetary; tick282\n"
    )

# amounts in EUR (from kEUR tables * 1000)
bud = [
    "bud_nbb_personeel_2024,nbb,2024,335693000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,P&L personeelskosten 335.693m 2024 (kEUR table)",
    "bud_nbb_personeel_2023,nbb,2023,451341000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Personeelskosten 451.341m 2023 (elevated vs 320m 2022 path)",
    "bud_nbb_personeel_2022,nbb,2022,319980000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Personeelskosten 319.980m 2022",
    "bud_nbb_beheers_2024,nbb,2024,131305000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Beheerskosten 131.305m 2024 (ICT/admin 43.9 building 12.7 third parties 37.9 tax 6.4)",
    "bud_nbb_beheers_2023,nbb,2023,120397000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Beheerskosten 120.397m 2023",
    "bud_nbb_afschrijvingen_2024,nbb,2024,10009000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Afschrijvingen 10.009m 2024",
    "bud_nbb_biljetten_2024,nbb,2024,9620000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Productiekosten bankbiljetten 9.620m 2024",
    "bud_nbb_ops_pack_2024,nbb,2024,486627000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Ops pack personeel+beheers+afschr+biljetten 335.7+131.3+10.0+9.6=486.6m 2024",
    "bud_nbb_loss_2024,nbb,2024,3678961000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Boekjaarverlies 3.678961bn 2024 (monetary policy not ops waste)",
    "bud_nbb_loss_2023,nbb,2023,3370413000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Verlies 3.370bn 2023",
    "bud_nbb_overige_baten_2024,nbb,2024,220485000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Overige baten 220.485m incl recoveries",
    "bud_nbb_prudential_recovery_2024,nbb,2024,134100000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Prudentieel toezicht recovery 134.1m from supervised (art12bis); dual FSMA",
    "bud_nbb_prudential_banks_2024,nbb,2024,85800000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Prudential costs banks+beursvennootschappen 85.8m 2024",
    "bud_nbb_prudential_ins_2024,nbb,2024,46800000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Prudential costs verzekeraars 46.8m 2024",
    "bud_nbb_prudential_other_2024,nbb,2024,1500000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Other supervised institutions 1.5m 2024",
    "bud_nbb_balanscentrale_pack_2024,nbb,2024,55500000,,,outturn,src_nbb_ondernemingsverslag_2024,strong,Balanscentrale+credit centrales+CAP recoveries 55.5m 2024",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

cash = {
    "personeel_2024_m": 335.693,
    "personeel_2023_m": 451.341,
    "personeel_2022_m": 319.980,
    "beheers_2024_m": 131.305,
    "beheers_ict_admin_m": 43.9,
    "beheers_building_m": 12.7,
    "beheers_third_parties_m": 37.9,
    "beheers_tax_m": 6.4,
    "ops_pack_2024_m": 486.627,
    "loss_2024_bn": 3.679,
    "loss_2023_bn": 3.370,
    "prudential_recovery_2024_m": 134.1,
    "prudential_banks_m": 85.8,
    "prudential_ins_m": 46.8,
    "prudential_other_m": 1.5,
    "balanscentrale_pack_m": 55.5,
    "overige_baten_2024_m": 220.485,
    "note": "Monetary loss not ops waste; prudential dual FSMA conduct 107.5m; recoveries sector-financed",
}
j = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
cmt = (
    "cmt_nbb_ops_prudential_2023_24,NBB central bank ops + prudential supervision dual FSMA,"
    "nbb,Financial institutions State public,"
    "Organieke wet NBB + art12bis/12ter + KB 17 jul 2012,2022-01-01,2022,2024,486627000,"
    + j
    + ",0,active,docs/doge/data/raw/nbb_ondernemingsverslag_2024.pdf,"
    "Monetary policy payment systems + prudential supervision,"
    "FOI staff FTE multi-year; dual unit-cost FSMA conduct; track monetary loss path,"
    "src_nbb_ondernemingsverslag_2024,strong,Federal>NBB>ops_prudential,tick282 dual FSMA\n"
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt)

lb = [
    "lb_nbb_ops_487m,NBB ops pack 486.6m 2024 dual FSMA,federal,ops,Federal>NBB>ops,486627000,486627000,Strong OV: personeel 335.7 + beheers 131.3 + afschr 10.0 + biljetten 9.6 = 486.6m 2024; core central bank ops not pure waste,strong,src_nbb_ondernemingsverslag_2024,Public financial system,Central bank operating capacity,Core dual FSMA; monetary loss separate,3,8.5,3,5.85,Publish FTE; dual unit-cost FSMA,seed,,tick282",
    "lb_nbb_personeel_336m,NBB personnel 335.7m 2024,federal,ops,Federal>NBB>personnel,335693000,335693000,Strong: 335.693m 2024 (451.3m 2023 spike; 320.0m 2022); dual FSMA 79.8m,strong,src_nbb_ondernemingsverslag_2024,NBB staff,Central bank staffing,Core capacity,3,8.0,3,5.65,FOI FTE path explain 2023 spike,seed,,tick282",
    "lb_nbb_prudential_134m,NBB prudential supervision recovery 134.1m 2024 dual FSMA,federal,ops,Federal>NBB>prudential,134100000,134100000,Strong toelichting30: 134.1m recovered (banks 85.8 + ins 46.8 + other 1.5); sector-financed dual FSMA conduct 107.5m not additive,strong,src_nbb_ondernemingsverslag_2024,Banks insurers,Prudential supervision funding,Core dual FSMA conduct supervision stack,3,7.5,3,5.55,Publish dual NBB-FSMA fee map,seed,,tick282 dual FSMA",
    "lb_nbb_loss_3_7bn,NBB book loss 3.679bn 2024 monetary policy,federal,ops,Federal>NBB>monetary_loss,3678961000,3678961000,Strong: loss 3.679bn 2024 (3.370bn 2023) from net interest on monetary portfolios; reserves depleted; not ops waste,strong,src_nbb_ondernemingsverslag_2024,State capital position,ECB monetary policy transmission costs,Monetary regime feature not discretionary waste,5,9.5,4,7.55,Track reserve rebuild path; not cut as programme waste,seed,,tick282 monetary not ops",
    "lb_supervision_dual_nbb_fsma,Supervision dual NBB prudential 134m + FSMA 107.5m,federal,ops,BE>Finance>dual_NBB_FSMA,0,0,Strong dual: NBB prudential recovery 134.1m + FSMA werkings 107.5m 2024; Twin Peaks model; not additive full TCO,strong,src_nbb_ondernemingsverslag_2024,Financial sector,Split prudential vs conduct supervision,Institutional dual post-2011 reform,4,8.5,4,6.05,Joint fee transparency matrix,seed,,tick282 dual not additive",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# FOI residual FTE
foi_path = base / "foi_queue.csv"
lines = foi_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
out = []
for line in lines:
    if line.startswith("gap_fsma_budget_2025_26,") and "tick282" not in line:
        line = line.rstrip() + " | tick282: NBB prudential 134.1m dual public"
    out.append(line)
gap = "gap_nbb_fte_ops_2024_26"
if not any(l.startswith(gap + ",") for l in out):
    out.append(
        f"{gap},Federal>NBB>FTE_ops_L5,nbb,"
        "Staff FTE multi-year 2022-2026 and explanation of personeelskosten spike 451m 2023 vs 336m 2024; "
        "L5 split prudential vs monetary vs statistics inside 486.6m ops pack; "
        "beheers third-parties top vendors under 37.9m,"
        "Ops totals strong; FTE and internal split residual dual FSMA unit-cost,"
        "4,NBB openbaarheid / Regentenraad,,"
        "https://www.nbb.be,"
        f"docs/doge/foi/drafts/{gap}.md,ready,2026-07-30,,,,,,"
        f"cmt_nbb_ops_prudential_2023_24,lb_nbb_ops_487m,{now},{now},"
        "tick282 draft ready human send; ops totals filled"
    )
foi_path.write_text("\n".join(out) + "\n", encoding="utf-8")

rq_path = base / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq:
    if line.startswith("rq_273,"):
        out.append(
            "rq_273,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; NBB dual FSMA; Fedasil L5 residual; other FOI-adjacent after FSMA).,"
            f"gap_nbb_fte_ops_2024_26,2026-07-30T03:15:00Z,{now},"
            "tick282: NBB ops 486.6m + prudential 134.1m dual FSMA; spawn rq_274"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_274,") for l in out):
    out.append(
        "rq_274,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after NBB).,,"
        f"{now},,Spawned tick282 after NBB; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_273,282,no,"
    "Scheduler 60s. Next prio5 rq_274; rq_116 SWA deferred. FOI ready human send. tick282 NBB ops 486.6m dual FSMA 134.1m.\n",
    encoding="utf-8",
)
print("OK tick282")

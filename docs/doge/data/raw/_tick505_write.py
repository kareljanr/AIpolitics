# tick505 — CoA 2026_29 KMO VenB control follow-up + dual fraud yields
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_kmo_venb_followup_2026,CoA Controle kmo VenB opvolging 2025 aanbevelingen 2026_29,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_29_KMO_VENB_Opvolging.pdf,"
        "Rekenhof AG 3 Jun 2026,2026-07-28,court_of_audit,"
        "Strong: VenB cash 25.729bn 2024; 111988 controls +5.6bn uplifts; staff gap 383 FTE; "
        "recs 3/8/2/4 of 17; BasketFisc; dual fraud claims; tick505\n"
    )
    f.write(
        "src_ccrek_kmo_venb_press_2026,CoA press KMO VenB follow-up Jun 2026,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_29_KMO_VENB_Opvolging_Persbericht.pdf,"
        "Rekenhof,2026-07-28,court_of_audit_press,"
        "Strong headlines: 3 of 17 recs done; BasketFisc; 383 FTE short; no fiscal discipline metric; tick505\n"
    )
    f.write(
        "src_dual_kmo_control_fraud_tick505,Dual KMO VenB control capacity vs fiscal fraud yield claims,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_29_KMO_VENB_Opvolging.pdf,"
        "DOGE synthesis CoA KMO + fed aju fraud claims tick503,2026-07-28,synthesis,"
        "Strong dual: control staff -383 FTE + 5.6bn uplifts vs fraud yield claim 300/600m opaque; tick505\n"
    )

buds = [
    "bud_venb_cash_2024_coa,sec_federal,2024,25729000000,,,outturn,src_ccrek_kmo_venb_followup_2026,strong,VenB cash receipts 25.729bn 2024 CoA from general account; tick505",
    "bud_venb_controls_uplift_2024,sec_federal,2024,5600000000,,,outturn,src_ccrek_kmo_venb_followup_2026,strong,VenB controls 111988 returns 2024 yielded income increases >5.6bn CoA; tick505",
    "bud_pb_cash_2024_coa,sec_federal,2024,56055000000,,,outturn,src_ccrek_kmo_venb_followup_2026,strong,PB cash receipts 56.055bn 2024 CoA figure general account; tick505",
    "bud_btw_cash_2024_coa,sec_federal,2024,37514000000,,,outturn,src_ccrek_kmo_venb_followup_2026,strong,BTW cash receipts 37.514bn 2024 CoA figure; tick505",
    "bud_rv_cash_2024_coa,sec_federal,2024,14480000000,,,outturn,src_ccrek_kmo_venb_followup_2026,strong,Roerende voorheffing cash 14.480bn 2024 CoA; tick505",
    "bud_douane_accijns_cash_2024_coa,sec_federal,2024,7618000000,,,outturn,src_ccrek_kmo_venb_followup_2026,strong,Douane-accijnzen cash 7.618bn 2024 CoA; tick505",
    "bud_kmo_staff_gap_383_fte,sec_federal,2024,383,,,estimated,src_ccrek_kmo_venb_followup_2026,strong,Admin KMO control staff gap 383 FTE vs 2018 plan eoy2024 (not EUR); tick505",
    "bud_dual_venb_uplift_vs_fraud_claim,sec_federal,2024,5600000000,,,derived,src_dual_kmo_control_fraud_tick505,strong,Dual: VenB control uplifts 5.6bn 2024 vs fraud yield claims 0.3-0.6bn path; tick505",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_kmo_venb_control_followup,KMO VenB tax control CoA follow-up 2025,"
        "sec_federal,SME corporate taxpayers FPS Finance,"
        "CoA 2022 audit + 2026_29 follow-up,"
        "2022-12-07,2022,2026,5600000000,"
        '"{""venb_cash_2024_bn"":25.729,""controls_2024_n"":111988,""uplift_2024_bn"":5.6,'
        '""staff_gap_fte"":383,""recs_done"":3,""recs_progress"":8,""recs_not"":2,""recs_na"":4,'
        '""basketfisc"":true,""fiscal_discipline_metric"":false,'
        '""note"":""Strong CoA: capacity gap persists; language inequality residual""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_29_KMO_VENB_Opvolging.pdf,"
        "Improve SME CIT control equity and yield,Fill 383 FTE; dual fraud claims FOI method,"
        "src_ccrek_kmo_venb_followup_2026,strong,Federal>FPS_Finance>KMO_VenB,tick505"
    ),
    (
        "cmt_dual_kmo_control_fraud,Dual KMO control capacity vs fiscal fraud budget yields,"
        "sec_federal,Taxpayers FPS Finance,"
        "CoA KMO 2026_29 + fed aju fraud claims,"
        "2024-01-01,2024,2029,5600000000,"
        '"{""uplift_2024_bn"":5.6,""fraud_claim_2026_m"":300,""fraud_claim_2029_m"":600,'
        '""staff_gap_fte"":383,'
        '""note"":""not additive; control uplifts realized vs claimed future fraud yields""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_29_KMO_VENB_Opvolging.pdf,"
        "Align control capacity with revenue claims,Staff + method transparency FOI,"
        "src_dual_kmo_control_fraud_tick505,strong,Federal>dual>Tax_control_fraud,tick505"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_venb_25_7bn_2024,VenB cash receipts 25.7bn 2024,federal,tax_revenue,Federal>Fiscalite>VenB_2024,25729000000,25729000000,Strong CoA: 25.729bn cash general account 2024; third major tax after PB/BTW,strong,src_ccrek_kmo_venb_followup_2026,Corporate taxpayers,Corporate income tax,Core revenue not waste; control quality matters,2.0,9.5,4,5.7,Protect control capacity,seed,,tick505",
    "lb_venb_control_uplift_5_6bn,VenB control income uplifts >5.6bn 2024,federal,enforcement,Federal>FPS_Finance>VenB_controls,5600000000,5600000000,Strong CoA: 111988 returns controlled; >5.6bn income increases; dual staff gap 383 FTE,strong,src_ccrek_kmo_venb_followup_2026,SME taxpayers,Tax compliance enforcement,High yield enforcement; capacity under-staffed,4.0,9.5,5,6.7,Fill FTE gap; equal treatment languages,seed,,tick505",
    "lb_kmo_staff_gap_383,Admin KMO control staff short 383 FTE,federal,governance,Federal>FPS_Finance>KMO_staff_gap,0,0,Strong CoA: 383 FTE short vs 2018 plan eoy2024; controllers -21pct 2016-21 prior; annual0 FTE,strong,src_ccrek_kmo_venb_followup_2026,FPS Finance,Control capacity,Under-capacity vs fraud yield claims dual,7.5,3.5,4,5.75,Recruit controllers; dual fraud FOI,seed,,tick505",
    "lb_kmo_recs_partial,KMO VenB CoA recs only 3 of 17 fully done,federal,governance,Federal>FPS_Finance>KMO_recs,0,0,Strong CoA follow-up: 3 done 8 in progress 2 not done 4 N/A; BasketFisc partial equality,strong,src_ccrek_kmo_venb_followup_2026,Parliament taxpayers,Implement control reforms,Slow reform after 3 years,6.5,3.5,4,5.35,Close remaining 2+8 recs FOI timeline,seed,,tick505",
    "lb_dual_venb_control_fraud,Dual VenB uplifts 5.6bn vs fraud claims 0.3-0.6bn,multi,enforcement,BE>dual>Tax_control_fraud,5600000000,5600000000,Strong dual: realized control uplifts >> claimed future fraud yields; staff gap 383,strong,src_dual_kmo_control_fraud_tick505,Taxpayers,Tax enforcement integrity,Capacity before claimed yields,6.0,9.5,5,7.35,Staff first; method FOI for claims,seed,,tick505",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_kmo_venb_control_l5,Federal>FPS_Finance>KMO_VenB>control_L5,sec_federal,"
    "Timeline to close remaining CoA recs (2 not done + 8 in progress); staff recruitment plan "
    "for 383 FTE gap; BasketFisc language-equality fix; fiscal discipline KPI design if any; "
    "method link of control uplifts to fraud yield claims 300/600m,"
    "CoA 2026_29: aggregates strong; residual implementation + dual fraud method opaque,7,"
    "FOD Financiën Administratie KMO / SPF Finances,info@minfin.fed.be,"
    ",docs/doge/foi/drafts/gap_kmo_venb_control_l5.md,"
    "ready,2026-07-28,,,,,cmt_kmo_venb_control_followup,"
    "lb_venb_control_uplift_5_6bn|lb_kmo_staff_gap_383,"
    "2026-07-28T22:30:00Z,2026-07-28T22:30:00Z,"
    "tick505: CoA 2026_29 primary fill; residual control L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_496,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T22:10:00Z,,Spawned tick504 after CoA Kustbeveiliging; rq_116 deferred"
)
new = (
    "rq_496,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_kmo_venb_control_l5,"
    "2026-07-28T22:10:00Z,2026-07-28T22:30:00Z,"
    "tick505: CoA 2026_29 KMO VenB controls 5.6bn uplift staff -383 dual fraud; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_496 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_497,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T22:30:00Z,,Spawned tick505 after CoA KMO VenB follow-up; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T22:30:00Z,rq_496,505,no,"
    "Tick505 CoA KMO VenB 5.6bn uplift staff-383 dual fraud; next prio5 rq_497; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick505 OK")

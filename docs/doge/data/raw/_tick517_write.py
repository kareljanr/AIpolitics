# tick517 — CoA consultancy residual Smals broker L5 dual IT detach
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_consultancy_smals_broker_2025,CoA consultancy 2025 Ch5 Smals broker residual L5,"
        "docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Rekenhof AG 22 Oct 2025,2026-07-29,court_of_audit,"
        "Strong tick517: ProUnity broker est 1.8bn + lot2 250m; orders 2023-24 471.4m; day rates junior-expert; "
        "detach cheaper ~21pct VAT; dual prior consultancy; tick517\n"
    )
    f.write(
        "src_dual_smals_broker_tick517,Dual Smals broker mega-framework + federal IT consultancy stack,"
        "docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "DOGE synthesis CoA Smals broker + tick514 consultancy total,2026-07-29,synthesis,"
        "Strong dual: broker 471m/2y under 1.8bn framework vs consultancy IT 2.03bn 3y; tick517\n"
    )

buds = [
    "bud_smals_broker_framework_18bn,smals,2022,1800000000,,,commitment,src_ccrek_consultancy_smals_broker_2025,strong,Smals ProUnity broker lot1 framework estimated value 1.8bn awarded 15 Dec 2022; tick517",
    "bud_smals_broker_lot2_250m,smals,2022,250000000,,,commitment,src_ccrek_consultancy_smals_broker_2025,strong,Smals broker lot2 fixed-price IT projects framework est 250m; tick517",
    "bud_smals_broker_orders_471m_2023_24,smals,2024,471400000,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Orders under Smals broker framework 2023-2024 total 471.4m; tick517",
    "bud_smals_direct_orders_nonbroker_21m_2022,smals,2022,20900000,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Direct user orders on Smals contracts outside broker 20.9m 2022; tick517",
    "bud_smals_direct_broker_orders_47m_2022,smals,2022,47000000,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Direct user orders on broker contract 47m 2022; tick517",
    "bud_smals_dayrate_junior_avg_672,smals,2024,672,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Avg day rate junior external IT via Smals 672.24 EUR incl VAT (min 302.5 max 822.8) orders 2023-Jan2025; amount is EUR/day; tick517",
    "bud_smals_dayrate_senior_avg_759,smals,2024,759,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Avg day rate senior external IT 759.43 EUR incl VAT (min 420 max 1149.5); tick517",
    "bud_smals_dayrate_expert_avg_923,smals,2024,923,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Avg day rate expert external IT 923.38 EUR incl VAT (min 434 max 2127.9); tick517",
    "bud_smals_hourly_detach_prog_66,smals,2025,66,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Smals Mar2025: detach programmer hourly 65.71 vs external 111.43 incl VAT; tick517",
    "bud_smals_hourly_detach_analyst_94,smals,2025,94,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Smals Mar2025: detach analyst hourly 93.62 vs external 126.30 incl VAT; tick517",
    "bud_smals_detach_admin_198_month,smals,2025,198,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Detach admin cost 198 EUR/month included in Smals cost comparison; tick517",
    "bud_fod_fin_detach_197_2024,sec_federal,2024,0,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,FOD Fin Feb2024: 198 internal staff + 197 Smals/Egov detachments (near 50-50); count in notes; tick517",
    "bud_rsvz_it_detach_82_2022,sec_ss,2022,0,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,RSVZ Mar2022 IT: 10 internal FTE + 82 detached FTE; tick517",
]
# Clean dayrate/hourly as confusing in amount_eur - keep only large euros + note rates in cmt
buds = [
    "bud_smals_broker_framework_18bn,smals,2022,1800000000,,,commitment,src_ccrek_consultancy_smals_broker_2025,strong,Smals ProUnity broker lot1 framework estimated value 1.8bn awarded 15 Dec 2022; tick517",
    "bud_smals_broker_lot2_250m,smals,2022,250000000,,,commitment,src_ccrek_consultancy_smals_broker_2025,strong,Smals broker lot2 fixed-price IT projects framework est 250m; tick517",
    "bud_smals_broker_orders_471m_2023_24,smals,2024,471400000,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Orders under Smals broker framework 2023-2024 total 471.4m; tick517",
    "bud_smals_broker_orders_avg_annual_236m,smals,2024,235700000,,,derived,src_ccrek_consultancy_smals_broker_2025,medium,Illustrative avg annual broker orders 471.4/2 ~235.7m 2023-24; tick517",
    "bud_smals_direct_orders_nonbroker_21m_2022,smals,2022,20900000,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Direct user orders on Smals contracts outside broker 20.9m 2022; tick517",
    "bud_smals_direct_broker_orders_47m_2022,smals,2022,47000000,,,outturn,src_ccrek_consultancy_smals_broker_2025,strong,Direct user orders on broker contract 47m 2022; tick517",
    "bud_smals_framework_total_est_205bn,smals,2022,2050000000,,,commitment,src_ccrek_consultancy_smals_broker_2025,strong,Smals broker lots combined est 1.8+0.25=2.05bn; tick517",
    "bud_dual_smals_broker_2024,gg_belgium,2024,471400000,,,derived,src_dual_smals_broker_tick517,strong,Dual Smals broker cash 471m under mega framework; tick517",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_smals_broker_18bn_471m,Smals ProUnity broker framework 1.8bn + orders 471m 2023-24,"
        "smals,Federal IT users ProUnity,"
        "CoA consultancy 2025 §5.4.3,"
        "2022-12-15,2022,2024,1800000000,"
        '"{""lot1_est_bn"":1.8,""lot2_est_m"":250,""orders_2023_24_m"":471.4,'
        '""direct_nonbroker_2022_m"":20.9,""direct_broker_2022_m"":47.0,'
        '""dayrate_junior_avg"":672.24,""dayrate_senior_avg"":759.43,""dayrate_expert_avg"":923.38,'
        '""dayrate_expert_max"":2127.9,""hourly_detach_prog"":65.71,""hourly_ext_prog"":111.43,'
        '""hourly_detach_analyst"":93.62,""hourly_ext_analyst"":126.30,'
        '""detach_admin_month"":198,""single_broker_bid"":true,'
        '""note"":""Strong CoA; only one broker bid; ranking deviations FOI""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Cheaper internal/detach IT capacity,Publish rate vs market FOI,"
        "src_ccrek_consultancy_smals_broker_2025,strong,Federal>Smals>broker,tick517"
    ),
    (
        "cmt_smals_detach_vs_external,Smals detach cheaper than external IT consultancy,"
        "smals,Federal IT units,"
        "CoA consultancy 2025 Tables 3-4,"
        "2025-03-01,2019,2024,0,"
        '"{""detachments_2019"":1395,""detachments_2024"":2072,""growth_pct"":48.5,'
        '""fod_fin_internal"":198,""fod_fin_detach"":197,""rsvz_internal_fte"":10,'
        '""rsvz_detach_fte"":82,""vat_external_pct"":21,""ext_share_turnover_2014_pct"":17.8,'
        '""ext_share_turnover_2024_pct"":36.0,'
        '""note"":""Strong CoA; structural tasks on detachments risk replacing internal staff""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Prefer detach over external for structural IT,Planning FOI,"
        "src_ccrek_consultancy_smals_broker_2025,strong,Federal>Smals>detach,tick517"
    ),
    (
        "cmt_dual_smals_broker_consultancy,Dual Smals broker mega-spend under consultancy IT stack,"
        "gg_belgium,Federal IT,"
        "CoA consultancy dual,"
        "2025-10-22,2022,2024,471400000,"
        '"{""broker_orders_m"":471.4,""framework_bn"":1.8,""consultancy_it_3y_bn"":2.032,'
        '""note"":""not additive pure TE; dual IT procurement channel""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Map dual IT purchase channels,Inventory+broker FOI,"
        "src_dual_smals_broker_tick517,strong,BE>dual>Smals_broker,tick517"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_smals_broker_framework_18bn,Smals ProUnity broker framework est 1.8bn,federal,ops,Federal>Smals>broker_framework,235700000,1800000000,Strong CoA: lot1 1.8bn + lot2 250m; orders 471.4m 2023-24; single bidder,strong,src_ccrek_consultancy_smals_broker_2025,IT vendors freelancers,Central IT staffing marketplace,Mega procurement channel,6.5,9.0,5,7.35,Market competition FOI,seed,,tick517",
    "lb_smals_broker_orders_471m,Smals broker orders 471m 2023-24,federal,ops,Federal>Smals>broker_orders,235700000,471400000,Strong CoA Table5: 471.4m orders two years; dual consultancy IT,strong,src_ccrek_consultancy_smals_broker_2025,Federal IT users,External IT via broker,Large annual flow,5.5,7.5,4,6.35,Rate vs market FOI,seed,,tick517",
    "lb_smals_dayrate_expert_923,Smals external IT day rates junior-expert,federal,ops,Federal>Smals>day_rates,923,2128,Strong CoA: avg junior 672 senior 759 expert 923 max 2128 EUR/day incl VAT,strong,src_ccrek_consultancy_smals_broker_2025,Consultants,IT specialist pricing,High unit rates,6.0,5.5,3,5.85,Benchmark FOI,seed,,tick517",
    "lb_smals_detach_cheaper,Smals detach ~40pct cheaper than external IT,federal,ops,Federal>Smals>detach_vs_ext,0,0,Strong CoA: programmer 65.71 vs 111.43 hourly; analyst 93.62 vs 126.30; 21pct VAT wedge,strong,src_ccrek_consultancy_smals_broker_2025,Federal IT units,Make-or-buy IT staffing,Efficiency flag,5.0,4.0,3,4.55,Prefer detach structural FOI,seed,,tick517",
    "lb_smals_single_broker_bid,Smals broker re-tender only one bid,federal,ops,Federal>Smals>broker_competition,0,1800000000,Strong CoA: only one broker offered for dual-broker design; competition weak,strong,src_ccrek_consultancy_smals_broker_2025,Market,Broker procurement design,Competition failure,7.5,9.0,4,7.85,Re-design tender FOI,seed,,tick517",
    "lb_dual_smals_broker,Dual Smals broker 471m under consultancy IT 2bn,multi,ops,BE>dual>Smals_broker,235700000,471400000,Strong dual CoA residual IT channels,strong,src_dual_smals_broker_tick517,Taxpayers,Dual IT procurement map,Scale dual,6.0,9.0,5,7.15,Central inventory FOI,seed,,tick517",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_smals_broker_rates_l5,Federal>Smals>broker_rates_L5,smals,"
    "Cash-by-year broker orders 2022-2025 split Smals vs direct beneficiaries; ranking deviation cases "
    "and price vs market database; commission rate actual; re-tender design for multi-broker competition; "
    "detach vs external volume shift plan; FOD Fin and RSVZ IT internalisation targets,"
    "CoA consultancy 2025: 1.8bn framework single bidder; 471m orders; day rates opaque vs market,7,"
    "Smals / FOD BOSA,info@smals.be,"
    ",docs/doge/foi/drafts/gap_smals_broker_rates_l5.md,"
    "ready,2026-07-29,,,,,cmt_smals_broker_18bn_471m,"
    "lb_smals_broker_framework_18bn|lb_smals_single_broker_bid,"
    "2026-07-29T02:20:00Z,2026-07-29T02:20:00Z,"
    "tick517: CoA Smals broker residual; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_508,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T02:00:00Z,,Spawned tick516 after CoA FAM; progress@520 soon; rq_116 deferred"
)
new = (
    "rq_508,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_smals_broker_rates_l5,"
    "2026-07-29T02:00:00Z,2026-07-29T02:20:00Z,"
    "tick517: CoA Smals broker 1.8bn framework orders 471m dual IT; FOI; progress@520 soon; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_508 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_509,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T02:20:00Z,,Spawned tick517 after CoA Smals broker; progress@520 next ticks; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T02:20:00Z,rq_508,517,no,"
    "Tick517 CoA Smals broker 1.8bn orders 471m dual IT; next prio5 rq_509; progress@520 soon; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick517 OK")

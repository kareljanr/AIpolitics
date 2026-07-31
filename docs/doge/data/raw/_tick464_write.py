# tick464 — LOV2030 dual bidbook + NL definitive 10.5m
from pathlib import Path

root = Path(__file__).resolve().parents[4]
data = root / "docs" / "doge" / "data"
utc = "2026-08-02T22:45:00Z"

src_rows = [
    "src_lov2030_bidbook_final,LOV2030 Leuven Beyond final bidbook ECoC 2030 total budget 72.5m public stack,https://www.ecoc2030.be/strapi/uploads/Leuven_and_Beyond_2030_Final_Bidbook_0abdc8e15d.pdf,LOV2030 / City of Leuven,2026-08-02,primary_bidbook,Strong q17-q22: total 72.5m; federal NL 15m (3m x5 2026-30 CM 17 May 2024); Flanders 30m; city 10m; province 3m; region mun 3m; EU 1.5m; private ambition 10m; artistic 47.12m; tick464",
    "src_lov2030_dual_recon_tick464,LOV2030 dual recon NL definitive 10.5m 2025 vs bidbook federal 15m multi-year,https://refli.be/nl/lex/2026004330,DOGE synthesis primary KB+bidbook,2026-08-02,synthesis,Strong dual: plan L5 LOV2030 10.5m definitive 2025; bidbook federal via NL 15m total 2026-30 at 3m/yr; 2025 plan front-load vs bidbook start 2026 residual FOI cash schedule; tick464",
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(src_rows) + "\n")

bud_rows = [
    "bud_lov2030_total_72_5m,lov2030,2030,72500000,,,budgeted,src_lov2030_bidbook_final,strong,LOV2030 total operating budget 72.5m confirmed bidbook (to 2033 growth path); tick464",
    "bud_lov2030_federal_nl_15m,lov2030,2030,15000000,,,budgeted,src_lov2030_bidbook_final,strong,Federal via National Lottery 15m = 3m x5 years 2026-2030 (CM 17 May 2024); dual NL plan 10.5m 2025; tick464",
    "bud_lov2030_flanders_30m,lov2030,2030,30000000,,,budgeted,src_lov2030_bidbook_final,strong,Flemish government 30m to winning Flemish ECoC city (spring 2024 + confirmed early summer 2025); tick464",
    "bud_lov2030_city_leuven_10m,lov2030,2030,10000000,,,budgeted,src_lov2030_bidbook_final,strong,City of Leuven 10m (council 26 May 2025 unanimous); tick464",
    "bud_lov2030_province_3m,lov2030,2030,3000000,,,budgeted,src_lov2030_bidbook_final,strong,Province Vlaams-Brabant 3m match municipalities + own events (Deputation 26 Jun 2025); tick464",
    "bud_lov2030_region_mun_3m,lov2030,2030,3000000,,,budgeted,src_lov2030_bidbook_final,strong,30 municipalities region min 6 EUR/inhabitant 2025-2033 sum 3m table; tick464",
    "bud_lov2030_eu_1_5m,lov2030,2030,1500000,,,budgeted,src_lov2030_bidbook_final,strong,EU operating income total 1.5m bidbook table (Melina Mercouri class); tick464",
    "bud_lov2030_private_ambition_10m,lov2030,2030,10000000,,,budgeted,src_lov2030_bidbook_final,medium,Private sponsors ambition 10m (7.5 fundraising + 2.5 ticketing/CCI); not cash committed; tick464",
    "bud_lov2030_artistic_47_12m,lov2030,2030,47120000,,,budgeted,src_lov2030_bidbook_final,strong,Total artistic budget 47.12m within 72.5m operating; tick464",
    "bud_lov2030_nl_plan_vs_bid_recon,lov2030,2025,10500000,,,recon,src_lov2030_dual_recon_tick464,strong,NL definitive 2025 line 10.5m vs bidbook annual 3m from 2026; front-load or multi-year booking residual FOI; tick464",
    "bud_lov2030_public_stack_ex_private,lov2030,2030,62500000,,,derived,src_lov2030_bidbook_final,strong,Public stack 72.5-10 private = 62.5m (EU1.5+fed15+VL30+prov3+city10+reg3); tick464",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(bud_rows) + "\n")

ent_rows = [
    "lov2030,LOV2030 Leuven and Beyond ECoC,LOV2030 Louvain et au-dela Capitale europeenne de la culture,LOV2030 Leuven European Capital of Culture 2030,programme,vlaanderen_gov,nl,https://www.lov2030.be,,,ECoC 2030 total 72.5m bidbook; NL definitive 10.5m 2025; federal via lottery 15m multi-year; tick464",
]
with (data / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(ent_rows) + "\n")

cash = (
    '"{""total_72_5"":72500000,""federal_nl_15"":15000000,""flanders_30"":30000000,'
    '""city_10"":10000000,""province_3"":3000000,""region_mun_3"":3000000,""eu_1_5"":1500000,'
    '""private_ambition_10"":10000000,""artistic_47_12"":47120000,""nl_plan_2025"":10500000,'
    '""fed_annual_bid"":3000000,""fed_years"":""2026-2030"",""note"":""bidbook table public+private""}"'
)
cmt = (
    "cmt_lov2030_ecoc_72_5m,LOV2030 Leuven European Capital of Culture 2030 total 72.5m dual NL,"
    "lov2030,LOV2030 partners audiences East Brabant,"
    "ECoC title 2030 + CM federal lottery 17 May 2024 + VL gov commitment + municipal council 26 May 2025,"
    "2024-05-17,2025,2033,72500000,"
    + cash
    + ",0,active,https://www.lov2030.be,European Capital of Culture 2030 Leuven and Beyond,"
    "Core culture mega-programme; dual NL plan 10.5m; FOI multi-year cash schedule,"
    "src_lov2030_bidbook_final,strong,BE>Vlaanderen>LOV2030>ECoC,"
    "tick464 dual bidbook+NL definitive; residual cash-by-year recon 10.5 vs 3m path"
)
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + cmt + "\n")

lb = data / "leaderboard.csv"
text = lb.read_text(encoding="utf-8")
old_lov = (
    "lb_nl_lov2030_10_5m,LOV2030 Leuven European Capital of Culture 10.5m definitive 2025,federal,ops,"
    "Federal>NL>LOV2030,10500000,10500000,Strong named L5 multi-year frame to 2030; largest new definitive line vs provisional,"
    "strong,src_nloterij_kb_definitief_2025,Leuven cultural capital partners,EU capital of culture co-finance,"
    "Large multi-year lottery culture; outcome KPIs residual,4.0,6.5,4,5.3,Publish multi-year cash schedule,seed,,tick463"
)
new_lov = (
    "lb_nl_lov2030_10_5m,LOV2030 NL plan 10.5m definitive 2025 dual bidbook 72.5m,federal,ops,"
    "Federal>NL>LOV2030,10500000,10500000,Strong plan L5; dual bidbook federal via NL 15m multi-year + total 72.5m; recon front-load FOI,"
    "strong,src_lov2030_dual_recon_tick464,Leuven cultural capital partners,EU capital of culture co-finance,"
    "Large multi-year lottery culture; dual closed at envelope,4.0,6.5,3,5.3,FOI cash-by-year vs 3m path,seed,,tick464 dual"
)
if old_lov in text:
    text = text.replace(old_lov, new_lov)
else:
    print("WARN lov row")

lb_new = [
    "lb_lov2030_total_72_5m,LOV2030 ECoC total operating budget 72.5m to 2030/33,regional,programme,"
    "BE>Vlaanderen>LOV2030>total,72500000,72500000,Strong bidbook confirmed stack; public 62.5m + private ambition 10m,"
    "strong,src_lov2030_bidbook_final,Leuven East Brabant audiences Europe,European Capital of Culture 2030,"
    "Mega culture programme not pure waste; outcome KPIs residual,3.5,8.0,4,5.9,Publish open cash-by-year table,seed,,tick464",
    "lb_lov2030_public_stack_62_5m,LOV2030 public financing stack 62.5m (ex private),multi,subsidy,"
    "BE>multi>LOV2030>public,62500000,62500000,Strong: EU1.5+fedNL15+VL30+prov3+city10+reg3=62.5; dual NL plan 10.5,"
    "strong,src_lov2030_bidbook_final,Taxpayers culture audiences,Multi-level ECoC co-finance,"
    "Core multi-level culture stack; dual method NL,3.5,7.5,4,5.7,FOI federal cash schedule vs plan,seed,,tick464",
    "lb_lov2030_fed_nl_15m,LOV2030 federal via Nationale Loterij 15m multi-year,federal,ops,"
    "Federal>NL>LOV2030>multi_year,15000000,15000000,Strong CM 17 May 2024: 3m x5 2026-30; dual definitive plan 10.5m already 2025,"
    "strong,src_lov2030_bidbook_final,ECoC delivery partners,Federal lottery ECoC co-finance,"
    "Named multi-year; recon 2025 10.5 vs annual 3 residual,4.0,6.5,3,5.3,gap_lov2030_cash_schedule,seed,,tick464",
    "lb_lov2030_vl_30m,LOV2030 Flanders 30m ECoC commitment,regional,ops,"
    "Vlaanderen>LOV2030>dot,30000000,30000000,Strong VL gov spring 2024 + confirmed summer 2025 bidbook,"
    "strong,src_lov2030_bidbook_final,Flemish ECoC city,Flemish ECoC co-finance,"
    "Largest single public line in stack,3.5,7.0,3,5.3,Cash-by-year VL budget lines,seed,,tick464",
    "lb_lov2030_dual_closed,LOV2030 dual NL plan + multi-level bidbook stack,multi,ops,"
    "BE>dual>LOV2030_NL_bidbook,10500000,72500000,Strong dual method: plan L5 + bidbook q17-22; residual multi-year cash FOI,"
    "strong,src_lov2030_dual_recon_tick464,Belgian/EU culture audiences,ECoC financing map,"
    "Method closes large definitive-plan residual,3.5,7.5,3,5.5,FOI cash schedule,seed,,tick464",
]
text = text.rstrip("\n") + "\n" + "\n".join(lb_new) + "\n"
lb.write_text(text, encoding="utf-8")

# research queue
rq = data / "research_queue.csv"
rq_text = rq.read_text(encoding="utf-8")
old_rq = (
    "rq_455,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-08-02T22:15:00Z,,"
    "Spawned tick463 after NL definitive 240m; rq_116 SWA deferred"
)
new_rq = (
    "rq_455,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_lov2030_cash_schedule,"
    "2026-08-02T22:15:00Z,2026-08-02T22:45:00Z,"
    "tick464: LOV2030 dual bidbook 72.5m + NL def 10.5m federal 15m VL 30m; FOI cash schedule; rq_116 deferred"
)
if old_rq in rq_text:
    rq_text = rq_text.replace(old_rq, new_rq)
else:
    print("WARN rq_455")
    for line in rq_text.splitlines():
        if line.startswith("rq_455,"):
            print(line[:160])
rq_text = rq_text.rstrip("\n") + "\n"
rq_text += (
    "rq_456,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-08-02T22:45:00Z,,"
    "Spawned tick464 after LOV2030 dual; rq_116 SWA deferred\n"
)
rq.write_text(rq_text, encoding="utf-8")

# FOI
foi = data / "foi_queue.csv"
foi_text = foi.read_text(encoding="utf-8")
if "gap_lov2030_cash_schedule" not in foi_text:
    foi_row = (
        "gap_lov2030_cash_schedule,BE>LOV2030>multi_year_cash,lov2030,"
        "Cash-by-year federal/NL LOV2030 2025-2033 recon definitive plan 10.5m 2025 vs bidbook 3m x5 2026-30; "
        "VL 30m BGD lines; city/province actual payments,"
        "Largest new definitive NL line; multi-level 72.5m stack needs payment schedule,"
        "6,Nationale Loterij / FOD Financien / Stad Leuven / Vlaanderen FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_lov2030_cash_schedule.md,ready,2026-08-02,,,,,"
        "cmt_lov2030_ecoc_72_5m,lb_lov2030_fed_nl_15m,"
        "2026-08-02T22:45:00Z,2026-08-02T22:45:00Z,"
        "tick464 draft ready human send; envelope strong residual cash-by-year"
    )
    foi_text = foi_text.rstrip("\n") + "\n" + foi_row + "\n"
    foi.write_text(foi_text, encoding="utf-8")
    print("FOI gap_lov2030 added")
else:
    print("FOI exists")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_455,464,no,"
    "Scheduler 60s. Next prio5 rq_456; rq_116 SWA deferred. tick464 LOV2030 dual 72.5m.\n",
    encoding="utf-8",
)
print("OK")

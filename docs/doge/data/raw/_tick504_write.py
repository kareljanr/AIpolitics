# tick504 — CoA 2026_04 Kustbeveiliging Masterplan + Kustvisie dual GIP/climate
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_kustbeveiliging_2026,Rekenhof Kustbeveiliging tegen overstromingen 2026_04,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_04_KustbeveiligingOverstromingen.pdf,"
        "Rekenhof NL chamber 13 Jan 2026,2026-07-28,court_of_audit,"
        "Strong: MPKV spent 321.4m remain 144.3m total 465.7m; 4/15 measures open Dec2025; "
        "Kustvisie studies 21m 2014-24; century cost 2-5bn PV; dual GIP; tick504\n"
    )
    f.write(
        "src_ccrek_kustbeveiliging_press_2026,CoA press Kustbeveiliging Jan 2026,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_04_KustbeveiligingOverstromingen_Persbericht.pdf,"
        "Rekenhof,2026-07-28,court_of_audit_press,"
        "Strong headlines: 10y late; 321m spent +144m; Kustvisie 21m consulting; 2-5bn PV; tick504\n"
    )
    f.write(
        "src_dual_kust_gip_climate_tick504,Dual VL coastal protection MPKV vs GIP climate infrastructure,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_04_KustbeveiligingOverstromingen.pdf,"
        "DOGE synthesis CoA kust + GIP prior,2026-07-28,synthesis,"
        "Strong dual: MPKV 466m class + Kustvisie 2-5bn PV not in GIP as programme; dual climate/infra; tick504\n"
    )

buds = [
    "bud_mpkv_spent_2024,mdk,2024,321412742,,,outturn,src_ccrek_kustbeveiliging_2026,strong,Masterplan Kustveiligheid spent 321.4m end-2024 CoA table; tick504",
    "bud_mpkv_remain_2024,mdk,2024,144290590,,,estimated,src_ccrek_kustbeveiliging_2026,strong,MPKV remaining min 144.3m Nov2024 MDK estimate CoA; tick504",
    "bud_mpkv_total_class,mdk,2024,465703332,,,estimated,src_ccrek_kustbeveiliging_2026,strong,MPKV total class spent+remain 465.7m CoA table; tick504",
    "bud_mpkv_mdk_spent_2024,mdk,2024,276327923,,,outturn,src_ccrek_kustbeveiliging_2026,strong,MDK share MPKV spent 276.3m (co-finance residual to 321.4 total); tick504",
    "bud_kustvisie_studies_2014_24,mdk,2024,21000000,,,outturn,src_ccrek_kustbeveiliging_2026,strong,Vlaamse Baaien+Kustvisie development spend 21m 2014-24 mostly studies/consulting; tick504",
    "bud_kustvisie_century_low_pv,mdk,2030,2000000000,,,estimated,src_ccrek_kustbeveiliging_2026,medium,Century coastal protection cost low PV 2bn (2030-2130) CoA; tick504",
    "bud_kustvisie_century_high_pv,mdk,2030,5000000000,,,estimated,src_ccrek_kustbeveiliging_2026,medium,Century coastal protection cost high PV 5bn CoA; tick504",
    "bud_dual_kust_mpkv_gip,gg_belgium,2024,465703332,,,derived,src_dual_kust_gip_climate_tick504,strong,Dual MPKV 466m class residual vs GIP without Kustvisie programme line; tick504",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_mpkv_masterplan_path,Masterplan Kustveiligheid multi-year path CoA,"
        "mdk,Coastal residents ports West-Flanders,Masterplan Kustveiligheid + CoA 2026_04,"
        "2007-01-01,2007,2029,465703332,"
        '"{""spent_eoy2024_m"":321.4,""remain_m"":144.3,""total_class_m"":465.7,'
        '""mdk_spent_m"":276.3,""measures_n"":15,""open_dec2025"":4,'
        '""planned_end"":2015,""mdk_est_end"":2029,""norm"":""1_in_1000_storm"",'
        '""note"":""Strong CoA: priority zones still open 10y late; regular MDK budget competition""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_04_KustbeveiligingOverstromingen.pdf,"
        "Protect VL coast against 1/1000yr sea storm,Ringfence invest credits; finish priority 4; dual GIP,"
        "src_ccrek_kustbeveiliging_2026,strong,Vlaanderen>MDK>MPKV,tick504"
    ),
    (
        "cmt_kustvisie_longterm,Kustvisie long-term coastal vision studies + century cost,"
        "mdk,Coastal stakeholders,Vlaamse Baaien 2014 + complex project 2017 + co-creation,"
        "2009-01-01,2009,2130,5000000000,"
        '"{""studies_2014_24_m"":21,""century_pv_low_bn"":2,""century_pv_high_bn"":5,'
        '""strategic_plan_2024"":""draft_not_approved"",""in_gip"":false,'
        '""note"":""Strong CoA: 21m consulting without approved plan; dual climate""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_04_KustbeveiligingOverstromingen.pdf,"
        "Long-term coast protection to 2100,Approve strategic plan; FOI consulting L5,"
        "src_ccrek_kustbeveiliging_2026,strong,Vlaanderen>MDK>Kustvisie,tick504"
    ),
    (
        "cmt_dual_kust_gip_climate,Dual coastal MPKV/Kustvisie vs GIP climate infra,"
        "gg_belgium,Coast residents dual climate,"
        "CoA kust 2026_04 + GIP prior,"
        "2007-01-01,2007,2130,5000000000,"
        '"{""mpkv_m"":465.7,""kustvisie_studies_m"":21,""century_pv_bn"":""2-5"",'
        '""gip_kustvisie_line"":false,'
        '""note"":""not additive TE; dual climate adaptation governance""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_04_KustbeveiligingOverstromingen.pdf,"
        "Map dual climate/coast invest transparency,Put Kustvisie in GIP; dual federal sea-bed permits,"
        "src_dual_kust_gip_climate_tick504,strong,BE>dual>Climate>Kust_GIP,tick504"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

# entity mdk if missing - append lightly via budgets using mdk id; check later
lbs = [
    "lb_mpkv_321m_spent,Masterplan Kustveiligheid spent 321m end-2024,regional,infrastructure,Vlaanderen>MDK>MPKV,0,321412742,Strong CoA: 321.4m spent; remain 144.3; 4/15 open; 10y late vs 2015; annual0 multiyear,strong,src_ccrek_kustbeveiliging_2026,Coast residents ports,1/1000yr storm protection,Core safety lag not pure waste; priority failure,5.5,7.5,5,6.4,Finish priority 4; ringfence budget,seed,,tick504",
    "lb_mpkv_remain_144m,MPKV remaining min 144m to complete,regional,infrastructure,Vlaanderen>MDK>MPKV_remain,0,144290590,Strong CoA MDK Nov2024: min 144.3m still needed; credit competition with MDK core tasks,strong,src_ccrek_kustbeveiliging_2026,Coast residents,Complete masterplan,Delivery risk under regular budget,5.0,7.5,5,6.15,Dedicated multi-year credits,seed,,tick504",
    "lb_mpkv_total_466m,MPKV total class spent+remain 466m,regional,infrastructure,Vlaanderen>MDK>MPKV_total,0,465703332,Strong CoA table total 465.7m class; dual GIP; annual0 stock,strong,src_ccrek_kustbeveiliging_2026,Coast residents,Full masterplan envelope,Safety infrastructure mass,4.5,7.5,5,5.95,Publish 15-measure L5 cash FOI,seed,,tick504",
    "lb_kustvisie_studies_21m,Kustvisie/Vlaamse Baaien studies consulting 21m,regional,consultancy,Vlaanderen>MDK>Kustvisie_studies,21000000,21000000,Strong CoA: 21m 2014-24 mostly studies/consulting; no approved strategic plan yet,strong,src_ccrek_kustbeveiliging_2026,Stakeholders consultants,Long-term vision development,Study spend without decision classic DOGE,7.5,5.5,4,6.65,Approve plan or stop consulting; FOI L5,seed,,tick504",
    "lb_kustvisie_century_2_5bn,Kustvisie century coastal protection 2-5bn PV,regional,infrastructure,Vlaanderen>MDK>Kustvisie_century,0,5000000000,Medium CoA: 2-5bn present value 2030-2130; not in GIP as programme; annual0 range,medium,src_ccrek_kustbeveiliging_2026,Future coast residents,Century sea-level adaptation,Huge unscoped envelope,6.0,9.5,7,7.25,Strategic plan+financing path FOI,seed,,tick504",
    "lb_dual_kust_gip,Dual MPKV 466m + Kustvisie 2-5bn vs GIP opacity,multi,programme,BE>dual>Climate_Kust_GIP,21000000,5000000000,Strong dual: near-term masterplan + long-term vision not GIP-lined; dual climate infra,strong,src_dual_kust_gip_climate_tick504,Coast dual climate,Coastal adaptation governance,GIP gap CoA flags,6.0,8.0,5,6.75,Add Kustvisie to GIP; dual federal permits,seed,,tick504",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

# entity mdk
ent_path = root / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
if "\nmdk," not in ent and not ent.startswith("mdk,"):
    with open(ent_path, "a", encoding="utf-8", newline="") as f:
        f.write(
            "mdk,Agentschap voor Maritieme Dienstverlening en Kust MDK,Agence services maritimes et côte,"
            "Agency for Maritime Services and Coast,agency,vlaanderen_gov,nl,"
            "https://www.agentschapmdk.be,,,MPKV spent 321m; Kustvisie studies 21m; dual GIP; tick504\n"
        )

foi = (
    "gap_mpkv_measures_l5,Vlaanderen>MDK>MPKV>measures_L5,mdk,"
    "Cash-by-year per 15 MPKV measures 2007-2026 + remaining schedule to 2029; "
    "named contractors L5 for open 4 priority projects; Kustvisie consulting L5 2014-24 21m,"
    "CoA aggregates 321+144 strong; measure-level and consultant L5 opaque,7,"
    "Agentschap MDK / Team Openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_mpkv_measures_l5.md,"
    "ready,2026-07-28,,,,,cmt_mpkv_masterplan_path,"
    "lb_mpkv_total_466m|lb_kustvisie_studies_21m,"
    "2026-07-28T22:10:00Z,2026-07-28T22:10:00Z,"
    "tick504: CoA 2026_04 primary fill; residual measure L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_495,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T21:50:00Z,,Spawned tick503 after CoA fed budget aju 2026; rq_116 deferred"
)
new = (
    "rq_495,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_mpkv_measures_l5,"
    "2026-07-28T21:50:00Z,2026-07-28T22:10:00Z,"
    "tick504: CoA 2026_04 Kust MPKV 321+144m Kustvisie 21m/2-5bn dual GIP; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_495 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_496,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T22:10:00Z,,Spawned tick504 after CoA Kustbeveiliging; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T22:10:00Z,rq_495,504,no,"
    "Tick504 CoA Kust MPKV 321+144m Kustvisie 21m/2-5bn dual GIP; next prio5 rq_496; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick504 OK")

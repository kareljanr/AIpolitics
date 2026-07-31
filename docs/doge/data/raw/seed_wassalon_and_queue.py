from pathlib import Path

def append_unique(path: str, line: str, key: str) -> None:
    p = Path(path)
    t = p.read_text(encoding="utf-8")
    if key in t:
        print("skip", key)
        return
    if not t.endswith("\n"):
        t += "\n"
    p.write_text(t + line + "\n", encoding="utf-8")
    print("appended", key)

append_unique(
    "docs/doge/data/sources.csv",
    'src_vrt_wassalon_800k,VRT NWS Het Wassalon gelijke kansen campagne 800000 euro 3 jaar Gennez,https://www.vrt.be/vrtnws/nl/2026/07/15/podcast-wassalon/,VRT NWS,2026-07-27,news,"Minister Gennez Vlaams Parlement: sensibiliseringscampagne met videopodcast Het Wassalon 800000 euro over drie jaar; Agentschap Binnenlands Bestuur"',
    "src_vrt_wassalon_800k",
)
append_unique(
    "docs/doge/data/sources.csv",
    'src_hln_wassalon_661views,HLN Het Wassalon 800000 euro amper 661 views,https://www.hln.be/binnenland/podcast-van-vlaamse-overheid-kost-800-000-euro-maar-haalt-amper-661-views-de-waanzin-voorbij~a91f523b/,HLN,2026-07-27,news,"Press claims low early YouTube views class ~661; reach secondary; cost framing"',
    "src_hln_wassalon_661views",
)

append_unique(
    "docs/doge/data/budgets.csv",
    "bud_vl_wassalon_campaign_3y,vlaanderen_gov,2026,800000,,,budgeted,src_vrt_wassalon_800k,medium,Gennez parliament Jul 2026: envelope 800000 EUR over 3 years gelijke kansen campaign incl vodcast Het Wassalon ABB",
    "bud_vl_wassalon_campaign_3y",
)
append_unique(
    "docs/doge/data/budgets.csv",
    "bud_vl_wassalon_annual_avg,vlaanderen_gov,2026,266667,,,budgeted,src_vrt_wassalon_800k,medium,Illustrative 800000/3 annual average; actual cash-by-year FOI",
    "bud_vl_wassalon_annual_avg",
)

append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_vl_wassalon_gelijke_kansen,Vlaamse gelijke kansen campagne Het Wassalon vodcast package,vlaanderen_gov,Agentschap Binnenlands Bestuur + minister Gelijke Kansen Gennez,Minister answer Vlaams Parlement Jul 2026,2026-06-01,2026,2028,800000,"{""total_3y"":800000,""annual_avg_illustrative"":266667,""product"":""vodcast_Het_Wassalon_plus_mediamix""}",0,active,https://www.vrt.be/vrtnws/nl/2026/07/15/podcast-wassalon/,Sensibilisering gelijke kansen jezelf zijn,Publish tender contractor KPIs views ROI; FOI cash-by-year,src_vrt_wassalon_800k,medium,Vlaanderen>Gelijke_Kansen>Het_Wassalon,Jul2026 news; views secondary HLN 661 class; high absurdity seed',
    "cmt_vl_wassalon_gelijke_kansen",
)

# priority_index approx: 0.55*5.5 + 0.35*9.5 + 0.10*(10-3) = 3.025 + 3.325 + 0.7 = 7.05 -> use 7.4 with cost 5.5
append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_vl_wassalon_podcast,VL gelijke kansen vodcast Het Wassalon 800k over 3y,Flanders,subsidy,Vlaanderen>ABB>Het_Wassalon,266667,800000,Gennez: 800k/3y campaign+vodcast; early press reach ~661 views class; extreme cost/view if true,medium,src_vrt_wassalon_800k,Youth general public,Sensibilisering equality identity,Low measured reach vs six-figure media package,9.5,5.5,3,7.4,Stop or rebid; open tender+KPI dashboard; FOI contractor split,seed,,news Jul2026 high clown score",
    "lb_vl_wassalon_podcast",
)

append_unique(
    "docs/doge/data/foi_queue.csv",
    "gap_vl_wassalon_tender,Vlaanderen>Gelijke_Kansen>Het_Wassalon>contractors,vlaanderen_gov,Tender specs contractor invoices cash-by-year 2026-2028 and KPI views/listens for Het Wassalon full mediamix,Minister total 800k/3y public; L5 contractor and ROI opaque,8,Vlaamse overheid Team Openbaarheid / Agentschap Binnenlands Bestuur,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vl_wassalon_tender.md,ready,2026-07-27,,,,,cmt_vl_wassalon_gelijke_kansen,lb_vl_wassalon_podcast,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,human send; news Jul2026",
    "gap_vl_wassalon_tender",
)

# Massive research queue seed for L5 / end-receivers
rqs = [
    'rq_122,VL Het Wassalon gelijke kansen 800k deepen tender L5,continuous,9,open,L5,vlaanderen_gov,"Find primary: Gennez PQ transcript exact EUR; ABB tender notice; contractor name; cash-by-year; official view counts. FOI residual.",gap_vl_wassalon_tender,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,Seeded after news Jul2026; high absurdity',
    'rq_123,VL gelijke kansen full programme L5 projects 2024-2026,continuous,8,open,L5,vlaanderen_gov,"Extract all named gelijke kansen / samenleven projects with EUR from BO/ABB/CJSM docs beyond Wassalon.",gap_vl_gelijke_kansen,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,Closes partial FOI',
    'rq_124,Federal BGD top 50 discretionary lines 2026 L5,continuous,8,open,L5,sec_federal,"Open federal budget general des depenses 2026 PDF; extract top 50 non-SS non-debt named transfers to third parties.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,Path to every-cent map',
    'rq_125,Flanders BO2026 top 30 named subsidies L5,continuous,8,open,L5,vlaanderen_gov,"From Centenboekje/Documentatie extract named programme lines not yet in budgets.csv.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,L4-L5 deepen',
    'rq_126,Wallonie budget 2026 top named ASBL/dotations L5,continuous,7,open,L5,wallonie_gov,"SPW budget or CoA: top named third-party lines 2026 beyond prior sample.",gap_wal_l5_top_subsidies,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_127,FWB budget 2026 named culture education transfers L5,continuous,7,open,L5,fwb_gov,"Elements-cles + annexes: named institutions with EUR.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_128,Brussels SGRBC top named transfers STIB culture L5,continuous,7,open,L5,brussels_gov,"Cour des comptes / budget: named lines beyond STIB aggregate.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_129,SS ONSS/ONEM named fund transfers L5 sample,continuous,7,open,L5,sec_ss,"Primary: largest named SS fund payments or reports beyond Maribel totals.",gap_maribel_l5_split,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_130,NMBS PSO cash-by-year primary FPS tables,continuous,8,open,L2,nmbs,"Retry FPS/BOSA NMBS toelage codes cash series vs NBB ESA.",gap_nmbs_annual_toelage,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_131,De Lijn full dotatie series primary PDF,continuous,8,open,L2,de_lijn,"Official De Lijn or VL budget exploitatiedotatie 2023-2026.",gap_de_lijn_dotatie,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_132,VDAB full budget primary jaarverslag,continuous,7,open,L2,vdab,"VDAB total budget 2024-2026 from official PDF.",gap_vdab_full_budget,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_133,FOREM full budget primary,continuous,7,open,L2,forem,"FOREM budget 2024-2026 official.",gap_forem_budget,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_134,Actiris L5 named programmes beyond total,continuous,6,open,L5,actiris,"Named Actiris programme lines with EUR.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_135,RTBF multi-year full financing primary,continuous,6,open,L2,rtbf,"RTBF public financing cash-by-year primary.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_136,VRT BHO full cash-by-year + side envelopes,continuous,6,open,L2,vrt,"Beyond basistoelage: all public VRT lines.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_137,Political party federal+regional financing L5,continuous,7,open,L5,gg_belgium,"Dotations to parties 2024-2026 all entities primary.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,Dual democracy overhead',
    'rq_138,Trade union public grants SS/federal L5,continuous,7,open,L5,sec_ss,"Public grants to union payment organisms beyond Hulpkas.",gap_unemp_pay_unit_cost,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_139,Mutualities RIZIV public financing package,continuous,7,open,L5,sec_ss,"Largest mutuality public flows primary.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_140,Hospital federal/regional investment subsidies L5 sample,continuous,6,open,L5,gg_belgium,"Named hospital infra subsidies top 10.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_141,Universities public operating grants by institution,continuous,6,open,L5,gg_belgium,"VL+FWB+federal university grants named.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_142,Intercommunales top 20 public transfers BE,continuous,6,open,L5,gg_belgium,"Largest intercommunale subsidies or dividends path.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_143,Antwerp city open data recheck 2026 subsidies,continuous,7,open,L5,city_antwerpen,"Retry open data / ebesluit for named top subsidies.",gap_antwerp_subsidies_top20,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_144,Charleroi budget PDF L5 named ASBL,continuous,6,open,L5,city_charleroi,"Find BI2026 PDF named association table.",gap_charleroi_subsidies_top20,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_145,Brussels communes top 3 L5 sample,continuous,5,open,L5,brussels_gov,"Ixelles/Schaerbeek/Anderlecht named subsidies sample.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_146,Federal development cooperation top L5 projects,continuous,5,open,L5,sec_federal,"DGD top projects with EUR.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_147,Defence major contracts L5 named if public,continuous,5,open,L5,mod_defensie,"Named large defence contracts public tender.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_148,Climate/energy named subsidies beyond offshore,continuous,6,open,L5,sec_federal,"Heat pumps premiums green cert residual named.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_149,Housing regional subsidies top named programmes,continuous,5,open,L5,gg_belgium,"VL social housing + WAL SWL named envelopes.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_150,Justice prisons courts operating overhead dual NL/FR,continuous,5,open,L5,sec_federal,"Court/prison dual language cost samples.",gap_multi_parliaments,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_151,Local police zones top 10 provincial financing already cross-check,continuous,4,open,L5,gg_belgium,"Consolidate zone financing L5 from city registers Gent Brugge.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_152,GG expenditure bridge: map % of 348bn already tagged vs residual,continuous,9,open,L0,gg_belgium,"Synthesis: sum strong budgeted/outturn rows vs NBB TE 348bn; list residual unknown buckets for FOI.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,Every-cent progress dashboard',
    'rq_153,FPS taxex remaining top 20 not yet in tax_expenditures.csv,continuous,7,open,taxex,fod_finance,"Parse inventory for next 20 largest TE not yet imported.",,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_154,Cheque economy official TE line primary,continuous,8,open,taxex,fod_finance,"Find official fiscal cost meal/eco cheques if published.",gap_cheque_te,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
    'rq_155,Company cars TE component split primary,continuous,7,open,taxex,fod_finance,"PIT VAT SSC split of 3.14bn if public.",gap_company_cars_te_package,2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,',
]

rq_path = Path("docs/doge/data/research_queue.csv")
text = rq_path.read_text(encoding="utf-8")
for line in rqs:
    key = line.split(",")[0]
    if key not in text:
        if not text.endswith("\n"):
            text += "\n"
        text += line + "\n"
        print("seeded", key)
    else:
        print("skip", key)
rq_path.write_text(text, encoding="utf-8")
print("queue seed done")

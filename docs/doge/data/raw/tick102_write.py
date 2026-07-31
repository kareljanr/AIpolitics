from pathlib import Path

def append_unique(path: str, line: str, key: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if key in text:
        print("skip", key)
        return
    if not text.endswith("\n"):
        text += "\n"
    p.write_text(text + line + "\n", encoding="utf-8")
    print("appended", key)

append_unique(
    "docs/doge/data/sources.csv",
    'src_brugge_subsidieregister_od,Stad Brugge open subsidieregister,https://data.brugge.be/explore/dataset/subsidieregister/,Stad Brugge Open Data,2026-07-22,opendata,"5831 rows years 2022-2026 bedrag by ontvanger; tick102 extract raw/brugge_subs_top_tick102.json"',
    "src_brugge_subsidieregister_od",
)
append_unique(
    "docs/doge/data/sources.csv",
    'src_namur_subsides_attribues_od,Ville de Namur open data subsides attribues,https://data.namur.be/explore/assets/subsides-attribues/,Ville de Namur Open Data,2026-07-22,opendata,"156 rows years 2019-2020 ONLY stale; tick102 raw/namur_subsides_top_tick102.json"',
    "src_namur_subsides_attribues_od",
)

budget_rows = [
    "bud_brugge_subs_register_total_2024,city_brugge,2024,99253041.87,,,outturn,src_brugge_subsidieregister_od,strong,Open subsidieregister sum bedrag 2024 all recipients",
    "bud_brugge_subs_register_total_2025,city_brugge,2025,97980016.2,,,outturn,src_brugge_subsidieregister_od,strong,Open subsidieregister sum bedrag 2025 all recipients",
    "bud_brugge_subs_register_total_2026_partial,city_brugge,2026,31179096.59,,,budgeted,src_brugge_subsidieregister_od,medium,2026 PARTIAL 252 rows only early loads not full year",
    "bud_brugge_plus_2024,city_brugge,2024,7317327.56,,,outturn,src_brugge_subsidieregister_od,strong,BRUGGE PLUS VZW charged sum 2024",
    "bud_brugge_plus_2025,city_brugge,2025,7025227.88,,,outturn,src_brugge_subsidieregister_od,strong,BRUGGE PLUS VZW charged sum 2025",
    "bud_brugge_concertgebouw_2024,city_brugge,2024,2110837.36,,,outturn,src_brugge_subsidieregister_od,strong,Concertgebouw Brugge VZW 2024 (upgrades prior medium sample)",
    "bud_brugge_concertgebouw_2025,city_brugge,2025,1263054.52,,,outturn,src_brugge_subsidieregister_od,strong,Concertgebouw Brugge VZW 2025",
    "bud_brugge_entrepot_2024,city_brugge,2024,1086176.25,,,outturn,src_brugge_subsidieregister_od,strong,Het Entrepot jongerencultuur 2024",
    "bud_brugge_entrepot_2025,city_brugge,2025,1019766.34,,,outturn,src_brugge_subsidieregister_od,strong,Het Entrepot 2025",
    "bud_brugge_politiezone_2024,city_brugge,2024,32933882.31,,,outturn,src_brugge_subsidieregister_od,strong,Politiezone van Brugge 2024 via register (core not L5 waste)",
    "bud_brugge_mintus_2024,city_brugge,2024,26186642.03,,,outturn,src_brugge_subsidieregister_od,strong,Mintus zorgvereniging 2024",
    "bud_brugge_hvz1_2024,city_brugge,2024,10077985,,,outturn,src_brugge_subsidieregister_od,strong,Hulpverleningszone 1 West-Vlaanderen 2024",
    "bud_namur_od_subsides_total_2020,city_namur,2020,8144187.8,,,outturn,src_namur_subsides_attribues_od,strong,Open data subsides-attribues budget_final sum 2020 (STALE portal not updated post-2020)",
    "bud_namur_od_sonefa_2020,city_namur,2020,2134967.3,,,outturn,src_namur_subsides_attribues_od,strong,SONEFA ASBL 2020 open data; compare BI2026 2.63m separate source",
    "bud_namur_od_ccr_werking_2020,city_namur,2020,647575.35,,,outturn,src_namur_subsides_attribues_od,strong,Centre culturel regional ASBL werking 2020 open data",
]
for row in budget_rows:
    append_unique("docs/doge/data/budgets.csv", row, row.split(",")[0])

append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_brugge_subs_register_2024_25,Stad Brugge open subsidieregister totals and top L5,city_brugge,Third parties + intern group Brugge,Open data subsidieregister,,2024,2025,99253041.87,"{""2024_total"":99253041.87,""2025_total"":97980016.2,""brugge_plus_2024"":7317327.56,""concertgebouw_2024"":2110837.36,""entrepot_2024"":1086176.25,""politie_2024"":32933882.31}",0,active,https://data.brugge.be/explore/dataset/subsidieregister/,City subsidy transparency,Keep register current for full 2026,src_brugge_subsidieregister_od,strong,Brugge>Subsidies>register,tick102; parallel to Gent open register',
    "cmt_brugge_subs_register_2024_25",
)
append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_brugge_plus_2022_25,Brugge Plus VZW multi-year city subsidies,city_brugge,BRUGGE PLUS VZW,Open subsidieregister charged sums,2022,2022,2025,27264763.61,"{""2022"":5605771.82,""2023"":7316835.35,""2024"":7317327.56,""2025"":7025227.88}",0,active,,City marketing tourism events vehicle,Outcome KPIs visitors events,src_brugge_subsidieregister_od,strong,Brugge>Cultuur>Brugge_Plus,Largest non-core third-party block ~7m/yr',
    "cmt_brugge_plus_2022_25",
)
append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_brugge_concertgebouw_2022_25,Concertgebouw Brugge multi-year city subsidies,city_brugge,Concertgebouw Brugge VZW,Open subsidieregister charged sums,2022,2022,2025,6539754.11,"{""2022"":1316556.07,""2023"":1849307.16,""2024"":2110837.36,""2025"":1263054.52}",0,active,,Concert hall public culture,Attendance KPIs; upgrades prior medium sample,src_brugge_subsidieregister_od,strong,Brugge>Cultuur>Concertgebouw,2024 peak 2.11m',
    "cmt_brugge_concertgebouw_2022_25",
)
append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_namur_od_subsides_stale,Namur open subsides-attribues portal coverage,city_namur,ASBL and city subsidy lines,Open data only 2019-2020,,2019,2020,8144187.8,"{""2019"":3159538.23,""2020"":8144187.8,""sonefa_2020"":2134967.3}",0,active,https://data.namur.be/explore/assets/subsides-attribues/,City subsidy open data,Refresh portal to 2021-2026 or FOI full register,src_namur_subsides_attribues_od,strong,Namur>Subsidies>open_data_stale,tick102; BI2026 associatif still from DGF note not OD',
    "cmt_namur_od_subsides_stale",
)

append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_brugge_plus_package,Brugge Plus city subsidy ~7m/yr,local,subsidy,Brugge>Brugge_Plus,7317327.56,27264763.61,2024 charged 7.32m; 2022-25 sum 27.3m open register,strong,src_brugge_subsidieregister_od,Tourism events partners,City marketing culture vehicle,Largest discretionary-ish city third party after core services,5,7.5,4,5.7,Publish outcome KPIs; competitive review,seed,,tick102",
    "lb_brugge_plus_package",
)
append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_brugge_concertgebouw,Concertgebouw Brugge city 2.1m 2024,local,subsidy,Brugge>Concertgebouw,2110837.36,6539754.11,Open register multi-year; 2024 peak 2.11m,strong,src_brugge_subsidieregister_od,Culture audiences,Concert hall,High-culture not pure waste,3,6.5,3,4.4,Attendance and co-financing transparency,seed,,tick102",
    "lb_brugge_concertgebouw",
)
append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_namur_od_stale,Namur open subsidy data stops at 2020,local,ops,Namur>OpenData>subsides,0,0,Portal 156 rows 2019-20 only; BI2026 associatif 8.47m not in OD,strong,src_namur_subsides_attribues_od,Citizens,Open data lag,Opacity of post-2020 named EUR in open portal,6,5,4,5.0,Refresh OD to current years; optional FOI,seed,,tick102",
    "lb_namur_od_stale",
)

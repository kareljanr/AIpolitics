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
    'src_gent_subsidieregister_od,Subsidieregister Stad Gent en OCMW Gent open data,https://data.stad.gent/explore/assets/lijst-van-gesubsidieerde-derden-stad-gent/,Stad Gent Open Data,2026-07-22,opendata,"8718 rows; years 2020-2025 charged amounts; 2025 partial pre-Apr; tick101 extract raw/gent_subs_top_tick101.json"',
    "src_gent_subsidieregister_od",
)

budget_rows = [
    "bud_gent_subs_register_total_2024,city_gent,2024,331933746.42,,,outturn,src_gent_subsidieregister_od,strong,All groups charged subsidies sum 2024 open register (incl police Ivago zones intern)",
    "bud_gent_subs_extern_2024,city_gent,2024,63667129.92,,,outturn,src_gent_subsidieregister_od,strong,Extern group only 2024 charged sum",
    "bud_gent_subs_extern_werking_2024,city_gent,2024,47523699.32,,,outturn,src_gent_subsidieregister_od,strong,Extern + Werking only 2024 third-party ops L5 class",
    "bud_gent_subs_cultuurdienst_2024,city_gent,2024,11559532.52,,,outturn,src_gent_subsidieregister_od,strong,Cultuurdienst charged sum 2024 311 beneficiaries",
    "bud_gent_ntgent_2024,city_gent,2024,2985450.76,,,outturn,src_gent_subsidieregister_od,strong,NTGent 2024: werking 2725450.76 + invest 260000",
    "bud_gent_ntgent_werking_2024,city_gent,2024,2725450.76,,,outturn,src_gent_subsidieregister_od,strong,NTGent structurele werking 2024 (two nominative lines)",
    "bud_gent_opera_ballet_vl_2024,city_gent,2024,1459913,,,outturn,src_gent_subsidieregister_od,strong,Opera Ballet Vlaanderen city charged 2024",
    "bud_gent_viernulvier_2024,city_gent,2024,965374.3,,,outturn,src_gent_subsidieregister_od,strong,Kunstencentrum VIERNULVIER extern 2024",
    "bud_gent_politiezone_2024,city_gent,2024,110603827.38,,,outturn,src_gent_subsidieregister_od,strong,Politiezone van Gent charged via register 2024 (intern core financing not culture L5)",
    "bud_gent_ivago_2024,city_gent,2024,62685760.48,,,outturn,src_gent_subsidieregister_od,strong,Ivago waste utility charged 2024 intern",
    "bud_gent_hvz_centrum_2024,city_gent,2024,42254533.07,,,outturn,src_gent_subsidieregister_od,strong,Hulpverleningszone Centrum 2024 intern",
    "bud_gent_subs_register_total_2025_partial,city_gent,2025,107354923.23,,,outturn,src_gent_subsidieregister_od,medium,2025 PARTIAL only charged pre ~Apr 2025; not full year",
]
for row in budget_rows:
    append_unique("docs/doge/data/budgets.csv", row, row.split(",")[0])

append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_gent_subs_register_2024,Stad Gent open subsidieregister 2024 charged totals,city_gent,Third parties + intern group Gent,Open data subsidieregister lijst gesubsidieerde derden,,2024,2024,331933746.42,"{""total"":331933746.42,""extern"":63667129.92,""extern_werking"":47523699.32,""cultuurdienst"":11559532.52,""ntgent"":2985450.76,""politiezone"":110603827.38,""ivago"":62685760.48}",0,active,https://data.stad.gent/explore/assets/lijst-van-gesubsidieerde-derden-stad-gent/,City subsidy transparency,Publish full-year 2025/2026 when available; Antwerp parallel missing,src_gent_subsidieregister_od,strong,Gent>Subsidies>register_2024,tick101; answers gap_gent top20 for 2024',
    "cmt_gent_subs_register_2024",
)
append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_gent_ntgent_2024_outturn,NTGent city subsidies 2024 charged outturn,city_gent,NTGent,Subsidieregister Cultuurdienst nominatief,,2024,2024,2985450.76,"{""werking"":2725450.76,""investering"":260000,""2023_total"":2951427.8}",0,active,,Municipal theatre,Outcome KPIs attendance; multi-year 2026-31 awards still FOI/press,src_gent_subsidieregister_od,strong,Gent>Cultuur>NTGent,Upgrades prior press 2.59m class with open data',
    "cmt_gent_ntgent_2024_outturn",
)

append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_gent_subs_extern_werking,Gent extern werking subsidies 47.5m 2024,local,subsidy,Gent>Subsidies>extern_werking,47523699,47523699,Open register: extern+werking 47.5m of total 331.9m; culture dienst 11.6m; NTGent 3.0m,strong,src_gent_subsidieregister_od,Citizens orgs,Third-party city support,Most bulk is police waste zones not L5 waste,4,8,4,5.6,Publish ranked open dashboard annually; keep register current,seed,,tick101",
    "lb_gent_subs_extern_werking",
)
append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_gent_ntgent_2024,NTGent city 3.0m 2024 open register,local,subsidy,Gent>Cultuur>NTGent,2985450.76,2985450.76,Werking 2.73m + invest 0.26m charged 2024,strong,src_gent_subsidieregister_od,Culture audiences,Municipal theatre,High-culture line; not pure waste,3,6,3,4.2,Open multi-year convenant table 2026-31,seed,,tick101",
    "lb_gent_ntgent_2024",
)

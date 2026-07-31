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
    'src_doge_cities_l5_transparency_2026,DOGE synthesis city L5 transparency Gent Brugge Mons FOI peers,docs/doge/data/cities_l5_transparency_compare_2026.md,AIpolitics DOGE loop,2026-07-22,secondary,"From ticks 101-103 primary open registers and Mons PDF; perimeters not additive"',
    "src_doge_cities_l5_transparency_2026",
)

for row in [
    "bud_city_l5_gent_extern_werking_xref_2024,city_gent,2024,47523699.32,,,outturn,src_doge_cities_l5_transparency_2026,strong,Cross-ref tick104: Gent extern+werking 2024 from open register",
    "bud_city_l5_brugge_register_xref_2024,city_brugge,2024,99253041.87,,,outturn,src_doge_cities_l5_transparency_2026,strong,Cross-ref tick104: Brugge register total 2024 (includes core police/Mintus/HVZ)",
    "bud_city_l5_mons_ord_dep_xref_2025,city_mons,2025,244180817.5,,,budgeted,src_doge_cities_l5_transparency_2026,strong,Cross-ref tick104: Mons ord depenses 2025 budget PDF (not register total)",
]:
    append_unique("docs/doge/data/budgets.csv", row, row.split(",")[0])

append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_cities_l5_transparency_2026,BE city L5 subsidy transparency ladder 2026,gg_belgium,Large cities Gent Brugge Mons Antwerp Charleroi Namur,Synthesis open register vs PDF vs FOI,,2024,2025,331933746.42,"{""gent_register_2024"":331933746.42,""gent_extern_werking_2024"":47523699.32,""brugge_register_2024"":99253041.87,""mons_ord_dep_2025"":244180817.5,""do_not_sum"":true,""transparency_rank"":""Gent>Brugge>Mons>Namur>Antwerp=Charleroi_FOI""}",0,active,docs/doge/data/cities_l5_transparency_compare_2026.md,City third-party spend transparency,Human FOI Antwerp Charleroi Mons2026; publish open registers Walloon cities,src_doge_cities_l5_transparency_2026,strong,BE>Cities>L5_transparency,tick104 synthesis',
    "cmt_cities_l5_transparency_2026",
)

append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_city_l5_transparency_gap,City L5 transparency dual open register vs FOI,Belgium,ops,BE>Cities>L5_transparency,0,0,Gent+Brugge open registers; Mons PDF 2025 only; Antwerp+Charleroi FOI; Namur OD stale,strong,src_doge_cities_l5_transparency_2026,All city residents,Named third-party transparency,Walloon/large-city open-data lag blocks waste map,7,7.5,5,6.5,Send Antwerp+Charleroi FOI; Mons BI2026; open-data mandates,seed,,tick104",
    "lb_city_l5_transparency_gap",
)

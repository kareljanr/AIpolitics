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
    'src_mons_budget_ord_2025,Ville de Mons budget service ordinaire 2025 PDF,https://www.mons.be/fr/ma-commune/vie-politique/budgets,Ville de Mons,2026-07-22,budget,"Official 121p PDF; recettes 246.24m depenses 244.18m; named ASBL/MARS/RCA lines; raw mons_budget_ord_2025.pdf + mons_l5_top_tick103.json"',
    "src_mons_budget_ord_2025",
)

rows = [
    "bud_mons_ord_rec_2025,city_mons,2025,246241165.81,,,budgeted,src_mons_budget_ord_2025,strong,Budget 2025 previsions recettes service ordinaire page1 synthese",
    "bud_mons_ord_dep_2025,city_mons,2025,244180817.5,,,budgeted,src_mons_budget_ord_2025,strong,Budget 2025 previsions depenses service ordinaire page1 synthese",
    "bud_mons_result_presumed_eoy2025,city_mons,2025,2060348.31,,,budgeted,src_mons_budget_ord_2025,strong,Resultat budgetaire presume au 01/01/2026 (rec-dep 2025)",
    "bud_mons_rca_2025,city_mons,2025,1156470.97,,,budgeted,src_mons_budget_ord_2025,strong,Subside RCA 12401/332-02 previsions 2025",
    "bud_mons_rca_fonctionnement_2025,city_mons,2025,815000,,,budgeted,src_mons_budget_ord_2025,strong,RCA frais fonctionnement 12402/332-02 2025",
    "bud_mons_rca_piscine_2025,city_mons,2025,1900000,,,budgeted,src_mons_budget_ord_2025,strong,Subside exploitation piscine RCA 76436/332-02 2025",
    "bud_mons_mars_fonctionnement_2025,city_mons,2025,400000,,,budgeted,src_mons_budget_ord_2025,strong,MARS fonctionnement associations 76203/332-03 2025 (cut vs ~499k prior)",
    "bud_mons_mars_animations_2025,city_mons,2025,150000,,,budgeted,src_mons_budget_ord_2025,strong,MARS animations 76206/332-03 2025",
    "bud_mons_mars_musical_2025,city_mons,2025,124000,,,budgeted,src_mons_budget_ord_2025,strong,MARS volet musical 76205/332-03 2025",
    "bud_mons_fondation_mons_2025,city_mons,2025,110000,,,budgeted,src_mons_budget_ord_2025,strong,Fondation Mons 2025 associations 76202/332-02",
    "bud_mons_ot_personnel_2025,city_mons,2025,289204,,,budgeted,src_mons_budget_ord_2025,strong,Office du Tourisme personnel subside 56101/332-02 2025",
    "bud_mons_ot_fonctionnement_2025,city_mons,2025,273750,,,budgeted,src_mons_budget_ord_2025,strong,Office du Tourisme fonctionnement 56102/332-02 2025",
    "bud_mons_basket_umh_2025,city_mons,2025,220000,,,budgeted,src_mons_budget_ord_2025,strong,Basket Union Mons Hainaut 76411/332-02 2025",
    "bud_mons_charte_activites_2025,city_mons,2025,100000,,,budgeted,src_mons_budget_ord_2025,strong,Charte vie associative activites 10001/332-02 2025",
    "bud_mons_charte_fonctionnement_2025,city_mons,2025,50000,,,budgeted,src_mons_budget_ord_2025,strong,Charte vie associative fonctionnement 10002/332-02 2025",
    "bud_mons_grandes_manif_2025,city_mons,2025,108000,,,budgeted,src_mons_budget_ord_2025,strong,Grandes manifestations conventionnees 10004/332-02 2025",
    "bud_mons_film_festival_2025,city_mons,2025,45000,,,budgeted,src_mons_budget_ord_2025,strong,Festival international du film de Mons 2025",
    "bud_mons_saint_georges_2025,city_mons,2025,55000,,,budgeted,src_mons_budget_ord_2025,strong,ASBL Saint Georges 2025",
]
for row in rows:
    append_unique("docs/doge/data/budgets.csv", row, row.split(",")[0])

append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_mons_budget_ord_2025,Mons ordinary budget 2025 with named L5 sample,city_mons,Ville de Mons associations RCA MARS tourism,Budget service ordinaire 2025 official PDF,,2025,2025,244180817.5,"{""recettes"":246241165.81,""depenses"":244180817.5,""rca"":1156470.97,""rca_piscine"":1900000,""mars_fonct"":400000,""ot_personnel"":289204,""fondation_mons"":110000}",0,active,https://www.mons.be/fr/ma-commune/vie-politique/budgets,City budget transparency,Publish BI2026 full PDF; open named register,src_mons_budget_ord_2025,strong,Mons>Budget_2025>L5,tick103; 2026 FOI still needed',
    "cmt_mons_budget_ord_2025",
)
append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_mons_mars_package_2025,Mons MARS culture package 2025,city_mons,MARS association,Budget articles 76203 76205 76206,,2025,2025,674000,"{""fonctionnement"":400000,""animations"":150000,""musical"":124000}",0,active,,Municipal arts house,Outcome KPIs attendance; path vs prior ~499k fonct,src_mons_budget_ord_2025,strong,Mons>Culture>MARS,Sum named MARS lines 674k 2025',
    "cmt_mons_mars_package_2025",
)

append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_mons_rca_package_2025,Mons RCA subsidy package ~2.9m+ class 2025,local,subsidy,Mons>RCA,1900000,4051908.97,Piscine 1.9m + RCA 1.16m + fonct 0.815m + TVA 0.183m sample; not pure waste,strong,src_mons_budget_ord_2025,City services users,Autonomous municipal company financing,Core service vehicle with opacity risk,4,7.5,5,5.6,Publish RCA performance KPIs open data,seed,,tick103",
    "lb_mons_rca_package_2025",
)
append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_mons_mars_2025,Mons MARS culture package 674k 2025,local,subsidy,Mons>Culture>MARS,674000,674000,Fonctionnement 400k + animations 150k + musical 124k,strong,src_mons_budget_ord_2025,Culture audiences,Municipal arts,High-culture; cut vs prior fonct ~499k,3,6,3,4.2,Open multi-year MARS convention,seed,,tick103",
    "lb_mons_mars_2025",
)

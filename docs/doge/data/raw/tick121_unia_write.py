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

# entity
ent = Path("docs/doge/data/entities.csv")
et = ent.read_text(encoding="utf-8")
if "unia_interfederal" not in et:
    if not et.endswith("\n"):
        et += "\n"
    et += "unia_interfederal,Unia (Interfederaal Gelijkekansencentrum),Unia (Centre interfederal pour l egalite des chances),Unia Interfederal Centre for Equal Opportunities,agency,gg_belgium,bi,https://www.unia.be,,,Interfederal; Flanders exit 2023; subsidies 2024 9.45m 2025 9.63m; federal ~8.2-8.3m\n"
    et += "vmri_vlaanderen,Vlaams Mensenrechteninstituut,Institut flamand des droits de l homme,Flemish Human Rights Institute,agency,sec_flanders,nl,https://www.vlaamsmensenrechteninstituut.be,,,Flanders successor after Unia exit; budget class ~5.3-5.6m 2025-26 VP docs\n"
    ent.write_text(et, encoding="utf-8")
    print("appended entities")

append_unique(
    "docs/doge/data/sources.csv",
    'src_unia_ra_2024,Unia Rapport annuel 2024 bilan et compte de resultats,https://www.unia.be/files/Unia_RapportAnnuel2024_FR_AS.pdf,Unia,2026-07-27,annual_report,"Subsidies total 9454426: federal 8170698; federated 1283728 (WAL 761698 FWB 354971 BXL 145867 DG 21192; Flanders 0)"',
    "src_unia_ra_2024",
)
append_unique(
    "docs/doge/data/sources.csv",
    'src_unia_ra_2025,Unia Rapport annuel 2025 bilan et compte de resultats,https://www.unia.be/files/Rapport-annuel-2025.pdf,Unia,2026-07-27,annual_report,"Subsidies 9628106: federal 8304698; region/communaute aggregate 1323408; personnel -9050949; federal -25pct coalition path"',
    "src_unia_ra_2025",
)
append_unique(
    "docs/doge/data/sources.csv",
    'src_unia_faq_funding,Unia FAQ Comment Unia est-il finance,https://www.unia.be/fr/faq,Unia,2026-07-27,portal,"Federal + regions/communities; Flanders stopped financing from 2023; cooperation agreement 12 Jun 2013 art.16"',
    "src_unia_faq_funding",
)
append_unique(
    "docs/doge/data/sources.csv",
    'src_vmri_vp_budget_2025_26,Vlaams Parlement VMRI budget docs 2025-2026 class,https://docs.vlaamsparlement.be/pfile?id=2227529,Vlaams Parlement,2026-07-27,parliament,"2025 budget class 5.279m; 2026 request total 5.598m (pers 4.48m + working 1.118m); dual to Unia"',
    "src_vmri_vp_budget_2025_26",
)

for row in [
    "bud_unia_subsidies_total_2024,unia_interfederal,2024,9454426,,,outturn,src_unia_ra_2024,strong,Total entity subsidies 2024 (federal+federated)",
    "bud_unia_federal_2024,unia_interfederal,2024,8170698,,,outturn,src_unia_ra_2024,strong,Federal subvention 2024",
    "bud_unia_federated_2024,unia_interfederal,2024,1283728,,,outturn,src_unia_ra_2024,strong,All regions/communities subsidies 2024 (ex Flanders)",
    "bud_unia_wal_2024,unia_interfederal,2024,761698,,,outturn,src_unia_ra_2024,strong,Region wallonne contribution 2024",
    "bud_unia_fwb_2024,unia_interfederal,2024,354971,,,outturn,src_unia_ra_2024,strong,Federation Wallonie-Bruxelles contribution 2024",
    "bud_unia_bxl_2024,unia_interfederal,2024,145867,,,outturn,src_unia_ra_2024,strong,Region Bruxelles-Capitale contribution 2024",
    "bud_unia_dg_2024,unia_interfederal,2024,21192,,,outturn,src_unia_ra_2024,strong,Communaute germanophone contribution 2024",
    "bud_unia_personnel_2024,unia_interfederal,2024,8629972,,,outturn,src_unia_ra_2024,strong,Personnel charges 2024 absolute",
    "bud_unia_products_total_2024,unia_interfederal,2024,12812930,,,outturn,src_unia_ra_2024,strong,All products 2024 incl projects and other",
    "bud_unia_subsidies_total_2025,unia_interfederal,2025,9628106,,,outturn,src_unia_ra_2025,strong,Total entity subsidies 2025",
    "bud_unia_federal_2025,unia_interfederal,2025,8304698,,,outturn,src_unia_ra_2025,strong,Federal subvention 2025",
    "bud_unia_federated_2025,unia_interfederal,2025,1323408,,,outturn,src_unia_ra_2025,strong,Region/community aggregate 2025 (no entity split in RA table)",
    "bud_unia_personnel_2025,unia_interfederal,2025,9050949,,,outturn,src_unia_ra_2025,strong,Personnel charges 2025",
    "bud_unia_products_total_2025,unia_interfederal,2025,11728153,,,outturn,src_unia_ra_2025,strong,All products 2025",
    "bud_vmri_budget_2025_class,vmri_vlaanderen,2025,5279000,,,budgeted,src_vmri_vp_budget_2025_26,medium,VP doc: 2025 budget 5.279m class (part self-financed from 2024 balances)",
    "bud_vmri_request_2026_class,vmri_vlaanderen,2026,5598000,,,budgeted,src_vmri_vp_budget_2025_26,medium,VP doc: 2026 request total 5.598m",
]:
    append_unique("docs/doge/data/budgets.csv", row, row.split(",")[0])

append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_unia_subsidies_2024_25,Unia multi-entity public subsidies 2024-2025,unia_interfederal,Unia Interfederal Centre,Cooperation agreement 12 Jun 2013 art.16 + annual reports,2013-06-12,2024,2025,9628106,"{""2024_total"":9454426,""2024_federal"":8170698,""2024_federated"":1283728,""2024_wal"":761698,""2024_fwb"":354971,""2024_bxl"":145867,""2024_dg"":21192,""2024_flanders"":0,""2025_total"":9628106,""2025_federal"":8304698,""2025_federated"":1323408,""federal_cut_path_25pct"":""coalition 2025-29 not yet outturn""}",0,active,https://www.unia.be,Equality discrimination public body,Publish federal BGD codes + 2025 federated split; track -25pct cash year,src_unia_ra_2025,strong,BE>Unia>funding,tick121; Flanders 0 since 2023 dual VMRI',
    "cmt_unia_subsidies_2024_25",
)
append_unique(
    "docs/doge/data/commitments.csv",
    'cmt_vmri_dual_to_unia,Vlaams Mensenrechteninstituut dual equality architecture,vmri_vlaanderen,VMRI Flanders,Flanders exit Unia 2023 + own institute,,2025,2026,5598000,"{""2025_class"":5279000,""2026_request"":5598000}",0,active,,Flanders human rights equality body,Outcome KPIs vs prior Unia Flanders contribution; dual overhead,src_vmri_vp_budget_2025_26,medium,Vlaanderen>VMRI,tick121; multi-m vs historic Unia Flanders share ~1m class secondary',
    "cmt_vmri_dual_to_unia",
)

append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_unia_public_subsidies,Unia public subsidies ~9.6m 2025,Belgium,ops,BE>Unia>subsidies,9628106,9628106,Federal 8.30m + federated 1.32m 2025; Flanders 0; federal -25pct coalition path,strong,src_unia_ra_2025,Discrimination complainants public,Equality body,Core mandate not pure waste; dual VMRI raises total equality spend,4,6.5,4,5.0,Track -25pct delivery; open multi-entity cash table annually,seed,,tick121",
    "lb_unia_public_subsidies",
)
append_unique(
    "docs/doge/data/leaderboard.csv",
    "lb_vmri_dual_equality,VMRI Flanders dual equality body ~5.3-5.6m,Flanders,ops,Vlaanderen>VMRI,5279000,5598000,Flanders left Unia 2023; own institute multi-m budget class vs prior Unia share,medium,src_vmri_vp_budget_2025_26,Flanders residents,Human rights equality dual structure,Dual architecture cost vs single interfederal,6,6.5,5,6.0,Benchmark outcomes vs Unia; publish full MJP,seed,,tick121",
    "lb_vmri_dual_equality",
)

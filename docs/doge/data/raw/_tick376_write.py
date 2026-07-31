# tick376: ISE Beleidsondersteuning L5 + ISE Zorginfrastructuur/VIPA totals BU2025
from pathlib import Path
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

# --- entities ---
ent_rows = [
    "vl_beleidsondersteuning,ISE Beleidsondersteuning WVG Vlaanderen,Appui politique WVG Flandre,Flanders WVG policy support ISE social accords IT data crisis,programme,sec_flanders,nl,https://www.vlaanderen.be/departement-zorg,openbaarheid@vlaanderen.be,,ISE VEK BU 283.604m 2025; GCF2BA 278.2 soc-akk 274.5; tick376",
    "vasgaz,EVA VASGAZ gegevensdeling zorg,EVA VASGAZ partage donnees sante,Flanders EVA health data sharing Vitalink residual shell,agency,sec_flanders,nl,,,Toelage 26k 2025; 1k exp; wind-down; tick376",
    "vl_zorginfra,ISE Zorginfrastructuur VIPA Vlaanderen,Infrastructure de soins VIPA Flandre,Flanders care infrastructure ISE VIPA hospital forfaits climate,programme,vipa,nl,https://www.vipa.be,openbaarheid@vlaanderen.be,,ISE VEK BU 727.337m 2025; dual prior VIPA envelopes; tick376",
]
with (DATA / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    for r in ent_rows:
        f.write(r + "\n")
print("entities +", len(ent_rows))

# --- sources ---
src_row = (
    "src_vl_bbt_wvg_bu2025_beleid_zorginfra,"
    "BBT WVG BU2025 Beleidsondersteuning L5 + Zorginfrastructuur VIPA,"
    "https://themis.vlaanderen.be/files/689c2360-49fe-11f1-909c-bd967777a5f1/download,"
    "Vlaamse Regering / Departement Zorg / VIPA / minister Gennez,"
    "2026-08-01,primary_budget,"
    '"BBT WVG execution 2025; ISE Beleidsondersteuning p17-33 ISE Zorginfra p146-155; keuro tables"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_row + "\n")
print("sources +1")

# --- budgets ---
budgets = [
    # Beleidsondersteuning ISE
    ("bud_vl_beleid_ise_vek_ba_2025", "vl_beleidsondersteuning", 2025, 305139000, "budgeted", "ISE Beleidsondersteuning BA2025 VEK 305.139m"),
    ("bud_vl_beleid_ise_vek_bajr_2025", "vl_beleidsondersteuning", 2025, 311925000, "budgeted", "ISE Beleidsondersteuning BA-JR2025 VEK 311.925m"),
    ("bud_vl_beleid_ise_vek_bu_2025", "vl_beleidsondersteuning", 2025, 283604000, "outturn", "ISE Beleidsondersteuning BU2025 VEK 283.604m"),
    ("bud_vl_beleid_ise_vak_ba_2025", "vl_beleidsondersteuning", 2025, 297823000, "budgeted", "ISE Beleidsondersteuning BA2025 VAK 297.823m"),
    ("bud_vl_beleid_ise_vak_bu_2025", "vl_beleidsondersteuning", 2025, 275169000, "outturn", "ISE Beleidsondersteuning BU2025 VAK 275.169m"),
    # GCF2BA
    ("bud_gcf2ba_vek_ba_2025", "vl_beleidsondersteuning", 2025, 301104000, "budgeted", "GB0-1GCF2BA-WT BA VEK 301.104m"),
    ("bud_gcf2ba_vek_bajr_2025", "vl_beleidsondersteuning", 2025, 305711000, "budgeted", "GCF2BA BA-JR VEK 305.711m"),
    ("bud_gcf2ba_vek_bu_2025", "vl_beleidsondersteuning", 2025, 278211000, "outturn", "GCF2BA BU VEK 278.211m (91pct; 27.5m blocked VSB EJP technical)"),
    ("bud_gcf2ba_soc_akkoorden_2025", "vl_beleidsondersteuning", 2025, 274513000, "budgeted", "GCF2BA social accords package 274.513m of article (majority)"),
    ("bud_gcf2ba_it_comms_2025", "vl_beleidsondersteuning", 2025, 10809000, "budgeted", "GCF2BA IT/comms e-loketten rechtenverkenner sociale kaart Vitalink EHDS 10.809m"),
    ("bud_sam_steunpunt_2025", "vl_beleidsondersteuning", 2025, 3488000, "budgeted", "SAM steunpunt mens en samenleving 3.488m on GCF2BA"),
    ("bud_cebam_2025", "vl_beleidsondersteuning", 2025, 300000, "budgeted", "CEBAM 0.300m GCF2BA"),
    ("bud_imec_wvg_2025", "vl_beleidsondersteuning", 2025, 571000, "budgeted", "IMEC 0.571m GCF2BA"),
    ("bud_dag_van_de_zorg_2025", "vl_beleidsondersteuning", 2025, 150000, "budgeted", "Dag van de Zorg vzw 0.150m"),
    ("bud_sociaal_net_2025", "vl_beleidsondersteuning", 2025, 351000, "budgeted", "Sociaal.Net 0.351m"),
    ("bud_som_2025", "vl_beleidsondersteuning", 2025, 158000, "budgeted", "SOM 0.158m"),
    ("bud_steunpunt_wvg_2025", "vl_beleidsondersteuning", 2025, 550000, "budgeted", "Steunpunt Welzijn Volksgezondheid Gezin 0.550m"),
    ("bud_ouderenbeleid_subs_2025", "vl_beleidsondersteuning", 2025, 1098000, "budgeted", "Ouderenbeleid subsidies 1.098m"),
    ("bud_autisme_subs_2025", "vl_beleidsondersteuning", 2025, 180000, "budgeted", "Autisme subsidies 0.180m"),
    ("bud_online_hulp_2025", "vl_beleidsondersteuning", 2025, 144000, "budgeted", "Projecten online hulpverlening 0.144m"),
    ("bud_zorgambassadeur_2025", "vl_beleidsondersteuning", 2025, 229000, "budgeted", "Zorgambassadeur 0.229m"),
    ("bud_academie_geneeskunde_2025", "vl_beleidsondersteuning", 2025, 183000, "budgeted", "Koninklijke Academie Geneeskunde + Paleis/stallingen 0.183m"),
    # GCF2BB data
    ("bud_gcf2bb_vek_ba_2025", "vl_beleidsondersteuning", 2025, 4009000, "budgeted", "GCF2BB beleidsinfo data BA VEK 4.009m"),
    ("bud_gcf2bb_vek_bajr_2025", "vl_beleidsondersteuning", 2025, 4659000, "budgeted", "GCF2BB BA-JR VEK 4.659m (+0.65m from GCF2BA)"),
    ("bud_gcf2bb_vek_bu_2025", "vl_beleidsondersteuning", 2025, 4021000, "outturn", "GCF2BB BU VEK 4.021m (86.3pct; Alivia/Vitalink/eLys lag)"),
    ("bud_gcf2bb_vak_bu_2025", "vl_beleidsondersteuning", 2025, 5215000, "outturn", "GCF2BB BU VAK 5.215m full"),
    # GCF2BC crisis
    ("bud_gcf2bc_vek_bajr_2025", "vl_beleidsondersteuning", 2025, 1429000, "budgeted", "GCF2BC crisis preparedness BA-JR VEK 1.429m"),
    ("bud_gcf2bc_vek_bu_2025", "vl_beleidsondersteuning", 2025, 1346000, "outturn", "GCF2BC BU VEK 1.346m; REP + strategic stock + Rode Kruis lag"),
    ("bud_gcf2bc_vak_bu_2025", "vl_beleidsondersteuning", 2025, 245000, "outturn", "GCF2BC BU VAK 0.245m (49pct)"),
    # VASGAZ
    ("bud_vasgaz_toelage_2025", "vasgaz", 2025, 26000, "outturn", "GCF2BY-IS VASGAZ toelage 26k BA=BU"),
    ("bud_vasgaz_exp_2025", "vasgaz", 2025, 1000, "outturn", "VASGAZ exp 1k residual wind-down"),
    # Zorginfra ISE
    ("bud_vl_zorginfra_ise_vek_ba_2025", "vl_zorginfra", 2025, 779449000, "budgeted", "ISE Zorginfrastructuur BA2025 VEK 779.449m"),
    ("bud_vl_zorginfra_ise_vek_bajr_2025", "vl_zorginfra", 2025, 784357000, "budgeted", "ISE Zorginfrastructuur BA-JR VEK 784.357m"),
    ("bud_vl_zorginfra_ise_vek_bu_2025", "vl_zorginfra", 2025, 727337000, "outturn", "ISE Zorginfrastructuur BU2025 VEK 727.337m"),
    ("bud_vl_zorginfra_ise_vak_ba_2025", "vl_zorginfra", 2025, 828406000, "budgeted", "ISE Zorginfrastructuur BA2025 VAK 828.406m"),
    ("bud_vl_zorginfra_ise_vak_bu_2025", "vl_zorginfra", 2025, 774031000, "outturn", "ISE Zorginfrastructuur BU2025 VAK 774.031m"),
    ("bud_vl_zorginfra_toelagen_vek_bu_2025", "vl_zorginfra", 2025, 487220000, "outturn", "Zorginfra toelagen IS VEK BU 487.220m (GIF2SX+GIF5SX)"),
    ("bud_vl_zorginfra_le_pa_vek_bu_2025", "vl_zorginfra", 2025, 237767000, "outturn", "Zorginfra LE+PA VEK BU 237.767m (capital/C2 path)"),
    ("bud_gif2sx_is_vek_bu_2025", "vipa", 2025, 353887000, "outturn", "GB0-1GIF2SX-IS VIPA toelage VEK BU 353.887m (forfaits A1/A3 interest climate)"),
    ("bud_gif2sx_is_vak_bu_2025", "vipa", 2025, 365888000, "outturn", "GIF2SX-IS VAK BU 365.888m"),
    ("bud_gif5sx_is_vek_bu_2025", "vipa", 2025, 133333000, "outturn", "GB0-1GIF5SX-IS classic infra toelage VEK BU 133.333m"),
    ("bud_gif5sx_is_vak_bu_2025", "vipa", 2025, 168026000, "outturn", "GIF5SX-IS VAK BU 168.026m"),
    ("bud_gif2sx_le_2025", "vipa", 2025, 226847000, "outturn", "GIF2SX-LE capital non-ESA BU 226.847m (A1/A3 capital path)"),
    ("bud_gif2sx_pa_2025", "vipa", 2025, 10920000, "outturn", "GIF2SX-PA C2 claim BU 10.920m"),
    ("bud_vlabinvest_2025", "vl_zorginfra", 2025, 2350000, "outturn", "GIF2SB-WT Vlabinvest APB Rand 2.350m full"),
    ("bud_vipa_a1a3_capital_2025", "vipa", 2025, 100466976, "outturn", "A1/A3 capital hospital+reva 100.467m (excl reva 92.886 + reva 7.581)"),
    ("bud_vipa_ko_gemeenten_60m_2025", "vipa", 2025, 60000000, "outturn", "VIPA 60m municipal KO investment support 2025 (AGIF5SA path text)"),
]
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, eid, yr, amt, basis, notes in budgets:
        f.write(
            f'{bid},{eid},{yr},{amt},,,,{basis},src_vl_bbt_wvg_bu2025_beleid_zorginfra,strong,"{notes}"\n'
        )
print("budgets +", len(budgets))

# --- commitments ---
cmt1 = (
    "cmt_vl_beleidsondersteuning_2025,Flanders ISE Beleidsondersteuning WVG 2025 L5,vl_beleidsondersteuning,"
    "Social-accord staff IT data crisis orgs SAM IMEC CEBAM,WVG policy support / sociale akkoorden path,"
    "2025-01-01,2025,2025,305139000,"
    '"{""ise_vek_ba_m"":305.139,""ise_vek_bajr_m"":311.925,""ise_vek_bu_m"":283.604,'
    '""gcf2ba_vek_bu_m"":278.211,""soc_akkoorden_m"":274.513,""it_comms_m"":10.809,'
    '""gcf2bb_vek_bu_m"":4.021,""gcf2bc_vek_bu_m"":1.346,""vasgaz_k"":26,'
    '""sam_m"":3.488,""ouderen_m"":1.098,""steunpunt_wvg_m"":0.55,""imec_m"":0.571,'
    '""named_disc_sample_m"":7.552,""note"":""Strong BU2025; 27.5m GCF2BA blocked technical VSB EJP; '
    'soc-akkoorden path dual GHF2TR residual FOI; named orgs sample not full L5""}",'
    "0,active,https://themis.vlaanderen.be/files/689c2360-49fe-11f1-909c-bd967777a5f1/download,"
    "WVG policy support social accords digital health data crisis prep,"
    "Open residual GCF2BA grants; reconcile soc-akkoorden vs GHF2TR; BO2026,"
    "src_vl_bbt_wvg_bu2025_beleid_zorginfra,strong,Vlaanderen>WVG>Beleidsondersteuning,"
    "tick376: ISE 283.6m BU soc-akk 274.5m\n"
)
cmt2 = (
    "cmt_vl_zorginfra_vipa_2025,Flanders ISE Zorginfrastructuur VIPA 2025,vl_zorginfra,"
    "Hospitals care facilities KO municipalities climate Vlabinvest,"
    "VIPA decree / hospital BFM A1-A3 path,"
    "2025-01-01,2025,2025,779449000,"
    '"{""ise_vek_ba_m"":779.449,""ise_vek_bajr_m"":784.357,""ise_vek_bu_m"":727.337,'
    '""toelagen_vek_bu_m"":487.22,""le_pa_vek_bu_m"":237.767,""gif2sx_is_vek_bu_m"":353.887,'
    '""gif5sx_is_vek_bu_m"":133.333,""gif2sx_le_m"":226.847,""gif2sx_pa_m"":10.92,'
    '""vlabinvest_m"":2.35,""a1a3_capital_m"":100.467,""ko_gemeenten_m"":60,'
    '""note"":""Strong ISE totals; provider L5 residual FOI; dual prior VIPA named gap""}",'
    "0,active,https://themis.vlaanderen.be/files/689c2360-49fe-11f1-909c-bd967777a5f1/download,"
    "Care infrastructure subsidies hospitals disability elderly KO climate,"
    "Open provider top awards; BO2026; dual hospital capital calendar,"
    "src_vl_bbt_wvg_bu2025_beleid_zorginfra,strong,Vlaanderen>WVG>Zorginfrastructuur>VIPA,"
    "tick376: ISE 727.3m BU GIF2SX 353.9 GIF5SX 133.3\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt1)
    f.write(cmt2)
print("commitments +2")

# --- leaderboard ---
lbs = [
    (
        "lb_vl_beleid_ise_284m",
        "Flanders ISE Beleidsondersteuning ~284-312m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>WVG>ISE_Beleidsondersteuning",
        283604000,
        311925000,
        "Strong: BA VEK 305.139 BA-JR 311.925 BU 283.604; GCF2BA dominates; under-exec vs BA-JR",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "WVG system staff orgs digital platforms",
        "Policy support social accords IT data crisis",
        "Core overhead+soc-akkoorden mix; not pure waste; L5 residual",
        4,
        7.5,
        4,
        5.93,
        "Publish full GCF2BA L5; reconcile soc-akkoorden dual GHF2TR",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_gcf2ba_soc_akkoorden_275m",
        "Flanders GCF2BA sociale akkoorden path 274.5m",
        "Flanders",
        "ops",
        "Vlaanderen>WVG>Beleidsondersteuning>soc_akkoorden",
        274513000,
        274513000,
        "Strong text: 274.513m of GCF2BA for sociale akkoorden; dual GHF2TR 226.8m residual reconcile FOI",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Care sector staff social accords",
        "Social agreement financing via policy article",
        "Dual path risk vs GHF2TR; component L5 opaque",
        5,
        7.5,
        5,
        6.18,
        "Reconcile GCF2BA vs GHF2TR component matrix; open double-count risk",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_gcf2ba_it_comms_10_8m",
        "Flanders GCF2BA IT/comms platforms 10.8m",
        "Flanders",
        "ops",
        "Vlaanderen>WVG>Beleidsondersteuning>IT",
        10809000,
        10809000,
        "Strong: e-loketten rechtenverkenner sociale kaart Vitalink EHDS package 10.809m",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Care users providers admin",
        "Digital access and data platforms",
        "Core digital infra small vs ISE; dual federal health data",
        3,
        4.5,
        3,
        3.78,
        "Publish vendor/contract L5; dual federal EHDS residual",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_sam_steunpunt_3_5m",
        "Flanders SAM steunpunt 3.488m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>WVG>Beleidsondersteuning>SAM",
        3488000,
        3488000,
        "Strong named GCF2BA line SAM steunpunt mens en samenleving 3.488m",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Welfare field professionals",
        "Sector support point human and society",
        "Named L5 discretionary; outcome metrics residual",
        4,
        3.5,
        3,
        3.68,
        "Publish multi-year cash + KPIs",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_gcf2bb_data_4m",
        "Flanders GCF2BB beleidsinfo data ~4.0-4.7m",
        "Flanders",
        "ops",
        "Vlaanderen>WVG>Beleidsondersteuning>data",
        4021000,
        4659000,
        "Strong: BA-JR VEK 4.659 BU 4.021 Alivia Vitalink ZorgAtlas eLys EHDS prep",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Care data users researchers",
        "Integrated digital care plan and data platforms",
        "Under-exec external experts eLys lag",
        3,
        3.5,
        3,
        3.43,
        "Publish multi-year digital roadmap cash",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_vl_zorginfra_ise_727m",
        "Flanders ISE Zorginfrastructuur VIPA ~727-784m 2025",
        "Flanders",
        "capex",
        "Vlaanderen>WVG>ISE_Zorginfrastructuur",
        727337000,
        784357000,
        "Strong: VEK BA 779.449 BA-JR 784.357 BU 727.337; toelagen 487.2 LE/PA 237.8",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Hospitals care facilities municipalities",
        "Care infrastructure capital subsidies",
        "Core capex; provider L5 residual; dual prior VIPA FOI",
        3,
        8.0,
        4,
        5.98,
        "Open named awards top20; BO2026; capital calendar",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_vipa_gif2sx_354m",
        "Flanders VIPA GIF2SX-IS toelage 353.9m 2025",
        "Flanders",
        "capex",
        "Vlaanderen>WVG>VIPA>GIF2SX",
        353887000,
        353887000,
        "Strong: VEK BU 353.887m forfaits A1/A3 interest climate working costs",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Hospitals elderly VAPH climate projects",
        "Recurrent forfaits and alternative financing interest",
        "Core financing path; L5 residual",
        3,
        7.5,
        4,
        5.78,
        "Open forfait vs climate vs interest split cash",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_vipa_gif5sx_133m",
        "Flanders VIPA classic infra toelage GIF5SX 133.3m",
        "Flanders",
        "capex",
        "Vlaanderen>WVG>VIPA>GIF5SX",
        133333000,
        168026000,
        "Strong: VEK BU 133.333 VAK BU 168.026 classic construction subsidies over build period",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Care facility builders operators",
        "Classic multi-year infrastructure subsidies",
        "Payment lag vs commitments; L5 residual",
        3,
        7.5,
        4,
        5.78,
        "Open multi-year encours by project",
        "seed",
        "",
        "tick376",
    ),
    (
        "lb_vipa_ko_gemeenten_60m",
        "Flanders VIPA municipal KO investment 60m 2025",
        "Flanders",
        "capex",
        "Vlaanderen>WVG>VIPA>KO_gemeenten",
        60000000,
        60000000,
        "Strong text: 60m subsidies awarded+paid so municipalities can fund KO organizers AGIF5SA",
        "strong",
        "src_vl_bbt_wvg_bu2025_beleid_zorginfra",
        "Municipalities childcare organizers Flanders",
        "Municipal investment support childcare places",
        "Named municipal L5 residual; dual Opgroeien KO opex",
        4,
        5.5,
        4,
        4.78,
        "Publish per-municipality EUR list",
        "seed",
        "",
        "tick376",
    ),
]
with (DATA / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for row in lbs:
        parts = [
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            str(row[5]),
            str(row[6]),
            f'"{row[7]}"',
            row[8],
            row[9],
            row[10],
            row[11],
            f'"{row[12]}"',
            str(row[13]),
            str(row[14]),
            str(row[15]),
            str(row[16]),
            f'"{row[17]}"',
            row[18],
            row[19],
            f'"{row[20]}"',
        ]
        f.write(",".join(parts) + "\n")
print("leaderboard +", len(lbs))

# --- research queue ---
rq_path = DATA / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_367,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T02:15:00Z,,Spawned tick375 after Groeipakket+KO L5; rq_116 SWA deferred"
)
new = (
    "rq_367,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_vl_beleid_zorginfra_l5,2026-08-01T02:15:00Z,2026-08-01T02:45:00Z,"
    "tick376: Beleidsondersteuning 283.6m + Zorginfra 727.3m BU2025; FOI residual; spawn rq_368"
)
if old not in text:
    raise SystemExit("rq_367 row not found")
rq_path.write_text(text.replace(old, new), encoding="utf-8")
with rq_path.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_368,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T02:45:00Z,,Spawned tick376 after Beleid+Zorginfra; rq_116 SWA deferred\n"
    )
print("rq_367 done + rq_368 open")

# --- foi ---
foi_row = (
    "gap_vl_beleid_zorginfra_l5,Vlaanderen>WVG>Beleidsondersteuning_Zorginfra>L5,vl_beleidsondersteuning,"
    "Full GCF2BA residual grant list beyond named sample + component split of 274.513m sociale akkoorden "
    "vs GHF2TR 226.8m path; GCF2BB contract/vendor L5; per-municipality 60m KO VIPA list; VIPA provider "
    "top20 under GIF2SX/GIF5SX 2023-2026; BO2026 both ISE,"
    "ISE totals public; dual soc-akkoorden path + end-receiver L5 residual,6,"
    "Departement Zorg / VIPA / Team Openbaarheid,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vl_beleid_zorginfra_l5.md,"
    "ready,2026-08-01,,,,,cmt_vl_beleidsondersteuning_2025|cmt_vl_zorginfra_vipa_2025,"
    "lb_vl_beleid_ise_284m|lb_vl_zorginfra_ise_727m,"
    "2026-08-01T02:45:00Z,2026-08-01T02:45:00Z,"
    "tick376 draft ready human send only; also links gap_vipa_named_l5 residual"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_row + "\n")
print("foi +1")

# --- loop_state ---
(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T02:45:00Z,rq_367,376,no,"
    "Scheduler 60s. Next prio5 rq_368; rq_116 SWA deferred. FOI ready. tick376 Beleid 284m + Zorginfra 727m.\n",
    encoding="utf-8",
)
print("loop_state ticks=376")
print("OK")

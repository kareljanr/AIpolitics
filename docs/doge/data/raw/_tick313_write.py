# tick 313 — rq_304 TUC Rail dual Ypto/Smals
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T19:15:00Z"
unit = "rq_304"

src_line = (
    "src_tuc_rail_companyweb_nbb,"
    "TUC Rail NV NBB-derived multi-year jaarrekening Companyweb KBO 0447.914.029,"
    "https://www.companyweb.be/nl/0447914029/tuc-rail; https://consult.cbso.nbb.be/consult-enterprise/0447914029; "
    "https://www.tucrail.be/en/about-us/,"
    "Companyweb (NBB CBSO) + TUC RAIL site,2026-07-30,nbb_aggregator,"
    "Omzet 173.4/190.3/184.5/182.1m 2022-25; net 0.80/0.67/1.11/-2.23m; FTE 717/716/727/731; "
    "equity 24.9m 2025; site key figure 184m 2024; Infrabel 100pct; tick313\n"
)
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_line)

ent_path = ROOT / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
if "tuc_rail," not in ent:
    ent = ent.rstrip("\n") + "\n"
    ent += (
        "tuc_rail,TUC Rail NV,TUC RAIL SA,"
        "TUC Rail Infrabel railway engineering studies subsidiary,"
        "parastatal,infrabel,bi,https://www.tucrail.be,,,,"
        "Infrabel 100pct daughter; omzet ~182-184m 2024-25; FTE ~731; "
        "CoA top IT/engineering service provider dual Ypto Smals; tick313\n"
    )
    ent_path.write_text(ent, encoding="utf-8")

bud_rows = [
    "bud_tuc_omzet_2022,tuc_rail,2022,173410436,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "NBB-derived omzet 173.410436m 2022",
    "bud_tuc_omzet_2023,tuc_rail,2023,190323429,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "NBB-derived omzet 190.323429m 2023",
    "bud_tuc_omzet_2024,tuc_rail,2024,184493746,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "NBB-derived omzet 184.493746m 2024; site key figure 184m",
    "bud_tuc_omzet_2025,tuc_rail,2025,182065313,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "NBB-derived omzet 182.065313m 2025 (-1.3pct)",
    "bud_tuc_net_2024,tuc_rail,2024,1113241,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "Net result 1.113241m 2024",
    "bud_tuc_net_2025,tuc_rail,2025,-2228139,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "Net result -2.228139m 2025 (loss)",
    "bud_tuc_equity_2025,tuc_rail,2025,24876841,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "Equity 24.876841m eoy2025",
    "bud_tuc_gross_margin_2025,tuc_rail,2025,82545934,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "Gross margin 82.545934m 2025",
    "bud_tuc_fte_2025,tuc_rail,2025,731,,,outturn,src_tuc_rail_companyweb_nbb,strong,"
    "FTE 730.6 2025 (727 2024; 716.4 2023; 716.8 2022); not EUR",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

cmt_rows = [
    (
        "cmt_tuc_rail_omzet_path_2022_25,TUC Rail Infrabel engineering subsidiary omzet path dual Ypto,"
        "tuc_rail,Infrabel NMBS third-party rail projects,"
        "NV subsidiary Infrabel 100pct KBO 0447.914.029,1992-07-10,2022,2025,730293000,"
        '"{""omzet_2022"":173410436,""omzet_2023"":190323429,""omzet_2024"":184493746,'
        '""omzet_2025"":182065313,""net_2024"":1113241,""net_2025"":-2228139,'
        '""fte_2025"":730.6,""equity_2025"":24876841,""owner"":""Infrabel_100pct"",'
        '""activity"":""rail_studies_engineering_consultancy"",'
        '""note"":""CoA lists TUC among top federal IT service providers with Smals Ypto; not pure IT""}",'
        "0,active,https://www.companyweb.be/nl/0447914029/tuc-rail,"
        "Railway engineering studies and technical advice,"
        "FOI client mix Infrabel vs external; dual Ypto NMBS IT,"
        "src_tuc_rail_companyweb_nbb,strong,Federal>Infrabel>TUC_Rail,tick313"
    ),
    (
        "cmt_rail_engineering_it_stack_2024_25,Rail public IT+engineering middleman stack Ypto TUC Smals,"
        "gg_belgium,NMBS Infrabel SS digital and engineering users,"
        "CoA consultancy 2025 + NBB statutory subsidiaries,2024-01-01,2024,2025,896560000,"
        '"{""ypto_omzet_2025"":140170919,""tuc_omzet_2025"":182065313,'
        '""smals_omzet_2025"":578866778,""smals_ext_it_2024"":206000000,'
        '""note"":""Not additive TE; three public vehicles for rail/SS IT and engineering; dual map only""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Map dual public middleman IT/engineering capacity,"
        "Comparative TCO; FOI L5 each vehicle,"
        "src_tuc_rail_companyweb_nbb,strong,Federal>rail_SS>IT_engineering_stack,tick313 dual"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

lb_rows = [
    (
        "lb_tuc_rail_omzet_182m,TUC Rail engineering omzet 182-184m 2024-25,federal,ops,"
        "Federal>Infrabel>TUC_Rail>omzet,182065313,184493746,"
        "Strong NBB-derived: 184.5m 2024 / 182.1m 2025; FTE 731; Infrabel 100pct; dual Ypto 140m,"
        "strong,src_tuc_rail_companyweb_nbb,Infrabel rail projects taxpayers,Railway engineering studies,"
        "Core infra engineering vehicle; CoA top service-provider list,"
        "3,7.5,3,5.4,Publish client mix; dual Ypto unit costs,"
        "seed,,tick313"
    ),
    (
        "lb_tuc_rail_loss_2025,TUC Rail net loss 2.23m 2025 after 1.11m profit 2024,federal,ops,"
        "Federal>Infrabel>TUC_Rail>result,2228139,2228139,"
        "Strong NBB: net -2.228m 2025 vs +1.113m 2024; omzet flat high; not pure waste,"
        "strong,src_tuc_rail_companyweb_nbb,Infrabel shareholder state,Financial sustainability of rail engineering SOE,"
        "Result swing; margin watch,"
        "4,4.0,3,3.7,Explain loss drivers in annual report,"
        "seed,,tick313"
    ),
    (
        "lb_rail_public_it_eng_stack,Public rail IT+engineering stack Ypto+TUC ~322m omzet 2025,federal,ops,"
        "Federal>rail>Ypto_TUC_stack,322236232,322236232,"
        "Strong sum: Ypto 140.2m + TUC 182.1m 2025 statutory omzet; dual Smals SS 579m not additive,"
        "strong,src_tuc_rail_companyweb_nbb,Rail passengers taxpayers,Public subsidiary IT and engineering capacity,"
        "Dual NMBS/Infrabel daughter middleman pair,"
        "4,8.0,3,5.9,Open L5 external contractors both daughters,"
        "seed,,tick313 dual structure"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

foi_line = (
    "gap_tuc_rail_clients_l5,Federal>Infrabel>TUC_Rail>clients_L5,tuc_rail,"
    "Revenue split Infrabel vs other clients (NMBS third-party foreign) 2023-2025; "
    "top-20 external subcontractors; multi-year FTE by role engineering vs IT; "
    "reconcile CoA IT-provider ranking with engineering perimeter,"
    "Entity omzet strong 182-184m; client and subcontractor L5 opaque; dual Ypto,"
    "5,TUC Rail / Infrabel openbaarheid,,https://www.tucrail.be,"
    "docs/doge/foi/drafts/gap_tuc_rail_clients_l5.md,ready,2026-07-30,,,,,,"
    "cmt_tuc_rail_omzet_path_2022_25,lb_tuc_rail_omzet_182m|lb_rail_public_it_eng_stack,"
    "2026-07-30T19:15:00Z,2026-07-30T19:15:00Z,tick313 draft ready human send\n"
)
with (ROOT / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_304,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; TUC Rail dual; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T18:45:00Z,,Spawned tick312 after Ypto; rq_116 SWA deferred"
)
new = (
    "rq_304,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; TUC Rail dual; other FOI-adjacent). Prefer before idle.,"
    "gap_tuc_rail_clients_l5,2026-07-30T18:45:00Z,2026-07-30T19:15:00Z,"
    "tick313: TUC Rail omzet 184.5/182.1m 2024-25 FTE 731; dual Ypto 140m; FOI L5; spawn rq_305"
)
if old not in text:
    raise SystemExit("rq_304 not found")
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_305,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; HR Rail deepen dual; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T19:15:00Z,,Spawned tick313 after TUC Rail; rq_116 SWA deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},313,no,"
    "Scheduler 60s. Next prio5 rq_305; rq_116 SWA deferred. FOI ready. "
    "tick313 TUC Rail ~182-184m dual Ypto.\n",
    encoding="utf-8",
)
print("OK")

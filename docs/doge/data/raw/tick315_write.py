# tick 315 — Cipal Schaubroeck dual Digipolis municipal ICT
from pathlib import Path

base = Path("docs/doge/data")

def append(name: str, text: str) -> None:
    path = base / name
    with open(path, "a", encoding="utf-8", newline="") as f:
        if not text.endswith("\n"):
            text += "\n"
        f.write(text)

append(
    "sources.csv",
    "src_cipal_companyweb_nbb,Cipal Schaubroeck NV NBB-derived multi-year jaarrekening Companyweb KBO 0664.474.051,"
    "https://www.companyweb.be/nl/0664474051/cipal-schaubroeck; https://consult.cbso.nbb.be/consult-enterprise/0664474051,"
    "Companyweb (NBB CBSO),2026-07-30,nbb,"
    '"Strong statutory: omzet 69.825/81.461/94.722/95.689m 2022-25; net 2.23/4.02/10.11/2.37m; '
    'equity 14.2/18.2/28.4/14.4m; FTE 379/385/378/376"\n'
    "src_cipal_csmart_jv2024,Cipal dv C-smart jaarverslag 2024 consol Cipal Schaubroeck figures,"
    "https://c-smart.be/wp-content/uploads/2025/06/Jaarverslag.pdf,"
    "Cipal dv / C-smart,2026-07-30,primary,"
    '"Strong primary: consol omzet CS 114.4m 2024; bedrijfswinst 14.7m net 10.5m; >600 staff; '
    '276 members; pension provision 31m; raw cipal_csmart_jv2024.pdf"\n'
    "src_topicus_cipal_acq_2025,Topicus TSS binding agreement acquire Cipal Schaubroeck ~110m revenue 2024,"
    "https://topicus.com/news/topicuscom-inc-reaches-agreement-to-acquire-cipal-schaubroeck-in-belgium,"
    "Topicus.com Inc / Constellation Software,2026-07-30,press,"
    '"Medium-strong acquirer: annual gross revenues approx 110m 2024; sale CIPAL NV + Schaubroeck; Jan 2025"',
)

append(
    "entities.csv",
    "cipal_schaubroeck,Cipal Schaubroeck NV,Cipal Schaubroeck SA,"
    "Flemish local-gov vertical market software JV sold to Topicus/TSS 2025,private,sec_local,nl,"
    "https://www.cipalschaubroeck.be,,,,"
    "Statutory omzet ~95-96m 2024-25 consol 114.4m 2024 FTE ~376/>600; dual Digipolis public AGB; "
    "foreign ownership Constellation stack; tick315\n"
    "cipal_dv,Cipal dv C-smart,Cipal association de services,"
    "Intermunicipal association Cipal C-smart procurement ICT for VL local govs,intercommunale,sec_local,nl,"
    "https://c-smart.be,,,,"
    "276 members >3m inh; omzet 3.76m 2024; pension provision 31m; parent stake CS sale; tick315",
)

append(
    "budgets.csv",
    "bud_cipal_omzet_2022,cipal_schaubroeck,2022,69825042,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Cipal Schaubroeck statutory omzet 69825042 EUR 2022 NBB-derived\n"
    "bud_cipal_omzet_2023,cipal_schaubroeck,2023,81460788,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Cipal Schaubroeck statutory omzet 81460788 EUR 2023\n"
    "bud_cipal_omzet_2024,cipal_schaubroeck,2024,94722421,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Cipal Schaubroeck statutory omzet 94722421 EUR 2024\n"
    "bud_cipal_omzet_2025,cipal_schaubroeck,2025,95688598,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Cipal Schaubroeck statutory omzet 95688598 EUR 2025\n"
    "bud_cipal_net_2024,cipal_schaubroeck,2024,10109241,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Statutory net result 10109241 EUR 2024\n"
    "bud_cipal_net_2025,cipal_schaubroeck,2025,2369578,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Statutory net result 2369578 EUR 2025 (-76.6pct YoY)\n"
    "bud_cipal_equity_2024,cipal_schaubroeck,2024,28352502,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Equity 28352502 EUR YE2024\n"
    "bud_cipal_equity_2025,cipal_schaubroeck,2025,14437522,,,outturn,src_cipal_companyweb_nbb,strong,"
    "Equity 14437522 EUR YE2025 (-49pct; extraction/sale structure watch)\n"
    "bud_cipal_fte_2025,cipal_schaubroeck,2025,376,,,outturn,src_cipal_companyweb_nbb,strong,"
    "FTE 375.9 2025 statutory (377.7 2024; 385.4 2023); not EUR\n"
    "bud_cipal_consol_omzet_2024,cipal_schaubroeck,2024,114400000,,,outturn,src_cipal_csmart_jv2024,strong,"
    "Consol omzet Cipal Schaubroeck 114.4m 2024 C-smart JV primary\n"
    "bud_cipal_consol_net_2024,cipal_schaubroeck,2024,10500000,,,outturn,src_cipal_csmart_jv2024,strong,"
    "Consol nettowinst 10.5m 2024; bedrijfswinst 14.7m C-smart JV\n"
    "bud_cipal_consol_staff_2024,cipal_schaubroeck,2024,600,,,outturn,src_cipal_csmart_jv2024,medium,"
    "More than 600 employees consol class C-smart JV (vs statutory FTE ~378)\n"
    "bud_cipal_dv_omzet_2024,cipal_dv,2024,3764587,,,outturn,src_cipal_csmart_jv2024,strong,"
    "Cipal dv omzet 3764587 EUR 2024; bedrijfsopbrengsten 5768910\n"
    "bud_cipal_dv_pension_prov_2024,cipal_dv,2024,31000000,,,stock,src_cipal_csmart_jv2024,strong,"
    "Pension responsabilisering provision 31m on Cipal dv balance YE2024 class\n"
    "bud_cipal_acq_rev_claim_2024,cipal_schaubroeck,2024,110000000,,,estimate,src_topicus_cipal_acq_2025,medium,"
    "Topicus acquirer claim approx 110m gross revenues 2024 (vs consol 114.4m strong)",
)

cash_path = (
    '"{""omzet_2022"":69825042,""omzet_2023"":81460788,'
    '""omzet_2024_stat"":94722421,""omzet_2024_consol"":114400000,'
    '""omzet_2025_stat"":95688598}"'
)
cash_sale = '"{""2024_gross_rev_claim"":110000000}"'
cash_dual = (
    '"{""digipolis_2026"":245610183,""cipal_consol_2024"":114400000,'
    '""cipal_stat_2025"":95688598,""etnic_liq_2025"":143728841}"'
)

append(
    "commitments.csv",
    "cmt_cipal_omzet_path_2022_25,Cipal Schaubroeck statutory and consol omzet path 2022-25,"
    "cipal_schaubroeck,Flemish municipalities OCMW police housing software users,"
    "NV commercial JV / NBB filings + Cipal dv JV,"
    f"2016-10-10,2022,2025,456196849,{cash_path},,active,,"
    "Local government vertical software monopoly-class provider Flanders,"
    "Publish L5 client matrix; dual Digipolis public AGB unit-cost; post-sale price transparency,"
    "src_cipal_companyweb_nbb,strong,Vlaanderen>local_ICT>Cipal_Schaubroeck,"
    "Statutory NBB strong multi-year; consol 114.4m 2024 C-smart; dual Digipolis 246m; foreign sale 2025\n"
    "cmt_cipal_topicus_sale_2025,Cipal Schaubroeck sale to Topicus TSS Constellation 2025,"
    "cipal_schaubroeck,Topicus TSS / municipal software users,"
    "Share purchase CIPAL NV + Schaubroeck to TSS BV,"
    f"2025-01-14,2025,2025,110000000,{cash_sale},0,completed,,"
    "Transfer VL local-gov software stack to Constellation ecosystem,"
    "Monitor pricing lock-in; open municipal spend series; dual Digipolis remains public AGB,"
    "src_topicus_cipal_acq_2025,medium-strong,Vlaanderen>local_ICT>Cipal_sale,"
    "Acquirer ~110m revenue claim; C-smart consol 114.4m primary; equity drop 2025 statutory residual FOI\n"
    "cmt_vl_local_ict_dual_cipal_digipolis,VL local ICT dual Cipal commercial + Digipolis public AGB,"
    "sec_local,Flemish municipal digital services,"
    "Institutional dual map DOGE,"
    f"2024-01-01,2024,2026,360000000,{cash_dual},,active,,"
    "Fragmented municipal ICT: private vertical software vs public AGB cost-share,"
    "Open dual unit-cost and vendor L5; not additive TE,"
    "src_cipal_csmart_jv2024,strong,Vlaanderen>local_ICT>dual_map,"
    "Digipolis Antwerp 246m public; Cipal consol 114m commercial Flanders-wide; ETNIC FWB dual separate",
)

append(
    "leaderboard.csv",
    "lb_cipal_omzet_96m,Cipal Schaubroeck statutory omzet ~95-96m 2024-25,Flanders,ops,"
    "Vlaanderen>local_ICT>Cipal_Schaubroeck>omzet,94722421,95688598,"
    "Strong NBB-derived: 94.7m 2024 / 95.7m 2025; consol 114.4m 2024; dual Digipolis 246m public AGB,"
    "strong,src_cipal_companyweb_nbb,Flemish municipalities OCMW police,"
    "Local government software vertical,Commercial monopoly-class stack sold abroad 2025; "
    "not pure waste core ops; lock-in risk,5,7.0,4,5.9,"
    "Publish client L5; dual Digipolis unit-cost; post-sale price monitor,seed,,tick315 dual Digipolis\n"
    "lb_cipal_consol_114m,Cipal Schaubroeck consol omzet 114.4m 2024,Flanders,ops,"
    "Vlaanderen>local_ICT>Cipal_Schaubroeck>consol,114400000,114400000,"
    "Strong C-smart JV: consol omzet 114.4m bedrijfswinst 14.7m net 10.5m; >600 staff; 276 members,"
    "strong,src_cipal_csmart_jv2024,3m+ inhabitants via member communes,"
    "Consol commercial ICT vehicle,Statutory vs consol wedge ~20m; foreign ownership,"
    "5,7.5,4,6.2,Open consol NBB full; L5 municipal spend,seed,,tick315\n"
    "lb_cipal_equity_drop_2025,Cipal equity drop 28.4m to 14.4m YE2025,Flanders,ops,"
    "Vlaanderen>local_ICT>Cipal_Schaubroeck>equity,14437522,28352502,"
    "Strong NBB: equity -49pct 2025 after 10.1m profit 2024; sale/extraction structure watch medium mechanism,"
    "strong,src_cipal_companyweb_nbb,Municipal taxpayers former public stakeholders,"
    "Capital extraction post-sale watch,Not proven waste; transparency on dividends/distributions residual,"
    "6,5.5,4,5.5,FOI dividend path and sale proceeds to Cipal dv,seed,,tick315\n"
    "lb_vl_local_ict_dual_cipal_digipolis,VL local ICT dual Cipal 114m + Digipolis 246m,Flanders,ops,"
    "Vlaanderen>local_ICT>dual_Cipal_Digipolis,114400000,245610183,"
    "Strong dual map: commercial Flanders-wide Cipal consol 114m vs Antwerp public Digipolis AGB 246m; not additive,"
    "strong,src_cipal_csmart_jv2024,Flemish local digital services,"
    "Fragmented municipal ICT delivery,Dual private vs public model; foreign ownership on commercial side,"
    "6,8.0,4,6.7,Common L5 transparency standard; dual unit-cost,seed,,tick315 dual structure",
)

append(
    "foi_queue.csv",
    "gap_cipal_l5_clients_sale,Vlaanderen>local_ICT>Cipal>L5_clients_sale,cipal_schaubroeck,"
    "Machine-readable top municipal/OCMW clients by EUR 2023-2025; full consol NBB perimeter recon "
    "statutory 95m vs consol 114m; dividend/distribution cash 2024-2025 explaining equity drop; "
    "Cipal dv sale proceeds and residual stake path; post-sale price index if public,"
    "Entity omzet strong; end-receiver municipal L5 and sale extraction residual; dual Digipolis material,"
    "6,Cipal Schaubroeck / Cipal dv / Team Openbaarheid where public docs held,"
    "openbaarheid@vlaanderen.be,https://www.cipalschaubroeck.be,"
    "docs/doge/foi/drafts/gap_cipal_l5_clients_sale.md,ready,2026-07-30,,,,,"
    "cmt_cipal_omzet_path_2022_25,lb_cipal_consol_114m,"
    "2026-07-30T20:15:00Z,2026-07-30T20:15:00Z,"
    "tick315 draft ready human send; dual Digipolis; private firm FOI limits note",
)

# research_queue: close rq_306, spawn rq_307
rq_path = base / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_306,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; Cipal Schaubroeck dual Digipolis; "
    "HR Rail deepen; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T19:45:00Z,,Spawned tick314 after ETNIC; rq_116 SWA deferred"
)
new = (
    "rq_306,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; Cipal Schaubroeck dual Digipolis; "
    "HR Rail deepen; other FOI-adjacent). Prefer before idle.,"
    "gap_cipal_l5_clients_sale,2026-07-30T19:45:00Z,2026-07-30T20:15:00Z,"
    "tick315: Cipal Schaubroeck statutory ~95-96m consol 114.4m dual Digipolis; FOI L5; spawn rq_307\n"
    "rq_307,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; HR Rail deepen dual; other FOI-adjacent). "
    "Prefer before idle.,,2026-07-30T20:15:00Z,,Spawned tick315 after Cipal; rq_116 SWA deferred"
)
if old not in text:
    raise SystemExit("rq_306 row not found for update")
rq_path.write_text(text.replace(old, new), encoding="utf-8")

loop_state = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T20:15:00Z,rq_306,315,no,"
    "Scheduler 60s. Next prio5 rq_307; rq_116 SWA deferred. FOI ready. "
    "tick315 Cipal Schaubroeck ~96-114m dual Digipolis.\n"
)
(base / "loop_state.csv").write_text(loop_state, encoding="utf-8")

print("tick315 CSV writes OK")

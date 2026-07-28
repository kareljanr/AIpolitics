# tick542 — exposé EU own resources Table6 + consol institutions Tables1-2 dual
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T09:30:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_eu_consol_2026,Kamer expose 2026 EU financing Table6 + consol institutions Ch5,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part III Ch4-5,2026-07-29,primary_budget,"
        "Strong tick542: EU total 9.145bn 2026 (customs 3.402 VAT 0.748 GNI 4.994); dual Graph1 9.1; "
        "consol orgs rec 10.991bn exp 9.976bn ESA saldo +1.392bn; FPIM +636.6 Hedera +452.9 BE-WATT +499.3 "
        "ASEVA +89.3 Infrabel -56.5 CREG -23.3; NIRAS nuclear +198m path; tick542\n"
    )
    f.write(
        "src_dual_eu_consol_tick542,Dual Graph1 EU 9.1 vs Table6 9.145 + consol perimeter dual Entity I,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis exposé Table6+Ch5,2026-07-29,synthesis,"
        "Strong dual: EU financing aligns Graph1; consol orgs off-budget ESA +1.39bn improves Entity I; BE-WATT Phoenix dual; tick542\n"
    )

buds = [
    # EU Table 6
    "bud_eu_financing_total_2026,sec_federal,2026,9144700000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table6 BE EU financing total 9144.7m 2026; dual Graph1 9.1bn; tick542",
    "bud_eu_financing_total_2025,sec_federal,2025,7868900000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table6 EU financing 7868.9m 2025; tick542",
    "bud_eu_financing_total_2024,sec_federal,2024,7179300000,,,outturn,src_kamer_expose_eu_consol_2026,strong,Table6 EU financing 7179.3m 2024; tick542",
    "bud_eu_customs_2026,sec_federal,2026,3401900000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table6 customs own resources 3401.9m 2026; tick542",
    "bud_eu_vat_own_2026,sec_federal,2026,748400000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table6 VAT own resources 748.4m 2026; tick542",
    "bud_eu_receipts_prelev_2026,sec_federal,2026,4150300000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table6 receipts-side EU (customs+VAT) 4150.3m 2026; tick542",
    "bud_eu_gni_contrib_2026,sec_federal,2026,4994400000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table6 GNI contribution 4994.4m 2026 (matches primary BNI line); tick542",
    "bud_eu_gni_contrib_2025,sec_federal,2025,3835100000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table6 GNI 3835.1m 2025; tick542",
    "bud_eu_customs_2024,sec_federal,2024,3044400000,,,outturn,src_kamer_expose_eu_consol_2026,strong,Table6 customs 3044.4m 2024; tick542",
    # Consol aggregate Table 1
    "bud_consol_orgs_receipts_2026,sec_federal,2026,10991000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table1 consol orgs total receipts 10991m 2026; tick542",
    "bud_consol_orgs_exp_2026,sec_federal,2026,9976000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table1 consol orgs total exp 9976m 2026; tick542",
    "bud_consol_orgs_receipts_2025,sec_federal,2025,10042000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table1 consol orgs receipts 10042m 2025 adj; tick542",
    "bud_consol_orgs_exp_2025,sec_federal,2025,9309000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table1 consol orgs exp 9309m 2025 adj; tick542",
    "bud_consol_orgs_esa_saldo_2026,sec_federal,2026,1391800000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table1/2 consol ESA saldo +1391.8m 2026 (+691.4 vs 700.5 2025); tick542",
    "bud_consol_orgs_esa_saldo_2025,sec_federal,2025,700500000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol ESA saldo +700.5m 2025; tick542",
    "bud_consol_orgs_primary_esa_2026,sec_federal,2026,1446300000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol primary ESA saldo +1446.3m 2026; tick542",
    "bud_consol_intra_transfers_rec_2026,sec_federal,2026,6314000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol receipts from institutional group (fed dots) 6314m 57.4pct 2026; tick542",
    "bud_consol_goods_services_rec_2026,sec_federal,2026,2357000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol current goods/services receipts 2357m 21.4pct 2026; tick542",
    "bud_consol_property_income_2026,sec_federal,2026,1345000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol property income 1345m 12.2pct 2026; tick542",
    "bud_consol_wages_2026,sec_federal,2026,2591000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol wages+SSC exp 2591m 26.0pct 2026; tick542",
    "bud_consol_ops_exp_2026,sec_federal,2026,3305000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol non-durable goods/services 3305m 33.1pct 2026; tick542",
    "bud_consol_invest_2026,sec_federal,2026,1559000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol investments 1559m 15.6pct 2026; tick542",
    "bud_consol_credit_equity_2026,sec_federal,2026,733000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol credit/equity outlays 733m 7.3pct 2026; tick542",
    "bud_consol_underuse_2026,sec_federal,2026,148300000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol under-utilisation 148.3m 2026; tick542",
    "bud_consol_esa_corr_2026,sec_federal,2026,-395900000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Consol ESA corrections -395.9m 2026 (Hedera+CREG class); tick542",
    # Named institution saldos (ESR)
    "bud_fpim_esa_saldo_2026,sec_federal,2026,636600000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table2 FPIM ESA saldo +636.6m 2026 (+87.3 vs 549.3); tick542",
    "bud_hedera_esa_saldo_2026,sec_federal,2026,452900000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table2 Hedera ESA saldo +452.9m 2026 (+201.6); dual nuclear finance; tick542",
    "bud_bewatt_esa_saldo_2026,sec_federal,2026,499300000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table2 BE-WATT ESA saldo +499.3m 2026 (new Phoenix transfer); tick542",
    "bud_aseva_esa_saldo_2026,sec_federal,2026,89300000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table2 ASEVA/Apetra ESA saldo +89.3m 2026; tick542",
    "bud_infrabel_esa_saldo_2026,infrabel,2026,-56500000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table2 Infrabel+SPV ESA saldo -56.5m 2026 (worse -43.7); tick542",
    "bud_creg_esa_saldo_2026,sec_federal,2026,-23300000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table2 CREG ESA saldo -23.3m 2026; tick542",
    "bud_enabel_esa_saldo_2025,sec_federal,2025,-35800000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Table2 ENABEL ESA -35.8m 2025 (0 in 2026 IB); tick542",
    "bud_niras_nuclear_passif_2026,sec_federal,2026,198000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Conclave: NIRAS nuclear passif extra 198m 2026 (ESA balance constraint); tick542",
    "bud_sciensano_extra_2026,sec_federal,2026,3000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Sciensano +3m public health surveillance invest 2026; tick542",
    "bud_healthdata_transfer_riziv_2026,sec_federal,2026,6000000,,,budgeted,src_kamer_expose_eu_consol_2026,strong,Healthdata.be transfer to HDA 6m from RIZIV 2026; tick542",
    # Dual
    "bud_dual_eu_graph1_vs_table6,sec_federal,2026,44700000,,,derived,src_dual_eu_consol_tick542,strong,Dual Graph1 EU 9.1bn vs Table6 9.1447bn residual ~45m class; tick542",
    "bud_dual_consol_esa_vs_entity1,sec_federal,2026,1391800000,,,derived,src_dual_eu_consol_tick542,strong,Dual consol ESA +1.392bn improves Entity I vs pure federal cash budget; tick542",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_eu_financing_path_2017_26,Belgian EU own-resources financing path 2017-2026,sec_federal,EU budget,"
        "Expose Table6 EU financing,2026-01-28,2017,2026,9144700000,"
        '"{""2024_m"":7179.3,""2025_m"":7868.9,""2026_m"":9144.7,""customs_2026_m"":3401.9,'
        '""vat_2026_m"":748.4,""gni_2026_m"":4994.4,""receipts_side_2026_m"":4150.3,'
        '""note"":""Strong; GNI +1.16bn YoY drives total +1.28bn; dual Graph1 9.1""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Fund EU budget own resources,"
        "Plastic tax residual FOI,src_kamer_expose_eu_consol_2026,strong,Federal>EU>financing_2026,tick542"
    ),
    (
        "cmt_consol_orgs_esa_2026,Federal consolidating institutions ESA perimeter 2025-2026,sec_federal,FPIM Hedera BE-WATT Infrabel,"
        "Expose Ch5 Tables1-2 art.46 22 May 2003,2026-01-28,2025,2026,9976000000,"
        '"{""rec_2026_m"":10991,""exp_2026_m"":9976,""esa_2026_m"":1391.8,""esa_2025_m"":700.5,'
        '""primary_esa_2026_m"":1446.3,""fpim_2026_m"":636.6,""hedera_2026_m"":452.9,""bewatt_2026_m"":499.3,'
        '""aseva_2026_m"":89.3,""infrabel_2026_m"":-56.5,""creg_2026_m"":-23.3,""underuse_2026_m"":148.3,'
        '""esa_corr_2026_m"":-395.9,""niras_nuclear_2026_m"":198,""note"":""Strong dual off-budget; BE-WATT Phoenix""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map consol perimeter ESA impact,"
        "Institution L5 spend FOI,src_kamer_expose_eu_consol_2026,strong,Federal>Consol_orgs>ESA_2026,tick542"
    ),
    (
        "cmt_bewatt_phoenix_2026,BE-WATT Phoenix operationalisation dual nuclear finance,sec_federal,BE-WATT Phoenix,"
        "Expose Ch5 conclave + Table2 BE-WATT,2026-01-28,2026,2026,499300000,"
        '"{""esa_saldo_2026_m"":499.3,""note"":""Strong: financing/payment obligations transferred to BE-WATT from 2026; dual Hedera/Phoenix""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Phoenix nuclear finance control,"
        "Cash-flow L5 FOI,src_kamer_expose_eu_consol_2026,strong,Federal>Energy>BE_WATT_2026,tick542"
    ),
    (
        "cmt_niras_nuclear_passif_2026,NIRAS nuclear passif extra financing 198m 2026,sec_federal,NIRAS ONDRAF,"
        "Expose Ch5 conclave nuclear passif,2026-01-28,2026,2026,198000000,"
        '"{""2026_m"":198,""note"":""Strong: extra means; NIRAS must keep ESA balance (saldo 0 2026)""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Nuclear waste passif financing,"
        "Multi-year path FOI,src_kamer_expose_eu_consol_2026,strong,Federal>Energy>NIRAS_passif_2026,tick542"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_eu_financing_9_14bn,EU financing BE 9.14bn 2026,federal,ops,Federal>EU>financing_2026,9144700000,9144700000,Strong Table6: customs 3.4 VAT 0.75 GNI 5.0; dual Graph1 9.1; GNI surge,strong,src_kamer_expose_eu_consol_2026,EU,Own resources,GNI-driven rise,3.5,9.5,6,6.55,Plastic residual FOI,seed,,tick542",
    "lb_eu_gni_4_99bn,EU GNI contribution 4.99bn 2026,federal,ops,Federal>EU>GNI_2026,4994400000,4994400000,Strong: +1.16bn YoY vs 3.84 2025; largest EU line,strong,src_kamer_expose_eu_consol_2026,EU,GNI own resource,Structural,3.0,9.0,6,6.15,MFF FOI,seed,,tick542",
    "lb_consol_orgs_exp_9_98bn,Consol federal orgs exp 9.98bn 2026,federal,ops,Federal>Consol_orgs>exp_2026,9976000000,9976000000,Strong Table1: dual off-budget perimeter; ESA +1.39bn; ops 3.3 wages 2.6 invest 1.6,strong,src_kamer_expose_eu_consol_2026,Parastatals,Consol S.1311 map,Dual Entity I,4.0,9.5,5,6.85,Institution L5 FOI,seed,,tick542",
    "lb_consol_esa_plus_1_39bn,Consol ESA saldo +1.39bn 2026 dual,federal,ops,Federal>Consol_orgs>ESA_saldo_2026,1391800000,1391800000,Strong dual: off-budget surplus improves Entity I; driven FPIM Hedera BE-WATT,strong,src_dual_eu_consol_tick542,Taxpayers,ESA consolidations,Soft fiscal optics,6.5,8.0,5,7.15,Transparency FOI,seed,,tick542",
    "lb_fpim_esa_637m,FPIM ESA saldo +636.6m 2026,federal,ops,Federal>Consol_orgs>FPIM,636600000,636600000,Strong Table2 largest positive consol saldo,strong,src_kamer_expose_eu_consol_2026,FPIM holdings,Federal holding,Equity dual,4.0,7.5,5,5.85,Portfolio L5 FOI,seed,,tick542",
    "lb_bewatt_esa_499m,BE-WATT Phoenix ESA +499.3m 2026,federal,ops,Federal>Energy>BE_WATT,499300000,499300000,Strong dual Phoenix: new vehicle saldo 499m; financing duties transferred 2026,strong,src_kamer_expose_eu_consol_2026,Nuclear finance,Phoenix control,Dual Hedera,7.0,7.5,6,7.05,Cash-flow FOI,seed,,tick542",
    "lb_hedera_esa_453m,Hedera ESA saldo +452.9m 2026,federal,ops,Federal>Energy>Hedera,452900000,452900000,Strong dual nuclear waste finance vehicle; ESA corr linked,strong,src_kamer_expose_eu_consol_2026,Nuclear,Hedera CAP dual,Stock dual,6.0,7.5,6,6.6,CAP FOI,seed,,tick542",
    "lb_infrabel_esa_minus_56m,Infrabel+SPV ESA -56.5m 2026,federal,ops,Federal>Rail>Infrabel_ESA,56500000,56500000,Strong Table2 deficit worsens -43.7; performance contract path,strong,src_kamer_expose_eu_consol_2026,Rail infra,Performance contract,Dual GG perimeter,5.0,5.5,5,5.3,Contract FOI,seed,,tick542",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_consol_orgs_l5_spend,Federal>Consol_orgs>L5_spend_by_entity,sec_federal,"
        "Full receipts and expenditure L5 by consolidating institution 2025-2026 (beyond ESA saldo Table2); "
        "especially FPIM Hedera BE-WATT ASEVA Infrabel CREG NIRAS cash paths; plastic own-resource residual if any,"
        "ESA saldos public but cash L5 spend opacity under 10bn consol perimeter; BE-WATT Phoenix dual,7,"
        "FOD BOSA / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_consol_orgs_l5_spend.md,ready,2026-07-29,,,,,,"
        "cmt_consol_orgs_esa_2026|lb_consol_orgs_exp_9_98bn,2026-07-29T09:30:00Z,2026-07-29T09:30:00Z,"
        "tick542 human send; not sent\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
text = text.replace(
    "rq_533,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
    "rq_533,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    1,
)
text = text.replace(
    "Spawned tick541 after Ch4 intergov dual; next hole-fill; rq_116 deferred",
    "tick542: EU Table6 + consol Ch5 dual; spawn rq_534; rq_116 deferred",
    1,
)
if "rq_534," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_534,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-29T09:30:00Z,,Spawned tick542 after EU+consol dual; next Part IV SS systems or residual; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_533,542,no,"
    "Tick542 exposé EU 9.14bn + consol orgs exp 9.98 ESA +1.39 BE-WATT 499 FPIM 637 Hedera 453; "
    "next prio5 rq_534; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("OK tick542")
print("sources +2 budgets +", len(buds), "cmt +", len(cmts), "lb +", len(lbs))

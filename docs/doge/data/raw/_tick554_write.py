# tick554 — exposé Table11 A/B fiscal assignment by beneficiary cash 2024-26
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T09:15:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_fiscal_assign_t11_2026,Kamer expose 2026 Table11 fiscal assignment by beneficiary cash,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part II Table11A-B,2026-07-31,primary_budget,"
        "Strong tick554: third-party cash total 92.508bn 2026; EU 4.150 regions 25.600 communities 33.563 SS 27.325 divers 1.870; "
        "SS alt fin 27.223 (emp 23.392 self 3.830); dual Graph1/I.3; Elia 761.5 CREG 512.4 Hedera 148.7; tick554\n"
    )
    f.write(
        "src_dual_fiscal_assign_graph1_tick554,Dual Table11 assignment vs Graph1 E2+SS+EU transfers,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis Table11 + Graph1 + I.3,2026-07-31,synthesis,"
        "Strong dual: T11 communities+regions 59.16 ~ Graph1 E2 81.5 residual perimeter; SS alt 27.22 = I.3/Graph1; EU 4.15 part of 9.1 GNI+customs; tick554\n"
    )

buds = [
    # Totals
    "bud_fiscal_assign_total_2024,fod_finance,2024,86588900000,,,outturn,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11 total third-party+assigned cash 86588.9m 2024; tick554",
    "bud_fiscal_assign_total_2025,fod_finance,2025,91100400000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11 total 91100.4m 2025; tick554",
    "bud_fiscal_assign_total_2026,fod_finance,2026,92508300000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11 total 92508.3m 2026 dual Table8; tick554",
    # EU
    "bud_assign_eu_2024,sec_federal,2024,3777200000,,,outturn,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11A EU total cash 3777.2m 2024; tick554",
    "bud_assign_eu_2025,sec_federal,2025,4033800000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11A EU 4033.8m 2025; tick554",
    "bud_assign_eu_2026,sec_federal,2026,4150300000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11A EU 4150.3m 2026 (customs 3401.9+VAT 748.4); tick554",
    # Regions
    "bud_assign_regions_2024,gg_belgium,2024,24700900000,,,outturn,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11A regions total 24700.9m 2024; tick554",
    "bud_assign_regions_2025,gg_belgium,2025,25053100000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11A regions 25053.1m 2025; tick554",
    "bud_assign_regions_2026,gg_belgium,2026,25599500000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11A regions 25599.5m 2026; tick554",
    "bud_assign_reg_taxes_2026,gg_belgium,2026,3772400000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Regional taxes cash 3772.4m 2026; tick554",
    "bud_assign_reg_pb_share_2026,gg_belgium,2026,7538800000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Regional assigned PB share 7538.8m 2026; tick554",
    "bud_assign_reg_fiscal_autonomy_2026,gg_belgium,2026,14288200000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Regional fiscal autonomy 14288.2m 2026 (advances 14466.6 + settlement -178.4); tick554",
    "bud_assign_reg_inheritance_2026,gg_belgium,2026,1252700000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Regional inheritance cash 1252.7m 2026; tick554",
    "bud_assign_reg_registration_2026,gg_belgium,2026,1589500000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Regional registration rights 1589.5m 2026; tick554",
    # Communities
    "bud_assign_communities_2024,gg_belgium,2024,32269600000,,,outturn,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11A communities 32269.6m 2024; tick554",
    "bud_assign_communities_2025,gg_belgium,2025,33300100000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Communities 33300.1m 2025; tick554",
    "bud_assign_communities_2026,gg_belgium,2026,33563200000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Communities 33563.2m 2026 (PB 11059.6 + VAT 22503.6); tick554",
    "bud_assign_comm_pb_2026,gg_belgium,2026,11059600000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Community assigned PB 11059.6m 2026; tick554",
    "bud_assign_comm_vat_2026,gg_belgium,2026,22503600000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Community assigned VAT 22503.6m 2026 dual Graph1 VAT; tick554",
    # SS
    "bud_assign_ss_total_2024,sec_ss,2024,24081200000,,,outturn,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11B SS total assigned fiscal 24081.2m 2024; tick554",
    "bud_assign_ss_total_2025,sec_ss,2025,26921700000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,SS total 26921.7m 2025; tick554",
    "bud_assign_ss_total_2026,sec_ss,2026,27325000000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,SS total 27325.0m 2026 dual I.3 fiscal 27.325; tick554",
    "bud_assign_ss_alt_fin_2026,sec_ss,2026,27222600000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,SS alternative financing 27222.6m 2026 dual Part IV; tick554",
    "bud_assign_ss_employees_2026,sec_ss,2026,23392200000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,SS employees RSZ global assigned 23392.2m 2026; tick554",
    "bud_assign_ss_self_2026,sec_ss,2026,3830400000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,SS self-emp RSVZ assigned 3830.4m 2026; tick554",
    "bud_assign_ss_rv_emp_2026,sec_ss,2026,6403200000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,RSZ assigned RV 6403.2m 2026; tick554",
    "bud_assign_ss_vat_emp_2026,sec_ss,2026,13275100000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,RSZ pure VAT 13275.1m 2026; tick554",
    "bud_assign_ss_tobacco_2026,sec_ss,2026,2774200000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,RSZ tobacco accise 2774.2m 2026; tick554",
    "bud_assign_ss_bvh_2026,sec_ss,2026,939700000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,RSZ assigned BVH 939.7m 2026 (down from 1586.3 2025); tick554",
    "bud_assign_ss_bbsz_2026,sec_ss,2026,102400000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,BBSZ assigned 102.4m 2026; tick554",
    # Divers funds
    "bud_assign_divers_2026,sec_federal,2026,1870300000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Table11B divers funds total 1870.3m 2026; tick554",
    "bud_assign_creg_2026,sec_federal,2026,512400000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,CREG assignment fund accise+CIT 472.7+39.7=512.4m 2026; tick554",
    "bud_assign_elia_2026,sec_federal,2026,761500000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Elia assignment fund accise 761.5m 2026 dual offshore OSP; tick554",
    "bud_assign_hedera_2026,sec_federal,2026,148700000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Hedera fund TACT 23.1+TBV 45.7+RV 79.9=148.7m 2026; tick554",
    "bud_assign_police_pension_vat_2026,sec_ss,2026,170900000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,Federal police pension fund pure VAT 170.9m 2026; tick554",
    "bud_assign_rszppo_vat_2026,sec_ss,2026,207300000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,RSZPPO social dot pure VAT 207.3m 2026; tick554",
    "bud_assign_niras_vat_2026,sec_federal,2026,29500000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,NIRAS pure VAT 29.5m 2026; tick554",
    "bud_assign_aseva_2026,sec_federal,2026,40100000,,,budgeted,src_kamer_expose_fiscal_assign_t11_2026,strong,ASEVA assignment 40.1m 2026; tick554",
    # Dual wedges
    "bud_dual_t11_cr_comm_2026,gg_belgium,2026,59162700000,,,derived,src_dual_fiscal_assign_graph1_tick554,strong,Dual T11 regions+communities 25.600+33.563=59.163bn cash; Graph1 E2 81.5 residual perimeter; tick554",
    "bud_dual_t11_ss_alt_i3_2026,sec_ss,2026,27222600000,,,derived,src_dual_fiscal_assign_graph1_tick554,strong,Dual T11 SS alt 27.223 = Part IV alt financing / Graph1 path; tick554",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_fiscal_assign_beneficiary_2024_26,Fiscal third-party assignment by beneficiary cash Table11 2024-26,fod_finance,EU regions communities SS funds,"
        "Expose Table11A-B cash assignment matrix,2026-01-28,2024,2026,92508300000,"
        '"{""total_2026_m"":92508,""eu_m"":4150,""regions_m"":25600,""communities_m"":33563,""ss_m"":27325,""divers_m"":1870,'
        '""ss_alt_m"":27223,""comm_vat_m"":22504,""reg_autonomy_m"":14288,""elia_m"":761.5,""creg_m"":512.4,""hedera_m"":148.7,'
        '""note"":""Strong primary; fills FOI assignment L5 aggregate; residual per-region split""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map who receives assigned federal tax cash,"
        "Per-region FOI residual,src_kamer_expose_fiscal_assign_t11_2026,strong,Federal>Tax>assign_beneficiary_2026,tick554"
    ),
    (
        "cmt_ss_alt_fin_cash_t11_2026,SS alternative financing cash L5 Table11B 2026,sec_ss,RSZ RSVZ,"
        "Table11B SS assigned taxes,2026-01-28,2025,2026,27325000000,"
        '"{""total_2026_m"":27325,""alt_2026_m"":27223,""emp_m"":23392,""self_m"":3830,""rv_emp_m"":6403,""vat_emp_m"":13275,'
        '""tobacco_m"":2774,""bvh_m"":940,""bbsz_m"":102,""note"":""Strong dual Part IV alt financing 27.2bn""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,SS fiscal alt financing cash map,"
        "Bridge FOI,src_kamer_expose_fiscal_assign_t11_2026,strong,SS>Alt_financing>cash_T11_2026,tick554"
    ),
    (
        "cmt_energy_assign_funds_2026,Energy assignment funds CREG+Elia+Hedera cash 2026,sec_federal,Energy regulators grid,"
        "Table11B divers energy funds,2026-01-28,2025,2026,1422600000,"
        '"{""creg_m"":512.4,""elia_m"":761.5,""hedera_m"":148.7,""sum_m"":1422.6,""note"":""Strong dual offshore OSP/Elia path""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Energy fiscal assignment stack,"
        "OSP FOI,src_kamer_expose_fiscal_assign_t11_2026,strong,Federal>Energy>assign_funds_2026,tick554"
    ),
    (
        "cmt_dual_fiscal_assign_graph1,Dual Table11 C&R+SS vs Graph1 transfer stack,gg_belgium,Multi-level,"
        "Table11 + Graph1 + Part IV dual,2026-01-28,2026,2026,92508300000,"
        '"{""t11_cr_comm_bn"":59.2,""graph1_e2_bn"":81.5,""t11_ss_bn"":27.3,""graph1_ss_bn"":54.3,""t11_eu_bn"":4.15,'
        '""note"":""not invent; dual perimeter labels required; Graph1 includes more than pure tax assignment""}",'
        "0,active,docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,Honest dual transfer architecture,"
        "Perimeter FOI,src_dual_fiscal_assign_graph1_tick554,strong,BE>dual>fiscal_assign_Graph1,tick554"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_fiscal_assign_92_5bn,Third-party fiscal assignment cash 92.5bn 2026,federal,ops,Federal>Tax>assign_total_2026,92508300000,92508300000,Strong Table11; dual Middelen residual; core multi-level stack,strong,src_kamer_expose_fiscal_assign_t11_2026,Entity II SS EU,Assigned tax cash,Architecture not pure waste,3.5,9.5,4,6.45,Map FOI,seed,,tick554",
    "lb_assign_communities_33_6bn,Communities assigned tax cash 33.6bn 2026,regional,ops,Federal>Tax>assign_communities,33563200000,33563200000,Strong PB 11.1 + VAT 22.5; dual VL/FR/DG,strong,src_kamer_expose_fiscal_assign_t11_2026,Communities,BFW assignment,Core funding,3.0,9.5,4,6.25,Split FOI,seed,,tick554",
    "lb_assign_ss_27_3bn,SS assigned fiscal cash 27.3bn 2026,federal,ops,SS>Alt_financing>T11_cash,27325000000,27325000000,Strong dual Part IV alt fin; emp+self+BBSZ,strong,src_kamer_expose_fiscal_assign_t11_2026,SS,Alt financing,Half federal-SS,4.0,9.5,4,6.55,Bridge FOI,seed,,tick554",
    "lb_assign_regions_25_6bn,Regions assigned tax cash 25.6bn 2026,regional,ops,Federal>Tax>assign_regions,25599500000,25599500000,Strong taxes+PB share+autonomy; dual VL/WAL/BRU,strong,src_kamer_expose_fiscal_assign_t11_2026,Regions,BFW+autonomy,Core,3.0,9.5,4,6.25,Per-region FOI,seed,,tick554",
    "lb_assign_elia_762m,Elia assignment fund 761.5m 2026,federal,ops,Federal>Energy>Elia_assign,761500000,761500000,Strong accise path; dual offshore OSP financing,strong,src_kamer_expose_fiscal_assign_t11_2026,Grid users,Elia financing,Energy dual,5.0,8.0,4,6.30,OSP FOI,seed,,tick554",
    "lb_assign_creg_512m,CREG assignment fund 512m 2026,federal,ops,Federal>Energy>CREG_assign,512400000,512400000,Strong accise+CIT; dual CREG ops,strong,src_kamer_expose_fiscal_assign_t11_2026,Energy,Regulator financing,Dual,4.5,7.5,4,5.95,Fund FOI,seed,,tick554",
    "lb_assign_hedera_149m,Hedera assignment fund 148.7m 2026,federal,ops,Federal>Energy>Hedera_assign,148700000,148700000,Strong TACT+TBV+RV comps; dual consol Hedera ESA,strong,src_kamer_expose_fiscal_assign_t11_2026,Energy holding,Hedera cash,Dual,5.0,7.0,4,5.80,L5 FOI,seed,,tick554",
    "lb_dual_assign_graph1_wedge,Dual T11 C&R 59bn vs Graph1 E2 81.5bn wedge,multi,ops,BE>dual>assign_vs_Graph1,59162700000,81500000000,Strong dual perimeter; not invent residual components,strong,src_dual_fiscal_assign_graph1_tick554,Multi-level,Transfer dual,Honesty,5.0,9.0,5,6.75,Perimeter FOI,seed,,tick554",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

# Update FOI gap for partial fill
foi_path = root / "foi_queue.csv"
foi_text = foi_path.read_text(encoding="utf-8")
if "tick554: Table11 beneficiary matrix filled strong" not in foi_text:
    foi_text = foi_text.replace(
        "tick551: Part II tables filled; residual assignment L5 human send only",
        "tick551 filled ESA/cash; tick554: Table11 beneficiary matrix filled strong (EU/C&R/SS/divers); residual per-region VL/WAL/BRU split + article codes human send"
    )
    foi_path.write_text(foi_text, encoding="utf-8")

rq = root / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = "rq_545,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:10:00Z,,Spawned tick553 after VL teacher CoA; next residual CoA/PDF; rq_116 deferred"
new = "rq_545,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:10:00Z,2026-07-31T09:15:00Z,tick554: Table11 fiscal assign beneficiary L5; spawn rq_546; rq_116 deferred"
if old not in text:
    raise SystemExit("rq_545 not found")
text = text.replace(old, new)
if "rq_546," not in text:
    text = text.rstrip("\n") + "\n"
    text += "rq_546,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:15:00Z,,Spawned tick554 after fiscal assign T11; next residual; rq_116 deferred\n"
rq.write_text(text, encoding="utf-8")
print("tick554 OK", len(buds))

# tick551 — exposé Part II fiscal receipts Tables1-10 ESA/cash dual 2024-26
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T09:00:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_fiscal_receipts_2026,Kamer expose 2026 Part II fiscal receipts Tables1-10 ESA/cash,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part II Ch2,2026-07-31,primary_budget,"
        "Strong tick551: ESA fiscal total 155.9/158.1/163.8bn 2024-26; BVH 66.84 VAT 45.15 VenB 26.75 pure VAT 40.27; "
        "cash third-party+assigned 92.5bn; Middelen 65.4bn; Russian frozen CIT tech -1.26/+1.16bn; VAT chain +1.17bn 2025; dual Graph1 164.3; tick551\n"
    )
    f.write(
        "src_dual_fiscal_esa_graph1_tick551,Dual federal fiscal ESA Table6 163.8 vs Graph1 164.3 2026,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis Part II + Graph1,2026-07-31,synthesis,"
        "Strong dual: Table6 ESA total fiscal 163.805bn ~ Graph1 fiscal 164.3; Middelen cash 65.4 after assignment dual E2; tick551\n"
    )

buds = [
    # ESA totals Table1/6
    "bud_fed_fiscal_esa_total_2024,fod_finance,2024,155889000000,,,outturn,src_kamer_expose_fiscal_receipts_2026,strong,Table1/6 ESA total fiscal receipts fed-collected 155889m 2024; tick551",
    "bud_fed_fiscal_esa_total_2025,fod_finance,2025,158099700000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table1/6 ESA total fiscal 158099.7m 2025 monitoring; tick551",
    "bud_fed_fiscal_esa_total_2026,fod_finance,2026,163805500000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table6 ESA total fiscal 163805.5m 2026 (+5.706bn / +3.6pct); tick551",
    "bud_fed_direct_tax_esa_2025,fod_finance,2025,96728300000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table1 direct taxes ESA 96728.3m 2025; tick551",
    "bud_fed_direct_tax_esa_2024,fod_finance,2024,94864500000,,,outturn,src_kamer_expose_fiscal_receipts_2026,strong,Table1 direct taxes ESA 94864.5m 2024; tick551",
    # L5 major lines 2025-26 ESA
    "bud_bvh_esa_2024,fod_finance,2024,63276800000,,,outturn,src_kamer_expose_fiscal_receipts_2026,strong,Table1/6 bedrijfsvoorheffing ESA 63276.8m 2024; tick551",
    "bud_bvh_esa_2025,fod_finance,2025,65987700000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,BVH ESA 65987.7m 2025; tick551",
    "bud_bvh_esa_2026,fod_finance,2026,66841400000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,BVH ESA 66841.4m 2026 (+853.7m); tick551",
    "bud_vat_esa_total_2024,fod_finance,2024,41713000000,,,outturn,src_kamer_expose_fiscal_receipts_2026,strong,VAT ESA total 41713.0m 2024; tick551",
    "bud_vat_esa_total_2025,fod_finance,2025,41934500000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,VAT ESA total 41934.5m 2025; tick551",
    "bud_vat_esa_total_2026,fod_finance,2026,45148500000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,VAT ESA total 45148.5m 2026 (+3214m / +7.7pct); tick551",
    "bud_vat_pure_esa_2025,fod_finance,2025,37825200000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Pure VAT ESA 37825.2m 2025; tick551",
    "bud_vat_pure_esa_2026,fod_finance,2026,40274300000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table5 pure VAT ESA 40274.3m 2026; tick551",
    "bud_venb_esa_2025,fod_finance,2025,26142700000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table5 VenB ESA 26142.7m 2025; tick551",
    "bud_venb_esa_2026,fod_finance,2026,26748200000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table5 VenB ESA 26748.2m 2026; tick551",
    "bud_venb_va_esa_2026,fod_finance,2026,21966100000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,VenB advances ESA 21966.1m 2026; tick551",
    "bud_rv_total_esa_2025,fod_finance,2025,7612400000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Roerende voorheffing total ESA 7612.4m 2025; tick551",
    "bud_rv_total_esa_2026,fod_finance,2026,7990000000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,RV total ESA 7990.0m 2026; tick551",
    "bud_rv_natural_esa_2026,fod_finance,2026,7291700000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table5 RV natural persons ESA 7291.7m 2026; tick551",
    "bud_excise_esa_2025,fod_finance,2025,11216100000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Excise+divers ESA 11216.1m 2025; tick551",
    "bud_excise_esa_2026,fod_finance,2026,11211400000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Excise ESA 11211.4m 2026; tick551",
    "bud_customs_esa_2025,fod_finance,2025,3304900000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Customs ESA 3304.9m 2025 dual EU; tick551",
    "bud_customs_esa_2026,fod_finance,2026,3401900000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Customs ESA 3401.9m 2026 dual EU financing; tick551",
    "bud_registration_esa_2025,fod_finance,2025,2157100000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Registration rights ESA 2157.1m 2025; tick551",
    "bud_registration_esa_2026,fod_finance,2026,2259500000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Registration ESA 2259.5m 2026; tick551",
    "bud_inheritance_esa_2025,fod_finance,2025,1283600000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Inheritance ESA 1283.6m 2025; tick551",
    "bud_inheritance_esa_2026,fod_finance,2026,1253300000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Inheritance ESA 1253.3m 2026; tick551",
    "bud_va_total_esa_2025,fod_finance,2025,23184800000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Voorafbetalingen total ESA 23184.8m 2025; tick551",
    "bud_va_total_esa_2026,fod_finance,2026,23700500000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Voorafbetalingen total ESA 23700.5m 2026; tick551",
    "bud_pb_global_product_2026,fod_finance,2026,62370000000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table5 global PB product current law 62370.0m 2026; tick551",
    # Cash dual Table8/9
    "bud_fed_fiscal_cash_third_2025,fod_finance,2025,91100400000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table8 cash third-party+assigned fiscal 91100.4m 2025; tick551",
    "bud_fed_fiscal_cash_third_2026,fod_finance,2026,92508300000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table8 cash third-party+assigned 92508.3m 2026; tick551",
    "bud_fed_fiscal_middelen_cash_2025,fod_finance,2025,62247200000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table9 Middelen fiscal cash 62247.2m 2025; tick551",
    "bud_fed_fiscal_middelen_cash_2026,fod_finance,2026,65434500000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table9 Middelen fiscal cash 65434.5m 2026 (+3.187bn); tick551",
    "bud_bvh_cash_third_2026,fod_finance,2026,34004700000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table10 BVH cash third-party path 34004.7m 2026; tick551",
    "bud_bvh_middelen_cash_2026,fod_finance,2026,28080600000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table9 BVH Middelen cash 28080.6m 2026; tick551",
    # Technical factors L5
    "bud_tech_russian_cit_interest_2025,fod_finance,2025,-1260000000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3 tech: VenB profits frozen Russian assets interest -1260m 2025; tick551",
    "bud_tech_russian_cit_interest_2026,fod_finance,2026,1163000000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3 tech: VenB Russian frozen interest +1163m 2026; tick551",
    "bud_tech_vat_chain_2025,fod_finance,2025,1170000000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3/5 VAT chain technical +1170m 2025; tick551",
    "bud_tech_bvh_reform_2026,fod_finance,2026,220800000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3 BVH reform tech +220.8m 2026; tick551",
    "bud_tech_hedera_tbv_2026,fod_finance,2026,45700000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3 HEDERA compensation TBV +45.7m 2026; tick551",
    "bud_tech_hedera_tcter_2026,fod_finance,2026,23100000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3 HEDERA TCTER +23.1m 2026; tick551",
    "bud_tech_hedera_rv_2026,fod_finance,2026,-39200000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3 HEDERA RV compensation -39.2m 2026; tick551",
    "bud_tech_bvh_inkohiering_2026,fod_finance,2026,-184000000,,,budgeted,src_kamer_expose_fiscal_receipts_2026,strong,Table3 BVH inkohiering rhythm -184m 2026; tick551",
    # Dual
    "bud_dual_fiscal_esa_vs_graph1_2026,fod_finance,2026,163805500000,,,derived,src_dual_fiscal_esa_graph1_tick551,strong,Dual Table6 ESA 163.8bn ~ Graph1 fiscal 164.3bn 2026; tick551",
    "bud_dual_middelen_vs_esa_wedge_2026,fod_finance,2026,98371000000,,,derived,src_dual_fiscal_esa_graph1_tick551,strong,Dual ESA 163.8 - Middelen cash 65.4 = assignment/third-party wedge ~98.4bn class; tick551",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_fed_fiscal_esa_l5_2024_26,Federal fiscal receipts ESA L5 package 2024-2026,fod_finance,Taxpayers firms workers,"
        "Expose Part II Tables1/5/6,2026-01-28,2024,2026,163805500000,"
        '"{""total_2024_m"":155889,""total_2025_m"":158100,""total_2026_m"":163806,""bvh_2026_m"":66841,""vat_2026_m"":45149,'
        '""vat_pure_2026_m"":40274,""venb_2026_m"":26748,""rv_2026_m"":7990,""excise_2026_m"":11211,""customs_2026_m"":3402,'
        '""va_2026_m"":23701,""note"":""Strong before BVH remittance exemptions grossing; dual Graph1 164.3""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map federal tax revenue architecture,"
        "Assignment FOI,src_kamer_expose_fiscal_receipts_2026,strong,Federal>Tax>ESA_L5_2024_26,tick551"
    ),
    (
        "cmt_fed_fiscal_cash_dual_2026,Federal fiscal cash Middelen vs third-party assignment dual 2026,fod_finance,Entity II SS EU,"
        "Expose Tables8-10 cash dual,2026-01-28,2025,2026,92508300000,"
        '"{""third_2025_m"":91100,""third_2026_m"":92508,""middelen_2025_m"":62247,""middelen_2026_m"":65435,'
        '""bvh_third_2026_m"":34005,""bvh_middelen_2026_m"":28081,'
        '""note"":""Strong dual cash split; assignment is core federal-E2 stack""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Cash assignment dual map,"
        "Beneficiary L5 FOI,src_kamer_expose_fiscal_receipts_2026,strong,Federal>Tax>cash_dual_2026,tick551"
    ),
    (
        "cmt_fiscal_tech_factors_2025_26,Fiscal technical correction factors Table3 2025-26,fod_finance,ESA compilers Hedera,"
        "Expose Table3 technical factors,2026-01-28,2025,2026,0,"
        '"{""russian_cit_2025_m"":-1260,""russian_cit_2026_m"":1163,""vat_chain_2025_m"":1170,""bvh_reform_2026_m"":220.8,'
        '""hedera_tbv_m"":45.7,""hedera_tcter_m"":23.1,""hedera_rv_m"":-39.2,""bvh_inkohiering_m"":-184,'
        '""note"":""Strong one-off/tech dual; Russian frozen assets CIT interest swing material""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Tech one-off honesty,"
        "Detail FOI,src_kamer_expose_fiscal_receipts_2026,strong,Federal>Tax>tech_factors_2025_26,tick551"
    ),
    (
        "cmt_dual_fiscal_esa_graph1_2026,Dual fiscal ESA Table6 vs Graph1 2026,gg_belgium,Multi-level,"
        "Part II + Graph1 dual,2026-01-28,2026,2026,163805500000,"
        '"{""esa_bn"":163.8,""graph1_bn"":164.3,""middelen_cash_bn"":65.4,""third_cash_bn"":92.5,'
        '""note"":""not invent; close dual on totals; assignment wedge large""}",'
        "0,active,docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,Unified tax revenue dual,"
        "Reconcile FOI,src_dual_fiscal_esa_graph1_tick551,strong,BE>dual>fiscal_ESA_Graph1,tick551"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_fed_fiscal_esa_164bn,Federal fiscal ESA total 163.8bn 2026,federal,ops,Federal>Tax>ESA_total_2026,163805500000,163805500000,Strong Table6 +3.6pct; dual Graph1 164.3; core revenue,strong,src_kamer_expose_fiscal_receipts_2026,Taxpayers,Federal tax mass,Not waste — architecture map,3.0,9.5,4,6.25,Assignment FOI,seed,,tick551",
    "lb_bvh_esa_66_8bn,Payroll withholding BVH ESA 66.8bn 2026,federal,ops,Federal>Tax>BVH_2026,66841400000,66841400000,Strong largest direct line; remittance exemptions off this gross,strong,src_kamer_expose_fiscal_receipts_2026,Workers employers,Wage tax,Dual EIWT FOI,4.0,9.5,5,6.85,Remittance FOI,seed,,tick551",
    "lb_vat_esa_45_1bn,VAT ESA total 45.1bn 2026,federal,ops,Federal>Tax>VAT_2026,45148500000,45148500000,Strong +7.7pct YoY; pure 40.3 + divers; dual EU VAT resource,strong,src_kamer_expose_fiscal_receipts_2026,Consumers,VAT mass,DRM path class,4.0,9.5,5,6.85,Rate FOI,seed,,tick551",
    "lb_venb_esa_26_7bn,Corporate tax ESA 26.7bn 2026,federal,ops,Federal>Tax>VenB_2026,26748200000,26748200000,Strong; Russian frozen interest tech swing -1.26/+1.16,strong,src_kamer_expose_fiscal_receipts_2026,Firms,CIT,One-off tech dual,5.0,9.5,5,7.15,Tech FOI,seed,,tick551",
    "lb_middelen_cash_65_4bn,Middelen fiscal cash 65.4bn 2026,federal,ops,Federal>Tax>Middelen_cash_2026,65434500000,65434500000,Strong Table9 federal own cash after assignment; dual E2,strong,src_kamer_expose_fiscal_receipts_2026,Federal budget,Voies et Moyens,Assignment stack,4.5,9.5,4,6.75,Dual FOI,seed,,tick551",
    "lb_fiscal_cash_third_92_5bn,Third-party+assigned fiscal cash 92.5bn 2026,federal,ops,Federal>Tax>third_cash_2026,92508300000,92508300000,Strong Table8; dual SS/C&R assignment,strong,src_kamer_expose_fiscal_receipts_2026,Entity II SS,Assigned taxes,Core dual,4.5,9.5,4,6.75,Beneficiary FOI,seed,,tick551",
    "lb_russian_cit_interest_swing,Russian frozen CIT interest tech swing 1.26bn,federal,ops,Federal>Tax>russian_cit_tech,1260000000,1260000000,Strong Table3 -1260 2025 / +1163 2026; one-off class,strong,src_kamer_expose_fiscal_receipts_2026,ESA,Technical factor,Not structural,6.5,8.0,3,6.85,Disclose FOI,seed,,tick551",
    "lb_dual_fiscal_esa_graph1,Dual fiscal ESA 163.8 vs Graph1 164.3 2026,multi,ops,BE>dual>fiscal_ESA_Graph1,163805500000,164300000000,Strong dual close totals; assignment wedge ~98bn cash class,strong,src_dual_fiscal_esa_graph1_tick551,Multi-level,Tax architecture,Honesty map,4.0,9.5,4,6.55,Unified FOI,seed,,tick551",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

foi = (
    f"gap_fiscal_assignment_l5_2026,Federal>Tax>assignment_L5_cash_2026,fod_finance,"
    "Cash-by-year L5 of assigned/third-party fiscal receipts by beneficiary (SS / VL / WAL / BRU / EU) 2024-2026; "
    "Table11 beneficiary matrix if not public; BVH remittance exemptions grossing recon to EIWT; Russian frozen CIT interest legal basis and multi-year path,"
    "ESA and cash aggregates strong; end-beneficiary and remittance L5 still thin,"
    "6,FOD Financiën / FOD BOSA / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_fiscal_assignment_l5_2026.md,ready,2026-07-31,,,,"
    "cmt_fed_fiscal_esa_l5_2024_26|cmt_fed_fiscal_cash_dual_2026,"
    "lb_fed_fiscal_esa_164bn|lb_fiscal_cash_third_92_5bn,"
    f"{now},{now},tick551: Part II tables filled; residual assignment L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq = root / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = "rq_542,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T08:55:00Z,,Spawned tick550 progress; next public residual after exposé deep wave; rq_116 deferred"
new = "rq_542,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T08:55:00Z,2026-07-31T09:00:00Z,tick551: Part II fiscal ESA/cash L5 163.8bn; spawn rq_543; rq_116 deferred"
if old not in text:
    raise SystemExit("rq_542 not found")
text = text.replace(old, new)
if "rq_543," not in text:
    text = text.rstrip("\n") + "\n"
    text += "rq_543,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:00:00Z,,Spawned tick551 after fiscal receipts; next residual (Table4 tax measures L5 / non-fiscal / new PDF); rq_116 deferred\n"
rq.write_text(text, encoding="utf-8")
print("tick551 OK", len(buds))

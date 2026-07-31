# tick555 — CoA Flanders rekeningenrapport 2025 (ccrek 2026_32)
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T09:20:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_vl_rekeningen_2025,CoA Flanders rekeningenrapport 2025 general+consolidated accounts,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "Rekenhof NL chamber 30 Jun 2026,2026-07-31,court_of_audit,"
        "Strong tick555: VL consolidated financing -3982.4m 2025 (budget -4503.8); Maastricht debt 50171.9m eoy25 "
        "(+8383 from 41788.6); PMV Zaventem 2553.6m; ministry ESR 80315.5 in/out contribution 20868; "
        "credit carry 1415.3 to 2026; relance 399.4m/4.2bn commit; land missing 1.6bn art 1.4bn Zandvliet 366.6; "
        "raw ccrek_2026_32_rekeningenrapport2025.pdf\n"
    )
    f.write(
        "src_ccrek_vl_rekeningen_press_2025,CoA press Flanders accounts 2025,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025_Persbericht.pdf,"
        "Rekenhof,2026-07-31,court_of_audit_press,"
        "Strong headlines: disclaimer economic accounts; clean ESR consol; debt 50.2bn; Zaventem capital; tick555\n"
    )
    f.write(
        "src_dual_vl_debt_zaventem_tick555,Dual VL Maastricht debt path + PMV Zaventem equity,"
        "docs/doge/data/raw/ccrek_2026_32_rekeningenrapport2025.pdf,DOGE synthesis CoA accounts + prior BA debt,2026-07-31,synthesis,"
        "Strong dual: debt +8.38bn YoY of which Zaventem 2.55bn equity injection; dual prior non-Maastricht claims; tick555\n"
    )

buds = [
    # Financing saldo path
    "bud_vl_financing_saldo_2024,vlaanderen_gov,2024,-4101300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VL consolidated financing saldo -4101.3m 2024 CoA; tick555",
    "bud_vl_financing_saldo_budget_2025,vlaanderen_gov,2025,-4503800000,,,budgeted,src_ccrek_vl_rekeningen_2025,strong,VL financing saldo budget -4503.8m 2025; tick555",
    "bud_vl_financing_saldo_2025,vlaanderen_gov,2025,-3982400000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VL consolidated financing saldo -3982.4m 2025 CoA clean ESR; tick555",
    # Maastricht debt
    "bud_vl_maastricht_debt_2024,vlaanderen_gov,2024,41788600000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VL Maastricht debt contribution 41788.6m eoy2024; tick555",
    "bud_vl_maastricht_debt_budget_2025,vlaanderen_gov,2025,48283200000,,,budgeted,src_ccrek_vl_rekeningen_2025,strong,VL Maastricht debt budget path 48283.2m 2025 BA; tick555",
    "bud_vl_maastricht_debt_2025,vlaanderen_gov,2025,50171900000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VL Maastricht debt 50171.9m eoy2025 (+8383.3 YoY); tick555",
    "bud_vl_maastricht_debt_delta_2025,vlaanderen_gov,2025,8383300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VL debt rise 8383.3m 2025 of which excess vs BA 1888.7; tick555",
    "bud_vl_pmv_zaventem_capital_2025,vlaanderen_gov,2025,2553600000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,PMV capital raise for Brussels Airport/Zaventem 2553.6m 2025 post-BA amendement; tick555",
    # Ministry ESR reporting
    "bud_vl_ministry_esa_rec_2025,vlaanderen_gov,2025,80315500000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Ministry ESA reporting receipts 80315.5m 2025 clean opinion; tick555",
    "bud_vl_ministry_esa_exp_2025,vlaanderen_gov,2025,80315500000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Ministry ESA reporting expenditures 80315.5m 2025; tick555",
    "bud_vl_ministry_saldo_contrib_2025,vlaanderen_gov,2025,20868000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Ministry contribution to financing saldo 20868.0m 2025; tick555",
    # Credit carryovers
    "bud_vl_credit_carry_into_2025,vlaanderen_gov,2025,1255300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Policy credit carry-in to 2025 1255.3m; tick555",
    "bud_vl_credit_carry_to_2026,vlaanderen_gov,2026,1415300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Policy credit carry to 2026 1415.3m (index provision underuse); tick555",
    # Relance
    "bud_vl_relance_spend_2025,vlaanderen_gov,2025,399400000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Vlaamse Veerkracht relance spend 399.4m 2025 (-342.2 vs budget); tick555",
    "bud_vl_relance_underuse_2025,vlaanderen_gov,2025,342200000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Relance under-execution 342.2m 2025; tick555",
    "bud_vl_relance_committed_cum_2025,vlaanderen_gov,2025,4200000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Relance total committed 4.2bn eoy2025; tick555",
    "bud_vl_relance_paid_cum_2025,vlaanderen_gov,2025,3500000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Relance liquidated 3.5bn eoy2025; tick555",
    "bud_vl_relance_open_2025,vlaanderen_gov,2025,700000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Relance open commitments 0.7bn eoy2025; tick555",
    # Balance sheet gaps
    "bud_vl_missing_land_buildings_est,vlaanderen_gov,2025,1600000000,,,estimate,src_ccrek_vl_rekeningen_2025,medium,CoA estimate missing land/buildings still zero-valued ~1.6bn; tick555",
    "bud_vl_art_collection_balance,vlaanderen_gov,2025,1400000000,,,outturn,src_ccrek_vl_rekeningen_2025,medium,Art collection on balance 1.4bn since 2022; valuation incomplete CoA; tick555",
    "bud_vl_zandvlietsluis_nbv_2025,vlaanderen_gov,2025,366600000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Zandvlietsluis NBV 366.6m wrongly on VL books; write-off due 2026 (Port Antwerp-Bruges owner); tick555",
    "bud_vl_fwo_commitment_adj,vlaanderen_gov,2025,561600000,,,estimate,src_ccrek_vl_rekeningen_2025,strong,Open commitments opening balance still needs +561.6m FWO adjustment; tick555",
    "bud_vl_fio_commitment_adj,vlaanderen_gov,2025,188600000,,,estimate,src_ccrek_vl_rekeningen_2025,strong,Open commitments FIO adjustment +188.6m still needed; tick555",
    # Dual
    "bud_dual_vl_debt_zaventem_2025,vlaanderen_gov,2025,2553600000,,,derived,src_dual_vl_debt_zaventem_tick555,strong,Dual debt rise driven by Zaventem equity 2.55bn of +8.38bn; tick555",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_vl_accounts_2025_coa,Flanders consolidated accounts 2025 CoA certification stack,vlaanderen_gov,VL taxpayers parliament,"
        "CoA rekeningenrapport 2025,2026-06-30,2025,2025,-3982400000,"
        '"{""financing_2025_m"":-3982.4,""financing_budget_m"":-4503.8,""financing_2024_m"":-4101.3,'
        '""debt_2025_m"":50171.9,""debt_2024_m"":41788.6,""debt_delta_m"":8383.3,""zaventem_m"":2553.6,'
        '""ministry_esa_m"":80315.5,""ministry_contrib_m"":20868,""opinion_economic"":""disclaimer"",'
        '""opinion_budget"":""qualified"",""opinion_esa"":""clean"",""opinion_consol"":""clean"",'
        '""note"":""Strong primary; balance-sheet opacity residual""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_32_rekeningenrapport2025.pdf,Certify VL public accounts,"
        "Fix balance sheet FOI,src_ccrek_vl_rekeningen_2025,strong,Vlaanderen>Accounts>2025,tick555"
    ),
    (
        "cmt_vl_debt_zaventem_path_2025,VL Maastricht debt + PMV Zaventem capital 2025,vlaanderen_gov,PMV BAC airport,"
        "CoA accounts + post-BA amendement,2025-01-01,2025,2025,2553600000,"
        '"{""debt_eoy_m"":50171.9,""delta_m"":8383.3,""vs_ba_excess_m"":1888.7,""zaventem_m"":2553.6,'
        '""also"":[""social_housing"",""Lantis""],""note"":""Strong; equity injection drives debt stock""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_32_rekeningenrapport2025.pdf,Honest VL debt drivers,"
        "Airport FOI,src_dual_vl_debt_zaventem_tick555,strong,Vlaanderen>Schuld>Zaventem_2025,tick555"
    ),
    (
        "cmt_vl_relance_execution_2025,Vlaamse Veerkracht relance execution eoy2025,vlaanderen_gov,RRF project promoters,"
        "CoA accounts summary relance,2021-01-01,2021,2025,4200000000,"
        '"{""spend_2025_m"":399.4,""underuse_2025_m"":342.2,""committed_bn"":4.2,""paid_bn"":3.5,""open_bn"":0.7,'
        '""note"":""Strong; delivery lag on large projects""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_32_rekeningenrapport2025.pdf,Relance delivery map,"
        "Project L5 FOI,src_ccrek_vl_rekeningen_2025,strong,Vlaanderen>Relance>execution_2025,tick555"
    ),
    (
        "cmt_vl_balance_sheet_gaps_2025,VL balance-sheet gaps land art locks CoA 2025,vlaanderen_gov,Heritage infrastructure,"
        "CoA economic accounts disclaimer,2019-01-01,2019,2026,0,"
        '"{""missing_land_bn"":1.6,""art_bn"":1.4,""zandvliet_m"":366.6,""fwo_adj_m"":561.6,""fio_adj_m"":188.6,'
        '""note"":""Strong CoA; progress slow capacity/budget""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_32_rekeningenrapport2025.pdf,Clean balance sheet,"
        "Inventory FOI,src_ccrek_vl_rekeningen_2025,strong,Vlaanderen>Accounts>balance_gaps,tick555"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_vl_financing_minus_4bn_2025,VL consolidated financing -3.98bn 2025,regional,ops,Vlaanderen>Accounts>financing_2025,3982400000,3982400000,Strong CoA clean ESR consol; better than budget -4.50; dual Entity I path,strong,src_ccrek_vl_rekeningen_2025,Taxpayers,Fiscal outturn,Structural deficit,5.0,9.0,5,6.75,Path FOI,seed,,tick555",
    "lb_vl_debt_50_2bn_2025,VL Maastricht debt 50.2bn eoy2025,regional,ops,Vlaanderen>Schuld>Maastricht_2025,50171900000,50171900000,Strong +8.38bn YoY; dual prior BA path,strong,src_ccrek_vl_rekeningen_2025,Bondholders,Subnational debt,Zaventem+housing+Lantis,5.5,9.5,5,7.25,Driver FOI,seed,,tick555",
    "lb_vl_zaventem_pmv_2_55bn,PMV Zaventem capital injection 2.55bn 2025,regional,ops,Vlaanderen>PMV>Zaventem,2553600000,2553600000,Strong post-BA amendement drives debt excess; equity not pure TE,strong,src_ccrek_vl_rekeningen_2025,Airport,SOE equity,Debt dual,6.0,8.5,5,7.05,Return FOI,seed,,tick555",
    "lb_vl_relance_open_0_7bn,Vlaamse Veerkracht open 0.7bn eoy2025,regional,ops,Vlaanderen>Relance>open,700000000,700000000,Strong 4.2 commit / 3.5 paid; 2025 spend only 399m,strong,src_ccrek_vl_rekeningen_2025,Projects,RRF delivery,Underuse,5.5,8.0,4,6.45,Project FOI,seed,,tick555",
    "lb_vl_credit_carry_1_42bn,VL policy credit carry to 2026 1.42bn,regional,ops,Vlaanderen>Budget>credit_carry,1415300000,1415300000,Strong annuality breach class; index provision,strong,src_ccrek_vl_rekeningen_2025,Departments,Carryover,Governance,5.5,8.0,3,6.35,Limit FOI,seed,,tick555",
    "lb_vl_missing_land_1_6bn,VL missing land/buildings est 1.6bn,regional,ops,Vlaanderen>Accounts>land_gap,1600000000,1600000000,Medium CoA estimate zero-valued assets; disclaimer driver,medium,src_ccrek_vl_rekeningen_2025,Balance sheet,Inventory gap,Opacity,7.0,8.0,5,7.15,Inventory FOI,seed,,tick555",
    "lb_vl_zandvliet_367m,Zandvlietsluis wrong books 367m,regional,ops,Vlaanderen>Accounts>Zandvliet,366600000,366600000,Strong NBV; Port Antwerp-Bruges owner; write-off 2026,strong,src_ccrek_vl_rekeningen_2025,Ports,Ownership error,Classic DOGE,7.5,7.5,3,7.05,Correct FOI,seed,,tick555",
    "lb_dual_vl_debt_zaventem,Dual VL debt rise Zaventem equity stack,multi,ops,BE>dual>VL_debt_airport,2553600000,8383300000,Strong dual equity+debt; not pure waste TE,strong,src_dual_vl_debt_zaventem_tick555,Multi,Airport financing,Honesty,5.5,8.5,5,6.90,Map FOI,seed,,tick555",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

foi = (
    f"gap_vl_accounts_balance_l5,Vlaanderen>Accounts>balance_sheet_L5_2025,vlaanderen_gov,"
    "Full inventory of zero-valued land/buildings with CoA 1.6bn method; art collection detail and disputed works; "
    "Zandvliet write-off journal 2026; FWO/FIO commitment opening corrections cash; PMV Zaventem capital agreement terms; "
    "relance project list with >10m underuse causes,"
    "CoA 2026_32 aggregates strong; balance-sheet and project L5 residual,"
    "7,Vlaamse overheid Team Openbaarheid / Departement FB / PMV,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
    "docs/doge/foi/drafts/gap_vl_accounts_balance_l5.md,ready,2026-07-31,,,,"
    "cmt_vl_accounts_2025_coa|cmt_vl_balance_sheet_gaps_2025|cmt_vl_debt_zaventem_path_2025,"
    "lb_vl_debt_50_2bn_2025|lb_vl_zaventem_pmv_2_55bn|lb_vl_missing_land_1_6bn,"
    f"{now},{now},tick555 CoA accounts filled; residual inventory human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq = root / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = "rq_546,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:15:00Z,,Spawned tick554 after fiscal assign T11; next residual; rq_116 deferred"
new = "rq_546,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:15:00Z,2026-07-31T09:20:00Z,tick555: CoA VL rekeningen 2025 debt/relance/balance; spawn rq_547; rq_116 deferred"
if old not in text:
    raise SystemExit("rq_546 not found")
text = text.replace(old, new)
if "rq_547," not in text:
    text = text.rstrip("\n") + "\n"
    text += "rq_547,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:20:00Z,,Spawned tick555 after VL accounts CoA; next residual; rq_116 deferred; progress@560 in 5 ticks\n"
rq.write_text(text, encoding="utf-8")
print("tick555 OK", len(buds))

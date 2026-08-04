# tick832 — Genk JR2025 fill
from pathlib import Path

root = Path("docs/doge/data")

budgets = """
bud_genk_assets_2025,city_genk,2025,628701151,,,stock,src_genk_jr2025,strong,Consol stad+OCMW total assets YE2025 628.701m; tick832
bud_genk_equity_2025,city_genk,2025,120076206,,,stock,src_genk_jr2025,strong,Nettoactief YE2025 120.076m; tick832
bud_genk_debt_total_2025,city_genk,2025,508624946,,,stock,src_genk_jr2025,strong,Total schulden YE2025 508.625m; tick832
bud_genk_fin_debt_2025,city_genk,2025,174612670,,,stock,src_genk_jr2025,strong,Financiele schulden total YE2025 174.613m (LT 143.177 + ST due 10.436 + ST treasury 21.000); tick832
bud_genk_fin_debt_lt_2025,city_genk,2025,143176727,,,stock,src_genk_jr2025,strong,Financiele schulden LT YE2025 143.177m; tick832
bud_genk_fin_debt_st_treasury_2025,city_genk,2025,21000000,,,stock,src_genk_jr2025,strong,Thesauriebewijzen ST YE2025 21.0m (was 15.0m); tick832
bud_genk_pension_prov_2025,city_genk,2025,312599985,,,stock,src_genk_jr2025,strong,Pensioenvoorzieningen YE2025 312.600m (was 309.736m); largest VL city pension stock found to date; tick832
bud_genk_cash_2025,city_genk,2025,15377286,,,stock,src_genk_jr2025,strong,Liquide middelen YE2025 15.377m; tick832
bud_genk_cap_subs_2025,city_genk,2025,34783689,,,stock,src_genk_jr2025,strong,Kapitaalsubsidies YE2025 34.784m; tick832
bud_genk_fva_igs_2025,city_genk,2025,84367663,,,stock,src_genk_jr2025,strong,Fin VA IGS 84.368m; tick832
bud_genk_fva_eva_2025,city_genk,2025,36082034,,,stock,src_genk_jr2025,strong,Fin VA EVA/AGB 36.082m; tick832
bud_genk_expl_rec_2025,city_genk,2025,171852184,,,cash,src_genk_jr2025,strong,Exploitatieontvangsten 171.852m; tick832
bud_genk_expl_exp_2025,city_genk,2025,162256912,,,cash,src_genk_jr2025,strong,Exploitatieuitgaven 162.257m (-1.42pct YoY); tick832
bud_genk_expl_saldo_2025,city_genk,2025,9595272,,,cash,src_genk_jr2025,strong,Exploitatiesaldo +9.595m; tick832
bud_genk_invest_exp_2025,city_genk,2025,32345674,,,cash,src_genk_jr2025,strong,Investeringsuitgaven 32.346m; tick832
bud_genk_invest_rec_2025,city_genk,2025,4863946,,,cash,src_genk_jr2025,strong,Investeringsontvangsten 4.864m; tick832
bud_genk_invest_saldo_2025,city_genk,2025,-27481728,,,cash,src_genk_jr2025,strong,Investeringssaldo -27.482m; tick832
bud_genk_fin_rec_2025,city_genk,2025,23236486,,,cash,src_genk_jr2025,strong,Financieringsontvangsten 23.236m; tick832
bud_genk_fin_exp_2025,city_genk,2025,11247026,,,cash,src_genk_jr2025,strong,Financieringsuitgaven 11.247m; tick832
bud_genk_new_loans_2025,city_genk,2025,22795186,,,cash,src_genk_jr2025,strong,Nieuwe leningen/leasings 22.795m (20m banks Belfius+BNPPF +2.795m leasing); tick832
bud_genk_aflossingen_2025,city_genk,2025,9548806,,,cash,src_genk_jr2025,strong,Periodieke aflossingen 9.549m; tick832
bud_genk_afm_2025,city_genk,2025,487767,,,cash,src_genk_jr2025,strong,Autofinancieringsmarge AFM +0.488m (gecorr -2.393m); tick832
bud_genk_afm_corr_2025,city_genk,2025,-2392731,,,cash,src_genk_jr2025,strong,Gecorrigeerde AFM -2.393m (8pct debt norm); tick832
bud_genk_bbr_2025,city_genk,2025,-4374028,,,cash,src_genk_jr2025,strong,Beschikbaar budgettair resultaat BBR -4.374m (treasury booking effect); tick832
bud_genk_budget_result_2025,city_genk,2025,-5896996,,,cash,src_genk_jr2025,strong,Budgettair resultaat boekjaar -5.897m; tick832
bud_genk_pnl_result_2025,city_genk,2025,-12384715,,,cash,src_genk_jr2025,strong,Vennootschapsresultaat J5 -12.385m; tick832
bud_genk_bezold_2025,city_genk,2025,79567002,,,cash,src_genk_jr2025,strong,J5 bezoldigingen/sociale/pensioenen 79.567m (-3.1pct YoY; RSZ regularisation effect); tick832
bud_genk_goederen_2025,city_genk,2025,31393810,,,cash,src_genk_jr2025,strong,J5 goederen en diensten 31.394m; tick832
bud_genk_toelagen_2025,city_genk,2025,35315814,,,cash,src_genk_jr2025,strong,J5 toegestane werkingssubsidies 35.316m (police 13.715 fire 3.432 IGS 3.529 AGB 2.515 other 9.531); tick832
bud_genk_inv_subs_granted_2025,city_genk,2025,6791321,,,cash,src_genk_jr2025,strong,J5/T2 toegestane investeringssubsidies 6.791m (AGB 4.626m); tick832
bud_genk_ocmw_aid_2025,city_genk,2025,10941986,,,cash,src_genk_jr2025,strong,J5 individuele hulpverlening OCMW 10.942m; tick832
bud_genk_fiscal_2025,city_genk,2025,63136030,,,cash,src_genk_jr2025,strong,J5 fiscale opbrengsten en boetes 63.136m; tick832
bud_genk_werk_subs_rec_2025,city_genk,2025,88387129,,,cash,src_genk_jr2025,strong,J5 werkingssubsidies ontvangen 88.387m (gemeentefonds 49.249m); tick832
bud_genk_fin_costs_2025,city_genk,2025,4450346,,,cash,src_genk_jr2025,strong,J5 financiele kosten 4.450m; tick832
bud_genk_police_toelage_2025,city_genk,2025,13714659,,,cash,src_genk_jr2025,strong,Toelage politiezone 13.715m; tick832
""".strip() + "\n"

lb = """
lb_genk_pension_prov_313m,Genk pension provisions stock 312.6m YE2025 (largest VL city stock found),L5,stock,Vlaanderen>Gemeenten>Genk>pensions,0,312599985,Strong primary; +2.9m YoY; dual Mechelen 134.8m Kortrijk 34.5m; stock not pure annual waste,strong,src_genk_jr2025,statutory pensioners,Cover pension liabilities,312.6m stock,6.5,8.0,6.0,6.83,Funding ratio + multipjaar path FOI,active,,tick832 stock filtered from pure annual top10
lb_genk_fin_debt_175m,Genk financial debt stock 174.6m YE2025 (+19.2m YoY),L5,stock,Vlaanderen>Gemeenten>Genk>debt,4450346,174612670,Strong; LT 143.2m + ST due 10.4m + treasury 21m; new loans 22.8m vs repay 9.5m; dual Kortrijk 258m Mechelen 284m,strong,src_genk_jr2025,lenders / infrastructure users,Finance investment programme 32m 2025,174.6m stock / +19.2m,5.5,7.0,5.5,6.0,Debt schedule FOI,active,,tick832 stock
lb_genk_bezold_80m_2025,Genk J5 bezoldigingen 79.6m 2025 (-3.1pct YoY),L5,ops,Vlaanderen>Gemeenten>Genk>personnel,79567002,79567002,Strong primary; down via lower RSZ regularisations vs 2024; dual Kortrijk loon 136m Mechelen 113m different perimeter,strong,src_genk_jr2025,city/OCMW staff,Deliver local services,79.6m / -3.1pct,5.0,6.5,5.0,5.5,ETP productivity FOI,active,,tick832
lb_genk_toelagen_35m_2025,Genk granted operating subsidies 35.3m 2025,L5,subsidy,Vlaanderen>Gemeenten>Genk>toelagen,35315814,35315814,Strong; police 13.7 fire 3.4 IGS 3.5 AGB 2.5 other 9.5; dual Kortrijk 39.6m Mechelen ~90m,strong,src_genk_jr2025,police zone / fire / IGS / AGB / associations,Fund safety zones and local partners,35.3m,5.5,6.5,5.5,5.83,Named beneficiary matrix FOI,active,,tick832
lb_genk_bbr_minus_4m,Genk beschikbaar budgettair resultaat -4.37m YE2025,L5,ops,Vlaanderen>Gemeenten>Genk>liquidity,0,4374028,Strong BBR negative after treasury booking effect; AFM still +0.49m; cash 15.4m,strong,src_genk_jr2025,liquidity buffer,Budgetary cash position,BBR -4.37m / cash 15.4m,5.5,5.0,4.0,4.83,Treasury programme FOI,active,,tick832
lb_genk_invest_32m_2025,Genk investment spend 32.3m 2025 (net -27.5m after 4.9m receipts),L5,capex,Vlaanderen>Gemeenten>Genk>invest,32345674,32345674,Strong; roads 7.4m AGB toelage 3.2m Stiemerbeek 2.4m datacenter 2.0m green centre 1.6m; dual Kortrijk 57m Mechelen 26m,strong,src_genk_jr2025,city infrastructure users,Maintain and expand city infrastructure,32.3m,4.5,6.0,5.0,5.17,Project-level ROI FOI,active,,tick832
lb_dual_genk_kortrijk_mechelen_tick832,Dual Genk 629m vs Kortrijk 720m vs Mechelen 611m city residual,L5,ops,Belgium>dual>vl_cities,0,628701151,Strong dual not TE-additive; Genk standout pension stock 313m,strong,src_dual_genk_kortrijk_mechelen_tick832,multi-channel,Dual residual map,primary,4.5,7.5,5.0,5.67,Cross FOI,active,,tick832
""".strip() + "\n"

cmt = """
cmt_genk_balance_629m_2025,Genk consol stad+OCMW balance sheet YE2025 assets 628.7m,city_genk,Stad en OCMW Genk,BBC jaarrekening 2025 schema J4,2026-05-19,2025,2025,628701151,"{""assets_m"": 628.701, ""equity_m"": 120.076, ""debt_total_m"": 508.625, ""fin_debt_m"": 174.613, ""pension_prov_m"": 312.600, ""cash_m"": 15.377, ""cap_subs_m"": 34.784}",0,active,https://www.genk.be/jaarrekening-2025,Municipal consolidated balance sheet,Publish debt schedule + pension funding FOI,src_genk_jr2025,strong,Vlaanderen>Gemeenten>Genk>balance,tick832 GR/OCMW 19.05.2026
cmt_genk_pension_prov_313m_2025,Genk pension provisions stock 312.6m YE2025,city_genk,Statutory pensioners / Ethias-class,BBC J4 provisies pensioenen,2025-12-31,2025,2025,312599985,"{""stock_m"": 312.600, ""prior_m"": 309.736, ""delta_m"": 2.864}",0,active,docs/doge/data/raw/genk_jr2025.pdf,Largest VL city pension provision stock found (dual Mechelen 135 Kortrijk 35),Funding ratio multipjaar FOI,src_genk_jr2025,strong,Vlaanderen>Gemeenten>Genk>pensions,tick832 DOGE flag
cmt_genk_afm_bbr_2025,Genk AFM +0.49m and BBR -4.37m 2025,city_genk,Fiscal sustainability indicators,BBC schema J2 2025,2025-12-31,2025,2025,487767,"{""afm_m"": 0.488, ""afm_corr_m"": -2.393, ""bbr_m"": -4.374, ""budget_result_m"": -5.897, ""expl_saldo_m"": 9.595}",0,active,docs/doge/data/raw/genk_jr2025.pdf,Thin positive AFM; BBR negative via treasury booking,Sustain AFM path FOI MJP,src_genk_jr2025,strong,Vlaanderen>Gemeenten>Genk>AFM,tick832
cmt_dual_genk_kortrijk_mechelen_tick832,Dual Genk JR2025 vs Kortrijk vs Mechelen city residual,gg_belgium,dual map,Genk JR2025 dual prior city fills,2026-08-05,2025,2025,628701151,"{""genk_assets_m"": 628.7, ""kortrijk_assets_m"": 720.4, ""mechelen_assets_m"": 610.8, ""genk_pension_m"": 312.6, ""mechelen_pension_m"": 134.8, ""kortrijk_pension_m"": 34.5}",0,active,docs/doge/data/raw/genk_jr2025.pdf,Dual residual map tick832,Cross FOI city L5,src_dual_genk_kortrijk_mechelen_tick832,strong,Belgium>dual>vl_cities,tick832 not TE-additive
""".strip() + "\n"

src = """
src_genk_jr2025,"Stad en OCMW Genk Jaarrekening 2025 (BBC, GR/OCMW 19.05.2026, 490p)",https://www.genk.be/file/download/66286/9B1A7E114A1AB2E52DA5397E1A686A6A,Stad Genk / OCMW Genk,2026-08-05,entity_accounts,Strong tick832 primary: consol stad+OCMW assets 628.7m equity 120.1m; expl ontvangsten 171.9m uitgaven 162.3m saldo +9.6m; AFM 0.49m BBR -4.37m; bezold 79.6m; fin debt 174.6m; pension prov 312.6m; toelagen 35.3m; invest 32.3m; new loans 22.8m; raw genk_jr2025.pdf
src_dual_genk_kortrijk_mechelen_tick832,Dual Genk JR2025 629m vs Kortrijk 720m vs Mechelen 611m residual tick832,docs/doge/data/raw/genk_jr2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: Genk assets 628.7m pension 312.6m expl 172m bezold 79.6m AFM +0.49m vs Kortrijk assets 720.4m pension 34.5m loon 135.6m AFM +7.2m vs Mechelen assets 610.8m pension 134.8m personnel 113m AFM +2.5m
""".strip() + "\n"

ent = "city_genk,Stad Genk,Ville de Genk,City of Genk,municipality,vlaanderen_gov,nl,https://www.genk.be,,Stadsplein 1 3600 Genk,JR2025 assets 628.7m pension prov 312.6m fin debt 174.6m; tick832\n"

foi = "gap_genk_debt_pension_subs_l5,Vlaanderen>Gemeenten>Genk_L5,city_genk,Full debt schedule by lender for fin debt 174.6m (incl treasury 21m programme); pension funding ratio and actuarial study behind 312.6m provision; named toelagen matrix within 35.3m beyond police/fire/IGS/AGB aggregates; AGB invest toelage project detail; MJP multi-year AFM path reconciliation,\"629m city+OCMW book with 313m pension provisions (largest VL city stock), 175m fin debt and 35m toelagen blocks dual VL city waste ranking vs Kortrijk/Mechelen\",7,Stad Genk / financieel directeur / openbaarheid van bestuur,,https://www.genk.be,docs/doge/foi/drafts/gap_genk_debt_pension_subs_l5.md,ready,2026-08-05,,,,,cmt_genk_balance_629m_2025|cmt_genk_pension_prov_313m_2025|cmt_genk_afm_bbr_2025,lb_genk_pension_prov_313m|lb_genk_fin_debt_175m|lb_genk_bezold_80m_2025|lb_genk_toelagen_35m_2025,2026-08-05T13:00:00Z,2026-08-05T13:00:00Z,tick832 primary JR2025; ready draft; do not send\n"

# research_queue: mark rq_822 done and spawn rq_823
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_822,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Kortrijk JR2025 filled tick831; residual Aalst/Genk/Roeselare/Hasselt city or BELNET AR2025 or skeyes residual",,2026-08-05T12:30:00Z,2026-08-05T12:30:00Z,spawned tick831 after Kortrijk dual Mechelen'
new = 'rq_822,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Kortrijk JR2025 filled tick831; residual Aalst/Genk/Roeselare/Hasselt city or BELNET AR2025 or skeyes residual",gap_genk_debt_pension_subs_l5,2026-08-05T12:30:00Z,2026-08-05T13:00:00Z,tick832 Genk JR2025 assets 628.7m expl 171.9m bezold 79.6m AFM 0.49m fin debt 174.6m pension 312.6m toelagen 35.3m dual Kortrijk/Mechelen; FOI ready'
if old not in text:
    raise SystemExit("rq_822 row not found for replace")
text = text.replace(old, new)
spawn = 'rq_823,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Genk JR2025 filled tick832; residual Aalst/Roeselare/Hasselt city or BELNET AR2025 or skeyes residual",,2026-08-05T13:00:00Z,2026-08-05T13:00:00Z,spawned tick832 after Genk dual Kortrijk/Mechelen\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

# loop_state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T13:00:00Z,rq_822,832,no,"
    "tick832 Genk JR2025 dual Kortrijk/Mechelen; next rq_823 residual dual L5; progress@840 in 8; rq_116 deferred\n",
    encoding="utf-8",
)

for name, payload in [
    ("budgets.csv", budgets),
    ("leaderboard.csv", lb),
    ("commitments.csv", cmt),
    ("sources.csv", src),
    ("entities.csv", ent),
    ("foi_queue.csv", foi),
]:
    p = root / name
    with p.open("a", encoding="utf-8", newline="") as f:
        f.write(payload)

print("tick832 CSV updates OK")

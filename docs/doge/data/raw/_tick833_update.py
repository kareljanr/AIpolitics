# tick833 — Aalst JR2025 fill
from pathlib import Path

root = Path("docs/doge/data")

budgets = """
bud_aalst_assets_2025,city_aalst,2025,616504271,,,stock,src_aalst_jr2025,strong,Consol stad+OCMW total assets YE2025 616.504m; tick833
bud_aalst_equity_2025,city_aalst,2025,406799666,,,stock,src_aalst_jr2025,strong,Nettoactief YE2025 406.800m; tick833
bud_aalst_debt_total_2025,city_aalst,2025,209704606,,,stock,src_aalst_jr2025,strong,Total schulden YE2025 209.705m; tick833
bud_aalst_fin_debt_2025,city_aalst,2025,164299390,,,stock,src_aalst_jr2025,strong,Financiele schulden total YE2025 164.299m (LT 148.521 + ST due 10.778 + ST treasury 5.000); -15.2m YoY; tick833
bud_aalst_fin_debt_lt_2025,city_aalst,2025,148521475,,,stock,src_aalst_jr2025,strong,Financiele schulden LT YE2025 148.521m; tick833
bud_aalst_fin_debt_st_treasury_2025,city_aalst,2025,5000000,,,stock,src_aalst_jr2025,strong,Thesaurie/lening ST YE2025 5.0m (was 10.0m); tick833
bud_aalst_pension_prov_2025,city_aalst,2025,8592483,,,stock,src_aalst_jr2025,strong,Pensioenvoorzieningen YE2025 8.592m (was 9.196m); dual Genk 312.6m; tick833
bud_aalst_cash_2025,city_aalst,2025,18493501,,,stock,src_aalst_jr2025,strong,Liquide middelen YE2025 18.494m (was 38.820m); tick833
bud_aalst_cap_subs_2025,city_aalst,2025,98035666,,,stock,src_aalst_jr2025,strong,Kapitaalsubsidies YE2025 98.036m; tick833
bud_aalst_fva_igs_2025,city_aalst,2025,70910863,,,stock,src_aalst_jr2025,strong,Fin VA IGS 70.911m; tick833
bud_aalst_expl_rec_2025,city_aalst,2025,276171685,,,cash,src_aalst_jr2025,strong,Exploitatieontvangsten 276.172m; tick833
bud_aalst_expl_exp_2025,city_aalst,2025,260234131,,,cash,src_aalst_jr2025,strong,Exploitatieuitgaven 260.234m (+7.1pct YoY cash path); tick833
bud_aalst_expl_saldo_2025,city_aalst,2025,15937554,,,cash,src_aalst_jr2025,strong,Exploitatiesaldo +15.938m; tick833
bud_aalst_invest_exp_2025,city_aalst,2025,34537629,,,cash,src_aalst_jr2025,strong,Investeringsuitgaven 34.538m; tick833
bud_aalst_invest_rec_2025,city_aalst,2025,12373751,,,cash,src_aalst_jr2025,strong,Investeringsontvangsten 12.374m; tick833
bud_aalst_invest_saldo_2025,city_aalst,2025,-22163877,,,cash,src_aalst_jr2025,strong,Investeringssaldo -22.164m; tick833
bud_aalst_fin_rec_2025,city_aalst,2025,2806994,,,cash,src_aalst_jr2025,strong,Financieringsontvangsten 2.807m (low new debt year); tick833
bud_aalst_fin_exp_2025,city_aalst,2025,10805528,,,cash,src_aalst_jr2025,strong,Financieringsuitgaven 10.806m; tick833
bud_aalst_new_loans_2025,city_aalst,2025,645636,,,cash,src_aalst_jr2025,strong,Nieuwe leningen/leasings 0.646m (low vs plan 35-40m); tick833
bud_aalst_aflossingen_2025,city_aalst,2025,10805513,,,cash,src_aalst_jr2025,strong,Periodieke aflossingen 10.806m; tick833
bud_aalst_afm_2025,city_aalst,2025,7985825,,,cash,src_aalst_jr2025,strong,Autofinancieringsmarge AFM +7.986m (gecorr +4.435m); tick833
bud_aalst_afm_corr_2025,city_aalst,2025,4434597,,,cash,src_aalst_jr2025,strong,Gecorrigeerde AFM +4.435m; tick833
bud_aalst_bbr_2025,city_aalst,2025,16320776,,,cash,src_aalst_jr2025,strong,Beschikbaar budgettair resultaat BBR 16.321m (177 EUR/inwoner); tick833
bud_aalst_budget_result_2025,city_aalst,2025,-14224858,,,cash,src_aalst_jr2025,strong,Budgettair resultaat boekjaar -14.225m; tick833
bud_aalst_pnl_result_2025,city_aalst,2025,850178,,,cash,src_aalst_jr2025,strong,Vennootschapsresultaat J5 +0.850m; tick833
bud_aalst_bezold_2025,city_aalst,2025,139124117,,,cash,src_aalst_jr2025,strong,J5/T2 bezoldigingen 139.124m (incl onderwijzend 21.058m other-gov; cash own-charge class ~118.1m); tick833
bud_aalst_goederen_2025,city_aalst,2025,44629280,,,cash,src_aalst_jr2025,strong,J5 goederen en diensten 44.629m; tick833
bud_aalst_toelagen_2025,city_aalst,2025,51423586,,,cash,src_aalst_jr2025,strong,J5/T2 toegestane werkingssubsidies 51.424m (police 28.052 fire 7.129 AGB 8.598 other 6.559); tick833
bud_aalst_police_toelage_2025,city_aalst,2025,28051511,,,cash,src_aalst_jr2025,strong,Toelage politiezone 28.052m; tick833
bud_aalst_fire_toelage_2025,city_aalst,2025,7128523,,,cash,src_aalst_jr2025,strong,Toelage hulpverleningszone 7.129m; tick833
bud_aalst_agb_toelage_2025,city_aalst,2025,8597680,,,cash,src_aalst_jr2025,strong,Toelage AGB 8.598m; tick833
bud_aalst_ocmw_aid_2025,city_aalst,2025,15671082,,,cash,src_aalst_jr2025,strong,J5 individuele hulpverlening OCMW 15.671m; tick833
bud_aalst_ocmw_deficit_cover_2025,city_aalst,2025,15036583,,,cash,src_aalst_jr2025,strong,Tussenkomst stad in OCMW-tekort 15.037m; tick833
bud_aalst_fiscal_2025,city_aalst,2025,90441741,,,cash,src_aalst_jr2025,strong,J5 fiscale opbrengsten en boetes 90.442m; tick833
bud_aalst_werk_subs_rec_2025,city_aalst,2025,129218541,,,cash,src_aalst_jr2025,strong,J5 werkingssubsidies ontvangen 129.219m (gemeentefonds 57.070m); tick833
bud_aalst_fin_costs_2025,city_aalst,2025,3986665,,,cash,src_aalst_jr2025,strong,J5 financiele kosten 3.987m; tick833
bud_aalst_inv_subs_granted_2025,city_aalst,2025,3627926,,,cash,src_aalst_jr2025,strong,Toegestane investeringssubsidies 3.628m; tick833
bud_aalst_debt_per_capita_2025,city_aalst,2025,1784,,,stock,src_aalst_jr2025,strong,Openstaande schuld per inwoner 1784 EUR (incl ST); tick833
""".strip() + "\n"

lb = """
lb_aalst_bezold_139m_2025,Aalst J5 bezoldigingen 139.1m 2025 (own-charge class ~118m),L5,ops,Vlaanderen>Gemeenten>Aalst>personnel,139124117,139124117,Strong primary; +9.3pct YoY; includes 21.1m onderwijzend other-gov; dual Genk 79.6m Kortrijk 136m Mechelen 113m,strong,src_aalst_jr2025,city/OCMW/school staff,Deliver local services,139.1m / +9.3pct,5.0,7.2,5.0,5.73,ETP productivity FOI,active,,tick833
lb_aalst_toelagen_51m_2025,Aalst granted operating subsidies 51.4m 2025,L5,subsidy,Vlaanderen>Gemeenten>Aalst>toelagen,51423586,51423586,Strong; police 28.1 fire 7.1 AGB 8.6 other 6.6; dual Kortrijk 39.6m Genk 35.3m Mechelen ~90m,strong,src_aalst_jr2025,police zone / fire / AGB / associations,Fund safety zones and local partners,51.4m,5.5,6.8,5.5,5.93,Named beneficiary matrix FOI,active,,tick833
lb_aalst_fin_debt_164m,Aalst financial debt stock 164.3m YE2025 (-15.2m YoY),L5,stock,Vlaanderen>Gemeenten>Aalst>debt,3986665,164299390,Strong; LT 148.5m + ST due 10.8m + treasury 5m; low new loans 0.65m vs repay 10.8m; dual Genk 175m Kortrijk 258m,strong,src_aalst_jr2025,lenders / infrastructure users,Finance investment programme 34.5m 2025,164.3m stock / -15.2m,5.0,7.0,5.5,5.83,Debt schedule FOI,active,,tick833 stock
lb_aalst_ocmw_cover_15m_2025,Aalst city cover of OCMW deficit 15.0m 2025,L5,transfer,Vlaanderen>Gemeenten>Aalst>OCMW,15036583,15036583,Strong kengetallen tussenkomst; dual social stack with OCMW aid 15.7m,strong,src_aalst_jr2025,OCMW Aalst,Balance OCMW exploitation deficit,15.0m city transfer,5.0,6.0,5.5,5.5,Outcomes + dual OCMW FOI,active,,tick833
lb_aalst_invest_35m_2025,Aalst investment spend 34.5m 2025 (net -22.2m after 12.4m receipts),L5,capex,Vlaanderen>Gemeenten>Aalst>invest,34537629,34537629,Strong; roads 15.2m buildings 9.7m; dual Genk 32m Kortrijk 57m,strong,src_aalst_jr2025,city infrastructure users,Maintain and expand city infrastructure,34.5m,4.5,6.0,5.0,5.17,Project-level ROI FOI,active,,tick833
lb_aalst_bbr_16m,Aalst beschikbaar budgettair resultaat +16.3m YE2025,L5,ops,Vlaanderen>Gemeenten>Aalst>liquidity,0,16320776,Strong BBR solid; AFM +8.0m; cash 18.5m after 2024 drawdown from 38.8m,strong,src_aalst_jr2025,liquidity buffer,Budgetary cash position,BBR +16.3m / cash 18.5m,3.5,5.5,4.0,4.33,Sustain AFM path FOI,active,,tick833 positive buffer not waste
lb_dual_aalst_genk_kortrijk_tick833,Dual Aalst 617m vs Genk 629m vs Kortrijk 720m city residual,L5,ops,Belgium>dual>vl_cities,0,616504271,Strong dual not TE-additive; Aalst high expl 276m and toelagen 51m vs peers,strong,src_dual_aalst_genk_kortrijk_tick833,multi-channel,Dual residual map,primary,4.5,7.5,5.0,5.67,Cross FOI,active,,tick833
""".strip() + "\n"

cmt = """
cmt_aalst_balance_617m_2025,Aalst consol stad+OCMW balance sheet YE2025 assets 616.5m,city_aalst,Stad en OCMW Aalst,BBC jaarrekening 2025 schema J4,2026-07-03,2025,2025,616504271,"{""assets_m"": 616.504, ""equity_m"": 406.800, ""debt_total_m"": 209.705, ""fin_debt_m"": 164.299, ""pension_prov_m"": 8.592, ""cash_m"": 18.494, ""cap_subs_m"": 98.036}",0,active,https://aalst.be/bestuur-en-participatie/beleid/beleidsrapporten,Municipal consolidated balance sheet,Publish debt schedule FOI,src_aalst_jr2025,strong,Vlaanderen>Gemeenten>Aalst>balance,tick833 published 3 Jul 2026
cmt_aalst_expl_276m_2025,Aalst exploitation receipts 276.2m expenses 260.2m 2025,city_aalst,Stad en OCMW Aalst,BBC J2/J5 2025,2025-12-31,2025,2025,276171685,"{""expl_rec_m"": 276.172, ""expl_exp_m"": 260.234, ""expl_saldo_m"": 15.938, ""bezold_m"": 139.124, ""toelagen_m"": 51.424, ""fiscal_m"": 90.442, ""werk_subs_rec_m"": 129.219}",0,active,docs/doge/data/raw/aalst_jr2025.pdf,Large VL city exploitation stack,Named toelagen matrix FOI,src_aalst_jr2025,strong,Vlaanderen>Gemeenten>Aalst>exploitation,tick833
cmt_aalst_afm_bbr_2025,Aalst AFM +8.0m and BBR +16.3m 2025,city_aalst,Fiscal sustainability indicators,BBC schema J2 2025,2025-12-31,2025,2025,16320776,"{""afm_m"": 7.986, ""afm_corr_m"": 4.435, ""bbr_m"": 16.321, ""budget_result_m"": -14.225, ""expl_saldo_m"": 15.938, ""bbr_per_capita"": 177}",0,active,docs/doge/data/raw/aalst_jr2025.pdf,Solid AFM and BBR; low new loans 0.65m,Sustain AFM path FOI MJP,src_aalst_jr2025,strong,Vlaanderen>Gemeenten>Aalst>AFM,tick833
cmt_dual_aalst_genk_kortrijk_tick833,Dual Aalst JR2025 vs Genk vs Kortrijk city residual,gg_belgium,dual map,Aalst JR2025 dual prior city fills,2026-08-05,2025,2025,616504271,"{""aalst_assets_m"": 616.5, ""genk_assets_m"": 628.7, ""kortrijk_assets_m"": 720.4, ""aalst_expl_m"": 276.2, ""aalst_toelagen_m"": 51.4, ""aalst_pension_m"": 8.6, ""genk_pension_m"": 312.6}",0,active,docs/doge/data/raw/aalst_jr2025.pdf,Dual residual map tick833,Cross FOI city L5,src_dual_aalst_genk_kortrijk_tick833,strong,Belgium>dual>vl_cities,tick833 not TE-additive
""".strip() + "\n"

src = """
src_aalst_jr2025,"Stad en OCMW Aalst Jaarrekening 2025 (BBC, 260p, publicatiedatum 3 jul 2026)",https://raadpleeg-aalst.onlinesmartcities.be/document/6a30102ca02759b5fd7cf0c4,Stad Aalst / OCMW Aalst,2026-08-05,entity_accounts,Strong tick833 primary: consol assets 616.5m equity 406.8m; expl ontvangsten 276.2m uitgaven 260.2m saldo +15.9m; AFM 8.0m BBR 16.3m; bezold 139.1m; fin debt 164.3m; pension prov 8.6m; toelagen 51.4m (police 28.1); invest 34.5m; OCMW cover 15.0m; raw aalst_jr2025.pdf
src_dual_aalst_genk_kortrijk_tick833,Dual Aalst JR2025 617m vs Genk 629m vs Kortrijk 720m residual tick833,docs/doge/data/raw/aalst_jr2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: Aalst assets 616.5m expl 276m bezold 139m toelagen 51m AFM +8.0m vs Genk assets 629m pension 313m vs Kortrijk assets 720m loon 136m
""".strip() + "\n"

ent = "city_aalst,Stad Aalst,Ville d'Alost,City of Aalst,municipality,vlaanderen_gov,nl,https://aalst.be,,Grote Markt 3 9300 Aalst,JR2025 assets 616.5m expl 276m bezold 139m toelagen 51m fin debt 164m; tick833\n"

foi = 'gap_aalst_debt_pension_subs_l5,Vlaanderen>Gemeenten>Aalst_L5,city_aalst,Full debt schedule by lender for fin debt 164.3m; named toelagen matrix within 51.4m beyond police/fire/AGB aggregates; OCMW deficit-cover multipjaar path (15.0m 2025); MJP multi-year new-loan path (0.65m actual vs 35-40m plan; plan 2026-27 up to 234m stock); ETP behind 139m bezold,"617m city+OCMW book with 276m exploitation, 139m personnel and 51m toelagen blocks dual VL city waste ranking vs Genk/Kortrijk/Mechelen",7,Stad Aalst / financieel directeur / openbaarheid van bestuur,,https://aalst.be,docs/doge/foi/drafts/gap_aalst_debt_pension_subs_l5.md,ready,2026-08-05,,,,,cmt_aalst_balance_617m_2025|cmt_aalst_expl_276m_2025|cmt_aalst_afm_bbr_2025,lb_aalst_bezold_139m_2025|lb_aalst_toelagen_51m_2025|lb_aalst_fin_debt_164m|lb_aalst_ocmw_cover_15m_2025,2026-08-05T13:30:00Z,2026-08-05T13:30:00Z,tick833 primary JR2025; ready draft; do not send\n'

# research_queue
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_823,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Genk JR2025 filled tick832; residual Aalst/Roeselare/Hasselt city or BELNET AR2025 or skeyes residual",,2026-08-05T13:00:00Z,2026-08-05T13:00:00Z,spawned tick832 after Genk dual Kortrijk/Mechelen'
new = 'rq_823,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Genk JR2025 filled tick832; residual Aalst/Roeselare/Hasselt city or BELNET AR2025 or skeyes residual",gap_aalst_debt_pension_subs_l5,2026-08-05T13:00:00Z,2026-08-05T13:30:00Z,tick833 Aalst JR2025 assets 616.5m expl 276.2m bezold 139.1m AFM 8.0m fin debt 164.3m toelagen 51.4m dual Genk/Kortrijk; FOI ready'
if old not in text:
    raise SystemExit("rq_823 row not found for replace")
text = text.replace(old, new)
spawn = 'rq_824,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Aalst JR2025 filled tick833; residual Roeselare/Hasselt city or BELNET AR2025 accounts or skeyes residual",,2026-08-05T13:30:00Z,2026-08-05T13:30:00Z,spawned tick833 after Aalst dual Genk/Kortrijk\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T13:30:00Z,rq_823,833,no,"
    "tick833 Aalst JR2025 dual Genk/Kortrijk; next rq_824 residual dual L5; progress@840 in 7; rq_116 deferred\n",
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
    with (root / name).open("a", encoding="utf-8", newline="") as f:
        f.write(payload)

# extract key pages
import fitz

doc = fitz.open("docs/doge/data/raw/aalst_jr2025.pdf")
pages = [0, 7, 52, 53, 54, 55, 56, 57, 61, 62, 63, 64, 100, 231]
with open("docs/doge/data/raw/aalst_jr2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("Aalst JR2025 key extract tick833\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick833 CSV updates OK")

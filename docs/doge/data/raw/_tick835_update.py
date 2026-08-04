# tick835 — Tielt JR2025 fill (Hasselt JR scan-only blocked)
from pathlib import Path
import fitz

root = Path("docs/doge/data")
FIN_DEBT = 15832254 + 1979827  # 17812081

budgets = f"""
bud_tielt_assets_2025,city_tielt,2025,193086097,,,stock,src_tielt_jr2025,strong,Consol stad+OCMW total assets YE2025 193.086m (post-fusion perimeter); tick835
bud_tielt_equity_2025,city_tielt,2025,144039796,,,stock,src_tielt_jr2025,strong,Nettoactief YE2025 144.040m; tick835
bud_tielt_debt_total_2025,city_tielt,2025,49046301,,,stock,src_tielt_jr2025,strong,Total schulden YE2025 49.046m; tick835
bud_tielt_fin_debt_2025,city_tielt,2025,{FIN_DEBT},,,stock,src_tielt_jr2025,strong,Financiele schulden YE2025 17.812m (LT 15.832 + ST due 1.980; kerncijfers 17.812m; 557 EUR/capita); tick835
bud_tielt_fin_debt_lt_2025,city_tielt,2025,15832254,,,stock,src_tielt_jr2025,strong,Financiele schulden LT YE2025 15.832m; tick835
bud_tielt_pension_prov_2025,city_tielt,2025,16633568,,,stock,src_tielt_jr2025,strong,Pensioenvoorzieningen YE2025 16.634m; tick835
bud_tielt_cash_2025,city_tielt,2025,24554682,,,stock,src_tielt_jr2025,strong,Liquide middelen YE2025 24.555m; tick835
bud_tielt_cap_subs_2025,city_tielt,2025,30417853,,,stock,src_tielt_jr2025,strong,Kapitaalsubsidies YE2025 30.418m; tick835
bud_tielt_fva_igs_2025,city_tielt,2025,32714545,,,stock,src_tielt_jr2025,strong,Fin VA IGS 32.715m; tick835
bud_tielt_expl_rec_2025,city_tielt,2025,66917039,,,cash,src_tielt_jr2025,strong,Exploitatieontvangsten 66.917m; tick835
bud_tielt_expl_exp_2025,city_tielt,2025,55437290,,,cash,src_tielt_jr2025,strong,Exploitatieuitgaven 55.437m; tick835
bud_tielt_expl_saldo_2025,city_tielt,2025,11479749,,,cash,src_tielt_jr2025,strong,Exploitatiesaldo +11.480m; tick835
bud_tielt_invest_exp_2025,city_tielt,2025,12174756,,,cash,src_tielt_jr2025,strong,Investeringsuitgaven 12.175m (Tielt Noord lands 6.97m via WVI); tick835
bud_tielt_invest_rec_2025,city_tielt,2025,210875,,,cash,src_tielt_jr2025,strong,Investeringsontvangsten 0.211m; tick835
bud_tielt_invest_saldo_2025,city_tielt,2025,-11963881,,,cash,src_tielt_jr2025,strong,Investeringssaldo -11.964m; tick835
bud_tielt_fin_rec_2025,city_tielt,2025,879433,,,cash,src_tielt_jr2025,strong,Financieringsontvangsten 0.879m; tick835
bud_tielt_fin_exp_2025,city_tielt,2025,2588512,,,cash,src_tielt_jr2025,strong,Financieringsuitgaven 2.589m; tick835
bud_tielt_afm_2025,city_tielt,2025,9460032,,,cash,src_tielt_jr2025,strong,Autofinancieringsmarge AFM +9.460m; tick835
bud_tielt_afm_corr_2025,city_tielt,2025,11683204,,,cash,src_tielt_jr2025,strong,Gecorrigeerde AFM +11.683m (J2 schema); tick835
bud_tielt_bbr_2025,city_tielt,2025,18498417,,,cash,src_tielt_jr2025,strong,Beschikbaar budgettair resultaat BBR 18.498m; tick835
bud_tielt_budget_result_2025,city_tielt,2025,-2193210,,,cash,src_tielt_jr2025,strong,Budgettair resultaat boekjaar -2.193m; tick835
bud_tielt_pnl_result_2025,city_tielt,2025,5566067,,,cash,src_tielt_jr2025,strong,Vennootschapsresultaat J5 +5.566m; tick835
bud_tielt_personnel_2025,city_tielt,2025,30003504,,,cash,src_tielt_jr2025,strong,Personeelsuitgaven/J5 bezold 30.004m (incl Agodi onderwijzend 3.641m + Zorg detach 3.121m + respo 0.273m); tick835
bud_tielt_toelagen_2025,city_tielt,2025,11390556,,,cash,src_tielt_jr2025,strong,Toegestane werkingssubsidies 11.391m (police 3.082 fire 0.982 IGS 2.741 other 3.659 AGB 0.534); tick835
bud_tielt_police_toelage_2025,city_tielt,2025,3082019,,,cash,src_tielt_jr2025,strong,Werkingstoelage politiezone 3.082m (+invest 0.202m); tick835
bud_tielt_fire_toelage_2025,city_tielt,2025,981614,,,cash,src_tielt_jr2025,strong,Werkingstoelage hulpverleningszone 0.982m (+invest 0.219m); tick835
bud_tielt_ocmw_aid_2025,city_tielt,2025,3404615,,,cash,src_tielt_jr2025,strong,Individuele hulpverlening OCMW 3.405m; tick835
bud_tielt_fiscal_2025,city_tielt,2025,29643836,,,cash,src_tielt_jr2025,strong,J5 fiscale opbrengsten en boetes 29.644m (APB 12.152 OV 15.125); tick835
bud_tielt_werk_subs_rec_2025,city_tielt,2025,27398795,,,cash,src_tielt_jr2025,strong,Ontvangen werkingssubsidies 27.399m; tick835
bud_tielt_fin_costs_2025,city_tielt,2025,332142,,,cash,src_tielt_jr2025,strong,J5 financiele kosten 0.332m; tick835
bud_tielt_population_2025,city_tielt,2025,31973,,,stock,src_tielt_jr2025,strong,Inwoners 1 jan 2025 31973; tick835
""".strip() + "\n"

lb = f"""
lb_tielt_personnel_30m_2025,Tielt personnel 30.0m 2025 (post-fusion perimeter),L5,ops,Vlaanderen>Gemeenten>Tielt>personnel,30003504,30003504,Strong; dual Brugge 189 Aalst 139; includes Agodi 3.6m + Zorg detach 3.1m,strong,src_tielt_jr2025,city/OCMW/school staff,Deliver local services,30.0m,4.5,5.5,5.0,5.0,ETP FOI,active,,tick835
lb_tielt_toelagen_11m_2025,Tielt granted operating subsidies 11.4m 2025,L5,subsidy,Vlaanderen>Gemeenten>Tielt>toelagen,11390556,11390556,Strong; police 3.1 fire 1.0 IGS 2.7 other 3.7; dual Brugge 95 Aalst 51,strong,src_tielt_jr2025,police/fire/IGS/AGB/associations,Fund safety zones and partners,11.4m,5.0,5.0,5.5,5.17,Named matrix FOI,active,,tick835
lb_tielt_fin_debt_18m,Tielt financial debt stock 17.8m YE2025 (557 EUR/capita),L5,stock,Vlaanderen>Gemeenten>Tielt>debt,332142,17812081,Strong; low leverage vs large VL cities; dual Brugge 192 Genk 175,strong,src_tielt_jr2025,lenders,Finance invest 12.2m,17.8m stock,3.5,4.5,5.0,4.33,Debt schedule FOI,active,,tick835 stock
lb_tielt_invest_12m_2025,Tielt investment spend 12.2m 2025 (Tielt Noord lands 7.0m),L5,capex,Vlaanderen>Gemeenten>Tielt>invest,12174756,12174756,Strong; WVI industrial land 6.97m dominant; dual Brugge 84,strong,src_tielt_jr2025,industry zone / city infra,Expand industrial land and local infra,12.2m,4.0,5.0,5.0,4.67,ROI industrial FOI,active,,tick835
lb_tielt_afm_9m_2025,Tielt AFM +9.46m BBR +18.5m 2025,L5,ops,Vlaanderen>Gemeenten>Tielt>AFM,0,9460032,Strong solid buffers midsize post-fusion city,strong,src_tielt_jr2025,liquidity,Fiscal sustainability,AFM 9.5m BBR 18.5m,3.0,4.5,4.0,3.83,Sustain path FOI,active,,tick835 positive buffer
lb_dual_tielt_brugge_tick835,Dual Tielt 193m vs Brugge 1462m midsize/large VL city residual,L5,ops,Belgium>dual>vl_cities,0,193086097,Strong dual not TE-additive; Tielt post-fusion perimeter,strong,src_dual_tielt_brugge_tick835,multi-channel,Dual residual map,primary,4.0,6.5,5.0,5.17,Cross FOI,active,,tick835
""".strip() + "\n"

cmt = f"""
cmt_tielt_balance_193m_2025,Tielt consol stad+OCMW balance sheet YE2025 assets 193.1m,city_tielt,Stad en OCMW Tielt,BBC jaarrekening 2025 schema J4,2025-12-31,2025,2025,193086097,"{{""assets_m"": 193.086, ""equity_m"": 144.040, ""debt_total_m"": 49.046, ""fin_debt_m"": 17.812, ""pension_prov_m"": 16.634, ""cash_m"": 24.555, ""pop"": 31973}}",0,active,https://www.tielt.be/sites/default/files/2026-07/Stad_OCMW_Tielt_Jaarrekening_2025.pdf,Post-fusion midsize city BS,Publish debt FOI,src_tielt_jr2025,strong,Vlaanderen>Gemeenten>Tielt>balance,tick835
cmt_tielt_expl_67m_2025,Tielt exploitation receipts 66.9m expenses 55.4m 2025,city_tielt,Stad en OCMW Tielt,BBC J2/J5 2025,2025-12-31,2025,2025,66917039,"{{""expl_rec_m"": 66.917, ""expl_exp_m"": 55.437, ""expl_saldo_m"": 11.480, ""personnel_m"": 30.004, ""toelagen_m"": 11.391, ""fiscal_m"": 29.644}}",0,active,docs/doge/data/raw/tielt_jr2025.pdf,Midsize VL city exploitation stack,Named toelagen FOI,src_tielt_jr2025,strong,Vlaanderen>Gemeenten>Tielt>exploitation,tick835
cmt_tielt_afm_bbr_2025,Tielt AFM +9.46m and BBR +18.5m 2025,city_tielt,Fiscal sustainability indicators,BBC schema J2 2025,2025-12-31,2025,2025,18498417,"{{""afm_m"": 9.460, ""afm_corr_m"": 11.683, ""bbr_m"": 18.498, ""budget_result_m"": -2.193, ""expl_saldo_m"": 11.480}}",0,active,docs/doge/data/raw/tielt_jr2025.pdf,Solid AFM/BBR post-fusion,Sustain path FOI,src_tielt_jr2025,strong,Vlaanderen>Gemeenten>Tielt>AFM,tick835
cmt_dual_tielt_brugge_tick835,Dual Tielt JR2025 vs Brugge JR2025 city residual,gg_belgium,dual map,Tielt JR2025 dual Brugge tick834,2026-08-05,2025,2025,193086097,"{{""tielt_assets_m"": 193.1, ""brugge_assets_m"": 1462.3, ""tielt_expl_m"": 66.9, ""brugge_expl_m"": 419.1, ""tielt_personnel_m"": 30.0, ""brugge_personnel_m"": 189.2}}",0,active,docs/doge/data/raw/tielt_jr2025.pdf,Dual residual map tick835,Cross FOI,src_dual_tielt_brugge_tick835,strong,Belgium>dual>vl_cities,tick835 not TE-additive
""".strip() + "\n"

src = """
src_tielt_jr2025,"Stad en OCMW Tielt Jaarrekening 2025 (BBC, 100p, post-fusion perimeter)",https://www.tielt.be/sites/default/files/2026-07/Stad_OCMW_Tielt_Jaarrekening_2025.pdf,Stad Tielt / OCMW Tielt,2026-08-05,entity_accounts,Strong tick835 primary: consol assets 193.1m equity 144.0m; expl ontvangsten 66.9m uitgaven 55.4m saldo +11.5m; AFM 9.46m BBR 18.5m; personnel 30.0m; fin debt 17.8m (557/capita); pension 16.6m; toelagen 11.4m; invest 12.2m (Tielt Noord 7.0m); pop 31973; raw tielt_jr2025.pdf
src_dual_tielt_brugge_tick835,Dual Tielt JR2025 193m vs Brugge 1462m residual tick835,docs/doge/data/raw/tielt_jr2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: Tielt midsize post-fusion assets 193m expl 67m personnel 30m AFM +9.5m vs Brugge assets 1462m expl 419m personnel 189m
src_hasselt_jr2025_scanblocked,Stad en OCMW Hasselt Jaarrekening 2025 PDF scan-only (362p 171MB no text layer),https://www.hasselt.be/sites/hasselt/files/2026-05/111_jaarrekening_stad_ocmw_2025.pdf,Stad Hasselt,2026-08-05,entity_accounts,tick835 attempted; zero extractable text; residual OCR/FOI; raw hasselt_jr2025.pdf retained
""".strip() + "\n"

ent = "city_tielt,Stad Tielt,Ville de Tielt,City of Tielt,municipality,vlaanderen_gov,nl,https://www.tielt.be,info@tielt.be,Markt 13 8700 Tielt,JR2025 assets 193m expl 67m personnel 30m fin debt 18m post-fusion; tick835\n"

foi = f'gap_tielt_debt_subs_l5,Vlaanderen>Gemeenten>Tielt_L5,city_tielt,Full debt schedule by lender for fin debt 17.8m; named toelagen matrix within 11.4m beyond police/fire/IGS/AGB; ETP behind 30.0m personnel (Agodi/Zorg detach split); Tielt Noord industrial land ROI path 7.0m WVI; fusion perimeter reconciliation 2024-2025,"193m post-fusion city+OCMW book with 67m exploitation and 30m personnel blocks midsize VL dual ranking vs Brugge/Aalst",6,Stad Tielt / financieel directeur / openbaarheid,,https://www.tielt.be,docs/doge/foi/drafts/gap_tielt_debt_subs_l5.md,ready,2026-08-05,,,,,cmt_tielt_balance_193m_2025|cmt_tielt_expl_67m_2025|cmt_tielt_afm_bbr_2025,lb_tielt_personnel_30m_2025|lb_tielt_toelagen_11m_2025|lb_tielt_fin_debt_18m|lb_tielt_invest_12m_2025,2026-08-05T14:30:00Z,2026-08-05T14:30:00Z,tick835 primary JR2025; ready draft; do not send; Hasselt scan-blocked residual\n'

# also FOI for Hasselt scan gap (optional brief)
foi2 = 'gap_hasselt_jr2025_ocr_l5,Vlaanderen>Gemeenten>Hasselt_L5,city_hasselt,Machine-readable JR2025 stad+OCMW (current PDF 171MB scan-only 362p no text layer); key J2/J4/J5 tables AFM BBR debt pension personnel toelagen,Blocks VL city dual map residual after Mechelen Kortrijk Genk Aalst Brugge Tielt fills,7,Stad Hasselt / financieel directeur / openbaarheid,,https://www.hasselt.be,docs/doge/foi/drafts/gap_hasselt_jr2025_ocr_l5.md,ready,2026-08-05,,,,,cmt_tielt_balance_193m_2025,,2026-08-05T14:30:00Z,2026-08-05T14:30:00Z,tick835 attempted extract; FOI for text/CSV export; do not send\n'

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_825,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Brugge JR2025 filled tick834; residual Roeselare/Hasselt city or BELNET AR2025 accounts or skeyes residual",,2026-08-05T14:00:00Z,2026-08-05T14:00:00Z,spawned tick834 after Brugge dual Aalst/Genk'
new = 'rq_825,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Brugge JR2025 filled tick834; residual Roeselare/Hasselt city or BELNET AR2025 accounts or skeyes residual",gap_tielt_debt_subs_l5,2026-08-05T14:00:00Z,2026-08-05T14:30:00Z,tick835 Tielt JR2025 assets 193m expl 67m personnel 30m AFM 9.5m dual Brugge; Hasselt JR scan-blocked FOI; FOI ready'
if old not in text:
    raise SystemExit("rq_825 not found")
text = text.replace(old, new)
spawn = 'rq_826,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Tielt JR2025 filled tick835; Hasselt scan FOI; residual Roeselare/Leuven city or UHasselt JV2025 or BELNET accounts or skeyes residual",,2026-08-05T14:30:00Z,2026-08-05T14:30:00Z,spawned tick835 after Tielt dual Brugge\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T14:30:00Z,rq_825,835,no,"
    "tick835 Tielt JR2025 dual Brugge; Hasselt scan FOI; next rq_826 residual dual L5; progress@840 in 5; rq_116 deferred\n",
    encoding="utf-8",
)

for name, payload in [
    ("budgets.csv", budgets),
    ("leaderboard.csv", lb),
    ("commitments.csv", cmt),
    ("sources.csv", src),
    ("entities.csv", ent),
    ("foi_queue.csv", foi + foi2),
]:
    with (root / name).open("a", encoding="utf-8", newline="") as f:
        f.write(payload)

doc = fitz.open("docs/doge/data/raw/tielt_jr2025.pdf")
pages = [11, 19, 22, 23, 24, 27]
with open("docs/doge/data/raw/tielt_jr2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("Tielt JR2025 key extract tick835\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick835 OK fin_debt=", FIN_DEBT)

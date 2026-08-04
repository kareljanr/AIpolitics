# tick841 — Leuven JR2025 fill dual Brugge; VUB PDF encoding FOI
from pathlib import Path
import fitz

root = Path("docs/doge/data")
FIN_DEBT = 308395579 + 13810384 + 12350000  # 334555963

budgets = f"""
bud_leuven_assets_2025,city_leuven,2025,956966739,,,stock,src_leuven_jr2025,strong,Consol stad+OCMW total assets YE2025 956.967m; tick841
bud_leuven_equity_2025,city_leuven,2025,502252950,,,stock,src_leuven_jr2025,strong,Nettoactief YE2025 502.253m; tick841
bud_leuven_debt_total_2025,city_leuven,2025,454713789,,,stock,src_leuven_jr2025,strong,Total schulden YE2025 454.714m; tick841
bud_leuven_fin_debt_2025,city_leuven,2025,{FIN_DEBT},,,stock,src_leuven_jr2025,strong,Financiele schulden total YE2025 334.556m (LT 308.396 + ST due 13.810 + ST treasury 12.350); +79.8m YoY; tick841
bud_leuven_fin_debt_lt_2025,city_leuven,2025,308395579,,,stock,src_leuven_jr2025,strong,Financiele schulden LT YE2025 308.396m; tick841
bud_leuven_fin_debt_st_2025,city_leuven,2025,12350000,,,stock,src_leuven_jr2025,strong,Thesaurie ST YE2025 12.350m (was 29.965m); tick841
bud_leuven_pension_prov_2025,city_leuven,2025,51503687,,,stock,src_leuven_jr2025,strong,Pensioenvoorzieningen YE2025 51.504m; tick841
bud_leuven_cash_2025,city_leuven,2025,14843066,,,stock,src_leuven_jr2025,strong,Liquide middelen YE2025 14.843m; tick841
bud_leuven_cap_subs_2025,city_leuven,2025,61541187,,,stock,src_leuven_jr2025,strong,Kapitaalsubsidies YE2025 61.541m; tick841
bud_leuven_fva_igs_2025,city_leuven,2025,72017763,,,stock,src_leuven_jr2025,strong,Fin VA IGS 72.018m; tick841
bud_leuven_expl_rec_2025,city_leuven,2025,331314507,,,cash,src_leuven_jr2025,strong,Exploitatieontvangsten 331.315m; tick841
bud_leuven_expl_exp_2025,city_leuven,2025,302104355,,,cash,src_leuven_jr2025,strong,Exploitatieuitgaven 302.104m; tick841
bud_leuven_expl_saldo_2025,city_leuven,2025,29210152,,,cash,src_leuven_jr2025,strong,Exploitatiesaldo +29.210m; tick841
bud_leuven_invest_exp_2025,city_leuven,2025,90090279,,,cash,src_leuven_jr2025,strong,Investeringsuitgaven 90.090m; tick841
bud_leuven_invest_rec_2025,city_leuven,2025,21310196,,,cash,src_leuven_jr2025,strong,Investeringsontvangsten 21.310m; tick841
bud_leuven_invest_saldo_2025,city_leuven,2025,-68780083,,,cash,src_leuven_jr2025,strong,Investeringssaldo -68.780m (net invest ~68.8m narrative); tick841
bud_leuven_fin_rec_2025,city_leuven,2025,114062618,,,cash,src_leuven_jr2025,strong,Financieringsontvangsten 114.063m (new loans ~108m); tick841
bud_leuven_fin_exp_2025,city_leuven,2025,31774532,,,cash,src_leuven_jr2025,strong,Financieringsuitgaven 31.775m; tick841
bud_leuven_new_loans_2025,city_leuven,2025,109464801,,,cash,src_leuven_jr2025,strong,Nieuwe leningen T4 109.465m (KBC 108m + energy pass-through); tick841
bud_leuven_aflossingen_2025,city_leuven,2025,12010378,,,cash,src_leuven_jr2025,strong,Periodieke aflossingen 12.010m; tick841
bud_leuven_afm_2025,city_leuven,2025,21590468,,,cash,src_leuven_jr2025,strong,AFM +21.590m (was 2.6m 2024); tick841
bud_leuven_afm_corr_2025,city_leuven,2025,13223523,,,cash,src_leuven_jr2025,strong,Gecorrigeerde AFM +13.224m; tick841
bud_leuven_bbr_2025,city_leuven,2025,18758606,,,cash,src_leuven_jr2025,strong,BBR 18.759m after onbeschikbaar Kreglinger 11.206m; tick841
bud_leuven_budget_result_2025,city_leuven,2025,42718156,,,cash,src_leuven_jr2025,strong,Budgettair resultaat boekjaar +42.718m; tick841
bud_leuven_pnl_result_2025,city_leuven,2025,3696584,,,cash,src_leuven_jr2025,strong,Vennootschapsresultaat J5 +3.697m (was -33.459m); tick841
bud_leuven_personnel_2025,city_leuven,2025,117167373,,,cash,src_leuven_jr2025,strong,Personeel excl onderwijs 117.167m (+3.8pct); onderwijs 8.413m pass-through; tick841
bud_leuven_bezold_2025,city_leuven,2025,125580154,,,cash,src_leuven_jr2025,strong,J5 bezoldigingen 125.580m; tick841
bud_leuven_toelagen_2025,city_leuven,2025,96286298,,,cash,src_leuven_jr2025,strong,Toegestane werkingssubsidies 96.286m (-7pct; EVA inkanteling); tick841
bud_leuven_ocmw_aid_2025,city_leuven,2025,26490508,,,cash,src_leuven_jr2025,strong,OCMW individuele hulp 26.491m; tick841
bud_leuven_fiscal_2025,city_leuven,2025,150884464,,,cash,src_leuven_jr2025,strong,J5 fiscale opbrengsten en boetes 150.884m; tick841
bud_leuven_werk_subs_rec_2025,city_leuven,2025,135893491,,,cash,src_leuven_jr2025,strong,J5 werkingssubsidies ontvangen 135.893m (gemeentefonds 81.885m); tick841
bud_leuven_fin_costs_2025,city_leuven,2025,8391756,,,cash,src_leuven_jr2025,strong,J5 financiele kosten 8.392m; tick841
bud_leuven_kreglinger_escrow_2025,city_leuven,2025,11205634,,,stock,src_leuven_jr2025,strong,Onbeschikbare gelden Kreglinger kantonnement 11.206m; tick841
""".strip() + "\n"

lb = f"""
lb_leuven_personnel_117m_2025,Leuven personnel excl onderwijs 117.2m 2025 (+3.8pct),L5,ops,Vlaanderen>Gemeenten>Leuven>personnel,117167373,117167373,Strong; J5 bezold 125.6m incl onderwijs; dual Brugge 189 Aalst 139,strong,src_leuven_jr2025,city/OCMW staff,Deliver local services,117.2m / 39pct expl,5.0,7.0,5.0,5.67,ETP FOI,active,,tick841
lb_leuven_toelagen_96m_2025,Leuven granted operating subsidies 96.3m 2025 (-7pct),L5,subsidy,Vlaanderen>Gemeenten>Leuven>toelagen,96286298,96286298,Strong; dual Brugge 95 Mechelen 90; EVA inkanteling cut,strong,src_leuven_jr2025,Zorg Leuven / police / fire / EVA,Fund partners and safety zones,96.3m / -6.7m YoY,5.5,7.0,5.0,5.83,Named matrix FOI,active,,tick841
lb_leuven_fin_debt_335m,Leuven financial debt stock 334.6m YE2025 (+79.8m YoY),L5,stock,Vlaanderen>Gemeenten>Leuven>debt,8391756,334555963,Strong; new loans 109m KBC; dual Brugge 192 Genk 175 Kortrijk 258,strong,src_leuven_jr2025,lenders,Finance invest 90m 2025,334.6m stock / +80m,5.5,7.5,5.5,6.17,Debt schedule FOI,active,,tick841 stock
lb_leuven_invest_90m_2025,Leuven investment spend 90.1m 2025 (net -68.8m),L5,capex,Vlaanderen>Gemeenten>Leuven>invest,90090279,90090279,Strong; dual Brugge 84 Aalst 35,strong,src_leuven_jr2025,city infrastructure users,Expand city infrastructure,90.1m,4.5,7.0,5.0,5.5,Project ROI FOI,active,,tick841
lb_leuven_ocmw_aid_26m_2025,Leuven OCMW individual aid 26.5m 2025,L5,transfer,Vlaanderen>Gemeenten>Leuven>OCMW,26490508,26490508,Strong; +1.8m leefloon inflow,strong,src_leuven_jr2025,OCMW clients,Social assistance,26.5m,3.5,5.5,7.0,5.33,Outcomes FOI,active,,tick841 safety-net
lb_leuven_afm_22m_2025,Leuven AFM +21.6m BBR +18.8m 2025 (recovery from AFM 2.6m 2024),L5,ops,Vlaanderen>Gemeenten>Leuven>AFM,0,21590468,Strong recovery; Kreglinger escrow 11.2m reduces BBR,strong,src_leuven_jr2025,liquidity,Fiscal sustainability,AFM 21.6 BBR 18.8,4.0,6.0,4.0,4.67,Sustain path FOI,active,,tick841 positive
lb_dual_leuven_brugge_tick841,Dual Leuven 957m vs Brugge 1462m city residual,L5,ops,Belgium>dual>vl_cities,0,956966739,Strong dual not TE-additive,strong,src_dual_leuven_brugge_tick841,multi-channel,Dual residual map,primary,4.5,7.5,5.0,5.67,Cross FOI,active,,tick841
""".strip() + "\n"

cmt = f"""
cmt_leuven_balance_957m_2025,Leuven consol stad+OCMW balance YE2025 assets 957.0m,city_leuven,Stad en OCMW Leuven,BBC jaarrekening 2025 schema J4 GR 27.04.2026,2026-04-27,2025,2025,956966739,"{{""assets_m"": 956.967, ""equity_m"": 502.253, ""fin_debt_m"": 334.556, ""pension_prov_m"": 51.504, ""cash_m"": 14.843, ""kreglinger_escrow_m"": 11.206}}",0,active,https://leuven.be/sites/leuven.be/files/documents/2026-05/2025_Jaarrekening.pdf,Municipal consolidated BS,Publish debt+pension FOI,src_leuven_jr2025,strong,Vlaanderen>Gemeenten>Leuven>balance,tick841
cmt_leuven_expl_331m_2025,Leuven exploitation receipts 331.3m expenses 302.1m 2025,city_leuven,Stad en OCMW Leuven,BBC J2 2025,2025-12-31,2025,2025,331314507,"{{""expl_rec_m"": 331.315, ""expl_exp_m"": 302.104, ""expl_saldo_m"": 29.210, ""personnel_m"": 117.167, ""toelagen_m"": 96.286, ""fiscal_m"": 150.884}}",0,active,docs/doge/data/raw/leuven_jr2025.pdf,Large VL city exploitation stack,Named toelagen FOI,src_leuven_jr2025,strong,Vlaanderen>Gemeenten>Leuven>exploitation,tick841
cmt_leuven_afm_bbr_2025,Leuven AFM +21.6m and BBR +18.8m 2025,city_leuven,Fiscal sustainability indicators,BBC schema J2 2025,2025-12-31,2025,2025,18758606,"{{""afm_m"": 21.590, ""afm_corr_m"": 13.224, ""bbr_m"": 18.759, ""budget_result_m"": 42.718, ""new_loans_m"": 109.465}}",0,active,docs/doge/data/raw/leuven_jr2025.pdf,Strong AFM recovery; large new loans,Sustain path FOI,src_leuven_jr2025,strong,Vlaanderen>Gemeenten>Leuven>AFM,tick841
cmt_dual_leuven_brugge_tick841,Dual Leuven JR2025 vs Brugge JR2025 city residual,gg_belgium,dual map,Leuven JR2025 dual Brugge tick834,2026-08-05,2025,2025,956966739,"{{""leuven_assets_m"": 957.0, ""brugge_assets_m"": 1462.3, ""leuven_expl_m"": 331.3, ""brugge_expl_m"": 419.1, ""leuven_personnel_m"": 117.2, ""brugge_personnel_m"": 189.2}}",0,active,docs/doge/data/raw/leuven_jr2025.pdf,Dual residual map tick841,Cross FOI,src_dual_leuven_brugge_tick841,strong,Belgium>dual>vl_cities,tick841 not TE-additive
""".strip() + "\n"

src = """
src_leuven_jr2025,"Stad en OCMW Leuven Jaarrekening 2025 geconsolideerd (BBC, 132p, GR 27.04.2026)",https://leuven.be/sites/leuven.be/files/documents/2026-05/2025_Jaarrekening.pdf,Stad Leuven / OCMW Leuven,2026-08-05,entity_accounts,Strong tick841 primary: assets 957.0m equity 502.3m; expl 331.3/302.1 saldo +29.2m; AFM 21.6m BBR 18.8m; personnel 117.2m; toelagen 96.3m; fin debt 334.6m; pension 51.5m; invest 90.1m; new loans 109.5m; raw leuven_jr2025.pdf
src_dual_leuven_brugge_tick841,Dual Leuven JR2025 957m vs Brugge 1462m residual tick841,docs/doge/data/raw/leuven_jr2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: Leuven assets 957m expl 331m personnel 117m AFM +21.6m vs Brugge assets 1462m expl 419m personnel 189m
src_vub_jr2025_encoding_blocked,VUB Jaarrekening 2025 VL neerlegging PDF custom font Identity-H no ToUnicode (unreadable text extract),https://docs.vlaamsparlement.be/files/pfile?id=2321557,Vrije Universiteit Brussel / Departement FB,2026-08-05,entity_accounts,tick841 attempted extract 87p FlandersArtSans CID; residual FOI machine-readable; raw vub_jr2025.pdf retained
""".strip() + "\n"

ent_path = root / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
if "city_leuven," not in ent_text:
    with ent_path.open("a", encoding="utf-8", newline="") as f:
        f.write("city_leuven,Stad Leuven,Ville de Louvain,City of Leuven,municipality,vlaanderen_gov,nl,https://leuven.be,,Professor Van Overstraetenplein 1 3000 Leuven,JR2025 assets 957m expl 331m personnel 117m fin debt 335m; tick841\n")
else:
    lines = []
    for line in ent_text.splitlines():
        if line.startswith("city_leuven,") and "tick841" not in line:
            line = line.rstrip() + " | JR2025 assets 957m; tick841"
        lines.append(line)
    ent_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

foi = f'gap_leuven_debt_pension_subs_l5,Vlaanderen>Gemeenten>Leuven_L5,city_leuven,Full debt schedule by lender for fin debt 334.6m (KBC new loans 108m path); pension funding behind 51.5m; named toelagen matrix within 96.3m (Zorg Leuven/police/fire/EVA); Kreglinger escrow status 11.2m; MJP AFM path,957m city+OCMW with 335m fin debt and 96m toelagen blocks dual VL city ranking vs Brugge,7,Stad Leuven / financieel directeur / openbaarheid,,https://leuven.be,docs/doge/foi/drafts/gap_leuven_debt_pension_subs_l5.md,ready,2026-08-05,,,,,cmt_leuven_balance_957m_2025|cmt_leuven_expl_331m_2025|cmt_leuven_afm_bbr_2025,lb_leuven_personnel_117m_2025|lb_leuven_toelagen_96m_2025|lb_leuven_fin_debt_335m,2026-08-05T17:30:00Z,2026-08-05T17:30:00Z,tick841 primary JR2025; ready draft; do not send\n'
foi2 = 'gap_vub_jr2025_machine_readable_l5,Vlaanderen>Universiteiten>VUB_L5,vub,Machine-readable JR2025 VO neerlegging (current PDF FlandersArtSans Identity-H CID unreadable; 87p); J2/J4/J5 and 1st stream split like UA/UGent forms,Completes VL 5-uni statutory map after KUL/UH/UGent/UA fills; dual HE residual,7,Vrije Universiteit Brussel / AHOVOKS / Departement FB,,https://www.vub.be,docs/doge/foi/drafts/gap_vub_jr2025_machine_readable_l5.md,ready,2026-08-05,,,,,,2026-08-05T17:30:00Z,2026-08-05T17:30:00Z,tick841 extract failed font encoding; FOI text/CSV; do not send\n'

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_831,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UA JR2025 filled tick839; residual Roeselare/Leuven city or VUB JV or BELNET accounts or skeyes residual",,2026-08-05T16:30:00Z,2026-08-05T16:30:00Z,spawned tick839 after UA dual UGent'
new = 'rq_831,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UA JR2025 filled tick839; residual Roeselare/Leuven city or VUB JV or BELNET accounts or skeyes residual",gap_leuven_debt_pension_subs_l5,2026-08-05T16:30:00Z,2026-08-05T17:30:00Z,tick841 Leuven JR2025 assets 957m expl 331m personnel 117m fin debt 335m dual Brugge; VUB PDF encoding FOI; FOI ready'
if old not in text:
    raise SystemExit("rq_831 not found")
text = text.replace(old, new)
spawn = 'rq_832,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Leuven JR2025 filled tick841; VUB encoding FOI; residual Roeselare city or VUB machine-readable when available or BELNET/skeyes residual",,2026-08-05T17:30:00Z,2026-08-05T17:30:00Z,spawned tick841 after Leuven dual Brugge\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T17:30:00Z,rq_831,841,no,"
    "tick841 Leuven JR2025 dual Brugge; VUB FOI encoding; next rq_832 residual dual L5; progress@850 in 9; rq_116 deferred\n",
    encoding="utf-8",
)

for name, payload in [
    ("budgets.csv", budgets),
    ("leaderboard.csv", lb),
    ("commitments.csv", cmt),
    ("sources.csv", src),
    ("foi_queue.csv", foi + foi2),
]:
    with (root / name).open("a", encoding="utf-8", newline="") as f:
        f.write(payload)

doc = fitz.open("docs/doge/data/raw/leuven_jr2025.pdf")
pages = [32, 37, 38, 40, 47, 91]
with open("docs/doge/data/raw/leuven_jr2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("Leuven JR2025 key extract tick841\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick841 OK fin_debt=", FIN_DEBT)

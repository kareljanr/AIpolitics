# tick834 — Brugge JR2025 fill
from pathlib import Path
import fitz

root = Path("docs/doge/data")

# Fin debt = LT 136162394 + ST 45670655 + ST due 9881789
FIN_DEBT = 136162394 + 45670655 + 9881789  # 191714838

budgets = f"""
bud_brugge_assets_2025,city_brugge,2025,1462253952,,,stock,src_brugge_jr2025,strong,Consol stad+OCMW total assets YE2025 1462.254m (largest VL city BS found); tick834
bud_brugge_equity_2025,city_brugge,2025,1105315589,,,stock,src_brugge_jr2025,strong,Nettoactief YE2025 1105.316m (stad 1038.7 ocmw 66.6); tick834
bud_brugge_debt_total_2025,city_brugge,2025,356938363,,,stock,src_brugge_jr2025,strong,Total schulden YE2025 356.938m; tick834
bud_brugge_fin_debt_2025,city_brugge,2025,{FIN_DEBT},,,stock,src_brugge_jr2025,strong,Financiele schulden total YE2025 191.715m (LT 136.162 + ST 45.671 + ST due 9.882); tick834
bud_brugge_fin_debt_lt_2025,city_brugge,2025,136162394,,,stock,src_brugge_jr2025,strong,Financiele schulden LT YE2025 136.162m; tick834
bud_brugge_fin_debt_st_2025,city_brugge,2025,45670655,,,stock,src_brugge_jr2025,strong,Financiele schulden ST YE2025 45.671m (was 52.75m treasury); tick834
bud_brugge_lt_loans_kern_2025,city_brugge,2025,133800000,,,stock,src_brugge_jr2025,strong,Kerncijfers LT loans excl leasing 133.8m (stad 125.1 ocmw 8.6); tick834
bud_brugge_pension_prov_2025,city_brugge,2025,116226729,,,stock,src_brugge_jr2025,strong,Pensioenvoorzieningen LT YE2025 116.227m (was 111.785m); dual Genk 312.6m Mechelen 134.8m; tick834
bud_brugge_cash_2025,city_brugge,2025,36651428,,,stock,src_brugge_jr2025,strong,Liquide middelen YE2025 36.651m (was 59.926m); tick834
bud_brugge_cap_subs_2025,city_brugge,2025,55778861,,,stock,src_brugge_jr2025,strong,Kapitaalsubsidies YE2025 55.779m; tick834
bud_brugge_fva_igs_2025,city_brugge,2025,152020047,,,stock,src_brugge_jr2025,strong,Fin VA IGS 152.020m; tick834
bud_brugge_fva_other_2025,city_brugge,2025,540164050,,,stock,src_brugge_jr2025,strong,Andere FVA 540.164m (Port Antwerp-Bruges/MBZ ~538.7m class); tick834
bud_brugge_expl_rec_2025,city_brugge,2025,419083263,,,cash,src_brugge_jr2025,strong,Exploitatieontvangsten consol 419.083m; tick834
bud_brugge_expl_exp_2025,city_brugge,2025,380702498,,,cash,src_brugge_jr2025,strong,Exploitatieuitgaven consol 380.702m; tick834
bud_brugge_expl_saldo_2025,city_brugge,2025,38380765,,,cash,src_brugge_jr2025,strong,Exploitatiesaldo +38.381m; tick834
bud_brugge_invest_exp_2025,city_brugge,2025,84319077,,,cash,src_brugge_jr2025,strong,Investeringsuitgaven 84.319m; tick834
bud_brugge_invest_rec_2025,city_brugge,2025,21704947,,,cash,src_brugge_jr2025,strong,Investeringsontvangsten 21.705m; tick834
bud_brugge_invest_saldo_2025,city_brugge,2025,-62614130,,,cash,src_brugge_jr2025,strong,Investeringssaldo -62.614m; tick834
bud_brugge_fin_rec_2025,city_brugge,2025,32374255,,,cash,src_brugge_jr2025,strong,Financieringsontvangsten 32.374m; tick834
bud_brugge_fin_exp_2025,city_brugge,2025,9968567,,,cash,src_brugge_jr2025,strong,Financieringsuitgaven 9.969m; tick834
bud_brugge_afm_2025,city_brugge,2025,30771546,,,cash,src_brugge_jr2025,strong,Autofinancieringsmarge AFM +30.772m; tick834
bud_brugge_afm_corr_2025,city_brugge,2025,26185934,,,cash,src_brugge_jr2025,strong,Gecorrigeerde AFM +26.186m; tick834
bud_brugge_bbr_2025,city_brugge,2025,31966250,,,cash,src_brugge_jr2025,strong,Beschikbaar budgettair resultaat BBR 31.966m; tick834
bud_brugge_budget_result_2025,city_brugge,2025,-1827677,,,cash,src_brugge_jr2025,strong,Budgettair resultaat boekjaar -1.828m; tick834
bud_brugge_personnel_2025,city_brugge,2025,189200000,,,cash,src_brugge_jr2025,strong,Bruto personeelsuitgaven kerncijfers 189.2m (stad 150.9 ocmw 38.3; +2.7pct); tick834
bud_brugge_toelagen_2025,city_brugge,2025,95200000,,,cash,src_brugge_jr2025,strong,Toegestane werkingssubsidies kerncijfers 95.2m (stad 86.7 ocmw 8.6; -2.0pct); dual prior register ~98m; tick834
bud_brugge_fiscal_2025,city_brugge,2025,141900000,,,cash,src_brugge_jr2025,strong,Fiscale ontvangsten kerncijfers 141.9m (+5.6pct); tick834
bud_brugge_werk_subs_rec_2025,city_brugge,2025,200600000,,,cash,src_brugge_jr2025,strong,Ontvangen werkingssubsidies kerncijfers 200.6m (+4.2pct); tick834
bud_brugge_ocmw_cover_2025,city_brugge,2025,22200000,,,cash,src_brugge_jr2025,strong,Stedelijke bijdrage OCMW circa 22.2m (narrative; excl from stad/ocmw budget result split); tick834
bud_brugge_respo_prov_lt_2025,city_brugge,2025,67100000,,,stock,src_brugge_jr2025,strong,LT voorziening responsabiliseringsbijdrage stad ~67.1m YE2025 (narrative); tick834
""".strip() + "\n"

lb = f"""
lb_brugge_assets_1462m_2025,Brugge consol assets stock 1462m YE2025 (largest VL city BS),L5,stock,Vlaanderen>Gemeenten>Brugge>balance,0,1462253952,Strong primary; Port/MBZ FVA ~539m inflates assets; dual Aalst 617 Genk 629 Kortrijk 720,strong,src_brugge_jr2025,city/OCMW/port stake,Municipal consolidated wealth,1462m stock,4.5,8.5,5.0,6.0,Port stake dual FOI,active,,tick834 stock filtered from pure annual top10
lb_brugge_personnel_189m_2025,Brugge bruto personnel 189.2m 2025 (stad 150.9 ocmw 38.3),L5,ops,Vlaanderen>Gemeenten>Brugge>personnel,189200000,189200000,Strong kerncijfers; +2.7pct YoY; dual Aalst 139 Kortrijk 136 Mechelen 113,strong,src_brugge_jr2025,city/OCMW staff,Deliver local services,189.2m / +2.7pct,5.0,7.5,5.0,5.83,ETP productivity FOI,active,,tick834
lb_brugge_toelagen_95m_2025,Brugge granted operating subsidies 95.2m 2025,L5,subsidy,Vlaanderen>Gemeenten>Brugge>toelagen,95200000,95200000,Strong kerncijfers; dual prior open register ~98m; dual Mechelen ~90m Aalst 51m,strong,src_brugge_jr2025,police/Mintus/HVZ/culture partners,Fund safety zones and partners,95.2m / -2pct,5.5,7.2,5.0,5.9,Named matrix FOI vs register,active,,tick834
lb_brugge_fin_debt_192m,Brugge financial debt stock 191.7m YE2025,L5,stock,Vlaanderen>Gemeenten>Brugge>debt,9968567,191714838,Strong J4; LT 136.2 + ST 45.7 + ST due 9.9; kern LT loans excl lease 133.8m; dual Aalst 164 Genk 175 Kortrijk 258,strong,src_brugge_jr2025,lenders / infrastructure users,Finance invest 84.3m 2025,191.7m stock,5.0,7.2,5.5,5.9,Debt schedule FOI,active,,tick834 stock
lb_brugge_pension_prov_116m,Brugge pension provisions stock 116.2m YE2025,L5,stock,Vlaanderen>Gemeenten>Brugge>pensions,0,116226729,Strong; +4.4m YoY; respo LT provision stad ~67.1m within; dual Genk 313 Mechelen 135,strong,src_brugge_jr2025,statutory pensioners,Cover pension liabilities,116.2m stock,5.5,7.0,6.0,6.17,Funding path FOI,active,,tick834 stock
lb_brugge_invest_84m_2025,Brugge investment spend 84.3m 2025 (net -62.6m after 21.7m receipts),L5,capex,Vlaanderen>Gemeenten>Brugge>invest,84319077,84319077,Strong; largest invest among recent city fills dual Aalst 35 Genk 32 Kortrijk 57,strong,src_brugge_jr2025,city infrastructure users,Maintain and expand city infrastructure,84.3m,4.5,7.0,5.0,5.5,Project-level ROI FOI,active,,tick834
lb_brugge_ocmw_cover_22m_2025,Brugge city cover of OCMW ~22.2m 2025,L5,transfer,Vlaanderen>Gemeenten>Brugge>OCMW,22200000,22200000,Strong narrative circa 22.2m; dual Aalst 15.0m,strong,src_brugge_jr2025,OCMW Brugge / Mintus,Balance OCMW exploitation,22.2m city transfer,5.0,6.0,5.5,5.5,Exact multipjaar FOI,active,,tick834
lb_dual_brugge_aalst_genk_tick834,Dual Brugge 1462m vs Aalst 617m vs Genk 629m city residual,L5,ops,Belgium>dual>vl_cities,0,1462253952,Strong dual not TE-additive; Brugge Port stake inflates assets,strong,src_dual_brugge_aalst_genk_tick834,multi-channel,Dual residual map,primary,4.5,8.0,5.0,5.83,Cross FOI,active,,tick834
""".strip() + "\n"

cmt = f"""
cmt_brugge_balance_1462m_2025,Brugge consol stad+OCMW balance sheet YE2025 assets 1462m,city_brugge,Stad en OCMW Brugge,BBC jaarrekening 2025 boekdeel 2 schema J4,2026-07-02,2025,2025,1462253952,"{{""assets_m"": 1462.254, ""equity_m"": 1105.316, ""debt_total_m"": 356.938, ""fin_debt_m"": 191.715, ""pension_prov_m"": 116.227, ""cash_m"": 36.651, ""fva_port_class_m"": 538.7}}",0,active,https://www.brugge.be/stad-bestuur/bestuur/jaarrekening-stad-ocmw-brugge,Largest VL city BS found (Port FVA),Publish debt+pension FOI,src_brugge_jr2025,strong,Vlaanderen>Gemeenten>Brugge>balance,tick834 publ 2 jul 2026
cmt_brugge_expl_419m_2025,Brugge exploitation receipts 419.1m expenses 380.7m 2025,city_brugge,Stad en OCMW Brugge,BBC J2 2025,2025-12-31,2025,2025,419083263,"{{""expl_rec_m"": 419.083, ""expl_exp_m"": 380.702, ""expl_saldo_m"": 38.381, ""personnel_m"": 189.2, ""toelagen_m"": 95.2, ""fiscal_m"": 141.9, ""werk_subs_rec_m"": 200.6}}",0,active,docs/doge/data/raw/brugge_jr2025_bd2.pdf,Largest VL city exploitation stack in recent fills,Named toelagen matrix FOI,src_brugge_jr2025,strong,Vlaanderen>Gemeenten>Brugge>exploitation,tick834
cmt_brugge_afm_bbr_2025,Brugge AFM +30.8m and BBR +32.0m 2025,city_brugge,Fiscal sustainability indicators,BBC schema J2 2025,2025-12-31,2025,2025,31966250,"{{""afm_m"": 30.772, ""afm_corr_m"": 26.186, ""bbr_m"": 31.966, ""budget_result_m"": -1.828, ""expl_saldo_m"": 38.381}}",0,active,docs/doge/data/raw/brugge_jr2025_bd2.pdf,Strong AFM and BBR; invest 84m,Sustain AFM path FOI MJP,src_brugge_jr2025,strong,Vlaanderen>Gemeenten>Brugge>AFM,tick834
cmt_dual_brugge_aalst_genk_tick834,Dual Brugge JR2025 vs Aalst vs Genk city residual,gg_belgium,dual map,Brugge JR2025 dual prior city fills,2026-08-05,2025,2025,1462253952,"{{""brugge_assets_m"": 1462.3, ""aalst_assets_m"": 616.5, ""genk_assets_m"": 628.7, ""brugge_expl_m"": 419.1, ""brugge_personnel_m"": 189.2, ""brugge_toelagen_m"": 95.2}}",0,active,docs/doge/data/raw/brugge_jr2025_bd2.pdf,Dual residual map tick834,Cross FOI city L5,src_dual_brugge_aalst_genk_tick834,strong,Belgium>dual>vl_cities,tick834 not TE-additive
""".strip() + "\n"

src = """
src_brugge_jr2025,"Stad en OCMW Brugge Geconsolideerde Jaarrekening 2025 boekdeel 2 (BBC, 310p, publ. 2 jul 2026)",https://www.brugge.be/sites/default/files/2026-07/Jaarrekening%202025%20boekdeel%202.pdf,Stad Brugge / OCMW Brugge,2026-08-05,entity_accounts,Strong tick834 primary: consol assets 1462.3m equity 1105.3m; expl ontvangsten 419.1m uitgaven 380.7m saldo +38.4m; AFM 30.8m BBR 32.0m; personnel 189.2m; fin debt 191.7m; pension prov 116.2m; toelagen 95.2m; invest 84.3m; OCMW cover ~22.2m; Port FVA ~539m; raw brugge_jr2025_bd2.pdf
src_dual_brugge_aalst_genk_tick834,Dual Brugge JR2025 1462m vs Aalst 617m vs Genk 629m residual tick834,docs/doge/data/raw/brugge_jr2025_bd2.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: Brugge assets 1462m expl 419m personnel 189m toelagen 95m AFM +30.8m vs Aalst assets 617m expl 276m vs Genk assets 629m pension 313m
""".strip() + "\n"

# update entity notes for city_brugge
ent_path = root / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
old_ent = "city_brugge,Stad Brugge,Ville de Bruges,City of Bruges,local,sec_local,nl,https://www.brugge.be,,,Open subsidieregister: 2024 total 99.3m; Brugge Plus 7.3m; Concertgebouw 2.1m; Entrepot 1.1m; tick102"
new_ent = "city_brugge,Stad Brugge,Ville de Bruges,City of Bruges,municipality,vlaanderen_gov,nl,https://www.brugge.be,,Burg 12 8000 Brugge,JR2025 assets 1462m expl 419m personnel 189m toelagen 95m fin debt 192m; prior register tick102; tick834"
if old_ent in ent_text:
    ent_text = ent_text.replace(old_ent, new_ent)
    ent_path.write_text(ent_text, encoding="utf-8")
else:
    # append note if structure differs
    if "JR2025 assets 1462m" not in ent_text:
        with ent_path.open("a", encoding="utf-8", newline="") as f:
            f.write("\n")  # ensure

foi = f'gap_brugge_debt_pension_subs_l5,Vlaanderen>Gemeenten>Brugge_L5,city_brugge,Full debt schedule by lender for fin debt 191.7m (LT/ST/lease split); pension+respo funding path behind 116.2m provisions (respo LT ~67.1m); named toelagen matrix within 95.2m reconciling open register; OCMW cover multipjaar path (~22.2m 2025); ETP behind 189.2m personnel,"1462m city+OCMW book (Port FVA) with 419m exploitation, 189m personnel and 95m toelagen blocks dual VL city waste ranking",7,Stad Brugge / financieel directeur / openbaarheid van bestuur,,https://www.brugge.be,docs/doge/foi/drafts/gap_brugge_debt_pension_subs_l5.md,ready,2026-08-05,,,,,cmt_brugge_balance_1462m_2025|cmt_brugge_expl_419m_2025|cmt_brugge_afm_bbr_2025,lb_brugge_personnel_189m_2025|lb_brugge_toelagen_95m_2025|lb_brugge_fin_debt_192m|lb_brugge_pension_prov_116m,2026-08-05T14:00:00Z,2026-08-05T14:00:00Z,tick834 primary JR2025 bd2; ready draft; do not send\n'

# research_queue
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_824,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Aalst JR2025 filled tick833; residual Roeselare/Hasselt city or BELNET AR2025 accounts or skeyes residual",,2026-08-05T13:30:00Z,2026-08-05T13:30:00Z,spawned tick833 after Aalst dual Genk/Kortrijk'
new = 'rq_824,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Aalst JR2025 filled tick833; residual Roeselare/Hasselt city or BELNET AR2025 accounts or skeyes residual",gap_brugge_debt_pension_subs_l5,2026-08-05T13:30:00Z,2026-08-05T14:00:00Z,tick834 Brugge JR2025 assets 1462m expl 419m personnel 189m AFM 30.8m fin debt 192m toelagen 95m dual Aalst/Genk; FOI ready'
if old not in text:
    raise SystemExit("rq_824 row not found")
text = text.replace(old, new)
spawn = 'rq_825,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Brugge JR2025 filled tick834; residual Roeselare/Hasselt city or BELNET AR2025 accounts or skeyes residual",,2026-08-05T14:00:00Z,2026-08-05T14:00:00Z,spawned tick834 after Brugge dual Aalst/Genk\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T14:00:00Z,rq_824,834,no,"
    "tick834 Brugge JR2025 dual Aalst/Genk; next rq_825 residual dual L5; progress@840 in 6; rq_116 deferred\n",
    encoding="utf-8",
)

for name, payload in [
    ("budgets.csv", budgets),
    ("leaderboard.csv", lb),
    ("commitments.csv", cmt),
    ("sources.csv", src),
    ("foi_queue.csv", foi),
]:
    with (root / name).open("a", encoding="utf-8", newline="") as f:
        f.write(payload)

# extract
doc = fitz.open("docs/doge/data/raw/brugge_jr2025_bd2.pdf")
pages = [9, 10, 13, 14, 37, 38, 39, 48]
with open("docs/doge/data/raw/brugge_jr2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("Brugge JR2025 bd2 key extract tick834\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick834 CSV updates OK fin_debt=", FIN_DEBT)

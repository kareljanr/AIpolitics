# tick836 — UHasselt financieel JV2025 fill
from pathlib import Path
import fitz

root = Path("docs/doge/data")

# Fin debt = LT 2.6m + ST due 2.6m = 5.2m
FIN_DEBT = 2600000 + 2600000

budgets = f"""
bud_uhasselt_assets_2025,uhasselt,2025,281294559,,,stock,src_uhasselt_jv2025,strong,Total assets YE2025 281.295m (was 284.494m); tick836
bud_uhasselt_equity_2025,uhasselt,2025,240044415,,,stock,src_uhasselt_jv2025,strong,Eigen vermogen YE2025 240.044m; tick836
bud_uhasselt_cap_subs_2025,uhasselt,2025,41487233,,,stock,src_uhasselt_jv2025,strong,Kapitaalsubsidies YE2025 41.487m; tick836
bud_uhasselt_bestemde_fondsen_2025,uhasselt,2025,198557182,,,stock,src_uhasselt_jv2025,strong,Bestemde fondsen YE2025 198.557m; tick836
bud_uhasselt_debt_total_2025,uhasselt,2025,40906144,,,stock,src_uhasselt_jv2025,strong,Total schulden YE2025 40.906m; tick836
bud_uhasselt_fin_debt_2025,uhasselt,2025,{FIN_DEBT},,,stock,src_uhasselt_jv2025,strong,Financiele schulden LT 2.6m + ST due 2.6m = 5.2m YE2025; tick836
bud_uhasselt_fin_debt_lt_2025,uhasselt,2025,2600000,,,stock,src_uhasselt_jv2025,strong,Financiele schulden LT kredietinstellingen YE2025 2.6m (was 5.2m); tick836
bud_uhasselt_cash_2025,uhasselt,2025,10892977,,,stock,src_uhasselt_jv2025,strong,Liquide middelen YE2025 10.893m; tick836
bud_uhasselt_geldbeleggingen_2025,uhasselt,2025,107816109,,,stock,src_uhasselt_jv2025,strong,Geldbeleggingen YE2025 107.816m; tick836
bud_uhasselt_cash_beleg_2025,uhasselt,2025,118709086,,,stock,src_uhasselt_jv2025,strong,Cash+beleggingen YE2025 118.709m (was 139.537m); tick836
bud_uhasselt_mva_2025,uhasselt,2025,142419117,,,stock,src_uhasselt_jv2025,strong,Materiele vaste activa YE2025 142.419m; tick836
bud_uhasselt_bedrijfsopbr_2025,uhasselt,2025,172383060,,,cash,src_uhasselt_jv2025,strong,Bedrijfsopbrengsten 172.383m (+6.9pct YoY); tick836
bud_uhasselt_1st_stream_2025,uhasselt,2025,96769951,,,cash,src_uhasselt_jv2025,strong,1ste geldstroom basisfinanciering 96.770m STRONG (upgrades 2024 medium implied 93.8m); tick836
bud_uhasselt_werking_2025,uhasselt,2025,90872400,,,cash,src_uhasselt_jv2025,strong,Werkingsuitkeringen 90.872m within 1st stream; tick836
bud_uhasselt_invest_uitkering_2025,uhasselt,2025,2177550,,,cash,src_uhasselt_jv2025,strong,Investeringsuitkeringen 2.178m within 1st stream; tick836
bud_uhasselt_2nd_stream_2025,uhasselt,2025,17588240,,,cash,src_uhasselt_jv2025,strong,2de geldstroom fundamenteel onderzoek 17.588m (BOF 10.734 FWO/VLAIO 6.854); tick836
bud_uhasselt_3rd_stream_2025,uhasselt,2025,25279723,,,cash,src_uhasselt_jv2025,strong,3de geldstroom toegepast onderzoek 25.280m; tick836
bud_uhasselt_4th_stream_2025,uhasselt,2025,5649789,,,cash,src_uhasselt_jv2025,strong,4de geldstroom contractonderzoek prive 5.650m; tick836
bud_uhasselt_tuition_2025,uhasselt,2025,6056691,,,cash,src_uhasselt_jv2025,strong,Reguliere inschrijvingsgelden 6.057m; tick836
bud_uhasselt_bedrijfskosten_2025,uhasselt,2025,169865940,,,cash,src_uhasselt_jv2025,strong,Bedrijfskosten 169.866m; tick836
bud_uhasselt_bezold_2025,uhasselt,2025,118451749,,,cash,src_uhasselt_jv2025,strong,Bezoldigingen 118.452m (+6.5pct; ZAP 26.6 AAP 12.3 ATP 18.1 bursalen 19.9); tick836
bud_uhasselt_diensten_2025,uhasselt,2025,39684479,,,cash,src_uhasselt_jv2025,strong,Diensten en diverse goederen 39.684m; tick836
bud_uhasselt_afschr_2025,uhasselt,2025,11265174,,,cash,src_uhasselt_jv2025,strong,Afschrijvingen 11.265m; tick836
bud_uhasselt_bedrijfs_2025,uhasselt,2025,2517120,,,cash,src_uhasselt_jv2025,strong,Bedrijfsoverschot 2.517m (was 1.041m 2024); tick836
bud_uhasselt_result_2025,uhasselt,2025,5605805,,,cash,src_uhasselt_jv2025,strong,Overschot boekjaar 5.606m (was 9.543m 2024 CRC strong); tick836
bud_uhasselt_invest_2025,uhasselt,2025,25822201,,,cash,src_uhasselt_jv2025,strong,Netto investeringen 25.822m (+69pct vs 15.227m 2024); tick836
bud_uhasselt_aflossing_2025,uhasselt,2025,2600000,,,cash,src_uhasselt_jv2025,strong,Aflossingen leningen 2.6m; tick836
bud_uhasselt_fin_costs_2025,uhasselt,2025,1829167,,,cash,src_uhasselt_jv2025,strong,Financiele kosten 1.829m; tick836
bud_uhasselt_1st_stream_2024_jv,uhasselt,2024,94039518,,,outturn,src_uhasselt_jv2025,strong,1ste geldstroom 2024 from JV comparative 94.040m (was medium implied 93.828m CRC); tick836 upgrade
""".strip() + "\n"

lb = f"""
lb_uhasselt_1st_97m_2025,UHasselt 1st stream basisfinanciering 96.8m 2025 strong,L5,subsidy,Vlaanderen>Universiteiten>UHasselt>1st_stream,96769951,96769951,Strong primary JV RvB 19.03.2026; werkingsuitkering 90.9m within; dual CRC 2024 medium 93.8m upgraded,strong,src_uhasselt_jv2025,students/staff,Public HE operating grant,96.8m / +2.9pct YoY,4.0,7.0,5.0,5.33,AHOVOKS open matrix FOI residual sector,active,,tick836 closes gap_univ partial
lb_uhasselt_bezold_118m_2025,UHasselt bezoldigingen 118.5m 2025,L5,ops,Vlaanderen>Universiteiten>UHasselt>personnel,118451749,118451749,Strong; +6.5pct YoY; bursalen 19.9m within; dual CRC VTE 1494 2024,strong,src_uhasselt_jv2025,academic/admin staff,Deliver HE teaching and research,118.5m / 69pct of bedrijfskosten,5.0,7.0,5.0,5.67,ETP productivity FOI,active,,tick836
lb_uhasselt_invest_26m_2025,UHasselt CAPEX invest 25.8m 2025,L5,capex,Vlaanderen>Universiteiten>UHasselt>invest,25822201,25822201,Strong liquidity table; +69pct YoY; dual CoA HE debt draw 50m 2026 path,strong,src_uhasselt_jv2025,campus users,Campus infrastructure expansion,25.8m / path to 50m debt draw FOI,4.5,6.5,5.5,5.5,Purpose L5 dual gap_vl_ba2026_he_debt,active,,tick836
lb_uhasselt_cash_beleg_119m,UHasselt cash+beleggingen stock 118.7m YE2025 (-20.8m YoY),L5,stock,Vlaanderen>Universiteiten>UHasselt>liquidity,0,118709086,Strong; invest 25.8m + working capital drawdown; not pure annual waste,strong,src_uhasselt_jv2025,university treasury,Buffer for multi-year campus plan,118.7m stock / -20.8m,3.5,6.5,5.0,5.0,Treasury policy FOI,active,,tick836 stock
lb_dual_uhasselt_crc_tick836,Dual UHasselt JV2025 strong 1st 96.8m vs CRC 2024 medium residual,L5,ops,Belgium>dual>vl_universities,96769951,96769951,Strong dual upgrades prior medium implied; residual AHOVOKS exact multi-year FOI,strong,src_dual_uhasselt_crc_tick836,HE multi-channel,Dual residual map,primary,4.0,6.5,5.0,5.17,Cross FOI,active,,tick836
""".strip() + "\n"

cmt = f"""
cmt_uhasselt_balance_281m_2025,UHasselt balance sheet YE2025 assets 281.3m equity 240.0m,uhasselt,Universiteit Hasselt,Financieel jaarverslag 2025 RvB 19.03.2026,2026-03-19,2025,2025,281294559,"{{""assets_m"": 281.295, ""equity_m"": 240.044, ""cap_subs_m"": 41.487, ""fin_debt_m"": 5.2, ""cash_beleg_m"": 118.709, ""mva_m"": 142.419}}",0,active,https://www.uhasselt.be/media/pxaaourh/financieel-jaarverslag-2025-totaal.pdf,University statutory balance sheet,Publish multi-year debt path dual 50m 2026 FOI,src_uhasselt_jv2025,strong,Vlaanderen>Universiteiten>UHasselt>balance,tick836
cmt_uhasselt_1st_stream_2025,UHasselt 1st stream basisfinanciering 96.8m 2025 strong,uhasselt,Universiteit Hasselt / AHOVOKS,JV2025 resultatenrekening code 700,2025-12-31,2025,2025,96769951,"{{""1st_m"": 96.770, ""werking_m"": 90.872, ""invest_uitk_m"": 2.178, ""sociaal_m"": 1.563, ""other_m"": 2.157, ""2024_1st_m"": 94.040}}",0,active,docs/doge/data/raw/uhasselt_financieel_jv2025.pdf,Public HE first-stream grant exact,Open AHOVOKS matrix sector FOI,src_uhasselt_jv2025,strong,Vlaanderen>Universiteiten>UHasselt>1st_stream,tick836 upgrades cmt_uhasselt_1st_stream_2024 medium
cmt_uhasselt_result_path_2024_25,UHasselt result path 9.54m 2024 to 5.61m 2025,uhasselt,Universiteit Hasselt,JV2025 comparative,2025-12-31,2024,2025,5605805,"{{""result_2024_m"": 9.543, ""result_2025_m"": 5.606, ""bedrijfs_2025_m"": 2.517, ""bezold_2025_m"": 118.452, ""invest_2025_m"": 25.822}}",0,active,docs/doge/data/raw/uhasselt_financieel_jv2025.pdf,Lower result after invest surge,Publish cost drivers FOI,src_uhasselt_jv2025,strong,Vlaanderen>Universiteiten>UHasselt>result,tick836
cmt_dual_uhasselt_crc_tick836,Dual UHasselt JV2025 strong vs CRC 2024 medium residual,gg_belgium,dual map,UHasselt JV2025 dual CRC tick163,2026-08-05,2024,2025,96769951,"{{""1st_2025_strong_m"": 96.770, ""1st_2024_jv_m"": 94.040, ""1st_2024_crc_implied_m"": 93.828, ""result_2025_m"": 5.606, ""result_2024_m"": 9.543}}",0,active,docs/doge/data/raw/uhasselt_financieel_jv2025.pdf,Dual residual map tick836,Cross FOI HE,src_dual_uhasselt_crc_tick836,strong,Belgium>dual>vl_universities,tick836 not TE-additive
""".strip() + "\n"

src = """
src_uhasselt_jv2025,"Universiteit Hasselt Financieel jaarverslag 2025 (RvB 19.03.2026, 91p)",https://www.uhasselt.be/media/pxaaourh/financieel-jaarverslag-2025-totaal.pdf,Universiteit Hasselt,2026-08-05,entity_accounts,Strong tick836 primary: assets 281.3m equity 240.0m; bedrijfsopbr 172.4m; 1st stream 96.8m strong; bezold 118.5m; result 5.61m; invest 25.8m; fin debt 5.2m; cash+beleg 118.7m; raw uhasselt_financieel_jv2025.pdf
src_dual_uhasselt_crc_tick836,Dual UHasselt JV2025 1st 96.8m strong vs CRC 2024 residual tick836,docs/doge/data/raw/uhasselt_financieel_jv2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual: JV upgrades 1st stream from medium CRC reverse-engineer; residual AHOVOKS multi-year matrix + 50m 2026 debt purpose FOI
""".strip() + "\n"

# update entity
ent_path = root / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
old_ent = "uhasselt,Universiteit Hasselt,Universite de Hasselt,Hasselt University,university,sec_flanders,nl,https://www.uhasselt.be,,,CRC 2024: result +9.5m; students 7303; VTE 1494; implied 1st ~94m medium; tick163"
new_ent = "uhasselt,Universiteit Hasselt,Universite de Hasselt,Hasselt University,university,sec_flanders,nl,https://www.uhasselt.be,financien@uhasselt.be,,JV2025: assets 281m 1st 96.8m strong bezold 118m result 5.6m invest 26m; CRC 2024 residual; tick836"
if old_ent in ent_text:
    ent_path.write_text(ent_text.replace(old_ent, new_ent), encoding="utf-8")

foi = 'gap_uhasselt_debt_ahovoks_l5,Vlaanderen>Universiteiten>UHasselt_L5,uhasselt,AHOVOKS exact multi-year werkingsuitkering path 2023-2027 reconciling JV 1st 96.8m 2025; purpose+amort of CoA 50m debt draw 2026; ETP matrix behind 118.5m bezold; campus CAPEX project L5 within 25.8m invest 2025,Strong JV fills annual BS/P&L but multi-year AHOVOKS matrix and 50m debt purpose still residual dual gap_univ_per_institution + gap_vl_ba2026_he_debt,6,Universiteit Hasselt / AHOVOKS / openbaarheid Vlaanderen,financien@uhasselt.be,https://www.uhasselt.be,docs/doge/foi/drafts/gap_uhasselt_debt_ahovoks_l5.md,ready,2026-08-05,,,,,cmt_uhasselt_1st_stream_2025|cmt_uhasselt_balance_281m_2025|cmt_vl_he_debt_draws_named_104_9m,lb_uhasselt_1st_97m_2025|lb_uhasselt_bezold_118m_2025|lb_uhasselt_invest_26m_2025,2026-08-05T15:00:00Z,2026-08-05T15:00:00Z,tick836 JV2025 primary strong 1st stream; residual multi-year FOI; do not send\n'

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_826,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Tielt JR2025 filled tick835; Hasselt scan FOI; residual Roeselare/Leuven city or UHasselt JV2025 or BELNET accounts or skeyes residual",,2026-08-05T14:30:00Z,2026-08-05T14:30:00Z,spawned tick835 after Tielt dual Brugge'
new = 'rq_826,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; Tielt JR2025 filled tick835; Hasselt scan FOI; residual Roeselare/Leuven city or UHasselt JV2025 or BELNET accounts or skeyes residual",gap_uhasselt_debt_ahovoks_l5,2026-08-05T14:30:00Z,2026-08-05T15:00:00Z,tick836 UHasselt JV2025 assets 281m 1st 96.8m strong bezold 118m result 5.6m invest 26m dual CRC; FOI ready'
if old not in text:
    raise SystemExit("rq_826 not found")
text = text.replace(old, new)
spawn = 'rq_827,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UHasselt JV2025 filled tick836; residual Roeselare/Leuven city or BELNET accounts or skeyes residual or other uni JV",,2026-08-05T15:00:00Z,2026-08-05T15:00:00Z,spawned tick836 after UHasselt dual CRC\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T15:00:00Z,rq_826,836,no,"
    "tick836 UHasselt JV2025 dual CRC; next rq_827 residual dual L5; progress@840 in 4; rq_116 deferred\n",
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

doc = fitz.open("docs/doge/data/raw/uhasselt_financieel_jv2025.pdf")
pages = [2, 3, 4, 5, 6, 24]
with open("docs/doge/data/raw/uhasselt_jv2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("UHasselt JV2025 key extract tick836\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick836 OK")

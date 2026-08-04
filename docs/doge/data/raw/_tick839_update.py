# tick839 — UA Jaarrekening 2025 VL neerlegging (kEUR ×1000)
from pathlib import Path
import fitz

root = Path("docs/doge/data")

def k(x):
    return int(round(float(str(x).replace(".", "").replace(",", ".")) if False else x)) * 1000

# amounts already integers in kEUR from PDF (European thousands dots are thousand separators)
def keur(n):
    return int(n) * 1000

FIN_DEBT = keur(6961) + keur(584)

budgets = f"""
bud_ua_assets_2025,ua,2025,{keur(647203)},,,stock,src_ua_jr2025,strong,Total assets YE2025 647.203m (VL neerlegging kEUR); tick839
bud_ua_equity_2025,ua,2025,{keur(483032)},,,stock,src_ua_jr2025,strong,Eigen vermogen YE2025 483.032m; tick839
bud_ua_reserves_2025,ua,2025,{keur(457502)},,,stock,src_ua_jr2025,strong,Reserves/wettelijke YE2025 457.502m (was 393.602m); tick839
bud_ua_cap_subs_2025,ua,2025,{keur(25530)},,,stock,src_ua_jr2025,strong,Kapitaalsubsidies YE2025 25.530m; tick839
bud_ua_debt_total_2025,ua,2025,{keur(154397)},,,stock,src_ua_jr2025,strong,Total schulden YE2025 154.397m; tick839
bud_ua_fin_debt_2025,ua,2025,{FIN_DEBT},,,stock,src_ua_jr2025,strong,Fin schulden LT 6.961 + ST due 0.584 = 7.545m YE2025; tick839
bud_ua_fin_debt_lt_2025,ua,2025,{keur(6961)},,,stock,src_ua_jr2025,strong,Fin schulden LT overige leningen YE2025 6.961m; tick839
bud_ua_provisions_2025,ua,2025,{keur(9774)},,,stock,src_ua_jr2025,strong,Voorzieningen YE2025 9.774m; tick839
bud_ua_pension_prov_2025,ua,2025,{keur(4500)},,,stock,src_ua_jr2025,strong,Pensioenvoorzieningen YE2025 4.500m; tick839
bud_ua_cash_2025,ua,2025,{keur(119872)},,,stock,src_ua_jr2025,strong,Liquide middelen YE2025 119.872m; tick839
bud_ua_geldbeleggingen_2025,ua,2025,{keur(205926)},,,stock,src_ua_jr2025,strong,Geldbeleggingen YE2025 205.926m; tick839
bud_ua_cash_beleg_2025,ua,2025,{keur(119872+205926)},,,stock,src_ua_jr2025,strong,Cash+beleggingen YE2025 325.798m; tick839
bud_ua_mva_2025,ua,2025,{keur(252712)},,,stock,src_ua_jr2025,strong,Materiele vaste activa YE2025 252.712m; tick839
bud_ua_bedrijfsopbr_2025,ua,2025,{keur(470696)},,,cash,src_ua_jr2025,strong,Bedrijfsopbrengsten 470.696m; 1st stream not split VO form FOI; tick839
bud_ua_omzet_2025,ua,2025,{keur(423198)},,,cash,src_ua_jr2025,strong,Omzet 423.198m; tick839
bud_ua_bedrijfskosten_2025,ua,2025,{keur(469756)},,,cash,src_ua_jr2025,strong,Bedrijfskosten 469.756m; tick839
bud_ua_bezold_2025,ua,2025,{keur(314922)},,,cash,src_ua_jr2025,strong,Bezoldigingen 314.922m (+4.0pct vs 302.915m); tick839
bud_ua_diensten_2025,ua,2025,{keur(101244)},,,cash,src_ua_jr2025,strong,Diensten en diverse goederen 101.244m; tick839
bud_ua_afschr_2025,ua,2025,{keur(25340)},,,cash,src_ua_jr2025,strong,Afschrijvingen 25.340m (was 54.163m); tick839
bud_ua_bedrijfs_2025,ua,2025,{keur(940)},,,cash,src_ua_jr2025,strong,Bedrijfsresultaat +0.940m (was -23.393m); tick839
bud_ua_result_2025,ua,2025,{keur(-5039)},,,cash,src_ua_jr2025,strong,Resultaat boekjaar -5.039m (was +2.373m CRC 2024 match); tick839
bud_ua_fin_opbr_2025,ua,2025,{keur(11601)},,,cash,src_ua_jr2025,strong,Financiele opbrengsten 11.601m; tick839
bud_ua_fin_costs_2025,ua,2025,{keur(17580)},,,cash,src_ua_jr2025,strong,Financiele kosten 17.580m; tick839
bud_ua_project_prepay_2025,ua,2025,{keur(74249)},,,stock,src_ua_jr2025,strong,Ontvangen vooruitbetalingen YE2025 74.249m; tick839
bud_ua_result_2024_jv,ua,2024,{keur(2373)},,,outturn,src_ua_jr2025,strong,Resultaat 2024 +2.373m (matches CRC 2024 +2.4m); tick839
""".strip() + "\n"

lb = f"""
lb_ua_bezold_315m_2025,UA bezoldigingen 314.9m 2025,L5,ops,Vlaanderen>Universiteiten>UA>personnel,314922000,314922000,Strong VL neerlegging; dual UGent 667 KUL 917 UH 118,strong,src_ua_jr2025,academic/admin staff,Deliver HE teaching and research,314.9m,5.0,7.0,5.0,5.67,ETP FOI; 1st stream split FOI,active,,tick839
lb_ua_result_minus_5m_2025,UA result -5.0m 2025 (from +2.4m 2024),L5,ops,Vlaanderen>Universiteiten>UA>result,-5039000,5039000,Strong; fin costs 17.6m > fin opbr 11.6m; dual UGent +62m,strong,src_ua_jr2025,university,Annual result, -5.0m loss,5.0,5.5,5.0,5.17,Driver FOI,active,,tick839
lb_ua_cash_beleg_326m,UA cash+beleggingen stock 325.8m YE2025,L5,stock,Vlaanderen>Universiteiten>UA>liquidity,0,325798000,Strong; dual UGent 703 KUL 2357; stock not pure annual waste,strong,src_ua_jr2025,university treasury,Multi-year buffer,325.8m stock,3.5,6.5,5.0,5.0,Treasury FOI,active,,tick839 stock
lb_ua_omzet_423m_2025,UA omzet 423.2m 2025 (1st stream opaque in VO form),L5,ops,Vlaanderen>Universiteiten>UA>omzet,423198000,423198000,Strong aggregate; dual CRC 2024 1st medium 206.9m residual exact FOI,strong,src_ua_jr2025,students/research funders,HE operating revenue stack,423.2m / stream FOI,4.5,7.0,5.5,5.67,AHOVOKS 1st FOI,active,,tick839
lb_dual_ua_ugent_tick839,Dual UA assets 647m vs UGent 1376m residual,L5,ops,Belgium>dual>vl_universities,0,647203000,Strong dual not TE-additive; both VO form 1st stream residual,strong,src_dual_ua_ugent_tick839,HE multi-channel,Dual residual map,primary,4.0,7.5,5.0,5.5,Cross FOI,active,,tick839
""".strip() + "\n"

cmt = f"""
cmt_ua_balance_647m_2025,UA balance sheet YE2025 assets 647.2m equity 483.0m,ua,Universiteit Antwerpen,VL neerlegging jaarrekening 2025 AV 31.03.2026,2026-03-31,2025,2025,{keur(647203)},"{{""assets_m"": 647.203, ""equity_m"": 483.032, ""cash_beleg_m"": 325.798, ""fin_debt_m"": 7.545, ""bezold_m"": 314.922, ""result_m"": -5.039}}",0,active,https://docs.vlaamsparlement.be/files/pfile?id=2321554,UA statutory BS kEUR form,Publish 1st stream split FOI,src_ua_jr2025,strong,Vlaanderen>Universiteiten>UA>balance,tick839 amounts kEUR×1000
cmt_ua_result_path_2024_25,UA result path +2.4m 2024 to -5.0m 2025,ua,Universiteit Antwerpen,VL neerlegging comparative,2025-12-31,2024,2025,{keur(-5039)},"{{""result_2024_m"": 2.373, ""result_2025_m"": -5.039, ""bedrijfs_2025_m"": 0.940, ""bezold_2025_m"": 314.922, ""omzet_2025_m"": 423.198}}",0,active,docs/doge/data/raw/ua_jr2025.pdf,Loss year after CRC 2024 small surplus,Publish cost drivers FOI,src_ua_jr2025,strong,Vlaanderen>Universiteiten>UA>result,tick839
cmt_dual_ua_ugent_tick839,Dual UA JR2025 vs UGent JR2025 residual,gg_belgium,dual map,UA JR2025 dual UGent tick838,2026-08-05,2025,2025,{keur(647203)},"{{""ua_assets_m"": 647.2, ""ugent_assets_m"": 1375.8, ""ua_bezold_m"": 314.9, ""ugent_bezold_m"": 666.6, ""ua_result_m"": -5.0, ""ugent_result_m"": 61.9}}",0,active,docs/doge/data/raw/ua_jr2025.pdf,Dual residual map tick839,Cross FOI HE,src_dual_ua_ugent_tick839,strong,Belgium>dual>vl_universities,tick839 not TE-additive
""".strip() + "\n"

src = """
src_ua_jr2025,"Universiteit Antwerpen Jaarrekening 2025 VL neerleggingsformulier (AV 31.03.2026, 38p, amounts kEUR)",https://docs.vlaamsparlement.be/files/pfile?id=2321554,Universiteit Antwerpen / Departement FB,2026-08-05,entity_accounts,Strong tick839 primary: assets 647.2m equity 483.0m; omzet 423.2m; bezold 314.9m; result -5.0m (was +2.4m); cash+beleg 325.8m; fin debt 7.5m; 1st stream NOT split VO model FOI; raw ua_jr2025.pdf
src_dual_ua_ugent_tick839,Dual UA JR2025 647m vs UGent 1376m residual tick839,docs/doge/data/raw/ua_jr2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: UA assets 647m bezold 315m result -5m vs UGent assets 1376m bezold 667m result +62m
""".strip() + "\n"

ent_path = root / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
if "ua," in ent_text or ",Universiteit Antwerpen," in ent_text:
    lines = ent_text.splitlines()
    out = []
    for line in lines:
        if (line.startswith("ua,") or "Universiteit Antwerpen" in line.split(",")[1] if len(line.split(","))>1 else False) and "tick839" not in line:
            if line.startswith("ua,") or line.startswith("uantwerpen,"):
                line = line.rstrip() + " | JR2025 assets 647m result -5m bezold 315m; tick839"
        out.append(line)
    ent_path.write_text("\n".join(out) + ("\n" if ent_text.endswith("\n") else ""), encoding="utf-8")
else:
    with ent_path.open("a", encoding="utf-8", newline="") as f:
        f.write("ua,Universiteit Antwerpen,Universite d'Anvers,University of Antwerp,university,sec_flanders,nl,https://www.uantwerpen.be,,,JR2025 assets 647m result -5m bezold 315m; tick839\n")

foi = 'gap_ua_1st_stream_l5,Vlaanderen>Universiteiten>UA_L5,ua,AHOVOKS 1st/2nd/3rd/4th stream cash split within omzet 423.2m 2025 (VO form no disaggregation); multi-year 1st path 2023-2027 reconciling CRC 2024 medium 206.9m; ETP behind 314.9m bezold; loss-year drivers,Strong BS/P&L fill; stream L5 residual dual KUL/UH strong and UGent FOI,6,Universiteit Antwerpen / AHOVOKS / openbaarheid Vlaanderen,,https://www.uantwerpen.be,docs/doge/foi/drafts/gap_ua_1st_stream_l5.md,ready,2026-08-05,,,,,cmt_ua_balance_647m_2025|cmt_ua_result_path_2024_25,lb_ua_bezold_315m_2025|lb_ua_result_minus_5m_2025|lb_ua_omzet_423m_2025,2026-08-05T16:30:00Z,2026-08-05T16:30:00Z,tick839 VL neerlegging primary; stream FOI; do not send\n'

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_829,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UGent JR2025 filled tick838; residual Roeselare/Leuven city or UA/VUB JV or BELNET accounts or skeyes residual",,2026-08-05T16:00:00Z,2026-08-05T16:00:00Z,spawned tick838 after UGent dual KUL'
new = 'rq_829,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UGent JR2025 filled tick838; residual Roeselare/Leuven city or UA/VUB JV or BELNET accounts or skeyes residual",gap_ua_1st_stream_l5,2026-08-05T16:00:00Z,2026-08-05T16:30:00Z,tick839 UA JR2025 assets 647m omzet 423m bezold 315m result -5m dual UGent; stream FOI; FOI ready'
if old not in text:
    raise SystemExit("rq_829 not found")
text = text.replace(old, new)
spawn = 'rq_840,MANDATORY progress@840 coverage % + waste top10 refresh,hole_fill,10,open,progress,gg_belgium,Refresh progress_every_10_ticks.md layers A-E + doge_waste_top10_current.md after ticks 831-839 (VL cities + HE unis),,2026-08-05T16:30:00Z,2026-08-05T16:30:00Z,spawned tick839; progress@840 NEXT tick\n'
spawn2 = 'rq_831,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UA JR2025 filled tick839; residual Roeselare/Leuven city or VUB JV or BELNET accounts or skeyes residual",,2026-08-05T16:30:00Z,2026-08-05T16:30:00Z,spawned tick839 after UA dual UGent\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn + spawn2
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T16:30:00Z,rq_829,839,no,"
    "tick839 UA JR2025 dual UGent; next progress@840 THEN rq_831 residual; rq_116 deferred\n",
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

doc = fitz.open("docs/doge/data/raw/ua_jr2025.pdf")
pages = [4, 5, 6]
with open("docs/doge/data/raw/ua_jr2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("UA JR2025 key extract tick839 (amounts kEUR in source)\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick839 OK fin_debt=", FIN_DEBT)

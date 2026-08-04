# tick838 — UGent Jaarrekening 2025 VL neerlegging (kEUR ×1000)
from pathlib import Path
import fitz

root = Path("docs/doge/data")

# All VO form amounts are thousands EUR — store full euros
def k(x):
    return int(x) * 1000

FIN_DEBT = k(25453) + k(775) + k(34943)  # LT + ST due + ST banks

budgets = f"""
bud_ugent_assets_2025,ugent,2025,{k(1375787)},,,stock,src_ugent_jr2025,strong,Total assets YE2025 1375.787m (VL neerlegging kEUR form); tick838
bud_ugent_equity_2025,ugent,2025,{k(901843)},,,stock,src_ugent_jr2025,strong,Eigen vermogen YE2025 901.843m; tick838
bud_ugent_kapitaal_2025,ugent,2025,{k(319750)},,,stock,src_ugent_jr2025,strong,Geplaatst kapitaal YE2025 319.750m; tick838
bud_ugent_bestemde_fondsen_2025,ugent,2025,{k(501010)},,,stock,src_ugent_jr2025,strong,Bestemde fondsen YE2025 501.010m (was 533.286m); tick838
bud_ugent_cap_subs_2025,ugent,2025,{k(19208)},,,stock,src_ugent_jr2025,strong,Kapitaalsubsidies YE2025 19.208m; tick838
bud_ugent_debt_total_2025,ugent,2025,{k(369674)},,,stock,src_ugent_jr2025,strong,Total schulden YE2025 369.674m; tick838
bud_ugent_fin_debt_2025,ugent,2025,{FIN_DEBT},,,stock,src_ugent_jr2025,strong,Fin schulden LT 25.453 + ST due 0.775 + ST banks 34.943 = 61.171m YE2025; tick838
bud_ugent_fin_debt_lt_2025,ugent,2025,{k(25453)},,,stock,src_ugent_jr2025,strong,Fin schulden LT YE2025 25.453m (lease 14.854 other 10.599); tick838
bud_ugent_provisions_2025,ugent,2025,{k(104269)},,,stock,src_ugent_jr2025,strong,Voorzieningen YE2025 104.269m; tick838
bud_ugent_pension_prov_2025,ugent,2025,{k(60803)},,,stock,src_ugent_jr2025,strong,Pensioenvoorzieningen YE2025 60.803m; tick838
bud_ugent_cash_2025,ugent,2025,{k(130551)},,,stock,src_ugent_jr2025,strong,Liquide middelen YE2025 130.551m; tick838
bud_ugent_geldbeleggingen_2025,ugent,2025,{k(572199)},,,stock,src_ugent_jr2025,strong,Geldbeleggingen YE2025 572.199m; tick838
bud_ugent_cash_beleg_2025,ugent,2025,{k(130551+572199)},,,stock,src_ugent_jr2025,strong,Cash+beleggingen YE2025 702.750m; tick838
bud_ugent_mva_2025,ugent,2025,{k(532312)},,,stock,src_ugent_jr2025,strong,Materiele vaste activa YE2025 532.312m; tick838
bud_ugent_bedrijfsopbr_2025,ugent,2025,{k(996207)},,,cash,src_ugent_jr2025,strong,Bedrijfsopbrengsten 996.207m (omzet 979.465m); 1st stream not split in VO form FOI; tick838
bud_ugent_omzet_2025,ugent,2025,{k(979465)},,,cash,src_ugent_jr2025,strong,Omzet 979.465m; tick838
bud_ugent_bedrijfskosten_2025,ugent,2025,{k(971444)},,,cash,src_ugent_jr2025,strong,Bedrijfskosten 971.444m; tick838
bud_ugent_bezold_2025,ugent,2025,{k(666570)},,,cash,src_ugent_jr2025,strong,Bezoldigingen 666.570m (+4.9pct vs 635.132m); tick838
bud_ugent_diensten_2025,ugent,2025,{k(227875)},,,cash,src_ugent_jr2025,strong,Diensten en diverse goederen 227.875m (was 306.116m); tick838
bud_ugent_afschr_2025,ugent,2025,{k(62874)},,,cash,src_ugent_jr2025,strong,Afschrijvingen 62.874m; tick838
bud_ugent_bedrijfs_2025,ugent,2025,{k(24763)},,,cash,src_ugent_jr2025,strong,Bedrijfsresultaat +24.763m (was -45.614m); tick838
bud_ugent_result_2025,ugent,2025,{k(61875)},,,cash,src_ugent_jr2025,strong,Resultaat boekjaar +61.875m (was -32.276m CRC 2024 strong match); tick838
bud_ugent_fin_opbr_2025,ugent,2025,{k(24245)},,,cash,src_ugent_jr2025,strong,Financiele opbrengsten 24.245m; tick838
bud_ugent_project_prepay_2025,ugent,2025,{k(189556)},,,stock,src_ugent_jr2025,strong,Ontvangen vooruitbetalingen op bestellingen/projecten YE2025 189.556m; tick838
bud_ugent_result_2024_jv,ugent,2024,{k(-32276)},,,outturn,src_ugent_jr2025,strong,Resultaat 2024 -32.276m (matches CRC 2024 -32.3m); tick838
""".strip() + "\n"

lb = f"""
lb_ugent_bezold_667m_2025,UGent bezoldigingen 666.6m 2025,L5,ops,Vlaanderen>Universiteiten>UGent>personnel,666570000,666570000,Strong VL neerlegging; +4.9pct YoY; dual KUL 917.5 UH 118.5,strong,src_ugent_jr2025,academic/admin staff,Deliver HE teaching and research,666.6m,5.0,8.0,5.0,6.0,ETP FOI; 1st stream split FOI,active,,tick838
lb_ugent_result_62m_2025,UGent result +61.9m 2025 (turnaround from -32.3m 2024),L5,ops,Vlaanderen>Universiteiten>UGent>result,61875000,61875000,Strong; recovery from CRC 2024 loss year; dual KUL 198.8m,strong,src_ugent_jr2025,university,Restore surplus after 2024 loss,61.9m / turnaround,4.5,7.0,5.0,5.5,Driver analysis FOI,active,,tick838
lb_ugent_cash_beleg_703m,UGent cash+beleggingen stock 702.8m YE2025,L5,stock,Vlaanderen>Universiteiten>UGent>liquidity,0,702750000,Strong; dual KUL 2357 UH 119; stock not pure annual waste,strong,src_ugent_jr2025,university treasury,Multi-year buffer,702.8m stock,3.5,7.5,5.0,5.33,Treasury FOI,active,,tick838 stock
lb_ugent_fin_debt_61m,UGent financial debt stock 61.2m YE2025,L5,stock,Vlaanderen>Universiteiten>UGent>debt,0,61171000,Strong; LT 25.5 ST banks 34.9; dual KUL 47.6 UH 5.2,strong,src_ugent_jr2025,lenders,Campus financing,61.2m stock,4.0,6.0,5.5,5.17,Debt schedule FOI,active,,tick838 stock
lb_dual_ugent_kuleuven_tick838,Dual UGent assets 1376m vs KU Leuven 3386m JV residual,L5,ops,Belgium>dual>vl_universities,0,1375787000,Strong dual not TE-additive; UGent 1st stream not split in VO form residual FOI,strong,src_dual_ugent_kuleuven_tick838,HE multi-channel,Dual residual map,primary,4.0,8.0,5.0,5.67,Cross FOI,active,,tick838
""".strip() + "\n"

cmt = f"""
cmt_ugent_balance_1376m_2025,UGent balance sheet YE2025 assets 1375.8m equity 901.8m,ugent,Universiteit Gent,VL neerlegging jaarrekening 2025 AV 27.03.2026,2026-03-27,2025,2025,{k(1375787)},"{{""assets_m"": 1375.787, ""equity_m"": 901.843, ""cash_beleg_m"": 702.750, ""fin_debt_m"": 61.171, ""pension_prov_m"": 60.803, ""bezold_m"": 666.570}}",0,active,https://docs.vlaamsparlement.be/files/pfile?id=2321555,UGent statutory BS kEUR form,Publish 1st stream split FOI,src_ugent_jr2025,strong,Vlaanderen>Universiteiten>UGent>balance,tick838 amounts kEUR×1000
cmt_ugent_result_path_2024_25,UGent result path -32.3m 2024 to +61.9m 2025,ugent,Universiteit Gent,VL neerlegging comparative,2025-12-31,2024,2025,{k(61875)},"{{""result_2024_m"": -32.276, ""result_2025_m"": 61.875, ""bedrijfs_2025_m"": 24.763, ""bezold_2025_m"": 666.570, ""omzet_2025_m"": 979.465}}",0,active,docs/doge/data/raw/ugent_jr2025.pdf,Turnaround after CRC 2024 loss,Publish cost drivers FOI,src_ugent_jr2025,strong,Vlaanderen>Universiteiten>UGent>result,tick838
cmt_dual_ugent_kuleuven_tick838,Dual UGent JR2025 vs KU Leuven JV2025 residual,gg_belgium,dual map,UGent JR2025 dual KUL tick837,2026-08-05,2025,2025,{k(1375787)},"{{""ugent_assets_m"": 1375.8, ""kul_assets_m"": 3386.2, ""ugent_bezold_m"": 666.6, ""kul_bezold_m"": 917.5, ""ugent_result_m"": 61.9, ""kul_result_m"": 198.8}}",0,active,docs/doge/data/raw/ugent_jr2025.pdf,Dual residual map tick838,Cross FOI HE,src_dual_ugent_kuleuven_tick838,strong,Belgium>dual>vl_universities,tick838 not TE-additive
""".strip() + "\n"

src = """
src_ugent_jr2025,"Universiteit Gent Jaarrekening 2025 VL neerleggingsformulier (AV 27.03.2026, 39p, amounts kEUR)",https://docs.vlaamsparlement.be/files/pfile?id=2321555,Universiteit Gent / Departement FB,2026-08-05,entity_accounts,Strong tick838 primary: assets 1375.8m equity 901.8m; omzet 979.5m; bezold 666.6m; result +61.9m (was -32.3m); cash+beleg 702.8m; fin debt 61.2m; pension prov 60.8m; 1st stream NOT split in VO model FOI residual; raw ugent_jr2025.pdf
src_dual_ugent_kuleuven_tick838,Dual UGent JR2025 1376m vs KU Leuven 3386m residual tick838,docs/doge/data/raw/ugent_jr2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: UGent assets 1376m bezold 667m result 62m vs KUL assets 3386m 1st 568m bezold 917m result 199m
""".strip() + "\n"

ent_path = root / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
if "ugent," in ent_text:
    lines = ent_text.splitlines()
    out = []
    for line in lines:
        if line.startswith("ugent,") and "tick838" not in line:
            line = line.rstrip() + " | JR2025 assets 1376m result +62m bezold 667m; tick838"
        out.append(line)
    ent_path.write_text("\n".join(out) + ("\n" if ent_text.endswith("\n") else ""), encoding="utf-8")
else:
    with ent_path.open("a", encoding="utf-8", newline="") as f:
        f.write("ugent,Universiteit Gent,Universite de Gand,Ghent University,university,sec_flanders,nl,https://www.ugent.be,,,JR2025 assets 1376m result +62m bezold 667m; tick838\n")

foi = 'gap_ugent_1st_stream_l5,Vlaanderen>Universiteiten>UGent_L5,ugent,AHOVOKS 1st/2nd/3rd/4th stream cash split within omzet 979.5m 2025 (VO neerlegging form does not disaggregate); multi-year 1st stream path 2023-2027; ETP behind 666.6m bezold; CAPEX project L5,Strong BS/P&L fill but stream L5 residual dual KUL/UHasselt strong 1st fills,6,Universiteit Gent / AHOVOKS / openbaarheid Vlaanderen,,https://www.ugent.be,docs/doge/foi/drafts/gap_ugent_1st_stream_l5.md,ready,2026-08-05,,,,,cmt_ugent_balance_1376m_2025|cmt_ugent_result_path_2024_25,lb_ugent_bezold_667m_2025|lb_ugent_result_62m_2025,2026-08-05T16:00:00Z,2026-08-05T16:00:00Z,tick838 VL neerlegging primary; stream split FOI; do not send\n'

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_828,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; KU Leuven JV2025 filled tick837; residual Roeselare/Leuven city or UGent/UA/VUB JV or BELNET accounts or skeyes residual",,2026-08-05T15:30:00Z,2026-08-05T15:30:00Z,spawned tick837 after KU Leuven dual UHasselt'
new = 'rq_828,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; KU Leuven JV2025 filled tick837; residual Roeselare/Leuven city or UGent/UA/VUB JV or BELNET accounts or skeyes residual",gap_ugent_1st_stream_l5,2026-08-05T15:30:00Z,2026-08-05T16:00:00Z,tick838 UGent JR2025 assets 1376m omzet 980m bezold 667m result +62m dual KUL; stream FOI; FOI ready'
if old not in text:
    raise SystemExit("rq_828 not found")
text = text.replace(old, new)
spawn = 'rq_829,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UGent JR2025 filled tick838; residual Roeselare/Leuven city or UA/VUB JV or BELNET accounts or skeyes residual",,2026-08-05T16:00:00Z,2026-08-05T16:00:00Z,spawned tick838 after UGent dual KUL\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T16:00:00Z,rq_828,838,no,"
    "tick838 UGent JR2025 dual KUL; next rq_829 residual dual L5; progress@840 in 2; rq_116 deferred\n",
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

doc = fitz.open("docs/doge/data/raw/ugent_jr2025.pdf")
pages = [4, 5, 6]
with open("docs/doge/data/raw/ugent_jr2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("UGent JR2025 key extract tick838 (amounts kEUR in source)\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick838 OK fin_debt=", FIN_DEBT)

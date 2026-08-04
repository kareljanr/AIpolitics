# tick837 — KU Leuven JV2025 fill dual UHasselt
from pathlib import Path
import fitz

root = Path("docs/doge/data")
FIN_DEBT = 43005320 + 4550142  # LT fin + ST due

budgets = f"""
bud_kuleuven_assets_2025,kuleuven,2025,3386177320,,,stock,src_kuleuven_jv2025,strong,Total assets YE2025 3386.177m (+5.6pct); tick837
bud_kuleuven_equity_2025,kuleuven,2025,2519857971,,,stock,src_kuleuven_jv2025,strong,Eigen vermogen YE2025 2519.858m; tick837
bud_kuleuven_bestemde_fondsen_2025,kuleuven,2025,2518136560,,,stock,src_kuleuven_jv2025,strong,Bestemde fondsen YE2025 2518.137m (research 1620.2m); tick837
bud_kuleuven_cap_subs_2025,kuleuven,2025,1721411,,,stock,src_kuleuven_jv2025,strong,Kapitaalsubsidies YE2025 1.721m; tick837
bud_kuleuven_debt_total_2025,kuleuven,2025,612018182,,,stock,src_kuleuven_jv2025,strong,Total schulden YE2025 612.018m; tick837
bud_kuleuven_fin_debt_2025,kuleuven,2025,{FIN_DEBT},,,stock,src_kuleuven_jv2025,strong,Financiele schulden LT 43.005m + ST due 4.550m = 47.555m YE2025; tick837
bud_kuleuven_fin_debt_lt_2025,kuleuven,2025,43005320,,,stock,src_kuleuven_jv2025,strong,Financiele schulden LT YE2025 43.005m (banks 36.4 lease 6.6); tick837
bud_kuleuven_provisions_2025,kuleuven,2025,254301167,,,stock,src_kuleuven_jv2025,strong,Voorzieningen YE2025 254.301m (pensioen 12.3 groot onderhoud 195.3); tick837
bud_kuleuven_pension_prov_2025,kuleuven,2025,12314544,,,stock,src_kuleuven_jv2025,strong,Pensioenvoorzieningen YE2025 12.315m; tick837
bud_kuleuven_cash_2025,kuleuven,2025,40452363,,,stock,src_kuleuven_jv2025,strong,Liquide middelen YE2025 40.452m; tick837
bud_kuleuven_geldbeleggingen_2025,kuleuven,2025,2316588562,,,stock,src_kuleuven_jv2025,strong,Geldbeleggingen YE2025 2316.589m; tick837
bud_kuleuven_cash_beleg_2025,kuleuven,2025,2357040925,,,stock,src_kuleuven_jv2025,strong,Cash+beleggingen YE2025 2357.041m; tick837
bud_kuleuven_mva_2025,kuleuven,2025,775746242,,,stock,src_kuleuven_jv2025,strong,Materiele vaste activa YE2025 775.746m; tick837
bud_kuleuven_bedrijfsopbr_2025,kuleuven,2025,1565183111,,,cash,src_kuleuven_jv2025,strong,Bedrijfsopbrengsten 1565.183m (+3.5pct); tick837
bud_kuleuven_1st_stream_2025,kuleuven,2025,567940708,,,cash,src_kuleuven_jv2025,strong,1ste geldstroom basisfinanciering 567.941m STRONG (+21.4m YoY; matches prior 546.5m 2024); tick837
bud_kuleuven_werking_2025,kuleuven,2025,536061091,,,cash,src_kuleuven_jv2025,strong,Werkingsuitkeringen 536.061m within 1st stream (+20.9m); tick837
bud_kuleuven_invest_uitkering_2025,kuleuven,2025,19741757,,,cash,src_kuleuven_jv2025,strong,Investeringsuitkeringen 19.742m within 1st stream; tick837
bud_kuleuven_2nd_stream_2025,kuleuven,2025,193753782,,,cash,src_kuleuven_jv2025,strong,2de geldstroom 193.754m (BOF 107.7 FWO 80.6); tick837
bud_kuleuven_3rd_stream_2025,kuleuven,2025,287781953,,,cash,src_kuleuven_jv2025,strong,3de geldstroom 287.782m (+33.9m); tick837
bud_kuleuven_4th_stream_2025,kuleuven,2025,247230240,,,cash,src_kuleuven_jv2025,strong,4de geldstroom contract/valorisatie 247.230m; tick837
bud_kuleuven_tuition_2025,kuleuven,2025,62130394,,,cash,src_kuleuven_jv2025,strong,Reguliere inschrijvingsgelden 62.130m; tick837
bud_kuleuven_bedrijfskosten_2025,kuleuven,2025,1432419711,,,cash,src_kuleuven_jv2025,strong,Bedrijfskosten 1432.420m (+2.9pct); tick837
bud_kuleuven_bezold_2025,kuleuven,2025,917494684,,,cash,src_kuleuven_jv2025,strong,Bezoldigingen 917.495m (+4.5pct; VTE 10159.6); tick837
bud_kuleuven_diensten_2025,kuleuven,2025,391787372,,,cash,src_kuleuven_jv2025,strong,Diensten en diverse goederen 391.787m; tick837
bud_kuleuven_afschr_2025,kuleuven,2025,68360244,,,cash,src_kuleuven_jv2025,strong,Afschrijvingen 68.360m; tick837
bud_kuleuven_bedrijfs_2025,kuleuven,2025,132763400,,,cash,src_kuleuven_jv2025,strong,Bedrijfsoverschot 132.763m; tick837
bud_kuleuven_result_2025,kuleuven,2025,198755329,,,cash,src_kuleuven_jv2025,strong,Overschot boekjaar bedrijfsecon 198.755m (was 180.188m); tick837
bud_kuleuven_result_cashview_2025,kuleuven,2025,154209191,,,cash,src_kuleuven_jv2025,strong,Overschot cashview 154.209m; tick837
bud_kuleuven_vte_2025,kuleuven,2025,10160,,,outturn,src_kuleuven_jv2025,strong,Verbruiks-VTE 10159.6 2025 (was 10075.2); tick837
bud_kuleuven_project_prepay_2025,kuleuven,2025,189835604,,,stock,src_kuleuven_jv2025,strong,Ontvangen vooruitbetalingen op projecten YE2025 189.836m; tick837
""".strip() + "\n"

lb = f"""
lb_kuleuven_1st_568m_2025,KU Leuven 1st stream basisfinanciering 567.9m 2025,L5,subsidy,Vlaanderen>Universiteiten>KULeuven>1st_stream,567940708,567940708,Strong primary JV RvB 31.03.2026; werkingsuitkering 536.1m within; dual UHasselt 96.8m,strong,src_kuleuven_jv2025,students/staff,Public HE operating grant,567.9m / +21.4m YoY,4.0,8.5,4.5,5.67,AHOVOKS open matrix FOI residual,active,,tick837
lb_kuleuven_bezold_917m_2025,KU Leuven bezoldigingen 917.5m 2025 (VTE 10160),L5,ops,Vlaanderen>Universiteiten>KULeuven>personnel,917494684,917494684,Strong; +4.5pct YoY; bursalen 135.8m within; dual UHasselt 118.5m,strong,src_kuleuven_jv2025,academic/admin staff,Deliver HE teaching and research,917.5m / 64pct of bedrijfskosten,5.0,8.5,4.5,6.0,ETP productivity FOI,active,,tick837
lb_kuleuven_cash_beleg_2357m,KU Leuven cash+beleggingen stock 2357m YE2025,L5,stock,Vlaanderen>Universiteiten>KULeuven>liquidity,0,2357040925,Strong largest HE treasury stock; research-restricted fonds; stock not pure annual waste,strong,src_kuleuven_jv2025,university treasury,Multi-year research and campus buffer,2357m stock,3.5,9.0,5.0,5.83,Treasury policy FOI,active,,tick837 stock filtered pure annual top10
lb_kuleuven_result_199m_2025,KU Leuven result 198.8m 2025 (research-restricted),L5,ops,Vlaanderen>Universiteiten>KULeuven>result,198755329,198755329,Strong; largely AOF research multi-year restricted not free surplus; dual UHasselt 5.6m,strong,src_kuleuven_jv2025,research funders,Match multi-year research contracts,198.8m / restricted class,4.0,7.5,5.5,5.67,Publish free vs restricted FOI,active,,tick837
lb_dual_kuleuven_uhasselt_tick837,Dual KU Leuven 1st 568m vs UHasselt 96.8m JV2025 residual,L5,ops,Belgium>dual>vl_universities,567940708,567940708,Strong dual not TE-additive; completes VL uni JV pair after tick836,strong,src_dual_kuleuven_uhasselt_tick837,HE multi-channel,Dual residual map,primary,4.0,8.0,4.5,5.5,Cross FOI,active,,tick837
""".strip() + "\n"

cmt = f"""
cmt_kuleuven_balance_3386m_2025,KU Leuven balance sheet YE2025 assets 3386m equity 2520m,kuleuven,KU Leuven,Jaarverslag 2025 RvB 31.03.2026,2026-03-31,2025,2025,3386177320,"{{""assets_m"": 3386.177, ""equity_m"": 2519.858, ""cash_beleg_m"": 2357.041, ""fin_debt_m"": 47.555, ""provisions_m"": 254.301, ""mva_m"": 775.746}}",0,active,https://www.kuleuven.be/over-kuleuven/pdf/jaarverslag-ku-leuven-2025.pdf,Largest VL university BS,Publish free vs restricted treasury FOI,src_kuleuven_jv2025,strong,Vlaanderen>Universiteiten>KULeuven>balance,tick837
cmt_kuleuven_1st_stream_2025,KU Leuven 1st stream basisfinanciering 567.9m 2025 strong,kuleuven,KU Leuven / AHOVOKS,JV2025 resultatenrekening code 700,2025-12-31,2025,2025,567940708,"{{""1st_m"": 567.941, ""werking_m"": 536.061, ""invest_uitk_m"": 19.742, ""sociaal_m"": 11.960, ""2024_1st_m"": 546.506}}",0,active,docs/doge/data/raw/kuleuven_jv2025.pdf,Public HE first-stream grant exact,Open AHOVOKS matrix sector FOI,src_kuleuven_jv2025,strong,Vlaanderen>Universiteiten>KULeuven>1st_stream,tick837 matches prior CRC strong 546.5m 2024
cmt_kuleuven_result_path_2024_25,KU Leuven result path 180.2m 2024 to 198.8m 2025,kuleuven,KU Leuven,JV2025 comparative,2025-12-31,2024,2025,198755329,"{{""result_2024_m"": 180.188, ""result_2025_m"": 198.755, ""bedrijfs_2025_m"": 132.763, ""bezold_2025_m"": 917.495, ""vte_2025"": 10159.6}}",0,active,docs/doge/data/raw/kuleuven_jv2025.pdf,Research-restricted surplus path,Publish free surplus FOI,src_kuleuven_jv2025,strong,Vlaanderen>Universiteiten>KULeuven>result,tick837
cmt_dual_kuleuven_uhasselt_tick837,Dual KU Leuven JV2025 vs UHasselt JV2025 residual,gg_belgium,dual map,KUL JV2025 dual UH tick836,2026-08-05,2025,2025,567940708,"{{""kul_1st_m"": 567.941, ""uh_1st_m"": 96.770, ""kul_assets_m"": 3386.2, ""uh_assets_m"": 281.3, ""kul_bezold_m"": 917.5, ""uh_bezold_m"": 118.5}}",0,active,docs/doge/data/raw/kuleuven_jv2025.pdf,Dual residual map tick837,Cross FOI HE,src_dual_kuleuven_uhasselt_tick837,strong,Belgium>dual>vl_universities,tick837 not TE-additive
""".strip() + "\n"

src = """
src_kuleuven_jv2025,"KU Leuven Jaarverslag 2025 (jaarrekening RvB 31.03.2026, 167p)",https://www.kuleuven.be/over-kuleuven/pdf/jaarverslag-ku-leuven-2025.pdf,KU Leuven,2026-08-05,entity_accounts,Strong tick837 primary: assets 3386m equity 2520m; bedrijfsopbr 1565m; 1st stream 567.9m strong; bezold 917.5m VTE 10160; result 198.8m; cash+beleg 2357m; fin debt 47.6m; raw kuleuven_jv2025.pdf
src_dual_kuleuven_uhasselt_tick837,Dual KU Leuven JV2025 1st 568m vs UHasselt 96.8m residual tick837,docs/doge/data/raw/kuleuven_jv2025.pdf,DOGE synthesis,2026-08-05,synthesis,Strong dual not TE-additive: KUL assets 3386m 1st 568m bezold 917m vs UH assets 281m 1st 97m bezold 118m
""".strip() + "\n"

# entity - check if kuleuven exists
ent_path = root / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
if "kuleuven," in ent_text or "ku_leuven," in ent_text:
    # try update common patterns
    for old, new in [
        ("CRC 2024", "JV2025 assets 3386m 1st 568m strong bezold 917m; CRC residual; tick837"),
    ]:
        pass
    if "JV2025 assets 3386m" not in ent_text:
        # append note via replace first matching line containing kuleuven
        lines = ent_text.splitlines()
        out = []
        for line in lines:
            if line.startswith("kuleuven,") or line.startswith("ku_leuven,"):
                if "tick837" not in line:
                    line = line.rstrip() + " | JV2025 assets 3386m 1st 568m; tick837"
            out.append(line)
        ent_path.write_text("\n".join(out) + ("\n" if ent_text.endswith("\n") else ""), encoding="utf-8")
else:
    with ent_path.open("a", encoding="utf-8", newline="") as f:
        f.write("kuleuven,KU Leuven,KU Leuven,KU Leuven,university,sec_flanders,nl,https://www.kuleuven.be,,,JV2025 assets 3386m 1st 568m strong bezold 917m result 199m; tick837\n")

foi = 'gap_kuleuven_ahovoks_restricted_l5,Vlaanderen>Universiteiten>KULeuven_L5,kuleuven,AHOVOKS multi-year 1st stream path 2023-2027 reconciling JV 567.9m 2025; free vs research-restricted surplus split within 198.8m result and 2357m treasury; CAPEX project L5 Vijfjarenplan; lease/EIB debt schedule within 47.6m fin debt,Strong annual JV but multi-year AHOVOKS matrix and free surplus opacity residual dual gap_univ_per_institution,5,KU Leuven / AHOVOKS / openbaarheid Vlaanderen,,https://www.kuleuven.be,docs/doge/foi/drafts/gap_kuleuven_ahovoks_restricted_l5.md,ready,2026-08-05,,,,,cmt_kuleuven_1st_stream_2025|cmt_kuleuven_balance_3386m_2025,lb_kuleuven_1st_568m_2025|lb_kuleuven_bezold_917m_2025|lb_kuleuven_cash_beleg_2357m,2026-08-05T15:30:00Z,2026-08-05T15:30:00Z,tick837 JV2025 primary; residual multi-year FOI; do not send\n'

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_827,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UHasselt JV2025 filled tick836; residual Roeselare/Leuven city or BELNET accounts or skeyes residual or other uni JV",,2026-08-05T15:00:00Z,2026-08-05T15:00:00Z,spawned tick836 after UHasselt dual CRC'
new = 'rq_827,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; UHasselt JV2025 filled tick836; residual Roeselare/Leuven city or BELNET accounts or skeyes residual or other uni JV",gap_kuleuven_ahovoks_restricted_l5,2026-08-05T15:00:00Z,2026-08-05T15:30:00Z,tick837 KU Leuven JV2025 assets 3386m 1st 568m strong bezold 917m result 199m dual UHasselt; FOI ready'
if old not in text:
    raise SystemExit("rq_827 not found")
text = text.replace(old, new)
spawn = 'rq_828,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual, VL provinces); prefer FOI-adjacent L5; skip rq_116; KU Leuven JV2025 filled tick837; residual Roeselare/Leuven city or UGent/UA/VUB JV or BELNET accounts or skeyes residual",,2026-08-05T15:30:00Z,2026-08-05T15:30:00Z,spawned tick837 after KU Leuven dual UHasselt\n'
if not text.endswith("\n"):
    text += "\n"
text += spawn
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-05T15:30:00Z,rq_827,837,no,"
    "tick837 KU Leuven JV2025 dual UHasselt; next rq_828 residual dual L5; progress@840 in 3; rq_116 deferred\n",
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

doc = fitz.open("docs/doge/data/raw/kuleuven_jv2025.pdf")
pages = [154, 155, 156, 162, 163]
with open("docs/doge/data/raw/kuleuven_jv2025_extract.txt", "w", encoding="utf-8") as f:
    f.write("KU Leuven JV2025 key extract tick837\n")
    for p in pages:
        f.write(f"\n===== PAGE {p+1} =====\n")
        f.write(doc[p].get_text())

print("tick837 OK fin_debt=", FIN_DEBT)

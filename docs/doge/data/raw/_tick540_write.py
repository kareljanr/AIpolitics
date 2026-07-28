# tick540 — exposé ODA dual + federal debt financing schema + progress@540
from pathlib import Path
import csv
from collections import Counter

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T09:00:00Z"

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_oda_debt_2026,Kamer expose 2026 ODA solidarity note + federal interest/debt financing,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part III Afdeling2-3,2026-07-29,primary_budget,"
        "Strong tick540: ODA total 2.990bn 2024 (0.48pct GNI) to 2.350bn 2026 (0.35pct); DGD VLK 1040m VEK 654m 2026; "
        "Fedasil ODA 437m 2024 to 234m 2026; EC share 897m; federal interest series to 12.34bn 2026; "
        "gross financing need 59.7bn 2026; unconsol fed debt 540.7/570.2/601.3bn eoy24-26; tick540\n"
    )
    f.write(
        "src_dual_oda_dgd_multi_tick540,Dual ODA DGD vs multi-actor (EC Fedasil Finance non-fed) composition,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis exposé ODA table,2026-07-29,synthesis,"
        "Strong dual: DGD share 48pct 2024 falling; EC ~40pct path; Fedasil refugee ODA doubles 2024 then halves; tick540\n"
    )

buds = [
    # ODA totals
    "bud_oda_total_2024,sec_federal,2024,2989572000,,,outturn,src_kamer_expose_oda_debt_2026,strong,ODA total BE 2989.572m 2024 (0.48pct GNI); peak Ukraine+refugee; tick540",
    "bud_oda_total_2025,sec_federal,2025,2391896000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,ODA total est 2391.896m 2025 (0.37pct GNI); tick540",
    "bud_oda_total_2026,sec_federal,2026,2349979000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,ODA total est 2349.979m 2026 (0.35pct GNI); path down from 0.48; tick540",
    "bud_oda_total_2022,sec_federal,2022,2532037000,,,outturn,src_kamer_expose_oda_debt_2026,strong,ODA total 2532.037m 2022 (0.45pct GNI); tick540",
    "bud_oda_total_2023,sec_federal,2023,2604042000,,,outturn,src_kamer_expose_oda_debt_2026,strong,ODA total 2604.042m 2023 (0.44pct GNI); tick540",
    # DGD
    "bud_dgd_vlk_2026,sec_federal,2026,1040000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,DGD VLK budget 1040m 2026 (VEK 654m dual); 25pct cut path; tick540",
    "bud_dgd_vek_2026,sec_federal,2026,654000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,DGD VEK 654m 2026 vs VLK 1040m dual; tick540",
    "bud_dgd_vlk_2024,sec_federal,2024,1449394000,,,outturn,src_kamer_expose_oda_debt_2026,strong,DGD budget line 1449.394m 2024; tick540",
    "bud_dgd_oda_eligible_2026,sec_federal,2026,1031120000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,ODA on DGD budget 1031.120m 2026; tick540",
    "bud_dgd_oda_eligible_2024,sec_federal,2024,1434193000,,,outturn,src_kamer_expose_oda_debt_2026,strong,ODA on DGD 1434.193m 2024 (48pct of total ODA); tick540",
    # Multi-actor ODA
    "bud_oda_ec_share_2026,sec_federal,2026,897199000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,ODA via EC share 897.199m 2026 (~38pct of total); tick540",
    "bud_oda_ec_share_2024,sec_federal,2024,868490000,,,outturn,src_kamer_expose_oda_debt_2026,strong,ODA EC share 868.490m 2024; tick540",
    "bud_oda_fedasil_2024,sec_federal,2024,437138000,,,outturn,src_kamer_expose_oda_debt_2026,strong,Fedasil ODA-eligible 437.138m 2024 refugee peak; tick540",
    "bud_oda_fedasil_2026,sec_federal,2026,234000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Fedasil ODA est 234m 2026 (halved vs 2024); tick540",
    "bud_oda_fedasil_2025,sec_federal,2025,233468000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Fedasil ODA est 233.468m 2025; tick540",
    "bud_oda_finance_2026,fod_finance,2026,15960000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,FPS Finance ODA 15.960m 2026 (down from 67.5m 2024); tick540",
    "bud_oda_foreign_2026,sec_federal,2026,92000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Foreign Affairs ODA 92m 2026; tick540",
    "bud_oda_nonfed_2026,gg_belgium,2026,82700000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Non-federal ODA (C&R local) 82.7m 2026; tick540",
    "bud_gni_oda_denom_2026,gg_belgium,2026,665215000000,,,estimate,src_kamer_expose_oda_debt_2026,strong,GNI denominator for ODA 665.215bn 2026; tick540",
    # Interest path years
    "bud_fed_interest_2023,sec_federal,2023,8600000000,,,outturn,src_kamer_expose_oda_debt_2026,strong,Fed interest 8.60bn 2023 (+24.1pct YoY); tick540",
    "bud_fed_interest_2024,sec_federal,2024,10030000000,,,outturn,src_kamer_expose_oda_debt_2026,strong,Fed interest 10.03bn 2024 (+16.6pct); tick540",
    "bud_fed_interest_treasury_2026,sec_federal,2026,12165000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Treasury ESR interest 12165m of total 12343m 2026; consol 55 + FPS Fin 124; tick540",
    "bud_fed_interest_consol_2026,sec_federal,2026,55000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Consol institutions interest 55m 2026 (excl Hedera imputed); tick540",
    # Financing
    "bud_fed_gross_financing_2026,sec_federal,2026,59700000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Gross financing need 59.7bn 2026 (net 28.5 + maturing 28.0 + prefin 3.2); tick540",
    "bud_fed_net_financing_2026,sec_federal,2026,28500000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Net financing need 28.5bn 2026; tick540",
    "bud_fed_maturing_debt_2026,sec_federal,2026,28000000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Debt maturing in year 28.0bn 2026; tick540",
    "bud_fed_olo_issuance_2026,sec_federal,2026,52000000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,OLO long-term issuance plan 52.0bn 2026 of LT 55.3; tick540",
    "bud_fed_lt_issuance_2026,sec_federal,2026,55300000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Long-term issuance 55.3bn 2026 (OLO 52 + EMTN/RRF 3.1 + retail 0.2); tick540",
    "bud_fed_gross_financing_2025,sec_federal,2025,53000000000,,,budgeted,src_kamer_expose_oda_debt_2026,strong,Gross financing need 53.0bn 2025 (net 28.0 + maturing 22.5 + prefin 2.5); tick540",
    # Debt stock
    "bud_fed_debt_unconsol_2024,sec_federal,2024,540700000000,,,outturn,src_kamer_expose_oda_debt_2026,strong,Unconsol federal gross debt eoy2024 540.7bn (87.2pct GDP); tick540",
    "bud_fed_debt_unconsol_2025,sec_federal,2025,570200000000,,,estimate,src_kamer_expose_oda_debt_2026,strong,Unconsol federal gross debt eoy2025 ~570.2bn (+29.5bn; 88.7pct GDP); tick540",
    "bud_fed_debt_unconsol_2026,sec_federal,2026,601300000000,,,estimate,src_kamer_expose_oda_debt_2026,strong,Unconsol federal gross debt eoy2026 ~601.3bn (+31.1bn; 90.8pct GDP); tick540",
    # Dual
    "bud_dual_oda_dgd_vs_total_2026,sec_federal,2026,1031120000,,,derived,src_dual_oda_dgd_multi_tick540,strong,Dual DGD-eligible 1031m vs total ODA 2350m 2026 (~44pct); EC+Fedasil+other residual; tick540",
    "bud_dual_fed_debt_vs_gg_2026,sec_federal,2026,601300000000,,,derived,src_kamer_expose_oda_debt_2026,medium,Dual unconsol fed debt 601.3bn vs GG Maastricht ~692bn class; not same perimeter; tick540",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_oda_be_path_2022_26,Belgian ODA multi-actor path 2022-2026 dual DGD,sec_federal,Partner countries multilaterals refugees,"
        "Expose Solidariteitsnota + ODA table,2026-01-28,2022,2026,2989572000,"
        '"{""2022_m"":2532.0,""2023_m"":2604.0,""2024_m"":2989.6,""2025_m"":2391.9,""2026_m"":2350.0,'
        '""pct_gni_2022"":0.45,""pct_gni_2023"":0.44,""pct_gni_2024"":0.48,""pct_gni_2025"":0.37,""pct_gni_2026"":0.35,'
        '""dgd_vlk_2026_m"":1040,""dgd_vek_2026_m"":654,""dgd_oda_2026_m"":1031.1,""ec_2026_m"":897.2,'
        '""fedasil_2024_m"":437.1,""fedasil_2026_m"":234,""cut_path"":""25pct DGD government agreement"",'
        '""note"":""Strong primary; 0.7pct GNI target missed; DGD share falling under 50pct""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Official development assistance dual,"
        "Partner-country L5 FOI; efficiency concentration,src_kamer_expose_oda_debt_2026,strong,Federal>ODA>path_2022_26,tick540"
    ),
    (
        "cmt_fed_financing_schema_2026,Federal Debt Agency financing schema 2025-2026,sec_federal,Bondholders,"
        "Expose financing table Debt Agency Monitoring Committee,2026-01-28,2025,2026,59700000000,"
        '"{""gross_2025_bn"":53.0,""gross_2026_bn"":59.7,""net_2025_bn"":28.0,""net_2026_bn"":28.5,'
        '""maturing_2025_bn"":22.5,""maturing_2026_bn"":28.0,""prefin_2026_bn"":3.2,""olo_2026_bn"":52.0,'
        '""lt_2026_bn"":55.3,""emtn_rrf_2026_bn"":3.1,""avg_rate_10y"":0.0362,""wavg_lt_rate"":0.0383,'
        '""wavg_maturity_y"":16.04,""interest_cut_conclave_m"":27}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Refinance + fund federal deficit,"
        "Primary surplus path,src_kamer_expose_oda_debt_2026,strong,Federal>Debt>financing_schema_2026,tick540"
    ),
    (
        "cmt_fed_debt_stock_path_2024_26,Federal unconsol gross debt stock path eoy2024-26,sec_federal,Taxpayers bondholders,"
        "Expose debt section post-conclave,2026-01-28,2024,2026,601300000000,"
        '"{""eoy2024_bn"":540.7,""eoy2025_bn"":570.2,""eoy2026_bn"":601.3,""delta_2025_bn"":29.5,'
        '""delta_2026_bn"":31.1,""pct_gdp_2024"":87.2,""pct_gdp_2025"":88.7,""pct_gdp_2026"":90.8,'
        '""note"":""Unconsol federal power; dual vs GG Maastricht 107.9pct""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Track federal debt stock,"
        "Consolidate dual perimeters FOI,src_kamer_expose_oda_debt_2026,strong,Federal>Debt>stock_path,tick540"
    ),
    (
        "cmt_fed_interest_series_2005_26,Federal interest charges long series 2005-2026,sec_federal,Bondholders,"
        "Expose interest table bn EUR,2026-01-28,2005,2026,12340000000,"
        '"{""2005_bn"":12.26,""2019_bn"":8.48,""2021_bn"":7.37,""2022_bn"":6.93,""2023_bn"":8.60,'
        '""2024_bn"":10.03,""2025_bn"":10.94,""2026_bn"":12.34,""pct_gdp_2026"":1.86,'
        '""idx_2005_100_2026"":100.7,""note"":""Trough 2022 then steep rise; 2026 back above 2005 level""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Service federal debt long run,"
        "Primary surplus to bend path,src_kamer_expose_oda_debt_2026,strong,Federal>Debt>interest_series,tick540"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_oda_total_2_35bn,Belgian ODA total 2.35bn 2026 (0.35pct GNI),federal,ops,Federal>ODA>total_2026,2349979000,2349979000,Strong exposé: down from 2.99bn/0.48pct 2024; 0.7pct target missed; 25pct DGD cut path,strong,src_kamer_expose_oda_debt_2026,Partner countries multilaterals,ODA 0.7pct GNI target,Falling %GNI,5.5,8.0,5,6.65,Partner L5 FOI,seed,,tick540",
    "lb_dgd_vlk_1_04bn,DGD development VLK 1.04bn dual VEK 0.65bn,federal,ops,Federal>ODA>DGD_2026,1040000000,1040000000,Strong dual: VLK 1040m VEK 654m; DGD share of ODA falling under 50pct,strong,src_dual_oda_dgd_multi_tick540,DGD partners,Core development budget,Dual commit cash,5.0,7.5,4,6.25,Country matrix FOI,seed,,tick540",
    "lb_oda_ec_share_897m,ODA via European Commission 897m 2026,federal,ops,Federal>ODA>EC_share_2026,897199000,897199000,Strong: EC ~38pct of BE ODA; rising share as DGD shrinks,strong,src_kamer_expose_oda_debt_2026,EU development,Multilateral channel,Dual EU MFF,4.5,7.5,5,5.95,MFF transparency,seed,,tick540",
    "lb_oda_fedasil_dual_437_234m,Fedasil ODA dual 437m 2024 to 234m 2026,federal,ops,Federal>ODA>Fedasil,234000000,437138000,Strong dual: refugee ODA peak 437m 2024 halves; in-country asylum counts as ODA,strong,src_dual_oda_dgd_multi_tick540,Asylum seekers,Refugee ODA DAC rules,Composition shift,7.0,7.5,4,7.05,DAC eligibility FOI,seed,,tick540",
    "lb_fed_interest_12_34bn_series,Federal interest 12.34bn 2026 series peak path,federal,ops,Federal>Debt>interest_2026_series,12340000000,12340000000,Strong long series: trough 6.93bn 2022 then +78pct to 12.34bn; 1.86pct GDP; not pure waste,strong,src_kamer_expose_oda_debt_2026,Bondholders,Debt service,Snowball after 2022,4.5,9.5,7,6.7,Primary surplus,seed,,tick540",
    "lb_fed_gross_financing_59_7bn,Gross financing need 59.7bn 2026,federal,ops,Federal>Debt>gross_financing_2026,59700000000,59700000000,Strong Debt Agency: net 28.5 + maturing 28.0 + prefin 3.2; OLO 52bn,strong,src_kamer_expose_oda_debt_2026,Capital markets,Refinance + deficit,Gross not TE,3.0,9.5,6,6.35,Issuance transparency,seed,,tick540",
    "lb_fed_debt_stock_601bn,Federal unconsol debt stock 601.3bn eoy2026,federal,ops,Federal>Debt>stock_unconsol_2026,0,601300000000,Strong stock: 540.7 to 601.3bn eoy24-26; 90.8pct GDP unconsol dual vs GG,strong,src_kamer_expose_oda_debt_2026,Taxpayers,Federal debt stock,Dual perimeter,4.0,9.5,7,6.4,Perimeter FOI,seed,,tick540",
    "lb_dual_oda_composition,Dual ODA DGD vs EC vs Fedasil composition,multi,ops,BE>dual>ODA_composition,2350000000,2989572000,Strong dual multi-actor ODA; DGD <50pct; EC~40pct path; Fedasil refugee dual,strong,src_dual_oda_dgd_multi_tick540,Multi-level,ODA architecture,Composition opacity L5,6.0,8.0,5,6.85,Full matrix FOI,seed,,tick540",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_oda_partner_l5,Federal>ODA>DGD>partner_country_org_L5,sec_federal,"
        "Named L5 partner country and organisation matrix under DGD VLK 1.04bn 2025-2026 with EUR; "
        "reconcile multi-actor ODA table (EC Fedasil Finance non-fed) cash-by-year; residual after exposé aggregates,"
        "ODA L5 end-receivers opaque under 2.35bn total; efficiency/concentration claims unverified,6,"
        "FOD Buitenlandse Zaken DGD / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_oda_partner_l5.md,ready,2026-07-29,,,,,,"
        "cmt_oda_be_path_2022_26|lb_dgd_vlk_1_04bn,2026-07-29T09:00:00Z,2026-07-29T09:00:00Z,"
        "tick540 human send; not sent\n"
    )

# research_queue
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
text = text.replace(
    "rq_531,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
    "rq_531,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    1,
)
text = text.replace(
    "Spawned tick539 after primary dept Tables1-7; progress@540 next tick; rq_116 deferred",
    "tick540: ODA dual+debt financing+progress@540; spawn rq_532; rq_116 deferred",
    1,
)
if "rq_532," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_532,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-29T09:00:00Z,,Spawned tick540 after ODA+debt+progress; next hole-fill; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_531,540,no,"
    "Tick540 ODA 2.35bn 0.35pctGNI dual DGD/EC/Fedasil + fed debt 601bn interest 12.34bn gross fin 59.7bn; "
    "progress@540 done; next prio5 rq_532; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

# inventory counts for progress file
def count_rows(name):
    with open(root / name, encoding="utf-8", newline="", errors="replace") as f:
        return sum(1 for _ in csv.reader(f)) - 1

with open(root / "foi_queue.csv", encoding="utf-8", newline="", errors="replace") as f:
    foi_rows = list(csv.DictReader(f))
st = Counter((r.get("status") or "").strip() for r in foi_rows)
ready = st.get("ready", 0)
answered = st.get("answered", 0)

inv = {
    "budgets": count_rows("budgets.csv"),
    "commitments": count_rows("commitments.csv"),
    "leaderboard": count_rows("leaderboard.csv"),
    "entities": count_rows("entities.csv"),
    "sources": count_rows("sources.csv"),
    "foi_total": len(foi_rows),
    "foi_ready": ready,
    "foi_answered": answered,
    "rq": count_rows("research_queue.csv"),
}

print("OK tick540 research")
print("sources +2 budgets +", len(buds), "cmt +", len(cmts), "lb +", len(lbs))
print("inventory", inv)

# write inventory for progress template
(root / "raw" / "_tmp_tick540_inv.txt").write_text(repr(inv), encoding="utf-8")

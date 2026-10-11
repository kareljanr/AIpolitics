#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ENT = "nv_pmbs"
SRC = "src_pmbs_jr2025_nbb"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
rows = [
    f"bud_pmbs_assets_2025,{ENT},2025,1600122,,,executed,{SRC},strong,2025 assets 1600122 VOL-kap 20/58; tick1413; primary official NBB WVV; table match not used as source",
    f"bud_pmbs_assets_2024,{ENT},2024,1608777,,,executed,{SRC},strong,2024 assets 1608777 comparative; tick1413; primary official NBB WVV 20/58",
    f"bud_pmbs_fixed_2025,{ENT},2025,1058150,,,executed,{SRC},strong,2025 vaste activa 1058150 unchanged; tick1413; primary official NBB WVV 21/28",
    f"bud_pmbs_mva_2025,{ENT},2025,1058150,,,executed,{SRC},strong,2025 MVA overige 1058150 only; tick1413; primary official NBB WVV 22/27/26",
    f"bud_pmbs_mva_aanschaf_2025,{ENT},2025,42326000,,,executed,{SRC},strong,2025 MVA aanschafwaarde 42326000 unchanged; tick1413; primary official NBB WVV 8195",
    f"bud_pmbs_mva_afschr_2025,{ENT},2025,41267850,,,executed,{SRC},strong,2025 MVA afschr 41267850 unchanged; tick1413; primary official NBB WVV 8325",
    f"bud_pmbs_current_2025,{ENT},2025,541972,,,executed,{SRC},strong,2025 vlottend 541972 vs 550627; tick1413; primary official NBB WVV 29/58",
    f"bud_pmbs_strecv_2025,{ENT},2025,9347,,,executed,{SRC},strong,2025 ST vorderingen 9347 vs 7427; tick1413; primary official NBB WVV 40/41",
    f"bud_pmbs_trade_recv_2025,{ENT},2025,204,,,executed,{SRC},strong,2025 handelsvorderingen 204; tick1413; primary official NBB WVV 40",
    f"bud_pmbs_othrecv_2025,{ENT},2025,9143,,,executed,{SRC},strong,2025 overige vorderingen 9143 vs 7427 counterpart unpublished; tick1413; primary official NBB WVV 41",
    f"bud_pmbs_invest_2025,{ENT},2025,522,,,executed,{SRC},strong,2025 geldbeleggingen termijn <1m 522 vs 518; tick1413; primary official NBB WVV 50/53",
    f"bud_pmbs_cash_2025,{ENT},2025,528367,,,executed,{SRC},strong,2025 liquide middelen 528367 DROP vs 542681; tick1413; primary official NBB WVV 54/58",
    f"bud_pmbs_cash_2024,{ENT},2024,542681,,,executed,{SRC},strong,2024 liquide middelen 542681 comparative; tick1413; primary official NBB WVV 54/58",
    f"bud_pmbs_prepaid_2025,{ENT},2025,3737,,,executed,{SRC},strong,2025 overlopend actief 3737 JUMP vs 1; tick1413; primary official NBB WVV 490/1",
    f"bud_pmbs_equity_2025,{ENT},2025,1599050,,,executed,{SRC},strong,2025 EV 1599050 unchanged; tick1413; primary official NBB WVV 10/15",
    f"bud_pmbs_kapitaal_2025,{ENT},2025,1000000,,,executed,{SRC},strong,2025 geplaatst kapitaal 1000000; tick1413; primary official NBB WVV 100",
    f"bud_pmbs_wett_reserve_2025,{ENT},2025,599050,,,executed,{SRC},strong,2025 wettelijke reserve 599050; tick1413; primary official NBB WVV 130",
    f"bud_pmbs_debt_2025,{ENT},2025,1072,,,executed,{SRC},strong,2025 schulden 1072 DROP vs 9727; tick1413; primary official NBB WVV 17/49",
    f"bud_pmbs_debt_2024,{ENT},2024,9727,,,executed,{SRC},strong,2024 schulden 9727 comparative; tick1413; primary official NBB WVV 17/49",
    f"bud_pmbs_st_2025,{ENT},2025,1072,,,executed,{SRC},strong,2025 ST schulden 1072 no LT; tick1413; primary official NBB WVV 42/48",
    f"bud_pmbs_tax_pay_2025,{ENT},2025,322,,,executed,{SRC},strong,2025 belastingschulden 322 vs 2628; tick1413; primary official NBB WVV 450/3",
    f"bud_pmbs_othdebt_2025,{ENT},2025,750,,,executed,{SRC},strong,2025 overige schulden 750 vs 6132 counterpart unpublished; tick1413; primary official NBB WVV 47/48",
    f"bud_pmbs_omzet_2025,{ENT},2025,107101,,,executed,{SRC},strong,2025 omzet 107101; 6.10 category/geo empty; tick1413; primary official NBB WVV 70",
    f"bud_pmbs_omzet_2024,{ENT},2024,103825,,,executed,{SRC},strong,2024 omzet 103825 comparative; tick1413; primary official NBB WVV 70",
    f"bud_pmbs_diensten_2025,{ENT},2025,112337,,,executed,{SRC},strong,2025 diensten 112337 vs 109511 split unpublished; tick1413; primary official NBB WVV 61",
    f"bud_pmbs_diensten_2024,{ENT},2024,109511,,,executed,{SRC},strong,2024 diensten 109511 comparative; tick1413; primary official NBB WVV 61",
    f"bud_pmbs_bedrijfskosten_2025,{ENT},2025,112457,,,executed,{SRC},strong,2025 bedrijfskosten 112457 (diensten 112337 + andere 120); tick1413; primary official NBB WVV 60/66A",
    f"bud_pmbs_andere_kosten_2025,{ENT},2025,120,,,executed,{SRC},strong,2025 andere bedrijfskosten / bedrijfsbelastingen 120 vs 118; tick1413; primary official NBB WVV 640",
    f"bud_pmbs_expl_2025,{ENT},2025,-5356,,,executed,{SRC},strong,2025 expl -5356 vs -5804; tick1413; primary official NBB WVV 9901",
    f"bud_pmbs_expl_2024,{ENT},2024,-5804,,,executed,{SRC},strong,2024 expl -5804 comparative; tick1413; primary official NBB WVV 9901",
    f"bud_pmbs_finopbr_2025,{ENT},2025,7024,,,executed,{SRC},strong,2025 fin opbr 7024 (vlottend) vs 18369; tick1413; primary official NBB WVV 75",
    f"bud_pmbs_fincost_2025,{ENT},2025,206,,,executed,{SRC},strong,2025 fin kosten 206 andere; tick1413; primary official NBB WVV 65",
    f"bud_pmbs_tax_2025,{ENT},2025,390,,,executed,{SRC},strong,2025 belastingen 390 vs 2920; tick1413; primary official NBB WVV 67/77",
    f"bud_pmbs_pnl_2025,{ENT},2025,1072,,,executed,{SRC},strong,2025 PnL 1072 vs 9439 all as vergoeding inbreng; tick1413; primary official NBB WVV 9904",
    f"bud_pmbs_pnl_2024,{ENT},2024,9439,,,executed,{SRC},strong,2024 PnL 9439 comparative; tick1413; primary official NBB WVV 9904",
    f"bud_pmbs_div_2025,{ENT},2025,1072,,,executed,{SRC},strong,2025 vergoeding inbreng 1072 vs 8760; tick1413; primary official NBB WVV 694",
    f"bud_pmbs_capex_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 capex aanschaf empty 0; tick1413; primary official NBB WVV 8165",
    f"bud_pmbs_commissaris_2025,{ENT},2025,4356,,,executed,{SRC},strong,2025 commissaris fee 4356 EY B160; tick1413; primary official NBB WVV 9505",
    f"bud_pmbs_presentiegeld_2025,{ENT},2025,5539,,,executed,{SRC},strong,2025 presentiegeld 5539.05 remuneratieverslag (9503 empty); tick1413; primary official NBB WVV 11",
    f"bud_pmbs_reis_2025,{ENT},2025,162,,,executed,{SRC},strong,2025 reisvergoedingen 162.13 remuneratieverslag; tick1413; primary official NBB WVV 11",
    f"bud_pmbs_svz_2025,{ENT},2025,864,,,executed,{SRC},strong,2025 SVZ zelfstandigen 863.70 remuneratieverslag; tick1413; primary official NBB WVV 11",
]
append_lf(DATA / "budgets.csv", rows)
print("budgets +41")

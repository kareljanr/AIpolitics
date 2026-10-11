#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_wstrt"
SRC = "src_wstrt_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_wstrt_assets_2025,{ENT},2025,97529158,,,executed,{SRC},strong,2025 assets 97529158 UP (was 73473843); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_current_2025,{ENT},2025,7549559,,,executed,{SRC},strong,2025 vlottend 7549559 (was 7006597); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_cash_2025,{ENT},2025,2036624,,,executed,{SRC},strong,2025 liquide middelen 2036624 UP (was 1573182); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_strecv_2025,{ENT},2025,758353,,,executed,{SRC},strong,2025 ST vorderingen 758353 (was 751518); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_trade_2025,{ENT},2025,615092,,,executed,{SRC},strong,2025 handelsvorderingen 615092 (was 664492); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_othrecv_2025,{ENT},2025,143261,,,executed,{SRC},strong,2025 overige ST vorderingen 143261 (was 87027); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_voorr_2025,{ENT},2025,4027900,,,executed,{SRC},strong,2025 voorraden 4027900 DROP (was 4353551); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_prepaid_2025,{ENT},2025,726681,,,executed,{SRC},strong,2025 overlopend actief 726681 (was 328345); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_fixed_2025,{ENT},2025,89979599,,,executed,{SRC},strong,2025 vaste activa 89979599 UP (was 66467246); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 0 empty; tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_mva_2025,{ENT},2025,89963360,,,executed,{SRC},strong,2025 MVA 89963360 UP (was 66447210; terreinen/gebouwen 88480680); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_fva_2025,{ENT},2025,16239,,,executed,{SRC},strong,2025 FVA 16239 (was 20036); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_equity_2025,{ENT},2025,15514356,,,executed,{SRC},strong,2025 eigen vermogen 15514356 UP (was 11815535); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_inbreng_2025,{ENT},2025,20000,,,executed,{SRC},strong,2025 inbreng 20000 onbeschikbaar (was 18317); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_reserves_2025,{ENT},2025,14137368,,,executed,{SRC},strong,2025 reserves 14137368 (was 10840176); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_kapsubs_2025,{ENT},2025,4452943,,,executed,{SRC},strong,2025 kapitaalsubsidies 4452943 (was 3292737); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_voorz_2025,{ENT},2025,314809,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 314809 (uitgestelde 314809); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_debt_2025,{ENT},2025,81699993,,,executed,{SRC},strong,2025 schulden 81699993 UP (was 61402084; LT 76514884 + ST 4531757 + deferred 653352); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_ltdebt_2025,{ENT},2025,76514884,,,executed,{SRC},strong,2025 LT schulden 76514884 UP (was 56262977; fin krediet 75672267); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_stdebt_2025,{ENT},2025,4531757,,,executed,{SRC},strong,2025 ST schulden 4531757 (was 4796628; 42 3171045 + leveranciers 242921); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_lev_2025,{ENT},2025,242921,,,executed,{SRC},strong,2025 leveranciers 242921 DROP (was 816941); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_deferred_2025,{ENT},2025,653352,,,executed,{SRC},strong,2025 overlopend passief 653352 (was 342479); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_omzet_2025,{ENT},2025,7325986,,,executed,{SRC},strong,2025 omzet 70 7325986 UP (was 5633706; VKT no 6.10 split); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_diensten_2025,{ENT},2025,4260712,,,executed,{SRC},strong,2025 handelsgoederen+diensten 60/61 4260712 (was 3003012; VKT combined); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_pers_2025,{ENT},2025,1536245,,,executed,{SRC},strong,2025 pers 62 1536245; 17.1 VTE vs 17.2; 25893 uur; YE 21 / 18.2 VTE; tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_afschr_2025,{ENT},2025,2707648,,,executed,{SRC},strong,2025 afschrijvingen 2707648 (was 2056283); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_expl_2025,{ENT},2025,-421712,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -421712 (was -298495); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_finopbr_2025,{ENT},2025,1583727,,,executed,{SRC},strong,2025 financiele opbrengsten 1583727 (interestsubs 1576284); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_finkost_2025,{ENT},2025,2002874,,,executed,{SRC},strong,2025 financiele kosten 2002874 (was 1304212); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_pnl_2025,{ENT},2025,-835178,,,executed,{SRC},strong,2025 PnL 9904 -835178 (was -699553); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0; tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_capex_2025,{ENT},2025,31842106,,,executed,{SRC},strong,2025 capex MVA aanschaf 8169 31842106 JUMP; tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_in_aanbouw_2025,{ENT},2025,1370567,,,executed,{SRC},strong,2025 activa in aanbouw 1370567 DROP (was 5140478); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_krediet_2025,{ENT},2025,75672267,,,executed,{SRC},strong,2025 LT kredietinstellingen 75672267 UP (was 55626014); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_terreinen_2025,{ENT},2025,88480680,,,executed,{SRC},strong,2025 terreinen en gebouwen 88480680 UP (was 61164278); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_interestsubs_2025,{ENT},2025,1576284,,,executed,{SRC},strong,2025 interestsubsidies 753/9078 1576284 (was 850853); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_brutomarge_2025,{ENT},2025,4588107,,,executed,{SRC},strong,2025 brutomarge 9900 4588107 (was 3669702); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_overgedragen_2025,{ENT},2025,-3095955,,,executed,{SRC},strong,2025 overgedragen verlies 14 -3095955 (was -2335696); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_nrec_opbr_2025,{ENT},2025,512470,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 512470 (was 315679); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_nrec_kost_2025,{ENT},2025,254821,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 254821 (was 273); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_andere_2025,{ENT},2025,436954,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 436954 (was 519009); tick1495; primary official NBB WVV VKT",
    f"bud_wstrt_meubilair_2025,{ENT},2025,107510,,,executed,{SRC},strong,2025 meubilair en rollend materieel 107510 (was 142454); tick1495; primary official NBB WVV VKT",
]
import csv, io
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

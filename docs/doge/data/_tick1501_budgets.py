#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_prvd"
SRC = "src_prvd_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_prvd_assets_2025,{ENT},2025,228332050,,,executed,{SRC},strong,2025 assets 228332050 UP (was 201258588); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_current_2025,{ENT},2025,9587863,,,executed,{SRC},strong,2025 vlottend 9587863 (was 8793020); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_cash_2025,{ENT},2025,5321913,,,executed,{SRC},strong,2025 liquide middelen 5321913 UP (was 4421330); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_strecv_2025,{ENT},2025,1240787,,,executed,{SRC},strong,2025 ST vorderingen 1240787 (was 1419083); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_trade_2025,{ENT},2025,1007920,,,executed,{SRC},strong,2025 handelsvorderingen 1007920 DROP (was 1151380); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_othrecv_2025,{ENT},2025,232867,,,executed,{SRC},strong,2025 overige ST vorderingen 232867 (was 267703); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_ltrecv_2025,{ENT},2025,233315,,,executed,{SRC},strong,2025 LT vorderingen 233315 (was 172035); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_voorr_2025,{ENT},2025,1473474,,,executed,{SRC},strong,2025 voorraden 1473474 DROP (was 2031121; onroerend 35); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_prepaid_2025,{ENT},2025,1318374,,,executed,{SRC},strong,2025 overlopend actief 1318374 (was 749451); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_fixed_2025,{ENT},2025,218744187,,,executed,{SRC},strong,2025 vaste activa 218744187 UP (was 192465568); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_mva_2025,{ENT},2025,218741048,,,executed,{SRC},strong,2025 MVA 218741048 UP (was 192462429; terreinen/gebouwen 212253871); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_fva_2025,{ENT},2025,3139,,,executed,{SRC},strong,2025 FVA 3139 stable (was 3139); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_equity_2025,{ENT},2025,29021932,,,executed,{SRC},strong,2025 eigen vermogen 29021932 UP (was 24139796); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_inbreng_2025,{ENT},2025,30015,,,executed,{SRC},strong,2025 inbreng 30015 onbeschikbaar (was 18236); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_reserves_2025,{ENT},2025,18052758,,,executed,{SRC},strong,2025 reserves 18052758 (was 14689890); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_kapsubs_2025,{ENT},2025,10939159,,,executed,{SRC},strong,2025 kapitaalsubsidies 10939159 (was 9431670); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_voorz_2025,{ENT},2025,3383093,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 3383093 (uitgestelde 532435); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_debt_2025,{ENT},2025,195927025,,,executed,{SRC},strong,2025 schulden 195927025 UP (was 174152569; LT 180311874 + ST 14730975 + deferred 884176); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_ltdebt_2025,{ENT},2025,180311874,,,executed,{SRC},strong,2025 LT schulden 180311874 UP (was 158588358; fin krediet 172755477); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_stdebt_2025,{ENT},2025,14730975,,,executed,{SRC},strong,2025 ST schulden 14730975 (was 14791012; 42 9732781 + leveranciers 1332627); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_lev_2025,{ENT},2025,1332627,,,executed,{SRC},strong,2025 leveranciers 1332627 DROP (was 1785468); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_deferred_2025,{ENT},2025,884176,,,executed,{SRC},strong,2025 overlopend passief 884176 (was 773199); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_omzet_2025,{ENT},2025,20807498,,,executed,{SRC},strong,2025 omzet 70 20807498 DROP (was 20921943); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_diensten_2025,{ENT},2025,9020541,,,executed,{SRC},strong,2025 diensten 61 9020541 DROP (was 9492446); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_pers_2025,{ENT},2025,3571584,,,executed,{SRC},strong,2025 pers 62 3571584 UP; 39.1 VTE vs 38.6; YE 44; tick1501; primary official NBB WVV VOL",
    f"bud_prvd_afschr_2025,{ENT},2025,6778546,,,executed,{SRC},strong,2025 afschrijvingen 6778546 (was 6108634); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_expl_2025,{ENT},2025,2929638,,,executed,{SRC},strong,2025 bedrijfswinst 9901 2929638 (was 3948877); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_finopbr_2025,{ENT},2025,672205,,,executed,{SRC},strong,2025 financiele opbrengsten 672205 (was 872896); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_finkost_2025,{ENT},2025,1873891,,,executed,{SRC},strong,2025 financiele kosten 1873891 (was 2264026); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_pnl_2025,{ENT},2025,1625580,,,executed,{SRC},strong,2025 PnL 9904 1625580 DROP (was 2449202); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 empty; tick1501; primary official NBB WVV VOL",
    f"bud_prvd_capex_2025,{ENT},2025,92686585,,,executed,{SRC},strong,2025 capex MVA aanschaf 8161+8162+8163+8166 92686585; tick1501; primary official NBB WVV VOL",
    f"bud_prvd_in_aanbouw_2025,{ENT},2025,6171593,,,executed,{SRC},strong,2025 activa in aanbouw 6171593 (was 6224623); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_krediet_2025,{ENT},2025,172755477,,,executed,{SRC},strong,2025 LT kredietinstellingen 172755477 UP (was 151263203); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_terreinen_2025,{ENT},2025,212253871,,,executed,{SRC},strong,2025 terreinen en gebouwen 212253871 UP (was 185836539); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_explsubs_2025,{ENT},2025,1180949,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 1180949 (was 1024919); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_nrec_opbr_2025,{ENT},2025,2639855,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 2639855 (was 2156056); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_nrec_kost_2025,{ENT},2025,19345,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 19345; tick1501; primary official NBB WVV VOL",
    f"bud_prvd_andere_2025,{ENT},2025,1818830,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 1818830 UP (was 1583915); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_meubilair_2025,{ENT},2025,307356,,,executed,{SRC},strong,2025 meubilair en rollend materieel 307356 (was 401267); tick1501; primary official NBB WVV VOL",
    f"bud_prvd_bestuur_2025,{ENT},2025,22635,,,executed,{SRC},strong,2025 bestuurders 9503 22635; commissaris 9505 21502 + extra 12100; tick1501; primary official NBB WVV VOL",
    f"bud_prvd_interim_2025,{ENT},2025,377727,,,executed,{SRC},strong,2025 interim 617 377727 / 4 VTE (was 164393 / 2.4); tick1501; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

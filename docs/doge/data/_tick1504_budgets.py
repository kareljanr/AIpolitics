#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_dnkm"
SRC = "src_dnkm_jr2025_nbb"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_dnkm_assets_2025,{ENT},2025,129317196,,,executed,{SRC},strong,2025 assets 129317196 DROP (was 129938861); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_current_2025,{ENT},2025,4375949,,,executed,{SRC},strong,2025 vlottend 4375949 UP (was 3479369); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_cash_2025,{ENT},2025,2718970,,,executed,{SRC},strong,2025 liquide middelen 2718970 UP (was 1275234); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_strecv_2025,{ENT},2025,436627,,,executed,{SRC},strong,2025 ST vorderingen 436627 (was 282383); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_trade_2025,{ENT},2025,205944,,,executed,{SRC},strong,2025 handelsvorderingen 205944 UP (was 123192); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_othrecv_2025,{ENT},2025,230682,,,executed,{SRC},strong,2025 overige ST vorderingen 230682 (was 159190); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_voorr_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 voorraden 0 empty; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_prepaid_2025,{ENT},2025,1029350,,,executed,{SRC},strong,2025 overlopend actief 1029350 DROP (was 1171704); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_fixed_2025,{ENT},2025,124941247,,,executed,{SRC},strong,2025 vaste activa 124941247 DROP (was 126459491); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_mva_2025,{ENT},2025,124685977,,,executed,{SRC},strong,2025 MVA 124685977 DROP (was 126254084; terreinen/gebouwen 116077625); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_fva_2025,{ENT},2025,195940,,,executed,{SRC},strong,2025 FVA 195940 stable (was 195940); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_equity_2025,{ENT},2025,19508599,,,executed,{SRC},strong,2025 eigen vermogen 19508599 UP (was 18558787); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_inbreng_2025,{ENT},2025,689894,,,executed,{SRC},strong,2025 inbreng 689894 onbeschikbaar (was 681271); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_reserves_2025,{ENT},2025,12238658,,,executed,{SRC},strong,2025 reserves 12238658 UP (was 10475692); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_kapsubs_2025,{ENT},2025,6580047,,,executed,{SRC},strong,2025 kapitaalsubsidies 6580047 DROP (was 7401825); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_voorz_2025,{ENT},2025,574752,,,executed,{SRC},strong,2025 voorzieningen+uitgestelde belasting 574752 (herstel 180775; uitgestelde 393977); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_debt_2025,{ENT},2025,109233846,,,executed,{SRC},strong,2025 schulden 109233846 DROP (was 110935758; LT 102838049 + ST 5880136 + deferred 515661); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_ltdebt_2025,{ENT},2025,102838049,,,executed,{SRC},strong,2025 LT schulden 102838049 DROP (was 104728984; fin krediet 95707198); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_stdebt_2025,{ENT},2025,5880136,,,executed,{SRC},strong,2025 ST schulden 5880136 UP (was 5659452; 42 4308999 + leveranciers 644450); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_lev_2025,{ENT},2025,644450,,,executed,{SRC},strong,2025 leveranciers 644450 DROP (was 1099906); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_deferred_2025,{ENT},2025,515661,,,executed,{SRC},strong,2025 overlopend passief 515661 DROP (was 547322); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_omzet_2025,{ENT},2025,7793810,,,executed,{SRC},strong,2025 omzet 70 7793810 DROP (was 9603459); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_diensten_2025,{ENT},2025,2117459,,,executed,{SRC},strong,2025 diensten 61 2117459 UP (was 2078129); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_pers_2025,{ENT},2025,1372325,,,executed,{SRC},strong,2025 pers 62 1372325 UP; 18.3 VTE vs 17.6; YE 19; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_afschr_2025,{ENT},2025,3544098,,,executed,{SRC},strong,2025 afschrijvingen 3544098 DROP (was 3575875); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_expl_2025,{ENT},2025,1225025,,,executed,{SRC},strong,2025 bedrijfswinst 9901 1225025 vs 871906; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_finopbr_2025,{ENT},2025,1590745,,,executed,{SRC},strong,2025 financiele opbrengsten 1590745 (was 1532918); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_finkost_2025,{ENT},2025,1973032,,,executed,{SRC},strong,2025 financiele kosten 1973032 (was 1971332); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_pnl_2025,{ENT},2025,853059,,,executed,{SRC},strong,2025 PnL 9904 853059 vs 445678; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 empty; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_capex_2025,{ENT},2025,42448162,,,executed,{SRC},strong,2025 capex MVA aanschaf 8161+8162+8163+8166 42448162; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_in_aanbouw_2025,{ENT},2025,2545818,,,executed,{SRC},strong,2025 activa in aanbouw 2545818 DROP (was 5403985); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_krediet_2025,{ENT},2025,95707198,,,executed,{SRC},strong,2025 LT kredietinstellingen 95707198 DROP (was 97486398); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_terreinen_2025,{ENT},2025,116077625,,,executed,{SRC},strong,2025 terreinen en gebouwen 116077625 UP (was 114712316); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_explsubs_2025,{ENT},2025,149163,,,executed,{SRC},strong,2025 exploitatiesubsidies 740 149163 DROP (was 210780); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_nrec_opbr_2025,{ENT},2025,814605,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 814605 (was 264609); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_nrec_kost_2025,{ENT},2025,44835,,,executed,{SRC},strong,2025 niet-recurrente bedrijfskosten 66A 44835; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_andere_2025,{ENT},2025,541324,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 541324 (was 553403); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_meubilair_2025,{ENT},2025,107658,,,executed,{SRC},strong,2025 meubilair en rollend materieel 107658 (was 83962); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_bestuur_2025,{ENT},2025,29126,,,executed,{SRC},strong,2025 bestuurders 9503 29126; commissaris 9505 9000 + extra 2625 + belastingadvies 1113; tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_iva_2025,{ENT},2025,59330,,,executed,{SRC},strong,2025 IVA 59330 UP (was 9467); tick1504; primary official NBB WVV VOL",
    f"bud_dnkm_geldbeleg_2025,{ENT},2025,191002,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 191002 DROP (was 750050; eigen aandelen 191002); tick1504; primary official NBB WVV VOL",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_crlf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

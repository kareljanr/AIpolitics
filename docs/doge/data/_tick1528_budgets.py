#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwrv"
SRC = "src_cwrv_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwrv_assets_2025,{ENT},2025,9362853,,,executed,{SRC},strong,2025 assets 9362853 DROP (was 10151833); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_vaste_2025,{ENT},2025,7169547,,,executed,{SRC},strong,2025 vaste activa 21/28 7169547 DROP (was 7385631); IVA 21 35046 JUMP; FVA 28 6408 JUMP; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_mva_2025,{ENT},2025,7128093,,,executed,{SRC},strong,2025 MVA 22/27 7128093 DROP (was 7384975); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_gebouwen_2025,{ENT},2025,6871851,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 6871851 DROP (was 7105122); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_install_2025,{ENT},2025,32545,,,executed,{SRC},strong,2025 installaties 23 32545 DROP (was 50201); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_meubilair_2025,{ENT},2025,162373,,,executed,{SRC},strong,2025 meubilair 24 162373 DROP (was 197362); leasing 25 empty; overige 26 17896 DROP; in aanbouw 27 43428 JUMP; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_iva_2025,{ENT},2025,35046,,,executed,{SRC},strong,2025 IVA 21 35046 JUMP (was 98; aanschaffingen 8021 36304); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_fva_2025,{ENT},2025,6408,,,executed,{SRC},strong,2025 FVA 28 6408 JUMP (aandelen 284 558 + borg 285/8 5850); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_current_2025,{ENT},2025,2193306,,,executed,{SRC},strong,2025 vlottende 29/58 2193306 DROP (was 2766202); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_strecv_2025,{ENT},2025,237473,,,executed,{SRC},strong,2025 ST vorderingen 40/41 237473 (trade 90580 + other 146893); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_handelsrecv_2025,{ENT},2025,90580,,,executed,{SRC},strong,2025 handelsvorderingen 40 90580 DROP (was 99255); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_otherrecv_2025,{ENT},2025,146893,,,executed,{SRC},strong,2025 overige ST 41 146893 JUMP (was 48604); LT other 291 empty; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_beleg_2025,{ENT},2025,1500401,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1500401 DROP (was 2000400); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_cash_2025,{ENT},2025,312739,,,executed,{SRC},strong,2025 liquide middelen 54/58 312739 DROP (was 507300); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_prepaid_2025,{ENT},2025,142693,,,executed,{SRC},strong,2025 overlopende 490/1 142693 UP (was 110643); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_equity_2025,{ENT},2025,5744350,,,executed,{SRC},strong,2025 eigen vermogen 10/15 5744350 DROP (was 5897107); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_fondsen_2025,{ENT},2025,12500,,,executed,{SRC},strong,2025 fondsen 10 12500 stable; bestemde 13 1419358 UP; overgedragen 14 717970; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_bestemde_2025,{ENT},2025,1419358,,,executed,{SRC},strong,2025 bestemde fondsen 13 1419358 UP (was 1407801; 691 11558); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_kapsubs_2025,{ENT},2025,3594522,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 3594522 DROP (was 3758836); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_prov_2025,{ENT},2025,54058,,,executed,{SRC},strong,2025 voorzieningen 16 54058 stable (overige 164/5 54058); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_debt_2025,{ENT},2025,3564445,,,executed,{SRC},strong,2025 schulden 17/49 3564445 DROP (was 4200668); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_ltdebt_2025,{ENT},2025,1661064,,,executed,{SRC},strong,2025 LT schulden 17 1661064 DROP (krediet 173 1661064 was 1896780); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_stdebt_2025,{ENT},2025,1714178,,,executed,{SRC},strong,2025 ST schulden 42/48 1714178 DROP (was 1748356; current portion 235716 / lev 199121 / vooruit 126267 / taxsoc 1054199 / other 98875); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_lev_2025,{ENT},2025,199121,,,executed,{SRC},strong,2025 leveranciers 440/4 199121 DROP (was 261562); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_vooruit_2025,{ENT},2025,126267,,,executed,{SRC},strong,2025 vooruitbetalingen 46 126267 JUMP (was 23009); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_taxsoc_2025,{ENT},2025,1054199,,,executed,{SRC},strong,2025 tax/soc 45 1054199 DROP (tax 69791 + bezold 984408 was 1081967); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_otherst_2025,{ENT},2025,98875,,,executed,{SRC},strong,2025 overige ST 48 98875 DROP (was 146102); overlopend 492/3 189203 DROP was 555532; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_opbr_2025,{ENT},2025,8432403,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 8432403 DROP (was 9052754); annual envelope; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_omzet_2025,{ENT},2025,371409,,,executed,{SRC},strong,2025 omzet 70 371409 UP (was 277826); 6.9 category/geo empty; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_subs_2025,{ENT},2025,7780184,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 7780184 DROP (731 15823 + 733 7764361); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_subs733_2025,{ENT},2025,7764361,,,executed,{SRC},strong,2025 subsidies 733 7764361 DROP (was 8682353); schenkingen 731 15823; lidgelden 730 empty; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_andere74_2025,{ENT},2025,280810,,,executed,{SRC},strong,2025 andere 74 280810 JUMP (was 79046); nrec 76A empty (was 1667); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_diensten_2025,{ENT},2025,965337,,,executed,{SRC},strong,2025 diensten 61 965337 DROP (was 1016650); handelsgoederen 60 67512; uitzend 617 empty (was 36000); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_pers_2025,{ENT},2025,7006469,,,executed,{SRC},strong,2025 pers 62 7006469 / 95.1 VTE DROP (was 7018228 / 96.3); YE 128 was 131 / 135075 uur; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_afschr_2025,{ENT},2025,329859,,,executed,{SRC},strong,2025 afschrijvingen 630 329859 (was 337718); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_expl_2025,{ENT},2025,-9004,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -9004 LOSS (was +634632); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_finopbr_2025,{ENT},2025,48833,,,executed,{SRC},strong,2025 financiele opbrengsten 75 48833 (was 49690; vlottend 751 48506); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_finkost_2025,{ENT},2025,28271,,,executed,{SRC},strong,2025 financiele kosten 65 28271 (schulden 26109); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_pnl_2025,{ENT},2025,11558,,,executed,{SRC},strong,2025 winst 9904 11558 DROP (was 661044); tax 67/77 empty; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; uit te keren winst empty; 691 11558 naar bestemde); tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_capex_2025,{ENT},2025,107925,,,executed,{SRC},strong,2025 capex IVA 8021 36304 + MVA 8161 28193 + 8166 43428 = 107925; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
    f"bud_cwrv_commissaris_2025,{ENT},2025,8627,,,executed,{SRC},strong,2025 commissaris 9505 8627; VGD Bedrijfsrevisoren BV B00150 via Roose Bart A02143; tick1528; primary official NBB WVV VOL-VZW 2026-00090859",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

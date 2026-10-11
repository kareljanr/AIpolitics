#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgad"
SRC = "src_cgad_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgad_assets_2025,{ENT},2025,9833698,,,executed,{SRC},strong,2025 assets 9833698 UP (was 9493367); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_opricht_2025,{ENT},2025,863,,,executed,{SRC},strong,2025 oprichtingskosten 20 863 (was 1036); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_vaste_2025,{ENT},2025,4725018,,,executed,{SRC},strong,2025 vaste activa 21/28 4725018 DROP (was 4868806); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_iva_2025,{ENT},2025,2520,,,executed,{SRC},strong,2025 IVA 21 2520 (was 92; aanschaf 8022 3150); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_mva_2025,{ENT},2025,4694420,,,executed,{SRC},strong,2025 MVA 22/27 4694420 DROP (was 4840636); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_gebouwen_2025,{ENT},2025,4589448,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 4589448 (was 4742793); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_install_2025,{ENT},2025,67849,,,executed,{SRC},strong,2025 installaties 23 67849 (was 59358); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_meubilair_2025,{ENT},2025,37123,,,executed,{SRC},strong,2025 meubilair 24 37123 (was 38484); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_fva_2025,{ENT},2025,28078,,,executed,{SRC},strong,2025 FVA 28 28078 stable; leasing 25 empty; in aanbouw 27 empty; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_current_2025,{ENT},2025,5107817,,,executed,{SRC},strong,2025 vlottende 29/58 5107817 UP (was 4623526); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_strecv_2025,{ENT},2025,2169207,,,executed,{SRC},strong,2025 ST vorderingen 40/41 2169207 (trade 1295655 + other 873552); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_cash_2025,{ENT},2025,2905244,,,executed,{SRC},strong,2025 liquide middelen 54/58 2905244 JUMP (was 2170012); beleggingen 50/53 empty; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_prepaid_2025,{ENT},2025,33366,,,executed,{SRC},strong,2025 overlopend actief 490/1 33366 (verzekeringen); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_equity_2025,{ENT},2025,7390848,,,executed,{SRC},strong,2025 eigen vermogen 10/15 7390848 UP (was 6852216); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_fondsen_2025,{ENT},2025,1938556,,,executed,{SRC},strong,2025 fondsen 10 1938556 (begin 691369 + permanente 1247186); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_bestemde_2025,{ENT},2025,4355670,,,executed,{SRC},strong,2025 bestemde fondsen 13 4355670 JUMP (was 3312855; toevoeging 1084416; infra 3832633 / sociaal 523038); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_overgedragen_2025,{ENT},2025,100000,,,executed,{SRC},strong,2025 overgedragen winst 14 100000 (was 544457); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_kapsubs_2025,{ENT},2025,996622,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 996622 (was 1056348); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_voorz_2025,{ENT},2025,98255,,,executed,{SRC},strong,2025 voorzieningen 16 98255 (all pensions 160; was 87633); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_debt_2025,{ENT},2025,2344595,,,executed,{SRC},strong,2025 schulden 17/49 2344595 DROP (was 2553518); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_ltdebt_2025,{ENT},2025,145611,,,executed,{SRC},strong,2025 LT schulden 17 145611 (all krediet 173; was 178188); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_stdebt_2025,{ENT},2025,2036214,,,executed,{SRC},strong,2025 ST schulden 42/48 2036214 (was 2082287); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_lev_2025,{ENT},2025,388973,,,executed,{SRC},strong,2025 leveranciers 440/4 388973 DROP (was 543949); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_taxsoc_2025,{ENT},2025,1572760,,,executed,{SRC},strong,2025 tax/soc 45 1572760 (tax 8533 + bezold 1564227); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_opbr_2025,{ENT},2025,13798629,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 13798629; annual envelope; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_omzet_2025,{ENT},2025,597815,,,executed,{SRC},strong,2025 omzet 70 597815 UP (was 546766); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_lidgeld_2025,{ENT},2025,13172501,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 13172501 UP (was 12209201; all 733 subsidies); CGG-dotatie; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_andere_opbr_2025,{ENT},2025,28313,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 28313 (was 22518); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_pers_2025,{ENT},2025,11157856,,,executed,{SRC},strong,2025 pers 62 11157856 / 121.1 VTE (was 10663969 / 119); YE 170 / YE VTE 122.9; 169577 uur; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_diensten_2025,{ENT},2025,1641099,,,executed,{SRC},strong,2025 diensten 61 1641099 (was 1406626); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_afschr_2025,{ENT},2025,242099,,,executed,{SRC},strong,2025 afschrijvingen 630 242099 (was 225076); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_voorz_kost_2025,{ENT},2025,10623,,,executed,{SRC},strong,2025 voorzieningen kost 635/9 10623 (was -19311); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_andere_2025,{ENT},2025,198023,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 198023 (was 172141); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_nrec_kost_2025,{ENT},2025,9486,,,executed,{SRC},strong,2025 nrec kosten 66A 9486 (was 1782); nrec 76A empty; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_bedrijfskost_2025,{ENT},2025,13259186,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 13259186 (was 12450283); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_expl_2025,{ENT},2025,539443,,,executed,{SRC},strong,2025 bedrijfswinst 9901 539443 (was 328202); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_finopbr_2025,{ENT},2025,64608,,,executed,{SRC},strong,2025 financiele opbrengsten 75 64608 (was 70749; kap.sub 40231); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_finkost_2025,{ENT},2025,5373,,,executed,{SRC},strong,2025 financiele kosten 65 5373 (was 6865); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_tax_2025,{ENT},2025,319,,,executed,{SRC},strong,2025 belastingen 67/77 319 (was 6927); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_pnl_2025,{ENT},2025,598359,,,executed,{SRC},strong,2025 winst 9904 598359 (was 385159); tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_capex_2025,{ENT},2025,94989,,,executed,{SRC},strong,2025 capex 8161+8162+8163 94989 (43819+32002+19168); 8164+8165 empty; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
    f"bud_cgad_commissaris_2025,{ENT},2025,10257,,,executed,{SRC},strong,2025 commissaris Callens Vandelanotte B00083 fee 10257; tick1511; primary official NBB WVV VOL-VZW 2026-00188352",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

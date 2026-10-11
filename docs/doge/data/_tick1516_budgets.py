#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgkp"
SRC = "src_cgkp_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgkp_assets_2025,{ENT},2025,10466965,,,executed,{SRC},strong,2025 assets 10466965 DROP (was 10668365); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_vaste_2025,{ENT},2025,6398405,,,executed,{SRC},strong,2025 vaste activa 21/28 6398405 DROP (was 6723756); IVA 21 empty after full 11845 afschr; FVA 28 7255 DROP; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_mva_2025,{ENT},2025,6391150,,,executed,{SRC},strong,2025 MVA 22/27 6391150 DROP (was 6691808); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_gebouwen_2025,{ENT},2025,6136493,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 6136493 DROP (was 6441061); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_install_2025,{ENT},2025,82361,,,executed,{SRC},strong,2025 installaties 23 82361 (was 89805); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_meubilair_2025,{ENT},2025,172296,,,executed,{SRC},strong,2025 meubilair 24 172296 UP (was 160942); leasing 25 empty; overige 26 empty; in aanbouw 27 empty; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_fva_2025,{ENT},2025,7255,,,executed,{SRC},strong,2025 FVA 28 7255 DROP (was 31948; WV 8475 24693); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_current_2025,{ENT},2025,4068559,,,executed,{SRC},strong,2025 vlottende 29/58 4068559 UP (was 3944609); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_ltrecv_2025,{ENT},2025,1000,,,executed,{SRC},strong,2025 LT vorderingen 29 1000 (was 2000; all other 291); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_strecv_2025,{ENT},2025,2048257,,,executed,{SRC},strong,2025 ST vorderingen 40/41 2048257 (trade 809739 JUMP was 496232 + other 1238518 DROP was 1529768); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_handelsrecv_2025,{ENT},2025,809739,,,executed,{SRC},strong,2025 handelsvorderingen 40 809739 JUMP (was 496232); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_beleg_2025,{ENT},2025,302335,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 302335 JUMP (was empty); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_cash_2025,{ENT},2025,1534479,,,executed,{SRC},strong,2025 liquide middelen 54/58 1534479 DROP (was 1791315); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_prepaid_2025,{ENT},2025,182489,,,executed,{SRC},strong,2025 overlopend actief 490/1 182489 (was 125295); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_equity_2025,{ENT},2025,6409473,,,executed,{SRC},strong,2025 eigen vermogen 10/15 6409473 UP (was 5896738); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_fondsen_2025,{ENT},2025,442126,,,executed,{SRC},strong,2025 fondsen 10 442126 stable; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_bestemde_2025,{ENT},2025,1163762,,,executed,{SRC},strong,2025 bestemde fondsen 13 1163762 stable; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_overgedragen_2025,{ENT},2025,1926633,,,executed,{SRC},strong,2025 overgedragen 14 1926633 UP (was 1237665; + PnL 688968); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_kapsubs_2025,{ENT},2025,2876952,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 2876952 DROP (was 3053184); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_debt_2025,{ENT},2025,4057491,,,executed,{SRC},strong,2025 schulden 17/49 4057491 DROP (was 4771627); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_ltdebt_2025,{ENT},2025,1914074,,,executed,{SRC},strong,2025 LT schulden 17 1914074 (all krediet 172/3; was 1998309); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_stdebt_2025,{ENT},2025,2038635,,,executed,{SRC},strong,2025 ST schulden 42/48 2038635 (was 2344636; 42 86552 / lev 215944 / taxsoc 1536390 / other 199749 JUMP); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_lev_2025,{ENT},2025,215944,,,executed,{SRC},strong,2025 leveranciers 440/4 215944 DROP (was 781223); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_taxsoc_2025,{ENT},2025,1536390,,,executed,{SRC},strong,2025 tax/soc 45 1536390 (tax 270470 + bezold 1265920); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_otherst_2025,{ENT},2025,199749,,,executed,{SRC},strong,2025 overige ST 48 199749 JUMP (was 42661); overlopend passief 104782 DROP was 428682; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_bruto_2025,{ENT},2025,10124140,,,executed,{SRC},strong,2025 brutomarge 9900 10124140 UP (was 9164150); annual envelope VKT (omzet 70 empty; 73 empty); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_omzet_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 omzet 70 empty VKT; 73 empty; 60/61 empty; nrec 76A empty; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_pers_2025,{ENT},2025,8390551,,,executed,{SRC},strong,2025 pers 62 8390551 / 99.5 VTE (was 7871751 / 95.1); YE 142 / YE VTE 99.3; 134424 uur; PC 331; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_afschr_2025,{ENT},2025,418934,,,executed,{SRC},strong,2025 afschrijvingen 630 418934 (was 627814); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_andere_2025,{ENT},2025,563846,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 563846 (was 559605); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_expl_2025,{ENT},2025,750808,,,executed,{SRC},strong,2025 bedrijfswinst 9901 750808 JUMP (was 104979); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_finopbr_2025,{ENT},2025,3907,,,executed,{SRC},strong,2025 financiele opbrengsten 75 3907 (was 11770); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_finkost_2025,{ENT},2025,65747,,,executed,{SRC},strong,2025 financiele kosten 65 65747 JUMP (was 25335); tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_pnl_2025,{ENT},2025,688968,,,executed,{SRC},strong,2025 winst 9904 688968 JUMP (was 90526); tax 67/77 empty; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_capex_2025,{ENT},2025,118276,,,executed,{SRC},strong,2025 capex IVA 8029 11845 + MVA 8169 106431 = 118276; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
    f"bud_cgkp_gewaarborgd_2025,{ENT},2025,1788472,,,executed,{SRC},strong,2025 door BE overheidsinstellingen gewaarborgde schulden 9061 1788472; tick1516; primary official NBB WVV VKT-VZW 2026-00178615",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

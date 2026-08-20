#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_erfp"
SRC = "src_erfp_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_erfp_assets_2025,{ENT},2025,438711,,,executed,{SRC},strong,2025 assets 438711 UP (was 344552); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_vaste_2025,{ENT},2025,41434,,,executed,{SRC},strong,2025 vaste activa 21/28 41434 JUMP (was 25917); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_iva_2025,{ENT},2025,3989,,,executed,{SRC},strong,2025 IVA 21 3989 DROP (was 4306; aanschaffingen 8029 3581); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_mva_2025,{ENT},2025,35635,,,executed,{SRC},strong,2025 MVA 22/27 35635 JUMP (was 21051); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_install_2025,{ENT},2025,1379,,,executed,{SRC},strong,2025 installaties 23 1379 DROP (was 2432); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_meubilair_2025,{ENT},2025,34256,,,executed,{SRC},strong,2025 meubilair 24 34256 JUMP (was 18619); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_fva_2025,{ENT},2025,1810,,,executed,{SRC},strong,2025 FVA 28 1810 JUMP (was 560; aanschaffingen 8365 1250); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_current_2025,{ENT},2025,397277,,,executed,{SRC},strong,2025 vlottende 29/58 397277 UP (was 318635); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_strecv_2025,{ENT},2025,207001,,,executed,{SRC},strong,2025 ST vorderingen 40/41 207001 JUMP (was 67934); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_handelsrecv_2025,{ENT},2025,191912,,,executed,{SRC},strong,2025 handelsvorderingen 40 191912 JUMP (was 52934); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_otherrecv_2025,{ENT},2025,15089,,,executed,{SRC},strong,2025 overige ST 41 15089 (was 15000); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_beleg_2025,{ENT},2025,117476,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 117476 DROP (was 140641); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_cash_2025,{ENT},2025,61449,,,executed,{SRC},strong,2025 liquide middelen 54/58 61449 DROP (was 110060); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_prepaid_2025,{ENT},2025,11350,,,executed,{SRC},strong,2025 overlopende 490/1 11350 JUMP (was empty); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_equity_2025,{ENT},2025,140814,,,executed,{SRC},strong,2025 eigen vermogen 10/15 140814 DROP (was 141743; all overgedragen 14); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_debt_2025,{ENT},2025,297897,,,executed,{SRC},strong,2025 schulden 17/49 297897 JUMP (was 202809); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_stdebt_2025,{ENT},2025,171949,,,executed,{SRC},strong,2025 ST schulden 42/48 171949 JUMP (was 81983); LT 17 empty; tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_lev_2025,{ENT},2025,105313,,,executed,{SRC},strong,2025 leveranciers 440/4 105313 JUMP (was 13892); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_taxsoc_2025,{ENT},2025,66636,,,executed,{SRC},strong,2025 tax/soc 45 66636 (tax 15297 + bezold 51339 was 67187); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_accrued_2025,{ENT},2025,125948,,,executed,{SRC},strong,2025 overlopend 492/3 125948 UP (was 120826); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_bruto_2025,{ENT},2025,700561,,,executed,{SRC},strong,2025 brutomarge 9900 700561 DROP (was 739769); annual envelope (omzet 70 empty); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_omzet_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 omzet 70 empty; 60/61 empty; 73 split unpublished; tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_pers_2025,{ENT},2025,677959,,,executed,{SRC},strong,2025 pers 62 677959 / 7.8 VTE DROP (was 710790 / 8.4; YE 105 7.8 / 15382 uur; social 102 653291); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_afschr_2025,{ENT},2025,13491,,,executed,{SRC},strong,2025 afschrijvingen 630 13491 (was 11024); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_andere_2025,{ENT},2025,368,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 368 (was 364); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_expl_2025,{ENT},2025,8742,,,executed,{SRC},strong,2025 bedrijfswinst 9901 8742 DROP (was 17591); official 1-euro vs 700561-677959-13491-368=8743; tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_finopbr_2025,{ENT},2025,593,,,executed,{SRC},strong,2025 financiele opbrengsten 75 593 UP (was 346); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_finkost_2025,{ENT},2025,959,,,executed,{SRC},strong,2025 financiele kosten 65 959 (was 964); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_tax_2025,{ENT},2025,9304,,,executed,{SRC},strong,2025 belastingen 67/77 9304 (was 8092); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_pnl_2025,{ENT},2025,-929,,,executed,{SRC},strong,2025 verlies 9904 -929 LOSS (was +8882); official 1-euro vs 8376-9304=-928; tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (694/7 empty; 14 140814); tick1536; primary official NBB WVV VKT-kap 2026-00165556",
    f"bud_erfp_capex_2025,{ENT},2025,29009,,,executed,{SRC},strong,2025 capex IVA 8029 3581 + MVA 8169 24178 + FVA 8365 1250 = 29009; tick1536; primary official NBB WVV VKT-kap 2026-00165556",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgan"
SRC = "src_cgan_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgan_assets_2025,{ENT},2025,10657318,,,executed,{SRC},strong,2025 assets 10657318 UP (was 6426061); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_vaste_2025,{ENT},2025,4759882,,,executed,{SRC},strong,2025 vaste activa 21/28 4759882 UP (was 3642992); IVA 21 empty; FVA 28 71060; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_mva_2025,{ENT},2025,4688821,,,executed,{SRC},strong,2025 MVA 22/27 4688821 UP (was 3572182); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_gebouwen_2025,{ENT},2025,2349606,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 2349606 DROP (was 2415605); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_install_2025,{ENT},2025,56819,,,executed,{SRC},strong,2025 installaties 23 56819 DROP (was 61610); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_meubilair_2025,{ENT},2025,15646,,,executed,{SRC},strong,2025 meubilair 24 15646 DROP (was 20294); leasing 25 empty; overige 26 empty; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_inaanbouw_2025,{ENT},2025,2266750,,,executed,{SRC},strong,2025 in aanbouw 27 2266750 JUMP (was 1074672); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_fva_2025,{ENT},2025,71060,,,executed,{SRC},strong,2025 FVA 28 71060 (was 70810); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_current_2025,{ENT},2025,5897436,,,executed,{SRC},strong,2025 vlottende 29/58 5897436 JUMP (was 2783068); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_ltrecv_2025,{ENT},2025,1859107,,,executed,{SRC},strong,2025 LT vorderingen 29 1859107 JUMP (all other 291; was empty); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_strecv_2025,{ENT},2025,2447721,,,executed,{SRC},strong,2025 ST vorderingen 40/41 2447721 JUMP (trade 358136 + other 2089584 JUMP was 1086780); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_handelsrecv_2025,{ENT},2025,358136,,,executed,{SRC},strong,2025 handelsvorderingen 40 358136 UP (was 272050); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_otherrecv_2025,{ENT},2025,2089584,,,executed,{SRC},strong,2025 overige ST 41 2089584 JUMP (was 1086780); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_cash_2025,{ENT},2025,1540487,,,executed,{SRC},strong,2025 liquide middelen 54/58 1540487 UP (was 1272283); beleg 50/53 empty; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_prepaid_2025,{ENT},2025,50122,,,executed,{SRC},strong,2025 overlopende 490/1 50122 DROP (was 147962); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_equity_2025,{ENT},2025,8493688,,,executed,{SRC},strong,2025 eigen vermogen 10/15 8493688 UP (was 4902674); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_fondsen_2025,{ENT},2025,838818,,,executed,{SRC},strong,2025 fondsen 10 838818 stable; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_bestemde_2025,{ENT},2025,1490000,,,executed,{SRC},strong,2025 bestemde fondsen 13 1490000 JUMP (was 600000; 691 +890000); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_overgedragen_2025,{ENT},2025,1804147,,,executed,{SRC},strong,2025 overgedragen 14 1804147 DROP (was 2732980; 691 +890000); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_kapsubs_2025,{ENT},2025,4360723,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 4360723 JUMP (was 730876); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_debt_2025,{ENT},2025,2163630,,,executed,{SRC},strong,2025 schulden 17/49 2163630 UP (was 1523387); LT 17 empty; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_stdebt_2025,{ENT},2025,2163126,,,executed,{SRC},strong,2025 ST schulden 42/48 2163126 (was 1518523; lev 402027 / taxsoc 1704117 / other 56982); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_lev_2025,{ENT},2025,402027,,,executed,{SRC},strong,2025 leveranciers 440/4 402027 JUMP (was 85237); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_taxsoc_2025,{ENT},2025,1704117,,,executed,{SRC},strong,2025 tax/soc 45 1704117 (tax 416608 + bezold 1287509); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_otherst_2025,{ENT},2025,56982,,,executed,{SRC},strong,2025 overige ST 48 56982 (was 16183); overlopend 492/3 504; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_opbr_2025,{ENT},2025,10796084,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 10796084 UP (was 10429127); annual envelope (omzet 70 filled); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_omzet_2025,{ENT},2025,802604,,,executed,{SRC},strong,2025 omzet 70 802604 DROP (was 849092); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_lidgeld73_2025,{ENT},2025,9664811,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 9664811 UP (was 9268116); subsidies 733 9663086 / lidgelden 730 1725; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_andere74_2025,{ENT},2025,328670,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 328670 (was 311919); nrec 76A empty; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_diensten_2025,{ENT},2025,1369443,,,executed,{SRC},strong,2025 diensten 61 1369443 JUMP (was 1162977); handelsgoederen 60 3993; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_pers_2025,{ENT},2025,9295936,,,executed,{SRC},strong,2025 pers 62 9295936 / 108.7 VTE (was 8441883 / 102.4); YE 144 / 141036 uur; PC 330-331; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_afschr_2025,{ENT},2025,163921,,,executed,{SRC},strong,2025 afschrijvingen 630 163921 (was 176544); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_andere_2025,{ENT},2025,12166,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 12166 (was 13018); nrec 66A empty; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_expl_2025,{ENT},2025,-49373,,,executed,{SRC},strong,2025 bedrijfswinst 9901 -49373 LOSS (was 634595); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_finopbr_2025,{ENT},2025,14604,,,executed,{SRC},strong,2025 financiele opbrengsten 75 14604 (was 13695); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_finkost_2025,{ENT},2025,4064,,,executed,{SRC},strong,2025 financiele kosten 65 4064 (was 5884); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_pnl_2025,{ENT},2025,-38833,,,executed,{SRC},strong,2025 winst 9904 -38833 LOSS (was 642407); tax 67/77 empty; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_capex_2025,{ENT},2025,1280560,,,executed,{SRC},strong,2025 capex MVA 8161 75846 + 8162 12637 + 8166 1192077 = 1280560; tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
    f"bud_cgan_subsidies733_2025,{ENT},2025,9663086,,,executed,{SRC},strong,2025 subsidies 733 9663086 (of 73 9664811); tick1519; primary official NBB WVV VOL-VZW 2026-00103827",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

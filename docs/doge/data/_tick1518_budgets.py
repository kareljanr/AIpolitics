#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cglr"
SRC = "src_cglr_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cglr_assets_2025,{ENT},2025,6034498,,,executed,{SRC},strong,2025 assets 6034498 UP (was 5138399); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_vaste_2025,{ENT},2025,752611,,,executed,{SRC},strong,2025 vaste activa 21/28 752611 DROP (was 869337); IVA 21 empty; FVA 28 14124; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_mva_2025,{ENT},2025,738487,,,executed,{SRC},strong,2025 MVA 22/27 738487 DROP (was 855272); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_gebouwen_2025,{ENT},2025,639268,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 639268 DROP (was 721533); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_install_2025,{ENT},2025,17995,,,executed,{SRC},strong,2025 installaties 23 17995 DROP (was 35060); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_meubilair_2025,{ENT},2025,1476,,,executed,{SRC},strong,2025 meubilair 24 1476 DROP (was 2637); leasing 25 empty; overige 26 79749; in aanbouw 27 empty; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_overigemva_2025,{ENT},2025,79749,,,executed,{SRC},strong,2025 overige MVA 26 79749 DROP (was 96042); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_fva_2025,{ENT},2025,14124,,,executed,{SRC},strong,2025 FVA 28 14124 (was 14065); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_current_2025,{ENT},2025,5281887,,,executed,{SRC},strong,2025 vlottende 29/58 5281887 UP (was 4269062); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_strecv_2025,{ENT},2025,1615566,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1615566 JUMP (trade 198012 + other 1417554 JUMP was 603415); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_handelsrecv_2025,{ENT},2025,198012,,,executed,{SRC},strong,2025 handelsvorderingen 40 198012 UP (was 183068); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_otherrecv_2025,{ENT},2025,1417554,,,executed,{SRC},strong,2025 overige ST 41 1417554 JUMP (was 603415); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_beleg_2025,{ENT},2025,2000000,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 2000000 stable; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_cash_2025,{ENT},2025,1666321,,,executed,{SRC},strong,2025 liquide middelen 54/58 1666321 UP (was 1480701); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_equity_2025,{ENT},2025,4730724,,,executed,{SRC},strong,2025 eigen vermogen 10/15 4730724 UP (was 3820245); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_fondsen_2025,{ENT},2025,270877,,,executed,{SRC},strong,2025 fondsen 10 270877 stable; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_bestemde_2025,{ENT},2025,2043117,,,executed,{SRC},strong,2025 bestemde fondsen 13 2043117 JUMP (was 1043117; +1000000 sociaal passief + de prairie); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_overgedragen_2025,{ENT},2025,1483088,,,executed,{SRC},strong,2025 overgedragen 14 1483088 DROP (was 2317950; 691 +1000000); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_kapsubs_2025,{ENT},2025,933642,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 933642 JUMP (was 188301); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_voorz_2025,{ENT},2025,15943,,,executed,{SRC},strong,2025 voorzieningen 16/167 15943 (projectsubsidie geschil); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_debt_2025,{ENT},2025,1287831,,,executed,{SRC},strong,2025 schulden 17/49 1287831 DROP (was 1303215); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_ltdebt_2025,{ENT},2025,82283,,,executed,{SRC},strong,2025 LT schulden 17 82283 (all krediet 172/3; was 100444); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_stdebt_2025,{ENT},2025,1195801,,,executed,{SRC},strong,2025 ST schulden 42/48 1195801 (was 1180267; 42 18162 / lev 177964 / taxsoc 997175 / other 2500); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_lev_2025,{ENT},2025,177964,,,executed,{SRC},strong,2025 leveranciers 440/4 177964 DROP (was 205823); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_taxsoc_2025,{ENT},2025,997175,,,executed,{SRC},strong,2025 tax/soc 45 997175 (tax 175174 + bezold 822001); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_opbr_2025,{ENT},2025,6764354,,,executed,{SRC},strong,2025 reconstructed bedrijfsopbrengsten 6764354 = bruto 9900 5934821 + 60/61 829533; annual envelope (omzet 70 filled); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_bruto_2025,{ENT},2025,5934821,,,executed,{SRC},strong,2025 brutomarge 9900 5934821 UP (was 5710888); nrec 76A 0 (was 38360); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_omzet_2025,{ENT},2025,251094,,,executed,{SRC},strong,2025 omzet 70 251094 UP (was 233987); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_lidgeld73_2025,{ENT},2025,6391572,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 6391572 UP (was 6036078); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_diensten_2025,{ENT},2025,829533,,,executed,{SRC},strong,2025 handelsgoederen/diensten 60/61 829533 (was 736330); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_pers_2025,{ENT},2025,5512029,,,executed,{SRC},strong,2025 pers 62 5512029 / 60.9 VTE (was 5104326 / 57.6); YE 80 / YE VTE 63; 86529 uur; PC 331; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_afschr_2025,{ENT},2025,127291,,,executed,{SRC},strong,2025 afschrijvingen 630 127291 (was 143968); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_andere_2025,{ENT},2025,138319,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 138319 (was 128678); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_nrec66a_2025,{ENT},2025,15299,,,executed,{SRC},strong,2025 nrec 66A 15299 (was 20143); nrec 76A 0; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_expl_2025,{ENT},2025,141882,,,executed,{SRC},strong,2025 bedrijfswinst 9901 141882 DROP (was 313775); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_finopbr_2025,{ENT},2025,29795,,,executed,{SRC},strong,2025 financiele opbrengsten 75 29795 (was 48200); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_finkost_2025,{ENT},2025,6540,,,executed,{SRC},strong,2025 financiele kosten 65 6540 (was 7078); tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_pnl_2025,{ENT},2025,165138,,,executed,{SRC},strong,2025 winst 9904 165138 DROP (was 354897); tax 67/77 empty; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_capex_2025,{ENT},2025,10507,,,executed,{SRC},strong,2025 capex MVA 8169 10507 + FVA 8365 59 = 10566; reported MVA aanschaffingen 10507; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_gewaarborgd_2025,{ENT},2025,100444,,,executed,{SRC},strong,2025 zakelijk gewaarborgde schulden 9062 100444; hypotheek boekwaarde 107317; mandaat 235000; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
    f"bud_cglr_commissaris_2025,{ENT},2025,7204,,,executed,{SRC},strong,2025 vergoeding commissaris 7204; tick1518; primary official NBB WVV VKT-VZW 2026-00186340",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

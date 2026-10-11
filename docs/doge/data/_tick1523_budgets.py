#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgkh"
SRC = "src_cgkh_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cgkh_assets_2025,{ENT},2025,7706860,,,executed,{SRC},strong,2025 assets 7706860 DROP (was 7785054); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_vaste_2025,{ENT},2025,3584012,,,executed,{SRC},strong,2025 vaste activa 21/28 3584012 DROP (was 3726811); IVA 21 7664; FVA 28 60; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_mva_2025,{ENT},2025,3576288,,,executed,{SRC},strong,2025 MVA 22/27 3576288 DROP (was 3726751); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_gebouwen_2025,{ENT},2025,3466884,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 3466884 DROP (was 3635243); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_install_2025,{ENT},2025,24260,,,executed,{SRC},strong,2025 installaties 23 24260 UP (was 21963); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_meubilair_2025,{ENT},2025,79365,,,executed,{SRC},strong,2025 meubilair 24 79365 UP (was 67049); leasing 25 empty; overige 26 5780; in aanbouw 27 empty; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_fva_2025,{ENT},2025,60,,,executed,{SRC},strong,2025 FVA 28 60 stable; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_current_2025,{ENT},2025,4122848,,,executed,{SRC},strong,2025 vlottende 29/58 4122848 UP (was 4058243); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_ltrecv_2025,{ENT},2025,518960,,,executed,{SRC},strong,2025 LT vorderingen 29 518960 JUMP (all other 291; was 373563); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_strecv_2025,{ENT},2025,1568125,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1568125 (trade 87104 + other 1481021); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_handelsrecv_2025,{ENT},2025,87104,,,executed,{SRC},strong,2025 handelsvorderingen 40 87104 DROP (was 100639); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_otherrecv_2025,{ENT},2025,1481021,,,executed,{SRC},strong,2025 overige ST 41 1481021 UP (was 1394427); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_cash_2025,{ENT},2025,1981073,,,executed,{SRC},strong,2025 liquide middelen 54/58 1981073 JUMP (was 1625019); beleg 50/53 0 DROP was 500000; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_beleg_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 0 DROP (was 500000 termijn 53); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_prepaid_2025,{ENT},2025,54690,,,executed,{SRC},strong,2025 overlopende 490/1 54690 DROP (was 64596); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_equity_2025,{ENT},2025,4764907,,,executed,{SRC},strong,2025 eigen vermogen 10/15 4764907 DROP (was 4846734); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_bestemde_2025,{ENT},2025,1534160,,,executed,{SRC},strong,2025 bestemde fondsen 13 1534160 stable; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_overgedragen_2025,{ENT},2025,1795649,,,executed,{SRC},strong,2025 overgedragen 14 1795649 DROP (was 1800685); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_kapsubs_2025,{ENT},2025,1435098,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 1435098 DROP (was 1511889); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_debt_2025,{ENT},2025,2941952,,,executed,{SRC},strong,2025 schulden 17/49 2941952 (was 2938320); LT 17 940580 DROP was 1074669; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_ltdebt_2025,{ENT},2025,940580,,,executed,{SRC},strong,2025 LT schulden 17 940580 DROP (krediet 173; was 1074669); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_stdebt_2025,{ENT},2025,1908194,,,executed,{SRC},strong,2025 ST schulden 42/48 1908194 UP (was 1726575; lev 176489 / taxsoc 898132 / other 699485); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_lev_2025,{ENT},2025,176489,,,executed,{SRC},strong,2025 leveranciers 440/4 176489 DROP (was 183003); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_taxsoc_2025,{ENT},2025,898132,,,executed,{SRC},strong,2025 tax/soc 45 898132 (tax 87448 + bezold 810683); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_otherst_2025,{ENT},2025,699485,,,executed,{SRC},strong,2025 overige ST 48 699485 JUMP (was 549870); overlopend 492/3 93178; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_opbr_2025,{ENT},2025,8794445,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 8794445 UP (was 8735097); annual envelope (omzet 70 filled); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_omzet_2025,{ENT},2025,717138,,,executed,{SRC},strong,2025 omzet 70 717138 UP (was 684686); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_lidgeld73_2025,{ENT},2025,7941612,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 7941612 UP (was 7898839); subsidies 733 7941612 / lidgelden 730 empty; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_andere74_2025,{ENT},2025,135694,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 135694 (was 149073); nrec 76A 1; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_diensten_2025,{ENT},2025,2307277,,,executed,{SRC},strong,2025 diensten 61 2307277 JUMP (was 2015724); handelsgoederen 60 empty; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_pers_2025,{ENT},2025,6248426,,,executed,{SRC},strong,2025 pers 62 6248426 / 73.4 VTE (was 6136642 / 71.6); YE 107 / 91054 uur; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_afschr_2025,{ENT},2025,202185,,,executed,{SRC},strong,2025 afschrijvingen 630 202185 (was 210120); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_andere_2025,{ENT},2025,10781,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 10781 (was 38435); nrec 66A 95; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_expl_2025,{ENT},2025,10440,,,executed,{SRC},strong,2025 bedrijfswinst 9901 10440 DROP (was 332395); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_finopbr_2025,{ENT},2025,16914,,,executed,{SRC},strong,2025 financiele opbrengsten 75 16914 (was 32831); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_finkost_2025,{ENT},2025,26978,,,executed,{SRC},strong,2025 financiele kosten 65 26978 (was 32220); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_pnl_2025,{ENT},2025,-5036,,,executed,{SRC},strong,2025 winst 9904 -5036 LOSS (was 322756); tax 67/77 5412; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 VZW; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_capex_2025,{ENT},2025,59387,,,executed,{SRC},strong,2025 capex IVA 8022 11495 + MVA 8162 7157 + 8163 35790 + 8165 4945 = 59387; tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
    f"bud_cgkh_subsidies733_2025,{ENT},2025,7941612,,,executed,{SRC},strong,2025 subsidies 733 7941612 (of 73 7941612); tick1523; primary official NBB WVV VOL-VZW 2026-00242985",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

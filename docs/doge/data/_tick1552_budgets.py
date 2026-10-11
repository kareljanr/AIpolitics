#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1552 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io, sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vvsg"
SRC = "src_vvsg_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:180]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

rows = [
    f"bud_vvsg_opbr_2025,{ENT},2025,31266193,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 31266193 envelope (leftover public koepel VZW; omzet 70 present but commercial-only); DROP was 31352677; tick1552; primary official NBB VOL-VZW AV 24.06.2026",
    f"bud_vvsg_omzet_2025,{ENT},2025,2672153,,,executed,{SRC},strong,2025 omzet 70 2672153 UP was 2141338; commercial-only Belgie; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_subsid_2025,{ENT},2025,27759906,,,executed,{SRC},strong,2025 lidgeld/schenkingen/legaten/subsidies 73 27759906 DROP was 28326111; 730 lidgeld 11067493 + 733 subsidies 16692413; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_lidgeld_2025,{ENT},2025,11067493,,,executed,{SRC},strong,2025 lidgelden 730 11067493 UP was 10924563; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_733_2025,{ENT},2025,16692413,,,executed,{SRC},strong,2025 subsidies 733 16692413 DROP was 17401548; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_74_2025,{ENT},2025,834134,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 834134 DROP was 885228; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_assets_2025,{ENT},2025,43332320,,,executed,{SRC},strong,2025 balanstotaal 20/58 43332320 UP was 38047781; VA+vlottend holds; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_va_2025,{ENT},2025,5565418,,,executed,{SRC},strong,2025 vaste activa 21/28 5565418 DROP was 5978371; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_iva_2025,{ENT},2025,154205,,,executed,{SRC},strong,2025 IVA 21 154205 JUMP was 123750; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_mva_2025,{ENT},2025,4879282,,,executed,{SRC},strong,2025 MVA 22/27 4879282 DROP was 5322691; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_gebouwen_2025,{ENT},2025,4739094,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 4739094 DROP was 5155277; bezwaarde 91611 4739094; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_install_2025,{ENT},2025,133156,,,executed,{SRC},strong,2025 installaties 23 133156 DROP was 156647; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_meubilair_2025,{ENT},2025,7032,,,executed,{SRC},strong,2025 meubilair 24 7032 DROP was 10767; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_fva_2025,{ENT},2025,531930,,,executed,{SRC},strong,2025 FVA 28 531930 identiek (verbonden 280 530730 + andere 284/8 1200); tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_vlottend_2025,{ENT},2025,37766902,,,executed,{SRC},strong,2025 vlottende 29/58 37766902 JUMP was 32069409; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_ltrecv_2025,{ENT},2025,7447995,,,executed,{SRC},strong,2025 LT vorderingen 291 7447995 DROP was 8269975; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_handelsrecv_2025,{ENT},2025,9690908,,,executed,{SRC},strong,2025 handelsvorderingen 40 9690908 JUMP was 1204447 (lidgeld 2026 gefactureerd dec 2025); tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_otherrecv_2025,{ENT},2025,16894377,,,executed,{SRC},strong,2025 overige vorderingen 41 16894377 DROP was 17047313; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_beleg_2025,{ENT},2025,1551460,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1551460 identiek; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_cash_2025,{ENT},2025,1857566,,,executed,{SRC},strong,2025 liquide middelen 54/58 1857566 DROP was 3644459; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_prepaid_2025,{ENT},2025,324596,,,executed,{SRC},strong,2025 overlopend actief 490/1 324596 DROP was 351757; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_equity_2025,{ENT},2025,4042304,,,executed,{SRC},strong,2025 eigen vermogen 10/15 4042304; fondsen 23731 + bestemde 4151267 + overgedragen -132694; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_fondsen_2025,{ENT},2025,23731,,,executed,{SRC},strong,2025 fondsen 10 23731 identiek; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_reserves_2025,{ENT},2025,4151267,,,executed,{SRC},strong,2025 bestemde fondsen 13 4151267; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_overgedragen_2025,{ENT},2025,-132694,,,executed,{SRC},strong,2025 overgedragen resultaat 14 -132694; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_voorz_2025,{ENT},2025,667696,,,executed,{SRC},strong,2025 voorzieningen 16 667696 DROP; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_debt_2025,{ENT},2025,38622319,,,executed,{SRC},strong,2025 schulden 17/49 38622319 JUMP; EV+voorz+debt holds official 1-euro; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_lt_2025,{ENT},2025,4062584,,,executed,{SRC},strong,2025 LT 17 4062584 (krediet 173); tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_st_2025,{ENT},2025,5932481,,,executed,{SRC},strong,2025 ST 42/48 5932481; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_lt_current_2025,{ENT},2025,279642,,,executed,{SRC},strong,2025 LT binnen jaar 42 279642; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_lev_2025,{ENT},2025,1847048,,,executed,{SRC},strong,2025 handelsschulden 44 1847048 DROP was 2232049; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_taxsoc_2025,{ENT},2025,3361156,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 3361156; tax 102602 + pers 3258554; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_otherdebt_2025,{ENT},2025,444636,,,executed,{SRC},strong,2025 overige schulden 48 444636 DROP was 1051784; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_accrued_2025,{ENT},2025,28627254,,,executed,{SRC},strong,2025 overlopend passief 492/3 28627254 JUMP was 22421897; werkgroepen 1347109 + over te dragen subsid 17505555 + over te dragen opbr 9774591; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_costs_2025,{ENT},2025,31162255,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 31162255 DROP was 31642719; 60+61+62+630+635/9+640/8 holds; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_60_2025,{ENT},2025,2189115,,,executed,{SRC},strong,2025 handelsgoederen 60 2189115 UP was 1712514; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_61_2025,{ENT},2025,4282984,,,executed,{SRC},strong,2025 diensten 61 4282984 DROP was 5821882; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_pers_2025,{ENT},2025,22996957,,,executed,{SRC},strong,2025 bezoldigingen 62 22996957 / 208.5 VTE UP was 22501212 / 206.4; YE 227 / 279424 uur; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_afschr_2025,{ENT},2025,604230,,,executed,{SRC},strong,2025 afschrijvingen 630 604230 UP was 588420; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_expl_2025,{ENT},2025,103938,,,executed,{SRC},strong,2025 bedrijfswinst 9901 103938 PROFIT was -290042 LOSS; opbr-costs holds; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_fin_2025,{ENT},2025,124308,,,executed,{SRC},strong,2025 financiele opbrengsten 75 124308 DROP was 297040 (750 101275 + 751 20127 + 752/9 2907); tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_fincost_2025,{ENT},2025,183026,,,executed,{SRC},strong,2025 financiele kosten 65 183026 DROP was 194782 (schulden 180177); tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_pnl_2025,{ENT},2025,45220,,,executed,{SRC},strong,2025 resultaat 9903/9904/9905 45220 PROFIT was -187784 LOSS; tax empty; expl+fin holds; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_commissaris_2025,{ENT},2025,10204,,,executed,{SRC},strong,2025 commissaris 9505 10204 (Clybouw Bedrijfsrevisoren BV B00162 0446.129.922); extra 95061 2863; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_uitzend_2025,{ENT},2025,389171,,,executed,{SRC},strong,2025 uitzend 617 389171 / 4.2 VTE DROP was 549913 / 3.9; YE 4; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_capex_2025,{ENT},2025,191277,,,executed,{SRC},strong,2025 IVA aanschaffingen 8021 117553 + MVA install 8162 73724 = 191277; 8163 empty; tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_gewaarborgd_2025,{ENT},2025,2940103,,,executed,{SRC},strong,2025 door Belgische overheidsinstellingen gewaarborgde schulden 9061 2940103 (krediet 8961); tick1552; primary official NBB VOL-VZW",
    f"bud_vvsg_zakelijk_2025,{ENT},2025,1402123,,,executed,{SRC},strong,2025 schulden gewaarborgd zakelijke zekerheden 9062 1402123; bezwaarde activa 91611 4739094; tick1552; primary official NBB VOL-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print(f"budgets +{len(rows)}", before, "->", after)

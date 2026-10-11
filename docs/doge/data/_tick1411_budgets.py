# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "agb_merchtem"
SRC = "src_mrch_jr2025_nbb"
BUDGETS = [
    ("bud_mrch_assets_2025", "2025", "4925278", "2025 assets 4925278 VKT-inb 20/58; tick1411; primary official NBB WVV"),
    ("bud_mrch_assets_2024", "2024", "5130914", "2024 assets 5130914 comparative; tick1411; primary official NBB WVV 20/58"),
    ("bud_mrch_fixed_2025", "2025", "3505527", "2025 vaste activa 3505527 vs 3741778; tick1411; primary official NBB WVV 21/28"),
    ("bud_mrch_mva_2025", "2025", "3504252", "2025 MVA 3504252 vs 3740503; tick1411; primary official NBB WVV 22/27"),
    ("bud_mrch_gebouwen_2025", "2025", "3392597", "2025 terreinen/gebouwen 3392597 vs 3623949; tick1411; primary official NBB WVV 22"),
    ("bud_mrch_machines_2025", "2025", "85525", "2025 machines 85525 vs 85206; tick1411; primary official NBB WVV 23"),
    ("bud_mrch_meubilair_2025", "2025", "23520", "2025 meubilair 23520 vs 28738; tick1411; primary official NBB WVV 24"),
    ("bud_mrch_cip_2025", "2025", "2611", "2025 CIP 2611 unchanged; tick1411; primary official NBB WVV 27"),
    ("bud_mrch_fva_2025", "2025", "1275", "2025 FVA 1275 (aanschaf 5025 / niet-opgevraagd 3750); tick1411; primary official NBB WVV 28"),
    ("bud_mrch_current_2025", "2025", "1419750", "2025 vlottend 1419750 vs 1389136; tick1411; primary official NBB WVV 29/58"),
    ("bud_mrch_strecv_2025", "2025", "1357567", "2025 ST vorderingen 1357567 vs 1274109; tick1411; primary official NBB WVV 40/41"),
    ("bud_mrch_trade_recv_2025", "2025", "29143", "2025 handelsvorderingen 29143 vs 30380; tick1411; primary official NBB WVV 40"),
    ("bud_mrch_othrecv_2025", "2025", "1328425", "2025 overige vorderingen 1328425 vs 1243729; tick1411; primary official NBB WVV 41"),
    ("bud_mrch_cash_2025", "2025", "57860", "2025 liquide middelen 57860 DROP vs 110022; tick1411; primary official NBB WVV 54/58"),
    ("bud_mrch_cash_2024", "2024", "110022", "2024 liquide middelen 110022 comparative; tick1411; primary official NBB WVV 54/58"),
    ("bud_mrch_prepaid_2025", "2025", "4323", "2025 overlopend actief 4323 vs 5004; tick1411; primary official NBB WVV 490/1"),
    ("bud_mrch_equity_2025", "2025", "1413160", "2025 EV 1413160 vs 1411100; tick1411; primary official NBB WVV 10/15"),
    ("bud_mrch_inbreng_2025", "2025", "5000", "2025 inbreng onbeschikbaar 5000; tick1411; primary official NBB WVV 111"),
    ("bud_mrch_reserves_2025", "2025", "26122", "2025 reserves 26122; tick1411; primary official NBB WVV 13"),
    ("bud_mrch_overgedragen_2025", "2025", "565400", "2025 overgedragen 565400 vs 543884; tick1411; primary official NBB WVV 14"),
    ("bud_mrch_capsub_2025", "2025", "816638", "2025 kapitaalsubsidies 816638 vs 836094; tick1411; primary official NBB WVV 15"),
    ("bud_mrch_deferred_tax_2025", "2025", "130013", "2025 uitgestelde belastingen 130013 vs 136525; tick1411; primary official NBB WVV 168"),
    ("bud_mrch_debt_2025", "2025", "3382104", "2025 schulden 3382104 vs 3583288; tick1411; primary official NBB WVV 17/49"),
    ("bud_mrch_debt_2024", "2024", "3583288", "2024 schulden 3583288 comparative; tick1411; primary official NBB WVV 17/49"),
    ("bud_mrch_lt_2025", "2025", "2734894", "2025 LT overige leningen 2734894 vs 2913619; tick1411; primary official NBB WVV 17/174"),
    ("bud_mrch_st_2025", "2025", "635523", "2025 ST schulden 635523 vs 651029; tick1411; primary official NBB WVV 42/48"),
    ("bud_mrch_ltdue_2025", "2025", "488754", "2025 LT-due binnen jaar 488754 vs 521453; tick1411; primary official NBB WVV 42"),
    ("bud_mrch_sttrade_2025", "2025", "103167", "2025 leveranciers 103167 vs 100909; tick1411; primary official NBB WVV 440/4"),
    ("bud_mrch_tax_st_2025", "2025", "4936", "2025 tax ST 4936 vs 4701; tick1411; primary official NBB WVV 450/3"),
    ("bud_mrch_stother_2025", "2025", "38668", "2025 overige ST 38668 vs 23868; tick1411; primary official NBB WVV 47/48"),
    ("bud_mrch_deferred_pass_2025", "2025", "11687", "2025 overlopend passief 11687 vs 18640; tick1411; primary official NBB WVV 492/3"),
    ("bud_mrch_debt_1_5y_2025", "2025", "848163", "2025 debt 1-5y 848163; tick1411; primary official NBB WVV 8912"),
    ("bud_mrch_debt_gt5y_2025", "2025", "1886731", "2025 debt >5y 1886731; tick1411; primary official NBB WVV 8913"),
    ("bud_mrch_brutomarge_2025", "2025", "313807", "2025 brutomarge 313807 vs 256796; omzet 70 empty / 60/61 empty; tick1411; primary official NBB WVV 9900"),
    ("bud_mrch_brutomarge_2024", "2024", "256796", "2024 brutomarge 256796 comparative; tick1411; primary official NBB WVV 9900"),
    ("bud_mrch_afschr_2025", "2025", "285127", "2025 afschrijvingen 285127 vs 282882; tick1411; primary official NBB WVV 630"),
    ("bud_mrch_othcost_2025", "2025", "12744", "2025 andere bedrijfskosten 12744 vs 12085; tick1411; primary official NBB WVV 640/8"),
    ("bud_mrch_expl_2025", "2025", "16722", "2025 expl 16722 vs -38399; tick1411; primary official NBB WVV 9901"),
    ("bud_mrch_expl_2024", "2024", "-38399", "2024 expl -38399 comparative; tick1411; primary official NBB WVV 9901"),
    ("bud_mrch_fininc_2025", "2025", "23364", "2025 fin opbr 23364 (capsub 19476); tick1411; primary official NBB WVV 75"),
    ("bud_mrch_capsub_pnl_2025", "2025", "19476", "2025 kapitaal- en interestsubsidies 19476; tick1411; primary official NBB WVV 753"),
    ("bud_mrch_fincost_2025", "2025", "100", "2025 fin kosten 100; tick1411; primary official NBB WVV 65"),
    ("bud_mrch_pnl_2025", "2025", "46516", "2025 PnL 46516 vs -7310; tick1411; primary official NBB WVV 9904"),
    ("bud_mrch_pnl_2024", "2024", "-7310", "2024 PnL -7310 comparative; tick1411; primary official NBB WVV 9904"),
    ("bud_mrch_div_2025", "2025", "25000", "2025 vergoeding inbreng 25000 vs 0; tick1411; primary official NBB WVV 694"),
    ("bud_mrch_overgedragen_dest_2025", "2025", "565400", "2025 over te dragen winst 565400; tick1411; primary official NBB WVV 14"),
    ("bud_mrch_capex_2025", "2025", "48876", "2025 capex MVA aanschaf 48876; tick1411; primary official NBB WVV 8169"),
    ("bud_mrch_commissaris_2025", "2025", "3705", "2025 commissaris fee 3705; tick1411; primary official NBB WVV 6.6"),
]
# append as raw LF lines to avoid DictWriter quoting rewrite
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
existing = set()
import io
for row in csv.reader(io.StringIO(raw.decode("utf-8"))):
    if row:
        existing.add(row[0])
added = []
for bid, year, amt, notes in BUDGETS:
    if bid in existing:
        continue
    added.append(f"{bid},{ENT},{year},{amt},,,executed,{SRC},strong,{notes}\n")
p.write_bytes(raw + "".join(added).encode("utf-8"))
print("budgets", len(added))

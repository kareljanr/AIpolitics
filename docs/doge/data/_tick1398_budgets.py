# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/budgets.csv")
ENT = "igs_ibeg"
SRC = "src_ibeg_jr2025_nbb"
BUDGETS = [
    ("bud_ibeg_assets_2025", "2025", "100488193", "2025 assets 100488193 VOL-inb 20/58; tick1398; primary official NBB WVV"),
    ("bud_ibeg_assets_2024", "2024", "103058477", "2024 assets 103058477 comparative; tick1398; primary official NBB WVV 20/58"),
    ("bud_ibeg_fixed_2025", "2025", "96372430", "2025 vaste activa 96372430 all FVA; MVA/IVA empty; tick1398; primary official NBB WVV 21/28"),
    ("bud_ibeg_fva_2025", "2025", "96372430", "2025 FVA 96372430 vs 96872430; tick1398; primary official NBB WVV 28"),
    ("bud_ibeg_fva_rel_2025", "2025", "83085538", "2025 verbonden FVA 83085538 vs 83585538; tick1398; primary official NBB WVV 280/1"),
    ("bud_ibeg_fva_part_2025", "2025", "74085538", "2025 verbonden deelnemingen 74085538 (Fluvius HV 64830538 + VENTUM 9255000); tick1398; primary official NBB WVV 280"),
    ("bud_ibeg_fva_loan_2025", "2025", "9000000", "2025 verbonden vorderingen 9000000 vs 9500000 (Fluvius HV credit; facility 30m); tick1398; primary official NBB WVV 281"),
    ("bud_ibeg_fva_oth_2025", "2025", "13286892", "2025 andere aandelen 13286892 (Publigas 423 + Publi-T 20117); tick1398; primary official NBB WVV 284"),
    ("bud_ibeg_fhv_fva_2025", "2025", "64830538", "2025 Fluvius HV 21.48pct valued 64830538.49; tick1398; primary official NBB WVV 6.19"),
    ("bud_ibeg_ventum_fva_2025", "2025", "9255000", "2025 VENTUM&green 92.55pct valued 9255000; tick1398; primary official NBB WVV 6.19"),
    ("bud_ibeg_current_2025", "2025", "4115762", "2025 vlottend 4115762 vs 6186047; tick1398; primary official NBB WVV 29/58"),
    ("bud_ibeg_strecv_2025", "2025", "576007", "2025 ST vorderingen 576007 tax prepaid; tick1398; primary official NBB WVV 40/41"),
    ("bud_ibeg_invest_2025", "2025", "1697144", "2025 geldbeleggingen 1697144 DROP vs 3330349; tick1398; primary official NBB WVV 50/53"),
    ("bud_ibeg_invest_2024", "2024", "3330349", "2024 geldbeleggingen 3330349 comparative; tick1398; primary official NBB WVV 50/53"),
    ("bud_ibeg_bonds_2025", "2025", "1501788", "2025 vastrentende effecten 1501788 vs 3066794; tick1398; primary official NBB WVV 52"),
    ("bud_ibeg_termijn_2025", "2025", "195357", "2025 termijnrekeningen >1y 195357 vs 263555; tick1398; primary official NBB WVV 53"),
    ("bud_ibeg_cash_2025", "2025", "1842610", "2025 liquide middelen 1842610 vs 1638882; tick1398; primary official NBB WVV 54/58"),
    ("bud_ibeg_cash_2024", "2024", "1638882", "2024 liquide middelen 1638882 comparative; tick1398; primary official NBB WVV 54/58"),
    ("bud_ibeg_equity_2025", "2025", "99038008", "2025 EV 99038008 vs 101254697; tick1398; primary official NBB WVV 10/15"),
    ("bud_ibeg_inbreng_2025", "2025", "94803958", "2025 inbreng onbeschikbaar 94803958 / 764918 aandelen; tick1398; primary official NBB WVV 10/11"),
    ("bud_ibeg_reserves_2025", "2025", "3159688", "2025 reserves 3159688 (onbeschikbaar 39527 / beschikbaar 3120162); tick1398; primary official NBB WVV 13"),
    ("bud_ibeg_re_2025", "2025", "1074362", "2025 overgedragen winst 1074362 vs 3371541; tick1398; primary official NBB WVV 14"),
    ("bud_ibeg_debt_2025", "2025", "1450184", "2025 schulden 1450184 vs 1803780; no LT; tick1398; primary official NBB WVV 17/49"),
    ("bud_ibeg_debt_2024", "2024", "1803780", "2024 schulden 1803780 comparative; tick1398; primary official NBB WVV 17/49"),
    ("bud_ibeg_st_2025", "2025", "1450184", "2025 ST schulden 1450184; tick1398; primary official NBB WVV 42/48"),
    ("bud_ibeg_sttrade_2025", "2025", "450184", "2025 leveranciers 450184 vs empty; tick1398; primary official NBB WVV 440/4"),
    ("bud_ibeg_stoth_2025", "2025", "1000000", "2025 overige ST 1000000 vs 1803780 (saldo dividend); tick1398; primary official NBB WVV 47/48"),
    ("bud_ibeg_diensten_2025", "2025", "809703", "2025 diensten 809703 JUMP vs 271411; omzet 70 empty; tick1398; primary official NBB WVV 61"),
    ("bud_ibeg_diensten_2024", "2024", "271411", "2024 diensten 271411 comparative; tick1398; primary official NBB WVV 61"),
    ("bud_ibeg_othcost_2025", "2025", "7012", "2025 andere bedrijfskosten 7012 vs 6093; tick1398; primary official NBB WVV 641/8"),
    ("bud_ibeg_nrec_2025", "2025", "519509", "2025 niet-recurrent 66A 519509 minderwaarde realisatie / onttrekking investeringsreserve; tick1398; primary official NBB WVV 66A"),
    ("bud_ibeg_expl_2025", "2025", "-1336225", "2025 expl -1336225 vs -874818; tick1398; primary official NBB WVV 9901"),
    ("bud_ibeg_expl_2024", "2024", "-874818", "2024 expl -874818 comparative; tick1398; primary official NBB WVV 9901"),
    ("bud_ibeg_fininc_2025", "2025", "2640731", "2025 fin opbr 2640731 vs 3556828; tick1398; primary official NBB WVV 75/76B"),
    ("bud_ibeg_fva_inc_2025", "2025", "2318574", "2025 opbrengsten FVA 2318574 DBI aftrek; tick1398; primary official NBB WVV 750"),
    ("bud_ibeg_fincost_2025", "2025", "21195", "2025 fin kosten 21195 vs 54684; tick1398; primary official NBB WVV 65/66B"),
    ("bud_ibeg_pnl_2025", "2025", "1283311", "2025 PnL +1283311 vs +2627327; tick1398; primary official NBB WVV 9904"),
    ("bud_ibeg_pnl_2024", "2024", "2627327", "2024 PnL +2627327 comparative; tick1398; primary official NBB WVV 9904"),
    ("bud_ibeg_div_2025", "2025", "3500000", "2025 dividend 3500000 DROP vs 5303780; tick1398; primary official NBB WVV 694"),
    ("bud_ibeg_div_2024", "2024", "5303780", "2024 dividend 5303780 comparative; tick1398; primary official NBB WVV 694"),
    ("bud_ibeg_rel_inc_2025", "2025", "458721", "2025 related-party FVA income 458721 vs 926009; tick1398; primary official NBB WVV 9421"),
    ("bud_ibeg_comm_2025", "2025", "8233", "2025 commissaris EY 8233 + extra 1671; tick1398; primary official NBB WVV 9505"),
    ("bud_ibeg_board_2025", "2025", "28314", "2025 bestuurders 28314; tick1398; primary official NBB WVV 9503"),
    ("bud_ibeg_taxprep_2025", "2025", "576007", "2025 geactiveerde VenB 576007; tick1398; primary official NBB WVV 9136"),
    ("bud_ibeg_latent_2025", "2025", "5068258", "2025 actieve latenties 5068258; tick1398; primary official NBB WVV 9141"),
    ("bud_ibeg_loanfac_2025", "2025", "30000000", "2025 Fluvius HV credit facility max 30000000; tick1398; primary official NBB WVV jaarverslag"),
]
rows = [{
    "budget_id": bid, "entity_id": ENT, "year": year, "amount_eur": amt,
    "amount_min_eur": "", "amount_max_eur": "", "basis": "executed",
    "source_id": SRC, "confidence": "strong", "notes": notes,
} for bid, year, amt, notes in BUDGETS]
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    seen = {row[fields[0]] for row in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    for row in rows:
        if row[fields[0]] in seen:
            continue
        w.writerow({k: row.get(k, "") for k in fields})
        added += 1
print("budgets", added)

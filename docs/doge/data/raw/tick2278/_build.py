from pathlib import Path
src = Path("docs/doge/data/raw/tick2277/write_tick2277.py").read_text(encoding="utf-8")
# systematic replacements
pairs = [
    ("tick 2277 — leftover dual AMAB YE2025 Medium (omzet JUMP 14.18m / bruto~1.53x / pnl LOSS FLIP / FTE 645.1)",
     "tick 2278 — leftover dual m-accent YE2025 Medium (omzet JUMP 2.75m / bruto~1.63x / pnl JUMP +87% / FTE 91.9)"),
    ("TICK = 2277", "TICK = 2278"),
    ("2026-08-27T11:30:00Z", "2026-08-27T11:45:00Z"),
    ("vzw_amab_asse", "vzw_m_accent_eeklo"),
    ("0411.635.039", "0465.841.411"),
    ("0411635039", "0465841411"),
    ("src_amab_jr2025_cw_en", "src_maccent_jr2025_cw_en"),
    ("gap_amab_nbb_pdf_assets_debt_bruto_gt_omzet_1_53x_pnl_loss_flip_matrix_l5",
     "gap_maccent_nbb_pdf_assets_debt_bruto_gt_omzet_1_63x_pnl_jump_87pct_matrix_l5"),
    ("comm_amab_jr2025_statutory_maatwerk_omzet_14_18m_pnl_loss_flip",
     "comm_maccent_jr2025_statutory_maatwerk_omzet_2_75m_pnl_jump"),
    ("lb_amab_omzet_14_18m_bruto_1_53x_pnl_loss_flip_jr2025",
     "lb_maccent_omzet_2_75m_bruto_1_63x_pnl_jump_87pct_jr2025"),
    ("RQ = \"rq_2277\"", "RQ = \"rq_2278\""),
    ("RQ_NEXT = \"rq_2278\"", "RQ_NEXT = \"rq_2279\""),
    ("OMZET = 14179340", "OMZET = 2747558"),
    ("OMZET24 = 12869693", "OMZET24 = 2499264"),
    ("BRUTO = 21690724", "BRUTO = 4486626"),
    ("BRUTO24 = 20926423", "BRUTO24 = 3938259"),
    ("PNL = -447493", "PNL = 774084"),
    ("PNL24 = 559019", "PNL24 = 414796"),
    ("EQUITY = 17950369", "EQUITY = 6353816"),
    ("EQUITY24 = 18491679", "EQUITY24 = 5598652"),
    ("FTE = 645.1", "FTE = 91.9"),
    ("FTE24 = 642.2", "FTE24 = 84.1"),
    ("PI = \"6.80\"", "PI = \"5.85\""),
]
for a,b in pairs:
    if a not in src:
        print("MISSING:", a[:70])
    src = src.replace(a,b)
# content-specific narrative replacements
narr = [
    ("AMAB YE2025 Medium", "m-accent YE2025 Medium"),
    ("AMAB VZW Asse", "m-accent VZW Eeklo"),
    ("AMAB VZW", "m-accent VZW"),
    ("AMAB", "m-accent"),
    ("Asse/Beersel/Zaventem", "Eeklo Meetjesland Kringwinkel"),
    ("Asse", "Eeklo"),
    ("info@amab.be", "info@m-accent.be"),
    ("https://www.amab.be/", "https://www.m-accent.be/"),
    ("Z. 5 Mollem 90, 1730 Asse", "Slachthuisstraat 2/B, 9900 Eeklo"),
    ("Z. 5 Mollem 90 1730 Asse", "Slachthuisstraat 2/B 9900 Eeklo"),
    ("+32 2 356 66 97", "+32 9 377 77 74"),
    ("Flemish maatwerk Asse", "Flemish maatwerk Eeklo Kringwinkel"),
    ("Flemish maatwerk", "Flemish maatwerk/Kringwinkel"),
    ("co-packing / electro / green / circular", "kringwinkel / secondhand retail / social employment"),
    ("co-packing/electro/green", "kringwinkel/secondhand"),
    ("co-packing/electro/green/circular", "kringwinkel/secondhand/social"),
    ("collectief maatwerk path", "collectief maatwerk / Kringwinkel Meetjesland path"),
    ("LOSS FLIP", "JUMP"),
    ("pnl LOSS FLIP", "pnl JUMP"),
    ("pnl_loss_flip", "pnl_jump"),
    ("after CARP@2276", "after AMAB@2277"),
    ("after C.A.R.P./ASV", "after AMAB"),
    ("CARP/ASV/APAC", "AMAB/CARP/ASV/APAC"),
    ("Do not redo CARP", "Do not redo AMAB/CARP"),
    ("Skip AMAB/", "Skip m-accent/AMAB/"),
    ("3 VE", "6 VE"),
    ("begindatum 28.10.1971", "begindatum 16.10.1998"),
    ("filed **10.06.2026**", "filed **14.07.2026**"),
    ("neerlegging **10.06.2026**", "neerlegging **14.07.2026**"),
    ("neerlegging 10.06.2026", "neerlegging 14.07.2026"),
    ("filed 10-06-2026", "filed 14-07-2026"),
    ("decision_date\": \"2026-06-10\"", "decision_date\": \"2026-07-14\""),
    ("Vlaanderen>VlaamsBrabant>Asse>AMAB", "Vlaanderen>OostVlaanderen>Eeklo>m_accent"),
    ("Vlaanderen>VlaamsBrabant>Asse>m-accent", "Vlaanderen>OostVlaanderen>Eeklo>m_accent"),
    ("/amab", "/m-accent"),
    ("src_amab_", "src_maccent_"),
    ("14.18m", "2.75m"),
    ("~1.53x", "~1.63x"),
    ("1_53x", "1_63x"),
    ("absurdity_score\": \"7.6\"", "absurdity_score\": \"5.8\""),
    ("cost_score\": \"7.0\"", "cost_score\": \"4.5\""),
    ("omzet JUMP 14.18m / bruto~1.53x / pnl LOSS FLIP / FTE 645.1",
     "omzet JUMP 2.75m / bruto~1.63x / pnl JUMP +87% / FTE 91.9"),
    ("omzet JUMP 14.18m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE}",
     "omzet JUMP 2.75m / bruto~{RATIO}x / pnl JUMP +{PNL_PCT}% / FTE {FTE}"),
]
for a,b in narr:
    src = src.replace(a,b)
# fix over-replacements from LOSS FLIP -> JUMP that may have broken titles
src = src.replace("pnl JUMP FLIP", "pnl JUMP")
src = src.replace("LOSS JUMP", "JUMP")
src = src.replace("behind JUMP despite omzet JUMP", "behind bruto>~1.6x omzet + FTE JUMP despite published retail omzet")
src = src.replace("NACE **88.993**", "NACE **47.792/47.793** (Kringwinkel; maatwerk Crevits list)")
src = src.replace("NACE 88.993", "NACE 47.792/47.793 (maatwerk/Kringwinkel)")
out = Path("docs/doge/data/raw/tick2278/write_tick2278.py")
out.write_text(src, encoding="utf-8")
print("wrote", out, "bytes", out.stat().st_size)
# sanity
assert "TICK = 2278" in src
assert "0465.841.411" in src
assert "rq_2279" in src
assert "info@m-accent.be" in src
print("sanity ok")

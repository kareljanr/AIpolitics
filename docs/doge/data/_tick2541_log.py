from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2541_stamp.txt").read_text().strip().splitlines()
log = ROOT / "docs/doge/loop_log.md"
entry = f"""
## Tick 2541 — {STAMP} — rq_2541 leftover dual De Plek Rotselaar YE2025

- Unit: **rq_2541** leftover dual after **Martine Van Camp@2540**. Prefer NON-stall leftover VAPH/maatwerk of leftover-mined AGB-only Flanders city with official YE2025 native PDF. STOP leftover-note loop. HARD SKIP leftover CIK. HARD SKIP leftover CAR website wander. HARD SKIP leftover KBO-activity. HARD SKIP leftover city_bonheiden leftover hospital Imelda 403. HARD SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian. HARD SKIP leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael remine leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover Aalternatief 0 deposits.
- Hunt skips: **Noorderhart 0445.662.144** leftover city_pelt leftover hospital YE2025 deposit 2026-00274691 **SCAN Xerox AltaLink HARD SKIP**; **Social Impact Fonds Toontjeshuis 0675.561.943** leftover city_schelle holding CV NACE 64.210 SKIP; Hoeve Megusta / Rommeshoef BV MIC-inb commercial SKIP; Ter Loke / Bindkracht / Den Ateljee YE2024-only SKIP; Klaverhof Agten CommV farm NACE 01.410 SKIP; Klavertje Hier / Joert / Windkracht 0 deposits SKIP.
- FIRST LOCK leftover city_rotselaar leftover VAPH **De Plek 0822.360.357** leftover-mined AGB-only unused leftover type (children agb_rotselaar). Confirmed unused (0 real entity rows) + official KBO zetel Hanewijk 44A **3118 Rotselaar** (not leftover-via-VE) + native YE2025 PDF. Took FREE leftover Flemish **VZW De Plek** YE2025 (KBO **0822.360.357**; official zetel Hanewijk 44A 3118 Rotselaar since 01.10.2012; **Actief** **1 VE** **2.228.262.719**; RSZ2025 **88.106**; leftover of mined **city_rotselaar**; FOI deplek@telenet.be from official VAPH; leftover VAPH / official VAPH adreslijst). Identity trap: 0822.360.357 ≠ leftover AGB Rotselaar **0865.782.903** ≠ leftover-via-VE. Confirmed leftover public leftover VAPH VZW not convent / not leftover-via-VE / not Armonea / not Korian / not Vulpia / not commercial BV / not OCMW. MIC-VZW **native text** (not scan) — 34977 B / 8p native euros (MIC-VZW 6.1.1 6.1.3 6.2 6.3 6.4 7 8 niet dienstig).
- Found: official NBB MIC-VZW native PDF deposit **2026-00317818** (34977 B / 8p; AV **28.06.2026**; header **22/07/2026**; CDN GET **200** 34977 OpenPDF 1.3.26 MD5 02fead2e68d2faa0370e1fe0ef97b547; NBB UUID 881dc344-860b-11f1-b284-3baacb2f7291) — bruto 9900 **EUR8964** DROP −32.90% (was 13360); omzet 70 **EUR17185** DROP −25.47% (was 23059); 73 **EUR2322** JUMP (was empty); 76A **EUR216** JUMP; bedrijfswinst 9901 **EUR2822** DROP −45.70%; pnl 9904 **EUR2750** DROP −46.39%; equity **EUR23262** JUMP +112.32%; assets **EUR39124** JUMP +209.97%; debt **EUR15863** JUMP +852.16%; cash **EUR12686** JUMP +189.44%; kapitaalsubsidies **EUR9556** JUMP from empty; 62 **EUR289** DROP −95.63%; 630 **EUR5580** JUMP; MVA **EUR19432** JUMP; capex **EUR21649**; FTE n/a MIC. Strong KBO + Strong PDF.
- Wrote: sources +4; budgets +11; commitments +1; leaderboard +1; entities +1; FOI **gap_de_plek_rotselaar_vaph_matrix_bruto_drop_8964_omzet_drop_17185_73_jump_2322_cash_jump_12686_l5** prio7 ready + draft; raw PDF docs/doge/raw/tick2541/; rq_2541=done; spawn **rq_2542**; ticks=2541.
- Next: **rq_2542** leftover dual (NOT every-10; next every-10 **2550**).
"""
text = log.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
log.write_text(text + entry, encoding="utf-8")
print("log ok")

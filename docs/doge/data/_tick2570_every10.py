#!/usr/bin/env python3
"""tick2570 EVERY-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md (surgical section rewrite)."""
import re
from pathlib import Path
P = Path("/workspace/AIpolitics/docs/doge/data")

pr = P / "progress_every_10_ticks.md"
t = pr.read_text(encoding="utf-8")
head, _ = t.split("## Snapshot at **tick 2560**", 1)
new = """## Snapshot at **tick 2570** (2026-10-12; loop resumed after human pause 2026-08-29 → 2026-10-12)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | unchanged vs 2560; residual dual 2561-2570 is L5 depth, not new L2 mass; AGB Bornem / FARO / AIESH still YE2024 stalls (not rechecked this tick) |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous; unchanged band) | **Gain 2561-2570 residual dual L5 (not near-complete of 348bn):** Berkenhof · Licht en Liefde Heem · Kerckstede · De Berken · Duinhelm · Vondels · Oikonde · Emiliani · Hoito · EVERY-10 primary **Het Balanske Tielt-Winge 73 JUMP 1.61m / debt JUMP 2.31m / 9901 DROP 12k** (Strong official NBB PDF 2026-00206974) |
| **E. FOI-ready gaps** | **2254** drafts ready | Human send only; answered **11**; partial **28**; total FOI rows **2306** (status column has ~14 legacy malformed rows — data-quality debt, not touched) |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie/CIK shells** (**NEW 2561-2570** Berkenhof · Licht en Liefde Heem · Kerckstede · De Berken · Duinhelm · Vondels · Oikonde · Emiliani · Hoito · **Het Balanske**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2570)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 56440 |
| commitments.csv | 6306 |
| leaderboard.csv | 8426 |
| entities.csv | 2326 |
| sources.csv | 7848 |
| FOI ready | 2254 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | 2306 |
| research_queue open | rq_2571 after Het Balanske Tielt-Winge EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2560 / last file refresh 2560

- **Residual dual (tick2561-2570):** leftover public VAPH **Berkenhof Leopoldsburg / Licht en Liefde Heem Jabbeke / Kerckstede Staden / De Berken Overijse / Duinhelm Oostende / Vondels Ieper / Oikonde Mechelen / Emiliani Lokeren (70/76A 22.02m) / Hoito Tienen** · EVERY-10 primary **Het Balanske Tielt-Winge** (KBO 0448.595.801; VKT-VZW YE2025: 73 **1.61m** JUMP +11.4% / bruto 9900 **1.27m** / 62 **1.15m** JUMP +18.1% / 9901 DROP to **12k** / debt 17/49 JUMP **2.31m** (+193%; overige leningen 174/0 **1.64m** new) / aanbouw **1.36m** + capex **1.24m** = new Villa84 woonproject Diest (2nd VE since 23.01.2026) / cash **1.28m** / FTE 17,9; Strong official NBB PDF; FOI ready on subsidy split + lender terms).
- **Pause note:** 2026-08-29 → 2026-10-12 human pause; no ticks in between. New YE2025 deposits may now exist for earlier 0-deposit / YE2024-only skips (VillaVip, Aalternatief, De Beukheuvel, OpWeg, Nethedal, Levenslust …) — recheck queued in rq_2571.
- **Rejected this tick (fast):** Eyckenborgh Gooik 0434.019.372 (WZC / Gravenkasteel inrichtende macht, not VAPH) · Zwart Goor Merksplas (Klavier = Emmaüs 0411.515.075, zetel Mechelen, leftover-via-VE) · CDN staatsbladmonitor timeouts → official NBB broker PDF endpoint used.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 · AIESH YE2024 · Bethanië Genk SCAN/OCR · leftover groenezorg deferred · leftover-via-VE parents · city_kapellen / city_londerzeel / city_wortegem_petegem slugs MISSING.
"""
pr.write_text(head + new, encoding="utf-8")

tp = P / "doge_waste_top10_current.md"
t = tp.read_text(encoding="utf-8")
t = t.replace("**As-of:** tick **2560** (2026-08-29) · **8416** leaderboard rows", "**As-of:** tick **2570** (2026-10-12) · **8426** leaderboard rows")
i = t.index("**Stock filter (off pure annual top10):**")
t = t[:i] + """**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2561-2570:** **Het Balanske Tielt-Winge 73 JUMP 1.61m / debt JUMP 2.31m / 9901 DROP 12k** (EVERY-10@2570 Strong PDF) · Hoito Tienen · Emiliani Lokeren · Oikonde Mechelen · Vondels Ieper · Duinhelm Oostende · De Berken Overijse · Kerckstede Staden · Licht en Liefde Heem Jabbeke · Berkenhof Leopoldsburg · De Hoge Kouter EVERY-10@2560.

**Change vs tick 2560:** pure annual top10 **stable** (10 new leaderboard rows 2561-2570 all pi 5.30-6.00, far below #10 cut-off 8.4; top10_changed False). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Emiliani Lokeren** envelope 70/76A JUMP **EUR22.02m** / 73 JUMP **EUR18.57m** / debt JUMP **EUR5.02m** leftover city_lokeren leftover VAPH (pi 6.00, highest of 2561-2570).
- **Duinhelm Oostende** 70/76A JUMP **EUR12.61m** / 9901 JUMP **EUR887k** leftover city_oostende leftover VAPH.
- **Kerckstede Staden** 70/76A JUMP **EUR12.04m** / cash DROP **EUR608k** leftover city_staden leftover VAPH.
- **Het Balanske Tielt-Winge** EVERY-10 primary: debt **EUR787577 → EUR2308489** (+193%; new overige leningen **EUR1644111**) financing aanbouw **EUR1359758** (Villa84 Diest) while 9901 fell to **EUR12273**; 73 **EUR1608109**.
- **Vondels Ieper** 70/76A JUMP **EUR10.49m** / cash DROP **EUR762k** leftover city_ieper leftover VAPH.
"""
tp.write_text(t, encoding="utf-8")
print("every-10 refreshed")

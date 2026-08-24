# -*- coding: utf-8 -*-
from pathlib import Path

p = Path("docs/doge/loop_log.md")
entry = """

## Tick 2169 - 2026-08-26T02:20:00Z - rq_2169 Sint-Vincentius Aaigem (bruto JUMP 743k / omzet empty / pnl LOSS FLIP / Medium)

- Unit: **rq_2169** leftover dual after **rq_2168 Sint Lodewijk / Lork Hoeselt race**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (filed 24-11-2025); AIESH still **YE2024**; REW still **YE2024**. Took named deferred unused leftover **Sint-Vincentius Aaigem VZW** YE2025 (KBO **0644.843.825**; Aaigemdorp 68 Erpe-Mere; **VZW** / **2 VE**; HealthPro; dual operating WZC CoBRHA **0422.620.585** same address no YE2025). Deferred FREE Melis Home 0787.300.696 (bruto 72k) + Abdij Affligem 0400.371.161. Do not redo Sint Lodewijk/Lork Hoeselt/Anima hold/Avondvrede/Anima Vlaanderen/t Hofke/Zorg-Saam/Sint-Bernardus/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork Geel.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR743497** JUMP +4.20% vs YE2024 EUR713540; pnl **EUR97823** LOSS FLIP vs YE2024 EUR-3297; equity **EUR4250630** JUMP +2.36%; FTE **0**; neerlegging **24.07.2026**. Assets/debt Unknown. Medium. Strong KBO Actief VZW 2 VE. CW activity label "Andere drinkgelegenheden" (likely mislabel). FOI via info@sint-vincentius-vzw.be (tel 053 60 12 12).
- Wrote: sources (+5); budgets (+4); commitments (+1); leaderboard (+1 pi 5.0); entities (+1 vzw_sint_vincentius_aaigem); foi + draft gap_sint_vincentius_aaigem_nbb_pdf_assets_debt_omzet_empty_pnl_flip_related_wzc_matrix_l5; rq_2169=done + rq_2170 open (EVERY-10); loop_state ticks=2169; raw docs/doge/data/raw/tick2169/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2160**; next **2170**). Next: rq_2170 EVERY-10 progress+top10 THEN leftover (AGB/FARO-if-YE2025 / AIESH-REW / Melis-or-Affligem / unused IGS-DSO-WZC-MRS).
"""
p.write_text(p.read_text(encoding="utf-8") + entry, encoding="utf-8")
print("log appended", p.stat().st_size)

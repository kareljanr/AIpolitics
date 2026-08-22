from pathlib import Path
p=Path("docs/doge/loop_log.md")
text=p.read_text(encoding="utf-8")
entry="""
### 2026-08-24T20:55:00Z — tick 1782
- Unit: rq_1782 — **RESIDENCE PRINCE LEOPOLD (CEDRE BLEU) SA** (Jodoigne / Vivalto)
- Found: Unused Vivalto maison Le Cedre Bleu legal entity. NBB A-cap YE2025 deposit [2026-00137103](http://cdn.staatsbladmonitor.be/2026pdf/2026-00137103.pdf) CDN 200 (215 KB / 31p); KBO **0451.294.082**; AV **12.05.2026**; mere Vivalto Home Belgium; Forvis Mazars — **opinion sans reserve**. Sourced: assets **EUR14,161,580**; equity **EUR36,987** (flip from NEG; Art **7:229** thin); debt **EUR14,056,594**; marge bruto **EUR3,178,410**; staff **EUR2,245,977** / VTE **36.6**; PnL **EUR133,725**; FVA **EUR7,503,000**; autres dettes ST **EUR4,272,538**; **RIVAGE gage EUR135,600,000**; **comfort letter** through AG YE2026.
- Wrote: sources (+3); entities nv_cedrebleu; budgets (+14); commitments; leaderboard; foi_queue ready; research_queue rq_1782=done + rq_1783 spawned; loop_state ticks=1782; FOI draft gap_cedrebleu_marge_3_18m_equity_thin_comfort_rivage_l5.md
- FOI opened: gap_cedrebleu_marge_3_18m_equity_thin_comfort_rivage_l5 (**ready**, not sent)
- Next: rq_1783 — unused Vivalto maisons / AGB / NSZ-if-200; every-10 at 1790
"""
if "tick 1782" not in text:
    p.write_text(text.rstrip()+"\n"+entry, encoding="utf-8")
    print("log appended")
else:
    print("log already present")

from pathlib import Path
p=Path("docs/doge/loop_log.md")
text=p.read_text(encoding="utf-8")
entry="""
### 2026-08-24T21:15:00Z — tick 1783
- Unit: rq_1783 — **LA RESIDENCE CHARLEMAGNE SA** (Liege / Vivalto)
- Found: Unused Vivalto maison. NBB A-cap YE2025 deposit [2026-00137104](http://cdn.staatsbladmonitor.be/2026pdf/2026-00137104.pdf) CDN 200 (227 KB / 28p); KBO **0870.962.307**; AV **12.05.2026**; mere Vivalto Home Belgium; Forvis Mazars — **opinion sans reserve**. Sourced: assets **EUR16,590,806**; equity **EUR4,682,133**; debt **EUR10,724,449**; marge bruto **EUR2,880,770**; staff **EUR2,170,037** / VTE **34.4**; **nrec fin EUR2,965,277** → PnL **EUR3,106,808**; dividend apport **EUR2,950,000**; controllers **EUR10,647,702**; autres creances JUMP **EUR3,231,757**; cash DROP; **no RIVAGE** (negative pledge only).
- Wrote: sources (+3); entities nv_charlemagne; budgets (+14); commitments; leaderboard; foi_queue ready; research_queue rq_1783=done + rq_1784 spawned; loop_state ticks=1783; FOI draft gap_charlemagne_marge_2_88m_nrec_fin_2_97m_dividend_2_95m_l5.md
- FOI opened: gap_charlemagne_marge_2_88m_nrec_fin_2_97m_dividend_2_95m_l5 (**ready**, not sent)
- Next: rq_1784 — unused Vivalto maisons / AGB / NSZ-if-200; every-10 at 1790
"""
if "tick 1783" not in text:
    p.write_text(text.rstrip()+"\n"+entry, encoding="utf-8")
    print("log appended")
else:
    print("log already present")

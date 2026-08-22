from pathlib import Path
p=Path("docs/doge/loop_log.md")
text=p.read_text(encoding="utf-8")
entry="""
### 2026-08-24T21:35:00Z — tick 1784
- Unit: rq_1784 — **AUX LILAS DE BONLEZ SA** (Bonlez / Vivalto)
- Found: Unused Vivalto maison. NBB A-cap YE2025 deposit [2026-00137101](http://cdn.staatsbladmonitor.be/2026pdf/2026-00137101.pdf) CDN 200 (236 KB / 28p); KBO **0459.968.951**; AV **12.05.2026**; mere Vivalto Home Belgium; Forvis Mazars — **opinion sans reserve**. Sourced: assets **EUR11,306,623**; equity **EUR2,413,697**; debt **EUR8,668,535**; marge bruto **EUR3,266,353**; staff **EUR2,456,066** / VTE **37.9**; PnL **EUR254,282**; controllers **EUR4,110,235**; FVA **EUR5,098,317**; cash JUMP **EUR244,941**; **RIVAGE gage EUR135,600,000**.
- Wrote: sources (+3); entities nv_lilas; budgets (+14); commitments; leaderboard; foi_queue ready; research_queue rq_1784=done + rq_1785 spawned; loop_state ticks=1784; FOI draft gap_lilas_marge_3_27m_controllers_4_11m_rivage_135m_l5.md
- FOI opened: gap_lilas_marge_3_27m_controllers_4_11m_rivage_135m_l5 (**ready**, not sent)
- Next: rq_1785 — ReposFleuri-if-vivalto / unused Vivalto / AGB / NSZ-if-200; every-10 at 1790
"""
if "tick 1784" not in text:
    p.write_text(text.rstrip()+"\n"+entry, encoding="utf-8")
    print("log appended")
else:
    print("log already present")

from pathlib import Path
p=Path("docs/doge/loop_log.md")
text=p.read_text(encoding="utf-8")
entry="""
### 2026-08-24T20:35:00Z — tick 1781
- Unit: rq_1781 — **Brembloem Immo NV** (Gent / property dual)
- Found: Preferred AGB Bornem still JR2024; NSZ CDN **403**; Brembloem VZW still no JR2025. Took leftover **Brembloem Immo NV** NBB VKT-kap YE2025 deposit [2026-00140604](http://cdn.staatsbladmonitor.be/2026pdf/2026-00140604.pdf) CDN 200 (51 KB / 14p); KBO **0644.744.944**; AV **18.05.2026**; Bultinck bestuur. Sourced: assets **EUR14,897,447**; equity **EUR4,703,547**; debt **EUR8,654,588**; MVA **EUR14,517,471**; marge bruto **EUR1,274,371** (CA undisclosed); expl **EUR756,884**; PnL **EUR434,277**; LT credit **EUR6,548,230**; mortgage mandate **EUR16,976,379**. Name-linked to Vivalto WZC Brembloem while operating VZW JR2025 still missing.
- Wrote: sources (+3); entities nv_brembloem_immo; budgets (+10); commitments; leaderboard; foi_queue ready; research_queue rq_1781=done + rq_1782 spawned; loop_state ticks=1781; FOI draft gap_brembloem_immo_marge_1_27m_debt_8_65m_mortgage_l5.md
- FOI opened: gap_brembloem_immo_marge_1_27m_debt_8_65m_mortgage_l5 (**ready**, not sent)
- Next: rq_1782 — AGB/NSZ-if-200/Bosgroep/BrembloemVZW-if-200/unused-Vivalto-maisons; every-10 at 1790
"""
if "tick 1781" not in text:
    p.write_text(text.rstrip()+"\n"+entry, encoding="utf-8")
    print("log appended")
else:
    print("log already present")

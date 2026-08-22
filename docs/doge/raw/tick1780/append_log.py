from pathlib import Path
p=Path("docs/doge/loop_log.md")
text=p.read_text(encoding="utf-8")
entry="""
### 2026-08-24T20:15:00Z — tick 1780 (every-10)
- Unit: rq_1780 — **every-10 progress coverage % + waste top10**
- Found: Re-verified pure annual top10 **stable** (GIP 8.7 · fossil direct 8.55 · accises 8.5 · company cars 8.5 · heatoil 8.43 · cheque/CO2/OAA/BCR/dual cars 8.4). Inventory: budgets **50592** · commitments **5359** · leaderboard **7558** · entities **1502** · sources **4162** · FOI ready **1402** / answered **9** / partial **27** / total **1450**. Layers A/B still **100%** of EUR347.956bn TE; C ~99%; D ~74-88% generous (not near-complete). **NEW residual 1771-1779:** Vivalto sister continuum closed (ClosRoses to AgeDor CDN batch + Meridienne/Braine/Centenaire) with undivided **RIVAGE gage EUR135.6m**; **AgeDor** NEG equity **EUR1.29m** + comfort outlier; full-CA **Tonnelle EUR6.76m** / **ClosRoses EUR5.17m**.
- Wrote: progress_every_10_ticks.md (snapshot 1780); doge_waste_top10_current.md; research_queue rq_1780=done + rq_1781 spawned; loop_state ticks=1780
- FOI opened: none (progress tick)
- Next: rq_1781 — leftover AGB/NSZ-if-200/Bosgroep/Brembloem-if-200; next every-10 **1790**
"""
if "tick 1780" not in text:
    p.write_text(text.rstrip()+"\n"+entry, encoding="utf-8")
    print("log appended")
else:
    print("log already present")

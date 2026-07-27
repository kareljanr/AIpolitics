# tick230: mandatory progress + waste top10 refresh
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T02:30:00Z,progress@230,230,no,"
    '"Scheduler 60s. Next prio5 rq_222 Mons/utilities; rq_116 SWA deferred. '
    'FOI ready human send. tick230 progress: L2~74-82 L5~9-17 culture16/16 Digipolis246m social~32m."\n',
    encoding="utf-8",
)
print("state ok")

log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = """
### 2026-07-29T02:30:00Z - tick 230 — progress coverage % + waste top10
- Unit: **progress@230** (mandatory every-10-ticks refresh; no new research unit)
- Coverage (order-of-magnitude vs EUR 347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~74-82%** (up from ~72-80% @220) — Digipolis AGB **245.6m** + member matrix **245.07m** + prior AGB stack ~631m class
  - **D L5:** **~9-17%** still thin structural — culture **16/16 complete 14.58m**; social+youth **~15 orgs ~31.8m** (CAW full 16.92m + Kras/JES/...)
  - **E FOI ready:** **~71** (total FOI rows ~75)
- Inventory: budgets ~2400 · commitments ~429 · leaderboard ~394 · entities ~309 · sources ~489
- Waste top10: taxex/FFS/cheque still dominate (cheque ~8.83 · company cars FPB ~8.5); Antwerp city L5 is core-service depth not pure-waste top
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log
- Next: prio5 **rq_222** (Mons/utilities); deferred **rq_116** SWA
"""
if "tick 230" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")
print("DONE tick230")

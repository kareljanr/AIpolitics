# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "loop_state.csv"
content = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T04:25:00Z,rq_158,163,no,"
    '"Scheduler 60s. Next prio5 rq_159 hole-fill De Lijn/Antwerp/VIPA/Mons/bpost/HR Rail; '
    'rq_116 SWA deferred. FOI ready human send. tick163 VL univ per-inst CRC."\n'
)
p.write_text(content, encoding="utf-8", newline="\n")
print("loop_state ok", p.read_bytes()[:8])

# sanity last lines
for name in ("entities.csv", "budgets.csv", "commitments.csv", "leaderboard.csv", "sources.csv"):
    lines = (Path(__file__).resolve().parents[1] / name).read_text(encoding="utf-8").splitlines()
    print(name, "n=", len(lines), "last=", lines[-1][:100])

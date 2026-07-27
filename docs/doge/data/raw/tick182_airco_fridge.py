# tick182: seed airco/fridge high-clown RQ + leaderboard (already partially written)
from pathlib import Path
from datetime import datetime, timezone

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = Path("docs/doge/data")

p = base / "loop_state.csv"
lines = p.read_text(encoding="utf-8").strip().splitlines()
notes = (
    "Seeded rq_178 prio9 + lb airco/fridge high absurdity; "
    "next research cash L5 or prio5 rq_177; FOI gap_vl_odv_mvp_cash expanded."
)
lines[1] = (
    f"main,continuous,hole_fill,{now},rq_178,182,no,\"{notes}\""
)
p.write_text("\n".join(lines) + "\n", encoding="utf-8")

log = Path("docs/doge/loop_log.md")
entry = f"""
### {now} - tick 182
- Unit: **rq_178 seed** (user flag — aircon + fridge subsidies high clown)
- Found: **NOT previously L5-mapped** (only aggregate heat-pump/MVP). Primary portals:
  - **Mijn Kortingsbon** 250 EUR means-tested fridge/washer/freezer; new apps stopped 2026-01-01; annual cash paid Unknown.
  - **MVP lucht-lucht warmtepomp** 300-600 EUR (income band); dual-use AC rules; pure cooling excluded on paper; cash split vs other WP Unknown.
- Wrote: research_queue **rq_178** prio9 open; sources 2; leaderboard **lb_vl_mijn_kortingsbon_appliances** abs 8.5 / **lb_vl_airco_mvp_luchtlucht** abs 9.0; FOI draft gap_vl_odv_mvp_cash + items 4-5 air-air + kortingsbon.
- FOI: expanded ready letter (human send); no invent euros.
- Next: execute **rq_178** cash hunt (VEKA/Fluvius/CoA) OR concurrent prio5 **rq_177**.
"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)

print("state+log updated tick 182")

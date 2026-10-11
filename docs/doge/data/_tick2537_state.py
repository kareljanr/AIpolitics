from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2537_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
notes = Path("/tmp/tick2537/rq_notes/state_notes.txt").read_text(encoding="utf-8").replace("\n", " ").strip()
state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2537,2537,no,{notes}\n",
    encoding="utf-8",
)
print("loop_state ok")
print("STATE DONE")

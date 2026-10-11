from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP, DAY = (DATA / "_tick2539_stamp.txt").read_text().strip().splitlines()
notes = Path("/tmp/tick2539/rq_notes/loop_state_notes.txt").read_text(encoding="utf-8").replace("\n", " ").strip()
if "," in notes[:20]:
    raise SystemExit("notes start bad")
import csv
from io import StringIO
buf = StringIO()
w = csv.writer(buf, lineterminator="\n")
w.writerow(["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"])
w.writerow(["main","continuous","hole_fill",STAMP,"rq_2539","2539","no",notes])
text = buf.getvalue()
if not text.endswith("\n"):
    raise SystemExit("no LF")
DATA.joinpath("loop_state.csv").write_text(text, encoding="utf-8")
print("loop_state ok", STAMP, "notes_len", len(notes))
print("STATE DONE")

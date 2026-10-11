from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOTES = Path("/tmp/tick2539/rq_notes")
STAMP, DAY = (DATA / "_tick2539_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_nloa_pelt"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2539,") != 1:
    raise SystemExit(f"bad 2539 count {rq_raw.count(b'rq_2539,')}")
if b"rq_2540," in rq_raw:
    raise SystemExit("2540 exists")
idx = rq_raw.rfind(b"rq_2539,")
if idx < 0:
    raise SystemExit("rq_2539 not found")

def rq_line(fields):
    buf = StringIO()
    csv.writer(buf, lineterminator="\n").writerow(fields)
    line = buf.getvalue()
    n = len(next(csv.reader(StringIO(line))))
    if n != 12:
        raise SystemExit(f"rq fields {n} != 12 for {fields[0]}")
    if not line.endswith("\n") or line.count("\n") != 1:
        raise SystemExit("rq line LF")
    return line.encode("utf-8")

notes_2539 = (NOTES / "notes_2539.txt").read_text(encoding="utf-8")
extra_2539 = (NOTES / "extra_2539.txt").read_text(encoding="utf-8")
notes_2540 = (NOTES / "notes_2540.txt").read_text(encoding="utf-8")
extra_2540 = (NOTES / "extra_2540.txt").read_text(encoding="utf-8")
new_2539 = rq_line(["rq_2539", "leftover dual NLOA Pelt YE2025", "hole_fill", "8", "done", "L5", EID, notes_2539, "", STAMP, STAMP, extra_2539])
new_2540 = rq_line(["rq_2540", "leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025 PLUS every-10", "hole_fill", "8", "open", "L5", "", notes_2540, "", STAMP, STAMP, extra_2540])
before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2539)
    f.write(new_2540)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2539", chk.count(b"rq_2539,"), "n2540", chk.count(b"rq_2540,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")
print("RQ TINY DONE")

from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOTES = Path("/tmp/tick2543/rq_notes")
STAMP, DAY = (DATA / "_tick2543_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_iona_nijlen"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2543,") != 1:
    raise SystemExit(f"bad 2543 count {rq_raw.count(b'rq_2543,')}")
if b"rq_2544," in rq_raw:
    raise SystemExit("2544 exists")
idx = rq_raw.rfind(b"rq_2543,")
if idx < 0:
    raise SystemExit("rq_2543 not found")

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

notes_2543 = (NOTES / "notes_2543.txt").read_text(encoding="utf-8").strip()
extra_2543 = (NOTES / "extra_2543.txt").read_text(encoding="utf-8").strip()
notes_2544 = (NOTES / "notes_2544.txt").read_text(encoding="utf-8").strip()
extra_2544 = (NOTES / "extra_2544.txt").read_text(encoding="utf-8").strip()
new_2543 = rq_line(["rq_2543", "leftover dual Iona Nijlen YE2025", "hole_fill", "8", "done", "L5", EID, notes_2543, "", STAMP, STAMP, extra_2543])
new_2544 = rq_line(["rq_2544", "leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025", "hole_fill", "8", "open", "L5", "", notes_2544, "", STAMP, STAMP, extra_2544])
before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2543)
    f.write(new_2544)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2543", chk.count(b"rq_2543,"), "n2544", chk.count(b"rq_2544,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")
print("RQ TINY DONE")

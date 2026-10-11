from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOTES = Path("/tmp/tick2537/rq_notes")
STAMP, DAY = (DATA / "_tick2537_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_leefbaar_wonen_oostkamp"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2537,") != 1:
    raise SystemExit(f"bad 2537 count {rq_raw.count(b'rq_2537,')}")
if b"rq_2538," in rq_raw:
    raise SystemExit("2538 exists")
idx = rq_raw.rfind(b"rq_2537,")
if idx < 0:
    raise SystemExit("rq_2537 not found")

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

notes_2537 = (NOTES / "notes_2537.txt").read_text(encoding="utf-8")
extra_2537 = (NOTES / "extra_2537.txt").read_text(encoding="utf-8")
notes_2538 = (NOTES / "notes_2538.txt").read_text(encoding="utf-8")
extra_2538 = (NOTES / "extra_2538.txt").read_text(encoding="utf-8")
new_2537 = rq_line(["rq_2537", "leftover dual Kringwinkel t rad Oostkamp YE2025 FOI NBB 403", "hole_fill", "8", "done", "L5", EID, notes_2537, "", STAMP, STAMP, extra_2537])
new_2538 = rq_line(["rq_2538", "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025", "hole_fill", "8", "open", "L5", "", notes_2538, "", STAMP, STAMP, extra_2538])
before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2537)
    f.write(new_2538)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2537", chk.count(b"rq_2537,"), "n2538", chk.count(b"rq_2538,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")
print("RQ TINY DONE")

from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOTES = Path("/tmp/tick2544/rq_notes")
STAMP, DAY = (DATA / "_tick2544_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_ritmica_hove"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2544,") != 1:
    raise SystemExit(f"bad 2544 count {rq_raw.count(b'rq_2544,')}")
if b"rq_2545," in rq_raw:
    raise SystemExit("2545 exists")
idx = rq_raw.rfind(b"rq_2544,")
if idx < 0:
    raise SystemExit("rq_2544 not found")

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

notes_2544 = (NOTES / "notes_2544.txt").read_text(encoding="utf-8").strip()
extra_2544 = (NOTES / "extra_2544.txt").read_text(encoding="utf-8").strip()
notes_2545 = (NOTES / "notes_2545.txt").read_text(encoding="utf-8").strip()
extra_2545 = (NOTES / "extra_2545.txt").read_text(encoding="utf-8").strip()
new_2544 = rq_line(["rq_2544", "leftover dual Ritmica Hove YE2025", "hole_fill", "8", "done", "L5", EID, notes_2544, "", STAMP, STAMP, extra_2544])
new_2545 = rq_line(["rq_2545", "leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025", "hole_fill", "8", "open", "L5", "", notes_2545, "", STAMP, STAMP, extra_2545])
before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2544)
    f.write(new_2545)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2544", chk.count(b"rq_2544,"), "n2545", chk.count(b"rq_2545,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")
print("RQ TINY DONE")

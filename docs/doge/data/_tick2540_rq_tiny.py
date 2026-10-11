from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOTES = Path("/tmp/tick2540/rq_notes")
STAMP, DAY = (DATA / "_tick2540_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_martine_van_camp_diest"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2540,") != 1:
    raise SystemExit(f"bad 2540 count {rq_raw.count(b'rq_2540,')}")
if b"rq_2541," in rq_raw:
    raise SystemExit("2541 exists")
idx = rq_raw.rfind(b"rq_2540,")
if idx < 0:
    raise SystemExit("rq_2540 not found")

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

notes_2540 = (NOTES / "notes_2540.txt").read_text(encoding="utf-8").strip()
extra_2540 = (NOTES / "extra_2540.txt").read_text(encoding="utf-8").strip()
notes_2541 = (NOTES / "notes_2541.txt").read_text(encoding="utf-8").strip()
extra_2541 = (NOTES / "extra_2541.txt").read_text(encoding="utf-8").strip()
new_2540 = rq_line(["rq_2540", "leftover dual Martine Van Camp Diest YE2025 PLUS every-10", "hole_fill", "8", "done", "L5", EID, notes_2540, "", STAMP, STAMP, extra_2540])
new_2541 = rq_line(["rq_2541", "leftover public dual unused VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025", "hole_fill", "8", "open", "L5", "", notes_2541, "", STAMP, STAMP, extra_2541])
before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2540)
    f.write(new_2541)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2540", chk.count(b"rq_2540,"), "n2541", chk.count(b"rq_2541,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")
print("RQ TINY DONE")

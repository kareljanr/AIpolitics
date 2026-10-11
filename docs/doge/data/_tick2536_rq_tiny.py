from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOTES = Path("/tmp/tick2536/rq_notes")
STAMP, DAY = (DATA / "_tick2536_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_terluchte_oostkamp"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2536,") != 1:
    raise SystemExit(f"bad 2536 count {rq_raw.count(b'rq_2536,')}")
if b"rq_2537," in rq_raw:
    raise SystemExit("2537 exists")
idx = rq_raw.rfind(b"rq_2536,")
if idx < 0:
    raise SystemExit("rq_2536 not found")

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

notes_2536 = (NOTES / "notes_2536.txt").read_text(encoding="utf-8")
extra_2536 = (NOTES / "extra_2536.txt").read_text(encoding="utf-8")
notes_2537 = (NOTES / "notes_2537.txt").read_text(encoding="utf-8")
extra_2537 = (NOTES / "extra_2537.txt").read_text(encoding="utf-8")
new_2536 = rq_line(["rq_2536", "leftover dual Ter Luchte Oostkamp YE2025", "hole_fill", "8", "done", "L5", EID, notes_2536, "", STAMP, STAMP, extra_2536])
new_2537 = rq_line(["rq_2537", "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025", "hole_fill", "8", "open", "L5", "", notes_2537, "", STAMP, STAMP, extra_2537])
before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2536)
    f.write(new_2537)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2536", chk.count(b"rq_2536,"), "n2537", chk.count(b"rq_2537,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")
print("RQ TINY DONE")

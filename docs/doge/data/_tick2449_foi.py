from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
row=Path("/tmp/tick2449_foi_row.txt").read_text(encoding="utf-8")
if not row.endswith("\n"): raise SystemExit("row no LF")
if row.count("\n")!=1: raise SystemExit("row must be one line")
path=DATA/"foi_queue.csv"
raw=path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with path.open("ab") as f:
    f.write(row.encode("utf-8"))
print("foi_queue appended", len(row))

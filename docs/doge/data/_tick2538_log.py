from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
log = ROOT / "docs/doge/loop_log.md"
entry = Path("/tmp/tick2538/loop_entry.md").read_text(encoding="utf-8")
raw = log.read_bytes()
if not raw.endswith(b"\n"):
    raise SystemExit("log no LF")
with log.open("a", encoding="utf-8") as f:
    f.write(entry if entry.startswith("\n") else "\n"+entry)
print("log appended", len(entry))
print("LOG DONE")
